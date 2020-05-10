---
author: Omar Kharsa
date: 2011-01-06 11:15:49+00:00
draft: false
title: إطلاق الإصدار 2.6.37 من نواة Linux
type: post
url: /2011/01/linux-kernel-2-6-37-released/
categories:
- Open source
- Unix/Linux
- برمجيات
tags:
- Kernel
- Linux
- Linux 2.6.37
---

**[إطلاق الإصدار 2.6.37 من نواة Linux](https://www.it-scoop.com/2011/01/linux-kernel-2-6-37-released/)**


أعلن Linus Torvalds يوم أمس عن [إطلاق ](http://article.gmane.org/gmane.linux.kernel/1083342)الإصدار 2.6.37 من نواة نظام التشغيل Linux .

[![](Linux-kernel.jpeg)
](https://www.it-scoop.com/2011/01/linux-kernel-2-6-37-released/)

تأتي هذه النواة بتحديثات وإضافات كثيرة جدا منها :

**بالنسبة لنظام الملفات :**

** **فيما يخص نظام  EXT4 تم الاقتراب بشكل كبير من طبقة Block I/O بدلا من طبقة buffer مما أدى إلى تسريعه بشكل هائل يصل إلى[ 300%](http://thunk.org/tytso/blog/2010/11/01/i-have-the-money-shot-for-my-lca-presentation/)، كما أنه وصل إلى أداء قريب من نظام XFS في اﻷنظمة الكبيرة. إضافة إلى تسريع عملية mkfs ، كما تم تحسين أداء نظام XFS بحوالي 15 % .

**التعريفات :**

دعم تعريف Nouveau المفتوح لبطاقات الشاشة GeForce 320M

تحسين أداء 2D,3D في تعريفات Radeon

إضافة كل من تعريف لبطاقات الشبكة اللاسلكية Broadcom ، تعريف Beeceem USB Wimax ، إلى جانب  المزيد من تعريفات أجهزة USB وبطاقات الصوت وغيرها

ليس هذا فحسب تأتي هذه الإصدارة بكل من

دعم الـ Apple Magic Trackpad

استخدام ضغط LZO لتسريع عملية hibernation

دعم أجهزة SCSI الموصولة عبر USB 3.0

تحسينات عديدة لتقنية KVM الخاصة باﻷنظمة الافتراضية

من المفترض أن يتم اعتماد هذا الإصدار من النواة في التوزيعات القادمة وأشهرها Ubuntu 11.04, Fedora 15.

ومن المتوقع أن ينتهي الإصدار القادم 2.6.38 في الشهر أبريل من العام الجاري

مزيد من التفاصيل عن التغييرات ستجدها في[ هذه الصفحة](http://kernelnewbies.org/Linux_2_6_37) .

كالعادة، يمكن تحميل نواة Linux من على موقع [http://www.kernel.org/](http://www.kernel.org/)

-   هل ستنتظر توفر النواة الجديدة في مستودعات توزيعتك أم أنك ستقوم ببنائها بنفسك ؟
