---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Bloomberg Apis Agentic Access
  operation_count: 22
  slug: bloomberg-apis-agentic-access
  summary_line: 22 operations · 22 acting
api_count: 1
apis:
- description: Real-time and historical market data for equities, fixed income, commodities, and currencies.
  name: Bloomberg Market Data Feed
  slug: bloomberg-market-data-feed
- description: Access to Bloomberg's global news content, including articles, videos, and multimedia.
  name: Bloomberg News API
  slug: bloomberg-news-api
- description: Bulk data delivery service for historical and reference data.
  name: Bloomberg Data License API
  slug: bloomberg-data-license-api
- description: API Authorization Service — entitlements and identity
  name: Bloomberg APIs apiauth API
  slug: bloomberg-apis-apiauth-api
- description: API Field Information Service — discover and search Bloomberg fields
  name: Bloomberg APIs apiflds API
  slug: bloomberg-apis-apiflds-api
- description: Instruments Service — security/curve/government lookups
  name: Bloomberg APIs instruments API
  slug: bloomberg-apis-instruments-api
- description: Market Bar Subscription Service — streaming subscription
  name: Bloomberg APIs mktbar API
  slug: bloomberg-apis-mktbar-api
- description: Market Data Service — streaming subscription paradigm
  name: Bloomberg APIs mktdata API
  slug: bloomberg-apis-mktdata-api
- description: Custom VWAP Service — streaming subscription
  name: Bloomberg APIs mktvwap API
  slug: bloomberg-apis-mktvwap-api
- description: Page Data Service — GPGX page subscription
  name: Bloomberg APIs pagedata API
  slug: bloomberg-apis-pagedata-api
- description: Reference Data Service operations — request/response paradigm
  name: Bloomberg APIs refdata API
  slug: bloomberg-apis-refdata-api
- description: Technical Analysis Service — historical, intraday, and real-time studies
  name: Bloomberg APIs tasvc API
  slug: bloomberg-apis-tasvc-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Bloomberg API (BLPAPI) apiauth API
  slug: open-bloomberg-apis-apiauth-api
- collection_type: open
  name: Bloomberg API (BLPAPI) apiauth apiflds API
  slug: open-bloomberg-apis-apiflds-api
- collection_type: open
  name: Bloomberg API (BLPAPI) apiauth instruments API
  slug: open-bloomberg-apis-instruments-api
- collection_type: open
  name: Bloomberg API (BLPAPI) apiauth mktbar API
  slug: open-bloomberg-apis-mktbar-api
- collection_type: open
  name: Bloomberg API (BLPAPI) apiauth mktdata API
  slug: open-bloomberg-apis-mktdata-api
- collection_type: open
  name: Bloomberg API (BLPAPI) apiauth mktvwap API
  slug: open-bloomberg-apis-mktvwap-api
- collection_type: open
  name: Bloomberg API (BLPAPI) apiauth pagedata API
  slug: open-bloomberg-apis-pagedata-api
- collection_type: open
  name: Bloomberg API (BLPAPI) apiauth refdata API
  slug: open-bloomberg-apis-refdata-api
- collection_type: open
  name: Bloomberg API (BLPAPI) apiauth tasvc API
  slug: open-bloomberg-apis-tasvc-api
- collection_type: open
  name: Bloomberg API (BLPAPI)
  slug: open-bloomberg-blpapi
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/bloomberg/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bloomberg-apis-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/bloomberg-apis-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bloomberg-apis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bloomberg-apis-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.bloomberg.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bloomberg.com/professional/support/api-library/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomberg.com/notices/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomberg.com/notices/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.bloomberg.com/professional/support/
created: '2024-01-01'
description: Collection of Bloomberg's financial data and news APIs for accessing market data, news content, data licensing, and enterprise connectivity.
finops:
- name: Bloomberg Apis Finops
  service_category: API
  slug: bloomberg-apis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomberg-apis.png
layout: provider
modified: '2026-08-27'
name: Bloomberg APIs
nav: Providers
network: true
overview: 'Bloomberg APIs publishes 9 APIs on the [APIs.io](https://apis.io/) network, including apiauth API, apiflds API, instruments API, and 6 more. Tagged areas include Analytics, Financial Data, Market Data, News, and Terminal.


  Bloomberg APIs'' developer surface includes authentication, developer portal, getting-started guide, support, and 6 more developer resources.'
plans:
- name: Bloomberg Apis Plans Pricing
  plan_count: 3
  slug: bloomberg-apis-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Bloomberg Apis Rate Limits
  slug: bloomberg-apis-rate-limits
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 9
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 47.6
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 53.3
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomberg-apis/refs/heads/main/screenshots/bloomberg-apis-2026-06-20T173407.png
security:
- kind: authentication
  name: Bloomberg Apis Authentication
  slug: bloomberg-apis-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Bloomberg Apis Domain Security
  slug: bloomberg-apis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Bloomberg Apis Vulnerability Disclosure
  slug: bloomberg-apis-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bloomberg-apis
tags:
- Analytics
- Financial Data
- Market Data
- News
- Terminal
website: https://developer.bloomberg.com/
---
