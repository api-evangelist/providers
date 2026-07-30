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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The IYK API provides primitives for building digi-physical experiences. Core endpoints manage chips (NFC tags such as NTAG 424, KONG, and ARX HaLo), chip groups, items, taps/refs (validated physical i
  name: IYK API
  slug: iyk-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iyk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://iyk.app
- group: docs
  title: ''
  type: Documentation
  url: https://docs.iyk.app
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.iyk.app
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.iyk.app/api-quickstart
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/ezppV2nj7w
- group: start
  title: ''
  type: SignUp
  url: https://studio.iyk.app
- group: commercial
  title: ''
  type: TermsOfService
  url: https://assets.iyk.app/iyk-terms-of-service.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://assets.iyk.app/iyk-privacy-policy.pdf
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/iyk-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/iyk-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/iyk-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/iyk-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/iyk-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/iyk-well-known.yml
created: '2026-07-17'
description: IYK provides useful primitives and apps for building digi-physical (phygital) experiences, connecting physical products and merchandise to blockchain tokens, POAPs, and digital content through NFC chips. The IYK API exposes three categories of endpoints - Core (chips, chip groups, items, taps/refs, OTP codes, and phygitals), Modules (POAP Events and Guestbook Events), and Self-Service POAP Devices - letting brands and artists chip physical items, verify authentic taps, gate content and rewards, mint or transfer linked NFTs, and recognize fans who show up. IYK Music applies the same primitives to fan engagement, turning chipped merch and show check-ins into a living fan identity. IYK is backed by a16z.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iyk.png
layout: provider
mcp_servers:
- description: ''
  name: iyk-mcp.yml
  slug: iyk-mcpyml
modified: '2026-07-19'
name: IYK
nav: Providers
network: true
overview: 'IYK publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, NFC, Phygital, Blockchain, and NFT.


  IYK''s developer surface includes documentation, getting-started guide, support, signup flow, authentication, and 10 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 24.7
  delta: -1.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 45.7
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 26.5
  provenance:
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iyk/refs/heads/main/screenshots/iyk-2026-07-25T223022.png
security:
- kind: authentication
  name: Iyk Authentication
  slug: iyk-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Iyk Domain Security
  slug: iyk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iyk
tags:
- Company
- NFC
- Phygital
- Blockchain
- NFT
- POAP
- Chips
- Authentication
- Fan Engagement
- Web3
website: https://iyk.app
---
