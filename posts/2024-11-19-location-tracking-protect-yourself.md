---
title: "Perturbed by Location Tracking Revelations? Here’s How to Protect Yourself"
date: 2024-11-19
slug: "location-tracking-protect-yourself"
original_url: "https://www.atlascarolina.com/blog/location-tracking-protect-yourself"
author: "Chad Keith"
source: atlascarolina
---

[Recent](<https://krebsonsecurity.com/2024/10/the-global-surveillance-free-for-all-in-mobile-ad-data/>) [news](<https://www.404media.co/inside-the-u-s-government-bought-tool-that-can-track-phones-at-abortion-clinics/>) [reports](<https://www.notus.org/technology/cell-phone-tracking-law-enforcement-abortion-clinic>) have revealed that a little-known company called Babel Street can track iPhone and Android user locations. Babel Street does this by leveraging data from mobile advertising data brokers. Investigators from data removal firm Atlas Privacy discovered they could use Babel Street’s Locate X tool to identify patients at a Florida abortion clinic, jurors in a New Jersey trial, attendees at a Los Angeles synagogue and a Dearborn mosque, and even children in a Philadelphia school.

Much of this is possible because people use apps that reveal their location to data brokers, who package the information and resell it to companies like Babel Street. Apple does have an advantage here—Atlas estimated they could locate roughly 80% of Android phones but only 25% of iPhones. That’s due to Apple’s App Tracking Transparency feature, introduced in iOS 14.5, which requires apps to get permission from users before tracking them for third-party advertising purposes. Unfortunately, many people unthinkingly grant such permissions, and location and identification data can also leak out in other ways.

Although it’s difficult to avoid being tracked by data brokers entirely, you can drastically reduce the likelihood and frequency of tracking, which helps ensure that any location information that does become available isn’t sufficient to identify you personally. Your employer may also consider your location to be sensitive information and want you to restrict it to the extent possible. To achieve this, you’ll need to adjust settings in several parts of Settings > Privacy & Security on your iPhone (and iPad, if you regularly use it in multiple locations). ​

### Turn Off Allow Apps to Request to Track

You’ll find the most important setting in Settings > Privacy & Security > Tracking. At the top of the screen is a switch labeled [Allow Apps to Request to Track](<https://support.apple.com/en-us/102420>). Make sure that is off! If it has been on in the past, apps that have requested permission will appear below.

By preventing apps from even asking if they can track you, you keep them from sharing a unique identifier associated with your iPhone with other apps and websites. Otherwise, advertisers can follow you from app to app and website to website, gathering information about you—often including your physical location—as you go about your life.

Don’t let apps persuade you to turn this setting on or allow them to track you. Apple’s rules explicitly forbid them from reducing functionality to those who refuse to allow tracking.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/36bb487c-3fff-4cbe-b3e8-f30b3e6f930c/Allow-Apps-to-Ask-to-Track.jpg)

### Allow Location Access Only for Apps That Need It

While you can turn off Allow Apps to Request to Track with a single switch, [preventing apps from seeing your location](<https://support.apple.com/guide/iphone/control-the-location-information-you-share-iph3dd5f9be/18.0/ios/18.0>) requires more targeted work. Although Settings > Privacy & Security > Location Services has a big Location Services switch, turning that off will drastically reduce the utility of your iPhone. You won’t be able to get directions from Maps, tag photos with their location, share your location with family members, and much more.

Instead, for each app in the list, determine what level of location access you want to grant based on its function and description of why it needs access. Grant the minimal level of access necessary, which varies by app. Navigation apps need location access to work at all. Camera apps need it to geotag photos. Weather apps use it to provide custom weather reports and extreme weather notifications. But do you want to give a social media app access to your location at all times?

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/4a2bc2fc-e7eb-42b3-a376-17cfb48ad38f/Location-access-permissions.jpg)

Apple provides five location access levels:

  * **Never:** Choose Never for any app with questionable explanations of why location access is requested.

  * **Ask Next Time or When I Share:** If you’re unsure if you want to allow or deny location access for an app, select this option. The app will prompt you the next time it wants your location, enabling you to make an informed decision based on your actions.

  * **While Using the App:** For most apps you want to allow to see your location, choose While Using the App. It’s entirely reasonable that a location-requiring app be allowed to determine your location while you’re using it.

  * **While Using the App or Widgets:** This option only appears for apps with widgets; choose it only if you use a widget that needs location access.

  * **Always:** Grant Always access only to apps that generate location-related notifications when the app is not open. The most common example is a weather app that provides notifications of incoming storms.

The Precise Location option becomes available if you allow location access for an app. Turn it on only if the app needs to know your location within 15 to 200 feet (5 to 60 meters). An Uber or Lyft driver will need to know where to pick you up, for instance, so those apps should have Precise Location turned on, as should navigation and camera apps. For most others, turn off Precise Location. Your approximate location—a variable radius between 2.5 to 12 miles (4 and 20 kilometers)—is usually sufficient to locate you in the right part of the world.​

### Block Bluetooth and Local Network Access for Apps That Don’t Need It

Apps can use Bluetooth to infer your general location through interactions with other Bluetooth devices and movement patterns, so Apple requires apps to [ask to use Bluetooth](<https://support.apple.com/en-us/102267>). As a result, just as with location, you should go through the apps listed in Settings > Privacy & Security > Bluetooth and revoke permission from any that don’t seem as though they should need it. Most will be legitimate—an app designed to communicate with a Bluetooth-connected device, for instance. Any app that needs access to Bluetooth and doesn’t have it should prompt you when you next open it.

Similarly, Apple now requires apps to request permission to [use your local network](<https://support.apple.com/en-us/102229>). For the most part, these requests are reasonable—apps may need to discover network-connected devices like routers, printers, speakers, smart home gadgets, and more. Or games may need to discover other players on the network. However, because your network can reveal information about your location, it’s best to revoke access for any apps that don’t seem as though they should need it. There’s no harm in doing so; they’ll ask again if they need access.

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/82ee185a-93cc-45b8-88fc-fca57adb4c6e/Bluetooth-Local-Network-permissions.jpg)

Ultimately, all we can do is stay vigilant about what we’re allowing on our devices, encourage Apple to add even more privacy protections, and lobby our elected representatives for legal protection. It’s unconscionable that private companies can gather extensive location data on hundreds of millions of citizens.
