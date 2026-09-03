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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Account API from ThriveCart — 1 operation(s) for account.
  name: ThriveCart Account API
  slug: thrivecart-account-api
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Affiliates API from ThriveCart — 9 operation(s) for affiliates.
  name: ThriveCart Affiliates API
  slug: thrivecart-affiliates-api
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Bumps API from ThriveCart — 3 operation(s) for bumps.
  name: ThriveCart Bumps API
  slug: thrivecart-bumps-api
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Customers API from ThriveCart — 2 operation(s) for customers.
  name: ThriveCart Customers API
  slug: thrivecart-customers-api
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Downsells API from ThriveCart — 3 operation(s) for downsells.
  name: ThriveCart Downsells API
  slug: thrivecart-downsells-api
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Event subscriptions API from ThriveCart — 2 operation(s) for event subscriptions.
  name: ThriveCart Event subscriptions API
  slug: thrivecart-event-subscriptions-api
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Learn API from ThriveCart — 1 operation(s) for learn.
  name: ThriveCart Learn API
  slug: thrivecart-learn-api
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Products API from ThriveCart — 3 operation(s) for products.
  name: ThriveCart Products API
  slug: thrivecart-products-api
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Subscriptions API from ThriveCart — 4 operation(s) for subscriptions.
  name: ThriveCart Subscriptions API
  slug: thrivecart-subscriptions-api
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Transactions API from ThriveCart — 1 operation(s) for transactions.
  name: ThriveCart Transactions API
  slug: thrivecart-transactions-api
- baseURL: https://thrivecart.com/api/external
  baseurl_source: declared
  description: The Upsells API from ThriveCart — 3 operation(s) for upsells.
  name: ThriveCart Upsells API
  slug: thrivecart-upsells-api
artifact_total: 22
asyncapis:
- description: ThriveCart delivers account events to subscriber endpoints over HTTP POST. Two surfaces exist and they do not share event names. **Event Subscription API (this document).** Created programmatically wi
  name: ThriveCart Event Subscriptions
  slug: thrivecart-events-asyncapi
collections:
- collection_type: postman
  name: ThriveCart API
  slug: postman-thrivecart-api
- collection_type: open
  name: ThriveCart API
  slug: open-thrivecart-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/thrivecart-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/thrivecart-api-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/thrivecart-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/thrivecart-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://thrivecart.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.thrivecart.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.thrivecart.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.thrivecart.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.thrivecart.com/documentation/
- group: build
  title: ''
  type: Postman
  url: https://apidocs.thrivecart.com/
- group: operate
  title: ''
  type: Support
  url: https://support.thrivecart.com/
- group: company
  title: ''
  type: Blog
  url: https://thrivecart.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://thrivecart.com/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thrivecart
- group: operate
  title: ''
  type: Roadmap
  url: https://thrivecart.com/resources/roadmap/
- group: commercial
  title: ''
  type: Pricing
  url: https://thrivecart.com/products/proplus/
- group: start
  title: ''
  type: SignUp
  url: https://checkout.thrivecart.com/thrivecart-standard-monthly-plan/
- group: start
  title: ''
  type: Login
  url: https://thrivecart.com/signin/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thrivecart.com/legal/thrivecart/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thrivecart.com/legal/thrivecart/?tab=privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://thrivecart.statuspage.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://thrivecart.com/blog/category/product-updates/
- group: build
  title: ''
  type: Packages
  url: packages/thrivecart-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/thrivecart-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/thrivecart-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/thrivecart-security.txt
- group: auth
  title: ''
  type: Security
  url: security/thrivecart-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/thrivecart-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thrivecart-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/thrivecart-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/thrivecart-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/thrivecart-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/thrivecart-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/thrivecart-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/thrivecart-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/thrivecart-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/thrivecart-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/thrivecart-llms.txt
created: '2026-08-12'
description: ThriveCart is a hosted shopping cart, checkout and course platform for creators, coaches and digital-product sellers, operated by ThriveCart LLC. It sells one-time and recurring digital and physical products through customisable checkout pages with order bumps, one-click upsells and downsells, A/B testing, abandoned-cart recovery, sales-tax automation and a built-in affiliate centre, and bundles a learning-management product (ThriveCart Learn / ThriveCart Academy). Payments are processed through Stripe, PayPal, Authorize.net and ThrivePay Installments rather than by ThriveCart itself. The public ThriveCart API is a bearer-token REST surface at https://thrivecart.com/api/external covering products, bump offers, upsells, downsells, pricing options, transactions, customers, subscriptions, affiliates, Learn students and event subscriptions, with an account-wide webhook surface and a targeted Event Subscription API alongside it.
image: https://thrivecart.com/wp-content/uploads/2025/07/TC-logo-on-White.png
layout: provider
mcp_servers:
- description: ''
  name: ThriveCart MCP Server
  slug: thrivecart-mcp-server
modified: '2026-08-12'
name: ThriveCart
nav: Providers
network: true
overview: 'ThriveCart publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Account API, Affiliates API, Bumps API, and 8 more. Tagged areas include Company, Checkout, Shopping Cart, Payments, and E-Commerce.


  The ThriveCart catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ThriveCart''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Thrivecart Plans Pricing
  plan_count: 3
  slug: thrivecart-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 1
  name: Thrivecart Rate Limits
  slug: thrivecart-rate-limits
scopes:
- name: Thrivecart Scopes
  scope_count: 0
  slug: thrivecart-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 72.5
  coverage:
    artifact_dirs: 26
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 61.1
    developer_ergonomics: 72.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 78.9
  previous_composite: 72.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thrivecart/refs/heads/main/screenshots/thrivecart-2026-08-17T082349.png
security:
- kind: authentication
  name: Thrivecart Authentication
  slug: thrivecart-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Thrivecart Domain Security
  slug: thrivecart-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Thrivecart Vulnerability Disclosure
  slug: thrivecart-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Thrivecart Trust Center
  slug: thrivecart-trust-center
  summary_line: PCI DSS, GDPR, CCPA
slug: thrivecart
tags:
- Company
- Checkout
- Shopping Cart
- Payments
- E-Commerce
- Subscription
- Affiliate Marketing
- Learning Management
- Creator Economy
- Webhook
website: https://thrivecart.com/
---
