---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.9
  scored_at: '2026-11-06'
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
- group: commercial
  href: https://artifacts.apis.io/diamond-search/plans/diamond-search-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/diamond-search-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/diamond-search/rate-limits/diamond-search-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/diamond-search-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/diamond-search/finops/diamond-search-finops.yml
  title: ''
  type: FinOps
  url: finops/diamond-search-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.idexonline.com/newsroom
- group: company
  title: ''
  type: Website
  url: https://www.idexonline.com/
- group: agent
  href: https://artifacts.apis.io/diamond-search/agentic-access/diamond-search-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/diamond-search-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/diamond-search/security/diamond-search-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diamond-search-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/diamond-search/authentication/diamond-search-authentication.yml
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
- has_sources: true
  method: generated
  name: Diamond Search Finops
  primary_unit: ''
  service_category: Market Data / Diamond Trading
  slug: diamond-search-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/diamond-search.png
layout: provider
modified: '2026-10-06'
name: Diamond Search
nav: Providers
network: true
overview: 'Diamond Search publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Fullfeed API, Getreport3 API, and Labgrownfullfile API. Tagged areas include Diamonds, Lab Grown, Pricing, and Trading.


  The Diamond Search catalog on APIs.io includes 1 Spectral governance ruleset.


  Diamond Search''s developer surface includes engineering blog, authentication, signup flow, and 10 more developer resources.'
plans:
- name: Diamond Search Plans Pricing
  plan_count: 4
  slug: diamond-search-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Diamond Search Rate Limits
  slug: diamond-search-rate-limits
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: Diamond Search API Rules
  rule_count: 38
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 1
  slug: diamond-search-rules
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 13.6
    contract_quality: 46.9
    developer_ergonomics: 23.8
    discoverability: 64.3
    operational_transparency: 5.3
  previous_composite: 33.5
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
    score: 24.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/diamond-search/diamond-search-2026-06-20T180003.png
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
website: https://www.idexonline.com/
---
