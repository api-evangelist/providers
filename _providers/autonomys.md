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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.5
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: The Auto Drive API API from Autonomys — 25 operation(s) for auto drive api.
  name: Autonomys Auto Drive API API
  slug: autonomys-auto-drive-api-api
- description: The Auto Drive Download Gateway API from Autonomys — 6 operation(s) for auto drive download gateway.
  name: Autonomys Auto Drive Download Gateway API
  slug: autonomys-auto-drive-download-gateway-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Auto Drive APIs Auto Drive API API
  slug: open-autonomys-auto-drive-api-api
- collection_type: open
  name: Auto Drive APIs Auto Drive API Auto Drive Download Gateway API
  slug: open-autonomys-auto-drive-download-gateway-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/autonomys-mcp.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/autonomys-auto-drive-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/autonomys-auto-drive-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/autonomys-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/autonomys-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/autonomys-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/autonomys-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/autonomys-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/autonomys-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://telemetry.subspace.foundation
- group: build
  title: ''
  type: Packages
  url: packages/autonomys-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/autonomys-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/autonomys-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/autonomys-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://develop.autonomys.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://develop.autonomys.xyz/
- group: docs
  title: ''
  type: APIReference
  url: https://develop.autonomys.xyz/sdk/auto-drive/api_reference
- group: start
  title: ''
  type: GettingStarted
  url: https://develop.autonomys.xyz/sdk/auto-drive/overview_setup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/autonomys
- group: operate
  title: ''
  type: Support
  url: https://autonomys.xyz/discord
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@autonomysnetwork
- group: start
  title: ''
  type: SignUp
  url: https://ai3.storage
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.autonomys.xyz/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.autonomys.xyz/terms-of-use
- group: company
  title: ''
  type: Website
  url: https://www.autonomys.xyz/
created: '2026-07-17'
description: Autonomys is a decentralized infrastructure network providing permanent, verifiable, content-addressed data storage and AI-ready blockchain services, secured by a Proof-of-Archival-Storage consensus. Its developer surface centers on Auto Drive — permanent storage exposed through a REST API where objects are addressed by IPFS-style CIDs — and the Auto SDK, a TypeScript toolkit (@autonomys/* npm packages) for consensus, storage, cross-domain messaging, and DAG data. The broader stack adds Auto EVM (an Ethereum- compatible execution domain), Auto Agents (a framework for autonomous on-chain AI agents), and Auto ID (self-sovereign identity). Storage is paid in native AI3 via an on-chain Intents flow. Autonomys was surfaced as a portfolio company of Pantera Capital and has now been enriched from its public developer surface.
image: https://www.autonomys.xyz/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: autonomys-mcp.yml
  slug: autonomys-mcpyml
modified: '2026-07-18'
name: Autonomys
nav: Providers
network: true
overview: 'Autonomys publishes 2 APIs on the [APIs.io](https://apis.io/) network: Auto Drive API API and Auto Drive Download Gateway API. Tagged areas include Company, Crypto, Blockchain, Web3, and Decentralized Storage.


  Autonomys'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 19 more developer resources.'
random_paper: 113
score:
  band: developing
  composite: 42.4
  delta: 0.5
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 16.7
    contract_quality: 41.6
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 18.4
  previous_composite: 41.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/autonomys/refs/heads/main/screenshots/autonomys-2026-07-25T201843.png
security:
- kind: authentication
  name: Autonomys Authentication
  slug: autonomys-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Autonomys Domain Security
  slug: autonomys-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: autonomys
tags:
- Company
- Crypto
- Blockchain
- Web3
- Decentralized Storage
- Storage
- AI Agents
- IPFS
- TypeScript SDK
website: https://www.autonomys.xyz/
---
