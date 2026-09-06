---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.5
  scored_at: '2026-09-05'
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
  baseurl_source: declared
  description: Public REST API to create and retrieve Pokémon Showdown team links, generate random teams, and access sample teams and authenticated Showdown helpers.
  name: crob.at REST API
  slug: crobat-rest-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crob-at-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/crob-at-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/crob-at-rate-limits.yml
- group: auth
  title: ''
  type: Security
  url: https://crob.at/api#security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crob-at-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/crob-at-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/crob-at-api-catalog.json
- group: start
  title: ''
  type: APIOnboarding
  url: well-known/crob-at-api-onboarding.json
- group: other
  title: ''
  type: ContentSignal
  url: well-known/crob-at-robots.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crob-at-llms.txt
- group: design
  title: ''
  type: SpectralRules
  url: rules/crob-at-spectral.yaml
- group: design
  title: ''
  type: Conventions
  url: conventions/crob-at-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/crob-at-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/crob-at-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/crob-at-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/crob-at-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/crob-at-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/crob-at-rest-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/crob-at-agentic-access.yml
created: '2026-07-20'
description: Free, no-login web tool for sharing Pokémon Showdown teams as visual pages, with an anonymous keyless public REST API for creating and retrieving team links, generating usage-weighted random teams, and fetching Smogon sample teams and Pokémon type reference data. Publishes an OpenAPI 3.1 contract, APIs.json, an RFC 9727 api-catalog, llms.txt, and markdown twins of every team page for AI agents.
layout: provider
modified: '2026-09-03'
name: crob.at
nav: Providers
network: true
overview: 'crob.at publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Gaming, Esports, Pokemon, Pokemon Showdown, and Team Building.


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
- effective_rule_count: 41
  extends:
  - spectral:oas
  name: crob.at API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: crob-at-spectral
score:
  band: developing
  composite: 52.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 33.3
    contract_quality: 55.8
    developer_ergonomics: 44.6
    discoverability: 72.2
    governance: 33.3
    operational_transparency: 42.1
  previous_composite: 52.7
  provenance:
    agentic_access: derived
    conformance: first-party
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
screenshot: https://raw.githubusercontent.com/api-evangelist/crob-at/refs/heads/main/screenshots/crob-at-2026-07-25T210738.png
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
