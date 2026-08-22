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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meundies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://meundies.com
created: '2026-07-17'
description: 'MeUndies is a direct-to-consumer apparel brand based in Los Angeles, selling underwear, loungewear, socks, and basics online through a subscription membership and one-time purchase model. It operates as an e-commerce retailer at meundies.com rather than a developer platform: an enrichment pass on 2026-07-20 probed the domain and found no public API surface (api.meundies.com and developer.meundies.com both return 404, and no /.well-known/, /llms.txt, or OpenAPI documents were discoverable). This profile was surfaced as a 500 Global portfolio company and carries the domain-security probe result; it will gain API artifacts only if MeUndies publishes a developer program.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/meundies.png
layout: provider
modified: '2026-07-20'
name: MeUndies
nav: Providers
network: true
overview: MeUndies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Apparel, and Direct-to-Consumer.
random_paper: 18
score:
  band: minimal
  composite: 5.0
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
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Meundies Domain Security
  slug: meundies-domain-security
  summary_line: TLSv1.3 · DMARC
slug: meundies
tags:
- Company
- E-Commerce
- Retail
- Apparel
- Direct-to-Consumer
- Subscription
- Consumer Products
website: https://meundies.com
---
