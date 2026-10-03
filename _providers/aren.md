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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aren/refs/heads/main/hosts/aren-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aren-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aren/refs/heads/main/vendors/aren-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aren-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aren/refs/heads/main/security/aren-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aren-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.getaren.com/
coverage:
  checked: 2026-09-26
  detail: Unable to resolve API host api.getaren.com to fetch OpenAPI spec
  evidence:
  - status: DNS resolution failed
    url: https://api.getaren.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: Aren provides AI‑powered recruiting guidance for high‑school athletes and their families. The platform offers tools such as ScoutLens video analysis, AI‑driven camp search, and personalized consulting to help navigate college recruiting, transfer portals, and NIL considerations. It aims to reduce uncertainty and cost for families by delivering data‑driven recommendations and educational resources.
layout: provider
modified: '2026-09-25'
name: Aren
nav: Providers
network: true
overview: Aren is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Recruiting, Education, and Sports.
random_paper: 4
score:
  band: minimal
  composite: 2.5
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
    discoverability: 44.6
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 5.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aren Domain Security
  slug: aren-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aren
tags:
- Company
- Artificial Intelligence
- Recruiting
- Education
- Sports
website: https://www.getaren.com/
---
