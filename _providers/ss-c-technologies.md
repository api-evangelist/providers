---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.4
  scored_at: '2026-09-15'
api_count: 1
apis:
- baseURL: https://emsuatxapi.taltrade.com:9001
  baseurl_source: declared
  description: Cross-platform execution-management API for Eze EMS, published by SS&C Eze as a gRPC contract (three proto3 files, 64 RPCs across MarketDataService, SubmitOrderService and UtilityServices) with an equ
  name: SS&C Eze EMS xAPI
  slug: ssc-eze-ems-xapi
- description: SS&C's corporate API management portal, where clients register applications, request access to SS&C API products and manage consumers against a Kong gateway. The API catalog itself is behind authentic
  name: SS&C APIM Developer Portal
  slug: ssc-apim-developer-portal
- description: REST API and developer portal for the SS&C Advent Black Diamond wealth platform, covering portfolio, account and client data exchange for advisors and integration partners. The portal requires sign-in
  name: SS&C Black Diamond Wealth Platform API
  slug: ssc-black-diamond-wealth-platform-api
artifact_total: 9
common:
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
  href: https://raw.githubusercontent.com/api-evangelist/ss-c-technologies/refs/heads/main/authentication/ss-c-technologies-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ss-c-technologies-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ss-c-technologies/refs/heads/main/conventions/ss-c-technologies-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ss-c-technologies-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ss-c-technologies/refs/heads/main/conformance/ss-c-technologies-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ss-c-technologies-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ss-c-technologies/refs/heads/main/errors/ss-c-technologies-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ss-c-technologies-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ss-c-technologies/refs/heads/main/lifecycle/ss-c-technologies-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ss-c-technologies-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ss-c-technologies/refs/heads/main/lifecycle/ss-c-technologies-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/ss-c-technologies-lifecycle.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ss-c-technologies/refs/heads/main/packages/ss-c-technologies-packages.yml
  title: ''
  type: Packages
  url: packages/ss-c-technologies-packages.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ss-c-technologies/refs/heads/main/rate-limits/ss-c-technologies-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ss-c-technologies-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ss-c-technologies/refs/heads/main/plans/ss-c-technologies-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ss-c-technologies-plans-pricing.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/ss-c-technologies/refs/heads/main/sandbox/ss-c-technologies-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ss-c-technologies-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ss-c-technologies/refs/heads/main/data-model/ss-c-technologies-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ss-c-technologies-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ss-c-technologies/refs/heads/main/well-known/ss-c-technologies-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ss-c-technologies-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ss-c-technologies/refs/heads/main/security/ss-c-technologies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ss-c-technologies-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ss-c-technologies/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ss-c-technologies/refs/heads/main/llms/ss-c-technologies-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ss-c-technologies-llms.txt
created: '2026-09-13'
description: 'SS&C Technologies Holdings (NASDAQ: SSNC) is a global provider of financial-services and healthcare software and outsourcing, headquartered in Windsor, Connecticut, operating under brands including SS&C Advent, SS&C Eze, SS&C GlobeOp, SS&C GIDS, SS&C Intralinks, SS&C Black Diamond, SS&C Algorithmics and SS&C Blue Prism. Most of the API surface is client-gated: the corporate SS&C APIM developer portal at developer.ssctech.com and the Black Diamond developer portal both require an account, and access is requested through a client relationship manager. The substantial public exception is SS&C Eze EMS xAPI, whose machine-readable contract SS&C Eze publishes openly on GitHub as three proto3 files — 64 gRPC RPCs across MarketDataService, SubmitOrderService and UtilityServices — alongside a matching REST projection described by a live OpenAPI 3.0.4 document with 73 operations covering order submission and amendment, pair and basket orders, allocations and trade reports, real-time
  and historical market data, and intraday balances, positions and activity.'
image: https://www.ssctech.com/hubfs/website/logos/ssc_logo_1200x630.png
layout: provider
modified: '2026-09-13'
name: SS&C Technologies
nav: Providers
network: true
overview: 'SS&C Technologies publishes 1 API on the [APIs.io](https://apis.io/) network: SS&C Eze EMS xAPI. Tagged areas include Financial-Services, Investment Management, Fund Administration, Wealth Management, and Execution Management.


  SS&C Technologies'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 21 more developer resources.'
plans:
- name: Ss C Technologies Plans Pricing
  plan_count: 0
  slug: ss-c-technologies-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Ss C Technologies Rate Limits
  slug: ss-c-technologies-rate-limits
scopes:
- name: Ss C Technologies Scopes
  scope_count: 0
  slug: ss-c-technologies-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 36.1
    developer_ergonomics: 68.5
    discoverability: 68.5
    operational_transparency: 31.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 48.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 76.7
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
slug: ss-c-technologies
tags:
- Financial-Services
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
