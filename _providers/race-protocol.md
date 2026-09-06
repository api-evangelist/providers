---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Developer guide and SDK/CLI surface for writing, publishing, and running WASM game bundles on the RACE Protocol multi-chain infrastructure.
  name: RACE Protocol
  slug: race-protocol
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/race-protocol-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RACE-Game
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/raceprotocol
created: '2025-02-06'
description: RACE Protocol is a multi-chain, on-chain infrastructure for developing and deploying secure and fair web3 games. It is delivered primarily through a TypeScript/JavaScript SDK (sdk-core, sdk-solana, sdk-sui, sdk-facade) and a command-line tool (race-cli) for game bundle publishing, account management, and payment claims, rather than as a traditional REST API. Smart contracts run on Solana and Sui.
finops:
- name: Race Protocol Finops
  service_category: API
  slug: race-protocol-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/race-protocol.png
layout: provider
modified: '2026-04-28'
name: RACE Protocol
nav: Providers
network: true
overview: RACE Protocol publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Web3, Blockchain, Gaming, SDK, and Solana.
plans:
- name: Race Protocol Plans Pricing
  plan_count: 3
  slug: race-protocol-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Race Protocol Rate Limits
  slug: race-protocol-rate-limits
score:
  band: emerging
  composite: 12.4
  coverage:
    artifact_dirs: 6
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 12.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/race-protocol/refs/heads/main/screenshots/race-protocol-2026-06-20T192517.png
security:
- kind: domain-security
  name: Race Protocol Domain Security
  slug: race-protocol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: race-protocol
tags:
- Web3
- Blockchain
- Gaming
- SDK
- Solana
- Sui
---
