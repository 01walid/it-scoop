---
author: يوغرطة بن علي (Youghourta Benali)
date: 2012-09-03 11:12:28+00:00
draft: false
title: Oracle تطلق تحديثا لسد ثغرة في Java يفتح الباب لثغرة أخرى
type: post
url: /2012/09/oracle-emergency-java-patch-brings-sandbox-bypass/
categories:
- Security
tags:
- Java
- Java 7
- oracle
- vulnerability
---

نشرت **Oracle** نهاية الأسبوع المنصرم تحديثا لـ **Java** يهدف إلى سد ثغرة تمكن من نشر برامج ضارة على الأجهزة التي تستخدم الإصدار 7 من Java. الكل سارع إلى تهنئة Oracle على سرعة استجابتها للثغرة وسدها لها، إلا أن الترقيع الذي نشرته يفتح الباب أمام ثغرة أخرى لا تقل خطورة عنها.




[![](java-patch.png)
](java-patch.png)




بداية وبالرغم مما قيل [حول سرعة استجابة Oracle](http://www.computerworld.com/s/article/9230786/Oracle_s_emergency_Java_patch_blocks_zero_day_exploits_researchers_confirm) وأنه أمر تُشكر عليه، أشارت بعض المصادر بأن الشركة كانت على علم بالثغرة منذ شهر [أبريل الماضي](http://seclists.org/bugtraq/2012/Aug/225)، حيث أبلغتها شركة Security Explorations البولندية بها حينئذ، لكن [Oracle لم تقم بترقيعها](https://blogs.oracle.com/security/entry/security_alert_for_cve_20121) إلا بعد أن تم استغلالها على نطاق واسع، وبعد أن انتشرت الأخبار حول الأمر، حيث أن Oracle دأبت على نشر تحديثاتها الأمنية بشكل دوري في أوقات معروفة (كل أربعة أشهر)، وكان موعد التحديث القادم مبرمجا لشهر أكتوبر.




بعد نشر الترقيع –والذي كما سبق ذكره لا يخص سوى الإصدار 7 من Java- أكد Adam Gowdiak بأنه منيع ضد الهجمات التي كانت تستغل الثغرة المعنية بالأمر، إلا أنه فتح الباب لاستغلال [ثغرة أخرى](http://seclists.org/bugtraq/2012/Aug/225) جديدة تسمح للمخترق لدى استغلالها بجانب ثغرة تم اكتشافها سابقا بتجاوز Sandbox الخاص بالآلة الافتراضية بـ Java.




يُشير Gowdiak بأنه تم إبلاغ Oracle بالأمر، كما أنهم أرسلوا إليها proof of concept جديد لاستغلال الثغرة، وسيتم نشر تفاصيل الثغرة بعد أن تؤكدها Oracle وتنشر ترقيعاً لها.
