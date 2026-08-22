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
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mth-sense-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mth-sense-plans-pricing.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mth-sense-llms.txt
- group: company
  title: ''
  type: Website
  url: https://mthsense.com/
- group: start
  title: ''
  type: Login
  url: https://mthsense.com/login.html
- group: operate
  title: ''
  type: FAQ
  url: https://mthsense.com/faq.html
- group: operate
  title: ''
  type: Support
  url: https://mthsense.com/contact.html
coverage:
  checked: '2026-08-12'
  detail: RevSense sells a managed publisher yield-optimization service, not an interface — its own FAQ describes RevSense using a publisher's handed-over ad-server and SSP credentials to drive Google Ad Manager, OpenX and PubMatic on their behalf, and the whole company web presence is a five-page static marketing site (last copyright 2017) where /openapi.json, /docs, /developers, /llms.txt and /robots.txt all 404, every /.well-known/ path answers an Apache content-negotiation 300, and api., docs., developer., app., portal. and dashboard. subdomains are all NXDOMAIN.
  evidence:
  - status: 404
    url: https://mthsense.com/openapi.json
  - status: 404
    url: https://mthsense.com/developers
  - status: 300
    url: https://mthsense.com/.well-known/api-catalog
  - status: 200
    url: https://mthsense.com/faq.html
  - status: 200
    url: https://mthsense.com/pricing.html
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: mth Sense (Mth Sense Inc.), operating as RevSense, is a mobile ad-technology company founded in 2011 by Mandar Agte and Mohan Balachandran and backed by Y Combinator (Summer 2012). It began as a mobile on-device profiling and ad-serving platform that inferred demographic and psychographic audience profiles from app-usage data, and has evolved into a programmatic yield and revenue-optimization platform for digital publishers. The RevSense product suite provides machine-learning yield optimization (real-time price floors, frequency caps, geo controls), automated header-bidding tag management, a unified reporting and data platform aggregating ad-server and demand-partner data, and one-click demand/buyer integration. mth Sense markets to publishers, agencies, SSPs, ad networks, and advertisers, and will build private exchanges with an RTB engine and common reporting dashboards. As of this profile the company publishes a static marketing website with no public developer portal, API
  documentation, or SDKs.
image: https://mthsense.com/images/logo.svg
layout: provider
modified: '2026-08-12'
name: mth Sense
nav: Providers
network: true
overview: 'mth Sense is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Programmatic Advertising, and Ad Server.


  mth Sense''s developer surface includes FAQ, support, and 5 more developer resources.'
plans:
- name: Mth Sense Plans Pricing
  plan_count: 0
  slug: mth-sense-plans-pricing
random_paper: 13
score:
  band: minimal
  composite: 8.0
  delta: -1.2
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mth-sense/refs/heads/main/screenshots/mth-sense-2026-08-07T184420.png
security:
- kind: domain-security
  name: Mth Sense Domain Security
  slug: mth-sense-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mth-sense
tags:
- Company
- Advertising
- AdTech
- Programmatic Advertising
- Ad Server
- Yield Optimization
- Header Bidding
- Mobile Advertising
- Publishers
- Data
website: https://mthsense.com/
---
