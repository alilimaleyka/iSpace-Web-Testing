# GRAD-302 · POST /bill-payments — Kommunal ödəniş etmək

EPIC-3 · Kommunal ödənişlər.
Mənbə: Bank_API_QA_Project.xlsx → API Test Cases. Ssenari adı = test case ID-si + başlığı.
Spec-in əvvəlindəki context step hər ssenaridən əvvəl user1 ilə yeni, boş sandbox açır — ssenarilər bir-birindən asılı deyil.

tags: bank-api, epic-3, GRAD-302

* user1 olaraq yeni sandbox-da login ol

## TC_PAY_POS_010 · Etibarlı ödənişdə 201: status SUCCESS, fee 0.50, total = amount + fee, balanceAfter = balans − total, Location header
tags: SC-023, P1, pos, smoke

* "acc_002" hesabından "100" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_POS_010.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "amount" deyeri "50" beraberdir
* Json cavabında "fee" deyeri "0.5" beraberdir
* Json cavabında "total" deyeri "50.5" beraberdir
* Json cavabında "balanceAfter" deyeri "49.5" beraberdir
* Json cavabında "id" deyeri "^bpm_[A-Za-z0-9]{8}$" regex-ine uyğun olmalıdır
* Json cavabında "id" deyerini "yeniId" olaraq yadda saxla
* Header "Location" deyerinde "/bill-payments/${yeniId}" olmalıdır
* Json cavabını cedvel ile yoxla

   |path|value|
   |----|-----|
   |biller.id|citynet|
   |biller.name|CityNet|
   |biller.category|INTERNET|

* Json cavabında "subscriberNo" deyeri "CN123456" beraberdir
* Json cavabında "currency" deyeri "AZN" beraberdir
* Json cavabında "cardId" deyeri "${cardId}" beraberdir
* Json cavabında "createdAt" deyeri "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}([.][0-9]{3})?Z$" regex-ine uyğun olmalıdır

## TC_PAY_POS_011 · Ödənişdən sonra GET /cards/{id}-də availableBalance və spentToday total (50.50) qədər dəyişir — amount (50) qədər yox
tags: SC-023, P1, pos

* "acc_002" hesabından "100" məbləğində kart burax
* "citynet" təchizatçısına "CN123456" nömrəsi üçün "50" AZN ödəniş et

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/cards/${cardId}"
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyeri "49.5" beraberdir
* Json cavabında "spentToday" deyeri "50.5" beraberdir

## TC_PAY_POS_012 · Sandbox-da ilk ödənişin qəbzi RCP-YYYYMMDD-000001, növbəti ödənişinki RCP-YYYYMMDD-000002 olur
tags: SC-023, P2, pos

Qeyd: gözlənilən nəticə Q-31 fərziyyəsinə əsaslanır (Grooming Questions).

* Bu gündən "0" gün sonranın tarixini "yyyyMMdd" formatında "bugun" olaraq yadda saxla
* "acc_002" hesabından "100" məbləğində kart burax
* "azersu" təchizatçısına "12345678" nömrəsi üçün "1" AZN ödəniş et
* Json cavabında "receiptNo" deyeri "RCP-${bugun}-000001" beraberdir

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_POS_012.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "receiptNo" deyeri "RCP-${bugun}-000002" beraberdir

## TC_PAY_BVA_013 · CityNet komissiyası 1%, min 0.20: 5 → 0.20, 20 → 0.20, 21 → 0.21, 150 → 1.50
tags: SC-023, P1, bva

* "acc_002" hesabından "1000" məbləğində kart burax

Sorğu 1 — 5 AZN:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_BVA_013_1.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "amount" deyeri "5" beraberdir
* Json cavabında "fee" deyeri "0.2" beraberdir
* Json cavabında "total" deyeri "5.2" beraberdir
* Json cavabında "balanceAfter" deyeri "994.8" beraberdir

Sorğu 2 — 20 AZN:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_BVA_013_2.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "amount" deyeri "20" beraberdir
* Json cavabında "fee" deyeri "0.2" beraberdir
* Json cavabında "total" deyeri "20.2" beraberdir
* Json cavabında "balanceAfter" deyeri "974.6" beraberdir

Sorğu 3 — 21 AZN:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_BVA_013_3.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "amount" deyeri "21" beraberdir
* Json cavabında "fee" deyeri "0.21" beraberdir
* Json cavabında "total" deyeri "21.21" beraberdir
* Json cavabında "balanceAfter" deyeri "953.39" beraberdir

