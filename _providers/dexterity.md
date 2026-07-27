---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 4
  human_in_the_loop: 1
  name: Dexterity Agentic Access
  operation_count: 8
  slug: dexterity-agentic-access
  summary_line: 8 operations · 4 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: Start, place boxes in, stop and query the status of packing games.
  name: Dexterity Games API
  slug: dexterity-games-api
- description: Retrieve the public Foresight Packing Challenge leaderboard.
  name: Dexterity Leaderboard API
  slug: dexterity-leaderboard-api
- description: List a player's games and update their public display name.
  name: Dexterity Players API
  slug: dexterity-players-api
- description: Service health and operational endpoints.
  name: Dexterity System API
  slug: dexterity-system-api
artifact_total: 54
collections:
- collection_type: open
  name: Dexterity Foresight Packing Challenge API
  slug: open-dexterity-foresight-packing-challenge
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dexterity-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dexterity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dexterity.ai
- group: other
  title: ''
  type: Platform
  url: https://www.dexterity.ai/platform
- group: other
  title: ''
  type: Foresight
  url: https://www.dexterity.ai/blog/foresight
- group: other
  title: ''
  type: Mech
  url: https://www.dexterity.ai/platform
- group: other
  title: ''
  type: Challenge
  url: https://dexterity.ai/challenge
- group: other
  title: ''
  type: TruckLoadingGame
  url: https://dexterity.ai/play
- group: company
  title: ''
  type: About
  url: https://www.dexterity.ai/about
- group: company
  title: ''
  type: Blog
  url: https://www.dexterity.ai/blog
- group: operate
  title: ''
  type: Contact
  url: https://www.dexterity.ai/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dexterity.ai/terms-conditions
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dexterityinc
- group: design
  title: ''
  type: SpectralRules
  url: rules/dexterity-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/dexterity-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/dexterity-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/dexterity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dexterity-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dexterity-finops.yml
created: '2026-05-24'
description: Dexterity is a Redwood City, California Physical AI company founded in 2017 by Samir Menon and a group of Stanford roboticists. It builds a full-stack industrial robotics platform that combines the Mech — a roving, dual-arm superhumanoid robot — with Foresight, an in-house world model trained on more than 100 million autonomous actions in production. Foresight orchestrates 68+ skill agents (packing, motion, actualization, trajectory, force-control) across the IRIS hardware abstraction layer to drive Kawasaki arms, HiWin motion components, and Dexterity's own mobile bases at sub-400ms decision latency with zero reported safety incidents. Customers include FedEx, UPS, Sagawa Express, Maersk, and VFC, and the company has raised more than 291M USD from Kleiner Perkins, Lightspeed Venture Partners, Obvious Ventures, Sumitomo Corporation, and B37 Ventures. Dexterity's commercial offering is enterprise Physical AI deployment (no self-service developer API), but it does run a public,
  research-grade REST API — the Foresight Packing Challenge — that exposes the bin-packing facet of Foresight as a programmable sequential placement game, with a 50,000 USD grand prize and participation restricted to .edu email holders.
examples:
- key_count: 2
  name: Dexterity Foresight Display Name Example
  slug: dexterity-foresight-display-name-example
- key_count: 2
  name: Dexterity Foresight Get Status Example
  slug: dexterity-foresight-get-status-example
- key_count: 2
  name: Dexterity Foresight Health Example
  slug: dexterity-foresight-health-example
- key_count: 2
  name: Dexterity Foresight Leaderboard Example
  slug: dexterity-foresight-leaderboard-example
- key_count: 2
  name: Dexterity Foresight My Games Example
  slug: dexterity-foresight-my-games-example
- key_count: 2
  name: Dexterity Foresight Place Box Example
  slug: dexterity-foresight-place-box-example
- key_count: 2
  name: Dexterity Foresight Start Game Example
  slug: dexterity-foresight-start-game-example
- key_count: 2
  name: Dexterity Foresight Stop Game Example
  slug: dexterity-foresight-stop-game-example
features:
- description: In-house world model trained on 100M+ autonomous actions for spatial reasoning, prediction, and dual-arm orchestration.
  name: Foresight World Model
- description: Specialized agents including Packing, Motion, Actualization, Trajectory, and Force-Control coordinated in real time.
  name: 68+ Autonomous Skill Agents
- description: Unified API enabling deployment of Physical AI across Kawasaki arms, HiWin motion components, and Dexterity-built mobile bases.
  name: IRIS Hardware Abstraction Layer
- description: Roving superhumanoid robot with two arms designed for industrial logistics tasks.
  name: Mech Dual-Arm Robot
