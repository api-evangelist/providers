---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Structured business data, indexed web search and source evidence for AI agents via a single API.
  name: AgentWeb.live API
  slug: agentweb-live-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/agentweb-live/rules/agentweb-live-rules.yml
  title: ''
  type: Spectral
  url: rules/agentweb-live-rules.yml
- group: design
  href: https://artifacts.apis.io/agentweb-live/json-ld/agentweb-live-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentweb-live-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentweb-live/vocabulary/agentweb-live-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentweb-live-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentweb-live/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentweb-live/data-model/agentweb-live-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentweb-live-data-model.yml
- group: design
  href: https://artifacts.apis.io/agentweb-live/errors/agentweb-live-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentweb-live-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentweb-live/conformance/agentweb-live-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentweb-live-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentweb-live/llms/agentweb-live-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentweb-live-llms.txt
- group: build
  href: https://artifacts.apis.io/agentweb-live/mcp/agentweb-live-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentweb-live-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agentweb-live/mcp/agentweb-live-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentweb-live-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentweb-live/well-known/agentweb-live-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentweb-live-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentweb-live/hosts/agentweb-live-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentweb-live-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentweb-live/vendors/agentweb-live-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentweb-live-vendors.yml
- group: build
  href: https://artifacts.apis.io/agentweb-live/packages/agentweb-live-packages.yml
  title: ''
  type: SDKs
  url: packages/agentweb-live-packages.yml
- group: build
  href: https://artifacts.apis.io/agentweb-live/packages/agentweb-live-packages.yml
  title: ''
  type: Packages
  url: packages/agentweb-live-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://agentweb.live/directory/category/security
- group: auth
  href: https://artifacts.apis.io/agentweb-live/security/agentweb-live-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentweb-live-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentweb.live
- group: docs
  title: ''
  type: Documentation
  url: https://api.agentweb.live/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.agentweb.live/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://agentweb.live/install.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agentweb
created: '2026-10-29'
description: AgentWeb provides real‑world business data, web search, live local search, travel information, and a recipe engine for AI agents via a single API. It indexes over 128 million businesses across 195 countries, offering structured data such as phone numbers, addresses, categories, ratings, and live booking links. The platform also delivers indexed web search results and supports tool integration through its hosted MCP, enabling agents to perform searches, fetch data, and execute recipes without scraping.
image: https://agentweb.live/apple-touch-icon.png
jsonld:
- class_count: 16
  name: Agentweb Live Context
  property_count: 77
  slug: agentweb-live-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.agentweb.live.
  name: AgentWeb MCP Server
  slug: agentweb-live-mcp-yml
modified: '2026-10-29'
name: AgentWeb
nav: Providers
network: true
overview: 'AgentWeb publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, AI, Search, and Business.


  The AgentWeb catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AgentWeb''s developer surface includes documentation, API reference, getting-started guide, and 19 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: AgentWeb API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 2
  slug: agentweb-live-rules
scopes:
- name: Agentweb Live Scopes
  scope_count: 0
  slug: agentweb-live-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 53.8
    catalog_earned_first_party: 0.0
    catalog_gap: 61.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 14.7
    developer_ergonomics: 37.5
    discoverability: 65.0
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 30
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentweb Live Authentication
  slug: agentweb-live-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agentweb Live Domain Security
  slug: agentweb-live-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: search-businesses
  slug: agentweb-live-search-businesses
slug: agentweb-live
tags:
- Company
- Data
- AI
- Search
- Business
website: https://agentweb.live
---