Sorğu 4 — 150 AZN:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_BVA_013_4.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "amount" deyeri "150" beraberdir
* Json cavabında "fee" deyeri "1.5" beraberdir
* Json cavabında "total" deyeri "151.5" beraberdir
* Json cavabında "balanceAfter" deyeri "801.89" beraberdir

## TC_PAY_EDGE_014 · CityNet 20.50 AZN üçün komissiya 0.205 yuxarı yuvarlaqlaşdırılaraq 0.21 olur
tags: SC-023, P3, edge

Qeyd: gözlənilən nəticə Q-30 fərziyyəsinə əsaslanır (Grooming Questions).

* "acc_002" hesabından "100" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_EDGE_014.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "amount" deyeri "20.5" beraberdir
* Json cavabında "fee" deyeri "0.21" beraberdir
* Json cavabında "total" deyeri "20.71" beraberdir
* Json cavabında "balanceAfter" deyeri "79.29" beraberdir

## TC_PAY_POS_015 · Aztelekom komissiyası məbləğdən asılı olmayaraq 0.50 sabitdir (2 AZN və 100 AZN)
tags: SC-023, P2, pos

* "acc_002" hesabından "200" məbləğində kart burax

Sorğu 1 — 2 AZN:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_POS_015_1.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "amount" deyeri "2" beraberdir
* Json cavabında "fee" deyeri "0.5" beraberdir
* Json cavabında "total" deyeri "2.5" beraberdir
* Json cavabında "balanceAfter" deyeri "197.5" beraberdir

Sorğu 2 — 100 AZN:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_POS_015_2.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "amount" deyeri "100" beraberdir
* Json cavabında "fee" deyeri "0.5" beraberdir
* Json cavabında "total" deyeri "100.5" beraberdir
* Json cavabında "balanceAfter" deyeri "97" beraberdir

## TC_PAY_POS_016 · Komissiyası olmayan təchizatçılarda (Azərişıq, Azərsu, Azercell, Bakcell) fee 0 və total = amount olur
tags: SC-023, P2, pos

* "acc_002" hesabından "100" məbləğində kart burax

Sorğu 1 — azerisiq:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_POS_016_1.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "amount" deyeri "10" beraberdir
* Json cavabında "fee" deyeri "0" beraberdir
* Json cavabında "total" deyeri "10" beraberdir
* Json cavabında "balanceAfter" deyeri "90" beraberdir

Sorğu 2 — azersu:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_POS_016_2.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "amount" deyeri "10" beraberdir
* Json cavabında "fee" deyeri "0" beraberdir
* Json cavabında "total" deyeri "10" beraberdir
* Json cavabında "balanceAfter" deyeri "80" beraberdir

Sorğu 3 — azercell:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_POS_016_3.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "amount" deyeri "10" beraberdir
* Json cavabında "fee" deyeri "0" beraberdir
* Json cavabında "total" deyeri "10" beraberdir
* Json cavabında "balanceAfter" deyeri "70" beraberdir

Sorğu 4 — bakcell:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_POS_016_4.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "amount" deyeri "10" beraberdir
* Json cavabında "fee" deyeri "0" beraberdir
* Json cavabında "total" deyeri "10" beraberdir
* Json cavabında "balanceAfter" deyeri "60" beraberdir

## TC_PAY_POS_017 · Eyni Idempotency-Key və eyni body təkrar göndərildikdə 200, eyni id və Idempotent-Replay: true qaytarılır
tags: SC-024, P1, pos, smoke

* "acc_002" hesabından "100" məbləğində kart burax
* "idemKey" deyişenine "${random.uuid}" deyerini ver
* "citynet" təchizatçısına "CN123456" nömrəsi üçün "50" AZN ödənişi idemKey açarı ilə göndər
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "ilkOdenisId" olaraq yadda saxla

* "odenisTeminatci" deyişenine "citynet" deyerini ver
* "odenisAbuneci" deyişenine "CN123456" deyerini ver
* "odenisMeblegi" deyişenine "50" deyerini ver
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${idemKey}"
* Body olaraq "bank/pay/odenis.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "id" deyeri "ilkOdenisId" ile eynidir
* Header "Idempotent-Replay" deyerinde "true" olmalıdır
* Json cavabında "balanceAfter" deyeri "49.5" beraberdir

