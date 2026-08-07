---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 25.9
  scored_at: '2026-08-06'
api_count: 2
apis:
- description: Unified ERC-4337 JSON-RPC endpoint exposing both the Pimlico bundler (eth_sendUserOperation, eth_estimateUserOperationGas, eth_getUserOperationReceipt, pimlico_getUserOperationGasPrice, pimlico_getUse
  name: Pimlico Bundler & Paymaster API
  slug: pimlico-bundler-paymaster-api
- description: 'REST management API for the Pimlico platform used to create, list, retrieve, and update sponsorship policies that govern which user operations are eligible for gas sponsorship. Uses cursor pagination '
  name: Pimlico Platform API
  slug: pimlico-platform-api
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.pimlico.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.pimlico.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pimlico.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pimlico.io/references/bundler
- group: start
  title: ''
  type: Quickstart
  url: https://docs.pimlico.io/references/permissionless
- group: operate
  title: ''
  type: Support
  url: https://t.me/pimlicoHQ
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pimlicolabs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pimlico.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.pimlico.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pimlico.io/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pimlico.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pimlico.io
- group: other
  title: ''
  type: X
  url: https://x.com/pimlicoHQ
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pimlico-llms.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/pimlico-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pimlico-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/pimlico-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pimlico-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pimlico-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pimlico-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pimlico-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pimlico-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.pimlico.io/.well-known/security.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/pimlico-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/pimlico-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pimlico-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/pimlico-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pimlico-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pimlico-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pimlico-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pimlico-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pimlico-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pimlico-plans.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pimlico-finops.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pimlico-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Pimlico is the world's most popular ERC-4337 account abstraction infrastructure platform, providing production bundler and paymaster APIs plus a platform management API for building, deploying, and operating smart accounts on Ethereum and 100+ EVM-compatible chains. Its verifying paymaster sponsors gas for gasless transactions, its ERC-20 paymaster lets users pay gas in stablecoins and other tokens, and its bundler submits, estimates, and tracks ERC-4337 user operations. Developers integrate through the permissionless.js TypeScript SDK (built on viem) against a single JSON-RPC endpoint keyed by chain, and manage sponsorship policies, API keys, and billing through the Pimlico dashboard.
finops:
- name: Pimlico Finops
  service_category: ''
  slug: pimlico-finops
image: https://avatars.githubusercontent.com/u/125581500?v=4
layout: provider
mcp_servers:
- description: ''
  name: pimlico-mcp.yml
  slug: pimlico-mcpyml
modified: '2026-07-20'
name: Pimlico
nav: Providers
network: true
overview: 'Pimlico publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Account Abstraction, ERC-4337, Blockchain, and Ethereum.


  Pimlico''s developer surface includes documentation, API reference, quickstart, support, pricing, signup flow, authentication, and 29 more developer resources.'
plans:
- name: Pimlico Plans
  plan_count: 2
  slug: pimlico-plans
random_paper: 71
rate_limits:
- limit_count: 2
  name: Pimlico Rate Limits
  slug: pimlico-rate-limits
score:
  band: developing
  composite: 49.3
  delta: 0.0
  facets:
    commercial_clarity: 89.5
    contract_quality: 0.0
    developer_ergonomics: 66.8
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 60.5
  previous_composite: 49.3
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Pimlico Authentication
  slug: pimlico-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pimlico Domain Security
  slug: pimlico-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Pimlico Vulnerability Disclosure
  slug: pimlico-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Pimlico Trust Center
  slug: pimlico-trust-center
  summary_line: SOC 2
slug: pimlico
tags:
- Company
- Account Abstraction
- ERC-4337
- Blockchain
- Ethereum
- Web3
- Paymaster
- Bundler
- Smart Accounts
- Gas Sponsorship
- Wallets
- Infrastructure
website: https://www.pimlico.io
---
