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
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
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
  href: https://raw.githubusercontent.com/api-evangelist/worldcoin/refs/heads/main/plans/worldcoin-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/worldcoin-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/worldcoin/refs/heads/main/rate-limits/worldcoin-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/worldcoin-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/worldcoin/refs/heads/main/finops/worldcoin-finops.yml
  title: ''
  type: FinOps
  url: finops/worldcoin-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://world.org/blog
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/worldcoin/idkit-js/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/worldcoin/idkit-js/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/worldcoin/idkit-js/blob/main/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/worldcoin/idkit-js/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/worldcoin/idkit-js/blob/main/LICENSE
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/worldcoin/refs/heads/main/security/worldcoin-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/worldcoin-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/worldcoin/refs/heads/main/security/worldcoin-domain-security.yml
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
- has_sources: false
  method: generated
  name: Worldcoin Finops
  primary_unit: ''
  service_category: API
  slug: worldcoin-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/worldcoin.png
layout: provider
modified: '2026-10-06'
name: World (Worldcoin)
nav: Providers
network: true
overview: 'World (Worldcoin) is listed with 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Proof of Personhood, Identity, World ID, Mini Apps, and Blockchain.


  World (Worldcoin)''s developer surface includes engineering blog, documentation, GitHub presence, support, and 15 more developer resources.'
plans:
- name: Worldcoin Plans Pricing
  plan_count: 1
  slug: worldcoin-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Worldcoin Rate Limits
  slug: worldcoin-rate-limits
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 66.1
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 85.0
  previous_composite: 28.9
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 11.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
- SDK
website: https://world.org/
---
