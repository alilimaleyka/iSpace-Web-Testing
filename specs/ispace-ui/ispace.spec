# iSpace UI Testleri

Test mühiti: https://ispace.az

## TC_SRCH_POS_001 Model adı ilə axtarış uyğun nəticələr qaytarır
tags: regression, axtaris

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "Search Input" görsensin deye maksimum "15" saniye gözle
* "Search Input" elementine "iPhone 17" yaz ve Enter düymesine bas
* URL "search?query=" içermelidir
* "Search Result Title" görsensin deye maksimum "15" saniye gözle
* "Search Result Title" elementinin metni "Axtarış nəticələri" olmalıdır
* "Search Result Product Name" elementlerinin sayı en az "1" olmalıdır
* "Search Result Product Name" elementin içinde "iPhone 17" yazısı var
* Brauzeri bağla

## TC_PLP_POS_001 iPhone kateqoriyası açıldıqda başlıq, breadcrumb, məhsul sayı və kartlar göstərilir
tags: smoke, listing

* "chrome" brauzeri aç ve keçid et "https://ispace.az/category/iphone"
* Cookie bildirişini rədd et
* "Category Title" görsensin deye maksimum "15" saniye gözle
* "Category Title" elementinin metni "iPhone" olmalıdır
* "Breadcrumb" elementin içinde "Ana səhifə" yazısı var
* "Breadcrumb" elementin içinde "iPhone" yazısı var
* "Product Count" elementin içinde "Məhsul" yazısı var
* "Product Card Name" elementlerinin sayı en az "1" olmalıdır
* Brauzeri bağla

## TC_PDP_POS_001 Stokda olan məhsulun səhifəsində ad, kod, qiymət, aylıq ödəniş və düymələr göstərilir
tags: smoke, pdp

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/iphone?filter_stock=1" siyahısından stokda olan ilk məhsulu aç
* "Product Title" görsensin deye maksimum "15" saniye gözle
* "Product Title" elementin içinde "iPhone" yazısı var
* "Product SKU" elementin içinde "SKU" yazısı var
* "Product Price" elementin içinde "₼" yazısı var
* "Product Monthly Payment" elementin içinde "ay" yazısı var
* "Breadcrumb" elementin içinde "iPhone" yazısı var
* "Add To Cart Button" görünür olmalıdır
* "Add To Cart Button" elementinin metni "Səbətə" olmalıdır
* "One Click Buy Button" görünür olmalıdır
* Brauzeri bağla

## TC_CART_POS_001 Məhsul PDP-dən səbətə əlavə olunur
tags: smoke, sebet

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/iphone?filter_stock=1" siyahısından stokda olan ilk məhsulu aç
* "Product Title" elementinin metnini "pdpAd" olaraq yadda saxla
* "Product Price" elementinin metnini "pdpQiymet" olaraq yadda saxla
* Açıq məhsulu səbətə əlavə et
* "Added To Cart Popup Title" elementin içinde "səbətə əlavə edildi" yazısı var
* "Cart Counter" elementinin metni "1" olmalıdır
* "View Cart Button" elementine klik et
* URL "/cart" içermelidir
* "Cart Item Name" görsensin deye maksimum "15" saniye gözle
* "Cart Item Name" elementin içinde "${pdpAd}" yazısı var
* "Cart Item Quantity" input deyeri "1" olmalıdır
* "Cart Item Price" elementinin metni "${pdpQiymet}" olmalıdır
* "Cart Total" elementinin metni "${pdpQiymet}" olmalıdır
* Brauzeri bağla

## TC_CART_POS_003 Eyni məhsul iki dəfə əlavə edildikdə bir sətirdə miqdar 2 və cəm qiymət × 2 olur
tags: regression, sebet

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/iphone?filter_stock=1" siyahısından stokda olan ilk məhsulu aç
* "Product Price" elementinin metnini "pdpQiymet" olaraq yadda saxla
* Açıq məhsulu səbətə əlavə et
* "Close Cart Popup Button" elementine klik et
* "Added To Cart Popup Title" yox olana qeder maksimum "10" saniye gözle
* "Add To Cart Button" elementine klik et
* "Added To Cart Popup Title" görsensin deye maksimum "10" saniye gözle
* "Cart Counter" elementinin metni "2" olmalıdır
* "View Cart Button" elementine klik et
* "Cart Item Name" görsensin deye maksimum "15" saniye gözle
* "Cart Item Name" elementlerinin sayı "1" olmalıdır
* "Cart Item Quantity" input deyeri "2" olmalıdır
* "Cart Item Price" qiyməti "${pdpQiymet}" qiymətinin "2" mislinə bərabər olmalıdır
* "Cart Total" qiyməti "${pdpQiymet}" qiymətinin "2" mislinə bərabər olmalıdır
* Brauzeri bağla

## TC_CART_POS_004 İki fərqli məhsul olduqda Cəmi sətir məbləğlərinin cəminə bərabərdir
tags: regression, sebet

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* Səbətə iki fərqli məhsul əlavə et və səbəti aç
* "Cart Counter" elementinin metni "2" olmalıdır
* "Cart Item Name" elementlerinin sayı "2" olmalıdır
* Sehifede "${qiymetA}" yazısı olmalıdır
* Sehifede "${qiymetB}" yazısı olmalıdır
* "Cart Item Price" qiymətlərinin cəmi "Cart Total" qiymətinə bərabər olmalıdır
* Brauzeri bağla

## TC_CART_POS_007 Məhsul səbətdən silinir
tags: regression, sebet

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* Səbətə iki fərqli məhsul əlavə et və səbəti aç
* "Cart Item Name" elementlerinin sayı "2" olmalıdır
* "Cart Remove Button" elementine klik et
* "Cart Item Name" elementlerinin sayı "1" olmalıdır
* "Cart Item Price" elementinin metnini "qalanQiymet" olaraq yadda saxla
* "Cart Total" elementinin metni "${qalanQiymet}" olmalıdır
* "Cart Counter" elementinin metni "1" olmalıdır
* Brauzeri bağla

