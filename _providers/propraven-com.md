---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 61.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Propraven Com Agentic Access
  operation_count: 92
  slug: propraven-com-agentic-access
  summary_line: 92 operations · 7 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://propraven.com
  baseurl_source: declared
  description: Account-scoped usage, quota, and key-level reporting.
  name: propraven-com Account API
  slug: propraven-com-account-api
- baseURL: https://propraven.com
  baseurl_source: declared
  description: Data coverage statistics.
  name: propraven-com Coverage API
  slug: propraven-com-coverage-api
- baseURL: https://propraven.com
  baseurl_source: declared
  description: The Credits API from propraven-com — 2 operation(s) for credits.
  name: propraven-com Credits API
  slug: propraven-com-credits-api
- baseURL: https://propraven.com
  baseurl_source: declared
  description: 'Deal sourcing: absentee owners, property flips.'
  name: propraven-com Deals API
  slug: propraven-com-deals-api
- baseURL: https://propraven.com
  baseurl_source: declared
  description: Bulk delivery metadata (Cloudflare R2, Databricks Delta Sharing). Signed-in session only; an anonymous call gets 401.
  name: propraven-com Distribution API
  slug: propraven-com-distribution-api
- baseURL: https://propraven.com
  baseurl_source: declared
  description: 'Lead feeds: buyable qualified target lists, priced per lead, with a free masked preview. Paid via x402 or a paid subscription.'
  name: propraven-com Leads API
  slug: propraven-com-leads-api
- baseURL: https://propraven.com
  baseurl_source: declared
  description: County-level market statistics and trends.
  name: propraven-com Market API
  slug: propraven-com-market-api
- baseURL: https://propraven.com
  baseurl_source: declared
  description: Owner search, profiles, and portfolios.
  name: propraven-com Owners API
  slug: propraven-com-owners-api
- baseURL: https://propraven.com
  baseurl_source: declared
  description: Parcel lookup, owner details, permits, deeds, and risk data.
  name: propraven-com Parcels API
  slug: propraven-com-parcels-api
- baseURL: https://propraven.com
  baseurl_source: declared
  description: Default-off, account/creator-scoped descriptive signals, retained evidence and explicit scenarios. Source and use rights remain independent gates.
  name: propraven-com Property Intelligence API
  slug: propraven-com-property-intelligence-api
- baseURL: https://propraven.com
  baseurl_source: declared
  description: Geographic and filtered parcel search.
  name: propraven-com Search API
  slug: propraven-com-search-api
- baseURL: https://propraven.com
  baseurl_source: declared
  description: 'Machine Storefront: the FREE data catalog + availability discovery surface (get the field dictionary and preview a jurisdiction or a per-parcel price), and the PAID, value-tiered parcel dossier bought'
  name: propraven-com Storefront API
  slug: propraven-com-storefront-api
- baseURL: https://propraven.com
  baseurl_source: declared
  description: The Verify API from propraven-com — 1 operation(s) for verify.
  name: propraven-com Verify API
  slug: propraven-com-verify-api
- baseURL: https://propraven.com
  baseurl_source: declared
  description: The Watch API from propraven-com — 2 operation(s) for watch.
  name: propraven-com Watch API
  slug: propraven-com-watch-api
- baseURL: https://propraven.com
  baseurl_source: declared
  description: Webhook subscriptions and delivery history. Manage which events PropRaven pushes to your endpoints.
  name: propraven-com Webhooks API
  slug: propraven-com-webhooks-api
- baseURL: https://propraven.com
  baseurl_source: declared
  description: 'Zoning from the jurisdiction that issues it: the raw code as published, overlays, and ordinance-parsed attributes with a citation per value, plus honest per-jurisdiction coverage. Account required.'
  name: propraven-com Zoning API
  slug: propraven-com-zoning-api
artifact_total: 34
asyncapis:
- description: ''
  name: Propraven Com Webhooks
  slug: propraven-com-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/propraven-com/agentic-access/propraven-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/propraven-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/propraven-com/rate-limits/propraven-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/propraven-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/propraven-com/rules/propraven-com-rules.yml
  title: ''
  type: Spectral
  url: rules/propraven-com-rules.yml
