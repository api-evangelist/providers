---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API reference for AquaMania services
  name: AquaMania API
  slug: aquamania-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/aqmania-com/plans/aqmania-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aqmania-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/aqmania-com/llms/aqmania-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aqmania-com-llms.txt
- group: other
  href: https://artifacts.apis.io/aqmania-com/hosts/aqmania-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aqmania-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/aqmania-com/security/aqmania-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aqmania-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aqmania.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aqmania.com/about
- group: commercial
  title: ''
  type: Pricing
  url: https://aqmania.com/pricing
- group: operate
  title: ''
  type: Contact
  url: https://aqmania.com/contacts
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aqmania.com/privacy
coverage:
  checked: '2026-11-01'
  detail: No public API specification found despite probing known API endpoints.
  evidence:
  - status: 404
    url: https://aqmania.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AquaMania manufactures PVC furniture for pools and changing rooms, offering a configurator, pricing, and tender package tools for B2B customers. Based in Saint‑Petersburg since 2017, the company provides 9 years of experience, 162 SKUs, and 9 MCP tools for contractors, designers, and government orders.
layout: provider
modified: '2026-11-01'
name: AquaMania
nav: Providers
network: true
overview: 'AquaMania is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include B2B, Manufacturing, PVC, Pools, and Russia.


  AquaMania''s developer surface includes documentation, pricing, and 7 more developer resources.'
plans:
- name: Aqmania Com Plans Pricing
  plan_count: 1
  slug: aqmania-com-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 8.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 53.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - russia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 14.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aqmania Com Domain Security
  slug: aqmania-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aqmania-com
tags:
- B2B
- Manufacturing
- PVC
- Pools
- Russia
website: https://aqmania.com/
---