## TC_PAY_POS_018 · Təkrar (replay) sorğudan sonra kartın balansı yalnız bir dəfə azalmış olur
tags: SC-024, P1, pos

* "acc_002" hesabından "100" məbləğində kart burax
* "idemKey" deyişenine "${random.uuid}" deyerini ver
* "citynet" təchizatçısına "CN123456" nömrəsi üçün "50" AZN ödənişi idemKey açarı ilə göndər
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "ilkOdenisId" olaraq yadda saxla
* "citynet" təchizatçısına "CN123456" nömrəsi üçün "50" AZN ödənişi idemKey açarı ilə göndər
* Status kodunun "200" olmalıdır

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/cards/${cardId}"
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyeri "49.5" beraberdir
* Json cavabında "spentToday" deyeri "50.5" beraberdir

## TC_PAY_NEG_019 · Eyni Idempotency-Key fərqli məbləğlə göndərildikdə 409 IDEMPOTENCY_CONFLICT qaytarılır
tags: SC-024, P1, neg

* "acc_002" hesabından "100" məbləğində kart burax
* "idemKey" deyişenine "${random.uuid}" deyerini ver
* "citynet" təchizatçısına "CN123456" nömrəsi üçün "50" AZN ödənişi idemKey açarı ilə göndər
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "ilkOdenisId" olaraq yadda saxla

* "odenisTeminatci" deyişenine "citynet" deyerini ver
* "odenisAbuneci" deyişenine "CN123456" deyerini ver
* "odenisMeblegi" deyişenine "60" deyerini ver
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${idemKey}"
* Body olaraq "bank/pay/odenis.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "IDEMPOTENCY_CONFLICT" beraberdir

## TC_PAY_NEG_020 · Idempotency-Key header-i olmadıqda 400 IDEMPOTENCY_KEY_REQUIRED qaytarılır
tags: SC-024, P1, neg

* "acc_002" hesabından "100" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/pay/TC_PAY_NEG_020.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "IDEMPOTENCY_KEY_REQUIRED" beraberdir

## TC_PAY_BVA_021 · Idempotency-Key 7 simvol (min − 1) və 65 simvol (max + 1) olduqda 400 IDEMPOTENCY_KEY_INVALID qaytarılır
tags: SC-024, P2, bva

* "acc_002" hesabından "100" məbləğində kart burax

Sorğu 1 — 7 simvol:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "abcdefg"
* Body olaraq "bank/pay/TC_PAY_BVA_021_1.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "IDEMPOTENCY_KEY_INVALID" beraberdir

Sorğu 2 — 65 simvol:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
* Body olaraq "bank/pay/TC_PAY_BVA_021_2.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "IDEMPOTENCY_KEY_INVALID" beraberdir

## TC_PAY_BVA_022 · Idempotency-Key 8 simvol (min) və 64 simvol (max) olduqda ödəniş qəbul edilir
tags: SC-024, P3, bva

* "acc_002" hesabından "100" məbləğində kart burax

Sorğu 1 — 8 simvol:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "k8abcdef"
* Body olaraq "bank/pay/TC_PAY_BVA_022_1.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "balanceAfter" deyeri "90" beraberdir

Sorğu 2 — 64 simvol:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
* Body olaraq "bank/pay/TC_PAY_BVA_022_2.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "balanceAfter" deyeri "80" beraberdir

## TC_PAY_EDGE_023 · Uğursuz (422) sorğunun açarı ilə düzəldilmiş sorğu göndərildikdə 201 qaytarılır (açar istifadə olunmayıb)
tags: SC-024, P2, edge

* "acc_002" hesabından "100" məbləğində kart burax
* "idemKey" deyişenine "${random.uuid}" deyerini ver
* "azercell" təchizatçısına "501234567" nömrəsi üçün "0.49" AZN ödənişi idemKey açarı ilə göndər
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "AMOUNT_OUT_OF_RANGE" beraberdir

* "odenisTeminatci" deyişenine "azercell" deyerini ver
* "odenisAbuneci" deyişenine "501234567" deyerini ver
* "odenisMeblegi" deyişenine "10" deyerini ver
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${idemKey}"
* Body olaraq "bank/pay/odenis.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "amount" deyeri "10" beraberdir

