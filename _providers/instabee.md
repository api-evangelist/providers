---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 41.3
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Budbee's public REST API for e-commerce merchants and integration partners to create delivery orders, book home and locker delivery intervals, validate serviceable postal codes, discover parcel locker
  name: Budbee Delivery API
  slug: budbee-delivery-api
artifact_total: 6
asyncapis:
- description: ''
  name: Instabee Webhooks
  slug: instabee-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://instabee.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.budbee.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.budbee.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.budbee.com/
- group: company
  title: ''
  type: Blog
  url: https://press.instabee.com/
- group: company
  title: ''
  type: Careers
  url: https://career.instabee.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://instabee.com/legal/general-terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://instabee.com/legal/external-privacy-notice
- group: start
  title: ''
  type: Login
  url: https://partner.instabee.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/instabee-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/instabee-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/instabee-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/instabee-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/instabee-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/instabee-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/instabee-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/instabee-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/instabee-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instabee-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/instabee-llms.txt
created: '2026-07-17'
description: Instabee is a European last-mile logistics technology company formed by the 2022 merger of Instabox and Budbee, operating consumer delivery brands Instabox (Sweden, Denmark, Norway), Budbee (Sweden, Denmark, Finland, the Netherlands, Belgium) and Porterbuddy (Norway). It moves tens of millions of parcels a year across parcel lockers, home delivery and returns for 1,150+ merchant clients through 45+ parcel terminals, serving 10M+ active users. Instabee exposes a public REST developer API under the Budbee brand for creating and managing delivery orders, booking delivery intervals, discovering lockers/boxes and serviceable postal codes, generating shipping labels, booking returns, and subscribing to parcel-status webhooks across its Nordic and Benelux network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/instabee.png
layout: provider
mcp_servers:
- description: ''
  name: instabee-mcp.yml
  slug: instabee-mcpyml
modified: '2026-07-19'
name: Instabee
nav: Providers
network: true
overview: 'Instabee publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Logistics, Last-Mile Delivery, and Shipping.


  The Instabee catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Instabee''s developer surface includes documentation, API reference, engineering blog, authentication, sandbox, and 15 more developer resources.'
random_paper: 27
rate_limits:
- limit_count: 3
  name: Instabee Rate Limits
  slug: instabee-rate-limits
score:
  band: thin
  composite: 38.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 22.6
    developer_ergonomics: 52.2
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 38.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Instabee Authentication
  slug: instabee-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Instabee Domain Security
  slug: instabee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: instabee
tags:
- Company
- Retail
- Logistics
- Last-Mile Delivery
- Shipping
- E-commerce
- Parcel Lockers
- Returns
- Nordics
website: https://instabee.com/
---
