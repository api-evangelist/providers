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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.8
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Embedded data import API for B2B SaaS applications.
  name: WeTransform API
  slug: wetransform-api-2
- description: 'WeTransform API as documented publicly: 16 operations. Contract generated from the documentation by API Evangelist (2026-10-19); not the provider''s own document.'
  name: WeTransform API
  slug: wetransform-api
artifact_total: 14
asyncapis:
- description: ''
  name: Wetransform Webhooks
  slug: wetransform-webhooks
common:
- group: docs
  title: ''
  type: Documentation
  url: https://help.wetransform.com/
- group: commercial
  href: https://artifacts.apis.io/wetransform/plans/wetransform-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/wetransform-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/wetransform/rules/wetransform-rules.yml
  title: ''
  type: Spectral
  url: rules/wetransform-rules.yml
- group: design
  href: https://artifacts.apis.io/wetransform/json-ld/wetransform-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/wetransform-context.jsonld
- group: design
  href: https://artifacts.apis.io/wetransform/vocabulary/wetransform-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/wetransform-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/wetransform/asyncapi/wetransform-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/wetransform-webhooks.yml
- group: design
  href: https://artifacts.apis.io/wetransform/data-model/wetransform-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wetransform-data-model.yml
- group: auth
  href: https://artifacts.apis.io/wetransform/authentication/wetransform-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wetransform-authentication.yml
- group: design
  href: https://artifacts.apis.io/wetransform/conformance/wetransform-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wetransform-conformance.yml
- group: agent
  href: https://artifacts.apis.io/wetransform/llms/wetransform-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wetransform-llms.txt
- group: auth
  href: https://artifacts.apis.io/wetransform/well-known/wetransform-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/wetransform-help-security.txt
- group: agent
  href: https://artifacts.apis.io/wetransform/well-known/wetransform-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wetransform-well-known.yml
- group: other
  href: https://artifacts.apis.io/wetransform/hosts/wetransform-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wetransform-hosts.yml
- group: build
  href: https://artifacts.apis.io/wetransform/packages/wetransform-packages.yml
  title: ''
  type: Packages
  url: packages/wetransform-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://help.wetransform.com/en/
- group: auth
  title: ''
  type: Security
  url: https://wetransform.com/product/security
- group: build
  title: ''
  type: SDKs
  url: https://wetransform.com/product/sdk
- group: start
  title: ''
  type: Login
  url: https://app.wetransform.com/login
- group: start
  title: ''
  type: GettingStarted
  url: https://help.wetransform.com/en/articles/14325197-use-case-remove-the-data-format-barrier-from-client-onboarding
- group: auth
  href: https://artifacts.apis.io/wetransform/security/wetransform-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wetransform-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wetransform.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://wetransform.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wetransform.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wetransform.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://wetransform.com/blog
coverage:
  detail: Documentation pages are rendered via JavaScript, no machine‑readable spec found.
  evidence:
  - status: 200
    url: https://api.wetransform.com/en/documentation
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-19'
description: WeTransform provides an embedded data import platform for B2B SaaS applications, enabling no‑code data ingestion, transformation, and enrichment. Their solution offers white‑label import widgets, AI‑assisted data cleaning, automated workflows, and customizable logic to help companies streamline data onboarding and improve data quality across products.
image: https://wetransform.com/og.svg?title=WeTransform%20%E2%80%94%20Embedded%20Data%20Importer%20for%20B2B%20SaaS&category=Embeddable%20AI%20Importer
json_schemas:
- name: DeleteEnHelloResponse
  property_count: 5
  slug: wetransform-delete-en-hello-response
- name: GetEnDocumentationApiFetcherMoviesIdResponse
  property_count: 6
  slug: wetransform-get-en-documentation-api-fetcher-movies-id-response
- name: GetEnDocumentationApiFetcherMoviesResponse
  property_count: 10
  slug: wetransform-get-en-documentation-api-fetcher-movies-response
- name: GetEnHelloResponse
  property_count: 5
  slug: wetransform-get-en-hello-response
- name: PostPowerFunctionsCallidCallnumberPopulateRequest
  property_count: 3
  slug: wetransform-post-power-functions-callid-callnumber-populate-request
- name: PostSenderSourceRequest
  property_count: 7
  slug: wetransform-post-sender-source-request
jsonld:
- class_count: 12
  name: Wetransform Context
  property_count: 29
  slug: wetransform-context
layout: provider
modified: '2026-10-19'
name: WeTransform
nav: Providers
network: true
overview: 'WeTransform is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Data Integration, B2B SaaS, No-Code, Artificial Intelligence, and Embedded Import.


  The WeTransform catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  WeTransform''s developer surface includes documentation, authentication, support, getting-started guide, pricing, engineering blog, and 19 more developer resources.'
plans:
- name: Wetransform Plans Pricing
  plan_count: 3
  slug: wetransform-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: WeTransform API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: wetransform-rules
score:
  band: developing
  composite: 44.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 31.5
    developer_ergonomics: 47.6
    discoverability: 57.1
    operational_transparency: 18.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Wetransform Authentication
  slug: wetransform-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Wetransform Domain Security
  slug: wetransform-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wetransform
tags:
- Data Integration
- B2B SaaS
- No-Code
- Artificial Intelligence
- Embedded Import
website: https://wetransform.com/
---
