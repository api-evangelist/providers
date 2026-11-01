---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 59.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 58
  human_in_the_loop: 8
  name: Anpheros Com Agentic Access
  operation_count: 140
  slug: anpheros-com-agentic-access
  summary_line: 140 operations · 58 acting · 8 human-in-the-loop
api_count: 1
apis:
- baseURL: https://platform.anpheros.com
  baseurl_source: declared
  description: The Access requests API from anpheros-com — 1 operation(s) for access requests.
  name: anpheros-com Access requests API
  slug: anpheros-com-access-requests-api
- baseURL: https://platform.anpheros.com
  baseurl_source: declared
  description: The Admin API from anpheros-com — 28 operation(s) for admin.
  name: anpheros-com Admin API
  slug: anpheros-com-admin-api
- baseURL: https://platform.anpheros.com
  baseurl_source: declared
  description: The Anpheros Search API from anpheros-com — 8 operation(s) for anpheros search.
  name: anpheros-com Anpheros Search API
  slug: anpheros-com-anpheros-search-api
- baseURL: https://platform.anpheros.com
  baseurl_source: declared
  description: The FHIR R4 API from anpheros-com — 18 operation(s) for fhir r4.
  name: anpheros-com FHIR R4 API
  slug: anpheros-com-fhir-r4-api
- baseURL: https://platform.anpheros.com
  baseurl_source: declared
  description: The ICD-10 to ICD-11 API from anpheros-com — 3 operation(s) for icd-10 to icd-11.
  name: anpheros-com ICD-10 to ICD-11 API
  slug: anpheros-com-icd-10-to-icd-11-api
- baseURL: https://platform.anpheros.com
  baseurl_source: declared
  description: The OAuth API from anpheros-com — 3 operation(s) for oauth.
  name: anpheros-com OAuth API
  slug: anpheros-com-oauth-api
- baseURL: https://platform.anpheros.com
  baseurl_source: declared
  description: The Patient (me) API from anpheros-com — 16 operation(s) for patient (me).
  name: anpheros-com Patient (me) API
  slug: anpheros-com-patient-me-api
- baseURL: https://platform.anpheros.com
  baseurl_source: declared
  description: The REST v1 API from anpheros-com — 36 operation(s) for rest v1.
  name: anpheros-com REST v1 API
  slug: anpheros-com-rest-v1-api
- baseURL: https://platform.anpheros.com
  baseurl_source: declared
  description: The SMART Health Links API from anpheros-com — 2 operation(s) for smart health links.
  name: anpheros-com SMART Health Links API
  slug: anpheros-com-smart-health-links-api
- baseURL: https://platform.anpheros.com
  baseurl_source: declared
  description: The Webhooks API from anpheros-com — 8 operation(s) for webhooks.
  name: anpheros-com Webhooks API
  slug: anpheros-com-webhooks-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/anpheros-com/agentic-access/anpheros-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/anpheros-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/anpheros-com/rate-limits/anpheros-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/anpheros-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/anpheros-com/plans/anpheros-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/anpheros-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/anpheros-com/rules/anpheros-com-rules.yml
  title: ''
  type: Spectral
  url: rules/anpheros-com-rules.yml
- group: design
  href: https://artifacts.apis.io/anpheros-com/json-ld/anpheros-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/anpheros-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/anpheros-com/vocabulary/anpheros-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/anpheros-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/anpheros-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/anpheros-com/data-model/anpheros-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anpheros-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/anpheros-com/conventions/anpheros-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/anpheros-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/anpheros-com/conventions/anpheros-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/anpheros-com-conventions.yml
- group: start
  href: https://artifacts.apis.io/anpheros-com/sandbox/anpheros-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/anpheros-com-sandbox.yml
- group: design
  href: https://artifacts.apis.io/anpheros-com/errors/anpheros-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/anpheros-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/anpheros-com/conformance/anpheros-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anpheros-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/anpheros-com/llms/anpheros-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anpheros-com-llms.txt
