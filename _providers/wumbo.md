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
  href: https://raw.githubusercontent.com/api-evangelist/wumbo/refs/heads/main/hosts/wumbo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wumbo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/wumbo/refs/heads/main/vendors/wumbo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wumbo-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wumbo.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wumbo.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://wumbo.com/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/wumbo/refs/heads/main/security/wumbo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wumbo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wumbo.com
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found at the API host despite probing common spec endpoints.
  evidence:
  - status: 0
    url: https://api.wumbo.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Wumbo is a technology startup focused on delivering innovative data integration solutions for modern enterprises. Founded in 2023 and backed by Starting Line VC, the company builds a platform that simplifies the connection, transformation, and orchestration of APIs across diverse services. Wumbo aims to reduce integration complexity, accelerate time‑to‑market, and enable businesses to create flexible, scalable data pipelines without extensive custom code.
image: https://wumbo.com/static/meta-image-8c53aa787c30c491171251f1ca85ce25.jpg
layout: provider
modified: '2026-10-12'
name: Wumbo
nav: Providers
network: true
overview: Wumbo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 4
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 41.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Wumbo Domain Security
  slug: wumbo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wumbo
tags:
- Company
website: https://wumbo.com
---
