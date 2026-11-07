---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'CardMind API as documented publicly: 12 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: CardMind API
  slug: cardmind-app-api
artifact_total: 14
asyncapis:
- description: ''
  name: Cardmind App Webhooks
  slug: cardmind-app-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/cardmind-app/rate-limits/cardmind-app-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cardmind-app-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/cardmind-app/plans/cardmind-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cardmind-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cardmind-app/rules/cardmind-app-rules.yml
  title: ''
  type: Spectral
  url: rules/cardmind-app-rules.yml
- group: design
  href: https://artifacts.apis.io/cardmind-app/json-ld/cardmind-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cardmind-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/cardmind-app/vocabulary/cardmind-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cardmind-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cardmind-app/asyncapi/cardmind-app-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cardmind-app-webhooks.yml
- group: design
  href: https://artifacts.apis.io/cardmind-app/data-model/cardmind-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cardmind-app-data-model.yml
- group: auth
  href: https://artifacts.apis.io/cardmind-app/authentication/cardmind-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cardmind-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/cardmind-app/conformance/cardmind-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cardmind-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cardmind-app/well-known/cardmind-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cardmind-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/cardmind-app/hosts/cardmind-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cardmind-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/cardmind-app/vendors/cardmind-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cardmind-app-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cardmind-app/security/cardmind-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cardmind-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cardmind.app/
- group: docs
  title: ''
  type: APIReference
  url: https://api.cardmind.app/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cardmind.app/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.cardmind.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cardmind.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cardmind.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cardmind.app/privacy
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/cardmind
- group: start
  title: ''
  type: SignUp
  url: https://www.cardmind.app/auth/signup
- group: start
  title: ''
  type: Login
  url: https://www.cardmind.app/auth/signin
coverage:
  checked: '2026-11-03'
  detail: Provider documentation is publicly accessible but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract could be found.
  evidence:
  - status: 200
    url: https://api.cardmind.app/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: 'CardMind provides market intelligence for Magic: The Gathering (MTG) cards, offering real‑time price data, signals, and analytics for collectors and traders. Built by a longtime collector and engineer, the platform tracks over 113,000 cards, monitors daily signals, and delivers tools such as price calculators, market movers, and ban‑watch lists. The service emphasizes transparency, data‑driven insights, and open methodology, aiming to help users understand card values without financial advice.'
json_schemas:
- name: DeleteApiWebhooksResponse
  property_count: 3
  slug: cardmind-app-delete-api-webhooks-response
- name: GetApiCardsCardidResponse
  property_count: 3
  slug: cardmind-app-get-api-cards-cardid-response
- name: GetApiPricesMoversResponse
  property_count: 2
  slug: cardmind-app-get-api-prices-movers-response
- name: PostApiCardsSearchResponse
  property_count: 9
  slug: cardmind-app-post-api-cards-search-response
- name: PostApiInternalFleetHeartbeatRequest
  property_count: 4
  slug: cardmind-app-post-api-internal-fleet-heartbeat-request
- name: PostApiWebhooksResponse
  property_count: 2
  slug: cardmind-app-post-api-webhooks-response
jsonld:
- class_count: 16
  name: Cardmind App Context
  property_count: 21
  slug: cardmind-app-context
layout: provider
modified: '2026-11-03'
name: CardMind
nav: Providers
network: true
overview: 'CardMind is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Market Intelligence, Price Data, Signals, Ban Watch, and Deck Intelligence.


  The CardMind catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  CardMind''s developer surface includes authentication, API reference, getting-started guide, engineering blog, pricing, support, signup flow, and 16 more developer resources.'
plans:
- name: Cardmind App Plans Pricing
  plan_count: 4
  slug: cardmind-app-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Cardmind App Rate Limits
  slug: cardmind-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: CardMind API Rules
  rule_count: 45
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 2
  slug: cardmind-app-rules
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 75.8
    catalog_earned_first_party: 20.0
    catalog_gap: 39.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 32.5
    developer_ergonomics: 25.0
    discoverability: 53.6
    operational_transparency: 28.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cardmind App Authentication
  slug: cardmind-app-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Cardmind App Domain Security
  slug: cardmind-app-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cardmind-app
tags:
- Market Intelligence
- Price Data
- Signals
- Ban Watch
- Deck Intelligence
website: https://www.cardmind.app/
---