## TC_CART_POS_010 Səbət səhifə yenilənəndə və yeni tabda qorunur
tags: regression, sebet

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/airpods?filter_stock=1" siyahısından stokda olan ilk məhsulu səbətə əlavə et və qiymətini "qiymet" olaraq yadda saxla
* "View Cart Button" elementine klik et
* "Cart Item Name" görsensin deye maksimum "15" saniye gözle
* "Cart Item Name" elementinin metnini "ad" olaraq yadda saxla
* "Cart Item Quantity" elementinin "value" atributunu "miqdar" olaraq yadda saxla
* "Cart Total" elementinin metnini "cem" olaraq yadda saxla
* Sehifeni yenile
* "Cart Item Name" görsensin deye maksimum "15" saniye gözle
* "Cart Item Name" elementinin metni "${ad}" olmalıdır
* "Cart Item Quantity" input deyeri "${miqdar}" olmalıdır
* "Cart Total" elementinin metni "${cem}" olmalıdır
* Yeni tabda "https://ispace.az/cart" aç
* "Cart Item Name" görsensin deye maksimum "15" saniye gözle
* "Cart Item Name" elementinin metni "${ad}" olmalıdır
* "Cart Item Quantity" input deyeri "${miqdar}" olmalıdır
* "Cart Total" elementinin metni "${cem}" olmalıdır
* Brauzeri bağla

## TC_CART_POS_005 Səbətdə miqdar dəyişəndə sətir və ümumi cəm yenilənir
tags: regression, sebet

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/airpods?filter_stock=1" siyahısından stokda olan ilk məhsulu səbətə əlavə et və qiymətini "Q" olaraq yadda saxla
* "View Cart Button" elementine klik et
* "Cart Item Quantity" görsensin deye maksimum "15" saniye gözle
* "Cart Item Quantity" input deyeri "1" olmalıdır
* "Cart Item Increase" elementine klik et
* "Cart Item Quantity" input deyeri "2" olmalıdır
* "Cart Item Increase" elementine klik et
* "Cart Item Quantity" input deyeri "3" olmalıdır
* "Cart Item Price" qiyməti "${Q}" qiymətinin "3" mislinə bərabər olmalıdır
* "Cart Total" qiyməti "${Q}" qiymətinin "3" mislinə bərabər olmalıdır
* "Cart Counter" elementinin metni "3" olmalıdır
* "Cart Item Decrease" elementine klik et
* "Cart Item Quantity" input deyeri "2" olmalıdır
* "Cart Item Price" qiyməti "${Q}" qiymətinin "2" mislinə bərabər olmalıdır
* "Cart Total" qiyməti "${Q}" qiymətinin "2" mislinə bərabər olmalıdır
* "Cart Counter" elementinin metni "2" olmalıdır
* Brauzeri bağla

## TC_PDP_BVA_006 Miqdar 1-dən aşağı enmir, + ilə artır
tags: regression, pdp, bva

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/iphone?filter_stock=1" siyahısından stokda olan ilk məhsulu aç
* "Quantity Input" görsensin deye maksimum "15" saniye gözle
* "Quantity Input" input deyeri "1" olmalıdır
* "Quantity Decrease Button" deaktiv olmalıdır
* "Quantity Increase Button" elementine klik et
* "Quantity Input" input deyeri "2" olmalıdır
* "Quantity Decrease Button" aktiv olmalıdır
* "Quantity Decrease Button" elementine klik et
* "Quantity Input" input deyeri "1" olmalıdır
* "Quantity Decrease Button" deaktiv olmalıdır
* Brauzeri bağla

## TC_PDP_POS_004 Yaddaş variantı dəyişəndə məhsul məlumatları yenilənir
tags: regression, pdp

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/iphone?filter_stock=1" siyahısından stokda olan ilk məhsulu aç
* "Product Title" elementinin metnini "ad0" olaraq yadda saxla
* "Product SKU" elementinin metnini "kod0" olaraq yadda saxla
* "Product Price" elementinin metnini "qiymet0" olaraq yadda saxla
* "Color Title" elementinin metnini "reng0" olaraq yadda saxla
* "In Stock Memory Option" görsensin deye maksimum "10" saniye gözle
* "In Stock Memory Option" elementinin metnini "yeniYaddas" olaraq yadda saxla
* "In Stock Memory Option" elementine klik et
* "Product Title" elementinin metni "${ad0}" olmamalıdır
* "Product Title" elementin içinde "${yeniYaddas}" yazısı var
* "Active Memory Option" elementinin metni "${yeniYaddas}" olmalıdır
* "Product SKU" elementinin metni "${kod0}" olmamalıdır
* "Product Price" elementinin metni "${qiymet0}" olmamalıdır
* "Color Title" elementinin metni "${reng0}" olmalıdır
* Brauzeri bağla

## TC_PLP_POS_003 Kartdakı ad və qiymət məhsul səhifəsindəki ilə eynidir
tags: regression, listing

* "chrome" brauzeri aç ve keçid et "https://ispace.az/category/iphone"
* Cookie bildirişini rədd et
* "Product Card Name" görsensin deye maksimum "15" saniye gözle
* "Product Card Name" elementinin metnini "kartAdi" olaraq yadda saxla
* "Product Card Price" elementinin metnini "kartQiymeti" olaraq yadda saxla
* "First Product Image" elementine klik et
* URL "/product/" içermelidir
* "Product Price" görünənə qədər A/B testini köhnə dizayna qaytar
* "Product Title" elementinin metni "${kartAdi}" olmalıdır
* "Product Price" elementinin metni "${kartQiymeti}" olmalıdır
* Brauzeri bağla

## TC_PLP_POS_019 Aşağı qiymət sıralaması qiymətləri artan sırada göstərir
tags: regression, listing

* "chrome" brauzeri aç ve keçid et "https://ispace.az/category/iphone"
* Cookie bildirişini rədd et
* "Sort Dropdown" görsensin deye maksimum "15" saniye gözle
* "Sort Dropdown" elementine klik et
* "Sort Option" siyahısında "Aşağı qiymət" metnli elemente klik et
* URL "sort=cheap" içermelidir
* "Product Card Price" elementlerinin sayı en az "2" olmalıdır
* "Product Card Price" qiymətləri artan sırada olmalıdır
* Brauzeri bağla

## TC_PLP_POS_020 Yüksək qiymət sıralaması azalan sıradadır və ilk məhsul ən bahalısıdır
tags: regression, listing

* "chrome" brauzeri aç ve keçid et "https://ispace.az/category/iphone"
* Cookie bildirişini rədd et
* "Max Price Label" görsensin deye maksimum "15" saniye gözle
* "Max Price Label" elementinin metnini "Qmax" olaraq yadda saxla
* "Sort Dropdown" elementine klik et
* "Sort Option" siyahısında "Yüksək qiymət" metnli elemente klik et
* URL "sort=expensive" içermelidir
* "Product Card Price" qiymətləri azalan sırada olmalıdır
* "Product Card Price" qiyməti "${Qmax}" qiymətinin "1" mislinə bərabər olmalıdır
* Brauzeri bağla

