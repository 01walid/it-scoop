---
author: Xacker
date: 2010-11-04 15:18:08+00:00
draft: false
title: Microsoft تحذر من ثغرة zero-Day جديدة تخص Internet Explorer بإصداراته 6، 7
  و 8
type: post
url: /2010/11/microsoft-internet-explorer-zero-day-vunlerability/
categories:
- Microsoft
- Security
- متصفحات
tags:
- 0-day-vunlerability
- internet explorer
- Microsoft
- Zero-day
---

**[Microsoft تحذر من ثغرة zero-Day جديدة تخص Internet Explorer بإصداراته 6، 7 و 8](https://www.it-scoop.com/2010/11/microsoft-internet-explorer-zero-day-vunlerability)**




تقوم Microsoft حاليا بالتحقيق في معلومات جديدة حول ثغرة في جميع إصدارات متصفح Internet Explorer والتي يمكن أن يتم استغلالها في تنفيذ هجمات remote code execution.


[![](Internet_Explorer_7_Logo_red.png)
](https://www.it-scoop.com/2010/11/microsoft-internet-explorer-zero-day-vunlerability)

التقرير الذي أعلن عن وجود هذه الثغرة والذي تم نشره على الانترنت يتضمن معلومات حول طرق تفادي الوقوع ضحية استغلالها بشكل مؤقت ريثما يتم طرح ترقيع رسمي لها من قبل Microsoft.

سبب الثغرة هو مرجع خاطئ (invalid reference) في ذاكرة متصفح Internet Explorer والذي يمكن تحت ظروف معينة الوصول إليه بعد حذف الكائن (object). النجاح في تنفيذ هذا الهجوم سيمكن المهاجم من تنفيذ كود عن بعد (remote code execution).

حالياً – تقول Microsoft – "نحن على علم بوجود هجمات موجهة تحاول استغلال هذه الثغرة".

تقوم Microsoft الآن بالتحقيق في هذا الموضوع وستقوم باتخاذ التدابير المناسبة لحماية المستخدمين، والذي قد يكون من خلال طرح ترقيع أمني لهذه المشكلة في نشرتها الأمنية الدورية، أو كسر الروتين وطرح الترقيع في غير الموعد الافتراضي وذلك وفقاً للضرورة.

**العوامل المخففة لخطورة الثغرة:**



	  * خاصية Data Execution Prevention (DEP) تساعد في الوقاية من الهجمات التي تحاول استغلال هذه الثغرة وهي مفعلة بشكل افتراضي على أنظمة Windows XP sp3, Windows Vista sp1 + sp2, Windows 7 لبرنامج Internet Explorer 8.
	  * الوضع المحمي (Protected Mode) في Internet Explorer على نظام Windows Vista وما تلاه يساعد في الحد من تأثير الثغرة في حال نجاح المهاجم في استغلالها، عندها سيكون لديه صلاحيات وصول قليلة جداً في النظام.
	  * المهاجم الذي ينجح في استغلال هذه الثغرة على الإصدارين 7 و 8 لـ Internet Explorer سيحصل على صلاحيات المستخدم الحالي. هذا يعني أن المستخدمين بصلاحيات Administrator سيكونون أكثر عرضة للخطر من المجموعات ذات المستوى الأدنى في الصلاحية.
	  * سيكون على المهاجم أن يقنع المستخدم بزيارة صفحة ويب تحوي على كود الاستغلال للثغرة. لن يكون بإمكان المهاجم فرض الاستغلال قسراً على المستخدم إن لم يقم هذا الأخير بزيارة صفحة ويب تحوي على الاستغلال.
	  * بشكل افتراضي، جميع إصدارات Microsoft Outlook, Microsoft Outlook Express, Windows Mail المدعومة تقوم بعرض الرسائل التي تحوي على كود HTML ضمن منطقة Restricted sites، والتي يتم فيها بشكل افتراضي تعطيل جميع السكربتات وعناصر ActiveX، بالتالي إزالة الخطر من أن يتم تنفيذ الرماز الضار، لكن في حال قيام المستخدم بالنقر على رابط يقوم بأخذه إلى صفحة تحوي على الاستغلال للثغرة يكون المستخدم ما يزال تحت تأثير الخطر.

لمزيد من المعلومات حول الثغرة والإصدارات المصابة يمكن زيارة [الرابط](http://www.microsoft.com/technet/security/advisory/2458511.mspx?pf=true).
