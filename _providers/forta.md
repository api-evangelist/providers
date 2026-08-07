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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The Forta GraphQL API exposes the network's alerts and blockchain project threat-intelligence data. A single GraphQL endpoint accepts POST queries authenticated with a Bearer API key; the primary root
  name: Forta GraphQL API
  slug: forta-graphql-api
artifact_total: 4
asyncapis:
- description: ''
  name: Forta Webhooks
  slug: forta-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forta-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://forta.org
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.forta.network/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.forta.network/en/latest/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.forta.network/en/latest/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.forta.network/en/latest/forta-quickstart/
- group: company
  title: ''
  type: Blog
  url: https://www.forta.org/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/forta-network
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/KACdTEutQq
- group: start
  title: ''
  type: SignUp
  url: https://app.forta.network/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.forta.org/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.forta.org/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/forta-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/forta-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/forta-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/forta-cli.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/forta-agent.proto
- group: design
  title: ''
  type: Conventions
  url: conventions/forta-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/forta-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/forta-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/forta-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/forta-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/forta-llms.txt
created: '2026-07-17'
description: Forta is a decentralized, real-time detection network for monitoring the security and operational health of Web3 systems. Spun out of OpenZeppelin and backed by a16z crypto, Forta runs thousands of community-built detection bots across independent scan nodes that inspect every transaction and block on chains such as Ethereum, Polygon, BNB Chain, Avalanche, Arbitrum and Optimism, emitting alerts that DeFi protocols and security teams subscribe to via email, Slack, Telegram, Discord and webhooks. Developers query alerts and threat intelligence through a GraphQL API, build and deploy detection bots with the Forta Bot SDK and CLI (JavaScript/TypeScript and Python), and the Forta Firewall product uses the Forta Chain (a Layer 3 network) to block smart-contract exploits before they execute.
image: https://avatars.githubusercontent.com/u/87823599?v=4
layout: provider
modified: '2026-07-19'
name: Forta
nav: Providers
network: true
overview: 'Forta publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Security, Blockchain, Web3, and Monitoring.


  The Forta catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Forta''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 16 more developer resources.'
random_paper: 88
score:
  band: developing
  composite: 44.9
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 71.7
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 13.2
  previous_composite: 44.9
  provenance:
    conformance: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/forta/refs/heads/main/screenshots/forta-2026-07-25T214954.png
security:
- kind: authentication
  name: Forta Authentication
  slug: forta-authentication
  summary_line: http-bearer-apikey · 1 scheme
- kind: domain-security
  name: Forta Domain Security
  slug: forta-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: forta
tags:
- Company
- Security
- Blockchain
- Web3
- Monitoring
- Threat Detection
- DeFi
- GraphQL
- Alerts
- Smart Contracts
website: https://forta.org
---