## TC_PLP_POS_007 Yaddaş filtri yalnız seçilmiş yaddaşlı məhsulları göstərir
tags: regression, filtr

* "chrome" brauzeri aç ve keçid et "https://ispace.az/category/iphone"
* Cookie bildirişini rədd et
* "Memory Filter Caption" elementine klik et
* "Filter 256 GB" elementine klik et
* URL "filter_features" içermelidir
* "Product Card Name" elementlerinin sayı en az "1" olmalıdır
* "Product Card Name" elementlerinin hamısında "256 GB" yazısı olmalıdır
* Brauzeri bağla

## TC_PLP_POS_009 256 GB və Mövcuddur birlikdə seçildikdə yalnız hər iki şərtə uyğun məhsullar göstərilir
tags: regression, filtr

* "chrome" brauzeri aç ve keçid et "https://ispace.az/category/iphone"
* Cookie bildirişini rədd et
* "Memory Filter Caption" elementine klik et
* "Filter 256 GB" elementine klik et
* URL "filter_features" içermelidir
* "Stock Filter Caption" elementine klik et
* "Filter In Stock" elementine klik et
* URL "filter_stock=1" içermelidir
* "Product Card Name" elementlerinin sayı en az "1" olmalıdır
* "Product Card Name" elementlerinin hamısında "256 GB" yazısı olmalıdır
* "Product Card Name" elementlerinin sayı "Product Card Cart Button" elementlerinin sayına bərabər olmalıdır
* Brauzeri bağla

## TC_FLT_POS_002 Seriya filtri yalnız dəqiq seriyanı qaytarır
tags: regression, filtr

* "chrome" brauzeri aç ve keçid et "https://ispace.az/category/iphone"
* Cookie bildirişini rədd et
* "Series Filter Caption" elementine klik et
* "Filter iPhone 16" elementine klik et
* URL "filter_" içermelidir
* "Product Card Name" elementlerinin hamısında "iPhone 16," yazısı olmalıdır
* "Filter iPhone 16" elementine klik et
* "Filter iPhone 15" elementine klik et
* "Product Card Name" elementlerinin hamısında "iPhone 15," yazısı olmalıdır
* Brauzeri bağla

## TC_PLP_BVA_015 Qiymət filtrinin sərhədləri daxildir (min = max = məhsulun qiyməti)
tags: regression, filtr, bva

* "chrome" brauzeri aç ve keçid et "https://ispace.az/category/iphone"
* Cookie bildirişini rədd et
* "Product Card Name" görsensin deye maksimum "15" saniye gözle
* "Product Card Name" elementinin metnini "kartAdi" olaraq yadda saxla
* "Product Card Price" elementinin metnini "kartQiymeti" olaraq yadda saxla
* "Product Card Price" qiymətini rəqəm kimi "Q" olaraq yadda saxla
* "Price Min Input" elementine "${Q}" yaz ve Enter düymesine bas
* URL "filter_price" içermelidir
* "Price Max Input" elementini temizle
* "Price Max Input" elementine "${Q}" yaz ve Enter düymesine bas
* "Product Card Price" elementlerinin hamısında "${kartQiymeti}" yazısı olmalıdır
* Sehifede "${kartAdi}" yazısı olmalıdır
* Brauzeri bağla

## TC_FLT_EDGE_018 Filtr və Aşağı qiymət sıralaması səhifələr arasında saxlanır
tags: regression, filtr, edge

* "chrome" brauzeri aç ve keçid et "https://ispace.az/category/iphone"
* Cookie bildirişini rədd et
* "Stock Filter Caption" elementine klik et
* "Filter Out Of Stock" elementine klik et
* URL "filter_stock=0" içermelidir
* "Sort Dropdown" elementine klik et
* "Sort Option" siyahısında "Aşağı qiymət" metnli elemente klik et
* URL "sort=cheap" içermelidir
* "Product Card Price" qiymətləri artan sırada olmalıdır
* "Product Card Cart Button" elementlerinin sayı "0" olmalıdır
* "Last Product Card Price" elementinin metnini "sehife1SonQiymet" olaraq yadda saxla
* "Pagination Page 2" elementine klik et
* URL "page=2" içermelidir
* URL "filter_stock=0" içermelidir
* URL "sort=cheap" içermelidir
* "Sort Dropdown" elementinin metni "Aşağı qiymət" olmalıdır
* "Product Card Price" qiyməti "${sehife1SonQiymet}" qiymətindən az olmamalıdır
* "Product Card Price" qiymətləri artan sırada olmalıdır
* "Product Card Cart Button" elementlerinin sayı "0" olmalıdır
* "Pagination Last Page" elementine klik et
* URL "filter_stock=0" içermelidir
* URL "sort=cheap" içermelidir
* "Product Card Cart Button" elementlerinin sayı "0" olmalıdır
* Brauzeri bağla

## TC_FIN_POS_003 Hər tərəfdaş üçün aylıq × ödəniş sayı Ümumi ödəniş məbləğinə bərabərdir (BUG-017)
tags: regression, taksit, known-bug

* "chrome" brauzeri aç ve keçid et "https://ispace.az/product/iphone-18-pro-256-gb-black-mjrp4af-a"
* Cookie bildirişini rədd et
* "Installment Programs Button" görsensin deye maksimum "15" saniye gözle
* "Installment Programs Button" elementine klik et
* "Credits Modal Title" görsensin deye maksimum "10" saniye gözle
* "Credits Modal Title" elementinin metni "Taksitlə alış" olmalıdır
* "Credit Term 18" elementine klik et
* "Credit Total" görsensin deye maksimum "15" saniye gözle
* Taksit pəncərəsində "Credit Monthly" × "Credit Payment Count" hər tərəfdaş üçün "Credit Total" ilə bərabər olmalıdır
* Brauzeri bağla

## TC_PLP_POS_014 Qiymət aralığı daxilində olan məhsullar göstərilir
tags: regression, filtr

