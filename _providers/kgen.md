---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 5.4
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: Developer APIs for the KGeN Esports and Loyalty protocols — sessions, tournaments, leaderboards, wallets (KCash), rewards, and rewardable events for game developers.
  name: KGeN Economy Protocols
  slug: kgen-economy-protocols
artifact_total: 3
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
  type: X-MCPServerCandidate
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
modified: '2026-07-19'
name: KGeN
nav: Providers
network: true
overview: 'KGeN publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplaces, Gaming, Esports, and Loyalty.


  KGeN''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 9 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.5
  provenance:
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Ai Data
- Developer API
website: https://www.kgen.io/
---
