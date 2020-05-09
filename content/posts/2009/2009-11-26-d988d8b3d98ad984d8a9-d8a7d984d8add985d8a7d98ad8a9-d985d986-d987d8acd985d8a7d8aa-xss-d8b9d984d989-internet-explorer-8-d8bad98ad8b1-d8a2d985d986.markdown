---
author: يوغرطة بن علي (Youghourta Benali)
date: 2009-11-26 09:38:26+00:00
draft: false
title: وسيلة الحماية من هجمات XSS على  Internet Explorer 8  غير آمنة
type: post
url: /2009/11/%d9%88%d8%b3%d9%8a%d9%84%d8%a9-%d8%a7%d9%84%d8%ad%d9%85%d8%a7%d9%8a%d8%a9-%d9%85%d9%86-%d9%87%d8%ac%d9%85%d8%a7%d8%aa-xss-%d8%b9%d9%84%d9%89-internet-explorer-8-%d8%ba%d9%8a%d8%b1-%d8%a2%d9%85%d9%86/
categories:
- Microsoft
- Security
- Web
- متصفحات
tags:
- internet explorer
- XSS
---

**وسيلة الحماية من هجمات XSS على  Internet Explorer 8  غير آمنة**



أعلنت مطور إضافة Noscript الخاصة بمتصفح Firefox عن أن الحماية المستعملة ضد هجمات XSS في المتصفح Internet Explorer 8 غير آمنة بل خطيرة.

![](https://djug.developpez.com/rsc/internet_explorer-8.jpg)


حسب Giorgio Maone و الذي لم يكشف بعد عن تفاصيل الأمر أن الأمر برمته مبني على خطأ في التصميم الأساسي مما يتوجب إعادة النظر في التصميم.

و يضيف Maone أن نظام الحماية من هجمات XSS في المتصفح Internet Explorer 8 على خلاف مع الإضافة Noscript فإنه يقوم بتحليل إجابات الخوادم و ليس طلبات المستخدمين ، مما يمكن للمهاجمين من التلاعب في إجابات الخوادم و حقن شيفرة معينة لتنفيذها.

لكن حسب Maone فإنه يجب على المهاجم أن يملك بعضا من الصلاحيات على الصفحات التي تتم زيارتها، و هذا الأمر ممكن حاليا في كل من صفحات الشبكات الاجتماعية و المنتديات و الـ wikis  و حتى  Google Apps .

لكن حسب مكتشف الثغرة فإن الظاهر أن  Google على علم بالثغرة إذ أنها تقوم بتعطيل تلك الحماية بإرسال الترويسة  X-XSS-Protection: 0 مما يجعل من استغلال الثغرة أمرا غير ممكن.

المصدر:

[http://hackademix.net/2009/11/21/ies-xss-filter-creates-xss-vulnerabilities/](http://hackademix.net/2009/11/21/ies-xss-filter-creates-xss-vulnerabilities/)
