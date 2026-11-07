---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.4
  scored_at: '2026-11-06'
api_count: 23
apis:
- description: Public API providing workforce management data such as audits, budgets, and authentication.
  name: Rotageek Public API
  slug: rotageek-public-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: The Auth API from Rotageek — 1 operation(s) for auth.
  name: Rotageek Auth API
  slug: rotageek-auth-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: The Rotageek API API from Rotageek — 1 operation(s) for rotageek api.
  name: Rotageek Rotageek API
  slug: rotageek-rotageek-api-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: The Schedule API from Rotageek — 2 operation(s) for schedule.
  name: Rotageek Schedule API
  slug: rotageek-schedule-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: The Audits API from Rotageek — 1 operation(s) for audits.
  name: Rotageek Audits API
  slug: rotageek-audits-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: The Budget API from Rotageek — 1 operation(s) for budget.
  name: Rotageek Budget API
  slug: rotageek-budget-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: The ContractTypes API from Rotageek — 1 operation(s) for contracttypes.
  name: Rotageek Contract Types API
  slug: rotageek-contracttypes-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: The Demand API from Rotageek — 2 operation(s) for demand.
  name: Rotageek Demand API
  slug: rotageek-demand-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: The Gaps API from Rotageek — 3 operation(s) for gaps.
  name: Rotageek Gaps API
  slug: rotageek-gaps-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: Holiday entitlement endpoints. The {userId} route parameter is the employee's external identifier.
  name: Rotageek Leave API
  slug: rotageek-leave-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: The Locations API from Rotageek — 3 operation(s) for locations.
  name: Rotageek Locations API
  slug: rotageek-locations-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: The Other API from Rotageek — 2 operation(s) for other.
  name: Rotageek Other API
  slug: rotageek-other-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: The Positions API from Rotageek — 2 operation(s) for positions.
  name: Rotageek Positions API
  slug: rotageek-positions-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: The SalesTotal API from Rotageek — 1 operation(s) for salestotal.
  name: Rotageek Sales Total API
  slug: rotageek-salestotal-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: The Tasks API from Rotageek — 2 operation(s) for tasks.
  name: Rotageek Tasks API
  slug: rotageek-tasks-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: The Timesheets API from Rotageek — 1 operation(s) for timesheets.
  name: Rotageek Timesheets API
  slug: rotageek-timesheets-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: The UserAvailability API from Rotageek — 1 operation(s) for useravailability.
  name: Rotageek User Availability API
  slug: rotageek-useravailability-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: The UserClassifications API from Rotageek — 2 operation(s) for userclassifications.
  name: Rotageek User Classifications API
  slug: rotageek-userclassifications-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: The UserConfigurableFields API from Rotageek — 2 operation(s) for userconfigurablefields.
  name: Rotageek User Configurable Fields API
  slug: rotageek-userconfigurablefields-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: The UserEmployeeTypes API from Rotageek — 2 operation(s) for useremployeetypes.
  name: Rotageek User Employee Types API
  slug: rotageek-useremployeetypes-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: The Version API from Rotageek — 1 operation(s) for version.
  name: Rotageek Version API
  slug: rotageek-version-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: The VisaTypes API from Rotageek — 3 operation(s) for visatypes.
  name: Rotageek Visa Types API
  slug: rotageek-visatypes-api
- baseURL: https://publicapi.rotageek.com
  baseurl_source: declared
  description: The WebhooksConsumer API from Rotageek — 1 operation(s) for webhooksconsumer.
  name: Rotageek Webhooks Consumer API
  slug: rotageek-webhooksconsumer-api
artifact_total: 32
asyncapis:
- description: ''
  name: Rotageek Webhooks
  slug: rotageek-webhooks
common:
- group: design
  href: https://artifacts.apis.io/rotageek/rules/rotageek-rules.yml
  title: ''
  type: Spectral
  url: rules/rotageek-rules.yml
- group: design
  href: https://artifacts.apis.io/rotageek/json-ld/rotageek-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/rotageek-context.jsonld
