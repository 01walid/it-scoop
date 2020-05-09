---
author: يوغرطة بن علي (Youghourta Benali)
date: 2013-04-26 09:56:27+00:00
draft: false
title: SkySQL وMonty Program تندمجان وتعلنان عن تحويل MariaDB إلى قاعدة بيانات NewSQL
type: post
url: /2013/04/skysql-mariadb-newsql/
categories:
- Open source
- برمجيات
tags:
- MariaDB
- Monty Program
- Mysql
- NewSQL
- NoSQL
- SkySQL
- SQL
---

أعلنت كل من **SkySQL** و**Monty Program**** **اندماجهما مع بعض في خطوة تهدف إلى جعل **MariaDB** الخيار الأفضل لكل مستخدمي أنظمة قواعد البيانات العلائقية الي تعتمد على لغة **SQL** إضافة إلى قواعد البيانات من صنف **NoSQL**.




[![mariadb-SkySQL](http://www.it-scoop.com/wp-content/uploads/2013/04/mariadb-SkySQL.png)
](http://www.it-scoop.com/wp-content/uploads/2013/04/mariadb-SkySQL.png)




قد يبدو الوضع مُبهما بعض الشيء، دعونا نفصل الفقرة السابقة جملة جملة. كما هو معروف فإن MySql تُعتبر قاعدة البيانات العلائقية [Relational database](https://en.wikipedia.org/wiki/Relational_database) مفتوحة المصدر الأكثر شهرة والأكثر انتشارا، للأسف (أو لحسن الحظ) الوضع لم يعد كسابق عهده (فيما يخص الجانب المتعلق بكونها مفتوحة المصدر)، والسبب هو التغيير الذي طرأ على آلية تطويره بعد أن سقط في يد Oracle. ما علاقة Oracle بكل هذا؟ بكل بساطة، سبق لـ Oracle أن اشترت Sun، وقبل ذلك اشترت Sun شركة MySQL AB التي كانت تطور هذا النظام. بعبارة أخرى أصبح مستقبل MySql في يد Oracle والتي تطور منتجات منافسة غير مفتوحة المصدر.




الآن بعد أن حدث كل ذلك، قرر موظفون سابقون لدى MySql أن يواصلوا نفس العمل الذي كانوا يقومون به لكن على طريقتهم الخاصة وعبر شركاتهم الجديدة الخاصة، حيث تم [أطلقت شركة Monty AB نظام MariaDB بداية 2010](http://www.it-scoop.com/2010/01/%d8%a5%d8%b7%d9%84%d8%a7%d9%82-mariadb-5-1-%d8%a7%d9%84%d9%85%d8%b4%d8%a7%d8%a8%d9%87-%d9%88-%d8%a7%d9%84%d9%85%d9%86%d8%a7%d9%81%d8%b3-%d9%84%d9%80-mysql-%d8%b0%d9%88-4-storage-engine/) والذي يُعتبر [Fork](http://en.wikipedia.org/wiki/Fork_(software_development)) لنظام MySQL متوافق معه بشكل كامل، ثم تلاها بعد ذلك [في أواخر 2010 إنشاء شركة SkySQL](http://www.it-scoop.com/2010/10/skysql/)  التي تهدف إلى تقديم الدعم الفني لكل من MySql وMariaDB.




لكن ما محل NoSQL من الإعراب؟ NoSQL والتي تعني [Not only SQL](https://en.wikipedia.org/wiki/NoSQL)  تهدف إلى توفير آلية للإجابة على متطلبات تطبيقات الويب الحديثة والتي لا يُمكن الإجابة عنها من خلال قواعد البيانات العلائقية، خاصة ما تعلق منها بالتعامل مع بيانات غير المنظمة Unstructured Data (يمكن أخذ فكرة حول الأمر بقراءة [مقال NoSQL على Wikipedia](https://en.wikipedia.org/wiki/NoSQL))، ولقد ظهرت عدة أنظمة لإدارة قواعد البيانات NoSQL لعل من أشهرها MongoDB، [Cassandra](http://www.it-scoop.com/2010/04/apache-cassandra-0-6-released/). بعبارة أخرى تُعتبر أنظمة NoSQL منافسة مباشرة لأنظمة SQL الكلاسيكية ولدى تصميم أي تطبيق (ويب) جديد فإنه يجب عليك أن تختار إما هذا أو ذاك، ولضمان مستقبل لمنتجهم قررت الشركتان آنفتي الذكر اختيار أفضل ما يوجد في SQL ومزجه مع أفضل ما يوجد في NoSQL  لتكوين [NewSQL](http://en.wikipedia.org/wiki/NewSQL) (يبدو بأن مبدأ NewSQL هو نتيجة أعمال Michael Stonebraker العقل الذي يقف وراء نظامي Ingres و Postgres، حسب [هذا المقال](http://www.lemondeinformatique.fr/actualites/lire-newsql-pour-combiner-le-meilleur-de-sql-et-nosql-34475-page-1.html) على موقع Le Monde Informatique الفرنسي) واستخدامه في نظام MariaDB.




[أشارت](http://www.skysql.com/news-and-events/press-releases/skysql-merges-with-mariadb-developers) SkySQL إلى أنها ستواصل توفير الدعم الفني لزبائنها الذين يستخدمون قواعد البيانات MySQL (إلا أن يقرروا الانتقال إلى MariaDB، والتي -كما سبق ذكره- تتوافق كلية مع MySQL)، كما أنها انضمت إلى مؤسسة MariaDB Foundation لتساهم في تطوير النظام (بالمال وبالموارد).




تجدر الإشارة إلى أن ويكيبيديا [أعلنت](http://blog.wikimedia.org/2013/04/22/wikipedia-adopts-mariadb/) مؤخرا عن تخليها عن [نسخة مطورة من طرف فيس بوك من نظام MySql](https://launchpad.net/mysqlatfacebook/51) لصالح MariaDB وهو ما يُعتبر مسمارا إضافيا يُدق في نعش MySQL والذي يعرف هجرة جماعية منه إلى منافسيه، حيث أعلنت عدة توزيعات لينكس عن انتقالها إلى MariaDB مؤخرا، على غرار كل من [فيدورا وOpenSuse](http://www.it-scoop.com/2013/02/fedora-opensuse-replace-mysql-mariadb/).




هل لا تزال تعتمد على MySQL؟ لماذا؟ هل قررت التحول إلى MariaDB؟ لماذا يتم تجنب PostgreSQL في كل مرة يتم الحديث فيها عن بدائل لـ MySQL؟



