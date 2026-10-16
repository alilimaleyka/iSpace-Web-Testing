# GRAD-203 · POST /cards/{id}/block — Kartı bloklamaq / dondurmaq

EPIC-2 · Virtual kartlar.
Mənbə: Bank_API_QA_Project.xlsx → API Test Cases. Ssenari adı = test case ID-si + başlığı.
Spec-in əvvəlindəki context step hər ssenaridən əvvəl user1 ilə yeni, boş sandbox açır — ssenarilər bir-birindən asılı deyil.

tags: bank-api, epic-2, GRAD-203

* user1 olaraq yeni sandbox-da login ol

## TC_CRD_POS_033 · ACTIVE kart TEMPORARY səbəbi ilə dondurulduqda 200: status FROZEN, blockReason TEMPORARY, blockedAt dolu
tags: SC-018, P1, pos, smoke

* "acc_002" hesabından "10" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_POS_033.json" faylını elave et
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "FROZEN" beraberdir
* Json cavabında "blockReason" deyeri "TEMPORARY" beraberdir
* Json cavabında "blockedAt" deyeri "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}([.][0-9]{3})?Z$" regex-ine uyğun olmalıdır

## TC_CRD_POS_034 · ACTIVE kart LOST səbəbi ilə bloklandıqda 200: status BLOCKED
tags: SC-018, P1, pos

* "acc_002" hesabından "10" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_POS_034.json" faylını elave et
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Json cavabında "blockReason" deyeri "LOST" beraberdir
* Json cavabında "blockedAt" deyeri "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}([.][0-9]{3})?Z$" regex-ine uyğun olmalıdır

## TC_CRD_POS_035 · ACTIVE kart STOLEN səbəbi ilə bloklandıqda 200: status BLOCKED
tags: SC-018, P2, pos

* "acc_002" hesabından "10" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_POS_035.json" faylını elave et
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Json cavabında "blockReason" deyeri "STOLEN" beraberdir
* Json cavabında "blockedAt" deyeri "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}([.][0-9]{3})?Z$" regex-ine uyğun olmalıdır

## TC_CRD_NEG_036 · FROZEN kart yenidən TEMPORARY ilə dondurulduqda 409 ALREADY_FROZEN qaytarılır
tags: SC-018, P2, neg

* "acc_002" hesabından "10" məbləğində kart burax
* Kartı "TEMPORARY" səbəbi ilə blokla

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_NEG_036.json" faylını elave et
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "ALREADY_FROZEN" beraberdir

## TC_CRD_POS_037 · FROZEN kart LOST səbəbi ilə bloklandıqda 200: status BLOCKED (eskalasiya)
tags: SC-018, P2, pos

Qeyd: gözlənilən nəticə Q-25 fərziyyəsinə əsaslanır (Grooming Questions).

* "acc_002" hesabından "10" məbləğində kart burax
* Kartı "TEMPORARY" səbəbi ilə blokla

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_POS_037.json" faylını elave et
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Json cavabında "blockReason" deyeri "LOST" beraberdir
* Json cavabında "blockedAt" deyeri "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}([.][0-9]{3})?Z$" regex-ine uyğun olmalıdır

## TC_CRD_POS_038 · FROZEN kart STOLEN səbəbi ilə bloklandıqda 200: status BLOCKED (eskalasiya)
tags: SC-018, P1, pos

Qeyd: gözlənilən nəticə Q-25 fərziyyəsinə əsaslanır (Grooming Questions).

* "acc_002" hesabından "10" məbləğində kart burax
* Kartı "TEMPORARY" səbəbi ilə blokla

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_POS_038.json" faylını elave et
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "BLOCKED" beraberdir
* Json cavabında "blockReason" deyeri "STOLEN" beraberdir
* Json cavabında "blockedAt" deyeri "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}([.][0-9]{3})?Z$" regex-ine uyğun olmalıdır

## TC_CRD_NEG_039 · BLOCKED kart TEMPORARY ilə dondurulmaq istədikdə 409 CARD_BLOCKED qaytarılır
tags: SC-018, P1, neg

* "acc_002" hesabından "10" məbləğində kart burax
* Kartı "LOST" səbəbi ilə blokla

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_NEG_039.json" faylını elave et
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "CARD_BLOCKED" beraberdir

## TC_CRD_NEG_040 · BLOCKED kart yenidən LOST ilə bloklandıqda 409 CARD_BLOCKED qaytarılır
tags: SC-018, P3, neg

* "acc_002" hesabından "10" məbləğində kart burax
* Kartı "LOST" səbəbi ilə blokla

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_NEG_040.json" faylını elave et
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "CARD_BLOCKED" beraberdir

## TC_CRD_NEG_041 · BLOCKED kart STOLEN ilə bloklandıqda 409 CARD_BLOCKED qaytarılır
tags: SC-018, P3, neg

* "acc_002" hesabından "10" məbləğində kart burax
* Kartı "LOST" səbəbi ilə blokla

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_NEG_041.json" faylını elave et
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "CARD_BLOCKED" beraberdir