## TC_PAY_EDGE_024 · Eyni body fərqli açarlarla göndərildikdə iki ayrı ödəniş yaranır və balans iki dəfə azalır
tags: SC-024, P3, edge

* "acc_002" hesabından "100" məbləğində kart burax
* "citynet" təchizatçısına "CN123456" nömrəsi üçün "20" AZN ödəniş et
* Json cavabında "id" deyerini "ilkOdenisId" olaraq yadda saxla

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_EDGE_024.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyeri "ilkOdenisId" ile ferqlidir
* Json cavabında "balanceAfter" deyeri "59.6" beraberdir

## TC_PAY_NEG_025 · amount mətn kimi ("10") göndərildikdə 400 VALIDATION_ERROR qaytarılır
tags: SC-025, P2, neg

* "acc_002" hesabından "100" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_NEG_025.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "amount" olmalıdır

## TC_PAY_NEG_026 · amount 0, mənfi (−5) və ya 3 onluqlu (10.555) olduqda 400 VALIDATION_ERROR qaytarılır
tags: SC-025, P2, neg

* "acc_002" hesabından "100" məbləğində kart burax

Sorğu 1 — 0:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_NEG_026_1.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "amount" olmalıdır

Sorğu 2 — −5:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_NEG_026_2.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "amount" olmalıdır

Sorğu 3 — 10.555:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_NEG_026_3.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "amount" olmalıdır

## TC_PAY_NEG_027 · Bütün məcburi sahələr göndərilmədikdə (body {}) details-də hər sahə ayrıca qaytarılır
tags: SC-025, P3, neg

* "acc_002" hesabından "100" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_NEG_027.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "4" olmalıdır
* Json cavabında "details.field" deyerinde "amount" olmalıdır
* Json cavabında "details.field" deyerinde "billerId" olmalıdır
* Json cavabında "details.field" deyerinde "cardId" olmalıdır
* Json cavabında "details.field" deyerinde "subscriberNo" olmalıdır
* Json cavabında "details.field" siyahısındakı deyerler unikal olmalıdır

## TC_PAY_NEG_028 · Azercell-ə Bakcell nömrəsi (551234567) ilə ödənişdə 422 INVALID_SUBSCRIBER və cavabda expected qaytarılır
tags: SC-025, P1, neg

* "acc_002" hesabından "100" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_NEG_028.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INVALID_SUBSCRIBER" beraberdir
* Json cavabında "expected" deyeri boş olmamalıdır

## TC_PAY_NEG_029 · Abunəçi nömrəsi təchizatçının formatına uymadıqda (Azərişıq 9 rəqəm, CityNet CN + 5 rəqəm, Aztelekom 8 rəqəm) 422 INVALID_SUBSCRIBER qaytarılır
tags: SC-025, P2, neg

* "acc_002" hesabından "100" məbləğində kart burax

Sorğu 1 — azerisiq 9 rəqəm:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_NEG_029_1.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INVALID_SUBSCRIBER" beraberdir

Sorğu 2 — citynet CN12345:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_NEG_029_2.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INVALID_SUBSCRIBER" beraberdir

Sorğu 3 — aztelekom 8 rəqəm:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_NEG_029_3.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INVALID_SUBSCRIBER" beraberdir

## TC_PAY_BVA_030 · Azercell məbləği 0.49 (min − 0.01) və 200.01 (max + 0.01) olduqda 422 AMOUNT_OUT_OF_RANGE qaytarılır
tags: SC-025, P1, bva

* "acc_002" hesabından "100" məbləğində kart burax

Sorğu 1 — 0.49:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_BVA_030_1.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "AMOUNT_OUT_OF_RANGE" beraberdir

Sorğu 2 — 200.01:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_BVA_030_2.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "AMOUNT_OUT_OF_RANGE" beraberdir

## TC_PAY_BVA_031 · Azercell məbləği 0.50 (min) və 200.00 (max) olduqda ödəniş qəbul edilir
tags: SC-025, P2, bva

* "acc_002" hesabından "300" məbləğində kart burax

Sorğu 1 — 0.50:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_BVA_031_1.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "amount" deyeri "0.5" beraberdir
* Json cavabında "fee" deyeri "0" beraberdir
* Json cavabında "total" deyeri "0.5" beraberdir
* Json cavabında "balanceAfter" deyeri "299.5" beraberdir

