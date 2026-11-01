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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API reference for Nibbles PBC (no machine‑readable spec discovered).
  name: Nibbles API
  slug: nibbles-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/nibbl-es/hosts/nibbl-es-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nibbl-es-hosts.yml
- group: other
  href: https://artifacts.apis.io/nibbl-es/vendors/nibbl-es-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nibbl-es-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nibbles.com/terms-of-use/
- group: auth
  href: https://artifacts.apis.io/nibbl-es/security/nibbl-es-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nibbl-es-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nibbles.com
coverage:
  checked: '2026-10-25'
  detail: Docs page returns HTML shell without a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://nibbles.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Nibbles PBC is a public benefit corporation offering a pet‑focused credit card that combines built‑in pet insurance, rewards on pet‑related purchases, and a streamlined claims process. The company aims to simplify pet ownership finances while providing financial incentives and protection for pet owners across the United States.
image: https://nibbles.com/images/nibbles/image/upload/q_auto,f_jpg,w_1200,h_630/production/raster/og-lockup
layout: provider
modified: '2026-10-25'
name: Nibbles PBC
nav: Providers
network: true
overview: Nibbles PBC is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, PetCare, CreditCard, and Insurance.
random_paper: 12
score:
  band: minimal
  composite: 6.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 8.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nibbl Es Domain Security
  slug: nibbl-es-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nibbl-es
tags:
- Company
- Finance
- PetCare
- CreditCard
- Insurance
- PBC
website: https://nibbles.com
---
