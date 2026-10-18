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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 0
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/walrus/refs/heads/main/hosts/walrus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/walrus-hosts.yml
coverage:
  checked: '2026-10-12'
  detail: Unable to retrieve OpenAPI spec from known API host https://api.walrus.ai/ (network error).
  evidence:
  - status: network_error
    url: https://api.walrus.ap i .json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Walrus is a technology company focused on providing innovative cloud-based solutions for data management and analytics. Founded with the vision to simplify complex data workflows, Walrus offers a suite of APIs that enable developers to integrate data ingestion, processing, and visualization capabilities into their applications. The company emphasizes scalability, security, and ease of use, targeting enterprises and developers seeking robust data infrastructure services.
layout: provider
modified: '2026-10-12'
name: Walrus
nav: Providers
network: true
overview: Walrus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Cloud, and Analytics.
random_paper: 10
score:
  band: minimal
  composite: 1.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 35.7
    operational_transparency: 0.0
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
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: walrus
tags:
- Company
- Data
- Cloud
- Analytics
---
