# GRAD-102 · GET /beneficiaries — Axtarış, filtr, sıralama

EPIC-1 · Saxlanmış alıcılar.
Mənbə: Bank_API_QA_Project.xlsx → API Test Cases. Ssenari adı = test case ID-si + başlığı.
Spec-in əvvəlindəki context step hər ssenaridən əvvəl user1 ilə yeni, boş sandbox açır — ssenarilər bir-birindən asılı deyil.
Dataset A (8 alıcı) və Dataset B (5 alıcı) bank.cpt faylındakı concept-lərlə yaradılır.

tags: bank-api, epic-1, GRAD-102

* user1 olaraq yeni sandbox-da login ol

## TC_BEN_POS_042 · Parametrsiz sorğuda 200, total = items sayı və ən yeni əlavə edilən alıcı birinci qaytarılır
tags: SC-007, P1, pos, smoke

* Dataset A alıcılarını yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" deyerinin tipi "array" olmalıdır
* Json cavabında "total" deyeri "8" beraberdir
* Json cavabında "items" massivinin ölçüsü "8" olmalıdır
* Json cavabında "total" deyeri "8" beraberdir
* Json cavabını cedvel ile yoxla

   |path|value|
   |----|-----|
   |items[0].fullName|Kamal Nəsirov|
   |items[1].fullName|Qasım Əliyev|
   |items[2].fullName|Elvin Kərimov|
   |items[3].fullName|Xəyal Quliyev|
   |items[4].fullName|Çingiz Abbasov|
   |items[5].fullName|Əli Rzayev|
   |items[6].fullName|Zaur Həsənov|
   |items[7].fullName|Cavid Məmmədov|


## TC_BEN_POS_043 · Siyahıdakı hər alıcı POST cavabındakı bütün sahələrlə qaytarılır
tags: SC-007, P2, pos

* Dataset A alıcılarını yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" deyerinin tipi "array" olmalıdır
* Json cavabında "total" deyeri "8" beraberdir
* Json cavabında "items" massivinin ölçüsü "8" olmalıdır
* Cavab "bank/beneficiary-list.schema.json" JSON schema-sına uyğun olmalıdır

## TC_BEN_POS_044 · sort=fullName&order=asc olduqda adlar Azərbaycan əlifbası sırası ilə düzülür (Ç, Ə, X, Q öz yerində)
tags: SC-007, P2, pos

* Dataset A alıcılarını yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "sort" = "fullName"
* Query parametri elave et "order" = "asc"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" deyerinin tipi "array" olmalıdır
* Json cavabında "total" deyeri "8" beraberdir
* Json cavabını cedvel ile yoxla

   |path|value|
   |----|-----|
   |items[0].fullName|Cavid Məmmədov|
   |items[1].fullName|Çingiz Abbasov|
   |items[2].fullName|Elvin Kərimov|
   |items[3].fullName|Əli Rzayev|
   |items[4].fullName|Xəyal Quliyev|
   |items[5].fullName|Kamal Nəsirov|
   |items[6].fullName|Qasım Əliyev|
   |items[7].fullName|Zaur Həsənov|


## TC_BEN_POS_045 · sort=fullName&order=desc olduqda adlar Azərbaycan əlifbasının tərs sırası ilə düzülür
tags: SC-007, P3, pos

* Dataset A alıcılarını yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "sort" = "fullName"
* Query parametri elave et "order" = "desc"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" deyerinin tipi "array" olmalıdır
* Json cavabında "total" deyeri "8" beraberdir
* Json cavabını cedvel ile yoxla

   |path|value|
   |----|-----|
   |items[0].fullName|Zaur Həsənov|
   |items[1].fullName|Qasım Əliyev|
   |items[2].fullName|Kamal Nəsirov|
   |items[3].fullName|Xəyal Quliyev|
   |items[4].fullName|Əli Rzayev|
   |items[5].fullName|Elvin Kərimov|
   |items[6].fullName|Çingiz Abbasov|
   |items[7].fullName|Cavid Məmmədov|


