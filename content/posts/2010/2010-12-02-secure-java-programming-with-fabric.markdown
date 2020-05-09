---
author: dzgeek
date: 2010-12-02 09:25:03+00:00
draft: false
title: إطلاق لغة Fabric، التي تعزز أمن الـ Java من داخلها!
type: post
url: /2010/12/secure-java-programming-with-fabric/
categories:
- Security
- برمجيات
- عام
tags:
- cloud computing
- distributed systems
- fabric
- Java
- oracle
- Security
- sun
---

**[إطلاق لغة Fabric، التي تعزز أمن الـ Java من داخلها!](http://www.it-scoop.com/2010/12/secure-java-programming-with-fabric)**


لغرض تعزيز أمن التطبيقات التي تعمل على الأنظمة الموزعة، تمكن ست باحثون  لدى جامعة [Cornell University](http://www.cornell.edu/) الأمريكية من إخراج لغة برمجة ذي نمط أمني تحت اسم: [Fabric](http://www.news.cornell.edu/stories/Sept10/Fabric.html) تسمح بزرع إجراءات أمنية على برامج الـ Java.


هذه محاولتنا لترجمة مخطط مبدأ اللغة القائمة عليه




[![](http://www.it-scoop.com/wp-content/uploads/2010/12/fabric_ar.jpg)
](http://www.it-scoop.com/2010/12/secure-java-programming-with-fabric)يمكن الرجوع للمخط الأصلي من خلال المصدر أدناه








تعتبر Fabric من لغات البرمجة ذي نمط أمني أو security-typed programming language وهي في الأصل امتداد للغـة [Jif](http://www.cs.cornell.edu/jif/) ، وتعتمد فكرتها الأساسية على النظار - جمع ناظر إن صحت الترجمة وهو أشبه بالمدير في المدرسة- هذا الأخير هو الذي يصوغ ويزرع المتطلبات الأمنية، وهناك علاقات وعمال تسمح للمستخدمين، العمليات، المجموعات، ووحدات التطبيقات أن تتبع نموذجا أمنيا خاصا بها، كل على حدة، وللنظار صلاحيات القراءة والكتابة على الكائنات المصاغة في 'labels'. فمثلا int {Alice Bob} x يحدد أن الناظر Alice يتحكم في المتغيرة `x` وأن لـ Bob  صلاحية النفاذ لقيمتها. الأمر {Alice←Bob} يسمح لـ Bob أن يغير من قيمة x أثناء وقت التصريف compilation. والمصرف compiler يفحص إذا كان الكود المصدري يحترم صلاحيات النفاذ إلى الكائنات وباقي المعايير الأمنية. عندها يولد كود Java ويمرره إلى  standard Java compilers لمزيد من المعالجة.

كما أن الكائن "أ" مثلا لا يملك صلاحيات القراءة/الكتابة على الكائن "ب" . وهكذا نتحصل على أمن جوهري مضمن في البرمجية.

عدة خيوط معالجة تتشارك في برنامج Fabric قيد التشغيل، عُقد تخزين تدير الكائنات، عقد عاملة تشغل البرمجية وعقد نشر/توزيع أخرى توفر نسخ من الكائنات لتخفيض عبئ العمل على عقد التخزين. كل هذه العمليات يمكنها أن تعمل على نفس الآلة، عادة باستخدام JVM أو شبكة موزعة.

إذا كان ما سردناه سابقا يبدو مبهما فيمكنك الإطلاع على [هذا المقال العلمي ](http://www.cs.cornell.edu/andru/papers/fabric-sosp09.pdf)الذي نشره الباحثون نفسه.

النسخة الأولى من لغة Fabric, للتحميل مجانا [من هنا](http://www.cs.cornell.edu/Projects/fabric/releases/fabric-0.1.0.tar.gz). وهنا[ إعلان](http://www.news.cornell.edu/stories/Sept10/Fabric.html) الباحثين. من جامعة cornell.

- ما رأيك بهكذا آلية؟ وهل سنرى استنساخا لها في لغات برمجة أخرى؟
