---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Bridgenode Cc Agentic Access
  operation_count: 3
  slug: bridgenode-cc-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://bridgenode.cc
  baseurl_source: declared
  description: The Models API from BridgeNode — 1 operation(s) for models.
  name: BridgeNode Models API
  slug: bridgenode-cc-models-api
- baseURL: https://bridgenode.cc
  baseurl_source: declared
  description: The Chat Completions API from BridgeNode — 1 operation(s) for chat completions.
  name: BridgeNode Chat Completions API
  slug: bridgenode-cc-chat-completions-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/bridgenode-cc/agentic-access/bridgenode-cc-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bridgenode-cc-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/bridgenode-cc/plans/bridgenode-cc-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bridgenode-cc-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bridgenode-cc/rules/bridgenode-cc-rules.yml
  title: ''
  type: Spectral
  url: rules/bridgenode-cc-rules.yml
- group: agent
  href: https://artifacts.apis.io/bridgenode-cc/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bridgenode-cc/errors/bridgenode-cc-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bridgenode-cc-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bridgenode-cc/conformance/bridgenode-cc-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bridgenode-cc-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bridgenode-cc/llms/bridgenode-cc-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bridgenode-cc-llms.txt
- group: other
  href: https://artifacts.apis.io/bridgenode-cc/a2a/bridgenode-cc-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/bridgenode-cc-a2a.yml
- group: agent
  href: https://artifacts.apis.io/bridgenode-cc/mcp/bridgenode-cc-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bridgenode-cc-mcp.yml
- group: agent
  href: https://artifacts.apis.io/bridgenode-cc/well-known/bridgenode-cc-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bridgenode-cc-well-known.yml
- group: other
  href: https://artifacts.apis.io/bridgenode-cc/hosts/bridgenode-cc-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bridgenode-cc-hosts.yml
- group: other
  href: https://artifacts.apis.io/bridgenode-cc/vendors/bridgenode-cc-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bridgenode-cc-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bridgenode.cc/terms
- group: auth
  href: https://artifacts.apis.io/bridgenode-cc/authentication/bridgenode-cc-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bridgenode-cc-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bridgenode-cc/security/bridgenode-cc-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bridgenode-cc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bridgenode.cc/
created: '2026-11-03'
description: BridgeNode provides AI inference bridge for AI agents, offering OpenAI‑compatible chat completions paid per request with Solana USDC via x402. No API keys, no registration, and free models are available. The service includes tool calling, model pricing, and detailed documentation at bridgenode.cc.
image: https://bridgenode.cc/logos/bridgenode-v2.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at bridgenode.cc.
  name: BridgeNode MCP Server
  slug: bridgenode-cc-mcp-yml
modified: '2026-11-03'
name: BridgeNode
nav: Providers
network: true
overview: 'BridgeNode publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Models API and Chat Completions API. Tagged areas include Artificial Intelligence, Inference, Payments, Solana, and OpenAI-Compatible.


  The BridgeNode catalog on APIs.io includes 1 Spectral governance ruleset.


  BridgeNode''s developer surface includes authentication and 15 more developer resources.'
plans:
- name: Bridgenode Cc Plans Pricing
  plan_count: 36
  slug: bridgenode-cc-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: BridgeNode API Rules
  rule_count: 37
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 1
  slug: bridgenode-cc-rules
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 50.5
    developer_ergonomics: 13.7
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bridgenode Cc Authentication
  slug: bridgenode-cc-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bridgenode Cc Domain Security
  slug: bridgenode-cc-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: bridgenode-cc-chat-completion-with-model-list
  slug: bridgenode-cc-chat-completion-with-model-list
slug: bridgenode-cc
tags:
- Artificial Intelligence
- Inference
- Payments
- Solana
- OpenAI-Compatible
website: https://bridgenode.cc/
---