* "chrome" brauzeri aç ve keçid et "https://ispace.az/category/iphone"
* Cookie bildirişini rədd et
* "Price Min Input" görsensin deye maksimum "15" saniye gözle
* "Price Min Input" elementine "2000" yaz ve Enter düymesine bas
* URL "filter_price" içermelidir
* "Price Max Input" elementini temizle
* "Price Max Input" elementine "3000" yaz ve Enter düymesine bas
* URL "3000" içermelidir
* "Product Card Price" elementlerinin sayı en az "1" olmalıdır
* "Product Card Price" qiymətləri "2000" ilə "3000" arasında olmalıdır
* Brauzeri bağla

## TC_PLP_POS_005 Mövcuddur filtri: nəticə sayı sayğaca bərabərdir
tags: regression, filtr

* "chrome" brauzeri aç ve keçid et "https://ispace.az/category/iphone"
* Cookie bildirişini rədd et
* "Stock Filter Caption" elementine klik et
* "Filter In Stock" görsensin deye maksimum "10" saniye gözle
* "Filter In Stock" elementinin metnini "sayğac" olaraq yadda saxla
* "Filter In Stock" elementine klik et
* URL "filter_stock=1" içermelidir
* "Product Count" elementindəki rəqəm "${sayğac}" dəyərindəki rəqəmə bərabər olmalıdır
* "Product Card Name" elementlerinin sayı "Product Card Cart Button" elementlerinin sayına bərabər olmalıdır
* Brauzeri bağla

## TC_PLP_POS_004 Stokda olan kartda Səbətə, stokda olmayan kartda Səbətə düyməsi yoxdur
tags: regression, filtr

* "chrome" brauzeri aç ve keçid et "https://ispace.az/category/iphone"
* Cookie bildirişini rədd et
* "Stock Filter Caption" elementine klik et
* "Filter In Stock" elementine klik et
* URL "filter_stock=1" içermelidir
* "Product Card Name" elementlerinin sayı en az "1" olmalıdır
* "Product Card Name" elementlerinin sayı "Product Card Cart Button" elementlerinin sayına bərabər olmalıdır
* "Filter In Stock" elementine klik et
* "Filter Out Of Stock" elementine klik et
* URL "filter_stock=0" içermelidir
* "Product Card Name" elementlerinin sayı en az "1" olmalıdır
* "Product Card Cart Button" elementlerinin sayı "0" olmalıdır
* Brauzeri bağla

## TC_FIN_POS_001 Bütün proqramlara baxın Taksitlə alış pəncərəsini PDP-dəki məhsulla açır
tags: regression, taksit

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/iphone?filter_stock=1" siyahısından stokda olan ilk məhsulu aç
* "Product Title" elementinin metnini "pdpAd" olaraq yadda saxla
* "Product Price" elementinin metnini "pdpQiymet" olaraq yadda saxla
* "Installment Programs Button" görsensin deye maksimum "15" saniye gözle
* "Installment Programs Button" elementine klik et
* "Credits Modal Title" görsensin deye maksimum "10" saniye gözle
* "Credits Modal Title" elementinin metni "Taksitlə alış" olmalıdır
* "Credits Modal Product Name" elementinin metni "${pdpAd}" olmalıdır
* "Credits Modal Price" elementinin metni "${pdpQiymet}" olmalıdır
* "Credit Total" görsensin deye maksimum "15" saniye gözle
* "Credit Monthly" elementlerinin sayı en az "1" olmalıdır
* "Credits Modal Buy Button" görünür olmalıdır
* "Credits Modal Credit Button" görünür olmalıdır
* Brauzeri bağla

## TC_FIN_POS_009 Müddət düyməsi dəyişdikdə tərəfdaş məbləğləri yenilənir
tags: taksit

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/iphone?filter_stock=1" siyahısından stokda olan ilk məhsulu aç
* "Installment Programs Button" görsensin deye maksimum "15" saniye gözle
* "Installment Programs Button" elementine klik et
* "Credit Term 18" görsensin deye maksimum "15" saniye gözle
* "Credit Term 18" elementine klik et
* "Credit Payment Count" elementin içinde "18" yazısı var
* "Credit Monthly" elementinin metnini "aylıq18" olaraq yadda saxla
* "Credit Term 12" elementine klik et
* "Credit Payment Count" elementin içinde "12" yazısı var
* "Credit Monthly" elementinin metni "${aylıq18}" olmamalıdır
* "Credit Term 18" elementine klik et
* "Credit Payment Count" elementin içinde "18" yazısı var
* "Credit Monthly" elementinin metni "${aylıq18}" olmalıdır
* Brauzeri bağla

## TC_PLP_POS_011 Filtrlər təmizlənəndə ilkin siyahı bərpa olunur
tags: filtr

* "chrome" brauzeri aç ve keçid et "https://ispace.az/category/iphone"
* Cookie bildirişini rədd et
* "Product Count" görsensin deye maksimum "15" saniye gözle
* "Product Count" elementinin metnini "ilkinSay" olaraq yadda saxla
* "Memory Filter Caption" elementine klik et
* "Filter 256 GB" elementine klik et
* "Stock Filter Caption" elementine klik et
* "Filter In Stock" elementine klik et
* URL "filter_stock=1" içermelidir
* "Product Count" elementinin metni "${ilkinSay}" olmamalıdır
* "Filter 256 GB" elementine klik et
* "Filter In Stock" elementine klik et
* "Product Count" elementinin metni "${ilkinSay}" olmalıdır
* Brauzeri bağla

## TC_PLP_POS_012 Filtrli səhifə yeniləndikdə və link yeni tabda açıldıqda filtr qorunur
tags: filtr

* "chrome" brauzeri aç ve keçid et "https://ispace.az/category/iphone"
* Cookie bildirişini rədd et
* "Memory Filter Caption" elementine klik et
* "Filter 256 GB" elementine klik et
* URL "filter_features" içermelidir
* "Product Card Name" elementlerinin hamısında "256 GB" yazısı olmalıdır
* "Product Count" elementinin metnini "say256" olaraq yadda saxla
* Cari URL-i "filtrUrl" olaraq yadda saxla
* Sehifeni yenile
* "Product Count" görsensin deye maksimum "15" saniye gözle
* URL "filter_features" içermelidir
* "Product Count" elementinin metni "${say256}" olmalıdır
* "Product Card Name" elementlerinin hamısında "256 GB" yazısı olmalıdır
* Yeni tabda "${filtrUrl}" aç
* "Product Count" görsensin deye maksimum "15" saniye gözle
* "Product Count" elementinin metni "${say256}" olmalıdır
* "Product Card Name" elementlerinin hamısında "256 GB" yazısı olmalıdır
* Brauzeri bağla

