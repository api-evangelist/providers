---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.7
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Martian Ai Agentic Access
  operation_count: 3
  slug: martian-ai-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.withmartian.com/v1
  baseurl_source: declared
  description: The Chat Completions API from Martian — 1 operation(s) for chat completions.
  name: Martian Chat Completions API
  slug: martian-ai-chat-completions-api
- baseURL: https://api.withmartian.com/v1
  baseurl_source: declared
  description: The Messages API from Martian — 1 operation(s) for messages.
  name: Martian Messages API
  slug: martian-ai-messages-api
- baseURL: https://api.withmartian.com/v1
  baseurl_source: declared
  description: The Models API from Martian — 1 operation(s) for models.
  name: Martian Models API
  slug: martian-ai-models-api
artifact_total: 16
asyncapis:
- description: AsyncAPI 2.6 description of the Martian Gateway's **chat completion streaming** surface. Martian does not publish a WebSocket API. The Martian Gateway is an OpenAI-compatible model router; its only as
  name: Martian Gateway Chat Completions Streaming (HTTP + SSE)
  slug: martian-ai-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Martian Gateway Chat Completions API
  slug: open-martian-ai-chat-completions-api
- collection_type: open
  name: Martian Gateway Chat Completions Messages API
  slug: open-martian-ai-messages-api
- collection_type: open
  name: Martian Gateway Chat Completions Models API
  slug: open-martian-ai-models-api
- collection_type: open
  name: Martian Gateway API
  slug: open-martian-ai
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/martian-ai/refs/heads/main/agentic-access/martian-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/martian-ai-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/martian-ai/refs/heads/main/security/martian-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/martian-ai-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/martian-ai/refs/heads/main/authentication/martian-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/martian-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/withmartian
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/withmartian
- group: company
  title: ''
  type: Website
  url: https://www.withmartian.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.withmartian.com
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/martian-ai/refs/heads/main/plans/martian-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/martian-ai-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/martian-ai/refs/heads/main/rate-limits/martian-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/martian-ai-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/martian-ai/refs/heads/main/finops/martian-ai-finops.yml
  title: ''
  type: FinOps
  url: finops/martian-ai-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.withmartian.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.withmartian.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.withmartian.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.withmartian.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.withmartian.com/resources/support
- group: start
  title: ''
  type: SignUp
  url: https://app.withmartian.com/
- group: start
  title: ''
  type: Login
  url: https://app.withmartian.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.withmartian.com
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/martian-ai/refs/heads/main/packages/martian-ai-packages.yml
  title: ''
  type: Packages
  url: packages/martian-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/martian-ai/refs/heads/main/packages/martian-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/martian-ai-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/martian-ai/refs/heads/main/conventions/martian-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/martian-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/martian-ai/refs/heads/main/errors/martian-ai-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/martian-ai-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/martian-ai/refs/heads/main/lifecycle/martian-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/martian-ai-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/martian-ai/refs/heads/main/conformance/martian-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/martian-ai-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/martian-ai/refs/heads/main/well-known/martian-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/martian-ai-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/martian-ai/refs/heads/main/mcp/martian-ai-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/martian-ai-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/martian-ai/refs/heads/main/llms/martian-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/martian-ai-llms.txt
created: '2026-06-20'
description: Martian operates an LLM model router and gateway that dynamically routes each request to the best underlying model across providers for the optimal balance of quality, latency, and cost. The Martian Gateway exposes a drop-in, OpenAI-compatible REST API (and an Anthropic Messages-compatible surface) so applications can route across a large catalog of models by changing only the base URL.
finops:
- name: Martian Ai Finops
  service_category: AI and Machine Learning
  slug: martian-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/martian-ai.png
layout: provider
modified: '2026-08-08'
name: Martian
nav: Providers
network: true
overview: 'Martian publishes 3 APIs on the [APIs.io](https://apis.io/) network: Chat Completions API, Messages API, and Models API. Tagged areas include Artificial Intelligence, LLM, Model Router, Gateways, and Cost Optimization.


  The Martian catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Martian''s developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, support, signup flow, and 20 more developer resources.'
plans:
- name: Martian Ai Plans Pricing
  plan_count: 3
  slug: martian-ai-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 4
  name: Martian Ai Rate Limits
  slug: martian-ai-rate-limits
rules:
- effective_rule_count: 30
  extends:
  - spectral:asyncapi
  name: Martian API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: martian-ai-asyncapi-spectral-rules
score:
  band: developing
  composite: 52.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 65.4
    catalog_earned_first_party: 0.0
    catalog_gap: 49.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 49.5
    contract_governance: 29.5
    contract_quality: 57.6
    developer_ergonomics: 65.5
    discoverability: 73.2
    operational_transparency: 38.9
  previous_composite: 55.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/martian-ai/refs/heads/main/screenshots/martian-ai-2026-07-25T230258.png
security:
- kind: authentication
  name: Martian Ai Authentication
  slug: martian-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Martian Ai Domain Security
  slug: martian-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: martian-ai
tags:
- Artificial Intelligence
- LLM
- Model Router
- Gateways
- Cost Optimization
website: https://www.withmartian.com
---
