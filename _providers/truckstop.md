---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-08-30'
api_count: 8
apis:
- description: REST API for posting, updating, refreshing, and deleting loads on the Truckstop load board. Includes Load Boost for promoted visibility, pause/unpause for BIN loads, and tender management for booked l
  name: Truckstop Load Management API
  slug: truckstop-load-management-api
- description: API for carriers and brokers to search available loads on the Truckstop load board with filtering, sorting, and bulk detail retrieval.
  name: Truckstop Load Search API
  slug: truckstop-load-search-api
- description: API for managing carrier networks, including bulk add/update/remove by DOT number, preferred carrier lists, carrier groups, compliance status access, and carrier search within groups.
  name: Truckstop Carrier Network API
  slug: truckstop-carrier-network-api
- description: API for accessing predictive rate data including booked rate estimates and trendlines over 4-week and 36-month periods, posted rate estimates, and rate crowdsourcing submissions.
  name: Truckstop Rate Insights API
  slug: truckstop-rate-insights-api
- description: API for carrier risk analysis including single and multiple carrier risk reports by MC/DOT number, search by email or phone, RMIS certification status queries, and monitored carrier list management.
  name: Truckstop Risk Factor API
  slug: truckstop-risk-factor-api
- description: API for posting trucks with equipment options, searching posted trucks, viewing truck details individually and in bulk, deleting trucks, and accessing Hot Prospects hidden capacity search.
  name: Truckstop Truck Management API
  slug: truckstop-truck-management-api
- description: API for managing freight-related documents associated with loads and transactions on the Truckstop platform.
  name: Truckstop Document API
  slug: truckstop-document-api
- description: API for retrieving booked load details by Load ID, tender details by Tender ID, CSV exports of booked loads, and tenders by account for freight payment processing.
  name: Truckstop Booked Rates API
  slug: truckstop-booked-rates-api
artifact_total: 12
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truckstop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://truckstop.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.truckstop.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/truckstop
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/truckstop/
- group: company
  title: ''
  type: Blog
  url: https://truckstop.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://truckstop.com/product/load-board/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.truckstop.com/
- group: other
  title: ''
  type: X
  url: https://x.com/trckstopdotcom
- group: commercial
  title: ''
  type: Plans
  url: plans/truckstop-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/truckstop-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/truckstop-finops.yml
created: '2026-06-13'
description: Truckstop is a freight marketplace and load board platform offering a REST API for managing load postings, carrier searches, rate negotiation, and freight payment processing. The platform serves shippers, brokers, and carriers with tools for truck and lane searching, rate insights, carrier compliance monitoring, tender management, risk factor analysis, and document management. Founded in 1995 as the first load board on the internet, Truckstop provides API integrations requiring a signed Systems Integration Agreement (SIA) and supports both Resource Owner Password and Authorization Code OAuth 2.0 flows.
finops:
- name: Truckstop Finops
  service_category: ''
  slug: truckstop-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/truckstop.png
layout: provider
modified: '2026-06-13'
name: Truckstop
nav: Providers
network: true
overview: 'Truckstop publishes 1 API on the [APIs.io](https://apis.io/) network: Load Management API. Tagged areas include Freight, Load Board, Trucking, Logistics, and Freight Marketplace.


  Truckstop''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Truckstop Plans Pricing
  plan_count: 13
  slug: truckstop-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Truckstop Rate Limits
  slug: truckstop-rate-limits
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 7
    catalog_gap: 60.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 26.7
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 25.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/truckstop/refs/heads/main/screenshots/truckstop-2026-06-20T195750.png
security:
- kind: domain-security
  name: Truckstop Domain Security
  slug: truckstop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: truckstop
tags:
- Freight
- Load Board
- Trucking
- Logistics
- Freight Marketplace
- Carrier Search
- Rate Insights
- Transportation
- Brokers
- Shipper
website: https://truckstop.com/
---
