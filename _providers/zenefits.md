---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API providing programmatic access to people, companies, locations, employments, compensation, time-off, paystubs, and journal data inside a Zenefits account. Authentication uses OAuth 2.0 with sc
  name: TriNet Zenefits REST API
  slug: rest-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zenefits-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zenefits
- group: company
  title: ''
  type: Website
  url: https://www.trinet.com/products/zenefits
- group: docs
  title: ''
  type: Documentation
  url: https://developers.zenefits.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zenefits.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://secure.zenefits.com/accounts/register
- group: operate
  title: ''
  type: Support
  url: https://help.zenefits.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.zenefits.com
- group: start
  title: ''
  type: TriNet API Portal
  url: https://apidocs.trinet.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trinet
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.zenefits.com/llms.txt
created: '2026-05-11'
description: TriNet Zenefits (formerly Zenefits) is an all-in-one cloud HR platform for small and medium-sized businesses, providing payroll, benefits administration, time and scheduling, hiring and onboarding, performance management, and compliance in a single system of record. Acquired by TriNet in 2022, the platform combines self-service HR software with optional advisory services. TriNet Zenefits exposes a REST API at https://api.zenefits.com for programmatic access to people, companies, employments, compensation, payroll, and time-off resources, secured via OAuth 2.0.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zenefits.png
layout: provider
modified: '2026-05-11'
name: TriNet Zenefits
nav: Providers
network: true
overview: 'TriNet Zenefits publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Human Resources, HRIS, Payroll, Benefits Administration, and Onboarding.


  TriNet Zenefits'' developer surface includes documentation, pricing, signup flow, support, and 7 more developer resources.'
random_paper: 52
score:
  band: emerging
  composite: 14.0
  delta: -2.4
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 16.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zenefits/refs/heads/main/screenshots/zenefits-2026-06-20T201818.png
security:
- kind: domain-security
  name: Zenefits Domain Security
  slug: zenefits-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zenefits
tags:
- Human Resources
- HRIS
- Payroll
- Benefits Administration
- Onboarding
- Time Tracking
website: https://www.trinet.com/products/zenefits
---
