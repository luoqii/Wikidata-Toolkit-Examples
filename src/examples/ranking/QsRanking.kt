package examples.ranking

import com.google.common.reflect.TypeToken
import com.google.gson.Gson
import java.io.BufferedReader
import java.io.FileNotFoundException
import java.io.FileReader
import java.io.IOException
import java.util.regex.Matcher
import java.util.regex.Pattern

const val PATTERN = "[^\\d]*(\\d+)$"

class QsRanking : UniversityiRanking() {
    fun parseDataAndUpload2wikidata() {
        processDataSet("2022")
//        processDataSet("2023")
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

    fun getUniversityDatas(): Array<UniversityItem> {
        var type = object : TypeToken<Array<UniversityItem>>() {}.type
        var jsonPath = "./qschina/ranking_backup.json"
        val wikidataJsonArray = Gson().fromJson<Array<UniversityItem>>(FileReader(jsonPath), type)
        return wikidataJsonArray
    }


    var lastIndex = 0
    fun parseUniversityDatasAndUpload2wikidata() {

        val config = Config()
        // make config.valid happy, it will be update below
        config.year = "9999"
        config.qidDeterminateMethod = "Q1790510"
        config.comment += " more see " +
                "[[User:Bangbang.S/ranking/qs|here]]"

        login()
        initFetcherEditor()
        config.populate(wbdf!!)
        getUniversityDatas().forEachIndexed { index, universityItem ->
            if (index < lastIndex) {
                return@forEachIndexed
            }

            println("index:$index $universityItem")

            processUniversityItem(universityItem, config)
        }
    }

    private fun processUniversityItem(item: UniversityItem, config: Config) {
        config.referenceUrl = item.url
        val siteKey = "enwiki"
        val lang = LANG.EN
        val pattern = Pattern.compile(PATTERN)
        item?.ranking_class?.forEach {
            if ("QS World University Ranking".contentEquals(it.ranking_name)){
                it.rankings.forEach{ ranking ->
                    var matcher: Matcher = pattern.matcher(ranking.ranking)
                    if (matcher.matches()) {
                        config.year = ranking.year.toString()
                        val record = UniversityRecord()
                        record.ranking = matcher.group(1).toLong()
                        record.universityName = item.name

                        println("year:${config.year} univ:$record")
                        process(record, config, siteKey, lang)
                    }
                }
            }
        }
//
//        proces(config)
//        processRecords(config, LANG.EN, records)
    }
}



data class RankingItem(val year: Int, val ranking: String)
data class Ranking(val ranking_name: String, val rankings:List<RankingItem>)
data class UniversityItem(val name: String, val url: String, val ranking_class: List<Ranking>)

private fun main() {
    println("Hello wikidata!")

    val ranking = QsRanking()
//    ranking.parseDataAndUpload2wikidata()
    ranking.parseUniversityDatasAndUpload2wikidata()
}
