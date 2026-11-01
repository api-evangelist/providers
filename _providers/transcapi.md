---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Transcapi Agentic Access
  operation_count: 28
  slug: transcapi-agentic-access
  summary_line: 28 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.transcapi.com
  baseurl_source: declared
  description: The Airports API from TransCAPI — 2 operation(s) for airports.
  name: TransCAPI Airports API
  slug: transcapi-airports-api
- baseURL: https://api.transcapi.com
  baseurl_source: declared
  description: The Alerts API from TransCAPI — 3 operation(s) for alerts.
  name: TransCAPI Alerts API
  slug: transcapi-alerts-api
- baseURL: https://api.transcapi.com
  baseurl_source: declared
  description: The Bus API from TransCAPI — 9 operation(s) for bus.
  name: TransCAPI Bus API
  slug: transcapi-bus-api
- baseURL: https://api.transcapi.com
  baseurl_source: declared
  description: The Disruptions API from TransCAPI — 1 operation(s) for disruptions.
  name: TransCAPI Disruptions API
  slug: transcapi-disruptions-api
- baseURL: https://api.transcapi.com
  baseurl_source: declared
  description: The Journey API from TransCAPI — 3 operation(s) for journey.
  name: TransCAPI Journey API
  slug: transcapi-journey-api
- baseURL: https://api.transcapi.com
  baseurl_source: declared
  description: The Places API from TransCAPI — 1 operation(s) for places.
  name: TransCAPI Places API
  slug: transcapi-places-api
- baseURL: https://api.transcapi.com
  baseurl_source: declared
  description: The Rail API from TransCAPI — 7 operation(s) for rail.
  name: TransCAPI Rail API
  slug: transcapi-rail-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/transcapi/agentic-access/transcapi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/transcapi-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/transcapi/rate-limits/transcapi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/transcapi-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/transcapi/plans/transcapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/transcapi-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/transcapi/rules/transcapi-rules.yml
  title: ''
  type: Spectral
  url: rules/transcapi-rules.yml
- group: design
  href: https://artifacts.apis.io/transcapi/vocabulary/transcapi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/transcapi-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/transcapi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/transcapi/changelog/transcapi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/transcapi-changelog.yml
- group: design
  href: https://artifacts.apis.io/transcapi/conventions/transcapi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/transcapi-conventions.yml
- group: auth
  href: https://artifacts.apis.io/transcapi/authentication/transcapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/transcapi-authentication.yml
- group: design
  href: https://artifacts.apis.io/transcapi/errors/transcapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/transcapi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/transcapi/conformance/transcapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/transcapi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/transcapi/llms/transcapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/transcapi-llms.txt
- group: other
  href: https://artifacts.apis.io/transcapi/hosts/transcapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/transcapi-hosts.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.transcapi.com/docs/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.transcapi.com`
- group: auth
  href: https://artifacts.apis.io/transcapi/security/transcapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/transcapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.transcapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.transcapi.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.transcapi.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://www.transcapi.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.transcapi.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.transcapi.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tcdataconsultants
- group: commercial
  title: ''
  type: Pricing
  url: https://www.transcapi.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.transcapi.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.transcapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.transcapi.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.transcapi.com/static/transcapi.postman_collection.json
created: '2026-10-30'
description: TransCAPI provides a public transport API covering the United Kingdom and Ireland, with extensions to the Netherlands and Belgium. It offers live bus and train timetables, journey planning, rail fare data, disruption alerts, bus punctuality metrics, reachability maps, and webhook notifications. The service includes a free tier of 100 requests per day and paid plans for higher volume.
image: https://www.transcapi.com/static/img/favicon.ico
layout: provider
modified: '2026-10-30'
name: TransCAPI
nav: Providers
network: true
overview: 'TransCAPI publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Airports API, Alerts API, Bus API, and 4 more. Tagged areas include Company, Transport, API, UK, and Ireland.


  The TransCAPI catalog on APIs.io includes 1 Spectral governance ruleset.


  TransCAPI''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 21 more developer resources.'
plans:
- name: Transcapi Plans Pricing
  plan_count: 4
  slug: transcapi-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 8
  name: Transcapi Rate Limits
  slug: transcapi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: TransCAPI API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: transcapi-rules
scopes:
- name: Transcapi Scopes
  scope_count: 0
  slug: transcapi-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 64.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 79.3
    catalog_earned_first_party: 0.0
    catalog_gap: 35.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 42.2
    developer_ergonomics: 68.3
    discoverability: 66.1
    operational_transparency: 49.5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Transcapi Authentication
  slug: transcapi-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Transcapi Domain Security
  slug: transcapi-domain-security
  summary_line: TLSv1.3 · DMARC
slug: transcapi
tags:
- Company
- Transport
- API
- UK
- Ireland
website: https://www.transcapi.com/
---
