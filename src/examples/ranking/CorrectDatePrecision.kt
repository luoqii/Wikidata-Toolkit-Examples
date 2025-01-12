package examples.ranking

import com.google.common.reflect.TypeToken
import com.google.gson.Gson
import org.wikidata.wdtk.datamodel.helpers.*
import org.wikidata.wdtk.datamodel.implementation.DataObjectFactoryImpl
import org.wikidata.wdtk.datamodel.implementation.EntityIdValueImpl
import org.wikidata.wdtk.datamodel.implementation.ValueSnakImpl
import org.wikidata.wdtk.datamodel.interfaces.*
import java.io.FileReader
import java.util.*
import kotlin.system.exitProcess

class CorrectDatePrecision : BaseRanking() {
    fun corret() {
        login()
        initFetcherEditor()

        val datas = getErrorDatas()
        val config = Config()
//        processItem(datas.get(0), config)
        datas.forEachIndexed { index, it ->
            val qid = it.university.split("/").last()
            println("index:$index qid:$qid")

            processItem(it, config)
        }
    }

    private fun processItem(data: ErrorData, config: Config) {
        val qid = data.university.split("/").last()
        val entityDocument = wbdf!!.getEntityDocument(qid) as ItemDocument

        val statementGroup = entityDocument.findStatementGroup(Datamodel.makeWikidataPropertyIdValue(config.pidRanking))

        statementGroup.forEach { statement ->

            var errorPrecisionStatement: Statement? = null
            var referenceUrl = ""
            statement.references.get(0).snakGroups.get(0).snaks.forEach {snak ->
                if (config.pidReferenceUrl.contentEquals(snak.propertyId.id)) {
                    referenceUrl = ((snak as ValueSnak).value as StringValue).string
                }
            }
            var year = 0
            var ranking = (statement.value as QuantityValue).numericValue
            var determineMethod = ""

            run loop@{
                statement.qualifiers.forEach {qualifier ->
                    if (config.pidDeterminateMethod.contentEquals(qualifier.property.id)) {
                        qualifier.forEach { q ->
                            val valueSnak = q as ValueSnak
                            val v = valueSnak.value as EntityIdValueImpl
                            determineMethod = v.id
//                            println("determineMethod:$determineMethod")
                        }
                    }
                }
                statement.qualifiers.forEach { qualifier ->
                     if (config.pidPointTime.contentEquals(qualifier.property.id)) {
                        //                        println("statement:$statement qualifier:$qualifier")
                        qualifier.forEach { q ->
                            val valueSnak = q as ValueSnak
                            //                            println("valueSnak:$valueSnak")
                            val v = valueSnak.value as TimeValue
                            if (v.precision != TimeValue.PREC_YEAR) {
                                errorPrecisionStatement = statement

                                year = v.year.toInt()
                                return@loop
                            }
                        }
                    }
                }
            }

            if (null != errorPrecisionStatement) {
                println("errorPrecisionStatement:$errorPrecisionStatement")
                println("ranking:$ranking")
                println("determineMethod:$determineMethod")
                println("year:$year")
                println("referenceUrl:$referenceUrl")

                val c = Calendar.getInstance()
                val reference = ReferenceBuilder
                        .newInstance()
                        .withPropertyValue(Datamodel.makeWikidataPropertyIdValue(config.pidReferenceUrl),
                                Datamodel.makeStringValue(referenceUrl))
                        .withPropertyValue(Datamodel.makeWikidataPropertyIdValue(config.pidRetrievedTime),
                                Datamodel.makeTimeValue((c.get(Calendar.YEAR)).toLong(),
                                        (c.get(Calendar.MONTH) + 1).toByte(),
                                        c.get(Calendar.DAY_OF_MONTH).toByte(),
                                        TimeValue.CM_GREGORIAN_PRO)
                        )
                        .build()
                val statement = StatementBuilder
                        .forSubjectAndProperty(Datamodel.makeWikidataItemIdValue(qid), Datamodel.makeWikidataPropertyIdValue(config.pidRanking))
                        .withId(errorPrecisionStatement!!.statementId)
                        .withValue(Datamodel.makeQuantityValue((ranking)))
                        .withQualifierValue(Datamodel.makeWikidataPropertyIdValue(config.pidPointTime),
                                DataObjectFactoryImpl().getTimeValue(year.toLong(),
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
                        .withQualifierValue(Datamodel.makeWikidataPropertyIdValue(config.pidDeterminateMethod), Datamodel.makeWikidataItemIdValue(determineMethod))
                        .withReference(reference)
                        .build()

                val statementUpdate: StatementUpdate = StatementUpdateBuilder.create()

//                        .add(statement)
//                        .remove(errorPrecisionStatement!!.statementId)

                        .replace(statement)
                        .build()
                val update: EntityUpdate =  ItemUpdateBuilder.forEntityId(Datamodel.makeWikidataItemIdValue(qid))
                        .updateStatements(statementUpdate)
                        .build()
                val comment:String =
//                        "[[Property:P1352]]:" + ranking +
                        " [[Property:${config.pidPointTime}]]:${year} adjust date precision to year. more to see [[User:Bangbang.S/ranking/correctDatePrecision|here]]"
                wbde!!.editEntityDocument(update, false, comment, listOf())

//                exitProcess(0)
            }
        }
    }

    /*

    #Ranking(s) of university(es)
#ranking(s) of university(es)
#defaultView:LineChart
SELECT
#?year
#?universityLabel
(COUNT(?ranking) AS ?count)

#?deternimationMethodLabel
?university WHERE {
#   VALUES ?university {
#     wd:Q832355
#     wd:Q1108197
#     wd:Q16952
#     wd:Q16955
#
#     # to add another university
#     # 1,uncomment the last commented line,
#     # 2,put cursor to the end of line,
#     # 3,and press CTRL+SPACE，or CTRL+ALT+SPACE, or ALT+ENTER.
#     # 4,and select first item, and press CTRL+ENTER.
#     #wd:Zhejiang_University
#
#     }

  VALUES ?deternimationMethod {
    wd:Q478743
    wd:Q56274575
    wd:Q1790510

    # to add another deternimationMethod
    # 1,uncomment the last commented line,
    # 2,put cursor to the end of line,
    # 3,and press CTRL+SPACE，or CTRL+ALT+SPACE, or ALT+ENTER.
    # 4,and select first item, and press CTRL+ENTER.
    #wd:Shanghai_Academic_Ranking_of_World_Universities

    }


  ?university p:P1352 ?statement.
  ?statement ps:P1352 ?ranking.
  ?statement pq:P459 ?deternimationMethod.
#   ?statement pq:P585 ?date.

#   BIND (STR(YEAR(?date)) as ?year)
#   SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],mul,en". }
}

GROUP BY(?university)
     */
    fun getErrorDatas(): Array<ErrorData> {
        var type = object : TypeToken<Array<ErrorData>>() {}.type
        var jsonPath = "./resources/wrong_precision.json"
        val wikidataJsonArray = Gson().fromJson<Array<ErrorData>>(FileReader(jsonPath), type)
        return wikidataJsonArray
    }
}

data class ErrorData(val university: String)

private fun main() {
    println("Hello wikidata!")

    val id = CorrectDatePrecision()
    id.corret()

}