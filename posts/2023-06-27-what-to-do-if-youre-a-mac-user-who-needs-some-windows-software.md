---
title: "What to Do If You’re a Mac User Who Needs Some Windows Software"
date: 2023-06-27
slug: "what-to-do-if-youre-a-mac-user-who-needs-some-windows-software"
original_url: "https://www.atlascarolina.com/blog/zf6xj022pwtnyxuowwp6qmlyqkvkvs"
author: "Chad Keith"
source: atlascarolina
---

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/15ef7857-a6dd-45f3-8c17-ef8990c1f381/iMac-running-windows-photo.png)

For the most part, the days of [Mac versus PC](<https://www.youtube.com/watch?v=0eEG5LVXdKo>) are over. Common apps now exist on both platforms, and when they don’t, there are plenty of alternatives in nearly every app category. Plus, many apps either run entirely on the Web in any browser. Large organizations now regularly run “employee choice” programs that allow people to pick the platform where they’re the most comfortable.

But the fact remains that there are many more Windows-based PCs out there than Macs, and particularly for an old or unusual app, or for software needed for specific hardware peripherals, sometimes the only available option is a Windows app. What’s a modern Mac user to do? Here are a few possibilities.​

### Use Boot Camp on an Intel-based Mac

The cheapest approach to running Windows software on a Mac is to use Apple’s free [Boot Camp](<https://support.apple.com/guide/bootcamp-assistant/get-started-with-boot-camp-assistant-bcmp712cfeb8/6.1/mac/13.0>). However, it comes with a number of limitations compared with the virtualization software we’ll discuss next:

Boot Camp works only on Intel-based Macs; it’s not available for M-series Macs.

You must choose between macOS and Windows every time you turn on or restart your Mac, rather than being able to run both side-by-side.

Boot Camp creates its own partition on your drive, and you can’t resize it later. You must guess how much space you need and leave enough for future expansion, all without wasting too much available space.

[Installing Windows 11 is involved](<https://machow2.com/windows-11-mac-boot-camp/>) and can’t be accomplished on a Mac with a Touch Bar. You can install Windows 10 and then update it to Windows 11.

The main advantage of Boot Camp over virtualization software is that it provides the best performance for Windows apps because no resources are being shared with macOS. Also, a few apps, primarily games, won’t run on a virtual machine.

Given that Intel-based Macs are on the way out, we recommend the Boot Camp approach mostly if you have an extra Intel-based Mac that can be dedicated to your Windows task.​

### Use Virtualization Software on an Intel-based Mac

Shortly after Apple switched Macs from PowerPC processors to Intel chips in 2006, virtualization apps appeared, notably [Parallels Desktop](<https://www.parallels.com/en/products/desktop/>), [VMware Fusion](<https://www.vmware.com/products/fusion.html>), and [VirtualBox](<https://www.virtualbox.org/>). Because Windows runs natively on those same Intel chips, virtualization software can create a virtual machine (VM) that Windows runs on just as though it were running on a physical PC. A few of the significant advantages of virtualization software include:

You can run Windows apps alongside Mac apps, switching back and forth with a click.

You can install Windows on a disk image that you can resize as necessary.

You can move data from macOS to Windows with copy-and-paste and by dragging files, plus you can specify a shared folder whose contents are accessible to both macOS and Windows.

You can install different versions of Windows or other Intel-compatible operating systems, and maintain multiple virtual machines for testing.

The main downside of virtualization software is that its performance can’t be quite as good as Boot Camp because it must share some CPU and RAM resources with macOS. Plus, Parallels Desktop and VMware Fusion aren’t free, although VMware Fusion offers a free personal license. VirtualBox is free but more complicated, and it’s not yet compatible with macOS 13 Ventura.

Parallels Desktop ([starting at $99.99](<https://www.parallels.com/products/desktop/buy/>)) and VMware Fusion ([starting at $149](<https://store-us.vmware.com/vmware-fusion-13-player-5708568200.html?country_code=US>); [free for personal use](<https://customerconnect.vmware.com/evalcenter?p=fusion-player-personal>)) provide the best user experience for most Windows needs if you have an Intel-based Mac.​

### Use Parallels Desktop on an M-series Mac

When Apple introduced the first Macs based on Apple silicon, people wondered what would happen to virtualization software, which could no longer just pass the software commands down to an Intel chip. The solution was to create a new virtualization engine that leverages the M-series chips’ hardware-assisted virtualization to run Arm-based virtual machines. (Apple’s M-series chips are based on the Arm architecture, which differs from the x86 architecture used by Intel chips.)

The upshot is that the latest versions of Parallels Desktop and VMware Fusion can run on M-series Macs, but you can install only Arm-based operating systems, not Intel-based operating systems. Luckily, Microsoft makes [Windows 11 on Arm](<https://support.microsoft.com/en-us/windows/windows-arm-based-pcs-faq-477f51df-2e3b-f68f-31b0-06f5e4f8ebb5>), a full-fledged version of Windows that can run most Windows apps, even those designed for Intel chips.

In early 2023, Microsoft announced that it is [officially supporting Windows 11 on M-series Macs](<https://support.microsoft.com/en-us/windows/options-for-using-windows-11-with-mac-computers-with-apple-m1-and-m2-chips-cd15fd62-9b34-4b78-b0bc-121baa3c568c>) when run in Parallels Desktop. Although VMware Fusion can run Windows 11 on Arm Insider Preview—a beta version—[installation is challenging](<https://cellular.fm/2022/08/03/install-windows-11-arm-vmware-fusion-apple-silicon-m1-m2-mac-macbook-air-pro-imac-macstudio-video/>). We recommend [sticking with Parallels Desktop for an experience that’s significantly easier](<https://kb.parallels.com/125343>) and officially supported.​

### Use a Windows 365 Cloud PC

Virtualization enables you to run Windows not just on a Mac, but also in the cloud. Microsoft’s [Windows 365](<https://www.microsoft.com/en-us/windows-365>) service is another alternative that lets you stream Windows to any device with a Web browser. While the concept of Windows 365 is compelling, the pricing is not. The cheapest plan costs $31 per user per month, or $372 per year, for a virtual PC with 2 CPUs, 4 GB of RAM, and 128 GB of storage. Parallels Desktop is about a quarter the price.​

### Buy a Cheap PC

We know, we know. The entire point of running Windows on a Mac is so you don’t have to buy a PC. But there are situations where it makes more sense to purchase an inexpensive PC than to fuss with virtualizing Windows on a Mac. Perhaps multiple people in your office need access to your essential Windows app, or maybe some hardware device can be controlled only from a PC. In such cases, a dedicated PC may be the better part of valor. Contact us for configuration and buying advice—the PC world can be a confusing place for those accustomed to buying from Apple.

(Featured image based on originals by iStock.com/manaemedia)