## TC_PLP_POS_021 Sıralama növbəti səhifədə də davam edir
tags: listing

* "chrome" brauzeri aç ve keçid et "https://ispace.az/category/iphone"
* Cookie bildirişini rədd et
* "Sort Dropdown" görsensin deye maksimum "15" saniye gözle
* "Sort Dropdown" elementine klik et
* "Sort Option" siyahısında "Aşağı qiymət" metnli elemente klik et
* URL "sort=cheap" içermelidir
* "Product Card Price" qiymətləri artan sırada olmalıdır
* "Last Product Card Price" elementinin metnini "sehife1SonQiymet" olaraq yadda saxla
* "Pagination Page 2" elementine klik et
* URL "page=2" içermelidir
* URL "sort=cheap" içermelidir
* "Product Card Price" qiyməti "${sehife1SonQiymet}" qiymətindən az olmamalıdır
* "Product Card Price" qiymətləri artan sırada olmalıdır
* Brauzeri bağla

## TC_PLP_BVA_016 Sərhəddən bir vahid kənar dəyər məhsulu xaric edir
tags: filtr, bva

* "chrome" brauzeri aç ve keçid et "https://ispace.az/category/iphone"
* Cookie bildirişini rədd et
* "Product Card Price" görsensin deye maksimum "15" saniye gözle
* "Product Card Price" elementinin metnini "Q" olaraq yadda saxla
* "Product Card Price" qiymətinə "1" əlavə edib rəqəm kimi "Qplus1" olaraq yadda saxla
* "Product Card Price" qiymətinə "500" əlavə edib rəqəm kimi "Qplus500" olaraq yadda saxla
* "Product Card Price" qiymətinə "-500" əlavə edib rəqəm kimi "Qminus500" olaraq yadda saxla
* "Product Card Price" qiymətinə "-1" əlavə edib rəqəm kimi "Qminus1" olaraq yadda saxla
* "Price Min Input" elementine "${Qplus1}" yaz ve Enter düymesine bas
* URL "filter_price" içermelidir
* "Price Max Input" elementini temizle
* "Price Max Input" elementine "${Qplus500}" yaz ve Enter düymesine bas
* URL "${Qplus500}" içermelidir
* "Product Card Price" elementlerinin heç birinin metni "${Q}" olmamalıdır
* "Price Min Input" elementini temizle
* "Price Min Input" elementine "${Qminus500}" yaz ve Enter düymesine bas
* URL "${Qminus500}" içermelidir
* "Price Max Input" elementini temizle
* "Price Max Input" elementine "${Qminus1}" yaz ve Enter düymesine bas
* URL "${Qminus1}" içermelidir
* "Product Card Price" elementlerinin heç birinin metni "${Q}" olmamalıdır
* Brauzeri bağla

## TC_PLP_POS_010 256 GB və 512 GB birlikdə seçildikdə nəticə sayı iki sayğacın cəminə bərabərdir
tags: filtr

* "chrome" brauzeri aç ve keçid et "https://ispace.az/category/iphone"
* Cookie bildirişini rədd et
* "Memory Filter Caption" elementine klik et
* "Filter 256 GB" görsensin deye maksimum "10" saniye gözle
* "Filter 256 GB" elementinin metnini "sayğac256" olaraq yadda saxla
* "Filter 512 GB" elementinin metnini "sayğac512" olaraq yadda saxla
* "Filter 256 GB" elementine klik et
* "Filter 512 GB" elementine klik et
* URL "filter_features" içermelidir
* "Product Count" elementindəki rəqəm "${sayğac256}" və "${sayğac512}" rəqəmlərinin cəminə bərabər olmalıdır
* Brauzeri bağla

## TC_PLP_POS_006 Bir filtr qrupunda sayğacların cəmi ümumi məhsul sayına bərabərdir
tags: filtr

* "chrome" brauzeri aç ve keçid et "https://ispace.az/category/iphone"
* Cookie bildirişini rədd et
* "Product Count" görsensin deye maksimum "15" saniye gözle
* "Stock Filter Caption" elementine klik et
* "Filter In Stock" görsensin deye maksimum "10" saniye gözle
* "Stock Filter Options" qiymətlərinin cəmi "Product Count" qiymətinə bərabər olmalıdır
* "SIM Filter Caption" elementine klik et
* "SIM Filter Options" görsensin deye maksimum "10" saniye gözle
* "SIM Filter Options" qiymətlərinin cəmi "Product Count" qiymətinə bərabər olmalıdır
* Brauzeri bağla

## TC_CART_BVA_006 Səbətdə miqdar 1-dən aşağı enmir
tags: sebet, bva

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/airpods?filter_stock=1" siyahısından stokda olan ilk məhsulu səbətə əlavə et və qiymətini "Q" olaraq yadda saxla
* "View Cart Button" elementine klik et
* "Cart Item Quantity" görsensin deye maksimum "15" saniye gözle
* "Cart Item Quantity" input deyeri "1" olmalıdır
* "Cart Item Decrease" deaktiv olmalıdır
* "Cart Item Price" elementinin metni "${Q}" olmalıdır
* Brauzeri bağla

## TC_CART_POS_008 Sonuncu məhsul silinəndə boş səbət vəziyyəti göstərilir
tags: sebet

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/airpods?filter_stock=1" siyahısından stokda olan ilk məhsulu səbətə əlavə et və qiymətini "Q" olaraq yadda saxla
* "View Cart Button" elementine klik et
* "Cart Item Name" görsensin deye maksimum "15" saniye gözle
* "Cart Item Name" elementlerinin sayı "1" olmalıdır
* "Cart Remove Button" elementine klik et
* "Empty Cart Title" görsensin deye maksimum "15" saniye gözle
* "Empty Cart Title" elementinin metni "Səbətiniz boşdur" olmalıdır
* "Cart Item Name" elementlerinin sayı "0" olmalıdır
* Brauzeri bağla

## TC_CART_EDGE_016 Fərqli məhsullar ayrı sətirlərdə saxlanılır, cəm sətirlərin cəmidir
tags: sebet, edge

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/iphone?filter_stock=1" siyahısından "First Product Image" məhsulunu səbətə əlavə et
* "https://ispace.az/category/iphone?filter_stock=1" siyahısından "Second Product Image" məhsulunu səbətə əlavə et
* "https://ispace.az/category/iphone?filter_stock=1" siyahısından "Third Product Image" məhsulunu səbətə əlavə et
* "Cart Counter" elementinin metni "3" olmalıdır
* "View Cart Button" elementine klik et
* "Cart Item Name" görsensin deye maksimum "15" saniye gözle
* "Cart Item Name" elementlerinin sayı "3" olmalıdır
* "Cart Item Price" qiymətlərinin cəmi "Cart Total" qiymətinə bərabər olmalıdır
* Brauzeri bağla

