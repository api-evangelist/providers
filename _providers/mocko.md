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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.6
  scored_at: '2026-10-31'
api_count: 5
apis:
- description: Mocko provides a dynamic HTTP mocking tool with a developer portal at https://mocko.dev/docs/.
  name: Mocko API
  slug: mocko-api
- baseURL: https://demo-api.mockoapp.net
  baseurl_source: declared
  description: 'Mocko core API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Mocko core API
  slug: core-api
- baseURL: https://demo-api.mockoapp.net
  baseurl_source: declared
  description: 'Mocko creating mocks API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Mocko creating mocks API
  slug: creating-mocks-api
- baseURL: https://demo-api.mockoapp.net
  baseurl_source: declared
  description: 'Mocko Recipes Overview API as documented publicly: 16 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Mocko Recipes Overview API
  slug: recipes-api
- baseURL: https://demo-api.mockoapp.net
  baseurl_source: declared
  description: 'Mocko Legacy v1 docs API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: Mocko Legacy v1 docs API
  slug: v1-api
artifact_total: 21
common:
- group: design
  href: https://artifacts.apis.io/mocko/rules/mocko-rules.yml
  title: ''
  type: Spectral
  url: rules/mocko-rules.yml
- group: design
  href: https://artifacts.apis.io/mocko/json-ld/mocko-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mocko-context.jsonld
- group: design
  href: https://artifacts.apis.io/mocko/vocabulary/mocko-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mocko-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mocko/data-model/mocko-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mocko-data-model.yml
- group: build
  href: https://artifacts.apis.io/mocko/cli/mocko-cli.yml
  title: ''
  type: CLI
  url: cli/mocko-cli.yml
- group: auth
  href: https://artifacts.apis.io/mocko/authentication/mocko-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mocko-authentication.yml
- group: design
  href: https://artifacts.apis.io/mocko/conformance/mocko-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mocko-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mocko/llms/mocko-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mocko-llms.txt
- group: other
  href: https://artifacts.apis.io/mocko/hosts/mocko-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mocko-hosts.yml
- group: other
  href: https://artifacts.apis.io/mocko/vendors/mocko-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mocko-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://mocko.dev/docs/reference/cli
- group: start
  title: ''
  type: GettingStarted
  url: https://mocko.dev/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mocko.dev/
- group: auth
  href: https://artifacts.apis.io/mocko/security/mocko-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mocko-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mocko.dev/
coverage:
  checked: '2026-10-20'
  detail: Provider documentation at https://mocko.dev/docs/ contains no machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract files.
  evidence:
  - status: 0
    url: https://api.mocko.dev/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: Mocko provides a platform for creating, managing, and deploying mock APIs for testing and development purposes. The service enables developers to quickly spin up realistic API simulations without writing extensive backend code, supporting a variety of protocols and response configurations. Mocko’s dashboard offers analytics, versioning, and collaboration tools, helping teams streamline integration testing and accelerate product cycles. With robust security features and customizable rate limits, it ensures safe and reliable mock environments for both internal and external stakeholders.
image: https://cdn.codetunnel.net/mocko/og-v1.png
json_schemas:
- name: GetExportsIdResponse
  property_count: 3
  slug: mocko-get-exports-id-response
- name: GetInvoicesIdResponse
  property_count: 2
  slug: mocko-get-invoices-id-response
- name: GetOrdersIdResponse
  property_count: 2
  slug: mocko-get-orders-id-response
- name: GetPaymentsIdResponse
  property_count: 3
  slug: mocko-get-payments-id-response
- name: GetProductsIdResponse
  property_count: 4
  slug: mocko-get-products-id-response
- name: GetUsersIdResponse
  property_count: 2
  slug: mocko-get-users-id-response
- name: PostOrdersOrderidRequest
  property_count: 1
  slug: mocko-post-orders-orderid-request
- name: PostOrdersRequest
  property_count: 1
  slug: mocko-post-orders-request
- name: PostOrdersResponse
  property_count: 2
  slug: mocko-post-orders-response
- name: PostOutageStateResponse
  property_count: 1
  slug: mocko-post-outage-state-response
- name: PutUsersIdRequest
  property_count: 1
  slug: mocko-put-users-id-request
- name: PutUsersIdResponse
  property_count: 2
  slug: mocko-put-users-id-response
jsonld:
- class_count: 20
  name: Mocko Context
  property_count: 15
  slug: mocko-context
layout: provider
modified: '2026-10-20'
name: Mocko
nav: Providers
network: true
overview: 'Mocko is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including core API, creating mocks API, and 3 more. Tagged areas include Company, API Mocking, Development Tools, Testing, and Collaboration.


  The Mocko catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Mocko''s developer surface includes CLI, authentication, API reference, getting-started guide, documentation, and 10 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Mocko API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: mocko-rules
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 25.7
    developer_ergonomics: 47.6
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 21
      marker_coverage: 100.0
      total: 21
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Mocko Authentication
  slug: mocko-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Mocko Domain Security
  slug: mocko-domain-security
  summary_line: TLSv1.3 · HSTS
slug: mocko
tags:
- Company
- API Mocking
- Development Tools
- Testing
- Collaboration
website: https://mocko.dev/
---
