---
author: Omar Kharsa
date: 2010-12-08 11:47:19+00:00
draft: false
title: 'إطلاق النسخة التجريبية اﻷولى رقم 4 لبرنامج VirtualBox '
type: post
url: /2010/12/virtualbox-4-beta/
categories:
- Open source
- برمجيات
tags:
- Oracle VM VirtualBox
- VirtualBox
---

**[إطلاق النسخة التجريبية اﻷولى رقم 4 لبرنامج VirtualBox](https://www.it-scoop.com/2010/12/virtualbox-4-beta)**


أطلقت Oracle الإصدار التجريبي للنسخة  رقم 4.0.0 من برنامج VirtualBox الشهير الخاص باﻷنظمة الافتراضية بعد حوالي سنتين على الإصدار رقم 2.

[![](https://www.it-scoop.com/wp-content/uploads/2010/10/oracle-virtualbox.png)
](https://www.it-scoop.com/2010/12/virtualbox-4-beta)

تأتي هذه النسخة الرئيسية بمزايا عديدة منها :



	  * دعم نسخ الملفات للنظام الضيف
	  * دعم لصيغة الضغط Open Virtualization Format Archive
	  * دعم حجوم ذاكرة Ram أكبر من 2GB بالنسبة للنظام الضيف
	  * إضافة دعم لرقاقة Intel ICH9 chipset
	  * بالنسبة للصوت إتاحة Intel HD Audio كجهاز للنظام الضيف
	  * بالنسبة للواجهات :إعادة تصميم واجهة المستخدم
	  * دعم نقل البيانات غير المتزامن ﻷجهزة iSCSI, VMDK, VHD
	  * لنظام Windows دعم التحديث التلقائي للنظام الضيف بشرط تنزيل النسخة رقم 4 من Windows Guest Additions .

تم معالجة الكثير من اﻷخطاء والمشاكل وهذه بعضها :

	  * إصلاح الأخطاء التي تحدث عند تصغير وتكبير الواجهة الخاصة بالنظام الضيف
	  * تم دمج  Linux Additions الخاصة ب 32Bit و 64Bit  في ملف واحد
	  * المجلدات المشتركة أصبحت تدعم symbolic links (خاصة بنظام Linux كضيف)
	  * إمكانية تشغيل الصوت من أكثر من نظام ضيف (guest) في نفس الوقت
	  * إمكانية حذف الأقراص المتصلة بالنظام االضيف أثناء حذفه.

لمعلومات تفصيلية عن الخواص الجديدة والإصلاحات انظر [هذه الصفحة](http://forums.virtualbox.org/viewtopic.php?f=15&t=36748) .

يذكر ان آخر نسخة ثابتة من هذا البرنامج تم إصدارها منذ عدة أيام برقم 3.2.12 .

لمزيد من المعلومات عن الخواص الجديدة وطريقة الاستخدام يمكنك تحميل الدليل المؤلف من 254 صفحة من [هنا](http://download.virtualbox.org/virtualbox/4.0.0_BETA1/UserManual.pdf) .

صفحة تحميل هذا الإصدار التجريبي للأنظمة المختلفة من [هنا ](http://download.virtualbox.org/virtualbox/4.0.0_BETA1/)علما انه لاينصح الاعتماد بشكل كلي عليه .

تحديث : بعد أيام قليلة على الإصدار Beta 1 أصدرت Oracle[ التحديث الثاني](http://bit.ly/i4VrP6) Virtualbox 4 beta 2
صفحة تحميل الإصدار Beta 2 من[ هنا](http://download.virtualbox.org/virtualbox/4.0.0_BETA2/)

تحديث 2 (17 ديمسبر): تتوالى إصدارات Beta لـ Virtualbox 4 حيث صدرت خلال الأيام الثلاثة الماضية الـ [Beta3 ](http://vbox.innotek.de/pipermail/vbox-announce/2010-December/000053.html)و الـ [Beta4](http://vbox.innotek.de/pipermail/vbox-announce/2010-December/000054.html).
