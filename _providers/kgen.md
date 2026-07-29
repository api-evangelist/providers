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
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 18.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Developer APIs for the KGeN Esports and Loyalty protocols — sessions, tournaments, leaderboards, wallets (KCash), rewards, and rewardable events for game developers.
  name: KGeN Economy Protocols
  slug: kgen-economy-protocols
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.kgen.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kgen.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kgen.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kgen.io/docs/Esport%20Protocol%20V1/Tech%20integration/api-usage
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kgen.io/docs/Esport%20Protocol%20V1/Introduction
- group: company
  title: ''
  type: Blog
  url: https://kgennewsletter.substack.com
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/kgen-904054419597955164
- group: auth
  title: ''
  type: Authentication
  url: authentication/kgen-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kgen-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kgen-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kgen-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kgen-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kgen-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kgen-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kgen-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kgen-well-known.yml
created: '2026-07-17'
description: KGeN (Kratos Gamer Network) is a verified-human data network powering Physical AI and Large Language Models across the Global South, and the operator of the KGeN Economy Protocols — a suite of developer APIs (Esports and Loyalty) that let game studios add leaderboard-based competitions and customizable reward systems paid in KCash, redeemable for real-world items at the Kratos Store. Server-to-server and per-user (JWT/OTP) endpoints cover sessions, tournaments, wallets, rewards, and rewardable events. Company revenue feeds $KGEN tokenomics, where every AI-data contract permanently retires token supply on-chain. Backed by Accel and Prosus Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kgen.png
layout: provider
mcp_servers:
- description: ''
  name: kgen-mcp.yml
  slug: kgen-mcpyml
modified: '2026-07-19'
name: KGeN
nav: Providers
network: true
overview: 'KGeN publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplaces, Gaming, Esports, and Loyalty.


  KGeN''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 9 more developer resources.'
random_paper: 26
score:
  band: emerging
  composite: 20.9
  delta: -1.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 22.7
  provenance:
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kgen/refs/heads/main/screenshots/kgen-2026-07-25T223702.png
security:
- kind: authentication
  name: Kgen Authentication
  slug: kgen-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Kgen Domain Security
  slug: kgen-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kgen
tags:
- Company
- Marketplaces
- Gaming
- Esports
- Loyalty
- Rewards
- Web3
- AI Data
- Developer API
website: https://www.kgen.io/
---