## TC_SRCH_POS_003 Böyük-kiçik hərflə eyni sorğu eyni nəticəni, qismən söz uyğun məhsulları qaytarır
tags: axtaris

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "Search Input" görsensin deye maksimum "15" saniye gözle
* "Search Input" elementine "airpods" yaz ve Enter düymesine bas
* "Search Result Product Name" görsensin deye maksimum "15" saniye gözle
* "Search Result Product Name" elementin içinde "AirPods" yazısı var
* "Search Result Product Name" elementinin metnini "ilkNetice" olaraq yadda saxla
* "https://ispace.az/search?query=AIRPODS" adresine keçid et
* URL "AIRPODS" içermelidir
* "Search Result Product Name" görsensin deye maksimum "15" saniye gözle
* "Search Result Product Name" elementinin metni "${ilkNetice}" olmalıdır
* "https://ispace.az/search?query=airp" adresine keçid et
* URL "airp" içermelidir
* "Search Result Product Name" görsensin deye maksimum "15" saniye gözle
* "Search Result Product Name" elementin içinde "AirPods" yazısı var
* Brauzeri bağla

## TC_PLP_POS_002 Hər məhsul kartında şəkil, ad, qiymət və vəziyyətə uyğun düymə göstərilir
tags: regression, listing

* "chrome" brauzeri aç ve keçid et "https://ispace.az/category/iphone"
* Cookie bildirişini rədd et
* "Product Cards" görsensin deye maksimum "15" saniye gözle
* "Product Cards" elementlerinin sayı en az "1" olmalıdır
* "Product Card Images" elementlerinin sayı "Product Cards" elementlerinin sayına bərabər olmalıdır
* "Product Card Name" elementlerinin sayı "Product Cards" elementlerinin sayına bərabər olmalıdır
* "Product Card Price" elementlerinin sayı "Product Cards" elementlerinin sayına bərabər olmalıdır
* "Product Card Action Button" elementlerinin sayı "Product Cards" elementlerinin sayına bərabər olmalıdır
* "Product Card Name" elementlerinin heç birinin metni "" olmamalıdır
* "Product Card Price" elementlerinin hamısında "₼" yazısı olmalıdır
* "Product Card Price" qiymətləri "1" ilə "999999" arasında olmalıdır
* Brauzeri bağla

## TC_FLT_POS_017 Üç fərqli qrupdan filtr kombinasiyası dəqiq nəticə verir
tags: regression, filtr

* "chrome" brauzeri aç ve keçid et "https://ispace.az/category/iphone"
* Cookie bildirişini rədd et
* "Series Filter Caption" elementine klik et
* "Filter iPhone 18 Pro" elementine klik et
* URL "filter_features" içermelidir
* "Memory Filter Caption" elementine klik et
* "Filter 1 TB" elementine klik et
* "Color Filter Caption" elementine klik et
* "Filter Silver" elementine klik et
* "Product Card Name" elementlerinin sayı en az "1" olmalıdır
* "Product Card Name" elementlerinin hamısında "iPhone 18 Pro, 1 TB, Gümüş" yazısı olmalıdır
* "Filter Silver" elementine klik et
* "Filter Black" elementine klik et
* "Product Card Name" elementlerinin sayı en az "1" olmalıdır
* "Product Card Name" elementlerinin hamısında "iPhone 18 Pro, 1 TB, Qara" yazısı olmalıdır
* Brauzeri bağla

## TC_PDP_POS_002 PDP-dəki ad, qiymət və aylıq ödəniş listing kartındakı ilə eynidir
tags: regression, pdp

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/iphone?filter_stock=1" adresine keçid et
* "First Product Card Monthly" görsensin deye maksimum "15" saniye gözle
* "First Product Card Name" elementinin metnini "kartAd" olaraq yadda saxla
* "First Product Card Price" elementinin metnini "kartQiymet" olaraq yadda saxla
* "First Product Card Monthly" elementinin metnini "kartAylıq" olaraq yadda saxla
* "First Product Image" elementine klik et
* URL "/product/" içermelidir
* "Product Price" görünənə qədər A/B testini köhnə dizayna qaytar
* "Product Title" elementinin metni "${kartAd}" olmalıdır
* "Product Price" elementinin metni "${kartQiymet}" olmalıdır
* "Product Monthly Payment" elementindəki rəqəm "${kartAylıq}" dəyərindəki rəqəmə bərabər olmalıdır
* Brauzeri bağla

## TC_PDP_POS_005 Rəng variantı dəyişəndə məhsul məlumatları yenilənir, yaddaş və qiymət qorunur
tags: regression, pdp

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/iphone?filter_stock=1" siyahısından stokda olan ilk məhsulu aç
* "Product Title" elementinin metnini "ad0" olaraq yadda saxla
* "Product SKU" elementinin metnini "kod0" olaraq yadda saxla
* "Product Price" elementinin metnini "qiymet0" olaraq yadda saxla
* "Active Memory Option" elementinin metnini "yaddas0" olaraq yadda saxla
* "Color Title" elementinin metnini "reng0" olaraq yadda saxla
* "Other Color Option" elementine klik et
* "Color Title" elementinin metni "${reng0}" olmamalıdır
* "Product Title" elementinin metni "${ad0}" olmamalıdır
* "Product SKU" elementinin metni "${kod0}" olmamalıdır
* "Product Title" elementin içinde "${yaddas0}" yazısı var
* "Active Memory Option" elementinin metni "${yaddas0}" olmalıdır
* "Product Price" elementinin metni "${qiymet0}" olmalıdır
* Brauzeri bağla

## TC_PDP_POS_011 Stokda olmayan məhsul alına bilmir
tags: regression, pdp

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/iphone?filter_stock=0" adresine keçid et
* "First Product Image" görsensin deye maksimum "15" saniye gözle
* "First Product Image" elementine klik et
* URL "/product/" içermelidir
* "Product Title" görünənə qədər A/B testini köhnə dizayna qaytar
* "Delivery Block" elementin içinde "Mövcud deyil" yazısı var
* "PDP Notify Button" elementlerinin sayı en az "1" olmalıdır
* "Add To Cart Button" elementlerinin sayı "0" olmalıdır
* "One Click Buy Button" elementlerinin sayı "0" olmalıdır
* "Quantity Input" elementlerinin sayı "0" olmalıdır
* Brauzeri bağla

