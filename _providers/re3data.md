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
- description: Programmatic access to repository records via the re3data API.
  name: re3data API
  slug: re3data-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/re3data/refs/heads/main/hosts/re3data-hosts.yml
  title: ''
  type: Hosts
  url: hosts/re3data-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.re3data.org/terms
- group: company
  title: ''
  type: Blog
  url: https://blog.re3data.org/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/re3data/refs/heads/main/security/re3data-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/re3data-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.re3data.org
coverage:
  checked: '2026-10-14'
  detail: OpenAPI spec not found at https://api.re3data.org/openapi.json (404)
  evidence:
  - status: 404
    url: https://api.re3data.org/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: re3data.org is a global registry of research data repositories, providing structured metadata and a searchable catalog of repositories across disciplines. It offers an API for programmatic access to repository records, supporting open science and data discovery. The platform also supplies documentation, schemas, and analytics to help researchers locate and reuse data assets worldwide.
layout: provider
modified: '2026-10-14'
name: re3data
nav: Providers
network: true
overview: 're3data is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Registry, Open Science, and Metadata.


  re3data''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Re3Data Domain Security
  slug: re3data-domain-security
  summary_line: TLSv1.3
slug: re3data
tags:
- Company
- Data
- Registry
- Open Science
- Metadata
- Research
website: https://www.re3data.org
---
