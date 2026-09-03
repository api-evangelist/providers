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
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 30.8
  scored_at: '2026-09-03'
api_count: 2
apis:
- baseURL: https://aggregator.walrus-mainnet.walrus.space
  baseurl_source: declared
  description: The routes API from Walrus Protocol — 9 operation(s) for routes.
  name: Walrus Protocol routes API
  slug: walrus-protocol-routes-api
artifact_total: 5
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Walrus Aggregator routes API
  slug: open-walrus-protocol-routes-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/walrus-protocol-aggregator-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/walrus-protocol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.walrus.xyz/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.wal.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wal.app/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.wal.app/docs/http-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.wal.app/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://blog.walrus.xyz/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MystenLabs
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/walrusprotocol
- group: commercial
  title: ''
  type: Pricing
  url: https://costcalculator.wal.app/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.wal.app/docs/legal/walrus_general_tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.wal.app/docs/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.walrus.xyz
- group: other
  title: ''
  type: Whitepaper
  url: https://docs.wal.app/walrus.pdf
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/MystenLabs/walrus/releases
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/walrus-protocol-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/walrus-protocol-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/walrus-protocol-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/walrus-protocol-api-catalog.json
- group: build
  title: ''
  type: Packages
  url: packages/walrus-protocol-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/walrus-protocol-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/walrus-protocol-cli.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/walrus-protocol-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/walrus-protocol-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/walrus-protocol-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/walrus-protocol-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/walrus-protocol-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/walrus-protocol-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/walrus-protocol-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/walrus-protocol-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/walrus-protocol-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Walrus is a decentralized blob storage protocol built on Sui by Mysten Labs, the team behind the Sui blockchain. It provides robust, cost-effective storage for large binary objects with high-availability guarantees using Red Stuff erasure coding across a permissionless set of storage nodes. Data is content-addressed, immutable, verifiable without trusting any single provider, and portable across apps, providers, and AI agents. Developers interact through the `walrus` client CLI, a TypeScript SDK, and an HTTP API served by publisher (write) and aggregator (read) daemons, with storage paid in WAL and on-chain coordination in SUI. Walrus also powers Walrus Sites (decentralized web hosting) and Walrus Memory (a portable memory layer for AI agents). Backed by Electric Capital.
image: https://walrus.xyz/images/open-graph/og-home.jpg
layout: provider
modified: '2026-07-21'
name: Walrus Protocol
nav: Providers
network: true
overview: 'Walrus Protocol publishes 1 API on the [APIs.io](https://apis.io/) network: routes API. Tagged areas include Company, Infrastructure, Storage, Decentralized Storage, and Blockchain.


  Walrus Protocol''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, changelog, and 26 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 52.5
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 46.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/walrus-protocol/refs/heads/main/screenshots/walrus-protocol-2026-08-17T082844.png
security:
- kind: authentication
  name: Walrus Protocol Authentication
  slug: walrus-protocol-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Walrus Protocol Domain Security
  slug: walrus-protocol-domain-security
  summary_line: TLSv1.3 · DMARC
slug: walrus-protocol
tags:
- Company
- Infrastructure
- Storage
- Decentralized Storage
- Blockchain
- Web3
- Data
- Artificial Intelligence
- Sui
website: https://www.walrus.xyz/
---
