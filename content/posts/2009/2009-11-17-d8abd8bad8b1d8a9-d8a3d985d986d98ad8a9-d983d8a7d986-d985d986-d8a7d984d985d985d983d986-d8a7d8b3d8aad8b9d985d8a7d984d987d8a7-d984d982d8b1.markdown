---
author: يوغرطة بن علي (Youghourta Benali)
date: 2009-11-17 19:04:32+00:00
draft: false
title: ثغرة أمنية كان من الممكن استعمالها لقرصنة Twitter
type: post
url: /2009/11/%d8%ab%d8%ba%d8%b1%d8%a9-%d8%a3%d9%85%d9%86%d9%8a%d8%a9-%d9%83%d8%a7%d9%86-%d9%85%d9%86-%d8%a7%d9%84%d9%85%d9%85%d9%83%d9%86-%d8%a7%d8%b3%d8%aa%d8%b9%d9%85%d8%a7%d9%84%d9%87%d8%a7-%d9%84%d9%82%d8%b1/
categories:
- Security
- Web
tags:
- SSL
- Twitter
---

**ثغرة أمنية كان من الممكن استعمالها لقرصنة Twitter**



تم مؤخرا الإعلان عن ثغرة أمني في بروتوكول SSL و التي تسمع للمخترقين بالتلاعب بالحماية وبإمكانية التواصل مع الخوادم  التي يتصل معها جهاز الضحية.

قلل بعض من الخبراء من أهمية الثغرة خصوصا إذا كان من الصعب جدا أو من المستحيل استخراج معلومات من البيانات المشفرة.

الأسبوع الماضي، قام باحث في  أمن المعلومات يدعى  Anil Kurmus بنشر ما يصطلح عليه بـ proof of concept  ليثبت خطورة الثغرة إذا قام باستخراج الرقم السري  لحساب Twitter و ذلك بتطبيق هجمة من نوع Man-in-the-Middle (MITM)  التي تستغل هذه الثغرة.

![twitter_logo](https://www.it-scoop.com/wp-content/uploads/2009/11/twitter_logo.jpg)


حسب نفس الباحث، بما أن الكثيرين يستعملون برامج إضافية لتحديث حساباتهم على Twitter فإنه يكفي لاختراق حساب Twitter  اعتراض الطلبات المرسلة من طرف هذه البرامج إلى الـ API الخاصة بـ Twitter  ، هذه الطلبات التي تحوي كلها  الرقم السري للمستخدم.

من جهتها سارعت Twitter لسد الثغرة المعلن عنها مما يثبت وجودها.

المصدر:

[http://www.securegoose.org/2009/11/tls-renegotiation-vulnerability-cve.html](http://www.securegoose.org/2009/11/tls-renegotiation-vulnerability-cve.html)
