---
title: "Never Run AppleScripts from Untrusted Sources"
date: 2026-06-02
slug: "applescripts-from-untrusted-sources"
original_url: "https://www.atlascarolina.com/blog/applescripts-from-untrusted-sources"
author: "Chad Keith"
source: atlascarolina
---

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/e98d5aa5-ed36-434d-995c-bfc1910e0b40/Script-Editor-malware-photo.jpg)

The la[t](<https://www.jamf.com/blog/clickfix-macos-script-editor-atomic-stealer/>)est scam to watch out for is fake websites that try to get you to open Script Editor directly from your browser with a pre-filled AppleScript. Don’t do this! Security researchers at[ Jamf Threat Labs documented an attack](<https://www.jamf.com/blog/clickfix-macos-script-editor-atomic-stealer/>) wh[ere a convincing Apple-themed page cl](<https://www.jamf.com/blog/clickfix-macos-script-editor-atomic-stealer/>)aiming to help “reclaim disk space” prompted users to allow Script Editor to open, then used the applescript:// URL scheme to open a seemingly legitimate script that—if the user ran it—would download and install the Atomic Stealer malware. In macOS 26.4, a new warning in Script Editor flags the script as from an unidentified developer, which should alert more users to the danger. (Yet another reason to install macOS updates!) The rule is simple: never run an AppleScript unless you wrote it yourself or acquired the code from a source you trust. If a website asks to open Script Editor—or any other app—click Cancel, and if you ever see this warning, close the script immediately. No legitimate webpage needs to run scripts on your Mac.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/1894de7a-bfd0-45de-9d40-266079affd87/Safari-script-warning.png)
