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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Public API and MCP server for accessing tool data and job guides.
  name: Coghelm API
  slug: coghelm-api
- description: 'Coghelm API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Coghelm API
  slug: coghelm-com-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/coghelm-com/rules/coghelm-com-rules.yml
  title: ''
  type: Spectral
  url: rules/coghelm-com-rules.yml
- group: design
  href: https://artifacts.apis.io/coghelm-com/json-ld/coghelm-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/coghelm-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/coghelm-com/vocabulary/coghelm-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coghelm-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/coghelm-com/data-model/coghelm-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coghelm-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/coghelm-com/changelog/coghelm-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/coghelm-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/coghelm-com/conformance/coghelm-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coghelm-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coghelm-com/llms/coghelm-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coghelm-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/coghelm-com/mcp/coghelm-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/coghelm-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/coghelm-com/well-known/coghelm-com-clickup-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coghelm-com-clickup-security.txt
- group: auth
  href: https://artifacts.apis.io/coghelm-com/well-known/coghelm-com-circleback-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coghelm-com-circleback-security.txt
- group: auth
  href: https://artifacts.apis.io/coghelm-com/well-known/coghelm-com-chatgpt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coghelm-com-chatgpt-security.txt
- group: auth
  href: https://artifacts.apis.io/coghelm-com/well-known/coghelm-com-asana-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coghelm-com-asana-security.txt
- group: agent
  href: https://artifacts.apis.io/coghelm-com/well-known/coghelm-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coghelm-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/coghelm-com/hosts/coghelm-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coghelm-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/coghelm-com/vendors/coghelm-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coghelm-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coghelm.com/terms/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://coghelm.com/developers/
- group: start
  title: ''
  type: GettingStarted
  url: https://coghelm.com/jobs/onboarding-a-new-hire/
- group: auth
  href: https://artifacts.apis.io/coghelm-com/security/coghelm-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coghelm-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coghelm.com/
coverage:
  checked: '2026-11-04'
  detail: Developers page provides API info but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contracts.
  evidence:
  - status: 200
    url: https://coghelm.com/developers/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Coghelm curates a directory of AI tools organized by the specific jobs leaders need to accomplish. It serves nonprofit, business, academic, and government leaders with curated tool recommendations, guides, and a playbook PDF. The platform also offers a public API and MCP server for developers to access tool data and job guides programmatically.
json_schemas:
- name: PostApiJobsRunning11SRequest
  property_count: 3
  slug: coghelm-com-post-api-jobs-running11-srequest
- name: PostMcpRequest
  property_count: 4
  slug: coghelm-com-post-mcp-request
jsonld:
- class_count: 2
  name: Coghelm Com Context
  property_count: 4
  slug: coghelm-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at coghelm.com.
  name: Coghelm MCP Server
  slug: coghelm-com-mcp-yml
modified: '2026-11-04'
name: Coghelm
nav: Providers
network: true
overview: 'Coghelm is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Directory, Tools, Leaders, and Non-Profit.


  The Coghelm catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Coghelm''s developer surface includes changelog, getting-started guide, and 18 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: Coghelm API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: coghelm-com-rules
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 49.8
    catalog_earned_first_party: 0.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 18.9
    developer_ergonomics: 21.4
    discoverability: 53.3
    operational_transparency: 26.3
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
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coghelm Com Domain Security
  slug: coghelm-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: coghelm-com
tags:
- Artificial Intelligence
- Directory
- Tools
- Leaders
- Non-Profit
website: https://coghelm.com/
---
