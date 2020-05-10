---
author: يوغرطة بن علي (Youghourta Benali)
date: 2010-10-06 16:47:03+00:00
draft: false
title: 'Adobe تنشر ترقيعات لـ 23 ثغرة على كل من Reader و Acrobat '
type: post
url: /2010/10/adobe-acrobat-reader-security-updates/
categories:
- Security
- برمجيات
tags:
- Acrobat
- Adobe
- ASLR
- buffer overflow
- DEP
- patch
- reader
- Security
- Vulnerabilities
---

**[Adobe تنشر ترقيعات لـ 23 ثغرة على كل من Reader و Acrobat](https://www.it-scoop.com/2010/10/adobe-acrobat-reader-security-updates)**


نشرت Adobe أمس جملة من الترقيعات تخص 23 ثغرة على منتجيها Reader و Acrobat ، مسجلة رقما قياسيا فيما يخص عدد الثغرات المرقعة دفعة واحدة خلال 2010.

[![](adobe-security.jpg)
](https://www.it-scoop.com/2010/10/adobe-acrobat-reader-security-updates)

الثغرات [المرقعة ](http://www.adobe.com/support/security/bulletins/apsb10-21.html)تخص الإصدار 9.3.4 لتطبيقي Reader و Acrobat على كل من Windows، Mac  إضافة إلى نفس الإصدار من تطبيق Reader على أنظمة Unix.

تأتي هذه الترقيعات خارج برنامج الترقيع الدوري لـ Adobe كون إحدى الثغرات المعنية بالأمر (و التي تم الإعلان عنها مطلع شهر سبتمبر الماضي) شهدت استغلال واسعا و لقد صُنفت على أنها ثغرة خطيرة جدا.

هذه الثغرة تسمح بتنفيذ كود معين و التي يمكن تستغل فيض في المكدس buffer overflow و ذلك لدى فتح ملف PDF معد خصيصا لاستغلال الثغرة.

كما تكمن خطورة الثغرة في مقدرتها تجاوز حمايتي ASLR ( Address Space Layout Randomization) و DEP (Data Execution Prevention) الخاصتين بـ Vista و Windows7.

[تحميل الإصدار 9.4 من Adobe Reader](http://www.adobe.com/go/EN_US-H-GET-READER)
