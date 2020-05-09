---
author: dzgeek
date: 2012-03-19 16:20:39+00:00
draft: false
title: 'جسر PySide ينضمّ إلى منصة Qt '
type: post
url: /2012/03/pyside-becomes-a-qt-add-on/
categories:
- Open source
- برمجيات
tags:
- Nokia
- PyQt
- PySide
- python
- Qt
- Qt Quick
---

بعد اعتمادها طريقة التطوير المفتوح حسب نموذج [Open Gouvernance](http://labs.qt.nokia.com/2010/06/03/qt-and-open-governance/) لمنصة [Qt](http://qt.nokia.com/)، إدخال تغييرات جذرية على المنصة، اعتماد [تقنية Qt Quick](http://qt.nokia.com/qtquick/) ولغة [QML ](http://en.wikipedia.org/wiki/QML)الوصفية لبناء واجهات تطبيقات تفاعلية (بل وحتى [نقل الواجهة مباشرة من Photoshop و Gimp](http://labs.qt.nokia.com/2010/10/19/exporting-qml-from-photoshop-and-gimp/)) ، إدخال HTML5 و Javascript، إمكانية التطوير لعدد لا بأس به من أنظمة تشغيل الهواتف، تقرر Nokia أن تضيف المزيد، و[تقرّب](http://www.pyside.org/2012/03/pyside-becomes-a-qt-add-on/) مشروع [PySide](http://www.pyside.org/) منها، لتصبح على شكل إضافة Add-on لمكتبة Qt التي يرى الكثير أنها واعدة جدا وذات مستقبل باهر ...

[![](http://www.it-scoop.com/wp-content/uploads/2012/03/PySide.png)
](http://www.it-scoop.com/wp-content/uploads/2012/03/PySide.png)ولمن لا يعرف [PySide](http://en.wikipedia.org/wiki/PySide) فهو عبارة عن جسر ([binding](http://en.wikipedia.org/wiki/Language_binding)) يربط ما بين لغة Python ومكتبة ++Qt/C برخصة حرّة، جاءت بعد مشاكل PyQt مع رخصة LGPL، لتكون بديلا لها (آنذاك)، ثم تقدمت بشكل سريع لتحاكي تطور PyQt و هاهي الآن تنضم لمشروع Qt بشكل رسمي، لتستفيد من جميع البنيات التحتية (القائمة البريدية، متابعة العلل على [Jira](https://bugreports.qt-project.org/secure/Dashboard.jspa)، حُكم الجدارة "meritocracy" حسب [نظام Open Gouvernance ](http://wiki.qt-project.org/The_Qt_Governance_Model)... ).

ومع هذا فإن عملية التحوّل ستكون شفافة وسلسة، الرخصة ستبقى نفسها، بعض الروابط ستتغير، المصدر -مثل Qt- [متوفر على Gitorious](http://qt.gitorious.org/pyside) للقراءة فقط، وأي مساهمات لابد أن تمر على [Gerrit ](http://codereview.qt-project.org/login/mine)أولا للـ Code review (نفسه أيضًا المستخدَم لـ Qt).

- ما رأيك أخي القارئ بهذا الاجتماع؟ وكيف تراه سينعكس على المستخدم؟
