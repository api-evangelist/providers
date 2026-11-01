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
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API for List Bulb directory
  name: List Bulb API
  slug: list-bulb-api
- description: 'List Bulb API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: List Bulb API
  slug: listbulb-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/listbulb/plans/listbulb-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/listbulb-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/listbulb/rules/listbulb-rules.yml
  title: ''
  type: Spectral
  url: rules/listbulb-rules.yml
- group: design
  href: https://artifacts.apis.io/listbulb/json-ld/listbulb-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/listbulb-context.jsonld
- group: design
  href: https://artifacts.apis.io/listbulb/vocabulary/listbulb-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/listbulb-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/listbulb/data-model/listbulb-data-model.yml
  title: ''
  type: DataModel
  url: data-model/listbulb-data-model.yml
- group: operate
  href: https://artifacts.apis.io/listbulb/changelog/listbulb-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/listbulb-changelog.yml
- group: design
  href: https://artifacts.apis.io/listbulb/conventions/listbulb-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/listbulb-conventions.yml
- group: design
  href: https://artifacts.apis.io/listbulb/conventions/listbulb-conventions.yml
  title: ''
  type: Conventions
  url: conventions/listbulb-conventions.yml
- group: auth
  href: https://artifacts.apis.io/listbulb/authentication/listbulb-authentication.yml
  title: ''
  type: Authentication
  url: authentication/listbulb-authentication.yml
- group: design
  href: https://artifacts.apis.io/listbulb/conformance/listbulb-conformance.yml
  title: ''
  type: Conformance
  url: conformance/listbulb-conformance.yml
- group: agent
  href: https://artifacts.apis.io/listbulb/llms/listbulb-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/listbulb-llms.txt
- group: agent
  href: https://artifacts.apis.io/listbulb/mcp/listbulb-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/listbulb-mcp.yml
- group: agent
  href: https://artifacts.apis.io/listbulb/well-known/listbulb-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/listbulb-well-known.yml
- group: other
  href: https://artifacts.apis.io/listbulb/hosts/listbulb-hosts.yml
  title: ''
  type: Hosts
  url: hosts/listbulb-hosts.yml
- group: other
  href: https://artifacts.apis.io/listbulb/vendors/listbulb-vendors.yml
  title: ''
  type: Vendors
  url: vendors/listbulb-vendors.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hakimuddinkika
- group: start
  title: ''
  type: GettingStarted
  url: https://www.listbulb.com/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/listbulb/security/listbulb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/listbulb-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://listbulb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://listbulb.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://listbulb.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://listbulb.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://listbulb.com/blog
- group: operate
  title: ''
  type: Changelog
  url: https://listbulb.com/changelog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://listbulb.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://listbulb.com/privacy-policy
coverage:
  checked: '2026-10-18'
  detail: API documentation provides limits and errors but no OpenAPI or other machine-readable contract.
  evidence:
  - status: 200
    url: https://listbulb.com/docs/api/reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: List Bulb is a hand‑reviewed AI and SaaS directory that helps founders and product teams discover, launch, and promote their tools. The platform offers a searchable catalog, pricing information, and a developer portal with an MCP server and OpenAPI spec for integration. It also provides blog content, changelog, and resources for AI agents and crawlers, aiming to increase visibility through dofollow backlinks and community engagement.
image: https://www.listbulb.com/og-image.png?v=56b7d08e
json_schemas:
- name: GetApiV1CategoriesResponse
  property_count: 1
  slug: listbulb-get-api-v1-categories-response
- name: GetApiV1OpenapiJsonResponse
  property_count: 1
  slug: listbulb-get-api-v1-openapi-json-response
- name: GetApiV1ToolsResponse
  property_count: 1
  slug: listbulb-get-api-v1-tools-response
- name: GetApiV1ToolsSlugResponse
  property_count: 13
  slug: listbulb-get-api-v1-tools-slug-response
- name: PostApiV1ToolsRequest
  property_count: 6
  slug: listbulb-post-api-v1-tools-request
- name: PostApiV1ToolsResponse
  property_count: 2
  slug: listbulb-post-api-v1-tools-response
jsonld:
- class_count: 6
  name: Listbulb Context
  property_count: 20
  slug: listbulb-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.listbulb.com.
  name: List Bulb MCP Server
  slug: listbulb-mcp-yml
modified: '2026-10-18'
name: List Bulb
nav: Providers
network: true
overview: 'List Bulb is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Software-as-a-Service, Directory, and Startups.


  The List Bulb catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  List Bulb''s developer surface includes changelog, authentication, getting-started guide, documentation, API reference, pricing, engineering blog, and 19 more developer resources.'
plans:
- name: Listbulb Plans Pricing
  plan_count: 3
  slug: listbulb-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: List Bulb API Rules
  rule_count: 13
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 0
  slug: listbulb-rules
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.0
    catalog_earned_first_party: 12.0
    catalog_gap: 46.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 19.7
    contract_quality: 24.8
    developer_ergonomics: 42.9
    discoverability: 56.7
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: first-party
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
  name: Listbulb Authentication
  slug: listbulb-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Listbulb Domain Security
  slug: listbulb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: listbulb
tags:
- Company
- Artificial Intelligence
- Software-as-a-Service
- Directory
- Startups
website: https://listbulb.com/
---
