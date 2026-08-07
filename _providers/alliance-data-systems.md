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
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Alliance Data Systems Agentic Access
  operation_count: 14
  slug: alliance-data-systems-agentic-access
  summary_line: 14 operations · 8 acting
api_count: 9
apis:
- description: Browser-side JavaScript SDK that exposes the BreadPayments object for rendering the Bread modal, embedded placements, prequalification, and cart/checkout flows on merchant sites. Loaded from Bread CDN
  name: Bread JavaScript SDK
  slug: bread-javascript-sdk
- description: Official Bread Financial mobile SDK for iOS published as breadfinancial-brand-partners-ios on the bppub GitHub organization. Provides batch prescreen, unified prequalification, placement rendering, ap
  name: Bread Financial Brand Partners iOS SDK
  slug: bread-financial-brand-partners-ios-sdk
- description: Official Bread Financial mobile SDK for Android (Kotlin) published as breadfinancial-brand-partners-android on the bppub GitHub organization. Provides batch prescreen, unified prequalification, placem
  name: Bread Financial Brand Partners Android SDK
  slug: bread-financial-brand-partners-android-sdk
- description: Outbound webhook system for the BreadPay Platform that notifies merchant systems of transaction lifecycle events. Documented under the BreadPay developer site with setup, concepts, validation, and cli
  name: Bread Webhooks
  slug: bread-webhooks
- description: Manage buyer records and look up personalized payment options.
  name: Alliance Data Systems (Bread Financial Holdings) Buyers API
  slug: alliance-data-systems-buyers-api
- description: Manage Bread shopping carts that initiate the BNPL checkout flow.
  name: Alliance Data Systems (Bread Financial Holdings) Carts API
  slug: alliance-data-systems-carts-api
- description: Retrieve buyer-personalized payment option pricing and terms.
  name: Alliance Data Systems (Bread Financial Holdings) Payment Options API
  slug: alliance-data-systems-payment-options-api
- description: Attach carrier and tracking-number information to a transaction.
  name: Alliance Data Systems (Bread Financial Holdings) Shipping API
  slug: alliance-data-systems-shipping-api
- description: Manage completed Bread Pay transactions.
  name: Alliance Data Systems (Bread Financial Holdings) Transactions API
  slug: alliance-data-systems-transactions-api
artifact_total: 42
collections:
- collection_type: open
  name: Bread Classic Merchant API
  slug: open-bread-classic-merchant
- collection_type: open
  name: Bread Pay Platform API
  slug: open-bread-pay-platform
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/alliance-data-systems-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alliance-data-systems-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/alliance-data-systems-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/alliance-data-systems-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.breadfinancial.com
- group: company
  title: ''
  type: FormerWebsite
  url: https://www.alliancedata.com
- group: company
  title: ''
  type: BNPLWebsite
  url: https://www.breadpayments.com
- group: other
  title: ''
  type: BusinessSolutions
  url: https://www.breadfinancial.com/en/business-solutions.html
- group: other
  title: ''
  type: BuyNowPayLater
  url: https://www.breadfinancial.com/en/business-solutions/buy-now-pay-later.html
- group: company
  title: ''
  type: Newsroom
  url: https://newsroom.breadfinancial.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.breadfinancial.com
- group: other
  title: ''
  type: SECRebrandFiling
  url: https://www.sec.gov/Archives/edgar/data/0001101215/000110121522000058/form_8-k.htm
- group: other
  title: ''
  type: WikipediaPage
  url: https://en.wikipedia.org/wiki/Bread_Financial
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform-docs.breadpayments.com/bread-developers
- group: start
  title: ''
  type: ClassicDeveloperPortal
  url: https://docs.breadpayments.com/bread-classic/reference
- group: start
  title: ''
  type: OnboardingDocs
  url: https://platform-docs.breadpayments.com/bread-onboarding
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bppub
- group: build
  title: ''
  type: IntegrationsGitHubOrganization
  url: https://github.com/breadfinance
- group: build
  title: ''
  type: LegacyGitHubOrganization
  url: https://github.com/getbread
