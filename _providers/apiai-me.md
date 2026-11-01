---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Complete reference for the apiai.me API pipelines and AI orchestration platform. Authentication, image generation, background removal, pipeline orchestration, batch processing, and MCP integration — w
  name: apiai.me API
  slug: apiai-me-api-2
- description: 'apiai-me API as documented publicly: 103 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: apiai-me API
  slug: apiai-me-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/apiai-me/rules/apiai-me-rules.yml
  title: ''
  type: Spectral
  url: rules/apiai-me-rules.yml
- group: design
  href: https://artifacts.apis.io/apiai-me/json-ld/apiai-me-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apiai-me-context.jsonld
- group: design
  href: https://artifacts.apis.io/apiai-me/vocabulary/apiai-me-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apiai-me-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/apiai-me/data-model/apiai-me-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apiai-me-data-model.yml
- group: design
  href: https://artifacts.apis.io/apiai-me/conformance/apiai-me-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apiai-me-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apiai-me/llms/apiai-me-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apiai-me-llms.txt
- group: agent
  href: https://artifacts.apis.io/apiai-me/mcp/apiai-me-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apiai-me-mcp.yml
- group: agent
  href: https://artifacts.apis.io/apiai-me/well-known/apiai-me-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apiai-me-well-known.yml
- group: other
  href: https://artifacts.apis.io/apiai-me/hosts/apiai-me-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apiai-me-hosts.yml
- group: other
  href: https://artifacts.apis.io/apiai-me/vendors/apiai-me-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apiai-me-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://apiai.me/articles/category/media
- group: auth
  href: https://artifacts.apis.io/apiai-me/security/apiai-me-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apiai-me-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apiai.me/
- group: docs
  title: ''
  type: Documentation
  url: https://apiai.me/docs
- group: docs
  title: ''
  type: APIReference
  url: https://apiai.me/docs
- group: operate
  title: ''
  type: Support
  url: https://apiai.me/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://apiai.me/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apiai.me/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apiai.me/privacy
- group: start
  title: ''
  type: SignUp
  url: https://apiai.me/dashboard
created: '2026-10-30'
description: apiai.me provides an API‑first platform that lets developers chain together AI models, deterministic tools, and quality‑check steps into a single pipeline. With a single REST call you can invoke image generation, background removal, video creation, and custom model orchestration, receiving finished assets instantly. The service offers a dashboard for building pipelines visually and a robust API for programmatic integration, targeting AI‑driven applications and automation workflows.
image: https://apiai.me/static/assets/og-image.png?v=2
json_schemas:
- name: GetApiV1WorkflowsResponse
  property_count: 13
  slug: apiai-me-get-api-v1-workflows-response
- name: GetWorkflowsResponse
  property_count: 13
  slug: apiai-me-get-workflows-response
- name: PostApiV1QualityGateResponse
  property_count: 8
  slug: apiai-me-post-api-v1-quality-gate-response
- name: PostFlowsRequest
  property_count: 5
  slug: apiai-me-post-flows-request
- name: PostQualityGateRequest
  property_count: 5
  slug: apiai-me-post-quality-gate-request
- name: PostV1EvalRunRequest
  property_count: 5
  slug: apiai-me-post-v1-eval-run-request
jsonld:
- class_count: 59
  name: Apiai Me Context
  property_count: 62
  slug: apiai-me-context
layout: provider
mcp_servers:
- description: Remote MCP server at apiai.me.
  name: apiai-me MCP Server
  slug: apiai-me-mcp-yml
modified: '2026-10-30'
name: apiai-me
nav: Providers
network: true
overview: 'apiai-me is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Orchestration, Automation, and Platform.


  The apiai-me catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  apiai-me''s developer surface includes documentation, API reference, support, pricing, signup flow, and 15 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 0
  name: Apiai Me Rate Limits
  slug: apiai-me-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: apiai-me API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: apiai-me-rules
score:
  band: developing
  composite: 41.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 72.7
    catalog_earned_first_party: 0.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 79.1
    contract_quality: 45.6
    developer_ergonomics: 21.4
    discoverability: 58.3
    operational_transparency: 0.0
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
- kind: domain-security
  name: Apiai Me Domain Security
  slug: apiai-me-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apiai-me
tags:
- Company
- AI
- Orchestration
- Automation
- Platform
website: https://apiai.me/
---
