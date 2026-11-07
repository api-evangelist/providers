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
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Emission Factors Com Agentic Access
  operation_count: 18
  slug: emission-factors-com-agentic-access
  summary_line: 18 operations · 5 acting
api_count: 1
apis:
- baseURL: https://emission-factors.com
  baseurl_source: declared
  description: The Bulk API from emission-factors-com — 1 operation(s) for bulk.
  name: emission-factors-com Bulk API
  slug: emission-factors-com-bulk-api
- baseURL: https://emission-factors.com
  baseurl_source: declared
  description: The Calculate API from emission-factors-com — 1 operation(s) for calculate.
  name: emission-factors-com Calculate API
  slug: emission-factors-com-calculate-api
- baseURL: https://emission-factors.com
  baseurl_source: declared
  description: The Cleanest Hours API from emission-factors-com — 1 operation(s) for cleanest hours.
  name: emission-factors-com Cleanest Hours API
  slug: emission-factors-com-cleanest-hours-api
- baseURL: https://emission-factors.com
  baseurl_source: declared
  description: The Compare API from emission-factors-com — 1 operation(s) for compare.
  name: emission-factors-com Compare API
  slug: emission-factors-com-compare-api
- baseURL: https://emission-factors.com
  baseurl_source: declared
  description: The Fuel Emissions API from emission-factors-com — 1 operation(s) for fuel emissions.
  name: emission-factors-com Fuel Emissions API
  slug: emission-factors-com-fuel-emissions-api
- baseURL: https://emission-factors.com
  baseurl_source: declared
  description: The Health API from emission-factors-com — 1 operation(s) for health.
  name: emission-factors-com Health API
  slug: emission-factors-com-health-api
- baseURL: https://emission-factors.com
  baseurl_source: declared
  description: The Intensity API from emission-factors-com — 1 operation(s) for intensity.
  name: emission-factors-com Intensity API
  slug: emission-factors-com-intensity-api
- baseURL: https://emission-factors.com
  baseurl_source: declared
  description: The Lookup API from emission-factors-com — 3 operation(s) for lookup.
  name: emission-factors-com Lookup API
  slug: emission-factors-com-lookup-api
- baseURL: https://emission-factors.com
  baseurl_source: declared
  description: The Mcp API from emission-factors-com — 1 operation(s) for mcp.
  name: emission-factors-com MCP API
  slug: emission-factors-com-mcp-api
- baseURL: https://emission-factors.com
  baseurl_source: declared
  description: The Methodology API from emission-factors-com — 1 operation(s) for methodology.
  name: emission-factors-com Methodology API
  slug: emission-factors-com-methodology-api
- baseURL: https://emission-factors.com
  baseurl_source: declared
  description: The Openapi.json API from emission-factors-com — 1 operation(s) for openapi.json.
  name: emission-factors-com Openapi.json API
  slug: emission-factors-com-openapi-json-api
- baseURL: https://emission-factors.com
  baseurl_source: declared
  description: The Plant Emissions API from emission-factors-com — 1 operation(s) for plant emissions.
  name: emission-factors-com Plant Emissions API
  slug: emission-factors-com-plant-emissions-api
- baseURL: https://emission-factors.com
  baseurl_source: declared
  description: The Rate API from emission-factors-com — 1 operation(s) for rate.
  name: emission-factors-com Rate API
  slug: emission-factors-com-rate-api
- baseURL: https://emission-factors.com
  baseurl_source: declared
  description: The Status API from emission-factors-com — 1 operation(s) for status.
  name: emission-factors-com Status API
  slug: emission-factors-com-status-api
- baseURL: https://emission-factors.com
  baseurl_source: declared
  description: The Utility Rate API from emission-factors-com — 1 operation(s) for utility rate.
  name: emission-factors-com Utility Rate API
  slug: emission-factors-com-utility-rate-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/emission-factors-com/agentic-access/emission-factors-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/emission-factors-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/emission-factors-com/rate-limits/emission-factors-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/emission-factors-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/emission-factors-com/rules/emission-factors-com-rules.yml
  title: ''
  type: Spectral
  url: rules/emission-factors-com-rules.yml
