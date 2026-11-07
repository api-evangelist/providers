---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: three_quarters
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.3
  scored_at: '2026-11-06'
api_count: 11
apis:
- description: Real-time, end-of-day and historical transaction-based market data for environmental and energy commodities, sourced from CBL and global intermediaries including Evolution Markets. Delivered as time s
  name: Xpansiv Data API
  slug: xpansiv-data
- description: The Xpansiv Marketplace Server API for retrieving real-time market data and executing and managing orders on CBL, published as rules of engagement against the FIX 4.4 specification from the FIX Tradin
  name: Xpansiv Marketplace FIX API
  slug: xpansiv-marketplace-fix
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: Account Information
  name: Xpansiv Account API
  slug: xpansiv-account-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: Building types
  name: Xpansiv Building types API
  slug: xpansiv-building-types-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: Clean Transportation
  name: Xpansiv Clean Transportation API
  slug: xpansiv-clean-transportation-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: Corporate Entities Operations
  name: Xpansiv Corporate Entity API
  slug: xpansiv-corporateentity-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: The Exchange APIs allow users to take various actions, both read and write, for their interactions with execution venues, such as the CBL platform. The Search Deposits API allows the user to search th
  name: Xpansiv Exchange API
  slug: xpansiv-exchange-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: Facilities
  name: Xpansiv Facilities API
  slug: xpansiv-facilities-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: Facility import error handling
  name: Xpansiv Facility import error handling API
  slug: xpansiv-facility-import-error-handling-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: View, update or upload a file
  name: Xpansiv File Type V1 API
  slug: xpansiv-file-type-v1-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: the File Registry REST API
  name: Xpansiv /file Registry API
  slug: xpansiv-fileregistry-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: 'The Forward Deals API allows the user to search The Forward Deals associated with their Xpansiv Connect account and/or other Xpansiv Connect accounts that have granted their user that access. Forward '
  name: Xpansiv Forward Deals API
  slug: xpansiv-forward-deals-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: The Generators API from Xpansiv — 1 operation(s) for generators.
  name: Xpansiv Generators API
  slug: xpansiv-generators-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: The Instruments API from Xpansiv — 1 operation(s) for instruments.
  name: Xpansiv Instruments API
  slug: xpansiv-instruments-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: The Issuance API allows the user to pull information on any Issuances associated with their account, or permissioned account, for the various registries they are linked with. The Instrument details on
  name: Xpansiv Issuances API
  slug: xpansiv-issuances-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: Ledger Operations
  name: Xpansiv Ledger API
  slug: xpansiv-ledger-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: View an Account's current and historical instrument details
  name: Xpansiv Ledger V1 API
  slug: xpansiv-ledger-v1-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: Market
  name: Xpansiv Market API
  slug: xpansiv-market-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: View or submit measurement data. Measurement data includes, but it is not limited to, telemetry data, emission records, verification records, etc.
  name: Xpansiv Meter Reading V1 API
  slug: xpansiv-meter-reading-v1-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: Meter Readings
  name: Xpansiv Meter Readings API
  slug: xpansiv-meter-readings-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: 'The Portfolio API allows the user to search their credit inventory (tax lot) data on active positions across all registry accounts linked to their Xpansiv Connect account and/or other Xpansiv Connect '
  name: Xpansiv Portfolio API
  slug: xpansiv-portfolio-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: The Project API allows the user to pull publicly available information about carbon projects registered in the registries that are integrated with Xpansiv Connect. Note - this call has a number of opt
  name: Xpansiv Projects API
  slug: xpansiv-projects-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: Qualified reporting entities
  name: Xpansiv Qualified reporting entities API
  slug: xpansiv-qualified-reporting-entities-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: Remote data collectors
  name: Xpansiv Remote data collectors API
  slug: xpansiv-remote-data-collectors-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: Issuance Reports
  name: Xpansiv Report Issuance V1 API
  slug: xpansiv-report-issuance-v1-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: Resource Reports
  name: Xpansiv Report Resource V1 API
  slug: xpansiv-report-resource-v1-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: the Reporting REST API
  name: Xpansiv /reporting API
  slug: xpansiv-reporting-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: The Reports API allows the user to retrieve a comprehensive credit inventory (aka Tax Lot by Program Report) on all active positions with a single call across all registry accounts linked to their Xpa
  name: Xpansiv Reports API
  slug: xpansiv-reports-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: View, update or create a Resource.
  name: Xpansiv Resource V1 API
  slug: xpansiv-resource-v1-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: View or submit a retirement request, or redemption claim, on instrument(s).
  name: Xpansiv Retirementbatch V1 API
  slug: xpansiv-retirementbatch-v1-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: The Retirements APIs allow users to take various actions, both read and write, for their retirement activity. The Create Retirements API allows users of Xpansiv Connect to retire one or more positions
  name: Xpansiv Retirements API
  slug: xpansiv-retirements-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: The Split Lots API allows the user to search split lot data on their Xpansiv Connect account and/or other Xpansiv Connect accounts that have granted your user that access.
  name: Xpansiv Split Lots API
  slug: xpansiv-split-lots-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: View or create subaccounts. Use subaccounts to organize your account’s instruments. All accounts have a "Default" subaccount, where all new issuances and incoming transfers will be deposited. Subaccou
  name: Xpansiv Subaccount V1 API
  slug: xpansiv-subaccount-v1-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: System Information
  name: Xpansiv System API
  slug: xpansiv-system-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: Check the API system health.
  name: Xpansiv System V1 API
  slug: xpansiv-system-v1-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: Transactions
  name: Xpansiv Transactions API
  slug: xpansiv-transactions-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: Initiate a transfer request (between subaccounts or another account holder), view or act upon pending transfers, as well as view historical transfer details.
  name: Xpansiv Transferbatch V1 API
  slug: xpansiv-transferbatch-v1-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: The Transfers APIs allow users to take various actions, both read and write, for their bilateral transaction activity. The Search Transfers API allows the user to search registry transfer data for the
  name: Xpansiv Transfers API
  slug: xpansiv-transfers-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: Retrieve usage point identifiers for resources (projects, facilities, etc.) for which measurement readings may be submitted
  name: Xpansiv Usage Point Identifier V1 API
  slug: xpansiv-usage-point-identifier-v1-api
