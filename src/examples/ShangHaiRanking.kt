package examples

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


class ShangHaiRanking {
    private var connection: BasicApiConnection? = null
    private var wbde: WikibaseDataEditor? = null
    private var wbdf: WikibaseDataFetcher? = null

    val DEBUG = false

    /**
     * 只處理第一個數據，測試，驗證用
     */
    val PROCESS_FIRST_RECORD_ONLY = false

    /**
     * 僅僅驗證原始數據格式，測試用
     */
    val VALID_DATASET_ONLY = false

    fun parseDataAndUpload2wikidata() {
        //bcur
//        processDataSet("2023")
//        processDataSet("2015", TYPE.BCUR)
//        processDataSet("2016", TYPE.BCUR)
//        processDataSet("2017", TYPE.BCUR)
//        processDataSet("2018", TYPE.BCUR)
//        processDataSet("2019", TYPE.BCUR)
//        processDataSet("2020", TYPE.BCUR)
//        processDataSet("2021", TYPE.BCUR)
//        processDataSet("2022", TYPE.BCUR)
//        processDataSet("2023", TYPE.BCUR)

        //arwu
//        processDataSet("2024", TYPE.ARWU)
    }

    private fun processDataSet(year: String, type: TYPE) {

        val config = Config()
        config.year = year
        val records = parseResource("./resources/" +
                type.type +
                "_" + config.year + "_zh.data.txt")


        var last: BcurRecord? = null
        records.forEachIndexed { index, bcurRecord ->
            if (null != last) {
//                if (last?.ranking != bcurRecord.ranking - 1) {
//                    println("last:$last curent:$bcurRecord")
//                    return
//                }
                if (last?.universityName.equals(bcurRecord.universityName)) {
                    println("last:$last current:$bcurRecord")
                    return
                }
            }
            last = bcurRecord
        }
        if (VALID_DATASET_ONLY) {
            return
        }

        config.referenceUrl = "https://www.shanghairanking.cn/rankings/" +
                type.type +
                "/" + year
        config.pidRanking = "P1352"
        config.pidDeterminateMethod = "P459"
        config.pidPointTime = "P585"
        config.qidDeterminateMethod = when (type) {
            TYPE.BCUR -> "Q56274575"
            TYPE.ARWU -> "Q478743"
        }
        config.comment = when (type) {
            TYPE.BCUR -> "增加" + config.year + "年 软科中国大学排名數據"
            TYPE.ARWU -> TODO()
        }

        config.comment += " top150  more see https://github.com/luoqii/Wikidata-Toolkit-Examples/blob/master/src/examples/ShangHaiRanking.kt"

        println("prepare wikidata")
        login()
        wbdf = WikibaseDataFetcher(connection, Datamodel.SITE_WIKIDATA)
        wbde = WikibaseDataEditor(connection, Datamodel.SITE_WIKIDATA)
        var entityDocument = wbdf?.getEntityDocument(config.pidRanking)
        config.pidValueRanking = (entityDocument as PropertyDocument).entityId
        entityDocument = wbdf?.getEntityDocument(config.pidPointTime)
        config.pidValuePointTime = (entityDocument as PropertyDocument).entityId
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

        if (PROCESS_FIRST_RECORD_ONLY) {
            process(wbdf!!, wbde!!, records[0], config)
        } else {
            records.forEach {
                process(wbdf!!, wbde!!, it, config)
            }
        }
    }

    fun process(fetcher: WikibaseDataFetcher, editor: WikibaseDataEditor, record: BcurRecord, config: Config){
        println("")
        System.out.println("process record:$record")
        var action = Action.NOP
        val university = fetcher.getEntityDocumentByTitle("zhwiki", record.universityName)
        var item: ItemDocument? = null
        if (university is ItemDocument) {
            item = university
            try {
                println("${item.entityId}")
                println("學校中文名："
                        + item.labels["zh"]!!.text)
            } catch (e: Exception) {

            }

            var foundMatchedRanking = false
            var foundMatchedPoninttime = false
            var foundMatchedDeterminateMethod = false
            var foundMatchReference = false
            for (g in university.statementGroups) {
                if (g.property.id.equals(config.pidRanking, true)) {
                    foundMatchedRanking = false
                    foundMatchedPoninttime = false
                    foundMatchedDeterminateMethod = false
                    foundMatchReference = false

                    for (s in g.statements) {
                        val mainSnak = s.mainSnak
                        if (DEBUG) {
                            println("mainSnak:$mainSnak")
                        }
                        if (mainSnak is ValueSnak) {
                            val vs = mainSnak
                            if (vs.value is QuantityValue) {
                                if ((vs.value as QuantityValue).numericValue.toLong() == record.ranking) {
                                    foundMatchedRanking = true
                                    println("mainSnak:" + vs.propertyId.id + " value:" + vs.value)
                                }
                            }
                        }
                        val qualifiers = s.allQualifiers
                        while (qualifiers.hasNext()) {
                            val q = qualifiers.next()
                            if (DEBUG) {
                                println("qualifier:$q")
                            }
                            if (q is ValueSnak) {
                                val vq = q
                                if ((vq.propertyId.id.equals(config.pidPointTime, ignoreCase = true)
                                        && vq.value is TimeValue)
                                        && (vq.value as TimeValue).year == config.year.toLong()) {1
                                    foundMatchedPoninttime = true
                                    println("qualifier:" + vq.propertyId.id + " value:" + (vq.value as TimeValue).year)
                                }
                                if (vq.propertyId.id.equals(config.pidDeterminateMethod, ignoreCase = true)
                                        && vq.value is ItemIdValue
                                        && (vq.value as ItemIdValue).id.equals(config.qidDeterminateMethod, ignoreCase = true)) {
                                    foundMatchedDeterminateMethod = true
                                    println("qualifier:" + vq.propertyId.id + " value:" + vq.value)
                                }
                            }
                        }

                        s.references?.forEach{ ref ->
                            ref.snakGroups.forEach { group ->
                                val pid = group.property.id
                                if (config.pidReferenceUrl.equals(pid, false)) {
                                    group.snaks.forEach {
                                        if (DEBUG) {
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

        when (action) {
            Action.NOP -> {}
            Action.ADD_ITEM -> {}
            Action.ADD_STATEMENT -> {
                val reference = ReferenceBuilder
                        .newInstance()
                        .withPropertyValue(config.pidValueReferenceUrl,
                                Datamodel.makeStringValue(config.referenceUrl))
                        .build()
                val noid = ItemIdValue.NULL
                val statement = StatementBuilder
                        .forSubjectAndProperty(item!!.entityId, config.pidValueRanking)
                        .withValue(Datamodel.makeQuantityValue(BigDecimal.valueOf(record.ranking)))
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
                editor.updateStatements(item!!.entityId, listOf(statement), emptyList(), config.comment, config.tags)
                println("create statement successfully")
            }
            Action.UPDATE_STATEMENT_REFERENCE -> {

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
            throw RuntimeException(e)
        } catch (e: IOException) {
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
        ARWU("arwu")
    }

}

private fun main() {
    println("Hello wikidata!")

    val ranking = ShangHaiRanking()
    ranking.parseDataAndUpload2wikidata()
}


