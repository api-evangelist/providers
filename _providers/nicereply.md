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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: REST API for managing customer satisfaction surveys, retrieving ratings and comments, tracking CSAT, CES, and NPS scores, and managing users, teams, and customers within the Nicereply platform.
  name: Nicereply API
  slug: nicereply-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nicereply-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nicereply.com
- group: docs
  title: ''
  type: Documentation
  url: https://cdn.nicereply.com/s/api/latest/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/nicereply
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nicereply
- group: company
  title: ''
  type: Blog
  url: https://www.nicereply.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.nicereply.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://stats.uptimerobot.com/M9lQEFqLDv
- group: other
  title: ''
  type: X
  url: https://twitter.com/nice_reply
- group: commercial
  title: ''
  type: Plans
  url: plans/nicereply-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nicereply-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nicereply-finops.yml
created: '2026-06-13'
description: Nicereply is a customer satisfaction and NPS survey platform providing a REST API for managing surveys, accessing ratings and comments, tracking CSAT, CES, and NPS scores, and integrating with helpdesks such as Zendesk, Front, and Helpscout.
finops:
- name: Nicereply Finops
  service_category: ''
  slug: nicereply-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nicereply.png
layout: provider
modified: '2026-06-13'
name: Nicereply
nav: Providers
network: true
overview: 'Nicereply publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Customer Satisfaction, CSAT, CES, NPS, and Surveys.


  Nicereply''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Nicereply Plans Pricing
  plan_count: 5
  slug: nicereply-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Nicereply Rate Limits
  slug: nicereply-rate-limits
score:
  band: emerging
  composite: 24.2
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 24.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nicereply/refs/heads/main/screenshots/nicereply-2026-06-20T190319.png
security:
- kind: domain-security
  name: Nicereply Domain Security
  slug: nicereply-domain-security
  summary_line: TLSv1.3 · DMARC
slug: nicereply
tags:
- Customer Satisfaction
- CSAT
- CES
- NPS
- Surveys
- Helpdesk
- Customer Experience
website: https://www.nicereply.com
---
