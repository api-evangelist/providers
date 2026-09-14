---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://airsidemobile.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.entrust.com/products/airside-app — a different registrable domain (airsidemobile.com -> entrust.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airside-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://airsidemobile.com/
created: '2026-07-17'
description: 'Airside (formerly Airside Mobile) is a digital identity and mobile credential product whose website airsidemobile.com now permanently redirects (HTTP 301) to Entrust''s Airside app page, indicating the product and its assets were acquired by Entrust. As of this enrichment pass no public API, OpenAPI specification, SDK, developer portal, or developer documentation surface could be discovered: developer/api/docs subdomains do not resolve and the root domain and /.well-known/security.txt both redirect off-site to Entrust. The company was originally surfaced as a bain-capital-ventures portfolio lead (sector ai-apps) and remains a stub pending any first-party developer program.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airside.png
layout: provider
modified: '2026-07-17'
name: Airside
nav: Providers
network: true
overview: Airside is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Apps, Digital Identity, Mobile Credentials, and Identity Verification.
random_paper: 2
screenshot: https://raw.githubusercontent.com/api-evangelist/airside/refs/heads/main/screenshots/airside-2026-07-25T195435.png
security:
- kind: domain-security
  name: Airside Domain Security
  slug: airside-domain-security
  summary_line: TLSv1.3 · DMARC
slug: airside
tags:
- Company
- Ai Apps
- Digital Identity
- Mobile Credentials
- Identity Verification
- Acquired
- Entrust
website: https://airsidemobile.com/
---
