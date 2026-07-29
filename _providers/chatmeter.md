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
- description: REST API for accessing and administrating all Chatmeter platform data including location listings, review management, social monitoring, surveys, and user administration. Uses JSON Web Token (JWT) aut
  name: Chatmeter API
  slug: chatmeter-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chatmeter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.chatmeter.com
- group: docs
  title: ''
  type: Documentation
  url: https://support.chatmeter.com/hc/en-us/categories/4465860037275-Chatmeter-API
- group: company
  title: ''
  type: Blog
  url: https://www.chatmeter.com/category/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.chatmeter.com/pricing/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chatmeter
- group: other
  title: ''
  type: X
  url: https://x.com/chatmeter
- group: commercial
  title: ''
  type: Plans
  url: plans/chatmeter-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chatmeter-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chatmeter-finops.yml
created: '2026-06-13'
description: Chatmeter is an AI-powered multi-location intelligence platform offering a REST API for managing business listings, monitoring and responding to reviews, tracking social mentions, running surveys, and benchmarking competitive performance across locations.
finops:
- name: Chatmeter Finops
  service_category: ''
  slug: chatmeter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chatmeter.png
jsonld:
- class_count: 0
  name: Chatmeter Context
  property_count: 0
  slug: chatmeter-context
layout: provider
modified: '2026-06-13'
name: Chatmeter
nav: Providers
network: true
overview: 'Chatmeter publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Reputation Management, Local SEO, Listings Management, Review Management, and Social Media.


  The Chatmeter catalog on APIs.io includes 1 JSON-LD context.


  Chatmeter''s developer surface includes documentation, engineering blog, pricing, and 7 more developer resources.'
plans:
- name: Chatmeter Plans Pricing
  plan_count: 3
  slug: chatmeter-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 0
  name: Chatmeter Rate Limits
  slug: chatmeter-rate-limits
score:
  band: emerging
  composite: 21.1
  delta: -2.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 8.1
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 23.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chatmeter/refs/heads/main/screenshots/chatmeter-2026-06-20T174238.png
security:
- kind: domain-security
  name: Chatmeter Domain Security
  slug: chatmeter-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: chatmeter
tags:
- Reputation Management
- Local SEO
- Listings Management
- Review Management
- Social Media
- Multi-Location
- Competitive Intelligence
website: https://www.chatmeter.com
---