## TC_CRD_NEG_042 · reason icazəli dəyər olmadıqda ("BROKEN") 400 VALIDATION_ERROR qaytarılır
tags: SC-019, P2, neg

* "acc_002" hesabından "10" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_NEG_042.json" faylını elave et
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "reason" olmalıdır

## TC_CRD_NEG_043 · reason göndərilmədikdə (body {}) 400 VALIDATION_ERROR qaytarılır
tags: SC-019, P2, neg

* "acc_002" hesabından "10" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_NEG_043.json" faylını elave et
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "reason" olmalıdır

## TC_CRD_NEG_044 · reason kiçik hərflə ("temporary") göndərildikdə 400 VALIDATION_ERROR qaytarılır
tags: SC-019, P3, neg

Qeyd: gözlənilən nəticə Q-26 fərziyyəsinə əsaslanır (Grooming Questions).

* "acc_002" hesabından "10" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_NEG_044.json" faylını elave et
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "reason" olmalıdır

## TC_CRD_NEG_045 · Body ümumiyyətlə göndərilmədikdə 400 INVALID_JSON qaytarılır
tags: SC-019, P3, neg

* "acc_002" hesabından "10" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "INVALID_JSON" beraberdir

## TC_CRD_EDGE_046 · Mövcud olmayan kart + icazəsiz reason olduqda 400 VALIDATION_ERROR qaytarılır (404 deyil)
tags: SC-019, P3, edge

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_EDGE_046.json" faylını elave et
* "POST" sorğusu gönder "/cards/vcd_zzzzzzzz/block"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir

## TC_CRD_EDGE_047 · BLOCKED kart + icazəsiz reason olduqda 400 VALIDATION_ERROR qaytarılır (409 CARD_BLOCKED deyil)
tags: SC-019, P3, edge

* "acc_002" hesabından "10" məbləğində kart burax
* Kartı "LOST" səbəbi ilə blokla

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_EDGE_047.json" faylını elave et
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir

## TC_CRD_NEG_048 · Mövcud olmayan kart (vcd_zzzzzzzz) bloklanmaq istədikdə 404 NOT_FOUND qaytarılır
tags: SC-020, P2, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_NEG_048.json" faylını elave et
* "POST" sorğusu gönder "/cards/vcd_zzzzzzzz/block"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC_CRD_EDGE_049 · user2 user1-in kartını bloklamağa çalışdıqda 404 NOT_FOUND qaytarılır və kart ACTIVE qalır
tags: SC-020, P1, edge

* "acc_002" hesabından "10" məbləğində kart burax
* "user1Token" deyişenine "${token}" deyerini ver
* user2 olaraq yeni sandbox-da login ol

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_EDGE_049.json" faylını elave et
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC_CRD_NEG_050 · Token olmadan və ya saxta tokenlə bloklama sorğusunda 401 qaytarılır
tags: SC-020, P2, neg


Sorğu 1 — token yoxdur:

* Yeni API sorğusu hazırla
* Body olaraq "bank/crd/TC_CRD_NEG_050_1.json" faylını elave et
* "POST" sorğusu gönder "/cards/vcd_zzzzzzzz/block"
* Status kodunun "401" olmalıdır

Sorğu 2 — saxta token:

* Yeni API sorğusu hazırla
* Bearer token elave et "fake.token.123"
* Body olaraq "bank/crd/TC_CRD_NEG_050_2.json" faylını elave et
* "POST" sorğusu gönder "/cards/vcd_zzzzzzzz/block"
* Status kodunun "401" olmalıdır

## TC_CRD_POS_051 · Dondurulmuş kart GET /cards/{id}-də dərhal FROZEN, blockReason TEMPORARY və eyni blockedAt ilə görünür
tags: SC-020, P2, pos

* "acc_002" hesabından "10" məbləğində kart burax
* Kartı "TEMPORARY" səbəbi ilə blokla
* Json cavabında "blockedAt" deyerini "blokTarixi" olaraq yadda saxla

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/cards/${cardId}"
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "FROZEN" beraberdir
* Json cavabında "blockReason" deyeri "TEMPORARY" beraberdir
* Json cavabında "availableBalance" deyeri "10" beraberdir
* Json cavabında "blockedAt" deyeri "blokTarixi" ile eynidir

## TC_CRD_NEG_052 · FROZEN kartla ödəniş edildikdə 422 CARD_NOT_ACTIVE qaytarılır
tags: SC-020, P1, neg

* "acc_002" hesabından "100" məbləğində kart burax
* Kartı "TEMPORARY" səbəbi ilə blokla

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/crd/TC_CRD_NEG_052.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CARD_NOT_ACTIVE" beraberdir

## TC_CRD_NEG_053 · BLOCKED kartla ödəniş edildikdə 422 CARD_NOT_ACTIVE qaytarılır
tags: SC-020, P2, neg

* "acc_002" hesabından "100" məbləğində kart burax
* Kartı "LOST" səbəbi ilə blokla

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/crd/TC_CRD_NEG_053.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "CARD_NOT_ACTIVE" beraberdir
