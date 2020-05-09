---
author: dzgeek
date: 2010-11-18 15:26:58+00:00
draft: false
title: 'Linux يحظى بترقيع معجزة يسرع تعددية المهام '
type: post
url: /2010/11/the-200-line-linux-kernel-patch-that-does-wonders/
categories:
- Unix/Linux
- برمجيات
tags:
- Kernel
- Linux
- Mike Galbraith
- patch
---

**[Linux يحظى بترقيع معجزة يسرع تعددية المهام](http://www.it-scoop.com/2010/11/the-200-line-linux-kernel-patch-that-does-wonders)**


في عالم البرمجيات وخاصة منها أنظمة التشغيل، يندر وجود حلول خارقة للعادة، تغير من الأمور جذريا، فالمعهود هو التحسين من البرمجية شيئا فشيئا مع مرور الزمن،  لكن أن تأتي رقعة صغيرة لتقلب الأمور والموازين ، وتقفز بها إلى الأحسن، هذا ما يسميه الكثيرون "معجزة"، وبالضبط هذا ما حدث مؤخرا مع نواة Linux في رقعة جد مبشرة لهذا النظام جاءت من طرف ثالث!.

[![](http://www.it-scoop.com/wp-content/uploads/2010/11/kernel_panic-273x300.png)
](http://www.it-scoop.com/2010/11/the-200-line-linux-kernel-patch-that-does-wonders)

نجحت هذه الرقعة في اختزال جوهري لضغط النظام في الوضع الرسومي دون تعلق الوضع الكتابي، وكذا في إثبات وجودها لدى Linus Trovalds، لأن مثل هذه الترقيعات تُقترح بانتظام عليه لكن يعيبها الكثير فيتم رفضها، لكن هذه الأخيرة حظيت بمباركة الأب الروحي  وصنف حالتها  ضمن "الميزة القاتلة" أو killer feature.

فقط 224 سطر برمجي، هو ما كان يحتاجه المطور Mike Galbraith ليحصل على نتائج مذهلة مع مجدول المهام scheduler، وهو المكون الذي يلعب دورا في تقسيم المهام بين أنوية المعالجات الحديثة  حسب أولوية كل عملية.

والغالب على أنشطة المستخدم في أيامنا هو تعدد المهام والعمل على عدة نوافذ، أين تصبح كفاءة الحاسوب تلعب دورا حيويا في سرعة الإنتاجية، وهنا تأتي هذه الرقعة لتدلي بدلوها في هذه اللعبة، والنتائج فوق التوقعات.

وهنا فيديو يوضح أداء حاسوب مع نواة عادية في وقت تصريف برنامج  compilation:

<!-- more -->



<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" width="640" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0" height="385"><embed src="http://www.youtube.com/v/uk70SeGA7pg?fs=1&hl=fr_FR" allowscriptaccess="always" height="385" width="640" allowfullscreen="true" type="application/x-shockwave-flash"></embed></object>

وهذا فيديو آخر يوضح الفرق بعد أن تم تنصيب الرقعة:



<object classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000" width="640" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,40,0" height="385"><embed src="http://www.youtube.com/v/prxInRdaNfc?fs=1&hl=fr_FR" allowscriptaccess="always" height="385" width="640" allowfullscreen="true" type="application/x-shockwave-flash"></embed></object>

وكما يبدو لنا جليا، فالفرق شاسع، لا مزيد من تقطع في الفيديو (وهو ملف Ogg بدقة 1080p )، لا مزيد من أي تثاقل في حركات الـ3D، هناك انتعاش رسومي وسيولة أكثر في حركة الصفحات.

يجدر الإشارة إلى أن هذا الترقيع حظي بمراجعة Linus Trovalds شخصيا، هذا الأخير[ هنّأ المطور Mike Galbraith ](http://marc.info/?l=linux-kernel&m=128979084506774&w=2)على ترقيعه ذي النقلة النوعية في النظام دون الإخلاء بباقي مكوناته ودون توليد علل أخرى. وقد لاحظ -Linus- أن تحميل صفحات الويب زاد سرعة بعد أن كان يعلق هذا بكفاءة الشبكة، لكن تبين له أن لضغط المعالج دور كبير.

وكما[ ذكر موقع Phoronix](http://www.phoronix.com/scan.php?page=article&item=linux_2637_video&num=2) فسيتم زراعة هذا الترقيع في النواة إصدارة 2.6.38، لأنه سبق وأن أخذت ميزات الاصدارة 2.6.37 مكانها، وتأثير الرقعة سيشعر به أكثر المستخدمين الذي يعملون على أكثر من تطبيق في نفس الوقت (كما هو الحال مع أغلبنا :D ) خاصة إذا كانت هذه التطبيقات شرهة لموارد النظام.

- كيف ترى عزيزي القارئ هذا الترقيع؟ وهل ستسبق الأحداث لتنصيب الإصدارة 2.6.8 من النواة؟ أم ستصبر مع الصابرين؟
