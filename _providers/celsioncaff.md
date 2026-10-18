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
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/celsioncaff/refs/heads/main/hosts/celsioncaff-hosts.yml
  title: ''
  type: Hosts
  url: hosts/celsioncaff-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://celsion.de/news/
- group: other
  title: ''
  type: Leadership
  url: https://celsion.de/team/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/celsioncaff/refs/heads/main/security/celsioncaff-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/celsioncaff-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://celsion.de
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://celsion.de
  - status: 403
    url: https://equityzen.com/company/celsioncaff
  reason: no-developer-program
  state: none
created: '2026-10-07'
description: Celsioncaff, operating under the brand Celsion, provides fire protection systems and related services. The company offers a range of products for fire safety, including detection, alarm, and suppression solutions, targeting industrial and commercial markets across Europe. Their website presents detailed product information, company history, sustainability initiatives, and contact details, reflecting a mature enterprise in the fire protection sector.
layout: provider
modified: '2026-10-07'
name: Celsioncaff
nav: Providers
network: true
overview: Celsioncaff is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FireProtection, Safety, Europe, and Industrial.
random_paper: 5
score:
  band: minimal
  composite: 3.4
  coverage:
    artifact_dirs: 4
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
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Celsioncaff Domain Security
  slug: celsioncaff-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: celsioncaff
tags:
- Company
- FireProtection
- Safety
- Europe
- Industrial
website: https://celsion.de
---
