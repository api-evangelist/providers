---
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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-08'
api_count: 0
artifact_total: 0
coverage:
  checked: '2026-09-07'
  detail: Addiction Campuses of America is a residential behavioral-healthcare campus operator, not a software vendor — the 4,000 archived addictioncampuses.com URLs contain no /api, /developers or /docs path, and the only machine-readable surface found on any of its hosts is the stock WordPress REST index at https://vertavahealth.com/wp-json/, which is generic CMS plumbing rather than a published API.
  evidence:
  - status: 202
    url: https://addictioncampuses.com/
  - status: 202
    url: https://addictioncampuses.com/openapi.json
  - status: 202
    url: https://addictioncampuses.com/.well-known/agent-card.json
  - status: 301
    url: https://vertavahealth.com/
  - status: 404
    url: https://vertavahealth.com/openapi.json
  - status: 404
    url: https://vertavahealth.com/.well-known/agent-card.json
  - status: 200
    url: https://vertavahealth.com/wp-json/
  - status: 404
    url: https://api.github.com/orgs/addictioncampuses
  - status: 404
    url: https://pypi.org/pypi/vertava/json
  - status: 200
    url: https://equityzen.com/company/addictioncampusesofamerica/
  reason: not-a-software-company
  state: none
created: '2026-09-07'
description: 'Addiction Campuses of America (EquityZen ticker ACOA) was founded in 2014 in Brentwood, Tennessee and owned, operated and managed residential behavioral-healthcare campuses across the United States, treating substance use disorder and co-occurring mental health conditions through detox, residential, partial-hospitalization and outpatient programs, several of them holding the Joint Commission Gold Seal of Approval. Summit Partners invested in the company in 2018, and on 2020-08-01 it renamed itself Vertava Health. The successor host vertavahealth.com is still a live WordPress installation but now 301-redirects its homepage to Connections Wellness Group, an unrelated behavioral-health provider, and the original addictioncampuses.com answers every request with a SiteGround proof-of-work bot interstitial. This is a clinical services operator, not a software vendor: a full contract-discovery pass across all three hosts, the package registries, GitHub and 4,000 archived URLs found
  no developer program, API documentation, SDK or machine-readable contract of any kind.'
layout: provider
modified: '2026-09-07'
name: Addiction Campuses of America
nav: Providers
network: true
overview: Addiction Campuses of America is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Behavioral Health, Addiction Treatment, and Substance Use Disorder.
random_paper: 13
score:
  band: minimal
  composite: 1.8
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 1.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 0.0
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: addictioncampusesofamerica
tags:
- Company
- Healthcare
- Behavioral Health
- Addiction Treatment
- Substance Use Disorder
- Mental Health
- Residential Treatment
- Tennessee
---
