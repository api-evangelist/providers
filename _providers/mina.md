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
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: GraphQL API exposed by a running Mina daemon (node) for querying node, account, and chain state and submitting payments, delegations, and zkApp transactions. Bound to localhost:3085 by default. 41 que
  name: Mina Daemon GraphQL API
  slug: mina-daemon-graphql-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://minaprotocol.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.minaprotocol.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.minaprotocol.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://minaprotocol.com/get-started
- group: company
  title: ''
  type: Blog
  url: https://minaprotocol.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MinaProtocol
- group: operate
  title: ''
  type: Support
  url: https://bit.ly/MinaDiscord
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://minaprotocol.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://minaprotocol.com/tos
- group: build
  title: ''
  type: Packages
  url: packages/mina-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mina-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mina-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mina-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/mina-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/mina-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/mina-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mina-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mina-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mina-conventions.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mina-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mina-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mina-problem-types.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mina-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mina-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://docs.minaprotocol.com/mina-security
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Mina Protocol is a lightweight, layer-1 blockchain powered by zero-knowledge proofs (zk-SNARKs) that keeps the entire chain a constant ~22KB in size so any device can sync and verify the network. Developers build privacy-preserving smart contracts called zkApps using o1js, a TypeScript zk framework, and the mina-signer library for offline transaction signing. Each Mina daemon (node) exposes a GraphQL API on localhost:3085 for querying node/account/chain state and submitting payments, delegations, and zkApp commands; a Rosetta interface and Archive Node support exchange integration and historical data. Mina uses the Ouroboros Samasika proof-of-stake consensus and is stewarded by the Mina Foundation and o1Labs. Surfaced as a portfolio company of pantera-capital.
image: https://docs.minaprotocol.com/img/favicon.ico
layout: provider
modified: '2026-07-20'
name: Mina
nav: Providers
network: true
overview: 'Mina publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Blockchain, Zero Knowledge, and zkApps.


  Mina''s developer surface includes documentation, getting-started guide, engineering blog, support, CLI, sandbox, changelog, and 19 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 18
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 80.4
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 28.9
  previous_composite: 31.3
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mina/refs/heads/main/screenshots/mina-2026-08-07T172921.png
security:
- kind: authentication
  name: Mina Authentication
  slug: mina-authentication
  summary_line: none/passphrase-unlock · 3 schemes
- kind: domain-security
  name: Mina Domain Security
  slug: mina-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Mina Vulnerability Disclosure
  slug: mina-vulnerability-disclosure
  summary_line: disclosure policy published
slug: mina
tags:
- Company
- Crypto
- Blockchain
- Zero Knowledge
- zkApps
- GraphQL
- Web3
- Cryptocurrency
website: https://minaprotocol.com/
---
