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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.1
  scored_at: '2026-09-05'
api_count: 5
apis:
- description: HTTPS REST access to OneTick Cloud market data and analytics queries, authenticated with an OAuth2 client-credentials Bearer token issued by the OneTick Keycloak realm (https://cloud-auth.parent.oneti
  name: OneTick Cloud REST API (WebAPI)
  slug: onetick-cloud-rest-api
- description: A pandas-like Python API for querying tick-by-tick market data in OneTick, published on PyPI as onetick-py with openly browsable documentation. Against OneTick Cloud it executes over the WebAPI transp
  name: OneTick Python API - onetick-py (pandas-style)
  slug: onetick-py-python-api
- description: The lower-level directed-graph-style Python query API for OneTick, composing event-processor graphs against tick series, with openly browsable documentation and worked examples on the OneTick Cloud si
  name: OneTick Python API - Directed Graph
  slug: onetick-python-directed-graph-api
- description: SQL querying over OneTick tick and reference data, documented openly and runnable against OneTick Cloud (including via otp.SqlQuery in onetick-py over the WebAPI transport).
  name: OneTick SQL API
  slug: onetick-sql-api
- description: Cloud API for extracting adjusted and unadjusted point-in-time quotes and trades at nanosecond precision across 200+ venues for transaction cost analysis, packaged for Python integration; marketed sal
  name: OneTick Point-in-Time TCA API
  slug: onetick-point-in-time-tca-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onetick-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/onetick-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/onetick-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/onetick-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/onetick-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/onetick-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/onetick-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/onetick-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/onetick-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/onetick-changelog.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pip.distribution.sol.onetick.com/static/getting_started/root.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pip.distribution.sol.onetick.com/api/root.html
- group: company
  title: ''
  type: Website
  url: https://www.onetick.com/
- group: start
  title: ''
  type: Portal
  url: https://authdash.cloud.onetick.com/web_dashboard/?dash=sub_profile
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pip.distribution.sol.onetick.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/onemarketdata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/onemarketdata
- group: company
  title: ''
  type: Blog
  url: https://blog.onetick.com/
- group: start
  title: ''
  type: SignUp
  url: https://cloud-auth.parent.onetick.com/realms/OMD/protocol/openid-connect/registrations?client_id=acf_onetick_cloud&scope=openid%20profile&redirect_uri=https://authdash.cloud.onetick.com/web_dashboard/j_security_check&response_type=code
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.onetick.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.onetick.com/privacy-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.onetick.com/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://www.onetick.com/cloud-services/system-availability
created: '2026-07-21'
description: OneTick, from OneMarketData, is an enterprise tick database and analytics platform for capital markets, capturing, storing, and analyzing trade, quote, and order-book time series at scale for quant research, transaction cost analysis, and trade surveillance. OneTick Cloud sells historical and reference market data covering 200+ global equities, options, and futures venues (history back to 1993, corporate actions, symbol cross-reference) delivered on demand through an OAuth2-secured REST WebAPI, a pandas-like Python API (onetick-py), a directed-graph Python API, SQL querying, and file delivery, with a self-serve trial registration. The detailed REST endpoint reference sits behind the cloud dashboard login. OneMarketData merged with KX in September 2025 under TA Associates ownership.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onetick.png
layout: provider
modified: '2026-07-22'
name: OneTick (OneMarketData)
nav: Providers
network: true
overview: 'OneTick (OneMarketData) publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Financial, Market Data, Tick Data, Historical Data, and Trading.


  OneTick (OneMarketData)''s developer surface includes authentication, changelog, getting-started guide, API reference, developer portal, documentation, engineering blog, and 16 more developer resources.'
random_paper: 14
scopes:
- name: Onetick Scopes
  scope_count: 28
  slug: onetick-scopes
  summary_line: 28 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 36.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 36.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 58.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onetick/refs/heads/main/screenshots/onetick-2026-07-22T202525.png
security:
- kind: authentication
  name: Onetick Authentication
  slug: onetick-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Onetick Domain Security
  slug: onetick-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: onetick
tags:
- Financial
- Market Data
- Tick Data
- Historical Data
- Trading
- Analytics
- Surveillance
- Time Series
- Equities
- Options
website: https://www.onetick.com/
---
