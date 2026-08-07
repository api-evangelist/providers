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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Trade Desk Agentic Access
  operation_count: 6
  slug: trade-desk-agentic-access
  summary_line: 6 operations · 6 acting
api_count: 8
apis:
- description: The original REST Platform API covering advertisers, campaigns, ad groups, creatives, targeting data, reporting, and audience operations. Documentation is gated behind the TTD Partner Portal. New inte
  name: The Trade Desk Platform API
  slug: trade-desk-platform-api
- description: Server-side and client-side conversion event ingestion (Apache 2.0 Google Tag Manager templates) for capturing high-fidelity attribution signals in a cookie-deprecated environment. Pairs with UID2 for
  name: The Trade Desk Real-Time Conversion Events API
  slug: trade-desk-realtime-conversion-events-api
- description: Unified ID 2.0 is an open-source, deterministic identity framework seeded by The Trade Desk and now governed by the IAB Tech Lab. UID2 resolves hashed email addresses and phone numbers into rotating t
  name: Unified ID 2.0 (UID2)
  slug: trade-desk-uid2-api
- description: OpenSincera (from the May 2024 Sincera acquisition) provides programmatic supply-side transparency data — ad slot quality, page attributes, viewability metadata, supply-path metrics — to help buyers v
  name: OpenSincera API
  slug: trade-desk-opensincera-api
- description: The Advertiser API from The Trade Desk — 1 operation(s) for advertiser.
  name: The Trade Desk Advertiser API
  slug: trade-desk-advertiser-api
- description: The DeletionOptOut API from The Trade Desk — 3 operation(s) for deletionoptout.
  name: The Trade Desk DeletionOptOut API
  slug: trade-desk-deletionoptout-api
- description: The OfflineConversion API from The Trade Desk — 1 operation(s) for offlineconversion.
  name: The Trade Desk OfflineConversion API
  slug: trade-desk-offlineconversion-api
- description: The ThirdParty API from The Trade Desk — 1 operation(s) for thirdparty.
  name: The Trade Desk ThirdParty API
  slug: trade-desk-thirdparty-api
artifact_total: 12
collections:
- collection_type: open
  name: TTD Data API
  slug: open-trade-desk-data-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trade-desk-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trade-desk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.thetradedesk.com
- group: start
  title: ''
  type: Portal
  url: https://www.thetradedesk.com/us
- group: docs
  title: ''
  type: Documentation
  url: https://open.thetradedesk.com
- group: docs
  title: ''
  type: Documentation
  url: https://partner.thetradedesk.com
- group: start
  title: ''
  type: GettingStarted
  url: https://partner.thetradedesk.com/v3/portal/api/doc/ApiPlatformGetStarted
- group: other
  title: ''
  type: Product
  url: https://www.thetradedesk.com/us/our-platform
- group: other
  title: ''
  type: Product
  url: https://www.thetradedesk.com/us/our-platform/dsp-demand-side-platform
- group: other
  title: ''
  type: Product
  url: https://www.thetradedesk.com/us/openpath
- group: other
  title: ''
  type: Product
  url: https://www.thetradedesk.com/us/our-platform/koa-ai-artificial-intelligence
- group: other
  title: ''
  type: Product
  url: https://www.thetradedesk.com/us/news/introducing-galileo
- group: other
  title: ''
  type: Identity
  url: https://unifiedid.com
- group: other
  title: ''
  type: Identity
  url: https://euid.eu
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TheTradeDesk
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/IABTechLab
- group: build
  title: ''
  type: SDKs
  url: https://github.com/TheTradeDesk/ttd-workflows-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/TheTradeDesk/ttd-workflows-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/TheTradeDesk/ttd-workflows-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/TheTradeDesk/ttd-data-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/TheTradeDesk/ttd-databricks-python
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/TheTradeDesk/Platform
- group: company
  title: ''
  type: PressRoom
  url: https://www.thetradedesk.com/us/news
- group: company
  title: ''
  type: Blog
  url: https://www.thetradedesk.com/us/news-insights
- group: company
  title: ''
  type: Newsroom
  url: https://www.thetradedesk.com/us/press-room
- group: company
  title: ''
  type: AboutUs
  url: https://www.thetradedesk.com/us/about-us
- group: company
  title: ''
  type: Careers
  url: https://careers.thetradedesk.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.thetradedesk.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thetradedesk.com/us/website-privacy-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thetradedesk.com/us/website-privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.thetradedesk.com/us/contact-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-trade-desk
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/thetradedesk
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@thetradedesk
created: '2026-05-25'
description: 'The Trade Desk is an independent, omnichannel demand-side platform (DSP) for programmatic advertising, headquartered in Ventura, California. Its cloud-based platform — Kokai (the current flagship, succeeding Solimar) — lets agencies, brands, and trading desks buy and optimize digital ad inventory across connected TV (CTV), audio, mobile, video, native, display, and digital out-of-home. The Trade Desk positions itself as the buy-side counterweight to the walled gardens by championing the open internet through OpenPath (direct publisher integrations that bypass SSPs) and Unified ID 2.0 (UID2), an open-source, deterministic identity framework governed by the IAB Tech Lab. The company also stewards EUID (UID2''s European equivalent), the Galileo first-party data activation framework, and Koa — its in-platform AI used for forecasting, bidding optimization, and audience modeling. Programmatic developers integrate via the TTD Workflows API (REST + GraphQL for campaign, ad group, and
  creative management), the Data API (advertiser/third-party data ingestion, offline conversions, deletion/opt-out), the Real-Time Conversion Events API (RTCE), and the OpenSincera data-quality APIs (acquired May 2024). Official SDKs are published in Python, Go, and Java and are Speakeasy-generated from OpenAPI specs. Most documentation lives behind the Partner Portal (partner.thetradedesk.com) but a public docs surface is exposed at open.thetradedesk.com. The Trade Desk is publicly traded (NASDAQ: TTD).'
graphqls:
- description: The Workflows API exposes the high-level campaign, ad group, creative, and bulk-job operations that previously required navigating the legacy Platform API. It blends REST and GraphQL surfaces (includi
  name: The Trade Desk GraphQL API
  slug: trade-desk-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trade-desk.png
layout: provider
modified: '2026-05-25'
name: The Trade Desk
nav: Providers
network: true
overview: 'The Trade Desk publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Advertiser API, DeletionOptOut API, OfflineConversion API, and 1 more. Tagged areas include Advertising, Programmatic Advertising, Demand-Side Platform, DSP, and AdTech.


  The Trade Desk''s developer surface includes developer portal, documentation, getting-started guide, code examples, engineering blog, YouTube channel, and 28 more developer resources.'
random_paper: 92
score:
  band: thin
  composite: 31.6
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 44.2
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 31.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trade-desk/refs/heads/main/screenshots/trade-desk-2026-06-20T195532.png
security:
- kind: domain-security
  name: Trade Desk Domain Security
  slug: trade-desk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trade-desk
tags:
- Advertising
- Programmatic Advertising
- Demand-Side Platform
- DSP
- AdTech
- Connected TV
- CTV
- Identity
- Unified ID 2.0
- UID2
- OpenPath
- Kokai
- Koa AI
- Galileo
- Sincera
- Open Internet
- Real-Time Bidding
- Open Measurement
website: https://www.thetradedesk.com
---
