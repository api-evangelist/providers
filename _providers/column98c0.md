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
api_count: 1
apis:
- description: Column provides banking infrastructure APIs for developers.
  name: Column API
  slug: column-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/column98c0/refs/heads/main/conformance/column98c0-conformance.yml
  title: ''
  type: Conformance
  url: conformance/column98c0-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/column98c0/refs/heads/main/hosts/column98c0-hosts.yml
  title: ''
  type: Hosts
  url: hosts/column98c0-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/column98c0/refs/heads/main/vendors/column98c0-vendors.yml
  title: ''
  type: Vendors
  url: vendors/column98c0-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/column98c0/refs/heads/main/security/column98c0-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/column98c0-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/column98c0
created: '2026-10-09'
description: Column98c0 is a technology-focused company identified through the API Evangelist secondary-market harvest. While detailed public information is limited, the company is positioned as a provider of data services and API-driven solutions. Further investigation is required to uncover its exact product offerings, target markets, and operational scope. This placeholder description will be refined as more concrete information becomes available through subsequent profiling steps.
layout: provider
modified: '2026-10-09'
name: Column98c0
nav: Providers
network: true
overview: Column98c0 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Technology, and Services.
random_paper: 12
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: venue_as_website
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Column98C0 Domain Security
  slug: column98c0-domain-security
  summary_line: TLSv1.3 · DMARC
slug: column98c0
tags:
- Company
- Data
- Technology
- Services
website: https://equityzen.com/company/column98c0
---
