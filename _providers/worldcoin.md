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
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-17'
api_count: 6
apis:
- description: Anonymous proof-of-human credential. Users prove uniqueness via Orb (highest assurance), government document with NFC, or selfie liveness check (beta). Applications request a zero-knowledge proof tied
  name: World ID
  slug: world-id
- description: Server-side verification endpoint that checks a World ID proof against the action and signal the client used. Apps call /api/v2/verify with the proof payload and receive a success / fail response plus
  name: World ID Verify API
  slug: verify-api
- description: Client-side widget for triggering a World ID verification from a web or React app. Handles QR-code / deep-link handoff to World App, proof collection, and callback to the host application.
  name: IDKit (Web / React Widget)
  slug: idkit
- description: Mini Apps run inside World App and use MiniKit to access wallet capabilities - payments in WLD / USDC, signing, World ID verification, contacts, and notifications - without leaving the host app. Inclu
  name: World Mini Apps (MiniKit)
  slug: mini-apps
- description: Toolkit and APIs for distinguishing human-backed agents from anonymous bots and scripts by binding agent actions to a World ID proof. Used to gate AI agents and automation in human-verified contexts.
  name: AgentKit
  slug: agent-kit
- description: OP Stack Ethereum L2 designed to prioritise verified humans with reduced fees and gas allowances for World ID-holders. EVM-compatible with public RPC endpoints, block explorer, bridges, and contract a
  name: World Chain
  slug: world-chain
artifact_total: 11
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/worldcoin/idkit-js/blob/main/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/worldcoin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/worldcoin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://world.org/
- group: other
  title: ''
  type: Developers
  url: https://world.org/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.world.org/
- group: agent
  title: ''
  type: LLMsIndex
  url: https://docs.world.org/llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.worldcoin.org/
- group: other
  title: ''
  type: Whitepaper
  url: https://whitepaper.world.org/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/worldcoin
- group: operate
  title: ''
  type: Support
  url: https://t.me/worlddevelopersupport
created: '2026-05-23'
description: World (formerly Worldcoin, built by Tools for Humanity) is a proof-of-personhood network combining biometric Orb verification, the World App wallet, and World Chain - an OP Stack L2 prioritised for verified humans. World's developer platform at docs.world.org exposes World ID (anonymous proof of human), Mini Apps (apps distributed inside World App via MiniKit), AgentKit (distinguishing human-backed agents from bots), and World Chain (EVM RPC, contracts, indexers). World ID integrations use IDKit (web/React widget) and the Verify API on the developer portal at developer.worldcoin.org.
finops:
- name: Worldcoin Finops
  service_category: API
  slug: worldcoin-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/worldcoin.png
layout: provider
modified: '2026-05-23'
name: World (Worldcoin)
nav: Providers
network: true
overview: 'World (Worldcoin) publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Proof of Personhood, Identity, World ID, Mini Apps, and Blockchain.


  World (Worldcoin)''s developer surface includes documentation, GitHub presence, support, and 8 more developer resources.'
plans:
- name: Worldcoin Plans Pricing
  plan_count: 1
  slug: worldcoin-plans-pricing
random_paper: 83
rate_limits:
- limit_count: 2
  name: Worldcoin Rate Limits
  slug: worldcoin-rate-limits
score:
  band: emerging
  composite: 20.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/worldcoin/refs/heads/main/screenshots/worldcoin-2026-06-20T201620.png
security:
- kind: domain-security
  name: Worldcoin Domain Security
  slug: worldcoin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Worldcoin Vulnerability Disclosure
  slug: worldcoin-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: worldcoin
tags:
- Proof of Personhood
- Identity
- World ID
- Mini Apps
- Blockchain
- World Chain
- Web3
- Biometrics
- SDKs
website: https://world.org/
---
