---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://hellorelish.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.DropCatch.com/domain/hellorelish.com — a different registrable domain (hellorelish.com -> dropcatch.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/relish-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hellorelish.com
created: '2026-07-17'
description: Relish is a consumer product operated at hellorelish.com and backed by Bullpen Capital, added to the API Evangelist network as a venture-portfolio lead. Live enrichment probing found the marketing site sitting behind a bot/captcha challenge and marked noindex, with no developer, API, or documentation subdomains resolving, no first-party GitHub organization, no published SDK packages, and no machine-readable well-known files. No public API surface was discovered during enrichment; the only verified technical artifact is a domain-security posture probe (TLS 1.3, SPF and DMARC present, no HSTS/DNSSEC/CAA records).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/relish.png
layout: provider
modified: '2026-07-21'
name: Relish
nav: Providers
network: true
overview: Relish is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Venture Backed, Bullpen Capital, and No Public API.
random_paper: 17
screenshot: https://raw.githubusercontent.com/api-evangelist/relish/refs/heads/main/screenshots/relish-2026-09-02T153328.png
security:
- kind: domain-security
  name: Relish Domain Security
  slug: relish-domain-security
  summary_line: TLSv1.3 · DMARC
slug: relish
tags:
- Company
- Consumer
- Venture Backed
- Bullpen Capital
- No Public API
website: https://hellorelish.com
---
