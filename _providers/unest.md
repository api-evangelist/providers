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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unest-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unest.co
- group: agent
  title: ''
  type: WellKnown
  url: well-known/unest-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unest-llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://unest.co/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unest.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unest.co/privacy
- group: company
  title: ''
  type: Blog
  url: https://unest.co/insights
- group: operate
  title: ''
  type: Support
  url: https://unest.co/faq
- group: start
  title: ''
  type: SignUp
  url: https://web.unest.co
created: '2026-07-17'
description: UNest is a Los Angeles-based fintech app that helps parents and families save and invest for their children's futures through UTMA/UGMA custodial investment accounts, with brand rewards contributions, gifting, financial literacy content, and term life insurance offered through Ladder. UNest Advisers, LLC is an SEC-registered investment adviser, with brokerage through UNest Securities, LLC (FINRA/SIPC) and clearing through Apex Clearing. The company is a consumer mobile-app business and publishes no public developer API, though its site ships a real llms.txt. Surfaced as a 500 Global portfolio company in the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unest.png
layout: provider
modified: '2026-07-21'
name: UNest
nav: Providers
network: true
overview: 'UNest is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Investing, Custodial Accounts, and Savings.


  UNest''s developer surface includes pricing, engineering blog, support, signup flow, and 6 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 5
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unest/refs/heads/main/screenshots/unest-2026-09-02T164850.png
security:
- kind: domain-security
  name: Unest Domain Security
  slug: unest-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: unest
tags:
- Company
- Fintech
- Investing
- Custodial Accounts
- Savings
- Insurance
- Family Finance
website: https://unest.co
---
