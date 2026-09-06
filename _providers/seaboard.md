---
access_model:
  confidence: high
  label: No API access model — EDI trading-partner agreement only
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.seaboardmarine.com/edi-request/
  - plans (plan_count 0)
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
  scored_at: '2026-09-05'
api_count: 1
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Seaboard Corporation API
  slug: open-seaboard
common:
- group: company
  title: ''
  type: Website
  url: https://www.seaboardcorp.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/seaboard-corporation
- group: company
  title: ''
  type: Blog
  url: https://www.seaboardcorp.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.seaboardcorp.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://www.seaboardcorp.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.seaboardcorp.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.seaboardcorp.com/privacy-policy/
- group: design
  title: ''
  type: Conformance
  url: conformance/seaboard-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seaboard-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/seaboard-llms.txt
coverage:
  checked: '2026-09-04'
  detail: Seaboard Corporation is a physical-goods holding company (pork, grain, ocean freight, renewable diesel, power generation) and ships no software product; the only machine-to-machine surface anywhere in the group is Seaboard Marine's batch EDI program, whose public page enumerates twelve ANSI X12 transaction sets and nine UN/EDIFACT messages but no HTTP API, and every spec and .well-known path probed across seaboardcorp.com, seaboardmarine.com, seaboardfoods.com and the MySeaboard portal returned 404 or a login redirect.
  evidence:
  - status: 404
    url: https://www.seaboardcorp.com/openapi.json
  - status: 404
    url: https://www.seaboardmarine.com/openapi.json
  - status: 404
    url: https://www.seaboardcorp.com/.well-known/agent-card.json
  - status: 302
    url: https://myseaboard.seaboardmarine.com/.well-known/oauth-authorization-server
  - status: 200
    url: https://www.seaboardmarine.com/services/electronic-data-interchange/
  reason: not-a-software-company
  state: none
created: '2026-05-22'
description: Seaboard Corporation is a diversified global agribusiness and transportation holding company headquartered in Merriam, Kansas, operating through Seaboard Foods (pork production and processing), Seaboard Marine (containerized ocean cargo between the United States, the Caribbean, and Central and South America), Seaboard Overseas and Trading Group (grain merchandising and milling), Seaboard Energy (renewable diesel), Transcontinental Capital Corporation (electric power generation in the Dominican Republic), Mount Dora Farms, and a minority interest in Butterball. Seaboard publishes no public developer API or developer portal; its only documented machine-to-machine integration surface is the Seaboard Marine Electronic Data Interchange program, which publishes an ANSI ASC X12 and UN/EDIFACT transaction-set catalog and onboards trading partners through a request form.
finops:
- name: Seaboard Finops
  service_category: API
  slug: seaboard-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/seaboard.png
layout: provider
modified: '2026-09-04'
name: Seaboard
nav: Providers
network: true
overview: 'Seaboard publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Agribusiness, Ocean Transportation, Container Shipping, and Pork Production.


  Seaboard''s developer surface includes engineering blog, support, and 8 more developer resources.'
plans:
- name: Seaboard Plans Pricing
  plan_count: 0
  slug: seaboard-plans-pricing
press:
- date: '2026-05-25'
  title: Daniel Allum - Director of Business Intelligence at ...
  url: https://www.linkedin.com/in/daniel-allum-b263146
- date: '2026-05-25'
  title: Seaboard Corporation Report of Earnings and Dividend ...
  url: https://www.gurufocus.com/news/1416006/seaboard-corporation-report-of-earnings-and-dividend-declaration?mobile=true%3Fmobile%3Dtrue&mobile=true%3Fmobile%3Dtrue%3Fmobile%3Dtrue&mobile=true&mobile=true
- date: '2026-05-25'
  title: AI Could Set a New Bar for Designing Hurricane-Resistant ...
  url: https://www.nist.gov/news-events/news/2023/03/ai-could-set-new-bar-designing-hurricane-resistant-buildings
- date: '2026-05-25'
  title: SEABOARD CORPORATION REPORT OF EARNINGS ...
  url: https://www.prnewswire.com/news-releases/seaboard-corporation-report-of-earnings-and-dividend-declaration-302686932.html
- date: '2026-05-25'
  title: 'Roli Seaboard RISE 2: The 200 Best Inventions of 2022'
  url: https://time.com/collections/best-inventions-2022/6225464/roli-seaboard-rise-2/
- date: '2024-07-30'
  title: 'By: EARNINGS REPORT 2ND QUARTER 2024 | Seaboard'
  url: https://www.seaboardcorp.com/investors/#comment-119
- date: '2023-10-30'
  title: 'By: EARNINGS REPORT 3RD QUARTER 2023 | Seaboard'
  url: https://www.seaboardcorp.com/investors/#comment-107
- date: '2023-08-01'
  title: 'By: EARNINGS REPORT 2ND QUARTER 2023 | Seaboard'
  url: https://www.seaboardcorp.com/investors/#comment-104
random_paper: 14
rate_limits:
- limit_count: 0
  name: Seaboard Rate Limits
  slug: seaboard-rate-limits
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
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
  previous_composite: 13.1
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 25.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Seaboard Domain Security
  slug: seaboard-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: seaboard
tags:
- Fortune 500
- Agribusiness
- Ocean Transportation
- Container Shipping
- Pork Production
- Commodity Trading
- Grain Milling
- Power Generation
- Logistics
- EDI
website: https://www.seaboardcorp.com
---
