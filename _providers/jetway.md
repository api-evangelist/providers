---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://nextravel.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.perk.com/ — a different registrable domain (nextravel.com -> perk.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/travelperk/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jetway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nextravel.com
created: '2026-07-17'
description: Jetway was surfaced as a 500 Global portfolio lead pointing at nextravel.com. Enrichment found that nextravel.com now 301-redirects to TravelPerk (www.travelperk.com), which itself redirects to www.perk.com, an all-in-one business travel and expense-management platform. NexTravel was a US corporate-travel startup acquired by TravelPerk; it no longer operates as an independent brand and publishes no public developer API, API documentation, developer portal, or /.well-known discovery documents at nextravel.com (every probed path soft-404s to the Perk marketing site). This profile is retained as an acquired/redirected lead with no independent developer surface to enrich.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jetway.png
layout: provider
modified: '2026-07-19'
name: Jetway
nav: Providers
network: true
overview: Jetway is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Corporate Travel, Business Travel, and Expense Management.
random_paper: 9
screenshot: https://raw.githubusercontent.com/api-evangelist/jetway/refs/heads/main/screenshots/jetway-2026-07-25T223138.png
security:
- kind: domain-security
  name: Jetway Domain Security
  slug: jetway-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jetway
tags:
- Company
- Travel
- Corporate Travel
- Business Travel
- Expense Management
- Acquired
website: https://nextravel.com
---