- group: design
  href: https://artifacts.apis.io/propraven-com/json-ld/propraven-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/propraven-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/propraven-com/vocabulary/propraven-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/propraven-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/propraven-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/propraven-com/asyncapi/propraven-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/propraven-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/propraven-com/data-model/propraven-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/propraven-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/propraven-com/changelog/propraven-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/propraven-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/propraven-com/authentication/propraven-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/propraven-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/propraven-com/errors/propraven-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/propraven-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/propraven-com/conformance/propraven-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/propraven-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/propraven-com/llms/propraven-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/propraven-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/propraven-com/mcp/propraven-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/propraven-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/propraven-com/well-known/propraven-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/propraven-com-security.txt
- group: auth
  href: https://artifacts.apis.io/propraven-com/well-known/propraven-com-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/propraven-com-api-security.txt
- group: agent
  href: https://artifacts.apis.io/propraven-com/well-known/propraven-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/propraven-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/propraven-com/hosts/propraven-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/propraven-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/propraven-com/vendors/propraven-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/propraven-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/propraven-com/packages/propraven-com-packages.yml
  title: ''
  type: Packages
  url: packages/propraven-com-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://propraven.com/security
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@propraven/sdk
- group: start
  title: ''
  type: DeveloperPortal
  url: https://propraven.com/developers
- group: start
  title: ''
  type: Login
  url: https://propraven.com/sign-in
- group: start
  title: ''
  type: SignUp
  url: https://propraven.com/api/v1/agent/signup
- group: docs
  title: ''
  type: APIReference
  url: https://propraven.com/changelog
- group: auth
  href: https://artifacts.apis.io/propraven-com/security/propraven-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/propraven-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/propraven-com/security/propraven-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/propraven-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://propraven.com/
- group: docs
  title: ''
  type: Documentation
  url: https://propraven.com/docs/v1
- group: start
  title: ''
  type: GettingStarted
  url: https://propraven.com/docs/v1
- group: commercial
  title: ''
  type: Pricing
  url: https://propraven.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://propraven.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://propraven.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jdw2111
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://propraven.com/openapi.json
  - status: null
    url: https://api.propraven.com/openapi.json
  - status: 401
    url: https://propraven.com/mcp
  - status: 401
    url: https://api.propraven.com/mcp
  - status: 200
    url: https://propraven.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: PropRaven LLC, based in Charlotte, NC, provides U.S. parcel and property intelligence by aggregating county assessor, recorder, permit, and other public records. The platform offers datasets covering ownership, values, sales, permits, and risk signals, with coverage and update dates varying by dataset and delivery channel.
image: https://propraven.com/icon.png
json_schemas:
- name: IntelligenceHandoff
  property_count: 10
  slug: propraven-com-intelligence-handoff
- name: IntelligenceRun
  property_count: 7
  slug: propraven-com-intelligence-run
- name: OwnerCard
  property_count: 4
  slug: propraven-com-owner-card
- name: ParcelDossier
  property_count: 6
  slug: propraven-com-parcel-dossier
- name: Parcel
  property_count: 117
  slug: propraven-com-parcel
- name: ZillowContext
  property_count: 7
  slug: propraven-com-zillow-context
jsonld:
- class_count: 89
  name: Propraven Com Context
  property_count: 669
  slug: propraven-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at propraven.com.
  name: propraven-com MCP Server
  slug: propraven-com-mcp-yml
modified: '2026-10-31'
name: propraven-com
nav: Providers
network: true
overview: 'propraven-com publishes 16 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Coverage API, Credits API, and 13 more. Tagged areas include Real Estate, Data, Property Intelligence, and US.


  The propraven-com catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  propraven-com''s developer surface includes changelog, authentication, signup flow, API reference, documentation, getting-started guide, pricing, and 28 more developer resources.'
plans:
- name: Propraven Com Plans Pricing
  plan_count: 0
  slug: propraven-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Propraven Com Rate Limits
  slug: propraven-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: propraven-com API Rules
  rule_count: 17
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 3
  slug: propraven-com-rules
scopes:
- name: Propraven Com Scopes
  scope_count: 0
  slug: propraven-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 33
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.8
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 71.4
    developer_ergonomics: 44.5
    discoverability: 56.7
    operational_transparency: 63.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 61.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 6.3
      total: 16
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/propraven-com/propraven-com-2026-11-03T141631.png
security:
- kind: authentication
  name: Propraven Com Authentication
  slug: propraven-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Propraven Com Domain Security
  slug: propraven-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Propraven Com Vulnerability Disclosure
  slug: propraven-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: get-parcel
  slug: propraven-com-get-parcel
slug: propraven-com
tags:
- Real Estate
- Data
- Property Intelligence
- US
website: https://propraven.com/
---
