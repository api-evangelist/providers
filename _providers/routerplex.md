---
access_model:
  confidence: high
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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Routerplex Agentic Access
  operation_count: 5
  slug: routerplex-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.routerplex.com/v1
  baseurl_source: declared
  description: The Images API from RouterPlex — 1 operation(s) for images.
  name: RouterPlex Images API
  slug: routerplex-images-api
- baseURL: https://api.routerplex.com/v1
  baseurl_source: declared
  description: The Messages API from RouterPlex — 1 operation(s) for messages.
  name: RouterPlex Messages API
  slug: routerplex-messages-api
- baseURL: https://api.routerplex.com/v1
  baseurl_source: declared
  description: The Models API from RouterPlex — 1 operation(s) for models.
  name: RouterPlex Models API
  slug: routerplex-models-api
- baseURL: https://api.routerplex.com/v1
  baseurl_source: declared
  description: The Responses API from RouterPlex — 1 operation(s) for responses.
  name: RouterPlex Responses API
  slug: routerplex-responses-api
- baseURL: https://api.routerplex.com/v1
  baseurl_source: declared
  description: The Chat Completions API from RouterPlex — 1 operation(s) for chat completions.
  name: RouterPlex Chat Completions API
  slug: routerplex-chat-completions-api
artifact_total: 22
collections:
- collection_type: open
  name: RouterPlex Chat API
  slug: open-routerplex-chat-api
- collection_type: open
  name: RouterPlex Images API
  slug: open-routerplex-images-api
- collection_type: open
  name: RouterPlex Messages API
  slug: open-routerplex-messages-api
- collection_type: open
  name: RouterPlex Models API
  slug: open-routerplex-models-api
- collection_type: open
  name: RouterPlex Responses API
  slug: open-routerplex-responses-api
common:
- group: other
  href: https://artifacts.apis.io/routerplex/capabilities/routerplex-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/routerplex-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/routerplex/overlays/routerplex-inference-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/routerplex-inference-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/routerplex/agentic-access/routerplex-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/routerplex-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/routerplex/security/routerplex-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/routerplex-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/routerplex/authentication/routerplex-authentication.yml
  title: ''
  type: Authentication
  url: authentication/routerplex-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://routerplex.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.routerplex.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.routerplex.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.routerplex.com/chat-completions
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.routerplex.com/quickstart
- group: operate
  title: ''
  type: Support
  url: mailto:support@routerplex.com
- group: operate
  title: ''
  type: Support
  url: https://t.me/RouterPlex
- group: company
  title: ''
  type: Blog
  url: https://routerplex.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://routerplex.com/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RouterPlex
- group: commercial
  title: ''
  type: Pricing
  url: https://routerplex.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://routerplex.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://routerplex.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://routerplex.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://routerplex.com/privacy
- group: agent
  href: https://artifacts.apis.io/routerplex/mcp/routerplex-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/routerplex-mcp.yml
- group: build
  href: https://artifacts.apis.io/routerplex/mcp/routerplex-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/routerplex-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/routerplex/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/routerplex/llms/routerplex-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/routerplex-llms.txt
- group: agent
  href: https://artifacts.apis.io/routerplex/well-known/routerplex-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/routerplex-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://routerplex.com/.well-known/api-catalog
- group: other
  title: ''
  type: ContentSignal
  url: https://routerplex.com/robots.txt
- group: design
  href: https://artifacts.apis.io/routerplex/conformance/routerplex-conformance.yml
  title: ''
  type: Conformance
  url: conformance/routerplex-conformance.yml
- group: design
  href: https://artifacts.apis.io/routerplex/errors/routerplex-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/routerplex-problem-types.yml
- group: design
  href: https://artifacts.apis.io/routerplex/lifecycle/routerplex-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/routerplex-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/routerplex/conventions/routerplex-conventions.yml
  title: ''
  type: Conventions
  url: conventions/routerplex-conventions.yml
