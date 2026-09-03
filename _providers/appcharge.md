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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 62.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 45
  human_in_the_loop: 0
  name: Appcharge Agentic Access
  operation_count: 63
  slug: appcharge-agentic-access
  summary_line: 63 operations · 45 acting
api_count: 1
apis:
- baseURL: https://api.appcharge.com
  baseurl_source: declared
  description: The Assets API from Appcharge — 2 operation(s) for assets.
  name: Appcharge Assets API
  slug: appcharge-assets-api
- baseURL: https://api.appcharge.com
  baseurl_source: declared
  description: The Authentication API from Appcharge — 2 operation(s) for authentication.
  name: Appcharge Authentication API
  slug: appcharge-authentication-api
- baseURL: https://api.appcharge.com
  baseurl_source: declared
  description: The Badges API from Appcharge — 2 operation(s) for badges.
  name: Appcharge Badges API
  slug: appcharge-badges-api
- baseURL: https://api.appcharge.com
  baseurl_source: declared
  description: The Coupons API from Appcharge — 2 operation(s) for coupons.
  name: Appcharge Coupons API
  slug: appcharge-coupons-api
- baseURL: https://api.appcharge.com
  baseurl_source: declared
  description: The General API from Appcharge — 9 operation(s) for general.
  name: Appcharge General API
  slug: appcharge-general-api
- baseURL: https://api.appcharge.com
  baseurl_source: declared
  description: The Localization API from Appcharge — 1 operation(s) for localization.
  name: Appcharge Localization API
  slug: appcharge-localization-api
- baseURL: https://api.appcharge.com
  baseurl_source: declared
  description: The Offer Designs API from Appcharge — 2 operation(s) for offer designs.
  name: Appcharge Offer Designs API
  slug: appcharge-offer-designs-api
- baseURL: https://api.appcharge.com
  baseurl_source: declared
  description: The Offers API from Appcharge — 5 operation(s) for offers.
  name: Appcharge Offers API
  slug: appcharge-offers-api
- baseURL: https://api.appcharge.com
  baseurl_source: declared
  description: The Orders API from Appcharge — 1 operation(s) for orders.
  name: Appcharge Orders API
  slug: appcharge-orders-api
- baseURL: https://api.appcharge.com
  baseurl_source: declared
  description: The Personalization API from Appcharge — 1 operation(s) for personalization.
  name: Appcharge Personalization API
  slug: appcharge-personalization-api
- baseURL: https://api.appcharge.com
  baseurl_source: declared
  description: The Popups API from Appcharge — 1 operation(s) for popups.
  name: Appcharge Popups API
  slug: appcharge-popups-api
- baseURL: https://api.appcharge.com
  baseurl_source: declared
  description: The Portal Content API from Appcharge — 4 operation(s) for portal content.
  name: Appcharge Portal Content API
  slug: appcharge-portal-content-api
- baseURL: https://api.appcharge.com
  baseurl_source: declared
  description: The Products API from Appcharge — 2 operation(s) for products.
  name: Appcharge Products API
  slug: appcharge-products-api
- baseURL: https://api.appcharge.com
  baseurl_source: declared
  description: The Promo Codes API from Appcharge — 3 operation(s) for promo codes.
  name: Appcharge Promo Codes API
  slug: appcharge-promo-codes-api
- baseURL: https://api.appcharge.com
  baseurl_source: declared
  description: The Rolling Offers API from Appcharge — 2 operation(s) for rolling offers.
  name: Appcharge Rolling Offers API
  slug: appcharge-rolling-offers-api
- baseURL: https://api.appcharge.com
  baseurl_source: declared
  description: The Store Refresh Popups API from Appcharge — 2 operation(s) for store refresh popups.
  name: Appcharge Store Refresh Popups API
  slug: appcharge-store-refresh-popups-api
- baseURL: https://api.appcharge.com
  baseurl_source: declared
  description: The Triggered Popups API from Appcharge — 2 operation(s) for triggered popups.
  name: Appcharge Triggered Popups API
  slug: appcharge-triggered-popups-api
