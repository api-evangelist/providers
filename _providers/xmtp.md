---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-06'
api_count: 7
apis:
- description: Core gRPC-based API for the XMTP decentralized messaging network. Provides operations for sending and retrieving encrypted group messages, managing MLS key packages, publishing identity updates, and s
  name: XMTP Network gRPC API
  slug: xmtp-network-grpc-api
- description: Client SDK for browsers and Node.js enabling applications to send and receive end-to-end encrypted messages via the XMTP network. Supports wallet-based authentication (EVM-compatible wallets using ECD
  name: XMTP JavaScript/TypeScript SDK
  slug: xmtp-javascripttypescript-sdk
- description: Node.js SDK tailored for building AI agents and bots on the XMTP network. Enables agents to participate in XMTP conversations, respond to messages, and interact with users through encrypted decentrali
  name: XMTP Agent SDK
  slug: xmtp-agent-sdk
- description: 'Native Kotlin SDK for integrating XMTP encrypted messaging into Android applications. Supports wallet-based identity, group conversations, message streaming, and the full XMTP content type system for '
  name: XMTP Android SDK
  slug: xmtp-android-sdk
- description: 'Native Swift SDK for integrating XMTP encrypted messaging into iOS applications. Provides wallet-based authentication, group conversations, real-time message streaming, and comprehensive content type '
  name: XMTP iOS SDK
  slug: xmtp-ios-sdk
- description: Cross-platform SDK for building XMTP encrypted messaging into React Native and Expo applications. Bridges the libxmtp core library to JavaScript, enabling wallet-based messaging, group chats, streamin
  name: XMTP React Native SDK
  slug: xmtp-react-native-sdk
- description: JSON-RPC API for the XMTP Layer-3 appchain built on Arbitrum and settling to Base. Used for smart contract interactions including group management, identity updates, node registration, and fee payment
  name: XMTP App Chain RPC API
  slug: xmtp-app-chain-rpc-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xmtp-domain-security.yml
- group: build
  title: ''
  type: GitHub
  url: https://github.com/xmtp
- group: company
  title: ''
  type: Blog
  url: https://blog.xmtp.org
- group: operate
  title: ''
  type: Community
  url: https://community.xmtp.org
- group: operate
  title: ''
  type: Status
  url: https://status.xmtp.org
- group: other
  title: ''
  type: ImprovementProposals
  url: https://github.com/xmtp/XIPs
- group: operate
  title: ''
  type: DecentralizationRoadmap
  url: https://xmtp.org/decentralization
- group: other
  title: ''
  type: FeeCalculator
  url: https://docs.xmtp.org/fund-agents-apps/calculate-fees
- group: commercial
  title: ''
  type: TermsOfService
  url: https://xmtp.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://xmtp.org/privacy
- group: operate
  title: ''
  type: Contact
  url: https://community.xmtp.org
created: '2026-06-13'
description: XMTP (Extensible Message Transport Protocol) is a decentralized, open messaging protocol that enables end-to-end encrypted communication between Ethereum wallet addresses and other decentralized identifiers. Built on MLS (Messaging Layer Security), XMTP provides developer SDKs and a gRPC-based network API for sending encrypted messages in decentralized applications, AI agents, and Web3 wallets without relying on centralized servers.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://xmtp.org/img/xmtp-icon.png
layout: provider
modified: '2026-06-13'
name: XMTP
nav: Providers
network: true
overview: 'XMTP publishes 1 API on the [APIs.io](https://apis.io/) network: Network gRPC API. Tagged areas include Web3, Messaging, Encryption, Decentralized, and Ethereum.


  XMTP''s developer surface includes GitHub presence, engineering blog, status page, and 8 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 5
rate_limits:
- limit_count: 2
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 31.0
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 32.3
    developer_ergonomics: 6.5
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 31.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 19.4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xmtp/refs/heads/main/screenshots/xmtp-2026-06-20T201710.png
security:
- kind: domain-security
  name: Xmtp Domain Security
  slug: xmtp-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: xmtp
tags:
- Web3
- Messaging
- Encryption
- Decentralized
- Ethereum
- MLS
- Wallets
- Agents
website: https://xmtp.org
---