## TC_FIN_POS_002 PDP-dəki aylıq ödəniş pəncərədə həmin müddət və məbləğlə var
tags: regression, taksit

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/iphone?filter_stock=1" siyahısından stokda olan ilk məhsulu aç
* "Product Monthly Payment" görsensin deye maksimum "15" saniye gözle
* "Product Monthly Payment" elementinin metnini "pdpAylıq" olaraq yadda saxla
* "Installment Programs Button" elementine klik et
* "Credit Total" görsensin deye maksimum "15" saniye gözle
* "Credit Term Chips" düymələrindən "${pdpAylıq}" mətnindəki müddəti seç, "Credit Monthly" aylıq məbləği həmin mətndəki kimi olmalıdır
* Brauzeri bağla

## TC_FIN_POS_004 0% proqramda ümumi məbləğ qiymətə bərabərdir, heç bir proqramda qiymətdən az deyil
tags: regression, taksit

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/iphone?filter_stock=1" siyahısından stokda olan ilk məhsulu aç
* "Product Price" elementinin metnini "pdpQiymet" olaraq yadda saxla
* "Product Price" qiymətini rəqəm kimi "Q" olaraq yadda saxla
* "Installment Programs Button" elementine klik et
* "Credit Term 18" görsensin deye maksimum "15" saniye gözle
* "Credit Term 18" elementine klik et
* "Credit Payment Count" elementin içinde "18" yazısı var
* "Credits Modal Price" elementinin metni "${pdpQiymet}" olmalıdır
* "Modal Pay Total" elementinin metni "${pdpQiymet}" olmalıdır
* "Credit Total" elementlerinin sayı en az "1" olmalıdır
* "Credit Total" qiymətləri "${Q}" ilə "999999" arasında olmalıdır
* Brauzeri bağla

## TC_FIN_BVA_006 Ən ucuz məhsulda aylıq × müddət qiymətdən çox göstərilməməlidir
tags: regression, taksit, bva, known-bug

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/accessories-for-iphone?sort=cheap&filter_stock=1" adresine keçid et
* "First Product Card Price" görsensin deye maksimum "15" saniye gözle
* "First Product Card Price" qiymətləri "1" ilə "20" arasında olmalıdır
* "First Product Image" elementine klik et
* URL "/product/" içermelidir
* "Installment Programs Button" görünənə qədər A/B testini köhnə dizayna qaytar
* "Installment Programs Button" elementine klik et
* "Last Credit Term" görsensin deye maksimum "15" saniye gözle
* "Last Credit Term" elementine klik et
* "Credit Total" görsensin deye maksimum "15" saniye gözle
* Taksit pəncərəsində "Credit Monthly" × "Credit Payment Count" hər tərəfdaş üçün "Credit Total" ilə bərabər olmalıdır
* Brauzeri bağla

## TC_FIN_POS_012 Pəncərədə qoruma proqramı seçimi Ödəmək və taksit məbləğini yeniləyir, ləğv bərpa edir
tags: regression, taksit

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/iphone?filter_stock=1" siyahısından stokda olan ilk məhsulu aç
* "Product Price" elementinin metnini "pdpQiymet" olaraq yadda saxla
* "Installment Programs Button" elementine klik et
* "Credit Term 18" görsensin deye maksimum "15" saniye gözle
* "Credit Term 18" elementine klik et
* "Modal Pay Total" elementinin metni "${pdpQiymet}" olmalıdır
* "Credit Monthly" elementinin metnini "aylıq0" olaraq yadda saxla
* "Modal Protection Price" elementinin metnini "qoruma" olaraq yadda saxla
* "Modal Protection Option" elementine klik et
* "Modal Protection Option" elementinin "class" atributunda "product-services_item__active" olmalıdır
* "Modal Pay Total" elementindəki rəqəm "${pdpQiymet}" və "${qoruma}" rəqəmlərinin cəminə bərabər olmalıdır
* "Credit Total" elementindəki rəqəm "${pdpQiymet}" və "${qoruma}" rəqəmlərinin cəminə bərabər olmalıdır
* "Credit Monthly" elementinin metni "${aylıq0}" olmamalıdır
* "Modal No Protection Option" elementine klik et
* "Modal Pay Total" elementinin metni "${pdpQiymet}" olmalıdır
* "Credit Monthly" elementinin metni "${aylıq0}" olmalıdır
* Brauzeri bağla

## TC_FIN_BVA_013 Pəncərədə miqdar dəyişdikdə qiymət və taksitlər yenilənir
tags: regression, taksit, bva

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/iphone?filter_stock=1" siyahısından stokda olan ilk məhsulu aç
* "Installment Programs Button" elementine klik et
* "Credit Term 18" görsensin deye maksimum "15" saniye gözle
* "Credit Term 18" elementine klik et
* "Modal Quantity Input" input deyeri "1" olmalıdır
* "Modal Quantity Decrease" deaktiv olmalıdır
* "Credits Modal Price" elementinin metnini "qiymet1" olaraq yadda saxla
* "Credit Monthly" elementinin metnini "aylıq1" olaraq yadda saxla
* "Modal Quantity Increase" elementine klik et
* "Modal Quantity Input" input deyeri "2" olmalıdır
* "Credits Modal Price" qiyməti "${qiymet1}" qiymətinin "2" mislinə bərabər olmalıdır
* "Modal Pay Total" qiyməti "${qiymet1}" qiymətinin "2" mislinə bərabər olmalıdır
* "Credit Total" qiyməti "${qiymet1}" qiymətinin "2" mislinə bərabər olmalıdır
* "Credit Monthly" elementinin metni "${aylıq1}" olmamalıdır
* "Modal Quantity Decrease" aktiv olmalıdır
* "Modal Quantity Decrease" elementine klik et
* "Modal Quantity Input" input deyeri "1" olmalıdır
* "Credits Modal Price" elementinin metni "${qiymet1}" olmalıdır
* "Credit Monthly" elementinin metni "${aylıq1}" olmalıdır
* "Modal Quantity Decrease" deaktiv olmalıdır
* Brauzeri bağla

