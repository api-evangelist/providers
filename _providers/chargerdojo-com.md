---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://chargerdojo.com
  baseurl_source: declared
  description: 'ChargerDojo API as documented publicly: 31 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: ChargerDojo API
  slug: chargerdojo-com-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/chargerdojo-com/plans/chargerdojo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chargerdojo-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/chargerdojo-com/rules/chargerdojo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/chargerdojo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/chargerdojo-com/json-ld/chargerdojo-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chargerdojo-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/chargerdojo-com/vocabulary/chargerdojo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chargerdojo-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/chargerdojo-com/data-model/chargerdojo-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chargerdojo-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/chargerdojo-com/changelog/chargerdojo-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/chargerdojo-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/chargerdojo-com/conventions/chargerdojo-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/chargerdojo-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/chargerdojo-com/authentication/chargerdojo-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chargerdojo-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/chargerdojo-com/conformance/chargerdojo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chargerdojo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chargerdojo-com/llms/chargerdojo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chargerdojo-com-llms.txt
- group: other
  href: https://artifacts.apis.io/chargerdojo-com/a2a/chargerdojo-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/chargerdojo-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/chargerdojo-com/well-known/chargerdojo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chargerdojo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/chargerdojo-com/hosts/chargerdojo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chargerdojo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/chargerdojo-com/vendors/chargerdojo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chargerdojo-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chargerdojo.com/terms-of-service/
- group: auth
  title: ''
  type: Security
  url: https://chargerdojo.com/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chargerdojo.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chargerdojo
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.chargerdojo.com/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.chargerdojo.com/guide/plans.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.chargerdojo.com/guide/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.chargerdojo.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.chargerdojo.com/api-reference/reports/delete-a-report-you-own
- group: auth
  href: https://artifacts.apis.io/chargerdojo-com/security/chargerdojo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chargerdojo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chargerdojo.com/
- group: other
  title: ''
  type: Image
  url: https://chargerdojo.com/icon-512x512.png
coverage:
  detail: Provider documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://docs.chargerdojo.com/api
  - status: 200
    url: https://docs.chargerdojo.com/api-reference/reports/delete-a-report-you-own
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: ChargerDojo provides an OCPI testing tool and simulator for electric vehicle charging interoperability. It offers free sandbox testing and paid plans for deeper integration, allowing users to run conformance suites across OCPI versions 2.1.1, 2.2.1, and 2.3.0 without login. The platform supports timed charging journeys, detailed reporting, and offers both sandbox and enterprise pricing options.
image: https://chargerdojo.com/og/chargerdojo-og.png
json_schemas:
- name: GetTestingRunsIdResponse
  property_count: 2
  slug: chargerdojo-com-get-testing-runs-id-response
- name: GetTestingRunsResponse
  property_count: 3
  slug: chargerdojo-com-get-testing-runs-response
- name: PostConnectionsRequest
  property_count: 5
  slug: chargerdojo-com-post-connections-request
- name: PostTestingRunsRequest
  property_count: 1
  slug: chargerdojo-com-post-testing-runs-request
- name: PostTestingRunsResponse
  property_count: 2
  slug: chargerdojo-com-post-testing-runs-response
- name: PutConnectionsIdAddressRequest
  property_count: 1
  slug: chargerdojo-com-put-connections-id-address-request
jsonld:
- class_count: 9
  name: Chargerdojo Com Context
  property_count: 14
  slug: chargerdojo-com-context
layout: provider
modified: '2026-11-03'
name: ChargerDojo
nav: Providers
network: true
overview: 'ChargerDojo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Electric Vehicles, OCPI, Testing, Simulator, and Charging.


  The ChargerDojo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ChargerDojo''s developer surface includes changelog, authentication, pricing, getting-started guide, documentation, API reference, and 20 more developer resources.'
plans:
- name: Chargerdojo Com Plans Pricing
  plan_count: 4
  slug: chargerdojo-com-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: ChargerDojo API Rules
  rule_count: 46
  severity_counts:
    error: 41
    hint: 0
    info: 1
    warn: 4
  slug: chargerdojo-com-rules
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 26.2
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Chargerdojo Com Authentication
  slug: chargerdojo-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Chargerdojo Com Domain Security
  slug: chargerdojo-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chargerdojo-com
tags:
- Electric Vehicles
- OCPI
- Testing
- Simulator
- Charging
website: https://chargerdojo.com/
---
