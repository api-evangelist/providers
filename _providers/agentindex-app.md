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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 12.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Agentindex App Agentic Access
  operation_count: 3
  slug: agentindex-app-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- description: Public read‑only API for browsing agents, MCP servers and tools. No authentication required.
  name: AgentIndex API
  slug: agentindex-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/agentindex-app/agentic-access/agentindex-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agentindex-app-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agentindex-app/rules/agentindex-app-rules.yml
  title: ''
  type: Spectral
  url: rules/agentindex-app-rules.yml
- group: agent
  href: https://artifacts.apis.io/agentindex-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agentindex-app/errors/agentindex-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentindex-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentindex-app/conformance/agentindex-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentindex-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentindex-app/llms/agentindex-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentindex-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentindex-app/mcp/agentindex-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentindex-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentindex-app/well-known/agentindex-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentindex-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentindex-app/hosts/agentindex-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentindex-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentindex-app/vendors/agentindex-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentindex-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentindex.app/en/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentindex.app/en/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://agentindex.app/en/guides/
- group: docs
  title: ''
  type: APIReference
  url: https://agentindex.app/llms.txt
- group: auth
  href: https://artifacts.apis.io/agentindex-app/security/agentindex-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentindex-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentindex.app/
created: '2026-11-01'
description: AgentIndex is a curated directory of over 3,000 open-source AI agents, MCP servers, and agent frameworks. Updated daily, it provides reviews, selection guides, and detailed listings to help users discover and compare AI tools across categories. The platform also offers insights into MCP server implementations and community-driven rankings, serving developers, researchers, and enterprises seeking the best AI solutions in 2026.
image: https://agentindex.app/en/opengraph-image?d8eaa465c6d634ef
layout: provider
mcp_servers:
- description: Remote MCP server at agentindex.app.
  name: AgentIndex MCP Server
  slug: agentindex-app-mcp-yml
modified: '2026-11-01'
name: AgentIndex
nav: Providers
network: true
overview: 'AgentIndex is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Directory, Open Source, Tools, and MCP.


  The AgentIndex catalog on APIs.io includes 1 Spectral governance ruleset.


  AgentIndex''s developer surface includes documentation, API reference, and 14 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: AgentIndex API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: agentindex-app-rules
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.8
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 17.9
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentindex App Domain Security
  slug: agentindex-app-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agentindex-app
tags:
- Artificial Intelligence
- Directory
- Open Source
- Tools
- MCP
website: https://agentindex.app/
---
