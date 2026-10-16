package helper;

import java.util.regex.Pattern;

// Bitirmə layihəsi (Bank API) üçün əlavə yoxlamalar.
// README §10 qaydası ilə əlavə olunub: məntiq helper-də, @Step imp/ExtraApiAssertImp-dədir.
public class ExtraApiAssertHelper extends ApiAssertHelper {

    // 204 No Content cavabları üçün: body tam boş olmalıdır
    public void bodyIsEmpty() {
        String body = response().asString();
        if (body != null && !body.trim().isEmpty()) {
            throw new AssertionError("Cavab body-si boş olmalı idi, faktiki: " + body);
        }
    }

    // Cavabdakı regex (məs. təchizatçının subscriberPattern-i) verilən dəyəri qəbul edirmi?
    public void regexAccepts(String path, String sample, boolean shouldMatch) {
        Object pattern = value(path);
        if (pattern == null) throw new AssertionError("\"" + path + "\" cavabda tapılmadı");
        boolean matches = Pattern.compile(String.valueOf(pattern)).matcher(sample).find();
        if (matches != shouldMatch) {
            throw new AssertionError("\"" + path + "\" = " + pattern + " regex-i \"" + sample + "\" dəyərini "
                    + (shouldMatch ? "qəbul etməli idi" : "rədd etməli idi"));
        }
    }
}
