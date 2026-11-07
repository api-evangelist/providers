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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: derived
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
  score: 43.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Scheduling, availability and bookings for the 42min platform.
  name: 42min API
  slug: 42min-api
- baseURL: https://api.42min.us
  baseurl_source: declared
  description: The 42min public REST API.
  name: 42min API API
  slug: 42min-api-api
artifact_total: 15
asyncapis:
- description: ''
  name: 42Min Us Webhooks
  slug: 42min-us-webhooks
common:
- group: design
  href: https://artifacts.apis.io/42min-us/rules/42min-us-rules.yml
  title: ''
  type: Spectral
  url: rules/42min-us-rules.yml
- group: design
  href: https://artifacts.apis.io/42min-us/json-ld/42min-us-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/42min-us-context.jsonld
- group: design
  href: https://artifacts.apis.io/42min-us/vocabulary/42min-us-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/42min-us-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/42min-us/conventions/42min-us-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/42min-us-conventions.yml
- group: design
  href: https://artifacts.apis.io/42min-us/conventions/42min-us-conventions.yml
  title: ''
  type: Conventions
  url: conventions/42min-us-conventions.yml
- group: design
  href: https://artifacts.apis.io/42min-us/conformance/42min-us-conformance.yml
  title: ''
  type: Conformance
  url: conformance/42min-us-conformance.yml
- group: operate
  href: https://artifacts.apis.io/42min-us/rate-limits/42min-us-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/42min-us-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/42min-us/plans/42min-us-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/42min-us-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/42min-us/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/42min-us/asyncapi/42min-us-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/42min-us-webhooks.yml
- group: design
  href: https://artifacts.apis.io/42min-us/data-model/42min-us-data-model.yml
  title: ''
  type: DataModel
  url: data-model/42min-us-data-model.yml
- group: operate
  href: https://artifacts.apis.io/42min-us/changelog/42min-us-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/42min-us-changelog.yml
- group: auth
  href: https://artifacts.apis.io/42min-us/authentication/42min-us-authentication.yml
  title: ''
  type: Authentication
  url: authentication/42min-us-authentication.yml
- group: design
  href: https://artifacts.apis.io/42min-us/errors/42min-us-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/42min-us-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/42min-us/llms/42min-us-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/42min-us-llms.txt
- group: agent
  href: https://artifacts.apis.io/42min-us/well-known/42min-us-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/42min-us-well-known.yml
- group: other
  href: https://artifacts.apis.io/42min-us/hosts/42min-us-hosts.yml
  title: ''
  type: Hosts
  url: hosts/42min-us-hosts.yml
- group: other
  href: https://artifacts.apis.io/42min-us/vendors/42min-us-vendors.yml
  title: ''
  type: Vendors
  url: vendors/42min-us-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://42min.us/help/api/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://42min.us/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://42min.us/help
- group: start
  title: ''
  type: SignUp
  url: https://42min.us/360/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://42min.us/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://42min.us/news
- group: operate
  title: ''
  type: ChangeLog
  url: https://42min.us/news/changelog
- group: company
  title: ''
  type: Blog
  url: https://42min.us/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://42min.us/help/getting-started/what-is-42min
- group: docs
  title: ''
  type: APIReference
  url: https://42min.us/help/api/llms-full.txt
- group: auth
  href: https://artifacts.apis.io/42min-us/security/42min-us-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/42min-us-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://42min.us/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.42min.us/openapi.yaml
  - status: 401
    url: https://api.42min.us/mcp
  - status: 200
    url: https://42min.us/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: 42min offers a free, highly customizable meeting scheduling platform featuring routing forms, automations, round‑robin scheduling, meeting polls, team management, and a robust API with webhooks in 14 programming languages. It enables businesses to streamline appointment booking, integrate with CRM systems, and automate workflows without cost.
image: https://42min.us/og/cover.png
json_schemas:
- name: Booking
  property_count: 27
  slug: 42min-us-booking
- name: CreateBookingRequest
  property_count: 12
  slug: 42min-us-create-booking-request
- name: CreateSeriesRequest
  property_count: 14
  slug: 42min-us-create-series-request
- name: EventTypeDetail
  property_count: 26
  slug: 42min-us-event-type-detail
- name: SeriesActionResult
  property_count: 9
  slug: 42min-us-series-action-result
- name: Series
  property_count: 19
  slug: 42min-us-series
jsonld:
- class_count: 24
  name: 42Min Us Context
  property_count: 115
  slug: 42min-us-context
layout: provider
modified: '2026-10-31'
name: 42min
nav: Providers
network: true
overview: '42min publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Scheduling, Free, Webhook, and Automation.


  The 42min catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  42min''s developer surface includes changelog, authentication, support, signup flow, pricing, engineering blog, getting-started guide, and 23 more developer resources.'
plans:
- name: 42Min Us Plans Pricing
  plan_count: 2
  slug: 42min-us-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 8
  name: 42Min Us Rate Limits
  slug: 42min-us-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: 42min API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 1
  slug: 42min-us-rules
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 38.2
    contract_governance: 22.0
    contract_quality: 60.4
    developer_ergonomics: 31.4
    discoverability: 58.0
    operational_transparency: 43.4
  previous_composite: 52.5
  provenance:
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 42Min Us Authentication
  slug: 42min-us-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: 42Min Us Domain Security
  slug: 42min-us-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 42min-us
tags:
- Scheduling
- Free
- Webhook
- Automation
website: https://42min.us/
---
