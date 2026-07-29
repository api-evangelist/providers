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
- description: The Reachdesk REST API enables programmatic triggering of gift campaigns and sending of physical gifts, branded merchandise, and digital rewards. Authenticated via API tokens generated in the Reachdes
  name: Reachdesk API
  slug: reachdesk-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reachdesk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.reachdesk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.reachdesk.com/hc/en-gb/categories/4404901379473-Integrations-API
- group: operate
  title: ''
  type: Support
  url: https://support.reachdesk.com/hc/en-gb
- group: company
  title: ''
  type: Blog
  url: https://www.reachdesk.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.reachdesk.com/pricing
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reachdesk
- group: other
  title: ''
  type: X
  url: https://x.com/ReachdeskHQ
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/reachdesk
- group: commercial
  title: ''
  type: Plans
  url: plans/reachdesk-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/reachdesk-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/reachdesk-finops.yml
created: '2026-06-13'
description: Reachdesk is a global B2B corporate gifting and direct mail platform that enables sales, marketing, and customer success teams to send physical gifts, branded merchandise, and digital rewards at scale. The Reachdesk REST API allows programmatic triggering of gift campaigns, integration with CRM and marketing automation tools, and management of sending workflows across 180+ countries. API tokens are generated via the platform settings and used to authenticate requests for campaign triggering and gift delivery operations.
finops:
- name: Reachdesk Finops
  service_category: ''
  slug: reachdesk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reachdesk.png
jsonld:
- class_count: 10
  name: Reachdesk Context
  property_count: 24
  slug: reachdesk-context
layout: provider
modified: '2026-06-13'
name: Reachdesk
nav: Providers
network: true
overview: 'Reachdesk publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Corporate Gifting, Direct Mail, Swag, B2B, and Sales Enablement.


  The Reachdesk catalog on APIs.io includes 1 JSON-LD context.


  Reachdesk''s developer surface includes documentation, support, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Reachdesk Plans Pricing
  plan_count: 3
  slug: reachdesk-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Reachdesk Rate Limits
  slug: reachdesk-rate-limits
score:
  band: emerging
  composite: 25.0
  delta: -3.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 17.7
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 28.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reachdesk/refs/heads/main/screenshots/reachdesk-2026-06-20T192631.png
security:
- kind: domain-security
  name: Reachdesk Domain Security
  slug: reachdesk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reachdesk
tags:
- Corporate Gifting
- Direct Mail
- Swag
- B2B
- Sales Enablement
- Customer Success
- Marketing Automation
- Gifting Platform
- Rewards
website: https://www.reachdesk.com/
---
