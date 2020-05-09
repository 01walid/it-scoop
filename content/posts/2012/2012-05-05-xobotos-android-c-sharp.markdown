---
author: يوغرطة بن علي (Youghourta Benali)
date: 2012-05-05 19:43:28+00:00
draft: false
title: 'XobotOS: نسخة من نظام Android مكتوبة بلغة C# من شأنها أن تخلص Google من مشاكلها
  مع Oracle حول لغة Java  '
type: post
url: /2012/05/xobotos-android-c-sharp/
categories:
- Google
- Open source
- برمجيات
- هواتف/ أجهزة لوحية
tags:
- Android
- C++
- Dalvik
- Google
- Java
- Miguel de Icaza
- Mono
- Sharpen
- Xamarin
- XobotOS
---

أعلن **Miguel de Icaza** الأب الروحي لإطار عمل Mono (النسخة مفتوحة المصدر من إطار عمل Dotnet) ومؤسس شركة **Xamarin** الناشئة التي ترعاه، عن إطلاق **XobotOS**، نسخة من نظام **Android** أُعيدت كتابتها بلغة **C#** ومتخلصة بشكل كامل من لغة Java.




[![](https://www.it-scoop.com/wp-content/uploads/2012/05/XobotOS.jpg)
](https://www.it-scoop.com/wp-content/uploads/2012/05/XobotOS.jpg)




وفي [التدوينة](http://blog.xamarin.com/2012/05/01/android-in-c-sharp/) التي يعلن فيها عن الأمر يشير de Icaza إلى استعانة فريقه بمترجم **Sharpen** الذي يقوم بترجمة شفرات Java إلى C# والذي عملوا على إدخال تحسينات عليه لهذه المناسبة، مما سمح لهم بترجمة كامل شفرة Android إلى لغة ومنصة أكثر حرية، ويتعلق الأمر بلغة C# وإطار عمل Dotnet.




ماذا يعني ذلك؟ سيصبح بالإمكان كتابة تطبيقات لنظام Android (أو بالأحرى لإصدار XobotOS) بلغة C# دون أن يتطلب ذلك أي ترجمات إضافية، لكن المثير في الأمر هو أن هذه التطبيقات هي أكثر كفاءة من التطبيقات التي تكتب بلغة Java، وذلك نظرا لنضج Runtime  الخاص بإطار عمل Mono المتقدم مقارنة بالآلة الافتراضية الخاصة Dalvik (آلة Java الافتراضية الخاصة بنظام Android) والتي لا تزال حديثة السن. كما أن هذه الآلة الافتراضية لا تستفيد من التحسينات التي تعرفها آلة HotSpot التي تطورها Oracle.




[![](https://www.it-scoop.com/wp-content/uploads/2012/05/mono-vs-dalvik.png)
](https://www.it-scoop.com/wp-content/uploads/2012/05/mono-vs-dalvik.png)




لكن هل فعلا إطار عمل Dotnet ولغة تطوير C# هي أكثر انفتاحا من Java؟ نعم الأمر كذلك، حيث أنه سبق وأن قامت Microsoft بتقديم لغة  C# إلى ECMA لجعلها لغة قياسية standardization، كما أن هذه اللغة متوفرة تحت رخصة Microsoft Community Promise، مما يعني أن كل شركة لها القدرة على استعمالها مثلما شاءت دون الحاجة إلى شراء أية تراخيص حول الأمر.




ماذا عن كفاءة XobotOS؟ تشير التجارب التي أجرتها Xamarin بأن كفاءة Mono تصدر في بعض الحالات إلى 7 أضعاف كفاءة Dalvik. الأمر مرشح للذهاب إلى أبعد من ذلك، حيث أن مطوري الشركة يعكفون حاليا على تطوير القسم المتعلق بالرسوميات، وذلك للتمكن من الوصول إلى المكتبة البرمجية Skia من دون الحاجة إلى المرور عبر Java.




[
](https://www.it-scoop.com/wp-content/uploads/2012/05/mono-vs-dalvik.png)




تجدر الإشارة إلى أنه سبق وأن ["ورثت" Xamarin كل "تركة" Suse](https://www.it-scoop.com/2011/07/novell-xamarin-mono/) فيما يخص مشروع Mono ولواحقه، كما أنه سبق لها وأن أطلقت تطبيق [Mono for Android](https://www.it-scoop.com/2011/04/mono-for-android-dotnet/) الذي يسمح بكتابة تطبيقات لنظام Android باستعمال لغة C#. بعبارة أخرى، Xamarin تعي وتعرف جيدا المجال الذي دخلت إليه.




مشروع XobotOS متوفر للتحميل على GitHub [من هنا](https://github.com/xamarin/XobotOS).




هل ستنقذ Microsoft منافستها Google من أطماع Oracle في نظام تشغيلها؟ وهل سنسمع قريبا عن شراء Google لشركة Xamarin الراعية لمشروع XobotOS؟
