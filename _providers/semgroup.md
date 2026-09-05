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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/energy-transfer/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/semgroup-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/semgroup-corporation
- group: company
  title: ''
  type: Website
  url: https://www.semgroup.com
coverage:
  checked: '2026-09-04'
  detail: SemGroup ceased to exist as a company when its merger into Energy Transfer LP closed on 2019-12-05; www.semgroup.com now answers 302 on every path — including every /.well-known/ and spec path probed — and lands on Energy Transfer's corporate site, while the semgroup.com apex has no A record at all.
  evidence:
  - status: 302
    url: http://www.semgroup.com/
  - status: 302
    url: http://www.semgroup.com/.well-known/security.txt
  - status: 302
    url: http://www.semgroup.com/openapi.json
  - status: 503
    url: http://www.semgroup.com/developers
  - status: 0
    url: https://www.semgroup.com/
  reason: defunct
  state: none
created: '2026-03-24'
description: SemGroup Corporation was a Tulsa, Oklahoma midstream energy service provider that gathered, transported, stored, processed, and marketed crude oil, refined products, and natural gas liquids across North America, and operated the Houston Fuel Oil Terminal (HFOTCO) on the Houston Ship Channel. Energy Transfer LP acquired SemGroup in a $5.1 billion transaction that closed on December 5, 2019; the company was absorbed into Energy Transfer, its NYSE listing retired, and www.semgroup.com now redirects to energytransfer.com. SemGroup never operated a public developer program or API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/semgroup.png
layout: provider
modified: '2026-09-04'
name: SemGroup
nav: Providers
network: true
overview: SemGroup is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Midstream, Oil and Gas, Pipelines, and Crude Oil.
press:
- date: '2026-05-25'
  title: SemGroup buying Houston Fuel Oil Terminal Co. in $2B deal
  url: https://energynow.ca/2017/06/semgroup-buying-houston-fuel-oil-terminal-co-in-2b-deal/
- date: '2026-05-25'
  title: SemGroup's $3.2 billion failure shocks backers
  url: https://www.reuters.com/article/world/semgroups-32-billion-failure-shocks-backers-idUSN25503394/
- date: '2026-05-25'
  title: XBRL Viewer
  url: https://www.sec.gov/ix?doc=/Archives/edgar/data/0001489136/000119312519307334/d816435d8k.htm
- date: '2026-05-25'
  title: Producers Back SemGroup Reorganization Plan
  url: https://www.law360.com/energy/articles/122526/producers-back-semgroup-reorganization-plan
- date: '2026-05-25'
  title: 'Energy Transfer''s AI Strategy: Analysis of Dominance in ...'
  url: https://www.klover.ai/energy-transfer-ai-strategy-analysis-of-dominance-in-energy-ai/
random_paper: 0
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 2.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/semgroup/refs/heads/main/screenshots/semgroup-2026-06-20T193648.png
security:
- kind: domain-security
  name: Semgroup Domain Security
  slug: semgroup-domain-security
  summary_line: DMARC
slug: semgroup
tags:
- Energy
- Midstream
- Oil and Gas
- Pipelines
- Crude Oil
- Natural Gas Liquids
- Terminals
- Acquired
- Fortune 1000
website: https://www.semgroup.com
---
