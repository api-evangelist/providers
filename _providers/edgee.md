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
  trial: false
  try_now: true
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 33.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Management API for an Edgee organization: export AI Gateway usage and cost data as CSV or JSON, create/list/update/delete AI Gateway API keys, and configure custom BYOK provider keys. Bearer-token aut'
  name: Edgee Console API
  slug: edgee-console
- baseURL: https://edgee.io
  baseurl_source: declared
  description: Standalone token compression endpoint
  name: Edgee Compress API
  slug: edgee-compress-api
- baseURL: https://edgee.io
  baseurl_source: declared
  description: Messages endpoints (Anthropic format)
  name: Edgee Messages API
  slug: edgee-messages-api
- baseURL: https://edgee.io
  baseurl_source: declared
  description: Model management endpoints
  name: Edgee Models API
  slug: edgee-models-api
- baseURL: https://edgee.io
  baseurl_source: declared
  description: Responses endpoints (OpenAI Responses API format)
  name: Edgee Responses API
  slug: edgee-responses-api
- baseURL: https://edgee.io
  baseurl_source: declared
  description: Token estimation endpoints
  name: Edgee Tokens API
  slug: edgee-tokens-api
- baseURL: https://api.edgee.app
  baseurl_source: declared
  description: Chat completion endpoints (OpenAI format)
  name: Edgee Chat Completions API
  slug: edgee-chat-completions-api
artifact_total: 18
common:
- group: other
  href: https://artifacts.apis.io/edgee/capabilities/edgee-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/edgee-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/edgee/overlays/edgee-gateway-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/edgee-gateway-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/edgee/security/edgee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/edgee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.edgee.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.edgee.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.edgee.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.edgee.ai/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.edgee.ai/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.edgee.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/edgee-ai
- group: operate
  title: ''
  type: Support
  url: https://www.edgee.ai/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.edgee.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.edgee.ai/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.edgee.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.edgee.ai/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.edgee.ai/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.edgee.ai/changelog
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.edgee.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.edgee.ai/
- group: build
  href: https://artifacts.apis.io/edgee/packages/edgee-packages.yml
  title: ''
  type: Packages
  url: packages/edgee-packages.yml
- group: build
  href: https://artifacts.apis.io/edgee/packages/edgee-packages.yml
  title: ''
  type: SDKs
  url: packages/edgee-packages.yml
- group: build
  href: https://artifacts.apis.io/edgee/cli/edgee-cli.yml
  title: ''
  type: CLI
  url: cli/edgee-cli.yml
- group: agent
  href: https://artifacts.apis.io/edgee/mcp/edgee-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/edgee-mcp.yml
- group: build
  href: https://artifacts.apis.io/edgee/mcp/edgee-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/edgee-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/edgee/llms/edgee-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/edgee-llms.txt
- group: auth
  href: https://artifacts.apis.io/edgee/authentication/edgee-authentication.yml
  title: ''
  type: Authentication
  url: authentication/edgee-authentication.yml
- group: design
  href: https://artifacts.apis.io/edgee/conventions/edgee-conventions.yml
  title: ''
  type: Conventions
  url: conventions/edgee-conventions.yml
- group: design
  href: https://artifacts.apis.io/edgee/errors/edgee-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/edgee-problem-types.yml
- group: design
  href: https://artifacts.apis.io/edgee/errors/edgee-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/edgee-error-codes.yml
- group: design
  href: https://artifacts.apis.io/edgee/lifecycle/edgee-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/edgee-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/edgee/conformance/edgee-conformance.yml
  title: ''
  type: Conformance
  url: conformance/edgee-conformance.yml
- group: design
  href: https://artifacts.apis.io/edgee/data-model/edgee-data-model.yml
  title: ''
  type: DataModel
  url: data-model/edgee-data-model.yml
- group: operate
  href: https://artifacts.apis.io/edgee/changelog/edgee-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/edgee-changelog.yml
- group: commercial
  href: https://artifacts.apis.io/edgee/plans/edgee-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/edgee-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/edgee/rate-limits/edgee-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/edgee-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/edgee/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-17'
description: Edgee is a French edge-native AI Gateway that sits between coding agents and LLM providers, intercepting, routing, compressing, metering and securing every request. Its OpenAI-compatible gateway API at edgee.io exposes chat completions, an Anthropic Messages endpoint, an OpenAI Responses endpoint, a model catalog of 230+ models across providers, token counting and a standalone compression endpoint, while a separate Console API at api.edgee.app handles organization management, gateway key management, BYOK provider keys and usage/cost export. A Rust CLI launches Claude Code, Codex, OpenCode, Cursor and VS Code Copilot through the gateway, and official TypeScript, Python, Go and Rust SDKs wrap the same surface. Edgee previously operated as an edge component runtime and data-collection platform at edgee.cloud; that documentation now redirects to the AI Gateway product at edgee.ai.
finops:
- has_sources: true
  method: derived
  name: Edgee Finops
  primary_unit: 1 developer
  service_category: ''
  slug: edgee-finops
  template: false
image: https://www.edgee.ai/assets/img/og/og.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at api.edgee.app requiring an API key.
  name: Edgee MCP Server
  slug: edgee-mcp-yml
modified: '2026-08-17'
name: Edgee
nav: Providers
network: true
overview: 'Edgee publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Compress API, Messages API, Models API, and 4 more. Tagged areas include Company, Artificial Intelligence, LLM, AI Gateway, and Agents.


  The Edgee catalog on APIs.io includes 1 Spectral governance ruleset.


  Edgee''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Edgee Plans Pricing
  plan_count: 3
  slug: edgee-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Edgee Rate Limits
  slug: edgee-rate-limits
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Edgee API Rules
  rule_count: 66
  severity_counts:
    error: 58
    hint: 0
    info: 5
    warn: 3
  slug: edgee-rules
score:
  band: strong
  composite: 63.0
  coverage:
    artifact_dirs: 28
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 56.6
    developer_ergonomics: 73.2
    discoverability: 75.0
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 61.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/edgee/edgee-2026-09-02T145329.png
security:
- kind: authentication
  name: Edgee Authentication
  slug: edgee-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Edgee Domain Security
  slug: edgee-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Edgee Trust Center
  slug: edgee-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2
skill_count: 3
skills:
- name: Estimate and compress a payload before you spend on it
  slug: edgee-estimate-and-compress-a-payload
- name: Move existing Anthropic Messages traffic onto Edgee
  slug: edgee-migrate-anthropic-traffic
- name: Route a chat completion through the Edgee AI Gateway
  slug: edgee-route-a-chat-completion
slug: edgee
tags:
- Company
- Artificial Intelligence
- LLM
- AI Gateway
- Agents
- Developer Tools
- Observability
- FinOps
- Edge Computing
- Cost Management
website: https://www.edgee.ai/
---
