package examples

import examples.ranking.*
import java.io.BufferedReader
import java.io.FileNotFoundException
import java.io.FileReader
import java.io.IOException
import kotlin.collections.ArrayList


class ShangHaiRanking : UniversityiRanking() {
    init {
        zhErrata = listOf(
                Title2Qid("Massachusetts Institute of Technology (MIT)", "Q49108")
        )
    }

    fun parseDataAndUpload2wikidata() {
        //arwu
//        processDataSet("2003", TYPE.ARWU, LANG.EN)
//        processDataSet("2004", TYPE.ARWU, LANG.EN)
//        processDataSet("2005", TYPE.ARWU, LANG.EN)
//        processDataSet("2006", TYPE.ARWU, LANG.EN)
//        processDataSet("2007", TYPE.ARWU, LANG.EN)
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
        processDataSet("2020", TYPE.ARWU, LANG.EN)
        processDataSet("2021", TYPE.ARWU, LANG.EN)
        processDataSet("2022", TYPE.ARWU, LANG.EN)
        processDataSet("2023", TYPE.ARWU, LANG.EN)
        processDataSet("2024", TYPE.ARWU, LANG.EN)
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

        var last: UniversityRecord? = null
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
        if (DUMP_DATASET_ONLY) {
            records.forEach {
                println("$it")
            }
            return
        }

        config.referenceUrl = "https://www.shanghairanking.cn/rankings/" +
                type.type +
                "/" + year
        config.qidDeterminateMethod = when (type) {
            TYPE.BCUR -> "Q56274575"
            TYPE.ARWU -> "Q478743"
            TYPE.BCVCR -> "Q131413842"
        }
        config.comment += " more see " +
                "[[User:Bangbang.S/shanghairanking|here]]"

        processRecords(config, lang, records)
    }

    fun parseResource(path: String): List<UniversityRecord> {
        println("parseResource path:$path")

        val records: MutableList<UniversityRecord> = ArrayList()
        try {
            FileReader(path).use { reader ->
                BufferedReader(reader).use { bReader ->
                    var line: String? = ""
                    var matchRanking = false
                    var record: UniversityRecord? = null
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
                            record = UniversityRecord()
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

    enum class TYPE(val type: String) {
        BCUR("bcur"),
        ARWU("arwu"),
        BCVCR("bcvcr"),
    }

}

private fun main() {
    println("Hello wikidata!")

    val ranking = ShangHaiRanking()
    ranking.parseDataAndUpload2wikidata()
}


