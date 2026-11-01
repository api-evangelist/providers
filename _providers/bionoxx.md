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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Bionoxx does not appear to expose a public developer API; the website provides company information and product descriptions only.
  name: Bionoxx API
  slug: bionoxx-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/bionoxx/vendors/bionoxx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bionoxx-vendors.yml
- group: other
  href: https://artifacts.apis.io/bionoxx/hosts/bionoxx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bionoxx-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://equityzen.com/company/bionoxx
- group: auth
  href: https://artifacts.apis.io/bionoxx/security/bionoxx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bionoxx-domain-security.yml
- group: other
  title: ''
  type: coverage
  url: http://bionoxx.com
created: '2026-09-28'
description: Bionoxx is a biotechnology company focused on developing innovative solutions in the field of molecular diagnostics and bioinformatics. The company aims to provide advanced data-driven tools for researchers and clinicians, leveraging cutting‑edge technologies to improve health outcomes. This stub was initially added to the API Evangelist network from secondary‑market sources and is being enriched through the full profiling pipeline.
layout: provider
modified: '2026-09-28'
name: Bionoxx
nav: Providers
network: true
overview: Bionoxx is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Molecular Diagnostics, Bioinformatics, and Health Tech.
random_paper: 7
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 4.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/bionoxx/bionoxx-2026-10-11T102324.png
security:
- kind: domain-security
  name: Bionoxx Domain Security
  slug: bionoxx-domain-security
  summary_line: no transport/DNS hardening detected
slug: bionoxx
tags:
- Company
- Biotechnology
- Molecular Diagnostics
- Bioinformatics
- Health Tech
website: https://equityzen.com/company/bionoxx
---
