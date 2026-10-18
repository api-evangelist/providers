---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.3
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: The Casafari API provides methods for manipulating alerts feeds, accounts, and consulting a reference of available locations, features and conditions.
  name: Casafari API
  slug: casafari-api
- baseURL: https://api.casafari.com
  baseurl_source: declared
  description: The alerts-api---feeds API from Casafari API and MCP Platform — 2 operation(s) for alerts-api---feeds.
  name: Casafari API and MCP Platform Alerts API Feeds API
  slug: casafari-alerts-api-feeds-api
- baseURL: https://api.casafari.com
  baseurl_source: declared
  description: The alerts-api---webhooks API from Casafari API and MCP Platform — 2 operation(s) for alerts-api---webhooks.
  name: Casafari API and MCP Platform Alerts API Webhooks API
  slug: casafari-alerts-api-webhooks-api
- baseURL: https://api.casafari.com
  baseurl_source: declared
  description: The api---alerts API from Casafari API and MCP Platform — 4 operation(s) for api---alerts.
  name: Casafari API and MCP Platform API Alerts API
  slug: casafari-api-alerts-api
- baseURL: https://api.casafari.com
  baseurl_source: declared
  description: The api---comparables API from Casafari API and MCP Platform — 3 operation(s) for api---comparables.
  name: Casafari API and MCP Platform API Comparables API
  slug: casafari-api-comparables-api
- baseURL: https://api.casafari.com
  baseurl_source: declared
  description: The api---properties API from Casafari API and MCP Platform — 5 operation(s) for api---properties.
  name: Casafari API and MCP Platform API Properties API
  slug: casafari-api-properties-api
- baseURL: https://api.casafari.com
  baseurl_source: declared
  description: The api---references API from Casafari API and MCP Platform — 10 operation(s) for api---references.
  name: Casafari API and MCP Platform API References API
  slug: casafari-api-references-api
- baseURL: https://api.casafari.com
  baseurl_source: declared
  description: The api---valuation API from Casafari API and MCP Platform — 1 operation(s) for api---valuation.
  name: Casafari API and MCP Platform API Valuation API
  slug: casafari-api-valuation-api
- baseURL: https://api.casafari.com
  baseurl_source: declared
  description: The market-analytics-api---analysis API from Casafari API and MCP Platform — 1 operation(s) for market-analytics-api---analysis.
  name: Casafari API and MCP Platform Market Analytics API Analysis API
  slug: casafari-market-analytics-api-analysis-api
- baseURL: https://api.casafari.com
  baseurl_source: declared
  description: The market-analytics-api---distributions API from Casafari API and MCP Platform — 4 operation(s) for market-analytics-api---distributions.
  name: Casafari API and MCP Platform Market Analytics API Distributions API
  slug: casafari-market-analytics-api-distributions-api
- baseURL: https://api.casafari.com
  baseurl_source: declared
  description: The market-analytics-api---time series API from Casafari API and MCP Platform — 1 operation(s) for market-analytics-api---time series.
  name: Casafari API and MCP Platform market-analytics-api---time series API
  slug: casafari-market-analytics-api-time-series-api
- baseURL: https://api.casafari.com
  baseurl_source: declared
  description: The user-management---authentication API from Casafari API and MCP Platform — 2 operation(s) for user-management---authentication.
  name: Casafari API and MCP Platform User Management Authentication API
  slug: casafari-user-management-authentication-api
