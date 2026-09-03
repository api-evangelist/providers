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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The SendOwl REST API provides third-party applications access to a merchant account's products, bundles (packages), subscriptions, drip items, orders, discounts, discount codes and license keys. Reque
  name: SendOwl API
  slug: sendowl-api
artifact_total: 6
asyncapis:
- description: ''
  name: Sendowl Webhooks
  slug: sendowl-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sendowl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sendowl.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.sendowl.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://help.sendowl.com/help
- group: docs
  title: ''
  type: APIReference
  url: https://dashboard.sendowl.com/developers/api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sendowl.com/help/developer-overview-custom-integrations
- group: operate
  title: ''
  type: Support
  url: https://help.sendowl.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.sendowl.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SendOwl
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sendowl.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.sendowl.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sendowl.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sendowl.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://sendowl.status.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/sendowl-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sendowl-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sendowl-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sendowl-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sendowl-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sendowl-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sendowl-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/sendowl-packages.yml
- group: design
  title: ''
  type: Components
  url: components/sendowl-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sendowl-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sendowl-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sendowl-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sendowl-llms.txt
created: '2026-08-12'
description: SendOwl is a UK-based digital commerce platform that lets creators and small businesses sell digital products, subscriptions, memberships, license keys, drip-delivered courses and physical goods, with hosted checkout, automated file delivery, PDF stamping, affiliate programs, discount codes and EU VAT handling. It exposes a public REST API at api.sendowl.com covering products, bundles (packages), subscriptions, drip items, orders, discounts and licenses in both JSON and XML, authenticated with HTTP Basic using an account API key and secret, alongside an outbound webhook surface signed with HMAC-SHA256 and a browser-side sendowl.js library that drives the lightbox checkout and cart widget.
image: https://www.sendowl.com/twitter-image.png
layout: provider
modified: '2026-08-12'
name: SendOwl
nav: Providers
network: true
overview: 'SendOwl publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Digital Products, Payments, and Subscription.


  The SendOwl catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SendOwl''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
plans:
- name: Sendowl Plans Pricing
  plan_count: 4
  slug: sendowl-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 1
  name: Sendowl Rate Limits
  slug: sendowl-rate-limits
score:
  band: strong
  composite: 54.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 64.3
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 47.4
  previous_composite: 54.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sendowl/refs/heads/main/screenshots/sendowl-2026-08-17T081759.png
security:
- kind: authentication
  name: Sendowl Authentication
  slug: sendowl-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sendowl Domain Security
  slug: sendowl-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sendowl
tags:
- Company
- E-Commerce
- Digital Products
- Payments
- Subscription
- Checkout
- Memberships
- Licensing
- Creator Economy
- Webhook
website: https://sendowl.com/
---
