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
  url: security/service-corp-international-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scicorp
- group: company
  title: ''
  type: Website
  url: https://www.sci-corp.com
- group: company
  title: ''
  type: Blog
  url: https://news.sci-corp.com/news-releases
- group: company
  title: ''
  type: BlogRSS
  url: https://investors.sci-corp.com/news?pagetemplate=rss
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sci-corp.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sci-corp.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://www.sci-corp.com/contact-us
coverage:
  checked: '2026-09-04'
  detail: Service Corporation International sells funeral, cremation and cemetery services through physical locations, not software — developer.sci-corp.com, developers.sci-corp.com, api.sci-corp.com, docs.sci-corp.com and api.dignitymemorial.com are all NXDOMAIN, there is no GitHub organization under any SCI or Dignity Memorial name, and the only /api/ namespace on the brand sites is the one dignitymemorial.com's own robots.txt labels internal.
  evidence:
  - status: 0
    url: https://api.sci-corp.com/
  - status: 404
    url: https://api.github.com/orgs/sci-corp
  - status: 404
    url: https://www.sci-corp.com/.well-known/api-catalog
  - status: 404
    url: https://www.sci-corp.com/llms.txt
  - status: 403
    url: https://www.dignitymemorial.com/api/v1/openapi.json
  - status: 200
    url: https://www.sci-corp.com/robots.txt
  reason: not-a-software-company
  state: none
created: '2026-05-25'
description: 'Service Corporation International (NYSE: SCI), headquartered in Houston, Texas, is North America''s leading provider of deathcare products and services, owning and operating funeral homes and cemeteries across the United States and Canada. SCI markets its network under the Dignity Memorial brand, alongside Neptune Society and National Cremation, and sells funeral and cemetery services on both an at-need and a preneed basis. It publishes no developer program, no API documentation and no machine-readable API contract.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/service-corp-international.png
layout: provider
modified: '2026-09-04'
name: Service Corp International
nav: Providers
network: true
overview: 'Service Corp International is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 1000, Deathcare, Funeral Services, Cemeteries, and Cremation.


  Service Corp International''s developer surface includes engineering blog, support, and 6 more developer resources.'
press:
- date: '2026-05-25'
  title: SERVICE CORP INTERNATIONAL SEC 10-K Report
  url: https://www.tradingview.com/news/tradingview:3b11fe766b384:0-service-corp-international-sec-10-k-report/
- date: '2026-05-25'
  title: SERVICE CORP INTERNATIONAL (SCI) SEC Filings
  url: https://moneysense.ai/sec-filings/company/sci
- date: '2026-05-25'
  title: Service Corporation International (SCI) Stock Price, News ...
  url: https://finance.yahoo.com/quote/SCI/
- date: '2026-05-25'
  title: Service Corp International (SCI) Q1 2024 Earnings
  url: https://www.gurufocus.com/news/2424291/service-corp-international-sci-q1-2024-earnings-aligns-with-eps-projections-amidst-revenue-growth?mobile=true%3Fmobile%3Dtrue&mobile=true%3Fmobile%3Dtrue%3Fmobile%3Dtrue&mobile=true&mobile=true
- date: '2026-05-25'
  title: Service Corporation International at 47th Annual Raymond ...
  url: https://www.investing.com/news/transcripts/service-corporation-international-at-47th-annual-raymond-james-strategic-insights-93CH-4538716
random_paper: 12
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 10.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Service Corp International Domain Security
  slug: service-corp-international-domain-security
  summary_line: TLSv1.3
slug: service-corp-international
tags:
- Fortune 1000
- Deathcare
- Funeral Services
- Cemeteries
- Cremation
- Consumer Services
website: https://www.sci-corp.com
---