- group: operate
  href: https://artifacts.apis.io/routerplex/rate-limits/routerplex-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/routerplex-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/routerplex/plans/routerplex-plans.yml
  title: ''
  type: Plans
  url: plans/routerplex-plans.yml
- group: build
  href: https://artifacts.apis.io/routerplex/packages/routerplex-packages.yml
  title: ''
  type: Packages
  url: packages/routerplex-packages.yml
- group: other
  title: ''
  type: Playground
  url: https://routerplex.com/dashboard/playground
- group: start
  href: https://artifacts.apis.io/routerplex/sandbox/routerplex-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/routerplex-sandbox.yml
- group: other
  title: ''
  type: Benchmarks
  url: https://routerplex.com/benchmarks.md
- group: commercial
  title: ''
  type: Pricing
  url: https://routerplex.com/pricing.md
created: '2026-07-26'
description: RouterPlex is an OpenAI- and Anthropic-compatible AI gateway that fronts 64 chat and image models from 15 vendors — OpenAI, Anthropic, Google, DeepSeek, Moonshot, Alibaba, MiniMax, Zhipu, xAI and others — behind one API key and one prepaid balance, at vendor list prices with no markup and no top-up fee. It exposes OpenAI Chat Completions, the OpenAI Responses route for Codex, Anthropic Messages, image generation and a model catalog on a single v1 REST surface, so the official OpenAI and Anthropic SDKs work unmodified with only a base URL change. Per-key hard spend budgets, model allowlists and optional RPM/TPM limits are the containment model for autonomous agents. RouterPlex also runs an anonymous read-only MCP server for model discovery and publishes an RFC 9727 API catalog, an OpenAPI 3.1 description, llms.txt and Markdown pricing and benchmark companions.
finops:
- has_sources: true
  method: derived
  name: Routerplex Finops
  primary_unit: token
  service_category: ''
  slug: routerplex-finops
  template: false
image: https://routerplex.com/icon.svg
layout: provider
mcp_servers:
- description: Read-only model discovery, pricing, and official RouterPlex API references.
  name: RouterPlex Public Catalog
  slug: routerplex-public-catalog
modified: '2026-08-09'
name: RouterPlex
nav: Providers
network: true
overview: 'RouterPlex publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Images API, Messages API, Models API, and 2 more. Tagged areas include LLM, Artificial Intelligence, AI Gateway, Inference, and Model Router.


  The RouterPlex catalog on APIs.io includes 1 Spectral governance ruleset.


  RouterPlex''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 31 more developer resources.'
plans:
- name: Routerplex Plans
  plan_count: 4
  slug: routerplex-plans
- name: Routerplex Price Estimates
  plan_count: 0
  slug: routerplex-price-estimates
random_paper: 10
rate_limits:
- limit_count: 3
  name: Routerplex Rate Limits
  slug: routerplex-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: RouterPlex API Rules
  rule_count: 48
  severity_counts:
    error: 45
    hint: 0
    info: 2
    warn: 1
  slug: routerplex-rules
score:
  band: developing
  composite: 48.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 61.8
    contract_governance: 18.2
    contract_quality: 53.9
    developer_ergonomics: 36.3
    discoverability: 85.0
    operational_transparency: 34.2
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/routerplex/routerplex-2026-08-17T081643.png
security:
- kind: authentication
  name: Routerplex Authentication
  slug: routerplex-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Routerplex Domain Security
  slug: routerplex-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Call any RouterPlex model through the Anthropic Messages format
  slug: routerplex-anthropic-compatible-messages
- name: Generate an image through RouterPlex
  slug: routerplex-generate-an-image
- name: Select a RouterPlex model and call it
  slug: routerplex-select-and-call-a-model
slug: routerplex
tags:
- LLM
- Artificial Intelligence
- AI Gateway
- Inference
- Model Router
- OpenAI-Compatible
- Anthropic Compatible
- Claude
- GPT
- Gemini
- API Gateway
- Agent Infrastructure
- Developer Tools
- MCP
- LLMOps
website: https://routerplex.com
---