- baseURL: https://connect.xpansiv.com/app/api/v1
  baseurl_source: declared
  description: Utilities
  name: Xpansiv Utilities API
  slug: xpansiv-utilities-api
- baseURL: https://api.data.xpansiv.com
  baseurl_source: declared
  description: The Account Holders API from Xpansiv — 1 operation(s) for account holders.
  name: Xpansiv Account Holders API
  slug: xpansiv-account-holders-api
- baseURL: https://api.data.xpansiv.com
  baseurl_source: declared
  description: The Reference Data API enables discovering Xpansiv Connect reference data types and values.
  name: Xpansiv Reference Data API
  slug: xpansiv-reference-data-api
- baseURL: https://api.data.xpansiv.com
  baseurl_source: declared
  description: Subaccount Operations
  name: Xpansiv Sub Account API
  slug: xpansiv-sub-account-api
artifact_total: 55
common:
- group: other
  href: https://artifacts.apis.io/xpansiv/capabilities/xpansiv-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/xpansiv-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/xpansiv/overlays/xpansiv-managed-solutions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/xpansiv-managed-solutions-overlay.yaml
- group: other
  href: https://artifacts.apis.io/xpansiv/overlays/xpansiv-nar-registry-client-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/xpansiv-nar-registry-client-overlay.yaml
- group: other
  href: https://artifacts.apis.io/xpansiv/overlays/xpansiv-tigr-registry-client-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/xpansiv-tigr-registry-client-overlay.yaml
- group: other
  href: https://artifacts.apis.io/xpansiv/overlays/xpansiv-optimal-transfer-position-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/xpansiv-optimal-transfer-position-overlay.yaml
- group: other
  href: https://artifacts.apis.io/xpansiv/overlays/xpansiv-apx-power-markets-file-registry-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/xpansiv-apx-power-markets-file-registry-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.xpansiv.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.xpansiv.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.xpansiv.com/developer-portal
- group: docs
  title: ''
  type: APIReference
  url: https://developer.xpansiv.com/developer-portal
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.xpansiv.com/developer-portal/xpansiv-connect/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.xpansiv.com/
- group: start
  title: ''
  type: SignUp
  url: https://connect.xpansiv.com/app/login/
- group: company
  title: ''
  type: Blog
  url: https://www.xpansiv.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.xpansiv.com/general-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.xpansiv.com/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://developer.xpansiv.com/developer-portal/xpansiv-power/rest_api/postman
- group: agent
  href: https://artifacts.apis.io/xpansiv/llms/xpansiv-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/xpansiv-llms.txt
- group: agent
  href: https://artifacts.apis.io/xpansiv/mcp/xpansiv-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/xpansiv-mcp.yml
- group: build
  href: https://artifacts.apis.io/xpansiv/mcp/xpansiv-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/xpansiv-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/xpansiv/well-known/xpansiv-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/xpansiv-well-known.yml
- group: build
  href: https://artifacts.apis.io/xpansiv/packages/xpansiv-packages.yml
  title: ''
  type: Packages
  url: packages/xpansiv-packages.yml
- group: build
  href: https://artifacts.apis.io/xpansiv/packages/xpansiv-packages.yml
  title: ''
  type: SDKs
  url: packages/xpansiv-packages.yml
- group: auth
  href: https://artifacts.apis.io/xpansiv/authentication/xpansiv-authentication.yml
  title: ''
  type: Authentication
  url: authentication/xpansiv-authentication.yml
- group: auth
  href: https://artifacts.apis.io/xpansiv/scopes/xpansiv-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/xpansiv-scopes.yml
