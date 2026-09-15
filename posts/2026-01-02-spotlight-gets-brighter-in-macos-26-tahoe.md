---
title: "Spotlight Gets Brighter in macOS 26 Tahoe"
date: 2026-01-02
slug: "spotlight-gets-brighter-in-macos-26-tahoe"
original_url: "https://www.atlascarolina.com/blog/spotlight-gets-brighter-in-macos-26-tahoe"
author: "Chad Keith"
source: atlascarolina
---

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/9b0bb634-9c25-4beb-ac29-1e1aff5ad3e3/Spotlight-stage-photo.jpg)

Spotlight has been a staple on macOS for decades, and at various points in its history, Apple has added new search capabilities. However, the revamp that Spotlight enjoyed in macOS 26 Tahoe is the most significant change in a long time. Here are the new features you’ll experience in Tahoe.

### Filterable Interface

Apple has refocused the Spotlight interface to list all result types in a single view, rather than separating them by type as before. Apple claims the results are intelligently ranked, so in theory, what you’re most likely to want will appear at the top. As before, you invoke Spotlight with Command-Space, but when you start typing, it tries to auto-complete using the top hit. In the screenshot below, the user typed “Apple” and Spotlight added “Configurator” in white. Keep typing to change the autocomplete, double-click a result to open it, or use the arrow keys to select a result and press Return to open it or Tab to search inside it.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/ca13f0b0-8d29-4d95-8ce2-3e9f459f9bb6/Spotlight-new-UI.png)

Having all the results in a single window may still be overwhelming, so Spotlight now lets you filter the results in several ways. Most notable is the horizontally scrollable line of buttons above the search results that lets you filter the results list to particular files or data types, results from specific apps, files stored in a third-party file provider like Google Drive, and even menu items. For example, clicking the Calendar button above the results shows only matching events.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/74327596-13e2-4cd2-b952-4e374b97e502/Spotlight-buttons.png)

Spotlight also features new dedicated browsing modes, so if you press Command-1 through Command-4 (or wiggle the pointer after invoking Spotlight to reveal browsing mode buttons), Spotlight limits the results to specific types of items:

● **Applications:** Press Command-1 to display all your apps in a Launchpad-like view; type a few letters to filter the results to matching apps. The button row at the top lets you filter further by App Store category.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/6bcb089b-cdc2-4516-953c-6ef8502ea14d/Spotlight-apps.png)

● **Files:** Press Command-2 for a file browser. Although Spotlight provides suggestions and recent files, you’ll probably want to type words from the filename. The button row lets you limit the results to specific file types or documents from specific apps.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/9de433e1-e284-4958-bae9-3dcdb3701210/Spotlight-files.png)

● **Actions:** Press Command-3 to see a long list of actions you can now perform from Spotlight. Many of these are from Apple’s apps, but third-party apps can also expose actions via Spotlight. More on this new feature shortly.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/69150d01-aa47-4b0c-9435-0f85a44966f4/Spotlight-actions.png)

● **Clipboard:** Press Command-4 to see what you have copied to the clipboard recently and insert selected items with a click. More on clipboard history later, too.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/26e13525-f9e8-4c87-a26b-e72892fe46dd/Spotlight-clipboard.png)

Spotlight provides three additional ways to filter the results:

● **By location:** To search within top-level macOS containers and third-party cloud containers, you can type the location name and press Tab before typing a search string. Filtering by location works for the Desktop, Documents, Downloads, and Applications folders, as well as iCloud Drive, Google Drive, Dropbox, and OneDrive. (You may need to select the folder from the search results manually before pressing Tab the first few times; this trains Spotlight.) Unfortunately, searching by location doesn’t work for arbitrary folders; use a Finder search instead.

● **By app:** To filter the results to include only documents that a specific app can open, type its name and press Tab. Enter a search string to search within the filtered results.

● **By kind:** You can filter kinds of files by typing / and then the file type, like /PDF or /text, and then pressing Return. For even more[ kind searches](<https://support.apple.com/guide/mac-help/narrow-search-results-in-spotlight-mchl4d69efd3/26/mac/26.1>), prefix your search with kind:_filetype_ , like kind:csv or kind:presentation.

### Trigger Actions (with Quick Keys)

Perhaps the most significant new feature of Spotlight is the ability to trigger actions across a wide variety of apps using the keyboard. For example, you can invoke Spotlight and type an action name, like start timer and press Return to initiate a timer in the Clock app. Spotlight then prompts you for the number of minutes.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/45c6119b-4d18-461d-8ca0-3aa2a535ac15/Spotlight-timer.png)

For actions you perform regularly, you can speed things up by defining Quick Keys, which are character sequence shortcuts that stand in for the full action name. For example, you could set it up so that typing st in Spotlight expands to start timer.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/1b789180-17e2-4dc7-b61a-05ff7494d3c6/Spotlight-assign-Quick-Keys.png)

Many Apple apps expose their features as Spotlight actions, and an ever-increasing number of third-party apps do as well. The only way to see which actions are available is to open Spotlight, press Command-3, and scroll through the list.

It’s worth calling out the fact that Apple’s Shortcuts app makes all its shortcuts available as Spotlight actions, so you can now use Spotlight to trigger additional automations.

### Clipboard History

The other huge addition to Spotlight is clipboard history, which until now has required using a third-party utility. Clipboard history lets you access everything you have copied to the clipboard over a period of time, making it easy to paste text and graphics more than once. You turn on clipboard history and set Spotlight to remember clipboard items from the last 30 minutes, 8 hours, or 7 days in **System Settings > Spotlight**.

To access your clipboard history, invoke Spotlight, press Command-4, and either double-click an entry in the list or press the Down arrow key to select the desired clipboard item and press Return to paste it into the current text field. You can also type a few characters from the clipboard item to filter the list, but unfortunately, that works only with characters at the beginning of the item, not elsewhere.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/86d864eb-6c86-4cd0-b640-330f9c01c9ae/Spotlight-clipboard-filtered.png)

**Website Searches**

Spotlight Web searches are quicker than switching to your Web browser, navigating to the site, finding the search field, and entering your search. Just open Spotlight, type the website name, press Tab, and then type a search string to search directly on that site. Sites that work well include Wikipedia, YouTube, Amazon, IMDb, and eBay, but it’s worth trying any website you have already searched in Safari.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/a60d5f9b-48a5-4561-bdfb-00009e7b1d74/Spotlight-website-search.png)

Spotlight learns its site‑specific searches from Safari; if you primarily use another browser, perform a few searches in Safari first to seed Spotlight’s knowledge.

### Spotlight History

Finally, if you use the same Spotlight commands repeatedly, you might be able to avoid some unnecessary typing by invoking Spotlight and then pressing the Up arrow repeatedly to cycle back through your previous Spotlight commands. Once the one you want appears, press Return to insert it just as though you had typed it. Having access to your Spotlight history isn’t a game-changer, but it’s worth remembering for occasional use.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/37816520-b262-4e12-9766-e2502859d190/Spotlight-history.png)

### Going Beyond Spotlight

Spotlight in Tahoe takes a big step toward launchers like[ LaunchBar](<https://www.obdev.at/products/launchbar/index.html>),[ Alfred](<https://www.alfredapp.com/>), and[ Raycast](<https://www.raycast.com/>), but those tools still lead in customization and extensibility. For many users, Spotlight now covers the basics—launching apps, opening files, triggering actions, and recalling clipboard items. If you need more—file operations beyond opening, deep in‑app data access, universal Web search, window management, or bespoke extensions—LaunchBar, Alfred, and Raycast remain the better choice.
