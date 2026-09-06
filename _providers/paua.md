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
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Partner and Paua Pro APIs providing fleet charging data (charging history, costs, energy consumption, timestamps, network data across drivers and vehicles) and chargepoint location data for route plan
  name: Paua API
  slug: paua-api
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/paua-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/paua-lifecycle.yml
- group: company
  title: ''
  type: Website
  url: https://www.paua.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.paua.com/paua-apis
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paua.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.pauatech.com/register/
- group: start
  title: ''
  type: Login
  url: https://app.pauatech.com/PauaFleet/Login
- group: operate
  title: ''
  type: Support
  url: https://intercom.help/paua/en
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pauatech.com/
- group: company
  title: ''
  type: Blog
  url: https://www.paua.com/news-and-opinion
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.paua.com/downloads/paua-business-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.paua.com/privacy-policy
- group: operate
  title: ''
  type: ContactForm
  url: https://www.paua.com/contact-us
- group: company
  title: ''
  type: Jobs
  url: https://www.paua.com/jobs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pauatech/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/evpaua
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/pauaev/
created: '2026-07-17'
description: Paua is a UK business EV charging platform that consolidates public, home, and workplace electric-vehicle charging into a single EV charge card, driver app, and fleet dashboard, with one monthly invoice across the UK's 95,000+ charging connectors. Paua offers products including Paua Access, Paua Reimburse, Paua Share, Paua PRO, and Salary Sacrifice charging, and exposes partner and Paua Pro APIs for fleet charging data (charging history, costs, energy, timestamps) and chargepoint location data. API access is not public - it is provided to partners and Paua Pro customers after a technical discussion. Paua is backed by Seedcamp and Speedinvest.
image: https://cdn.prod.website-files.com/65aab0b75f6b00acccea258c/66aa444680a8796d987e510c_touch-icon.svg
layout: provider
modified: '2026-07-20'
name: Paua
nav: Providers
network: true
overview: 'Paua publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, EV Charging, Electric Vehicles, Fleet Management, and Mobility.


  Paua''s developer surface includes documentation, pricing, signup flow, support, engineering blog, and 12 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 18.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/paua/refs/heads/main/screenshots/paua-2026-08-07T191603.png
security:
- kind: domain-security
  name: Paua Domain Security
  slug: paua-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: paua
tags:
- Company
- EV Charging
- Electric Vehicles
- Fleet Management
- Mobility
- Payments
- Energy
- Charge Card
- United Kingdom
website: https://www.paua.com
---
