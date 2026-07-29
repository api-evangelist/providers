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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST Admin API (and GraphQL Admin API) for building apps, themes, and payment gateways on ShopBase — products, orders, transactions, fulfillments, customers, inventory, checkouts, shipping, price rule
  name: ShopBase Admin API
  slug: shopbase-admin-api
artifact_total: 6
asyncapis:
- description: ''
  name: Beeketing Webhooks
  slug: beeketing-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://opencommercegroup.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.shopbase.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.shopbase.com
- group: docs
  title: ''
  type: APIReference
  url: https://api-doc.shopbase.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.shopbase.com/build-an-app/making-your-first-request.md
- group: operate
  title: ''
  type: Support
  url: https://help.shopbase.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.shopbase.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/beeketing
- group: commercial
  title: ''
  type: Pricing
  url: https://www.shopbase.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://accounts.shopbase.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://accounts.shopbase.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.shopbase.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.shopbase.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.shopbasestatus.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/beeketing-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/beeketing-scopes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/beeketing-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/beeketing-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/beeketing-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/beeketing-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/beeketing-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/beeketing-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/beeketing-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/beeketing-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beeketing-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/beeketing-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beeketing-llms.txt
created: '2026-07-17'
description: 'Beeketing began as a Vietnam-founded e-commerce marketing startup (backed by 500 Global) that built conversion-optimization apps for Shopify and other online stores, and evolved into OpenCommerce Group — the operator of ShopBase, a cross-border commerce platform serving 100,000+ merchants across 195 countries alongside PrintBase and PlusBase. The developer surface is the ShopBase Developer Platform: a Shopify-style REST Admin API (plus a GraphQL Admin API) for building public and private apps, themes, and payment gateways. It is secured with OAuth 2.0 authorization-code flow (public apps) or HTTP Basic auth (private apps), scoped with granular access scopes, and supports webhooks, leaky-bucket rate limiting, an app/theme store, and a Storefront SDK.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/beeketing.png
layout: provider
modified: '2026-07-18'
name: Beeketing
nav: Providers
network: true
overview: 'Beeketing publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-commerce, Cross-border Commerce, Marketing, and Shopify Apps.


  The Beeketing catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Beeketing''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 51
rate_limits:
- limit_count: 0
  name: Beeketing Rate Limits
  slug: beeketing-rate-limits
scopes:
- name: Beeketing Scopes
  scope_count: 24
  slug: beeketing-scopes
  summary_line: 24 scopes · authorizationCode
score:
  band: developing
  composite: 48.6
  delta: 3.7
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 58.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 28.9
  previous_composite: 44.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beeketing/refs/heads/main/screenshots/beeketing-2026-07-25T202630.png
security:
- kind: authentication
  name: Beeketing Authentication
  slug: beeketing-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Beeketing Domain Security
  slug: beeketing-domain-security
  summary_line: TLSv1.3 · DMARC
slug: beeketing
tags:
- Company
- E-commerce
- Cross-border Commerce
- Marketing
- Shopify Apps
- REST API
- OAuth
- Webhooks
- Themes
- Payments
website: https://opencommercegroup.com
---
