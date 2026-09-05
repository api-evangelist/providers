---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://rocketrip.com'', ''status'': 301, ''note'': ''declared website redirects to https://tabhi.ai/ — a different registrable domain (rocketrip.com -> tabhi.ai), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rocketrip-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rocketrip.com
created: '2026-07-17'
description: Rocketrip was a New York City corporate travel cost-savings platform that gave business travelers a personalized budget (a "Price to Beat") and rewarded employees who booked flights, hotels, and rail below it, sharing the savings between the traveler and the company. It was backed by Canaan Partners, GV, Bessemer, and Y Combinator. As of this enrichment pass the rocketrip.com and www.rocketrip.com domains 301-redirect to Tabhi (tabhi.ai / tabhi.com), the developer, docs, and api subdomains no longer resolve, and no public API, developer portal, or OpenAPI could be found — the standalone Rocketrip product and its API surface appear to have been retired or folded into Tabhi.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rocketrip.png
layout: provider
modified: '2026-07-21'
name: Rocketrip
nav: Providers
network: true
overview: Rocketrip is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Corporate Travel, Expense Management, and Travel Management.
random_paper: 13
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
screenshot: https://raw.githubusercontent.com/api-evangelist/rocketrip/refs/heads/main/screenshots/rocketrip-2026-09-02T154036.png
security:
- kind: domain-security
  name: Rocketrip Domain Security
  slug: rocketrip-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rocketrip
tags:
- Company
- Travel
- Corporate Travel
- Expense Management
- Travel Management
- Fintech
- Rewards
website: https://rocketrip.com
---
