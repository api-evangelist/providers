---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Partner integration API for the AppFolio Performance Platform, covering resources such as attachments, bank accounts, bills, charges, properties, units, owners, occupancies and work orders. The public
  name: AppFolio Stack API
  slug: appfolio-stack-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/appfolio/plans/appfolio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appfolio-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/appfolio/lifecycle/appfolio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/appfolio-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/appfolio/llms/appfolio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appfolio-llms.txt
- group: other
  href: https://artifacts.apis.io/appfolio/hosts/appfolio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appfolio-hosts.yml
- group: build
  href: https://artifacts.apis.io/appfolio/integrations/appfolio-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/appfolio-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/appfolio/vendors/appfolio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appfolio-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.appfolio.com/trust/
- group: operate
  title: ''
  type: Support
  url: https://www.appfolio.com/help/owner
- group: other
  title: ''
  type: Leadership
  url: https://www.appfolio.com/markets/hoa/management
- group: auth
  href: https://artifacts.apis.io/appfolio/security/appfolio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appfolio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.appfolio.com
- group: other
  title: ''
  type: PropertyManager
  url: https://www.appfolio.com/property-manager
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
  type: StatusPage
  url: https://status.appfolio.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.appfolio.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.appfolio.com/privacy
- group: start
  title: ''
  type: Login
  url: https://www.appfolio.com/login
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
  type: Company
  url: https://www.appfolio.com/company
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
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.appfolio.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-05-25'
description: AppFolio is a Santa Barbara, California cloud-based real estate technology company providing property management software to residential, commercial, community association (HOA), student housing, single-family, and affordable housing operators, plus investment management tooling for sponsors and funds. Its flagship AppFolio Performance Platform unifies workflow automation, accounting and reporting, marketing and leasing, maintenance, resident communication, and resident services on a single multi-tenant SaaS. AppFolio embeds Realm-X, an in-house agentic AI layer (Realm-X Assistant, Performers, Flows) directly into the platform rather than as an add-on. Integrations are delivered through the AppFolio Stack marketplace, where certified partners (ButterflyMX, Conservice, HappyCo, Knock, Lowe's, Property Meld, and many more) connect via the AppFolio Stack API. The Stack API is gated behind a partner application, security-compliance questionnaire, and terms-of-service signing; OAuth
  2.0, a sandbox environment, webhooks, and an OpenAPI/Swagger reference are made available only to approved partners through the developer.appfolio.com portal, so no public specification is reachable for catalog inclusion. AppFolio's revenue model is per-unit SaaS subscription plus value-added services (payments, screening, insurance, marketing). The AppFolio GitHub organization publishes internal Ruby on Rails, React, and tooling libraries (react-gears, ae_page_objects, store_base_sti_class) but no public API SDK, CLI, or OpenAPI artifact.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/appfolio.png
layout: provider
modified: '2026-10-20'
name: AppFolio
nav: Providers
network: true
overview: 'AppFolio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Property Management, Real Estate, Residential, Commercial, and Community Associations.


  AppFolio''s developer surface includes support, Stack Overflow tag, GitHub presence, engineering blog, pricing, YouTube channel, and 26 more developer resources.'
plans:
- name: Appfolio Plans Pricing
  plan_count: 3
  slug: appfolio-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 66.1
    operational_transparency: 13.2
  previous_composite: 30.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/appfolio/appfolio-2026-06-20T172316.png
security:
- kind: domain-security
  name: Appfolio Domain Security
  slug: appfolio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appfolio
tags:
- Property Management
- Real Estate
- Residential
- Commercial
- Community Associations
- HOA
- Multifamily
- Single-Family Rental
- Student Housing
- Affordable Housing
- Investment Management
- PropTech
- Software-as-a-Service
- Accounting
- Leasing
- Maintenance
- AI Agents
- Realm-X
- AppFolio Stack
website: https://www.appfolio.com
---
