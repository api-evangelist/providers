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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Run BiOS REST API basics including base URL, authentication, error response format, rate limits, and common status codes.
  name: Run BiOS REST API
  slug: run-bios-rest-api
- baseURL: https://api.runbios.ai
  baseurl_source: declared
  description: 'UltraSafe AI API as documented publicly: 62 operations. Contract generated from the documentation by API Evangelist (2026-10-18); not the provider''s own document.'
  name: UltraSafe AI API
  slug: runbios-api
artifact_total: 12
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://runbios.ai/get-started/
- group: design
  href: https://artifacts.apis.io/runbios/rules/runbios-rules.yml
  title: ''
  type: Spectral
  url: rules/runbios-rules.yml
- group: design
  href: https://artifacts.apis.io/runbios/json-ld/runbios-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/runbios-context.jsonld
- group: design
  href: https://artifacts.apis.io/runbios/vocabulary/runbios-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/runbios-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/runbios/data-model/runbios-data-model.yml
  title: ''
  type: DataModel
  url: data-model/runbios-data-model.yml
- group: auth
  href: https://artifacts.apis.io/runbios/authentication/runbios-authentication.yml
  title: ''
  type: Authentication
  url: authentication/runbios-authentication.yml
- group: design
  href: https://artifacts.apis.io/runbios/conformance/runbios-conformance.yml
  title: ''
  type: Conformance
  url: conformance/runbios-conformance.yml
- group: agent
  href: https://artifacts.apis.io/runbios/llms/runbios-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/runbios-llms.txt
- group: agent
  href: https://artifacts.apis.io/runbios/well-known/runbios-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/runbios-well-known.yml
- group: other
  href: https://artifacts.apis.io/runbios/hosts/runbios-hosts.yml
  title: ''
  type: Hosts
  url: hosts/runbios-hosts.yml
- group: other
  href: https://artifacts.apis.io/runbios/vendors/runbios-vendors.yml
  title: ''
  type: Vendors
  url: vendors/runbios-vendors.yml
- group: auth
  href: https://artifacts.apis.io/runbios/security/runbios-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/runbios-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://runbios.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.runbios.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://platform.runbios.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://platform.runbios.ai/docs/api-overview
- group: operate
  title: ''
  type: Support
  url: https://platform.runbios.ai/docs/support
- group: company
  title: ''
  type: Blog
  url: https://runbios.ai/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://runbios.ai/pricing-calculator/
- group: start
  title: ''
  type: SignUp
  url: https://platform.runbios.ai/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://runbios.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://runbios.ai/privacy/
coverage:
  detail: API documentation is rendered via JavaScript and no machine‑readable OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://platform.runbios.ai/docs/api-overview
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: UltraSafe AI, operating under the brand Run BiOS, provides an enterprise AI platform offering training, serverless inference, evaluation, data generation, and continuous model improvement. The platform enables enterprises to manage AI workloads with reliability, control, and scale, either as a managed service or deployed within their own cloud or data center. Run BiOS is a product of UltraSafe AI, delivering end‑to‑end AI stack solutions for high‑performance inference and fine‑tuning.
image: https://runbios.ai/opengraph-image.png?8dbb4b60692716af
json_schemas:
- name: GetApiLoopTracesResponse
  property_count: 2
  slug: runbios-get-api-loop-traces-response
- name: GetApiModelsResponse
  property_count: 15
  slug: runbios-get-api-models-response
- name: GetV1ChatCompletionsResponse
  property_count: 1
  slug: runbios-get-v1-chat-completions-response
- name: PostApiLoopPipelinesRequest
  property_count: 2
  slug: runbios-post-api-loop-pipelines-request
- name: PostV1ChatCompletionsRequest
  property_count: 2
  slug: runbios-post-v1-chat-completions-request
- name: PutApiLoopConfigsDeploymentidRequest
  property_count: 4
  slug: runbios-put-api-loop-configs-deploymentid-request
jsonld:
- class_count: 7
  name: Runbios Context
  property_count: 26
  slug: runbios-context
layout: provider
modified: '2026-10-18'
name: UltraSafe AI
nav: Providers
network: true
overview: 'UltraSafe AI is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Enterprise, Platform, and Training.


  The UltraSafe AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  UltraSafe AI''s developer surface includes getting-started guide, authentication, documentation, API reference, support, engineering blog, pricing, and 15 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: UltraSafe AI API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: runbios-rules
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 57.1
    discoverability: 66.1
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
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Runbios Authentication
  slug: runbios-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Runbios Domain Security
  slug: runbios-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: runbios
tags:
- Company
- Artificial Intelligence
- Enterprise
- Platform
- Training
- Inference
website: https://runbios.ai/
---
