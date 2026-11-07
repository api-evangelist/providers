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
  band: agent-ready
  dimensions:
    agent_card: false
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.datamcp.app/api
  baseurl_source: declared
  description: 'datamcp API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: datamcp API
  slug: datamcp-app-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/datamcp-app/plans/datamcp-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datamcp-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/datamcp-app/rules/datamcp-app-rules.yml
  title: ''
  type: Spectral
  url: rules/datamcp-app-rules.yml
- group: design
  href: https://artifacts.apis.io/datamcp-app/json-ld/datamcp-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/datamcp-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/datamcp-app/vocabulary/datamcp-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datamcp-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/datamcp-app/data-model/datamcp-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/datamcp-app-data-model.yml
- group: operate
  href: https://artifacts.apis.io/datamcp-app/changelog/datamcp-app-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/datamcp-app-changelog.yml
- group: auth
  href: https://artifacts.apis.io/datamcp-app/authentication/datamcp-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datamcp-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/datamcp-app/conformance/datamcp-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datamcp-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/datamcp-app/llms/datamcp-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datamcp-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/datamcp-app/well-known/datamcp-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datamcp-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/datamcp-app/hosts/datamcp-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datamcp-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/datamcp-app/vendors/datamcp-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datamcp-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datamcp.app/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://datamcp.app/support
- group: operate
  title: ''
  type: Roadmap
  url: https://datamcp.app/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datamcp.app/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://datamcp.app/pricing
- group: start
  title: ''
  type: Login
  url: https://dashboard.datamcp.app/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://datamcp.app/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://datamcp.app/changelog
- group: company
  title: ''
  type: Blog
  url: https://datamcp.app/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://datamcp.app/docs/zapier
- group: auth
  href: https://artifacts.apis.io/datamcp-app/security/datamcp-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datamcp-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datamcp.app/
coverage:
  checked: '2026-11-05'
  detail: Documentation pages are rendered via JavaScript and no machine‑readable OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 200
    url: https://datamcp.app/docs/integration-api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-05'
description: datamcp provides hosted Model Context Protocol endpoints for PostgreSQL 12+, MySQL, OpenAPI and Swagger APIs, and shared Agent Memory, plus an outbound Local Agent Tunnel for private PostgreSQL and an official connector available in Claude. It offers services such as PostgreSQL MCP Server, MySQL MCP Server, OpenAPI to MCP conversion, and hosted Agent Memory, enabling developers to create secure, managed data access layers and integrate AI agents with private databases.
image: https://datamcp.app/opengraph-image?6a74644d540ec4f1
json_schemas:
- name: GetIntegrationCredentialsResponse
  property_count: 2
  slug: datamcp-app-get-integration-credentials-response
- name: GetIntegrationsV1SourcesResponse
  property_count: 8
  slug: datamcp-app-get-integrations-v1-sources-response
- name: PostIntegrationCredentialsRequest
  property_count: 5
  slug: datamcp-app-post-integration-credentials-request
- name: PostIntegrationCredentialsResponse
  property_count: 3
  slug: datamcp-app-post-integration-credentials-response
- name: PostIntegrationsV1SourcesSourceidQueryRequest
  property_count: 3
  slug: datamcp-app-post-integrations-v1-sources-sourceid-query-request
- name: PostIntegrationsV1SourcesSourceidQueryResponse
  property_count: 6
  slug: datamcp-app-post-integrations-v1-sources-sourceid-query-response
jsonld:
- class_count: 7
  name: Datamcp App Context
  property_count: 15
  slug: datamcp-app-context
layout: provider
modified: '2026-11-05'
name: datamcp
nav: Providers
network: true
overview: 'datamcp is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Database, MCP, OpenAPI, and Artificial Intelligence.


  The datamcp catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  datamcp''s developer surface includes changelog, authentication, support, pricing, documentation, engineering blog, getting-started guide, and 17 more developer resources.'
plans:
- name: Datamcp App Plans Pricing
  plan_count: 4
  slug: datamcp-app-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: datamcp API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: datamcp-app-rules
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 25.5
    developer_ergonomics: 40.5
    discoverability: 57.1
    operational_transparency: 21.1
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
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Datamcp App Authentication
  slug: datamcp-app-authentication
  summary_line: 6 schemes
- kind: domain-security
  name: Datamcp App Domain Security
  slug: datamcp-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: datamcp-app
tags:
- Database
- MCP
- OpenAPI
- Artificial Intelligence
website: https://datamcp.app/
---
