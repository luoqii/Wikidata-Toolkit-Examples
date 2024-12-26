package examples.ranking

import examples.ShangHaiRanking
import java.io.BufferedReader
import java.io.FileNotFoundException
import java.io.FileReader
import java.io.IOException

class QsRanking : UniversityiRanking() {
    fun parseDataAndUpload2wikidata() {
        processDataSet("2024")
    }

    private fun processDataSet(year: String) {
        val config = Config()
        config.year = year
        val records = parseResource("./resources/qs/" +
                "qschina.cn_en_" + "" +
                config.year +
                ".data.txt")

        if (DUMP_DATASET_ONLY) {
            records.forEach {
                println("$it")
            }
            return
        }

        config.referenceUrl = "https://www.qschina.cn/en/university-rankings/world-university-rankings/" +
                config.year
        config.qidDeterminateMethod = "Q1790510"
        config.comment += " more see " +
                "[[User:Bangbang.S/ranking/qs|here]]"

        processRecords(config, LANG.EN, records)
    }

    private fun parseResource(path: String): List<UniversityRecord> {
        println("parseResource path:$path")

        val records: MutableList<UniversityRecord> = ArrayList()
        try {
            FileReader(path).use { reader ->
                BufferedReader(reader).use { bReader ->
                    var line: String? = ""

                    var rankingStr: String
                    var name: String
                    var score: Int
                    val contents: MutableList<String> = mutableListOf()

                    var record: UniversityRecord? = null
//                    line = bReader.readLine()
                    while (line != null) {
                        if (line.startsWith("#")) {
                            line = bReader.readLine()
                            continue
                        }
                        if (line.matches("\\s*".toRegex())) {
                            line = bReader.readLine()
                            continue
                        }
                        if (line.isNotEmpty()) {
                            contents.add(line)
                        }
                        if (contents.size == 2) {
                            rankingStr = contents[0]
                            name = contents[1]
                            if (rankingStr.startsWith("=")) {
                                rankingStr = rankingStr.substring(1)
                            } else if (rankingStr.contains("-")) {
                                break
                            }
                            val record = UniversityRecord()
                            record.ranking = rankingStr.toLong()
                            record.universityName = name

                            records.add(record)
                            contents.clear()
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
//        } catch (e: Exception) {
//            e.printStackTrace()
//            throw RuntimeException(e)
        }
        return records
    }

}

private fun main() {
    println("Hello wikidata!")

    val ranking = QsRanking()
    ranking.parseDataAndUpload2wikidata()
}