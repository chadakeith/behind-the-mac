---
title: "Don’t Listen to Anyone Who Tells You to Drag a Text File into Terminal"
date: 2024-12-20
slug: "dont-drag-a-text-file-into-terminal"
original_url: "https://www.atlascarolina.com/blog/dont-drag-a-text-file-into-terminal"
author: "Chad Keith"
source: atlascarolina
---

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/52e3f3cc-0552-4cce-bf00-43c1020e9b8e/hacker-terminal-photo.jpg)

In macOS 15 Sequoia, Apple made it more difficult to bypass Gatekeeper to run apps that aren’t notarized. (Notarization is one of the ways Apple ensures that apps distributed outside the Mac App Store are unmodified and free from malware.) Cybercriminals have responded to this increase in security with a new social engineering attack. They provide the victim with a disk image, ostensibly to install some desired piece of software, instructing the user to drag a text file into Terminal. Doing so executes a malicious script that installs an “infostealer” designed to exfiltrate a wide variety of data from your Mac. The simple advice here is to treat any guidance to drop a file into Terminal with extreme suspicion—no legitimate software or developer will ever ask you to do that.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/6abfbf2e-006f-4419-a09e-736d18baf2ee/Drag-and-drop-infostealer.jpg)