## TC_CART_POS_002 Məhsul listing kartından birbaşa səbətə əlavə olunur
tags: regression, sebet

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/iphone?filter_stock=1" adresine keçid et
* "First Product Card Cart Button" görsensin deye maksimum "15" saniye gözle
* "First Product Card Name" elementinin metnini "kartAd" olaraq yadda saxla
* "First Product Card Price" elementinin metnini "kartQiymet" olaraq yadda saxla
* "First Product Card Cart Button" elementine klik et
* "Added To Cart Popup Title" görsensin deye maksimum "10" saniye gözle
* "Cart Counter" elementinin metni "1" olmalıdır
* "View Cart Button" elementine klik et
* "Cart Item Name" görsensin deye maksimum "15" saniye gözle
* "Cart Item Name" elementlerinin sayı "1" olmalıdır
* "Cart Item Name" elementinin metni "${kartAd}" olmalıdır
* "Cart Item Price" elementinin metni "${kartQiymet}" olmalıdır
* "Cart Item Quantity" input deyeri "1" olmalıdır
* Brauzeri bağla

## TC_CART_POS_009 Qoruma proqramı ilə əlavə edilən məhsulda proqram səbətdə seçili qalır və cəmə daxil olur
tags: regression, sebet, known-bug

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/iphone?filter_stock=1" siyahısından stokda olan ilk məhsulu aç
* "Product Price" elementinin metnini "pdpQiymet" olaraq yadda saxla
* "Protection Price" elementinin metnini "qoruma" olaraq yadda saxla
* "Protection Option" elementine klik et
* "Protection Option" elementinin "class" atributunda "product-services_item__active" olmalıdır
* Açıq məhsulu səbətə əlavə et
* "View Cart Button" elementine klik et
* "Cart Item Name" görsensin deye maksimum "15" saniye gözle
* "Cart Item Name" elementlerinin sayı "1" olmalıdır
* "Cart Item Price" elementinin metni "${pdpQiymet}" olmalıdır
* "Cart Protection Option" elementinin "class" atributunda "product-services_item__active" olmalıdır
* "Cart Protection Price" elementinin metni "${qoruma}" olmalıdır
* "Cart Total" elementindəki rəqəm "${pdpQiymet}" və "${qoruma}" rəqəmlərinin cəminə bərabər olmalıdır
* Brauzeri bağla

## TC_CART_EDGE_019 Məhsul silinəndə ona bağlı qoruma proqramı da silinir
tags: regression, sebet, edge

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/iphone?filter_stock=1" siyahısından stokda olan ilk məhsulu aç
* "Protection Option" elementine klik et
* "Protection Option" elementinin "class" atributunda "product-services_item__active" olmalıdır
* Açıq məhsulu səbətə əlavə et
* "View Cart Button" elementine klik et
* "Cart Protection Option" görsensin deye maksimum "15" saniye gözle
* "Cart Protection Option" elementinin "class" atributunda "product-services_item__active" olmalıdır
* "Cart Remove Button" elementine klik et
* "Empty Cart Title" görsensin deye maksimum "15" saniye gözle
* Sehifeni yenile
* "Empty Cart Title" görsensin deye maksimum "15" saniye gözle
* "Cart Item Name" elementlerinin sayı "0" olmalıdır
* "Cart Protection Option" elementlerinin sayı "0" olmalıdır
* "Cart Total" elementlerinin sayı "0" olmalıdır
* Brauzeri bağla

## TC_CART_POS_023 Səbətdə qoruma proqramı seçimi Cəmi, Tam ödəmək və taksit blokunu yeniləyir
tags: regression, sebet

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* Səbətə iki fərqli məhsul əlavə et və səbəti aç
* "Cart Item Name" elementlerinin sayı "2" olmalıdır
* "Cart Total" görsensin deye maksimum "15" saniye gözle
* "Cart Total" elementinin metnini "cem0" olaraq yadda saxla
* "Cart Financing Price" elementinin metnini "taksit0" olaraq yadda saxla
* "Cart Protection Price" elementinin metnini "qoruma" olaraq yadda saxla
* "Cart Protection Option" elementine klik et
* "Cart Protection Option" elementinin "class" atributunda "product-services_item__active" olmalıdır
* "Cart Total" elementindəki rəqəm "${cem0}" və "${qoruma}" rəqəmlərinin cəminə bərabər olmalıdır
* "Cart Full Payment" elementindəki rəqəm "${cem0}" və "${qoruma}" rəqəmlərinin cəminə bərabər olmalıdır
* "Cart Financing Price" elementinin metni "${taksit0}" olmamalıdır
* "Cart Item Name" elementlerinin sayı "2" olmalıdır
* "Cart No Protection Option" elementine klik et
* "Cart Total" elementinin metni "${cem0}" olmalıdır
* "Cart Financing Price" elementinin metni "${taksit0}" olmalıdır
* Brauzeri bağla

## TC_PDP_POS_008 Qoruma proqramı seçimi yekun məbləği proqram qiyməti qədər artırır, ləğv bərpa edir
tags: pdp

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "https://ispace.az/category/iphone?filter_stock=1" siyahısından stokda olan ilk məhsulu aç
* "PDP Total Price" görsensin deye maksimum "15" saniye gözle
* "PDP Total Price" elementinin metnini "yekun0" olaraq yadda saxla
* "Protection Price" elementinin metnini "qoruma" olaraq yadda saxla
* "Protection Option" elementine klik et
* "Protection Option" elementinin "class" atributunda "product-services_item__active" olmalıdır
* "PDP Total Price" elementindəki rəqəm "${yekun0}" və "${qoruma}" rəqəmlərinin cəminə bərabər olmalıdır
* "No Protection Option" elementine klik et
* "No Protection Option" elementinin "class" atributunda "product-services_item-no-plan__active" olmalıdır
* "PDP Total Price" elementinin metni "${yekun0}" olmalıdır
* Brauzeri bağla

## TC_SRCH_NEG_005 Nəticəsiz sorğuda boş vəziyyət mesajı göstərilir
tags: axtaris, neg

* "chrome" brauzeri aç ve keçid et "https://ispace.az"
* Cookie bildirişini rədd et
* "Search Input" görsensin deye maksimum "15" saniye gözle
* "Search Input" elementine "qwertyzx123" yaz ve Enter düymesine bas
* URL "search?query=" içermelidir
* "Search Result Title" görsensin deye maksimum "15" saniye gözle
* "Search Result Title" elementinin metni "Axtarış nəticələri" olmalıdır
* Sehifede "Heç nə tapılmadı" yazısı olmalıdır
* Brauzeri bağla