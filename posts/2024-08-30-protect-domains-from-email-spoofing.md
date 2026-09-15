---
title: "Protect Domains That Don’t Send Email from Email Spoofing"
date: 2024-08-30
slug: "protect-domains-from-email-spoofing"
original_url: "https://www.atlascarolina.com/blog/protect-domains-from-email-spoofing"
author: "Chad Keith"
source: atlascarolina
---

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/784312fd-1779-4b24-b6ed-31f0cf8b91b7/protect-non-email-domains-text-photo.jpg)

We recently wrote an article for those who manage their own Internet domain names about using SPF, DKIM, and DMARC to prevent your domains from being used in phishing attacks and enhance the deliverability of legitimate email. But what about other domains you own but don’t use for email? To make phishing attacks more believable, spammers sometimes forge email so it appears to come from parked domains that aren’t protected. You can use SPF, DKIM, and DMARC to ensure that forged email that seems to come from your unused domains isn’t accepted. The details are too specific to go into here, but Cloudflare has an [excellent article outlining what you need to do](<https://www.cloudflare.com/learning/dns/dns-records/protect-domains-without-email/>).

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/b49390da-b04f-47d2-89b7-571794e881bb/SPF-DKIM-DMARC-for-no-email-domains.png)
