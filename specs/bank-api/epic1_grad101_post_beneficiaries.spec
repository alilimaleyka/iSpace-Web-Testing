# GRAD-101 · POST /beneficiaries — Yeni alıcı əlavə etmək

EPIC-1 · Saxlanmış alıcılar.
Mənbə: Bank_API_QA_Project.xlsx → API Test Cases. Ssenari adı = test case ID-si + başlığı.
Spec-in əvvəlindəki context step hər ssenaridən əvvəl user1 ilə yeni, boş sandbox açır — ssenarilər bir-birindən asılı deyil.

tags: bank-api, epic-1, GRAD-101

* user1 olaraq yeni sandbox-da login ol

## TC_BEN_POS_001 · Bütün sahələr etibarlı olduqda alıcı yaradılır: 201, cavabda bütün sahələr və Location header qaytarılır
tags: SC-001, P1, pos, smoke

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_POS_001.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "201" olmalıdır
* Cavab "bank/beneficiary.schema.json" JSON schema-sına uyğun olmalıdır
* Json cavabında "id" deyeri "^ben_[A-Za-z0-9]{8}$" regex-ine uyğun olmalıdır
* Json cavabında "id" deyerini "benId" olaraq yadda saxla
* Header "Location" deyerinde "/beneficiaries/${benId}" olmalıdır
* Json cavabında "createdAt" deyeri "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}([.][0-9]{3})?Z$" regex-ine uyğun olmalıdır
* Json cavabında "fullName" deyeri "bank/ben/TC_BEN_POS_001.json" request body-sindeki "fullName" ile eyni olmalıdır
* Json cavabında "iban" deyeri "bank/ben/TC_BEN_POS_001.json" request body-sindeki "iban" ile eyni olmalıdır
* Json cavabında "currency" deyeri "bank/ben/TC_BEN_POS_001.json" request body-sindeki "currency" ile eyni olmalıdır
* Json cavabında "nickname" deyeri "bank/ben/TC_BEN_POS_001.json" request body-sindeki "nickname" ile eyni olmalıdır

## TC_BEN_POS_002 · IBAN boşluqlu və kiçik hərflə göndərildikdə boşluqsuz və böyük hərflə saxlanılır
tags: SC-001, P1, pos

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_POS_002.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "201" olmalıdır
* Cavab "bank/beneficiary.schema.json" JSON schema-sına uyğun olmalıdır
* Json cavabında "iban" deyeri "AZ77AIIB40060019440123456789" beraberdir

## TC_BEN_POS_003 · Cavabdakı ibanMasked IBAN-ın yalnız ilk 4 və son 4 simvolunu göstərir
tags: SC-001, P2, pos

Qeyd: gözlənilən nəticə Q-01 fərziyyəsinə əsaslanır (Grooming Questions).

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_POS_003.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "201" olmalıdır
* Cavab "bank/beneficiary.schema.json" JSON schema-sına uyğun olmalıdır
* Json cavabında "ibanMasked" deyeri "^AZ55[^0-9]*4455$" regex-ine uyğun olmalıdır
* Json cavabında "ibanMasked" deyeri "AZ55 **** **** **** **** 4455" beraberdir

## TC_BEN_POS_004 · nickname göndərilmədikdə alıcı yaradılır və cavabda "nickname": null qaytarılır
tags: SC-001, P2, pos

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_POS_004.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "201" olmalıdır
* Cavab "bank/beneficiary.schema.json" JSON schema-sına uyğun olmalıdır
* Json cavabında "nickname" açarı mövcud olmalıdır
* Json cavabında "nickname" deyeri null olmalıdır

## TC_BEN_POS_005 · currency USD və EUR olduqda alıcı yaradılır və valyuta cavabda eynilə qaytarılır
tags: SC-001, P2, pos


Sorğu 1 — USD:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_POS_005_1.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "201" olmalıdır
* Cavab "bank/beneficiary.schema.json" JSON schema-sına uyğun olmalıdır
* Json cavabında "currency" deyeri "USD" beraberdir

Sorğu 2 — EUR:

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_POS_005_2.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "201" olmalıdır
* Cavab "bank/beneficiary.schema.json" JSON schema-sına uyğun olmalıdır
* Json cavabında "currency" deyeri "EUR" beraberdir

## TC_BEN_BVA_006 · fullName 2 simvol (aşağı sərhəd) olduqda qəbul edilir
tags: SC-002, P2, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_BVA_006.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "201" olmalıdır
* Cavab "bank/beneficiary.schema.json" JSON schema-sına uyğun olmalıdır
* Json cavabında "fullName" deyeri "Al" beraberdir

