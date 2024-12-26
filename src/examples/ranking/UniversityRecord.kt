package examples.ranking

class UniversityRecord {
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