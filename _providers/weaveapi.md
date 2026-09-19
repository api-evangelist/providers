---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - https://weaveapi.dev/pricing/
  - https://console.weaveapi.dev/register
  - plans
  - authentication
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.1
  scored_at: '2026-09-18'
api_count: 2
apis:
- description: OpenAI-wire-compatible REST API for chat completions, responses-style requests and the model catalog, authenticated with a bearer API key in the Authorization header. Three endpoints are documented (P
  name: WeaveAPI OpenAI-compatible API
  slug: weaveapi-openai-compatible-api
- description: 'Anthropic/Claude-wire-compatible messages route served from the bare api.weaveapi.dev host. The Claude Code setup guide instructs clients to use the host WITHOUT /v1 because Claude-compatible clients '
  name: WeaveAPI Anthropic-compatible Messages API
  slug: weaveapi-anthropic-compatible-messages-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://weaveapi.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.weaveapi.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://weaveapi.dev/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://weaveapi.dev/docs/#chat-completions
- group: start
  title: ''
  type: GettingStarted
  url: https://weaveapi.dev/docs/#quick-start
- group: operate
  title: ''
  type: Support
  url: https://weaveapi.dev/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://weaveapi.dev/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://console.weaveapi.dev/register
- group: start
  title: ''
  type: Login
  url: https://console.weaveapi.dev/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://weaveapi.dev/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://weaveapi.dev/privacy/
- group: company
  title: ''
  type: About
  url: https://weaveapi.dev/about/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/weaveapi/refs/heads/main/authentication/weaveapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/weaveapi-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/weaveapi/refs/heads/main/conventions/weaveapi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/weaveapi-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/weaveapi/refs/heads/main/errors/weaveapi-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/weaveapi-error-codes.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/weaveapi/refs/heads/main/rate-limits/weaveapi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/weaveapi-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/weaveapi/refs/heads/main/plans/weaveapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/weaveapi-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/weaveapi/refs/heads/main/lifecycle/weaveapi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/weaveapi-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/weaveapi/refs/heads/main/conformance/weaveapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/weaveapi-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/weaveapi/refs/heads/main/packages/weaveapi-packages.yml
  title: ''
  type: Packages
  url: packages/weaveapi-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/weaveapi/refs/heads/main/llms/weaveapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/weaveapi-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/weaveapi/refs/heads/main/well-known/weaveapi-content-signals.yml
  title: ''
  type: ContentSignal
  url: well-known/weaveapi-content-signals.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/weaveapi/refs/heads/main/security/weaveapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/weaveapi-domain-security.yml
created: '2026-07-10'
description: 'WeaveAPI is a hosted, OpenAI-wire-compatible inference gateway: one base URL (https://api.weaveapi.dev/v1) and one bearer API key give access to model routes drawn from several upstream families, while keys, prepaid balance, usage logs and top-ups are managed in a hosted console. The pitch is drop-in substitution — keep an existing OpenAI SDK, change the base URL and the key, and pick a model id from the console Model Marketplace. It also exposes an Anthropic-compatible messages route, and publishes setup guides for Claude Code, Codex, OpenCode, OpenClaw, Claude Desktop and Hermes via CC Switch. Billing is prepaid credits shared across every route, metered per model, with a $1 signup testing credit and no subscription tiers. The gateway runs the open-source New API platform. WeaveAPI publishes no OpenAPI or other machine-readable contract, no SDK of its own, no MCP server, no status page and no changelog.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/weaveapi.png
layout: provider
modified: '2026-08-11'
name: WeaveAPI - OpenAI-compatible AI API Gateway
nav: Providers
network: true
overview: 'WeaveAPI - OpenAI-compatible AI API Gateway publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, LLM, AI Inference, API Gateway, and Aggregator.


  WeaveAPI - OpenAI-compatible AI API Gateway''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 16 more developer resources.'
plans:
- name: Weaveapi Plans Pricing
  plan_count: 2
  slug: weaveapi-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Weaveapi Rate Limits
  slug: weaveapi-rate-limits
score:
  band: thin
  composite: 33.2
  coverage:
    artifact_dirs: 13
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 68.5
    operational_transparency: 0.0
  previous_composite: 33.2
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/weaveapi/refs/heads/main/screenshots/weaveapi-2026-09-02T170527.png
security:
- kind: authentication
  name: Weaveapi Authentication
  slug: weaveapi-authentication
  summary_line: apiKey · 0 schemes
- kind: domain-security
  name: Weaveapi Domain Security
  slug: weaveapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: weaveapi
tags:
- Artificial Intelligence
- LLM
- AI Inference
- API Gateway
- Aggregator
- OpenAI-Compatible
- Developer Tools
- Model Routing
- LLM Gateway
- prepaid credits
- Agent Tools
- Model Marketplace
website: https://weaveapi.dev/
---
