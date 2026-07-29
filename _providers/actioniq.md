---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
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
api_count: 2
apis:
- description: 'The ActionIQ Profile API provides real-time access to customer identities, attributes, and audience membership within milliseconds. It powers inbound decisioning use cases such as web personalization '
  name: ActionIQ Profile API
  slug: profile-api
- description: ActionIQ provides a real-time REST API endpoint for streaming customer event data into the platform. The ingestion API supports push-based streaming from in-house systems, enabling businesses to captu
  name: ActionIQ Data Ingestion API
  slug: data-ingestion-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/actioniq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.actioniq.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.actioniq.com/library/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ActionIQ
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/actioniq
- group: company
  title: ''
  type: Blog
  url: https://www.actioniq.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.g2.com/products/actioniq/pricing
- group: other
  title: ''
  type: X
  url: https://twitter.com/actioniqinc
- group: commercial
  title: ''
  type: Plans
  url: plans/actioniq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/actioniq-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/actioniq-finops.yml
created: '2026-06-13'
description: ActionIQ is an enterprise customer data platform (CDP) that provides a REST API for managing customer profiles, building audiences, orchestrating campaigns, and activating data across marketing channels. The platform offers a Profile API for real-time personalization, enabling businesses to access customer identities, attributes, and audience membership within milliseconds to power web personalization, call center decisioning, and real-time customer experiences. ActionIQ was acquired by Uniphore in December 2024 and is now offered as part of Uniphore's composable CDP platform.
finops:
- name: Actioniq Finops
  service_category: ''
  slug: actioniq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/actioniq.png
jsonld:
- class_count: 0
  name: Actioniq Context
  property_count: 7
  slug: actioniq-context
layout: provider
modified: '2026-06-13'
name: ActionIQ
nav: Providers
network: true
overview: 'ActionIQ publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Customer Data Platform, CDP, Audience Management, Real-Time Personalization, and Marketing Orchestration.


  The ActionIQ catalog on APIs.io includes 1 JSON-LD context.


  ActionIQ''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Actioniq Plans Pricing
  plan_count: 1
  slug: actioniq-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Actioniq Rate Limits
  slug: actioniq-rate-limits
score:
  band: emerging
  composite: 19.6
  delta: -2.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 8.1
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 22.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/actioniq/refs/heads/main/screenshots/actioniq-2026-06-20T164035.png
security:
- kind: domain-security
  name: Actioniq Domain Security
  slug: actioniq-domain-security
  summary_line: TLSv1.3 · DMARC
slug: actioniq
tags:
- Customer Data Platform
- CDP
- Audience Management
- Real-Time Personalization
- Marketing Orchestration
- Data Activation
- Enterprise
- REST API
website: https://www.actioniq.com
---
