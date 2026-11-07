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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for scanning sites, retrieving scan history, badges, reports, and MCP tools.
  name: AgentGrade API
  slug: agentgrade-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/agentgrade-com/rules/agentgrade-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agentgrade-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agentgrade-com/conformance/agentgrade-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentgrade-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentgrade-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/agentgrade-com/security/agentgrade-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/agentgrade-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/agentgrade-com/errors/agentgrade-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentgrade-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/agentgrade-com/llms/agentgrade-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentgrade-com-llms.txt
- group: build
  href: https://artifacts.apis.io/agentgrade-com/mcp/agentgrade-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentgrade-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/agentgrade-com/mcp/agentgrade-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentgrade-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/agentgrade-com/well-known/agentgrade-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentgrade-com-security.txt
- group: agent
  href: https://artifacts.apis.io/agentgrade-com/well-known/agentgrade-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentgrade-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentgrade-com/hosts/agentgrade-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentgrade-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/agentgrade-com/security/agentgrade-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentgrade-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentgrade-com/security/agentgrade-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentgrade-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentgrade.com/
- group: docs
  title: ''
  type: Documentation
  url: https://agentgrade.com/kb/
- group: docs
  title: ''
  type: APIReference
  url: https://agentgrade.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://agentgrade.com/kb/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Agentic-Adventures
created: '2026-10-31'
description: AgentGrade is an AI agent readiness scanner that evaluates websites for compliance with protocols such as MCP, llms.txt, x402 payments, A2A, and more. It provides free instant grading and remediation guidance, helping site owners make their services discoverable and usable by autonomous AI agents. The platform offers tools like llms.txt validator, MCP server tester, and robots.txt generator, and publishes extensive knowledge base articles covering standards, payment protocols, and best practices for AI agents.
image: https://agentgrade.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at agentgrade.com.
  name: AgentGrade MCP Server
  slug: agentgrade-com-mcp-yml
modified: '2026-10-31'
name: AgentGrade
nav: Providers
network: true
overview: 'AgentGrade publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Agent Readiness, MCP, Llms.txt, and Payments.


  The AgentGrade catalog on APIs.io includes 1 Spectral governance ruleset.


  AgentGrade''s developer surface includes documentation, API reference, getting-started guide, and 15 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: AgentGrade API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: agentgrade-com-rules
scopes:
- name: Agentgrade Com Scopes
  scope_count: 0
  slug: agentgrade-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.2
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 24.0
    developer_ergonomics: 20.7
    discoverability: 65.0
    operational_transparency: 13.2
  previous_composite: 24.2
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agentgrade Com Authentication
  slug: agentgrade-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agentgrade Com Domain Security
  slug: agentgrade-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Agentgrade Com Vulnerability Disclosure
  slug: agentgrade-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: scan-url
  slug: agentgrade-com-scan-url-skill
slug: agentgrade-com
tags:
- Artificial Intelligence
- Agent Readiness
- MCP
- Llms.txt
- Payments
website: https://agentgrade.com/
---
