---
author: Xacker
date: 2012-06-12 10:02:10+00:00
draft: false
title: فيروس Flame "ينتحر" ليمنع المحققين من استجوابه ومعرفة أسراره
type: post
url: /2012/06/flame-issues-self-destruct-command/
categories:
- Security
tags:
- Duqu
- Flame
- Kaspersky
- Stuxnet
- win32/flamer.a worm
- Worm.Win32.Flame
---

[بعد اكتشافها](http://www.it-scoop.com/2012/05/worm-win32-flame/)، و[نشر تفاصيل عن آلية عملها](http://www.it-scoop.com/2012/06/flame-crypto-breakthrough/) وما تم فضحه من معلومات حولها حتى الآن، فإن **Flame**، دودة الانترنت الخبيثة أخذت أواخر الأسبوع الماضي تتلقى توجيهات بتدمير نفسها وجميع ملحقاتها وإخفاء جميع الأدلة حولها من الأنظمة المصابة والتي ما تزال تحت سيطرتها، وذلك بعد ورود هذه التوجيهات من مراكز الإدارة والتحكم C&C التابعة لها والتي تتحكم بها الجهة أو الجهات خلف Flame.




[![](http://www.it-scoop.com/wp-content/uploads/2012/06/flame-virus.jpg)
](http://www.it-scoop.com/wp-content/uploads/2012/06/flame-virus.jpg)




حيث قام الباحثون بنشر أفخاخ "جرار العسل" honeypots عبر الانترنت (تكون هذه الأفخاخ عادة أنظمة ضعيفة الحماية وبدون جدران نارية، تسمح للمخترقين والبرمجيات العابثة بالسيطرة عليها، ولكن في الوقت نفسه، يتم رصد وتسجيل جميع التغيرات والأوامر والملفات التي يتم إصدارها إلى تلك الأفخاخ، حيث يكون من الصعب على المخترقين والبرمجيات الخبيثة التمييز بين نظام المستخدم العادي وبينها) لمساعدتهم في التقاط أكبر قدر ممكن من المعلومات حول فيروس Flame، وبالفعل، فقد نجح الباحثون بالتقاط أمر أصدر إلى Flame بتحميل إضافة برمجية مهمتها مسح وإخفاء جميع الأدلة حول الإصابة وذلك بهدف منع محللي الجرائم الالكترونية والخبراء الأمنيين من كشف المزيد من المعلومات عن Flame وعن الجهة خلفه.




ووفقاً للدراسة التي خضع لها Flame حتى الآن، فقد اكتشف الباحثون بأنه يحوي على إجرائية برمجية موجودة في تصميمه مسبقاً اسمها **SUICIDE** والتي تعني "انتحار" والتي من الممكن استخدامها لإزالة الإصابة من النظام المصاب. مع هذا، فقد قرر صانعوا Flame ولأسباب -ما تزال مجهولة- عدم الاعتماد على هذه الإجرائية، وفضلوا توجيهه لاستخدام إضافة برمجية منفصلة تم توفيرها له عبر الانترنت ليقوم باستخدامها لإزالة نفسه من الأنظمة المصابة.




هذا وقد سمّيت الإضافة البرمجية المذكورة، بالاسم **browse32.ocx** وكان آخر تعديل لها هو 9 مايو المنصرم (أي منذ شهر تقريباً).




وعلى الرغم من أن تصميمها البرمجي شبيه جداً بالإجرائية SUICIDE الموجودة أساساً ضمن بنية Flame، إلا أنها تقوم بتحديد جميع نسخ Flame على النظام المصاب، فتزيله، ومن ثم تقوم بكتابة بيانات عشوائية بشكل متكرر في المناطق التي كانت تلك الملفات تشغلها على القرص الصلب، وما الهدف من هذا إلا جعل إمكانية استعادة البيانات المحذوفة أمراً شبه (إن لم يكن) مستحيل على محللي الجرائم الالكترونية الساعين خلف كشف المزيد من الغموض حول Flame. ومن الجدير بالذكر، أن الإضافة تقوم بتوليد سلسلة بايتات عشوائية لاستخدامها في تشويه وتدمير البيانات الأصلية التابعة لـ Flame.




تحتوي الإضافة browse32.ocx على تابعين مصدّرين exported functions (أي يمكن استدعاؤهما من أي برنامج):






	  * EnableBrowser: وهي الإجرائية التمهيدية، التي تقوم بإعداد البيئة المناسبة للتنفيذ (mutex, events, shared memory, etc) قبل استدعاء الإجرائية التالية...
	  * StartBrowse: وهي الإجرائية المسؤولة عن عملية البحث والإزالة Search & Destroy لجميع آثار Flame.



<!-- more -->




وتحتوي الإضافة على قائمة كبيرة من الملفات والمجلدات المستخدمة من قبل Flame، نذكرها لكم فيما يلي بعد أن قامت شركة Symantec [بنشرها](http://www.symantec.com/connect/blogs/flamer-urgent-suicide) في تدوينة على موقعهم:




**الملفات**






	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAudio\audcache
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAudio\audfilter.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAudio\dstrlog.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAudio\dstrlogh.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAudio\m3aaux.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAudio\m3afilter.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAudio\m3asound.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAudio\m4aaux.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAudio\m4afilter.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAudio\m4asound.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAudio\m5aaux.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAudio\m5afilter.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAudio\m5asound.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAudio\mlcache.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAudio\mpgaaux.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAudio\mpgaud.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAudio\qpgaaux.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAudio\srcache.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAudio\wavesup3.drv
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAudio\wpgfilter.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAuthCtrl\authcfg.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAuthCtrl\ctrllist.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAuthCtrl\lmcache.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAuthCtrl\ntcache.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAuthCtrl\posttab.bin
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAuthCtrl\secindex.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAuthCtrl\tokencpt
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\dmmsap.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\domm.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\domm2.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\domm3.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\dommt.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\dstrlog.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\dstrlogh.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\lmcache.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\Lncache.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\ltcache.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\mscorest.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\mscrol.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\mscrypt.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\mspovst.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\msrovst.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\msrsysv.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\msvolrst.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\nt2cache.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\ntcache.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\rccache.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\rdcache.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\rmcache.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\ssitable
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\syscache.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr\syscache3.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSndMix\audtable.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSndMix\fmpidx.bin
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSndMix\lmcache.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSndMix\lrlogic
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSndMix\mixercfg.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSndMix\mixerdef.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSndMix\ntcache.dat
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSndMix\sndmix.drv
	  * %SystemDrive%\system32\msglu32.ocx
	  * %SystemDrive%\Temp\~8C5FF6C.tmp
	  * %Temp%\~*
	  * %Temp%\~a28.tmp
	  * %Temp%\~a38.tmp
	  * %Temp%\~DF05AC8.tmp
	  * %Temp%\~DFD85D3.tmp
	  * %Temp%\~DFL542.tmp
	  * %Temp%\~DFL543.tmp
	  * %Temp%\~DFL544.tmp
	  * %Temp%\~DFL545.tmp
	  * %Temp%\~DFL546.tmp
	  * %Temp%\~dra51.tmp
	  * %Temp%\~dra52.tmp
	  * %Temp%\~dra53.tmp
	  * %Temp%\~dra61.tmp
	  * %Temp%\~dra73.tmp
	  * %Temp%\~fghz.tmp
	  * %Temp%\~HLV084.tmp
	  * %Temp%\~HLV294.tmp
	  * %Temp%\~HLV473.tmp
	  * %Temp%\~HLV751.tmp
	  * %Temp%\~HLV927.tmp
	  * %Temp%\~KWI988.tmp
	  * %Temp%\~KWI989.tmp
	  * %Temp%\~mso2a0.tmp
	  * %Temp%\~mso2a1.tmp
	  * %Temp%\~mso2a2.tmp
	  * %Temp%\~rei524.tmp
	  * %Temp%\~rei525.tmp
	  * %Temp%\~rf288.tmp
	  * %Temp%\~rft374.tmp
	  * %Temp%\~TFL848.tmp
	  * %Temp%\~TFL849.tmp
	  * %Temp%\~ZFF042.tmp
	  * %Temp%\comspol32.ocx
	  * %Temp%\GRb9M2.bat
	  * %Temp%\indsvc32.ocx
	  * %Temp%\scaud32.exe
	  * %Temp%\scsec32.exe
	  * %Temp%\sdclt32.exe
	  * %Temp%\sstab.dat
	  * %Temp%\sstab15.dat
	  * %Temp%\winrt32.dll
	  * %Temp%\winrt32.ocx
	  * %Temp%\wpab32.bat
	  * %Temp%\wpab32.bat
	  * %Windir%\Ef_trace.log
	  * %Windir%\Prefetch\Layout.ini
	  * %Windir%\Prefetch\NTOSBOOT-B00DFAAD.pf
	  * %Windir%\repair\default
	  * %Windir%\repair\sam
	  * %Windir%\repair\security
	  * %Windir%\repair\software
	  * %Windir%\repair\system
	  * %Windir%\system32\advnetcfg.ocx
	  * %Windir%\system32\advpck.dat
	  * %Windir%\system32\aud*
	  * %Windir%\system32\authpack.ocx
	  * %Windir%\system32\boot32drv.sys
	  * %Windir%\system32\ccalc32.sys
	  * %Windir%\system32\commgr32.dll
	  * %Windir%\system32\comspol32.dll
	  * %Windir%\system32\comspol32.ocx
	  * %Windir%\system32\config\default.sav
	  * %Windir%\system32\config\sam.sav
	  * %Windir%\system32\config\security.sav
	  * %Windir%\system32\config\software.sav
	  * %Windir%\system32\config\system.sav
	  * %Windir%\system32\config\userdiff.sav
	  * %Windir%\system32\ctrllist.dat
	  * %Windir%\system32\indsvc32.dll
	  * %Windir%\system32\indsvc32.ocx
	  * %Windir%\system32\lrl*
	  * %Windir%\system32\modevga.com
	  * %Windir%\system32\mssecmgr.ocx
	  * %Windir%\system32\mssui.drv
	  * %Windir%\system32\mssvc32.ocx
	  * %Windir%\system32\ntaps.dat
	  * %Windir%\system32\nteps32.ocx
	  * %Windir%\system32\pcldrvx.ocx
	  * %Windir%\system32\rpcnc.dat
	  * %Windir%\system32\scaud32.exe
	  * %Windir%\system32\sdclt32.exe
	  * %Windir%\system32\soapr32.ocx
	  * %Windir%\system32\ssi*
	  * %Windir%\system32\sstab.dat
	  * %Windir%\system32\sstab0.dat
	  * %Windir%\system32\sstab1.dat
	  * %Windir%\system32\sstab10.dat
	  * %Windir%\system32\sstab11.dat
	  * %Windir%\system32\sstab12.dat
	  * %Windir%\system32\sstab2.dat
	  * %Windir%\system32\sstab3.dat
	  * %Windir%\system32\sstab4.dat
	  * %Windir%\system32\sstab5.dat
	  * %Windir%\system32\sstab6.dat
	  * %Windir%\system32\sstab7.dat
	  * %Windir%\system32\sstab8.dat
	  * %Windir%\system32\sstab9.dat
	  * %Windir%\system32\tok*
	  * %Windir%\system32\watchxb.sys
	  * %Windir%\system32\winconf32.ocx



**المجلدات:**






	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAudio
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSAuthCtrl
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSecurityMgr
	  * %ProgramFiles%\Common Files\Microsoft Shared\MSSndMix

