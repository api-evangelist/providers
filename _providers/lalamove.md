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
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 27.9
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: 'The Lalamove Delivery API (v3) is a REST API for on-demand and scheduled courier delivery. Partners request a quotation for a route of stops, place an order against that quotation, retrieve order and '
  name: Lalamove Delivery API
  slug: lalamove-delivery-api
artifact_total: 4
asyncapis:
- description: ''
  name: Lalamove Delivery Webhooks
  slug: lalamove-delivery-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://lalamove.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.lalamove.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.lalamove.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.lalamove.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.lalamove.com/
- group: start
  title: ''
  type: SignUp
  url: https://partnerportal.lalamove.com/
- group: operate
  title: ''
  type: Support
  url: mailto:partner.support@lalamove.com
- group: company
  title: ''
  type: Blog
  url: https://www.lalamove.com/en-hk/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lalamove
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lalamove.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lalamove.com/en-hk/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lalamove.com/en-hk/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/lalamove-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lalamove-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lalamove-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lalamove-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lalamove-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lalamove-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lalamove-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/lalamove-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lalamove-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lalamove-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lalamove-delivery-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lalamove-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lalamove-domain-security.yml
created: '2026-07-17'
description: Lalamove is a Hong Kong-founded on-demand logistics and same-day delivery platform operating across Asia and Latin America, matching businesses and consumers with a fleet of motorcycle, car, van and truck drivers. Its Delivery API (v3) lets partners programmatically request quotations, place and edit delivery orders, track assigned drivers in real time, add priority fees, and receive order lifecycle webhooks. The REST API is authenticated with HMAC SHA256 request signing, is segmented by market via a UN/LOCODE `Market` header, and is available in eleven markets including Hong Kong SAR, Singapore, Malaysia, Thailand, Philippines, Indonesia, Vietnam, Taiwan, Japan, Mexico and Brazil. Lalamove publishes a sandbox environment, a Node.js SDK, multi-language code examples, and a public status page.
image: https://avatars.githubusercontent.com/u/20277126?v=4
layout: provider
modified: '2026-07-19'
name: Lalamove
nav: Providers
network: true
overview: 'Lalamove publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, Logistics, Delivery, and Last Mile Delivery.


  The Lalamove catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lalamove''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 19 more developer resources.'
random_paper: 33
score:
  band: thin
  composite: 41.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 22.6
    developer_ergonomics: 71.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 41.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lalamove/refs/heads/main/screenshots/lalamove-2026-07-25T224438.png
security:
- kind: authentication
  name: Lalamove Authentication
  slug: lalamove-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Lalamove Domain Security
  slug: lalamove-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lalamove
tags:
- Company
- Technology
- Logistics
- Delivery
- Last Mile Delivery
- Courier
- Transportation
- On Demand
- Fleet
- Shipping
website: https://lalamove.com
---
