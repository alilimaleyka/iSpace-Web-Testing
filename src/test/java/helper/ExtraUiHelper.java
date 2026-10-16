package helper;

import org.openqa.selenium.WebElement;
import utils.ScenarioContext;

import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

// iSpace UI üçün əlavə yoxlamalar: "2 699 ₼", "Movcuddur (45)", "216 Məhsul" kimi mətnləri rəqəmə çevirib hesablayır.
public class ExtraUiHelper extends BaseHelper {

    // "2 699 ₼" -> 2699 (rəqəm olmayan hər şey silinir)
    protected long parsePrice(String text) {
        String digits = text.replaceAll("[^0-9]", "");
        if (digits.isEmpty()) {
            throw new AssertionError("Qiymət mətnində rəqəm yoxdur: \"" + text + "\"");
        }
        return Long.parseLong(digits);
    }

    // "256 GB (66)" -> 66 (mötərizədəki say); mötərizə yoxdursa bütün rəqəmlər: "216 Məhsul" -> 216
    protected long parseNumber(String text) {
        Matcher m = Pattern.compile("\\((\\d+)\\)").matcher(text);
        long last = -1;
        while (m.find()) {
            last = Long.parseLong(m.group(1));
        }
        return last >= 0 ? last : parsePrice(text);
    }

    // ---------- qiymət hesabları ----------

    // element qiyməti = yadda saxlanmış qiymət × say
    public void verifyPriceIsMultiple(String elementName, String savedPrice, int times) {
        long expected = parsePrice(resolve(savedPrice)) * times;
        visible(elementName);
        assertEventually(() -> parsePrice(visible(elementName).getText()) == expected,
                () -> "\"" + elementName + "\" qiyməti " + expected + " olmalı idi, faktiki: \""
                        + visible(elementName).getText() + "\"");
    }

    // bütün sətir qiymətlərinin (və ya sayğacların) cəmi = Cəmi
    public void verifySumEqualsTotal(String itemsElement, String totalElement) {
        visible(totalElement);
        assertEventually(() -> sum(itemsElement) == parseNumber(visible(totalElement).getText()),
                () -> "\"" + itemsElement + "\" cəmi " + sum(itemsElement) + ", amma \"" + totalElement
                        + "\" = \"" + visible(totalElement).getText() + "\"");
    }

    private long sum(String elementName) {
        long total = 0;
        for (WebElement item : all(elementName)) {
            total += parseNumber(item.getText());
        }
        return total;
    }

    // element qiyməti yadda saxlanmış qiymətdən AZ olmamalıdır (səhifələr arası sıralama)
    public void verifyPriceNotLess(String elementName, String savedPrice) {
        long min = parsePrice(resolve(savedPrice));
        visible(elementName);
        assertEventually(() -> parsePrice(visible(elementName).getText()) >= min,
                () -> "\"" + elementName + "\" qiyməti " + min + "-dən az olmamalı idi, faktiki: \""
                        + visible(elementName).getText() + "\"");
    }

    // siyahıdakı bütün qiymətlər [min, max] aralığındadır
    public void verifyPricesBetween(String elementName, String minValue, String maxValue) {
        long min = parsePrice(resolve(minValue));
        long max = parsePrice(resolve(maxValue));
        visible(elementName);
        assertEventually(() -> {
                    List<Long> list = prices(elementName);
                    return !list.isEmpty() && list.stream().allMatch(p -> p >= min && p <= max);
                },
                () -> "\"" + elementName + "\" qiymətləri " + min + "–" + max + " aralığında deyil: " + prices(elementName));
    }

    // ---------- sıralama ----------

    public void verifyPricesAscending(String elementName) {
        visible(elementName);
        assertEventually(() -> isSorted(prices(elementName), true),
                () -> "\"" + elementName + "\" qiymətləri artan sırada deyil: " + prices(elementName));
    }

    public void verifyPricesDescending(String elementName) {
        visible(elementName);
        assertEventually(() -> isSorted(prices(elementName), false),
                () -> "\"" + elementName + "\" qiymətləri azalan sırada deyil: " + prices(elementName));
    }

    private List<Long> prices(String elementName) {
        List<Long> result = new ArrayList<>();
        for (WebElement item : all(elementName)) {
            result.add(parsePrice(item.getText()));
        }
        return result;
    }