- group: other
  title: ''
  type: APITracker
  url: https://apitracker.io/a/breadpayments
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bread-financial
- group: commercial
  title: ''
  type: Plans
  url: plans/alliance-data-systems-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/alliance-data-systems-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/alliance-data-systems-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/alliance-data-systems-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/alliance-data-systems-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://newsroom.breadfinancial.com/rss.xml
created: '2026-04-19'
description: Alliance Data Systems Corporation (ADS) was a Plano/Columbus-based financial and marketing services holding company built in 1996 from the merger of J.C. Penney's credit card processing unit and The Limited's World Financial Network National Bank, taken public on the NYSE in 2001. The company historically operated three segments — Card Services (private label and co-brand retail credit cards), Epsilon (data-driven marketing and CRM), and LoyaltyOne (the AIR MILES Reward Program in Canada and BrandLoyalty in the Netherlands). In July 2019 ADS sold Epsilon to Publicis Groupe for $4.4 billion. In December 2020 ADS acquired Bread, a New York-based BNPL platform, for $450 million. In November 2021 ADS spun off LoyaltyOne as Loyalty Ventures Inc. (LTRN). On March 23, 2022 the remaining card-and-payments business rebranded as Bread Financial Holdings, Inc., with the common stock starting to trade on NYSE under the new ticker BFH on April 4, 2022. Today Bread Financial is a tech-forward
  financial services company headquartered in Columbus, Ohio (Wikipedia 2024 figures&#58; $3.84B revenue, ~6,000 employees, $22.9B total assets, 135+ managed card programs across partners including Victoria's Secret, Wayfair, Williams-Sonoma, Academy Sports, HP, PlayStation, and the Crypto.com Visa Card). The developer surface lives under the Bread Pay BNPL brand at developer-facing properties docs.breadpayments.com (legacy "bread-classic" Merchant API) and platform-docs.breadpayments.com (next-generation "BreadPay Platform" APIs, OAuth 2.0 Client Credentials, hosted on https://api.platform.breadpayments.com/api), plus a JavaScript Bread SDK (preview + production CDN), iOS/Android mobile SDKs published as the Bread Financial Brand Partners SDKs on github.com/bppub, and platform integrations for Shopify, Magento 2, WooCommerce, BigCommerce, Salesforce Commerce Cloud, Miva, Volusion, and Turbify. The corporate/holding side (private-label and co-brand cards issued through Comenity Bank and
  Comenity Capital Bank, plus high-yield savings, CDs, IRAs, and personal loans) is delivered through B2B partner integrations rather than a public developer portal.
examples:
- key_count: 2
  name: Bread Classic Add Shipping Example
  slug: bread-classic-add-shipping-example
- key_count: 2
  name: Bread Classic Create Cart Example
  slug: bread-classic-create-cart-example
- key_count: 2
  name: Bread Pay Platform Authorize Transaction Example
  slug: bread-pay-platform-authorize-transaction-example
- key_count: 2
  name: Bread Pay Platform Create Transaction Example
  slug: bread-pay-platform-create-transaction-example
- key_count: 2
  name: Bread Pay Platform Get Buyer Example
  slug: bread-pay-platform-get-buyer-example
- key_count: 2
  name: Bread Pay Platform Get Transaction Example
  slug: bread-pay-platform-get-transaction-example
- key_count: 2
  name: Bread Pay Platform Refund Transaction Example
  slug: bread-pay-platform-refund-transaction-example
finops:
- name: Alliance Data Systems Finops
  service_category: Financial Services
  slug: alliance-data-systems-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alliance-data-systems.png
json_schemas:
- name: BreadClassicCartItem
  property_count: 5
  slug: bread-classic-cart-item
- name: BreadClassicCart
  property_count: 8
  slug: bread-classic-cart
- name: BreadClassicShipping
  property_count: 3
  slug: bread-classic-shipping
- name: BreadClassicTransaction
  property_count: 7
  slug: bread-classic-transaction
- name: BreadPayPlatformAddress
  property_count: 6
  slug: bread-pay-platform-address
- name: BreadPayPlatformAmount
  property_count: 2
  slug: bread-pay-platform-amount
- name: BreadPayPlatformBuyer
  property_count: 7
  slug: bread-pay-platform-buyer
