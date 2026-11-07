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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.0
  scored_at: '2026-11-06'
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
  name: Proof of Play Public API
  slug: proof-of-play-public-api-api
artifact_total: 7
collections:
- collection_type: open
  name: Proof of Play Public API API
  slug: open-proof-of-play-public-api-api
common:
- group: company
  title: ''
  type: Website
  url: https://proofofplay.com
- group: other
  href: https://artifacts.apis.io/proof-of-play/overlays/proof-of-play-vrf-overlay.yaml
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
  href: https://artifacts.apis.io/proof-of-play/authentication/proof-of-play-authentication.yml
  title: ''
  type: Authentication
  url: authentication/proof-of-play-authentication.yml
- group: design
  href: https://artifacts.apis.io/proof-of-play/conventions/proof-of-play-conventions.yml
  title: ''
  type: Conventions
  url: conventions/proof-of-play-conventions.yml
- group: design
  href: https://artifacts.apis.io/proof-of-play/lifecycle/proof-of-play-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/proof-of-play-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/proof-of-play/conformance/proof-of-play-conformance.yml
  title: ''
  type: Conformance
  url: conformance/proof-of-play-conformance.yml
- group: agent
  href: https://artifacts.apis.io/proof-of-play/mcp/proof-of-play-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/proof-of-play-mcp.yml
- group: agent
  href: https://artifacts.apis.io/proof-of-play/llms/proof-of-play-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/proof-of-play-llms.txt
- group: agent
  href: https://artifacts.apis.io/proof-of-play/well-known/proof-of-play-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/proof-of-play-well-known.yml
- group: agent
  href: https://artifacts.apis.io/proof-of-play/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/proof-of-play/agentic-access/proof-of-play-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/proof-of-play-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/proof-of-play/security/proof-of-play-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/proof-of-play-domain-security.yml
created: '2026-07-17'
description: 'Proof of Play is an a16z-backed gaming studio and on-chain infrastructure company, founded by Amitt Mahajan and best known for the fully on-chain RPG Pirate Nation. It builds a platform for high-performance, serverless on-chain applications and games, exposing a set of developer services: a verified random number generator (vRNG) for fast, secure on-chain randomness; a Marketplace API for peer-to-peer trading across on-chain and off-chain inventory; an on-chain NoSQL Entity-Component-System (ECS) database and indexer; token mirroring to replicate NFT ownership data across chains; a gasless relayer; and multichain scaling. Documentation and a public OpenAPI are published at docs.proofofplay.com, and much of the stack is progressively open-sourced under MIT on GitHub.'
image: https://media.proofofplay.com/public/POP_Home_OG.png
layout: provider
modified: '2026-09-16'
name: Proof of Play
nav: Providers
network: true
overview: 'Proof of Play publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Company, Gaming, Blockchain, Web3, and Randomness.


  The Proof of Play catalog on APIs.io includes 1 Spectral governance ruleset.


  Proof of Play''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 17 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: Proof of Play API Rules
  rule_count: 38
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 1
  slug: proof-of-play-rules
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 43.5
    developer_ergonomics: 51.8
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/proof-of-play/proof-of-play-2026-09-02T152147.png
security:
- kind: authentication
  name: Proof Of Play Authentication
  slug: proof-of-play-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Proof Of Play Domain Security
  slug: proof-of-play-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
skill_count: 1
skills:
- name: Get a signed vRNG message
  slug: proof-of-play-vrf-signed-message
slug: proof-of-play
tags:
- Company
- Gaming
- Blockchain
- Web3
- Randomness
- Onchain Infrastructure
- NFT
website: https://proofofplay.com
---
