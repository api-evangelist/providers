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
  url: security/lamudi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lamudi.com.ph/
- group: company
  title: ''
  type: Website
  url: https://www.lamudi.co.id/
- group: company
  title: ''
  type: Website
  url: https://www.lamudi.com.mx/
- group: company
  title: ''
  type: Blog
  url: https://www.lamudi.com.ph/journal/
- group: start
  title: ''
  type: SignUp
  url: https://pro.lamudi.com/?country=ph
- group: start
  title: ''
  type: Login
  url: https://pro.lamudi.com/login
- group: operate
  title: ''
  type: Support
  url: https://www.lifullconnect.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lifullconnect.com/legal-notice-direct/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lifullconnect.com/global-privacy-policy-region2/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lamudi-ph-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lamudi-id-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lamudi-mx-llms.txt
created: '2026-07-17'
description: Lamudi is an online real estate classifieds marketplace focused exclusively on emerging markets, founded in 2013 and today operating consumer property portals in the Philippines (lamudi.com.ph), Indonesia (lamudi.co.id) and Mexico (lamudi.com.mx). The platform lets buyers, renters, sellers and landlords search and list houses, condominiums/apartments, land, commercial space and offices, filtered by geography, property group and operation (buy/rent). Search results pages carry area market statistics, interactive maps and nearby points of interest, alongside country-specific features such as Philippine foreclosures and home-loan comparison, Indonesian KPR mortgage simulators, and Mexican Infonavit-eligible listings and bank repossessions. Agencies and developers publish inventory through the pro.lamudi.com professional portal. Lamudi operates as part of LIFULL Connect, which supplies its legal notice, privacy policy and contact surface. Lamudi publishes no public developer API,
  SDK or developer portal; its notable machine-readable surface is a first-party llms.txt on each country site that documents the URL grammar of its search, new development and project pages for AI agents.
image: https://multimedia.lamudi.com/lamudi/common/images/favicon.ico
layout: provider
modified: '2026-07-19'
name: Lamudi
nav: Providers
network: true
overview: 'Lamudi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Real-Estate, Property, and Classifieds.


  Lamudi''s developer surface includes engineering blog, signup flow, support, and 10 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - indonesia
    - mexico
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
    - southeast-asia
  previous_composite: 14.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lamudi/refs/heads/main/screenshots/lamudi-2026-07-25T224449.png
security:
- kind: domain-security
  name: Lamudi Domain Security
  slug: lamudi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lamudi
tags:
- Company
- Marketplace
- Real-Estate
- Property
- Classifieds
- Emerging Markets
- Philippines
- Indonesia
- Mexico
- Listings
website: https://www.lamudi.com.ph/
---