- name: BreadPayPlatformPaymentOption
  property_count: 5
  slug: bread-pay-platform-payment-option
- name: BreadPayPlatformTransaction
  property_count: 8
  slug: bread-pay-platform-transaction
json_structures:
- name: Bread Classic Cart Structure
  property_count: 6
  slug: bread-classic-cart-structure
- name: Bread Pay Platform Address Structure
  property_count: 6
  slug: bread-pay-platform-address-structure
- name: Bread Pay Platform Buyer Structure
  property_count: 7
  slug: bread-pay-platform-buyer-structure
- name: Bread Pay Platform Transaction Structure
  property_count: 8
  slug: bread-pay-platform-transaction-structure
jsonld:
- class_count: 35
  name: Alliance Data Systems Context
  property_count: 15
  slug: alliance-data-systems-context
layout: provider
modified: '2026-05-23'
name: Alliance Data Systems (Bread Financial Holdings)
nav: Providers
network: true
overview: 'Alliance Data Systems (Bread Financial Holdings) publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Buyers API, Carts API, Payment Options API, and 2 more. Tagged areas include Financial Services, Fintech, Buy Now Pay Later, BNPL, and Bread Pay.


  The Alliance Data Systems (Bread Financial Holdings) catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  Alliance Data Systems (Bread Financial Holdings)''s developer surface includes authentication, engineering blog, and 25 more developer resources.'
plans:
- name: Alliance Data Systems Plans Pricing
  plan_count: 3
  slug: alliance-data-systems-plans-pricing
press:
- date: '2026-05-25'
  title: Bread to be Acquired by Alliance Data Systems for $450 ...
  url: https://www.stblaw.com/about-us/news/view/2020/10/29/bread-to-be-acquired-by-alliance-data-systems-for-$450-million
- date: '2026-05-25'
  title: Alliance Data Inks $450M Deal For FinTech Bread
  url: https://www.pymnts.com/news/partnerships-acquisitions/2020/alliance-data-inks-450m-deal-for-fintech-bread/
- date: '2026-05-25'
  title: Alliance Data Completes Acquisition of Bread®
  url: https://www.prnewswire.com/news-releases/alliance-data-completes-acquisition-of-bread-301186414.html
- date: '2026-05-25'
  title: Alliance Data becomes Bread, taking buy now/pay later ...
  url: https://www.americanbanker.com/payments/news/alliance-data-becomes-bread-taking-buy-now-pay-later-units-name
- date: '2026-05-25'
  title: 'Q2: Alliance Data Systems Bets On Conversant''s Pipeline'
  url: https://www.adexchanger.com/online-advertising/q2-alliance-data-systems-bets-on-coversants-pipeline/
random_paper: 83
rate_limits:
- limit_count: 1
  name: Alliance Data Systems Rate Limits
  slug: alliance-data-systems-rate-limits
rules:
- name: Alliance Data Systems (Bread Financial Holdings) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: alliance-data-systems-jsonschema-spectral-rules
- name: Alliance Data Systems (Bread Financial Holdings) API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: bread-classic-merchant-rules
- name: Alliance Data Systems (Bread Financial Holdings) API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: bread-pay-platform-rules
scopes:
- name: Alliance Data Systems Scopes
  scope_count: 3
  slug: alliance-data-systems-scopes
  summary_line: 3 scopes · clientCredentials
score:
  band: developing
  composite: 48.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 72.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 43.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alliance-data-systems/refs/heads/main/screenshots/alliance-data-systems-2026-07-25T195654.png
security:
- kind: authentication
  name: Alliance Data Systems Authentication
  slug: alliance-data-systems-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Alliance Data Systems Domain Security
  slug: alliance-data-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alliance-data-systems
tags:
- Financial Services
- Fintech
- Buy Now Pay Later
- BNPL
- Bread Pay
- Private Label Credit
- Co Brand Credit Cards
- Loyalty Programs
- Marketing
- Data Driven Marketing
- Payments
- Lending
- Savings
- Personal Loans
- Consumer Banking
- Retail Finance
- Fortune 500
- NYSE BFH
- Comenity Bank
- Rebrand
website: https://www.breadfinancial.com
---
