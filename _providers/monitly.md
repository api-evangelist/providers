---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: The Charts API from Monitly — 1 operation(s) for charts.
  name: Monitly Charts API
  slug: monitly-charts-api
- description: The Datasets API from Monitly — 3 operation(s) for datasets.
  name: Monitly Datasets API
  slug: monitly-datasets-api
- description: The Mcp API from Monitly — 1 operation(s) for mcp.
  name: Monitly MCP API
  slug: monitly-mcp-api
artifact_total: 17
common:
- group: commercial
  href: https://artifacts.apis.io/monitly/plans/monitly-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/monitly-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/monitly/rules/monitly-rules.yml
  title: ''
  type: Spectral
  url: rules/monitly-rules.yml
- group: design
  href: https://artifacts.apis.io/monitly/json-ld/monitly-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/monitly-context.jsonld
- group: design
  href: https://artifacts.apis.io/monitly/vocabulary/monitly-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/monitly-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/monitly/data-model/monitly-data-model.yml
  title: ''
  type: DataModel
  url: data-model/monitly-data-model.yml
- group: design
  href: https://artifacts.apis.io/monitly/conformance/monitly-conformance.yml
  title: ''
  type: Conformance
  url: conformance/monitly-conformance.yml
- group: agent
  href: https://artifacts.apis.io/monitly/llms/monitly-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/monitly-llms.txt
- group: agent
  href: https://artifacts.apis.io/monitly/mcp/monitly-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/monitly-mcp.yml
- group: auth
  href: https://artifacts.apis.io/monitly/well-known/monitly-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/monitly-security.txt
- group: agent
  href: https://artifacts.apis.io/monitly/well-known/monitly-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/monitly-well-known.yml
- group: other
  href: https://artifacts.apis.io/monitly/hosts/monitly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/monitly-hosts.yml
- group: other
  href: https://artifacts.apis.io/monitly/vendors/monitly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/monitly-vendors.yml
- group: build
  href: https://artifacts.apis.io/monitly/packages/monitly-packages.yml
  title: ''
  type: SDKs
  url: packages/monitly-packages.yml
- group: build
  href: https://artifacts.apis.io/monitly/packages/monitly-packages.yml
  title: ''
  type: Packages
  url: packages/monitly-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://monit.ly/status
- group: auth
  title: ''
  type: Security
  url: https://monit.ly/statistics/chad/categories/security
- group: auth
  href: https://artifacts.apis.io/monitly/security/monitly-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/monitly-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/monitly/security/monitly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/monitly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://monit.ly
- group: docs
  title: ''
  type: Documentation
  url: https://monit.ly/api-docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://monit.ly/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://monit.ly/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://monit.ly/researcher
- group: operate
  title: ''
  type: Support
  url: https://monit.ly/contact
- group: company
  title: ''
  type: Blog
  url: https://monit.ly/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://monit.ly/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://monit.ly/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://monit.ly/privacy
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://monit.ly/api/mcp
  - status: 200
    url: https://monit.ly
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-08'
description: Monitly provides a live data platform aggregating millions of official statistics and economic indicators from sources like Eurostat. Users can browse datasets, create custom dashboards, receive updates, and integrate data via a unified JSON API. The service offers AI‑assisted dataset selection, chart generation, and collaboration tools for individuals, teams, and organizations.
finops:
- has_sources: true
  method: derived
  name: Monitly Finops
  primary_unit: seat
  service_category: ''
  slug: monitly-finops
  template: false
image: https://monit.ly/og.png
json_schemas:
- name: GetApiDatasetsIdResponse
  property_count: 2
  slug: monitly-get-api-datasets-id-response
- name: GetApiDatasetsResponse
  property_count: 2
  slug: monitly-get-api-datasets-response
- name: PostApiChartsGeneratePngRequest
  property_count: 9
  slug: monitly-post-api-charts-generate-png-request
- name: PostApiChartsGeneratePngResponse
  property_count: 2
  slug: monitly-post-api-charts-generate-png-response
- name: PostApiMcpRequest
  property_count: 3
  slug: monitly-post-api-mcp-request
- name: PostApiMcpResponse
  property_count: 2
  slug: monitly-post-api-mcp-response
jsonld:
- class_count: 7
  name: Monitly Context
  property_count: 20
  slug: monitly-context
layout: provider
mcp_servers:
- description: Remote MCP server at monit.ly requiring an API key.
  name: Monitly MCP Server
  slug: monitly-mcp-yml
modified: '2026-10-08'
name: Monitly
nav: Providers
network: true
overview: 'Monitly is listed with 3 APIs on the [APIs.io](https://apis.io/) network: Charts API, Datasets API, and MCP API. Tagged areas include Company, Data, Statistics, and Dashboards.


  The Monitly catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Monitly''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 22 more developer resources.'
plans:
- name: Monitly Plans Pricing
  plan_count: 3
  slug: monitly-plans-pricing
- name: Monitly Price Estimates
  plan_count: 0
  slug: monitly-price-estimates
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Monitly API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: monitly-rules
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 70.8
    catalog_earned_first_party: 12.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.0
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 24.4
    developer_ergonomics: 29.8
    discoverability: 63.3
    operational_transparency: 13.2
  previous_composite: 43.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/monitly/monitly-2026-11-03T135836.png
security:
- kind: domain-security
  name: Monitly Domain Security
  slug: monitly-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Monitly Vulnerability Disclosure
  slug: monitly-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: monitly
tags:
- Company
- Data
- Statistics
- Dashboards
website: https://monit.ly
---
