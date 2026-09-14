---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://maystreet.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.lseg.com/en/data-analytics/market-data/data-feeds — a different registrable domain (maystreet.com -> lseg.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 2
apis:
- description: Low-latency, near-time market data query API delivered as a streaming WebSockets service so clients can process arbitrarily-sized result sets frame-by-frame without pagination. Publicly documented onl
  name: MayStreet High Performance Query (HPQ) API
  slug: maystreet-high-performance-query-api
- description: Query access to MayStreet's 20+ petabyte Market Data Lake of historical exchange data captured as PCAP and converted to Parquet, exposed as Athena SQL plus a growing set of client functions through th
  name: MayStreet Market Data Lake Query API
  slug: maystreet-data-lake-query-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maystreet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/maystreet-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/maystreet-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/maystreet-problem-types.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/maystreet-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/maystreet-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/maystreet-llms.txt
- group: company
  title: ''
  type: Website
  url: https://maystreet.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/maystreet
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/maystreet
created: '2026-07-21'
description: MayStreet is a low-latency market data infrastructure vendor founded in 2012 and acquired by London Stock Exchange Group (LSEG) in May 2022, with maystreet.com now redirecting into LSEG's data feeds pages. The company captures full-depth exchange feeds in raw PCAP form across 300+ venues and sells them through the Bellport feed handler (C++ library, on-premises or managed), a 20+ petabyte Market Data Lake of historical tick data (PCAP/Parquet queried via Athena SQL and the Medusa Python client), the cloud Analytics Workbench (JupyterLab), and the High Performance Query (HPQ) streaming WebSocket API for near-time data. Access is sales-gated and entitlement-managed with no self-serve signup or public developer portal; the public API surface that exists is documented through example "springboard" repositories on the MayStreet GitHub organization rather than a docs site.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maystreet.png
layout: provider
modified: '2026-07-22'
name: MayStreet
nav: Providers
network: true
overview: 'MayStreet publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial, Market Data, Real-Time, Trading, and Low Latency.


  MayStreet''s developer surface includes authentication, sandbox, and 8 more developer resources.'
random_paper: 3
screenshot: https://raw.githubusercontent.com/api-evangelist/maystreet/refs/heads/main/screenshots/maystreet-2026-07-22T202504.png
security:
- kind: authentication
  name: Maystreet Authentication
  slug: maystreet-authentication
  summary_line: http-bearer/custom-header · 2 schemes
- kind: domain-security
  name: Maystreet Domain Security
  slug: maystreet-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: maystreet
tags:
- Financial
- Market Data
- Real-Time
- Trading
- Low Latency
- Tick Data
- Order Book
- Equities
- Options
- Feed Handlers
- PCAP
website: https://maystreet.com/
---
