---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Fxmacrodata Agentic Access
  operation_count: 37
  slug: fxmacrodata-agentic-access
  summary_line: 37 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.fxmacrodata.com
  baseurl_source: declared
  description: 'Primary product: macroeconomic announcement time series.'
  name: FXMacroData Announcements API
  slug: fxmacrodata-announcements-api
- baseURL: https://api.fxmacrodata.com
  baseurl_source: declared
  description: Standalone economic and policy release calendar endpoint spanning announcements and central-bank decision timing.
  name: FXMacroData Calendar API
  slug: fxmacrodata-calendar-api
- baseURL: https://api.fxmacrodata.com
  baseurl_source: declared
  description: Commodity and energy datasets, including OPEC and planned commodity price endpoints.
  name: FXMacroData Commodities API
  slug: fxmacrodata-commodities-api
- baseURL: https://api.fxmacrodata.com
  baseurl_source: declared
  description: Cross-domain metadata index for available indicators.
  name: FXMacroData Data Catalogue API
  slug: fxmacrodata-data-catalogue-api
- baseURL: https://api.fxmacrodata.com
  baseurl_source: declared
  description: The factors API from FXMacroData — 1 operation(s) for factors.
  name: FXMacroData Factors API
  slug: fxmacrodata-factors-api
- baseURL: https://api.fxmacrodata.com
  baseurl_source: declared
  description: FX market-state datasets including spot FX, market sessions, risk sentiment, and COT positioning.
  name: FXMacroData Fx Markets API
  slug: fxmacrodata-fx-markets-api
- baseURL: https://api.fxmacrodata.com
  baseurl_source: declared
  description: Service health status endpoint.
  name: FXMacroData Health API
  slug: fxmacrodata-health-api
- baseURL: https://api.fxmacrodata.com
  baseurl_source: declared
  description: The monetary_policy API from FXMacroData — 1 operation(s) for monetary_policy.
  name: FXMacroData Monetary Policy API
  slug: fxmacrodata-monetary-policy-api
- baseURL: https://api.fxmacrodata.com
  baseurl_source: declared
  description: Forecasts/predictions for macroeconomic announcements, linked to the unique announcement they target via ``announcement_id``. Covers market consensus, central-bank forecasts, IMF WEO, and professional
  name: FXMacroData Predictions API
  slug: fxmacrodata-predictions-api
- baseURL: https://api.fxmacrodata.com
  baseurl_source: declared
  description: Official central-bank press-release archive endpoints.
  name: FXMacroData Press Releases API
  slug: fxmacrodata-press-releases-api
- baseURL: https://api.fxmacrodata.com
  baseurl_source: declared
  description: 'Settlement records for event contracts on official macro releases: first-print value, latest value, release timing (scheduled, actual release window, ingested, latency from the actual release) and the'
  name: FXMacroData Settlement API
  slug: fxmacrodata-settlement-api
artifact_total: 27
asyncapis:
- description: ''
  name: Fxmacrodata Webhooks
  slug: fxmacrodata-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/fxmacrodata/agentic-access/fxmacrodata-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fxmacrodata-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/fxmacrodata/plans/fxmacrodata-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fxmacrodata-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/fxmacrodata/rules/fxmacrodata-rules.yml
  title: ''
  type: Spectral
  url: rules/fxmacrodata-rules.yml
- group: design
  href: https://artifacts.apis.io/fxmacrodata/json-ld/fxmacrodata-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fxmacrodata-context.jsonld
- group: design
  href: https://artifacts.apis.io/fxmacrodata/vocabulary/fxmacrodata-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fxmacrodata-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/fxmacrodata/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/fxmacrodata/asyncapi/fxmacrodata-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/fxmacrodata-webhooks.yml
- group: design
  href: https://artifacts.apis.io/fxmacrodata/data-model/fxmacrodata-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fxmacrodata-data-model.yml
- group: build
  href: https://artifacts.apis.io/fxmacrodata/cli/fxmacrodata-cli.yml
  title: ''
  type: CLI
  url: cli/fxmacrodata-cli.yml
- group: operate
  href: https://artifacts.apis.io/fxmacrodata/changelog/fxmacrodata-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fxmacrodata-changelog.yml
- group: design
  href: https://artifacts.apis.io/fxmacrodata/conventions/fxmacrodata-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fxmacrodata-conventions.yml
- group: auth
  href: https://artifacts.apis.io/fxmacrodata/security/fxmacrodata-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/fxmacrodata-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/fxmacrodata/authentication/fxmacrodata-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fxmacrodata-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://fxmacrodata.com/documentation/deprecation-policy
- group: design
  href: https://artifacts.apis.io/fxmacrodata/lifecycle/fxmacrodata-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fxmacrodata-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/fxmacrodata/errors/fxmacrodata-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fxmacrodata-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fxmacrodata/conformance/fxmacrodata-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fxmacrodata-conformance.yml
