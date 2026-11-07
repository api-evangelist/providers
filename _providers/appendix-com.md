---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.9
  scored_at: '2026-11-06'
api_count: 3
apis:
- baseURL: https://api.appendix.com
  baseurl_source: declared
  description: 'Appendix api reference API as documented publicly: 24 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Appendix api reference API
  slug: api-reference-api
- baseURL: https://api.appendix.com
  baseurl_source: declared
  description: 'Appendix core API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Appendix core API
  slug: core-api
- baseURL: https://api.appendix.com
  baseurl_source: declared
  description: 'Appendix Prescribing API Overview API as documented publicly: 13 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Appendix Prescribing API Overview API
  slug: prescribing-api
artifact_total: 21
asyncapis:
- description: ''
  name: Appendix Com Webhooks
  slug: appendix-com-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/appendix-com/plans/appendix-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appendix-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/appendix-com/rules/appendix-com-rules.yml
  title: ''
  type: Spectral
  url: rules/appendix-com-rules.yml
- group: design
  href: https://artifacts.apis.io/appendix-com/json-ld/appendix-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/appendix-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/appendix-com/vocabulary/appendix-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/appendix-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/appendix-com/asyncapi/appendix-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/appendix-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/appendix-com/data-model/appendix-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/appendix-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/appendix-com/authentication/appendix-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/appendix-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/appendix-com/conformance/appendix-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appendix-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/appendix-com/llms/appendix-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appendix-com-llms.txt
- group: other
  href: https://artifacts.apis.io/appendix-com/hosts/appendix-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appendix-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/appendix-com/vendors/appendix-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appendix-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appendix.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appendix.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://appendix.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/appendixhealth
- group: docs
  title: ''
  type: Documentation
  url: https://appendix.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://appendix.com/developers/dashboard
- group: docs
  title: ''
  type: APIReference
  url: https://appendix.com/docs/api-reference/chat
- group: start
  title: ''
  type: GettingStarted
  url: https://appendix.com/docs/prescribing-api/quickstart
- group: auth
  href: https://artifacts.apis.io/appendix-com/security/appendix-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appendix-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appendix.com/
created: '2026-11-01'
description: Appendix provides a physician‑review API that lets AI agents and applications submit health queries for board‑certified doctor evaluation, including e‑prescribing when appropriate. The service offers a human‑in‑the‑loop experience, handling patient consent, identity verification, and delivering clinical assessments via webhooks, enabling developers to build health‑focused AI products with real medical oversight.
image: https://appendix.com/images/og-image.jpg
json_schemas:
- name: GetApiV1AgentEncountersEncounteridEventsResponse
  property_count: 3
  slug: appendix-com-get-api-v1-agent-encounters-encounterid-events-response
- name: GetApiV1PatientsResponse
  property_count: 1
  slug: appendix-com-get-api-v1-patients-response
- name: GetApiV1PrescribingEncountersIdDetailsResponse
  property_count: 13
  slug: appendix-com-get-api-v1-prescribing-encounters-id-details-response
- name: GetApiV1PrescribingPatientsIdResponse
  property_count: 13
  slug: appendix-com-get-api-v1-prescribing-patients-id-response
- name: GetApiV1UsersMeApiKeysResponse
  property_count: 6
  slug: appendix-com-get-api-v1-users-me-api-keys-response
- name: GetApiV1UsersMeResponse
  property_count: 5
  slug: appendix-com-get-api-v1-users-me-response
- name: PostApiV1PrescribingPatientsRequest
  property_count: 11
  slug: appendix-com-post-api-v1-prescribing-patients-request
- name: PostApiV1PrescribingSandboxEncountersB1A2AdvanceResponse
  property_count: 6
  slug: appendix-com-post-api-v1-prescribing-sandbox-encounters-b1-a2-advance-response
- name: PostApiV1UsersMeApiKeysRequest
  property_count: 2
  slug: appendix-com-post-api-v1-users-me-api-keys-request
- name: PostApiV1UsersMeApiKeysResponse
  property_count: 6
  slug: appendix-com-post-api-v1-users-me-api-keys-response
- name: PostPrescribingEncountersIdMessagesResponse
  property_count: 4
  slug: appendix-com-post-prescribing-encounters-id-messages-response
- name: PostPrescribingQueryResponse
  property_count: 6
  slug: appendix-com-post-prescribing-query-response
jsonld:
- class_count: 21
  name: Appendix Com Context
  property_count: 57
  slug: appendix-com-context
layout: provider
modified: '2026-11-01'
name: Appendix
nav: Providers
network: true
overview: 'Appendix is listed with 3 APIs on the [APIs.io](https://apis.io/) network: api reference API, core API, and Prescribing API Overview API. Tagged areas include Healthcare, Artificial Intelligence, Telehealth, and PhysicianReview.


  The Appendix catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Appendix''s developer surface includes authentication, pricing, documentation, API reference, getting-started guide, and 16 more developer resources.'
plans:
- name: Appendix Com Plans Pricing
  plan_count: 3
  slug: appendix-com-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Appendix API Rules
  rule_count: 44
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 4
  slug: appendix-com-rules
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 33.6
    developer_ergonomics: 31.0
    discoverability: 62.5
    operational_transparency: 10.5
  previous_composite: 43.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Appendix Com Authentication
  slug: appendix-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Appendix Com Domain Security
  slug: appendix-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appendix-com
tags:
- Healthcare
- Artificial Intelligence
- Telehealth
- PhysicianReview
website: https://appendix.com/
---
