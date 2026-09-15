---
title: "Never Save Your Work in These Locations"
date: 2025-03-11
slug: "never-save-your-work-in-these-locations"
original_url: "https://www.atlascarolina.com/blog/never-save-your-work-in-these-locations"
author: "Chad Keith"
source: atlascarolina
---

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/ac5c3e66-41d7-4a8c-bfbd-e0b9a34ab45e/save-to-folders-photo.jpg)

In every job that involves interaction with the public, amusing “Can you believe…” stories about customers abound. They’re often triggered by seemingly reasonable behaviors that experts recognize as problematic. A well-known example from the early days of personal computing is a college student who kept track of his floppy disk by attaching it to his fridge with a magnet, not realizing that magnetic fields could disrupt the disk’s magnetic patterns and corrupt files. The advice from tech support? “Don’t do that.”

No one is sticking floppies to their fridge anymore, but we still occasionally see the modern equivalent: saving data or documents in places that are likely to disappear. Just as you shouldn’t write the only copy of essential information on an easily erased whiteboard, you shouldn’t store important data in any of these locations:

  * **Unsaved documents:** While autosave is becoming more common, it isn’t universal and often doesn’t activate until a document has been saved for the first time. When you create a new document, always save it right away, before you do anything else. Otherwise, you risk losing all your work if the app crashes, the Mac kernel panics, or the power goes out.

  * **Trash:** We know, we know! Who would put something in the Trash that they want to keep? But it happens. Don’t do that! On the other hand, there’s also no reason to empty your Trash regularly unless you’re low on space. A good compromise is to choose **Finder > Settings > Advanced** and select “Remove items from the Trash after 30 days.” This way, you’ll always have a 30-day grace period to recover mistakenly deleted items.

  * **Clipboard:** Most people know that the clipboard serves as a temporary holding place, overwritten with each new Copy or Cut. However, if you’re unaware of this, you might write something lengthy, use Cut to place it on the clipboard with the intention of pasting it elsewhere, and then forget to do so right away, resulting in data loss on the next use of Copy or Cut. Always paste anything you cut immediately. Many utilities (such as [Copy ‘Em](<https://apprywhere.com/ce-mac.html>), [Keyboard Maestro](<https://www.keyboardmaestro.com/>), [LaunchBar](<http://www.obdev.com/products/launchbar/>), [Pastebot](<https://tapbots.com/pastebot/>), and [Raycast](<https://www.raycast.com/>)) provide clipboard history so you don’t lose clipboard data immediately, but you still shouldn’t rely on it persisting indefinitely.

  * **Email Drafts mailbox:** There’s nothing wrong with starting an email and coming back to it later to finish—that’s the point of the Drafts mailbox. It’s also a sensible way to begin a message on one device and complete it on another. However, avoid storing anything in Drafts for an extended period, and be aware that items there may disappear without warning. (And never, ever store anything in your email Trash mailbox—it will be deleted eventually.)

  * **Temporary folders:** Thanks to its Unix roots, macOS includes several temporary folders, one located at /tmp and others specific to each user. These folders are cleared regularly, such as when the Mac is restarted, left idle for a long time, or when drive space is low. Storing important data in a temporary folder is a digital version of Russian roulette.

  * **Downloads folder:** Although the Downloads folder isn’t inherently volatile, it’s unwise to store anything important there. You might forget about that document while tidying up and accidentally delete it, or you might use a cleanup tool in the future that does it for you.

  * **USB flash drives:** There is nothing wrong with putting files on a USB flash drive. However, avoid storing the only copy of an important file on one, as it is too easy for the drive to be lost or damaged.

  * **Public computers, virtual machines, and sandboxed environments:** This scenario is unlikely but not impossible. Imagine you’re working on a public computer in a lab and save a file on the desktop. When that computer reboots, it will likely delete all data to return to a fresh state for the next user. The same could apply to a virtual machine used for testing or a sandboxed environment that you log in to remotely.

There are also a few locations that generally aren’t problematic but deserve extra attention due to the higher likelihood of losing data:

  * **Third-party app folders in ~/Library:** Some apps store their data in folders they maintain within your user account’s Library folder. While this is acceptable for data managed by those apps, we advise against putting anything else in these folders since it’s impossible to know how the app might deal with data it doesn’t recognize during a cleanup or major update.

  * **Desktop:** It’s fine to work on documents stored on the desktop, but we recommend filing them away carefully when you’re finished. If you frequently move files in and out of your desktop, it’s all too easy to delete something important accidentally. Additionally, if you have iCloud Drive’s Desktop & Documents folder syncing enabled, you might unintentionally delete files from another Mac due to being in a different context.

  * **Box, Dropbox, Google Drive, iCloud Drive:** Cloud storage services are entirely acceptable locations for important data, but they all offer options that store files only online, downloading them only when necessary. These options may prevent online-only files from being accessible when you’re offline or from being backed up locally. Worse, if you share cloud storage with others for collaboration, they could accidentally delete your data. Be sure to enable any available version history options and ensure everything is backed up locally.

  * **External drives or network storage:** Many individuals and organizations store essential files and data on external drives and network storage. This approach is perfectly valid, provided that these locations are backed up. When designing your backup system, remember to include your external drives, network servers, and NAS devices. Lastly, if an external drive is encrypted, ensure that you have a backup of both its data and the decryption key.

If you want to avoid all these issues, save your files in your Documents folder and make sure you have a solid backup strategy.
