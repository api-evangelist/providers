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
    agent_skills: unknown
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.weatherai.io
  baseurl_source: declared
  description: weatherAI.io Decision API provides weather-based decision making with verdict, score, optimal time windows, and risk assessments.
  name: Decision API
  slug: decision-api
artifact_total: 15
common:
- group: docs
  title: ''
  type: Documentation
  url: https://www.weatherai.io/docs
- group: operate
  href: https://artifacts.apis.io/weatherai-io/rate-limits/weatherai-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/weatherai-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/weatherai-io/plans/weatherai-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/weatherai-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/weatherai-io/json-ld/weatherai-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/weatherai-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/weatherai-io/vocabulary/weatherai-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/weatherai-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/weatherai-io/data-model/weatherai-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/weatherai-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/weatherai-io/components/weatherai-io-components.yml
  title: ''
  type: Components
  url: components/weatherai-io-components.yml
- group: operate
  href: https://artifacts.apis.io/weatherai-io/changelog/weatherai-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/weatherai-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/weatherai-io/conventions/weatherai-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/weatherai-io-conventions.yml
- group: auth
  href: https://artifacts.apis.io/weatherai-io/authentication/weatherai-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/weatherai-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/weatherai-io/lifecycle/weatherai-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/weatherai-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/weatherai-io/errors/weatherai-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/weatherai-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/weatherai-io/conformance/weatherai-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/weatherai-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/weatherai-io/llms/weatherai-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/weatherai-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/weatherai-io/well-known/weatherai-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/weatherai-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/weatherai-io/hosts/weatherai-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/weatherai-io-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.weatherai.io/terms
- group: operate
  title: ''
  type: Support
  url: https://www.weatherai.io/support
- group: operate
  title: ''
  type: StatusPage
  url: https://www.weatherai.io/status
- group: start
  title: ''
  type: Sandbox
  url: https://www.weatherai.io/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.weatherai.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.weatherai.io/pricing
- group: start
  title: ''
  type: Login
  url: https://www.weatherai.io/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.weatherai.io/changelog
- group: auth
  href: https://artifacts.apis.io/weatherai-io/security/weatherai-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/weatherai-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://weatherai.io/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.weatherai.io/openapi.json
  - status: 401
    url: https://api.weatherai.io/mcp
  - status: 200
    url: https://weatherai.io/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: weatherAI.io provides a decision‑making weather API that returns a single verdict, a confidence score, optimal time windows and risk assessments for a wide range of outdoor activities such as hiking, construction, agriculture, drone flights and events. By supplying location, date and activity type, developers and AI agents receive concise guidance on whether to proceed, the best hours to act, and any weather‑related constraints. The service includes a free tier of 1,000 calls per month, detailed documentation, an MCP server for AI integration, and industry‑specific packs.
image: https://www.weatherai.io/img/og-image.png
json_schemas:
- name: AlertInput
  property_count: 9
  slug: weatherai-io-alert-input
- name: Alert
  property_count: 19
  slug: weatherai-io-alert
- name: BestDay
  property_count: 7
  slug: weatherai-io-best-day
- name: Decision
  property_count: 11
  slug: weatherai-io-decision
- name: ProfileInput
  property_count: 6
  slug: weatherai-io-profile-input
- name: Widget
  property_count: 9
  slug: weatherai-io-widget
jsonld:
- class_count: 8
  name: Weatherai Io Context
  property_count: 29
  slug: weatherai-io-context
layout: provider
modified: '2026-10-31'
name: weatherAI.io
nav: Providers
network: true
overview: 'weatherAI.io publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Decision API. Tagged areas include Weather, Artificial Intelligence, Decisions, and Forecast.


  The weatherAI.io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  weatherAI.io''s developer surface includes documentation, changelog, authentication, support, sandbox, pricing, and 20 more developer resources.'
plans:
- name: Weatherai Io Plans Pricing
  plan_count: 6
  slug: weatherai-io-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Weatherai Io Rate Limits
  slug: weatherai-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: weatherAI.io API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 2
  slug: weatherai-io-rules
scopes:
- name: Weatherai Io Scopes
  scope_count: 0
  slug: weatherai-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.4
  coverage:
    artifact_dirs: 28
    catalog_earned: 68.8
    catalog_earned_first_party: 20.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.1
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 47.9
    developer_ergonomics: 22.6
    discoverability: 57.1
    operational_transparency: 36.8
  previous_composite: 52.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
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
security:
- kind: authentication
  name: Weatherai Io Authentication
  slug: weatherai-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Weatherai Io Domain Security
  slug: weatherai-io-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: get-usage
  slug: weatherai-io-get_usage
slug: weatherai-io
tags:
- Weather
- Artificial Intelligence
- Decisions
- Forecast
website: https://weatherai.io/
---
