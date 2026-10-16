# Bitirmə layihəsi — Maleyka Alili

**API:** Bank sandbox — 211 test case, hamısı avtomat (211/211 Pass) + 1 bilinən bug testi
**Web:** iSpace.az — 126 test case, 51-i avtomat (40%); regression 40 case, 38-i avtomat (95%)
Son run (16.10.2026): Web 48 Pass + 3 bilinən bug, API 211 Pass + 1 bilinən bug.
Excel faylları: `docs/` qovluğunda.

## Run

```bash
# API
mvn test "-Dgauge.specs.dir=specs/bank-api" "-Dtags=!known-bug"

# Web
mvn test "-Dgauge.specs.dir=specs/ispace-ui" "-Dtags=!known-bug"

# Bilinən buglar (web + API) — qəsdən FAIL olur
mvn test "-Dgauge.specs.dir=specs" "-Dtags=known-bug"
```

Report: `reports/html-report/index.html`

## Bilinən buglar (known-bug)
Bu testlər düzgün nəticəni gözləyir, bug düzələnə qədər FAIL olur.

| Test | Bug |
|---|---|
| TC_FIN_POS_003 | BUG-017: taksitdə aylıq × ödəniş sayı ümumi məbləğə bərabər deyil (199 × 18 = 3 582, göstərilən 3 589 ₼) |
| TC_FIN_BVA_006 | BUG-016: 9 ₼-lıq məhsulda 1 ₼ × 18 ay = 18 ₼ göstərilir |
| TC_CART_POS_009 | BUG-032: qoruma proqramı məhsul səhifəsində 539 ₼, səbətdə 538 ₼ |
| BUG-API-001 | Azərişıq kataloqda maxAmount 500, amma 300-dən çox ödəniş 422 PER_TRANSACTION_LIMIT qaytarır |

## Qeyd
iSpace prod-dur, qiymət və stok dəyişə bilər. Testlər məhsulu və qiyməti icra zamanı seçir ("Mövcuddur" siyahısından ilk məhsul).
Sayt A/B test (pdp_v2) işlədir — testlər köhnə dizaynı cookie ilə sabitləyir.
Real sifariş və ya müraciət göndərilmir.