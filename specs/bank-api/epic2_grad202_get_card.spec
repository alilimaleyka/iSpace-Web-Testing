# GRAD-202 · GET /cards/{id} — Kart məlumatına baxmaq

EPIC-2 · Virtual kartlar.
Mənbə: Bank_API_QA_Project.xlsx → API Test Cases. Ssenari adı = test case ID-si + başlığı.
Spec-in əvvəlindəki context step hər ssenaridən əvvəl user1 ilə yeni, boş sandbox açır — ssenarilər bir-birindən asılı deyil.

tags: bank-api, epic-2, GRAD-202

* user1 olaraq yeni sandbox-da login ol

## TC_CRD_POS_028 · Yeni buraxılmış kart GET edildikdə 200 və POST cavabı ilə eyni dəyərlər qaytarılır
tags: SC-017, P1, pos, smoke

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_POS_028_on-sert.json" faylını elave et
* "POST" sorğusu gönder "/cards"
* Status kodunun "201" olmalıdır
* Json cavabında "id" deyerini "cardId" olaraq yadda saxla
* Json cavabında "id" deyerini "post_id" olaraq yadda saxla
* Json cavabında "accountId" deyerini "post_accountId" olaraq yadda saxla
* Json cavabında "maskedPan" deyerini "post_maskedPan" olaraq yadda saxla
* Json cavabında "expiry" deyerini "post_expiry" olaraq yadda saxla
* Json cavabında "currency" deyerini "post_currency" olaraq yadda saxla
* Json cavabında "status" deyerini "post_status" olaraq yadda saxla
* Json cavabında "availableBalance" deyerini "post_availableBalance" olaraq yadda saxla
* Json cavabında "createdAt" deyerini "post_createdAt" olaraq yadda saxla
* Json cavabında "spentToday" deyerini "post_spentToday" olaraq yadda saxla
* Json cavabında "limits.dailyOnline" deyerini "post_limits_dailyOnline" olaraq yadda saxla
* Json cavabında "limits.perTransaction" deyerini "post_limits_perTransaction" olaraq yadda saxla
* "post_label" deyişenine "Onlayn" deyerini ver
* "post_blockReason" deyişenine "null" deyerini ver
* "post_blockedAt" deyişenine "null" deyerini ver

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/cards/${cardId}"
* Status kodunun "200" olmalıdır
* Json cavabını cedvel ile yoxla

   |path|value|
   |----|-----|
   |id|${post_id}|
   |accountId|${post_accountId}|
   |label|${post_label}|
   |maskedPan|${post_maskedPan}|
   |expiry|${post_expiry}|
   |currency|${post_currency}|
   |status|${post_status}|
   |availableBalance|${post_availableBalance}|
   |blockReason|${post_blockReason}|
   |blockedAt|${post_blockedAt}|
   |createdAt|${post_createdAt}|
   |spentToday|${post_spentToday}|
   |limits.dailyOnline|${post_limits_dailyOnline}|
   |limits.perTransaction|${post_limits_perTransaction}|


## TC_CRD_EDGE_029 · user2 user1-in kartını GET etdikdə 404 NOT_FOUND qaytarılır
tags: SC-017, P1, edge

* "acc_002" hesabından "10" məbləğində kart burax
* "user1Token" deyişenine "${token}" deyerini ver
* user2 olaraq yeni sandbox-da login ol

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/cards/${cardId}"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC_CRD_NEG_030 · Mövcud olmayan kart id-si (vcd_zzzzzzzz) GET edildikdə 404 NOT_FOUND qaytarılır
tags: SC-017, P2, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/cards/vcd_zzzzzzzz"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC_CRD_NEG_031 · Token olmadan və ya saxta tokenlə kart GET edildikdə 401 qaytarılır
tags: SC-017, P2, neg


Sorğu 1 — token yoxdur:

* Yeni API sorğusu hazırla
* "GET" sorğusu gönder "/cards/vcd_zzzzzzzz"
* Status kodunun "401" olmalıdır

Sorğu 2 — saxta token:

* Yeni API sorğusu hazırla
* Bearer token elave et "fake.token.123"
* "GET" sorğusu gönder "/cards/vcd_zzzzzzzz"
* Status kodunun "401" olmalıdır

## TC_CRD_POS_032 · Kartla 50.50 AZN ödənişdən sonra GET-də availableBalance 50.50 azalır, spentToday 50.50 artır
tags: SC-017, P1, pos

* "acc_002" hesabından "100" məbləğində kart burax
* "azersu" təchizatçısına "12345678" nömrəsi üçün "50.5" AZN ödəniş et

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/cards/${cardId}"
* Status kodunun "200" olmalıdır
* Json cavabında "availableBalance" deyeri "49.5" beraberdir
* Json cavabında "spentToday" deyeri "50.5" beraberdir
