---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
  score: 35.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Pixapi provides image and video generation endpoints. Base URL https://api.pixapi.ai/v1.
  name: Pixapi API
  slug: pixapi-api
- baseURL: https://api.pixapi.ai
  baseurl_source: declared
  description: 'pixapi-ai API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: pixapi-ai API
  slug: pixapi-ai-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/pixapi-ai/rules/pixapi-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/pixapi-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/pixapi-ai/json-ld/pixapi-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pixapi-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/pixapi-ai/vocabulary/pixapi-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pixapi-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/pixapi-ai/data-model/pixapi-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pixapi-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/pixapi-ai/authentication/pixapi-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pixapi-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/pixapi-ai/conformance/pixapi-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pixapi-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pixapi-ai/llms/pixapi-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pixapi-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/pixapi-ai/mcp/pixapi-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pixapi-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/pixapi-ai/well-known/pixapi-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pixapi-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/pixapi-ai/hosts/pixapi-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pixapi-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/pixapi-ai/vendors/pixapi-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pixapi-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/pixapi-ai/packages/pixapi-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/pixapi-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/pixapi-ai/packages/pixapi-ai-packages.yml
  title: ''
  type: Packages
  url: packages/pixapi-ai-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pixapi.ai/terms-of-service
- group: start
  title: ''
  type: Sandbox
  url: https://pixapi.ai/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pixapi.ai/privacy-policy
- group: auth
  href: https://artifacts.apis.io/pixapi-ai/security/pixapi-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pixapi-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pixapi.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://pixapi.ai/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://pixapi.ai/docs/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://pixapi.ai/docs/develop/
- group: company
  title: ''
  type: Blog
  url: https://pixapi.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://pixapi.ai/pricing
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI/AsyncAPI/GraphQL spec found on the provider's documentation or API host.
  evidence:
  - status: 200
    url: https://pixapi.ai/docs/api-reference/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Pixapi AI provides a unified visual AI platform that offers image and video generation through a single API key. It aggregates multiple models such as Nano Banana, GPT Image, Seedance, and Kling, delivering consistent request formats, credit‑based billing (1 credit = $0.01), and a developer console for monitoring usage. The service abstracts upstream provider authentication, enabling developers to integrate diverse generative models without managing separate accounts.
image: https://pixapi.ai/logo.png
json_schemas:
- name: PostV1AsyncImagesEditsRequest
  property_count: 5
  slug: pixapi-ai-post-v1-async-images-edits-request
- name: PostV1AsyncImagesEditsResponse
  property_count: 2
  slug: pixapi-ai-post-v1-async-images-edits-response
- name: PostV1AsyncImagesGenerationsRequest
  property_count: 2
  slug: pixapi-ai-post-v1-async-images-generations-request
- name: PostV1AsyncVideosGenerationsRequest
  property_count: 4
  slug: pixapi-ai-post-v1-async-videos-generations-request
- name: PostV1ImagesEditsRequest
  property_count: 5
  slug: pixapi-ai-post-v1-images-edits-request
- name: PostV1ImagesGenerationsRequest
  property_count: 4
  slug: pixapi-ai-post-v1-images-generations-request
jsonld:
- class_count: 9
  name: Pixapi Ai Context
  property_count: 12
  slug: pixapi-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.pixapi.ai requiring OAuth.
  name: pixapi-ai MCP Server
  slug: pixapi-ai-mcp-yml
modified: '2026-10-30'
name: pixapi-ai
nav: Providers
network: true
overview: 'pixapi-ai is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Image Generation, Video Generation, and Machine Learning.


  The pixapi-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  pixapi-ai''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, engineering blog, pricing, and 16 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: pixapi-ai API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: pixapi-ai-rules
scopes:
- name: Pixapi Ai Scopes
  scope_count: 0
  slug: pixapi-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 38.1
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 35.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pixapi-ai/pixapi-ai-2026-11-03T141244.png
security:
- kind: authentication
  name: Pixapi Ai Authentication
  slug: pixapi-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Pixapi Ai Domain Security
  slug: pixapi-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pixapi-ai
tags:
- Artificial Intelligence
- Image Generation
- Video Generation
- Machine Learning
website: https://pixapi.ai/
---
