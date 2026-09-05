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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.mealticket.com/
- group: company
  title: ''
  type: Blog
  url: https://www.mealticket.com/blog
- group: operate
  title: ''
  type: Support
  url: https://mealticket.my.site.com/helpcenter/s/
- group: operate
  title: ''
  type: HelpCenter
  url: https://mealticket.my.site.com/helpcenter/s/
- group: start
  title: ''
  type: Login
  url: https://login.mealticket.com/
- group: start
  title: ''
  type: Demo
  url: https://www.mealticket.com/get-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mealticket.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mealticket.com/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/meal-ticket-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/meal-ticket-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meal-ticket-domain-security.yml
created: '2026-07-17'
description: Meal Ticket is a Boise, Idaho-based SaaS company (founded 2011) delivering profitability management software for the foodservice supply chain. Its TrackMax+ platform helps food distributors and suppliers manage rebates, allowances, trade programs, payments, and operator-level intelligence at line-item detail, while its MarketMan platform provides AI-powered inventory and food-cost management to 15,000+ restaurant locations across 55+ countries. Meal Ticket serves 100+ distributors and suppliers and processes $40B+ in annual sales and rebate volume. The company operates as a customer-facing SaaS with a single-sign-on login surface (OpenID Connect) but does not publish a public developer API, developer portal, or API documentation.
image: https://cdn.prod.website-files.com/69bb9bea9c683b00952f085d/69bbbd9b487f6dacf569a385_main_logo.svg
layout: provider
modified: '2026-07-20'
name: Meal Ticket
nav: Providers
network: true
overview: 'Meal Ticket is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food Service, Foodservice Distribution, Restaurant, and Rebate Management.


  Meal Ticket''s developer surface includes engineering blog, support, authentication, and 8 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/meal-ticket/refs/heads/main/screenshots/meal-ticket-2026-08-07T172255.png
security:
- kind: authentication
  name: Meal Ticket Authentication
  slug: meal-ticket-authentication
  summary_line: openIdConnect · 1 scheme
- kind: domain-security
  name: Meal Ticket Domain Security
  slug: meal-ticket-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: meal-ticket
tags:
- Company
- Food Service
- Foodservice Distribution
- Restaurant
- Rebate Management
- Profitability Management
- Supply Chain
- Software-as-a-Service
website: https://www.mealticket.com/
---
