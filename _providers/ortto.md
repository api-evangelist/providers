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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Ortto Agentic Access
  operation_count: 11
  slug: ortto-agentic-access
  summary_line: 11 operations · 11 acting
api_count: 6
apis:
- description: Create, update, retrieve, and manage accounts (organizations).
  name: Ortto Accounts API
  slug: ortto-accounts-api
- description: Send custom activity events and manage activity definitions.
  name: Ortto Activities API
  slug: ortto-activities-api
- description: Retrieve campaigns, reports, and assets.
  name: Ortto Campaigns API
  slug: ortto-campaigns-api
- description: Create, update, retrieve, and manage people (contacts).
  name: Ortto People API
  slug: ortto-people-api
- description: Retrieve account tags.
  name: Ortto Tags API
  slug: ortto-tags-api
- description: Send transactional email and SMS.
  name: Ortto Transactional API
  slug: ortto-transactional-api
artifact_total: 14
collections:
- collection_type: open
  name: Ortto API
  slug: open-ortto
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ortto-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ortto-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ortto-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ortto-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/autopilot3
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ortto
- group: company
  title: ''
  type: Website
  url: https://ortto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ortto.com/developers/
- group: commercial
  title: ''
  type: Plans
  url: plans/ortto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ortto-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ortto-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://ortto.com/blog
created: '2026-06-25'
description: Ortto (formerly Autopilot) is a marketing automation, customer data platform (CDP), and analytics product. Its REST API at https://api.ap3api.com/v1 lets applications create and update people/contacts and accounts, send custom activity events, manage tags, retrieve campaign reports, and send transactional email and SMS, all authenticated with a custom API key via the X-Api-Key header.
finops:
- name: Ortto Finops
  service_category: Marketing and Customer Engagement
  slug: ortto-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ortto.png
layout: provider
modified: '2026-06-25'
name: Ortto
nav: Providers
network: true
overview: 'Ortto publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Activities API, Campaigns API, and 3 more. Tagged areas include Marketing Automation, CDP, Customer Data Platform, Analytics, and Email.


  Ortto''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Ortto Plans Pricing
  plan_count: 5
  slug: ortto-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 7
  name: Ortto Rate Limits
  slug: ortto-rate-limits
score:
  band: thin
  composite: 37.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.8
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Ortto Authentication
  slug: ortto-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ortto Domain Security
  slug: ortto-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Ortto Vulnerability Disclosure
  slug: ortto-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ortto
tags:
- Marketing Automation
- CDP
- Customer Data Platform
- Analytics
- Email
website: https://ortto.com/
---
