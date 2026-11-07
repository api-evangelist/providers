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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'dotsweep-com API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-06); not the provider''s own document.'
  name: dotsweep-com API
  slug: dotsweep-com-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/dotsweep-com/rules/dotsweep-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dotsweep-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dotsweep-com/json-ld/dotsweep-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dotsweep-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dotsweep-com/vocabulary/dotsweep-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dotsweep-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dotsweep-com/data-model/dotsweep-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dotsweep-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/dotsweep-com/conformance/dotsweep-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dotsweep-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dotsweep-com/llms/dotsweep-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dotsweep-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dotsweep-com/mcp/dotsweep-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dotsweep-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/dotsweep-com/hosts/dotsweep-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dotsweep-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dotsweep-com/vendors/dotsweep-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dotsweep-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dotsweep.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://dotsweep.com/tld/press
- group: docs
  title: ''
  type: Documentation
  url: https://dotsweep.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://dotsweep.com/setup
- group: auth
  href: https://artifacts.apis.io/dotsweep-com/security/dotsweep-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dotsweep-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dotsweep.com/
coverage:
  checked: '2026-11-06'
  detail: Provider docs list API endpoints but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts are available.
  evidence:
  - status: 200
    url: https://dotsweep.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: 'dotsweep-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://dotsweep.com/img/og.jpg
json_schemas:
- name: GetCheckExampleComResponse
  property_count: 1
  slug: dotsweep-com-get-check-example-com-response
- name: PostCheckRequest
  property_count: 1
  slug: dotsweep-com-post-check-request
- name: PostCheckResponse
  property_count: 1
  slug: dotsweep-com-post-check-response
- name: PostMcpRequest
  property_count: 3
  slug: dotsweep-com-post-mcp-request
jsonld:
- class_count: 4
  name: Dotsweep Com Context
  property_count: 5
  slug: dotsweep-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at dotsweep.com.
  name: dotsweep-com MCP Server
  slug: dotsweep-com-mcp-yml
modified: '2026-11-05'
name: dotsweep-com
nav: Providers
network: true
overview: 'dotsweep-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Domain Search, Domain Registries, and Privacy.


  The dotsweep-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  dotsweep-com''s developer surface includes documentation, getting-started guide, and 13 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 69
  extends:
  - spectral:oas
  name: dotsweep-com API Rules
  rule_count: 28
  severity_counts:
    error: 26
    hint: 0
    info: 1
    warn: 1
  slug: dotsweep-com-rules
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 41.8
    catalog_earned_first_party: 0.0
    catalog_gap: 73.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 19.3
    developer_ergonomics: 21.4
    discoverability: 41.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
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
  name: Dotsweep Com Domain Security
  slug: dotsweep-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dotsweep-com
tags:
- Domain Search
- Domain Registries
- Privacy
website: https://dotsweep.com/
---