Sorğu 2 — 200.00:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_BVA_031_2.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "amount" deyeri "200" beraberdir
* Json cavabında "fee" deyeri "0" beraberdir
* Json cavabında "total" deyeri "200" beraberdir
* Json cavabında "balanceAfter" deyeri "99.5" beraberdir

## TC_PAY_NEG_032 · Kataloqda olmayan təchizatçı ("gasco") ilə ödənişdə 404 BILLER_NOT_FOUND qaytarılır
tags: SC-025, P2, neg

* "acc_002" hesabından "100" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_NEG_032.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "BILLER_NOT_FOUND" beraberdir

## TC_PAY_NEG_033 · Body etibarsız JSON olduqda 400 qaytarılır və ödəniş edilmir
tags: SC-025, P3, neg

Qeyd: gözlənilən nəticə Q-32 fərziyyəsinə əsaslanır (Grooming Questions).

* "acc_002" hesabından "100" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_NEG_033.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "^(INVALID_JSON|VALIDATION_ERROR)$" regex-ine uyğun olmalıdır

## TC_PAY_NEG_034 · USD kartı (user2) ilə ödənişdə 422 CURRENCY_NOT_SUPPORTED qaytarılır
tags: SC-026, P2, neg

* user2 olaraq yeni sandbox-da login ol
* "acc_003" hesabından "100" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_NEG_034.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CURRENCY_NOT_SUPPORTED" beraberdir

## TC_PAY_NEG_035 · Mövcud olmayan kartla (vcd_zzzzzzzz) ödənişdə 404 CARD_NOT_FOUND qaytarılır
tags: SC-026, P2, neg

* "acc_002" hesabından "100" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_NEG_035.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "CARD_NOT_FOUND" beraberdir

## TC_PAY_EDGE_036 · user2 user1-in kartı ilə ödəniş etməyə çalışdıqda 404 CARD_NOT_FOUND qaytarılır
tags: SC-026, P1, edge

* "acc_002" hesabından "100" məbləğində kart burax
* "user1Token" deyişenine "${token}" deyerini ver
* user2 olaraq yeni sandbox-da login ol

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_EDGE_036.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "CARD_NOT_FOUND" beraberdir

## TC_PAY_NEG_037 · Token olmadan və ya saxta tokenlə ödənişdə 401 qaytarılır
tags: SC-026, P1, neg, smoke


Sorğu 1 — token yoxdur:

* Yeni API sorğusu hazırla
* Header elave et "Idempotency-Key" = "abcdefgh12"
* Body olaraq "bank/pay/TC_PAY_NEG_037_1.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "401" olmalıdır

Sorğu 2 — saxta token:

* Yeni API sorğusu hazırla
* Bearer token elave et "fake.token.123"
* Header elave et "Idempotency-Key" = "abcdefgh12"
* Body olaraq "bank/pay/TC_PAY_NEG_037_2.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "401" olmalıdır

## TC_PAY_EDGE_038 · Token və Idempotency-Key olmadıqda 401 qaytarılır (400 IDEMPOTENCY_KEY_REQUIRED deyil)
tags: SC-026, P4, edge

* Yeni API sorğusu hazırla
* Body olaraq "bank/pay/TC_PAY_EDGE_038.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "401" olmalıdır

## TC_PAY_EDGE_039 · Idempotency-Key olmadıqda və body etibarsız JSON olduqda 400 IDEMPOTENCY_KEY_REQUIRED qaytarılır
tags: SC-026, P4, edge

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/pay/TC_PAY_EDGE_039.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "IDEMPOTENCY_KEY_REQUIRED" beraberdir

## TC_PAY_EDGE_040 · Mövcud olmayan kart və aralıqdan kənar məbləğ birlikdə olduqda 422 AMOUNT_OUT_OF_RANGE qaytarılır (404 deyil)
tags: SC-026, P4, edge

* "acc_002" hesabından "100" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_EDGE_040.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "AMOUNT_OUT_OF_RANGE" beraberdir

## TC_PAY_EDGE_041 · Dondurulmuş USD kartı ilə ödənişdə 422 CARD_NOT_ACTIVE qaytarılır (CURRENCY_NOT_SUPPORTED deyil)
tags: SC-026, P4, edge

* user2 olaraq yeni sandbox-da login ol
* "acc_003" hesabından "100" məbləğində kart burax
* Kartı "TEMPORARY" səbəbi ilə blokla

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_EDGE_041.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CARD_NOT_ACTIVE" beraberdir

