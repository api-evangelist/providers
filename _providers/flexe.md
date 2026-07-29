---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for managing warehouse programs, inventory, fulfillment orders, and supply chain operations across Flexe's distributed network of warehouse operators in North America. Supports integration vi
  name: Flexe API
  slug: flexe-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flexe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.flexe.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer-sandbox.flexe.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/flexe-inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flexe
- group: company
  title: ''
  type: Blog
  url: https://www.flexe.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.flexe.com/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://www.flexe.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/flexe
- group: commercial
  title: ''
  type: Plans
  url: plans/flexe-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flexe-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/flexe-finops.yml
created: '2026-06-13'
description: Flexe provides on-demand warehousing and logistics infrastructure for the world's leading retailers and brands. Its REST APIs enable integration with a network of 800+ warehouse operators across North America to manage warehouse programs, inventory, fulfillment orders, and supply chain flexibility across distributed fulfillment nodes via a single technology platform supporting API, EDI, and XML integrations.
finops:
- name: Flexe Finops
  service_category: ''
  slug: flexe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flexe.png
jsonld:
- class_count: 11
  name: Flexe Context
  property_count: 16
  slug: flexe-context
layout: provider
modified: '2026-06-13'
name: Flexe
nav: Providers
network: true
overview: 'Flexe publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Warehousing, Logistics, Fulfillment, Supply Chain, and Inventory.


  The Flexe catalog on APIs.io includes 1 JSON-LD context.


  Flexe''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Flexe Plans Pricing
  plan_count: 1
  slug: flexe-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 0
  name: Flexe Rate Limits
  slug: flexe-rate-limits
score:
  band: emerging
  composite: 24.1
  delta: -3.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 17.7
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 27.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flexe/refs/heads/main/screenshots/flexe-2026-06-20T181406.png
security:
- kind: domain-security
  name: Flexe Domain Security
  slug: flexe-domain-security
  summary_line: TLSv1.3 · DMARC
slug: flexe
tags:
- Warehousing
- Logistics
- Fulfillment
- Supply Chain
- Inventory
- On-Demand
website: https://www.flexe.com
---
