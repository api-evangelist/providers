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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.6
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Server-side custom event ingestion for attribution.
  name: Spindl Events API
  slug: spindl-events-api
- description: Redirect links mapping a Spindl link to a destination URL.
  name: Spindl Short Links API
  slug: spindl-short-links-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spindl-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spindl-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/spindl-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/spindl-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/spindl-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/spindl-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/spindl-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/spindl-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/spindl-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/spindl-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/spindl-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://spindl.xyz
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.spindl.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spindl.xyz
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.spindl.xyz/spindl/techncial/start-here.md
- group: company
  title: ''
  type: Blog
  url: https://blog.spindl.xyz
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spindl-xyz
- group: start
  title: ''
  type: SignUp
  url: https://app.spindl.xyz
- group: operate
  title: ''
  type: Support
  url: https://docs.spindl.xyz/spindl/contact-spindl.md
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spindl.xyz/privacy-policy
created: '2026-07-17'
description: Spindl is a Web3 growth platform providing onchain attribution, web3-native analytics, audiences, short links, referrals, and ads in one place, helping developers understand where their users come from and how they behave across onchain apps. It offers a JavaScript/HTML SDK, Android and iOS SDKs, and a Server-to-Server REST API for campaign and attribution management, short (redirect) links, server-side custom event ingestion, and daily data exports. Positioned as Web3's answer to Mixpanel and Amplitude, Spindl is used by teams including Uniswap, Base, Safe, and Morpho. Originally added to the API Evangelist network as a portfolio-lead stub, now enriched from its published developer documentation.
image: https://spindl.xyz/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: spindl-mcp.yml
  slug: spindl-mcpyml
modified: '2026-07-21'
name: Spindl
nav: Providers
network: true
overview: 'Spindl publishes 2 APIs on the [APIs.io](https://apis.io/) network: Events API and Short Links API. Tagged areas include Company, Crypto Web3, Attribution, Analytics, and Marketing.


  Spindl''s developer surface includes authentication, documentation, getting-started guide, engineering blog, signup flow, support, and 15 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 41.7
  delta: -2.4
  facets:
    commercial_clarity: 23.7
    contract_quality: 64.4
    developer_ergonomics: 56.0
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 44.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Spindl Authentication
  slug: spindl-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Spindl Domain Security
  slug: spindl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spindl
tags:
- Company
- Crypto Web3
- Attribution
- Analytics
- Marketing
- Growth
- SDK
- Web3
website: https://spindl.xyz
---
