---
title: "How to Develop Safely with AI"
date: 2026-08-21
slug: "develop-safely-with-ai"
original_url: "https://www.atlascarolina.com/blog/develop-safely-with-ai"
author: "Chad Keith"
source: atlascarolina
---

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/4502a3e2-f684-416f-be5b-f5880643e8c4/AI-development-photo.jpg)

Generative AI is transforming software development. Large language models are good at human languages, but they’re even better at programming languages, which have much smaller vocabularies and fewer ways to combine words. Most importantly, code does something, so running it confirms whether it performs as intended.

The result has been a democratization of development, much as happened with desktop publishing. The Macintosh and PageMaker made it possible for almost anyone to produce a newsletter or brochure, but they did not turn every user into a professional designer, illustrator, or prepress specialist. AI can now produce working software for people who could never have written it themselves, but generating code is only part of building a reliable, trustworthy system.

Today, if you have a repetitive task that’s annoying to do but doesn’t warrant hiring a developer, you can use ChatGPT, Claude, or Gemini to help you create an AppleScript, shell script, Mac or iPhone app, or even a full-fledged Web app. However, if you’re going to dip your toe into AI-assisted development, you need to be careful. Professional developers know to watch out for numerous pitfalls, but if you’re using an AI, it’s up to you to make sure the AI takes them into account. Also, be aware that you’re still ultimately responsible for what you create with AI.

### What Could Go Wrong?

In AI-powered development, there are two broad failure categories: problems with the development agent itself and problems with the finished product.

The AI world has moved past basic chatbots to agents that can look up information, change files, write and execute code, drive apps, and more. That makes them much more capable, but it also creates a situation where they could change or delete data, expose confidential data, or install software that itself creates a vulnerability.

On the other side of the equation is the finished product. If it’s local code, it could run but produce incorrect results, fill up a drive with data, overwrite important data, or cause crashes. A networked app could also generate excessive traffic, leak or expose confidential data, or serve as an entry point into your network.

### Take AI Development in Steps

Professional developers aren’t born that way. They start with simple tasks and tackle more involved projects as they gain experience. With AI handling the programming for you, it can be tempting to take on a major app, but it’s safer to start with simple data analysis and local automation tools before moving on to full-fledged apps and networked systems. The process won’t turn you into a professional developer, but you’ll have a greater appreciation for all the things they have to consider.

#### _Read-only Experiments_

The best way to get started with AI development is with data analysis that would otherwise require you to build spreadsheet formulas, parse large CSV files, compare exported files, and the like. This may not seem like development, but when you drag the files into a chatbot conversation and ask it to work on them, you’ll notice that it does so by writing and executing one or more scripts, often in Python.

With this sort of AI work, you’re limited only by your data and your imagination. You could analyze an event registration or inventory spreadsheet to find trends, get a human-readable summary of errors in a massive log file, or compare data between two differently formatted CSV files to see which people appear in both.

The reason to start here is that you can easily detect errors, and nothing you do can change the data. Incorrect results may still look convincing, however, so compare them against known examples, verify totals, and spot-check the underlying records.

#### _Local Automation Scripts_

The next type of AI development to try is local automation via AppleScript or shell scripts. (If you’re uncertain how to execute a script, remember that you can always ask the AI for detailed instructions.) You could build customized scripts for batch-renaming files, creating future calendar events, manipulating images, and even reformatting HTML files.

However, because scripts can modify and delete data, you need to be more careful here. When possible, have the script create new output rather than modifying the original. Otherwise, work on a copy and ask the AI to:

● Warn you about risks or ambiguities in your request

● Preview exactly what it plans to change

● Act only after you confirm the preview

● Log what it changed

● Record enough information to reverse its actions

####  _Standalone Mac or iOS App_

Apple’s App Store contains a vast number of apps, but it’s time-consuming to search for apps that promise to do what you want and test them to see if they actually do. All too often, they don’t.

With AI and Apple’s[ Xcode](<https://developer.apple.com/xcode>) development environment, you can now create native apps for all your Apple devices. Needless to say, even setting up Xcode is complicated, but once again, an AI agent can do much of it for you and walk you through the rest of the steps. The hard part is often figuring out where some interface control is located, so don’t be shy about pasting a screenshot into the chat and saying, “I don’t see that control—where is it?”

The sky is the limit when it comes to developing your own apps for personal or internal use. You could create an injury rehab tracker, a publishing production checker, a custom document converter, a specialized camera app that adds metadata to photos, and more. Any workflow that’s awkward or doesn’t meet your needs is a candidate. Mac apps can be shared by copying; iPhone and iPad apps must go through Apple’s[ TestFlight](<https://developer.apple.com/testflight/>). Again, ask for help.

When it comes to safety, as long as the apps are for personal or internal use, you mostly need to focus on app reliability and data integrity. Make sure to emphasize that the AI should build and run automated tests on every change, and when you’re testing, comment on _anything_ that seems wrong—don’t settle. Specify that data integrity is paramount, require automatic backups, and allow for manual exports.

The bar gets much higher if you plan to distribute the app more widely. You’ll need to consider your obligations regarding support, compatibility, privacy, distribution, and long-term maintenance. An AI can help with some of those issues—be sure to ask it if there are any ways that user privacy could be abused, for instance—but the buck stops with you.

If you’re contemplating selling your app, you’ll also need to confirm that the licenses for any external code, images, fonts, and other components permit commercial distribution. Be extremely cautious if you plan to build a business around an app!

#### _Networked Systems_

With great power comes great responsibility. You must be much more careful with networked systems, especially if they’ll be accessible over the Internet. But it can be compelling to build such systems—you could make an equipment checkout system, an event registration system that goes beyond Google Forms, a shared inventory system, a document submission service, or a dashboard that aggregates live data from multiple services.

The problem is that the list of considerations goes well beyond app reliability and data integrity, including these questions:

● **What data and operations must be protected?** Some data may be confidential, and personally identifiable information is especially important to protect. Authentication credentials, API keys, and other secrets should never be embedded in source code, prompts, logs, or shared configuration files. Instead, store them in a system designed to manage secrets and limit who and what can access them.

● **Who may perform each action, and how is that enforced?** Define user roles and limit each role’s permissions to only what is necessary. You don’t want a novice support representative accidentally deleting the database.

● **How do you contain hostile inputs and abusive use?** Attackers will probe what happens when they submit malicious URLs, API requests, filenames, uploaded files, Web hooks, and other unexpected input. To reduce your exposure, validate all input, limit its size and complexity, and restrict how frequently users can trigger operations.

● **How do you separate development, testing, and production?** Once you go live, it’s essential to separate these different environments so mistakes made during development don’t take down the live system and data generated during testing doesn’t contaminate the production database. Make sure to separate data and credentials as well.

● **How will the system handle simultaneous requests, retries, and partial failures?** Network requests can arrive twice, overlap, or fail midway through multi-step operations. Work with the AI to prevent these sorts of issues, which can result in duplicate payments, registrations, messages, or inconsistent records.

● **How will you detect and contain attacks, outages, and unexpected behavior?** Decide what to log, what conditions should trigger alerts, how access can be revoked, and if it’s possible to isolate a compromised component without shutting down the entire system.

Finally, assign an owner before putting any significant networked system into use. That person must be responsible for investigating failures, restoring data, updating dependencies, renewing credentials and certificates, responding to vulnerabilities, and eventually retiring the system. An internal application that nobody maintains may become less reliable and less secure with every operating-system update, expired credential, and newly discovered vulnerability.
