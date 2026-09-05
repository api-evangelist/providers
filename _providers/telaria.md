---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://telaria.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.magnite.com/ — a different registrable domain (telaria.com -> magnite.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://telaria.com
- group: other
  title: ''
  type: SuccessorCompany
  url: https://www.magnite.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/telaria-domain-security.yml
created: '2026-07-17'
description: 'Telaria was an independent supply-side platform (SSP) for premium video and connected TV (CTV) advertising, formerly known as Tremor Video''s sell-side business. Its Video Management Platform (VMP) combined an ad server built for advanced/OTT TV with real-time analytics, automated decisioning, yield optimization, and integrated programmatic plus direct-sold monetization for publishers of digital video inventory. On April 1, 2020 Telaria completed an all-stock merger of equals with Rubicon Project to form Magnite, now the largest independent sell-side advertising platform spanning CTV, desktop, and mobile. Telaria no longer operates as a standalone company: the telaria.com domain redirects to magnite.com, and the "Telaria" name survives publicly only as a Prebid.js header-bidding bidder adapter routed through Magnite. This profile documents the historical company; there is no independent public developer API, OpenAPI definition, SDK, or documentation portal to harvest.'
image: https://raw.githubusercontent.com/api-evangelist/telaria/refs/heads/main/apis.yml
layout: provider
modified: '2026-07-21'
name: Telaria
nav: Providers
network: true
overview: Telaria is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, AdTech, Video Advertising, and Connected TV.
random_paper: 3
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/telaria/refs/heads/main/screenshots/telaria-2026-09-02T162730.png
security:
- kind: domain-security
  name: Telaria Domain Security
  slug: telaria-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: telaria
tags:
- Company
- Advertising
- AdTech
- Video Advertising
- Connected TV
- CTV
- Supply Side Platform
- SSP
- Programmatic
- Acquired
website: https://telaria.com
---
