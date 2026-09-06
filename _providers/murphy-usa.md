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
- group: company
  title: ''
  type: Website
  url: https://www.murphyusa.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/murphyusa
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.murphyusa.com/murphyusa/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.murphyusa.com/murphyusa/legal#privacy-a
- group: operate
  title: ''
  type: Support
  url: https://www.murphyusa.com/murphyusa/Contact-Us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.murphyusa.com/murphyusa/faqs
- group: auth
  title: ''
  type: DomainSecurity
  url: security/murphy-usa-domain-security.yml
coverage:
  checked: '2026-08-28'
  detail: Murphy USA runs its consumer surface on a Kentico CMS that 404s every spec path and 403s the entire /.well-known/ prefix on all three hosts, has no api. or developer. subdomain in DNS, and no GitHub organization — the only programmatic surface is the private backend of the Murphy Drive Rewards mobile app.
  evidence:
  - status: 404
    url: https://www.murphyusa.com/openapi.json
  - status: 403
    url: https://www.murphyusa.com/.well-known/api-catalog
  - status: 404
    url: https://www.murphyusa.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/murphyusa
  - status: 200
    url: https://www.murphy-usa.com/
  reason: no-developer-program
  state: none
created: '2026-03-21'
description: 'Murphy USA (NYSE: MUSA) is a Fortune 500 retailer of gasoline and convenience merchandise, headquartered in El Dorado, Arkansas. The company operates roughly 1,700 Murphy USA and Murphy Express stores across a 27-state footprint in the southern and midwestern United States, most of them sited in or adjacent to Walmart Supercenter parking lots, and it also owns the QuickChek chain of fresh convenience stores in New Jersey and New York. Its fuel slate spans E-10, E-15, FlexFuel (E85), ethanol-free E0, ULSD diesel, biodiesel and winterized diesel, marketed alongside a FuelAssure fuel-quality monitoring program. Consumer digital engagement runs through the Murphy Drive Rewards loyalty app and a Business Fuel Card program. Murphy USA publishes no public developer program, API reference or machine-readable contract.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/murphy-usa.png
layout: provider
modified: '2026-08-28'
name: Murphy USA
nav: Providers
network: true
overview: 'Murphy USA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Fuel Retail, Convenience Stores, Gas Stations, and Retail.


  Murphy USA''s developer surface includes support and 6 more developer resources.'
press:
- date: '2026-05-25'
  title: Murphy USA signals 45 to 55 new sites in 2026 while ...
  url: https://seekingalpha.com/news/4583125-murphy-usa-signals-45-to-55-new-sites-in-2026-while-keeping-guidance-unchanged-amid-fuel
- date: '2026-05-25'
  title: Murphy USA Inc (MUSA-N) Press Releases
  url: https://www.theglobeandmail.com/investing/markets/stocks/MUSA-N/pressreleases/
- date: '2026-05-25'
  title: 'From Manual to Strategic: Murphy USA''s IR Transformation'
  url: https://q4blog.com/how-murphy-usa-unlocked-their-full-potential-with-q4/
- date: '2026-05-25'
  title: Murphy USA Q1 2026 earnings preview
  url: https://www.msn.com/en-us/money/savingandinvesting/murphy-usa-q1-2026-earnings-preview/ar-AA21X21Z?ocid=finance-verthp-feeds
- date: '2026-05-25'
  title: How Murphy USA is gearing up for the future
  url: https://www.cstoredive.com/news/how-murphy-usa-is-gearing-up-for-the-future/709562/
random_paper: 1
score:
  band: minimal
  composite: 10.8
  coverage:
    artifact_dirs: 7
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
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/murphy-usa/refs/heads/main/screenshots/murphy-usa-2026-06-20T185903.png
security:
- kind: domain-security
  name: Murphy Usa Domain Security
  slug: murphy-usa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: murphy-usa
tags:
- Fortune 500
- Fuel Retail
- Convenience Stores
- Gas Stations
- Retail
- Loyalty Programs
- Energy
website: https://www.murphyusa.com
---
