---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://sandbox.duve.com
  baseurl_source: declared
  description: 'Duve API as documented publicly: 17 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Duve API
  slug: duve-api
artifact_total: 15
asyncapis:
- description: ''
  name: Duve Webhooks
  slug: duve-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/duve/plans/duve-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/duve-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/duve/rules/duve-rules.yml
  title: ''
  type: Spectral
  url: rules/duve-rules.yml
- group: design
  href: https://artifacts.apis.io/duve/json-ld/duve-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/duve-context.jsonld
- group: design
  href: https://artifacts.apis.io/duve/vocabulary/duve-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/duve-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/duve/asyncapi/duve-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/duve-webhooks.yml
- group: design
  href: https://artifacts.apis.io/duve/data-model/duve-data-model.yml
  title: ''
  type: DataModel
  url: data-model/duve-data-model.yml
- group: operate
  href: https://artifacts.apis.io/duve/changelog/duve-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/duve-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://duve.com/security-center/
- group: auth
  href: https://artifacts.apis.io/duve/authentication/duve-authentication.yml
  title: ''
  type: Authentication
  url: authentication/duve-authentication.yml
- group: design
  href: https://artifacts.apis.io/duve/conformance/duve-conformance.yml
  title: ''
  type: Conformance
  url: conformance/duve-conformance.yml
- group: agent
  href: https://artifacts.apis.io/duve/llms/duve-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/duve-llms.txt
- group: auth
  href: https://artifacts.apis.io/duve/well-known/duve-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/duve-status-security.txt
- group: agent
  href: https://artifacts.apis.io/duve/well-known/duve-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/duve-well-known.yml
- group: other
  href: https://artifacts.apis.io/duve/hosts/duve-hosts.yml
  title: ''
  type: Hosts
  url: hosts/duve-hosts.yml
- group: other
  href: https://artifacts.apis.io/duve/vendors/duve-vendors.yml
  title: ''
  type: Vendors
  url: vendors/duve-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://duve.com/terms/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.duve.com/
- group: start
  title: ''
  type: Sandbox
  url: https://duve.com/sandbox/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://duve.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://duve.com/pricing/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.duve.com/landing-page
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.duve.com/change-log/changelog/changelog
- group: docs
  title: ''
  type: Documentation
  url: https://developers.duve.com/
- group: auth
  href: https://artifacts.apis.io/duve/security/duve-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/duve-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/duve/security/duve-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/duve-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://duve.com
coverage:
  checked: '2026-10-24'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on the provider's documented hosts.
  evidence:
  - status: 200
    url: https://developers.duve.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-24'
description: Duve provides a hospitality guest experience platform offering branded guest apps, AI‑driven communication, revenue‑maximizing upsells, digital check‑in, mobile ordering, analytics, and workflow automation for hotels worldwide. Their solutions enable hotels to personalize guest interactions, increase ancillary revenue, and streamline operations through a unified cloud‑based suite.
image: https://duve.com/wp-content/uploads/2023/03/duve-social-share-1.jpg
json_schemas:
- name: GetApiOpenapiV1WebhooksIdResponse
  property_count: 12
  slug: duve-get-api-openapi-v1-webhooks-id-response
- name: GetOpenapiV1ReservationsLinksResponse
  property_count: 11
  slug: duve-get-openapi-v1-reservations-links-response
- name: PostApiOpenapiV1WebhooksRequest
  property_count: 11
  slug: duve-post-api-openapi-v1-webhooks-request
- name: PostApiOpenapiV1WebhooksResponse
  property_count: 12
  slug: duve-post-api-openapi-v1-webhooks-response
- name: PutApiOpenapiV1WebhooksIdRequest
  property_count: 11
  slug: duve-put-api-openapi-v1-webhooks-id-request
- name: PutApiOpenapiV1WebhooksIdResponse
  property_count: 12
  slug: duve-put-api-openapi-v1-webhooks-id-response
jsonld:
- class_count: 15
  name: Duve Context
  property_count: 43
  slug: duve-context
layout: provider
modified: '2026-10-24'
name: Duve
nav: Providers
network: true
overview: 'Duve is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Hospitality, GuestExperience, SaaS, AI, and RevenueOptimization.


  The Duve catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Duve''s developer surface includes changelog, authentication, sandbox, pricing, documentation, and 21 more developer resources.'
plans:
- name: Duve Plans Pricing
  plan_count: 4
  slug: duve-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Duve API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: duve-rules
scopes:
- name: Duve Scopes
  scope_count: 0
  slug: duve-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 33.1
    developer_ergonomics: 38.1
    discoverability: 66.1
    operational_transparency: 50.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 36.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Duve Authentication
  slug: duve-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Duve Domain Security
  slug: duve-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Duve Trust Center
  slug: duve-trust-center
  summary_line: SOC 2, ISO 27001
slug: duve
tags:
- Hospitality
- GuestExperience
- SaaS
- AI
- RevenueOptimization
- Company
website: https://duve.com
---
