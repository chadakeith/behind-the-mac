---
title: "Apple’s iCloud Keychain Password Management Is All Many People Need"
date: 2024-05-03
slug: "apples-icloud-keychain-password-management-is-all-many-people-need"
original_url: "https://www.atlascarolina.com/blog/r0xstf49tin4ssam5nnd7qmswn48g0"
author: "Chad Keith"
source: atlascarolina
---

We constantly recommend using a password manager like [1Password](<https://1password.com/>), [BitWarden](<https://bitwarden.com/>), or [Dashlane](<https://www.dashlane.com/>). But many people resist committing to yet another app or paying for yet another service. Isn’t Apple’s built-in iCloud Keychain password management good enough?

The answer now is yes, thanks to two recent changes:

In iOS 17.3, Apple added [Stolen Device Protection](<https://support.apple.com/en-us/HT212510>), which leverages biometric authentication—Face ID or Touch ID—to protect users against thieves who would surreptitiously learn someone’s passcode, steal their iPhone, and then take over their digital lives. One of the worst aspects of that attack was that the iPhone passcode was sufficient to access the user’s stored passwords, so the thief could get into everything.

Until mid-2023, Apple’s built-in password management worked only in Safari, which was problematic for users who rely on other browsers. Then Apple updated its [iCloud Passwords](<https://chromewebstore.google.com/detail/icloud-passwords/pejdijmoenmkgeppbflobdenhhabjlaj>) extension for Google Chrome to work not just in Windows, but also in Mac browsers based on Google Chrome running in macOS 14 Sonoma. There’s also now an [iCloud Passwords](<https://addons.mozilla.org/en-US/firefox/addon/icloud-passwords/>) add-on for Firefox.

If you aren’t yet using a password manager, try iCloud Keychain.​

### Passwords Basics

Apple integrated iCloud Keychain into macOS, iOS, and iPadOS at a low level, so you mostly interact with your passwords in Safari. But first, make sure to enable [iCloud Keychain](<https://support.apple.com/en-us/109016>) so your passwords sync between your devices. On the Mac, you do that in System Settings > _Your Name_ > iCloud > Passwords & Keychain. On an iPhone or iPad, it’s in Settings > _Your Name_ > iCloud > Passwords and Keychain.

If you’re using a browser other than Safari, install the iCloud Passwords extension or add-on and activate it by clicking it in the toolbar and entering the verification code when prompted.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/efb01f9e-8251-4cf3-8824-2528eeed4cda/iCloud-Passwords-code.png)

When it comes to website accounts, there are two main actions: creating a login and logging in to a site:

**Create a new login:** When you need to create an account on a new website, after you enter whatever it wants for email or username, Safari creates a strong password for you. Unfortunately, the iCloud Passwords extension or add-on on the Mac can’t generate passwords—you can either create a strong password manually or switch to Safari temporarily to let it create one. When you submit your credentials, you’ll be prompted to save them.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/2d884a28-cc81-4425-9bec-28ebe9d6d326/iCloud-Keychain-create-login.png)

**Autofill an existing login:** The next time you want to log in to a site for which you’ve saved credentials, Safari or your other browser on the Mac displays a pop-up with logins matching the domain of the site you’re on. On the iPhone or iPad, you might get an alert at the bottom of the screen or have to pick a choice in the QuickType bar above the keyboard.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/14d467c2-0932-4c3d-92eb-cea32b5fd532/iCloud-Keychain-login.png)

For basic usage, that’s it! However, iCloud Keychain can make mistakes. The site shown above asks for both an email address and a username and wants the email address for logging in, but iCloud Keychain remembered the username instead. Happily, Apple makes it easy to fix such unusual missteps. On the Mac, open System Settings > Passwords, or on the iPhone or iPad, open Settings > Passwords. Here’s where you find and edit your saved logins.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/8da2b955-2dbb-4025-84ca-e226c721b47d/iCloud-Keychain-Passwords-UI.png)

Open the desired login by double-clicking it on the Mac or tapping it on the iPhone or iPad, then click or tap Edit and make any desired changes.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/2a2a6769-934b-40c6-8263-d8f1b77cef02/iCloud-Keychain-editing.png)

iCloud Keychain provides additional features and options:

A search field at the top of the Passwords window or screen helps you find logins if scanning the full list is frustrating.

You can use commands in the **+** menu to create new passwords and shared groups. On the Mac, commands in the ••• menu let you import and export passwords; the iPhone and iPad use that menu to bulk-select passwords for deletion and show generated passwords.

Shared groups let you share a subset of passwords with family or colleagues. Choosing New Shared Group triggers an assistant that walks you through naming the group, adding people from Contacts, and choosing which passwords to share. You can move passwords between groups at any time.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/9d14a4d2-5d1f-4cc4-8e29-30b271aa17d3/iCloud-Keychain-Shared-Group.png)

The Security Recommendations screen displays logins exposed in known breaches and points out logins with weak passwords. Check those and update them as necessary.

In Password Options, you can turn off autofill, but why would you? Another option automatically deletes verification codes you receive in Messages after it inserts them with autofill.

On websites that support two-factor authentication, you can set up a login to autofill the verification code. During setup on the site, you’ll get a QR code you can scan with an iPhone or iPad if you’re using a Mac; if you’re using an iPhone or iPad, touch and hold the QR code and choose Add Verification Code in Passwords. Once you finish configuring the login, you’ll have to enter the six-digit verification code on the site to link it with the login.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/7f6fc445-eea5-4a34-a7cb-4a4da7e80494/iCloud-Keychain-2FA.jpg)

Overall, iCloud Keychain provides the password management features that most people need, and it’s a massive security improvement over keeping a document of your passwords on your desktop.

(Featured image by iStock.com/loooby)
