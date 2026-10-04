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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.9
  scored_at: '2026-10-03'
api_count: 4
apis:
- description: Unified REST API for AI model generation, image, video, audio, and text. Provides endpoints for model listing, generation submission, result polling, face swap, moderation, and error codes.
  name: AirCube API
  slug: aircube-api-2
- baseURL: https://api.aircube.ai
  baseurl_source: declared
  description: The AirCube API API from AirCube — 1 operation(s) for aircube api.
  name: AirCube AirCube API
  slug: aircube-aircube-api-api
- baseURL: https://api.aircube.ai
  baseurl_source: declared
  description: The Models API from AirCube — 2 operation(s) for models.
  name: AirCube Models API
  slug: aircube-models-api
- baseURL: https://api.aircube.ai
  baseurl_source: declared
  description: The Qwen Image API from AirCube — 1 operation(s) for qwen image.
  name: AirCube Qwen Image API
  slug: aircube-qwen-image-api
artifact_total: 12
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aircube/refs/heads/main/plans/aircube-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aircube-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aircube/refs/heads/main/rules/aircube-rules.yml
  title: ''
  type: Spectral
  url: rules/aircube-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aircube/refs/heads/main/json-ld/aircube-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aircube-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aircube/refs/heads/main/vocabulary/aircube-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aircube-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aircube/refs/heads/main/data-model/aircube-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aircube-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aircube/refs/heads/main/authentication/aircube-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aircube-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aircube/refs/heads/main/errors/aircube-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aircube-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aircube/refs/heads/main/conformance/aircube-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aircube-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aircube/refs/heads/main/llms/aircube-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aircube-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aircube/refs/heads/main/hosts/aircube-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aircube-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aircube/refs/heads/main/vendors/aircube-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aircube-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aircube/refs/heads/main/security/aircube-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aircube-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aircube.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://aircube.ai/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aircube.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://aircube.ai/docs/api-reference/submit-generation
- group: start
  title: ''
  type: GettingStarted
  url: https://aircube.ai/docs/getting-started/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://aircube.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://aircube.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aircube.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aircube.ai/legal/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://aircube.ai/login
coverage:
  checked: 2026-09-25
  detail: API documentation pages are rendered as HTML with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://aircube.ai/docs/api-reference/submit-generation
  - status: 0
    url: https://api.aircube.ai/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-25'
description: AirCube provides a unified API platform that gives developers access to over 450 AI models across image, video, audio, and text domains. Through a single REST endpoint and API key, users can generate media, synthesize speech, and run advanced model inference without managing multiple vendor integrations. The service offers free tier access, transparent usage‑based pricing, and enterprise features such as high‑availability scaling and dedicated support.
image: https://aircube.ai/opengraph-image
json_schemas:
- name: PostApiV3QwenImageEdit2511ImageEditingRequest
  property_count: 2
  slug: aircube-post-api-v3-qwen-image-edit2511-image-editing-request
- name: PostApiV3V3IdRequest
  property_count: 2
  slug: aircube-post-api-v3-v3-id-request
- name: PostApiV3V3IdResponse
  property_count: 2
  slug: aircube-post-api-v3-v3-id-response
jsonld:
- class_count: 3
  name: Aircube Context
  property_count: 6
  slug: aircube-context
layout: provider
modified: '2026-09-25'
name: AirCube
nav: Providers
network: true
overview: 'AirCube publishes 4 APIs on the [APIs.io](https://apis.io/) network, including AirCube API, Models API, Qwen Image API, and 1 more. Tagged areas include Artificial Intelligence, Platform, Media Generation, and Unified API.


  The AirCube catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AirCube''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, and 15 more developer resources.'
plans:
- name: Aircube Plans Pricing
  plan_count: 2
  slug: aircube-plans-pricing
random_paper: 5
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: AirCube API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: aircube-rules
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 8.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 20.3
    developer_ergonomics: 52.4
    discoverability: 69.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Aircube Authentication
  slug: aircube-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Aircube Domain Security
  slug: aircube-domain-security
  summary_line: TLSv1.3
slug: aircube
tags:
- Artificial Intelligence
- Platform
- Media Generation
- Unified API
website: https://aircube.ai/
---
