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
    agentic_access: derived
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
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Ceruleanjobs Com Agentic Access
  operation_count: 4
  slug: ceruleanjobs-com-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 1
apis:
- baseURL: https://ceruleanjobs.com
  baseurl_source: declared
  description: The Model Context Protocol server over the same index — the same engine as Search, shaped for an AI agent rather than for a hand-written client.
  name: ceruleanjobs-com MCP API
  slug: ceruleanjobs-com-mcp-api
- baseURL: https://ceruleanjobs.com
  baseurl_source: declared
  description: Full-text search, filtering, and similar-job lookup.
  name: ceruleanjobs-com Search API
  slug: ceruleanjobs-com-search-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/ceruleanjobs-com/agentic-access/ceruleanjobs-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ceruleanjobs-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ceruleanjobs-com/rules/ceruleanjobs-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ceruleanjobs-com-rules.yml
- group: design
  href: https://artifacts.apis.io/ceruleanjobs-com/json-ld/ceruleanjobs-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ceruleanjobs-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/ceruleanjobs-com/vocabulary/ceruleanjobs-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ceruleanjobs-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ceruleanjobs-com/data-model/ceruleanjobs-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ceruleanjobs-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/ceruleanjobs-com/errors/ceruleanjobs-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ceruleanjobs-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ceruleanjobs-com/conformance/ceruleanjobs-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ceruleanjobs-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ceruleanjobs-com/llms/ceruleanjobs-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ceruleanjobs-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/ceruleanjobs-com/mcp/ceruleanjobs-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ceruleanjobs-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/ceruleanjobs-com/hosts/ceruleanjobs-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ceruleanjobs-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ceruleanjobs-com/vendors/ceruleanjobs-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ceruleanjobs-com-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CeruleanJobs
- group: auth
  href: https://artifacts.apis.io/ceruleanjobs-com/security/ceruleanjobs-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ceruleanjobs-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ceruleanjobs.com/
created: '2026-11-03'
description: Cerulean operates a job board and recruiting service that connects professionals with career opportunities at luxury brands worldwide. It lists open positions across fashion, beauty, fine jewelry, timepieces, fragrances, wines, spirits, travel and hospitality, covering roles from internships to executive levels.
image: https://ceruleanjobs.com/api/open-graph.jpg
json_schemas:
- name: SearchResponse
  property_count: 7
  slug: ceruleanjobs-com-search-response
jsonld:
- class_count: 4
  name: Ceruleanjobs Com Context
  property_count: 28
  slug: ceruleanjobs-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at ceruleanjobs.com.
  name: ceruleanjobs-com MCP Server
  slug: ceruleanjobs-com-mcp-yml
modified: '2026-11-03'
name: ceruleanjobs-com
nav: Providers
network: true
overview: 'ceruleanjobs-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: MCP API and Search API. Tagged areas include Luxury Jobs, Recruiting, Job Board, Fashion, and Beauty.


  The ceruleanjobs-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: ceruleanjobs-com API Rules
  rule_count: 60
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 1
  slug: ceruleanjobs-com-rules
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 56.2
    catalog_earned_first_party: 0.0
    catalog_gap: 58.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 55.1
    developer_ergonomics: 0.0
    discoverability: 65.0
    operational_transparency: 2.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ceruleanjobs Com Domain Security
  slug: ceruleanjobs-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ceruleanjobs-com
tags:
- Luxury Jobs
- Recruiting
- Job Board
- Fashion
- Beauty
- Hospitality
website: https://ceruleanjobs.com/
---
