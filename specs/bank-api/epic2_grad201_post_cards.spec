# GRAD-201 · POST /cards — Virtual kart buraxmaq

EPIC-2 · Virtual kartlar.
Mənbə: Bank_API_QA_Project.xlsx → API Test Cases. Ssenari adı = test case ID-si + başlığı.
Spec-in əvvəlindəki context step hər ssenaridən əvvəl user1 ilə yeni, boş sandbox açır — ssenarilər bir-birindən asılı deyil.

tags: bank-api, epic-2, GRAD-201

* user1 olaraq yeni sandbox-da login ol

## TC_CRD_POS_001 · Etibarlı sorğu ilə kart buraxıldıqda 201: status ACTIVE, availableBalance = initialAmount, limitlər 500/300, spentToday 0
tags: SC-013, P1, pos, smoke

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_POS_001.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "201" olmalıdır
* Cavab "bank/card.schema.json" JSON schema-sına uyğun olmalıdır
* Json cavabında "id" deyeri "^vcd_[A-Za-z0-9]{8}$" regex-ine uyğun olmalıdır
* Json cavabında "id" deyerini "yeniId" olaraq yadda saxla
* Header "Location" deyerinde "/cards/${yeniId}" olmalıdır
* Json cavabında "accountId" deyeri "acc_002" beraberdir
* Json cavabında "label" deyeri "Kommunal" beraberdir
* Json cavabında "currency" deyeri "AZN" beraberdir
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "availableBalance" deyeri "100" beraberdir
* Json cavabını cedvel ile yoxla

   |path|value|
   |----|-----|
   |limits.dailyOnline|500|
   |limits.perTransaction|300|

* Json cavabında "spentToday" deyeri "0" beraberdir
* Json cavabında "blockReason" deyeri null olmalıdır
* Json cavabında "blockedAt" deyeri null olmalıdır
* Json cavabında "createdAt" deyeri "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}([.][0-9]{3})?Z$" regex-ine uyğun olmalıdır

## TC_CRD_POS_002 · Kart buraxıldıqda maskedPan "4169 73** **** NNNN" formatında, expiry isə bu gündən 3 il sonranın MM/YY-idir
tags: SC-013, P2, pos

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_POS_002.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "201" olmalıdır
* Json cavabında "maskedPan" deyeri "^4169 73[*][*] [*][*][*][*] [0-9]{4}$" regex-ine uyğun olmalıdır
* Bu gündən "3" il sonranın tarixini "MM/yy" formatında "gozlenilenExpiry" olaraq yadda saxla
* Json cavabında "expiry" deyeri "${gozlenilenExpiry}" beraberdir

## TC_CRD_POS_003 · label göndərilmədikdə kart yaradılır və cavabda "label": null qaytarılır
tags: SC-013, P3, pos

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_POS_003.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "201" olmalıdır
* Json cavabında "label" açarı mövcud olmalıdır
* Json cavabında "label" deyeri null olmalıdır

## TC_CRD_POS_004 · user2 USD hesabından kart buraxdıqda kartın valyutası USD olur
tags: SC-013, P2, pos

* user2 olaraq yeni sandbox-da login ol

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_POS_004.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "201" olmalıdır
* Json cavabında "currency" deyeri "USD" beraberdir
* Json cavabında "availableBalance" deyeri "50" beraberdir

## TC_CRD_EDGE_005 · Kart buraxıldıqdan sonra əsas hesabın balansı (GET /me/accounts) dəyişmir
tags: SC-013, P2, edge

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/me/accounts"
* Status kodunun "200" olmalıdır
* Json cavabında "$" deyerini "hesablarEvvel" olaraq yadda saxla
* "acc_002" hesabından "100" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/me/accounts"
* Status kodunun "200" olmalıdır
* Json cavabında "$" deyeri "hesablarEvvel" ile eynidir