- group: design
  href: https://artifacts.apis.io/rotageek/vocabulary/rotageek-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rotageek-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/rotageek/asyncapi/rotageek-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/rotageek-webhooks.yml
- group: design
  href: https://artifacts.apis.io/rotageek/data-model/rotageek-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rotageek-data-model.yml
- group: operate
  href: https://artifacts.apis.io/rotageek/changelog/rotageek-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/rotageek-changelog.yml
- group: auth
  href: https://artifacts.apis.io/rotageek/authentication/rotageek-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rotageek-authentication.yml
- group: design
  href: https://artifacts.apis.io/rotageek/conformance/rotageek-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rotageek-conformance.yml
- group: agent
  href: https://artifacts.apis.io/rotageek/llms/rotageek-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rotageek-llms.txt
- group: auth
  href: https://artifacts.apis.io/rotageek/well-known/rotageek-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/rotageek-support-security.txt
- group: auth
  href: https://artifacts.apis.io/rotageek/well-known/rotageek-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/rotageek-status-security.txt
- group: agent
  href: https://artifacts.apis.io/rotageek/well-known/rotageek-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rotageek-well-known.yml
- group: other
  href: https://artifacts.apis.io/rotageek/hosts/rotageek-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rotageek-hosts.yml
- group: other
  href: https://artifacts.apis.io/rotageek/vendors/rotageek-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rotageek-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rotageek.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rotageek.com/privacy-policy
- group: other
  title: ''
  type: Leadership
  url: https://www.rotageek.com/team
- group: start
  title: ''
  type: GettingStarted
  url: https://support.rotageek.com/en/articles/11513847-public-api-getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RotaGeek
- group: auth
  href: https://artifacts.apis.io/rotageek/security/rotageek-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rotageek-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rotageek.com
- group: company
  title: ''
  type: Blog
  url: https://www.rotageek.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.rotageek.com/support
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://www.rotageek.com/mcp
  - status: 200
    url: https://www.rotageek.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Rotageek provides workforce management and scheduling solutions, offering digital rota planning, staff forecasting, labour modelling, auto‑scheduling, AI insights and HR integration. Their platform helps businesses optimise staff rotas, predict demand spikes, and improve employee engagement through a suite of cloud‑based tools.
image: https://www.rotageek.com/hubfs/Homepage%20meta.png
json_schemas:
- name: GetApiV1ScheduleLocationsLocationidResponse
  property_count: 29
  slug: rotageek-get-api-v1-schedule-locations-locationid-response
- name: GetApiV1ScheduleUsersUseridResponse
  property_count: 29
  slug: rotageek-get-api-v1-schedule-users-userid-response
- name: PostApiV1AuthRequest
  property_count: 4
  slug: rotageek-post-api-v1-auth-request
- name: PostApiV1AuthResponse
  property_count: 4
  slug: rotageek-post-api-v1-auth-response
jsonld:
- class_count: 4
  name: Rotageek Context
  property_count: 13
  slug: rotageek-context
layout: provider
modified: '2026-10-13'
name: Rotageek
nav: Providers
network: true
overview: 'Rotageek is listed with 23 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Rotageek API, Schedule API, and 20 more. Tagged areas include Company, Workforce Management, Scheduling, AI Insights, and HR Integration.


  The Rotageek catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Rotageek''s developer surface includes changelog, authentication, getting-started guide, engineering blog, support, and 18 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Rotageek API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: rotageek-rules
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 55.1
    developer_ergonomics: 21.4
    discoverability: 79.5
    operational_transparency: 44.7
  previous_composite: 46.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 17.4
      total: 23
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/rotageek/rotageek-2026-11-03T142413.png
security:
- kind: authentication
  name: Rotageek Authentication
  slug: rotageek-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Rotageek Domain Security
  slug: rotageek-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rotageek
tags:
- Company
- Workforce Management
- Scheduling
- AI Insights
- HR Integration
website: https://www.rotageek.com
---