    private boolean isSorted(List<Long> list, boolean ascending) {
        for (int i = 1; i < list.size(); i++) {
            if (ascending ? list.get(i) < list.get(i - 1) : list.get(i) > list.get(i - 1)) {
                return false;
            }
        }
        return list.size() > 1;
    }

    // ---------- siyahı yoxlamaları ----------

    // siyahıdakı HƏR elementin mətnində verilən yazı olmalıdır (filtr nəticələri)
    public void verifyAllContain(String elementName, String expectedText) {
        String expected = resolve(expectedText);
        visible(elementName);
        assertEventually(() -> {
                    List<String> list = texts(elementName);
                    return !list.isEmpty() && list.stream().allMatch(t -> t.contains(expected));
                },
                () -> "\"" + elementName + "\" elementlərinin hamısında \"" + expected + "\" yoxdur: " + texts(elementName));
    }

    // siyahıdakı heç bir elementin mətni verilən dəyərə bərabər olmamalıdır (siyahı boş ola bilər)
    public void verifyNoneEquals(String elementName, String notExpectedText) {
        String value = resolve(notExpectedText);
        assertEventually(() -> texts(elementName).stream().noneMatch(t -> t.equals(value)),
                () -> "\"" + elementName + "\" siyahısında \"" + value + "\" olmamalı idi: " + texts(elementName));
    }

    // iki siyahının elementlərinin sayı bərabərdir (məs. hər kartda 'Səbətə' düyməsi var)
    public void verifySameCount(String firstElement, String secondElement) {
        visible(firstElement);
        assertEventually(() -> all(firstElement).size() == all(secondElement).size(),
                () -> "\"" + firstElement + "\" sayı " + all(firstElement).size() + ", \""
                        + secondElement + "\" sayı " + all(secondElement).size());
    }

    private List<String> texts(String elementName) {
        List<String> result = new ArrayList<>();
        for (WebElement item : all(elementName)) {
            result.add(item.getText().trim());
        }
        return result;
    }

    // ---------- mətn və rəqəm müqayisəsi ----------

    // element mətni yadda saxlanmış dəyərdən FƏRQLİ olmalıdır (məs. variant dəyişəndə qiymət)
    public void verifyTextNotEquals(String elementName, String notExpected) {
        String value = resolve(notExpected);
        visible(elementName);
        assertEventually(() -> !visible(elementName).getText().trim().equals(value),
                () -> "\"" + elementName + "\" mətni dəyişmədi, hələ də \"" + value + "\"");
    }

    // elementdəki rəqəm = verilən dəyərdəki rəqəm: "45 Məhsul" = "Movcuddur (45)"
    public void verifyNumberEquals(String elementName, String value) {
        long expected = parseNumber(resolve(value));
        visible(elementName);
        assertEventually(() -> parseNumber(visible(elementName).getText()) == expected,
                () -> "\"" + elementName + "\" rəqəmi " + expected + " olmalı idi, faktiki: \""
                        + visible(elementName).getText() + "\"");
    }

    // elementdəki rəqəm = iki dəyərin cəmi: "132 Məhsul" = "256 GB (66)" + "512 GB (66)"
    public void verifyNumberIsSum(String elementName, String first, String second) {
        long expected = parseNumber(resolve(first)) + parseNumber(resolve(second));
        visible(elementName);
        assertEventually(() -> parseNumber(visible(elementName).getText()) == expected,
                () -> "\"" + elementName + "\" rəqəmi " + expected + " olmalı idi, faktiki: \""
                        + visible(elementName).getText() + "\"");
    }

    // ---------- yadda saxlama ----------

    // "3 589 ₼" -> "3589" kimi yadda saxlayır (filtr input-una yazmaq üçün)
    public void savePriceAsNumber(String elementName, String variableName) {
        savePriceWithOffset(elementName, "0", variableName);
    }

    // "3 589 ₼" + (-1000) -> "2589" (sərhəddən kənar dəyərlər üçün)
    public void savePriceWithOffset(String elementName, String offset, String variableName) {
        long value = parsePrice(visible(elementName).getText()) + Long.parseLong(resolve(offset).trim());
        ScenarioContext.put(variableName, String.valueOf(value));
        System.out.println(variableName + " = " + value);
    }

    public void saveCurrentUrl(String variableName) {
        String url = driver().getCurrentUrl();
        ScenarioContext.put(variableName, url);
        System.out.println(variableName + " = " + url);
    }

    // ---------- taksit ----------

