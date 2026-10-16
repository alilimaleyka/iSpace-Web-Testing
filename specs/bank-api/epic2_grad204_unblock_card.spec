# GRAD-204 · POST /cards/{id}/unblock — Dondurulmuş kartı açmaq

EPIC-2 · Virtual kartlar.
Mənbə: Bank_API_QA_Project.xlsx → API Test Cases. Ssenari adı = test case ID-si + başlığı.
Spec-in əvvəlindəki context step hər ssenaridən əvvəl user1 ilə yeni, boş sandbox açır — ssenarilər bir-birindən asılı deyil.

tags: bank-api, epic-2, GRAD-204

* user1 olaraq yeni sandbox-da login ol

## TC_CRD_POS_054 · FROZEN kart açıldıqda 200: status ACTIVE, blockReason və blockedAt null
tags: SC-021, P1, pos, smoke

* "acc_002" hesabından "10" məbləğində kart burax
* Kartı "TEMPORARY" səbəbi ilə blokla

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "POST" sorğusu gönder "/cards/${cardId}/unblock"
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "blockReason" deyeri null olmalıdır
* Json cavabında "blockedAt" deyeri null olmalıdır

## TC_CRD_NEG_055 · ACTIVE kart açılmaq istədikdə 409 NOT_FROZEN qaytarılır
tags: SC-021, P2, neg

* "acc_002" hesabından "10" məbləğində kart burax

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "POST" sorğusu gönder "/cards/${cardId}/unblock"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "NOT_FROZEN" beraberdir

## TC_CRD_NEG_056 · LOST ilə bloklanmış kart açılmaq istədikdə 409 PERMANENTLY_BLOCKED qaytarılır
tags: SC-021, P1, neg

* "acc_002" hesabından "10" məbləğində kart burax
* Kartı "LOST" səbəbi ilə blokla

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "POST" sorğusu gönder "/cards/${cardId}/unblock"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "PERMANENTLY_BLOCKED" beraberdir

## TC_CRD_NEG_057 · Əvvəl dondurulub sonra STOLEN ilə bloklanmış kart açılmaq istədikdə 409 PERMANENTLY_BLOCKED qaytarılır
tags: SC-021, P2, neg

* "acc_002" hesabından "10" məbləğində kart burax
* Kartı "TEMPORARY" səbəbi ilə blokla
* Kartı "STOLEN" səbəbi ilə blokla

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "POST" sorğusu gönder "/cards/${cardId}/unblock"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "PERMANENTLY_BLOCKED" beraberdir

## TC_CRD_EDGE_058 · Açılmış kart yenidən dondurula bilir (FROZEN → ACTIVE → FROZEN dövrü)
tags: SC-021, P3, edge

* "acc_002" hesabından "10" məbləğində kart burax
* Kartı "TEMPORARY" səbəbi ilə blokla
* Kartı blokdan çıxar

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/crd/TC_CRD_EDGE_058.json" faylını elave et
* "POST" sorğusu gönder "/cards/${cardId}/block"
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "FROZEN" beraberdir

## TC_CRD_POS_059 · Açılmış kart GET /cards/{id}-də ACTIVE, null blockReason/blockedAt və dəyişməmiş balansla görünür
tags: SC-021, P2, pos

* "acc_002" hesabından "10" məbləğində kart burax
* Kartı "TEMPORARY" səbəbi ilə blokla
* Kartı blokdan çıxar

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/cards/${cardId}"
* Status kodunun "200" olmalıdır
* Json cavabında "status" deyeri "ACTIVE" beraberdir
* Json cavabında "blockReason" deyeri null olmalıdır
* Json cavabında "blockedAt" deyeri null olmalıdır
* Json cavabında "availableBalance" deyeri "10" beraberdir

## TC_CRD_NEG_060 · Mövcud olmayan kart (vcd_zzzzzzzz) açılmaq istədikdə 404 NOT_FOUND qaytarılır
tags: SC-021, P3, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "POST" sorğusu gönder "/cards/vcd_zzzzzzzz/unblock"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC_CRD_EDGE_061 · user2 user1-in dondurulmuş kartını açmağa çalışdıqda 404 NOT_FOUND qaytarılır
tags: SC-021, P1, edge

* "acc_002" hesabından "10" məbləğində kart burax
* Kartı "TEMPORARY" səbəbi ilə blokla
* "user1Token" deyişenine "${token}" deyerini ver
* user2 olaraq yeni sandbox-da login ol

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "POST" sorğusu gönder "/cards/${cardId}/unblock"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC_CRD_NEG_062 · Token olmadan və ya saxta tokenlə kart açma sorğusunda 401 qaytarılır
tags: SC-021, P2, neg


Sorğu 1 — token yoxdur:

* Yeni API sorğusu hazırla
* "POST" sorğusu gönder "/cards/vcd_zzzzzzzz/unblock"
* Status kodunun "401" olmalıdır

Sorğu 2 — saxta token:

* Yeni API sorğusu hazırla
* Bearer token elave et "fake.token.123"
* "POST" sorğusu gönder "/cards/vcd_zzzzzzzz/unblock"
* Status kodunun "401" olmalıdır

## TC_CRD_POS_063 · Açılmış kartla ödəniş uğurla keçir (201)
tags: SC-021, P1, pos

* "acc_002" hesabından "100" məbləğində kart burax
* Kartı "TEMPORARY" səbəbi ilə blokla
* Kartı blokdan çıxar

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Header elave et "Idempotency-Key" = "${random.uuid}"
* Body olaraq "bank/crd/TC_CRD_POS_063.json" faylını elave et
* "POST" sorğusu gönder "/bill-payments"
* Status kodunun "201" olmalıdır
* Json cavabında "status" deyeri "SUCCESS" beraberdir
* Json cavabında "balanceAfter" deyeri "90" beraberdir
