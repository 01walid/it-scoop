---
author: يوغرطة بن علي (Youghourta Benali)
date: 2010-03-02 13:02:43+00:00
draft: false
title: ثغرة جديدة في الـ Internet explorer تجعل استعمال مفتاح F1 خطيرا
type: post
url: /2010/03/%d8%ab%d8%ba%d8%b1%d8%a9-%d8%ac%d8%af%d9%8a%d8%af%d8%a9-%d9%81%d9%8a-%d8%a7%d9%84%d9%80-internet-explorer-%d8%aa%d8%ac%d8%b9%d9%84-%d8%a7%d8%b3%d8%aa%d8%b9%d9%85%d8%a7%d9%84-%d9%85%d9%81%d8%aa%d8%a7/
categories:
- Microsoft
- Security
tags:
- internet explorer
- Microsoft
- Windows
---

[**ثغرة جديدة في الـ Internet explorer تجعل استعمال مفتاح F1 خطيرا**](https://www.it-scoop.com/2010/03/%d8%ab%d8%ba%d8%b1%d8%a9-%d8%ac%d8%af%d9%8a%d8%af%d8%a9-%d9%81%d9%8a-%d8%a7%d9%84%d9%80-internet-explorer-%d8%aa%d8%ac%d8%b9%d9%84-%d8%a7%d8%b3%d8%aa%d8%b9%d9%85%d8%a7%d9%84-%d9%85%d9%81%d8%aa%d8%a7/)


إذا كنت تستعمل متصفح Internet Explorer أيا كان إصداره، و إذا كنت لا تزال متشبثا بإحدى الإصدارات القديمة من نظام Windows و نقصد هنا كلا من Windows XP،  2000  و  Server 2003، فاحذر من استعمال مفتاح F1  على المتصفح  لو طلب منك أي موقع القيام بذلك، فالأمر لا يعدو كونه استغلالا لثغرة نشرت Microsoft يوم أمس تحذيرا منها.

[![](IE-problem.jpg)
](https://www.it-scoop.com/2010/03/%d8%ab%d8%ba%d8%b1%d8%a9-%d8%ac%d8%af%d9%8a%d8%af%d8%a9-%d9%81%d9%8a-%d8%a7%d9%84%d9%80-internet-explorer-%d8%aa%d8%ac%d8%b9%d9%84-%d8%a7%d8%b3%d8%aa%d8%b9%d9%85%d8%a7%d9%84-%d9%85%d9%81%d8%aa%d8%a7/)

يعود اكتشاف الثغرة إلى [Maurycy Prodeus](http://twitter.com/mprodeus) الباحث في الأمن و الحماية و الذي بين السيناريوهات  المحتملة لاستغلالها، و قامت Microsoft بعدها بتأكيد وجود الثغرة عبر[ نشرة خاصة بذلك](http://www.microsoft.com/technet/security/advisory/981169.mspx).

حسب Microsoft فإن الثغرة راجعة إلى خلل موجود  في آلية التواصل بين الـ VBScript و ملفات المساعدة ذوات الامتداد .hlp ، حيث يمكن استغلال ذلك باستدراج الضحية نحو موقع معد خصيصا لذلك، و يطلب منه الضغط على مفتاح F1 مما يسمح للمخترق تنفيذ كود معين على جهاز الضحية.

في انتظار صدور ترقيع للثغرة و التي قد يطول انتظارها شهورا، تنصح Microsoft مستخدمي متصفح Internet Explorer على أحد أنظمتها القديمة، تجنب استعمال المفتاح F1 و إيقاف الـ Process الخاص بـ Internet Explorer إن صادف أن  الموقع الذي تتم زيارته  يكرر طلب الضغط على مفتاح F1.
