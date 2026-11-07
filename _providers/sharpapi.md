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
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Sharpapi Agentic Access
  operation_count: 36
  slug: sharpapi-agentic-access
  summary_line: 36 operations · 5 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.sharpapi.io/api/v1
  baseurl_source: declared
  description: Account info, usage, and key management
  name: SharpAPI Account API
  slug: sharpapi-account-api
- baseURL: https://api.sharpapi.io/api/v1
  baseurl_source: declared
  description: Public betting splits — handle % and bet % from DraftKings (recreational) and Circa Sports (sharp-friendly), plus ticket-only percentages derived from BetMGM. Splits are a fixed three-source feature a
  name: SharpAPI Betting Splits API
  slug: sharpapi-betting-splits-api
- baseURL: https://api.sharpapi.io/api/v1
  baseurl_source: declared
  description: Sportsbook deep link generation
  name: SharpAPI Deep Links API
  slug: sharpapi-deep-links-api
- baseURL: https://api.sharpapi.io/api/v1
  baseurl_source: declared
  description: Event discovery and details
  name: SharpAPI Events API
  slug: sharpapi-events-api
- baseURL: https://api.sharpapi.io/api/v1
  baseurl_source: declared
  description: Futures markets and odds
  name: SharpAPI Futures API
  slug: sharpapi-futures-api
- baseURL: https://api.sharpapi.io/api/v1
  baseurl_source: declared
  description: Live game state data (Game State add-on or Enterprise)
  name: SharpAPI Game State API
  slug: sharpapi-game-state-api
- baseURL: https://api.sharpapi.io/api/v1
  baseurl_source: declared
  description: Service health and status
  name: SharpAPI Health API
  slug: sharpapi-health-api
- baseURL: https://api.sharpapi.io/api/v1
  baseurl_source: declared
  description: Odds snapshots, comparisons, batch, and deltas
  name: SharpAPI Odds API
  slug: sharpapi-odds-api
- baseURL: https://api.sharpapi.io/api/v1
  baseurl_source: declared
  description: +EV, arbitrage, middles, and low-hold opportunities
  name: SharpAPI Opportunities API
  slug: sharpapi-opportunities-api
- baseURL: https://api.sharpapi.io/api/v1
  baseurl_source: declared
  description: Sports, leagues, sportsbooks, markets, and teams
  name: SharpAPI Reference Data API
  slug: sharpapi-reference-data-api
- baseURL: https://api.sharpapi.io/api/v1
  baseurl_source: declared
  description: Real-time SSE streaming
  name: SharpAPI Streaming API
  slug: sharpapi-streaming-api
artifact_total: 27
common:
- group: other
  href: https://artifacts.apis.io/sharpapi/capabilities/sharpapi-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sharpapi-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/sharpapi/agentic-access/sharpapi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sharpapi-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/sharpapi/plans/sharpapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sharpapi-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/sharpapi/rules/sharpapi-rules.yml
  title: ''
  type: Spectral
  url: rules/sharpapi-rules.yml
- group: design
  href: https://artifacts.apis.io/sharpapi/json-ld/sharpapi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sharpapi-context.jsonld
- group: design
  href: https://artifacts.apis.io/sharpapi/vocabulary/sharpapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sharpapi-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/sharpapi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/sharpapi/data-model/sharpapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sharpapi-data-model.yml
- group: design
  href: https://artifacts.apis.io/sharpapi/conventions/sharpapi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sharpapi-conventions.yml
- group: auth
  href: https://artifacts.apis.io/sharpapi/authentication/sharpapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sharpapi-authentication.yml
- group: design
  href: https://artifacts.apis.io/sharpapi/errors/sharpapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sharpapi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sharpapi/conformance/sharpapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sharpapi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sharpapi/llms/sharpapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sharpapi-llms.txt
- group: other
  href: https://artifacts.apis.io/sharpapi/hosts/sharpapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sharpapi-hosts.yml
- group: other
  href: https://artifacts.apis.io/sharpapi/vendors/sharpapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sharpapi-vendors.yml
- group: build
  href: https://artifacts.apis.io/sharpapi/packages/sharpapi-packages.yml
  title: ''
  type: SDKs
  url: packages/sharpapi-packages.yml
- group: build
  href: https://artifacts.apis.io/sharpapi/packages/sharpapi-packages.yml
  title: ''
  type: Packages
  url: packages/sharpapi-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sharpapi.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sharpapi.io/privacy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sharpapi.io\\\
- group: auth
  href: https://artifacts.apis.io/sharpapi/security/sharpapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sharpapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sharpapi.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sharpapi.io
- group: commercial
  title: ''
  type: Pricing
  url: https://sharpapi.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://sharpapi.io/sign-up
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sharpapi.io/en/api-reference/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sharpapi.io/en/quickstart/
- group: other
  title: ''
  type: Image
  url: https://sharpapi.io/favicon.ico
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sharp-API
created: '2026-10-14'
description: SharpAPI provides real-time sports betting odds with built-in expected value (EV) and arbitrage data across major US sportsbooks. Their API delivers over 47 million odds daily, supporting multiple sports and leagues, and offers free tier access for developers to integrate betting data, odds comparison, and EV calculations into applications.
finops:
- has_sources: true
  method: derived
  name: Sharpapi Finops
  primary_unit: seat
  service_category: ''
  slug: sharpapi-finops
  template: false
image: https://sharpapi.io/og-image.png
json_schemas:
- name: EventGameState
  property_count: 40
  slug: sharpapi-event-game-state
- name: EVOpportunity
  property_count: 38
  slug: sharpapi-evopportunity
- name: MiddleOpportunity
  property_count: 36
  slug: sharpapi-middle-opportunity
- name: Odds
  property_count: 39
  slug: sharpapi-odds
- name: SplitsGame
  property_count: 11
  slug: sharpapi-splits-game
- name: StoreReadiness
  property_count: 7
  slug: sharpapi-store-readiness
jsonld:
- class_count: 30
  name: Sharpapi Context
  property_count: 192
  slug: sharpapi-context
layout: provider
modified: '2026-10-14'
name: SharpAPI
nav: Providers
network: true
overview: 'SharpAPI publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Betting Splits API, Deep Links API, and 8 more. Tagged areas include Company, Sports Betting, Real-Time Data, and Gambling.


  The SharpAPI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SharpAPI''s developer surface includes authentication, documentation, pricing, signup flow, API reference, getting-started guide, and 23 more developer resources.'
plans:
- name: Sharpapi Plans Pricing
  plan_count: 5
  slug: sharpapi-plans-pricing
- name: Sharpapi Price Estimates
  plan_count: 0
  slug: sharpapi-price-estimates
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: SharpAPI API Rules
  rule_count: 17
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 4
  slug: sharpapi-rules
score:
  band: developing
  composite: 46.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 61.8
    contract_governance: 22.0
    contract_quality: 65.8
    developer_ergonomics: 39.9
    discoverability: 64.3
    operational_transparency: 2.6
  previous_composite: 55.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sharpapi/sharpapi-2026-11-03T143110.png
security:
- kind: authentication
  name: Sharpapi Authentication
  slug: sharpapi-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Sharpapi Domain Security
  slug: sharpapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: sharpapi-compare-odds
  slug: sharpapi-compare-odds
- name: sharpapi-manage-api-keys
  slug: sharpapi-manage-api-keys
slug: sharpapi
tags:
- Company
- Sports Betting
- Real-Time Data
- Gambling
website: https://sharpapi.io
---
