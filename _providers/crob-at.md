---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Crob At Agentic Access
  operation_count: 10
  slug: crob-at-agentic-access
  summary_line: 10 operations · 2 acting
api_count: 1
apis:
- baseURL: https://crob.at
  baseurl_source: spec
  description: Optional same-origin helpers that use a crob.at browser session.
  name: crob.at Account API
  slug: crob-at-account-api
- baseURL: https://crob.at
  baseurl_source: spec
  description: Send product feedback to the crob.at team.
  name: crob.at Feedback API
  slug: crob-at-feedback-api
- baseURL: https://crob.at
  baseurl_source: spec
  description: Generate and optionally save competitive random teams.
  name: crob.at Generation API
  slug: crob-at-generation-api
- baseURL: https://crob.at
  baseurl_source: spec
  description: Read sample teams and Pokemon reference data.
  name: crob.at Reference API
  slug: crob-at-reference-api
- baseURL: https://crob.at
  baseurl_source: spec
  description: Create and retrieve shareable Pokemon Showdown teams.
  name: crob.at Teams API
  slug: crob-at-teams-api
artifact_total: 16
common:
- group: auth
  href: https://artifacts.apis.io/crob-at/security/crob-at-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crob-at-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/crob-at/authentication/crob-at-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crob-at-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://crob.at
- group: start
  title: ''
  type: Portal
  url: https://crob.at/api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crob.at/api#terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crob.at/privacy
- group: operate
  title: ''
  type: Support
  url: https://crob.at/contact
- group: start
  title: ''
  type: SignUp
  url: https://crob.at/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://crob.at/api#plans
- group: commercial
  href: https://artifacts.apis.io/crob-at/plans/crob-at-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crob-at-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/crob-at/rate-limits/crob-at-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/crob-at-rate-limits.yml
- group: auth
  title: ''
  type: Security
  url: https://crob.at/api#security
- group: auth
  href: https://artifacts.apis.io/crob-at/security/crob-at-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/crob-at-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/crob-at/well-known/crob-at-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crob-at-well-known.yml
- group: other
  href: https://artifacts.apis.io/crob-at/well-known/crob-at-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/crob-at-api-catalog.json
- group: start
  href: https://artifacts.apis.io/crob-at/well-known/crob-at-api-onboarding.json
  title: ''
  type: APIOnboarding
  url: well-known/crob-at-api-onboarding.json
- group: other
  href: https://artifacts.apis.io/crob-at/well-known/crob-at-robots.txt
  title: ''
  type: ContentSignal
  url: well-known/crob-at-robots.txt
- group: agent
  href: https://artifacts.apis.io/crob-at/llms/crob-at-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crob-at-llms.txt
- group: design
  href: https://artifacts.apis.io/crob-at/rules/crob-at-spectral.yaml
  title: ''
  type: SpectralRules
  url: rules/crob-at-spectral.yaml
- group: design
  href: https://artifacts.apis.io/crob-at/conventions/crob-at-conventions.yml
  title: ''
  type: Conventions
  url: conventions/crob-at-conventions.yml
- group: design
  href: https://artifacts.apis.io/crob-at/conventions/crob-at-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/crob-at-conventions.yml
- group: design
  href: https://artifacts.apis.io/crob-at/errors/crob-at-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/crob-at-problem-types.yml
- group: design
  href: https://artifacts.apis.io/crob-at/lifecycle/crob-at-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/crob-at-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/crob-at/conformance/crob-at-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crob-at-conformance.yml
- group: design
  href: https://artifacts.apis.io/crob-at/data-model/crob-at-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crob-at-data-model.yml
- group: other
  href: https://artifacts.apis.io/crob-at/overlays/crob-at-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/crob-at-rest-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/crob-at/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/crob-at/agentic-access/crob-at-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/crob-at-agentic-access.yml
created: '2026-07-20'
description: Free, no-login web tool for sharing Pokémon Showdown teams as visual pages, with an anonymous keyless public REST API for creating and retrieving team links, generating usage-weighted random teams, and fetching Smogon sample teams and Pokémon type reference data. Publishes an OpenAPI 3.1 contract, APIs.json, an RFC 9727 api-catalog, llms.txt, and markdown twins of every team page for AI agents.
finops:
- has_sources: true
  method: derived
  name: Crob At Finops
  primary_unit: ''
  service_category: ''
  slug: crob-at-finops
  template: true
layout: provider
modified: '2026-09-03'
name: crob.at
nav: Providers
network: true
overview: 'crob.at publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Feedback API, Generation API, and 2 more. Tagged areas include Gaming, Esports, Pokemon, Pokemon Showdown, and Team Building.


  The crob.at catalog on APIs.io includes 1 Spectral governance ruleset.


  crob.at''s developer surface includes authentication, developer portal, support, signup flow, pricing, and 23 more developer resources.'
plans:
- name: Crob At Plans Pricing
  plan_count: 1
  slug: crob-at-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Crob At Rate Limits
  slug: crob-at-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 41
  extends:
  - spectral:oas
  name: crob.at — spectral rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: crob-at-spectral
score:
  band: developing
  composite: 51.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 51.3
    catalog_earned_first_party: 20.0
    catalog_gap: 63.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 55.2
    developer_ergonomics: 44.6
    discoverability: 60.7
    operational_transparency: 42.1
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
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
screenshot: https://apis.io/screenshots/crob-at/crob-at-2026-07-25T210738.png
security:
- kind: authentication
  name: Crob At Authentication
  slug: crob-at-authentication
  summary_line: none/apiKey · 2 schemes
- kind: domain-security
  name: Crob At Domain Security
  slug: crob-at-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Crob At Vulnerability Disclosure
  slug: crob-at-vulnerability-disclosure
  summary_line: Hackerone
skill_count: 3
skills:
- name: Generate and save a random competitive team
  slug: crob-at-generate-random-team
- name: Look up sample teams and type data
  slug: crob-at-lookup-reference-data
- name: Share a Pokemon Showdown team as a visual page
  slug: crob-at-share-showdown-team
slug: crob-at
tags:
- Gaming
- Esports
- Pokemon
- Pokemon Showdown
- Team Building
- Content Rendering
- Developer Tools
- REST API
website: https://crob.at
---
