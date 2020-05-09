---
author: يوغرطة بن علي (Youghourta Benali)
date: 2012-03-08 19:59:12+00:00
draft: false
title: 'Pwn2Own: فريق أمني يخترق Chrome خلال أقل من 5 دقائق، والمتصفحات الأخرى لم
  تكن أوفر حظًا'
type: post
url: /2012/03/pwn2own-chrome-hacked-5-minutes/
categories:
- Google
- Security
- Web
- متصفحات
tags:
- chrome
- Pwn2Own
- VUPEN
---

كما هو معروف فإن مُتصفح Chrome يُعتبر أحد أكثر المُتصفحات أمانا ومن بين أهم الدلائل على ذلك صموده أمام المخترقين خلال [إصدار العام الماضي من مُسابقة Pwn2Own](../2011/03/pwn2own-safari-5-seconds/)، لكنه لم يستطع الصمود أمام فريق VUPEN الأمني خلال دورة هذا العام من نفس المُسابقة سوى 5 دقائق.




[![](https://www.it-scoop.com/wp-content/uploads/2012/03/chrome-hacked-Pwn2Own.jpg)
](https://www.it-scoop.com/wp-content/uploads/2012/03/chrome-hacked-Pwn2Own.jpg)




حسب [التغريدة](https://twitter.com/#%21/VUPEN/status/177518987972849664) التي يُعلن فيها الفريق عن الأمر فإنهم قد تمكنوا من تجاوز [DEP](http://en.wikipedia.org/wiki/Data_Execution_Prevention)  و [ASLR](http://en.wikipedia.org/wiki/Address_space_layout_randomization) إضافة إلى حماية Sandbox التي تُميز المتصفح، دون أن يدلوا بتفاصيل إضافية (ربما لم يكونوا يعرفون خدمة  [Long tweets](http://long-tweets.com/) لينشروا كافة التفاصيل في التغريدة :p).




أما باقي المُتصفحات المُشاركة في المُسابقة (Firefox، Interner Explorer و Safari) فلم تكن أوفر حظا، حيث [سقطت هي أيضا](https://twitter.com/#%21/VUPEN/status/177576000761237505) على أيدي نفس الفريق خلال نفس اليوم.




من المتوقع أن يحصل فريق VUPEN على جزء من المليون دولار التي [وعدت بها Google مخترقي مُتصفحها](http://blog.chromium.org/2012/02/pwnium-rewards-for-exploits.html).




للتذكير فإنه قد سبق وأن نشرت Google تحديثا أمنيا لمتصفحها بحر هذا الأسبوع والذي رقع 14 ثغرة [دفعت لمكتشفيها 47500 دولار.](../2012/03/google-patches-14-chrome-bugs-pays-record-47k/)
