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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: DataSignals is Yes Energy's REST API for automated access to its North American wholesale power market data — nodal prices, transmission, generation, outages, constraints, weather, and fuels — coverin
  name: Yes Energy DataSignals API
  slug: datasignals-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yes-energy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yes-energy-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/yes-energy-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/yes-energy-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/yes-energy-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/yes-energy-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yes-energy-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.yesenergy.com/
- group: other
  title: ''
  type: Products
  url: https://www.yesenergy.com/products
- group: operate
  title: ''
  type: Support
  url: https://www.yesenergy.com/support
- group: docs
  title: ''
  type: Documentation
  url: https://help.yesenergy.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.yesenergy.com/demo
- group: operate
  title: ''
  type: Contact
  url: https://www.yesenergy.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.yesenergy.com/packages
- group: operate
  title: ''
  type: StatusPage
  url: https://status.yesenergy.com/
- group: company
  title: ''
  type: Blog
  url: https://www.yesenergy.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.yesenergy.com/blog/rss.xml
- group: company
  title: ''
  type: News
  url: https://www.yesenergy.com/news
- group: company
  title: ''
  type: About
  url: https://www.yesenergy.com/about
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.yesenergy.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yes-energy/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@yes-energy
- group: company
  title: ''
  type: Partners
  url: https://www.yesenergy.com/partners/snowflake
- group: other
  title: ''
  type: DataMarketplace
  url: https://app.snowflake.com/marketplace/providers/GZSOZ71OEK/Yes%20Energy
created: '2026-07-27'
description: 'Yes Energy is a Boulder, Colorado power market data company serving the North American wholesale electricity markets — the seven ISOs and RTOs (ERCOT, PJM, MISO, CAISO, SPP, ISO-NE, NYISO) plus Canadian and Western markets. It aggregates, cleans, and enriches nodal locational marginal prices, FTR auction results, transmission and generation outages, real-time generation and flow telemetry, constraints, load, weather, and fuels data, and sells it through DataSignals (a REST API), DataSignals Cloud (Snowflake Secure Data Sharing), DataSignals Lake (bulk load into a customer warehouse), the PowerSignals and QuickSignals analyst front ends, EnCompass modeling, Live Power telemetry, Infrastructure Insights, Position Management, and bid-to-bill Submission Services. It sits in the private, commercial layer of the energy value chain: it does not generate, distribute, or retail electricity and it holds no consumer relationship — it resells and enriches public ISO/RTO market data to
  traders, IPPs, utilities, and asset developers. Its API posture is honestly closed: the DataSignals REST API is real and confirmed live at https://services.yesenergy.com/PS/rest/, but it answers every anonymous request with HTTP 401 and WWW-Authenticate Basic, and even the product documentation (help.yesenergy.com) redirects through services.yesenergy.com/PS/KnowledgeOwlAuthentication to a customer login. No public developer portal, no self-serve signup, no machine-readable specification, and no free tier are published. Home market is the United States. There is no consumer energy data mandate that applies to Yes Energy — it is not a utility, retailer, or metering agent, so Green Button, ESPI, and the Consumer Data Right are all out of scope — and while the underlying ISO/RTO market data is publicly available at the source, Yes Energy itself publishes none of it openly.'
image: https://www.yesenergy.com/hubfs/Favicon.png
layout: provider
modified: '2026-07-27'
name: Yes Energy
nav: Providers
network: true
overview: 'Yes Energy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, United States, Energy Markets, Electricity, and Grid.


  Yes Energy''s developer surface includes authentication, support, documentation, signup flow, pricing, engineering blog, product news, and 17 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 20.8
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 28.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/yes-energy/refs/heads/main/screenshots/yes-energy-2026-09-02T171246.png
security:
- kind: authentication
  name: Yes Energy Authentication
  slug: yes-energy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Yes Energy Domain Security
  slug: yes-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: yes-energy
tags:
- Energy
- United States
- Energy Markets
- Electricity
- Grid
- Market Data
- Wholesale Power
- ISO RTO
- Renewables
- Trading
website: https://www.yesenergy.com/
---
