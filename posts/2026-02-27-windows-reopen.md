---
title: "Why Your Windows Reopen (Or Don’t) As You Expect"
date: 2026-02-27
slug: "windows-reopen"
original_url: "https://www.atlascarolina.com/blog/windows-reopen"
author: "Chad Keith"
source: atlascarolina
---

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/29cf73f0-1a2c-43a1-8e36-7200815adea2/red-Restore-key-photo.jpg)

Have you noticed that when you restart your Mac or relaunch an app, your previous windows and documents sometimes reappear exactly as you left them, but at other times you’re greeted with a clean slate?

This behavior is controlled by Resume, a technology introduced in OS X 10.7 Lion back in 2011. Resume automatically reopens app windows and documents so you can pick up where you left off after a restart or app relaunch. Apple’s goal was to make macOS work more like iOS, which tries to preserve your place in apps. However, many Mac users found it confusing when apps opened old documents or appeared in unexpected positions when the number of displays changed. Some also objected to how long it took to open old documents that were not relevant to the task at hand. Apple quickly reversed course and made reopening apps and windows optional.

Users are much more familiar with how the iPhone and iPad work now, so you may wish your Mac apps remembered their open documents and window positions.[ Various settings control this behavior](<https://support.apple.com/en-us/102318>), but it can be hard to find them and understand what they’ll do. Let’s explore how Resume works and how you can make it do what you want.

First, note that Resume operates in two distinct situations. One applies only at restart or logout, and you decide at that moment. The other governs what happens every time you quit and relaunch an app and is controlled by a persistent system setting.

### The “Reopen Windows” Option at Restart

Whenever you restart, shut down, or log out of your Mac, macOS asks whether you want to reopen your apps and windows when you log back in. You’ve undoubtedly seen the checkbox in the confirmation dialog: “Reopen windows when logging back in.” When the checkbox is selected, macOS dutifully relaunches the currently running apps after you log in, putting you back where you were. If you uncheck it, your Mac will start fresh, without reloading previously open apps.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/2bb2b675-6080-4516-baa5-d533aedc9752/Reopen-windows.png)

macOS remembers how you’ve selected this checkbox, so if it’s checked when you click Restart, it will also be selected the next time you restart, and vice versa. If you ever perform a forced restart or skip the dialog by holding the Option key when choosing Restart or Shut Down, macOS uses the last known state of that checkbox on the next startup.

Many users either love or hate the “Reopen windows” behavior. For those who enjoy having their entire workspace restored after a reboot, keeping that checkbox checked makes sense. For others, including many IT professionals, the point of a reboot is to start fresh. Pick whichever behavior you prefer.

### Controlling Resume When Relaunching Apps

Resume also governs what happens each time you quit and reopen an individual app. This behavior is controlled by a switch in **System Settings > Desktop & Dock** under the Windows section, labeled “Close windows when quitting an application.”

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/2c0b5506-5f1a-4b98-826b-ac5c0a15be40/Close-windows-setting.png)

When this “Close windows” switch is turned on—it’s the default—macOS will close all windows and discard their restorable state before allowing an app to quit. Because macOS has closed the windows before quitting, there’s nothing for Resume to restore when you next launch that app. Effectively, the app will always start fresh with no memory of past windows (unless it has its own session-restore mechanism).

On the other hand, when this option is turned off, quitting an app will not discard its windows, so when you reopen the app later, Resume will automatically restore whatever documents and windows you had open, putting you right back where you left off.

There are three main scenarios where Resume can have effects that you may or may not like:

● **Document-centric apps:** With these apps, like Pages and Numbers, you work on individual documents, each of which opens in its own window. When “Close windows” is enabled, apps start fresh on each launch; when it’s disabled, the documents you were working on when you quit reopen automatically.

● **Unsaved documents:** As a corollary to the previous scenario, if you have unsaved documents open when “Close windows” is on, you’ll be prompted to save your changes before the window is closed. When “Close windows” is off, you won’t be prompted because those documents—with all their unsaved changes—will open automatically at the next launch.

● **Window-based apps:** Other apps, like Mail and Messages, display their content in a main window. They’ll open this window regardless of the “Close windows” setting. However, Resume determines _where_ that window appears. If “Close windows” is turned on, macOS does not remember which display or Space the window occupied, so the app often reopens on the primary display, even if that’s not where it was when it quit.

Most users have no idea that this “Close windows” setting exists or what it does. If you’re irritated by having to reopen Pages documents you were working on before or reposition Mail’s window after every relaunch, make sure “Close windows” is turned off. Conversely, leave it on if you want apps to start fresh.

### Exceptions and Caveats

For most people, controlling Resume using the “Reopen windows” checkbox and the “Close windows” switch is sufficient. However, some people may want more control or wonder why some apps ignore those settings.

● **Nonstandard apps:** Everything we’ve said so far describes the behavior of standard apps using Apple’s recommended development frameworks and tools. Some apps don’t use Apple tools or play by Apple’s rules—we’re looking at you, Microsoft—and will ignore the Resume settings. Don’t be surprised if Word, Excel, and PowerPoint fail to act as described.

● **Turn off Resume per launch:** If you set apps to restore their windows by turning off the “Close windows” switch, you can override that on a one-off basis in some apps by holding the Shift key down as they launch. This trick doesn’t work in all apps, but it’s worth trying.

● **Custom session restore:** Some apps manage session restoration on their own, most notably[ Safari](<https://support.apple.com/en-us/102192>) and apps built with the Electron framework, such as Slack, Discord, and Notion. For instance, in **Safari > Settings > General > Safari opens with**, you can choose a new window, a new private window, all windows from the last session, or all non-private windows from the last session. With such apps, look for internal settings that control their behavior.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/010267fb-2021-4233-89fa-75dbdc6a6393/Safari-session-launch.png)

● **Login Items:** Even if you deselect “Reopen windows” when restarting, apps and documents that you’ve added as login items in **System Settings > General > Login Items & Extensions > Open at Login** will still open. Think of this as a manual Resume—you’ll restart to a preset workspace, not to the way things were when you restarted. Some software may also install helper apps that control what appears at launch.

● **Full-screen apps and Spaces:** Apps that were last used in full-screen mode reopen into their own Spaces when “Close windows” is disabled. After a restart or relaunch, the app may appear not to have reopened because it is occupying a separate Space that is currently not visible.

In practice, Resume comes down to a simple set of choices:

● If you want your workspace restored after a restart, select “Reopen windows when logging back in.” Ensuring that apps—even if they’re set as login items—open full-screen or in particular Spaces also requires “Close windows when quitting an application” to be turned off.

● If you want apps to remember documents (even unsaved documents), window positions, and displays when you quit and relaunch them, turn off “Close windows.”

● If you want a clean slate, deselect “Reopen windows” and leave “Close windows” turned on.

When windows don’t appear as you expect, check these two settings as your first troubleshooting step.
