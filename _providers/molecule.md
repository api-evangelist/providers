---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 33.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Single GraphQL endpoint serving the Data API (browse IP-NFTs, IPTs, and market data), the Tokenization API (mint IP-NFTs and fractionalize into IPTs), and the Labs API (manage research datarooms, file
  name: Molecule GraphQL API
  slug: molecule-graphql-api
artifact_total: 4
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.molecule.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.molecule.xyz/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.molecule.xyz/api-reference/api-reference.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.molecule.xyz/user-guides/developers-ai-agents.md
- group: company
  title: ''
  type: Website
  url: https://molecule.xyz/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moleculeprotocol
- group: operate
  title: ''
  type: Support
  url: https://docs.molecule.xyz/resources/faqs.md
- group: company
  title: ''
  type: Blog
  url: https://molecule.xyz/blog
- group: auth
  title: ''
  type: Authentication
  url: authentication/molecule-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/molecule-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/molecule-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/molecule-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/molecule-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/molecule-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/molecule-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/molecule-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/molecule-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.molecule.xyz/security/bug-bounty
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Molecule is decentralized-science (DeSci) infrastructure for recording, tokenizing, funding, and accelerating scientific research onchain. Backed by Speedinvest, Molecule lets researchers create onchain Labs (secure research datarooms), mint IP-NFTs that register legal intellectual-property rights, fractionalize them into tradeable ERC-20 IP Tokens (IPTs), and raise funding from a global community. Its developer platform exposes a GraphQL API — a Data API for browsing IP-NFTs, IPTs, and market data; a Tokenization API for minting and fractionalizing IP; and a Labs API for managing research datarooms — plus an x402 pay-per-call HTTP 402 gateway for autonomous agents, a hosted Model Context Protocol (MCP) server, and MIRA/BIOS AI tooling. The onchain stack (ERC-4337/6551/7579 smart accounts, ERC-7484 module registry, IP-NFTs) is deployed on Base and audited by Cyfrin and Pashov.
image: https://github.com/moleculeprotocol.png
layout: provider
mcp_servers:
- description: ''
  name: molecule-mcp.yml
  slug: molecule-mcpyml
modified: '2026-07-20'
name: Molecule
nav: Providers
network: true
overview: 'Molecule publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DeSci, Decentralized Science, Blockchain, and Web3.


  Molecule''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 13 more developer resources.'
random_paper: 38
score:
  band: emerging
  composite: 28.6
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 67.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 28.6
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 50.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Molecule Authentication
  slug: molecule-authentication
  summary_line: apiKey/http/custom · 4 schemes
- kind: vulnerability-disclosure
  name: Molecule Vulnerability Disclosure
  slug: molecule-vulnerability-disclosure
  summary_line: disclosure policy published
slug: molecule
tags:
- Company
- DeSci
- Decentralized Science
- Blockchain
- Web3
- GraphQL
- Intellectual Property
- IP-NFT
- Tokenization
- Life Sciences
- Biotech
- Research Funding
- AI Agents
- MCP
- x402
website: https://molecule.xyz/
---
