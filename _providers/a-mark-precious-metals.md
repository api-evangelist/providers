---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.4
  scored_at: '2026-08-30'
api_count: 4
apis:
- description: A-Mark's wholesale precious metals trading platform enables dealers and financial institutions to buy and sell gold, silver, platinum, and palladium bullion products. Offers spot, forward, and deferre
  name: A-Mark Wholesale Trading
  slug: a-mark-wholesale-trading
- description: A-Mark provides comprehensive logistics, receiving, storage, and delivery services for precious metals through state-of-the-art facilities. Includes precious metals leases and consignments with compet
  name: A-Mark Logistics and Storage
  slug: a-mark-logistics-storage
- description: A-Mark offers custom minting services blending traditional craftsmanship with modern technology for production of precious metal coins, bars, and rounds from sovereign and private mints worldwide.
  name: A-Mark Minting
  slug: a-mark-minting
- description: A-Mark provides financing options using precious metals as collateral, offering collateralized loans to qualified commercial customers against precious metal holdings.
  name: A-Mark Collateralized Loans
  slug: a-mark-collateralized-loans
artifact_total: 27
common:
- group: agent
  title: ''
  type: WellKnown
  url: well-known/a-mark-precious-metals-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/a-mark-precious-metals-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/a-mark-precious-metals-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/a-mark-precious-metals-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/a-mark-precious-metals-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/a-mark-precious-metals-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/a-mark-precious-metals-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/a-mark-precious-metals-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/a-mark-precious-metals-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/a-mark-precious-metals-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/a-mark-precious-metals-finops.yml
- group: start
  title: ''
  type: Login
  url: https://portal.amark.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amark.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amark.com/privacy-policy/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/a-mark-precious-metals-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/goldcominc
- group: company
  title: ''
  type: Website
  url: https://www.amark.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.amark.com/services
- group: operate
  title: ''
  type: Contact
  url: https://www.gold.com/contact/
created: '2026-04-19'
description: 'A-Mark Precious Metals is a full-service precious metals trading company that wholesales gold, silver, platinum, and palladium bullion and coins to dealers, financial institutions, and investors. They operate trading desks 17 hours daily across global locations (US, Asia, Vienna) and offer wholesale sales, direct-to-consumer, logistics and storage, minting, and collateralized loans services. The company is renaming to Gold.com, Inc. and transferring to the NYSE under the ticker GOLD, alongside its $33M acquisition of Monex Deposit Company; A-Mark now sits as one brand inside the Gold.com brand family. A-Mark runs no public developer program: trading access is through the credentialed A-Mark Trading Portal at portal.amark.com, whose OAuth 2.0 discovery document is the only machine-readable contract the company serves.'
features:
- description: Bulk precious metals trading with market making through trading desks operating 17 hours daily across US, Asia, and Vienna locations.
  name: Wholesale Trading
- description: Spot and forward deferred transactions for qualified commercial customers in gold, silver, platinum, and palladium.
  name: Spot and Forward Transactions
- description: Limit orders, stop orders, and immediate execution capabilities for flexible precious metals trading strategies.
  name: Order Types
- description: 48-hour settlement with payment accepted in US Dollars, Euros, or product.
  name: Settlement Options
- description: State-of-the-art facilities for receiving, storage, and delivery of precious metals products globally.
  name: Storage and Logistics
- description: Custom minting services for coins, bars, and rounds blending traditional craftsmanship with modern production technology.
  name: Custom Minting
- description: Precious metals leases, consignments, and collateralized loans with competitive rates for qualified customers.
  name: Collateralized Financing
- description: Retail precious metals sales to individual consumers through their JMBullion.com brand.
  name: Direct-to-Consumer
finops:
- name: A Mark Precious Metals Finops
  service_category: Financial Services / Commodities
  slug: a-mark-precious-metals-finops
image: /assets/icons/a-mark-precious-metals.png
integrations:
- description: A-Mark's direct-to-consumer retail brand for individual precious metals buyers selling gold, silver, platinum, and palladium.
  name: JMBullion.com
- description: Integrated trading operations across US, Asian, and European (Vienna) offices for 17-hour daily market coverage.
  name: Global Trading Desks
- description: Sourcing relationships with sovereign and private mints worldwide for diverse product availability and custom minting.
  name: Sovereign and Private Mints
layout: provider
modified: '2026-08-29'
name: A-Mark Precious Metals
nav: Providers
network: true
overview: 'A-Mark Precious Metals publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Precious Metals, Trading, Wholesale, Gold, and Silver.


  A-Mark Precious Metals'' developer surface includes authentication, documentation, and 17 more developer resources.'
plans:
- name: A Mark Precious Metals Plans Pricing
  plan_count: 0
  slug: a-mark-precious-metals-plans-pricing
press:
- date: '2026-05-25'
  title: 'Monex Acquisition: A-Mark Rebrands to Gold.com, Moves ...'
  url: https://www.latimes.com/b2b/banking-finance/story/2025-11-25/a-mark-rebrands-gold-com-acquires-monex-33-million
- date: '2026-05-25'
  title: A-Mark Precious Metals, Inc. - Investor Relations
  url: https://ir.gold.com/sec-filings/all-sec-filings/content/0001193125-25-200462/0001193125-25-200462.pdf
- date: '2026-05-25'
  title: A-Mark Precious Metals Sets Fiscal First Quarter Earnings ...
  url: https://www.gurufocus.com/news/2556779/amark-precious-metals-sets-fiscal-first-quarter-earnings-call-for-wednesday-november-6-at-430-pm-et?mobile=true%3Fmobile%3Dtrue&mobile=true
- date: '2026-05-25'
  title: 10-K - 09/11/2025 - A-Mark Precious Metals, Inc.
  url: https://www.sec.gov/Archives/edgar/data/1591588/000119312525227653/amrk_ars_fy_25.pdf
- date: '2026-05-25'
  title: Global Privacy Policy
  url: https://www.amark.com/privacy-policy/
random_paper: 16
rate_limits:
- limit_count: 0
  name: A Mark Precious Metals Rate Limits
  slug: a-mark-precious-metals-rate-limits
scopes:
- name: A Mark Precious Metals Scopes
  scope_count: 0
  slug: a-mark-precious-metals-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 77.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 35.5
    commercial_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 25.7
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 68.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/a-mark-precious-metals/refs/heads/main/screenshots/a-mark-precious-metals-2026-06-20T162921.png
security:
- kind: authentication
  name: A Mark Precious Metals Authentication
  slug: a-mark-precious-metals-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: A Mark Precious Metals Domain Security
  slug: a-mark-precious-metals-domain-security
  summary_line: TLSv1.3 · DMARC
slug: a-mark-precious-metals
tags:
- Precious Metals
- Trading
- Wholesale
- Gold
- Silver
- Bullion
- Finance
use_cases:
- description: Precious metals dealers purchasing bulk gold, silver, platinum, and palladium bullion for resale to retail customers.
  name: Wholesale Dealer Trading
- description: Banks and financial institutions trading precious metals for portfolio hedging, risk management, and investment purposes.
  name: Financial Institution Hedging
- description: Institutional investors acquiring physical precious metals as a store of value and inflation hedge.
  name: Investor Bullion Acquisition
- description: Dealers and institutions using A-Mark's storage and logistics services for secure precious metals custody and delivery.
  name: Logistics and Custody
- description: Organizations commissioning custom precious metal coins, bars, and rounds for commemorative, promotional, or commercial purposes.
  name: Custom Coin Production
- description: Businesses leveraging precious metals holdings as collateral for working capital financing and liquidity.
  name: Precious Metals Financing
website: https://www.amark.com
---
