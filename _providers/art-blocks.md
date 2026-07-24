---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Art Blocks Agentic Access
  operation_count: 3
  slug: art-blocks-agentic-access
  summary_line: 3 operations
api_count: 8
apis:
- description: Hasura-backed GraphQL API providing structured access to on-chain and off-chain Art Blocks data including projects, tokens, artists, contracts, minter configurations, features, tags, and ownership. Al
  name: Art Blocks GraphQL API (Hasura)
  slug: graphql-api
- description: Decentralised subgraph on The Graph Network providing on-chain-only data for Art Blocks tokens, projects, and ownership on Ethereum mainnet. Uses camelCase field names and the base entity names (witho
  name: Art Blocks Subgraph — Ethereum
  slug: subgraph-ethereum
- description: Decentralised subgraph on The Graph Network providing on-chain-only data for Art Blocks tokens, projects, and ownership on Arbitrum One. Requires a developer API key from The Graph Studio.
  name: Art Blocks Subgraph — Arbitrum One
  slug: subgraph-arbitrum
- description: Decentralised subgraph on The Graph Network providing on-chain-only data for Art Blocks tokens, projects, and ownership on Base. Requires a developer API key from The Graph Studio.
  name: Art Blocks Subgraph — Base
  slug: subgraph-base
- description: Model Context Protocol server exposing 21 tools for AI agents to interact with the Art Blocks ecosystem across Ethereum, Arbitrum, and Base. Tools cover discovering projects, exploring artist portfoli
  name: Art Blocks MCP Server
  slug: mcp-server
- description: Live generative artwork view endpoints.
  name: Art Blocks Generator API
  slug: art-blocks-generator-api
- description: Static image media proxy endpoints.
  name: Art Blocks Media API
  slug: art-blocks-media-api
- description: ERC-721 token metadata endpoints.
  name: Art Blocks Token Metadata API
  slug: art-blocks-token-metadata-api
artifact_total: 14
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/art-blocks-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/art-blocks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.artblocks.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.artblocks.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ArtBlocks
- group: company
  title: ''
  type: Twitter
  url: https://x.com/artblocks_io
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/artblocks
- group: commercial
  title: ''
  type: Plans
  url: plans/art-blocks-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/art-blocks-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/art-blocks-finops.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/art-blocks.json
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: '2026-06-13'
description: 'Art Blocks is the leading on-chain generative art platform where artists deploy deterministic code to Ethereum, Arbitrum One, and Base; each token is minted by invoking the script with a unique hash, producing a one-of-a-kind artwork stored permanently on-chain. The platform exposes four public API surfaces: a Token API that returns ERC-721 metadata conforming to the OpenSea standard, a Generator API that serves an iframe-able live view of each artwork, a Media Proxy API that provides static PNG renders, and a Hasura GraphQL API (data.artblocks.io) that gives structured access to on-chain and off-chain data including projects, tokens, artists, features, minting configuration, and ownership. Decentralised access is available through The Graph subgraph for on-chain-only data across all three networks. An MCP Server with 21 tools enables AI-agent integration for querying, minting, and generative script scaffolding.'
finops:
- name: Art Blocks Finops
  service_category: ''
  slug: art-blocks-finops
graphqls:
- description: The Art Blocks Hasura GraphQL API provides structured access to on-chain and off-chain data for the Art Blocks generative art platform. It exposes projects, tokens, artists, contracts, minter configur
  name: Art Blocks GraphQL API
  slug: art-blocks-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/art-blocks.png
layout: provider
modified: '2026-06-13'
name: Art Blocks
nav: Providers
network: true
overview: 'Art Blocks publishes 3 APIs on the [APIs.io](https://apis.io/) network: Generator API, Media API, and Token Metadata API. Tagged areas include Generative Art, NFT, On-Chain Art, Blockchain, and Ethereum.


  Art Blocks'' developer surface includes documentation, engineering blog, and 10 more developer resources.'
plans:
- name: Art Blocks Plans
  plan_count: 4
  slug: art-blocks-plans
random_paper: 41
rate_limits:
- limit_count: 0
  name: Art Blocks Rate Limits
  slug: art-blocks-rate-limits
score:
  band: thin
  composite: 35.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.5
    developer_ergonomics: 10.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 35.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/art-blocks/refs/heads/main/screenshots/art-blocks-2026-06-20T172442.png
security:
- kind: domain-security
  name: Art Blocks Domain Security
  slug: art-blocks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: art-blocks
tags:
- Generative Art
- NFT
- On-Chain Art
- Blockchain
- Ethereum
- Arbitrum
- Base
- GraphQL
- Token Metadata
- Web3
- Smart Contracts
- The Graph
- MCP
website: https://www.artblocks.io
---
