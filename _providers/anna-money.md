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
  url: security/anna-money-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.anna.money/
- group: company
  title: ''
  type: Blog
  url: https://anna.money/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://anna.money/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anna.money/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anna.money/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anna-money
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/annamoneyuk
- group: operate
  title: ''
  type: Support
  url: https://anna.money/help/
- group: start
  title: ''
  type: SignUp
  url: https://anna.money/sign-up/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anna-money-llms.txt
created: '2026-07-23'
description: 'ANNA Money (a trading name of Absolutely No Nonsense Admin Ltd, company number 10149389, Cardiff, a subsidiary of ANNA Holdings Ltd) is a UK digital business account and tax app for freelancers, startups, and small businesses, positioned as a challenger to the high-street banks. ANNA is not a bank but an e-money proposition: its Mastercard and e-money services are issued by PayrNet Limited, authorised by the Financial Conduct Authority for electronic money service activities (FCA FRN 900594), and its Account Information Services are provided under agency of TrueLayer (FCA FRN 901096). Within UK Open Banking, ANNA is a consumer / third-party provider (TPP) rather than an account-holding ASPSP or a CMA9 mandated bank - it uses TrueLayer''s Data and Payments APIs for external account aggregation, automatic VAT calculation, and QR-code "pay by bank" collection. ANNA publishes no public developer portal, no Open Data API, and no OBIE Read/Write (AIS/PIS/CBPII) API surface of its
  own; its public GitHub organisation hosts open-source engineering tooling (asyncio, aiohttp, and Postgres libraries) rather than product APIs.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: ANNA Money
nav: Providers
network: true
overview: 'ANNA Money is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, Fintech, Business Account, and Open Banking.


  ANNA Money''s developer surface includes engineering blog, pricing, support, signup flow, and 7 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 14.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anna-money/refs/heads/main/screenshots/anna-money-2026-07-25T200301.png
security:
- kind: domain-security
  name: Anna Money Domain Security
  slug: anna-money-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anna-money
tags:
- Financial-Services
- Banking
- Fintech
- Business Account
- Open Banking
- PSD2
- Account Information
- Payments
- E-Money
- United Kingdom
- SME
website: https://www.anna.money/
---
