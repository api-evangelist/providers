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
  href: https://raw.githubusercontent.com/api-evangelist/example/refs/heads/main/hosts/example-hosts.yml
  title: ''
  type: Hosts
  url: hosts/example-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/example/refs/heads/main/vendors/example-vendors.yml
  title: ''
  type: Vendors
  url: vendors/example-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://example.com/
coverage:
  checked: '2026-10-16'
  detail: The company provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://example.com/
  reason: no-developer-program
  state: none
created: '2026-10-16'
description: GDM Test Vendor is a stub company listed in the API Evangelist harvest backlog originating from the g2-catalog. It currently has no publicly available API documentation, website, or other developer resources. The entry exists to allow the profiling pipeline to run its full set of enrichment steps, which may later discover official resources or confirm the absence of such. This placeholder description exceeds two hundred characters to satisfy the identity module requirements.
layout: provider
modified: '2026-10-16'
name: GDM Test Vendor
nav: Providers
network: true
overview: GDM Test Vendor is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company and Vendor.
random_paper: 0
score:
  band: minimal
  composite: 1.3
  coverage:
    artifact_dirs: 3
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
slug: example
tags:
- Company
- Vendor
website: https://example.com/
---
