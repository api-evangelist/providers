---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Product Fruits Agentic Access
  operation_count: 16
  slug: product-fruits-agentic-access
  summary_line: 16 operations · 13 acting
api_count: 4
apis:
- description: Custom event tracking
  name: Product Fruits Events API
  slug: product-fruits-events-api
- description: User feedback submission
  name: Product Fruits Feedback API
  slug: product-fruits-feedback-api
- description: Knowledge base article and category management
  name: Product Fruits Knowledge Base API
  slug: product-fruits-knowledge-base-api
- description: User identification and management
  name: Product Fruits Users API
  slug: product-fruits-users-api
artifact_total: 23
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/product-fruits-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/product-fruits-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/product-fruits-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://productfruits.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.productfruits.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/product-fruits
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/product-fruits
- group: company
  title: ''
  type: Blog
  url: https://productfruits.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://productfruits.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.productfruits.com
- group: other
  title: ''
  type: X
  url: https://x.com/productfruits
- group: commercial
  title: ''
  type: Plans
  url: plans/product-fruits-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/product-fruits-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/product-fruits-finops.yml
created: '2026-06-13'
description: Product Fruits is an AI-powered product adoption platform that enables SaaS teams to build in-app onboarding tours, checklists, tooltips, announcements, NPS surveys, and user segmentation without requiring developer resources. The platform offers a REST API and JavaScript API for programmatic control of onboarding flows, user identification, event tracking, knowledge base management, and feedback collection.
examples:
- key_count: 3
  name: Create Feedback
  slug: create-feedback
- key_count: 2
  name: Feedback Webhook Payload
  slug: feedback-webhook-payload
- key_count: 1
  name: Identify User
  slug: identify-user
- key_count: 1
  name: Import Articles
  slug: import-articles
- key_count: 2
  name: Survey Webhook Payload
  slug: survey-webhook-payload
- key_count: 2
  name: Track Event
  slug: track-event
finops:
- name: Product Fruits Finops
  service_category: ''
  slug: product-fruits-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/product-fruits.png
json_schemas:
- name: Feedback Webhook Payload
  property_count: 2
  slug: feedback-webhook-payload
- name: Identify User Request
  property_count: 1
  slug: identify-user-request
- name: Import Articles Request
  property_count: 1
  slug: import-articles-request
- name: Survey Webhook Payload
  property_count: 2
  slug: survey-webhook-payload
- name: Track Event Request
  property_count: 2
  slug: track-event-request
jsonld:
- class_count: 0
  name: Product Fruits Context
  property_count: 0
  slug: product-fruits
layout: provider
modified: '2026-06-13'
name: Product Fruits
nav: Providers
network: true
overview: 'Product Fruits publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Events API, Feedback API, Knowledge Base API, and 1 more. Tagged areas include Product Adoption, User Onboarding, In-App Guidance, Checklists, and NPS Surveys.


  The Product Fruits catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Product Fruits'' developer surface includes authentication, documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Product Fruits Plans Pricing
  plan_count: 4
  slug: product-fruits-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 0
  name: Product Fruits Rate Limits
  slug: product-fruits-rate-limits
rules:
- name: Product Fruits API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: product-fruits-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.5
  delta: -4.5
  facets:
    commercial_clarity: 50.0
    contract_quality: 68.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 53.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/product-fruits/refs/heads/main/screenshots/product-fruits-2026-06-20T192135.png
security:
- kind: authentication
  name: Product Fruits Authentication
  slug: product-fruits-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Product Fruits Domain Security
  slug: product-fruits-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: product-fruits
tags:
- Product Adoption
- User Onboarding
- In-App Guidance
- Checklists
- NPS Surveys
- Announcements
- User Segmentation
- SaaS
website: https://productfruits.com
---
