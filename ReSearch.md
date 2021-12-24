## Python

### ReSearch Topics

- Function in Python

    - Python-da Functionlar hesablama, məntiqi və ya qiymətləndirmə tapşırığını yerinə yetirmək üçün nəzərdə tutulmuş əlaqəli ifadələr blokudur. İdeya bundan ibarət ki, bəzi ümumi və ya dəfələrlə yerinə yetirilən tapşırıqları bir araya gətirmək və bir function yaratmaq, fərqli sectionlar üçün eyni kodu təkrar-təkrar yazmaqdansa , onun tərkibində olan kodu təkrar istifadə etmək üçün function çağırmaq kifayət edəcək. (DRY - Don't Repeat YourSelf)

- While Loop

    - Python While Loop , verilmiş şərt icra olunana qədər bir neçə dəfə ifadələr blokunu yerinə yetirmək üçün istifadə olunur, Və şərt yalnış olduqda, proqramda loop-dan dərhal sonrakı sətir yerinə yetirilir. While loop qeyri-müəyyən iterasiya kateqoriyasına düşür . Qeyri-müəyyən iterasiya o deməkdir ki, dövrənin neçə dəfə yerinə yetirildiyi əvvəlcədən açıq şəkildə göstərilmir. 

- Dictionary

    - Python-da Dictionary Map kimi data value-larını saxlamaq üçün istifadə edilən sıralanmamış verilənlər toplusudur, element kimi yalnız bir dəyəri saxlayan digər məlumat növlərindən fərqli olaraq Dictionary key: value cütünü saxlayır . Dictionary-də onu daha optimallaşdırmaq üçün key-value verilir. 

- CRUD

    - CRUD müvafiq olaraq daxil etmək, oxumaq, yeniləmək və silmək üçün qısaltmadır. Məlumat anbarına qeydlərin əlavə edilməsi, oxunması, yenilənməsi və silinməsi (bu adətən verilənlər bazalarına aiddir) CRUD ilə ifadə edilir, Bu abbreviatura ingilis dilindən *Create*, *Read*, *Update*, *Delete* sözlərindən ibarətdir.

- Modules

    - Python'da yazdığımız hər proqram əslində bir moduldur. Python'un bu baxımdan bizə verdiyi üstünlük isə bir növ function kimi modulları da istədiyimiz proqramın içində çağıra bilərik. Bu isə bizi kod təkrarından azad edir. Modullar 2 yerə bölünür:

        - Öz yazdığımız modullar
        - Hazır modullar

    - Hər yazdığımız .py faylının bir modul olduğunu qeyd etdik. Python bizim işimizi tezləşdirmək və asanlaşdırmaq üçün bizə hazır moddullar verir. Hazır modullar da öz içində 2 yerə bölünür:

        - Standart Library Modules
        - Third Party Modules

    - Standart kitabxana modulları pyhton yükləyəndə hazır gələn modullardır. Üçüncü şəxs modulları isə üçüncü şəxslər tərəfindən yazılıb istifadəyə verilən modullardır.

- Package 

    - Package modullar toplusudur deyə bilərik. Modulardan daha geniş bir qavramdır. Python'da ümumiyyətlə package'lərdən çox istifadə olunur. Hər sahə üçün ayrı bir package var. Məsələn, web application yazmaq üçün django, flask istifadə olunur. Yəni, bu framework'lər özlüyündə bir neçə moduldan ibarətdir.

- Differences between Module and Package

    - Yuxarıda da qeyd etdiyim kimi, package modullar toplusudur. Məsələn, os.py bir moduldur, django isə package'dir. Eyni zamanda hər package bir moduldur, ancaq modullar bir package deyildir. Yəni 'venv' package'inə biz 'venv' modulu da deyə bilərik.

- JSON

    - JSON (javascript Object Notation) — sadə verilənlər strukturlarını təmsil etmək üçün nəzərdə tutulmuş bir standalone məlumat mübadiləsi formatıdır. Əsasən iki sistem arasında məlumat mübadiləsi üçün istifadə olunur. Məsələn, JSON-dan istifadə edərək server və veb tətbiqi arasında məlumat ötürə bilərsiniz.

- Differences between Library and FrameWork

    - Library və FrameWork fərqləndiyi məqam texniki hissədir. İkisi arasındakı əsas texniki fərq kodun necə çağırıldığıdır. Library-dən istifadə edərkən library sizə bəzi xüsusiyyətlər verərək ondan istifadə etmənizi təmin edir, bu sayədə aldığınız kodu öz sisteminizdə tətbiq edərkən kodu harada və nə vaxt istifadə edəcəyinizə müdaxilə etmir və ya diktə etmir. Digər tərəfdən, Framework, Library-dən fərqli olaraq, kodu harada və nə vaxt istifadə edəcəyimizi xüsusiyyətinə uyğun olaraq söyləyir, və biz bu funksiyadan istifadə edəcəyik, əgər Framework sənəddə göstərildiyi kimi istifadə edilməsə, istifadədən çıxacaq.

- PIP

    - PIP python paketlərini idarə etmə sistemidir.PIP vasitəsi ilə python proqram təminatı paketlərini yükləmək və idarə etmək mümkündür,PIP Python paketləri və ya istəsəniz modullar üçün paket meneceridir.


- Web Server 

    - Web Server istifadəçilərin internetdəki web-səhifələrə və digər verilənlərə daxil olmasına şərait yaradan xüsusi proqramlar ilə təmin olunmuş kompüterdir. Web-server web-saytın əsasını təşkil edir. Web-server informasiyaların saxlanılmasını, təşkilini və göndərilməsini təmin edir. Web-server web-brauzerdən qəbul etdiyi sorğu əsasında soruşulan sənədin elektron surətini istifadəçiyə göndərir. Belə sorğuların emal edilməsi və yerinə yetirilmə ardıcıllığı HTTP protokolu vasitəsilə yerinə yetirilir.

- WSGI 

    - Web Server Gateway Interface - Python'da yazılan kodun web-serverin başa düşəcəyi hala gətirən interfeysdir. Veb server request'ləri WSGI'ə göndərir, WSGI isə proramınızı işə salıb bu requestin cavablarını HTML olaraq veb serverə çatdırır.

- Differences between WSGI and Web Server

    - WSGI, veb serverdən fərqli portda işləyir. Yəni, veb serverlər pythonda yazılmış kodu başa düşmürlər bunun üçün WSGI'dən istifadə edirlər

- HTTP Request 
    
    - Client server tərəfindən veb serverə verilən sorğudur. Əsas iki yerə bölünür:

        - GET request
        - POST request
        
- HTTP GET,POST Request

    - GET request veb serverdən sadəcə məlumat alır.    
    - POST request isə veb serverə məlumat daxil edir.

- BookStore
    
    - Demeli ilk once 3 eded class yaradilmalidir .
        
        - book_info (class-name)

            - def init ( 
                - book_topic
                - book_year
                - book_page
                - book_author
            )

        - book_sales (class-name)

            - def init ( 
                - book_number
                - book_cost
                - book_sale
            )

        - store_employes (class_name)

            - def init ( 
                - store_staff
                - store_name
                - store_surname
                - store_salary
            )

- OOP ( Abstraction, İnheritance, Encapsulation and Poplymorphism )

    - Yaxşı kod dizaynı üçün riayət edilməli olan bəzi prinsiplər var. Prinsiplər məcburi deyil, lakin onlara əməl edildikdə, biz dünya miqyasında standart kod yazmış oluruq. Əslində, hər hansı bir proqramlaşdırma dilində bir az məlumatınız varsa, yəqin ki, bu prinsiplərdən istifadə edirsiniz, lakin onların adlarını bilmirsiniz.
        
        - OOP 

            - OOP ( Objected Oriented Programming ), adından da göründüyü kimi, obyekt yönümlü proqramlaşdırma texnikasıdır. Başqa sözlə, bu proqramlaşdırma texnikasında hər şey bir obyektdir. Bəs bu obyekt nədir? Obyektlərin mövcud və ya qurulmuş strukturlarımızın nümayəndələri və ya nümunələri olduğunu deyə bilərik (type və ya classda deyə bilərik). Real həyatdan misal gətirsək, Biz öz növümüzün bir nümunəsi olduğumuz üçün hamımız obyektik. Gördüyümüz hər şey bir obyektdir. Ətrafımızda mövcud olan hər şey bir obyektdir. OOP əsasında 2 növ proqramlaşdırma dili var: Class əsaslı Məsələn, C# və Prototip əsaslı Məsələn, Javascript.

                - Abstraction

                    - Abstraction lazımsız təfərrüatlara məhəl qoymamaqla və məqsəd üçün vacib olana diqqət yetirməklə classların müəyyənləşdirilməsi prosesidir. Müəyyən bir tətbiq üçün nəyin uyğun olduğuna diqqət yetirmək üçün lazımsız detalların abstraksiyasından bəhs edir. Buradan başlasaq, ətrafımızda gördüyümüz hər şey əslində abstraksiyaya daxildir. Yəni gördüyümüz qədər mövcuddurlar. Abstraksiyaya avtomobilin idarə olunması prinsipindan numune verek : Sürücünün qaz pedalına və əyləcə basdıqında və ya skorsu dəyişdirdiyi zaman nə baş verdiyini bilməsi lazım deyil. O, yalnız giriş və çıxışları öyrənərək avtomobili rahatca idarə edə bilər.

                - Encapsulation

                    - Deyə bilərik ki, Encapsulation, yaratdığımız struktur daxilində detalları gizlətmək və/və ya əhatə etmək üçün istifadə edilən bir texnikadır. Yenə telefonla davam etsək, Bizim daxil ola biləcəyimiz düymələrimiz var ( təbiiki qalmişsa əgər ), Bu düymələrlə əməliyyatlar edərkən arxa tərəfdə məlumatların harada saxlandığı və ya arxa tərəfdəki proseslər və s. kimi xüsusiyyətlərə girişimiz yoxdur. Biz yalnız public funksiyalara daxil ola bilərik.(Acces Modifiers)

                - Inheritence

                    - Varislik , Xüsusiyyətin bir obyektdən digər obyektə köçürülməsidir. Valideynlərdən övladlarına keçən xüsusiyyətləri misal göstərə bilərik. Burada məqsəd reusebility’i  təmin etməkdir. İrsi alinan class Base class və ya Super-class, İrsi qalan class isə Sub class və ya Derived class adlanır.

                - Polymorphism  

                    - Polimorfizm, Base Class daxilinde yer alan bir davranisi, Derived Class icerisinden deyisdire bilmek qabiliyyetini təmin etməklə mesgul olur. Yeni Base class daxilinde davranış override ediləbilmektedir. İndiki şəraitdə misal gətirsək, Hər bir futbolçunun özünəməxsus xüsusiyyətləri var, Futbolçu bizim Baza Classimizdir, Və vəzifələr var. Müdafiəçi, Yarımmüdafiəçi, Hücumçu. Qoy bunlar bizim Derived class-larimiz olsun. İstənilən oyunçu pas ata bilər. Amma bütün oyuncular pas-i eyni sekilde ata bilmez . Buna görə də, pas ilə əlaqəli xüsusiyyət, yerə görə override oluna bilər.