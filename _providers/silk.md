---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.silk.security/'', ''status'': 301, ''note'': ''declared website redirects to https://www.armis.com/ — a different registrable domain (silk.security -> armis.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/silk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.silk.security/
created: '2026-07-17'
description: Silk (Silk Security) was a cybersecurity company backed by Insight Partners that built an exposure, vulnerability and security-finding correlation / risk-prioritization platform. As of this enrichment pass its primary domain silk.security issues a verified 301 redirect to armis.com, indicating the company and product have been absorbed into Armis; no standalone Silk developer or API surface (developer portal, OpenAPI, SDKs, docs, or status page) is currently published, so there is no independent API to enrich beyond a domain-security probe of the still-live silk.security host.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/silk.png
layout: provider
modified: '2026-07-21'
name: Silk
nav: Providers
network: true
overview: Silk is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Security, Vulnerability Management, and Exposure Management.
random_paper: 15
screenshot: https://raw.githubusercontent.com/api-evangelist/silk/refs/heads/main/screenshots/silk-2026-09-02T155458.png
security:
- kind: domain-security
  name: Silk Domain Security
  slug: silk-domain-security
  summary_line: TLSv1.3 · DMARC
slug: silk
tags:
- Company
- Cybersecurity
- Security
- Vulnerability Management
- Exposure Management
- Risk
website: https://www.silk.security/
---
