---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
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
  score: 20.5
  scored_at: '2026-08-26'
api_count: 7
apis:
- description: A set of JSON RESTful web service APIs that provide access to product and instrument reference data for CME Group, BrokerTec, EBS, hosted partners, and CME Group-cleared markets. Supports OAuth-secure
  name: CME Reference Data API
  slug: cme-reference-data-api
- description: Real-time market data API delivering futures and options price, volume, and open-interest information across CME Group markets. Available via REST and WebSocket on a monthly subscription basis from th
  name: Real-Time Futures and Options Data API
  slug: real-time-futures-options-api
- description: JSON-over-REST API delivering CME Term SOFR Reference Rates - the IOSCO-compliant forward-looking term Secured Overnight Financing Rate at 1-month, 3-month, 6-month, and 12-month tenors - with real-ti
  name: CME Term SOFR API
  slug: cme-term-sofr-api
- description: 'REST API exposing the data behind the CME FedWatch Tool: market-implied probabilities of FOMC rate-change decisions derived from 30-Day Fed Funds futures pricing.'
  name: CME FedWatch API
  slug: fedwatch-api
- description: REST API delivering CME-calculated option Greeks (delta, gamma, vega, theta, rho) and implied volatility surfaces for CME Group options markets. JSON payloads accessed via the Data Services self-servi
  name: Greeks and Implied Volatility API
  slug: greeks-iv-api
- description: JSON-over-REST API delivering the CME-administered EUR/USD Cross Currency Basis Index with real-time updates and full history.
  name: EUR/USD Cross Currency Basis Index API
  slug: eurusd-basis-api
- description: The CME ClearPort API enables electronic submission of bilaterally negotiated OTC trades for clearing through CME ClearPort. Used by brokers, exchanges, and trading systems to automate trade submissio
  name: CME ClearPort API
  slug: cme-clearport-api
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cme-group-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CMEGroupPublic
- group: build
  title: ''
  type: Packages
  url: packages/cme-group-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/cme-group-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cme-group-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cme-group-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cme-group-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cme-group-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cme-group-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cme-group-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cme-group-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cme-group-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cme-group-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cme-group-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cme-group-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/cmegroup
- group: docs
  title: ''
  type: APIReference
  url: https://cmegroupclientsite.atlassian.net/wiki/display/EPICSANDBOX
- group: start
  title: ''
  type: SignUp
  url: https://login.cmegroup.com/sso/register/
- group: company
  title: ''
  type: Website
  url: https://www.cmegroup.com
- group: start
  title: ''
  type: Portal
  url: https://www.cmegroup.com/market-data/market-data-api.html
- group: start
  title: ''
  type: Portal
  url: https://dataservices.cmegroup.com/pages/CME-Data-Via-API
- group: docs
  title: ''
  type: Documentation
  url: https://cmegroupclientsite.atlassian.net/wiki/display/EPICSANDBOX
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cmegroup.com/tools-information/webhelp/data-services-portal/Content/Onboarding%20CME%20Group%20Cloud-Based%20Market%20Data%20APIs.html
- group: company
  title: ''
  type: About
  url: https://www.cmegroup.com/markets.html
- group: company
  title: ''
  type: About
  url: https://www.cmegroup.com/company/about-us.html
- group: operate
  title: ''
  type: Support
  url: https://www.cmegroup.com/contact-us.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cmegroup.com/disclaimer.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cmegroup.com/privacy-policy.html
- group: company
  title: ''
  type: Blog
  url: https://www.cmegroup.com/openmarkets.html
- group: other
  title: ''
  type: X
  url: https://twitter.com/CMEGroup
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cme-group/
created: '2026-03-23'
description: CME Group is the world's largest derivatives exchange and operator of the CME, CBOT, NYMEX, and COMEX markets, offering futures and options across interest rates, equity indexes, foreign exchange, energy, agricultural products, and metals. CME Group exposes a portfolio of REST and streaming APIs through its Data Services Portal - including CME Reference Data API, Real-Time Futures and Options Data API, CME Term SOFR API, FedWatch API, Greeks and Implied Volatility API, EUR/USD Cross Currency Basis Index API, the CME ClearPort API for OTC trade submission, and iLink/MDP 3.0 connectivity to CME Globex for execution and market data.
finops:
- name: Cme Group Finops
  service_category: Market Data / Exchange Connectivity
  slug: cme-group-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cme-group.png
layout: provider
modified: '2026-07-22'
name: CME Group
nav: Providers
network: true
overview: 'CME Group publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Capital Markets, Derivatives, Exchange, Financial Markets, and Futures.


  CME Group''s developer surface includes authentication, changelog, sandbox, API reference, signup flow, developer portal, documentation, and 24 more developer resources.'
plans:
- name: Cme Group Plans Pricing
  plan_count: 3
  slug: cme-group-plans-pricing
press:
- date: '2026-05-25'
  title: Market data policy education center
  url: https://www.cmegroup.com/market-data/license-data/market-data-policy-education-center.html
- date: '2026-05-25'
  title: 'CME Group''s AI Strategy: Analysis of Dominance in ...'
  url: https://www.klover.ai/cme-group-ai-strategy-analysis-of-dominance-in-financial-ai-commodities/
- date: '2026-05-25'
  title: CME Group and Silicon Data Launch Compute Futures ...
  url: https://www.linkedin.com/posts/carmenrli_today-were-announcing-that-cme-group-and-activity-7460040679461679106-zsyL
- date: '2026-05-25'
  title: CME Group and Google Cloud Announce New Chicago ...
  url: https://www.cmegroup.com/media-room/press-releases/2024/6/26/cme_group_and_googlecloudannouncenewchicagoareaprivatecloudregio.html
- date: '2026-05-25'
  title: CME Group and Silicon Data Partner to Launch First ...
  url: https://www.prnewswire.com/news-releases/cme-group-and-silicon-data-partner-to-launch-first-compute-futures-302769215.html
random_paper: 8
rate_limits:
- limit_count: 3
  name: Cme Group Rate Limits
  slug: cme-group-rate-limits
scopes:
- name: Cme Group Scopes
  scope_count: 5
  slug: cme-group-scopes
  summary_line: 5 scopes · clientCredentials
score:
  band: developing
  composite: 47.3
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 36.8
  previous_composite: 47.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 91.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cme-group/refs/heads/main/screenshots/cme-group-2026-06-20T174629.png
security:
- kind: authentication
  name: Cme Group Authentication
  slug: cme-group-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cme Group Domain Security
  slug: cme-group-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cme Group Vulnerability Disclosure
  slug: cme-group-vulnerability-disclosure
  summary_line: Hackerone · security.txt
slug: cme-group
tags:
- Capital Markets
- Derivatives
- Exchange
- Financial Markets
- Futures
- Market Data
- Options
- Reference Data
- Trading
- Fortune 1000
website: https://www.cmegroup.com
---
