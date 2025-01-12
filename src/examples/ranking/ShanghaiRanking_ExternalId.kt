package examples.ranking

import com.google.common.reflect.TypeToken
import com.google.gson.Gson
import org.wikidata.wdtk.datamodel.helpers.Datamodel
import org.wikidata.wdtk.datamodel.helpers.StatementBuilder
import org.wikidata.wdtk.datamodel.interfaces.EntityDocument
import org.wikidata.wdtk.datamodel.interfaces.ItemDocument
import org.wikidata.wdtk.datamodel.interfaces.ItemIdValue
import org.wikidata.wdtk.datamodel.interfaces.StringValue
import java.io.FileReader
import java.io.IOException

private const val comment = "more see [[User:Bangbang.S/ranking/shanghairanking_external_id|here]]"

class ShanghaiRanking_external_id : BaseRanking() {
    val externalPid = "P5242"


    val excludeNames = mutableListOf<String>(
            "Shenyang City University",
            "University of Colorado Health Science Center",
            "Wuhan Huaxia University of Technology",
    )
    var lastIndex = 2660

    fun getShanghaiDatas(): List<UniversityInfo> {
        var type = object : TypeToken<Array<UniversityInfo>>() {}.type
        var jsonPath = "./shanghairangk_external_id/external_id.json"
        val shanghaiJsonArray = Gson().fromJson<Array<UniversityInfo>>(FileReader(jsonPath), type)
        return shanghaiJsonArray.toList()
    }

    fun getShanghaiCnDatas(): List<UniversityInfo> {
        var type = object : TypeToken<Array<UniversityCnInfo>>() {}.type
        var jsonPath = "./shanghai_institution/id.json"
        val shanghaiJsonArray = Gson().fromJson<Array<UniversityCnInfo>>(FileReader(jsonPath), type)

        val list = mutableListOf<UniversityInfo>()
        shanghaiJsonArray.forEach {
            list.add(UniversityInfo(it.name_cn, it.location, it.url))
        }

        return list
    }

    fun getWikiDatas(): List<WikiItem> {
        var type = object : TypeToken<Array<WikiItem>>() {}.type
        var jsonPath = "./resources/P5242.json"
        val wikidataJsonArray = Gson().fromJson<Array<WikiItem>>(FileReader(jsonPath), type)
        return wikidataJsonArray.toList()
    }

    fun check_external_id() {
        login()
        initFetcherEditor()

        var shanghaiJsonArray = getShanghaiDatas()

        var siteKey = "enwiki"
        var notFoundCount = 0

        shanghaiJsonArray = getShanghaiCnDatas()
        siteKey = "zhwiki"

        shanghaiJsonArray.forEachIndexed { index, universityInfo ->
            if (index < lastIndex) {
                return@forEachIndexed
            }

            println()
            println("index:$index $universityInfo")

            process(siteKey, universityInfo, notFoundCount)

            if (index % 50 == 0) {
                println("notFound/total:$notFoundCount/${index + 1}")
            }
        }
        println("notFound/total:$notFoundCount/${shanghaiJsonArray.size}")
    }

