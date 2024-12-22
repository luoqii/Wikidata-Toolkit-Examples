package examples

import okhttp3.internal.notify
import org.wikidata.wdtk.datamodel.helpers.Datamodel
import org.wikidata.wdtk.datamodel.helpers.ItemDocumentBuilder
import org.wikidata.wdtk.datamodel.helpers.ReferenceBuilder
import org.wikidata.wdtk.datamodel.helpers.StatementBuilder
import org.wikidata.wdtk.datamodel.implementation.DataObjectFactoryImpl
import org.wikidata.wdtk.datamodel.interfaces.*
import org.wikidata.wdtk.wikibaseapi.BasicApiConnection
import org.wikidata.wdtk.wikibaseapi.WikibaseDataEditor
import org.wikidata.wdtk.wikibaseapi.WikibaseDataFetcher
import java.io.BufferedReader
import java.io.FileInputStream
import java.io.FileNotFoundException
import java.io.FileReader
import java.io.IOException
import java.math.BigDecimal
import java.util.*
import kotlin.collections.ArrayList
import kotlin.collections.HashMap
import kotlin.time.TimedValue


class ShangHaiRanking {
    private var connection: BasicApiConnection? = null
    private var wbde: WikibaseDataEditor? = null
    private var wbdf: WikibaseDataFetcher? = null

    val DEBUG_VERBOSE = false
    val DEBUG = false

    /**
     * 只處理第一個數據，測試，驗證用
     */
    val PROCESS_FIRST_RECORD_ONLY = false

    /**
     * 僅僅驗證原始數據格式，測試用
     */
    val VALID_DATASET_ONLY = false
    val DRY_RUN = false
    var actionCountMap = HashMap<Action, Int>()

    val enErrData: List<Title2Qid> = listOf(
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
    )
    val zhErrData: List<Title2Qid> = listOf(
            Title2Qid("Massachusetts Institute of Technology (MIT)", "Q49108")
    )

    fun parseDataAndUpload2wikidata() {
        //arwu
        processDataSet("2003", TYPE.ARWU, LANG.EN)
        processDataSet("2004", TYPE.ARWU, LANG.EN)
        processDataSet("2005", TYPE.ARWU, LANG.EN)
        processDataSet("2006", TYPE.ARWU, LANG.EN)
        processDataSet("2007", TYPE.ARWU, LANG.EN)
//        processDataSet("2008", TYPE.ARWU, LANG.EN)
//        processDataSet("2009", TYPE.ARWU, LANG.EN)
//        processDataSet("2010", TYPE.ARWU, LANG.EN)
//        processDataSet("2011", TYPE.ARWU, LANG.EN)
//        processDataSet("2012", TYPE.ARWU, LANG.EN)
//        processDataSet("2013", TYPE.ARWU, LANG.EN)
//        processDataSet("2014", TYPE.ARWU, LANG.EN)
//        processDataSet("2015", TYPE.ARWU, LANG.EN)
//        processDataSet("2016", TYPE.ARWU, LANG.EN)
//        processDataSet("2018", TYPE.ARWU, LANG.EN)
//        processDataSet("2018", TYPE.ARWU, LANG.EN)
//        processDataSet("2019", TYPE.ARWU, LANG.EN)
//        processDataSet("2020", TYPE.ARWU)
//        processDataSet("2021", TYPE.ARWU)
//        processDataSet("2022", TYPE.ARWU)
//        processDataSet("2023", TYPE.ARWU)
//        processDataSet("2024", TYPE.ARWU)

//        bcur
//        processDataSet("2015", TYPE.BCUR)
//        processDataSet("2016", TYPE.BCUR)
//        processDataSet("2017", TYPE.BCUR)
//        processDataSet("2018", TYPE.BCUR)
//        processDataSet("2019", TYPE.BCUR)
//        processDataSet("2020", TYPE.BCUR)
//        processDataSet("2021", TYPE.BCUR)
//        processDataSet("2022", TYPE.BCUR)
//        processDataSet("2023", TYPE.BCUR)

        //bcvcr
//            processDataSet("2023", TYPE.BCVCR)
//            processDataSet("2024", TYPE.BCVCR)
    }

