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
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://offr.io/
- group: company
  title: ''
  type: About
  url: https://offr.io/about-us
- group: other
  title: ''
  type: HowItWorks
  url: https://offr.io/how-it-works
- group: commercial
  title: ''
  type: Pricing
  url: https://offr.io/pricing
- group: commercial
  title: ''
  type: Plans
  url: https://offr.io/plans
- group: start
  title: ''
  type: SignUp
  url: https://offr.io/register
- group: start
  title: ''
  type: Login
  url: https://offr.io/login
- group: operate
  title: ''
  type: Support
  url: https://offr.io/contact-us
- group: company
  title: ''
  type: Blog
  url: https://offr.io/articles
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://offr.io/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://offr.io/terms-and-conditions
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/offr-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/offr-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/offr-domain-security.yml
created: '2026-07-17'
description: Offr (Offr.io Ltd) is a Dublin-based property technology (proptech) platform that digitizes end-to-end real estate transactions. Estate and letting agents embed the Offr "offer panel" / button on their own website to run private-treaty sales, online auctions, tenders, lettings, and new-home sales - collecting verified offers and bids, scheduling viewings, managing a legal document vault with e-signing, taking secure deposits (via Stripe), and streaming live auction broadcasts, all with a fully auditable transaction trail. The platform serves residential and commercial agents, buyers, sellers, landlords, tenants, developers, and solicitors across Ireland, the UK, Europe, the USA, and Australia. Offr is a SaaS/embedded product; it exposes no public developer API, developer portal, or OpenAPI at this time and integrates DocuSign, Stripe, and AWS as a consumer. Surfaced as a Techstars portfolio company and enriched from public web sources.
image: https://cdn.offr.io/images/hero-background-card.jpg
layout: provider
modified: '2026-07-20'
name: Offr
nav: Providers
network: true
overview: 'Offr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, PropTech, Real-Estate, Property Transactions, and Auctions.


  Offr''s developer surface includes pricing, signup flow, support, engineering blog, and 10 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - ireland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 17.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/offr/refs/heads/main/screenshots/offr-2026-08-07T190026.png
security:
- kind: domain-security
  name: Offr Domain Security
  slug: offr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Offr Trust Center
  slug: offr-trust-center
  summary_line: trust center published
slug: offr
tags:
- Company
- PropTech
- Real-Estate
- Property Transactions
- Auctions
- Lettings
- Offer Management
- Ireland
website: https://offr.io/
---
