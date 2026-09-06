---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://earn.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.coinbase.com/earn?claim=true — a different registrable domain (earn.com -> coinbase.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/earn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://earn.com
created: '2026-07-17'
description: 'Earn.com (formerly 21 Inc / 21.co) was a cryptocurrency startup that let people earn Bitcoin by replying to paid messages and completing microtasks, effectively a paid-email and paid-task marketplace settled in crypto. Founded by Balaji Srinivasan and backed by DCVC among others, the company was acquired by Coinbase in April 2018 (Coinbase, ticker COIN) and folded into the Coinbase Earn product. The independent earn.com property no longer operates a standalone product or developer surface: earn.com now issues a 301 redirect to coinbase.com/earn, and earlier hosts such as 21.co and api.earn.com no longer resolve. This profile is retained in the API Evangelist network as an acquired-company record; there is no independent, first-party API, developer portal, or OpenAPI to enrich.'
image: https://raw.githubusercontent.com/api-evangelist/earn/refs/heads/main/apis.yml
layout: provider
modified: '2026-07-18'
name: Earn
nav: Providers
network: true
overview: Earn is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Bitcoin, Payments, and Acquired.
random_paper: 2
score:
  band: minimal
  composite: 1.5
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
  previous_composite: 1.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/earn/refs/heads/main/screenshots/earn-2026-07-25T212646.png
security:
- kind: domain-security
  name: Earn Domain Security
  slug: earn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: earn
tags:
- Company
- Cryptocurrency
- Bitcoin
- Payments
- Acquired
- Coinbase
website: https://earn.com
---
