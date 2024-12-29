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

    /**
     * 僅僅驗證原始數據格式，測試用
     */
    val DUMP_DATASET_ONLY = false

    /**
     * 只處理第一個數據，測試，驗證用
     */
    val PROCESS_FIRST_RECORD_ONLY = false


    protected var connection: BasicApiConnection? = null
    protected var wbde: WikibaseDataEditor? = null
    protected var wbdf: WikibaseDataFetcher? = null

    var actionCountMap = HashMap<Action, Int>()

    var enErrata: List<Title2Qid> = listOf()
    var zhErrata: List<Title2Qid> = listOf()

    init {
        enErrata = listOf(
                Title2Qid("Massachusetts Institute of Technology (MIT)", "Q49108"),
                Title2Qid("Swiss Federal Institute of Technology Zurich", "Q11942"),
                Title2Qid("University of Michigan-Ann Arbor", "Q230492"),
                Title2Qid("The University of Tokyo", "Q7842"),
                Title2Qid("University of Wisconsin - Madison", "Q838330"),
                Title2Qid("The University of Edinburgh", "Q160302"),
                Title2Qid("The University of Manchester", "Q230899"),
                Title2Qid("University of Paris-Sud (Paris 11)", "Q1480643"),
                Title2Qid("University of Colorado at Boulder", "Q736674"),
                Title2Qid("University of Illinois at Urbana-Champaign", "Q457281"),
                Title2Qid("The University of Melbourne", "Q319078"),
                Title2Qid("University of Minnesota, Twin Cities", "Q238101"),
                Title2Qid("The University of Texas at Austin", "Q49213"),
                Title2Qid("The University of Texas Southwestern Medical Center at Dallas", "Q2725999"),
                Title2Qid("University of Munich", "Q55044"),
                Title2Qid("The University of Queensland", "Q866012"),
                Title2Qid("Technical University Munich", "Q157808"),
                Title2Qid("The University of Texas M. D. Anderson Cancer Center", "Q1525831"),
                Title2Qid("Purdue University - West Lafayette", "Q217741"),
                Title2Qid("The Australian National University", "Q127990"),
                Title2Qid("Swiss Federal Institute of Technology Lausanne", "Q262760"),
                Title2Qid("Ecole Normale Superieure - Paris", "Q273604"),
                Title2Qid("Technion-Israel Institute of Technology", "Q333705"),
                Title2Qid("University of Pittsburgh, Pittsburgh Campus", "Q235034"),
                Title2Qid("The University of New South Wales", "Q734764"),
                Title2Qid("Pennsylvania State University - University Park", "Q7163241"),
                Title2Qid("The University of Western Australia", "Q1517021"),
                Title2Qid("The Ohio State University - Columbus", "Q309331"),
                Title2Qid("Georgia Institute of Technology", "Q864855"),
                Title2Qid("Mayo Medical School", "Q6797536"),
                Title2Qid("The Hebrew University of Jerusalem", "Q174158"),
                Title2Qid("University of Goettingen", "Q152838"),
                Title2Qid("Pierre and Marie  Curie University - Paris 6", "Q1144549"),
                Title2Qid("Pierre and Marie Curie University - Paris 6", "Q1144549"),
                Title2Qid("Rutgers, The State University of New Jersey - New Brunswick", "Q499451"),
                Title2Qid("The Imperial College of Science, Technology and Medicine", "Q189022"),
                Title2Qid("VU University Amsterdam", "Q1065414"),
                Title2Qid("The Johns Hopkins University", "Q193727"),
                Title2Qid("University of Michigan - Ann Arbor", "Q230492"),
                Title2Qid("University of Paris Sud (Paris 11)", "Q1480643"),
                Title2Qid("University of Heidelberg", "Q151510"),
                Title2Qid("Arizona State University - Tempe", "Q670897"),
                Title2Qid("The Imperial College of Science", "Q189022"),
                Title2Qid("Rutgers", "Q499451"),
                Title2Qid("Texas A&M University - College Station", "Q49212"),
                Title2Qid("The University of Sheffield", "Q823917"),
                Title2Qid("University of Roma - La Sapienza", "Q209344"),
                Title2Qid("University of Illinois at Chicago", "Q955764"),
                Title2Qid("North Carolina State University - Raleigh", "Q1132346"),
                Title2Qid("PSL University", "Q1163431"),
                Title2Qid("Université Grenoble Alpes", "Q945876"),
                Title2Qid("Université Paris Cité", "Q55849612"),
                Title2Qid("The University of Hong Kong", "Q15568"),
        )
    }

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

    fun process(record: UniversityRecord,
                config: Config,
                siteKey: String,
                lang: LANG){
        val fetcher = wbdf!!
        val editor = wbde!!
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
                    for (s in g.statements) {
                        foundMatchedRanking = false
                        foundMatchedPoninttime = false
                        foundMatchedDeterminateMethod = false
                        foundMatchReference = false

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
            process(records[0], config, siteKey, lang)
        } else {
            records.forEach {
                process(it, config, siteKey, lang)
            }
        }
        actionCountMap.forEach { t, u -> println("count for $t is $u") }
    }
}