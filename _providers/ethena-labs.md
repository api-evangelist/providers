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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Public request-for-quote (RFQ) minting and redemption API for USDe. Whitelisted participants check asset availability, request a firm 15-minute quote, fetch the fee schedule, sign the order with EIP-7
  name: Ethena Minting API
  slug: ethena-minting-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://ethena.fi
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ethena.fi
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ethena.fi/api-documentation/overview
- group: docs
  title: ''
  type: APIReference
  url: https://public.api.ethena.fi/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ethena.fi/technical-design/minting-usde
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ethena-labs
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ethena.fi/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.ethena.fi/resources/usde-mint-user-agreement
- group: auth
  title: ''
  type: TrustCenter
  url: https://docs.ethena.fi/resources/audits
- group: operate
  title: ''
  type: Support
  url: https://docs.ethena.fi
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ethena-labs-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/ethena-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ethena-labs-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ethena-labs-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ethena-labs-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ethena-labs-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/ethena-labs-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ethena-labs-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/ethena-labs-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ethena-labs-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ethena-labs-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ethena-labs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/ethena-labs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ethena-labs-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ethena-labs-mcp.yml
created: '2026-07-17'
description: 'Ethena Labs is the crypto-native protocol behind USDe, a synthetic dollar backed by spot crypto assets, onchain custody, and delta-neutral hedging positions on centralized liquidity venues, alongside the staked savings instrument sUSDe (the "Internet Bond"), the governance token ENA, and USDtb. Ethena exposes a public Minting API for whitelisted institutional participants to mint and redeem USDe: a request-for-quote (RFQ) flow returns firm 15-minute quotes that are signed with EIP-712 (or EIP-1271 for smart-contract wallets) and submitted onchain. This profile was surfaced as a portfolio company of Ribbit Capital and enriched with the real developer surface documented at docs.ethena.fi.'
image: https://ethena.fi/shared/ethena-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: ethena-labs-mcp.yml
  slug: ethena-labs-mcpyml
modified: '2026-07-19'
name: Ethena Labs
nav: Providers
network: true
overview: 'Ethena Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Stablecoin, DeFi, and Synthetic Dollar.


  Ethena Labs'' developer surface includes documentation, API reference, getting-started guide, support, authentication, changelog, and 19 more developer resources.'
random_paper: 48
score:
  band: thin
  composite: 32.8
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 55.3
  previous_composite: 32.8
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ethena-labs/refs/heads/main/screenshots/ethena-labs-2026-07-25T213648.png
security:
- kind: authentication
  name: Ethena Labs Authentication
  slug: ethena-labs-authentication
  summary_line: ip-allowlist/wallet-allowlist/signature · 4 schemes
- kind: domain-security
  name: Ethena Labs Domain Security
  slug: ethena-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ethena Labs Vulnerability Disclosure
  slug: ethena-labs-vulnerability-disclosure
  summary_line: contact published
slug: ethena-labs
tags:
- Company
- Crypto
- Stablecoin
- DeFi
- Synthetic Dollar
- Minting
- Blockchain
- Ethereum
website: https://ethena.fi
---
