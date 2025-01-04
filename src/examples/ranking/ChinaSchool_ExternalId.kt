package examples.ranking

import com.google.common.reflect.TypeToken
import com.google.gson.Gson
import org.wikidata.wdtk.datamodel.interfaces.EntityDocument
import org.wikidata.wdtk.datamodel.interfaces.ItemDocument
import java.io.FileReader

class ChinaSchool_Id : BaseRanking() {

    fun check_external_id() {
        login()
        initFetcherEditor()
//        wbdf!!.

        val ids = getSchoolIdDatas()

        var entity: EntityDocument? = null
        val siteKey = "zhwiki"
        var notFoundCount = 0
        ids.forEachIndexed { index, schoolId ->
            try {
                entity = wbdf!!.getEntityDocumentByTitle(siteKey, schoolId.name)
                //https://www.mediawiki.org/wiki/Help:Extension:WikibaseCirrusSearch
                var search = "inlabel:" + schoolId.name
                search = schoolId.name
                var searchResult = wbdf!!.searchEntities(search, 5)
                if (null == entity && searchResult != null && searchResult.size > 0) {
                    entity = wbdf!!.getEntityDocument(searchResult.get(0).entityId)
                    if (null != entity && entity is ItemDocument) {
                        println("label: "
                                + (entity as ItemDocument).labels["zh"]!!.text)

//                        var item: ItemDocument = entity as ItemDocument
//                        item.statementGroups.filter { it ->
//                            if (it.property.id.contentEquals("")){
//                                return true
//                            } else {
//                                return false
//                            }
//
//                        }.also {  }
                    }
                }
                if (null == entity) {
                    notFoundCount++
                    println("$index can not found for $schoolId")
                } else {
                    println("$index found for $schoolId")
                }
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
        println("notFound/total:$notFoundCount/${ids.size}")
    }

    fun getSchoolIdDatas(): Array<SchoolId> {
        var type = object : TypeToken<Array<SchoolId>>() {}.type
        var jsonPath = "./hudong_moe_gov_cn/id.json"
        val wikidataJsonArray = Gson().fromJson<Array<SchoolId>>(FileReader(jsonPath), type)
        return wikidataJsonArray
    }

    fun getWikidataSchoolIdDatas(): Array<WikiDataSchool> {
        var type = object : TypeToken<Array<WikiDataSchool>>() {}.type
        var jsonPath = "./resources/china_school_id_P10472.json"
        val wikidataJsonArray = Gson().fromJson<Array<WikiDataSchool>>(FileReader(jsonPath), type)
        return wikidataJsonArray
    }

    fun check_locally() {
        var ids_from_scrapy = getSchoolIdDatas().toMutableList()
        var ids_from_wikidata_query = getWikidataSchoolIdDatas().toMutableList()

        ids_from_scrapy.removeAll {
            var match = false
            ids_from_wikidata_query.forEach { wikidata_id ->
                if (it.id.contentEquals(wikidata_id.value)) {
                    match = true
                }
            }

            match
        }

        ids_from_scrapy.forEach{
            println("新增 $it")
        }

//        ids_from_scrapy = getSchoolIdDatas().toMutableList()
//        ids_from_wikidata_query = getWikidataSchoolIdDatas().toMutableList()
//
//        ids_from_wikidata_query.removeAll {
//            var match = false
//            ids_from_scrapy.forEach { school_id ->
//                if (it.value.contentEquals(school_id.id)) {
//                    match = true
//                }
//            }
//
//            match
//        }
//
//        ids_from_wikidata_query.forEach{
//            println("wikidata 上有但教育部网站上没有 $it")
//        }

    }
}

data class SchoolId(val name: String, val id: String, val owner: String, val location: String, val level: String, val note: String)
data class WikiDataSchool(val item: String, val itemLabel: String, val value: String)

private fun main() {
    println("Hello wikidata!")

    val id = ChinaSchool_Id()
    id.check_external_id()
//    id.check_locally()

}