- group: design
  href: https://artifacts.apis.io/emission-factors-com/json-ld/emission-factors-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/emission-factors-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/emission-factors-com/vocabulary/emission-factors-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/emission-factors-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/emission-factors-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/emission-factors-com/data-model/emission-factors-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/emission-factors-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/emission-factors-com/authentication/emission-factors-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/emission-factors-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/emission-factors-com/errors/emission-factors-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/emission-factors-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/emission-factors-com/conformance/emission-factors-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/emission-factors-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/emission-factors-com/llms/emission-factors-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/emission-factors-com-llms.txt
- group: build
  href: https://artifacts.apis.io/emission-factors-com/mcp/emission-factors-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/emission-factors-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/emission-factors-com/mcp/emission-factors-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/emission-factors-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/emission-factors-com/hosts/emission-factors-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/emission-factors-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/emission-factors-com/vendors/emission-factors-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/emission-factors-com-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://emission-factors.com/blog/egrid-2024-preliminary-emission-factors.html
- group: start
  title: ''
  type: GettingStarted
  url: https://emission-factors.com/mcp-setup
- group: auth
  href: https://artifacts.apis.io/emission-factors-com/security/emission-factors-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/emission-factors-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://emission-factors.com/
- group: docs
  title: ''
  type: Documentation
  url: https://emission-factors.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://emission-factors.com/api-docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://emission-factors.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://emission-factors.com/privacy.html
created: '2026-10-30'
description: Emission-factors.com provides a free REST API and MCP server that translates US ZIP codes into EPA eGRID grid‑carbon emission factors, electricity rates, hourly grid carbon data, utility tariffs, and plant emissions. It aggregates data from EPA eGRID, EIA‑930, EPA CAMD, and OpenEI URDB, offering 12 data endpoints for developers and sustainability teams to calculate Scope 2 emissions without requiring an API key or signup. The service includes tools for bulk CSV processing, hourly intensity calculations, and AI‑ready MCP tools, supporting CDP, CSRD, and SB 253 compliance.
image: https://emission-factors.com/favicon.svg
json_schemas:
- name: LookupResponse
  property_count: 4
  slug: emission-factors-com-lookup-response
jsonld:
- class_count: 2
  name: Emission Factors Com Context
  property_count: 34
  slug: emission-factors-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at emission-factors.com.
  name: emission-factors-com MCP Server
  slug: emission-factors-com-mcp-yml
modified: '2026-10-30'
name: emission-factors-com
nav: Providers
network: true
overview: 'emission-factors-com publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bulk API, Calculate API, Cleanest Hours API, and 12 more. Tagged areas include Company, Emission, Carbon, Energy, and Sustainability.


  The emission-factors-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  emission-factors-com''s developer surface includes authentication, engineering blog, getting-started guide, documentation, API reference, and 18 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 1
  name: Emission Factors Com Rate Limits
  slug: emission-factors-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: emission-factors-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: emission-factors-com-rules
scopes:
- name: Emission Factors Com Scopes
  scope_count: 0
  slug: emission-factors-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 32
    catalog_earned: 64.2
    catalog_earned_first_party: 8.0
    catalog_gap: 50.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 52.5
    developer_ergonomics: 33.8
    discoverability: 65.0
    operational_transparency: 21.1
  previous_composite: 42.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 31.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/emission-factors-com/emission-factors-com-2026-11-03T131451.png
security:
- kind: authentication
  name: Emission Factors Com Authentication
  slug: emission-factors-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Emission Factors Com Domain Security
  slug: emission-factors-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: emission-factors-com-mcp-tools
  slug: emission-factors-com-mcp-tools
slug: emission-factors-com
tags:
- Company
- Emission
- Carbon
- Energy
- Sustainability
website: https://emission-factors.com/
---
