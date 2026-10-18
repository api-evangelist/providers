---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 54.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 14
  human_in_the_loop: 1
  name: Travel Risk Api Agentic Access
  operation_count: 61
  slug: travel-risk-api-agentic-access
  summary_line: 61 operations · 14 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: Hosted remote MCP server (OAuth sign-in, 15 tools) over the travel risk data.
  name: Travel Risk API MCP Server
  slug: mcp
- baseURL: https://api.travelriskapi.com
  baseurl_source: declared
  description: The Adb API from Travel Risk API — 13 operation(s) for adb.
  name: Travel Risk API Adb API
  slug: travel-risk-api-adb-api
- baseURL: https://api.travelriskapi.com
  baseurl_source: declared
  description: Self-serve API key registration.
  name: Travel Risk API Auth API
  slug: travel-risk-api-auth-api
- baseURL: https://api.travelriskapi.com
  baseurl_source: declared
  description: Stripe checkout + webhook receiver.
  name: Travel Risk API Billing API
  slug: travel-risk-api-billing-api
- baseURL: https://api.travelriskapi.com
  baseurl_source: declared
  description: The Ext API from Travel Risk API — 24 operation(s) for ext.
  name: Travel Risk API Ext API
  slug: travel-risk-api-ext-api
- baseURL: https://api.travelriskapi.com
  baseurl_source: declared
  description: Country advisories, alerts, and risk scores. All endpoints require X-API-Key.
  name: Travel Risk API Public Data API
  slug: travel-risk-api-public-data-api
- baseURL: https://api.travelriskapi.com
  baseurl_source: declared
  description: Health and service metadata. No auth.
  name: Travel Risk API System API
  slug: travel-risk-api-system-api
- baseURL: https://api.travelriskapi.com
  baseurl_source: declared
  description: Per-key usage metering and quota status.
  name: Travel Risk API Usage API
  slug: travel-risk-api-usage-api
artifact_total: 19
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/travel-risk-api/refs/heads/main/agentic-access/travel-risk-api-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/travel-risk-api-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/travel-risk-api/refs/heads/main/rate-limits/travel-risk-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/travel-risk-api-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/travel-risk-api/refs/heads/main/plans/travel-risk-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/travel-risk-api-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/travel-risk-api/refs/heads/main/rules/travel-risk-api-rules.yml
  title: ''
  type: Spectral
  url: rules/travel-risk-api-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/travel-risk-api/refs/heads/main/json-ld/travel-risk-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/travel-risk-api-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/travel-risk-api/refs/heads/main/vocabulary/travel-risk-api-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/travel-risk-api-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/travel-risk-api/refs/heads/main/data-model/travel-risk-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/travel-risk-api-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/travel-risk-api/refs/heads/main/changelog/travel-risk-api-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/travel-risk-api-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/travel-risk-api/refs/heads/main/conventions/travel-risk-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/travel-risk-api-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/travel-risk-api/refs/heads/main/lifecycle/travel-risk-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/travel-risk-api-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/travel-risk-api/refs/heads/main/errors/travel-risk-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/travel-risk-api-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/travel-risk-api/refs/heads/main/conformance/travel-risk-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/travel-risk-api-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/travel-risk-api/refs/heads/main/llms/travel-risk-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/travel-risk-api-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/travel-risk-api/refs/heads/main/mcp/travel-risk-api-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/travel-risk-api-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/travel-risk-api/refs/heads/main/mcp/travel-risk-api-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/travel-risk-api-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/travel-risk-api/refs/heads/main/well-known/travel-risk-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/travel-risk-api-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/travel-risk-api/refs/heads/main/hosts/travel-risk-api-hosts.yml
  title: ''
  type: Hosts
  url: hosts/travel-risk-api-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/travel-risk-api/refs/heads/main/authentication/travel-risk-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/travel-risk-api-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/travel-risk-api/refs/heads/main/security/travel-risk-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/travel-risk-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://travelriskapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://travelriskapi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://travelriskapi.com/docs/risk
- group: company
  title: ''
  type: Blog
  url: https://travelriskapi.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://travelriskapi.com/changelog
- group: start
  title: ''
  type: Login
  url: https://travelriskapi.com/dashboard/login
- group: commercial
  title: ''
  type: Pricing
  url: https://travelriskapi.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://travelriskapi.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://travelriskapi.com/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://travelriskapi.com/terms
- group: other
  title: ''
  type: APICatalog
  url: https://travelriskapi.com/.well-known/api-catalog
- group: docs
  title: ''
  type: InteractiveDocs
  url: https://api.travelriskapi.com/docs
created: '2026-10-09'
description: 'Travel Risk API by Travel Code is a REST API for real-time travel safety data: government travel advisories, natural disaster alerts, armed-conflict events and composite country risk scores for 229 countries and territories, plus a companion Aviation API covering airport status, security, immigration, weather and flight data. One API key opens both; a free plan needs no card, and a hosted MCP server exposes 15 tools.'
image: https://travelriskapi.com/og/home.png?lang=en
json_schemas:
- name: RecoverRequest
  property_count: 1
  slug: travel-risk-api-recover-request
- name: RegisterRequest
  property_count: 2
  slug: travel-risk-api-register-request
- name: TripRequest
  property_count: 3
  slug: travel-risk-api-trip-request
jsonld:
- class_count: 6
  name: Travel Risk Api Context
  property_count: 20
  slug: travel-risk-api-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.travelriskapi.com requiring OAuth; 15 tools listed.
  name: Travel Risk API MCP Server
  slug: travel-risk-api-mcp-server
modified: '2026-10-09'
name: Travel Risk API
nav: Providers
network: true
overview: 'Travel Risk API publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Adb API, Auth API, Billing API, and 5 more. Tagged areas include Travel, Travel Risk, Travel Advisories, Aviation, and Airports.


  The Travel Risk API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Travel Risk API''s developer surface includes changelog, authentication, documentation, API reference, engineering blog, pricing, and 25 more developer resources.'
plans:
- name: Travel Risk Api Plans Pricing
  plan_count: 4
  slug: travel-risk-api-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 10
  name: Travel Risk Api Rate Limits
  slug: travel-risk-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Travel Risk API API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 1
  slug: travel-risk-api-rules
score:
  band: strong
  composite: 57.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 60.5
    developer_ergonomics: 31.0
    discoverability: 90.0
    operational_transparency: 63.2
  previous_composite: 56.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/travel-risk-api/refs/heads/main/screenshots/travel-risk-api-2026-10-11T131138.png
security:
- kind: authentication
  name: Travel Risk Api Authentication
  slug: travel-risk-api-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Travel Risk Api Domain Security
  slug: travel-risk-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: travel-risk-api
tags:
- Travel
- Travel Risk
- Travel Advisories
- Aviation
- Airports
- Risk Scoring
- Safety
- Disaster Alerts
website: https://travelriskapi.com/
---
