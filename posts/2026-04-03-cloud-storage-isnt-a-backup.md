---
title: "Why Cloud Storage Isn’t a Backup"
date: 2026-04-03
slug: "cloud-storage-isnt-a-backup"
original_url: "https://www.atlascarolina.com/blog/cloud-storage-isnt-a-backup"
author: "Chad Keith"
source: atlascarolina
---

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/b264dea6-6f9d-4eb2-9314-c273e2661ded/cloud-storage-error-photo.jpg)

Many people assume that storing files in iCloud Drive, Box, Dropbox, Google Drive, or OneDrive means those files are backed up. After all, the files exist on remote servers maintained by large companies with professional IT teams and redundant storage. But that doesn’t mean they are backed up.

Cloud storage is tremendously useful and can play a valuable role in recovering from disasters, but it is not a backup. Understanding the difference could save you from a devastating data loss.

### What Makes a Backup a Backup?

A true backup creates a separate copy of your files through a process that’s distinct from your normal saving. With cloud storage, saving is syncing—the moment you save a file (or it auto-saves), that exact version propagates everywhere. There’s no separate copy, just one file that exists in multiple places simultaneously.

With a real backup system like Time Machine, backing up is an independent operation. You work on your file, saving changes as you go, and separately, on its own schedule, Time Machine backs up that file. If something happens to that file at 2 PM, you can still recover it from the 1 PM backup.

### Risks Not Mitigated by Cloud Storage

Why might you need a real backup? Computers and apps are significantly more reliable than they used to be, but they’re not perfect. Plus, human error is always a risk, and you can never discount the possibility of unexpected events.

Cloud storage won’t fully protect you from these scenarios:

● **Inadvertent deletion:** It’s all too easy to delete important files or folders. With cloud storage, those deletions are synced across all your devices and the cloud. (Though hopefully you can pull them out of the trash—never empty it immediately after deleting files.)

● **Accidental changes:** A misbehaving app could corrupt data in an important file, or, more likely, you could change or delete data within the file that you later decide was a mistake. With cloud storage, those changes sync instantly, making it difficult or impossible to revert.

● **Account compromise:** Cloud storage is protected only by your password. If you don’t use a strong, unique password, an online thief could use it to access your account and delete or encrypt your files.

● **Account problems:** Even if an attacker doesn’t compromise your account, if you lose the password, have billing issues, or do something that the provider considers a terms-of-service violation, you could be locked out of your account and all your files.

● **Ransomware:** If malware encrypts all your files, those encrypted files will be synced to the cloud and become unrecoverable everywhere. Ransomware isn’t a significant problem on the Mac today, but that could change at any time.

### How to Back Up Cloud Storage Files

The solution to these problems is not to stop using cloud storage, but to back up your cloud storage files just like you back up everything else. However, there are two things to keep in mind when backing up cloud storage.

First, verify that the local copies of your cloud storage files are being backed up. By default, the local versions of cloud-based files are stored in ~/Library/CloudStorage/ for everything but iCloud Drive, which puts files in the hidden folder ~/Library/Mobile Documents/. Time Machine automatically backs up your entire user folder, including cloud storage folders, but other backup apps may exclude them.

Second, cloud storage services can optionally store data only in the cloud to save local disk space, showing just placeholder icons on your Mac. These cloud-only files won’t be backed up by Time Machine or most other backup apps, though[ Carbon Copy Cloner can download them](<https://support.bombich.com/hc/en-us/articles/20686419951767-Backing-up-the-content-of-cloud-storage-volumes>), back them up, and then evict the local data to save space.

How do you ensure cloud storage files are also kept locally? All cloud services offer an option to Control-click a folder or file and choose a command like Keep Downloaded, Make Available Offline, or Always Keep on This Device. That works, but requires manual intervention.

For all the major cloud storage services other than Box, you can also set a preference to keep files locally at all times:

  * [**iCloud Drive**](<https://support.apple.com/guide/mac-help/optimize-storage-space-sysp4ee93ca4/26/mac/26>)**:**[ Turn off **Sy**](<https://support.apple.com/guide/mac-help/optimize-storage-space-sysp4ee93ca4/26/mac/26>)**stem Settings > _Your Name_ > iCloud > iCloud Drive > Optimize Mac Storage**.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/96ab8b23-0813-45e2-8f1c-ecb7d4972ba0/iCloud-Drive-Optimize-Mac-Storage.png)

  * [**Dropbox**](<https://help.dropbox.com/sync/make-files-online-only>)**:**[ Click ](<https://help.dropbox.com/sync/make-files-online-only>)the Dropbox icon in the menu bar and then, in **Dropbox > Account > Preferences > Sync**, choose Available Offline for the Default Sync Preference. Note that this applies only to new files!

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/49de847b-1586-4362-9408-02201747fdd0/Dropbox-available-offline.png)

  * [**Google Drive**](<https://support.google.com/drive/answer/2375012?visit_id=639075503365250802-2603154936&p=driveprefs&rd=1#Use_files_offline_for_desktop&zippy=%2Cstorage-consumption-on-the-local-hard-drive>)**:**[ Click the G](<https://support.google.com/drive/answer/2375012?visit_id=639075503365250802-2603154936&p=driveprefs&rd=1#Use_files_offline_for_desktop&zippy=%2Cstorage-consumption-on-the-local-hard-drive>)oogle Drive icon in the menu bar, click the gear menu, choose Preferences, click Google Drive, and select Mirror Files for the My Drive syncing options.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/76e24f44-335d-4a2d-99b2-5afa6d1bad60/Google-Drive-Mirror-Files.png)

  * [**OneDrive**](<https://support.microsoft.com/en-us/office/save-disk-space-with-onedrive-files-on-demand-for-mac-529f6d53-e572-4922-a585-e7a318c135f0>)**:**[ Click t](<https://support.microsoft.com/en-us/office/save-disk-space-with-onedrive-files-on-demand-for-mac-529f6d53-e572-4922-a585-e7a318c135f0>)he OneDrive icon in the menu bar, click More, click Preferences, and in the Preferences screen, make sure Files On-Demand is turned off.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/ef8ff678-091a-4127-96c6-6fd64bf35ccd/OneDrive-Files-On-Demand.png)

### What About Version History?

Most cloud storage services other than iCloud Drive offer version history, allowing you to restore previous versions of changed or deleted files. Version history provides a safety net against inadvertent deletions or modifications, but it’s not a substitute for comprehensive backups. It has two notable limitations:

● **Time:** Version history is typically limited to 30–180 days, depending on your plan. You might not realize you need a deleted file or that your database has become corrupted until after that window closes.

● **Trouble:** Restoring many files from version history can be tedious compared to restoring from a proper backup. It might be fine for a file or two, but recovering from a more significant disaster might be difficult.

### The Real Value of Cloud Storage

None of this means cloud storage is useless for disaster recovery. If your Mac fails, is stolen, or is destroyed in a fire, you can access all your cloud storage files as soon as you sign in to your account from a new or repaired Mac. You can even get to them from an iPhone or iPad. That also applies to Web apps like Google Docs, where data is never stored locally.

But cloud storage won’t protect against accidental deletion, file corruption, ransomware, or account issues. For that, you need separate, independent backups of all your files—including those stored in the cloud.
