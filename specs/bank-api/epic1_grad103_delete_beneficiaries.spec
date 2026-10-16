# GRAD-103 · DELETE /beneficiaries/{id} — Alıcını silmək

EPIC-1 · Saxlanmış alıcılar.
Mənbə: Bank_API_QA_Project.xlsx → API Test Cases. Ssenari adı = test case ID-si + başlığı.
Spec-in əvvəlindəki context step hər ssenaridən əvvəl user1 ilə yeni, boş sandbox açır — ssenarilər bir-birindən asılı deyil.

tags: bank-api, epic-1, GRAD-103

* user1 olaraq yeni sandbox-da login ol

## TC_BEN_POS_069 · Mövcud alıcı silindikdə 204 No Content və boş body qaytarılır
tags: SC-011, P1, pos, smoke

* "bank/ben/TC_BEN_POS_069.json" faylı ile alıcı yarat ve id-ni "delId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "DELETE" sorğusu gönder "/beneficiaries/${delId}"
* Status kodunun "204" olmalıdır
* Cavab body-si boş olmalıdır

## TC_BEN_POS_070 · Silinmiş alıcı GET /beneficiaries siyahısında olmur və total 1 azalır
tags: SC-011, P1, pos

* "bank/ben/TC_BEN_POS_070.json" faylı ile alıcı yarat ve id-ni "delId" olaraq yadda saxla

Silmədən əvvəl: N = 1

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items.id" deyerinde "${delId}" olmalıdır
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "DELETE" sorğusu gönder "/beneficiaries/${delId}"
* Status kodunun "204" olmalıdır

Silmədən sonra: N − 1 = 0

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır

## TC_BEN_NEG_071 · Artıq silinmiş alıcı eyni id ilə ikinci dəfə silindikdə 404 NOT_FOUND qaytarılır
tags: SC-011, P2, neg

* "bank/ben/TC_BEN_NEG_071.json" faylı ile alıcı yarat ve id-ni "delId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "DELETE" sorğusu gönder "/beneficiaries/${delId}"
* Status kodunun "204" olmalıdır

Eyni id ilə ikinci silmə:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "DELETE" sorğusu gönder "/beneficiaries/${delId}"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC_BEN_EDGE_072 · Silinmiş alıcının IBAN-ı yenidən əlavə edildikdə 201 qaytarılır (409 BENEFICIARY_EXISTS yox)
tags: SC-011, P3, edge

Qeyd: gözlənilən nəticə Q-09 fərziyyəsinə əsaslanır (Grooming Questions).

* "bank/ben/TC_BEN_EDGE_072.json" faylı ile alıcı yarat ve id-ni "delId" olaraq yadda saxla
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "DELETE" sorğusu gönder "/beneficiaries/${delId}"
* Status kodunun "204" olmalıdır

Eyni IBAN ilə yenidən əlavə:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_EDGE_072.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "201" olmalıdır

## TC_BEN_EDGE_073 · Siyahı dolu (10) olduqda bir alıcı silinəndən sonra yeni alıcı əlavə edilə bilir
tags: SC-011, P2, edge

Qeyd: gözlənilən nəticə Q-09 fərziyyəsinə əsaslanır (Grooming Questions).

* Alıcılar siyahısını 10 alıcı ile doldur
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "DELETE" sorğusu gönder "/beneficiaries/${ilkAliciId}"
* Status kodunun "204" olmalıdır

Limitdə yer boşaldı — yeni alıcı:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_EDGE_073.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "201" olmalıdır

## TC_BEN_NEG_074 · Mövcud olmayan, düzgün formatlı id (ben_zzzzzzzz) silinmək istədikdə 404 NOT_FOUND qaytarılır
tags: SC-012, P2, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "DELETE" sorğusu gönder "/beneficiaries/ben_zzzzzzzz"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC_BEN_NEG_075 · Formatı səhv olan id ("abc") ilə silmə sorğusunda 404 NOT_FOUND qaytarılır
tags: SC-012, P3, neg

Qeyd: gözlənilən nəticə Q-16 fərziyyəsinə əsaslanır (Grooming Questions).

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "DELETE" sorğusu gönder "/beneficiaries/abc"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC_BEN_EDGE_076 · user2 user1-in alıcısını silməyə çalışdıqda 404 NOT_FOUND qaytarılır (403 yox)
tags: SC-012, P1, edge, smoke

* "bank/ben/TC_BEN_EDGE_076.json" faylı ile alıcı yarat ve id-ni "delId" olaraq yadda saxla
* "user1Token" deyişenine "${token}" deyerini ver
* user2 olaraq yeni sandbox-da login ol

user2 user1-in alıcısını silməyə çalışır:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "DELETE" sorğusu gönder "/beneficiaries/${delId}"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

## TC_BEN_EDGE_077 · user2-nin uğursuz silmə cəhdindən sonra user1-in alıcısı siyahıda qalır
tags: SC-012, P2, edge

* "bank/ben/TC_BEN_EDGE_077.json" faylı ile alıcı yarat ve id-ni "delId" olaraq yadda saxla
* "user1Token" deyişenine "${token}" deyerini ver
* user2 olaraq yeni sandbox-da login ol

user2 user1-in alıcısını silməyə çalışır:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "DELETE" sorğusu gönder "/beneficiaries/${delId}"
* Status kodunun "404" olmalıdır
* Json cavabında "code" deyeri "NOT_FOUND" beraberdir

user1-in siyahısı yoxlanılır:

* Yeni API sorğusu hazırla
* Bearer token elave et "${user1Token}"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items.id" deyerinde "${delId}" olmalıdır

## TC_BEN_NEG_078 · Authorization header olmadıqda və ya saxta token göndərildikdə 401 qaytarılır və alıcı silinmir
tags: SC-012, P1, neg

* "bank/ben/TC_BEN_NEG_078.json" faylı ile alıcı yarat ve id-ni "delId" olaraq yadda saxla

Sorğu 1 — token yoxdur:

* Yeni API sorğusu hazırla
* "DELETE" sorğusu gönder "/beneficiaries/${delId}"
* Status kodunun "401" olmalıdır

Sorğu 2 — saxta token:

* Yeni API sorğusu hazırla
* Bearer token elave et "fake.token.123"
* "DELETE" sorğusu gönder "/beneficiaries/${delId}"
* Status kodunun "401" olmalıdır

Alıcı silinməyib:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items.id" deyerinde "${delId}" olmalıdır

## TC_BEN_EDGE_079 · Token olmadıqda mövcud olmayan id üçün də 401 qaytarılır (404 yox)
tags: SC-012, P4, edge

* Yeni API sorğusu hazırla
* "DELETE" sorğusu gönder "/beneficiaries/ben_zzzzzzzz"
* Status kodunun "401" olmalıdır
