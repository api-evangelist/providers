---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.2
  scored_at: '2026-09-05'
api_count: 2
apis:
- baseURL: https://prod-merchant-service.hoolah.co/merchant
  baseurl_source: declared
  description: The Account Linking API from ShopBack — 4 operation(s) for account linking.
  name: ShopBack Account Linking API
  slug: shopback-account-linking-api
- baseURL: https://prod-merchant-service.hoolah.co/merchant
  baseurl_source: declared
  description: The Authentication API from ShopBack — 1 operation(s) for authentication.
  name: ShopBack Authentication API
  slug: shopback-authentication-api
- baseURL: https://prod-merchant-service.hoolah.co/merchant
  baseurl_source: declared
  description: The Notification API from ShopBack — 1 operation(s) for notification.
  name: ShopBack Notification API
  slug: shopback-notification-api
- baseURL: https://prod-merchant-service.hoolah.co/merchant
  baseurl_source: declared
  description: The Orders API from ShopBack — 8 operation(s) for orders.
  name: ShopBack Orders API
  slug: shopback-orders-api
- baseURL: https://prod-merchant-service.hoolah.co/merchant
  baseurl_source: declared
  description: The Pre-Auth API from ShopBack — 6 operation(s) for pre-auth.
  name: ShopBack Pre Auth API
  slug: shopback-pre-auth-api
artifact_total: 14
asyncapis:
- description: ''
  name: Shopback Payment Notification Webhooks
  slug: shopback-payment-notification-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Online Payments Account Linking API
  slug: open-shopback-account-linking-api
- collection_type: open
  name: Online Payments Authentication API
  slug: open-shopback-authentication-api
- collection_type: open
  name: In-Store Payments Notification API
  slug: open-shopback-notification-api
- collection_type: open
  name: Shopback Orders API
  slug: open-shopback-orders-api
- collection_type: open
  name: Online Payments Pre Auth API
  slug: open-shopback-pre-auth-api
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/shopback-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/shopback-in-store-payments-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.shopback.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.shopback.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.shopback.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.shopback.com/reference/initiateorder
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.shopback.com/docs/quickstart-api
- group: operate
  title: ''
  type: Support
  url: https://shopback.my.site.com/merchanthelpcenter/s/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.shopback.sg/hc/en-gb
- group: company
  title: ''
  type: Blog
  url: https://www.shopback.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shopback
- group: commercial
  title: ''
  type: Pricing
  url: https://business.shopback.com/sg/payments
- group: start
  title: ''
  type: SignUp
  url: https://business.shopback.sg/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://support.shopback.com/hc/en-us/articles/33321351340307-Terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://support.shopback.com/hc/en-us/articles/33321399347475-ShopBack-Privacy-Policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shopback.com/
- group: build
  title: ''
  type: Postman
  url: https://docs.shopback.com/docs/postman-payload-sample
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/shopback-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/shopback-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/shopback-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/shopback-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/shopback-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/shopback-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/shopback-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/shopback-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/shopback-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/shopback-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/shopback-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/shopback-payment-notification-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/shopback-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/shopback-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/shopback-domain-security.yml
created: '2026-08-02'
description: ShopBack is a Singapore-headquartered shopping, rewards and payments platform founded in 2014, operating across 13 markets in Asia-Pacific, Europe and the United States with more than 20 million members and 20,000 merchant partners. Alongside its consumer cashback and discovery app, ShopBack runs a merchant-facing payments business — ShopBack Pay and ShopBack PayLater — and publishes a public developer hub at docs.shopback.com covering two REST APIs. The Online Payments API (v2.0, also called the Online Bespoke API) handles merchant login, order initiation, order status, refunds, and a tokenized-payments surface for account linking, pre-authorization hold/capture/void, immediate charge and cashback-balance lookup. The In-Store Payments API (v1.4) covers merchant-presented and customer-presented QR ordering, order status, refunds, cancellations, and a payment-notification webhook for point-of-sale and customer-facing app checkout. Both are HMAC- or JWT-authenticated over HTTPS/TLS
  1.2+, support an X-ShopBack-Idempotent-Id idempotency header, and ship e-commerce plugins for Shopify, WooCommerce, Magento, PrestaShop, EasyStore and Salesforce Commerce Cloud.
image: https://corporate.shopback.com/opengraph.jpg
layout: provider
modified: '2026-08-02'
name: ShopBack
nav: Providers
network: true
overview: 'ShopBack publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account Linking API, Authentication API, Notification API, and 2 more. Tagged areas include Company, Payments, Cashback, Rewards, and Loyalty.


  The ShopBack catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ShopBack''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
random_paper: 3
score:
  band: developing
  composite: 47.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 58.8
    developer_ergonomics: 49.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - singapore
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  previous_composite: 47.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/shopback/refs/heads/main/screenshots/shopback-2026-08-17T081837.png
security:
- kind: authentication
  name: Shopback Authentication
  slug: shopback-authentication
  summary_line: http/hmac/apiKey · 3 schemes
- kind: domain-security
  name: Shopback Domain Security
  slug: shopback-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: shopback
tags:
- Company
- Payments
- Cashback
- Rewards
- Loyalty
- E-Commerce
- Buy Now Pay Later
- Point-of-Sale
- Checkout
- Singapore
website: https://www.shopback.com/
---
