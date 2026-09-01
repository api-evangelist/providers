---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 36
  human_in_the_loop: 1
  name: Beamable Agentic Access
  operation_count: 65
  slug: beamable-agentic-access
  summary_line: 65 operations · 36 acting · 1 human-in-the-loop
api_count: 4
apis:
- description: REST API for virtual currency, inventory, and in-game store management. Provides endpoints for granting, spending, and querying player currencies, managing item inventories, configuring store catalogs
  name: Beamable Game Economy API
  slug: game-economy
- description: The Basic API from Beamable — 43 operation(s) for basic.
  name: Beamable Basic API
  slug: beamable-basic-api
- description: The Object API from Beamable — 4 operation(s) for object.
  name: Beamable Object API
  slug: beamable-object-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: realms Basic API
  slug: open-beamable-basic-api
- collection_type: open
  name: realms Basic Object API
  slug: open-beamable-object-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/beamable-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beamable-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/beamable-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://beamable.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.beamable.com/docs/beamable-overview
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/beamable
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/beamable
- group: company
  title: ''
  type: Blog
  url: https://beamable.com/category/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://beamable.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://beamable.github.io/status/
- group: other
  title: ''
  type: X
  url: https://twitter.com/Beamable
- group: company
  title: ''
  type: BlogRSS
  url: https://beamable.com/feed/
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/beamable-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/beamable-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/beamable-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/beamable-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/beamable-finops.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/beamable-graphql.md
created: '2026-06-12'
description: Beamable is a cloud backend platform purpose-built for games and interactive applications, providing REST APIs and SDK integrations for Unity, Unreal, and web environments. The platform delivers production-ready services covering player identity and authentication, virtual currency and economy, inventory management, leaderboards, matchmaking, live events, and analytics. Developers can extend the platform with custom C# microservices and scheduled jobs, deploying server-side logic without managing infrastructure. Beamable is backed by AWS and has served over 30 million players, offering a LiveOps portal, CLI tooling, and content management for games-as-a-service operations.
examples:
- key_count: 7
  name: Beamable Live Event Score Example
  slug: beamable-live-event-score-example
- key_count: 7
  name: Beamable Microservice Manifest Example
  slug: beamable-microservice-manifest-example
- key_count: 7
  name: Beamable Player Auth Example
  slug: beamable-player-auth-example
finops:
- name: Beamable Finops
  service_category: ''
  slug: beamable-finops
graphqls:
- description: This conceptual GraphQL schema models the Beamable game backend platform for LiveOps. Beamable provides production-ready services for player identity, virtual economy, inventory management, leaderboar
  name: Beamable GraphQL Schema
  slug: beamable-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/beamable.png
json_schemas:
- name: Beamable Live Events Schemas
  property_count: 0
  slug: beamable-live-events
- name: Beamable Microservices Schemas
  property_count: 0
  slug: beamable-microservices
- name: Beamable Player Accounts Schemas
  property_count: 0
  slug: beamable-player-accounts
jsonld:
- class_count: 10
  name: Beamable Context
  property_count: 28
  slug: beamable-context
layout: provider
modified: '2026-06-12'
name: Beamable
nav: Providers
network: true
overview: 'Beamable publishes 2 APIs on the [APIs.io](https://apis.io/) network: Basic API and Object API. Tagged areas include Game Backend, LiveOps, Player Accounts, Virtual Currency, and Inventory.


  The Beamable catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Beamable''s developer surface includes authentication, documentation, engineering blog, pricing, and 15 more developer resources.'
plans:
- name: Beamable Plans Pricing
  plan_count: 5
  slug: beamable-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 12
  name: Beamable Rate Limits
  slug: beamable-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Beamable API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: beamable-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 16
    catalog_gap: 28.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 57.7
    developer_ergonomics: 19.0
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 52.6
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beamable/refs/heads/main/screenshots/beamable-2026-06-20T173103.png
security:
- kind: authentication
  name: Beamable Authentication
  slug: beamable-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Beamable Domain Security
  slug: beamable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beamable
tags:
- Game Backend
- LiveOps
- Player Accounts
- Virtual Currency
- Inventory
- Leaderboards
- Matchmaking
- Microservices
- Unity
- Unreal
- Game Economy
- Analytics
website: https://beamable.com/
---