## TC_BEN_POS_046 · sort=createdAt&order=asc olduqda ən köhnə alıcı birinci qaytarılır
tags: SC-007, P3, pos

* Dataset A alıcılarını yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "sort" = "createdAt"
* Query parametri elave et "order" = "asc"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" deyerinin tipi "array" olmalıdır
* Json cavabında "total" deyeri "8" beraberdir
* Json cavabını cedvel ile yoxla

   |path|value|
   |----|-----|
   |items[0].fullName|Cavid Məmmədov|
   |items[1].fullName|Zaur Həsənov|
   |items[2].fullName|Əli Rzayev|
   |items[3].fullName|Çingiz Abbasov|
   |items[4].fullName|Xəyal Quliyev|
   |items[5].fullName|Elvin Kərimov|
   |items[6].fullName|Qasım Əliyev|
   |items[7].fullName|Kamal Nəsirov|


## TC_BEN_POS_047 · Yalnız order=asc göndərildikdə defolt sort=createdAt tətbiq olunur (ən köhnə birinci)
tags: SC-007, P3, pos

* Dataset A alıcılarını yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "order" = "asc"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" deyerinin tipi "array" olmalıdır
* Json cavabında "total" deyeri "8" beraberdir
* Json cavabını cedvel ile yoxla

   |path|value|
   |----|-----|
   |items[0].fullName|Cavid Məmmədov|
   |items[1].fullName|Zaur Həsənov|
   |items[2].fullName|Əli Rzayev|
   |items[3].fullName|Çingiz Abbasov|
   |items[4].fullName|Xəyal Quliyev|
   |items[5].fullName|Elvin Kərimov|
   |items[6].fullName|Qasım Əliyev|
   |items[7].fullName|Kamal Nəsirov|


## TC_BEN_POS_048 · Yalnız sort=fullName göndərildikdə defolt order=desc tətbiq olunur
tags: SC-007, P3, pos

* Dataset A alıcılarını yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "sort" = "fullName"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" deyerinin tipi "array" olmalıdır
* Json cavabında "total" deyeri "8" beraberdir
* Json cavabını cedvel ile yoxla

   |path|value|
   |----|-----|
   |items[0].fullName|Zaur Həsənov|
   |items[1].fullName|Qasım Əliyev|
   |items[2].fullName|Kamal Nəsirov|
   |items[3].fullName|Xəyal Quliyev|
   |items[4].fullName|Əli Rzayev|
   |items[5].fullName|Elvin Kərimov|
   |items[6].fullName|Çingiz Abbasov|
   |items[7].fullName|Cavid Məmmədov|


## TC_BEN_POS_049 · q=nig olduqda adında "nig" olan bütün alıcılar (registrdən asılı olmayaraq) qaytarılır
tags: SC-008, P2, pos, smoke

* Dataset B alıcılarını yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "nig"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" deyerinin tipi "array" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır
* Json cavabında "items.fullName" deyerinde "Nigar Əliyeva" olmalıdır
* Json cavabında "items.fullName" deyerinde "Nigar Həsənova" olmalıdır

## TC_BEN_POS_050 · q=NİGAR (nöqtəli İ, böyük hərf) olduqda "Nigar" adlı alıcılar tapılır
tags: SC-008, P2, pos

* Dataset B alıcılarını yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "NİGAR"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" deyerinin tipi "array" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır
* Json cavabında "items.fullName" deyerinde "Nigar Əliyeva" olmalıdır
* Json cavabında "items.fullName" deyerinde "Nigar Həsənova" olmalıdır

## TC_BEN_POS_051 · q=NIGAR (nöqtəsiz I) olduqda da "Nigar" adlı alıcılar tapılır
tags: SC-008, P2, pos

* Dataset B alıcılarını yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "NIGAR"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" deyerinin tipi "array" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır
* Json cavabında "items.fullName" deyerinde "Nigar Əliyeva" olmalıdır
* Json cavabında "items.fullName" deyerinde "Nigar Həsənova" olmalıdır

