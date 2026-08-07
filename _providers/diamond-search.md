---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Diamond Search Agentic Access
  operation_count: 3
  slug: diamond-search-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 3
apis:
- description: The Fullfeed API from Diamond Search — 1 operation(s) for fullfeed.
  name: Diamond Search Fullfeed API
  slug: diamond-search-fullfeed-api
- description: The Getreport3 API from Diamond Search — 1 operation(s) for getreport3.
  name: Diamond Search Getreport3 API
  slug: diamond-search-getreport3-api
- description: The Labgrownfullfile API from Diamond Search — 1 operation(s) for labgrownfullfile.
  name: Diamond Search Labgrownfullfile API
  slug: diamond-search-labgrownfullfile-api
artifact_total: 12
collections:
- collection_type: open
  name: Diamond Search IDEX Data API - Report 3
  slug: open-idex-data-report-api
- collection_type: open
  name: Diamond Search Lab Grown Diamond Feed API
  slug: open-idex-lab-grown-file-api
- collection_type: open
  name: Diamond Search IDEX Onsite Full Feed API
  slug: open-idex-onsite-full-feed-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/diamond-search-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/diamond-search-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/diamond-search-authentication.yml
- group: company
  title: ''
  type: Newsroom
  url: http://www.idexonline.com/rssfeeds
- group: start
  title: ''
  type: Login
  url: https://www.idexonline.com/ns24/auth/login.aspx
- group: start
  title: ''
  type: Signup
  url: https://www.idexonline.com/register.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: http://www.idexonline.com/Privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: http://www.idexonline.com/Conditions
created: '2024-11-13'
description: IDEX Online is the leading polished diamonds trading platform for professionals, providing unbiased, market-driven diamond pricing tools, news and research. The IDEX Onsite and Data Report APIs deliver natural diamond, lab grown diamond, and market data feeds to subscribers of the IDEX trading platform.
finops:
- name: Diamond Search Finops
  service_category: Market Data / Diamond Trading
  slug: diamond-search-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/diamond-search.png
layout: provider
modified: '2026-05-19'
name: Diamond Search
nav: Providers
network: true
overview: 'Diamond Search publishes 3 APIs on the [APIs.io](https://apis.io/) network: Fullfeed API, Getreport3 API, and Labgrownfullfile API. Tagged areas include Diamonds, Lab Grown, Pricing, and Trading.


  Diamond Search''s developer surface includes authentication, signup flow, and 6 more developer resources.'
plans:
- name: Diamond Search Plans Pricing
  plan_count: 4
  slug: diamond-search-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 1
  name: Diamond Search Rate Limits
  slug: diamond-search-rate-limits
score:
  band: thin
  composite: 40.3
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 54.5
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 43.3
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/diamond-search/refs/heads/main/screenshots/diamond-search-2026-06-20T180003.png
security:
- kind: authentication
  name: Diamond Search Authentication
  slug: diamond-search-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Diamond Search Domain Security
  slug: diamond-search-domain-security
  summary_line: TLSv1.2 · DMARC
slug: diamond-search
tags:
- Diamonds
- Lab Grown
- Pricing
- Trading
---
