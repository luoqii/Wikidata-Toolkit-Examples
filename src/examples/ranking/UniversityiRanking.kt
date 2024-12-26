package examples.ranking

import org.wikidata.wdtk.datamodel.helpers.Datamodel
import org.wikidata.wdtk.datamodel.helpers.ItemDocumentBuilder
import org.wikidata.wdtk.datamodel.helpers.ReferenceBuilder
import org.wikidata.wdtk.datamodel.helpers.StatementBuilder
import org.wikidata.wdtk.datamodel.implementation.DataObjectFactoryImpl
import org.wikidata.wdtk.datamodel.interfaces.*
import org.wikidata.wdtk.wikibaseapi.BasicApiConnection
import org.wikidata.wdtk.wikibaseapi.WikibaseDataEditor
import org.wikidata.wdtk.wikibaseapi.WikibaseDataFetcher
import java.io.FileInputStream
import java.math.BigDecimal
import java.util.*

open class UniversityiRanking {
    val DEBUG_VERBOSE = false
    val DEBUG = false
    val DRY_RUN = false

    protected var connection: BasicApiConnection? = null
    protected var wbde: WikibaseDataEditor? = null
    protected var wbdf: WikibaseDataFetcher? = null

    var actionCountMap = HashMap<Action, Int>()

    var enErrata: List<Title2Qid> = listOf()
    var zhErrata: List<Title2Qid> = listOf()

    /**
     * 僅僅驗證原始數據格式，測試用
     */
    val VALID_DATASET_ONLY = false

    /**
     * 只處理第一個數據，測試，驗證用
     */
    val PROCESS_FIRST_RECORD_ONLY = true

    fun login() {
        val p = Properties()
        p.load(FileInputStream(".local.properties"))
        val name = p.get("user.name")
        val password = p.get("user.password")
        println(name)
        println(password)

        connection =
                BasicApiConnection.getWikidataApiConnection()
        connection?.login(name.toString(), password.toString())
        println("login success")
    }

    protected fun initFetcherEditor() {
        wbdf = WikibaseDataFetcher(connection, Datamodel.SITE_WIKIDATA)
        wbde = WikibaseDataEditor(connection, Datamodel.SITE_WIKIDATA)
    }

