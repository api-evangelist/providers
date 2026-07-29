---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'SM Energy Company (NYSE: SM) financial and operational data is accessible through investor relations resources, SEC EDGAR filings, and third-party financial data providers. The company reports quarter'
  name: SM Energy Investor Data
  slug: investor-data
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sm-energy-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sm-energy-company
- group: company
  title: ''
  type: Website
  url: https://www.sm-energy.com
- group: company
  title: ''
  type: About
  url: https://www.sm-energy.com/about-us
- group: other
  title: ''
  type: FactSheet
  url: https://www.sm-energy.com/about-us/fact-sheet
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.sm-energy.com/investors
- group: operate
  title: ''
  type: PressReleases
  url: https://www.sm-energy.com/investors/news-events/press-releases
- group: other
  title: ''
  type: SECFilings
  url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=SM&type=10-K
- group: other
  title: ''
  type: OwnerRelations
  url: https://www.sm-energy.com/owner-relations
- group: other
  title: ''
  type: Sustainability
  url: https://www.sm-energy.com/esg
- group: design
  title: ''
  type: JSONLD
  url: json-ld/sm-energy-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sm-energy-vocabulary.yml
created: '2026-05-02'
description: 'SM Energy Company (NYSE: SM) is an independent oil and gas exploration and production company headquartered in Denver, Colorado. Founded in 1908 (originally as St. Mary Land & Exploration Company), SM Energy focuses on acquiring, exploring, developing, and producing crude oil, natural gas, and natural gas liquids (NGLs) from top-tier assets across the Permian Basin in West Texas and New Mexico, the Maverick Basin in South Texas, the DJ Basin in Colorado, and the Uinta Basin in northeast Utah. The company is a Fortune 1000 member with approximately 1,241 employees and average daily net production of 206.8 MBoe/d. SM Energy completed a merger with Civitas Resources in early 2026. The company does not offer a public developer API; investor data is accessible through financial data APIs and SEC EDGAR.'
finops:
- name: Sm Energy Finops
  service_category: Oil and Gas Exploration and Production
  slug: sm-energy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sm-energy.png
jsonld:
- class_count: 0
  name: Sm Energy Context
  property_count: 6
  slug: sm-energy-context
layout: provider
modified: '2026-05-02'
name: SM Energy
nav: Providers
network: true
overview: 'SM Energy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Oil and Gas, Energy, Exploration, Production, and Permian Basin.


  The SM Energy catalog on APIs.io includes 1 JSON-LD context.'
plans:
- name: Sm Energy Plans Pricing
  plan_count: 1
  slug: sm-energy-plans-pricing
press:
- date: '2026-05-25'
  title: SM ENERGY APPOINTS DR. ASHWIN VENKATRAMAN ...
  url: https://www.sm-energy.com/investors/news-events/press-releases/detail/342/sm-energy-appoints-dr-ashwin-venkatraman-to-the-companys-board-of-directors
- date: '2026-05-25'
  title: Operations
  url: https://www.sm-energy.com/operations
- date: '2026-05-25'
  title: SM Energy details Civitas merger and capital returns
  url: https://www.stocktitan.net/sec-filings/SM/def-14a-sm-energy-co-definitive-proxy-statement-27018c62b7d4.html
- date: '2026-05-25'
  title: Sustainability
  url: https://www.sm-energy.com/sustainability
- date: '2026-05-25'
  title: SM ENERGY ANNOUNCES ADDITIONAL DETAILS ON ...
  url: https://www.prnewswire.com/news-releases/sm-energy-announces-additional-details-on-planned-merger-with-civitas-and-participation-in-upcoming-investor-conferences-302617582.html
- date: '2026-05-06'
  title: SM Energy Reports First Quarter 2026 Results
  url: https://www.sm-energy.com/investors/news-events/press-releases/detail/376/sm-energy-reports-first-quarter-2026-results
- date: '2026-04-30'
  title: SM ENERGY CLOSES $950 MILLION SOUTH TEXAS DIVESTITURE; ANNOUNCES REDEMPTION OF ALL OUTSTANDING 2026 SENIOR NOTES
  url: https://www.sm-energy.com/investors/news-events/press-releases/detail/375/sm-energy-closes-950-million-south-texas-divestiture-announces-redemption-of-all-outstanding-2026-senior-notes
- date: '2026-04-07'
  title: SM Energy Schedules First Quarter 2026 Conference Call for May 7, 2026
  url: https://www.sm-energy.com/investors/news-events/press-releases/detail/374/sm-energy-schedules-first-quarter-2026-conference-call-for-may-7-2026
random_paper: 28
rate_limits:
- limit_count: 1
  name: Sm Energy Rate Limits
  slug: sm-energy-rate-limits
score:
  band: emerging
  composite: 17.3
  delta: -3.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 8.1
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 10.4
    operational_transparency: 21.1
  previous_composite: 20.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 14.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sm-energy/refs/heads/main/screenshots/sm-energy-2026-06-20T194032.png
security:
- kind: domain-security
  name: Sm Energy Domain Security
  slug: sm-energy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sm-energy
tags:
- Oil and Gas
- Energy
- Exploration
- Production
- Permian Basin
- Fortune 1000
website: https://www.sm-energy.com
---
