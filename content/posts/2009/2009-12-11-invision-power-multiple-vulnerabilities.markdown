---
author: Xacker
date: 2009-12-11 10:30:24+00:00
draft: false
title: Invision Power multiple vulnerabilities
type: post
url: /2009/12/invision-power-multiple-vulnerabilities/
categories:
- Security
- Web
- برمجيات
tags:
- Cross Site Scripting
- Invision Power
- IPB
- SQL injection
- XSS
---

قامت شركة Invision Power المنتجة لمنتديات IP.Board الشهيرة بطرح الإصدار 3.0.5 من نسخة IP.Board الذي يحمل في طيّاته ترقيعات أمنية لثغرتين، الأولى ثغرة SQL injection و Local File Include، الثانية ثغرة XSS قمت بإبلاغهم بها بعد (استمرار) وجودها في الإصدار الأخير 3.0 لمنتديات IP.Board (فهي موجودة في الإصدارات القديمة لكني لم أبلّغ عنها :P).

![](https://www.it-scoop.com/wp-content/uploads/2009/12/untitled.PNG)


ثغرة XSS تصيب العديد من منتجات الشركة، IP.Board / IP.Gallery / IP.Community Blog بإصداراتها المختلفة.

يمكن استغلال ثغرة XSS من خلال الملفات text-based والتي يمكن إرفاقها في المنتديات ضمن المواضيع والمشاركات.

الأمر الجيد، الاستغلال يعمل على إصدارات متصفح +5 Internet Explorer فقط، ولكي ينجح المخترق باستغلال الثغرة عليه أن يقنع مستخدماً ما بتصفح ملف txt مرفق.

سبب المشكلة، الـ MIME type المحدد لملفات txt هو application/x-dirview - بناء عليه يقوم متصفح IE بمعالجة محتويات الملفات إن كانت HTML/JavaScript بينما تقوم باقي المتصفحات بإظهار نافذة لتحميل الملف ولا تقوم بمعالجته ضمن المتصفح.

لتصحيح الخطأ يكفي استبدال الـ MIME type بـ text/plain، وحينها سيتم إظهار محتويات الملف كاملة بدون parsing.

فيما يتعلق بالإصدارات 3.0.0 حتى 3.0.4 فقد تم إدخال آلية جديدة تقوم بتفحص محتويات الملفات المرفقة، النصّية فقط غالباً، وتمنع إرفاق هذه الملفات في حال احتوت على HTML tags يبدو أنها محددة سابقاً، مثل: <body>, <script>, ...
يمكن تجاوز هذه الآلية بأبسط صيغة ممكنة، فيما يلي PoC:


    
    <span onmouseover="javascript:alert('XSS is active');
    function fakeLoginPage(){...}">مرر المؤشر هنا</span>


يمكن كتابة توابع كاملة أو حتى استيرادها من ملفات خارجية وتنفيذ هجوم معقّد شكراً لـ XMLHttpRequest.

تم إرجاء الإعلان عن تفاصيل المشكلة حتى صدور ترقيع رسمي من الشركة وهو متوفر الآن للتحميل لعملائهم.

المصادر:


[Invision Power Board '.txt' File MIME-Type Cross Site Scripting Vulnerability](http://www.securityfocus.com/bid/37263)




[Invision Power Board Local File Include and SQL Injection Vulnerabilities](http://www.securityfocus.com/bid/37208)
