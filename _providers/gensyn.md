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
    agent_skills: true
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.1
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'REST + on-chain API for the Delphi information (prediction) market platform. REST endpoints cover market discovery, single-market lookup, wallet positions, and a public health check; on-chain methods '
  name: Delphi API
  slug: delphi-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://gensyn.ai
- group: docs
  title: ''
  type: Documentation
  url: https://gensyn.ai/infrastructure
- group: company
  title: ''
  type: Blog
  url: https://gensyn.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gensyn-ai
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/gensyn
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gensyn.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gensyn.ai/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/gensyn-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gensyn-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gensyn-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gensyn-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gensyn-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gensyn-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gensyn-domain-security.yml
created: '2026-07-17'
description: Gensyn is a decentralized infrastructure company building "the network for machine intelligence" — protocols that let AI systems train, verify, and transact in market-driven ecosystems. Its stack includes AXL (peer-to-peer networking for ML nodes, with built-in MCP/A2A support), CHAIN (on-chain identity, reputation, and stake), and REE (the Reproducible Execution Environment for cryptographically verifiable ML compute). Its flagship application, Delphi, is a live on-chain information (prediction) market where humans and AI agents trade predictions with on-chain settlement. Gensyn publishes a TypeScript Delphi SDK and an agent-skills package so autonomous agents can discover markets, quote, trade, and redeem positions programmatically. Backed by a16z.
image: https://github.com/gensyn-ai.png
layout: provider
modified: '2026-07-19'
name: Gensyn
nav: Providers
network: true
overview: 'Gensyn publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Decentralized Compute, and Blockchain.


  Gensyn''s developer surface includes documentation, engineering blog, support, authentication, and 11 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 22.1
  delta: 1.4
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 20.7
  provenance:
    skills: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gensyn/refs/heads/main/screenshots/gensyn-2026-07-25T215631.png
security:
- kind: authentication
  name: Gensyn Authentication
  slug: gensyn-authentication
  summary_line: apiKey/wallet-signing · 2 schemes
- kind: domain-security
  name: Gensyn Domain Security
  slug: gensyn-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gensyn
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- Decentralized Compute
- Blockchain
- Prediction Markets
- Agents
- Web3
website: https://gensyn.ai
---
