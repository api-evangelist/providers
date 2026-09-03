---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Live Nation Entertainment Agentic Access
  operation_count: 7
  slug: live-nation-entertainment-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://app.ticketmaster.com/discovery/v2
  baseurl_source: declared
  description: Search and retrieve attraction information.
  name: live-nation-entertainment Attractions API
  slug: live-nation-entertainment-attractions-api
- baseURL: https://app.ticketmaster.com/discovery/v2
  baseurl_source: declared
  description: Search and retrieve classification/genre information.
  name: live-nation-entertainment Classifications API
  slug: live-nation-entertainment-classifications-api
- baseURL: https://app.ticketmaster.com/discovery/v2
  baseurl_source: declared
  description: Search and retrieve event information.
  name: live-nation-entertainment Events API
  slug: live-nation-entertainment-events-api
- baseURL: https://app.ticketmaster.com/discovery/v2
  baseurl_source: declared
  description: Search and retrieve venue information.
  name: live-nation-entertainment Venues API
  slug: live-nation-entertainment-venues-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ticketmaster Discovery Attractions API
  slug: open-live-nation-entertainment-attractions-api
- collection_type: open
  name: Ticketmaster Discovery Attractions Classifications API
  slug: open-live-nation-entertainment-classifications-api
- collection_type: open
  name: Ticketmaster Discovery Attractions Events API
  slug: open-live-nation-entertainment-events-api
- collection_type: open
  name: Ticketmaster Discovery API
  slug: open-live-nation-entertainment-ticketmaster-discovery-api
- collection_type: open
  name: Ticketmaster Discovery Attractions Venues API
  slug: open-live-nation-entertainment-venues-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/live-nation-entertainment-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/live-nation-entertainment-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/live-nation-entertainment-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ticketmaster
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/live-nation
- group: company
  title: ''
  type: Blog
  url: https://newsroom.livenation.com/feed
description: Tap into the Ticketmaster open developer network which gives you the flexibility and scale to bring unforgettable live events to fans. It’s our technology – ...
finops:
- name: Live Nation Entertainment Finops
  service_category: Ticketing / Events
  slug: live-nation-entertainment-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/live-nation-entertainment.png
layout: provider
modified: '2026-05-19'
name: Live Nation Entertainment
nav: Providers
network: true
overview: 'Live Nation Entertainment publishes 4 APIs on the [APIs.io](https://apis.io/) network, including live-nation-entertainment Attractions API, live-nation-entertainment Classifications API, live-nation-entertainment Events API, and 1 more. Tagged areas include Fortune 500.


  Live Nation Entertainment''s developer surface includes authentication, engineering blog, and 4 more developer resources.'
plans:
- name: Live Nation Entertainment Plans Pricing
  plan_count: 3
  slug: live-nation-entertainment-plans-pricing
press:
- date: '2026-05-25'
  title: Live Nation Entertainment, Inc. (LYV) Presents at J.P. ...
  url: https://seekingalpha.com/article/4907113-live-nation-entertainment-inc-lyv-presents-at-j-p-morgan-54th-annual-global-technology-media
- date: '2026-05-25'
  title: Live Nation Entertainment Q1 Earnings Call Highlights
  url: https://www.theglobeandmail.com/investing/markets/stocks/LYV/pressreleases/1873250/live-nation-entertainment-q1-earnings-call-highlights/
- date: '2026-05-25'
  title: Live Nation Entertainment, Inc. Stock (LYV) - Quote Nyse
  url: https://www.marketscreener.com/quote/stock/LIVE-NATION-ENTERTAINMENT-13449/
- date: '2026-05-25'
  title: LIVE NATION ENTERTAINMENT FULL YEAR AND ...
  url: https://www.prnewswire.com/news-releases/live-nation-entertainment-full-year-and-fourth-quarter-2025-results-302693023.html
- date: '2026-05-25'
  title: Live Nation Entertainment Full Year And Fourth Quarter ...
  url: https://newsroom.livenation.com/news/live-nation-entertainment-full-year-and-fourth-quarter-2025-results/
random_paper: 15
rate_limits:
- limit_count: 2
  name: Live Nation Entertainment Rate Limits
  slug: live-nation-entertainment-rate-limits
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 12
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 23.8
    discoverability: 44.4
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 25.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/live-nation-entertainment/refs/heads/main/screenshots/live-nation-entertainment-2026-06-20T184616.png
security:
- kind: authentication
  name: Live Nation Entertainment Authentication
  slug: live-nation-entertainment-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Live Nation Entertainment Domain Security
  slug: live-nation-entertainment-domain-security
  summary_line: TLSv1.2 · DMARC
slug: live-nation-entertainment
tags:
- Fortune 500
---
