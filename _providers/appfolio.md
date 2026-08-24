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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.4
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appfolio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.appfolio.com
- group: other
  title: ''
  type: Products
  url: https://www.appfolio.com/products
- group: other
  title: ''
  type: PropertyManager
  url: https://www.appfolio.com/property-manager
- group: other
  title: ''
  type: InvestmentManager
  url: https://www.appfolio.com/investment-management
- group: other
  title: ''
  type: RealmX
  url: https://www.appfolio.com/realm-x
- group: operate
  title: ''
  type: Stack
  url: https://www.appfolio.com/stack
- group: operate
  title: ''
  type: StackAPI
  url: https://www.appfolio.com/stack/partners/api
- group: company
  title: ''
  type: BecomePartner
  url: https://www.appfolio.com/stack/become-a-partner
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.appfolio.com/
- group: company
  title: ''
  type: EngineeringBlog
  url: https://engineering.appfolio.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/appfolio
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpcenter.appfolio.com/
- group: company
  title: ''
  type: Newsroom
  url: https://www.appfolio.com/newsroom
- group: company
  title: ''
  type: Blog
  url: https://www.appfolio.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.appfolio.com/pricing
- group: other
  title: ''
  type: Customers
  url: https://www.appfolio.com/customers
- group: other
  title: ''
  type: Company
  url: https://www.appfolio.com/company
- group: company
  title: ''
  type: Careers
  url: https://www.appfolio.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://www.appfolio.com/contact
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.appfolioinc.com/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/appfolio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/appfolio
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@AppFolio
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/AppFolio
- group: docs
  title: ''
  type: GraphQL
  url: graphql/appfolio-graphql.md
created: '2026-05-25'
description: AppFolio is a Santa Barbara, California cloud-based real estate technology company providing property management software to residential, commercial, community association (HOA), student housing, single-family, and affordable housing operators, plus investment management tooling for sponsors and funds. Its flagship AppFolio Performance Platform unifies workflow automation, accounting and reporting, marketing and leasing, maintenance, resident communication, and resident services on a single multi-tenant SaaS. AppFolio embeds Realm-X, an in-house agentic AI layer (Realm-X Assistant, Performers, Flows) directly into the platform rather than as an add-on. Integrations are delivered through the AppFolio Stack marketplace, where certified partners (ButterflyMX, Conservice, HappyCo, Knock, Lowe's, Property Meld, and many more) connect via the AppFolio Stack API. The Stack API is gated behind a partner application, security-compliance questionnaire, and terms-of-service signing; OAuth
  2.0, a sandbox environment, webhooks, and an OpenAPI/Swagger reference are made available only to approved partners through the developer.appfolio.com portal, so no public specification is reachable for catalog inclusion. AppFolio's revenue model is per-unit SaaS subscription plus value-added services (payments, screening, insurance, marketing). The AppFolio GitHub organization publishes internal Ruby on Rails, React, and tooling libraries (react-gears, ae_page_objects, store_base_sti_class) but no public API SDK, CLI, or OpenAPI artifact.
graphqls:
- description: This conceptual GraphQL schema models the AppFolio property management platform domain. AppFolio provides cloud-based property management software covering residential, commercial, HOA, student housin
  name: AppFolio GraphQL Schema
  slug: appfolio-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/appfolio.png
layout: provider
modified: '2026-05-25'
name: AppFolio
nav: Providers
network: true
overview: 'AppFolio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Property Management, Real-Estate, Residential, Commercial, and Community Associations.


  AppFolio''s developer surface includes Stack Overflow tag, GitHub presence, engineering blog, pricing, YouTube channel, and 21 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 17.4
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 38.9
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 17.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/appfolio/refs/heads/main/screenshots/appfolio-2026-06-20T172316.png
security:
- kind: domain-security
  name: Appfolio Domain Security
  slug: appfolio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appfolio
tags:
- Property Management
- Real-Estate
- Residential
- Commercial
- Community Associations
- HOA
- Multifamily
- Single-Family Rentals
- Student Housing
- Affordable Housing
- Investment Management
- PropTech
- Software-as-a-Service
- Accounting
- Leasing
- Maintenance
- Agentic AI
- Realm-X
- AppFolio Stack
website: https://www.appfolio.com
---
