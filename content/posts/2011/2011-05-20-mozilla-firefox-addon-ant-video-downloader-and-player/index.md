---
author: يوغرطة بن علي (Youghourta Benali)
date: 2011-05-20 21:49:48+00:00
draft: false
title: Mozilla تسحب إضافة  خاصة بـ Firefox لتجميعها بيانات المستخدمين دون علمهم
type: post
url: /2011/05/mozilla-firefox-addon-ant-video-downloader-and-player/
categories:
- Security
- Web
- متصفحات
tags:
- Ant Video Downloader and Player
- Firefox
- Mozilla
- privacy
- Simon Newton
---

[**Mozilla تسحب إضافة  خاصة بـ Firefox لتجميعها بيانات المستخدمين دون علمهم**](https://www.it-scoop.com/2011/05/mozilla-firefox-addon-ant-video-downloader-and-player)


قامت Mozilla بسحب (أو بالأحرى تعليمها كتجريبية) إضافة [Ant Video Downloader and Player](https://addons.mozilla.org/fr/firefox/addon/video-downloader-player/) (الخاصة بتحميل الفيديوهات من المواقع التي تعرضها) من معرض إضافات Firefox لقيامها بتجميع بيانات المستخدمين دون علمهم و هو ما يخالف [القواعد](https://addons.mozilla.org/en-US/developers/docs/policies/submission) المعمول بها لدى المؤسسة.


[![](firefox-addons.jpg)
](https://www.it-scoop.com/2011/05/mozilla-firefox-addon-ant-video-downloader-and-player)


المخالفة لا تخص تجميع البيانات في حد ذاتها و إنما  لكون الإضافة لا تشير إلى ذلك في حين أنه إجباري مثلما [أشار إليه](http://www.theregister.co.uk/2011/05/20/firefox_addon_privacy_invasion/) موقع  The Register الذي استشهد بما قاله أحد متحدثي Mozilla الرسميين. و يعود الفضل إلى اكتشاف الأمر إلى الباحث الأمني Simon Newton الذي يشير على [مدونته](http://iwtf.net/2011/05/10/ant-video-downloader-firefox-addon-tracking-my-browsing/) أنه اكتشف الأمر عن طريق الصدفة لما كان يحاول فهم خطأ لدى كتابته لتطبيق ويب، حيث لاحظ أن كل استعلامات HTTP التي يقوم بها متصفحه كان ترسل بطريقة آلية إلى الخادم rpc.ant.com

و يضيف Newton أن الإضافة تستعمل معرفا عاما يسمح بمعرفة كل ما يقوم به المستخدم أيا كان و حتى و إن استخدم وضع التصفح الخاص أو مر عبر VPN خاص أو عبر مشروع Tor.

الإضافة التي تشهد رواجا كبيرا ([أزيد من 7 ملايين تحميل](https://addons.mozilla.org/en-US/statistics/addon/8174) على متصفح Firefox) لا تزال متوفرة على [موقعها الرسمي](http://www.ant.com/video-downloader) كما تتوفر أيضا على متصفح Internet Explorer مما يزيد من حجم البيانات التي تحصل عليها.

السؤال الذي يطرح نفسه هو كيف لم يتم اكتشاف هذا الوضع رغم كون الإضافة مفتوحة المصدر (هل فعلا فتح مصدر البرنامج دليل على أمانه) ؟

و ما الفائدة من مرحلة التحقق من كل إضافة قبل قبولها في معرض إضافات Firefox إن كانت تسمح بمرور مثل هذه الإضافات؟
