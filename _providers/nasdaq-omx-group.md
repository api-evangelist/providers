---
access_model:
  confidence: medium
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nasdaq Omx Group Agentic Access
  operation_count: 5
  slug: nasdaq-omx-group-agentic-access
  summary_line: 5 operations
api_count: 4
apis:
- description: REST API for retrieving Tables-style datasets, supporting filtering by column, query parameters, and large result sets via pagination or bulk download.
  name: Nasdaq Data Link Tables API
  slug: data-link-tables
- description: Streaming API providing real-time delivery of market data through persistent connections.
  name: Nasdaq Data Link Streaming API
  slug: data-link-streaming
- baseURL: https://data.nasdaq.com/api/v3
  baseurl_source: declared
  description: Databases that group related datasets.
  name: Nasdaq Databases API
  slug: nasdaq-omx-group-databases-api
- baseURL: https://data.nasdaq.com/api/v3
  baseurl_source: declared
  description: Time-series datasets and their metadata.
  name: Nasdaq Datasets API
  slug: nasdaq-omx-group-datasets-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nasdaq Data Link Databases API
  slug: open-nasdaq-omx-group-databases-api
- collection_type: open
  name: Nasdaq Data Link Databases Datasets API
  slug: open-nasdaq-omx-group-datasets-api
- collection_type: open
  name: Nasdaq Data Link API
  slug: open-nasdaq-omx-group
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nasdaq-omx-group-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nasdaq-omx-group-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nasdaq-omx-group-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nasdaq
- group: company
  title: ''
  type: Website
  url: https://www.nasdaq.com/
- group: start
  title: ''
  type: Portal
  url: https://data.nasdaq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.data.nasdaq.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.data.nasdaq.com/llms.txt
created: '2024-01-01'
description: Nasdaq is a global technology company serving capital markets and other industries, providing trading, clearing, exchange technology, listing, information, and public company services. Nasdaq Data Link offers REST APIs for accessing financial, economic, and alternative data.
finops:
- name: Nasdaq Omx Group Finops
  service_category: Market Data / Financial Data
  slug: nasdaq-omx-group-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nasdaq-omx-group.png
layout: provider
modified: '2026-05-19'
name: Nasdaq
nav: Providers
network: true
overview: 'Nasdaq publishes 2 APIs on the [APIs.io](https://apis.io/) network: Databases API and Datasets API. Tagged areas include Financial-Services, Capital Markets, Stock Exchange, Market Data, and Economics.


  Nasdaq''s developer surface includes authentication, developer portal, documentation, and 5 more developer resources.'
plans:
- name: Nasdaq Omx Group Plans Pricing
  plan_count: 4
  slug: nasdaq-omx-group-plans-pricing
press:
- date: '2026-05-25'
  title: NASDAQ OMX Selects Cisco Technology for High ...
  url: https://newsroom.cisco.com/c/r/newsroom/en/us/a/y2011/m07/nasdaq-omx-selects-cisco-technology-for-high-performance-options-trading-networks.html
- date: '2026-05-25'
  title: Invesco Expands Longstanding Partnership with Nasdaq ...
  url: https://www.prnewswire.com/news-releases/invesco-expands-longstanding-partnership-with-nasdaq-with-two-new-thematic-technology-etfs-301310370.html
- date: '2026-05-25'
  title: Rocket Fuel Inc. [FUEL] to Ring the NASDAQ Stock Market ...
  url: https://ir.nasdaq.com/news-releases/news-release-details/rocket-fuel-inc-fuel-ring-nasdaq-stock-market-opening-bell
- date: '2026-05-25'
  title: Amdocs CEO and President Eli Gelman rings the opening ...
  url: https://www.facebook.com/Amdocs/posts/amdocs-ceo-and-president-eli-gelman-rings-the-opening-bell-this-morning-at-the-n/10152476442936976/
- date: '2026-05-25'
  title: Nasdaq and Wall Street Executives Testify on Artificial ...
  url: https://www.c-span.org/program/house-committee/nasdaq-and-wall-street-executives-testify-on-artificial-intelligence/670205
random_paper: 2
rate_limits:
- limit_count: 11
  name: Nasdaq Omx Group Rate Limits
  slug: nasdaq-omx-group-rate-limits
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 49.0
    catalog_earned_first_party: 0.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 32.1
    discoverability: 88.9
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 33.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 30.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nasdaq-omx-group/refs/heads/main/screenshots/nasdaq-omx-group-2026-06-20T185958.png
security:
- kind: authentication
  name: Nasdaq Omx Group Authentication
  slug: nasdaq-omx-group-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nasdaq Omx Group Domain Security
  slug: nasdaq-omx-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nasdaq-omx-group
tags:
- Financial-Services
- Capital Markets
- Stock Exchange
- Market Data
- Economics
- Fortune 1000
website: https://www.nasdaq.com/
---
