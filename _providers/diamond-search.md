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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Diamond Search Agentic Access
  operation_count: 3
  slug: diamond-search-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 3
apis:
- baseURL: https://api.idexonline.com/onsite/api
  baseurl_source: declared
  description: The Fullfeed API from Diamond Search — 1 operation(s) for fullfeed.
  name: Diamond Search Fullfeed API
  slug: diamond-search-fullfeed-api
- baseURL: https://api.idexonline.com/onsite/api
  baseurl_source: declared
  description: The Getreport3 API from Diamond Search — 1 operation(s) for getreport3.
  name: Diamond Search Getreport3 API
  slug: diamond-search-getreport3-api
- baseURL: https://api.idexonline.com/onsite/api
  baseurl_source: declared
  description: The Labgrownfullfile API from Diamond Search — 1 operation(s) for labgrownfullfile.
  name: Diamond Search Labgrownfullfile API
  slug: diamond-search-labgrownfullfile-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Diamond Search IDEX Data API - Report 3 Fullfeed API
  slug: open-diamond-search-fullfeed-api
- collection_type: open
  name: Diamond Search IDEX Data API - Report 3 Fullfeed Getreport3 API
  slug: open-diamond-search-getreport3-api
- collection_type: open
  name: Diamond Search IDEX Data API - Report 3 Fullfeed Labgrownfullfile API
  slug: open-diamond-search-labgrownfullfile-api
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
random_paper: 0
rate_limits:
- limit_count: 1
  name: Diamond Search Rate Limits
  slug: diamond-search-rate-limits
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 10
    catalog_gap: 72.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 47.8
    developer_ergonomics: 21.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 34.6
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
