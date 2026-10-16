package imp;

import com.thoughtworks.gauge.Step;
import helper.ExtraApiAssertHelper;

// Bank API spec-ləri üçün əlavə step-lər (bax: helper/ExtraApiAssertHelper)
public class ExtraApiAssertImp extends ExtraApiAssertHelper {

    @Step("Cavab body-si boş olmalıdır")
    public void responseBodyShouldBeEmpty() {
        bodyIsEmpty();
    }

    @Step("Json cavabında <key> regex-i <value> deyerini qəbul etməlidir")
    public void regexShouldAccept(String key, String value) {
        regexAccepts(key, value, true);
    }

    @Step("Json cavabında <key> regex-i <value> deyerini qəbul etməməlidir")
    public void regexShouldReject(String key, String value) {
        regexAccepts(key, value, false);
    }
}
