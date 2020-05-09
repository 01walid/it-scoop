---
author: Xacker
date: 2009-12-04 08:09:36+00:00
draft: false
title: برمجية خبيثة جديدة من نوع ransomware
type: post
url: /2009/12/%d8%a8%d8%b1%d9%85%d8%ac%d9%8a%d8%a9-%d8%ae%d8%a8%d9%8a%d8%ab%d8%a9-%d8%ac%d8%af%d9%8a%d8%af%d8%a9-%d9%85%d9%86-%d9%86%d9%88%d8%b9-ransomware/
categories:
- Security
tags:
- bundled ransomware
- ransomware
- uFast Download Manager
---

عثر خبراء الأمن على برمجية خبيثة جديدة من نوع ransomware تقوم بمنع وصول الأجهزة المصابة إلى الانترنت حتى يتم دفع "فدية" من خلال الرسائل النصية SMS.

تأتي البرمجية الخبيثة مدمجة مع برنامج اسمه uFast Download Manager، وبمجرد أن تتم إصابة الجهاز تظهر رسالة باللغة الروسية (انظر الصورة) تطالب بفدية بحجة أن المبلغ مخصص لتفعيل نسخة برنامج uFast Download Manager.


![](http://community.ca.com/blogs/securityadvisor/Zarestel/RansomSMS.AH/desktop.gif)




فيما يلي ترجمة للرسالة باللغة الانكليزية:


<blockquote>_Internet access is blocked due to violation of the
license agreement schedules of uFast Download Manager
You must activate your copy _

_Get a registration code by sending an SMS with the following
code fw0004199 to number 7122_

_In response you will receive an activation message._

_Enter the activation message received from the SMS response  _________</blockquote>


أطلق خبراء CA الاسم **Win32/RansomSMS.AH** على هذه البرمجية.

<!-- more -->تم وضع الملاحظات التالية فيما يتعلق بتثبيتها/إزالتها:



	  * البرمجية الخبيثة المدمجة يتم تثبيتها بدون إعلام المستخدم بها.
	  * إجراء uninstall للبرنامج لا يزيل رسالة الفدية من على سطح المكتب أو عناصرها المثبتة.



![](http://community.ca.com/blogs/securityadvisor/Zarestel/RansomSMS.AH/bundled_app_white.gif)




قام خبراء CA بكتابة [مولد مفاتيح Keygenerator](http://community.ca.com/blogs/securityadvisor/Zarestel/RansomSMS.AH/RansomSMS.AH_ActivationCode.zip) :D من أجل هذه البرمجية الخبيثة لإزالتها والذي يعمل على الأجهزة المصابة فقط.

![](http://community.ca.com/blogs/securityadvisor/Zarestel/RansomSMS.AH/unlocked_desktop.gif)



<blockquote>

> 
> _Activation successful! Internet access is now unlocked_
> 
> 
</blockquote>


المصدر:


http://community.ca.com/blogs/securityadvisor/archive/2009/11/30/ransomware-blocks-internet-access.aspx