artifact_total: 61
asyncapis:
- description: Appcharge sends real-time, structured webhook events (Events V2) to a publisher-registered HTTPS endpoint for order lifecycle, web store and game portal interactions, logins, and disputes. Each reques
  name: Appcharge Events (V2) Webhooks
  slug: appcharge-events-asyncapi
collections:
- collection_type: postman
  name: Appcharge Assets API
  slug: postman-appcharge-assets-api
- collection_type: postman
  name: Appcharge Assets Authentication API
  slug: postman-appcharge-authentication-api
- collection_type: postman
  name: Appcharge Assets Badges API
  slug: postman-appcharge-badges-api
- collection_type: postman
  name: Appcharge Assets Coupons API
  slug: postman-appcharge-coupons-api
- collection_type: postman
  name: Appcharge Assets General API
  slug: postman-appcharge-general-api
- collection_type: postman
  name: Appcharge Assets Localization API
  slug: postman-appcharge-localization-api
- collection_type: postman
  name: Appcharge Assets Offer Designs API
  slug: postman-appcharge-offer-designs-api
- collection_type: postman
  name: Appcharge Assets Offers API
  slug: postman-appcharge-offers-api
- collection_type: postman
  name: Appcharge Assets Orders API
  slug: postman-appcharge-orders-api
- collection_type: postman
  name: Appcharge Assets Personalization API
  slug: postman-appcharge-personalization-api
- collection_type: postman
  name: Appcharge Assets Popups API
  slug: postman-appcharge-popups-api
- collection_type: postman
  name: Appcharge Assets Portal Content API
  slug: postman-appcharge-portal-content-api
- collection_type: postman
  name: Appcharge Assets Products API
  slug: postman-appcharge-products-api
- collection_type: postman
  name: Appcharge Assets Promo Codes API
  slug: postman-appcharge-promo-codes-api
- collection_type: postman
  name: Appcharge Assets Rolling Offers API
  slug: postman-appcharge-rolling-offers-api
- collection_type: postman
  name: Appcharge Assets Store Refresh Popups API
  slug: postman-appcharge-store-refresh-popups-api
- collection_type: postman
  name: Appcharge Assets Triggered Popups API
  slug: postman-appcharge-triggered-popups-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Appcharge Assets API
  slug: open-appcharge-assets-api
- collection_type: open
  name: Appcharge Assets Authentication API
  slug: open-appcharge-authentication-api
- collection_type: open
  name: Appcharge Assets Badges API
  slug: open-appcharge-badges-api
- collection_type: open
  name: Appcharge Assets Coupons API
  slug: open-appcharge-coupons-api
- collection_type: open
  name: Appcharge Assets General API
  slug: open-appcharge-general-api
- collection_type: open
  name: Appcharge Assets Localization API
  slug: open-appcharge-localization-api
- collection_type: open
  name: Appcharge Assets Offer Designs API
  slug: open-appcharge-offer-designs-api
- collection_type: open
  name: Appcharge Assets Offers API
  slug: open-appcharge-offers-api
- collection_type: open
  name: Appcharge Assets Orders API
  slug: open-appcharge-orders-api
- collection_type: open
  name: Appcharge Assets Personalization API
  slug: open-appcharge-personalization-api
- collection_type: open
  name: Appcharge Assets Popups API
  slug: open-appcharge-popups-api
- collection_type: open
  name: Appcharge Assets Portal Content API
  slug: open-appcharge-portal-content-api
- collection_type: open
  name: Appcharge Assets Products API
  slug: open-appcharge-products-api
- collection_type: open
  name: Appcharge Assets Promo Codes API
  slug: open-appcharge-promo-codes-api
- collection_type: open
  name: Appcharge Assets Rolling Offers API
  slug: open-appcharge-rolling-offers-api
- collection_type: open
  name: Appcharge Assets Store Refresh Popups API
  slug: open-appcharge-store-refresh-popups-api
