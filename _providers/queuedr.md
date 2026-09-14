---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://queuedr.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.phreesia.com/see-more-patients/appointments/ — a different registrable domain (queuedr.com -> phreesia.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/phreesia/
- group: company
  title: ''
  type: Website
  url: https://queuedr.com
- group: start
  title: ''
  type: Login
  url: https://app.queuedr.com/users/sign_in
- group: other
  title: ''
  type: Acquirer
  url: https://www.phreesia.com/queuedr/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/queuedr-domain-security.yml
created: '2026-07-17'
description: QueueDr is a healthcare scheduling automation product that automatically fills unexpected appointment cancellations, rebooks no-shows, and balances provider schedules to reduce lost revenue for medical practices and health systems. Originally a 500 Global-backed startup, QueueDr was acquired by Phreesia and is now offered as the Phreesia Appointment Accelerator within Phreesia's patient intake and engagement platform. The queuedr.com domain now redirects to Phreesia; existing customers continue to sign in at the app.queuedr.com dashboard. No independent public developer portal, API documentation, SDKs, or machine-readable API surface is published for QueueDr as a standalone product.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/queuedr.png
layout: provider
modified: '2026-07-20'
name: QueueDr
nav: Providers
network: true
overview: QueueDr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health IT, Appointment Scheduling, and Patient Engagement.
random_paper: 7
screenshot: https://raw.githubusercontent.com/api-evangelist/queuedr/refs/heads/main/screenshots/queuedr-2026-09-02T152648.png
security:
- kind: domain-security
  name: Queuedr Domain Security
  slug: queuedr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: queuedr
tags:
- Company
- Healthcare
- Health IT
- Appointment Scheduling
- Patient Engagement
- Medical Practice
- Acquired
website: https://queuedr.com
---
