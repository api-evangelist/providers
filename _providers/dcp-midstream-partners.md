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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
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
  score: 9.0
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dcp-midstream-partners-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dcp-midstream-partners-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dcp-midstream-partners-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dcp-midstream-partners-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dcp-midstream-partners-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dcp-midstream-partners-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dcp-midstream-partners-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dcp-midstream
- group: company
  title: ''
  type: Website
  url: https://www.phillips66.com/midstream/dcp/
- group: operate
  title: ''
  type: Support
  url: https://www.phillips66.com/midstream/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://p66.service-now.com/midstreamcsm
- group: start
  title: ''
  type: Login
  url: https://fits.ephillips66.com/
- group: company
  title: ''
  type: Blog
  url: https://www.phillips66.com/newsroom/category/midstream/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.phillips66.com/privacy-statement/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.phillips66.com/terms-and-conditions/
- group: start
  title: ''
  type: Customer Portal
  url: https://www.phillips66.com/midstream/customers/
- group: other
  title: ''
  type: Tariffs
  url: https://www.phillips66.com/midstream/tariffs/
- group: start
  title: ''
  type: Tax Portal
  url: https://www.phillips66.com/midstream/tax-portal/
- group: company
  title: ''
  type: Investor Relations
  url: https://investor.phillips66.com/
- group: other
  title: ''
  type: Sustainability
  url: https://www.phillips66.com/sustainability/
coverage:
  checked: '2026-09-05'
  detail: Phillips 66 runs real first-party software for DCP Midstream customers — FITS for wellhead and gathering data, TIPS/MyQuorum for allocations and revenue, Aligne for gas scheduling — but every one is an end-user web/mobile portal reached through an Azure AD B2C sign-in, and the Midstream customer-tools page that indexes them names no API, no data feed and no developer contact; the only machine-readable documents on the entire estate are the two OIDC discovery documents fronting those logins.
  evidence:
  - status: 200
    url: https://www.phillips66.com/midstream/customers/
  - status: 404
    url: https://www.phillips66.com/openapi.json
  - status: 404
    url: https://www.phillips66.com/.well-known/api-catalog
  - status: 200
    url: https://azrmdstadb2cr5.b2clogin.com/azrmdstadb2cr5.onmicrosoft.com/B2C_1A_FITS_SIGNUPSIGNIN/v2.0/.well-known/openid-configuration
  reason: no-developer-program
  state: none
created: '2025-01-08'
description: DCP Midstream Partners is a midstream energy company that gathers, processes, transports, stores, and markets natural gas and natural gas liquids (NGLs) across major U.S. producing regions. Following Phillips 66's acquisition of the remaining public units in 2023, DCP Midstream now operates as part of Phillips 66's midstream segment. The company does not publish a public developer API; integration with shippers and customers is handled through customer portals (tariffs, electronic flow measurement) rather than a self-service API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dcp-midstream-partners.png
layout: provider
modified: '2026-09-05'
name: DCP Midstream Partners
nav: Providers
network: true
overview: 'DCP Midstream Partners is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Midstream, Natural Gas, Natural Gas Liquids, and Oil and Gas.


  DCP Midstream Partners'' developer surface includes authentication, support, engineering blog, and 17 more developer resources.'
plans:
- name: Dcp Midstream Partners Plans Pricing
  plan_count: 0
  slug: dcp-midstream-partners-plans-pricing
press:
- date: '2026-05-25'
  title: 'DCP Midstream (DCP) Looks Good: Stock Adds 8.2% in Session'
  url: https://finance.yahoo.com/news/dcp-midstream-dcp-looks-good-124612103.html
- date: '2026-05-25'
  title: DCP Midstream Sinks $85M Into Texas Pipeline Project
  url: https://www.law360.com/articles/329514/dcp-midstream-sinks-85m-into-texas-pipeline-project
- date: '2026-05-25'
  title: XBRL Viewer
  url: https://www.sec.gov/ix?doc=/Archives/edgar/data/1338065/000133806520000019/dpm-20191231.htm
- date: '2026-05-25'
  title: Elliott Announces Director Candidates for the Board ...
  url: https://www.prnewswire.com/news-releases/elliott-announces-director-candidates-for-the-board-of-phillips-66-302391915.html
- date: '2026-05-25'
  title: DCP Midstream Benefits from Eagle Ford, DJ Basin Assets in ...
  url: https://www.industrialinfo.com/news/article/dcp-midstream-benefits-from-eagle-ford-dj-basin-assets-in-2014-puts-2015-growth-capex-at-300-million--246924
random_paper: 20
rate_limits:
- limit_count: 0
  name: Dcp Midstream Partners Rate Limits
  slug: dcp-midstream-partners-rate-limits
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 16.7
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 3.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 33.8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/dcp-midstream-partners/refs/heads/main/screenshots/dcp-midstream-partners-2026-06-20T175739.png
security:
- kind: authentication
  name: Dcp Midstream Partners Authentication
  slug: dcp-midstream-partners-authentication
  summary_line: openIdConnect · 2 schemes
- kind: domain-security
  name: Dcp Midstream Partners Domain Security
  slug: dcp-midstream-partners-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dcp-midstream-partners
tags:
- Energy
- Midstream
- Natural Gas
- Natural Gas Liquids
- Oil and Gas
- Pipelines
website: https://www.phillips66.com/midstream/dcp/
---
