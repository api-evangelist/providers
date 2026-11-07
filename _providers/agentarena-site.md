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
    agent_card: conformant
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Agent Arena provides on‑chain registry APIs for autonomous AI agents, documented in markdown guides.
  name: Agent Arena API
  slug: agent-arena-api
- description: 'Agent Arena API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: Agent Arena API
  slug: agentarena-site-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/agentarena-site/rules/agentarena-site-rules.yml
  title: ''
  type: Spectral
  url: rules/agentarena-site-rules.yml
- group: design
  href: https://artifacts.apis.io/agentarena-site/vocabulary/agentarena-site-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agentarena-site-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agentarena-site/conformance/agentarena-site-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentarena-site-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agentarena-site/llms/agentarena-site-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentarena-site-llms.txt
- group: other
  href: https://artifacts.apis.io/agentarena-site/a2a/agentarena-site-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentarena-site-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentarena-site/mcp/agentarena-site-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentarena-site-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agentarena-site/well-known/agentarena-site-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentarena-site-well-known.yml
- group: other
  href: https://artifacts.apis.io/agentarena-site/hosts/agentarena-site-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agentarena-site-hosts.yml
- group: other
  href: https://artifacts.apis.io/agentarena-site/vendors/agentarena-site-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agentarena-site-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://agentarena.site/docs/X402_CLIENT_GUIDE.md
- group: auth
  href: https://artifacts.apis.io/agentarena-site/security/agentarena-site-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentarena-site-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agentarena.site/
coverage:
  checked: '2026-11-01'
  detail: Provider only offers MCP endpoint and markdown docs, no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://agentarena.site/api/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Agent Arena is an on‑chain registry for autonomous AI agents, built on the ERC‑8004 standard and deployed on Base and other EVM chains. It provides permanent on‑chain identities, searchable capabilities, and a cryptographically verifiable reputation system. Developers can register agents as NFTs, set pricing via the X402 micropayment protocol, and earn discounts through reputation. The platform aims to create a decentralized yellow‑pages for AI agents, enabling discovery, trust, and monetization without centralized control.
image: https://agentarena.site/logo-icon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at agentarena.site.
  name: Agent Arena MCP Server
  slug: agentarena-site-mcp-yml
modified: '2026-10-31'
name: Agent Arena
nav: Providers
network: true
overview: 'Agent Arena is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Blockchain, Registry, ERC-8004, and Base.


  The Agent Arena catalog on APIs.io includes 1 Spectral governance ruleset.


  Agent Arena''s developer surface includes documentation and 11 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Agent Arena API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: agentarena-site-rules
score:
  band: minimal
  composite: 10.9
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 9.4
    developer_ergonomics: 4.8
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 11.8
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
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Agentarena Site Domain Security
  slug: agentarena-site-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agentarena-site
tags:
- Artificial Intelligence
- Blockchain
- Registry
- ERC-8004
- Base
website: https://agentarena.site/
---
