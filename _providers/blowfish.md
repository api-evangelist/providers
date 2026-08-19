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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.0
  scored_at: '2026-08-19'
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
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API reference Download blocklist API
  slug: open-blowfish-download-blocklist-api
- collection_type: open
  name: API reference Download blocklist Scan domain API
  slug: open-blowfish-scan-domain-api
- collection_type: open
  name: API reference Download blocklist Scan message API
  slug: open-blowfish-scan-message-api
- collection_type: open
  name: API reference Download blocklist Scan transaction API
  slug: open-blowfish-scan-transaction-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/blowfish-v20230308-overlay.yaml
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


  Blowfish''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, pricing, support, and 20 more developer resources.'
random_paper: 117
score:
  band: thin
  composite: 38.4
  delta: -5.2
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 20.5
    contract_quality: 60.8
    developer_ergonomics: 41.1
    discoverability: 81.5
    governance: 20.5
    operational_transparency: 2.6
  previous_composite: 43.6
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
    score: 29.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
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