## TC_BEN_BVA_007 · fullName 50 simvol (yuxarı sərhəd) olduqda qəbul edilir
tags: SC-002, P2, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_BVA_007.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "201" olmalıdır
* Cavab "bank/beneficiary.schema.json" JSON schema-sına uyğun olmalıdır
* Json cavabında "fullName" deyeri "Abbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb" beraberdir

## TC_BEN_BVA_008 · fullName 1 simvol (min − 1) olduqda 400 VALIDATION_ERROR qaytarılır
tags: SC-002, P2, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_BVA_008.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "fullName" olmalıdır
* Json cavabında "details.find { it.field == 'fullName' }.message" deyeri boş olmamalıdır

## TC_BEN_BVA_009 · fullName 51 simvol (max + 1) olduqda 400 VALIDATION_ERROR qaytarılır
tags: SC-002, P2, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_BVA_009.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "fullName" olmalıdır
* Json cavabında "details.find { it.field == 'fullName' }.message" deyeri boş olmamalıdır

## TC_BEN_BVA_010 · fullName trim-dən sonra 1 simvol qaldıqda (" A ") 400 VALIDATION_ERROR qaytarılır
tags: SC-002, P3, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_BVA_010.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "fullName" olmalıdır
* Json cavabında "details.find { it.field == 'fullName' }.message" deyeri boş olmamalıdır

## TC_BEN_POS_011 · fullName Azərbaycan hərfləri, boşluq, defis və apostrof olduqda qəbul edilir
tags: SC-002, P2, pos

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_POS_011.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "201" olmalıdır
* Cavab "bank/beneficiary.schema.json" JSON schema-sına uyğun olmalıdır
* Json cavabında "fullName" deyeri "Şəhla Qasımova-O'Neil" beraberdir

## TC_BEN_NEG_012 · fullName hərflə başlamadıqda ("---") 400 VALIDATION_ERROR qaytarılır
tags: SC-002, P2, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_NEG_012.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "fullName" olmalıdır
* Json cavabında "details.find { it.field == 'fullName' }.message" deyeri boş olmamalıdır

## TC_BEN_NEG_013 · fullName rəqəm olduqda ("Ali2") 400 VALIDATION_ERROR qaytarılır
tags: SC-002, P2, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_NEG_013.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "fullName" olmalıdır
* Json cavabında "details.find { it.field == 'fullName' }.message" deyeri boş olmamalıdır

## TC_BEN_NEG_014 · fullName icazəsiz xüsusi simvol olduqda ("Ali@") 400 VALIDATION_ERROR qaytarılır
tags: SC-002, P3, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_NEG_014.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "fullName" olmalıdır
* Json cavabında "details.find { it.field == 'fullName' }.message" deyeri boş olmamalıdır

## TC_BEN_NEG_015 · fullName göndərilmədikdə (məcburi sahə yoxdur) 400 VALIDATION_ERROR qaytarılır
tags: SC-002, P2, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_NEG_015.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "fullName" olmalıdır
* Json cavabında "details.find { it.field == 'fullName' }.message" deyeri boş olmamalıdır

## TC_BEN_BVA_016 · IBAN 27 simvol (28 − 1) olduqda 400 VALIDATION_ERROR qaytarılır
tags: SC-003, P2, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_BVA_016.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "iban" olmalıdır
* Json cavabında "details.find { it.field == 'iban' }.message" deyeri boş olmamalıdır

## TC_BEN_BVA_017 · IBAN 29 simvol (28 + 1) olduqda 400 VALIDATION_ERROR qaytarılır
tags: SC-003, P2, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_BVA_017.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "iban" olmalıdır
* Json cavabında "details.find { it.field == 'iban' }.message" deyeri boş olmamalıdır

## TC_BEN_NEG_018 · IBAN 'AZ' ilə başlamadıqda (TR, 28 simvol) 400 VALIDATION_ERROR qaytarılır
tags: SC-003, P2, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_NEG_018.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "iban" olmalıdır
* Json cavabında "details.find { it.field == 'iban' }.message" deyeri boş olmamalıdır

## TC_BEN_NEG_019 · IBAN-da bank kodu (5–8-ci simvollar) hərf əvəzinə rəqəm olduqda 400 VALIDATION_ERROR qaytarılır
tags: SC-003, P3, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_NEG_019.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "iban" olmalıdır
* Json cavabında "details.find { it.field == 'iban' }.message" deyeri boş olmamalıdır