## TC_PAY_BVA_042 · total 300.00 (maksimum) olan ödəniş qəbul edilir
tags: SC-027, P2, bva

* "acc_002" hesabından "1000" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_BVA_042.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "total" deyeri "300" beraberdir
* Json cavabında "balanceAfter" deyeri "700" beraberdir

## TC_PAY_BVA_043 · total 300.01 (maksimum + 0.01) olan ödənişdə 422 PER_TRANSACTION_LIMIT qaytarılır
tags: SC-027, P1, bva

* "acc_002" hesabından "1000" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_BVA_043.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "PER_TRANSACTION_LIMIT" beraberdir

## TC_PAY_BVA_044 · Bu gün 500 AZN xərclənibsə, 1 AZN-lik ödənişdə 422 DAILY_LIMIT_EXCEEDED və "remaining": 0 qaytarılır
tags: SC-027, P1, bva

* "acc_002" hesabından "1000" məbləğində kart burax
* "azerisiq" təchizatçısına "1234567890" nömrəsi üçün "300" AZN ödəniş et
* "azerisiq" təchizatçısına "1234567890" nömrəsi üçün "200" AZN ödəniş et

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_BVA_044.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "DAILY_LIMIT_EXCEEDED" beraberdir
* Json cavabında "remaining" deyeri "0" beraberdir

## TC_PAY_BVA_045 · Bu gün 499.50 AZN xərclənibsə, 0.50 AZN-lik ödəniş qəbul edilir (gündəlik cəmi tam 500)
tags: SC-027, P2, bva

* "acc_002" hesabından "1000" məbləğində kart burax
* "azerisiq" təchizatçısına "1234567890" nömrəsi üçün "300" AZN ödəniş et
* "azerisiq" təchizatçısına "1234567890" nömrəsi üçün "199.5" AZN ödəniş et

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_BVA_045.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "balanceAfter" deyeri "500" beraberdir

## TC_PAY_EDGE_046 · Gündəlik limit total üzrə yoxlanılır: 495 xərclənib, CityNet 5 AZN (total 5.20) ödənişində 422 DAILY_LIMIT_EXCEEDED, remaining 5
tags: SC-027, P2, edge

* "acc_002" hesabından "1000" məbləğində kart burax
* "azerisiq" təchizatçısına "1234567890" nömrəsi üçün "300" AZN ödəniş et
* "azerisiq" təchizatçısına "1234567890" nömrəsi üçün "195" AZN ödəniş et

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_EDGE_046.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "DAILY_LIMIT_EXCEEDED" beraberdir
* Json cavabında "remaining" deyeri "5" beraberdir

## TC_PAY_BVA_047 · Balans 49.50 olduqda 49.51 AZN ödənişdə 422 INSUFFICIENT_FUNDS qaytarılır
tags: SC-027, P1, bva

* "acc_002" hesabından "100" məbləğində kart burax
* "citynet" təchizatçısına "CN123456" nömrəsi üçün "50" AZN ödəniş et

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_BVA_047.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INSUFFICIENT_FUNDS" beraberdir

## TC_PAY_BVA_048 · Balans 49.50 olduqda 49.50 AZN ödəniş qəbul edilir və balanceAfter 0 olur
tags: SC-027, P1, bva

* "acc_002" hesabından "100" məbləğində kart burax
* "citynet" təchizatçısına "CN123456" nömrəsi üçün "50" AZN ödəniş et

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_BVA_048.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "total" deyeri "49.5" beraberdir
* Json cavabında "balanceAfter" deyeri "0" beraberdir

## TC_PAY_EDGE_049 · Balans total üzrə yoxlanılır: kartda 5.10 AZN var, CityNet 5 AZN (total 5.20) ödənişində 422 INSUFFICIENT_FUNDS
tags: SC-027, P2, edge

* "acc_002" hesabından "5.1" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_EDGE_049.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INSUFFICIENT_FUNDS" beraberdir

## TC_PAY_EDGE_050 · Balans 10 olan kartla 300.01 AZN ödənişdə 422 PER_TRANSACTION_LIMIT qaytarılır (INSUFFICIENT_FUNDS deyil)
tags: SC-027, P3, edge

* "acc_002" hesabından "10" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/pay/TC_PAY_EDGE_050.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "PER_TRANSACTION_LIMIT" beraberdir
