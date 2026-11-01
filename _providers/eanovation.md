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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Eanovation API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-24); not the provider''s own document.'
  name: Eanovation API
  slug: eanovation-api
artifact_total: 11
asyncapis:
- description: ''
  name: Eanovation Webhooks
  slug: eanovation-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/eanovation/plans/eanovation-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/eanovation-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/eanovation/rules/eanovation-rules.yml
  title: ''
  type: Spectral
  url: rules/eanovation-rules.yml
- group: design
  href: https://artifacts.apis.io/eanovation/json-ld/eanovation-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/eanovation-context.jsonld
- group: design
  href: https://artifacts.apis.io/eanovation/vocabulary/eanovation-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/eanovation-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/eanovation/asyncapi/eanovation-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/eanovation-webhooks.yml
- group: design
  href: https://artifacts.apis.io/eanovation/data-model/eanovation-data-model.yml
  title: ''
  type: DataModel
  url: data-model/eanovation-data-model.yml
- group: auth
  href: https://artifacts.apis.io/eanovation/authentication/eanovation-authentication.yml
  title: ''
  type: Authentication
  url: authentication/eanovation-authentication.yml
- group: design
  href: https://artifacts.apis.io/eanovation/conformance/eanovation-conformance.yml
  title: ''
  type: Conformance
  url: conformance/eanovation-conformance.yml
- group: agent
  href: https://artifacts.apis.io/eanovation/llms/eanovation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eanovation-llms.txt
- group: auth
  href: https://artifacts.apis.io/eanovation/well-known/eanovation-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/eanovation-help-security.txt
- group: agent
  href: https://artifacts.apis.io/eanovation/well-known/eanovation-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/eanovation-well-known.yml
- group: other
  href: https://artifacts.apis.io/eanovation/hosts/eanovation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eanovation-hosts.yml
- group: other
  href: https://artifacts.apis.io/eanovation/vendors/eanovation-vendors.yml
  title: ''
  type: Vendors
  url: vendors/eanovation-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eano.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://help.eano.com/en/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eano.com/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.eano.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.eano.com/pro/login
- group: company
  title: ''
  type: Blog
  url: https://www.eano.com/resources/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.eano.com/en/articles/16040854-project-templates-bundling-your-scope-milestones-and-tasks-into-one-reusable-setup
- group: docs
  title: ''
  type: Documentation
  url: https://developer.eano.com/
- group: auth
  href: https://artifacts.apis.io/eanovation/security/eanovation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eanovation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.eano.com
coverage:
  checked: '2026-10-24'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.eano.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-24'
description: Eanovation is a technology company focused on innovative solutions in the field of digital transformation and data analytics. The company aims to provide advanced platforms that enable businesses to integrate, process, and visualize data efficiently, supporting decision-making and operational excellence across various industries. While detailed public information is limited, the company appears to be emerging in the market with a focus on modern cloud-based services and API-driven architectures.
image: https://cdn.prod.website-files.com/670d5a126bda66dca6cdabeb/672174e1cad37880075a2860_webclip.jpg
json_schemas:
- name: GetApiV1ExternalBidsResponse
  property_count: 13
  slug: eanovation-get-api-v1-external-bids-response
- name: GetApiV1ExternalProjectsIdResponse
  property_count: 11
  slug: eanovation-get-api-v1-external-projects-id-response
- name: PostApiV1ExternalProjectsRequest
  property_count: 5
  slug: eanovation-post-api-v1-external-projects-request
- name: PostApiV1ExternalProjectsResponse
  property_count: 8
  slug: eanovation-post-api-v1-external-projects-response
jsonld:
- class_count: 4
  name: Eanovation Context
  property_count: 18
  slug: eanovation-context
layout: provider
modified: '2026-10-24'
name: Eanovation
nav: Providers
network: true
overview: 'Eanovation is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Technology, DataAnalytics, DigitalTransformation, and API.


  The Eanovation catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Eanovation''s developer surface includes authentication, support, pricing, engineering blog, getting-started guide, documentation, and 17 more developer resources.'
plans:
- name: Eanovation Plans Pricing
  plan_count: 6
  slug: eanovation-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Eanovation API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: eanovation-rules
score:
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 29.9
    developer_ergonomics: 40.5
    discoverability: 57.1
    operational_transparency: 18.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Eanovation Authentication
  slug: eanovation-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Eanovation Domain Security
  slug: eanovation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: eanovation
tags:
- Company
- Technology
- DataAnalytics
- DigitalTransformation
- API
website: https://www.eano.com
---
