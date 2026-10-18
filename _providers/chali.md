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
  href: https://raw.githubusercontent.com/api-evangelist/chali/refs/heads/main/hosts/chali-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chali-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.chali.com/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chali/refs/heads/main/security/chali-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chali-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chali.com
coverage:
  checked: '2026-10-08'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found on api.chali.com despite probing common spec paths.
  evidence:
  - status: 0
    url: https://api.chali.com/openapi.json
  - status: 0
    url: https://api.chali.com/swagger.json
  - status: 0
    url: https://api.chali.com/v1/openapi.json
  - status: 0
    url: https://api.chali.com/api-docs
  - status: 0
    url: https://api.chali.com/docs
  - status: 0
    url: https://api.chali.com/redoc
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Chali (广州茶里集团有限公司) is a Chinese high‑end tea brand and professional tea‑service provider founded in 2013 and headquartered in Guangzhou. It offers premium loose‑leaf, bagged and ready‑to‑drink teas, operates its own supply chain, R&D centre and tea academy, and serves hotels, airlines, banks and consumers worldwide, with over 20 million online customers.
layout: provider
modified: '2026-10-08'
name: Chali
nav: Providers
network: true
overview: Chali is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 7
score:
  band: minimal
  composite: 2.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 37.5
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Chali Domain Security
  slug: chali-domain-security
  summary_line: TLSv1.3
slug: chali
tags:
- Company
website: https://www.chali.com
---
