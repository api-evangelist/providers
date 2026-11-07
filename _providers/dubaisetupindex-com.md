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
  band: agent-ready
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Sourced, dated facts on UAE free zones, the Dubai mainland route and business activities.
  name: Dubai Setup Index HTTP API
  slug: dubai-setup-index-http-api
- baseURL: https://dubaisetupindex.com
  baseurl_source: declared
  description: Dubai Setup Index publishes guides to setting up a company in Dubai and the UAE. These endpoints serve the same facts as data.
  name: Dubai Setup Index HTTP API API
  slug: dubai-setup-index-http-api-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/dubaisetupindex-com/rules/dubaisetupindex-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dubaisetupindex-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dubaisetupindex-com/json-ld/dubaisetupindex-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dubaisetupindex-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dubaisetupindex-com/vocabulary/dubaisetupindex-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dubaisetupindex-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dubaisetupindex-com/conformance/dubaisetupindex-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dubaisetupindex-com-conformance.yml
- group: design
  href: https://artifacts.apis.io/dubaisetupindex-com/data-model/dubaisetupindex-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dubaisetupindex-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/dubaisetupindex-com/errors/dubaisetupindex-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dubaisetupindex-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/dubaisetupindex-com/llms/dubaisetupindex-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dubaisetupindex-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dubaisetupindex-com/mcp/dubaisetupindex-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dubaisetupindex-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dubaisetupindex-com/well-known/dubaisetupindex-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dubaisetupindex-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dubaisetupindex-com/hosts/dubaisetupindex-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dubaisetupindex-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dubaisetupindex-com/vendors/dubaisetupindex-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dubaisetupindex-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dubaisetupindex-com/security/dubaisetupindex-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dubaisetupindex-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dubaisetupindex.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://dubaisetupindex.com/openapi.json
  - status: 401
    url: https://dubaisetupindex.com/api/mcp
  - status: 403
    url: https://dubaisetupindex.com/
  reason: partner-login
  state: gated
created: '2026-11-06'
description: Dubai Setup Index provides a comprehensive comparison of UAE company setup costs across 43 free zones and Dubai mainland, offering up-to-date pricing, licensing requirements, and procedural details for entrepreneurs and businesses looking to establish a presence in the United Arab Emirates. The platform aggregates data from official sources, updates figures regularly, and presents them in an easy-to-navigate format, helping users make informed decisions about where to incorporate based on cost, speed, and regulatory considerations.
json_schemas:
- name: Attribution
  property_count: 11
  slug: dubaisetupindex-com-attribution
- name: Record
  property_count: 9
  slug: dubaisetupindex-com-record
jsonld:
- class_count: 4
  name: Dubaisetupindex Com Context
  property_count: 25
  slug: dubaisetupindex-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at dubaisetupindex.com requiring OAuth.
  name: Dubai Setup Index MCP Server
  slug: dubaisetupindex-com-mcp-yml
modified: '2026-11-06'
name: Dubai Setup Index
nav: Providers
network: true
overview: 'Dubai Setup Index publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including HTTP API API, and 1 more. Tagged areas include Company, United Arab Emirates, Business, Setup, and Comparison.


  The Dubai Setup Index catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Dubai Setup Index API Rules
  rule_count: 51
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 1
  slug: dubaisetupindex-com-rules
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 55.0
    developer_ergonomics: 0.0
    discoverability: 61.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dubaisetupindex Com Domain Security
  slug: dubaisetupindex-com-domain-security
  summary_line: TLSv1.3
slug: dubaisetupindex-com
tags:
- Company
- United Arab Emirates
- Business
- Setup
- Comparison
website: https://dubaisetupindex.com/
---
