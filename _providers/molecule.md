---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.9
  scored_at: '2026-09-04'
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
- description: Hosted Model Context Protocol server that lets AI assistants query the Molecule DeSci ecosystem (IP Tokens, prices, project activity) in natural language. Streamable HTTP transport. Public endpoint is
  name: Molecule MCP Server
  slug: molecule-mcp-server
modified: '2026-07-20'
name: Molecule
nav: Providers
network: true
overview: 'Molecule publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DeSci, Decentralized Science, Blockchain, and Web3.


  Molecule''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 13 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 23.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 28.7
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/molecule/refs/heads/main/screenshots/molecule-2026-08-07T184106.png
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