## TC_CRD_BVA_006 · initialAmount 1.00 (aşağı sərhəd) olduqda kart yaradılır
tags: SC-014, P2, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_BVA_006.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "201" olmalıdır
* Json cavabında "availableBalance" deyeri "1" beraberdir

## TC_CRD_BVA_007 · initialAmount 1000.00 (yuxarı sərhəd) olduqda kart yaradılır
tags: SC-014, P2, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_BVA_007.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "201" olmalıdır
* Json cavabında "availableBalance" deyeri "1000" beraberdir

## TC_CRD_BVA_008 · initialAmount 0.99 (min − 0.01) olduqda 400 VALIDATION_ERROR qaytarılır
tags: SC-014, P2, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_BVA_008.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "initialAmount" olmalıdır

## TC_CRD_BVA_009 · initialAmount 1000.01 (max + 0.01) olduqda 400 VALIDATION_ERROR qaytarılır
tags: SC-014, P2, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_BVA_009.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "initialAmount" olmalıdır

## TC_CRD_NEG_010 · initialAmount mətn kimi ("50") göndərildikdə 400 VALIDATION_ERROR qaytarılır
tags: SC-014, P2, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_NEG_010.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "initialAmount" olmalıdır

## TC_CRD_NEG_011 · initialAmount 3 onluqlu (10.555) olduqda 400 VALIDATION_ERROR qaytarılır
tags: SC-014, P2, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_NEG_011.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "initialAmount" olmalıdır

## TC_CRD_NEG_012 · initialAmount göndərilmədikdə 400 VALIDATION_ERROR qaytarılır
tags: SC-014, P3, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_NEG_012.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "initialAmount" olmalıdır

## TC_CRD_NEG_013 · user1 başqa istifadəçinin hesabı (acc_003) ilə kart açdıqda 403 FORBIDDEN qaytarılır
tags: SC-015, P1, neg

Qeyd: gözlənilən nəticə Q-18 fərziyyəsinə əsaslanır (Grooming Questions).

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_NEG_013.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "403" olmalıdır
* Json cavabında "code" deyeri "FORBIDDEN" beraberdir

## TC_CRD_NEG_014 · Mövcud olmayan hesab (acc_999) ilə kart açdıqda 404 ACCOUNT_NOT_FOUND qaytarılır
tags: SC-015, P2, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_NEG_014.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "ACCOUNT_NOT_FOUND" beraberdir

## TC_CRD_NEG_015 · accountId göndərilmədikdə 400 VALIDATION_ERROR qaytarılır
tags: SC-015, P3, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_NEG_015.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "accountId" olmalıdır

## TC_CRD_BVA_016 · label 31 simvol (max + 1) olduqda 400 VALIDATION_ERROR qaytarılır
tags: SC-015, P3, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_BVA_016.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "label" olmalıdır

## TC_CRD_BVA_017 · label boş string ("", min − 1) olduqda 400 VALIDATION_ERROR qaytarılır
tags: SC-015, P3, bva

Qeyd: gözlənilən nəticə Q-21 fərziyyəsinə əsaslanır (Grooming Questions).

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_BVA_017.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "label" olmalıdır

## TC_CRD_BVA_018 · label 30 simvol (yuxarı sərhəd) olduqda kart yaradılır
tags: SC-015, P3, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_BVA_018.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "201" olmalıdır
* Json cavabında "label" deyeri "LLLLLLLLLLLLLLLLLLLLLLLLLLLLLL" beraberdir

## TC_CRD_NEG_019 · Üç sahə eyni anda səhv olduqda details-də hər səhv sahə ayrıca qaytarılır
tags: SC-015, P3, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_NEG_019.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "3" olmalıdır
* Json cavabında "details.field" deyerinde "accountId" olmalıdır
* Json cavabında "details.field" deyerinde "initialAmount" olmalıdır
* Json cavabında "details.field" deyerinde "label" olmalıdır
* Json cavabında "details.field" siyahısındakı deyerler unikal olmalıdır

## TC_CRD_NEG_020 · Authorization header olmadıqda və ya saxta token göndərildikdə 401 qaytarılır
tags: SC-015, P1, neg, smoke


