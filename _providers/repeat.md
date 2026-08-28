---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://getrepeat.io/product/pricing
  - https://apps.shopify.com/repeat
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 4
asyncapis:
- description: ''
  name: Repeat Integration Events
  slug: repeat-integration-events
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/repeat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getrepeat.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getrepeat.io/en
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.getrepeat.io/en
- group: operate
  title: ''
  type: Support
  url: https://docs.getrepeat.io/en/
- group: commercial
  title: ''
  type: Pricing
  url: https://getrepeat.io/product/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/repeat-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/repeat-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/repeat-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/repeat-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/repeat-components.yml
- group: start
  title: ''
  type: Demo
  url: https://stamped.io/request-demo
- group: company
  title: ''
  type: Newsletter
  url: https://repeat.substack.com/
- group: company
  title: ''
  type: Blog
  url: https://website.stamped.io/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://getrepeat.io/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://getrepeat.io/legal/privacy-policy
created: '2026-07-17'
description: 'Repeat is a lifecycle and retention marketing platform for consumer packaged goods (CPG) and e-commerce brands, now operated as a product of Stamped. It connects to a brand''s Shopify store to ingest historical and incoming orders, predicts replenishment and reorder "Moments" for each customer, and automates personalized post-purchase campaigns across email, SMS, and direct mail. Repeat surfaces product predictions as reusable components inside Klaviyo, Postscript, and Attentive flows, and generates events that enrich customer profiles for segmentation and personalization. Founded in 2018 in Venice, California by Kim Stiefel and Sarah Wissel and backed by Battery Ventures and Techstars, Repeat is documented through a customer-facing Help Center rather than a public developer API or portal. It publishes no OpenAPI, GraphQL schema or developer console, but it does document a real integration surface in detail: five named lifecycle "Moment" events with typed payloads, a set of
  customer profile properties written into Klaviyo, and a parameterized hosted Personalized Cart URL that carries the reorder experience into email, SMS and printed QR codes.'
image: https://assets.super.so/18f07db5-d58c-4144-a891-0df945119dae/uploads/cover/d2af8d52-6fe3-4645-bfb2-364ede5549e8.png
layout: provider
modified: '2026-08-13'
name: Repeat
nav: Providers
network: true
overview: 'Repeat is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Lifecycle Marketing, Retention, and E-Commerce.


  The Repeat catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Repeat''s developer surface includes documentation, support, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Repeat Plans Pricing
  plan_count: 2
  slug: repeat-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Repeat Rate Limits
  slug: repeat-rate-limits
score:
  band: thin
  composite: 30.3
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 42.7
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 30.3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Repeat Domain Security
  slug: repeat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: repeat
tags:
- Company
- Marketing
- Lifecycle Marketing
- Retention
- E-Commerce
- Customer Data
- Shopify
- CPG
website: https://getrepeat.io/
---