artifact_total: 25
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/casafari/refs/heads/main/rate-limits/casafari-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/casafari-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/casafari/refs/heads/main/plans/casafari-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/casafari-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/casafari/refs/heads/main/rules/casafari-rules.yml
  title: ''
  type: Spectral
  url: rules/casafari-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/casafari/refs/heads/main/json-ld/casafari-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/casafari-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/casafari/refs/heads/main/vocabulary/casafari-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/casafari-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/casafari/refs/heads/main/data-model/casafari-data-model.yml
  title: ''
  type: DataModel
  url: data-model/casafari-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/casafari/refs/heads/main/authentication/casafari-authentication.yml
  title: ''
  type: Authentication
  url: authentication/casafari-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/casafari/refs/heads/main/errors/casafari-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/casafari-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/casafari/refs/heads/main/conformance/casafari-conformance.yml
  title: ''
  type: Conformance
  url: conformance/casafari-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/casafari/refs/heads/main/llms/casafari-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/casafari-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/casafari/refs/heads/main/mcp/casafari-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/casafari-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/casafari/refs/heads/main/well-known/casafari-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/casafari-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/casafari/refs/heads/main/hosts/casafari-hosts.yml
  title: ''
  type: Hosts
  url: hosts/casafari-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/casafari/refs/heads/main/vendors/casafari-vendors.yml
  title: ''
  type: Vendors
  url: vendors/casafari-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/casafari/refs/heads/main/packages/casafari-packages.yml
  title: ''
  type: SDKs
  url: packages/casafari-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/casafari/refs/heads/main/packages/casafari-packages.yml
  title: ''
  type: Packages
  url: packages/casafari-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.casafari.com/terms-of-use/
- group: start
  title: ''
  type: Sandbox
  url: https://platform.casafari.com/console
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.casafari.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.casafari.com/docs/rest/area-insights/price-distribution
- group: start
  title: ''
  type: Login
  url: https://www.casafari.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.casafari.com/docs/faq/first-rest-call
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.casafari.com`
- group: docs
  title: ''
  type: APIReference
  url: https://developers.casafari.com/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/casafari/refs/heads/main/security/casafari-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/casafari-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.casafari.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.casafari.com
created: '2026-10-15'
description: Casafari provides the pioneering, cleanest, and largest real‑estate database in Europe, powered by AI. It enables and accelerates property deals by offering comprehensive property data, analytics, and AI‑driven insights across the continent. The platform includes an MCP for AI agents to query property information, valuations, trends, and recent sales, supporting developers with robust APIs and documentation.
image: https://www.casafari.com/wp-content/uploads/2022/07/laptop-and-report.png
json_schemas:
- name: ApiPropertiesSearchResponseV1
  property_count: 64
  slug: casafari-api-properties-search-response-v1
- name: ApiPropertiesSearchResponseV2
  property_count: 64
  slug: casafari-api-properties-search-response-v2
- name: ApiPropertyDetailResponseV1
  property_count: 64
  slug: casafari-api-property-detail-response-v1
- name: ApiSearchComparablesRequestV1
  property_count: 37
  slug: casafari-api-search-comparables-request-v1
- name: ApiSearchComparablesRequestV2
  property_count: 37
  slug: casafari-api-search-comparables-request-v2
- name: ApiSearchComparablesResponseV2
  property_count: 7
  slug: casafari-api-search-comparables-response-v2
jsonld:
- class_count: 120
  name: Casafari Context
  property_count: 309
  slug: casafari-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.casafari.com requiring OAuth.
  name: Casafari API and MCP Platform MCP Server
  slug: casafari-mcp-yml
modified: '2026-10-15'
name: Casafari API and MCP Platform
nav: Providers
network: true
overview: 'Casafari API and MCP Platform publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alerts API Feeds API, Alerts API Webhooks API, API Alerts API, and 9 more. Tagged areas include Real Estate Data, Property Sourcing, Valuation, Market Analytics, and CRM.


  The Casafari API and MCP Platform catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Casafari API and MCP Platform''s developer surface includes authentication, sandbox, pricing, getting-started guide, API reference, documentation, and 21 more developer resources.'
plans:
- name: Casafari Plans Pricing
  plan_count: 3
  slug: casafari-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 7
  name: Casafari Rate Limits
  slug: casafari-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Casafari API and MCP Platform API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: casafari-rules
score:
  band: strong
  composite: 59.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 65.6
    developer_ergonomics: 64.3
    discoverability: 75.0
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Casafari Authentication
  slug: casafari-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Casafari Domain Security
  slug: casafari-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: casafari
tags:
- Real Estate Data
- Property Sourcing
- Valuation
- Market Analytics
- CRM
- Real Estate Software
website: https://www.casafari.com
---
