package examples

import examples.ranking.*
import java.io.BufferedReader
import java.io.FileNotFoundException
import java.io.FileReader
import java.io.IOException
import kotlin.collections.ArrayList
import kotlin.collections.HashMap


class ShangHaiRanking : UniversityiRanking() {


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
        if (VALID_DATASET_ONLY) {
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


