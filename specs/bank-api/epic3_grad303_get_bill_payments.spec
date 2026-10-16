# GRAD-303 · GET /bill-payments — Ödəniş tarixçəsi, filtr və səhifələmə

EPIC-3 · Kommunal ödənişlər.
Mənbə: Bank_API_QA_Project.xlsx → API Test Cases. Ssenari adı = test case ID-si + başlığı.
Spec-in əvvəlindəki context step hər ssenaridən əvvəl user1 ilə yeni, boş sandbox açır — ssenarilər bir-birindən asılı deyil.
Hər ssenari Dataset P ilə başlayır (bank.cpt): 2 kart və 18 ödəniş.

tags: bank-api, epic-3, GRAD-303

* user1 olaraq yeni sandbox-da login ol

## TC_PAY_POS_051 · Parametrsiz sorğuda 200: page 1, limit 10, total 18, totalPages 2 və ən yeni ödəniş (000018) birinci
tags: SC-028, P1, pos, smoke

* Dataset P ödəniş tarixçəsini yarat
* Bu gündən "0" gün sonranın tarixini "yyyyMMdd" formatında "bugun" olaraq yadda saxla

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "page" deyeri "1" beraberdir
* Json cavabında "limit" deyeri "10" beraberdir
* Json cavabında "total" deyeri "18" beraberdir
* Json cavabında "totalPages" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "10" olmalıdır
* Json cavabında "items.receiptNo" siyahısı azalan sırada olmalıdır
* Json cavabında "items.createdAt" siyahısı azalan sırada olmalıdır
* Json cavabında "items[0].receiptNo" deyeri "RCP-${bugun}-000018" beraberdir

## TC_PAY_POS_052 · page=2 olduqda qalan 8 ödəniş (000008 … 000001) qaytarılır və 1-ci səhifə ilə təkrarlanmır
tags: SC-028, P1, pos

* Dataset P ödəniş tarixçəsini yarat
* Bu gündən "0" gün sonranın tarixini "yyyyMMdd" formatında "bugun" olaraq yadda saxla

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "page" = "2"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "page" deyeri "2" beraberdir
* Json cavabında "limit" deyeri "10" beraberdir
* Json cavabında "total" deyeri "18" beraberdir
* Json cavabında "totalPages" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "8" olmalıdır
* Json cavabında "items.receiptNo" siyahısı azalan sırada olmalıdır
* Json cavabında "items.createdAt" siyahısı azalan sırada olmalıdır
* Json cavabında "items[7].receiptNo" deyeri "RCP-${bugun}-000001" beraberdir
* Json cavabında "items[0].receiptNo" deyeri "RCP-${bugun}-000008" beraberdir
* Json cavabında "items.receiptNo" siyahısındakı deyerler unikal olmalıdır

## TC_PAY_POS_053 · Mövcud olmayan səhifə (page=3) istədikdə 200 və boş items qaytarılır
tags: SC-028, P2, pos

* Dataset P ödəniş tarixçəsini yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "page" = "3"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır
* Json cavabında "total" deyeri "18" beraberdir
* Json cavabında "totalPages" deyeri "2" beraberdir

## TC_PAY_BVA_054 · limit=1 (min) və limit=50 (max) qəbul edilir: 1 → 18 səhifə, 50 → bütün 18 ödəniş bir səhifədə
tags: SC-028, P3, bva

* Dataset P ödəniş tarixçəsini yarat

Sorğu 1 — limit=1:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "limit" = "1"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "page" deyeri "1" beraberdir
* Json cavabında "limit" deyeri "1" beraberdir
* Json cavabında "total" deyeri "18" beraberdir
* Json cavabında "totalPages" deyeri "18" beraberdir
* Json cavabında "items" massivinin ölçüsü "1" olmalıdır

Sorğu 2 — limit=50:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "limit" = "50"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "page" deyeri "1" beraberdir
* Json cavabında "limit" deyeri "50" beraberdir
* Json cavabında "total" deyeri "18" beraberdir
* Json cavabında "totalPages" deyeri "1" beraberdir
* Json cavabında "items" massivinin ölçüsü "18" olmalıdır

