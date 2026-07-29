---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Stay Ai Agentic Access
  operation_count: 23
  slug: stay-ai-agentic-access
  summary_line: 23 operations · 14 acting
api_count: 8
apis:
- description: The Account API from Stay AI — 1 operation(s) for account.
  name: Stay AI Account API
  slug: stay-ai-account-api
- description: The Catalog API from Stay AI — 2 operation(s) for catalog.
  name: Stay AI Catalog API
  slug: stay-ai-catalog-api
- description: The Customer Portal API from Stay AI — 1 operation(s) for customer portal.
  name: Stay AI Customer Portal API
  slug: stay-ai-customer-portal-api
- description: The Data Export API from Stay AI — 1 operation(s) for data export.
  name: Stay AI Data Export API
  slug: stay-ai-data-export-api
- description: The Orders API from Stay AI — 2 operation(s) for orders.
  name: Stay AI Orders API
  slug: stay-ai-orders-api
- description: The Selling Plans API from Stay AI — 2 operation(s) for selling plans.
  name: Stay AI Selling Plans API
  slug: stay-ai-selling-plans-api
- description: The Subscriptions API from Stay AI — 9 operation(s) for subscriptions.
  name: Stay AI Subscriptions API
  slug: stay-ai-subscriptions-api
- description: The Webhooks API from Stay AI — 2 operation(s) for webhooks.
  name: Stay AI Webhooks API
  slug: stay-ai-webhooks-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/stay-ai-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/stay-ai-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stay-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stay-ai-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stayai
- group: company
  title: ''
  type: Website
  url: https://stay.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stay.ai
- group: start
  title: ''
  type: SignUp
  url: https://apps.shopify.com/stayai-subscriptions
- group: commercial
  title: ''
  type: Plans
  url: plans/stay-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stay-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/stay-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://stay.ai/blog
created: '2026-07-10'
description: Stay AI (formerly Retextion) is a subscription retention and growth platform for Shopify direct-to-consumer brands. It pairs a no-code customer portal with an ExperienceEngine for personalized promotions and upsells and a RetentionEngine for AI-driven churn prevention. Stay AI exposes a documented public REST API (base https://api.retextion.com/api/v2) authenticated with an X-RETEXTION-ACCESS-TOKEN header, covering subscriptions, recurring orders, selling plan groups, product catalog, the customer portal, account settings, bulk data export, and JWT-signed outbound webhooks.
finops:
- name: Stay Ai Finops
  service_category: Ecommerce and Retail
  slug: stay-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stay-ai.png
layout: provider
modified: '2026-07-10'
name: Stay AI
nav: Providers
network: true
overview: 'Stay AI publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, Catalog API, Customer Portal API, and 5 more. Tagged areas include Subscriptions, Retention, Churn, Shopify, and Ecommerce.


  Stay AI''s developer surface includes authentication, documentation, signup flow, engineering blog, and 8 more developer resources.'
plans:
- name: Stay Ai Plans Pricing
  plan_count: 2
  slug: stay-ai-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 3
  name: Stay Ai Rate Limits
  slug: stay-ai-rate-limits
score:
  band: thin
  composite: 39.5
  delta: -2.1
  facets:
    commercial_clarity: 50.0
    contract_quality: 54.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Stay Ai Authentication
  slug: stay-ai-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Stay Ai Domain Security
  slug: stay-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Stay Ai Trust Center
  slug: stay-ai-trust-center
  summary_line: SOC 2
slug: stay-ai
tags:
- Subscriptions
- Retention
- Churn
- Shopify
- Ecommerce
- DTC
website: https://stay.ai
---
