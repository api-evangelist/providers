---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    mcp_server: false
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Open GROW discovery, deterministic Arabic/English resolution, provider-aligned accountless non-effect invocation across Legal, Workforce, Business and Government services.
  name: SAASH Agent Connector
  slug: saash-agent-connector
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/saash-gateway/hosts/saash-gateway-hosts.yml
  title: ''
  type: Hosts
  url: hosts/saash-gateway-hosts.yml
- group: other
  href: https://artifacts.apis.io/saash-gateway/vendors/saash-gateway-vendors.yml
  title: ''
  type: Vendors
  url: vendors/saash-gateway-vendors.yml
- group: auth
  href: https://artifacts.apis.io/saash-gateway/security/saash-gateway-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/saash-gateway-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://saash-gateway.vercel.app
- group: docs
  title: ''
  type: APIReference
  url: https://saash-gateway.vercel.app/openapi.json
created: '2026-10-28'
description: SAASH provides a bilingual Saudi government, business, legal, and workforce service discovery platform. It offers a unified gateway for agents to access Saudi governmental services, business registration, legal compliance, and workforce management in both Arabic and English. The platform aggregates various official Saudi APIs, presenting them through a single interface while emphasizing privacy and non-execution of government functions.
layout: provider
modified: '2026-10-28'
name: SAASH
nav: Providers
network: true
overview: 'SAASH is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  SAASH''s developer surface includes API reference and 4 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 5.4
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/saash-gateway/saash-gateway-2026-11-03T142622.png
security:
- kind: domain-security
  name: Saash Gateway Domain Security
  slug: saash-gateway-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: saash-gateway
tags:
- Company
website: https://saash-gateway.vercel.app
---
