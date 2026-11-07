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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: A9N9 Net Agentic Access
  operation_count: 6
  slug: a9n9-net-agentic-access
  summary_line: 6 operations · 6 acting
api_count: 1
apis:
- baseURL: https://agent.a9n9.net
  baseurl_source: declared
  description: The Research API from a9n9 — 2 operation(s) for research.
  name: a9n9 Research API
  slug: a9n9-net-research-api
- baseURL: https://agent.a9n9.net
  baseurl_source: declared
  description: The Search API from a9n9 — 1 operation(s) for search.
  name: a9n9 Search API
  slug: a9n9-net-search-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/a9n9-net/agentic-access/a9n9-net-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/a9n9-net-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/a9n9-net/rules/a9n9-net-rules.yml
  title: ''
  type: Spectral
  url: rules/a9n9-net-rules.yml
- group: agent
  href: https://artifacts.apis.io/a9n9-net/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/a9n9-net/errors/a9n9-net-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/a9n9-net-problem-types.yml
- group: design
  href: https://artifacts.apis.io/a9n9-net/conformance/a9n9-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/a9n9-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/a9n9-net/llms/a9n9-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/a9n9-net-llms.txt
- group: agent
  href: https://artifacts.apis.io/a9n9-net/mcp/a9n9-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/a9n9-net-mcp.yml
- group: other
  href: https://artifacts.apis.io/a9n9-net/hosts/a9n9-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/a9n9-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/a9n9-net/vendors/a9n9-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/a9n9-net-vendors.yml
- group: auth
  href: https://artifacts.apis.io/a9n9-net/security/a9n9-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/a9n9-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://a9n9.net/
- group: docs
  title: ''
  type: APIReference
  url: https://agent.a9n9.net/openapi.json
- group: docs
  title: ''
  type: Documentation
  url: https://agent.a9n9.net/
- group: start
  title: ''
  type: GettingStarted
  url: https://agent.a9n9.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agent.a9n9.net/
- group: operate
  title: ''
  type: Support
  url: https://agent.a9n9.net/health
created: '2026-10-31'
description: a9n9 provides an MPP‑paid AI agent deep‑research service that lets developers submit research objectives and receive exact quotes, a planned source list, and a comprehensive cross‑source report. The platform offers a free daily quick search for news and papers, supports paid per‑request evaluations, and exposes an OpenAPI specification for integration.
image: https://agent.a9n9.net/favicon.ico
layout: provider
mcp_servers:
- description: Remote MCP server at agent.a9n9.net.
  name: a9n9 MCP Server
  slug: a9n9-net-mcp-yml
modified: '2026-10-31'
name: a9n9
nav: Providers
network: true
overview: 'a9n9 publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Research API and Search API. Tagged areas include Artificial Intelligence, Research, Agents, MPP, and Deep Research.


  The a9n9 catalog on APIs.io includes 1 Spectral governance ruleset.


  a9n9''s developer surface includes API reference, documentation, getting-started guide, support, and 12 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: a9n9 API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: a9n9-net-rules
scopes:
- name: A9N9 Net Scopes
  scope_count: 0
  slug: a9n9-net-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 40.4
    developer_ergonomics: 27.9
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 29.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: A9N9 Net Authentication
  slug: a9n9-net-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: A9N9 Net Domain Security
  slug: a9n9-net-domain-security
  summary_line: TLSv1.3
skill_count: 3
skills:
- name: research-browserbase
  slug: a9n9-net-research-browserbase
- name: research-sample
  slug: a9n9-net-research-sample
- name: search
  slug: a9n9-net-search
slug: a9n9-net
tags:
- Artificial Intelligence
- Research
- Agents
- MPP
- Deep Research
- PaidAPI
website: https://a9n9.net/
---
