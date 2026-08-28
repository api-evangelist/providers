---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
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
    delegated_identity: documented
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
  score: 21.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Toornament Agentic Access
  operation_count: 16
  slug: toornament-agentic-access
  summary_line: 16 operations · 6 acting
api_count: 9
apis:
- description: Read-only public API for accessing tournament information without full organizer authentication. Ideal for embedding tournament brackets, leaderboards, and match schedules in applications, streaming o
  name: Toornament Viewer API
  slug: viewer-api
- description: Access esports discipline metadata.
  name: Toornament Disciplines API
  slug: toornament-disciplines-api
- description: Manage tournament matches and results.
  name: Toornament Matches API
  slug: toornament-matches-api
- description: Manage tournament participants and registrations.
  name: Toornament Participants API
  slug: toornament-participants-api
- description: Retrieve tournament rankings and standings.
  name: Toornament Rankings API
  slug: toornament-rankings-api
- description: Manage tournament registrations.
  name: Toornament Registrations API
  slug: toornament-registrations-api
- description: Manage tournament stages and brackets.
  name: Toornament Stages API
  slug: toornament-stages-api
- description: Create, manage, and retrieve tournament information.
  name: Toornament Tournaments API
  slug: toornament-tournaments-api
- description: Manage webhook subscriptions for tournament events.
  name: Toornament Webhooks API
  slug: toornament-webhooks-api
artifact_total: 55
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Toornament Disciplines API
  slug: open-toornament-disciplines-api
- collection_type: open
  name: Toornament Disciplines Matches API
  slug: open-toornament-matches-api
- collection_type: open
  name: Toornament Disciplines Participants API
  slug: open-toornament-participants-api
- collection_type: open
  name: Toornament Disciplines Rankings API
  slug: open-toornament-rankings-api
- collection_type: open
  name: Toornament Disciplines Registrations API
  slug: open-toornament-registrations-api
- collection_type: open
  name: Toornament Disciplines Stages API
  slug: open-toornament-stages-api
- collection_type: open
  name: Toornament Disciplines Tournaments API
  slug: open-toornament-tournaments-api
- collection_type: open
  name: Toornament Disciplines Webhooks API
  slug: open-toornament-webhooks-api
- collection_type: open
  name: Toornament API
  slug: open-toornament
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/toornament-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/toornament-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/toornament-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/toornament-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/toornament
- group: company
  title: ''
  type: Website
  url: https://www.toornament.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.toornament.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.toornament.com/v2/overview/get-started
- group: start
  title: ''
  type: Signup
  url: https://www.toornament.com/signup/
- group: start
  title: ''
  type: Login
  url: https://app.toornament.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.toornament.com/en_US/p/tournament-api
- group: design
  title: ''
  type: JSONLD
  url: json-ld/toornament-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/toornament-tournament-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/toornament-tournament-structure.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/toornament-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/toornament-vocabulary.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.toornament.com/feed/
created: '2025-02-06'
description: Toornament is an esports tournament management platform providing a comprehensive API for creating, managing, and viewing tournaments across 100+ esports disciplines. The API supports full tournament lifecycle management including participant registration, bracket generation, match reporting, and real-time standings. Used by game publishers, esports organizers, broadcasters, and gaming communities worldwide.
examples:
- key_count: 4
  name: Toornament Create Tournament Example
  slug: toornament-create-tournament-example
- key_count: 4
  name: Toornament Report Match Example
  slug: toornament-report-match-example
features:
- name: Tournament Creation and Management
- name: Participant Registration
- name: Bracket Generation (Single/Double Elimination)
- name: Group Stage Management
- name: Match Reporting
- name: Live Rankings and Standings
- name: Custom Registration Fields
- name: Check-in Management
- name: Webhook Event Notifications
- name: Multi-discipline Support (100+ games)
- name: Team and Player Support
- name: Public Tournament Viewer API
finops:
- name: Toornament Finops
  service_category: API
  slug: toornament-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/toornament.png
integrations:
- name: Postman
- name: Insomnia
- name: OAuth2 Identity Providers
json_schemas:
- name: Toornament Participant
  property_count: 9
  slug: toornament-participant
- name: Toornament Tournament
  property_count: 25
  slug: toornament-tournament
json_structures:
- name: Toornament Tournament Structure
  property_count: 0
  slug: toornament-tournament-structure
jsonld:
- class_count: 0
  name: Toornament Context
  property_count: 7
  slug: toornament-context
layout: provider
modified: '2026-05-19'
name: Toornament
nav: Providers
network: true
overview: 'Toornament publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Disciplines API, Matches API, Participants API, and 5 more. Tagged areas include Esports, Gaming, Tournaments, Brackets, and Competition.


  The Toornament catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Toornament''s developer surface includes authentication, documentation, getting-started guide, signup flow, pricing, engineering blog, and 11 more developer resources.'
plans:
- name: Toornament Plans Pricing
  plan_count: 3
  slug: toornament-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Toornament Rate Limits
  slug: toornament-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Toornament API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: toornament-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Toornament API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 1
    info: 0
    warn: 5
  slug: toornament-rules
scopes:
- name: Toornament Scopes
  scope_count: 3
  slug: toornament-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 41.6
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 28.8
    contract_quality: 63.9
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/toornament/refs/heads/main/screenshots/toornament-2026-06-20T195451.png
security:
- kind: authentication
  name: Toornament Authentication
  slug: toornament-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Toornament Domain Security
  slug: toornament-domain-security
  summary_line: TLSv1.3 · HSTS
slug: toornament
tags:
- Esports
- Gaming
- Tournaments
- Brackets
- Competition
use_cases:
- name: Esports Tournament Platform
- name: Game Publisher Tournament Integration
- name: Streaming Overlay Bracket Display
- name: Community Tournament Management
- name: Fan Site Tournament Viewer
- name: Circuit and League Management
website: https://www.toornament.com/
---
