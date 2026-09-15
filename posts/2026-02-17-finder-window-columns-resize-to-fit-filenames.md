---
title: "Make Finder Window Columns Resize to Fit Filenames"
date: 2026-02-17
slug: "finder-window-columns-resize-to-fit-filenames"
original_url: "https://www.atlascarolina.com/blog/finder-window-columns-resize-to-fit-filenames"
author: "Chad Keith"
source: atlascarolina
---

Column view in the Finder has an annoying tendency to either show overly wide columns that waste space or truncate long filenames, forcing you to drag a column divider to see more of the name. In macOS 26.1 Tahoe, Apple added an option to the Finder’s View Options window that automatically adjusts column widths to display the longest visible filename in each column. To activate it, choose **View > Show View Options** with a column-view window frontmost, then select the “Resize columns to fit filenames” checkbox. If you’re running macOS 13 Ventura through macOS 15 Sequoia, this option is hidden, but you can enable it by pasting this command into Terminal: defaults write com.apple.finder _FXEnableColumnAutoSizing -bool YES; killall Finder. (Change YES to NO to revert the change.) Alternatively, the free[ TinkerTool 10](<https://www.bresink.com/osx/TinkerTool10.html>) utility provides a graphical toggle for these older operating systems—look for “Automatically adapt to file name widths in column mode” in the Finder section.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/824a4530-cb49-4c18-8e8a-819cf0a71eed/regular-and-resized-columns.jpg)
