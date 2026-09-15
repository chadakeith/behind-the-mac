---
title: "PostScript Type 1 Fonts Losing Support This Year—Here’s What to Do"
date: 2021-03-08
slug: "postscript-type-1-fonts-losing-support-this-year-heres-what-to-do"
original_url: "https://www.atlascarolina.com/blog/it40yl114dpbyrm5wmbikns0jgfbs8"
author: "Chad Keith"
source: atlascarolina
---

![Old-type-photo.jpg](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/1615218078972-4BFXW1OE5KFED14UEO8P/Old-type-photo.jpg)

For you graphic designers out there, Adobe has announced that it will be [ending support for PostScript Type 1 fonts](<https://helpx.adobe.com/fonts/kb/postscript-type-1-fonts-end-of-support.html>) starting with Photoshop in 2021. All Adobe apps will stop allowing users to author content using Type 1 fonts beginning January 2023.

This announcement shouldn’t come as a surprise. Adobe introduced Type 1 fonts at the dawn of the Macintosh age back in 1984, started collaborating with Microsoft on the more versatile OpenType fonts in 1996, and stopped developing Type 1 fonts in 1999. Although some operating systems still support Type 1 fonts, Web browsers and mobile operating systems don’t. Worse, Type 1 fonts don’t support Unicode, limiting their ability to support extended language character sets.

However, Mac users whose careers stretch back to the 1990s and earlier likely still have Type 1 fonts kicking around—who would toss a Type 1 font that worked perfectly well? Now’s the time to think about dealing with those ancient fonts.

First, however, it’s worth a quick trip to Font Book (or whatever font utility you use) to determine which of your fonts are Type 1 fonts. You can do this easily in Font Book by creating a smart collection that selects fonts by kind:

  1. Launch Font Book from your Applications folder.

  1. Choose File > New Smart Collection to open the Smart Collection dialog.

  2. Give the collection a name, like “PostScript Type 1.”

  3. Choose All from the first pop-up menu.

  4. From the criteria pop-up menu, choose Kind and complete the search by choosing “is” from the second menu and PostScript from the third menu.

  5. Click OK to save your smart collection.

![Font-Book-smart-collection.png](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/1615217778256-P69KS9VVMZ1BO0NC9HYQ/Font-Book-smart-collection.png)

Once you have a sense of which of your fonts will be impacted by this change, you have three options. You can just delete them and move on, replace them with modern OpenType fonts, or convert them to OpenType.​

### **Delete Type 1 Fonts**

Although it would seem like Font Book should let you delete fonts directly, when you Control-click a font, the Remove command may be dimmed out. If that’s the case, choose Show in Finder instead.

![Font-Book-Show-in-Finder.png](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/1615217832217-T1L0N5LS65UXZ95UA929/Font-Book-Show-in-Finder.png)

That opens a new Finder window with the font files selected. In all likelihood, there will be other font support files in there as well, so make sure you don’t need to keep anything before tossing it all in the trash.

If you’re more cautious, don’t trash those files immediately. Instead, temporarily sequester them in a special folder. This is just in case any old documents or older software on your Mac is using those font files. As you go about your weekly and monthly tasks, if you encounter a problem with a missing font, you may wish to reinstall that font until you can find a different solution.

![Font-in-Finder.png](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/1615217891596-8O2BYVMPURT178ZM70S8/Font-in-Finder.png)

### **Replace Type 1 Fonts**

For a Type 1 font published by Adobe Type, the company says you can [contact its partner Fontspring](<https://www.fontspring.com/contact>) to receive a discount when upgrading the font to an OpenType version. For other Type 1 fonts, including those sold by Adobe, Adobe recommends contacting the font foundry to see if there’s a discounted upgrade path.

That may be easier said than done, given how old many of these are likely to be. However, you can start by looking at the font metadata to see who created the font or holds its trademark. Select a font in Font Book and click the i button in the toolbar. The Trademark metadata is a good place to look, and some fonts may have Manufacturer, Designer, or Copyright metadata that might provide contact information.

![Font-Book-trademark.png](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/1615217949368-RYQ4PKX8POV1CMROOUTN/Font-Book-trademark.png)

### **Convert Type 1 Fonts to OpenType**

Finally, what should you do if you rely on specific Type 1 fonts and no OpenType versions are available? It might be possible to convert your fonts from Type 1 to OpenType. Although we haven’t tried it, [Mike Rankin at CreativePro](<https://creativepro.com/how-to-convert-postscript-fonts-to-opentype-with-transtype/>) recommends [TransType](<https://www.fontlab.com/font-converter/transtype/>), which costs $97. It’s not cheap, but it may be your only alternative.

It’s impressive that PostScript Type 1 fonts have retained support for nearly 40 years—those who bought in early got an amazing run for their money. But it’s not unreasonable for Adobe and other tech companies to move on to OpenType, which is still going strong after 25 years, with its most recent update so far in November 2020.
