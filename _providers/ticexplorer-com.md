---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 1
  name: Ticexplorer Com Agentic Access
  operation_count: 21
  slug: ticexplorer-com-agentic-access
  summary_line: 21 operations · 6 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.ticexplorer.com
  baseurl_source: declared
  description: API key management (admin scope).
  name: ticexplorer-com Admin API
  slug: ticexplorer-com-admin-api
- baseURL: https://api.ticexplorer.com
  baseurl_source: declared
  description: 'Market analytics: rate distributions per insurer across all providers in an area (scoped, just-in-time, async jobs).'
  name: ticexplorer-com Analytics API
  slug: ticexplorer-com-analytics-api
- baseURL: https://api.ticexplorer.com
  baseurl_source: declared
  description: Price or reconcile a whole visit / bill.
  name: ticexplorer-com Claims API
  slug: ticexplorer-com-claims-api
- baseURL: https://api.ticexplorer.com
  baseurl_source: declared
  description: Services in words → billing codes + code facts.
  name: ticexplorer-com Codes API
  slug: ticexplorer-com-codes-api
- baseURL: https://api.ticexplorer.com
  baseurl_source: declared
  description: Domain guide and Arazzo workflows (no auth).
  name: ticexplorer-com Guide API
  slug: ticexplorer-com-guide-api
- baseURL: https://api.ticexplorer.com
  baseurl_source: declared
  description: Which plan (and rate files) applies to a person.
  name: ticexplorer-com Plans API
  slug: ticexplorer-com-plans-api
- baseURL: https://api.ticexplorer.com
  baseurl_source: declared
  description: Places and clinicians → billing entities (TINs).
  name: ticexplorer-com Providers API
  slug: ticexplorer-com-providers-api
- baseURL: https://api.ticexplorer.com
  baseurl_source: declared
  description: Self-describing negotiated rate rows.
  name: ticexplorer-com Rates API
  slug: ticexplorer-com-rates-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/ticexplorer-com/agentic-access/ticexplorer-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ticexplorer-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/ticexplorer-com/rules/ticexplorer-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ticexplorer-com-rules.yml
- group: design
  href: https://artifacts.apis.io/ticexplorer-com/json-ld/ticexplorer-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ticexplorer-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/ticexplorer-com/vocabulary/ticexplorer-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ticexplorer-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/ticexplorer-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ticexplorer-com/data-model/ticexplorer-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ticexplorer-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/ticexplorer-com/conventions/ticexplorer-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ticexplorer-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/ticexplorer-com/authentication/ticexplorer-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ticexplorer-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ticexplorer-com/scopes/ticexplorer-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/ticexplorer-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/ticexplorer-com/errors/ticexplorer-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ticexplorer-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ticexplorer-com/conformance/ticexplorer-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ticexplorer-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ticexplorer-com/well-known/ticexplorer-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ticexplorer-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/ticexplorer-com/hosts/ticexplorer-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ticexplorer-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/ticexplorer-com/security/ticexplorer-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ticexplorer-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ticexplorer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.ticexplorer.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.ticexplorer.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://api.ticexplorer.com/v1/guide
- group: company
  title: ''
  type: Blog
  url: https://ticexplorer.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://ticexplorer.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://ticexplorer.com/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ticexplorer.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ticexplorer.com/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.ticexplorer.com/openapi.json
  - status: 401
    url: https://api.ticexplorer.com/mcp
  - status: 200
    url: https://ticexplorer.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: TiC Explorer provides a health plan price transparency API that offers negotiated health-care prices from every US health plan’s price transparency files, including plans, providers and billing codes, accessible over REST and MCP. $5 free to start.
image: https://ticexplorer.com/opengraph-image
json_schemas:
- name: AnalyticsRequest
  property_count: 10
  slug: ticexplorer-com-analytics-request
- name: ClaimRequest
  property_count: 8
  slug: ticexplorer-com-claim-request
- name: ClaimResult
  property_count: 7
  slug: ticexplorer-com-claim-result
- name: ProvidersResult
  property_count: 8
  slug: ticexplorer-com-providers-result
- name: RatesRequest
  property_count: 8
  slug: ticexplorer-com-rates-request
- name: RatesResult
  property_count: 10
  slug: ticexplorer-com-rates-result
jsonld:
- class_count: 40
  name: Ticexplorer Com Context
  property_count: 145
  slug: ticexplorer-com-context
layout: provider
modified: '2026-10-31'
name: ticexplorer-com
nav: Providers
network: true
overview: 'ticexplorer-com publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Analytics API, Claims API, and 5 more. Tagged areas include Health, Finance, Transparency, and Healthcare.


  The ticexplorer-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ticexplorer-com''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 16 more developer resources.'
plans:
- name: Ticexplorer Com Plans Pricing
  plan_count: 0
  slug: ticexplorer-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Ticexplorer Com Rate Limits
  slug: ticexplorer-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: ticexplorer-com API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 1
  slug: ticexplorer-com-rules
scopes:
- name: Ticexplorer Com Scopes
  scope_count: 1
  slug: ticexplorer-com-scopes
  summary_line: 1 scope
score:
  band: thin
  composite: 38.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 22.4
    contract_governance: 35.6
    contract_quality: 59.1
    developer_ergonomics: 33.8
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 47.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 29.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ticexplorer-com/ticexplorer-com-2026-11-03T144716.png
security:
- kind: authentication
  name: Ticexplorer Com Authentication
  slug: ticexplorer-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ticexplorer Com Domain Security
  slug: ticexplorer-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: ticexplorer-com-codes-skill
  slug: ticexplorer-com-codes-skill
- name: ticexplorer-com-plans-skill
  slug: ticexplorer-com-plans-skill
- name: ticexplorer-com-providers-skill
  slug: ticexplorer-com-providers-skill
slug: ticexplorer-com
tags:
- Health
- Finance
- Transparency
- Healthcare
website: https://ticexplorer.com/
---
