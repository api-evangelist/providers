---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Appbricx platform API as documented
  name: Appbricx API
  slug: appbricx-api
- description: 'Appbricx API as documented publicly: 126 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Appbricx API
  slug: appbricx-com-api
artifact_total: 13
asyncapis:
- description: ''
  name: Appbricx Com Webhooks
  slug: appbricx-com-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/appbricx-com/plans/appbricx-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appbricx-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/appbricx-com/rules/appbricx-com-rules.yml
  title: ''
  type: Spectral
  url: rules/appbricx-com-rules.yml
- group: design
  href: https://artifacts.apis.io/appbricx-com/json-ld/appbricx-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/appbricx-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/appbricx-com/vocabulary/appbricx-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/appbricx-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/appbricx-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/appbricx-com/asyncapi/appbricx-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/appbricx-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/appbricx-com/data-model/appbricx-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/appbricx-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/appbricx-com/conformance/appbricx-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appbricx-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/appbricx-com/llms/appbricx-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appbricx-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/appbricx-com/well-known/appbricx-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appbricx-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/appbricx-com/hosts/appbricx-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appbricx-com-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://appbricx.com/login
- group: docs
  title: ''
  type: APIReference
  url: https://appbricx.com/docs/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://appbricx.com/docs/quickstart/agent
- group: auth
  href: https://artifacts.apis.io/appbricx-com/security/appbricx-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appbricx-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appbricx.com/
- group: docs
  title: ''
  type: Documentation
  url: https://appbricx.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://appbricx.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://appbricx.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appbricx.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appbricx.com/privacy
coverage:
  checked: '2026-11-01'
  detail: Documentation pages are HTML without a downloadable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec.
  evidence:
  - status: 200
    url: https://appbricx.com/docs/reference
  - status: 200
    url: https://appbricx.com/docs/rest-api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Appbricx provides an AI‑driven platform that lets developers build, test, and ship applications using agents like Claude, Code, or custom MCP clients. It supports TypeScript, React, SQL, and offers features such as real‑time data, authentication, team collaboration, payments, workflows, serverless functions, and self‑hosting. The service includes a data API, webhooks, and integrations, targeting agencies, freelancers, and internal tools teams.
image: https://appbricx.com/opengraph-image
json_schemas:
- name: PostApiDevV1ProjectsIdDataExportRequest
  property_count: 8
  slug: appbricx-com-post-api-dev-v1-projects-id-data-export-request
- name: PostApiDevV1ProjectsIdDataImportRequest
  property_count: 10
  slug: appbricx-com-post-api-dev-v1-projects-id-data-import-request
- name: PostApiDevV1ProjectsIdDataQueryRequest
  property_count: 13
  slug: appbricx-com-post-api-dev-v1-projects-id-data-query-request
- name: PostApiDevV1ProjectsIdRowsRequest
  property_count: 11
  slug: appbricx-com-post-api-dev-v1-projects-id-rows-request
- name: PostApiDevV1ProjectsIdScreenshotRequest
  property_count: 8
  slug: appbricx-com-post-api-dev-v1-projects-id-screenshot-request
- name: PostApiDevV1ProjectsIdScreenshotResponse
  property_count: 8
  slug: appbricx-com-post-api-dev-v1-projects-id-screenshot-response
jsonld:
- class_count: 58
  name: Appbricx Com Context
  property_count: 104
  slug: appbricx-com-context
layout: provider
modified: '2026-11-01'
name: Appbricx
nav: Providers
network: true
overview: 'Appbricx is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Platform, Development, and Automation.


  The Appbricx catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Appbricx''s developer surface includes API reference, getting-started guide, documentation, pricing, engineering blog, and 16 more developer resources.'
plans:
- name: Appbricx Com Plans Pricing
  plan_count: 5
  slug: appbricx-com-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: Appbricx API Rules
  rule_count: 38
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 2
  slug: appbricx-com-rules
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 35.0
    developer_ergonomics: 21.9
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 42.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Appbricx Com Domain Security
  slug: appbricx-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: appbricx-com
tags:
- Company
- Artificial Intelligence
- Platform
- Development
- Automation
website: https://appbricx.com/
---
