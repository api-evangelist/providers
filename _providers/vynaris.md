---
access_model:
  confidence: high
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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 11.5
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: 'REST API in OpenAI Chat Completions wire format. Primary endpoint POST /v1/chat/completions with SSE streaming and tool/function-calling passthrough. Supporting endpoints for ping, usage, ledger, and '
  name: Vynaris Gateway API
  slug: vynaris-gateway-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.vynaris.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vynaris/refs/heads/main/security/vynaris-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vynaris-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vynaris/refs/heads/main/conventions/vynaris-conventions.yml
  title: ''
  type: Conventions
  url: conventions/vynaris-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vynaris/refs/heads/main/conformance/vynaris-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vynaris-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vynaris/refs/heads/main/errors/vynaris-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/vynaris-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vynaris/refs/heads/main/lifecycle/vynaris-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/vynaris-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/vynaris/refs/heads/main/authentication/vynaris-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vynaris-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/vynaris/refs/heads/main/data-model/vynaris-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vynaris-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/vynaris/refs/heads/main/plans/vynaris-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vynaris-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/vynaris/refs/heads/main/rate-limits/vynaris-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vynaris-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vynaris/refs/heads/main/llms/vynaris-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vynaris-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/vynaris/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://vynaris.com/docs#quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://vynaris.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.vynaris.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vynaris.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vynaris.com/privacy
- group: company
  title: ''
  type: Blog
  url: https://vynaris.com/blog
- group: operate
  title: ''
  type: Support
  url: mailto:hello@vynaris.com
created: '2026-08-26'
description: OpenAI-compatible LLM inference gateway with evidence-based model routing and a per-request cost receipt attached to every response. Offers routed inference at provider list price plus a small markup, Vynaris-hosted reduced-refusal models, and enterprise self-hosted deployments. Early beta.
image: https://vynaris.com/icon.png
layout: provider
modified: '2026-08-26'
name: Vynaris
nav: Providers
network: true
overview: 'Vynaris publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, LLM Gateway, LLM Router / Aggregator, Inference / Model Serving, and AI Cost Management / FinOps.


  Vynaris'' developer surface includes authentication, getting-started guide, pricing, signup flow, engineering blog, support, and 13 more developer resources.'
plans:
- name: Vynaris Plans Pricing
  plan_count: 5
  slug: vynaris-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Vynaris Rate Limits
  slug: vynaris-rate-limits
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.7
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 73.2
    operational_transparency: 0.0
  previous_composite: 34.6
  provenance:
    conformance: first-party
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/vynaris/refs/heads/main/screenshots/vynaris-2026-09-02T170341.png
security:
- kind: authentication
  name: Vynaris Authentication
  slug: vynaris-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Vynaris Domain Security
  slug: vynaris-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: vynaris
tags:
- Artificial Intelligence
- LLM Gateway
- LLM Router / Aggregator
- Inference / Model Serving
- AI Cost Management / FinOps
- Developer Tools
- Agent Infrastructure
website: https://www.vynaris.com/
---
