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
api_count: 1
apis:
- description: REST API for the Alyce corporate gifting platform enabling programmatic gift sending, recipient tracking, budget management, marketplace configuration, and CRM workflow automation. Supports integratio
  name: Alyce API
  slug: alyce-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alyce-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alyce.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.alyce.com/collection/357-integrations
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/alycecom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alyce-co
- group: company
  title: ''
  type: Blog
  url: https://www.alyce.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.alyce.com/product/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.alyce.com/
- group: other
  title: ''
  type: X
  url: https://x.com/alycegifts
- group: commercial
  title: ''
  type: Plans
  url: plans/alyce-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/alyce-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/alyce-finops.yml
created: '2026-06-13'
description: Alyce is an AI-powered corporate gifting platform that enables B2B sales, marketing, and customer success teams to send hyper-personalized gifts at scale. The platform provides a REST API for sending personalized gifts, tracking gift acceptance and engagement, managing budgets and marketplaces, and integrating with CRM and marketing automation tools including Salesforce, HubSpot, Marketo, Eloqua, Outreach, and Salesloft.
finops:
- name: Alyce Finops
  service_category: ''
  slug: alyce-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alyce.png
jsonld:
- class_count: 11
  name: Alyce Context
  property_count: 9
  slug: alyce-context
layout: provider
modified: '2026-06-13'
name: Alyce
nav: Providers
network: true
overview: 'Alyce publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Gifting, Corporate Gifting, B2B, Marketing Automation, and CRM Integration.


  The Alyce catalog on APIs.io includes 1 JSON-LD context.


  Alyce''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Alyce Plans Pricing
  plan_count: 3
  slug: alyce-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 4
  name: Alyce Rate Limits
  slug: alyce-rate-limits
score:
  band: thin
  composite: 37.2
  delta: -4.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 45.2
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 41.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Alyce Domain Security
  slug: alyce-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alyce
tags:
- Gifting
- Corporate Gifting
- B2B
- Marketing Automation
- CRM Integration
- Account-Based Marketing
- Sales Enablement
- AI
- Personalization
- Direct Mail
website: https://www.alyce.com/
---
