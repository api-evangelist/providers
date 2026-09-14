---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - '{''url'': ''https://leap.us'', ''status'': 301, ''note'': ''declared website redirects to https://www.leaplegalsoftware.com/us/ — a different registrable domain (leap.us -> leaplegalsoftware.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 5
apis:
- description: Modeled matter and contact/client management surface that third-party Marketplace apps integrate against - matters (number, title, practice area, status, responsible attorney), contacts/clients (indiv
  name: LEAP Matters & Contacts API
  slug: leap-matters-contacts-api
- description: Modeled time recording, invoicing, and billing surface, evidenced by LEAP's own marketed "automatic timekeeping" and "multiple billing and payment options" features and by production Marketplace integ
  name: LEAP Time & Billing API
  slug: leap-time-billing-api
- description: Modeled trust ledger surface (receipts, disbursements, transfers, balances) reflecting LEAP's marketed legal/trust accounting functionality, a core, heavily regulated feature of the practice managemen
  name: LEAP Trust Accounting API
  slug: leap-trust-accounting-api
- description: Modeled document metadata and automation surface - LEAP's core "automated legal documents" and court-form assembly capability, tightly coupled to Microsoft 365. Marketplace developers demonstrate docu
  name: LEAP Documents API
  slug: leap-documents-api
- description: Modeled calendar/diary and appointment-scheduling surface, evidenced by production Marketplace scheduling integrations (e.g. LawTap) and Microsoft 365 calendar integration. No public endpoint list, ba
  name: LEAP Calendar API
  slug: leap-calendar-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leap-legal-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/leap-legal-software-usa
- group: company
  title: ''
  type: Website
  url: https://leap.us
- group: docs
  title: ''
  type: Documentation
  url: https://developer.leap.build/
- group: commercial
  title: ''
  type: Plans
  url: plans/leap-legal-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://leaplegalsoftware.com/us/blog/
created: '2026-07-04'
description: LEAP is cloud-based legal practice management software for law firms, covering matter and contact management, document automation and court forms, time recording, billing, and trust accounting, tightly integrated with Microsoft 365. LEAP operates a LEAP Developer Console and LEAP Marketplace (developer.leap.build / console.leap.build) through which approved third-party developers build REST-based integrations (an "API Reference" is versioned there, e.g. v1.0.4, v1.0.5), but the technical reference - endpoint paths, base URL, and authentication schema - sits behind developer registration and an app review process rather than a public, self-serve API reference. There is no publicly published OpenAPI document, public base URL, or anonymous API key signup. Existing Marketplace integrations (Xero, Zoom, InfoTrack, LawTap, and others) confirm the API surface is real and in production use, but its concrete shape is not publicly disclosed.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/leap-legal.png
layout: provider
modified: '2026-07-04'
name: LEAP
nav: Providers
network: true
overview: 'LEAP publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Legal, Legal Tech, Practice Management, Legal Accounting, and Trust Accounting.


  LEAP''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Leap Legal Plans Pricing
  plan_count: 2
  slug: leap-legal-plans-pricing
random_paper: 14
screenshot: https://raw.githubusercontent.com/api-evangelist/leap-legal/refs/heads/main/screenshots/leap-legal-2026-07-25T224746.png
security:
- kind: domain-security
  name: Leap Legal Domain Security
  slug: leap-legal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: leap-legal
tags:
- Legal
- Legal Tech
- Practice Management
- Legal Accounting
- Trust Accounting
- Document Automation
website: https://leap.us
---