## TC_BEN_POS_052 · q=ilkin (kiçik i) olduqda "İlkin Səfərov" tapılır
tags: SC-008, P3, pos

* Dataset B alıcılarını yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "ilkin"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" deyerinin tipi "array" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items" massivinin ölçüsü "1" olmalıdır
* Json cavabında "items.fullName" deyerinde "İlkin Səfərov" olmalıdır

## TC_BEN_POS_053 · q=işıl (nöqtəli i) olduqda nöqtəsiz I ilə yazılmış "Işıl Kərimova" tapılır
tags: SC-008, P3, pos

* Dataset B alıcılarını yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "işıl"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" deyerinin tipi "array" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items" massivinin ölçüsü "1" olmalıdır
* Json cavabında "items.fullName" deyerinde "Işıl Kərimova" olmalıdır

## TC_BEN_POS_054 · q ləqəbin bir hissəsi olduqda ("müəl" → "Müəllim") alıcı ləqəbə görə tapılır
tags: SC-008, P2, pos

* Dataset B alıcılarını yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "müəl"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" deyerinin tipi "array" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items" massivinin ölçüsü "1" olmalıdır
* Json cavabında "items.fullName" deyerinde "Ramin Quliyev" olmalıdır

## TC_BEN_POS_055 · Heç bir alıcıya uyğun gəlməyən q=zzz olduqda 200, total 0 və boş items qaytarılır
tags: SC-008, P2, pos

* Dataset B alıcılarını yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "zzz"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" deyerinin tipi "array" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır

## TC_BEN_BVA_056 · q 2 simvol (minimum sərhəd, "ra") olduqda qəbul edilir və uyğun alıcı qaytarılır
tags: SC-008, P2, bva

* Dataset B alıcılarını yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "ra"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" deyerinin tipi "array" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items" massivinin ölçüsü "1" olmalıdır
* Json cavabında "items.fullName" deyerinde "Ramin Quliyev" olmalıdır

## TC_BEN_EDGE_057 · q IBAN-ın hissəsi olduqda ("AZ10") nəticə qaytarılmır — axtarış yalnız ad və ləqəb üzrədir
tags: SC-008, P3, edge

Qeyd: gözlənilən nəticə Q-14 fərziyyəsinə əsaslanır (Grooming Questions).

* Dataset B alıcılarını yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "AZ10"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" deyerinin tipi "array" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır

## TC_BEN_POS_058 · currency=USD olduqda yalnız USD alıcılar qaytarılır və total onların sayına bərabərdir
tags: SC-009, P2, pos

* Dataset B alıcılarını yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "currency" = "USD"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" deyerinin tipi "array" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabında "items" massivinin ölçüsü "2" olmalıdır
* Json cavabında "items.fullName" deyerinde "İlkin Səfərov" olmalıdır
* Json cavabında "items.fullName" deyerinde "Nigar Həsənova" olmalıdır
* Json cavabında "items.currency" siyahısındakı bütün deyerler "USD" olmalıdır

## TC_BEN_POS_059 · q=nigar&currency=USD birlikdə olduqda yalnız hər iki şərtə uyğun alıcı qaytarılır (AND)
tags: SC-009, P2, pos

* Dataset B alıcılarını yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "nigar"
* Query parametri elave et "currency" = "USD"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" deyerinin tipi "array" olmalıdır
* Json cavabında "total" deyeri "1" beraberdir
* Json cavabında "items" massivinin ölçüsü "1" olmalıdır
* Json cavabında "items.fullName" deyerinde "Nigar Həsənova" olmalıdır
* Json cavabında "items.currency" siyahısındakı bütün deyerler "USD" olmalıdır

## TC_BEN_POS_060 · currency=AZN&sort=fullName&order=asc olduqda AZN alıcılar əlifba sırası ilə qaytarılır (Işıl Nigar-dan əvvəl)
tags: SC-009, P3, pos

