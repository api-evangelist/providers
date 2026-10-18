---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Aihubmix Agentic Access
  operation_count: 30
  slug: aihubmix-agentic-access
  summary_line: 30 operations · 16 acting
api_count: 3
apis:
- baseURL: https://aihubmix.com
  baseurl_source: spec
  description: AIHubMix native image, video, task, and model-discovery endpoints.
  name: AIHubMix AIHubMix Unified API
  slug: aihubmix-aihubmix-unified-api-api
- baseURL: https://aihubmix.com
  baseurl_source: spec
  description: Anthropic-native endpoints (messages with Anthropic protocol).
  name: AIHubMix Anthropic Compatible API
  slug: aihubmix-anthropic-compatible-api
- baseURL: https://aihubmix.com
  baseurl_source: spec
  description: Google Gemini / Vertex AI endpoints.
  name: AIHubMix Google Vertex AI Compatible API
  slug: aihubmix-google-vertex-ai-compatible-api
- baseURL: https://aihubmix.com
  baseurl_source: spec
  description: OpenAI-compatible endpoints (chat, completions, embeddings, images, audio, videos, moderations).
  name: AIHubMix OpenAI Compatible API
  slug: aihubmix-openai-compatible-api
artifact_total: 16
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aihubmix/refs/heads/main/agentic-access/aihubmix-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aihubmix-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aihubmix/refs/heads/main/rules/aihubmix-rules.yml
  title: ''
  type: Spectral
  url: rules/aihubmix-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aihubmix/refs/heads/main/json-ld/aihubmix-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aihubmix-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aihubmix/refs/heads/main/vocabulary/aihubmix-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aihubmix-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aihubmix/refs/heads/main/data-model/aihubmix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aihubmix-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aihubmix/refs/heads/main/cli/aihubmix-cli.yml
  title: ''
  type: CLI
  url: cli/aihubmix-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aihubmix/refs/heads/main/errors/aihubmix-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aihubmix-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aihubmix/refs/heads/main/conformance/aihubmix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aihubmix-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aihubmix/refs/heads/main/llms/aihubmix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aihubmix-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aihubmix/refs/heads/main/a2a/aihubmix-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aihubmix-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aihubmix/refs/heads/main/well-known/aihubmix-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aihubmix-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aihubmix/refs/heads/main/hosts/aihubmix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aihubmix-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aihubmix/refs/heads/main/vendors/aihubmix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aihubmix-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aihubmix/refs/heads/main/packages/aihubmix-packages.yml
  title: ''
  type: SDKs
  url: packages/aihubmix-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aihubmix/refs/heads/main/packages/aihubmix-packages.yml
  title: ''
  type: Packages
  url: packages/aihubmix-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aihubmix/refs/heads/main/authentication/aihubmix-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aihubmix-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aihubmix/refs/heads/main/security/aihubmix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aihubmix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aihubmix.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aihubmix.com/en
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aihubmix.com/en/api-reference/openai-compatible/create-a-chat-completion
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aihubmix.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aihubmix.com/en/quick-start
- group: company
  title: ''
  type: Blog
  url: https://aihubmix.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.aihubmix.com/en/update/News
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AIhubmix
- group: start
  title: ''
  type: Login
  url: https://console.aihubmix.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aihubmix.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aihubmix.com/legal/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aihubmix.com
- group: other
  title: ''
  type: Playground
  url: https://playground.aihubmix.com
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.aihubmix.com/llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: https://aihubmix.com/mcp
created: '2026-10-13'
description: AIHubMix is an AI model routing gateway that exposes hundreds of large language, image, video and audio models from many vendors behind one API key, with OpenAI-compatible, Anthropic-compatible and Google Gemini/Vertex-compatible endpoints plus its own unified image, video and task APIs, pay-as-you-go billing, a remote MCP server, a command-line tool and agent skills.
image: https://aihubmix.com/og/default.png
json_schemas:
- name: CreateMessageParams
  property_count: 18
  slug: aihubmix-anthropic-create-message-params
- name: CreateChatCompletionRequest
  property_count: 1
  slug: aihubmix-create-chat-completion-request
- name: CreateCompletionRequest
  property_count: 18
  slug: aihubmix-create-completion-request
- name: CreateImageRequest
  property_count: 14
  slug: aihubmix-create-image-request
- name: CreateModerationResponse
  property_count: 3
  slug: aihubmix-create-moderation-response
- name: CreateTranscriptionRequest
  property_count: 12
  slug: aihubmix-create-transcription-request
jsonld:
- class_count: 120
  name: Aihubmix Context
  property_count: 189
  slug: aihubmix-context
layout: provider
mcp_servers:
- description: ''
  name: AIHubMix MCP Server
  slug: mcp
modified: '2026-10-13'
name: AIHubMix
nav: Providers
network: true
overview: 'AIHubMix publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including AIHubMix Unified API, Anthropic Compatible API, Google Vertex AI Compatible API, and 1 more. Tagged areas include Company, Artificial Intelligence, LLM, Model Routing, and AI Gateway.


  The AIHubMix catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AIHubMix''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, engineering blog, changelog, and 25 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: AIHubMix API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 2
  slug: aihubmix-rules
score:
  band: developing
  composite: 52.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 64.0
    developer_ergonomics: 73.8
    discoverability: 71.7
    operational_transparency: 36.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
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
  name: Aihubmix Authentication
  slug: aihubmix-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Aihubmix Domain Security
  slug: aihubmix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: aihubmix
tags:
- Company
- Artificial Intelligence
- LLM
- Model Routing
- AI Gateway
- Generative AI
- MCP
website: https://aihubmix.com
---
