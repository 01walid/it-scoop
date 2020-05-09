---
author: dzgeek
date: 2012-08-06 18:01:56+00:00
draft: false
title: '[مقال] منصة Qt ... إلى أين؟'
type: post
url: /2012/08/the-future-of-qt/
categories:
- Open source
- أخبار الشركات
- برمجيات
tags:
- Digia
- Nokia
- QML
- Qt
- Qt Quick
- RIM
---

**تحديث:**

[تم الإعلان عن بيع Nokia منصة Qt إلى Digia.](https://www.it-scoop.com/2012/08/digia-to-acquire-qt-from-nokia/)

لا يخفى على كل عارف بمنصة Qt قوتها، حجمها، عتاقتها، عدد البرامج الهائل ومنصات الهواتف التي تعتمد عليها، كما أنها تشهد تطويرا كثيفا للإصدارة الخامسة منها ولتقنية QML لكن ... Nokia، وجهة هذه الأخيرة لم يعد يعجب المطورين أنفسهم، خاصة مع تبنيها التصنيع لأجهزة Windows Phone وعقدها الأخير مع Microsoft، وآخر ما تم الإعلان عنه (نهاية شهر يوليو): [غلق مكتب Qt بأستراليا](http://lists.qt-project.org/pipermail/development/2012-August/005467.html)، أين يعمل مطوري اللواحق Qt3D ،QtDeclarative ،QtMultimedia ،QtSensors ،QtSystems module ،Qt Location . بمتابعتي للقائمة البريدية لمطوري منصة Qt، أحدث هذا الإعلان شرارة كشفت عن أسرار أخرى،...  شرارة بدأت في رسم مصير Qt في ظل Nokia، والحالة النفسية للمطورين.

[![](https://www.it-scoop.com/wp-content/uploads/2012/08/Qt-300x149.png)
](https://www.it-scoop.com/wp-content/uploads/2012/08/Qt.png)

**هل.. ؟**

هل سيتوقف تطوير Qt؟ - قطعا لا، خاصة مع اعتمادها على[ نظام Open Governance](http://labs.qt.nokia.com/2010/06/03/qt-and-open-governance/) وطبيعة تطويرها المفتوحة فلا يمكن لأية شركة إيقاف تطويرها، لكن هدف المقال مناقشة **وتيرة** التطوير التي ستؤول إليها والتأثيرات التي ستحدث على المنصة في ظل Nokia وسياستها الحالية، من سيدفع للمطورين ويأويهم، [خاصة بعد ما رد أحدهم على القائمة البريدية](http://lists.qt-project.org/pipermail/development/2012-August/005478.html) الشيء الجلل التالي، بعد خبر غلق مكتب أستراليا:


<blockquote>يا ناس:

لم يكن في نيتي ذكر هذا لكن وبما أنه قد أثير هذا الموضوع ...

فإن مصدرا أعتبره وثيقا همس في أذني أن في أعقاب Nokia مؤخرا

قتل نظام Meltemi، وقد قُدم توجيه مباشر لـ Sebastian Nyström

(نائب الرئيس الأول لدى Nokia المسؤول عن Qt ) لبيع باقة Qt.

خبرات Nokia الكبيرة في المنصة (على الهواتف وخلاف ذلك قد انتهت)

* بعد قتل أنظمة Symbian و Maemo/Meego سابقا.</blockquote>





<blockquote>Atlant

> 
> Folks:
> 
> 

> 
> I wasn’t going to mention this but since the topic has come up…
> 
> 

> 
> A source I consider reliable has whispered in my ear that
in the aftermath of Nokia recently shooting Meltemi dead*,
Sebastian Nyström (the Nokia Senior VP in charge of Qt) has
been given explicit direction to sell-off the Qt asset.
> 
> 

> 
> Nokia’s great experiment in frameworks (mobile and otherwise)
is over.
> 
> 

> 
> Atlant
> 
> 

> 
> * After having previously shot Symbian and Maemo/MeeGo dead
> 
> 
</blockquote>


وكما يبدو جليا، فإن في نية Nokia إن صح ما قال، بيع Qt والتخلي عنها!

لم يصدر أي بيان رسمي بعد من Nokia ولا من المطورين أنفسهم، لكن ما ذُكر في القائمة البريدية، شيء منطقي شبه محتوم، فلم تعد هناك استفادة فعلية مباشرة لـ Nokia من Qt في منتجاتها، بعضهم رجح أن Nokia في انتظار إصدار Qt 5.0 للقيام بهذه الخطوة. وفي نفس الوقت الذي أحبط فيه الخبر أناسا، استبشر آخرون به، لما؟ - لأنه قد يشتري Qt من يرعاها ويعطيها انتباهه أحسن من Nokia، فلوّح بعظهم باحتمالات من شركات وجهات معروفة أمثال: Blue Systems (التي استثمرت مؤخرا في توزيعة Kubuntu)  وأيضا Digia صاحبة النسخة التجارية من المنصة، Jolla ،Linux Foundation وأخيرا .Intel

**RIM ؟**

خيار آخر لوّح الكثير، هو شركة RIM، هذه الأخيرة التي أبدت اهتماما بـ Qt مؤخرا بل وأصبحت خيارها الأول، كما أن لها منتجات مبنية عليها ومنصة BlackBerry10 SDK. لكن السؤال الذي يطرح نفسه، الكل يعرف أن RIM حاليا في [وضع لئيم](https://www.it-scoop.com/2011/12/who-will-eat-rim/)، فهل بإمكانها الوقوف مجددا وشراء Qt ؟ حسب ردود المطورين على القائمة البريدية، الأمر وارد وغير مستبعد، بل ومرجوٌ أن تكون لـ RIM.

**مزاج المطورين:**

من الردود يظهر حب المطورين لعملهم على Qt وتشبثهم بها، فرغم أسف بعضهم، فهناك من صرح مواصلة العمل حتى ولو على حساب وقته الخاص، آخرون دعوا إلى النظر إلى الجانب الإيجابي من الأمر ودعوا إلى عدم الركون ومواصلة تطوير المنصة وجعلها أفضل.

** الخلاصة:**

طبيعة المجلة التقنية عدم نشر الإشاعات السابقة لأوانها، لذا آثرت جعل هذا الخبر على شكل مقال حتى يظفي عليه زي النقاش، خاصة وكونه مستمد من محادثات[ القائمة البريدية](http://lists.qt-project.org/pipermail/development/).

الشيء المؤكد بخصوص Qt هو أن وراءها مجتمع قوي ونشيط جدا، و همة عالية لمواصلة التطوير، لكن الشركة الراعية الجديدة، وما بعد Nokia وحال النفقات يبقى أمرا مجهولا، نأمل أن يكون في أيدٍ خير من أيد Nokia ولو أنه عند حدوث هذا، فأكيد سيكون هناك شيء من الخسارة، كون خبرة Nokia على المنصة كبيرة. عسى أن تعوض لاحقا أو أن تنتقل.

ما رأي القارئ في ما ذكرت؟ ومن ترجح من الشركات القادمة إن حصل وباعت Nokia منصة Qt ؟