## TC_BEN_NEG_020 · IBAN-da icazəsiz simvol ('#') olduqda 400 VALIDATION_ERROR qaytarılır
tags: SC-003, P3, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_NEG_020.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "iban" olmalıdır
* Json cavabında "details.find { it.field == 'iban' }.message" deyeri boş olmamalıdır

## TC_BEN_NEG_021 · currency icazəli siyahıda olmadıqda ("GBP") 400 VALIDATION_ERROR qaytarılır
tags: SC-004, P2, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_NEG_021.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "currency" olmalıdır
* Json cavabında "details.find { it.field == 'currency' }.message" deyeri boş olmamalıdır

## TC_BEN_NEG_022 · currency kiçik hərflə ("azn") göndərildikdə 400 VALIDATION_ERROR qaytarılır
tags: SC-004, P3, neg

Qeyd: gözlənilən nəticə Q-05 fərziyyəsinə əsaslanır (Grooming Questions).

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_NEG_022.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "currency" olmalıdır
* Json cavabında "details.find { it.field == 'currency' }.message" deyeri boş olmamalıdır

## TC_BEN_BVA_023 · nickname 20 simvol (yuxarı sərhəd) olduqda qəbul edilir
tags: SC-004, P3, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_BVA_023.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "201" olmalıdır
* Cavab "bank/beneficiary.schema.json" JSON schema-sına uyğun olmalıdır
* Json cavabında "nickname" deyeri "NNNNNNNNNNNNNNNNNNNN" beraberdir

## TC_BEN_BVA_024 · nickname 21 simvol (max + 1) olduqda 400 VALIDATION_ERROR qaytarılır
tags: SC-004, P3, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_BVA_024.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "nickname" olmalıdır
* Json cavabında "details.find { it.field == 'nickname' }.message" deyeri boş olmamalıdır

## TC_BEN_BVA_025 · nickname boş string ("", 0 simvol = min − 1) olduqda 400 VALIDATION_ERROR qaytarılır
tags: SC-004, P3, bva

Qeyd: gözlənilən nəticə Q-04 fərziyyəsinə əsaslanır (Grooming Questions).

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_BVA_025.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "nickname" olmalıdır
* Json cavabında "details.find { it.field == 'nickname' }.message" deyeri boş olmamalıdır

## TC_BEN_NEG_026 · Üç sahə eyni anda səhv olduqda details-də hər səhv sahə ayrıca qaytarılır
tags: SC-004, P2, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_NEG_026.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "3" olmalıdır
* Json cavabında "details.field" deyerinde "fullName" olmalıdır
* Json cavabında "details.field" deyerinde "iban" olmalıdır
* Json cavabında "details.field" deyerinde "currency" olmalıdır
* Json cavabında "details.field" siyahısındakı deyerler unikal olmalıdır

## TC_BEN_NEG_027 · Authorization header olmadıqda və ya saxta token göndərildikdə 401 qaytarılır
tags: SC-005, P1, neg, smoke


Sorğu 1 — token yoxdur:

* Yeni API sorğusu hazırla
* Body olaraq "bank/ben/TC_BEN_NEG_027_1.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "401" olmalıdır

Sorğu 2 — saxta token:

* Yeni API sorğusu hazırla
* Bearer token elave et "fake.token.123"
* Body olaraq "bank/ben/TC_BEN_NEG_027_2.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "401" olmalıdır

## TC_BEN_NEG_028 · Body sintaktik cəhətdən etibarsız JSON olduqda 400 INVALID_JSON qaytarılır
tags: SC-005, P2, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_NEG_028.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "INVALID_JSON" beraberdir

## TC_BEN_NEG_029 · Body JSON obyekti deyil, massiv olduqda 400 INVALID_JSON qaytarılır
tags: SC-005, P3, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_NEG_029.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "INVALID_JSON" beraberdir

## TC_BEN_EDGE_030 · Öz IBAN-ı ilə birlikdə fullName də səhv olduqda 400 VALIDATION_ERROR qaytarılır (422 OWN_ACCOUNT deyil)
tags: SC-005, P3, edge

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_EDGE_030.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "fullName" olmalıdır
* Json cavabında "details.find { it.field == 'fullName' }.message" deyeri boş olmamalıdır

