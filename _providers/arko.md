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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 8
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arko/refs/heads/main/security/arko-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arko-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/arko-corp-us
- group: company
  title: ''
  type: Website
  url: https://www.arkocorp.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.arkocorp.com/company-information
- group: company
  title: ''
  type: Blog
  url: https://www.arkocorp.com/news-events/press-releases/rss
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arkocorp.com/privacy-policy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/arko/refs/heads/main/llms/arko-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arko-llms.txt
coverage:
  checked: '2026-09-18'
  detail: ARKO Corp is a convenience-store operator and fuel wholesaler whose entire public web presence is an investor-relations site, a WordPress subsidiary site and a loyalty-app marketing page; every /.well-known/ discovery path, /openapi.json, /swagger.json, /api-docs and /llms.txt returned 404 on arkocorp.com, gpminvestments.com, fasrewards.com and arkopetroleum.com, no developer subdomain resolves (the two wildcard-DNS domains serve the marketing page or a bare 404 on api./developer.), and the only machine-readable endpoint anywhere is the stock WordPress /wp-json discovery document on gpminvestments.com.
  evidence:
  - status: 404
    url: https://www.arkocorp.com/openapi.json
  - status: 404
    url: https://www.arkocorp.com/.well-known/security.txt
  - status: 404
    url: https://www.arkocorp.com/llms.txt
  - status: 404
    url: https://www.gpminvestments.com/.well-known/api-catalog
  - status: 404
    url: https://api.fasrewards.com/openapi.json
  - status: 404
    url: https://api.arkopetroleum.com/openapi.json
  - status: 200
    url: https://www.gpminvestments.com/wp-json
  reason: not-a-software-company
  state: none
created: '2026-03-21'
description: 'ARKO Corp (Nasdaq: ARKO) is a Fortune 500 company and one of the largest operators of convenience stores and wholesalers of fuel in the United States. Through its subsidiary GPM Investments, ARKO operates approximately 1,400 company-operated stores under 25+ regional brands across 30+ states, as well as proprietary cardlock locations and a fleet fueling network. In 2026, ARKO completed the IPO of ARKO Petroleum Corp., which operates its wholesale, fleet fueling, and petroleum distribution segments.'
features:
- description: Operates approximately 1,400 company-operated convenience stores under 25+ regional brands across 30+ U.S. states and Washington D.C.
  name: Convenience Store Network
- description: Proprietary fleet fuel cards providing access to a nationwide network of fueling sites including cardlock locations for commercial fleets.
  name: Fleet Fueling Cards
- description: Wholesale fuel supply to approximately 1,660 independent dealer sites through GPM Petroleum and ARKO Petroleum Corp.
  name: Wholesale Fuel Distribution
- description: Operates approximately 121 proprietary cardlock (unstaffed) fueling locations for fleet and commercial vehicle fueling.
  name: Cardlock Operations
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/arko.png
layout: provider
modified: '2026-09-18'
name: ARKO
nav: Providers
network: true
overview: 'ARKO is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Convenience Stores, Fleet Fueling, Fuel, Petroleum, and Retail.


  ARKO''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 55.4
    operational_transparency: 0.0
  previous_composite: 10.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/arko/refs/heads/main/screenshots/arko-2026-06-20T172433.png
security:
- kind: domain-security
  name: Arko Domain Security
  slug: arko-domain-security
  summary_line: TLSv1.3
slug: arko
tags:
- Convenience Stores
- Fleet Fueling
- Fuel
- Petroleum
- Retail
use_cases:
- description: Commercial fleets use ARKO's proprietary fuel card network to manage fuel expenses and access cardlock fueling locations nationwide.
  name: Fleet Fuel Management
- description: Retail consumers purchase food, beverages, and fuel at ARKO-operated convenience stores under regional brand names.
  name: Convenience Retail
- description: Independent fuel dealers and operators receive wholesale fuel supply through ARKO's petroleum distribution network.
  name: Wholesale Fuel Supply
website: https://www.arkocorp.com
---