- description: End-to-end perception-to-action loop under 400ms in production environments.
  name: Sub-400ms Decision Loop
- description: 100M+ autonomous decisions in production with no reported safety incidents to date.
  name: Zero Safety Incidents
- description: Public, research-grade REST API exposing the bin-packing facet of Foresight with a public leaderboard and 50,000 USD prize.
  name: Foresight Packing Challenge API
finops:
- name: Dexterity Finops
  service_category: PhysicalAI
  slug: dexterity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dexterity.png
integrations:
- description: Partnership producing intelligent industrial robot arms for warehouse applications.
  name: Kawasaki Heavy Industries
- description: Precision motion control components integrated into Dexterity systems.
  name: HiWin
- description: GPU acceleration of Foresight via TensorRT and CUDA delivering a 17x speedup.
  name: NVIDIA
- description: Production deployment partner; Dexterity highlighted at FedEx Investor Day 2026.
  name: FedEx
- description: Production logistics deployment in Japan via partnership with Sumitomo Corporation.
  name: Sagawa Express
- description: Japan market partner and investor; led recent funding rounds.
  name: Sumitomo Corporation
- description: Enterprise customer deploying Dexterity robots in production logistics operations.
  name: UPS
- description: Global logistics customer running Dexterity systems.
  name: Maersk
- description: Enterprise customer.
  name: VFC
json_schemas:
- name: Box
  property_count: 3
  slug: dexterity-foresight-box
- name: Game
  property_count: 9
  slug: dexterity-foresight-game
- name: LeaderboardEntry
  property_count: 6
  slug: dexterity-foresight-leaderboard-entry
- name: PlacedBox
  property_count: 4
  slug: dexterity-foresight-placed-box
- name: TruckConfig
  property_count: 3
  slug: dexterity-foresight-truck-config
json_structures:
- name: Dexterity Foresight Game Structure
  property_count: 0
  slug: dexterity-foresight-game-structure
jsonld:
- class_count: 36
  name: Dexterity Context
  property_count: 2
  slug: dexterity-context
layout: provider
modified: '2026-05-24'
name: Dexterity
nav: Providers
network: true
overview: 'Dexterity publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Games API, Leaderboard API, Players API, and 1 more. Tagged areas include Physical AI, Industrial Robotics, Robotics, Warehouse Automation, and Logistics.


  The Dexterity catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Dexterity''s developer surface includes engineering blog and 18 more developer resources.'
plans:
- name: Dexterity Plans Pricing
  plan_count: 2
  slug: dexterity-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 3
  name: Dexterity Rate Limits
  slug: dexterity-rate-limits
rules:
- name: Dexterity API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: dexterity-jsonschema-spectral-rules
- name: Dexterity API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 3
  slug: dexterity-rules
score:
  band: developing
  composite: 48.6
  delta: 5.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.8
    developer_ergonomics: 2.2
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 31.6
  previous_composite: 43.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/dexterity/refs/heads/main/screenshots/dexterity-2026-06-20T180009.png
security:
- kind: domain-security
  name: Dexterity Domain Security
  slug: dexterity-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: dexterity
solutions:
- description: End-to-end automation of trailer-, pallet-, and case-handling tasks in warehouse and parcel operations.
  name: Logistics Automation
- description: Dual-arm material handling on the manufacturing floor.
  name: Manufacturing Material Handling
- description: Loading and unloading cargo for air freight workflows.
  name: Air Cargo Handling
- description: Free research access for academic teams to a slice of Foresight via a public REST API and competition.
  name: Research Access (Foresight Packing Challenge)
tags:
- Physical AI
- Industrial Robotics
- Robotics
- Warehouse Automation
- Logistics
- Manufacturing
- World Model
- Foresight
- Mech
- Dual-Arm
- Truck Loading
- Palletizing
- Depalletizing
- Singulation
- Research API
- Packing Challenge
use_cases:
- description: Autonomous dual-arm loading of mixed-SKU boxes into truck trailers at the dock.
  name: Trailer Loading
- description: Autonomous depalletization and unloading of inbound trailers.
  name: Trailer Unloading
- description: Building stable pallets from heterogeneous case mixes.
  name: Palletizing
- description: Breaking down pallets into individual cases for downstream handling.
  name: Depalletizing
- description: Separating items from bulk flow into a single, oriented stream for sortation.
  name: Singulation
- description: Cargo loading and unloading for air freight operations.
  name: Aircraft Loading and Unloading
- description: Academic and industry research into sequential 3D bin packing using the public Foresight Packing Challenge API.
  name: Bin Packing Research
website: https://www.dexterity.ai
---
