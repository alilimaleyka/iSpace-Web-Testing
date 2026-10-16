# GRAD-301 · GET /billers — Xidmət təchizatçıları kataloqu

EPIC-3 · Kommunal ödənişlər.
Mənbə: Bank_API_QA_Project.xlsx → API Test Cases. Ssenari adı = test case ID-si + başlığı.
Spec-in əvvəlindəki context step hər ssenaridən əvvəl user1 ilə yeni, boş sandbox açır — ssenarilər bir-birindən asılı deyil.

tags: bank-api, epic-3, GRAD-301

* user1 olaraq yeni sandbox-da login ol

## TC_PAY_POS_001 · Parametrsiz sorğuda 200, total 6 və hər təchizatçıda subscriberPattern, minAmount, maxAmount, fee qaytarılır
tags: SC-022, P2, pos, smoke

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/billers"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "6" beraberdir
* Json cavabında "items" massivinin ölçüsü "6" olmalıdır
* Json cavabında "items.id" deyerinde "azerisiq" olmalıdır
* Json cavabında "items.id" deyerinde "azersu" olmalıdır
* Json cavabında "items.id" deyerinde "azercell" olmalıdır
* Json cavabında "items.id" deyerinde "bakcell" olmalıdır
* Json cavabında "items.id" deyerinde "citynet" olmalıdır
* Json cavabında "items.id" deyerinde "aztelekom" olmalıdır
* Cavab "bank/billers.schema.json" JSON schema-sına uyğun olmalıdır

## TC_PAY_POS_002 · Hər təchizatçının kateqoriyası və məbləğ aralığı (minAmount–maxAmount) sənəddəki kataloqla eynidir
tags: SC-022, P2, pos

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/billers"
* Status kodunun "200" olmalıdır
* Json cavabını cedvel ile yoxla

   |path|value|
   |----|-----|
   |items.find { it.id == 'azerisiq' }.category|UTILITY|
   |items.find { it.id == 'azerisiq' }.minAmount|1|
   |items.find { it.id == 'azerisiq' }.maxAmount|500|
   |items.find { it.id == 'azersu' }.category|UTILITY|
   |items.find { it.id == 'azersu' }.minAmount|1|
   |items.find { it.id == 'azersu' }.maxAmount|300|
   |items.find { it.id == 'azercell' }.category|MOBILE|
   |items.find { it.id == 'azercell' }.minAmount|0.5|
   |items.find { it.id == 'azercell' }.maxAmount|200|
   |items.find { it.id == 'bakcell' }.category|MOBILE|
   |items.find { it.id == 'bakcell' }.minAmount|0.5|
   |items.find { it.id == 'bakcell' }.maxAmount|200|
   |items.find { it.id == 'citynet' }.category|INTERNET|
   |items.find { it.id == 'citynet' }.minAmount|5|
   |items.find { it.id == 'citynet' }.maxAmount|150|
   |items.find { it.id == 'aztelekom' }.category|INTERNET|
   |items.find { it.id == 'aztelekom' }.minAmount|2|
   |items.find { it.id == 'aztelekom' }.maxAmount|100|


## TC_PAY_POS_003 · Komissiya qaydası sənədə uyğundur: CityNet 1% (min 0.20, max 2.00), Aztelekom 0.50 sabit, digərlərində komissiya yoxdur
tags: SC-022, P2, pos

Qeyd: gözlənilən nəticə Q-28 fərziyyəsinə əsaslanır (Grooming Questions).

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/billers"
* Status kodunun "200" olmalıdır
* Json cavabını cedvel ile yoxla

   |path|value|
   |----|-----|
   |items.find { it.id == 'citynet' }.fee.type|PERCENT|
   |items.find { it.id == 'citynet' }.fee.value|1|
   |items.find { it.id == 'citynet' }.fee.min|0.2|
   |items.find { it.id == 'citynet' }.fee.max|2|

* Json cavabında "items.find { it.id == 'aztelekom' }.fee.value" deyeri "0.5" beraberdir
* Json cavabında "items.find { it.id == 'aztelekom' }.fee.type" deyeri "PERCENT" olmamalıdır
* Json cavabında "items.find { it.id == 'azerisiq' }.fee.type" deyeri "NONE" beraberdir
* Json cavabında "items.find { it.id == 'azersu' }.fee.type" deyeri "NONE" beraberdir
* Json cavabında "items.find { it.id == 'azercell' }.fee.type" deyeri "NONE" beraberdir
* Json cavabında "items.find { it.id == 'bakcell' }.fee.type" deyeri "NONE" beraberdir