## TC_PAY_BVA_055 · limit=0 (min − 1) və limit=51 (max + 1) olduqda 400 VALIDATION_ERROR qaytarılır
tags: SC-028, P2, bva

* Dataset P ödəniş tarixçəsini yarat

Sorğu 1 — limit=0:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "limit" = "0"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "limit" olmalıdır

Sorğu 2 — limit=51:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "limit" = "51"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "limit" olmalıdır

## TC_PAY_NEG_056 · page=0, page=-1 və page=abc olduqda 400 VALIDATION_ERROR qaytarılır
tags: SC-028, P2, neg

* Dataset P ödəniş tarixçəsini yarat

Sorğu 1 — page=0:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "page" = "0"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "page" olmalıdır

Sorğu 2 — page=-1:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "page" = "-1"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "page" olmalıdır

Sorğu 3 — page=abc:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "page" = "abc"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "page" olmalıdır

## TC_PAY_POS_057 · Hər tarixçə elementində sənəddəki sahələr var, status SUCCESS və total = amount + fee
tags: SC-028, P3, pos

* Dataset P ödəniş tarixçəsini yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "limit" = "50"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Cavab "bank/payment-history.schema.json" JSON schema-sına uyğun olmalıdır
* Json cavabında "items.status" siyahısındakı bütün deyerler "SUCCESS" olmalıdır
* Json cavabında "items.findAll { it.billerId == 'azersu' }.fee" siyahısındakı bütün deyerler "0" olmalıdır
* Json cavabında "items.findAll { it.billerId == 'azersu' }.total" siyahısındakı bütün deyerler "1" olmalıdır
* Json cavabında "items.findAll { it.billerId == 'citynet' }.fee" siyahısındakı bütün deyerler "0.2" olmalıdır
* Json cavabında "items.findAll { it.billerId == 'citynet' }.total" siyahısındakı bütün deyerler "5.2" olmalıdır
* Json cavabında "items.findAll { it.billerId == 'aztelekom' }.fee" siyahısındakı bütün deyerler "0.5" olmalıdır
* Json cavabında "items.findAll { it.billerId == 'aztelekom' }.total" siyahısındakı bütün deyerler "2.5" olmalıdır

## TC_PAY_EDGE_058 · user2 öz tarixçəsini istədikdə user1-in ödənişləri görünmür
tags: SC-028, P1, edge

* Dataset P ödəniş tarixçəsini yarat
* user2 olaraq yeni sandbox-da login ol
* user2 olaraq yeni sandbox-da login ol

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır

## TC_PAY_NEG_059 · Token olmadan və ya saxta tokenlə tarixçə istədikdə 401 qaytarılır
tags: SC-028, P2, neg

* Dataset P ödəniş tarixçəsini yarat

Sorğu 1 — token yoxdur:

* Yeni API sorğusu hazırla
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "401" olmalıdır

Sorğu 2 — saxta token:

* Yeni API sorğusu hazırla
* Bearer token elave et "fake.token.123"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "401" olmalıdır

## TC_PAY_POS_060 · billerId=citynet olduqda yalnız 6 CityNet ödənişi qaytarılır və total 6 olur
tags: SC-029, P2, pos

* Dataset P ödəniş tarixçəsini yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "billerId" = "citynet"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "page" deyeri "1" beraberdir
* Json cavabında "limit" deyeri "10" beraberdir
* Json cavabında "total" deyeri "6" beraberdir
* Json cavabında "totalPages" deyeri "1" beraberdir
* Json cavabında "items" massivinin ölçüsü "6" olmalıdır
* Json cavabında "items.billerId" siyahısındakı bütün deyerler "citynet" olmalıdır

## TC_PAY_POS_061 · billerId=citynet&limit=5 olduqda total 6 (filtrdən sonrakı ümumi say), səhifədə 5 element, totalPages 2
tags: SC-029, P2, pos