- group: other
  href: https://artifacts.apis.io/anpheros-com/a2a/anpheros-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/anpheros-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/anpheros-com/mcp/anpheros-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anpheros-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/anpheros-com/well-known/anpheros-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anpheros-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/anpheros-com/hosts/anpheros-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anpheros-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/anpheros-com/vendors/anpheros-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anpheros-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/anpheros-com/packages/anpheros-com-packages.yml
  title: ''
  type: Packages
  url: packages/anpheros-com-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@anpheros/sdk
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.anpheros.com/guides/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anpheros
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.anpheros.com/guides/getting-started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.anpheros.com/llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://developers.anpheros.com/
- group: auth
  href: https://artifacts.apis.io/anpheros-com/scopes/anpheros-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/anpheros-com-scopes.yml
- group: auth
  href: https://artifacts.apis.io/anpheros-com/authentication/anpheros-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/anpheros-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/anpheros-com/security/anpheros-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anpheros-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anpheros.com/
- group: operate
  title: ''
  type: Support
  url: https://anpheros.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anpheros.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anpheros.com/terms
- group: docs
  title: ''
  type: APIReference
  url: https://api.anpheros.com/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://developers.anpheros.com/openapi.json
  - status: null
    url: https://platform.anpheros.com/openapi.json
  - status: 401
    url: https://developers.anpheros.com/mcp
  - status: 401
    url: https://platform.anpheros.com/mcp
  - status: 200
    url: https://anpheros.com/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Anpheros provides a free medical records and daily health tracker app for families, allowing symptom logging, medication tracking, and lab result storage. The platform offers a patient‑controlled record system called Anpheros Daily and a HL7 FHIR R4 API for developers to integrate health data. Emphasizing consent‑based sharing, open standards, and secure cloud storage, Anpheros aims to empower individuals to manage and share their health information safely.
image: https://anpheros.com/assets/logo-icon.png
json_schemas:
- name: ApplicationOut
  property_count: 15
  slug: anpheros-com-application-out
- name: DocumentOut
  property_count: 15
  slug: anpheros-com-document-out
- name: HealthTermOut
  property_count: 22
  slug: anpheros-com-health-term-out
- name: ObservationOut
  property_count: 17
  slug: anpheros-com-observation-out
- name: PatternFinding
  property_count: 24
  slug: anpheros-com-pattern-finding
- name: SymptomConceptOut
  property_count: 15
  slug: anpheros-com-symptom-concept-out
jsonld:
- class_count: 82
  name: Anpheros Com Context
  property_count: 222
  slug: anpheros-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at developers.anpheros.com.
  name: anpheros-com MCP Server
  slug: anpheros-com-mcp-yml
modified: '2026-10-30'
name: anpheros-com
nav: Providers
network: true
overview: 'anpheros-com publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access requests API, Admin API, Anpheros Search API, and 7 more. Tagged areas include Health, Digital-Health, FHIR, Medical-Records, and API.


  The anpheros-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  anpheros-com''s developer surface includes sandbox, pricing, getting-started guide, documentation, authentication, support, API reference, and 27 more developer resources.'
plans:
- name: Anpheros Com Plans Pricing
  plan_count: 4
  slug: anpheros-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Anpheros Com Rate Limits
  slug: anpheros-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: anpheros-com API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: anpheros-com-rules
scopes:
- name: Anpheros Com Scopes
  scope_count: 11
  slug: anpheros-com-scopes
  summary_line: 11 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 64.6
  coverage:
    artifact_dirs: 29
    catalog_earned: 99.3
    catalog_earned_first_party: 0.0
    catalog_gap: 15.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 79.1
    contract_quality: 56.2
    developer_ergonomics: 75.5
    discoverability: 65.0
    operational_transparency: 33.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anpheros Com Authentication
  slug: anpheros-com-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Anpheros Com Domain Security
  slug: anpheros-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: oauth-flow
  slug: anpheros-com-oauth
- name: patient-summary
  slug: anpheros-com-patient-summary
slug: anpheros-com
tags:
- Health
- Digital-Health
- FHIR
- Medical-Records
- API
website: https://anpheros.com/
---
