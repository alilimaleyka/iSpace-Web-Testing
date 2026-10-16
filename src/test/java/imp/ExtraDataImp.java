package imp;

import com.thoughtworks.gauge.Step;
import helper.ExtraDataHelper;

// Tarix dəyişənləri (bax: helper/ExtraDataHelper). Nümunə: "yyyy-MM-dd", "yyyyMMdd", "MM/yy"
public class ExtraDataImp extends ExtraDataHelper {

    @Step("Bu gündən <days> gün sonranın tarixini <pattern> formatında <variable> olaraq yadda saxla")
    public void saveDateAfterDays(String days, String pattern, String variable) {
        saveDate(Long.parseLong(days.trim()), 0, pattern, variable);
    }

    @Step("Bu gündən <years> il sonranın tarixini <pattern> formatında <variable> olaraq yadda saxla")
    public void saveDateAfterYears(String years, String pattern, String variable) {
        saveDate(0, Long.parseLong(years.trim()), pattern, variable);
    }
}
