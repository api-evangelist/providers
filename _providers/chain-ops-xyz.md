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
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Chain Ops Xyz Agentic Access
  operation_count: 4
  slug: chain-ops-xyz-agentic-access
  summary_line: 4 operations
api_count: 2
apis:
- description: Compare real-time gas prices across up to 9 EVM chains and get a cheapest-chain recommendation. Pay-per-call via x402 (USDC on Base). No API key.
  name: MGO Multi-chain Gas Optimizer
  slug: mgo-multi-chain-gas-optimizer
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/chain-ops-xyz/agentic-access/chain-ops-xyz-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/chain-ops-xyz-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/chain-ops-xyz/rules/chain-ops-xyz-rules.yml
  title: ''
  type: Spectral
  url: rules/chain-ops-xyz-rules.yml
- group: design
  href: https://artifacts.apis.io/chain-ops-xyz/json-ld/chain-ops-xyz-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chain-ops-xyz-context.jsonld
- group: design
  href: https://artifacts.apis.io/chain-ops-xyz/vocabulary/chain-ops-xyz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chain-ops-xyz-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/chain-ops-xyz/data-model/chain-ops-xyz-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chain-ops-xyz-data-model.yml
- group: design
  href: https://artifacts.apis.io/chain-ops-xyz/errors/chain-ops-xyz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/chain-ops-xyz-problem-types.yml
- group: design
  href: https://artifacts.apis.io/chain-ops-xyz/conformance/chain-ops-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chain-ops-xyz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chain-ops-xyz/llms/chain-ops-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chain-ops-xyz-llms.txt
- group: other
  href: https://artifacts.apis.io/chain-ops-xyz/a2a/chain-ops-xyz-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/chain-ops-xyz-a2a.yml
- group: build
  href: https://artifacts.apis.io/chain-ops-xyz/mcp/chain-ops-xyz-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/chain-ops-xyz-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/chain-ops-xyz/mcp/chain-ops-xyz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/chain-ops-xyz-mcp.yml
- group: other
  href: https://artifacts.apis.io/chain-ops-xyz/hosts/chain-ops-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chain-ops-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/chain-ops-xyz/vendors/chain-ops-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chain-ops-xyz-vendors.yml
- group: build
  href: https://artifacts.apis.io/chain-ops-xyz/packages/chain-ops-xyz-packages.yml
  title: ''
  type: SDKs
  url: packages/chain-ops-xyz-packages.yml
- group: build
  href: https://artifacts.apis.io/chain-ops-xyz/packages/chain-ops-xyz-packages.yml
  title: ''
  type: Packages
  url: packages/chain-ops-xyz-packages.yml
- group: auth
  href: https://artifacts.apis.io/chain-ops-xyz/security/chain-ops-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chain-ops-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chain-ops.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://api.mgo.chain-ops.xyz/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://api.mgo.chain-ops.xyz
- group: start
  title: ''
  type: GettingStarted
  url: https://chain-ops.xyz/#quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dlrjsdl200-byte
created: '2026-11-03'
description: Chain-ops provides pay-per-call on-chain data APIs for AI agents, offering live gas price comparisons across 9 EVM chains via the x402 protocol. Pricing starts at $0.001 per call in USDC on Base, with no API key required. The platform includes an open-source SDK for Node.js and supports ERC‑8004 agent identity.
image: https://chain-ops.xyz/og.png
jsonld:
- class_count: 1
  name: Chain Ops Xyz Context
  property_count: 6
  slug: chain-ops-xyz-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.mgo.chain-ops.xyz.
  name: chain-ops MCP Server
  slug: chain-ops-xyz-mcp-yml
modified: '2026-11-03'
name: chain-ops
nav: Providers
network: true
overview: 'chain-ops publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, Artificial Intelligence, Payments, and Gas.


  The chain-ops catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  chain-ops'' developer surface includes documentation, API reference, getting-started guide, and 18 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: chain-ops API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: chain-ops-xyz-rules
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 6.7
    developer_ergonomics: 21.4
    discoverability: 56.7
    operational_transparency: 2.6
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chain Ops Xyz Domain Security
  slug: chain-ops-xyz-domain-security
  summary_line: TLSv1.3 · HSTS
slug: chain-ops-xyz
tags:
- Blockchain
- Artificial Intelligence
- Payments
- Gas
website: https://chain-ops.xyz/
---
