---
author: Xacker
date: 2009-12-04 09:27:47+00:00
draft: false
title: ثغرة zero-day في نظام FreeBSD
type: post
url: /2009/12/%d8%ab%d8%ba%d8%b1%d8%a9-zero-day-%d9%81%d9%8a-%d9%86%d8%b8%d8%a7%d9%85-freebsd/
categories:
- Security
- Unix/Linux
tags:
- 0day
- FreeBSD
- Security
- Zero-day
---

قام فريق الأمن المسؤول عن نظام FreeBSD بتعجيل إصدار ترقيع مؤقت للثغرة المكتشفة في نظام FreeBSD والتي تسمح لمستخدم محلّي local user بالحصول على صلاحيات مدير root وتعرض الأنظمة لهجمات Code Execution.


![](http://www.arabteam2000-forum.com/uploads/monthly_11_2009/post-7008-12594413948543.png)




قام مكتشف الثغرة والذي قام بطرحها للعلن، المخترق المعروف باسم Kingcope ب[طرح بعض التوضيح عنها](http://lists.grok.org.uk/pipermail/full-disclosure/2009-November/071686.html) أقتبس منه:


<blockquote>

> 
> The bug resides in the Run-Time Link-Editor (rtld). Normally rtld does not allow dangerous environment variables like LD_PRELOAD to be set when executing setugid binaries like “ping” or “su”. With a rather simple technique rtld can be tricked into accepting LD variables even on setugid binaries.
> 
> 
</blockquote>


Colin Percival، مسؤول أمني لدى FreeBSD [أكد وجود هذه الثغرة](http://docs.freebsd.org/cgi/getmsg.cgi?fetch=0+0+current/freebsd-announce) التي تسمح لمستخدم محلي بتنفيذ أوامر بصلاحيات مدير. تصيب هذه الثغرة نظام FreeBSD بإصداراته 7.1 و 8.0.

يقول Percival بأن هذا الترقيع الذي تم طرحه قد لا يكون النهائي لحل المشكلة، وربما يتسبب بنتائج غير معروفة باعتبار أنه تم التعجيل في طرحه لمحاولة الحد من انتشارها بشكل سريع في البداية تحضيراً لطرح الترقيع النهائي لها بعد إجراء الاختبارات اللازمة، وعليه ينبه بأن استخدام هذا الترقيع سيكون على مسؤولية مدراء الأنظمة هذه.

يتوفر الترقيع الأولي لهذه الثغرة، [هنـــا](http://people.freebsd.org/~cperciva/rtld.patch)

المصدر:


[http://docs.freebsd.org/cgi/getmsg.cgi?fetch=0+0+current/freebsd-announce](http://docs.freebsd.org/cgi/getmsg.cgi?fetch=0+0+current/freebsd-announce)