## TC_PAY_POS_004 · Hər təchizatçının subscriberPattern regex-i sənəddəki formata uyğun nömrələri qəbul, uyğun olmayanları rədd edir
tags: SC-022, P2, pos

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/billers"
* Status kodunun "200" olmalıdır
* Json cavabında "items.find { it.id == 'azerisiq' }.subscriberPattern" regex-i "1234567890" deyerini qəbul etməlidir
* Json cavabında "items.find { it.id == 'azerisiq' }.subscriberPattern" regex-i "123456789" deyerini qəbul etməməlidir
* Json cavabında "items.find { it.id == 'azerisiq' }.subscriberPattern" regex-i "12345678901" deyerini qəbul etməməlidir
* Json cavabında "items.find { it.id == 'azerisiq' }.subscriberPattern" regex-i "123456789a" deyerini qəbul etməməlidir
* Json cavabında "items.find { it.id == 'azersu' }.subscriberPattern" regex-i "12345678" deyerini qəbul etməlidir
* Json cavabında "items.find { it.id == 'azersu' }.subscriberPattern" regex-i "1234567" deyerini qəbul etməməlidir
* Json cavabında "items.find { it.id == 'azersu' }.subscriberPattern" regex-i "123456789" deyerini qəbul etməməlidir
* Json cavabında "items.find { it.id == 'azercell' }.subscriberPattern" regex-i "501234567" deyerini qəbul etməlidir
* Json cavabında "items.find { it.id == 'azercell' }.subscriberPattern" regex-i "511234567" deyerini qəbul etməlidir
* Json cavabında "items.find { it.id == 'azercell' }.subscriberPattern" regex-i "101234567" deyerini qəbul etməlidir
* Json cavabında "items.find { it.id == 'azercell' }.subscriberPattern" regex-i "551234567" deyerini qəbul etməməlidir
* Json cavabında "items.find { it.id == 'azercell' }.subscriberPattern" regex-i "991234567" deyerini qəbul etməməlidir
* Json cavabında "items.find { it.id == 'azercell' }.subscriberPattern" regex-i "50123456" deyerini qəbul etməməlidir
* Json cavabında "items.find { it.id == 'bakcell' }.subscriberPattern" regex-i "551234567" deyerini qəbul etməlidir
* Json cavabında "items.find { it.id == 'bakcell' }.subscriberPattern" regex-i "991234567" deyerini qəbul etməlidir
* Json cavabında "items.find { it.id == 'bakcell' }.subscriberPattern" regex-i "501234567" deyerini qəbul etməməlidir
* Json cavabında "items.find { it.id == 'bakcell' }.subscriberPattern" regex-i "5512345678" deyerini qəbul etməməlidir
* Json cavabında "items.find { it.id == 'citynet' }.subscriberPattern" regex-i "CN123456" deyerini qəbul etməlidir
* Json cavabında "items.find { it.id == 'citynet' }.subscriberPattern" regex-i "CN12345" deyerini qəbul etməməlidir
* Json cavabında "items.find { it.id == 'citynet' }.subscriberPattern" regex-i "CN1234567" deyerini qəbul etməməlidir
* Json cavabında "items.find { it.id == 'citynet' }.subscriberPattern" regex-i "XN123456" deyerini qəbul etməməlidir
* Json cavabında "items.find { it.id == 'aztelekom' }.subscriberPattern" regex-i "1234567" deyerini qəbul etməlidir
* Json cavabında "items.find { it.id == 'aztelekom' }.subscriberPattern" regex-i "123456" deyerini qəbul etməməlidir
* Json cavabında "items.find { it.id == 'aztelekom' }.subscriberPattern" regex-i "12345678" deyerini qəbul etməməlidir

## TC_PAY_POS_005 · category=MOBILE olduqda yalnız Azercell və Bakcell qaytarılır
tags: SC-022, P2, pos

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "category" = "MOBILE"
* "GET" sorğusu gönder "/billers"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır
* Json cavabında "items.id" deyerinde "azercell" olmalıdır
* Json cavabında "items.id" deyerinde "bakcell" olmalıdır

## TC_PAY_POS_006 · category=UTILITY və category=INTERNET olduqda yalnız həmin kateqoriyanın 2 təchizatçısı qaytarılır
tags: SC-022, P3, pos


Sorğu 1 — UTILITY:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "category" = "UTILITY"
* "GET" sorğusu gönder "/billers"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır
* Json cavabında "items.id" deyerinde "azerisiq" olmalıdır
* Json cavabında "items.id" deyerinde "azersu" olmalıdır

Sorğu 2 — INTERNET:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "category" = "INTERNET"
* "GET" sorğusu gönder "/billers"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır
* Json cavabında "items.id" deyerinde "aztelekom" olmalıdır
* Json cavabında "items.id" deyerinde "citynet" olmalıdır

## TC_PAY_NEG_007 · category icazəli dəyər olmadıqda ("GAS") 400 VALIDATION_ERROR qaytarılır
tags: SC-022, P2, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "category" = "GAS"
* "GET" sorğusu gönder "/billers"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "category" olmalıdır

## TC_PAY_NEG_008 · category kiçik hərflə ("mobile") göndərildikdə 400 VALIDATION_ERROR qaytarılır
tags: SC-022, P4, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "category" = "mobile"
* "GET" sorğusu gönder "/billers"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir

## TC_PAY_NEG_009 · Token olmadan və ya saxta tokenlə kataloq istədikdə 401 qaytarılır
tags: SC-022, P2, neg


Sorğu 1 — token yoxdur:

* Yeni API sorğusu hazırla
* "GET" sorğusu gönder "/billers"
* Status kodunun "401" olmalıdır

Sorğu 2 — saxta token:

* Yeni API sorğusu hazırla
* Bearer token elave et "fake.token.123"
* "GET" sorğusu gönder "/billers"
* Status kodunun "401" olmalıdır
