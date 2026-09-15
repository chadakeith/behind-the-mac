---
title: "When Should You “Ignore Ownership” on an External Drive?"
date: 2024-08-06
slug: "ignore-ownership-external-drive-permissions"
original_url: "https://www.atlascarolina.com/blog/ignore-ownership-external-drive-permissions"
author: "Chad Keith"
source: atlascarolina
---

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/c687dd29-b277-42e6-b3a9-d77dd7bb325a/Ignore-Ownership-external-drive-text-photo.jpg)

Under the hood, macOS relies on Unix, which is a multi-user operating system. That’s why a Mac can host multiple users who, as long as they don’t know each other’s passwords, cannot see each other’s files. To maintain each user’s privacy, macOS relies on permissions that specify who can do what with any given file or folder. For the most part, permissions work how they’re supposed to, letting you work with all your files and keep any other users on the Mac out of your stuff.

Where things can get tricky is with external drives. In some situations, permissions can prevent you from accessing files written to an external drive on one Mac from another Mac. That happens because the first admin user account created on a Mac is given the UniqueID of 501, regardless of its name. (Because, Unix.) If you create additional accounts, they get UniqueIDs of 502, 503, and so on. Again, the names are irrelevant; all that matters is the UniqueID.

If you write files to an external drive while logged into the 501 admin account on one Mac but then try to access those files from an account with any other UniqueID on that Mac or any other, macOS won’t let you. No 503 account, for instance, can access a 501 account’s files.

There are tweaky Unix solutions to this problem, but Apple realized this would be an issue from the early days of Mac OS X and provided a single-click solution: the “Ignore ownership on this volume” checkbox. When selected, it tells macOS to pay no attention to permissions for all the files and folders on a drive, regardless of what that might mean.

To access this setting, select the drive in the Finder, choose File > Get Info, and expand the Sharing & Permissions section at the bottom. Before you can select the checkbox, click the lock icon and enter your admin password when prompted.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/2e01b46a-596c-40a2-b2f9-c516918cd537/Ignore-ownership-off-on.png)

There are three scenarios where enabling “Ignore ownership on this volume” is helpful:

  * **Multi-user access:** Imagine that you share a Mac with family members or colleagues. You want to keep your email and text message conversations private but need to share numerous other large files stored on an external drive. (For just a few files, use the Shared folder alongside your user folders.) By enabling “Ignore ownership,” you can be certain that all users of the Mac can do whatever they need to with those files.

  * **Access from multiple Macs:** Suppose you have a portable SSD containing video files you want to display from any Mac. Perhaps they’re canned business presentations or home videos. Since you cannot know what the UniqueID of the current account on any given Mac will be, selecting “Ignore ownership” will ensure that you can open your videos regardless.

  * **Juggling user accounts:** Although it’s a bad idea to do this willy-nilly, some people regularly create and delete accounts for their own use. Since all the accounts are used by a single person, they don’t think about permissions as an issue, but macOS does unless they select “Ignore ownership.”

In general, when using an external drive to move files between accounts, people, or Macs, select “Ignore ownership” to prevent pesky permissions problems.

But that doesn’t mean you should turn on “Ignore ownership” in every situation. There are some situations where enabling the setting would be inappropriate because it’s essential to preserve permissions:

  * **Boot drives:** macOS itself relies on specific permissions and won’t even show the checkbox for boot drives. If you’re planning to install macOS on an external drive and use it to boot a Mac ([Apple provides instructions](<https://support.apple.com/en-us/111336>)), make sure not to select “Ignore ownership” before starting.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/b1625f39-9839-42d4-9100-7027f7e4ede0/Boot-drive.png)

  * **Time Machine drives:** Time Machine cares deeply about maintaining correct permissions, so you should not enable “Ignore ownership” on a drive that you plan to use with Time Machine. After Time Machine starts backing up to a drive, the “Ignore ownership” checkbox disappears.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/c1653977-af5c-4a48-9872-99fa74b88947/Time-Machine-drive.png)

  * **Bootable duplicates and other backups:** Similarly, if you’re using [Carbon Copy Cloner](<https://bombich.com/>) or [SuperDuper](<https://www.shirt-pocket.com/SuperDuper/SuperDuperDescription.html>) to create a bootable duplicate of your boot drive, “Ignore ownership” must be unchecked. [Retrospect](<https://www.retrospect.com/>) also warns users to turn off “Ignore ownership” on backup and restore drives to ensure that permissions are preserved. Other backup apps likely have similar requirements.

One last thought. If you run into permissions-related problems reading files from an external drive, it’s worth enabling “Ignore ownership” to see if that resolves your issues. If it doesn’t, or if the problems keep cropping up in different contexts, contact us.

(Featured image based on an original by iStock.com/Rawpixel)
