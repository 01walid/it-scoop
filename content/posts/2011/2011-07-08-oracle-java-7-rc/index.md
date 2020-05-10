---
author: يوغرطة بن علي (Youghourta Benali)
date: 2011-07-08 21:36:00+00:00
draft: false
title: 'تحديث: إطلاق الإصدار النهائي من Java 7'
type: post
url: /2011/07/oracle-java-7-rc/
categories:
- برمجيات
tags:
- Java
- Java 7
- Java 7 RC
- Nio2
---

تحديث: إطلاق الإصدار النهائي من Java 7

[صفحة التحميل](http://www.oracle.com/technetwork/java/javase/downloads/index.html)

[Release Note](http://www.oracle.com/technetwork/java/javase/jdk7-relnotes-429209.html) الخاصة بهذا الإصدار




[**Oracle تطلق الإصدار RC من Java 7**](https://www.it-scoop.com/2011/07/oracle-java-7-rc/)




[أطلقت](http://blogs.oracle.com/theaquarium/entry/java_7_d_day_is) Oracle يوم أمس الإصدارة المرشحة RC من Java 7 و التي تأتي محملة بالعديد من الخواص و المزايا الجديدة و التي طال انتظارها لأزيد من أربعة سنوات، و بذلك تعطي Oracle للغتها البرمجية نفسا جديدا.




[![](java_logo.gif)
](https://www.it-scoop.com/2011/07/oracle-java-7-rc/)




لا يسعنا أن نذكر هنا كافة المزايا الجديدة لكن قد يكون أهمها هو إضافة API جديدة للـ Input/Output تحمل الاسم Nio2  و التي توفر العديد من المزايا الجديدة خاصة ما تعلق بمنها بإدارة الملفات. و سيصبح ممكنا مع هذا الإصدار استخدام الـ _  في الأعداد حيث سنرى قريبا شفرات مصدرية تحتوي:




    
     int oneMillion = 1_000_000;




بدل




    
    int oneMillion = 1000000;




و التي بالرغم من "غرابتها" إلا أنها ستسهل كثيرا قراءة الشفرات المصدرية.




و يحمل هذا الإصدار خاصية مفيدة جدا و هي إمكانية استعمال الـ String في الهيكل الشرطي  switch على النحو التالي:




    
    case "string":
      doSomething();
        break;




يمكن الاطلاع على كافة ما يقدمه هذا الإصدار من [هنا](https://openjdk.java.net/projects/jdk7/features/)، و لمن لا يطيق صبرا حتى موعد الإصدار النهائي من Java 7 ما عليه سوى تحميل الإصدار RC من [هنا](http://jdk7.java.net/download.html)




يمكن معرفة المزيد حول Java 7 من خلال هذا النقاش الذي يدور حوله:




<!-- more -->



<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" width="486" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0" id="flashObj" height="322"><embed src="http://c.brightcove.com/services/viewer/federated_f9?isVid=1" pluginspage="http://www.macromedia.com/shockwave/download/index.cgi?P1_Prod_Version=ShockwaveFlash" seamlesstabbing="false" allowscriptaccess="always" swliveconnect="true" id="flashObj" width="486" base="http://admin.brightcove.com" allowfullscreen="true" height="322" type="application/x-shockwave-flash" flashvars="videoId=1034537450001&linkBaseURL=http%3A%2F%2Fmedianetwork.oracle.com%2Fmedia%2Fshow%2F16796&playerID=1640183659&playerKey=AQ~~,AAAAAFcSbzI~,OkyYKKfkn3za9MF0qI3Ufg1AerdkqfR3&domain=embed&dynamicStreaming=true"></embed></object>