    fun process(fetcher: WikibaseDataFetcher,
                editor: WikibaseDataEditor,
                record: UniversityRecord,
                config: Config,
                siteKey: String,
                lang: LANG){
        println("")
        System.out.println("process record:$record")
        var action = Action.NOP
        var university = fetcher.getEntityDocumentByTitle(siteKey, record.universityName)
        if (null == university) {
            println("try with errData")
            val list = if (lang == LANG.EN) {enErrata} else {zhErrata}
            list.forEach {
                if (it.title.contentEquals(record.universityName)) {
                    university = fetcher.getEntityDocument(it.qid)
                    println("found it ${it.qid}")
                    return@forEach
                }
            }
        }
        var item: ItemDocument? = null
        if (university is ItemDocument) {
            item = university as ItemDocument
            try {
                println("${item.entityId}")
                println("university name："
                        + item.labels[lang.lang]!!.text)
            } catch (e: Exception) {

            }

            var foundMatchedRanking = false
            var foundMatchedPoninttime = false
            var foundMatchedDeterminateMethod = false
            var foundMatchReference = false
            for (g in (university as ItemDocument).statementGroups) {
                if (g.property.id.equals(config.pidRanking, true)) {
                    foundMatchedRanking = false
                    foundMatchedPoninttime = false
                    foundMatchedDeterminateMethod = false
                    foundMatchReference = false

                    for (s in g.statements) {
                        val mainSnak = s.mainSnak
                        if (DEBUG_VERBOSE) {
                            println("mainSnak:$mainSnak")
                        }
                        if (mainSnak is ValueSnak) {
                            val vs = mainSnak
                            if (vs.value is QuantityValue) {
                                if ((vs.value as QuantityValue).numericValue.toLong() == record.ranking) {
                                    foundMatchedRanking = true
                                    if (DEBUG) {
                                        println("mainSnak:" + vs.propertyId.id + " value:" + vs.value)
                                    }
                                }
                            }
                        }
                        val qualifiers = s.allQualifiers
                        while (qualifiers.hasNext()) {
                            val q = qualifiers.next()
                            if (DEBUG_VERBOSE) {
                                println("qualifier:$q")
                            }
                            if (q is ValueSnak) {
                                val vq = q
                                if ((vq.propertyId.id.equals(config.pidPointTime, ignoreCase = true)
                                        && vq.value is TimeValue)
                                        && (vq.value as TimeValue).year == config.year.toLong()) {1
                                    foundMatchedPoninttime = true
                                    if (DEBUG) {
                                        println("qualifier:" + vq.propertyId.id + " value:" + (vq.value as TimeValue).year)
                                    }
                                }
                                if (vq.propertyId.id.equals(config.pidDeterminateMethod, ignoreCase = true)
                                        && vq.value is ItemIdValue
                                        && (vq.value as ItemIdValue).id.equals(config.qidDeterminateMethod, ignoreCase = true)) {
                                    foundMatchedDeterminateMethod = true
                                    if (DEBUG) {
                                        println("qualifier:" + vq.propertyId.id + " value:" + vq.value)
                                    }
                                }
                            }
                        }

                        s.references?.forEach{ ref ->
                            ref.snakGroups.forEach { group ->
                                val pid = group.property.id
                                if (config.pidReferenceUrl.equals(pid, false)) {
                                    group.snaks.forEach {
                                        if (DEBUG_VERBOSE) {
                                            System.out.println("reference snak:" + it)
                                        }
                                        if (it is ValueSnak) {
                                            if (it.propertyId.id.equals(config.pidReferenceUrl)
                                                    && (it.value as StringValue).string.equals(config.referenceUrl, false)) {
                                                foundMatchReference  = true
                                                println("reference:" + it.propertyId.id + " value:" + it.value)
                                            }
                                        }
                                    }
                                }
                            }

                        }

                        if (foundMatchedRanking && foundMatchedPoninttime && foundMatchedDeterminateMethod ) {
                            break
                        }
                    }
                }
            }
            println("foundMatchedRanking:$foundMatchedRanking " +
                    "foundMatchedPoninttime:$foundMatchedPoninttime " +
                    "foundMatchedDeterminateMethod:$foundMatchedDeterminateMethod " +
                    "foundMatchReference:$foundMatchReference"
            )
            action = if (!foundMatchedRanking || !foundMatchedPoninttime || !foundMatchedDeterminateMethod) {
                Action.ADD_STATEMENT
            } else if (foundMatchedRanking
                    && foundMatchedPoninttime
                    && foundMatchedDeterminateMethod
                    && !foundMatchReference
                    ){
                Action.UPDATE_STATEMENT_REFERENCE
            } else {
                Action.NOP
            }
        } else {
            action = Action.ADD_ITEM
        }

        println("action:$action")
        actionCountMap.set(action, actionCountMap.getOrDefault(action, 0) + 1)

        if (DRY_RUN) {
            return
        }
        when (action) {
            Action.NOP -> {}
            Action.ADD_ITEM -> {
                println("TODO ADD_ITEM")}
            Action.ADD_STATEMENT -> {
                val c = Calendar.getInstance()
                val reference = ReferenceBuilder
                        .newInstance()
                        .withPropertyValue(config.pidReferenceUrlValue,
                                Datamodel.makeStringValue(config.referenceUrl))
                        .withPropertyValue(config.pidRetrievedTimeValue,
                                Datamodel.makeTimeValue((c.get(Calendar.YEAR)).toLong(),
                                        (c.get(Calendar.MONTH) + 1).toByte(),
                                        c.get(Calendar.DAY_OF_MONTH).toByte(),
                                        TimeValue.CM_GREGORIAN_PRO)
                        )
                        .build()
                val noid = ItemIdValue.NULL
                val statement = StatementBuilder
                        .forSubjectAndProperty(item!!.entityId, config.pidRankingValue)
                        .withValue(Datamodel.makeQuantityValue(BigDecimal.valueOf(record.ranking)))
                        .withQualifierValue(config.pidPointTimeValue,
                                DataObjectFactoryImpl().getTimeValue(config.year.toLong(),
                                        0,
                                        0,
                                        0,
                                        0,
                                        0,
                                        TimeValue.PREC_YEAR,
                                        0,
                                        0,
                                        0, TimeValue.CM_GREGORIAN_PRO)
                        )
                        .withQualifierValue(config.pidDeterminateMethodValue, Datamodel.makeWikidataItemIdValue(config.qidDeterminateMethod))
                        .withReference(reference)
                        .build()
                val itemDocument = ItemDocumentBuilder.forItemId(item!!.entityId)
                        .withStatement(statement)
                        .build()
//                editor.createItemDocument(itemDocument, config.comment, config.tags)
                editor.updateStatements(item!!.entityId,
                        listOf(statement),
                        emptyList(),
                        "[[Property:P1352]]:" + record.ranking
                                + " [[Property:${config.pidPointTime}]]:${config.year}"
                                + " [[Property:${config.pidDeterminateMethod}]]:[[${config.qidDeterminateMethod}]]"
                                + " " + config.comment,
                        config.tags)
                println("create statement successfully randking:${record.ranking}  year:${config.year}, ${config.qidDeterminateMethod}")
            }
            Action.UPDATE_STATEMENT_REFERENCE -> {
                println("TODO UPDATE_STATEMENT_REFERENCE")
            }
        }

    }

    protected fun processRecords(config: Config, lang: LANG, records: List<UniversityRecord>) {
        println("prepare wikidata")
        login()
        initFetcherEditor()
        config.populate(wbdf!!)

        System.out.println("referenceUrl: ${config.referenceUrl} please CHECK !!!")

        var siteKey = "zhwiki"
        if (lang == LANG.EN) {
            siteKey = "enwiki"
        }
        actionCountMap.clear()
        if (PROCESS_FIRST_RECORD_ONLY) {
            process(wbdf!!, wbde!!, records[0], config, siteKey, lang)
        } else {
            records.forEach {
                process(wbdf!!, wbde!!, it, config, siteKey, lang)
            }
        }
        actionCountMap.forEach { t, u -> println("count for $t is $u") }
    }
}