* Dataset P ödəniş tarixçəsini yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "billerId" = "citynet"
* Query parametri elave et "limit" = "5"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "page" deyeri "1" beraberdir
* Json cavabında "limit" deyeri "5" beraberdir
* Json cavabında "total" deyeri "6" beraberdir
* Json cavabında "totalPages" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "5" olmalıdır
* Json cavabında "items.billerId" siyahısındakı bütün deyerler "citynet" olmalıdır

## TC_PAY_POS_062 · cardId={{cardB}} olduqda yalnız B kartının 2 ödənişi (Aztelekom) qaytarılır
tags: SC-029, P2, pos

* Dataset P ödəniş tarixçəsini yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "cardId" = "${cardB}"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "page" deyeri "1" beraberdir
* Json cavabında "limit" deyeri "10" beraberdir
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "totalPages" deyeri "1" beraberdir
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır
* Json cavabında "items.billerId" siyahısındakı bütün deyerler "aztelekom" olmalıdır

## TC_PAY_POS_063 · from = to = bu gün (Bakı vaxtı) olduqda bu günün bütün 18 ödənişi qaytarılır
tags: SC-029, P2, pos

* Dataset P ödəniş tarixçəsini yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "from" = "${today}"
* Query parametri elave et "to" = "${today}"
* Query parametri elave et "limit" = "50"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "page" deyeri "1" beraberdir
* Json cavabında "limit" deyeri "50" beraberdir
* Json cavabında "total" deyeri "18" beraberdir
* Json cavabında "totalPages" deyeri "1" beraberdir
* Json cavabında "items" massivinin ölçüsü "18" olmalıdır

## TC_PAY_EDGE_064 · from = sabah və ya to = dünən olduqda bu günün ödənişləri qaytarılmır (total 0)
tags: SC-029, P3, edge

* Dataset P ödəniş tarixçəsini yarat

Sorğu 1 — from = sabah:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "from" = "${tomorrow}"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir

Sorğu 2 — to = dünən:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "to" = "${yesterday}"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir

## TC_PAY_NEG_065 · Mövcud olmayan ay ilə tarix (from=2026-13-01) göndərildikdə 400 VALIDATION_ERROR qaytarılır
tags: SC-029, P2, neg

* Dataset P ödəniş tarixçəsini yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "from" = "2026-13-01"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir

## TC_PAY_EDGE_066 · Mövcud olmayan gün (from=2026-02-30) göndərildikdə 400 VALIDATION_ERROR qaytarılır
tags: SC-029, P3, edge

* Dataset P ödəniş tarixçəsini yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "from" = "2026-02-30"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir

## TC_PAY_NEG_067 · from > to (from = bu gün, to = dünən) olduqda 400 VALIDATION_ERROR qaytarılır
tags: SC-029, P2, neg

* Dataset P ödəniş tarixçəsini yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "from" = "${today}"
* Query parametri elave et "to" = "${yesterday}"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir

## TC_PAY_NEG_068 · Tarix YYYY-MM-DD formatında olmadıqda (from=11.10.2026) 400 VALIDATION_ERROR qaytarılır
tags: SC-029, P3, neg

* Dataset P ödəniş tarixçəsini yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "from" = "11.10.2026"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir

## TC_PAY_POS_069 · billerId, cardId və tarix filtrləri birlikdə olduqda yalnız bütün şərtlərə uyğun ödənişlər qaytarılır (AND)
tags: SC-029, P3, pos

* Dataset P ödəniş tarixçəsini yarat

Sorğu 1 — citynet + kart A + bu gün:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "billerId" = "citynet"
* Query parametri elave et "cardId" = "${cardA}"
* Query parametri elave et "from" = "${today}"
* Query parametri elave et "to" = "${today}"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "6" beraberdir
* Json cavabında "items.billerId" siyahısındakı bütün deyerler "citynet" olmalıdır

Sorğu 2 — citynet + kart B:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "billerId" = "citynet"
* Query parametri elave et "cardId" = "${cardB}"
* "GET" sorğusu gönder "/bill-payments"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
