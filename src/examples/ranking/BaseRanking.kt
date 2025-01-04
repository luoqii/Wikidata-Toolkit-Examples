package examples.ranking

import org.wikidata.wdtk.datamodel.helpers.Datamodel
import org.wikidata.wdtk.wikibaseapi.BasicApiConnection
import org.wikidata.wdtk.wikibaseapi.WikibaseDataEditor
import org.wikidata.wdtk.wikibaseapi.WikibaseDataFetcher
import java.io.FileInputStream
import java.util.*

open class BaseRanking {
    protected var connection: BasicApiConnection? = null
    protected var wbde: WikibaseDataEditor? = null
    protected var wbdf: WikibaseDataFetcher? = null

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

    protected fun initFetcherEditor() {
        wbdf = WikibaseDataFetcher(connection, Datamodel.SITE_WIKIDATA)
        wbde = WikibaseDataEditor(connection, Datamodel.SITE_WIKIDATA)
    }
}