## TC_BEN_EDGE_031 · Həm IBAN, həm də ləqəb artıq mövcud olduqda 409 BENEFICIARY_EXISTS qaytarılır (NICKNAME_TAKEN deyil)
tags: SC-005, P3, edge

* "bank/ben/TC_BEN_EDGE_031_on-sert1.json" faylı ile alıcı yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_EDGE_031.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "BENEFICIARY_EXISTS" beraberdir

## TC_BEN_EDGE_032 · Token olmadıqda və body etibarsız JSON olduqda 401 qaytarılır (400 INVALID_JSON deyil)
tags: SC-005, P4, edge

* Yeni API sorğusu hazırla
* Body olaraq "bank/ben/TC_BEN_EDGE_032.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "401" olmalıdır

## TC_BEN_NEG_033 · Eyni IBAN ikinci dəfə göndərildikdə 409 BENEFICIARY_EXISTS qaytarılır
tags: SC-006, P1, neg, smoke

* "bank/ben/TC_BEN_NEG_033_on-sert1.json" faylı ile alıcı yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_NEG_033.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "BENEFICIARY_EXISTS" beraberdir

## TC_BEN_NEG_034 · Mövcud IBAN boşluqlu və kiçik hərflə yenidən göndərildikdə 409 BENEFICIARY_EXISTS qaytarılır
tags: SC-006, P2, neg

* "bank/ben/TC_BEN_NEG_034_on-sert1.json" faylı ile alıcı yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_NEG_034.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "BENEFICIARY_EXISTS" beraberdir

## TC_BEN_NEG_035 · Mövcud ləqəb fərqli registrdə ("anam" → "ANAM") göndərildikdə 409 NICKNAME_TAKEN qaytarılır
tags: SC-006, P2, neg

* "bank/ben/TC_BEN_NEG_035_on-sert1.json" faylı ile alıcı yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_NEG_035.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "NICKNAME_TAKEN" beraberdir

## TC_BEN_NEG_036 · user1 öz hesabının IBAN-ını göndərdikdə 422 OWN_ACCOUNT qaytarılır
tags: SC-006, P1, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_NEG_036.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "OWN_ACCOUNT" beraberdir

## TC_BEN_NEG_037 · Öz IBAN-ı boşluqlu və kiçik hərflə göndərildikdə də 422 OWN_ACCOUNT qaytarılır
tags: SC-006, P2, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_NEG_037.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "OWN_ACCOUNT" beraberdir

## TC_BEN_POS_038 · user1 başqa istifadəçinin (admin) hesab IBAN-ını əlavə etdikdə alıcı yaradılır
tags: SC-006, P3, pos

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_POS_038.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "201" olmalıdır
* Cavab "bank/beneficiary.schema.json" JSON schema-sına uyğun olmalıdır
* Json cavabında "iban" deyeri "AZ21NABZ00000000137010001944" beraberdir

## TC_BEN_EDGE_039 · user1-in siyahısında olan IBAN-ı user2 öz siyahısına əlavə edə bilir (təkrar yoxlaması istifadəçi üzrədir)
tags: SC-006, P3, edge

Qeyd: gözlənilən nəticə Q-08 fərziyyəsinə əsaslanır (Grooming Questions).

* "bank/ben/TC_BEN_EDGE_039_on-sert1.json" faylı ile alıcı yarat
* user2 olaraq yeni sandbox-da login ol
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_EDGE_039.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "201" olmalıdır
* Cavab "bank/beneficiary.schema.json" JSON schema-sına uyğun olmalıdır

## TC_BEN_BVA_040 · Siyahıda 10 alıcı olduqda 11-ci alıcı üçün 422 LIMIT_REACHED və "limit": 10 qaytarılır
tags: SC-006, P1, bva

* Alıcılar siyahısını 10 alıcı ile doldur
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_BVA_040.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "422" olmalıdır
* Json cavabında "code" deyeri "LIMIT_REACHED" beraberdir
* Json cavabında "limit" deyeri "10" beraberdir

## TC_BEN_EDGE_041 · Siyahı dolu (10) olduqda mövcud IBAN göndərildikdə 409 BENEFICIARY_EXISTS qaytarılır (LIMIT_REACHED deyil)
tags: SC-006, P3, edge

* Alıcılar siyahısını 10 alıcı ile doldur
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Body olaraq "bank/ben/TC_BEN_EDGE_041.json" faylını elave et
* "POST" sorğusu gönder "/beneficiaries"
* Status kodunun "409" olmalıdır
* Json cavabında "code" deyeri "BENEFICIARY_EXISTS" beraberdir
