---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Inception Agentic Access
  operation_count: 7
  slug: inception-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.inceptionlabs.ai
  baseurl_source: declared
  description: Code edit completion endpoints.
  name: Inception Edit API
  slug: inception-edit-api
- baseURL: https://api.inceptionlabs.ai
  baseurl_source: declared
  description: Fill-in-the-middle code completion endpoints.
  name: Inception FIM API
  slug: inception-fim-api
- baseURL: https://api.inceptionlabs.ai
  baseurl_source: declared
  description: List available models.
  name: Inception Models API
  slug: inception-models-api
- baseURL: https://api.inceptionlabs.ai
  baseurl_source: declared
  description: Chat completion endpoints (OpenAI-compatible).
  name: Inception Chat Completions API
  slug: inception-chat-completions-api
arazzos:
- description: List the available Mercury chat models, then send a chat completion.
  name: Inception — discover a chat model and generate a completion
  slug: inception-chat-completion.arazzo
- description: Confirm a FIM model then generate an inline code completion with Mercury Edit 2.
  name: Inception — fill-in-the-middle code autocomplete
  slug: inception-code-autocomplete.arazzo
artifact_total: 20
collections:
- collection_type: open
  name: Inception Chat API
  slug: open-inception-chat-api
- collection_type: open
  name: Inception Chat Edit API
  slug: open-inception-edit-api
- collection_type: open
  name: Inception Chat FIM API
  slug: open-inception-fim-api
- collection_type: open
  name: Inception Chat Models API
  slug: open-inception-models-api
common:
- group: other
  href: https://artifacts.apis.io/inception/capabilities/inception-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/inception-capability-edges.yml
- group: design
  href: https://artifacts.apis.io/inception/arazzo/inception-chat-completion.arazzo.yml
  title: ''
  type: Arazzo
  url: arazzo/inception-chat-completion.arazzo.yml
- group: design
  href: https://artifacts.apis.io/inception/arazzo/inception-code-autocomplete.arazzo.yml
  title: ''
  type: Arazzo
  url: arazzo/inception-code-autocomplete.arazzo.yml
- group: company
  title: ''
  type: Website
  url: https://inceptionlabs.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.inceptionlabs.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inceptionlabs.ai/get-started/get-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.inceptionlabs.ai/api-reference/chat/create-a-chat-completion
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.inceptionlabs.ai/get-started/get-started
- group: auth
  href: https://artifacts.apis.io/inception/authentication/inception-authentication.yml
  title: ''
  type: Authentication
  url: authentication/inception-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.inceptionlabs.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://docs.inceptionlabs.ai/support/support
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.inceptionlabs.ai/get-started/models
- group: start
  title: ''
  type: SignUp
  url: https://platform.inceptionlabs.ai/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.inceptionlabs.ai/support/tou
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.inceptionlabs.ai/support/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/inception-ai-inc
- group: docs
  href: https://artifacts.apis.io/inception/openapi/_original/inception-openapi-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/inception-openapi-original.json
- group: agent
  href: https://artifacts.apis.io/inception/llms/inception-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/inception-llms.txt
- group: build
  href: https://artifacts.apis.io/inception/packages/inception-packages.yml
  title: ''
  type: Packages
  url: packages/inception-packages.yml
- group: build
  href: https://artifacts.apis.io/inception/packages/inception-packages.yml
  title: ''
  type: SDKs
  url: packages/inception-packages.yml
- group: agent
  href: https://artifacts.apis.io/inception/mcp/inception-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/inception-mcp.yml
- group: operate
  href: https://artifacts.apis.io/inception/rate-limits/inception-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/inception-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/inception/plans/inception-plans.yml
  title: ''
  type: Plans
  url: plans/inception-plans.yml
- group: commercial
  href: https://artifacts.apis.io/inception/finops/inception-finops.yml
  title: ''
  type: FinOps
  url: finops/inception-finops.yml
- group: design
  href: https://artifacts.apis.io/inception/errors/inception-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/inception-problem-types.yml
- group: design
  href: https://artifacts.apis.io/inception/lifecycle/inception-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/inception-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/inception/conventions/inception-conventions.yml
  title: ''
  type: Conventions
  url: conventions/inception-conventions.yml
- group: design
  href: https://artifacts.apis.io/inception/conformance/inception-conformance.yml
  title: ''
  type: Conformance
  url: conformance/inception-conformance.yml
- group: design
  href: https://artifacts.apis.io/inception/data-model/inception-data-model.yml
  title: ''
  type: DataModel
  url: data-model/inception-data-model.yml
- group: other
  href: https://artifacts.apis.io/inception/overlays/inception-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/inception-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/inception/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/inception/agentic-access/inception-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/inception-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/inception/authentication/inception-authentication.yml
  title: ''
  type: Authentication
  url: authentication/inception-authentication.yml
- group: auth
  href: https://artifacts.apis.io/inception/security/inception-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inception-domain-security.yml
created: '2026-07-17'
description: Inception Labs builds diffusion-based large language models (dLLMs) branded Mercury. Unlike autoregressive models that emit tokens one at a time, Mercury generates many tokens in parallel through discrete diffusion, running 5-10x faster at roughly half the cost of comparable frontier models. The Inception API is OpenAI-compatible and exposes chat completions (Mercury 2, a reasoning dLLM with a 128K context, tool calling, and structured outputs), plus fill-in-the-middle and next-edit code completions (Mercury Edit 2) for IDE-style autocomplete. It ships official Python and TypeScript SDKs, a streaming/diffusion mode, and enterprise deployment via the Inception API, AWS Bedrock, and Azure AI Foundry. Backed by Amplify Partners.
finops:
- has_sources: true
  method: searched
  name: Inception Finops
  primary_unit: ''
  service_category: ''
  slug: inception-finops
  template: false
image: https://www.inceptionlabs.ai/logo.png
layout: provider
modified: '2026-07-19'
name: Inception
nav: Providers
network: true
overview: 'Inception publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Edit API, FIM API, Models API, and 1 more. Tagged areas include Company, Artificial Intelligence, LLM, Diffusion Models, and Code Completion.


  The Inception catalog on APIs.io includes 1 Spectral governance ruleset.


  Inception''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, pricing, and 27 more developer resources.'
plans:
- name: Inception Plans
  plan_count: 6
  slug: inception-plans
random_paper: 9
rate_limits:
- limit_count: 0
  name: Inception Rate Limits
  slug: inception-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Inception API Rules
  rule_count: 62
  severity_counts:
    error: 60
    hint: 0
    info: 1
    warn: 1
  slug: inception-rules
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 69.7
    contract_governance: 18.2
    contract_quality: 61.9
    developer_ergonomics: 58.9
    discoverability: 73.2
    operational_transparency: 2.6
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/inception/inception-2026-07-25T222332.png
security:
- kind: authentication
  name: Inception Authentication
  slug: inception-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Inception Domain Security
  slug: inception-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 3
skills:
- name: Generate a chat completion with Mercury 2
  slug: inception-chat-completion
- name: Inline code autocomplete and next-edit with Mercury Edit 2
  slug: inception-code-autocomplete
- name: Run a tool-calling agent turn with Mercury 2
  slug: inception-tool-calling-agent
slug: inception
tags:
- Company
- Artificial Intelligence
- LLM
- Diffusion Models
- Code Completion
- Machine Learning
- Developer Tools
- Foundation Models
website: https://inceptionlabs.ai
---
