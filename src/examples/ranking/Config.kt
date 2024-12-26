package examples.ranking

import org.wikidata.wdtk.datamodel.interfaces.ItemDocument
import org.wikidata.wdtk.datamodel.interfaces.PropertyDocument
import org.wikidata.wdtk.datamodel.interfaces.PropertyIdValue
import org.wikidata.wdtk.wikibaseapi.WikibaseDataFetcher

class Config {
    var pidRanking: String = "P1352"
    var pidRankingValue: PropertyIdValue? = null
    var year: String = ""
    var pidDeterminateMethod: String = "P459"
    var pidDeterminateMethodValue: PropertyIdValue? = null
    var qidDeterminateMethod: String = ""
    var qidDeterminateMethodEntity: ItemDocument? = null
    var pidPointTime: String = "P585"
    var pidPointTimeValue: PropertyIdValue? = null
    var pidRetrievedTime: String = "P813"
    var pidRetrievedTimeValue: PropertyIdValue? = null

    var pidReferenceUrl: String = "P854"
    var pidReferenceUrlValue: PropertyIdValue? = null
    var referenceUrl: String = ""

    var comment: String = ""
    val tags: MutableList<String> = mutableListOf()

    fun populate(wbdf: WikibaseDataFetcher) {
        var entityDocument = wbdf.getEntityDocument(pidRanking)
        pidRankingValue = (entityDocument as PropertyDocument).entityId
        entityDocument = wbdf.getEntityDocument(pidPointTime)
        pidPointTimeValue = (entityDocument as PropertyDocument).entityId
        entityDocument = wbdf.getEntityDocument(pidRetrievedTime)
        pidRetrievedTimeValue = (entityDocument as PropertyDocument).entityId
        entityDocument = wbdf.getEntityDocument(pidDeterminateMethod)
        pidDeterminateMethodValue = (entityDocument as PropertyDocument).entityId
        entityDocument = wbdf.getEntityDocument(pidReferenceUrl)
        pidReferenceUrlValue = (entityDocument as PropertyDocument).entityId
        entityDocument = wbdf.getEntityDocument(qidDeterminateMethod)
        //        qidDeterminateMethodEntity = (entityDocument as ItemDocument).entityId

        if (!valid()) {
            throw IllegalStateException("config is not valid")
        }
    }

    fun valid(): Boolean {
        return pidRanking.isNotEmpty()
                && null != pidRankingValue
                && year.isNotEmpty()
                    && pidDeterminateMethod.isNotEmpty() && pidDeterminateMethodValue != null
                    && pidPointTime.isNotEmpty() && pidPointTimeValue != null
                    && pidReferenceUrl.isNotEmpty() && pidReferenceUrlValue != null
    }

}