    private fun process(siteKey: String, universityInfo: UniversityInfo, notFoundCount: Int) {
        var entity: EntityDocument? = null
        var notFoundCount1 = notFoundCount
        notFoundCount1++
        if (universityInfo.url.isEmpty()) {
            return
        }

        if (excludeNames.contains(universityInfo.name)) {
            println("exclude ")
            return
        }

        try {
            entity = wbdf!!.getEntityDocumentByTitle(siteKey, universityInfo.name)
            //https://www.mediawiki.org/wiki/Help:Extension:WikibaseCirrusSearch
            var search = "inlabel:" + universityInfo.name
            search = universityInfo.name
            var searchResult = wbdf!!.searchEntities(search, 5)
            if (null == entity && searchResult != null && searchResult.size > 0) {
                println("getEntityDocumentByTitle return null search it")

                run  loop@{
                    searchResult.forEach {
                        val search = wbdf!!.getEntityDocument(it.entityId)
                        if (isEducationItem(search)) {
//                        println("label $search.")
                            entity = search

                            return@loop
                        }
                    }
                }
            }
            if (null == entity || !(entity is ItemDocument)) {
                println("can not found for $universityInfo")

//                exit(0)
            } else {
                println("found ")
                var action = Action.NOP
                var idFromShangHaiRanking: String? = null
                var doc = entity as ItemDocument
                val url = universityInfo.url
                idFromShangHaiRanking = url.split("/").last()

                var externalStatement = doc.findStatement(externalPid)
                if (externalStatement == null) {
                    println("add statement")
                    action = Action.ADD_STATEMENT
                } else {
                    var id = externalStatement.value
                    if (id is StringValue) {
                        var stringId = id as StringValue
                        //=======1234567890123456789012
                        println("stringId             :${stringId.string}")

                        if (url.length > 0 && stringId.string.isNotEmpty()) {
                            //=======1234567890123456789012
                            println("idFromShangHaiRanking:${idFromShangHaiRanking}")
                            if (stringId.string!!.contentEquals(idFromShangHaiRanking, true)) {
                                println("id equal ignore")
                            } else {
                                println("update id")
                                action = Action.UPDATE_STATEMENT
                            }
                        } else {
                            println("ignore")
                        }
                    }
                }

                println("action:${action}")
                println("item:${doc.entityId}")
                when (action) {
                    Action.NOP -> {

                    }

                    Action.ADD_ITEM -> TODO()
                    Action.ADD_STATEMENT -> {
                        val statement = StatementBuilder.forSubjectAndProperty(doc.entityId, Datamodel.makeWikidataPropertyIdValue("P5242"))
                                .withValue(Datamodel.makeStringValue(idFromShangHaiRanking))
                                .build()

                        wbde!!.updateStatements(doc.entityId,
                                listOf(statement),
                                emptyList(),
                                "[[Property:P5242]]:" + idFromShangHaiRanking
                                        + ". add id, $comment",
                                mutableListOf())
                    }
                    Action.UPDATE_STATEMENT -> {
                        val statement = StatementBuilder.forSubjectAndProperty(doc.entityId, Datamodel.makeWikidataPropertyIdValue("P5242"))
                                .withValue(Datamodel.makeStringValue(idFromShangHaiRanking))
                                .build()

                        wbde!!.updateStatements(doc.entityId,
                                listOf(statement),
                                listOf(externalStatement),
                                "[[Property:P5242]]:" + idFromShangHaiRanking
                                        + ". change id, $comment",
                                mutableListOf())

//                        exit(0)
                    }
                    Action.UPDATE_STATEMENT_REFERENCE -> TODO()
                }
            }
        } catch (e: Exception) {
            e.printStackTrace()
            if (e is IOException) {
                throw e;
            }
        }
    }

    fun check_locally() {
        val shanghaiJsonArray = getShanghaiDatas()
        val wikidataJsonArray = getWikiDatas()
    }



    companion object {
        val PROPERTY_ID_INSTANC_OF = "P31"
        val educationIds = mutableListOf<String>(
                "Q2385804", //教育机构
                "Q875538",//公立大学
                "Q38723",//高等教育机构
                "Q3918",//大学
                "Q62078547",//公立研究型大学
                "Q23002039",//美国公立教育机构
                "Q3551775",//法国的大学
                "Q902104",//私立大学
                "Q322563",//专科学校
        )
        fun isEducationItem(entity: EntityDocument): Boolean {
            if (null != entity && entity is ItemDocument) {
                println("id ${entity.entityId.id}")
                try {
                    println("label: "
                            + (entity as ItemDocument).labels["en"]!!.text)
                } catch (e: Exception) {

                }
                try {
                    println("label: "
                            + (entity as ItemDocument).labels["zh"]!!.text)
                } catch (e: Exception) {

                }

                var item: ItemDocument = entity as ItemDocument
                val group = item.statementGroups.filter { group ->
                    group.property?.id.let {
                        PROPERTY_ID_INSTANC_OF.contentEquals(it)
                    } ?: true

                }

                if (group.isEmpty()) {
                    return false
                }

                val statement = group[0].statements.firstOrNull {
                    val v = it.value
                    var match = false
                    if (v is ItemIdValue) {
                        val idValue = v as ItemIdValue
                        if (educationIds.contains(idValue.id)) {
                            match = true
                        }
                    }

                    match
                }

                return statement != null
            }

            return false
        }
    }
}

data class UniversityCnInfo(val name_cn: String, val location: String, var url: String)
data class UniversityInfo(val name: String, val country: String, var url: String)
data class WikiItem(val itemLabel: String, val value: String)

private fun main() {
    println("Hello wikidata!")

    val ranking = ShanghaiRanking_external_id()
    ranking.check_external_id()
//    ranking.check_locally()

}