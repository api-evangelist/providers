---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 61.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Kymaapi Com Agentic Access
  operation_count: 52
  slug: kymaapi-com-agentic-access
  summary_line: 52 operations · 28 acting
api_count: 1
apis:
- baseURL: https://kymaapi.com/v1
  baseurl_source: declared
  description: The Audio API from kymaapi-com — 5 operation(s) for audio.
  name: kymaapi-com Audio API
  slug: kymaapi-com-audio-api
- baseURL: https://kymaapi.com/v1
  baseurl_source: declared
  description: Account management and API keys
  name: kymaapi-com Auth API
  slug: kymaapi-com-auth-api
- baseURL: https://kymaapi.com/v1
  baseurl_source: declared
  description: Chat completion endpoints (OpenAI + Anthropic format)
  name: kymaapi-com Chat API
  slug: kymaapi-com-chat-api
- baseURL: https://kymaapi.com/v1
  baseurl_source: declared
  description: The Completions API from kymaapi-com — 1 operation(s) for completions.
  name: kymaapi-com Completions API
  slug: kymaapi-com-completions-api
- baseURL: https://kymaapi.com/v1
  baseurl_source: declared
  description: Balance and pricing
  name: kymaapi-com Credits API
  slug: kymaapi-com-credits-api
- baseURL: https://kymaapi.com/v1
  baseurl_source: declared
  description: The Decisions API from kymaapi-com — 1 operation(s) for decisions.
  name: kymaapi-com Decisions API
  slug: kymaapi-com-decisions-api
- baseURL: https://kymaapi.com/v1
  baseurl_source: declared
  description: Auto-configuration and capability discovery (no auth required)
  name: kymaapi-com Discovery API
  slug: kymaapi-com-discovery-api
- baseURL: https://kymaapi.com/v1
  baseurl_source: declared
  description: The Embeddings API from kymaapi-com — 1 operation(s) for embeddings.
  name: kymaapi-com Embeddings API
  slug: kymaapi-com-embeddings-api
- baseURL: https://kymaapi.com/v1
  baseurl_source: declared
  description: The Images API from kymaapi-com — 2 operation(s) for images.
  name: kymaapi-com Images API
  slug: kymaapi-com-images-api
- baseURL: https://kymaapi.com/v1
  baseurl_source: declared
  description: Model catalog, recommendations, and filtering
  name: kymaapi-com Models API
  slug: kymaapi-com-models-api
- baseURL: https://kymaapi.com/v1
  baseurl_source: declared
  description: The Video API from kymaapi-com — 1 operation(s) for video.
  name: kymaapi-com Video API
  slug: kymaapi-com-video-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/kymaapi-com/agentic-access/kymaapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kymaapi-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/kymaapi-com/plans/kymaapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kymaapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/kymaapi-com/rules/kymaapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/kymaapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/kymaapi-com/json-ld/kymaapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kymaapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/kymaapi-com/vocabulary/kymaapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kymaapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/kymaapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/kymaapi-com/data-model/kymaapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kymaapi-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/kymaapi-com/changelog/kymaapi-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/kymaapi-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/kymaapi-com/authentication/kymaapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kymaapi-com-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://kymaapi.com/status
- group: design
  href: https://artifacts.apis.io/kymaapi-com/lifecycle/kymaapi-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kymaapi-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/kymaapi-com/errors/kymaapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kymaapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kymaapi-com/conformance/kymaapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kymaapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/kymaapi-com/llms/kymaapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kymaapi-com-llms.txt
- group: other
  href: https://artifacts.apis.io/kymaapi-com/a2a/kymaapi-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/kymaapi-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/kymaapi-com/mcp/kymaapi-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/kymaapi-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/kymaapi-com/mcp/kymaapi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kymaapi-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/kymaapi-com/well-known/kymaapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kymaapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/kymaapi-com/hosts/kymaapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kymaapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/kymaapi-com/vendors/kymaapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kymaapi-com-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://kymaapi.com/changelog
- group: auth
  href: https://artifacts.apis.io/kymaapi-com/security/kymaapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kymaapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kymaapi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://kymaapi.com/usage
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kymaapi.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kymaapi.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kymaapi.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://kymaapi.com/status
- group: company
  title: ''
  type: Blog
  url: https://kymaapi.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kyma-api
- group: commercial
  title: ''
  type: Pricing
  url: https://kymaapi.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://kymaapi.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kymaapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kymaapi.com/privacy
created: '2026-10-30'
description: Kyma API is an LLM API gateway that provides a single API key to access over 119 AI models across text, image, video, speech, and transcription domains. It offers real-time uptime metrics per model, a developer dashboard, pricing transparency, and extensive documentation. The platform emphasizes ease of integration, scalability, and monitoring for developers building AI-powered applications.
image: https://mintcdn.com/kyma/Ir71WrmY8XrY4SLl/logo/light.svg?fit=max&auto=format&n=Ir71WrmY8XrY4SLl&q=85&s=dcfc23077ffc3b8109d9c3d5d8c4cfc3
json_schemas:
- name: AnthropicMessageRequest
  property_count: 6
  slug: kymaapi-com-anthropic-message-request
- name: AudioBilling
  property_count: 6
  slug: kymaapi-com-audio-billing
- name: ChatCompletionRequest
  property_count: 8
  slug: kymaapi-com-chat-completion-request
- name: ChatCompletionResponse
  property_count: 6
  slug: kymaapi-com-chat-completion-response
- name: ImageJob
  property_count: 11
  slug: kymaapi-com-image-job
- name: VideoJob
  property_count: 11
  slug: kymaapi-com-video-job
jsonld:
- class_count: 11
  name: Kymaapi Com Context
  property_count: 71
  slug: kymaapi-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.kymaapi.com.
  name: kymaapi-com MCP Server
  slug: kymaapi-com-mcp-yml
modified: '2026-10-30'
name: kymaapi-com
nav: Providers
network: true
overview: 'kymaapi-com publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audio API, Auth API, Chat API, and 8 more. Tagged areas include LLM, API Gateway, Artificial Intelligence, Machine Learning, and Developer Tools.


  The kymaapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  kymaapi-com''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 27 more developer resources.'
plans:
- name: Kymaapi Com Plans Pricing
  plan_count: 1
  slug: kymaapi-com-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Kymaapi Com Rate Limits
  slug: kymaapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: kymaapi-com API Rules
  rule_count: 68
  severity_counts:
    error: 62
    hint: 0
    info: 1
    warn: 5
  slug: kymaapi-com-rules
scopes:
- name: Kymaapi Com Scopes
  scope_count: 0
  slug: kymaapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.8
  coverage:
    artifact_dirs: 34
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.9
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 65.5
    developer_ergonomics: 41.0
    discoverability: 65.0
    operational_transparency: 18.4
  previous_composite: 58.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kymaapi-com/kymaapi-com-2026-11-03T134617.png
security:
- kind: authentication
  name: Kymaapi Com Authentication
  slug: kymaapi-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Kymaapi Com Domain Security
  slug: kymaapi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: chat-completion
  slug: kymaapi-com-chat-completion-skill
slug: kymaapi-com
tags:
- LLM
- API Gateway
- Artificial Intelligence
- Machine Learning
- Developer Tools
website: https://kymaapi.com/
---
