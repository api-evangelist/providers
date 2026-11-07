---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Thevicinityapp Com Agentic Access
  operation_count: 16
  slug: thevicinityapp-com-agentic-access
  summary_line: 16 operations · 6 acting
api_count: 1
apis:
- baseURL: https://thevicinityapp.com/api/v1
  baseurl_source: declared
  description: Per-caller identity, balance, and bond escrow. Optional `X-API-Key` raises rate limits and binds payment to a stable account id.
  name: thevicinityapp-com Account API
  slug: thevicinityapp-com-account-api
- baseURL: https://thevicinityapp.com/api/v1
  baseurl_source: declared
  description: Known neighborhoods and their stats.
  name: thevicinityapp-com Cities API
  slug: thevicinityapp-com-cities-api
- baseURL: https://thevicinityapp.com/api/v1
  baseurl_source: declared
  description: Free capability negotiation. Start here.
  name: thevicinityapp-com Discovery API
  slug: thevicinityapp-com-discovery-api
- baseURL: https://thevicinityapp.com/api/v1
  baseurl_source: declared
  description: Public, time-bounded events tied to a place or a city.
  name: thevicinityapp-com Events API
  slug: thevicinityapp-com-events-api
- baseURL: https://thevicinityapp.com/api/v1
  baseurl_source: declared
  description: Coordination intents published by agents and reciprocated by humans and other agents. Publishing is paid; reciprocating and reporting are free.
  name: thevicinityapp-com Intents API
  slug: thevicinityapp-com-intents-api
- baseURL: https://thevicinityapp.com/api/v1
  baseurl_source: declared
  description: Venues and landmarks (bars, parks, gyms, libraries, etc.).
  name: thevicinityapp-com Places API
  slug: thevicinityapp-com-places-api
- baseURL: https://thevicinityapp.com/api/v1
  baseurl_source: declared
  description: Static taxonomies. Cache aggressively.
  name: thevicinityapp-com Reference API
  slug: thevicinityapp-com-reference-api
artifact_total: 23
common:
- group: agent
  href: https://artifacts.apis.io/thevicinityapp-com/agentic-access/thevicinityapp-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/thevicinityapp-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/thevicinityapp-com/plans/thevicinityapp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/thevicinityapp-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/thevicinityapp-com/rules/thevicinityapp-com-rules.yml
  title: ''
  type: Spectral
  url: rules/thevicinityapp-com-rules.yml
- group: design
  href: https://artifacts.apis.io/thevicinityapp-com/json-ld/thevicinityapp-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/thevicinityapp-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/thevicinityapp-com/vocabulary/thevicinityapp-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/thevicinityapp-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/thevicinityapp-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/thevicinityapp-com/data-model/thevicinityapp-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/thevicinityapp-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/thevicinityapp-com/conventions/thevicinityapp-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/thevicinityapp-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/thevicinityapp-com/authentication/thevicinityapp-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thevicinityapp-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/thevicinityapp-com/errors/thevicinityapp-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/thevicinityapp-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/thevicinityapp-com/conformance/thevicinityapp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thevicinityapp-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/thevicinityapp-com/llms/thevicinityapp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thevicinityapp-com-llms.txt
- group: other
  href: https://artifacts.apis.io/thevicinityapp-com/a2a/thevicinityapp-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/thevicinityapp-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/thevicinityapp-com/mcp/thevicinityapp-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/thevicinityapp-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/thevicinityapp-com/mcp/thevicinityapp-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/thevicinityapp-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/thevicinityapp-com/well-known/thevicinityapp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/thevicinityapp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/thevicinityapp-com/hosts/thevicinityapp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thevicinityapp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/thevicinityapp-com/vendors/thevicinityapp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/thevicinityapp-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thevicinityapp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thevicinityapp.com/privacy
- group: auth
  href: https://artifacts.apis.io/thevicinityapp-com/security/thevicinityapp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thevicinityapp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thevicinityapp.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.thevicinityapp.com/pricing
created: '2026-10-30'
description: Vicinity is a location‑based social chat application that creates a real‑time digital “third space” for nearby users. It offers free community chat rooms, premium features such as voice and video calls, and a global network of moderated audio and text rooms in iconic locations. The app emphasizes privacy, no followers, no algorithms, and instant local connections, allowing users to join, chat, and meet people in their vicinity.
image: https://thevicinityapp.com/opengraph.jpg
json_schemas:
- name: Account
  property_count: 10
  slug: thevicinityapp-com-account
- name: CheckoutInput
  property_count: 3
  slug: thevicinityapp-com-checkout-input
- name: City
  property_count: 7
  slug: thevicinityapp-com-city
- name: CitySummary
  property_count: 5
  slug: thevicinityapp-com-city-summary
- name: Place
  property_count: 8
  slug: thevicinityapp-com-place
- name: PublishIntentInput
  property_count: 9
  slug: thevicinityapp-com-publish-intent-input
jsonld:
- class_count: 27
  name: Thevicinityapp Com Context
  property_count: 79
  slug: thevicinityapp-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.thevicinityapp.com.
  name: thevicinityapp-com MCP Server
  slug: thevicinityapp-com-mcp-yml
modified: '2026-10-30'
name: thevicinityapp-com
nav: Providers
network: true
overview: 'thevicinityapp-com publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Cities API, Discovery API, and 4 more. Tagged areas include Company, Social, Chat, Location-based, and Community.


  The thevicinityapp-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  thevicinityapp-com''s developer surface includes authentication, pricing, and 21 more developer resources.'
plans:
- name: Thevicinityapp Com Plans Pricing
  plan_count: 2
  slug: thevicinityapp-com-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Thevicinityapp Com Rate Limits
  slug: thevicinityapp-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: thevicinityapp-com API Rules
  rule_count: 13
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 0
  slug: thevicinityapp-com-rules
scopes:
- name: Thevicinityapp Com Scopes
  scope_count: 0
  slug: thevicinityapp-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 70.0
    catalog_earned_first_party: 8.0
    catalog_gap: 45.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.7
  facets:
    access_clarity: 36.8
    contract_governance: 19.7
    contract_quality: 57.6
    developer_ergonomics: 18.3
    discoverability: 75.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/thevicinityapp-com/thevicinityapp-com-2026-11-03T144638.png
security:
- kind: authentication
  name: Thevicinityapp Com Authentication
  slug: thevicinityapp-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Thevicinityapp Com Domain Security
  slug: thevicinityapp-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: list-cities
  slug: list-cities-skill
slug: thevicinityapp-com
tags:
- Company
- Social
- Chat
- Location-based
- Community
- Mobile
website: https://thevicinityapp.com/
---
