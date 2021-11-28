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

- Differences between module and package

    - Yuxarıda da qeyd etdiyim kimi, package modullar toplusudur. Məsələn, os.py bir moduldur, django isə package'dir. Eyni zamanda hər package bir moduldur, ancaq modullar bir package deyildir. Yəni 'venv' package'inə biz 'venv' modulu da deyə bilərik.

- JSON

    - JSON (javascript Object Notation) — sadə verilənlər strukturlarını təmsil etmək üçün nəzərdə tutulmuş bir standalone məlumat mübadiləsi formatıdır. Əsasən iki sistem arasında məlumat mübadiləsi üçün istifadə olunur. Məsələn, JSON-dan istifadə edərək server və veb tətbiqi arasında məlumat ötürə bilərsiniz.


- Web Server 

    - Web Server istifadəçilərin internetdəki web-səhifələrə və digər verilənlərə daxil olmasına şərait yaradan xüsusi proqramlar ilə təmin olunmuş kompüterdir. Web-server web-saytın əsasını təşkil edir. Web-server informasiyaların saxlanılmasını, təşkilini və göndərilməsini təmin edir. Web-server web-brauzerdən qəbul etdiyi sorğu əsasında soruşulan sənədin elektron surətini istifadəçiyə göndərir. Belə sorğuların emal edilməsi və yerinə yetirilmə ardıcıllığı HTTP protokolu vasitəsilə yerinə yetirilir.

- WSGI 

    - Web Server Gateway Interface - Python'da yazılan kodun web-serverin başa düşəcəyi hala gətirən interfeysdir. Veb server request'ləri WSGI'ə göndərir, WSGI isə proramınızı işə salıb bu requestin cavablarını HTML olaraq veb serverə çatdırır.


Web Server və WSGI arasındakı fərqlər nələrdir?
WSGI, veb serverdən fərqli portda işləyir. Yəni, veb serverlər pythonda yazılmış kodu başa düşmürlər bunun üçün WSGI'dən istifadə edirlər


HTTP Request nədir?
Client server tərəfindən veb serverə verilən sorğudur. Əsas iki yerə bölünür:

GET request
POST request
GET,POST request nə deməkdir?
GET request veb serverdən sadəcə məlumat alır.
POST request isə veb serverə məlumat daxil edir.


Flask framework necə işləyir?
Web saytın işləmə məntiqi

Flask (django da həmçinin) jinja2 templete dilindən istifadə edir. Flask ümumiyyətlə python üçün yazılmış bir framework'dür. Vebə bir request göndərdiyimiz zaman, məlumat database'dən alınır, ORM'ə ötürülür, ordan flask framework'ə daha sonra isə HTML olaraq bizə qayıdır.
URL nədir? Detalları nədən ibarətdir?
Uniform Resource Loader - kompüterin serverlə əlaqə qurması üçün istifadə olunur. Domain kimi, ip ünvanlarını sözə çevirərək daha asan yaddaqalan edir.
Virtual environment nədir? Nə üçün istifadə olunur?
Hər bir layihə üçün ayrıca virtual bir mühit yaratmaq üçün istifadə olunur. Əgər hər layihə üçün eyni flask'dən istifadə etsək, flask'də baş verəcək hər dəyişiklik (update) avtomatik olaraq bütün layihələrdə dəyişəcək. Bu isə bir çox hallarda istəməyəcəyimiz bir şeydir. Bu səbəbdən virtual environment bizim üçün daha əlverişlidir.