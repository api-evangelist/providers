---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-12'
api_count: 3
apis:
- description: Railinc's suite of APIs empowers customers to simplify and automate business processes essential to the lifecycle of freight rail operations, including equipment, shipment, asset health, and routing d
  name: Railinc API Portal
  slug: api-portal
- description: Asset Health API Portal enabling electronic transmission of damaged and defective car tracking data and equipment health information across rail industry partners.
  name: Railinc Asset Health API Portal
  slug: asset-health-api
- description: RIGIS Routing + Mileage provides both a User Interface and Application Programming Interface delivering authoritative North American railroad routing and mileage data updated quarterly.
  name: RIGIS Routing and Mileage API
  slug: rigis
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/railinc-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/railinc
- group: docs
  title: ''
  type: Documentation
  url: https://public.railinc.com/
- group: start
  title: ''
  type: Signup
  url: https://public.railinc.com/
- group: operate
  title: ''
  type: Support
  url: https://public.railinc.com/
created: '2026-03-16'
description: Railinc, a wholly owned subsidiary of the Association of American Railroads, delivers IT and information services to the North American freight rail industry. Railinc's suite of APIs empowers customers to simplify and automate business processes essential to the lifecycle of freight rail operations.
finops:
- name: Railinc Finops
  service_category: API
  slug: railinc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/railinc.png
layout: provider
modified: '2026-04-28'
name: Railinc
nav: Providers
network: true
overview: 'Railinc publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Rail, Freight, Logistics, Transportation, and Supply Chain.


  Railinc''s developer surface includes documentation, signup flow, support, and 2 more developer resources.'
plans:
- name: Railinc Plans Pricing
  plan_count: 3
  slug: railinc-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Railinc Rate Limits
  slug: railinc-rate-limits
score:
  band: emerging
  composite: 15.9
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 15.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/railinc/refs/heads/main/screenshots/railinc-2026-06-20T192531.png
security:
- kind: domain-security
  name: Railinc Domain Security
  slug: railinc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: railinc
tags:
- Rail
- Freight
- Logistics
- Transportation
- Supply Chain
---
