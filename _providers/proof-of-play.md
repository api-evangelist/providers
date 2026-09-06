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
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Proof Of Play Agentic Access
  operation_count: 1
  slug: proof-of-play-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://staging.vrf.proofofplay.com
  baseurl_source: declared
  description: The Public API API from Proof of Play — 1 operation(s) for public api.
  name: Proof of Play Public API API
  slug: proof-of-play-public-api-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Proof of Play Public API API
  slug: open-proof-of-play-public-api-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/proof-of-play-vrf-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.proofofplay.com/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.proofofplay.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.proofofplay.com/api-reference/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.proofofplay.com/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/proofofplay
- group: operate
  title: ''
  type: Support
  url: https://z7a9jnrajv8.typeform.com/to/Ywh9xVFF
- group: company
  title: ''
  type: Blog
  url: https://www.proofofplay.com/resources
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arcade.piratenation.game/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arcade.piratenation.game/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/proof-of-play
- group: company
  title: ''
  type: Twitter
  url: https://x.com/ProofOfPlay
- group: auth
  title: ''
  type: Authentication
  url: authentication/proof-of-play-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/proof-of-play-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/proof-of-play-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/proof-of-play-conformance.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/proof-of-play-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/proof-of-play-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/proof-of-play-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/proof-of-play-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/proof-of-play-domain-security.yml
created: '2026-07-17'
description: 'Proof of Play is an a16z-backed gaming studio and on-chain infrastructure company, founded by Amitt Mahajan and best known for the fully on-chain RPG Pirate Nation. It builds a platform for high-performance, serverless on-chain applications and games, exposing a set of developer services: a verified random number generator (vRNG) for fast, secure on-chain randomness; a Marketplace API for peer-to-peer trading across on-chain and off-chain inventory; an on-chain NoSQL Entity-Component-System (ECS) database and indexer; token mirroring to replicate NFT ownership data across chains; a gasless relayer; and multichain scaling. Documentation and a public OpenAPI are published at docs.proofofplay.com, and much of the stack is progressively open-sourced under MIT on GitHub.'
image: https://media.proofofplay.com/public/POP_Home_OG.png
layout: provider
modified: '2026-07-20'
name: Proof of Play
nav: Providers
network: true
overview: 'Proof of Play publishes 1 API on the [APIs.io](https://apis.io/) network: Public API API. Tagged areas include Company, Gaming, Blockchain, Web3, and Randomness.


  Proof of Play''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 16 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 43.5
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 33.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/proof-of-play/refs/heads/main/screenshots/proof-of-play-2026-09-02T152147.png
security:
- kind: authentication
  name: Proof Of Play Authentication
  slug: proof-of-play-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Proof Of Play Domain Security
  slug: proof-of-play-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: proof-of-play
tags:
- Company
- Gaming
- Blockchain
- Web3
- Randomness
- Onchain Infrastructure
- NFT
- Developer Services
website: https://docs.proofofplay.com/introduction
---
