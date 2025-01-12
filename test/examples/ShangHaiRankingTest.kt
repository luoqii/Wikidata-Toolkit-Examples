package examples

import examples.ranking.PATTERN
import examples.ranking.QsRanking
import org.junit.jupiter.api.Assertions.*
import org.testng.annotations.Test
import java.util.regex.Matcher
import java.util.regex.Pattern

class ShangHaiRankingTest {

    @org.junit.jupiter.api.Test
    fun parseResource() {
        kotlin.test.assertTrue(true)
    }

    @org.junit.jupiter.api.Test
    fun match() {
        var input = "#39"
        var pattern = Pattern.compile(PATTERN)
        var matcher: Matcher = pattern.matcher(input)
        assertTrue(matcher.matches())
        var number = matcher.group(1).toInt()
        assertEquals(39, number)

        input = "#=39"
        matcher = pattern.matcher(input)
        assertTrue(matcher.matches())
        number = matcher.group(1).toInt()
        assertEquals(39, number)

        input = "#1"
        matcher = pattern.matcher(input)
        assertTrue(matcher.matches())
        number = matcher.group(1).toInt()
        assertEquals(1, number)

        input = "#651-700"
        matcher = pattern.matcher(input)
        assertFalse(matcher.matches())

        input = "#701+"
        matcher = pattern.matcher(input)
        assertFalse(matcher.matches())

    }
}