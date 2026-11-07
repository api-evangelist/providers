---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
artifact_total: 1
common:
- group: design
  href: https://artifacts.apis.io/worlddataapi/vocabulary/worlddataapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/worlddataapi-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/worlddataapi/conventions/worlddataapi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/worlddataapi-conventions.yml
- group: design
  href: https://artifacts.apis.io/worlddataapi/conformance/worlddataapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/worlddataapi-conformance.yml
- group: other
  href: https://artifacts.apis.io/worlddataapi/hosts/worlddataapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/worlddataapi-hosts.yml
- group: auth
  href: https://artifacts.apis.io/worlddataapi/security/worlddataapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/worlddataapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://worlddataapi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.worlddataapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://worlddataapi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://worlddataapi.com/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://worlddataapi.com/docs/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://worlddataapi.com/auth/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://worlddataapi.com/about/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://worlddataapi.com/about/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://worlddataapi.com/auth/login
coverage:
  checked: '2026-10-19'
  detail: Documentation pages are HTML only and no OpenAPI, GraphQL, or other machine-readable contract was found.
  evidence:
  - status: 200
    url: https://worlddataapi.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: World Data API provides a comprehensive suite of global data endpoints covering countries, regions, cities, currencies, languages, timezones, airports, airlines, holidays, and premium astronomy, business days, and travel data. The platform offers RESTful JSON APIs with extensive documentation, quickstart guides, authentication via API keys, and a developer portal for testing. It serves developers, businesses, and researchers needing reliable geographic and temporal data for applications, analytics, and integration.
image: https://worlddataapi.com/og/landing.png
layout: provider
modified: '2026-10-19'
name: World Data API
nav: Providers
network: true
overview: 'World Data API publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Geography, and Travel.


  World Data API''s developer surface includes documentation, API reference, getting-started guide, signup flow, and 10 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 23.3
    catalog_earned_first_party: 0.0
    catalog_gap: 91.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 17.1
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 39.3
    operational_transparency: 0.0
  previous_composite: 19.9
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/worlddataapi/worlddataapi-2026-11-03T150246.png
security:
- kind: domain-security
  name: Worlddataapi Domain Security
  slug: worlddataapi-domain-security
  summary_line: TLSv1.3
slug: worlddataapi
tags:
- Company
- Data
- Geography
- Travel
website: https://worlddataapi.com/
---