- group: agent
  href: https://artifacts.apis.io/fxmacrodata/llms/fxmacrodata-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fxmacrodata-llms.txt
- group: other
  href: https://artifacts.apis.io/fxmacrodata/a2a/fxmacrodata-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/fxmacrodata-a2a.yml
- group: agent
  href: https://artifacts.apis.io/fxmacrodata/mcp/fxmacrodata-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fxmacrodata-mcp.yml
- group: auth
  href: https://artifacts.apis.io/fxmacrodata/well-known/fxmacrodata-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fxmacrodata-security.txt
- group: auth
  href: https://artifacts.apis.io/fxmacrodata/well-known/fxmacrodata-chatgpt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fxmacrodata-chatgpt-security.txt
- group: agent
  href: https://artifacts.apis.io/fxmacrodata/well-known/fxmacrodata-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fxmacrodata-well-known.yml
- group: other
  href: https://artifacts.apis.io/fxmacrodata/hosts/fxmacrodata-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fxmacrodata-hosts.yml
- group: other
  href: https://artifacts.apis.io/fxmacrodata/vendors/fxmacrodata-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fxmacrodata-vendors.yml
- group: build
  href: https://artifacts.apis.io/fxmacrodata/packages/fxmacrodata-packages.yml
  title: ''
  type: SDKs
  url: packages/fxmacrodata-packages.yml
- group: build
  href: https://artifacts.apis.io/fxmacrodata/packages/fxmacrodata-packages.yml
  title: ''
  type: Packages
  url: packages/fxmacrodata-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://fxmacrodata.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://fxmacrodata.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fxmacrodata.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://fxmacrodata.com/documentation/changelog
- group: auth
  href: https://artifacts.apis.io/fxmacrodata/security/fxmacrodata-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/fxmacrodata-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/fxmacrodata/security/fxmacrodata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fxmacrodata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fxmacrodata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fxmacrodata.com/documentation/reference
- group: docs
  title: ''
  type: APIReference
  url: https://fxmacrodata.com/documentation/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://fxmacrodata.com/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://fxmacrodata.com/subscribe
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fxmacrodata.com/terms
created: '2026-10-17'
description: FXMacroData provides real-time macroeconomic data APIs for foreign exchange (FX) and quantitative research. Their platform offers extensive coverage of FX pairs, commodities, bond yields, and macro indicators, delivering data via REST, WebSocket, and streaming endpoints. Users can access dashboards, backtesting tools, and AI-driven insights, with options for CSV/JSON export, widgets, and integration with popular platforms. The service targets traders, analysts, and developers needing up-to-date market data for building trading models and research applications.
image: https://fxmacrodata.com/card.png
json_schemas:
- name: AnnouncementResponse
  property_count: 44
  slug: fxmacrodata-announcement-response
- name: CommodityResponse
  property_count: 13
  slug: fxmacrodata-commodity-response
- name: COTResponse
  property_count: 34
  slug: fxmacrodata-cotresponse
- name: ForexResponse
  property_count: 15
  slug: fxmacrodata-forex-response
- name: PredictionsResponse
  property_count: 25
  slug: fxmacrodata-predictions-response
- name: RateDifferentialResponse
  property_count: 27
  slug: fxmacrodata-rate-differential-response
jsonld:
- class_count: 97
  name: Fxmacrodata Context
  property_count: 813
  slug: fxmacrodata-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.fxmacrodata.com requiring OAuth.
  name: FXMacroData MCP Server
  slug: fxmacrodata-mcp-yml
modified: '2026-10-17'
name: FXMacroData
nav: Providers
network: true
overview: 'FXMacroData publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Announcements API, Calendar API, Commodities API, and 8 more. Tagged areas include Company, Finance, Data, and Foreign Exchange.


  The FXMacroData catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  FXMacroData''s developer surface includes CLI, changelog, authentication, support, documentation, API reference, getting-started guide, and 32 more developer resources.'
plans:
- name: Fxmacrodata Plans Pricing
  plan_count: 3
  slug: fxmacrodata-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: FXMacroData API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: fxmacrodata-rules
score:
  band: developing
  composite: 46.3
  coverage:
    artifact_dirs: 30
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.6
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 50.4
    developer_ergonomics: 44.6
    discoverability: 66.7
    operational_transparency: 38.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 55.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 36.4
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fxmacrodata/fxmacrodata-2026-11-03T132417.png
security:
- kind: authentication
  name: Fxmacrodata Authentication
  slug: fxmacrodata-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Fxmacrodata Domain Security
  slug: fxmacrodata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fxmacrodata Vulnerability Disclosure
  slug: fxmacrodata-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: fxmacrodata-fetch-announcement-data
  slug: fxmacrodata-fetch-announcement-data
slug: fxmacrodata
tags:
- Company
- Finance
- Data
- Foreign Exchange
website: https://fxmacrodata.com/
---
