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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/additiveintelligence/
coverage:
  checked: '2026-09-07'
  detail: Additive Intelligence's own declared website, www.additiveintelligence.com (the URL on its LinkedIn company page), is registered and delegated to Google Cloud DNS but publishes no A record, so the apex, www, api and docs hosts all fail to connect (curl 000) and STEP 0b contract discovery — /openapi.json, /swagger.json, /docs, /llms.txt, /.well-known/agent-card.json, /.well-known/security.txt — had no reachable host to run against; there is no GitHub organization, no published npm/PyPI package, and the EquityZen listing this record was harvested from now renders a different company (APrevent).
  evidence:
  - status: 0
    url: https://additiveintelligence.com/openapi.json
  - status: 0
    url: https://additiveintelligence.com/.well-known/agent-card.json
  - status: 0
    url: https://api.additiveintelligence.com/openapi.json
  - status: 0
    url: https://docs.additiveintelligence.com/
  - status: 404
    url: https://api.github.com/orgs/additiveintelligence
  - status: 404
    url: https://pypi.org/pypi/additive-intelligence/json
  - status: 200
    url: https://www.linkedin.com/company/additiveintelligence/
  - status: 200
    url: https://www.taiwanarena.tech/startups-detail/AdditiveIntelligence/
  - status: 200
    url: https://equityzen.com/company/additiveintelligencea7d2/
  reason: defunct
  state: none
created: '2026-09-07'
description: 'Additive Intelligence was a Taipei, Taiwan startup applying machine learning to metal additive manufacturing. Its focus was the deformation and shrinkage that occurs when metal 3D printed parts are sintered — the expensive trial-and-error step that keeps metal AM from being fast, scalable and cost-competitive — and it paired hardware with software, holding provisional patents on a machine learning method, a proprietary infill topology, and a method for varying the density of infilled sections. The company was selected by Taiwan Tech Arena as one of 100 startups showcased at CES 2021, and its LinkedIn page carries the slogan "Additive manufacturing, exponential progress." No first-party surface survives: the website the company itself declares on LinkedIn, www.additiveintelligence.com, holds an active registration on Google Cloud DNS but publishes no A record, so no host — apex, www, api or docs — can be connected to at all. There is no developer portal, GitHub organization,
  published package, or API of any kind.'
layout: provider
modified: '2026-09-16'
name: Additive Intelligence
nav: Providers
network: true
overview: Additive Intelligence is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Additive Manufacturing, 3D Printing, Metal 3D Printing, and Machine Learning.
random_paper: 13
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 0
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - taiwan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: additiveintelligencea7d2
tags:
- Company
- Additive Manufacturing
- 3D Printing
- Metal 3D Printing
- Machine Learning
- Artificial Intelligence
- Manufacturing
- Sintering
- Taiwan
- Defunct
---
