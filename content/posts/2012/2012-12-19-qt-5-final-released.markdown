---
author: dzgeek
date: 2012-12-19 17:46:40+00:00
draft: false
title: إطلاق النسخة النهائية الخامسة من منصة Qt
type: post
url: /2012/12/qt-5-final-released/
categories:
- Open source
- Unix/Linux
- برمجيات
tags:
- Android
- cross-platform
- Digia
- OpenGl
- QML
- ََQtَََ
- Qt5
- QtQuick
---

أطلقت اليوم شركة **Digia** المالكة لحقوق منصة **Qt**، النسخة الخامسة والتي طال انتظارها **Qt5**. والحقيقة ما تحمله هذه الإصدارة الراشدة من جديد لا يمكن حصره في مقال واحد، لكن سنحاول أن نعرض عليكم أهم ما جاءت به هذه النسخة.

![images](http://www.it-scoop.com/wp-content/uploads/2012/12/images.jpeg)


[
تعد Qt5](//qt.digia.com/qt5) إعادة هيكلة شاملة للنسخة Qt 4.x، حيث أصبحت وحدات الشفرة القاعدية Code base مجزّأة بشكل أكبر Modularized، مما يسمح لها للوصول إلى المزيد من المنصات، كما أنها أصبحت تعتمد على محرك OpenGL/OpenGL ES وإمكاناته لتسريع العرض وإضفاء المزيد من الحيوية على الرسوميات.

وفي ما يلي ملخص بسيط لما تحمله هذه النسخة من جديد:

<!-- more -->



	  * قدرات وأداء رسومي عالي مع تقنية **2 Qt Quick** واللغة الوصفية **QML** (الشبيهة بـ CSS)، إمكانية إضفاء حركيات 2D و 3D بسلاسة تامة.
	  * اعتماد **Javascript** للعمل جنبا إلى جنب مع لغة QML ، وإضافة Qt WebKit 2 لبناء التطبيقات باستخدام HTML5. كل هذا مع الحفاظ على الخيار الأساسي لاستعمال ++C خاصة مع Qt Widget.
	  * فصل المنصة إلى [Essentials](http://qt-project.org/doc/qt-5.0/qtdoc/modules.html) و [Add ons](http://qt-project.org/doc/qt-5.0/qtdoc/modules.html#qt-add-ons) مع اعتبار طبقة [Qt Platform Abstraction](http://qt-project.org/wiki/Qt-Platform-Abstraction) أو QPA، مما يسمح لـ Qt لعبور المزيد من المنصات كـ iOS ، Android و [BlackBerry](http://blog.qt.digia.com/blog/2012/12/17/blackberry-qt-porting-program/) هذا الأخير الذي تعتمد تطبيقاته في نسخته الأخيرة كليا على Qt. كذلك دعم جزئي (في الوقت الحالي) لنظام Windows 8.
	  * أصبح بالإمكان التطوير لمنصة **Android** باستعمال Qt عبر [مشروع Necessitas الذي انضم مؤخرا لـ Qt-project](http://blog.qt.digia.com/blog/2012/11/08/necessitas-android-port-contributed-to-the-qt-project/).
	  * دعم لشاشات Retina على منصة iOS.
	  * إضافة دعم لـ [Wayland](http://en.wikipedia.org/wiki/Wayland_%28display_server_protocol%29) الخليفة المرشح لاستبدال خادم العرض X11 على أنظمة Unix-like.
	  * بيئة التطوير [Qt Creator 2.6](http://blog.qt.digia.com/blog/2012/11/08/qt-creator-2-6-0-released/) والتي تم بناءها بـ Qt5 نفسها، والتي تدعم النسخة الجديدة من المنصة، ومشاريع Android والعديد...
	  * الحفاظ على توافقية رجعية كبيرة مع Qt4 حيث يمكن نقل تطبيقات Qt4 إلى Qt5 مع تغييرات طفيفة جدا، و Qt Creator 2.6 خير مثال على ذلك.
	  * دعم لكل من: JSON، C++11، الأجهزة ذات العتاد المقيد، الشبكات والاتصال، بروتوكول IPv6، اللمس وطرق الإدخال الجديدة، الوسائط المتعددة...
	  * [صياغة جديدة لطريقة اتصال Signal and Slots](http://qt-project.org/wiki/New_Signal_Slot_Syntax).

و[المزيد من الأمور](http://blog.qt.digia.com/blog/2012/12/19/qt-5-0/?utm_source=rss&utm_medium=rss&utm_campaign=qt-5-0) التي لا يمكن سردها هنا، الفيديو التالية تم عملها بـ Qt5 نفسها وهي عبارة عن ملخص جيد لما تحمله من جديد:


[youtube http://www.youtube.com/watch?v=vhWS_bN-T3k]


- يمكن تحميل الشفرة المصدرية للفيديو أعلاه [من هنا](http://qt.gitorious.org/qt-labs/qt5-launch-demo).

[رابط تحميل النسخة الجديدة](http://qt-project.org/downloads) من المنصة.

الجدير بالذكر أيضا، أن الأخ[ أحمد عصام](https://twitter.com/ahmed_isam)، صاحب مجتمع Qt العربي، قد بدأ سلسة من الدروس المصوّرة لتعليم منصة Qt، [يمكن الوصول إليها من هنا](http://qt-ar.org/community/viewforum.php?f=24).

- كيف ترى النسخة الجديدة من المنصة؟ وهل ستنقل برامجك إليها؟
