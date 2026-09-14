---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://hotmail.com'', ''status'': 301, ''note'': ''declared website redirects to https://outlook.live.com/mail/ — a different registrable domain (hotmail.com -> live.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hotmail-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hotmail.com
- group: other
  title: ''
  type: Successor
  url: https://outlook.com
created: '2026-07-17'
description: Hotmail was one of the first free web-based email services, launched in 1996 by Sabeer Bhatia and Jack Smith and among the earliest venture-backed consumer web companies (funded by Draper Fisher Jurvetson and Menlo Ventures). Microsoft acquired Hotmail in December 1997 and operated it as MSN Hotmail and later Windows Live Hotmail. In 2013 Microsoft folded Hotmail into Outlook.com; hotmail.com mailboxes remain fully active but are served by Outlook.com and Microsoft 365 infrastructure. Hotmail exists today only as a legacy consumer email brand and domain, with no standalone developer program. Programmatic access to hotmail.com mailboxes is provided through Microsoft Graph (Outlook Mail) and the standard IMAP, POP, and SMTP protocols, not a dedicated Hotmail API.
image: https://raw.githubusercontent.com/api-evangelist/hotmail/refs/heads/main/hotmail.png
layout: provider
modified: '2026-07-19'
name: Hotmail
nav: Providers
network: true
overview: Hotmail is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Email, Webmail, Consumer, and Communications.
random_paper: 15
screenshot: https://raw.githubusercontent.com/api-evangelist/hotmail/refs/heads/main/screenshots/hotmail-2026-07-25T221509.png
security:
- kind: domain-security
  name: Hotmail Domain Security
  slug: hotmail-domain-security
  summary_line: TLSv1.3 · DMARC
slug: hotmail
tags:
- Company
- Email
- Webmail
- Consumer
- Communications
- Microsoft
- Legacy
- Messaging
website: https://hotmail.com
---
