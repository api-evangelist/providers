---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Cost‑of‑living and quality‑of‑life comparison endpoints (non‑MCP clients).
  name: CityParity REST API
  slug: cityparity-rest-api
- baseURL: https://mcp.cityparity.com
  baseurl_source: declared
  description: Cost-of-living and quality-of-life comparison endpoints. Same compute as the MCP server at /mcp; this surface is for non-MCP clients (web apps, scripts, integrations). All responses are JSON with shap
  name: cityparity REST API API
  slug: cityparity-rest-api-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/cityparity-com/rules/cityparity-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cityparity-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cityparity-com/json-ld/cityparity-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cityparity-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cityparity-com/vocabulary/cityparity-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cityparity-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cityparity-com/conformance/cityparity-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cityparity-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/cityparity-com/data-model/cityparity-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cityparity-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/cityparity-com/errors/cityparity-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cityparity-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/cityparity-com/llms/cityparity-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cityparity-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cityparity-com/mcp/cityparity-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cityparity-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/cityparity-com/hosts/cityparity-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cityparity-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cityparity-com/vendors/cityparity-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cityparity-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/cityparity-com/packages/cityparity-com-packages.yml
  title: ''
  type: SDKs
  url: packages/cityparity-com-packages.yml
- group: build
  href: https://artifacts.apis.io/cityparity-com/packages/cityparity-com-packages.yml
  title: ''
  type: Packages
  url: packages/cityparity-com-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://cityparity.com/changelog/
- group: auth
  href: https://artifacts.apis.io/cityparity-com/security/cityparity-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cityparity-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cityparity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cityparity.com/mcp/
- group: docs
  title: ''
  type: Documentation
  url: https://cityparity.com/mcp/
- group: company
  title: ''
  type: Blog
  url: https://cityparity.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cityparity.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cityparity.com/terms/
created: '2026-11-03'
description: cityparity provides a cost‑of‑living and quality‑of‑life comparison tool that includes taxes, childcare, healthcare, vacation, parental leave and the social safety net. It lets users compare real take‑home pay and expenses between cities worldwide, offering detailed breakdowns and data‑driven insights for expats, remote workers and families considering relocation.
image: https://cityparity.com/og.png
json_schemas:
- name: CompareRequest
  property_count: 7
  slug: cityparity-com-compare-request
- name: RankRequest
  property_count: 4
  slug: cityparity-com-rank-request
- name: SafetyNetRequest
  property_count: 1
  slug: cityparity-com-safety-net-request
jsonld:
- class_count: 6
  name: Cityparity Com Context
  property_count: 23
  slug: cityparity-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.cityparity.com.
  name: cityparity MCP Server
  slug: cityparity-com-mcp-yml
modified: '2026-11-03'
name: cityparity
nav: Providers
network: true
overview: 'cityparity publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including REST API API, and 1 more. Tagged areas include Cost of Living, Comparison Tool, Data Visualization, Expatriate Resources, and Financial Planning.


  The cityparity catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  cityparity''s developer surface includes changelog, documentation, engineering blog, and 17 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: cityparity API Rules
  rule_count: 43
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 1
  slug: cityparity-com-rules
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 54.0
    developer_ergonomics: 17.9
    discoverability: 65.0
    operational_transparency: 7.9
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cityparity Com Domain Security
  slug: cityparity-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cityparity-com
tags:
- Cost of Living
- Comparison Tool
- Data Visualization
- Expatriate Resources
- Financial Planning
website: https://cityparity.com/
---
