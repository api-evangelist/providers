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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Blowfish Agentic Access
  operation_count: 5
  slug: blowfish-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 4
apis:
- description: Endpoints related to downloading blocklists
  name: Blowfish Download blocklist API
  slug: blowfish-download-blocklist-api
- description: Endpoints related to scanning dApp domains
  name: Blowfish Scan domain API
  slug: blowfish-scan-domain-api
- description: Endpoints related to scanning blockchain messages
  name: Blowfish Scan message API
  slug: blowfish-scan-message-api
- description: Endpoints related to scanning blockchain transactions
  name: Blowfish Scan transaction API
  slug: blowfish-scan-transaction-api
artifact_total: 8
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.blowfish.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blowfish.xyz
- group: docs
  title: ''
  type: APIReference
  url: https://docs.blowfish.xyz/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blowfish.xyz/docs/introduction
- group: start
  title: ''
  type: SignUp
  url: https://portal.blowfish.xyz/
- group: company
  title: ''
  type: Blog
  url: https://blog.blowfish.xyz
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blowfishxyz
- group: commercial
  title: ''
  type: Pricing
  url: https://blowfish.xyz
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://extension.blowfish.xyz/privacy
- group: operate
  title: ''
  type: Support
  url: https://form.typeform.com/to/BHue5Hg0
- group: auth
  title: ''
  type: Authentication
  url: authentication/blowfish-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/blowfish-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/blowfish-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/blowfish-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/blowfish-conformance.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/blowfish-scan-vocabulary.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/blowfish-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/blowfish-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/blowfish-packages.yml
- group: design
  title: ''
  type: Components
  url: components/blowfish-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/blowfish-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blowfish-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/blowfish-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blowfish-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blowfish.xyz
created: '2026-07-17'
description: Blowfish is a proactive web3 security platform that scans EVM and Solana transactions, EVM messages, and dApp domains before a user signs, returning a recommended action (NONE, WARN, or BLOCK), severity-sorted warnings, and human-readable transaction simulation results. Its Scan API and downloadable domain blocklist help wallets and dApps protect users from scams, malicious token approvals, and phishing across 10+ blockchains. Backed by Paradigm.
image: https://raw.githubusercontent.com/blowfishxyz/blowfish-openapi-specs/HEAD/blowfish.png
layout: provider
mcp_servers:
- description: ''
  name: blowfish-mcp.yml
  slug: blowfish-mcpyml
modified: '2026-07-18'
name: Blowfish
nav: Providers
network: true
overview: 'Blowfish publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Download blocklist API, Scan domain API, Scan message API, and 1 more. Tagged areas include Company, Security, Web3, Blockchain, and Wallet.


  Blowfish''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, pricing, support, and 19 more developer resources.'
random_paper: 72
score:
  band: developing
  composite: 43.9
  delta: -4.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 60.2
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 21.9
    operational_transparency: 5.3
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blowfish/refs/heads/main/screenshots/blowfish-2026-07-25T203426.png
security:
- kind: authentication
  name: Blowfish Authentication
  slug: blowfish-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Blowfish Domain Security
  slug: blowfish-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: blowfish
tags:
- Company
- Security
- Web3
- Blockchain
- Wallet
- Transaction Scanning
- Fraud Prevention
- Cryptocurrency
website: https://blowfish.xyz
---