Sorğu 1 — token yoxdur:

* Yeni API sorğusu hazırla
* Body olaraq "bank/crd/TC_CRD_NEG_020_1.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "401" olmalıdır

Sorğu 2 — saxta token:

* Yeni API sorğusu hazırla
* Bearer token elave et "fake.token.123"
* Body olaraq "bank/crd/TC_CRD_NEG_020_2.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "401" olmalıdır

## TC_CRD_NEG_021 · Body etibarsız JSON olduqda 400 qaytarılır və kart yaradılmır
tags: SC-015, P3, neg

Qeyd: gözlənilən nəticə Q-19 fərziyyəsinə əsaslanır (Grooming Questions).

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_NEG_021.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "^(INVALID_JSON|VALIDATION_ERROR)$" regex-ine uyğun olmalıdır

## TC_CRD_BVA_022 · user2 hesab balansına bərabər məbləğ (890.50) yüklədikdə kart yaradılır
tags: SC-016, P2, bva

* user2 olaraq yeni sandbox-da login ol

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_BVA_022.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "201" olmalıdır
* Json cavabında "availableBalance" deyeri "890.5" beraberdir

## TC_CRD_BVA_023 · user2 balansdan böyük məbləğ (890.51 və 891) yüklədikdə 422 INSUFFICIENT_FUNDS qaytarılır
tags: SC-016, P1, bva, smoke

* user2 olaraq yeni sandbox-da login ol

Sorğu 1 — 890.51:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_BVA_023_1.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INSUFFICIENT_FUNDS" beraberdir

Sorğu 2 — 891:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_BVA_023_2.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "INSUFFICIENT_FUNDS" beraberdir

## TC_CRD_BVA_024 · 3 ACTIVE kart olduqda 4-cü kart üçün 422 CARD_LIMIT_REACHED qaytarılır
tags: SC-016, P1, bva

* "acc_002" hesabından "10" məbləğində kart burax
* "acc_002" hesabından "10" məbləğində kart burax
* "acc_002" hesabından "10" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_BVA_024.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CARD_LIMIT_REACHED" beraberdir

## TC_CRD_EDGE_025 · 2 ACTIVE + 1 FROZEN kart olduqda 4-cü kart üçün 422 CARD_LIMIT_REACHED qaytarılır (FROZEN limitə sayılır)
tags: SC-016, P2, edge

* "acc_002" hesabından "10" məbləğində kart burax ve id-ni "ilkKartId" olaraq yadda saxla
* "acc_002" hesabından "10" məbləğində kart burax
* "acc_002" hesabından "10" məbləğində kart burax
* "cardId" deyişenine "${ilkKartId}" deyerini ver
* Kartı "TEMPORARY" səbəbi ilə blokla

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_EDGE_025.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CARD_LIMIT_REACHED" beraberdir

## TC_CRD_EDGE_026 · 3 kartdan biri BLOCKED edildikdən sonra yeni kart yaradılır (BLOCKED limitə sayılmır)
tags: SC-016, P1, edge

* "acc_002" hesabından "10" məbləğində kart burax ve id-ni "ilkKartId" olaraq yadda saxla
* "acc_002" hesabından "10" məbləğində kart burax
* "acc_002" hesabından "10" məbləğində kart burax
* "cardId" deyişenine "${ilkKartId}" deyerini ver
* Kartı "LOST" səbəbi ilə blokla

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_EDGE_026.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "ACTIVE" beraberdir

## TC_CRD_EDGE_027 · Karta yükləmə balansı azaltmadığı üçün user2 cəmi balansdan çox olan iki kart (500 + 500) aça bilir
tags: SC-016, P3, edge

Qeyd: gözlənilən nəticə Q-23 fərziyyəsinə əsaslanır (Grooming Questions).

* user2 olaraq yeni sandbox-da login ol
* "acc_003" hesabından "500" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_EDGE_027.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "201" olmalıdır
