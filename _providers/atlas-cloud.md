---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.1
  scored_at: '2026-10-17'
api_count: 10
apis:
- baseURL: https://api.atlascloud.ai
  baseurl_source: declared
  description: The Balance API from Atlas Cloud — 1 operation(s) for balance.
  name: Atlas Cloud Balance API
  slug: atlas-cloud-balance-api
- baseURL: https://api.atlascloud.ai
  baseurl_source: declared
  description: The Completions API from Atlas Cloud — 1 operation(s) for completions.
  name: Atlas Cloud Completions API
  slug: atlas-cloud-completions-api
- baseURL: https://api.atlascloud.ai
  baseurl_source: declared
  description: The Images API from Atlas Cloud — 1 operation(s) for images.
  name: Atlas Cloud Images API
  slug: atlas-cloud-images-api
- baseURL: https://api.atlascloud.ai
  baseurl_source: declared
  description: The Messages API from Atlas Cloud — 1 operation(s) for messages.
  name: Atlas Cloud Messages API
  slug: atlas-cloud-messages-api
- baseURL: https://api.atlascloud.ai
  baseurl_source: declared
  description: The Model API from Atlas Cloud — 3 operation(s) for model.
  name: Atlas Cloud Model API
  slug: atlas-cloud-model-api
- baseURL: https://api.atlascloud.ai
  baseurl_source: declared
  description: The Model Costs API from Atlas Cloud — 1 operation(s) for model costs.
  name: Atlas Cloud Model Costs API
  slug: atlas-cloud-model-costs-api
- baseURL: https://api.atlascloud.ai
  baseurl_source: declared
  description: The Model Usage API from Atlas Cloud — 1 operation(s) for model usage.
  name: Atlas Cloud Model Usage API
  slug: atlas-cloud-model-usage-api
- baseURL: https://api.atlascloud.ai
  baseurl_source: declared
  description: The V1Beta API from Atlas Cloud — 1 operation(s) for v1beta.
  name: Atlas Cloud V1Beta API
  slug: atlas-cloud-v1beta-api
- baseURL: https://api.atlascloud.ai
  baseurl_source: declared
  description: The Webhooks API from Atlas Cloud — 1 operation(s) for webhooks.
  name: Atlas Cloud Webhooks API
  slug: atlas-cloud-webhooks-api
- baseURL: https://api.atlascloud.ai
  baseurl_source: declared
  description: The Chat Completions API from Atlas Cloud — 2 operation(s) for chat completions.
  name: Atlas Cloud Chat Completions API
  slug: atlas-cloud-chat-completions-api
artifact_total: 24
asyncapis:
- description: ''
  name: Atlas Cloud Webhooks
  slug: atlas-cloud-webhooks
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/authentication/atlas-cloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/atlas-cloud-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/rate-limits/atlas-cloud-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/atlas-cloud-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/plans/atlas-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/atlas-cloud-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/rules/atlas-cloud-rules.yml
  title: ''
  type: Spectral
  url: rules/atlas-cloud-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/json-ld/atlas-cloud-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/atlas-cloud-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/vocabulary/atlas-cloud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/atlas-cloud-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/asyncapi/atlas-cloud-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/atlas-cloud-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/data-model/atlas-cloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/atlas-cloud-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/cli/atlas-cloud-cli.yml
  title: ''
  type: CLI
  url: cli/atlas-cloud-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/changelog/atlas-cloud-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/atlas-cloud-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/conventions/atlas-cloud-conventions.yml
  title: ''
  type: Conventions
  url: conventions/atlas-cloud-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/errors/atlas-cloud-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/atlas-cloud-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/conformance/atlas-cloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/atlas-cloud-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/llms/atlas-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atlas-cloud-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/mcp/atlas-cloud-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/atlas-cloud-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/mcp/atlas-cloud-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/atlas-cloud-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/hosts/atlas-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlas-cloud-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/integrations/atlas-cloud-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/atlas-cloud-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/vendors/atlas-cloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atlas-cloud-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/packages/atlas-cloud-packages.yml
  title: ''
  type: SDKs
  url: packages/atlas-cloud-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/packages/atlas-cloud-packages.yml
  title: ''
  type: Packages
  url: packages/atlas-cloud-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://www.atlascloud.ai/console
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atlas-cloud/refs/heads/main/security/atlas-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlas-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atlascloud.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.atlascloud.ai/developer
- group: docs
  title: ''
  type: Documentation
  url: https://www.atlascloud.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.atlascloud.ai/docs/openapi-index
