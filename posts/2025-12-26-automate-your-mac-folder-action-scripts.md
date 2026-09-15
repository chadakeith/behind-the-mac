---
title: "Automate Your Mac with Folder Action Scripts"
date: 2025-12-26
slug: "automate-your-mac-folder-action-scripts"
original_url: "https://www.atlascarolina.com/blog/automate-your-mac-folder-action-scripts"
author: "Chad Keith"
source: atlascarolina
---

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/b7f6f8fc-d696-45d6-af34-9a8eda46f42b/AI-folder-action-scripts-photo.jpg)

Do you repeatedly find yourself wanting to do something in the Finder with every file of a certain type? Perhaps you regularly download files from a particular website that come in with a .txt extension, even though they’re CSV files that should have a .csv extension? Or maybe you want to rename files according to their creation date whenever they’re moved into a specific folder? Or copy every file whose name matches a specific string to a remote file server?

Your desires will undoubtedly differ from everyone else’s, but the key to automating file-related actions in the Finder is a longstanding macOS technology called _folder action scripts_. In essence, you attach a custom AppleScript to a folder, and whenever the folder’s contents change, the script runs. Anything you can do with AppleScript, you can automate with a folder action script.

Don’t panic at the sight of the word “AppleScript.” Although creating a folder action script requires creating an AppleScript, we don’t expect you to write an AppleScript or even know much about it. You can get an AI chatbot like ChatGPT, Claude, or Gemini to write the actual code—all you need to do is explain what you want to the chatbot, copy and paste code into Script Editor, and link the script to the desired folder.

Two warnings: always start with test files in a test folder before letting a script work on real files in a real folder, and be doubly cautious about scripts that move files to the Trash.

Let’s get started! We’ll use the CSV renaming script as an example.

### Step 1: Create a Script with AI Help

When working with an AI chatbot to write an AppleScript, it’s helpful to be as specific as possible. Here’s the prompt we started with:

Write an AppleScript that I can use to make a folder action script for my Downloads folder. I want it to detect a newly downloaded file that has a .txt extension and present me with a dialog with two buttons asking if I would like to change the filename extension to .csv (the default) or leave it as .txt.

Paste that into the chatbot of your choice, and it will return a script. Copy it to the clipboard—chatbots usually include a button to copy just the text of the script, so you don’t have to select it manually.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/87d435c2-7df2-4468-b11c-cab71dc2984d/Claude-AppleScript.png)

### Step 2: Save Your Script

Now you need to turn that script into something functional. Follow these steps:

  1. Open Script Editor, which you’ll find in the Utilities folder in your Applications folder.

  2. Choose **File > New** to create a new script.

  3. Paste the text of the script from the chatbot into the script.

  4. Click the hammer icon in Script Editor’s toolbar to check for syntax errors. If there are none, the text turns from all purple to various colors, as shown below. (We’ll assume the script is correct for now; more on how to fix errors in Step 4 below.)

  5. Choose **File > Save**, and in the Save dialog, navigate to ~/Library/Scripts/Folder Action Scripts/ (that’s the Library folder in your user folder). If the Folder Action Scripts folder doesn’t exist within Scripts, press Command-Shift-N (while still in the Save dialog) to create a new folder. Be sure to name it exactly Folder Action Scripts.

  6. Still in the Save dialog, choose Script from the File Format pop-up menu and click Save to save the file.

### Step 3: Connect Your Script to a Folder

To open the Folder Actions Setup app, you may be able to Control-click the desired folder (such as a Test folder on your desktop) and choose Folder Actions Setup from the pop-up menu; it might also be in a Services submenu. But the easiest way to open it is with Spotlight. Press Command-Space, type Folder Actions Setup (or enough of the name for Spotlight to find it), and press Return. Once you have the app open:

  1. Select the Enable Folder Actions checkbox at the top.

  2. Click the + button under Folders with Actions, and open the Test folder in the file dialog.

  3. Click the + button under Script, then select the script you just saved—the list is sorted alphabetically, so you may need to scroll.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/147fde58-b826-4749-859c-809381c9c7be/Script-Editor-error.png)

A folder can have multiple folder action scripts linked to it, though be aware that they can interact with one another in unexpected ways. You can disable a script by deselecting its checkbox or remove it entirely by selecting it and clicking the – button. To make changes to a script, select it and click Edit Script to open it in Script Editor.

### Step 4: Test Your Script

This is the moment of truth—did the chatbot get it right? Create a text file in TextEdit and save it on the desktop with a .txt extension. Then drag it into the Test folder and see if you’re prompted to rename it to .csv. If so, you’re done!

But what if it doesn’t work? What to do depends on how it failed:

● **Script Editor complains about syntax errors:** Report the error to the chatbot by taking a screenshot like the one below and pasting or dragging it into the chatbot text entry field. It will analyze the screenshot to identify the error and try to provide you with revamped code that fixes the problem.

● **Nothing happens:** First, verify that the folder action is enabled in Folder Actions Setup and that the correct folder is listed. Then return to the chatbot and say exactly that. “I dropped a .txt file in my Test folder, but nothing happened.” It will analyze the code it previously wrote and attempt to address whatever is causing it to fail.

● **You get a permissions request:** The first time a folder action script runs, macOS may ask for permission to control the Finder or access certain folders. Click Allow when prompted.

● **You get some other error:** Just as with code errors in Script Editor, your best bet is to take a screenshot of the error and paste it into your chat. Be sure to add any additional information that might shed light on the reason for the error.

● **The wrong thing happens:** If something else happens, but it’s not what you want—like more files being acted on than you intended—go back to the chatbot and describe precisely what happened and how that was wrong, reiterating the results you want to achieve.

It’s not uncommon to go back and forth with the chatbot several times to end up with an AppleScript that works as you want. If you still have trouble, ask the chatbot to add debugging alerts that show you where the process breaks down.

### Other Useful Folder Action Ideas

Once you’ve mastered the basics, consider these automation possibilities:

● Automatically resize images added to a folder to specific dimensions

● Sort downloaded files into subfolders based on file type

● Add a timestamp or custom prefix to every file added to a project folder

● Play a sound or send a notification when files matching certain criteria appear

● Back up critical files by copying them to a second location whenever they’re added to a watched folder

There’s undoubtedly a DIY aspect to all this, but folder action scripts are both a practical use of AI chatbots and a relatively easy way to automate file-based workflows that are tedious or time-wasting when done by hand. If you’re attracted to the idea but uninterested in fussing with chatbots, Script Editor, and Folder Actions Setup, look into Noodlesoft’s[ Hazel](<https://www.noodlesoft.com/>), a $42 utility that provides an easy-to-use interface for automatically organizing files on your Mac.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/1f36b005-7b11-40b4-bccf-38f7f8382da8/Hazel.png)
