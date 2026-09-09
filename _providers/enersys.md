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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-08'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enersys-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/enersys
- group: company
  title: ''
  type: Website
  url: https://www.enersys.com
- group: build
  title: ''
  type: Tools
  url: https://bsp.enersys.com/bsp/logonScreen.do
- group: build
  title: ''
  type: Tools
  url: https://mptools.enersys.com/oem/
- group: build
  title: ''
  type: Tools
  url: https://mptools.enersys.com/carb/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/enersys-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/enersys-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/enersys-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/enersys-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/enersys-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://www.enersys.com/en/resources/enersys-pulse-weblog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.enersys.com/en/footer-pages/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.enersys.com/en/footer-pages/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://www.enersys.com/en/contact-us/
coverage:
  checked: '2026-09-06'
  detail: 'EnerSys ships real software as end-user products — the Xinx cloud battery-operations portal, the E-Connect app, the Battery Sizing Program and the CARB calculator — but publishes no developer surface for any of them: api/developer/developers/docs/apis.enersys.com do not resolve, and the Xinx portal''s only backend (/api/PowerBi, named in its own assets/appsettings.json) answers the Angular HTML shell to anonymous callers.'
  evidence:
  - status: 404
    url: https://www.enersys.com/openapi.json
  - status: 404
    url: https://xinx.enersys.com/swagger.json
  - status: 200
    url: https://xinx.enersys.com/api/PowerBi
  - status: 200
    url: https://www.enersys.com/en/sitemap.xml
  reason: no-developer-program
  state: none
created: '2026-03-24'
description: EnerSys is a global leader in stored energy solutions for industrial applications, manufacturing batteries, chargers, accessories, and outdoor equipment enclosures. EnerSys serves motive power, reserve power, aerospace and defense, and specialty markets. While EnerSys offers a number of customer-facing web tools (Battery Sizing Program, Motive Power configurator, CARB Compliance Calculator) and product-level telemetry such as the Wi-iQ battery monitoring system and NexSys iON connected fleet platform, no public developer APIs or open specifications have been published as of this index.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/enersys.png
layout: provider
modified: '2026-09-06'
name: EnerSys
nav: Providers
network: true
overview: 'EnerSys is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Batteries, Industrial, Energy Storage, and Fortune 1000.


  EnerSys'' developer surface includes tooling, engineering blog, support, and 12 more developer resources.'
plans:
- name: Enersys Plans Pricing
  plan_count: 0
  slug: enersys-plans-pricing
press:
- date: '2026-05-25'
  title: ENERSYS | Business Wire - Via Ritzau
  url: https://via.ritzau.dk/pressemeddelelse/13853379/enersys?publisherId=90456
- date: '2026-05-25'
  title: 'Data Centers in 2026: 5 Trends Reshaping Power, Cost ...'
  url: https://www.enersys.com/en/blog-articles/data-centers-five-trends-reshaping-power-cost-and-resilience/
- date: '2026-05-25'
  title: ENERSYS TECHNOLOGY ADVANCES DATA CENTRE ...
  url: https://investor.enersys.com/news/news-details/2025/ENERSYS-TECHNOLOGY-ADVANCES-DATA-CENTRE-BACKUP-POWER-MANAGEMENT-03-12-2025/default.aspx
- date: '2026-05-25'
  title: EnerSys Touts AI Data Center and Defense 'Super Cycles' ...
  url: https://www.theglobeandmail.com/investing/markets/stocks/ENS/pressreleases/1891809/enersys-touts-ai-data-center-and-defense-super-cycles-at-oppenheimer-conference/
- date: '2026-05-25'
  title: 'EnerSys: The Battery Company Sitting Right In The Middle ...'
  url: https://seekingalpha.com/article/4898339-enersysthe-battery-company-sitting-right-in-the-middle-of-the-ai-boom
random_paper: 0
rate_limits:
- limit_count: 0
  name: Enersys Rate Limits
  slug: enersys-rate-limits
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 9
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
    operational_transparency: 10.5
  previous_composite: 13.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 27.0
  schema_version: 0.20.0
  scored_at: '2026-09-08'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/enersys/refs/heads/main/screenshots/enersys-2026-06-20T180710.png
security:
- kind: domain-security
  name: Enersys Domain Security
  slug: enersys-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Enersys Vulnerability Disclosure
  slug: enersys-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: enersys
tags:
- Energy
- Batteries
- Industrial
- Energy Storage
- Fortune 1000
website: https://www.enersys.com
---
