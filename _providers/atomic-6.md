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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API for Atomic-6 services (no public OpenAPI spec found).
  name: Atomic-6 API
  slug: atomic-6-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atomic-6/refs/heads/main/hosts/atomic-6-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atomic-6-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atomic-6/refs/heads/main/vendors/atomic-6-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atomic-6-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atomic-6/refs/heads/main/security/atomic-6-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atomic-6-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atomic-6.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://atomic-6.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atomic-6.com/privacy-policy/
coverage:
  checked: 2026-09-26
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found at the API host (https://api.atomic-6.com/).
  evidence:
  - status: 0
    url: https://api.atomic-6.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Atomic-6 designs and manufactures advanced composite aerospace components, offering products such as Light Wing solar arrays, Space Armor protective tiles, and Light Sheet panels. The company provides high‑performance, ITAR‑registered solutions for satellite, spacecraft, and defense applications, emphasizing CMMC 2.0 compliance and AS9100 certification. Customers can request custom quotes, view detailed datasheets, and purchase through the online store. Atomic-6 aims to enable reliable, lightweight structures for space and terrestrial missions.
layout: provider
modified: '2026-09-26'
name: Atomic-6
nav: Providers
network: true
overview: Atomic-6 publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Aerospace, Composite Materials, Space Technology, and Defense.
random_paper: 10
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Atomic 6 Domain Security
  slug: atomic-6-domain-security
  summary_line: TLSv1.3 · DMARC
slug: atomic-6
tags:
- Company
- Aerospace
- Composite Materials
- Space Technology
- Defense
website: https://atomic-6.com/
---
