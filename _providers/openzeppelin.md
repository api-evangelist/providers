---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Openzeppelin Agentic Access
  operation_count: 43
  slug: openzeppelin-agentic-access
  summary_line: 43 operations · 22 acting
api_count: 9
apis:
- description: OpenZeppelin Monitor is an open-source blockchain monitoring service that watches for specific on-chain activities and triggers notifications based on configurable conditions. It supports real-time mo
  name: OpenZeppelin Monitor API
  slug: openzeppelin-monitor-api
- description: The OpenZeppelin Contracts library provides a comprehensive collection of modular, reusable, and secure Solidity smart contracts for building decentralized applications. The API reference covers ERC t
  name: OpenZeppelin Contracts API Reference
  slug: openzeppelin-contracts-api-reference
- description: Health is responsible for showing the health of the relayers.
  name: OpenZeppelin Health API
  slug: openzeppelin-health-api
- description: Metrics are responsible for showing the metrics related to the relayers.
  name: OpenZeppelin Metrics API
  slug: openzeppelin-metrics-api
- description: Networks represent blockchain network configurations including RPC endpoints and network-specific settings.
  name: OpenZeppelin Networks API
  slug: openzeppelin-networks-api
- description: Notifications are responsible for showing the notifications related to the relayers.
  name: OpenZeppelin Notifications API
  slug: openzeppelin-notifications-api
- description: Plugins are TypeScript functions that can be used to extend the OpenZeppelin Relayer API functionality.
  name: OpenZeppelin Plugins API
  slug: openzeppelin-plugins-api
- description: Relayers are the core components of the OpenZeppelin Relayer API. They are responsible for executing transactions on behalf of users and providing a secure and reliable way to interact with the blockc
  name: OpenZeppelin Relayers API
  slug: openzeppelin-relayers-api
- description: Signers are responsible for signing the transactions related to the relayers.
  name: OpenZeppelin Signers API
  slug: openzeppelin-signers-api
artifact_total: 24
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/OpenZeppelin/openzeppelin-monitor/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openzeppelin-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/openzeppelin-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openzeppelin-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openzeppelin-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.openzeppelin.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openzeppelin.com/
- group: operate
  title: ''
  type: Forums
  url: https://forum.openzeppelin.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/OpenZeppelin
- group: company
  title: ''
  type: Blog
  url: https://www.openzeppelin.com/blog
- group: company
  title: ''
  type: News
  url: https://www.openzeppelin.com/news
- group: operate
  title: ''
  type: OpenSourceStack
  url: https://www.openzeppelin.com/open-source-stack
- group: auth
  title: ''
  type: Security
  url: https://www.openzeppelin.com/security-audits
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/OpenZeppelin
- group: operate
  title: ''
  type: Discord
  url: https://discord.openzeppelin.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openzeppelin/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.openzeppelin.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.openzeppelin.com/privacy
- group: operate
  title: ''
  type: Status
  url: https://status.openzeppelin.com/
- group: start
  title: ''
  type: Signup
  url: https://defender.openzeppelin.com/
created: '2026-06-13'
description: OpenZeppelin is a Web3 security platform providing tools for secure smart contract development, deployment, monitoring, and automation. The platform includes OpenZeppelin Contracts (battle-tested Solidity libraries), Defender (a developer security platform for auditing, deploying, and operating blockchain applications), the open-source OpenZeppelin Relayer for transaction relay infrastructure across EVM, Solana, and Stellar networks, and OpenZeppelin Monitor for real-time on-chain activity detection and alerting. Defender is sunsetting on July 1, 2026, with users migrating to the open-source Relayer and Monitor projects.
examples:
- key_count: 4
  name: Create Relayer
  slug: create-relayer
- key_count: 4
  name: Health Check
  slug: health-check
- key_count: 4
  name: Send Transaction
  slug: send-transaction
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://www.openzeppelin.com/hubfs/openzeppelin-logo.png
json_schemas:
- name: NotificationResponse
  property_count: 6
  slug: notification
- name: RelayerResponse
  property_count: 12
  slug: relayer
- name: TransactionResponse
  property_count: 18
  slug: transaction
jsonld:
- class_count: 47
  name: Openzeppelin Context
  property_count: 2
  slug: openzeppelin
layout: provider
modified: '2026-06-13'
name: OpenZeppelin
nav: Providers
network: true
overview: 'OpenZeppelin publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Health API, Metrics API, Networks API, and 4 more. Tagged areas include Web3, Smart Contracts, Blockchain, Security, and Ethereum.


  The OpenZeppelin catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OpenZeppelin''s developer surface includes authentication, documentation, GitHub presence, engineering blog, product news, status page, signup flow, and 13 more developer resources.'
plans:
- name: Plans
  plan_count: 4
  slug: plans
random_paper: 29
rate_limits:
- limit_count: 5
  name: Rate Limits
  slug: rate-limits
rules:
- name: OpenZeppelin API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: openzeppelin-jsonschema-spectral-rules
score:
  band: developing
  composite: 55.8
  delta: 3.0
  facets:
    commercial_clarity: 81.6
    contract_quality: 58.3
    developer_ergonomics: 26.1
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 47.4
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openzeppelin/refs/heads/main/screenshots/openzeppelin-2026-06-20T191058.png
security:
- kind: authentication
  name: Openzeppelin Authentication
  slug: openzeppelin-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Openzeppelin Domain Security
  slug: openzeppelin-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Openzeppelin Trust Center
  slug: openzeppelin-trust-center
  summary_line: SOC 2, ISO 27001
slug: openzeppelin
tags:
- Web3
- Smart Contracts
- Blockchain
- Security
- Ethereum
- DeFi
- Solidity
- Relayer
- Monitoring
- Auditing
website: https://www.openzeppelin.com/
---
