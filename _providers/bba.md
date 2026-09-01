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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: InvestorPortfolio
  url: https://a16z.com/investment-list/
created: '2026-07-17'
description: 'BBA is a name-only entry harvested from the Andreessen Horowitz public investment list (https://a16z.com/investment-list/), where it appears alphabetically between Bayesian Health and Beacons.ai. As of the 2026-07-20 enrichment pass the entry could not be resolved to an operating company: a16z publishes no link, description, or category for it, the name does not appear in the a16z portfolio detail pages, and web searches surface no startup, funding round, or press coverage matching it. Candidate domains (bba.com, bba.ai, bba.co, getbba.com) either fail to resolve or are parked for sale, so there is no website, developer portal, documentation, or API surface to profile. This profile is retained as an unresolved venture-portfolio lead rather than an API provider; it should be re-checked if a16z ever attaches a link to the entry or the company emerges publicly under this name.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bba.png
layout: provider
modified: '2026-07-20'
name: BBA
nav: Providers
network: true
overview: BBA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Venture Backed, a16z Portfolio, Portfolio Lead, and Unresolved.
random_paper: 20
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 1
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  previous_composite: 5.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bba/refs/heads/main/screenshots/bba-2026-07-25T202453.png
slug: bba
tags:
- Company
- Venture Backed
- a16z Portfolio
- Portfolio Lead
- Unresolved
- Stub
---
