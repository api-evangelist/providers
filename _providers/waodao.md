---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 39.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Waodao Agentic Access
  operation_count: 5
  slug: waodao-agentic-access
  summary_line: 5 operations
api_count: 4
apis:
- description: Traverse the daily Human + AI ArtChain.
  name: WAODAO Art Chain API
  slug: waodao-artchain-api
- description: Discover official WAO token deployments and registered DEX pools.
  name: WAODAO Liquidity Pools API
  slug: waodao-liquidity-pools-api
- description: Read WAODAO-specific field semantics and discovery links.
  name: WAODAO Schema API
  slug: waodao-schema-api
- description: Read agent-friendly metadata for a published WAODAO day.
  name: WAODAO Token Metadata API
  slug: waodao-token-metadata-api
artifact_total: 22
collections:
- collection_type: postman
  name: WAODAO Agent API
  slug: postman-waodao-agent-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Waodao Art Chain API
  slug: open-waodao-artchain-api
- collection_type: open
  name: Waodao Liquidity Pools API
  slug: open-waodao-liquidity-pools-api
- collection_type: open
  name: Waodao Schema API
  slug: open-waodao-schema-api
- collection_type: open
  name: Waodao Token Metadata API
  slug: open-waodao-token-metadata-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://waodao.ai/ai-agents
- group: docs
  title: ''
  type: Documentation
  url: https://waodao.gitbook.io/docs/
- group: operate
  title: ''
  type: Support
  url: https://waodao.ai/ai-agents#api-access
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/hsrkWhvDeS
- group: other
  title: ''
  type: Telegram
  url: https://t.me/waodao_ai
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/waodao_ai
- group: operate
  title: ''
  type: Roadmap
  url: https://waodao.gitbook.io/docs/development/roadmap
- group: other
  title: ''
  type: Disclaimer
  url: https://waodao.gitbook.io/docs/disclaimer
- group: build
  title: ''
  type: Postman
  url: postman/waodao-agent-api.postman_collection.json
- group: other
  title: ''
  type: APIsJSON
  url: https://waodao.ai/apis.json
- group: other
  title: ''
  type: APICatalog
  url: https://waodao.ai/.well-known/api-catalog
- group: agent
  title: ''
  type: WellKnown
  url: well-known/waodao-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/waodao-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/waodao-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/waodao-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/waodao-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/waodao-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/waodao-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/waodao-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/waodao-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/waodao-agent-api-overlay.yaml
- group: build
  title: ''
  type: Examples
  url: examples/waodao-token-day-1-example.json
- group: build
  title: ''
  type: Examples
  url: examples/waodao-pools-example.json
- group: build
  title: ''
  type: Examples
  url: examples/waodao-schema-example.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/waodao-token.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/waodao-index.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/waodao-pools.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/waodao-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/waodao-error.json
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/waodao-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/waodao-domain-security.yml
created: '2026-07-24'
description: 'WAODAO is a daily Human + AI "ArtChain": since 14 February 2023 one AI-generated NFT has been minted every day from world news signals, digital trends, human input and AI art, producing an on-chain cultural archive that stood at 1,272 published days when the index was read on 2026-08-09. The WAODAO Agent API is a public, read-only JSON API — five GET operations, no account, no API key, no authentication, CORS enabled — for traversing that ArtChain day by day and for discovering the official WAO token deployments (Ethereum ERC-20 and a Wormhole-bridged Solana SPL token) and the registered DEX liquidity pools across Uniswap, Balancer and Meteora. The project publishes an unusually complete machine-readable discovery surface for its size: OpenAPI 3.1 and a 3.0.2 compatibility contract, an APIs.json index at both /apis.json and the /.well-known alias, an RFC 9727 API catalog advertised on every response via a Link header, a Postman collection, and llms.txt on both the site and
  the GitBook docs.'
examples:
- key_count: 11
  name: Waodao Pools Example
  slug: waodao-pools-example
- key_count: 5
  name: Waodao Schema Example
  slug: waodao-schema-example
- key_count: 19
  name: Waodao Token Day 1 Example
  slug: waodao-token-day-1-example
image: https://waodao.ai/img/logo.png
json_schemas:
- name: ErrorResponse
  property_count: 2
  slug: waodao-error
- name: IndexResponse
  property_count: 13
  slug: waodao-index
- name: PoolsResponse
  property_count: 11
  slug: waodao-pools
- name: SchemaResponse
  property_count: 5
  slug: waodao
- name: TokenResponse
  property_count: 19
  slug: waodao-token
layout: provider
mcp_servers:
- description: ''
  name: WAODAO MCP Server
  slug: waodao-mcp-server
modified: '2026-08-09'
name: WAODAO
nav: Providers
network: true
overview: 'WAODAO publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Art Chain API, Liquidity Pools API, Schema API, and 1 more. Tagged areas include AI Agents, ArtChain, Human and AI, NFT Metadata, and On-chain Culture.


  WAODAO''s developer surface includes documentation, support, authentication, code examples, and 28 more developer resources.'
random_paper: 5
score:
  band: developing
  composite: 40.6
  delta: 3.8
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 30.3
    contract_quality: 59.0
    developer_ergonomics: 61.3
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 5.3
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Waodao Authentication
  slug: waodao-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Waodao Domain Security
  slug: waodao-domain-security
  summary_line: TLSv1.3
slug: waodao
tags:
- AI Agents
- ArtChain
- Human and AI
- NFT Metadata
- On-chain Culture
- Liquidity Pools
- Web3
- OpenAPI
- Ethereum
- Solana
- agent-native
- Digital Art
website: https://waodao.ai/ai-agents
---
