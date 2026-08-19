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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 2
  name: Cipherowl Agentic Access
  operation_count: 16
  slug: cipherowl-agentic-access
  summary_line: 16 operations · 4 acting · 2 human-in-the-loop
api_count: 3
apis:
- description: Query blockchain balances and supported chain metadata across multiple networks.
  name: CipherOwl Onchain Service API
  slug: cipherowl-onchain-service-api
- description: Manage organization-scoped screening overrides (allowlists and denylists) for blockchain addresses.
  name: CipherOwl Private Data API API
  slug: cipherowl-private-data-api-api
- description: Screen blockchain addresses for risk, retrieve risk reasons, breakdowns, scores, and generate reports.
  name: CipherOwl SRR API API
  slug: cipherowl-srr-api-api
arazzos:
- description: Screen a blockchain address, and when it is risky, drill down through score, breakdown, and path-level evidence, then generate an analyst-ready risk assessment. Seeded with co-sandbox test values so a
  name: CipherOwl SRR Investigation Funnel
  slug: cipherowl-srr-investigation
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CipherOwl Onchain Service API
  slug: open-cipherowl-onchain-service-api
- collection_type: open
  name: CipherOwl Onchain Service Private Data API API
  slug: open-cipherowl-private-data-api-api
- collection_type: open
  name: CipherOwl Onchain Service SRR API API
  slug: open-cipherowl-srr-api-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/cipherowl-openapi-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://readme.cipherowl.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://readme.cipherowl.ai/reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://readme.cipherowl.ai/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://readme.cipherowl.ai/reference/build-a-client
- group: operate
  title: ''
  type: Support
  url: https://readme.cipherowl.ai/reference/support
- group: company
  title: ''
  type: Blog
  url: https://cipherowl.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cipherowl-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://cipherowl.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.cipherowl.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cipherowl.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cipherowl.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cipherowl.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://readme.cipherowl.ai/reference/release-notes
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cipherowl-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cipherowl-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cipherowl-security.txt
- group: build
  title: ''
  type: Packages
  url: packages/cipherowl-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/cipherowl-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cipherowl-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cipherowl-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/cipherowl-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cipherowl-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cipherowl.com/trust
- group: auth
  title: ''
  type: TrustCenter
  url: security/cipherowl-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cipherowl-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cipherowl-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cipherowl-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://cipherowl.com/trust
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cipherowl-agentic-access.yml
created: '2026-07-17'
description: 'CipherOwl provides AI-powered security and compliance for institutional stablecoins and digital assets. Its Screening, Risk & Reporting (SRR) API turns a blockchain address into a compliance decision: real-time sanctions and risk screening, deterministic 0-100 risk scoring, categorized risk breakdowns, path-level exposure evidence (including cross-chain), and analyst-ready risk assessment, SAR, and risk-flow-graph reports across Bitcoin, EVM, Tron, Solana, XRP and more. The platform also offers an Onchain balance service and a Private Data override service, an OwlTrace research experience, a Strix AI investigation agent, and a first-party CLI (cipherowl-sr3) that doubles as a Model Context Protocol server. Authentication is OAuth 2.0 client-credentials.'
image: https://cipherowl.com/og.png
layout: provider
mcp_servers:
- description: ''
  name: cipherowl-mcp.yml
  slug: cipherowl-mcpyml
modified: '2026-07-18'
name: CipherOwl
nav: Providers
network: true
overview: 'CipherOwl publishes 3 APIs on the [APIs.io](https://apis.io/) network: Onchain Service API, Private Data API API, and SRR API API. Tagged areas include Blockchain, Compliance, Crypto, Security, and Risk.


  CipherOwl''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
random_paper: 79
score:
  band: developing
  composite: 50.2
  delta: -8.1
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 30.3
    contract_quality: 52.4
    developer_ergonomics: 44.6
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 44.7
  previous_composite: 58.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/cipherowl/refs/heads/main/screenshots/cipherowl-2026-07-25T205400.png
security:
- kind: authentication
  name: Cipherowl Authentication
  slug: cipherowl-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cipherowl Domain Security
  slug: cipherowl-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Cipherowl Vulnerability Disclosure
  slug: cipherowl-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cipherowl Trust Center
  slug: cipherowl-trust-center
  summary_line: SOC 2 Type II
slug: cipherowl
tags:
- Blockchain
- Compliance
- Crypto
- Security
- Risk
- Sanctions Screening
- AML
- Digital Assets
- Stablecoins
- Web3
website: https://readme.cipherowl.ai/
---
