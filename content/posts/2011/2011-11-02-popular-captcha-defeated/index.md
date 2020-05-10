---
author: يوغرطة بن علي (Youghourta Benali)
date: 2011-11-02 17:46:06+00:00
draft: false
title: خبراء أمنيون يتمكنون من حل Captcha كبريات المواقع، وخدمة reChaptcha  تصمد أمام
  الهجمات
type: post
url: /2011/11/popular-captcha-defeated/
categories:
- Security
- Web
tags:
- Captcha
- Decaptcha
- Elie Bursztein
- John C. Mitchell
- Matthieu Martin
- Recaptcha
---

هناك مزحة يتداولها المبرمجون عادة والتي يقول فيها أحدهم: "لقد تأكدت لتوي من أنني كائن بشري" ، فيسأله أحدهم باستغراب: "وكيف ذلك؟"، فيجيب المبرمج : "لقد تمكنت من حل **Captcha** ، ذلك يعني أني كائن بشري". أعتقد أن هذه المزحة لن تصمد طويلا قبل أن تدخل كتاب "المزح التي لم يعد بإمكانك استعمالها من جديد"، وهذا ما تخبرنا به أحدث دراسة صادرة من جامعة Stanford حول هذا الموضوع.




[![recaptcha example](recaptcha-example.gif)
](recaptcha-example.gif)




فقد تمكن الباحثون التالية أسماؤهم:  **Elie Bursztein**, **Matthieu Martin**  و  **John C. Mitchell** من [التعرف على محتوى Captcha لأشهر المواقع](http://elie.im/publication/text-based-captcha-strengths-and-weaknesses) بنسب نجاح معتبرة وصلت إلى غاية 70% على موقع لعبة World of Warcraft. في حين لم يفشل الباحثون في تجاوز **Captcha** موقع eBay إلا في 43% من الحالات، وتتدنى نسبة النجاح لتصل إلى 20% على موقع Digg و 5% فقط على موقع Baidu الصيني.




ولم تسلم من أيادي الباحثين الثلاث سوى Google التي تملك **Captcha** يعجز في الكثير من الحالات حتى الآدميون الأسوياء عن حلها، إضافة إلى خدمة **[reCaptcha](http://www.google.com/recaptcha)** التي قامت بشرائها سابقا. وقد كانت نتائج هذه البحوث كفيلة بإقناع مواقع مثل Authorize.net أو Digg إلى الاعتماد بشكل كامل على هذه الخدمة.




ولتحسين أداء **Captcha** بشكل عام يضع الباحثون بيد أيدي المهتمين [دراستهم](http://cdn.ly.tl/publications/text-based-captcha-strengths-and-weaknesses.pdf) التي تلقي الضوء على نقاط الضعف التي تعرفها الخدمات الحالية، إضافة إلى جملة من النصائح لتقويتها وتحسين أدائها بشكل معتبر.




كما أنه يمكن الحصول على العرض التقديمي (بصيغة PDF) الذي رافق هذه الورقة البحثية [من هنا](http://cdn.ly.tl/publications/text-captcha-strenghts-and-weaknesses-ccs-2011-slides.pdf).




تجدر الإشارة إلى أن للباحثين الثلاثة أعمال سابقة تخص **Captcha** خاصة الصوتية منها حيث كتبوا تطبيق **[Decaptcha](http://news.stanford.edu/news/2011/may/captcha-security-flaw-052311.html)** الذي يتمكن من اجتياز حجاز **Captcha** الصوتية للعديد من المواقع العالمية مثل Yahoo، Microsoft و eBay، حيث يتكفل التطبيق بالاستماع إلى الملف الصوتي وتحليل محتواه بنسب نجاح تصل إلى غاية 50%.




للتذكير فإن **[Captcha](http://en.wikipedia.org/wiki/CAPTCHA)** عبارة عن آلية يُراد بها التمييز بين الآلات والبشر الذين يزورون مواقع معينة وذلك بوضعهم أمام اختبار "فك تشفير" كلمة أو جملة تمت تشويهها. وهي اختصار للعبارة التالية: Completely Automated Public Turing test to tell Computers and Humans Apart.




في رأيك إلى متى ستصمد Captcha أمام محاولات المخترقين؟



