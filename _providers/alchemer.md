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
- description: RESTful API v5 for managing surveys, responses, contacts, campaigns, and account resources within the Alchemer enterprise survey platform.
  name: Alchemer REST API
  slug: alchemer-rest-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alchemer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alchemer.com
- group: docs
  title: ''
  type: Documentation
  url: https://apihelp.alchemer.com/help
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.alchemer.com/help
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/apptentive
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alchemer
- group: company
  title: ''
  type: Blog
  url: https://www.alchemer.com/resources/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.alchemer.com/plans-pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://alchemer.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://twitter.com/AlchemerHQ
- group: commercial
  title: ''
  type: Plans
  url: plans/alchemer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/alchemer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/alchemer-finops.yml
created: '2026-06-13'
description: Enterprise survey and experience management platform with a REST API for managing surveys, accessing response data, managing contacts, and automating survey workflows. The Alchemer REST API v5 supports multi-region deployments across US, EU, Canada, and Australia, with API key and OAuth 1.0 authentication. API access is available exclusively on Business Platform accounts.
finops:
- name: Alchemer Finops
  service_category: ''
  slug: alchemer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alchemer.png
layout: provider
modified: '2026-06-13'
name: Alchemer
nav: Providers
network: true
overview: 'Alchemer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Survey, Experience Management, Feedback, Data Collection, and Enterprise.


  Alchemer''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Alchemer Plans Pricing
  plan_count: 4
  slug: alchemer-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 6
  name: Alchemer Rate Limits
  slug: alchemer-rate-limits
score:
  band: thin
  composite: 30.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 30.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alchemer/refs/heads/main/screenshots/alchemer-2026-06-20T171513.png
security:
- kind: domain-security
  name: Alchemer Domain Security
  slug: alchemer-domain-security
  summary_line: TLSv1.3 · DMARC
slug: alchemer
tags:
- Survey
- Experience Management
- Feedback
- Data Collection
- Enterprise
- Forms
website: https://www.alchemer.com
---
