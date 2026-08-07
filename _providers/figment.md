---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 66.4
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 87
  human_in_the_loop: 1
  name: Figment Agentic Access
  operation_count: 129
  slug: figment-agentic-access
  summary_line: 129 operations · 87 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: Unified REST API for institutional staking across proof-of-stake networks. Endpoints build ready-to-sign transactions (stake, delegate, undelegate, withdraw, exit, compound, consolidate, transfer, cla
  name: Figment API
  slug: figment-api
- description: Hosted Model Context Protocol server served from Figment's own documentation host at docs.figment.io/mcp, exposing the Figment documentation and API reference to MCP clients. The endpoint is OAuth-pro
  name: Figment Documentation MCP Server
  slug: figment-documentation-mcp-server
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://www.figment.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.figment.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.figment.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.figment.io/reference/getting-started-1
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.figment.io/reference/getting-started-1
- group: operate
  title: ''
  type: Support
  url: https://www.figment.io/company/meet-with-us/
- group: company
  title: ''
  type: Blog
  url: https://www.figment.io/insights/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/figment-networks
- group: start
  title: ''
  type: SignUp
  url: https://app.figment.io/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.figment.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.figment.io/general-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.figment.io/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.figment.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.figment.io/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/figment-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.figment.io/
- group: auth
  title: ''
  type: TrustCenter
  url: security/figment-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.figment.io/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/figment-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/figment-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/figment-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/figment-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/figment-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/figment-www-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/figment-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/figment-packages.yml
- group: design
  title: ''
  type: Components
  url: components/figment-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/figment-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/figment-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/figment-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/figment-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/figment-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/figment-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/figment-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/figment-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/figment-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/figment-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/figment-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/figment-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/figment-api-overlay.yaml
created: '2026-08-04'
description: 'Figment is an institutional staking infrastructure provider that runs validators and staking services across 40+ proof-of-stake networks for asset managers, exchanges, custodians, wallets, banks and protocol foundations. Its developer surface is a single REST API at api.figment.io that abstracts network-specific staking mechanics behind one contract: build ready-to-sign staking, delegation, undelegation, withdrawal, exit, compound and consolidation transactions; broadcast them; and read back stakes, validators, activities, balances, rewards, reward rates, statements and portfolio data. Coverage includes Ethereum (including Pectra 0x02 compounding validators and Figment Validator Vaults), Solana, Cardano, Cosmos, Osmosis, Injective, NEAR, Polkadot, Polygon, Avalanche, Sui, Aptos, Vaulta, OpenTrade stablecoin yield vaults, and an x402 payment facilitator. Figment also publishes Elements, a React component library for embeddable staking widgets, and a documentation MCP server
  for agents.'
image: https://www.figment.io/wp-content/uploads/2024/06/Site-Preview.jpg
layout: provider
mcp_servers:
- description: ''
  name: figment-mcp.yml
  slug: figment-mcpyml
modified: '2026-08-04'
name: Figment
nav: Providers
network: true
overview: 'Figment publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include staking, blockchain, digital-assets, proof-of-stake, and validators.


  Figment''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 34 more developer resources.'
random_paper: 68
rate_limits:
- limit_count: 2
  name: Figment Rate Limits
  slug: figment-rate-limits
score:
  band: strong
  composite: 57.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 47.8
    developer_ergonomics: 75.5
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 68.4
  previous_composite: 57.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Figment Authentication
  slug: figment-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Figment Domain Security
  slug: figment-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Figment Vulnerability Disclosure
  slug: figment-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Figment Trust Center
  slug: figment-trust-center
  summary_line: SOC 2 Type II, ISO Certificate
slug: figment
tags:
- staking
- blockchain
- digital-assets
- proof-of-stake
- validators
- institutional-finance
- rewards-reporting
- ethereum
- solana
- web3-infrastructure
- custody
- x402
website: https://www.figment.io/
---
