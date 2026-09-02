---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stessa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stessa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stessa.com
- group: other
  title: ''
  type: WebApplication
  url: https://app.stessa.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stessa.com/pricing/
- group: build
  title: ''
  type: RentCollection
  url: https://www.stessa.com/rent-collection/
- group: other
  title: ''
  type: TenantScreening
  url: https://www.stessa.com/tenant-screening/
- group: other
  title: ''
  type: Banking
  url: https://www.stessa.com/banking/
- group: other
  title: ''
  type: Leasing
  url: https://www.stessa.com/leasing/
- group: other
  title: ''
  type: Marketplace
  url: https://www.stessa.com/marketplace/
- group: company
  title: ''
  type: Blog
  url: https://www.stessa.com/blog/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.stessa.com
- group: operate
  title: ''
  type: Community
  url: https://community.stessa.com
- group: other
  title: ''
  type: Parent
  url: https://www.roofstock.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/stessa
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/stessa_app
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stessa
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/stessa
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/stessa
- group: other
  title: ''
  type: AppStore
  url: https://apps.apple.com/us/app/stessa-rental-property-tracker/id1252342941
- group: other
  title: ''
  type: GooglePlay
  url: https://play.google.com/store/apps/details?id=com.stessa.stessa
- group: operate
  title: ''
  type: Contact
  url: https://www.stessa.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.stessa.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.stessa.com/privacy-policy/
created: '2026-05-25'
description: Stessa is a financial reporting, accounting, and management platform for rental property owners and small-to-mid-size landlords, headquartered in San Francisco and operated as a brand of Roofstock alongside Mynd and RentPrep. The platform helps owners track unlimited properties and portfolios with automated bank and credit card feeds, transaction categorization, mileage tracking, receipt scanning, Schedule E-ready tax reporting, online rent collection, tenant screening through RentPrep, e-signature leasing with 50+ legal templates, maintenance request tracking, and property-specific Stessa Cash Management accounts with high-yield APY and FDIC insurance up to $3M per entity. Stessa is delivered as a web app and iOS/Android mobile apps with three tiers — Essentials (free), Manage, and Pro — and serves more than 350,000 landlords. Bank, credit card, and payment data flows in through aggregator partners (Plaid-style open banking) rather than a public Stessa API, and the only developer-facing
  GitHub presence is an org with a handful of forked Ruby and Vue.js utilities. There is no public Stessa REST API, no developer portal, no SDKs, and no published webhooks; the Stessa community has open feature requests for a public API to pull reports and transactions, but none has shipped.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stessa.png
layout: provider
modified: '2026-05-25'
name: Stessa
nav: Providers
network: true
overview: 'Stessa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real-Estate, Landlords, Rental Property, Property Management, and Accounting.


  Stessa''s developer surface includes pricing, engineering blog, GitHub presence, YouTube channel, and 20 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 6.8
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 6.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stessa/refs/heads/main/screenshots/stessa-2026-06-20T194548.png
security:
- kind: domain-security
  name: Stessa Domain Security
  slug: stessa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stessa Vulnerability Disclosure
  slug: stessa-vulnerability-disclosure
  summary_line: disclosure policy published
slug: stessa
tags:
- Real-Estate
- Landlords
- Rental Property
- Property Management
- Accounting
- Bookkeeping
- Financial Reporting
- Tax Reporting
- Rent Collection
- Tenant Screening
- Banking
- Roofstock
website: https://www.stessa.com
---
