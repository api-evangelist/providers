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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/tripod-glp-com/hosts/tripod-glp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tripod-glp-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/tripod-glp-com/security/tripod-glp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tripod-glp-com-domain-security.yml
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found at the provider’s API hosts.
  evidence:
  - status: 0
    url: https://api.tripod-glp.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Tripod GLP is a venture‑backed technology company focused on providing innovative global logistics platforms. The firm aims to streamline supply‑chain operations through cloud‑based services, data analytics, and integration with partner ecosystems. While currently a stub in the API Evangelist network, the company’s public presence suggests ongoing development of API offerings for partners and developers.
layout: provider
modified: '2026-10-29'
name: tripod-glp
nav: Providers
network: true
overview: tripod-glp is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Cloud, API, and Supply-Chain.
plans:
- name: Tripod Glp Com Plans Pricing
  plan_count: 0
  slug: tripod-glp-com-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Tripod Glp Com Rate Limits
  slug: tripod-glp-com-rate-limits
scopes:
- name: Tripod Glp Com Scopes
  scope_count: 0
  slug: tripod-glp-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 19
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
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Tripod Glp Com Authentication
  slug: tripod-glp-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Tripod Glp Com Domain Security
  slug: tripod-glp-com-domain-security
  summary_line: DMARC
slug: tripod-glp-com
tags:
- Company
- Logistics
- Cloud
- API
- Supply-Chain
---
