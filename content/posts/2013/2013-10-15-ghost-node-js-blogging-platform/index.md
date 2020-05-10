---
author: dzgeek
date: 2013-10-15 22:24:21+00:00
draft: false
title: 'Ghost: منصة تدوين جديدة مبنية على Node.js تهدف إلى إعطاء التدوين نفسًا جديدًا'
type: post
url: /2013/10/ghost-node-js-blogging-platform/
categories:
- Web
tags:
- blogging
- ghost
- John O'Nolan
- node.js
- WordPress
- جوست
- نود جي إس
---

أطلق **John O'Nolan** -والذي سبق له العمل على أكثر من منصة تدوين شهيرة- **منصة تدوين جديدة** مبنية على **Node.js** سماها  **Ghost**  هدفها إعادة صياغة التدوين وإنعاشه من جديد، وذلك عبر توفير تجربة تدوين أمتع، أكثر بساطة وأكثر إنتاجية.

[![Ghost Blogging platform logo](Ghost-Transparent-for-LIGHT-BG.png)
](Ghost-Transparent-for-LIGHT-BG.png)

قبل بضغة أشهر، لاحظ O’Nolan أن منصات التدوين بدأت تأخذ منحى آخر غير **مجرد** **التدوين**، أو على الأقل ليس بشكل حر بسيط وتلقائي. قد يقول قائل، وما بال Wordpress؟ ما به Tumblr؟ أو ماذا ينقص Blogger؟ يا رجل، ألم تسمع بـ Medium؟

حسنا، كل منصات التدوين المذكورة أعلاه رائعة ولا غبار عليها، ولكنها لم تعد "مجرد منصة تدوين وفقط: التدوين" لا أكثر ولا أقل، فقد تعدت ذلك لثلاثة أمور:



	  * أولها، ومثال ذلك Wordpress، أنها كبرت شيئا فشيئا حتى أصبحت نظام إدارة محتوى، مما زاد من تعقيدها.
	  * ثانيها، أنها ليست حرة بما يكفي، فكل من Tumblr، Blogger أو حتى Medium عبارة عن منصات غير مستضافة على مساحتك، وبالتالي فأنت تخضع لقوانينهم وقيودهم، أي أنك لست حرًّا بما يكفي في "حرية التعبير"  (حسب من أطلق هذا المشروع) ثم إن هذه المنصات **هدفها ربحي** بشكل أو بآخر.
	  * أخيرا، كثرة الترهّات على هذه المنصات (Tumblr مثلا)، فتضيع المدونات/المواضيع الجادة في خضمّ تلك الهزلية أو الرديئة وتؤثر سلبا عليها.



[ ](Ghost-Transparent-for-LIGHT-BG.png)


من هنا، رأى [John O'Nolan](http://twitter.com/JohnONolan) أن ما هكذا التدوين بدأ، وما هكذا يجب أن يكون.
<iframe src="http://www.kickstarter.com/projects/johnonolan/ghost-just-a-blogging-platform/widget/card.html" style="margin: 5px;" align="left" height="380" width="220" scrolling="no" frameborder="0"></iframe>لو كانت هذه المبادرة من شخص عادي، فربما قد تعبُر بسلام، لكن أن تأتي من شخص عمل على عدة منصات تدوين لدى شركات كبيرة منها Microsoft، Nokia وحتى Wordpress نفسها فإن الخَطْبَ يستحق النظر.

قرر John شهر أبريل الماضي، أن يستعين بـ Kickstarter فأطلق [حملة يوضّح فيها نظرته للتدوين](http://www.kickstarter.com/projects/johnonolan/ghost-just-a-blogging-platform)، وكيف يجب أن يكون، وأخبر عن منصة Ghost التي عن طريقها يريد أن يجسد تلك النظرة ويُنعش التدوين بنَفَس جديد.

لاقت الحملة ترحيبا واسعا جدا وقبولا، وحصلت على -بل وتجاوزت- الدعم المطلوب (كما هو موضّح على يسار هذه الفقرة)، وتم إطلاق -كما وعد بذلك في حملته- منصة Ghost يوم أمسِ، وقد لاقت استحسانا وترحيبا بين مجتمع المطورين والمدونين، وصدًى على الشبكات الاجتماعية، حتى إن الكثير من مزودي الاستضافة تبنوا المنصة ودعموها بتسهيلات لتنصيبها على الخوادم.

ما يُميز **Ghost** عن غيرها هو أنها حرة (تحت رخصة **MIT**)، ومن يقف وراءها مؤسسة غير ربحية (الأمر أشبه بالعلاقة بين موزيلا ومتصفح فَيرفُكس)، هدفها شيء **واحد فقط، التدوين وفقط التدوين**. لا منصة بناء مواقع ولا أي نوع آخر من إدارة المحتوى، مع التركيز على كيفية تسهيل عملية **كتابة التدوينة**. كما أنها متاحة مجانا للتحميل، التعديل، النشر، التنصيب المحلي .. الخ

الفيديو التالية لـ [John O'Nolan](http://twitter.com/JohnONolan) نفسه، توّضح الأمر بالمختصر المفيد:

<iframe src="http://www.kickstarter.com/projects/johnonolan/ghost-just-a-blogging-platform/widget/video.html" scrolling="no" width="640" frameborder="0" height="480"></iframe>من الناحية التقنية:



	  * بُنيت المنصة على [Node.js](http://nodejs.org/) وإطار عمل [Express](http://expressjs.com/).
	  * طريقة كتابة التدوينات بها عن طريقة الـ [Markdown](http://ar.wikipedia.org/wiki/%D9%85%D8%A7%D8%B1%D9%83%D8%AF%D8%A7%D9%88%D9%86)، حيث تُقسم الشاشة لنصفين، نصف لكتابة التدوين والنصف الآخر للمعاينة الآنية لما تكتب. وبالتالي لن تحتاج أي محرر متقدم، فقط استمر في الكتابة وركز على محتواك.
	  * تعتمد افتراضيا على قواعد البيانات SQLite لأنها تفي بالغرض وتلغي الحاجة لتنصيب نظام قاعدة بيانات مما قد يزيد من اعتمادها لدى مزودي الاستضافات.
	  * نظام إضافات وقوالب جيد وسريع.
	  * لوحة تحكم أنيقة تعطيك نظرة شاملة حول مواضيع المدونة والشبكات الاجتماعية، مع قليل من الإحصائيات.

الجدير بالذكر أن من يقف وراء المنصة، ينوون توفير استضافة لها لهدف توفير مصدر دخل لتطوير المنصة نفسها.

قمت شخصيا بتجريب المنصة، وهي توفر حقا ما وعدت به مع تصميم أنيق، الشيء الوحيد الذي أراه ينقصها حاليا هو دعم للغات التي تُقرأ من اليمين إلى اليسار RTL.

موقع [المنصة](http://ghost.org/).

هل يا تُرى ستنجح منصة Ghost في ما ترمي إليه؟ أم أن الأمر نزوة عابرة؟