- group: start
  title: ''
  type: GettingStarted
  url: https://www.atlascloud.ai/docs/get-started
- group: operate
  title: ''
  type: Support
  url: https://www.atlascloud.ai/docs/contact
- group: company
  title: ''
  type: Blog
  url: https://www.atlascloud.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AtlasCloudAI
- group: commercial
  title: ''
  type: Pricing
  url: https://www.atlascloud.ai/docs/models/price
- group: start
  title: ''
  type: Login
  url: https://www.atlascloud.ai/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atlascloud.ai/docs/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.atlascloud.ai/docs/changelog
- group: company
  title: ''
  type: Newsroom
  url: https://www.atlascloud.ai/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atlascloud.ai/privacy
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.atlascloud.ai
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: 'Atlas Cloud is an AI inference platform that serves 300+ third-party LLM, image, video, audio and 3D models through one API: an OpenAI-compatible chat completions surface at https://api.atlascloud.ai/v1 (plus Anthropic Messages and Gemini protocols), asynchronous image and video generation with prediction polling and signed webhooks at https://api.atlascloud.ai/api/v1, and a Billing Public API for balance, usage and cost at https://api.atlascloud.ai/public/v1. It also sells GPU cloud, bare-metal servers and storage, and ships an official MCP server, CLI and agent skills.'
image: https://www.atlascloud.ai/favicon.ico
json_schemas:
- name: GetApiV1WebhooksJwksJsonResponse
  property_count: 7
  slug: atlas-cloud-get-api-v1-webhooks-jwks-json-response
- name: PostChatCompletionsRequest
  property_count: 6
  slug: atlas-cloud-post-chat-completions-request
- name: PostChatCompletionsResponse
  property_count: 2
  slug: atlas-cloud-post-chat-completions-response
- name: PostV1ChatCompletionsRequest
  property_count: 4
  slug: atlas-cloud-post-v1-chat-completions-request
- name: PostV1V1IdRequest
  property_count: 3
  slug: atlas-cloud-post-v1-v1-id-request
- name: PostV1V1IdResponse
  property_count: 3
  slug: atlas-cloud-post-v1-v1-id-response
jsonld:
- class_count: 22
  name: Atlas Cloud Context
  property_count: 42
  slug: atlas-cloud-context
layout: provider
mcp_servers:
- description: MCP server requiring an API key; 13 tools listed.
  name: Atlas Cloud MCP Server
  slug: atlas-cloud-mcp-server
modified: '2026-10-13'
name: Atlas Cloud
nav: Providers
network: true
overview: 'Atlas Cloud is listed with 10 APIs on the [APIs.io](https://apis.io/) network, including Balance API, Completions API, Images API, and 7 more. Tagged areas include Company, Artificial Intelligence, LLM, Model Routing, and Image Generation.


  The Atlas Cloud catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Atlas Cloud''s developer surface includes authentication, CLI, changelog, sandbox, documentation, API reference, getting-started guide, and 31 more developer resources.'
plans:
- name: Atlas Cloud Plans Pricing
  plan_count: 2
  slug: atlas-cloud-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 2
  name: Atlas Cloud Rate Limits
  slug: atlas-cloud-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Atlas Cloud API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 1
  slug: atlas-cloud-rules
score:
  band: strong
  composite: 54.5
  coverage:
    artifact_dirs: 24
    catalog_earned: 81.8
    catalog_earned_first_party: 16.0
    catalog_gap: 33.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 33.3
    developer_ergonomics: 80.4
    discoverability: 78.3
    operational_transparency: 50.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 11
      marker_coverage: 100.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Atlas Cloud Authentication
  slug: atlas-cloud-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Atlas Cloud Domain Security
  slug: atlas-cloud-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: atlas-cloud
tags:
- Company
- Artificial Intelligence
- LLM
- Model Routing
- Image Generation
- Video Generation
- Inference
- GPU Cloud
- MCP
website: https://www.atlascloud.ai
---
