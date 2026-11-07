---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: true
  try_now: true
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
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Swathapi Com Agentic Access
  operation_count: 16
  slug: swathapi-com-agentic-access
  summary_line: 16 operations · 5 acting
api_count: 1
apis:
- baseURL: https://swathapi.com
  baseurl_source: declared
  description: The Billing API from swathapi-com — 1 operation(s) for billing.
  name: swathapi-com Billing API
  slug: swathapi-com-billing-api
- baseURL: https://swathapi.com
  baseurl_source: declared
  description: The Monitors API from swathapi-com — 1 operation(s) for monitors.
  name: swathapi-com Monitors API
  slug: swathapi-com-monitors-api
- baseURL: https://swathapi.com
  baseurl_source: declared
  description: The Property API from swathapi-com — 1 operation(s) for property.
  name: swathapi-com Property API
  slug: swathapi-com-property-api
- baseURL: https://swathapi.com
  baseurl_source: declared
  description: The Signup API from swathapi-com — 1 operation(s) for signup.
  name: swathapi-com Signup API
  slug: swathapi-com-signup-api
- baseURL: https://swathapi.com
  baseurl_source: declared
  description: The Storms API from swathapi-com — 3 operation(s) for storms.
  name: swathapi-com Storms API
  slug: swathapi-com-storms-api
- baseURL: https://swathapi.com
  baseurl_source: declared
  description: The Swaths API from swathapi-com — 6 operation(s) for swaths.
  name: swathapi-com Swaths API
  slug: swathapi-com-swaths-api
- baseURL: https://swathapi.com
  baseurl_source: declared
  description: The Usage API from swathapi-com — 1 operation(s) for usage.
  name: swathapi-com Usage API
  slug: swathapi-com-usage-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/swathapi-com/agentic-access/swathapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/swathapi-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/swathapi-com/rate-limits/swathapi-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/swathapi-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/swathapi-com/plans/swathapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/swathapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/swathapi-com/rules/swathapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/swathapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/swathapi-com/json-ld/swathapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/swathapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/swathapi-com/vocabulary/swathapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/swathapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/swathapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/swathapi-com/data-model/swathapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/swathapi-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/swathapi-com/authentication/swathapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/swathapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/swathapi-com/errors/swathapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/swathapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/swathapi-com/conformance/swathapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/swathapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/swathapi-com/well-known/swathapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/swathapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/swathapi-com/hosts/swathapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/swathapi-com-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://swathapi.com/status
- group: auth
  href: https://artifacts.apis.io/swathapi-com/security/swathapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/swathapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://swathapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://swathapi.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://swathapi.com/for/developers
- group: docs
  title: ''
  type: APIReference
  url: https://swathapi.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://swathapi.com/guide
- group: operate
  title: ''
  type: Support
  url: https://swathapi.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://swathapi.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://swathapi.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://swathapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://swathapi.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://swathapi.com/openapi.json
  - status: 401
    url: https://swathapi.com/mcp
  - status: 200
    url: https://swathapi.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Swath API provides AI‑native storm intelligence by verifying hail and damaging wind events against NOAA radar and NWS storm reports. It offers a REST API that returns every affected property, enriched with parcel data, and can fire webhooks when storms cross a defined area. Free API keys are issued in seconds, and developers can explore the service via comprehensive documentation, a developer portal, and example guides.
image: https://swathapi.com/icon-512.png
json_schemas:
- name: Monitor
  property_count: 8
  slug: swathapi-com-monitor
- name: Property
  property_count: 19
  slug: swathapi-com-property
- name: ReportQuote
  property_count: 6
  slug: swathapi-com-report-quote
- name: StormSwath
  property_count: 11
  slug: swathapi-com-storm-swath
- name: SwathDetail
  property_count: 12
  slug: swathapi-com-swath-detail
- name: SwathReport
  property_count: 11
  slug: swathapi-com-swath-report
jsonld:
- class_count: 14
  name: Swathapi Com Context
  property_count: 71
  slug: swathapi-com-context
layout: provider
modified: '2026-10-31'
name: swathapi-com
nav: Providers
network: true
overview: 'swathapi-com publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Billing API, Monitors API, Property API, and 4 more. Tagged areas include Company, Weather, Storm, Artificial Intelligence, and NOAA.


  The swathapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  swathapi-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 18 more developer resources.'
plans:
- name: Swathapi Com Plans Pricing
  plan_count: 4
  slug: swathapi-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 3
  name: Swathapi Com Rate Limits
  slug: swathapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: swathapi-com API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: swathapi-com-rules
scopes:
- name: Swathapi Com Scopes
  scope_count: 0
  slug: swathapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.7
  coverage:
    artifact_dirs: 31
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.3
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 62.5
    developer_ergonomics: 39.8
    discoverability: 66.1
    operational_transparency: 39.5
  previous_composite: 61.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/swathapi-com/swathapi-com-2026-11-03T144143.png
security:
- kind: authentication
  name: Swathapi Com Authentication
  slug: swathapi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Swathapi Com Domain Security
  slug: swathapi-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 4
skills:
- name: create-account
  slug: swathapi-com-create-account-skill
- name: find-storms
  slug: swathapi-com-find-storms-skill
- name: get-swath-report
  slug: swathapi-com-get-swath-report-skill
- name: storms-at-point
  slug: swathapi-com-storms-at-point-skill
slug: swathapi-com
tags:
- Company
- Weather
- Storm
- Artificial Intelligence
- NOAA
website: https://swathapi.com/
---
