---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://upteamco.com'', ''status'': 302, ''note'': ''declared website redirects to https://www.luxclusif.com/ — a different registrable domain (upteamco.com -> luxclusif.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upteam-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://upteamco.com
created: '2026-07-17'
description: 'Upteam is a 500 Global portfolio company whose public web presence now points at Luxclusif: upteamco.com returns an HTTP 302 redirect to luxclusif.com, the B2B luxury resale platform offering wholesale distribution of pre-owned luxury goods, stock acquisition, and resale-as-a-service programs. Enrichment probing found no developer portal, no API documentation, and no machine-readable API artifacts on either the Upteam domain or the Luxclusif site; /.well-known/ discovery paths on upteamco.com return 403 and site paths redirect to Luxclusif.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/upteam.png
layout: provider
modified: '2026-07-21'
name: Upteam
nav: Providers
network: true
overview: Upteam is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Luxury Resale, B2B, Pre-owned Goods, and Portfolio Company.
random_paper: 1
screenshot: https://raw.githubusercontent.com/api-evangelist/upteam/refs/heads/main/screenshots/upteam-2026-09-02T165129.png
security:
- kind: domain-security
  name: Upteam Domain Security
  slug: upteam-domain-security
  summary_line: TLSv1.3 · DMARC
slug: upteam
tags:
- Company
- Luxury Resale
- B2B
- Pre-owned Goods
- Portfolio Company
website: https://upteamco.com
---
