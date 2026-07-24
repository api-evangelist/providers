---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: REST API for managing cross-channel advertising campaigns including advertisers, insertion orders, line items, packages, creatives, and ads across programmatic channels. Authentication uses OAuth2 cli
  name: Amobee Campaign API
  slug: amobee-campaign-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amobee-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amobee-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/amobee/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/amobee/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/amobee/refs/heads/main/finops/finops.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amobee.com/trust/master-service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amobee.com/trust/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://www.amobee.com/
- group: company
  title: ''
  type: Blog
  url: https://www.amobee.com/blog/
- group: start
  title: ''
  type: Login
  url: https://login.amobee.com/
created: '2026-06-13'
description: Amobee (now Nexxen) is a digital advertising platform offering REST APIs for managing cross-channel programmatic campaigns, audience targeting, data management, and advertising analytics. The platform enables advertisers and agencies to plan, activate, and measure media across display, video, mobile, social, and TV channels through a unified DSP.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amobee.png
layout: provider
modified: '2026-06-13'
name: Amobee
nav: Providers
network: true
overview: 'Amobee publishes 1 API on the [APIs.io](https://apis.io/) network: Campaign API. Tagged areas include Digital Advertising, DSP, Programmatic, Campaign Management, and Audience Targeting.


  Amobee''s developer surface includes engineering blog and 9 more developer resources.'
plans:
- name: Plans
  plan_count: 2
  slug: plans
random_paper: 5
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 31.8
  delta: 0.0
  facets:
    commercial_clarity: 63.2
    contract_quality: 37.7
    developer_ergonomics: 2.2
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 31.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amobee/refs/heads/main/screenshots/amobee-2026-06-20T171938.png
security:
- kind: domain-security
  name: Amobee Domain Security
  slug: amobee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amobee Vulnerability Disclosure
  slug: amobee-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: amobee
tags:
- Digital Advertising
- DSP
- Programmatic
- Campaign Management
- Audience Targeting
- Data Management Platform
- Ad Tech
- Samsung Ads
website: https://www.amobee.com/
---
