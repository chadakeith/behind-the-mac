---
title: "Need to Share Files Securely? Try Password-Protected ZIP Archives"
date: 2021-09-20
slug: "need-to-share-files-securely-try-password-protected-zip-archives"
original_url: "https://www.atlascarolina.com/blog/need-to-share-files-securely-try-password-protected-zip-archives"
author: "Chad Keith"
source: atlascarolina
---

Imagine you’re staring at a file or folder—perhaps confidential employee information that you need to send to your accountant. If attaching it to an email message makes you think, “That doesn’t seem like a good idea,” award yourself a gold star!

Sending sensitive files via email is a bad idea, partly because the email could be intercepted in transit (possible but highly unlikely), but more because the files then live in both your and your recipient’s email accounts in an unprotected form. If an attacker were to gain access to either of your email accounts, they might scan for patterns like credit card numbers, ID numbers, phone numbers, and postal addresses and find them even in attachments.

There are ways of encrypting email messages so they can be read only by the recipient and never exist in an unencrypted form other than while being created or read, but they’re difficult to set up and fussy to use. For most people, most of the time, encrypted email is overkill.

For a more straightforward solution to exchanging information securely via email, use password-protected and encrypted ZIP archives. They’re easy to create on the Mac, either using a simple command in Terminal or with a third-party utility. And better yet, any Mac user can expand them using the built-in Archive Utility simply by double-clicking and entering the necessary password.​

### **Create Encrypted ZIP Archive Using Terminal**

Although many Mac users are intimidated by using the Unix command line in Terminal, making an encrypted ZIP archive is easy enough for anyone. All it takes is typing a single command, dragging a file or folder to Terminal, and entering a password twice. Follow these steps, which make an encrypted ZIP archive on your Desktop:

  1. In your Applications folder, open the Utilities folder and double-click Terminal to launch it.

  1. Type (or copy and paste) this command, replacing “archiveName” with whatever you want to name the ZIP file and making sure to type a space after the last letter—the “p” in “zip”. (The tilde ~ character is Shift-backtick, and it’s the key to the left of the numeral 1 key.)

zip -er ~/Desktop/archiveName.zip

  2. Drag the file or folder you want to protect into the Terminal window to complete the command.

  3. Press Return, and when prompted, enter the desired password twice—the second time is for confirmation.

![Terminal-encrypted-Zip.png](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/1632086970262-L72ZRICIKV95148GQ0WR/Terminal-encrypted-Zip.png)

### **Create Encrypted ZIP Archive Using Archiver**

If you have trouble with the command-line method or plan to create encrypted ZIP archives regularly, it’s worth using a Mac app that simplifies the process even more. There are various apps, but a particularly straightforward one for those running macOS 11 Big Sur is [Archiver](<https://archiverapp.com/>) ($19.99, with a free trial). Download it and then follow these steps to create an encrypted ZIP archive:

  1. Launch Archiver.

![Archiver-1.png](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/1632087025690-GL2FZY6WR3CPDAQ6HVHM/Archiver-1.png)

2\. Drag a file or folder to the Archiver window and click the Archive button in the toolbar.

![Archiver-2.png](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/1632087072416-CKI3FYAWY9I0ZL5ZSF9L/Archiver-2.png)

3\. Select the archive format (use ZIP), click the Encrypt checkbox, enter the password twice, and click the Archive button in the toolbar.

![Archiver-3.png](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/1632087106374-E24E72V65NJ2OOBAXAL3/Archiver-3.png)

4\. Drag the ZIP archive to the Desktop or another folder and click the Done button.

![Archiver-4.png](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/1632087152830-80QCO2R6S42BH2O89EPJ/Archiver-4.png)

### **Decrypting a ZIP Archive**

As noted earlier, decrypting a password-protected ZIP archive on the Mac is as simple as double-clicking it and entering the password when prompted.

![Decrypt-Zip-archive-Mac.png](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/1632087196932-UYD9S8QHC6ACGQ8HVHZV/Decrypt-Zip-archive-Mac.png)

What about iOS or iPadOS? Never fear, since the Files app can also decrypt ZIP archives; just tap the archive to open it and enter the password when prompted.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/1632087233240-S9ZNGG84YS7ZDHJP48HW/Decrypt-Zip-archive-iPhone.jpg)

### **A Word about Passwords**

It’s important to think briefly about how you’re going to communicate the password to your recipient. Don’t send it in email or else anyone who compromises either your email account or your recipient’s account could decrypt the ZIP archive.

Instead, use what’s called an “out of band” communication channel. In other words, if you’re going to send the ZIP archive via email, communicate the password in a phone call or text message. That would keep the password safe if either of your email accounts were compromised.

If you’re sending password-protected ZIP archives to a particular person regularly (and the files don’t contain state or corporate secrets), you could agree on a system for generating passwords so you don’t have to communicate each one individually. For instance, you could combine a random word and the current month, so the password would be “cheddar9September” one month and “cheddar10October” the next.

As you can see, you can use this technique with so little extra effort that it’s worth ensuring a higher level of security whenever you need to share confidential information.
