---
author: يوغرطة بن علي (Youghourta Benali)
date: 2011-01-24 19:07:36+00:00
draft: false
title: ترقيع من 20 سطر فقط يضاعف سرعة إقلاع Firefox  على أنظمة Windows
type: post
url: /2011/01/20-line-code-speed-up-firefox-windows/
categories:
- متصفحات
tags:
- Firefox
- Mozilla
---

**[ترقيع من 20 سطر فقط يضاعف سرعة إقلاع Firefox على أنظمة Windows](https://www.it-scoop.com/2011/01/20-line-code-speed-up-firefox-windows)**




هل تتذكرون [الـ Patch الذي يتكون من 200 سطر](https://www.it-scoop.com/2010/11/the-200-line-linux-kernel-patch-that-does-wonders/) و الذي يتيح تحسين أداء نظام Linux بشكل كبير ؟ أمر مشابه يحدث حاليا مع Firefox على أنظمة Windows و الذي يقسم زمن إقلاعه إلى نصفين بفضل Patch لا يتجاوز طوله 20 سطر برمجي.




[![](https://www.it-scoop.com/wp-content/uploads/2011/01/firefox-speed.jpg)
](https://www.it-scoop.com/2011/01/20-line-code-speed-up-firefox-windows)


هذا ما [أعلن عنه](https://bugzilla.mozilla.org/show_bug.cgi?id=627591) المطور Taras Glek و الذي لاحظ تحسنا يقدر بـ 40% على متصفح Firefox 4  -الذي لا يزال في الإصدار التجريبي- بفضل هذا  الترقيعه ، والذي لاقى ترحيبا من قِبَل جميع من جربه، حيث تقلص زمن الإقلاع في بعض الحالات إلى 50% و تظهر النتائج بشكل أفضل على الأقراص الصلبة البطيئة.

السبب الرئيسي وراء الإقلاع البطيء الذي يعرفه Firefox هو حاجته إلى تحميل مكتبات أساسية لإقلاعه منها xul.dll المسؤولة عن الواجهات الرسومية و mozjs.dllالمسؤولة عن محرك JavaScript، و يتم تحميلهما عبر قراءة أجزاء تتكون من 32 Kb ، و هنا يأتي دور الترقيع حيث يقوم بتحميل المكتبتين بقراءة أجزاء تتكون من 2 Mb .

و لقد أبدى Mike Shaver نائب رئيس قسم الهندسة لدى Mozilla اهتمامه بالترقيع حيث كتب تفاعل معه و كتب أكثر من تعليق ، مما يعني أنه من المحتمل أن يتم تضمينه لاحقا في المتصفح.

تجدر الإشارة إلى أن Chrome لا يزال حاليا في صدارة أسرع المتصفحات إقلاعا، و هو أسرع حتى من Internet Explorer رغم كونه مضمنا في النظام (على أنظمة Windows طبعا :)  ).
