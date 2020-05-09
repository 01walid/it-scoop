---
author: Ali
date: 2010-04-24 21:18:00+00:00
draft: false
title: بعد طول انتظار…طرح النسخة Beta من الإصدار السادس لـ Red Hat Enterprise
type: post
url: /2010/04/red-hat-enterprise-linux-6-beta-available-public-download/
categories:
- Unix/Linux
tags:
- Linux
- Red Hat
---

[**بعد طول انتظار…طرح النسخة Beta من الإصدار السادس لـ Red Hat Enterprise**](http://www.it-scoop.com/2010/04/Red-Hat-Enterprise-Linux-6 Beta-Available-Public-Download)


طرحت Red Hat نسخة تجريبية قابلة للتحميل من  Red Hat Enterprise 6، علما أن النسخة 5 قد مضى على طرحها أكثر من 3  سنوات. بنواته المعتمدة على 2.6.18 kernel وعدد من المكونات الأخرى ذات الطابع الكلاسيكي . تبقى النسخة هذه ، ولو للوهلة الأولى ، ذات مظهر قديم وعتيق.

[![](http://www.it-scoop.com/wp-content/uploads/2010/04/red_hat_logo_big.jpg)
](http://www.it-scoop.com/2010/04/Red-Hat-Enterprise-Linux-6 Beta-Available-Public-Download)

التغيير الأكبر في هذه النسخة قد يكون التخلي عن الـ hypervisor القديم Xen ، والاعتماد على آخر جديد هو KVM (Kernel-based Virtual Machine) .

بعض ميزات و تحسينات RHEL6 تشمل :

**قدرات شاملة لإدارة الطاقة.**

هناك أدوات مراقبة جديدة مثل Powertop مصممة خصيصا لمتابعة قضايا الطاقة في جهازك. هناك أيضا أدوات تحسين مثل Tuned الذي يسمح للنظام بالتكيف بناء على تحليل نمط استخدام الخدمات والتطبيقات من قبل المستخدم.

**تحسين الأداء.**

لقد تم إعادة كتابة الـ Process Scheduler  بالكامل بحيث يوزع قدرات المعالج على المهام بشكل أكثر عدلا ، و أيضا السماح للمهام ذات الأولوية العالية بالعمل مع وجود أقل قدر ممكن من التدخل من قبل المهام ذات الأولوية المنخفضة.

**مميزات أمنية جديدة**

الخدمة الجديدة المسماة System Security Services Daemon SSSD  تقدم إدارة مركزية للهويات identities. ميزة SELinux Sandbox الجديدة تسمح بتشغل المحتويات غير الآمنة في بيئة معزولة لضمان عدم تأثيرها على النظام سلبا.

**بيئة سطح المكتب و البرامج الأخرى**

ستكون البيئتان GNOME 2.28 و KDE 4.3 متضمنتان مع نظام التشغيل . قائمة البرامج تشمل FireFox 3.5، Thunderbird 3 و OpenOffice.org 3.1 . لا ننسى طبعا الـ PostreSQL 8.4  و MySQL 5.1 ، و أيضا بيئة تشغيل جافا OpenJDK 1.6 .

**نظام الملفات**

نظام الملفات المدعوم هو Ext4 ، ووفقا لخطط حاليا هناك أيضا XFS . سيتم دعم Btrfs أيضا.

بقي أخيرا أن نذكر أن هذه النسخة ستأتي بعدة إصدارات بما يتلاءم مع المعالج المستخدم ، فهناك إصدار خاصة بأنظمة x86-32 و آخر لأنظمة x86-64 ، إضافة إلى أنظمة System z و Power .

يمكن تحميل الإصدار Beta لـ Red Hat Enterprise من [هنا](http://www.redhat.com/rhel/beta/)

و لمزيد من التفاصيل يمكن الإطلاع على الـ Release notes من [هنا](http://www.redhat.com/docs/en-US/Red_Hat_Enterprise_Linux/6-Beta/html/Beta_Release_Notes/)

يبقى السؤل قائما فيما إذا كانت كل تلك الميزات قادرة على سحب البساط من تحت Windows server 2008 ، فما رأيكم ؟
