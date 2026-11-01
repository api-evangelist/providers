---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/exxpertapps/hosts/exxpertapps-hosts.yml
  title: ''
  type: Hosts
  url: hosts/exxpertapps-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.exxpertapps.com/Privacy.php
- group: auth
  href: https://artifacts.apis.io/exxpertapps/security/exxpertapps-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/exxpertapps-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://exxpertapps.com/
coverage:
  checked: '2026-10-20'
  detail: No machine‑readable API specification (OpenAPI/AsyncAPI/GraphQL) was found on the provider's site.
  evidence:
  - status: 200
    url: https://exxpertapps.com/
  - status: 404
    url: https://api.exxpertapps.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: ExxpertApps provides an integrated CRM, project management, and billing platform tailored for service‑based businesses. It connects sales, projects, and invoicing in a single system, supporting distributed teams, multiple languages, and multiple currencies. Designed for B2B consulting, engineering, and service firms, it aims to streamline operations and improve client relationships.
image: https://www.exxpertapps.com/LOGO_EXXPERTAPPS.png
layout: provider
modified: '2026-10-20'
name: Calvi Systems SL
nav: Providers
network: true
overview: Calvi Systems SL is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include CRM, Project Management, Billing, B2B Services, and Multi-Currency.
random_paper: 20
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Exxpertapps Domain Security
  slug: exxpertapps-domain-security
  summary_line: TLSv1.2 · DMARC
slug: exxpertapps
tags:
- CRM
- Project Management
- Billing
- B2B Services
- Multi-Currency
- ERP Integration
website: https://exxpertapps.com/
---
