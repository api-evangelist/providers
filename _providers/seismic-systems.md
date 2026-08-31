---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
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
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Seismic Systems Agentic Access
  operation_count: 2
  slug: seismic-systems-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: The tokens API from Seismic Systems — 2 operation(s) for tokens.
  name: Seismic Systems tokens API
  slug: seismic-systems-tokens-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Seismic SRC20 Factory REST tokens API
  slug: open-seismic-systems-tokens-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/seismic-systems-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/seismic-systems-src20-factory-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.seismic.systems/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.seismic.systems/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.seismic.systems/reference/rpc-methods.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.seismic.systems/getting-started/quickstart.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SeismicSystems
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/XSPNseXCvW
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.seismic.systems/reference/terms-of-service.md
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.seismic.systems/reference/privacy-policy.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/seismic-systems-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/seismic-systems-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/seismic-systems-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/seismic-systems-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/seismic-systems-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/seismic-systems-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/seismic-systems-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/seismic-systems-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/seismic-systems-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/seismic-systems-domain-security.yml
created: '2026-07-17'
description: Seismic Systems Inc. is a fintech company building a privacy-enabled ("encrypted") blockchain — a shielded EVM implementing the "Mercury" specification — that aims to power a complete stablecoin stack. Backed by a $17M seed led by a16z crypto, Seismic lets developers build private tokens (SRC20) whose balances and transfers are hidden from observers, using shielded types in Solidity, TEE-encrypted calldata (ECDH + AES-GCM), and authenticated "signed reads." It ships first-party client SDKs for TypeScript (seismic-viem, seismic-react), Python (seismic-web3), and Rust (seismic-alloy), an sfoundry developer toolchain (sforge/sanvil/ssolc), a public testnet with a faucet and block explorer, published Claude Code agent skills, and a read-only SRC20 Factory REST API for querying deployed tokens.
image: https://github.com/SeismicSystems.png
layout: provider
mcp_servers:
- description: No official hosted/remote MCP server was found for Seismic (the docs publish Claude Code workflow skills and CLAUDE.md templates instead — see skills/_index.yml). This is a CANDIDATE tool list derived
  name: Seismic Systems MCP Server
  slug: seismic-systems-mcp-server
modified: '2026-07-21'
name: Seismic Systems
nav: Providers
network: true
overview: 'Seismic Systems publishes 1 API on the [APIs.io](https://apis.io/) network: tokens API. Tagged areas include Company, Blockchain, Privacy, Encryption, and Stablecoins.


  Seismic Systems'' developer surface includes documentation, API reference, getting-started guide, support, CLI, sandbox, authentication, and 14 more developer resources.'
random_paper: 11
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 18
    catalog_gap: 63.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 4.5
    contract_quality: 12.4
    developer_ergonomics: 83.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 39.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Seismic Systems Authentication
  slug: seismic-systems-authentication
  summary_line: none/wallet-signature · 3 schemes
- kind: domain-security
  name: Seismic Systems Domain Security
  slug: seismic-systems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: seismic-systems
tags:
- Company
- Blockchain
- Privacy
- Encryption
- Stablecoins
- Fintech
- Web3
- Smart Contracts
- EVM
- Cryptography
- Developer Tools
website: https://docs.seismic.systems/
---
