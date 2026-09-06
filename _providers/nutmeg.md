---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.nutmeg.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.personalinvesting.jpmorgan.com/ — a different registrable domain (nutmeg.com -> jpmorgan.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/jp-morgan-chase/
- group: company
  title: ''
  type: Website
  url: https://www.nutmeg.com/
- group: company
  title: ''
  type: Website
  url: https://www.personalinvesting.jpmorgan.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.personalinvesting.jpmorgan.com/about/our-fee
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.personalinvesting.jpmorgan.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.personalinvesting.jpmorgan.com/legal/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.personalinvesting.jpmorgan.com/insights
- group: operate
  title: ''
  type: Support
  url: https://support.personalinvesting.jpmorgan.com
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nutmeg-domain-security.yml
created: '2026-07-17'
description: 'Nutmeg is a UK digital wealth manager and robo-advisor founded in 2011 and acquired by JPMorgan Chase in 2021, now operating as J.P. Morgan Personal Investing. It offers consumer investment accounts including Stocks and Shares ISAs, Lifetime ISAs, Junior ISAs, personal pensions, and general investment accounts, with fully managed, Smart Alpha, socially responsible, thematic, fixed allocation, and income portfolio strategies plus free financial guidance and paid advice. Nutmeg is authorised and regulated by the UK Financial Conduct Authority (FCA register #552016). It is a consumer-facing wealth platform and does not publish a public developer API, OpenAPI specification, SDK, or developer portal.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nutmeg.png
layout: provider
modified: '2026-07-20'
name: Nutmeg (J.P. Morgan Personal Investing)
nav: Providers
network: true
overview: 'Nutmeg (J.P. Morgan Personal Investing) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wealth Management, Robo-Advisor, Investing, and Fintech.


  Nutmeg (J.P. Morgan Personal Investing)''s developer surface includes pricing, engineering blog, support, and 6 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 3
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
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 12.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nutmeg/refs/heads/main/screenshots/nutmeg-2026-08-07T185757.png
security:
- kind: domain-security
  name: Nutmeg Domain Security
  slug: nutmeg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nutmeg
tags:
- Company
- Wealth Management
- Robo-Advisor
- Investing
- Fintech
- Pensions
- ISA
- United Kingdom
website: https://www.nutmeg.com/
---
