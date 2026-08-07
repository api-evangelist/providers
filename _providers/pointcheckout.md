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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.6
  scored_at: '2026-08-06'
api_count: 4
apis:
- description: API endpoints for branch management.
  name: PointCheckout Branches API
  slug: pointcheckout-branches-api
- description: API endpoints for checkout management.
  name: PointCheckout Checkout API
  slug: pointcheckout-checkout-api
- description: API endpoints for Customer subscription management.
  name: PointCheckout Customer subscription API
  slug: pointcheckout-customer-subscription-api
- description: API endpoints for webhook management.
  name: PointCheckout Webhooks API
  slug: pointcheckout-webhooks-api
artifact_total: 9
asyncapis:
- description: ''
  name: Pointcheckout Webhooks
  slug: pointcheckout-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pointcheckout-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pointcheckout-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/pointcheckout-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pointcheckout-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pointcheckout-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pointcheckout-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pointcheckout-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pointcheckout-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pointcheckout-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pointcheckout-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/pointcheckout-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pointcheckout-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pointcheckout-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/pointcheckout-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pointcheckout-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pointcheckout-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pointcheckout.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pointcheckout.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pointcheckout.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pointcheckout.com/docs/
- group: start
  title: ''
  type: Quickstart
  url: https://docs.pointcheckout.com/developer
- group: operate
  title: ''
  type: Support
  url: https://www.pointcheckout.com/en/home/contact
- group: company
  title: ''
  type: Blog
  url: https://www.pointcheckout.com/en/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pointcheckout
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pointcheckout.com/legal/merchant/merchant-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pointcheckout.com/legal/privacy/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://pointcheckout.com
created: '2026-07-17'
description: PointCheckout is a MENA-region payments and rewards platform, backed by 500 Global, that lets shoppers pay online with reward points and miles and lets merchants accept card and rewards payments. Its developer-facing Merchant API (powered by paymennt.com) exposes hosted web, payment-link, QR, and mobile checkouts, recurring subscriptions, merchant branches, and HMAC-signed webhooks. The API is RESTful JSON, versioned in the URI path (v2.0), secured with an API key and secret header pair, and ships with a separate test environment plus iOS/Android SDKs and e-commerce plugins for Magento 2, WooCommerce, OpenCart, and Shopify.
image: https://docs.pointcheckout.com/img/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: pointcheckout-mcp.yml
  slug: pointcheckout-mcpyml
modified: '2026-07-20'
name: PointCheckout
nav: Providers
network: true
overview: 'PointCheckout publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Branches API, Checkout API, Customer subscription API, and 1 more. Tagged areas include Company, Payments, Checkout, Subscriptions, and Rewards.


  The PointCheckout catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PointCheckout''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, quickstart, support, and 21 more developer resources.'
random_paper: 52
score:
  band: developing
  composite: 52.8
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 68.2
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 13.2
  previous_composite: 52.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 59.4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Pointcheckout Authentication
  slug: pointcheckout-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Pointcheckout Domain Security
  slug: pointcheckout-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Pointcheckout Trust Center
  slug: pointcheckout-trust-center
  summary_line: PCI DSS
slug: pointcheckout
tags:
- Company
- Payments
- Checkout
- Subscriptions
- Rewards
- Loyalty
- Webhooks
- MENA
- E-Commerce
website: https://pointcheckout.com
---
