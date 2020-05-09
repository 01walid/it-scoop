---
author: Xacker
date: 2009-12-30 13:55:51+00:00
draft: false
title: اكتشاف ثغرة جديدة في IIS
type: post
url: /2009/12/iis-%d9%88-%d8%ab%d8%ba%d8%b1%d8%a9-%d8%ac%d8%af%d9%8a%d8%af%d8%a9/
categories:
- Microsoft
- Security
- Web
- برمجيات
tags:
- IIS
- Internet Information Services
- Microsoft
- vulnerability
---

[**اكتشاف ثغرة جديدة في IIS**](http://www.it-scoop.com/2009/12/iis-%d9%88-%d8%ab%d8%ba%d8%b1%d8%a9-%d8%ac%d8%af%d9%8a%d8%af%d8%a9/)


أعلن الباحث Soroush Dalili عن وجود ثغرة 0day في الطريقة التي يعالج فيها IIS أسماء الملفات التي يتم رفعها إلى الموقع من قبل زائر مثلاً.


[![](http://www.it-scoop.com/wp-content/uploads/2009/12/iis_logo.png)
](http://www.it-scoop.com/2009/12/iis-%d9%88-%d8%ab%d8%ba%d8%b1%d8%a9-%d8%ac%d8%af%d9%8a%d8%af%d8%a9/)


تمكن الثغرة المهاجم من رفع سكربتات ضارة إلى السيرفر مستغلاً الخطأ في معالجة أسماء الملفات.

تعتمد الثغرة على إضافة فاصلة منقوطة semi-colon تفصل بين اللاحقة الحقيقية والوهمية للملف، مثلاً _malicious.asp;.jpg_

الإصدارات المصابة: تم اختبار الثغرة على الإصدار 6.0 وما سبقه وهي تعمل بنجاح، لم يتم إجراء اختبار على IIS 7.0 أما IIS 7.5 فهو آمن من الثغرة.

وفقاً [للتقرير الذي نشره Soroush Dalili](http://www.isecur1ty.org/uploads/iis-semicolon-report.pdf)، فإن IIS يمكنه أن يقوم بتنفيذ أي executable على السيرفر مثل ".asp, .cer, .asa" إلخ، الأمر الذي يعطي المهاجم العديد من الخيارات في الطريقة التي يريد بها استغلال الخطأ.

بالإضافة إلى هذه الثغرة الناتجة عن وضع semi-colon، بإمكان المهاجم استخدام النقطتين ":" لكي يقوم بحقن ملفات ضمن الـ Alternative Data Stream الخاصة بقرص مهئ كـ NTFS.

ربما لا تكون الثغرة على تلك الدرجة من الخطورة في الحالات الافتراضية، التي تكون فيها المجلدات عادة ذات صلاحيات Read فقط بشكل افتراضي - وتصبح الثغرة خطرة جداً في حالات رفع الملفات إلى مجلدات ذات صلاحيات Execute وهذا أمر يندر حصوله بشكل عام.

لم تقم Microsoft بنشر ترقيع للثغرة حتى الآن وتشير إلى أنها ما زالت [تحقق في الأمر](http://blogs.technet.com/msrc/archive/2009/12/27/new-reports-of-a-vulnerability-in-iis.aspx).

عموماً، يبقى IIS ثاني أكبر مخدم ويب خلف Apache HTTP Server الأمر الذي يجعل الثغرة منتشرة على نطاق واسع جداً.
