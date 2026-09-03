---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.5
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: gRPC / Protocol Buffers API for integrating a game with LinQ Wallet services. Covers geo restriction checks by IP and coordinates, anonymous and wallet-linked user authentication, account balances, de
  name: LinQ Wallet Public API
  slug: linq-wallet-public-api
artifact_total: 3
common:
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/linqgg-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linqgg-domain-security.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/linqgg-services.yml
- group: build
  title: ''
  type: Packages
  url: packages/linqgg-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/linqgg-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/linqgg-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/linqgg-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/linqgg-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/linqgg-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/linqgg-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/linqgg-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/linqgg-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/linqgg-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/linqgg-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/linqgg-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/linqgg-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/linqgg-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/linqgg-llms.txt
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/linqgg/unity-sdk/blob/main/VISION.md
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.linq.gg/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.linq.gg/
- group: docs
  title: ''
  type: APIReference
  url: https://buf.build/linq/linq
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.linq.gg/getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.linq.gg/contact
- group: company
  title: ''
  type: Blog
  url: https://linq.gg/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/linqgg
- group: commercial
  title: ''
  type: TermsOfService
  url: https://linq.gg/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://linq.gg/privacy-policy
created: '2026-07-17'
description: LinQ is the wallet, payments and loyalty platform operated by Galactica Games, Inc. (dba Toffee) for game developers building loyalty programs, real-money gaming (RMG) and branded debit-card experiences. Games integrate a LinQ Wallet account for each player, then deposit, withdraw, transfer and reconcile funds against internal game currencies. The LinQ Wallet Public API is a gRPC / Protocol Buffers surface published on the Buf Schema Registry as buf.build/linq/linq, organised into Geo (IP and coordinate restriction checks), Auth (anonymous game sign-in and wallet-linked user sign-in), Money (accounts, balances, replenishment orders, transfers, Brazil Pix, operations history) and Sandbox (integration-test helpers) modules. Client libraries are generated from the registry for TypeScript, JavaScript and other targets, and a first-party Unity SDK handles PCI-compliant native card and Apple Pay checkout on device.
image: https://framerusercontent.com/images/IDaPLV2CTzzUnLl1BCRzzHVprF4.png
layout: provider
modified: '2026-07-19'
name: Linq.gg
nav: Providers
network: true
overview: 'Linq.gg publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Payments, Wallets, and Loyalty.


  Linq.gg''s developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, support, and 22 more developer resources.'
random_paper: 12
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 26.7
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 45.0
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linqgg/refs/heads/main/screenshots/linqgg-2026-07-25T225259.png
security:
- kind: authentication
  name: Linqgg Authentication
  slug: linqgg-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Linqgg Domain Security
  slug: linqgg-domain-security
  summary_line: TLSv1.3 · DMARC
slug: linqgg
tags:
- Company
- Gaming
- Payments
- Wallets
- Loyalty
- Fintech
- Real-Money Gaming
- gRPC
- Geolocation
- Authentication
website: https://docs.linq.gg/
---
