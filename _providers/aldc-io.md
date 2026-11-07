---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
- description: Eclipse is the AI intelligence layer for business data, connecting tools and providing plain‑English insights.
  name: Eclipse API
  slug: eclipse-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/aldc-io/llms/aldc-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aldc-io-llms.txt
- group: other
  href: https://artifacts.apis.io/aldc-io/hosts/aldc-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aldc-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/aldc-io/vendors/aldc-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aldc-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.analyticlabs.io/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.analyticlabs.io/privacy.html
- group: auth
  href: https://artifacts.apis.io/aldc-io/security/aldc-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aldc-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://analyticlabs.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://eclipse.analyticlabs.io/
- group: docs
  title: ''
  type: Documentation
  url: https://eclipse.analyticlabs.io/
- group: docs
  title: ''
  type: APIReference
  url: https://eclipse.analyticlabs.io/
coverage:
  checked: '2026-11-01'
  detail: API documentation exists but requires login; no public OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts are accessible.
  evidence:
  - status: 307
    url: https://analyticlabs.io/openapi.json
  reason: auth-required
  state: gated
created: '2026-11-01'
description: AnalyticLabs delivers Eclipse, an AI-powered intelligence layer that enables businesses to connect their tools and data sources, ask natural language questions, and receive instant insights. The platform centralizes data, applies advanced machine learning models, and provides a unified interface for analytics, reporting, and decision-making across the enterprise. By integrating with popular SaaS applications, databases, and custom data pipelines, Eclipse helps organizations unlock value from their data without extensive engineering effort.
image: https://analyticlabs.io/eclipse-share.png
layout: provider
modified: '2026-11-01'
name: AnalyticLabs
nav: Providers
network: true
overview: 'AnalyticLabs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Analytics, Data, Business Intelligence, and Platform.


  AnalyticLabs'' developer surface includes documentation, API reference, and 8 more developer resources.'
plans:
- name: Aldc Io Plans Pricing
  plan_count: 0
  slug: aldc-io-plans-pricing
random_paper: 17
scopes:
- name: Aldc Io Scopes
  scope_count: 0
  slug: aldc-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 16.2
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aldc Io Authentication
  slug: aldc-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aldc Io Domain Security
  slug: aldc-io-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: aldc-io
tags:
- Artificial Intelligence
- Analytics
- Data
- Business Intelligence
- Platform
website: https://analyticlabs.io/
---
