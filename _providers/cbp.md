---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 4
apis:
- description: A web service that allows certified third-party applications to query Electronic Export Information (EEI) filings previously submitted to AESDirect via HTTP POST. Returns shipment status and filing da
  name: AESDirect WebLink Inquiry API
  slug: aesdirect-weblink-inquiry-api
- description: A web service that allows certified third-party Internet applications to pass Electronic Export Information (EEI) data directly into AESDirect via HTTP POST, eliminating double-entry for exporters and
  name: AESDirect WebLink Submission API
  slug: aesdirect-weblink-submission-api
- description: The U.S. Single Window for import and export trade reporting. The Automated Broker Interface (ABI) lets licensed customs brokers and self-filers transmit entry summaries, cargo release requests, and m
  name: Automated Commercial Environment (ACE) — EDI / ABI
  slug: ace-automated-commercial-environment
- description: A CBP web-based application for commercial and private carriers to electronically submit inbound and outbound traveler manifest data. Supports on-screen entry, bulk XML upload, and UN/EDIFACT PAXLST e
  name: eAPIS — Advance Passenger Information System
  slug: eapis-advance-passenger-information
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cbp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cbp.gov
- group: docs
  title: ''
  type: Documentation
  url: https://www.cbp.gov/trade/automated
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/US-CBP
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/customs-and-border-protection
- group: company
  title: ''
  type: Blog
  url: https://www.cbp.gov/newsroom
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cbp.gov/trade/automated/ace-faq
- group: operate
  title: ''
  type: StatusPage
  url: https://www.cbp.gov/trade/automated/ace-support
- group: other
  title: ''
  type: X
  url: https://x.com/CBP
- group: commercial
  title: ''
  type: Plans
  url: plans/cbp-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cbp-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cbp-finops.yml
- group: company
  title: ''
  type: News
  url: https://www.cbp.gov/newsroom/stats/cbp-public-data-portal
created: '2026-06-13'
description: U.S. Customs and Border Protection (CBP) is the nation's largest law enforcement agency and a major revenue-collecting authority, responsible for facilitating legitimate international trade and travel while enforcing trade laws, collecting duties, and securing the border. CBP provides REST APIs and EDI-based interfaces for trade data, import statistics, tariff schedules, ACE reporting, and automated import/export manifests through the Automated Commercial Environment (ACE), the Automated Export System (AES / AESDirect), and the Advance Passenger Information System (APIS/eAPIS).
finops:
- name: Cbp Finops
  service_category: ''
  slug: cbp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cbp.png
jsonld:
- class_count: 24
  name: Cbp Context
  property_count: 0
  slug: cbp-context
layout: provider
modified: '2026-07-25'
name: CBP
nav: Providers
network: true
overview: 'CBP publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include US Government, Trade, Customs, Import, and Export.


  The CBP catalog on APIs.io includes 1 JSON-LD context.


  CBP''s developer surface includes documentation, engineering blog, pricing, product news, and 9 more developer resources.'
plans:
- name: Cbp Plans Pricing
  plan_count: 4
  slug: cbp-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Cbp Rate Limits
  slug: cbp-rate-limits
score:
  band: emerging
  composite: 25.2
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 11.3
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 25.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cbp/refs/heads/main/screenshots/cbp-2026-06-20T174055.png
security:
- kind: domain-security
  name: Cbp Domain Security
  slug: cbp-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cbp
tags:
- US Government
- Trade
- Customs
- Import
- Export
- Border Protection
- Tariff
- Manifests
website: https://www.cbp.gov
---
