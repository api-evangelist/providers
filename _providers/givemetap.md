---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  schema_version: 0.2
  score: 10.8
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/givemetap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.givemetap.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/givemetap-well-known.yml
coverage:
  checked: '2026-08-04'
  detail: consumer physical-products e-commerce brand (Shopify storefront); no developer API surface
  migrated: true
  reason: not-a-software-company
  state: none
created: '2026-07-17'
description: GiveMeTap is a UK-based social-enterprise consumer brand that designs and sells reusable, BPA-free stainless-steel and insulated water bottles (500ml and 700ml, plus custom co-branded bottles for businesses). For every bottle sold, GiveMeTap funds five years of clean drinking water for a person in Ghana, giving 20% of its revenue to water projects in Africa; the company reports 116,391 people reached with clean water for life. It operates a direct-to-consumer e-commerce storefront on the Shopify platform. GiveMeTap is a physical-products company with no first-party developer API, developer portal, or public API documentation; it was surfaced as a Y Combinator portfolio lead and added to the API Evangelist network as a stub.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/givemetap.png
layout: provider
modified: '2026-07-19'
name: Givemetap
nav: Providers
network: true
overview: Givemetap is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Products, E-Commerce, Sustainability, and Social Enterprise.
random_paper: 17
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/givemetap/refs/heads/main/screenshots/givemetap-2026-08-07T165725.png
security:
- kind: domain-security
  name: Givemetap Domain Security
  slug: givemetap-domain-security
  summary_line: TLSv1.3 · HSTS
slug: givemetap
tags:
- Company
- Consumer Products
- E-Commerce
- Sustainability
- Social Enterprise
- Water
- Retail
website: https://www.givemetap.com/
---
