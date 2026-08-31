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
    agent_card: false
    agent_skills: true
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.4
  scored_at: '2026-08-30'
api_count: 2
apis:
- description: The protocol's read/write boundary — a caching and relay layer between protocol participants and the Vana L1 covering the onchain primitives (identity, permissions, fees, PGE, schemas, files, DLP cont
  name: Vana Data Portability RPC
  slug: vana-data-portability-rpc
- description: 'Standard Ethereum JSON-RPC for the EVM-compatible Vana L1 blockchain, which records registrations, grants, file records, and schemas. Mainnet at rpc.vana.org (explorer vanascan.io); Moksha testnet at '
  name: Vana L1 JSON-RPC
  slug: vana-l1-json-rpc
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.vana.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.vana.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vana.org
- group: docs
  title: ''
  type: APIReference
  url: https://docs.vana.org/protocol-reference/full-specification
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vana.org/build-a-vana-app
- group: operate
  title: ''
  type: Support
  url: https://docs.vana.org/resources/community-discord
- group: company
  title: ''
  type: Blog
  url: https://vana.org/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vana-com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vana.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vana.org/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.vana.org
- group: other
  title: ''
  type: Whitepaper
  url: https://docs.vana.org/resources/whitepaper
- group: build
  title: ''
  type: Packages
  url: packages/vana-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vana-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/vana-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vana-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vana-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vana-website-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/vana-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vana-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vana-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vana-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vana-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vana-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.vana.org/resources/security
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vana-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vana-conventions.yml
- group: build
  title: ''
  type: CLI
  url: cli/vana-cli.yml
- group: design
  title: ''
  type: Components
  url: components/vana-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Vana is an open protocol for user-owned, portable personal data — sovereign data infrastructure for the AI economy. Users store personal data in Personal Servers, grant builders access via signed, scope-native EIP-712 permissions, pay protocol fees from an onchain escrow, and revoke access at any time, with all consent recorded on the EVM-compatible Vana L1. Builders integrate through the @opendatalabs/vana-sdk, the Data Portability RPC, a local-first data-collection CLI, and an MCP interface on every Personal Server. Stewarded by the Vana Foundation and developed by Open Data Labs; backed by Paradigm.
image: https://vana.org/assets/logos/vana-asterisk-data-signal.svg
layout: provider
mcp_servers:
- description: ''
  name: Vana MCP Server
  slug: vana-mcp-server
modified: '2026-07-21'
name: Vana
nav: Providers
network: true
overview: 'Vana publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Ai, Data Portability, Personal Data, and Data Sovereignty.


  Vana''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 23 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 15
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 85.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 35.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Vana Authentication
  slug: vana-authentication
  summary_line: web3-signed/eip712-grants/oauth2-oidc · 4 schemes
- kind: domain-security
  name: Vana Domain Security
  slug: vana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vana Vulnerability Disclosure
  slug: vana-vulnerability-disclosure
  summary_line: contact published
slug: vana
tags:
- Company
- Crypto Ai
- Data Portability
- Personal Data
- Data Sovereignty
- Blockchain
- Web3
- Agents
- Artificial Intelligence
website: https://www.vana.org
---
