---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Matternet's proprietary cloud platform that receives customer delivery requests, generates routes, and commands, controls, and monitors all operating Matternet assets. A consistent internal Hasura-pow
  name: Matternet Cloud Software Platform
  slug: matternet-cloud-platform
- description: Operator-facing logistics surface for requesting deliveries and tracking payload chain-of-custody across hospital, laboratory, and pharmacy workflows. Matternet has referenced a secure medical drone d
  name: Matternet Logistics Integration
  slug: matternet-logistics-integration
artifact_total: 7
collections:
- collection_type: open
  name: Matternet Cloud Platform API
  slug: open-matternet
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/matternet-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/matternet-inc
- group: company
  title: ''
  type: Website
  url: https://www.matternet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.matternet.com/our-system
- group: commercial
  title: ''
  type: Plans
  url: plans/matternet-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/matternet-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/matternet-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.matternet.com/newsroom
- group: other
  title: ''
  type: ProductPage
  url: https://www.matternet.com/our-system-landing-station
created: '2026-06-20'
description: Matternet designs, builds, and operates autonomous urban drone-logistics networks for healthcare and on-demand delivery. The integrated system pairs the FAA type-certified M2 aircraft with the Matternet Station and a proprietary cloud Software Platform that routes, commands, and monitors flights. Telemetry streams from drones and stations to the cloud over an MQTT broker (HiveMQ) as protobuf messages, and a consistent internal Hasura-powered GraphQL data layer serves Matternet's operator and client applications. As of this profile, Matternet does not publish a public or self-serve developer API; integrations are delivered through partner and operator engagements.
finops:
- name: Matternet Finops
  service_category: Logistics and Delivery
  slug: matternet-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/matternet.png
layout: provider
modified: '2026-07-25'
name: Matternet
nav: Providers
network: true
overview: 'Matternet publishes 2 APIs on the [APIs.io](https://apis.io/) network: Cloud Software Platform and Logistics Integration. Tagged areas include Drone Delivery, Logistics, Healthcare, Autonomous, and UAS.


  Matternet''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Matternet Plans Pricing
  plan_count: 1
  slug: matternet-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 3
  name: Matternet Rate Limits
  slug: matternet-rate-limits
score:
  band: emerging
  composite: 23.3
  delta: -3.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 32.3
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 27.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/matternet/refs/heads/main/screenshots/matternet-2026-06-20T185042.png
security:
- kind: domain-security
  name: Matternet Domain Security
  slug: matternet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: matternet
tags:
- Drone Delivery
- Logistics
- Healthcare
- Autonomous
- UAS
- Telemetry
website: https://www.matternet.com/
---