    // hər tərəfdaş üçün aylıq × ödəniş sayı = Ümumi ödəniş məbləği
    public void verifyInstallmentMath(String monthlyElement, String countElement, String totalElement) {
        visible(totalElement);
        assertEventually(() -> installmentErrors(monthlyElement, countElement, totalElement).isEmpty(),
                () -> "Taksit hesabı uyğun gəlmir: " + installmentErrors(monthlyElement, countElement, totalElement));
    }

    private List<String> installmentErrors(String monthlyElement, String countElement, String totalElement) {
        List<WebElement> monthly = all(monthlyElement);
        List<WebElement> counts = all(countElement);
        List<WebElement> totals = all(totalElement);
        List<String> errors = new ArrayList<>();
        if (monthly.isEmpty() || monthly.size() != counts.size() || monthly.size() != totals.size()) {
            errors.add("sətir sayları fərqlidir: " + monthly.size() + "/" + counts.size() + "/" + totals.size());
            return errors;
        }
        for (int i = 0; i < monthly.size(); i++) {
            long a = parsePrice(monthly.get(i).getText());
            long n = parsePrice(counts.get(i).getText());
            long total = parsePrice(totals.get(i).getText());
            if (a * n != total) {
                errors.add((i + 1) + "-ci tərəfdaş: " + a + " × " + n + " = " + (a * n) + ", amma göstərilən " + total);
            }
        }
        return errors;
    }


    // ---------- PDP aylıq ödəniş ↔ taksit pəncərəsi ----------

    // "199 ₼/ay 18 aya" -> [199, 18]; "2 699 ₼" -> [2699]
    private List<Long> numbers(String text) {
        List<Long> result = new ArrayList<>();
        Matcher m = Pattern.compile("\\d+(?: \\d{3})*").matcher(text);
        while (m.find()) {
            result.add(Long.parseLong(m.group().replace(" ", "")));
        }
        return result;
    }

    // PDP mətnindəki müddətin düyməsini pəncərədə tapıb basır, aylıq məbləğ PDP-dəki ilə eyni olmalıdır
    public void selectTermFromText(String chipsElement, String text, String monthlyElement) {
        String pdpText = resolve(text);
        List<Long> pdp = numbers(pdpText);
        if (pdp.size() < 2) {
            throw new AssertionError("Mətndə məbləğ və müddət tapılmadı: \"" + pdpText + "\"");
        }
        long amount = pdp.get(0);
        long term = pdp.get(1);
        visible(chipsElement);
        WebElement chip = null;
        for (WebElement item : all(chipsElement)) {
            List<Long> n = numbers(item.getText());
            if (!n.isEmpty() && n.get(0) == term) {
                chip = item;
                break;
            }
        }
        if (chip == null) {
            throw new AssertionError("Pəncərədə " + term + " ay düyməsi yoxdur (PDP: \"" + pdpText + "\")");
        }
        scrollIntoView(chip);
        chip.click();
        assertEventually(() -> parsePrice(visible(monthlyElement).getText()) == amount,
                () -> term + " ay üçün aylıq məbləğ " + amount + " olmalı idi (PDP: \"" + pdpText + "\"), faktiki: \""
                        + visible(monthlyElement).getText() + "\"");
    }

    // ---------- A/B test (GrowthBook pdp_v2) ----------

    private static final String GB_ANON_ID = "76c7905b-f815-4db7-bb6d-2d6d44541e0a";

    // Sayt bəzən PDP-ni yeni dizaynda (pdp_v2) açır və locator-lar tapılmır.
    // Element görünmürsə: gb cookie-lərini yenidən qoyur, səhifəni yeniləyir (maks. 3 dəfə).
    public void ensureClassicLayout(String elementName) {
        for (int attempt = 1; attempt <= 3; attempt++) {
            try {
                visible(elementName, 8);
                return;
            } catch (RuntimeException | AssertionError e) {
                System.out.println("PDP köhnə dizaynda açılmadı (cəhd " + attempt + "), A/B cookie yenidən qoyulur");
                driver().manage().deleteCookieNamed("gb-anon-id");
                driver().manage().deleteCookieNamed("gb-exp");
                driver().manage().addCookie(new org.openqa.selenium.Cookie("gb-anon-id", GB_ANON_ID));
                driver().manage().addCookie(new org.openqa.selenium.Cookie("gb-exp", "pdp_v2:0"));
                driver().navigate().refresh();
            }
        }
        visible(elementName, 15);
    }
}