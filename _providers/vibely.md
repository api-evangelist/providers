---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://vibely.io'', ''status'': 301, ''note'': ''declared website redirects to https://www.kajabi.com/product/communities — a different registrable domain (vibely.io -> kajabi.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vibely-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vibely.io
created: '2026-07-17'
description: Vibely was a creator-community platform (surfaced as a 500 Global portfolio company) that let creators host paid communities, challenges, and group chat. As of this enrichment pass the domain vibely.io no longer serves an independent product; every path — including all /.well-known/ discovery endpoints — 301-redirects to kajabi.com/features/communities, indicating Vibely was folded into Kajabi's Communities product. No standalone Vibely developer portal, API, OpenAPI, SDK, MCP server, or llms.txt could be found; the only artifact captured is a probed TLS/DNS domain-security profile of the surviving redirect domain. This profile is retained as a defunct/acquired portfolio lead.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vibely.png
layout: provider
modified: '2026-07-21'
name: Vibely
nav: Providers
network: true
overview: Vibely is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Creator Economy, Community Platform, Membership, and Acquired.
random_paper: 0
screenshot: https://raw.githubusercontent.com/api-evangelist/vibely/refs/heads/main/screenshots/vibely-2026-09-02T165843.png
security:
- kind: domain-security
  name: Vibely Domain Security
  slug: vibely-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vibely
tags:
- Company
- Creator Economy
- Community Platform
- Membership
- Acquired
- Kajabi
website: https://vibely.io
---
