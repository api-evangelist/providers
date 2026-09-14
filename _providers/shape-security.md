---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''http://shapesecurity.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.f5.com/products/distributed-cloud-services/bot-defense — a different registrable domain (shapesecurity.com -> f5.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shape-security-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://shapesecurity.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.f5.com/products/security/shape-security
created: '2026-07-17'
description: Shape Security was an enterprise application-security company (backed by gv and wing-venture-capital) specializing in bot mitigation, credential-stuffing defense, and online-fraud prevention for login, checkout, and account-recovery flows. It was acquired by F5 in 2020 and its technology now ships as F5 Distributed Cloud Bot Defense; the shapesecurity.com domain 301-redirects wholesale into f5.com. Shape Security no longer operates an independent developer portal, public API, OpenAPI spec, or SDK surface of its own — its capabilities are delivered through the F5 Distributed Cloud platform. This profile is retained as an acquisition/lineage record in the API Evangelist network.
image: https://raw.githubusercontent.com/api-evangelist/shape-security/refs/heads/main/apis.yml
layout: provider
modified: '2026-07-21'
name: Shape Security
nav: Providers
network: true
overview: 'Shape Security is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Security, Bot Mitigation, and Fraud Prevention.


  Shape Security''s developer surface includes documentation and 2 more developer resources.'
random_paper: 13
screenshot: https://raw.githubusercontent.com/api-evangelist/shape-security/refs/heads/main/screenshots/shape-security-2026-09-02T155107.png
security:
- kind: domain-security
  name: Shape Security Domain Security
  slug: shape-security-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shape-security
tags:
- Company
- Enterprise
- Security
- Bot Mitigation
- Fraud Prevention
- Application Security
- Acquired
website: http://shapesecurity.com
---