    private fun processDataSet(year: String, type: TYPE, lang: LANG = LANG.ZH) {

        val config = Config()
        config.year = year
        val records = parseResource("./resources/" +
                type.type + "/" +
                type.type +
                "_" + config.year + "_" +
                lang.lang +
                ".data.txt")


        var last: BcurRecord? = null
        var accumulatedCount = 0
        records.forEachIndexed { index, bcurRecord ->
            if (null != last) {
                if (last!!.ranking == bcurRecord.ranking) {
                    accumulatedCount++
                    println("last:$last curent:$bcurRecord")
                } else if (last!!.ranking < bcurRecord.ranking){
                    if (last!!.ranking + 1 == bcurRecord.ranking) {

                    } else if ((index + 1).toLong() != bcurRecord.ranking) {
                        println("invalid data last:$last current:$bcurRecord")
                        return
                    }
                    accumulatedCount = 0
                } else {
                    println("invalid interval last:$last current:$bcurRecord")
                    return
                }

                if (last?.universityName.equals(bcurRecord.universityName)) {
                    println("invalid name last:$last current:$bcurRecord")
                    return
                }
            }
            last = bcurRecord
        }
        if (VALID_DATASET_ONLY) {
            records.forEach {
                println("$it")
            }
            return
        }

        config.referenceUrl = "https://www.shanghairanking.cn/rankings/" +
                type.type +
                "/" + year
        config.pidRanking = "P1352"
        config.pidDeterminateMethod = "P459"
        config.pidPointTime = "P585"
        config.pidRetrievedTime = "P813"
        config.qidDeterminateMethod = when (type) {
            TYPE.BCUR -> "Q56274575"
            TYPE.ARWU -> "Q478743"
            TYPE.BCVCR -> "Q131413842"
        }
//        config.comment += when (type) {
//            TYPE.BCUR -> "增加" + config.year + "年 软科中国大学排名數據"
//            TYPE.ARWU -> "增加" + config.year + "年 ShanghaiRanking's Academic Ranking of World Universities"
//            TYPE.BCVCR -> "增加" + config.year + "年 软科中国高职院校排名數據"
//        }

        config.comment += " more see " +
                "[[User:Bangbang.S/shanghairanking|here]]"

        println("prepare wikidata")
        login()
        wbdf = WikibaseDataFetcher(connection, Datamodel.SITE_WIKIDATA)
        wbde = WikibaseDataEditor(connection, Datamodel.SITE_WIKIDATA)
        var entityDocument = wbdf?.getEntityDocument(config.pidRanking)
        config.pidValueRanking = (entityDocument as PropertyDocument).entityId
        entityDocument = wbdf?.getEntityDocument(config.pidPointTime)
        config.pidValuePointTime = (entityDocument as PropertyDocument).entityId
        entityDocument = wbdf?.getEntityDocument(config.pidRetrievedTime)
        config.pidValueRetrievedTime = (entityDocument as PropertyDocument).entityId
        entityDocument = wbdf?.getEntityDocument(config.pidDeterminateMethod)
        config.pidValueDeterminateMethod = (entityDocument as PropertyDocument).entityId
        entityDocument = wbdf?.getEntityDocument(config.pidReferenceUrl)
        config.pidValueReferenceUrl = (entityDocument as PropertyDocument).entityId
        entityDocument = wbdf?.getEntityDocument(config.qidDeterminateMethod)
//        config.qidDeterminateMethodEntity = (entityDocument as ItemDocument).entityId

        System.out.println("referenceUrl: ${config.referenceUrl} please CHECK !!!")
//        try {
//            URL(config.referenceUrl).openConnection().contentLength
//        } catch (e: Exception) {
//            e.printStackTrace()
//            return
//        }

        if (!config.valid()) {
            System.err.println("config is not valid")
            return
        }

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

    fun process(fetcher: WikibaseDataFetcher,
                editor: WikibaseDataEditor,
                record: BcurRecord,
                config: Config,
                siteKey: String,
                lang: LANG){
        println("")
        System.out.println("process record:$record")
        var action = Action.NOP
        var university = fetcher.getEntityDocumentByTitle(siteKey, record.universityName)
        if (null == university) {
            println("try with errData")
            val list = if (lang == LANG.EN) {enErrData} else {zhErrData}
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
                println("學校名："
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
                val reference = ReferenceBuilder
                        .newInstance()
                        .withPropertyValue(config.pidValueReferenceUrl,
                                Datamodel.makeStringValue(config.referenceUrl))
                        .build()
                val noid = ItemIdValue.NULL
                val c = Calendar.getInstance()
                val statement = StatementBuilder
                        .forSubjectAndProperty(item!!.entityId, config.pidValueRanking)
                        .withValue(Datamodel.makeQuantityValue(BigDecimal.valueOf(record.ranking)))
                        .withQualifierValue(config.pidValueRetrievedTime,
                                Datamodel.makeTimeValue((c.get(Calendar.YEAR)).toLong(),
                                        (c.get(Calendar.MONTH) + 1).toByte(),
                                        c.get(Calendar.DAY_OF_MONTH).toByte(),
                                        TimeValue.CM_GREGORIAN_PRO)
                                )
                        .withQualifierValue(config.pidValuePointTime,
                                DataObjectFactoryImpl().getTimeValue(config.year.toLong(),
                                        0,
                                        0,
                                        0,
                                        0,
                                        0,
                                        0,
                                        0,
                                        0,
                                        0, TimeValue.CM_GREGORIAN_PRO)
                        )
                        .withQualifierValue(config.pidValueDeterminateMethod, Datamodel.makeWikidataItemIdValue(config.qidDeterminateMethod))
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

    fun parseResource(path: String): List<BcurRecord> {
        println("parseResource path:$path")

        val records: MutableList<BcurRecord> = ArrayList()
        try {
            FileReader(path).use { reader ->
                BufferedReader(reader).use { bReader ->
                    var line: String? = ""
                    var matchRanking = false
                    var record: BcurRecord? = null
                    while (line != null) {
                        if (line.startsWith("#")) {
                            line = bReader.readLine()
                            continue
                        }
                        if (line.matches("\\s*".toRegex())) {
                            line = bReader.readLine()
                            continue
                        }
                        if (!matchRanking && line.matches("\\d+".toRegex())) {
                            matchRanking = true
                            record = BcurRecord()
                            record.ranking = line.toLong()
                        }
                        if (matchRanking) {
                            record!!.universityName = bReader.readLine().trim { it <= ' ' }
                            matchRanking = false
                            records.add(record)
                        }

                        line = bReader.readLine()
                    }
                }
            }
        } catch (e: FileNotFoundException) {
            e.printStackTrace()
            throw RuntimeException(e)
        } catch (e: IOException) {
            e.printStackTrace()
            throw RuntimeException(e)
        }
//        for (r in records) {
//            println(r)
//        }
        return records
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

    class BcurRecord {
        var ranking: Long = 0
        @JvmField
        var universityName: String? = null

        override fun toString(): String {
            return "BcurRecord{" +
                    "ranking=" + ranking +
                    ", universityName='" + universityName + '\'' +
                    '}'
        }
    }

    class Config {
        val tags: MutableList<String> = mutableListOf()
        var pidRanking: String = ""
        var pidValueRanking: PropertyIdValue? = null
        var year: String = ""
        var pidDeterminateMethod: String = ""
        var pidValueDeterminateMethod: PropertyIdValue? = null
        var qidDeterminateMethod: String = ""
        var qidDeterminateMethodEntity: ItemDocument? = null
        var pidPointTime: String = ""
        var pidValuePointTime: PropertyIdValue? = null
        var pidRetrievedTime: String = ""
        var pidValueRetrievedTime: PropertyIdValue? = null
        var pidReferenceUrl: String = "P854"
        var pidValueReferenceUrl: PropertyIdValue? = null
        var referenceUrl: String = ""
        var comment: String = ""

        fun valid(): Boolean {
            return pidRanking.isNotEmpty()
                    && null != pidValueRanking
                    && year.isNotEmpty()
                        && pidDeterminateMethod.isNotEmpty() && pidValueDeterminateMethod != null
                        && pidPointTime.isNotEmpty() && pidValuePointTime != null
                        && pidReferenceUrl.isNotEmpty() && pidValueReferenceUrl != null
        }

    }

    enum class TYPE(val type: String) {
        BCUR("bcur"),
        ARWU("arwu"),
        BCVCR("bcvcr"),
    }

    enum class LANG(val lang: String) {
        ZH("zh"),
        EN("en"),
    }

    data class Title2Qid(val title: String, val qid: String)
}

private fun main() {
    println("Hello wikidata!")

    val ranking = ShangHaiRanking()
    ranking.parseDataAndUpload2wikidata()
}


