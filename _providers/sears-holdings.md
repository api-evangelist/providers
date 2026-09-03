---
access_model:
  confidence: medium
  label: Public docs, seller-account gated credentials, $39.99/mo program fee plus category commission
  onboarding: unknown
  pricing: paid
  public: true
  source:
  - https://marketplace.sears.com/sell-on-sears/program-fees/
  - https://marketplace.sears.com/docs/api-guide/using-sear-marketplace-apis-for-xml-integration/credentials-and-authentication/
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.1
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Versioned XML-over-HTTPS API for third-party sellers on Sears Marketplace (Sears.com, Kmart.com, ShopYourWay.com). GET calls export purchase orders, inventory, item classes, attributes, cancellation r
  name: Sears Marketplace Seller API
  slug: sears-marketplace-seller-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sears-holdings-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/transformco
- group: company
  title: ''
  type: Website
  url: https://www.sears.com/
- group: company
  title: ''
  type: Blog
  url: https://www.sears.com//blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.sears.com//blog/feed/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://marketplace.sears.com/
- group: docs
  title: ''
  type: Documentation
  url: https://marketplace.sears.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://marketplace.sears.com/docs/api-guide/
- group: start
  title: ''
  type: GettingStarted
  url: https://marketplace.sears.com/docs/api-guide/using-sear-marketplace-apis-for-xml-integration/
- group: operate
  title: ''
  type: Support
  url: https://marketplace.sears.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://marketplace.sears.com/seller-support/
- group: start
  title: ''
  type: SignUp
  url: https://marketplace.sears.com/sell-on-sears/
- group: start
  title: ''
  type: Login
  url: https://marketplace.sears.com/login/
- group: commercial
  title: ''
  type: Pricing
  url: https://marketplace.sears.com/sell-on-sears/program-fees/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://marketplace.sears.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sears.com/en_us/customer-service/policies/privacy-policy.html
- group: commercial
  title: ''
  type: Plans
  url: plans/sears-holdings-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sears-holdings-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sears-holdings-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sears-holdings-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sears-holdings-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sears-holdings-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sears-holdings-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/sears-holdings-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sears-holdings-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sears-holdings-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sears-holdings-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sears-holdings-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: XMLSchema
  url: xsd/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/sears-holdings-packages.yml
created: '2026-03-24'
description: Sears Holdings was the American holding company behind the Sears and Kmart department store chains. It filed for Chapter 11 in October 2018 and its retail operations were acquired in 2019 by Transform Holdco LLC, which trades as Transformco (Transform SR Brands LLC), the entity that operates Sears.com, Kmart.com and ShopYourWay.com today. The live developer surface carried forward from that estate is the Sears Marketplace Seller API — a versioned XML-over-HTTPS integration for third-party sellers covering catalog and item management, item class and attribute libraries, inventory, pricing, purchase order retrieval, order cancellations, returns and partial or full refunds, ASN and shipment updates, order prep time, installation service items, and remittance, removed-item, content-match and processing reports. Every API is published with a downloadable XSD and a sample XML document, both fetchable without credentials from seller.marketplace.sears.com, and calls are signed with
  an HMAC-SHA256 authorization header rather than OAuth. There is no OpenAPI, GraphQL, MCP server or A2A agent card on any Sears, Kmart or Transformco host.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sears-holdings.png
layout: provider
modified: '2026-08-28'
name: Sears Holdings
nav: Providers
network: true
overview: 'Sears Holdings publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 100, Retail, E-Commerce, Marketplace, and Order Management.


  Sears Holdings'' developer surface includes engineering blog, documentation, API reference, getting-started guide, support, signup flow, pricing, and 24 more developer resources.'
plans:
- name: Sears Holdings Plans Pricing
  plan_count: 1
  slug: sears-holdings-plans-pricing
press:
- date: '2026-05-25'
  title: Sears' Property Sales Prevent Q2 Loss
  url: https://www.cfo.com/news/sears-property-sales-prevent-q2-loss/663426/
- date: '2026-05-25'
  title: Sears Auto Center Uses Artificial Intelligence To Put ...
  url: https://searsholdings.com/press-releases/pr/2026
- date: '2026-05-25'
  title: Stanley Black & Decker Completes Purchase Of Craftsman ...
  url: https://www.aftermarketnews.com/stanley-black-decker-completes-purchase-craftsman-brand-sears-holdings/
- date: '2026-05-25'
  title: KULR Welcomes Microsoft Director and Pricing ...
  url: https://www.sec.gov/Archives/edgar/data/1662684/000110465926049843/tm2612908d1_ex99-1.htm
- date: '2026-05-25'
  title: Sears Auto Center Uses Artificial Intelligence To Put ...
  url: https://www.prnewswire.com/news-releases/sears-auto-center-uses-artificial-intelligence-to-put-personal-touch-on-tire-shopping-300392529.html
- date: '2022-01-22'
  title: Transformco to Close Sears Store in Ft. Lauderdale, Fla.
  url: https://transformco.com/press-releases/pr/2153
- date: '2021-07-26'
  title: Transform SR Holding Management LLC Identifies and Addresses Data Security Incident
  url: https://transformco.com/press-releases/pr/2152
- date: '2021-07-01'
  title: How Sears Home Services Helped Keep Puerto Rico's Appliances Running When It Mattered Most
  url: https://transformco.com/press-releases/pr/2151
random_paper: 15
rate_limits:
- limit_count: 8
  name: Sears Holdings Rate Limits
  slug: sears-holdings-rate-limits
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 22
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 6.7
    developer_ergonomics: 57.7
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 55.3
  previous_composite: 36.5
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: authentication
  name: Sears Holdings Authentication
  slug: sears-holdings-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Sears Holdings Domain Security
  slug: sears-holdings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sears-holdings
tags:
- Fortune 100
- Retail
- E-Commerce
- Marketplace
- Order Management
- Inventory
- Product Catalog
- Seller Integration
- XML
website: https://www.sears.com/
---
