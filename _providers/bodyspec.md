---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.2
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Bodyspec Agentic Access
  operation_count: 45
  slug: bodyspec-agentic-access
  summary_line: 45 operations · 10 acting
api_count: 1
apis:
- baseURL: https://app.bodyspec.com
  baseurl_source: declared
  description: Health check and monitoring endpoints
  name: BodySpec API Status API
  slug: bodyspec-api-status-api
- baseURL: https://app.bodyspec.com
  baseurl_source: declared
  description: Appointments scheduling and management
  name: BodySpec Appointments API
  slug: bodyspec-appointments-api
- baseURL: https://app.bodyspec.com
  baseurl_source: declared
  description: Check appointment availability at locations
  name: BodySpec Availability API
  slug: bodyspec-availability-api
- baseURL: https://app.bodyspec.com
  baseurl_source: declared
  description: The BodySpec API API from BodySpec — 0 operation(s) for bodyspec api.
  name: BodySpec BodySpec API
  slug: bodyspec-bodyspec-api-api
- baseURL: https://app.bodyspec.com
  baseurl_source: declared
  description: Browse and search scan locations
  name: BodySpec Locations API
  slug: bodyspec-locations-api
- baseURL: https://app.bodyspec.com
  baseurl_source: declared
  description: Partner integration endpoints for user appointments
  name: BodySpec Partner Appointments API
  slug: bodyspec-partner-appointments-api
- baseURL: https://app.bodyspec.com
  baseurl_source: declared
  description: Partner integration endpoints for intake form submission
  name: BodySpec Partner Intake API
  slug: bodyspec-partner-intake-api
- baseURL: https://app.bodyspec.com
  baseurl_source: declared
  description: Partner integration endpoints for medical order upload and management
  name: BodySpec Partner Orders API
  slug: bodyspec-partner-orders-api
- baseURL: https://app.bodyspec.com
  baseurl_source: declared
  description: Partner integration endpoints for user results
  name: BodySpec Partner Results API
  slug: bodyspec-partner-results-api
- baseURL: https://app.bodyspec.com
  baseurl_source: declared
  description: Partner integration endpoints for user management
  name: BodySpec Partner Users API
  slug: bodyspec-partner-users-api
- baseURL: https://app.bodyspec.com
  baseurl_source: declared
  description: Partner integration endpoints for webhook configuration
  name: BodySpec Partner Webhooks API
  slug: bodyspec-partner-webhooks-api
- baseURL: https://app.bodyspec.com
  baseurl_source: declared
  description: Partner integration endpoints for reservations
  name: BodySpec Reservations API
  slug: bodyspec-reservations-api
- baseURL: https://app.bodyspec.com
  baseurl_source: declared
  description: Test results and analysis data
  name: BodySpec Results API
  slug: bodyspec-results-api
- baseURL: https://app.bodyspec.com
  baseurl_source: declared
  description: Available scan types and services
  name: BodySpec Services API
  slug: bodyspec-services-api
- baseURL: https://app.bodyspec.com
  baseurl_source: declared
  description: Operations related to user management and profiles
  name: BodySpec Users API
  slug: bodyspec-users-api
artifact_total: 29
asyncapis:
- description: ''
  name: Bodyspec Webhooks
  slug: bodyspec-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bodyspec/refs/heads/main/vendors/bodyspec-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bodyspec-vendors.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bodyspec/refs/heads/main/agentic-access/bodyspec-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bodyspec-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bodyspec/refs/heads/main/rules/bodyspec-rules.yml
  title: ''
  type: Spectral
  url: rules/bodyspec-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bodyspec/refs/heads/main/json-ld/bodyspec-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bodyspec-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bodyspec/refs/heads/main/vocabulary/bodyspec-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bodyspec-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bodyspec/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bodyspec/refs/heads/main/asyncapi/bodyspec-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bodyspec-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bodyspec/refs/heads/main/data-model/bodyspec-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bodyspec-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bodyspec/refs/heads/main/errors/bodyspec-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bodyspec-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bodyspec/refs/heads/main/conformance/bodyspec-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bodyspec-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bodyspec/refs/heads/main/well-known/bodyspec-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bodyspec-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bodyspec/refs/heads/main/hosts/bodyspec-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bodyspec-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://www.bodyspec.com/sign-in
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bodyspec/refs/heads/main/scopes/bodyspec-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/bodyspec-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bodyspec/refs/heads/main/authentication/bodyspec-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bodyspec-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bodyspec/refs/heads/main/security/bodyspec-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bodyspec-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bodyspec.com/
- group: docs
  title: ''
  type: Documentation
  url: https://app.bodyspec.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://app.bodyspec.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bodyspec.com/pricing-packages
- group: company
  title: ''
  type: Blog
  url: https://www.bodyspec.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bodyspec.com/pricing-packages
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bodyspec.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bodyspec.com/privacy-policy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://app.bodyspec.com/openapi.json
  - status: null
    url: https://www.bodyspec.com/graphql
  - status: 401
    url: https://app.bodyspec.com/mcp
  - status: 401
    url: https://api.bodyspec.com/v1/graphql
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: partner-login
  state: gated
created: '2026-10-02'
description: BodySpec provides full-body DEXA scanning services that deliver precise body composition data, including fat, muscle, and bone density. Their platform offers an API and MCP access for integrating scan results into health, fitness, and AI applications, supporting bookings, pricing, and data retrieval for individuals and enterprises.
image: https://static.bodyspec.com/at/55/6b/556bb64891d971a6
json_schemas:
- name: Appointment
  property_count: 7
  slug: bodyspec-appointment
- name: DexaComposition
  property_count: 5
  slug: bodyspec-dexa-composition-response
- name: IntakeCreateRequest
  property_count: 4
  slug: bodyspec-intake-create-request
- name: InteractiveFormatRequest
  property_count: 6
  slug: bodyspec-interactive-format-request
- name: OrderResponse
  property_count: 10
  slug: bodyspec-order-response
- name: PdfFormatRequest
  property_count: 6
  slug: bodyspec-pdf-format-request
jsonld:
- class_count: 73
  name: Bodyspec Context
  property_count: 140
  slug: bodyspec-context
layout: provider
modified: '2026-10-02'
name: BodySpec
nav: Providers
network: true
overview: 'BodySpec publishes 15 APIs on the [APIs.io](https://apis.io/) network, including API Status API, Appointments API, Availability API, and 12 more. Tagged areas include Company, Health, Fitness, and Data.


  The BodySpec catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  BodySpec''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Bodyspec Plans Pricing
  plan_count: 0
  slug: bodyspec-plans-pricing
random_paper: 21
rules:
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: BodySpec API Rules
  rule_count: 16
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 3
  slug: bodyspec-rules
scopes:
- name: Bodyspec Scopes
  scope_count: 3
  slug: bodyspec-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 47.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 72.1
    developer_ergonomics: 44.6
    discoverability: 57.1
    operational_transparency: 7.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Bodyspec Authentication
  slug: bodyspec-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Bodyspec Domain Security
  slug: bodyspec-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bodyspec
tags:
- Company
- Health
- Fitness
- Data
website: https://www.bodyspec.com/
---