* Dataset B alıcılarını yarat
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "currency" = "AZN"
* Query parametri elave et "sort" = "fullName"
* Query parametri elave et "order" = "asc"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" deyerinin tipi "array" olmalıdır
* Json cavabında "total" deyeri "2" beraberdir
* Json cavabını cedvel ile yoxla

   |path|value|
   |----|-----|
   |items[0].fullName|Işıl Kərimova|
   |items[1].fullName|Nigar Əliyeva|


## TC_BEN_EDGE_061 · user2 öz siyahısını istədikdə user1-in alıcıları görünmür
tags: SC-009, P1, edge

* Dataset B alıcılarını yarat
* user2 olaraq yeni sandbox-da login ol
* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" deyerinin tipi "array" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır

## TC_BEN_POS_062 · Alıcı olmadıqda (boş siyahı) 200, total 0 və boş items qaytarılır
tags: SC-010, P3, pos

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "200" olmalıdır
* Json cavabında "items" deyerinin tipi "array" olmalıdır
* Json cavabında "total" deyeri "0" beraberdir
* Json cavabında "items" massivinin ölçüsü "0" olmalıdır

## TC_BEN_BVA_063 · q 1 simvol (min − 1) olduqda 400 VALIDATION_ERROR, field "q" qaytarılır
tags: SC-010, P2, bva

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "a"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "q" olmalıdır
* Json cavabında "details.find { it.field == 'q' }.message" deyeri boş olmamalıdır

## TC_BEN_NEG_064 · currency icazəli siyahıda olmadıqda ("GBP") 400 VALIDATION_ERROR qaytarılır
tags: SC-010, P2, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "currency" = "GBP"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "currency" olmalıdır
* Json cavabında "details.find { it.field == 'currency' }.message" deyeri boş olmamalıdır

## TC_BEN_NEG_065 · sort icazəli dəyər olmadıqda ("iban") 400 VALIDATION_ERROR qaytarılır
tags: SC-010, P2, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "sort" = "iban"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "sort" olmalıdır
* Json cavabında "details.find { it.field == 'sort' }.message" deyeri boş olmamalıdır

## TC_BEN_NEG_066 · order icazəli dəyər olmadıqda ("up") 400 VALIDATION_ERROR qaytarılır
tags: SC-010, P3, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "order" = "up"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details.field" deyerinde "order" olmalıdır
* Json cavabında "details.find { it.field == 'order' }.message" deyeri boş olmamalıdır

## TC_BEN_NEG_067 · Dörd parametr eyni anda səhv olduqda details-də hər səhv parametr ayrıca qaytarılır
tags: SC-010, P3, neg

* Yeni API sorğusu hazırla
* Authorization header-ine tokeni elave et
* Query parametri elave et "q" = "a"
* Query parametri elave et "currency" = "GBP"
* Query parametri elave et "sort" = "iban"
* Query parametri elave et "order" = "up"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "400" olmalıdır
* Json cavabında "code" deyeri "VALIDATION_ERROR" beraberdir
* Json cavabında "details" massivinin ölçüsü "4" olmalıdır
* Json cavabında "details.field" deyerinde "q" olmalıdır
* Json cavabında "details.field" deyerinde "currency" olmalıdır
* Json cavabında "details.field" deyerinde "sort" olmalıdır
* Json cavabında "details.field" deyerinde "order" olmalıdır
* Json cavabında "details.field" siyahısındakı deyerler unikal olmalıdır

## TC_BEN_NEG_068 · Authorization header olmadıqda və ya saxta token göndərildikdə 401 qaytarılır
tags: SC-010, P1, neg, smoke


Sorğu 1 — token yoxdur:

* Yeni API sorğusu hazırla
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "401" olmalıdır

Sorğu 2 — saxta token:

* Yeni API sorğusu hazırla
* Bearer token elave et "fake.token.123"
* "GET" sorğusu gönder "/beneficiaries"
* Status kodunun "401" olmalıdır
