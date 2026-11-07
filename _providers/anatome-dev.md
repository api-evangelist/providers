---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Anatome — Muscle Group Image Generator API providing SVG rendering of muscle groups and exercise data.
  name: Anatome Muscle Group Image Generator API
  slug: anatome-muscle-group-image-generator-api
- description: Unified human-body API platform offering exercise, anatomy, food, recipes, workouts, nutrition, AI, and more.
  name: Anatome Unified Human-Body Platform API
  slug: anatome-unified-human-body-platform-api
artifact_total: 8
common:
- group: operate
  href: https://artifacts.apis.io/anatome-dev/rate-limits/anatome-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/anatome-dev-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/anatome-dev/vocabulary/anatome-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/anatome-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/anatome-dev/errors/anatome-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/anatome-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/anatome-dev/conformance/anatome-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anatome-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/anatome-dev/llms/anatome-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anatome-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/anatome-dev/mcp/anatome-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anatome-dev-mcp.yml
- group: auth
  href: https://artifacts.apis.io/anatome-dev/well-known/anatome-dev-platform-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anatome-dev-platform-security.txt
- group: agent
  href: https://artifacts.apis.io/anatome-dev/well-known/anatome-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anatome-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/anatome-dev/hosts/anatome-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anatome-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/anatome-dev/vendors/anatome-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anatome-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anatome.dev/terms
- group: operate
  title: ''
  type: Support
  url: https://anatome.dev/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anatome.dev/privacy
- group: auth
  href: https://artifacts.apis.io/anatome-dev/security/anatome-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anatome-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anatome.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://wiki.anatome.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://wiki.anatome.dev/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://wiki.anatome.dev/docs/getting-started
created: '2026-11-01'
description: Anatome provides a free AI agent for workout and nutrition tracking without registration. Users can log exercises, meals, and view muscle diagrams and barcode food search. The service integrates with ChatGPT and Claude via a simple URL endpoint, allowing AI assistants to record health data. It offers over 800 exercises, an extensive nutrition database, and visual aids, all hosted at anatome.dev. This platform emphasizes privacy, keyless access, and AI‑enhanced health logging.
image: https://anatome.dev/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at anatome.dev.
  name: Anatome MCP Server
  slug: anatome-dev-mcp-yml
modified: '2026-11-01'
name: Anatome
nav: Providers
network: true
overview: 'Anatome is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fitness, Nutrition, Artificial Intelligence, Health, and Workout Tracking.


  Anatome''s developer surface includes support, documentation, API reference, getting-started guide, and 14 more developer resources.'
plans:
- name: Anatome Dev Plans Pricing
  plan_count: 0
  slug: anatome-dev-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 1
  name: Anatome Dev Rate Limits
  slug: anatome-dev-rate-limits
scopes:
- name: Anatome Dev Scopes
  scope_count: 0
  slug: anatome-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 46.3
    catalog_earned_first_party: 8.0
    catalog_gap: 68.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 65.0
    operational_transparency: 31.6
  previous_composite: 26.9
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 27.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anatome Dev Authentication
  slug: anatome-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Anatome Dev Domain Security
  slug: anatome-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: anatome-dev
tags:
- Fitness
- Nutrition
- Artificial Intelligence
- Health
- Workout Tracking
website: https://anatome.dev/
---
