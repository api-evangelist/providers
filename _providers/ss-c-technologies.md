---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: SS&C's corporate API management portal, where clients register applications, request access to SS&C API products and manage consumers against a Kong gateway. The API catalog itself is behind authentic
  name: SS&C APIM Developer Portal
  slug: ssc-apim-developer-portal
- description: REST API and developer portal for the SS&C Advent Black Diamond wealth platform, covering portfolio, account and client data exchange for advisors and integration partners. The portal requires sign-in
  name: SS&C Black Diamond Wealth Platform API
  slug: ssc-black-diamond-wealth-platform-api
- baseURL: https://emsuatxapi.taltrade.com:9001
  baseurl_source: declared
  description: The MarketDataService API from SS&C Technologies — 18 operation(s) for marketdataservice.
  name: SS&C Technologies Market Data Service API
  slug: ss-c-technologies-marketdataservice-api
- baseURL: https://emsuatxapi.taltrade.com:9001
  baseurl_source: declared
  description: The SubmitOrderService API from SS&C Technologies — 19 operation(s) for submitorderservice.
  name: SS&C Technologies Submit Order Service API
  slug: ss-c-technologies-submitorderservice-api
- baseURL: https://emsuatxapi.taltrade.com:9001
  baseurl_source: declared
  description: The UserServices API from SS&C Technologies — 1 operation(s) for userservices.
  name: SS&C Technologies User Services API
  slug: ss-c-technologies-userservices-api
- baseURL: https://emsuatxapi.taltrade.com:9001
  baseurl_source: declared
  description: The XAPIServer API from SS&C Technologies — 2 operation(s) for xapiserver.
  name: SS&C Technologies XAPI Server API
  slug: ss-c-technologies-xapiserver-api
- baseURL: https://apim.ssnc.cloud
  baseurl_source: declared
  description: The Utility Services API from SS&C Technologies — 21 operation(s) for utility services.
  name: SS&C Technologies Utility Services API
  slug: ss-c-technologies-utility-services-api
artifact_total: 18
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.ssctech.com/blog/rss.xml
- group: other
  href: https://artifacts.apis.io/ss-c-technologies/overlays/ss-c-technologies-eze-ems-xapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ss-c-technologies-eze-ems-xapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.ssctech.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ssctech.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/ezesoft/xapi/blob/master/readme.md
- group: docs
  title: ''
  type: APIReference
  url: https://emsuatxapi.taltrade.com:9001/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/ezesoft/xapi/blob/master/readme.md#how-do-i-get-started-with-xapi
- group: operate
  title: ''
  type: Support
  url: https://www.ssctech.com/about/support-client-portals
- group: company
  title: ''
  type: Blog
  url: https://www.ssctech.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ezesoft
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/ssnc-eze-ems-xapi/ems-xapi-rest/collection/jeebiq6/ss-c-eze-ems-xapi
- group: start
  title: ''
  type: SignUp
  url: https://developer.ssctech.com/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ssctech.com/about/disclaimer
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ssctech.com/about/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.ssctech.com/about/disclosures/security-addendum-schedule3
- group: auth
  href: https://artifacts.apis.io/ss-c-technologies/authentication/ss-c-technologies-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ss-c-technologies-authentication.yml
- group: design
  href: https://artifacts.apis.io/ss-c-technologies/conventions/ss-c-technologies-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ss-c-technologies-conventions.yml
- group: design
  href: https://artifacts.apis.io/ss-c-technologies/conformance/ss-c-technologies-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ss-c-technologies-conformance.yml
- group: design
  href: https://artifacts.apis.io/ss-c-technologies/errors/ss-c-technologies-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ss-c-technologies-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ss-c-technologies/lifecycle/ss-c-technologies-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ss-c-technologies-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/ss-c-technologies/lifecycle/ss-c-technologies-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/ss-c-technologies-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/ss-c-technologies/packages/ss-c-technologies-packages.yml
  title: ''
  type: Packages
  url: packages/ss-c-technologies-packages.yml
- group: operate
  href: https://artifacts.apis.io/ss-c-technologies/rate-limits/ss-c-technologies-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ss-c-technologies-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ss-c-technologies/plans/ss-c-technologies-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ss-c-technologies-plans-pricing.yml
