package imp;

import com.thoughtworks.gauge.Step;
import helper.ExtraUiHelper;

// iSpace UI üçün əlavə addımlar (məntiq: helper/ExtraUiHelper)
public class ExtraUiImp extends ExtraUiHelper {

    // ---------- qiymət hesabları ----------

    @Step("<element> qiyməti <price> qiymətinin <times> mislinə bərabər olmalıdır")
    public void priceShouldBeMultiple(String element, String price, int times) {
        verifyPriceIsMultiple(element, price, times);
    }

    @Step("<items> qiymətlərinin cəmi <total> qiymətinə bərabər olmalıdır")
    public void sumShouldEqualTotal(String items, String total) {
        verifySumEqualsTotal(items, total);
    }

    @Step("<element> qiyməti <price> qiymətindən az olmamalıdır")
    public void priceShouldNotBeLess(String element, String price) {
        verifyPriceNotLess(element, price);
    }

    @Step("<element> qiymətləri <min> ilə <max> arasında olmalıdır")
    public void pricesShouldBeBetween(String element, String min, String max) {
        verifyPricesBetween(element, min, max);
    }

    // ---------- sıralama ----------

    @Step("<element> qiymətləri artan sırada olmalıdır")
    public void pricesShouldBeAscending(String element) {
        verifyPricesAscending(element);
    }

    @Step("<element> qiymətləri azalan sırada olmalıdır")
    public void pricesShouldBeDescending(String element) {
        verifyPricesDescending(element);
    }

    // ---------- siyahı yoxlamaları ----------

    @Step("<element> elementlerinin hamısında <text> yazısı olmalıdır")
    public void allShouldContain(String element, String text) {
        verifyAllContain(element, text);
    }

    @Step("<element> elementlerinin heç birinin metni <text> olmamalıdır")
    public void noneShouldEqual(String element, String text) {
        verifyNoneEquals(element, text);
    }

    @Step("<first> elementlerinin sayı <second> elementlerinin sayına bərabər olmalıdır")
    public void countsShouldBeEqual(String first, String second) {
        verifySameCount(first, second);
    }

    // ---------- mətn və rəqəm müqayisəsi ----------

    @Step("<element> elementinin metni <text> olmamalıdır")
    public void textShouldNotBe(String element, String text) {
        verifyTextNotEquals(element, text);
    }

    @Step("<element> elementindəki rəqəm <value> dəyərindəki rəqəmə bərabər olmalıdır")
    public void numberShouldEqual(String element, String value) {
        verifyNumberEquals(element, value);
    }

    @Step("<element> elementindəki rəqəm <first> və <second> rəqəmlərinin cəminə bərabər olmalıdır")
    public void numberShouldBeSum(String element, String first, String second) {
        verifyNumberIsSum(element, first, second);
    }

    // ---------- yadda saxlama ----------

    @Step("<element> qiymətini rəqəm kimi <variable> olaraq yadda saxla")
    public void savePriceNumber(String element, String variable) {
        savePriceAsNumber(element, variable);
    }

    @Step("<element> qiymətinə <offset> əlavə edib rəqəm kimi <variable> olaraq yadda saxla")
    public void savePriceNumberWithOffset(String element, String offset, String variable) {
        savePriceWithOffset(element, offset, variable);
    }

    @Step("Cari URL-i <variable> olaraq yadda saxla")
    public void saveUrl(String variable) {
        saveCurrentUrl(variable);
    }

    // ---------- taksit ----------

    @Step("Taksit pəncərəsində <monthly> × <count> hər tərəfdaş üçün <total> ilə bərabər olmalıdır")
    public void installmentMathShouldMatch(String monthly, String count, String total) {
        verifyInstallmentMath(monthly, count, total);
    }

    @Step("<chips> düymələrindən <text> mətnindəki müddəti seç, <monthly> aylıq məbləği həmin mətndəki kimi olmalıdır")
    public void selectTermAndCheckMonthly(String chips, String text, String monthly) {
        selectTermFromText(chips, text, monthly);
    }

    @Step("<element> görünənə qədər A/B testini köhnə dizayna qaytar")
    public void ensureClassicLayoutStep(String element) {
        ensureClassicLayout(element);
    }
}