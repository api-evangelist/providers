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
- description: Public health data APIs referenced from the developer portal.
  name: Folkhalsomyndigheten API
  slug: folkhalsomyndigheten-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/folkhalsomyndigheten/refs/heads/main/hosts/folkhalsomyndigheten-hosts.yml
  title: ''
  type: Hosts
  url: hosts/folkhalsomyndigheten-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/folkhalsomyndigheten/refs/heads/main/vendors/folkhalsomyndigheten-vendors.yml
  title: ''
  type: Vendors
  url: vendors/folkhalsomyndigheten-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.folkhalsomyndigheten.se/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/folkhalsomyndigheten/refs/heads/main/security/folkhalsomyndigheten-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/folkhalsomyndigheten-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.folkhalsomyndigheten.se/
coverage:
  checked: '2026-10-12'
  detail: Developer portal requires login and provides no public OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://portal.folkhalsomyndigheten.se/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Folkhalsomyndigheten (Public Health Agency of Sweden) is Sweden’s national public health agency, responsible for public health surveillance, disease prevention, health promotion, and providing evidence-based guidance. It publishes statistics, data, reports, and guidance for healthcare professionals and the public, and operates open data portals and APIs for health data access.
image: https://www.folkhalsomyndigheten.se/mainweb/dist/images/share.png
layout: provider
modified: '2026-10-12'
name: Folkhalsomyndigheten (Public Health Agency of Sweden)
nav: Providers
network: true
overview: Folkhalsomyndigheten (Public Health Agency of Sweden) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Government, Public Health, Sweden, and Data.
random_paper: 9
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 4
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
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Folkhalsomyndigheten Domain Security
  slug: folkhalsomyndigheten-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: folkhalsomyndigheten
tags:
- Company
- Government
- Public Health
- Sweden
- Data
website: https://www.folkhalsomyndigheten.se/
---
