---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Sec Api Agentic Access
  operation_count: 7
  slug: sec-api-agentic-access
  summary_line: 7 operations · 5 acting
api_count: 1
apis:
- baseURL: wss://stream.sec-api.io
  baseurl_source: declared
  description: Real-time, push-based WebSocket feed of newly published SEC EDGAR filings. Connect to wss://stream.sec-api.io with an API key and receive a stringified JSON array of filing metadata objects the moment
  name: SEC API Filing Stream API
  slug: sec-api-filing-stream-api
- baseURL: https://api.sec-api.io
  baseurl_source: declared
  description: Extract textual sections (items) from 10-K, 10-Q, and 8-K filings.
  name: SEC API Extractor API
  slug: sec-api-extractor-api
- baseURL: https://api.sec-api.io
  baseurl_source: declared
  description: Search 18M+ EDGAR filings by metadata using Lucene syntax.
  name: SEC API Filing Query API
  slug: sec-api-filing-query-api
- baseURL: https://api.sec-api.io
  baseurl_source: declared
  description: Institutional investment manager holdings and cover pages.
  name: SEC API Form 13F API
  slug: sec-api-form-13f-api
- baseURL: https://api.sec-api.io
  baseurl_source: declared
  description: Keyword and phrase search over filing bodies and exhibits since 2001.
  name: SEC API Full-Text Search API
  slug: sec-api-full-text-search-api
- baseURL: https://api.sec-api.io
  baseurl_source: declared
  description: Structured insider transactions from Form 3, 4, and 5.
  name: SEC API Insider Trading API
  slug: sec-api-insider-trading-api
- baseURL: https://api.sec-api.io
  baseurl_source: declared
  description: Convert XBRL financial data in filings to standardized JSON.
  name: SEC API XBRL API
  slug: sec-api-xbrl-api
artifact_total: 23
asyncapis:
- description: AsyncAPI 2.6 description of the SEC API (sec-api.io) **Filing Stream API**, a documented public **WebSocket** surface. Per https://sec-api.io/docs/stream-api, clients open a raw WebSocket connection (
  name: SEC API Filing Stream (WebSocket)
  slug: sec-api-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SEC API (sec-api.io) REST Extractor API
  slug: open-sec-api-extractor-api
- collection_type: open
  name: SEC API (sec-api.io) REST Extractor Filing Query API
  slug: open-sec-api-filing-query-api
- collection_type: open
  name: SEC API (sec-api.io) REST Extractor Form 13F API
  slug: open-sec-api-form-13f-api
- collection_type: open
  name: SEC API (sec-api.io) REST Extractor Full-Text Search API
  slug: open-sec-api-full-text-search-api
- collection_type: open
  name: SEC API (sec-api.io) REST Extractor Insider Trading API
  slug: open-sec-api-insider-trading-api
- collection_type: open
  name: SEC API (sec-api.io) REST Extractor XBRL API
  slug: open-sec-api-xbrl-api
- collection_type: open
  name: SEC API (sec-api.io) REST API
  slug: open-sec-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sec-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sec-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sec-api-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sec-api-io
- group: company
  title: ''
  type: Website
  url: https://sec-api.io
- group: docs
  title: ''
  type: Documentation
  url: https://sec-api.io/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/sec-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sec-api-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sec-api-finops.yml
created: '2026-07-11'
description: SEC API (sec-api.io) is a commercial developer platform that turns the U.S. Securities and Exchange Commission's EDGAR system into a fast, queryable REST and real-time streaming API. It covers 18+ million filings back to 1993 across 400+ EDGAR form types, with a Lucene-based Filing Query API, a Full-Text Search API over filing bodies and exhibits since 2001, an XBRL-to-JSON financial statement converter, a section Extractor for 10-K/10-Q/8-K, and structured datasets for insider trading (Form 3/4/5), institutional holdings (Form 13F), 13D/13G, Form D, Form ADV, IPOs, and more. A real-time Filing Stream API pushes newly published filings to clients over a WebSocket connection as soon as they hit EDGAR. Access is via a single API token passed as an Authorization header or a token query parameter.
finops:
- name: Sec Api Finops
  service_category: Financial Data and Regulatory Filings
  slug: sec-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sec-api.png
layout: provider
modified: '2026-07-11'
name: SEC API
nav: Providers
network: true
overview: 'SEC API publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Filing Stream API, Extractor API, Filing Query API, and 4 more. Tagged areas include SEC Filings, Regulatory Filings, EDGAR, Financial Data, and Compliance.


  The SEC API catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  SEC API''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Sec Api Plans Pricing
  plan_count: 4
  slug: sec-api-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 8
  name: Sec Api Rate Limits
  slug: sec-api-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: SEC API API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: sec-api-asyncapi-spectral-rules
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 68.5
    catalog_earned_first_party: 0.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 13.6
    contract_quality: 62.9
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 31.6
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 30.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sec-api/refs/heads/main/screenshots/sec-api-2026-08-17T081743.png
security:
- kind: authentication
  name: Sec Api Authentication
  slug: sec-api-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Sec Api Domain Security
  slug: sec-api-domain-security
  summary_line: TLSv1.3
slug: sec-api
tags:
- SEC Filings
- Regulatory Filings
- EDGAR
- Financial Data
- Compliance
- Government Reports
- Insider Trading
- 13F
- XBRL
- Full-Text Search
website: https://sec-api.io
---
