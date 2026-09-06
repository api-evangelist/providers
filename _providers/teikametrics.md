---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    well_known_catalog: true
  schema_version: 0.2
  score: 2.9
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/teikametrics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.teikametrics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.teikametrics.com/en/
- group: operate
  title: ''
  type: Support
  url: https://help.teikametrics.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.teikametrics.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.teikametrics.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.teikametrics.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.teikametrics.com/
- group: start
  title: ''
  type: Login
  url: https://app.teikametrics.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.teikametrics.com/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.teikametrics.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teikametrics
- group: company
  title: ''
  type: Careers
  url: https://www.teikametrics.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.teikametrics.com/contact-us/
- group: company
  title: ''
  type: About
  url: https://www.teikametrics.com/company/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/teikametrics_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/teikametrics-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/teikametrics-packages.yml
created: '2026-08-02'
description: 'Teikametrics is a Boston-based commerce optimization company founded by Alasdair McLean-Foreman that builds ARI (Artificial Retail Intelligence), an AI platform for brands and sellers operating on Amazon, Walmart and TikTok Shop. The platform ingests advertising, catalog, sales and inventory data pulled from marketplace APIs (Amazon Advertising, Amazon Selling Partner, Walmart Marketplace and Ads, TikTok Shop) and applies retail-trained models to bid management, keyword harvesting, listing and feed optimization, demand forecasting and profit-based reporting. Product surfaces include Compass dashboards, the Recommendation Hub, Product Catalog, Advertising Optimization, Inventory Optimization, Market IQ and Business Intelligence, plus an Agency Edition with nested client accounts. Teikametrics is an API consumer rather than an API producer: as of this profiling pass it publishes no public developer portal, no OpenAPI or other machine-readable contract, and no customer-facing
  API reference — integration happens through OAuth-style marketplace channel connections made inside the application.'
image: https://www.teikametrics.com/wp-content/uploads/2026/01/Teikametrics-logo.svg
layout: provider
modified: '2026-08-02'
name: Teikametrics
nav: Providers
network: true
overview: 'Teikametrics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Advertising, Retail, E-Commerce, and Marketplaces.


  Teikametrics'' developer surface includes documentation, support, engineering blog, pricing, signup flow, and 13 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 15.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/teikametrics/refs/heads/main/screenshots/teikametrics-2026-09-02T162724.png
security:
- kind: domain-security
  name: Teikametrics Domain Security
  slug: teikametrics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: teikametrics
tags:
- Company
- Advertising
- Retail
- E-Commerce
- Marketplaces
- Artificial Intelligence
- Analytics
- Amazon
- Walmart
- Inventory
website: https://www.teikametrics.com/
---
