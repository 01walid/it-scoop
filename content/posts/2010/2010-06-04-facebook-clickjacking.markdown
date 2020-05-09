---
author: Xacker
date: 2010-06-04 11:27:19+00:00
draft: false
title: مستخدمو Facebook يقعون ضحايا للـ Clickjacking
type: post
url: /2010/06/facebook-clickjacking/
categories:
- Security
- Web
tags:
- Clickjacking
- facebook
---

[**مستخدمو Facebook يقعون ضحايا للـ Clickjacking**](https://www.it-scoop.com/2010/06/facebook-clickjacking/)


مئات آلاف مستخدمي Facebook وقعوا ضحايا ما يسمى بهجمات "clickjacking"، حيث يظهر لهم  روابط بعناوين مثيرة إلى مواضيع مثل "هذا الرجل  يلتقط صورة لنفسه يومياً منذ 8 سنوات!!"، والتي يظهر أن أحد أصدقائهم قد  "استحسنها" Like it.


![](https://www.it-scoop.com/wp-content/uploads/2009/11/facebook-logo.jpg)



النقر على هذا الرابط يخدع المستخدمين حيث  يقوم بإظهار هذا الموضوع على أنه موضوع مستحسن من طرفهم أيضاً، العملية تتم لما يقوم المستخدم بالنقر على الرابط الذي يأخذه إلى صفحة فارغة تحوي فقط على النص "انقر هنا للمتابعة".

النقر في أي مكان في تلك الصفحة يقوم بنشر عبارة الاستحسان في صفحة المستخدمين الشخصية (Like it).

هذا الهجوم يقوم باستخدام طريقة clickjacking في خطف حدث النقر وتوجيهه إلى زر مخفي ضمن الصفحة أينما نقرت، في هذه الحالة هذا الزر هو زر "Like" في Facebook.

يقول الخبراء بأن هذا الاحتيال حالياً لا يحوي أي أهداف خبيثة لكن من السهل تحويله ليقوم بنشر برمجيات خبيثة والتي يمكن أن تصيب الأجهزة وتسبب الأذى للبيانات.


[![](https://www.it-scoop.com/wp-content/uploads/2010/06/Click-Here-to-continue.jpg)
](https://www.it-scoop.com/2010/06/facebook-clickjacking/)


لقراءة المزيد من التفاصيل حول الخبر يمكن مراجعة تحذير Sophos حول القضية من [هنا](http://www.sophos.com/pressoffice/news/articles/2010/06/clickjacking.html).


http://www.dailymail.co.uk/sciencetech/article-1283763/Facebook-clickjacking-attack-spreads.html?ITO=1490
