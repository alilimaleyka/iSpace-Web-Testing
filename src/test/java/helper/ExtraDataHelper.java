package helper;

import utils.ScenarioContext;

import java.time.LocalDate;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;

// Tarixdən asılı gözlənilən dəyərlər (qəbz nömrəsi, kartın expiry-si, tarix filtrləri).
// Bank API-də "bu gün" Bakı vaxtı ilə hesablanır.
public class ExtraDataHelper {

    private static final ZoneId BAKU = ZoneId.of("Asia/Baku");

    public void saveDate(long days, long years, String pattern, String variableName) {
        LocalDate date = LocalDate.now(BAKU).plusDays(days).plusYears(years);
        String value = date.format(DateTimeFormatter.ofPattern(pattern));
        ScenarioContext.put(variableName, value);
        System.out.println(variableName + " = " + value);
    }
}
