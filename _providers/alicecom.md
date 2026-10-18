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
- description: Guest API for Alicecom providing hotel and ticket operations
  name: Guest API
  slug: guest-api
artifact_total: 2
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/alicecom/refs/heads/main/conformance/alicecom-conformance.yml
  title: ''
  type: Conformance
  url: conformance/alicecom-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alicecom/refs/heads/main/hosts/alicecom-hosts.yml
  title: ''
  type: Hosts
  url: hosts/alicecom-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/alicecom/refs/heads/main/vendors/alicecom-vendors.yml
  title: ''
  type: Vendors
  url: vendors/alicecom-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.aliceapp.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aliceapp
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/alicecom/refs/heads/main/security/alicecom-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/alicecom-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aliceapp.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://aliceapp.com/api/mcp
  - status: 403
    url: https://auth.aliceapp.com/mcp
  - status: 200
    url: https://aliceapp.com
  - status: 403
    url: https://equityzen.com/company/alicecom
  reason: no-developer-program
  state: none
created: '2026-09-24'
description: Alicecom is a stub entry in the API Evangelist catalog, representing a company identified from secondary-market sources. The entry is intended for full profiling through the enrichment pipeline, which will gather detailed information about its APIs, documentation, and operational characteristics. This placeholder description will be expanded as real data is collected and verified.
layout: provider
modified: '2026-09-24'
name: Alicecom
nav: Providers
network: true
overview: 'Alicecom is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Alicecom''s developer surface includes documentation and 6 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.5
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 5.3
  previous_composite: 0.3
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Alicecom Domain Security
  slug: alicecom-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: alicecom
tags:
- Company
website: https://aliceapp.com
---
