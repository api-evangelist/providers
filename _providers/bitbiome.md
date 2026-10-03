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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API for accessing Bitbiome dataset metadata and discovery.
  name: Bitbiome API
  slug: bitbiome-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitbiome/refs/heads/main/hosts/bitbiome-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitbiome-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bitbiome/refs/heads/main/vendors/bitbiome-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitbiome-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bitbiome/refs/heads/main/security/bitbiome-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitbiome-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/bitbiome
coverage:
  checked: '2026-09-28'
  detail: The provider's WordPress REST endpoint at https://bitbiome.bio/wp-json/ returns JSON but no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://bitbiome.bio/wp-json/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Bitbiome is a data‑focused biotechnology platform that aggregates, curates, and provides access to a wide range of biological datasets and analytical tools. It aims to accelerate research and development in life sciences by offering APIs for dataset discovery, metadata retrieval, and integration with computational pipelines. The company positions itself as a bridge between raw biological data and actionable insights for scientists, developers, and enterprises in the biotech sector.
layout: provider
modified: '2026-09-28'
name: Bitbiome
nav: Providers
network: true
overview: Bitbiome publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Biotechnology, Data, Life Sciences, and Platform.
random_paper: 7
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 5
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
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bitbiome Domain Security
  slug: bitbiome-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bitbiome
tags:
- Biotechnology
- Data
- Life Sciences
- Platform
website: https://equityzen.com/company/bitbiome
---
