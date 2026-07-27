---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-27'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.openx.com
- group: other
  title: ''
  type: Products
  url: https://www.openx.com/products/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openx.com
- group: other
  title: ''
  type: Developers
  url: https://docs.openx.com/Content/developers/index.html
- group: other
  title: ''
  type: OpenXExchange
  url: https://www.openx.com/products/openx-exchange/
- group: other
  title: ''
  type: OpenXSelect
  url: https://www.openx.com/products/openx-select/
- group: other
  title: ''
  type: OpenXBuild
  url: https://www.openx.com/products/openx-build/
- group: other
  title: ''
  type: OpenXControl
  url: https://www.openx.com/products/openx-control/
- group: other
  title: ''
  type: Publishers
  url: https://www.openx.com/publishers/
- group: other
  title: ''
  type: Advertisers
  url: https://www.openx.com/advertisers/
- group: company
  title: ''
  type: Partners
  url: https://www.openx.com/partners/
- group: other
  title: ''
  type: Leadership
  url: https://www.openx.com/leadership/
- group: company
  title: ''
  type: Newsroom
  url: https://www.openx.com/newsroom/
- group: company
  title: ''
  type: Blog
  url: https://www.openx.com/blog/
- group: company
  title: ''
  type: Careers
  url: https://www.openx.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.openx.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.openx.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.openx.com/terms-of-use/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openx
- group: build
  title: ''
  type: SDK — Python (OX3)
  url: https://github.com/openx/OX3-Python-API-Client
- group: build
  title: ''
  type: SDK — PHP (OX3)
  url: https://github.com/openx/OX3-PHP-API-Client
- group: build
  title: ''
  type: SDK — Java (OX3)
  url: https://github.com/openx/OX3-Java-API-Client
- group: build
  title: ''
  type: SDK — Perl (OX3)
  url: https://github.com/openx/OX3-Perl-API-Client
- group: build
  title: ''
  type: SDK — Ruby (OX3)
  url: https://github.com/openx/OX3-Ruby-API-Client
- group: build
  title: ''
  type: Tool — Prebid.js
  url: https://github.com/openx/Prebid.js
- group: build
  title: ''
  type: Tool — Prebid Server
  url: https://github.com/openx/prebid-server
- group: build
  title: ''
  type: Tool — Reporting API Client (Python)
  url: https://github.com/openx/reporting-api-client
- group: build
  title: ''
  type: Tool — SSRTBPriceCrypter
  url: https://github.com/openx/SSRTBPriceCrypter
- group: build
  title: ''
  type: Tool — Enrichment Service Template
  url: https://github.com/openx/openx-enrichment-service-template
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openx
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/OpenX
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/OpenXTV
created: '2026-05-25'
description: OpenX is an independent supply-side platform (SSP) and programmatic ad exchange headquartered in Pasadena, California, founded in 2008. OpenX connects publishers and app developers to advertiser demand through a real-time marketplace that runs OpenRTB-based auctions across display, video, CTV, native, and mobile inventory. Its product suite is organized around the OpenX Exchange (the core marketplace), OpenXSelect (curation, deal creation, and supply-path targeting), OpenXBuild (a software toolkit for assembling custom supply-side workflows and real-time bidstream integrations), and OpenXControl (publisher yield management and demand routing). OpenX exposes several developer-facing APIs documented at docs.openx.com — an OpenRTB API for DSP bidding integrations, a Platform API for account, inventory, demand, targeting, and deal management, a Reporting API for analytics and performance metrics, an OpenXSelect GraphQL API for managing audiences/deals/inventory lists, and an OpenXBuild
  Real-Time Bidstream API — but the references are gated behind OAuth and OpenX does not publish a public OpenAPI specification or Postman collection. The company is a major contributor to the Prebid.org header-bidding ecosystem (Prebid.js and Prebid Server) and maintains a large GitHub organization with OAuth-based API client libraries in Python, PHP, Java, Perl, and Ruby for the legacy OX3 API. OpenX's business model is transaction-fee based — it takes a share of each ad impression cleared through its exchange — and access to the developer APIs requires an active OpenX account and BD/account-management onboarding rather than self-service signup.
graphqls:
- description: ''
  name: OpenX GraphQL API
  slug: openx-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openx.png
layout: provider
modified: '2026-05-25'
name: OpenX
nav: Providers
network: true
overview: 'OpenX is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Programmatic Advertising, Ad Exchange, Supply Side Platform, and SSP.


  OpenX''s developer surface includes documentation, engineering blog, YouTube channel, and 30 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 13.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 13.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openx/refs/heads/main/screenshots/openx-2026-06-20T191054.png
security:
- kind: domain-security
  name: Openx Domain Security
  slug: openx-domain-security
  summary_line: TLSv1.3 · DMARC
slug: openx
tags:
- Advertising
- Programmatic Advertising
- Ad Exchange
- Supply Side Platform
- SSP
- Real Time Bidding
- OpenRTB
- Header Bidding
- Prebid
- AdTech
- CTV
- Video Advertising
- Display Advertising
- Curation
- Identity
website: https://www.openx.com
---