- collection_type: open
  name: Appcharge Assets Triggered Popups API
  slug: open-appcharge-triggered-popups-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/appcharge-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/appcharge/overview
- group: company
  title: ''
  type: Website
  url: https://appcharge.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.appcharge.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.appcharge.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.appcharge.com/api-reference/introduction
- group: operate
  title: ''
  type: Support
  url: https://help.appcharge.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.appcharge.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Appcharge
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.appcharge.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.appcharge.com/tc
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.appcharge.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/appcharge-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/appcharge-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/appcharge-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/appcharge-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/appcharge-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/appcharge-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://appcharge.instatus.com
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.appcharge.com/api-reference/versioning-policy
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/appcharge-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/appcharge-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/appcharge-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/appcharge-packages.yml
- group: design
  title: ''
  type: Components
  url: components/appcharge-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/appcharge-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/appcharge-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/appcharge-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/appcharge-openapi-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/appcharge-well-known.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/appcharge-events-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/appcharge-events-asyncapi.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/appcharge-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.appcharge.com/merchant-of-record/security/about-security-at-appcharge
- group: auth
  title: ''
  type: TrustCenter
  url: security/appcharge-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/appcharge-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.appcharge.com/merchant-of-record/security/about-security-at-appcharge
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appcharge-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/appcharge-agentic-access.yml
created: '2026-07-17'
description: Appcharge is a monetization and payments platform (merchant of record) for mobile game publishers. It lets studios sell in-game offers direct-to-consumer outside the app stores through a hosted web store, a mobile Checkout SDK, and Payment Links — covering checkout sessions, price localization, coupons and promo codes, refunds, web-store offers (bundles, daily bonuses, rolling/special offers, progress bars, reward calendars, triggered popups), offer components, game-portal content, media assets, translations, financial and analytics reporting, and player personalization/authentication callbacks. The REST API authenticates with an x-publisher-token API-key header; webhooks and Appcharge-to-publisher callbacks are HMAC-SHA256 signed with a replay window; and a hosted MCP server exposes agent access over OAuth 2.0 (authorization_code + PKCE).
image: https://appcharge.com/sharing-whatsapp.png
layout: provider
mcp_servers:
- description: Appcharge ships an official hosted MCP server. It is declared in the public appcharge-skills repo (.mcp.json) and advertised by the Claude/Cursor plugin manifests. The endpoint is live (returns 401 "M
  name: Appcharge MCP Server
  slug: appcharge-mcp-server
modified: '2026-07-18'
name: Appcharge
nav: Providers
network: true
overview: 'Appcharge publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Authentication API, Badges API, and 14 more. Tagged areas include Company, Payments, Monetization, Merchant of Record, and Mobile Games.


  The Appcharge catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Appcharge''s developer surface includes documentation, API reference, support, engineering blog, signup flow, authentication, changelog, and 33 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 1
  name: Appcharge Rate Limits
  slug: appcharge-rate-limits
scopes:
- name: Appcharge Scopes
  scope_count: 2
  slug: appcharge-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 61.8
  coverage:
    artifact_dirs: 26
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 63.7
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 61.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 17
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/appcharge/refs/heads/main/screenshots/appcharge-2026-07-25T200716.png
security:
- kind: authentication
  name: Appcharge Authentication
  slug: appcharge-authentication
  summary_line: apiKey/oauth2/mutualTLS/hmac-signature · 4 schemes
- kind: domain-security
  name: Appcharge Domain Security
  slug: appcharge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Appcharge Vulnerability Disclosure
  slug: appcharge-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Appcharge Trust Center
  slug: appcharge-trust-center
  summary_line: PCI DSS Level 1, SOC 2 Type II
slug: appcharge
tags:
- Company
- Payments
- Monetization
- Merchant of Record
- Mobile Games
- Gaming
- Checkout
- In-Game Purchases
- Web Store
- E-Commerce
website: https://appcharge.com/
---
