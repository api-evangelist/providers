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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-07-28'
api_count: 4
apis:
- description: The Availability API from Klook — 2 operation(s) for availability.
  name: Klook Availability API
  slug: klook-availability-api
- description: The Bookings API from Klook — 5 operation(s) for bookings.
  name: Klook Bookings API
  slug: klook-bookings-api
- description: The Products API from Klook — 2 operation(s) for products.
  name: Klook Products API
  slug: klook-products-api
- description: The Supplier API from Klook — 1 operation(s) for supplier.
  name: Klook Supplier API
  slug: klook-supplier-api
artifact_total: 8
asyncapis:
- description: ''
  name: Klook Notifications Webhooks
  slug: klook-notifications-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.klook.com/en-US/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://klook.gitbook.io/openapi
- group: docs
  title: ''
  type: Documentation
  url: https://klook.gitbook.io/openapi
- group: docs
  title: ''
  type: APIReference
  url: https://klook.gitbook.io/openapi/getting-started/endpoint-and-capabilities.md
- group: start
  title: ''
  type: GettingStarted
  url: https://klook.gitbook.io/openapi/getting-started/integration-process.md
- group: company
  title: ''
  type: Partners
  url: https://www.klook.com/partner/
- group: other
  title: ''
  type: Affiliate
  url: https://affiliate.klook.com/home
- group: start
  title: ''
  type: MerchantPortal
  url: https://merchant.klook.com/
- group: start
  title: ''
  type: SignUp
  url: https://affiliate.klook.com/home
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.klook.com/conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.klook.com/en-US/policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.klook.com/en-US/cookiepolicy/
- group: operate
  title: ''
  type: Support
  url: https://www.klook.com/en-US/faq/
- group: company
  title: ''
  type: About
  url: https://www.klook.com/en-US/about/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/klook-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/klook-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/klook-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/klook-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/klook-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/klook-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/klook-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/klook-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/klook-octo-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/klook-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/klook-notifications-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/klook-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/klook-domain-security.yml
created: '2026-07-17'
description: 'Klook is a Hong Kong-headquartered travel and experiences booking platform for the "things to do" sector — attractions, tours and activities, theme parks, food and beverage, WiFi and SIM cards, and transportation passes. Klook publishes an Open API specification for merchants, suppliers, reservation systems and channel managers who want to distribute their inventory through Klook''s website, app and partner channels. The specification is an implementation of OCTO (Open Connectivity for Tours, Activities and Attractions), the open standard for the in-destination experiences industry: the supplier implements the OCTO core endpoints (Supplier, Products, Availability, Bookings) at their own host and Klook consumes them as the reseller, with optional Capabilities negotiated through the Octo-Capabilities header. Klook additionally runs an affiliate program and a merchant portal.'
image: https://res.klook.com/image/upload/klook_logo.png
layout: provider
mcp_servers:
- description: ''
  name: klook-mcp.yml
  slug: klook-mcpyml
modified: '2026-07-19'
name: Klook
nav: Providers
network: true
overview: 'Klook publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Availability API, Bookings API, Products API, and 1 more. Tagged areas include Company, Marketplaces, Travel, Tours and Activities, and Booking.


  The Klook catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Klook''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, changelog, and 21 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 47.8
  delta: -1.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 61.3
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 23.7
  previous_composite: 49.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Klook Authentication
  slug: klook-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Klook Domain Security
  slug: klook-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: klook
tags:
- Company
- Marketplaces
- Travel
- Tours and Activities
- Booking
- Experiences
- Distribution
- OCTO
- Hospitality
website: https://www.klook.com/en-US/
---