- group: start
  href: https://artifacts.apis.io/ss-c-technologies/sandbox/ss-c-technologies-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ss-c-technologies-sandbox.yml
- group: design
  href: https://artifacts.apis.io/ss-c-technologies/data-model/ss-c-technologies-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ss-c-technologies-data-model.yml
- group: agent
  href: https://artifacts.apis.io/ss-c-technologies/well-known/ss-c-technologies-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ss-c-technologies-well-known.yml
- group: auth
  href: https://artifacts.apis.io/ss-c-technologies/security/ss-c-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ss-c-technologies-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/ss-c-technologies/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/ss-c-technologies/llms/ss-c-technologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ss-c-technologies-llms.txt
created: '2026-09-13'
description: 'SS&C Technologies Holdings (NASDAQ: SSNC) is a global provider of financial-services and healthcare software and outsourcing, headquartered in Windsor, Connecticut, operating under brands including SS&C Advent, SS&C Eze, SS&C GlobeOp, SS&C GIDS, SS&C Intralinks, SS&C Black Diamond, SS&C Algorithmics and SS&C Blue Prism. Most of the API surface is client-gated: the corporate SS&C APIM developer portal at developer.ssctech.com and the Black Diamond developer portal both require an account, and access is requested through a client relationship manager. The substantial public exception is SS&C Eze EMS xAPI, whose machine-readable contract SS&C Eze publishes openly on GitHub as three proto3 files — 64 gRPC RPCs across MarketDataService, SubmitOrderService and UtilityServices — alongside a matching REST projection described by a live OpenAPI 3.0.4 document with 73 operations covering order submission and amendment, pair and basket orders, allocations and trade reports, real-time
  and historical market data, and intraday balances, positions and activity.'
finops:
- has_sources: true
  method: derived
  name: Ss C Technologies Finops
  primary_unit: ''
  service_category: ''
  slug: ss-c-technologies-finops
  template: true
image: https://www.ssctech.com/hubfs/website/logos/ssc_logo_1200x630.png
layout: provider
modified: '2026-10-06'
name: SS&C Technologies
nav: Providers
network: true
overview: 'SS&C Technologies publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Market Data Service API, Submit Order Service API, User Services API, and 4 more. Tagged areas include Financial Services, Investment Management, Fund Administration, Wealth Management, and Execution Management.


  The SS&C Technologies catalog on APIs.io includes 1 Spectral governance ruleset.


  SS&C Technologies'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 23 more developer resources.'
plans:
- name: Ss C Technologies Plans Pricing
  plan_count: 0
  slug: ss-c-technologies-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 1
  name: Ss C Technologies Rate Limits
  slug: ss-c-technologies-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: SS&C Technologies API Rules
  rule_count: 45
  severity_counts:
    error: 38
    hint: 0
    info: 4
    warn: 3
  slug: ss-c-technologies-rules
scopes:
- name: Ss C Technologies Scopes
  scope_count: 14
  slug: ss-c-technologies-scopes
  summary_line: 14 scopes
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 28
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 42.4
    developer_ergonomics: 68.5
    discoverability: 66.1
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 47.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 42.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ss-c-technologies/ss-c-technologies-2026-10-11T130300.png
security:
- kind: authentication
  name: Ss C Technologies Authentication
  slug: ss-c-technologies-authentication
  summary_line: http/session-token/srp/openIdConnect · 5 schemes
- kind: domain-security
  name: Ss C Technologies Domain Security
  slug: ss-c-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Ss C Technologies Trust Center
  slug: ss-c-technologies-trust-center
  summary_line: SOC 1 Type 2
skill_count: 3
skills:
- name: ss-c-technologies-place-and-track-an-order
  slug: ss-c-technologies-place-and-track-an-order
- name: ss-c-technologies-reconcile-positions-and-activity
  slug: ss-c-technologies-reconcile-positions-and-activity
- name: ss-c-technologies-subscribe-to-market-data
  slug: ss-c-technologies-subscribe-to-market-data
slug: ss-c-technologies
tags:
- Financial Services
- Investment Management
- Fund Administration
- Wealth Management
- Execution Management
- Order Management
- Market Data
- Trading
- gRPC
- Enterprise Software
website: https://www.ssctech.com/
---
