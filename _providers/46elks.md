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
- acting_count: 6
  human_in_the_loop: 0
  name: 46Elks Agentic Access
  operation_count: 15
  slug: 46elks-agentic-access
  summary_line: 15 operations · 6 acting
api_count: 5
apis:
- description: Make and receive programmable voice calls.
  name: 46elks Calls API
  slug: 46elks-calls-api
- description: Access recordings and MMS images.
  name: 46elks Media API
  slug: 46elks-media-api
- description: Send and receive picture messages.
  name: 46elks MMS API
  slug: 46elks-mms-api
- description: Allocate and manage virtual phone numbers.
  name: 46elks Numbers API
  slug: 46elks-numbers-api
- description: Send and receive text messages.
  name: 46elks SMS API
  slug: 46elks-sms-api
artifact_total: 12
collections:
- collection_type: open
  name: 46elks API
  slug: open-46elks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/46elks-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/46elks-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/46elks-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/46elks
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/46elks
- group: company
  title: ''
  type: Website
  url: https://46elks.com/
- group: docs
  title: ''
  type: Documentation
  url: https://46elks.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/46elks-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/46elks-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/46elks-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://46elks.com/blog
created: '2026-07-01'
description: 46elks is a Swedish communications platform as a service (CPaaS) offering a simple HTTP REST API for sending and receiving SMS and MMS, making and receiving voice calls with programmable call actions, provisioning virtual phone numbers, and handling media and recordings. The API uses HTTP Basic authentication with an API username and password, and is billed pay-as-you-go.
finops:
- name: 46Elks Finops
  service_category: Communications
  slug: 46elks-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/46elks.png
layout: provider
modified: '2026-07-01'
name: 46elks
nav: Providers
network: true
overview: '46elks publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Calls API, Media API, MMS API, and 2 more. Tagged areas include CPaaS, SMS, MMS, Voice, and Messaging.


  46elks'' developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: 46Elks Plans Pricing
  plan_count: 2
  slug: 46elks-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 4
  name: 46Elks Rate Limits
  slug: 46elks-rate-limits
score:
  band: thin
  composite: 34.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 51.7
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: 46Elks Authentication
  slug: 46elks-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: 46Elks Domain Security
  slug: 46elks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 46elks
tags:
- CPaaS
- SMS
- MMS
- Voice
- Messaging
- Phone Numbers
- Communications
website: https://46elks.com/
---
