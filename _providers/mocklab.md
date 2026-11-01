---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://my-api.wiremockapi.cloud
  baseurl_source: declared
  description: 'MockLab API as documented publicly: 11 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: MockLab API
  slug: mocklab-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/mocklab/plans/mocklab-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/mocklab-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/mocklab/rules/mocklab-rules.yml
  title: ''
  type: Spectral
  url: rules/mocklab-rules.yml
- group: design
  href: https://artifacts.apis.io/mocklab/json-ld/mocklab-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mocklab-context.jsonld
- group: design
  href: https://artifacts.apis.io/mocklab/vocabulary/mocklab-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mocklab-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mocklab/data-model/mocklab-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mocklab-data-model.yml
- group: auth
  href: https://artifacts.apis.io/mocklab/authentication/mocklab-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mocklab-authentication.yml
- group: design
  href: https://artifacts.apis.io/mocklab/conformance/mocklab-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mocklab-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mocklab/llms/mocklab-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mocklab-llms.txt
- group: other
  href: https://artifacts.apis.io/mocklab/a2a/mocklab-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/mocklab-a2a.yml
- group: agent
  href: https://artifacts.apis.io/mocklab/mcp/mocklab-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mocklab-mcp.yml
- group: agent
  href: https://artifacts.apis.io/mocklab/well-known/mocklab-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mocklab-well-known.yml
- group: other
  href: https://artifacts.apis.io/mocklab/hosts/mocklab-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mocklab-hosts.yml
- group: other
  href: https://artifacts.apis.io/mocklab/vendors/mocklab-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mocklab-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.wiremock.io/blog
- group: auth
  href: https://artifacts.apis.io/mocklab/security/mocklab-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mocklab-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wiremock.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wiremock.io/
- group: docs
  title: ''
  type: APIReference
  url: https://www.wiremock.io/api-mocks
- group: start
  title: ''
  type: GettingStarted
  url: https://www.wiremock.io/platform/api-simulation
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wiremock.io/get-pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wiremock.io/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wiremock.io/privacy-policy
created: '2026-10-21'
description: MockLab, now operating under the WireMock brand, provides a cloud-based API mocking platform that enables developers to simulate complex service environments for testing and development. Their solution offers AI‑powered simulation, turnkey API templates, and integration with agentic development workflows, allowing teams to create realistic, short‑lived test environments without impacting production. WireMock Cloud supports enterprise‑grade features such as clean‑room testing, code quality checks, and extensive analytics, helping organizations accelerate delivery while ensuring reliability and security across their API ecosystems.
image: https://www.wiremock.io/images/og-default.jpg
json_schemas:
- name: DeleteBaskets1ItemsResponse
  property_count: 2
  slug: mocklab-delete-baskets1-items-response
- name: DeleteBaskets1Items2Response
  property_count: 2
  slug: mocklab-delete-baskets1-items2-response
- name: GetAdminExtJobs8E2F36415F0A45A29D1B39Cf16B2D0E7Response
  property_count: 8
  slug: mocklab-get-admin-ext-jobs8-e2-f36415-f0-a45-a29-d1-b39-cf16-b2-d0-e7-response
- name: GetAdminMappingsResponse
  property_count: 1
  slug: mocklab-get-admin-mappings-response
- name: GetWellKnownOpenidConfigurationResponse
  property_count: 3
  slug: mocklab-get-well-known-openid-configuration-response
- name: PostBaskets1ItemsRequest
  property_count: 3
  slug: mocklab-post-baskets1-items-request
jsonld:
- class_count: 10
  name: Mocklab Context
  property_count: 18
  slug: mocklab-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.wiremock.cloud requiring OAuth.
  name: MockLab MCP Server
  slug: mocklab-mcp-yml
modified: '2026-10-21'
name: MockLab
nav: Providers
network: true
overview: 'MockLab is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Mocking, Environment Simulation, Testing, Fintech, and Service Virtualization.


  The MockLab catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MockLab''s developer surface includes authentication, engineering blog, documentation, API reference, getting-started guide, pricing, and 16 more developer resources.'
plans:
- name: Mocklab Plans Pricing
  plan_count: 2
  slug: mocklab-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: MockLab API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: mocklab-rules
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 26.5
    developer_ergonomics: 42.9
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
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
  name: Mocklab Authentication
  slug: mocklab-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Mocklab Domain Security
  slug: mocklab-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mocklab
tags:
- API Mocking
- Environment Simulation
- Testing
- Fintech
- Service Virtualization
- Cloud Service
website: https://www.wiremock.io/
---
