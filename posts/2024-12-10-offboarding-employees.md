---
title: "The Importance of Properly Offboarding Employees"
date: 2024-12-10
slug: "offboarding-employees"
original_url: "https://www.atlascarolina.com/blog/offboarding-employees"
author: "Chad Keith"
source: atlascarolina
---

![](https://images.squarespace-cdn.com/content/v1/5d67c9fb19efcd000177ca21/465513d9-554b-4b21-aa03-c0b5d26862c5/employee-leaving-photo.jpg)

Employers and their employees part ways for all sorts of reasons. People may move on because of a contract’s completion, to take a new job, or because they’re retiring. Employees may also leave due to being laid off or fired. Whatever the reason, _offboarding_ —the process of managing an employee’s departure from an organization—is essential.

Without a systematic offboarding protocol, organizations face significant risks related to data security, device mismanagement, operational disruptions, and compliance violations. In a particularly troubling example, a fired employee allegedly [_hacked Disney World’s menu creation system_](<https://www.404media.co/fired-employee-allegedly-hacked-disney-worlds-menu-system-to-alter-peanut-allergy-information/>), changing prices, adding profanity, and—most problematically—adjusting allergen information in ways that could have caused someone allergic to peanuts to order food that contained them.

Obviously, offboarding has various administrative aspects. We’ll focus on those associated with technical infrastructure, but it’s also important to consider how you’ll communicate internally about the departure and any human resources and legal matters.

Our overarching advice regarding offboarding is to establish a formal protocol so everyone knows what’s involved. That’s particularly important for departures that happen with little notice. When building your offboarding plan, consider these three parts of the process: revoking access, retrieving devices, and preserving the organization’s data.​

### Revoke Digital Access

When offboarding an employee, the most important thing to consider is how you’ll revoke their digital access to organizational resources such as email, a shared password manager, and core service accounts. For those who are retiring or staying to train their replacement, access revocation can proceed gradually on a schedule. This approach provides sufficient time to transition ongoing projects and communications.

However, in most cases, it’s safest to revoke access immediately, especially when an employee has been terminated involuntarily due to layoffs, performance problems, or misconduct, or when dealing with employees in high-security roles, such as IT administrators, members of the legal team, or high-ranking executives. Even if their departure isn’t contentious, the risk of data leakage is too high.

Revoking access is significantly easier if you’re using Apple Business (formerly Apple Business Manager) and an MDM platform. Because Apple Business lets you use federated Apple Accounts, it’s simple to revoke access to iCloud and other Apple services. Plus, because Apple Business makes it possible to separate personal Apple Accounts and their associated data, employees can move their personal data off an organization’s device more easily.

MDM—mobile device management—is even more important because it enables administrators to revoke access to organization-managed email accounts, VPNs, Wi-Fi networks, and cloud services. If a device isn’t returned, an MDM platform can remotely lock, wipe, or reset it. For BYOD scenarios (Bring Your Own Device, where employees use their own devices rather than organization-owned ones), a properly configured MDM allows the removal of organizational data and profiles without affecting personal data.

Using an identity provider like Google Workspace, Microsoft Entra ID, or Okta with a single sign-on system makes revoking access even more straightforward. These services tie access to an organization’s apps, resources, and devices to a single login, so deactivating a departing employee’s account in the identity provider instantly cuts off access to all connected systems. Otherwise, you’ll find yourself doing the dance of deactivating Google, then Adobe, then Slack, and so on. It’s tedious and potentially error-prone.

Finally, the combination of an MDM system with single sign-on can also help monitor employee behavior during the offboarding period for unusual activities. You’ll want to know if a terminated employee logs in to a confidential database that they have no reason to access immediately after receiving notice. ​

### Retrieve Organization Devices

Another key aspect of your offboarding plan should revolve around retrieving organization-owned devices. Even if you can use MDM to revoke access, you need to get your devices back so they can be given to other employees or held in reserve as backups. Apple Business helps here, too, since it tracks all registered devices owned by the organization and can reassign devices to new users.

The real win of Apple Business in this regard is that it lets you [_turn off Activation Lock on all supervised devices_](<https://support.apple.com/guide/apple-business-manager/turn-off-activation-lock-axm812df1dd8/web>), whether it was turned on using a federated Apple or personal Apple Account. Without Apple Business, you may have to work with the employee to regain access to the device. If that’s not possible, Apple support may be able to help unlock the device if you can provide proof of purchase and ownership.

To ensure you don’t end up in such an awkward situation, follow these best practices when using Apple Business:

Make sure to purchase Apple devices through Apple Business-compatible channels.

Use Automated Device Enrollment to ensure that devices are supervised and managed by MDM out of the box.

Rely on federated Apple IDs to ensure the organization retains control over organizational content within Managed Apple Accounts.​

### Preserve Organization Data and Communications

Finally, think about what the departing employee was doing. You’ll want to transfer or archive everything they worked on, including their organizational email account. In most cases, someone else will have to take over their responsibilities and may need access to emails, files, contacts, and more.

An identity provider can help by transferring ownership of cloud-based files and other data stored in Google Workspace or Microsoft 365. Without one, you’ll have to review all their online files and reassign ownership manually.

Email requires additional thought. You’ll probably want to forward the departing employee’s email to whoever is taking over. If that’s not feasible, set up an auto-reply explaining that the employee is no longer available and providing alternative contacts. In that case, it’s also worth scanning the incoming email periodically to ensure essential communications aren’t being missed.​

### Next Steps

If you don’t have a formal offboarding policy, we recommend developing one soon to ensure that you aren’t at risk for data security, device mismanagement, or operational disruptions. It’s one of those tasks that are easy to put off until it’s too late, at which point you have to scramble. You can find offboarding policy templates and other resources online, and we’re happy to discuss the tech-specific aspects when you’re ready.

Of course, if you’re not already using Apple Business and an MDM solution, getting started with them is even more important to implement right away. Contact us to discuss what’s involved.

(Featured image by iStock.com/yacobchuk)
