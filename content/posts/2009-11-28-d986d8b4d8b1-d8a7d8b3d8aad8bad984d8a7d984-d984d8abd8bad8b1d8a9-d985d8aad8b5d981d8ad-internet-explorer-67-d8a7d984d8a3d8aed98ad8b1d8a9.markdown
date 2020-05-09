---
author: Xacker
date: 2009-11-28 18:20:37+00:00
draft: false
title: نشر استغلال لثغرة متصفح Internet Explorer 6/7 الأخيرة
type: post
url: /2009/11/%d9%86%d8%b4%d8%b1-%d8%a7%d8%b3%d8%aa%d8%ba%d9%84%d8%a7%d9%84-%d9%84%d8%ab%d8%ba%d8%b1%d8%a9-%d9%85%d8%aa%d8%b5%d9%81%d8%ad-internet-explorer-67-%d8%a7%d9%84%d8%a3%d8%ae%d9%8a%d8%b1%d8%a9/
categories:
- Microsoft
- Security
- متصفحات
tags:
- Exploit
- internet explorer
- PoC
- remote code execution
---

يبدو أن 0-day PoC [لثغرة IE 6/7 الأخيرة التي كتبنا عنها منذ بضع أيام](http://www.it-scoop.com/2009/11/microsoft-%D8%AA%D8%A4%D9%83%D8%AF-%D9%88%D8%AC%D9%88%D8%AF-%D8%A7%D9%84%D8%AB%D8%BA%D8%B1%D8%A9-%D8%A7%D9%84%D9%85%D9%83%D8%AA%D8%B4%D9%81%D8%A9-%D8%AD%D8%AF%D9%8A%D8%AB%D8%A7-%D9%81%D9%8A-internet-e/) تم نشره في الانترنت بمجرد اكتشاف الثغرة وفقاً لتقرير أعدّته Symantec.


![](http://djug.developpez.com/rsc/Internet_Explorer_7_Logo.png)




الاستغلال يستهدف ثغرة مكتشفه في الطريقة التي يستخدم متصفح Internet Explorer معلومات CSS المستخدمة في معظم صفحات الويب على الانترنت.


PoC:




![exploit.IE7](http://www.it-scoop.com/wp-content/uploads/2009/11/exploit.IE7_.PNG)




حان الوقت للانتقال إلى متصفح آخر، ولو بشكل مؤقت.. لكن هل يمكن أن تنتقل إلى الإصدار 8 في ظل نشر خبر آخر بأن IE8 و ميكانيكية الحماية من XSS تحوي على خطأ تصميمي يخلق ثغرات XSS في المواقع التي لا تحوي أساساً على ثغرات؟ :D
المصدر:


[Zero-Day Internet Explorer Exploit Published](http://www.symantec.com/connect/blogs/zero-day-internet-explorer-exploit-published)




[http://www.securityfocus.com/archive/1/507984/30/0/threaded](http://www.securityfocus.com/archive/1/507984/30/0/threaded)