- group: design
  href: https://artifacts.apis.io/xpansiv/conventions/xpansiv-conventions.yml
  title: ''
  type: Conventions
  url: conventions/xpansiv-conventions.yml
- group: design
  href: https://artifacts.apis.io/xpansiv/errors/xpansiv-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/xpansiv-problem-types.yml
- group: design
  href: https://artifacts.apis.io/xpansiv/lifecycle/xpansiv-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/xpansiv-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/xpansiv/conformance/xpansiv-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xpansiv-conformance.yml
- group: design
  href: https://artifacts.apis.io/xpansiv/data-model/xpansiv-data-model.yml
  title: ''
  type: DataModel
  url: data-model/xpansiv-data-model.yml
- group: auth
  href: https://artifacts.apis.io/xpansiv/security/xpansiv-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xpansiv-domain-security.yml
- group: operate
  href: https://artifacts.apis.io/xpansiv/rate-limits/xpansiv-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/xpansiv-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/xpansiv/plans/xpansiv-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/xpansiv-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/xpansiv/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  href: https://artifacts.apis.io/xpansiv/sandbox/xpansiv-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/xpansiv-sandbox.yml
- group: other
  href: https://artifacts.apis.io/xpansiv/overlays/xpansiv-connect-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/xpansiv-connect-overlay.yaml
created: '2026-09-04'
description: Xpansiv is market infrastructure for global environmental and energy commodities — carbon credits, renewable energy certificates, water, low-carbon fuels and recycled materials. It operates CBL, the largest spot exchange for environmental commodities, the Evolution Markets and OTX brokerage and execution desks, the H2OX water market and the ACE and JSEV carbon platforms, alongside the environmental registries it acquired with APX in 2022 — NAR (North American Renewables Registry), TIGR, I-REC, I-TRACK-G and the Xpansiv-powered digital fuels registries. Its public developer portal at developer.xpansiv.com publishes eleven OpenAPI descriptions across Xpansiv Connect (environmental commodity portfolio, retirement and transfer), Xpansiv Managed Solutions, the NAR and TIGR registry client APIs, the Optimal Outcomes suite and the APX Power Markets file registry, plus a FIX 4.4 marketplace protocol specification, Xpansiv Data market-data APIs and a first-party Python SDK.
finops:
- has_sources: true
  method: derived
  name: Xpansiv Finops
  primary_unit: ''
  service_category: ''
  slug: xpansiv-finops
  template: true
image: https://kinlane-productions2.s3.amazonaws.com/apis-io/apis-io-logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at developer.xpansiv.com; 7 tools listed.
  name: Xpansiv Developer Portal MCP Server
  slug: xpansiv-developer-portal-mcp-server
modified: '2026-09-04'
name: Xpansiv
nav: Providers
network: true
overview: 'Xpansiv publishes 43 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Building types API, Clean Transportation API, and 40 more. Tagged areas include Company, Environmental Commodities, Carbon Markets, Renewable Energy Certificates, and Registries.


  The Xpansiv catalog on APIs.io includes 1 Spectral governance ruleset.


  Xpansiv''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, engineering blog, authentication, and 29 more developer resources.'
plans:
- name: Xpansiv Plans Pricing
  plan_count: 0
  slug: xpansiv-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Xpansiv Rate Limits
  slug: xpansiv-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Xpansiv API Rules
  rule_count: 58
  severity_counts:
    error: 33
    hint: 0
    info: 6
    warn: 19
  slug: xpansiv-rules
scopes:
- name: Xpansiv Scopes
  scope_count: 0
  slug: xpansiv-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 31.8
    contract_quality: 51.3
    developer_ergonomics: 78.0
    discoverability: 80.0
    operational_transparency: 0.0
  previous_composite: 49.7
  provenance:
    conformance: first-party
    contracts:
      callable: 92.7
      derived: 0
      marker_coverage: 0.0
      total: 41
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 34.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/xpansiv/xpansiv-2026-10-11T194633.png
security:
- kind: authentication
  name: Xpansiv Authentication
  slug: xpansiv-authentication
  summary_line: http (bearer)/http (basic)/apiKey · 3 schemes
- kind: domain-security
  name: Xpansiv Domain Security
  slug: xpansiv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: xpansiv-discover-apis-via-mcp
  slug: xpansiv-discover-apis-via-mcp
- name: xpansiv-retire-environmental-commodity
  slug: xpansiv-retire-environmental-commodity
- name: xpansiv-submit-iso-schedule
  slug: xpansiv-submit-iso-schedule
- name: xpansiv-transfer-and-reverse
  slug: xpansiv-transfer-and-reverse
slug: xpansiv
tags:
- Company
- Environmental Commodities
- Carbon Markets
- Renewable Energy Certificates
- Registries
- Market Data
- Trading
- Energy
- Sustainability
- Climate
website: https://www.xpansiv.com/
---
