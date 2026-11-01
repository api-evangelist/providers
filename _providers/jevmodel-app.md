---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'JevModel API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: JevModel API
  slug: jevmodel-app-api
artifact_total: 12
asyncapis:
- description: ''
  name: Jevmodel App Webhooks
  slug: jevmodel-app-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/jevmodel-app/plans/jevmodel-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jevmodel-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/jevmodel-app/rules/jevmodel-app-rules.yml
  title: ''
  type: Spectral
  url: rules/jevmodel-app-rules.yml
- group: design
  href: https://artifacts.apis.io/jevmodel-app/json-ld/jevmodel-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/jevmodel-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/jevmodel-app/vocabulary/jevmodel-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/jevmodel-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/jevmodel-app/asyncapi/jevmodel-app-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/jevmodel-app-webhooks.yml
- group: design
  href: https://artifacts.apis.io/jevmodel-app/data-model/jevmodel-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/jevmodel-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/jevmodel-app/conformance/jevmodel-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jevmodel-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/jevmodel-app/llms/jevmodel-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jevmodel-app-llms.txt
- group: other
  href: https://artifacts.apis.io/jevmodel-app/hosts/jevmodel-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jevmodel-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/jevmodel-app/vendors/jevmodel-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jevmodel-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jevmodel.app/terms-of-service
- group: start
  title: ''
  type: Sandbox
  url: https://jevmodel.app/console
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jevmodel.app/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://jevmodel.app/pricing
- group: start
  title: ''
  type: Login
  url: https://jevmodel.app/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://jevmodel.app/guides
- group: start
  title: ''
  type: GettingStarted
  url: https://jevmodel.app/guides/getting-started
- group: auth
  href: https://artifacts.apis.io/jevmodel-app/security/jevmodel-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jevmodel-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jevmodel.app
coverage:
  checked: '2026-10-29'
  detail: Provider documentation pages are HTML without any published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts.
  evidence:
  - status: 200
    url: https://jevmodel.app/guides/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: JevModel offers a structured decision model that processes text or JSON and returns typed answers—Choice, Score, or Noul—with associated probabilities. The service provides a web console, batch tools, and an API that developers can integrate to perform tasks such as content moderation, spam filtering, support triage, ticket routing, and sentiment analysis. Access is sold via token packs or one‑time purchase plans.
image: https://jevmodel.app/og-image.png
json_schemas:
- name: GetApiV1SystemoneResponse
  property_count: 8
  slug: jevmodel-app-get-api-v1-systemone-response
- name: PostApiV1SystemoneRequest
  property_count: 2
  slug: jevmodel-app-post-api-v1-systemone-request
- name: PostTurnstileV0SiteverifyRequest
  property_count: 3
  slug: jevmodel-app-post-turnstile-v0-siteverify-request
- name: PostTurnstileV0SiteverifyResponse
  property_count: 2
  slug: jevmodel-app-post-turnstile-v0-siteverify-response
- name: Post11CommentCheckRequest
  property_count: 9
  slug: jevmodel-app-post11-comment-check-request
- name: Post11CommentCheckResponse
  property_count: 1
  slug: jevmodel-app-post11-comment-check-response
jsonld:
- class_count: 6
  name: Jevmodel App Context
  property_count: 25
  slug: jevmodel-app-context
layout: provider
modified: '2026-10-28'
name: JevModel
nav: Providers
network: true
overview: 'JevModel is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Decision API, Content Moderation, Spam Filtering, Support Triage, and Ticket Routing.


  The JevModel catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  JevModel''s developer surface includes sandbox, pricing, documentation, getting-started guide, and 15 more developer resources.'
plans:
- name: Jevmodel App Plans Pricing
  plan_count: 9
  slug: jevmodel-app-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: JevModel API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: jevmodel-app-rules
score:
  band: thin
  composite: 39.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 32.4
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Jevmodel App Domain Security
  slug: jevmodel-app-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jevmodel-app
tags:
- Decision API
- Content Moderation
- Spam Filtering
- Support Triage
- Ticket Routing
- Language Detection
- Personal Data Screening
website: https://jevmodel.app
---
