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
  scored_at: '2026-09-23'
api_count: 0
artifact_total: 1
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aivco/refs/heads/main/security/aivco-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aivco-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aivco.brookfield.com
coverage:
  checked: 2026-09-21
  detail: Access to the dashboard redirects to a Microsoft Azure AD login page, blocking API discovery.
  evidence:
  - status: 200
    url: https://aivco.brookfield.com
  reason: partner-login
  state: gated
created: '2026-09-21'
description: Aivco is a subsidiary or business unit within Brookfield, operating under the domain aivco.brookfield.com. Public information about Aivco is limited, with the site requiring authentication, suggesting internal or partner‑only access. The company appears in Brookfield’s portfolio listings but lacks a dedicated public-facing website or API documentation at this time.
layout: provider
modified: '2026-09-21'
name: Aivco
nav: Providers
network: true
overview: Aivco is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Asset Management, Infrastructure, and Energy.
random_paper: 2
score:
  band: minimal
  composite: 2.9
  coverage:
    artifact_dirs: 2
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    operational_transparency: 0.0
  previous_composite: 2.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aivco Domain Security
  slug: aivco-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aivco
tags:
- Company
- Finance
- Asset Management
- Infrastructure
- Energy
website: https://aivco.brookfield.com
---
