---
title: "Tim Cook’s last day as Apple CEO"
date: 2026-09-01
slug: "tim-cooks-last-day-as-apple-ceo"
original_url: "https://www.atlascarolina.com/blog/tim-cooks-last-day-as-apple-ceo"
author: "Chad Keith"
source: atlascarolina
---

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/7b496c96-2f15-4c5d-a1ea-ef8aa8053216/tim-cook-apple-park.jpg)

Photo: Brooks Kraft, Apple Park, 2021. Used under CC BY 4.0.

Today, September 1, 2026, is John Ternus’s first day as CEO of Apple. Tim Cook’s last day in the job was yesterday, August 31. Apple announced the change in April: Ternus becomes CEO effective September 1, and Cook becomes executive chairman the same day. He is not leaving the company.

Cook took over on August 24, 2011, after Steve Jobs stepped down. Jobs died later that year. A lot of people said Cook would live in the shadow of Steve Jobs. Fifteen years later, that take did not age well.

Cook did not try to be Jobs. He ran Apple like an operations person who still cared about the product. The iPhone stayed the center of the business. Around it, Apple built watches, wireless audio, its own Mac chips, a services layer, and a security story that IT teams actually have to live with. Apple’s own April note puts the growth in plain numbers: market cap from about $350 billion to $4 trillion, yearly revenue from $108 billion in fiscal 2011 to more than $416 billion in fiscal 2025.

This is Atlas’s thank you. We are an Apple Technical Partner in Davidson and Charlotte. Most of the Macs, iPhones, and iPads we manage at work were designed on Cook’s watch.

## Hardware that shipped while Cook was CEO

Steve Jobs era products still mattered (iPhone, iPad, Mac). The list below is what Apple launched or reinvented after August 2011. Years are first public launch or first ship.

### iPhone

  * iPhone 4S (2011), then iPhone 5 through the iPhone 16 line

  * iPhone 17, iPhone 17 Pro, iPhone 17 Pro Max, and iPhone Air (September 2025)

  * Touch ID on iPhone 5s (2013)

  * Larger Plus and later Max sizes

  * iPhone X (2017): Face ID, OLED Super Retina, no Home button

  * iPhone SE as the smaller, lower-cost line

  * MagSafe charging on iPhone 12 and later

  * Emergency SOS via satellite on iPhone 14 and later

  * USB-C on iPhone 15 and later

### iPad

  * iPad mini (2012)

  * iPad Air

  * iPad Pro (2015) with Apple Pencil and Smart Keyboard, later M-series chips and mini-LED

  * Face ID on iPad Pro, Touch ID in the top button on Air and others

### Mac

  * Retina MacBook Pro and MacBook Air refreshes, then the 12-inch MacBook, Touch Bar years, and the T2-chip Macs

  * Apple silicon: M1 Macs in 2020 (MacBook Air, 13-inch MacBook Pro, Mac mini, then iMac, MacBook Pro 14/16, Mac Studio, Mac Pro)

  * 24-inch iMac, Studio Display, Pro Display XDR

  * Touch ID on MacBook keyboards and Magic Keyboard

  * MacBook Neo, the lower-cost Mac laptop Apple called out in the same CEO transition note

### Apple Watch

  * Announced 2014, shipped 2015. First major new product category of the Cook years

  * Series updates, Apple Watch SE, Apple Watch Ultra

  * ECG, blood oxygen, crash detection, later sleep and heart features that made it a health device, not just a notification bracelet

### Audio, home, and accessories

  * AirPods (2016), then AirPods Pro, AirPods Max, USB-C and hearing-health features on later Pro models

  * HomePod (2018), HomePod mini, second-generation HomePod

  * Apple TV 4K

  * AirTag (2021)

  * MagSafe accessories and the modern Find My network accessories

### New computing

  * Apple Vision Pro (announced 2023, shipped 2024) as Apple’s spatial computer, with Optic ID

We are not pretending every one of those was a hit. Vision Pro is still a specialist device. The Watch and AirPods became everyday hardware. Apple silicon is why a lot of offices could finally treat the Mac as the default work computer again.

## Security that actually showed up on the device

Cook’s Apple talked about privacy in ads. The useful part for us is what landed in hardware and OS, because that is what we deploy with Jamf and what we explain to customers.

  * **Secure Enclave.** A separate security chip on the device. Keys, Touch ID, and Face ID data stay there, not in a random folder on the SSD.

  * **Touch ID (2013) and Face ID (2017).** Unlock, Apple Pay, and app auth without putting a password on a sticky note. Face ID maps the face on-device. It is not a cloud face search.

  * **Activation Lock and Find My.** Stolen Macs and iPhones stay bricks without the Apple Account. The Find My network later used other Apple devices to locate AirTags and offline devices.

  * **System Integrity Protection, Gatekeeper, and signed system volume on Mac.** Harder for junk to rewrite the OS. Apple silicon Macs boot from a hardware root of trust.

  * **T2 chip, then Apple silicon.** Hardware disk encryption, secure boot, and Touch ID on Mac in a way Intel-era Macs never quite matched.

  * **Two-factor authentication** for the Apple Account, later hardware security keys for people who need a physical key.

  * **App Tracking Transparency (2021).** Apps have to ask before tracking people across other companies’ apps.

  * **Privacy labels on the App Store.** Not perfect. Better than a PDF nobody reads.

  * **iCloud Private Relay and Hide My Email** on iCloud+.

  * **Passkeys.** Device-bound keys instead of reused passwords. Works with iPhone, iPad, Mac, and the password manager most of our customers already have on the device.

  * **Lockdown Mode (2022, iOS 16).** Extreme, optional protection for people who might be targeted by mercenary spyware. Most offices should not turn this on for everyone. It exists, and that matters.

  * **Advanced Data Protection for iCloud (rolled out late 2022 into 2023).** End-to-end encryption for iCloud Backup, Photos, Notes, and more, so Apple holds fewer keys.

  * **Stolen Device Protection (iOS 17.3)** and **Rapid Security Responses.** Extra Face ID or Touch ID prompts for account changes if the phone is away from familiar places, and small security fixes that do not wait for a full iOS release.

None of this replaces MDM. Jamf still enrolls the Mac. FileVault still needs a policy. Lockdown Mode is not a substitute for who has local admin. It is a better floor than 2011.

## Services that sat next to the hardware

Cook’s business story was services on top of the devices: Apple Pay (2014), Apple Music, iCloud storage growth, Apple TV+, Apple Arcade, Apple Card, later Apple Intelligence on the device. Apple says Services passed $100 billion a year on his watch. We mention it because the hardware and the Apple Account are one system now. Lose the account, and the laptop is not just a laptop.

## John Ternus and what we hope for next

Ternus joined Apple’s product design team in 2001 and has been there about 25 years. He became senior vice president of Hardware Engineering in 2021. Cook’s line: “the mind of an engineer, the soul of an innovator, and the heart to lead with integrity and with honor.” His first big public moment as CEO is expected at Apple’s September product event.

We want a CEO who still treats Mac, iPhone, and security as one product, not a phone company with a PC hobby. Apple Intelligence has to get better. MDM and Apple Business still need to work on day one of a new OS. That is the unglamorous bar.

## Why this belongs on our site

Atlas is an Apple Technical Partner and a Jamf MSP. We did not pick Apple last year because it was trendy. We have been in this stack for a long time, including the years when people said Cook would not measure up to Jobs.

If your Mac and iPhone fleet is the Cook-era hardware above, we can help you keep it enrolled, encrypted, and current.

[Book a 30-minute call](<https://scheduler.zoom.us/chad-keith-atlas/30-minute-meeting>)
