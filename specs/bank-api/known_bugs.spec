# Bank API · Məlum buglar (known-bug)

Bu spec tapılmış bugları təkrar edir. Gözlənilən nəticə sənədə/kataloqa görə yazılıb, ona görə bug düzələnə qədər FAIL olur.
Əsas run-da çıxarılır: "-Dtags=!known-bug". Ayrıca run: "-Dtags=known-bug".

tags: bank-api, known-bug

* user1 olaraq yeni sandbox-da login ol

## BUG-API-001 · Azərişıq kataloqda maxAmount 500 göstərir, amma 400 AZN ödəniş qəbul edilmir
tags: BUG-API-001, GRAD-301, GRAD-302

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/billers"
* Status kodunun "200" olmalıdır
* Json cavabında "items.find { it.id == 'azerisiq' }.maxAmount" deyeri "500" beraberdir

* "acc_002" hesabından "1000" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/BUG_API_001.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir