---
access_model:
  confidence: medium
  label: Partner onboarding · Treasury API Banking (sandbox + OAuth2)
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - developer-portal
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-12'
api_count: 5
apis:
- description: Move Money Transfer is First Horizon's RESTful payments-initiation API for Treasury Management clients, used to originate and manage funds transfers programmatically from an ERP, accounting, or treasu
  name: Move Money Transfer v1
  slug: move-money-transfer-v1
- description: 'The ACH Origination API lets First Horizon Treasury Management clients originate ACH transactions directly from their ERP or accounting system via a RESTful interface, paired with an ACH Tokenization '
  name: ACH Origination
  slug: ach-origination
- description: The Account Information API provides Treasury Management clients real-time visibility into account information, balances, and transactions through a RESTful interface, for reconciliation and cash-posi
  name: Account Information
  slug: account-information
- description: ABA Lookup is a RESTful utility endpoint on First Horizon's API Banking platform that validates and resolves U.S. ABA routing transit numbers, supporting payment-instruction validation ahead of ACH an
  name: ABA Lookup v1
  slug: aba-lookup-v1
- description: BIC Lookup is a RESTful utility endpoint on First Horizon's API Banking platform that validates and resolves SWIFT/BIC codes, supporting the validation of international payment instructions. Authorize
  name: BIC Lookup v1
  slug: bic-lookup-v1
artifact_total: 7
common:
- group: company
  title: ''
  type: AboutUs
  url: https://www.firsthorizon.com/About-Us
- group: other
  title: ''
  type: Personal
  url: https://www.firsthorizon.com/Personal
- group: other
  title: ''
  type: SmallBusiness
  url: https://www.firsthorizon.com/Small-Business
- group: other
  title: ''
  type: Commercial
  url: https://www.firsthorizon.com/Commercial-Banking
- group: other
  title: ''
  type: WealthManagement
  url: https://www.firsthorizon.com/Wealth-Management
- group: other
  title: ''
  type: TreasuryManagement
  url: https://www.firsthorizon.com/Commercial-Banking/Treasury-Management
- group: other
  title: ''
  type: CapitalMarkets
  url: https://www.fhnfinancial.com/
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.firsthorizon.com
- group: company
  title: ''
  type: Newsroom
  url: https://newsroom.firsthorizon.com
- group: operate
  title: ''
  type: PressReleases
  url: https://newsroom.firsthorizon.com/news-releases
- group: company
  title: ''
  type: Careers
  url: https://www.firsthorizon.com/Careers
- group: commercial
  title: ''
  type: PrivacyCenter
  url: https://www.firsthorizon.com/Privacy
- group: auth
  title: ''
  type: SecurityCenter
  url: https://www.firsthorizon.com/Security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/First-horizon
- group: other
  title: ''
  type: SECFilings
  url: https://ir.firsthorizon.com/financial-information/sec-filings
- group: other
  title: ''
  type: AggregatorPlaid
  url: https://plaid.com/institutions/
- group: other
  title: ''
  type: AggregatorMX
  url: https://www.mx.com/
- group: other
  title: ''
  type: AggregatorFinicity
  url: https://www.finicity.com/
- group: other
  title: ''
  type: AggregatorAkoya
  url: https://akoya.com/
- group: other
  title: ''
  type: FDXStandard
  url: https://financialdataexchange.org/
- group: other
  title: ''
  type: CFPB1033Rule
  url: https://www.consumerfinance.gov/personal-financial-data-rights/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/first-horizon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.firsthorizon.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers-test.firsthorizon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers-test.firsthorizon.com/get-started
- group: other
  title: ''
  type: ProductPage
  url: https://www.firsthorizon.com/Corporate/Products-and-Services/Treasury-Management/API-Banking-Solutions
- group: auth
  title: ''
  type: Authentication
  url: https://developers-test.firsthorizon.com/apis/v0/oauth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/first-horizon-bank
- group: auth
  title: ''
  type: Authentication
  url: authentication/first-horizon-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/first-horizon-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/first-horizon-llms.txt
created: '2026-05-04'
description: First Horizon Corporation is a Fortune 500 financial services holding company headquartered in Memphis, Tennessee. Through First Horizon Bank it provides commercial, private, consumer, and mortgage banking, wealth management, and capital markets services across the southern United States. First Horizon operates a real API Banking developer portal for Treasury Management clients, exposing RESTful products for money movement, ACH origination, real-time account information, and routing-number lookups, secured with OAuth 2.0 and a sandbox for build-and-test integration. Onboarding is partner/relationship gated and no OpenAPI/Swagger specifications are publicly downloadable — this repository captures the documented API surface honestly, humanURL-only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/first-horizon.png
layout: provider
modified: '2026-07-23'
name: First Horizon
nav: Providers
network: true
overview: 'First Horizon publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include United States, Banking, Financial-Services, Treasury Management, and API Banking.


  First Horizon''s developer surface includes documentation, authentication, and 29 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 11.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 72.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 11.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 21.5
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: First Horizon Authentication
  slug: first-horizon-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: First Horizon Domain Security
  slug: first-horizon-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: first-horizon
tags:
- United States
- Banking
- Financial-Services
- Treasury Management
- API Banking
- ACH
- Payments
- Open Banking
- Super-Regional Bank
- Fortune 500
- Wealth Management
- Capital Markets
website: https://www.firsthorizon.com
---
