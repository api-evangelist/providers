---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Agentfilings Com Agentic Access
  operation_count: 5
  slug: agentfilings-com-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://api.agentfilings.com
  baseurl_source: declared
  description: The Earnings API from AgentFilings — 1 operation(s) for earnings.
  name: AgentFilings Earnings API
  slug: agentfilings-com-earnings-api
- baseURL: https://api.agentfilings.com
  baseurl_source: declared
  description: The Filings API from AgentFilings — 1 operation(s) for filings.
  name: AgentFilings Filings API
  slug: agentfilings-com-filings-api
- baseURL: https://api.agentfilings.com
  baseurl_source: declared
  description: The Health API from AgentFilings — 1 operation(s) for health.
  name: AgentFilings Health API
  slug: agentfilings-com-health-api
- baseURL: https://api.agentfilings.com
  baseurl_source: declared
  description: The Insiders API from AgentFilings — 1 operation(s) for insiders.
  name: AgentFilings Insiders API
  slug: agentfilings-com-insiders-api
- baseURL: https://api.agentfilings.com
  baseurl_source: declared
  description: The Probe API from AgentFilings — 1 operation(s) for probe.
  name: AgentFilings Probe API
  slug: agentfilings-com-probe-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/agentfilings-com/agentic-access/agentfilings-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentfilings-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentfilings-com/rules/agentfilings-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agentfilings-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agentfilings-com/json-ld/agentfilings-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agentfilings-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/agentfilings-com/vocabulary/agentfilings-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentfilings-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agentfilings-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentfilings-com/data-model/agentfilings-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentfilings-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/agentfilings-com/errors/agentfilings-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentfilings-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentfilings-com/conformance/agentfilings-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentfilings-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentfilings-com/llms/agentfilings-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentfilings-com-llms.txt
- group: build
  href: https://artifacts.apis.io/agentfilings-com/mcp/agentfilings-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentfilings-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agentfilings-com/mcp/agentfilings-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentfilings-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/agentfilings-com/hosts/agentfilings-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentfilings-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/agentfilings-com/security/agentfilings-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentfilings-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentfilings.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.agentfilings.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.agentfilings.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.agentfilings.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://api.agentfilings.com/probe
created: '2026-10-31'
description: AgentFilings provides structured US SEC/EDGAR filing data for AI agents, offering filings, XBRL-derived earnings, and Form 4 insider transactions as clean JSON. The service offers unlimited calls to all endpoints and MCP tools with a single API key, no per‑call charges, and supports autonomous agents with payment via x402 in USDC on Base. Data is refreshed daily from SEC EDGAR, ensuring up-to‑date company metadata and insider transaction information.
image: https://api.agentfilings.com/favicon.svg
json_schemas:
- name: Envelope
  property_count: 2
  slug: agentfilings-com-envelope
jsonld:
- class_count: 2
  name: Agentfilings Com Context
  property_count: 3
  slug: agentfilings-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.agentfilings.com.
  name: AgentFilings MCP Server
  slug: agentfilings-com-mcp-yml
modified: '2026-10-31'
name: AgentFilings
nav: Providers
network: true
overview: 'AgentFilings publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Earnings API, Filings API, Health API, and 2 more. Tagged areas include SEC, EDGAR, Finance, Artificial Intelligence, and Data.


  The AgentFilings catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AgentFilings'' developer surface includes documentation, API reference, getting-started guide, and 15 more developer resources.'
random_paper: 7
rate_limits:
- limit_count: 0
  name: Agentfilings Com Rate Limits
  slug: agentfilings-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: AgentFilings API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: agentfilings-com-rules
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 53.2
    catalog_earned_first_party: 0.0
    catalog_gap: 61.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 46.5
    developer_ergonomics: 25.5
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 28.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 9.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentfilings Com Authentication
  slug: agentfilings-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agentfilings Com Domain Security
  slug: agentfilings-com-domain-security
  summary_line: TLSv1.3
skill_count: 4
skills:
- name: get-earnings-summary
  slug: agentfilings-com-get-earnings-summary
- name: get-insider-transactions
  slug: agentfilings-com-get-insider-transactions
- name: get-latest-filings
  slug: agentfilings-com-get-latest-filings
- name: probe-coverage
  slug: agentfilings-com-probe-coverage
slug: agentfilings-com
tags:
- SEC
- EDGAR
- Finance
- Artificial Intelligence
- Data
- Filings
website: https://agentfilings.com/
---
