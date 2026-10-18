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
- description: Developer portal for Trygg-Hansa offering insurance related APIs (no public OpenAPI spec discovered).
  name: Trygg-Hansa API
  slug: trygg-hansa-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/trygg-hansa/refs/heads/main/hosts/trygg-hansa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/trygg-hansa-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/trygg-hansa/refs/heads/main/vendors/trygg-hansa-vendors.yml
  title: ''
  type: Vendors
  url: vendors/trygg-hansa-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.trygghansa.se/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/trygg-hansa/refs/heads/main/security/trygg-hansa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trygg-hansa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trygghansa.se/
coverage:
  checked: '2026-10-15'
  detail: Developer portal https://portal.trygghansa.se/ returns HTML with no OpenAPI or other machine-readable contract.
  evidence:
  - status: 302
    url: https://portal.trygghansa.se/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Trygg-Hansa is a Swedish insurance company offering a wide range of insurance products for individuals and businesses, including car, home, travel, health, and life insurance. The company focuses on providing reliable coverage and customer service, leveraging digital channels for policy management and claims handling. As part of the API Evangelist network, its digital presence includes a public website and customer portals, though detailed API specifications are not publicly documented at this time.
image: https://www.trygghansa.se/siteassets/bilder/sp/hero/other/fronthero_1920x400.jpg
layout: provider
modified: '2026-10-14'
name: Trygg-Hansa
nav: Providers
network: true
overview: Trygg-Hansa is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Sweden, Financial Services, and InsuranceTech.
random_paper: 3
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 5.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Trygg Hansa Domain Security
  slug: trygg-hansa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: trygg-hansa
tags:
- Company
- Insurance
- Sweden
- Financial Services
- InsuranceTech
website: https://trygghansa.se/
---
