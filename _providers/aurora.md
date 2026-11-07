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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Ethereum-compatible JSON-RPC 2.0 API for the Aurora EVM network of virtual chains on NEAR. Exposes the standard eth_* method set over HTTPS (and WebSocket subscriptions) on public mainnet and testnet '
  name: Aurora JSON-RPC API
  slug: aurora-json-rpc-api
artifact_total: 4
common:
- group: operate
  href: https://artifacts.apis.io/aurora/lifecycle/aurora-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/aurora-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/aurora/hosts/aurora-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aurora-hosts.yml
- group: build
  href: https://artifacts.apis.io/aurora/integrations/aurora-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/aurora-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/aurora/vendors/aurora-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aurora-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://aurora.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://doc.aurora.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.aurora.dev/getting-started/what-is-aurora
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.aurora.dev/
- group: company
  title: ''
  type: Blog
  url: https://aurora.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aurora-is-near
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/auroralabs
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aurora.dev/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aurora.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aurora.dev/privacy
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.aurora.dev/
- group: other
  title: ''
  type: Explorer
  url: https://explorer.aurora.dev/
- group: build
  href: https://artifacts.apis.io/aurora/packages/aurora-packages.yml
  title: ''
  type: Packages
  url: packages/aurora-packages.yml
- group: build
  href: https://artifacts.apis.io/aurora/packages/aurora-packages.yml
  title: ''
  type: SDKs
  url: packages/aurora-packages.yml
- group: build
  href: https://artifacts.apis.io/aurora/cli/aurora-cli.yml
  title: ''
  type: CLI
  url: cli/aurora-cli.yml
- group: design
  href: https://artifacts.apis.io/aurora/components/aurora-components.yml
  title: ''
  type: Components
  url: components/aurora-components.yml
- group: auth
  href: https://artifacts.apis.io/aurora/authentication/aurora-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aurora-authentication.yml
- group: design
  href: https://artifacts.apis.io/aurora/conventions/aurora-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aurora-conventions.yml
- group: design
  href: https://artifacts.apis.io/aurora/conformance/aurora-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aurora-conformance.yml
- group: start
  href: https://artifacts.apis.io/aurora/sandbox/aurora-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/aurora-sandbox.yml
- group: design
  href: https://artifacts.apis.io/aurora/lifecycle/aurora-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aurora-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/aurora/changelog/aurora-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aurora-changelog.yml
- group: agent
  href: https://artifacts.apis.io/aurora/llms/aurora-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aurora-llms.txt
- group: auth
  href: https://artifacts.apis.io/aurora/security/aurora-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aurora-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/aurora/security/aurora-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aurora-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aurora/security/aurora-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/aurora-vulnerability-disclosure.yml
coverage:
  detail: Aurora documents an Ethereum-compatible JSON-RPC surface at doc.aurora.dev (mainnet.aurora.dev answers eth_chainId with 200) but publishes no OpenRPC or OpenAPI contract, and doc.aurora.dev/llms.txt returns 404.
  evidence:
  - status: 200
    url: https://aurora.dev/
  - status: 404
    url: https://doc.aurora.dev/llms.txt
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-07-17'
description: Aurora is an EVM-compatible blockchain platform that lets developers launch fully customizable Virtual Chains running as smart contracts on the NEAR Protocol, pairing full Ethereum tooling compatibility with NEAR's low fees, sub-second block times, and fast finality. Developers integrate with Aurora primarily through its Ethereum-compatible JSON-RPC API (public mainnet and testnet endpoints), the Rainbow Bridge for moving assets between Ethereum, NEAR, and Aurora, block explorers, price oracles, data indexers, and the Aurora Cloud platform for spinning up dedicated virtual chains. Aurora ships open-source Rust engine crates and SDK, a Rust command-line interface, and TypeScript widgets for building intents-based cross-chain swaps.
image: https://aurora.dev/favicon.ico
layout: provider
modified: '2026-07-18'
name: Aurora
nav: Providers
network: true
overview: 'Aurora is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, EVM, Web3, and JSON-RPC.


  Aurora''s developer surface includes documentation, getting-started guide, engineering blog, support, CLI, authentication, sandbox, and 23 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 29.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 73.2
    operational_transparency: 44.7
  previous_composite: 32.6
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/aurora/aurora-2026-07-25T201745.png
security:
- kind: authentication
  name: Aurora Authentication
  slug: aurora-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Aurora Domain Security
  slug: aurora-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aurora Vulnerability Disclosure
  slug: aurora-vulnerability-disclosure
  summary_line: disclosure policy published
slug: aurora
tags:
- Company
- Blockchain
- EVM
- Web3
- JSON-RPC
- NEAR
- Ethereum
- Layer 2
- Smart Contracts
- DeFi
website: https://aurora.dev/
---
