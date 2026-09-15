---
title: "Feel Free to Upgrade to macOS 15 Sequoia When You’re Ready"
date: 2025-01-28
slug: "upgrade-to-macos-15-sequoia"
original_url: "https://www.atlascarolina.com/blog/upgrade-to-macos-15-sequoia"
author: "Chad Keith"
source: atlascarolina
---

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/ba29ff80-31ab-488d-afdf-1457d62a55ae/Sequoia-upgrade-Apple-Park-photo.jpg)

While we typically advise caution when considering upgrades to the latest major macOS release, we believe Apple has sufficiently refined [macOS 15 Sequoia](<https://www.apple.com/macos/macos-sequoia/>) to warrant an upgrade for those interested. You don’t need to upgrade immediately, but there are no significant reasons for most people to delay further.

The big win in upgrading now is that Apple has released betas of most of its promised Apple Intelligence features for Macs with Apple silicon. In other posts, we’ve looked at the artificial intelligence-driven features that arrived in macOS 15.1 and macOS 15.2, including:

  * Writing Tools for proofreading, rewriting, summarizing, and composing text

  * Clean Up in Photos for removing background objects, plus natural language searches

  * Audio recording in Notes, with transcription and summarization

  * Summaries replacing snippets in Mail message lists, plus summarization of long messages or threads

  * A Smart Reply feature in Mail and Messages for quick replies

  * Notification summaries that reduce distractions from chatty apps

  * Integration of ChatGPT with Siri

  * Image Playground for generating custom images based on your descriptions

Sequoia has been quite stable, with two caveats. First, there have been some networking issues related to Apple’s built-in firewall and VPNs; we don’t yet know if macOS 15.2 resolves these. Second, macOS 15.2 introduced a new bug that causes problems for backup apps trying to make bootable backups on Apple silicon Macs. Although that’s annoying and will likely be fixed shortly, Apple has been deprecating bootable backups for years in the name of security. The modern approach is to install macOS from macOS Recovery, then use Migration Assistant to restore from Time Machine or a data-only backup.

Apple will continue to release macOS updates in 2025. If past performance is any indication, you can expect macOS 15.3 in January, 15.4 in March, and 15.5 in May with a few new features, plus a few security and bug fix updates in between.

That said, you can put off the Sequoia upgrade as long as you’re running macOS 13 Ventura or macOS 14 Sonoma and are staying current with Apple’s security updates. Earlier macOS versions no longer receive security fixes, rendering them more vulnerable to attack. Possible reasons to continue delaying include:

  * **You’re too busy.** The upgrade process will take a few hours, plus some additional time to configure everything properly afterward. When you are ready to upgrade, aim for when a little downtime will be convenient.

  * **You rely on incompatible software.** The jump from Ventura or Sonoma to Sequoia isn’t a big one, so most modern apps should have been updated by now. But if a necessary app is known to have issues, you’ll either need to wait for an update or switch to an alternative that works.

Sequoia may not transform your experience of using a Mac, but it has new features you might appreciate beyond Apple Intelligence. The most noticeable is probably iPhone mirroring, which lets you use your iPhone in a window on your Mac. Also potentially interesting are its new window tiling features that let you quickly arrange windows, the standalone Passwords app, Highlights and Distraction Control in Safari, and collapsible headers in Notes.​

### Before You Upgrade

Once you’ve decided to upgrade to Sequoia, you have three main tasks:

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/5f24eeef-ad93-461b-b501-96461f2625ee/Sequoia-upgrade-App-Store.png)

  * **Update apps:** Make sure all your apps are as up-to-date as possible. If you regularly put off updates, now’s the time to let them complete so you have Sequoia-compatible versions.

  * **Clear space:** Sequoia may need as much as 25 GB of free space to upgrade, and the Sequoia installer itself is nearly 15 GB, so we recommend making sure you have at least 50 GB free. Don’t cut this close—you should always have at least 10–20% free space for virtual memory, cache files, and breathing room. Check in Sonoma or Ventura by choosing System Settings > General > Storage; in earlier versions of macOS, choose About This Mac from the Apple menu and click Storage. System Settings provides quick ways to free up space. Another easy option for iCloud Drive users is to Control-click large folders and choose Remove Download to “evict” the local versions of those files temporarily; Box, Dropbox, and Google Drive have similar features.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/fd45295a-9311-4521-b17e-bbb441c32e71/Sequoia-upgrade-clear-space.png)

  * **Make a backup:** Never, ever install an update to macOS without ensuring you have at least one current backup first. In an ideal world, you’d have an updated Time Machine backup, a data-only duplicate, and an Internet backup. That way, if something goes wrong, you can quickly revert.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/b62acab9-ffa0-4a20-ae59-8c2d9ab127d8/Sequoia-upgrade-Time-Machine.png)

### Upgrading

After completing those tasks, ensure you won’t need your Mac for a few hours. There’s no telling exactly how long the upgrade will take, so never start an upgrade if you need the Mac soon.

To initiate the upgrade, open System Settings > General > Software Update in Sonoma or Ventura (System Preferences > Software Update in previous versions of macOS), click the Upgrade Now button, and follow the instructions. If you’d like more guidance, check out Joe Kissell’s ebook [_Take Control of Sequoia_](<https://www.takecontrolbooks.com/sequoia/>).

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/da7491d2-c8fe-40e7-9992-327f218cc1d7/Sequoia-upgrade-Software-Update.png)

### After You Upgrade

Part of the reason to set aside plenty of time for your Sequoia upgrade is that there are usually cleanup tasks afterward. We can’t predict precisely what you’ll run into, depending on what version of macOS you’re running now and what apps you use, but here are a few situations we’ve noticed in the past:

  * macOS may need to update its authentication setup by asking for your Apple ID password, your Mac’s password, and, if you have another Mac, its password. Don’t worry that malware has compromised your Mac—these authentication prompts are fine.

  * Some apps may have to ask for various permissions even though you previously granted them. Again, that’s fine.

  * If you use your Apple Watch to unlock your Mac and apps (and you should; it’s great!), you may need to re-enable that in System Settings > Touch ID & Password (or Login Password on a non-Touch ID-enabled Mac). In older versions of macOS, it was in System Preferences > Security & Privacy > General.

  * If you use Gmail, Google Calendar, or other Google services, you may need to log in to your Google account again.

  * Websites that usually remember your login state may require you to log in again. However, if you’re using a password manager like Apple’s Passwords or [1Password](<https://1password.com/>), that’s easy.

  * You may have to re-enable text message forwarding to your Mac. You do this on your iPhone in Settings > Messages > Text Message Forwarding.

With all that housekeeping done, it’s time to check out all the [new features in Sequoia](<https://www.apple.com/macos/macos-sequoia/pdf/macOS_All_New_Features_Sept_2024.pdf>)!

(Featured image by Apple)
