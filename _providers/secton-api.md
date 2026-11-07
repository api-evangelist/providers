---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.secton.org
  baseurl_source: declared
  description: The Models API from Secton API — 1 operation(s) for models.
  name: Secton API Models API
  slug: secton-api-models-api
- baseURL: https://api.secton.org
  baseurl_source: declared
  description: The Chat Completions API from Secton API — 1 operation(s) for chat completions.
  name: Secton API Chat Completions API
  slug: secton-api-chat-completions-api
artifact_total: 10
common:
- group: other
  href: https://artifacts.apis.io/secton-api/overlays/secton-api-chat-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/secton-api-chat-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/secton-api/skills/secton-api-chat-completion.md
  title: ''
  type: AgentSkill
  url: skills/secton-api-chat-completion.md
- group: other
  href: https://artifacts.apis.io/secton-api/capabilities/secton-api-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/secton-api-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.secton.org/
- group: auth
  href: https://artifacts.apis.io/secton-api/security/secton-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/secton-api-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/secton-api/authentication/secton-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/secton-api-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.secton.org/api
- group: docs
  title: ''
  type: Documentation
  url: https://console.secton.org/api
- group: company
  title: ''
  type: Blog
  url: https://secton.org/blog
- group: operate
  title: ''
  type: Support
  url: https://secton.org/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sectoncorp
- group: build
  title: ''
  type: SourceCode
  url: https://gitlab.com/wearesecton/secton-sdk
- group: start
  title: ''
  type: Login
  url: https://console.secton.org/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://secton.org/legal/console-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://secton.org/legal/privacy
- group: build
  href: https://artifacts.apis.io/secton-api/packages/secton-api-packages.yml
  title: ''
  type: Packages
  url: packages/secton-api-packages.yml
- group: build
  href: https://artifacts.apis.io/secton-api/packages/secton-api-packages.yml
  title: ''
  type: SDKs
  url: packages/secton-api-packages.yml
- group: design
  href: https://artifacts.apis.io/secton-api/lifecycle/secton-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/secton-api-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.secton.org
- group: operate
  href: https://artifacts.apis.io/secton-api/lifecycle/secton-api-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/secton-api-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/secton-api/security/secton-api-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/secton-api-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/secton-api/security/secton-api-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/secton-api-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/secton-api/conformance/secton-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/secton-api-conformance.yml
- group: design
  href: https://artifacts.apis.io/secton-api/errors/secton-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/secton-api-problem-types.yml
- group: design
  href: https://artifacts.apis.io/secton-api/conventions/secton-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/secton-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/secton-api/data-model/secton-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/secton-api-data-model.yml
- group: agent
  href: https://artifacts.apis.io/secton-api/llms/secton-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/secton-api-llms.txt
- group: agent
  href: https://artifacts.apis.io/secton-api/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/secton-api/plans/secton-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/secton-api-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/secton-api/rate-limits/secton-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/secton-api-rate-limits.yml
created: '2026-08-13'
description: Secton API is the OpenAI-compatible inference surface from Secton, a small developer-tools company operating at secton.org. It publishes two REST operations — POST /v1/chat/completions, with optional incremental streaming, and GET /v1/models — behind a static API key issued in the Secton Console and sent in the Authorization header. A first-party TypeScript SDK ("secton" on npm) wraps chat, model listing, credit usage and client-side conversation context management. Secton announced a permanent shutdown of the API on 2025-11-18 with an end date of 2025-12-19, yet the host, the OpenAPI and the status page remain live and the Console Terms of Service governing API keys were re-issued effective 2026-08-06 — see lifecycle/secton-api-lifecycle.yml before building on it.
image: https://cdn.secton.org/website-assets/summary_large_image.jpg
layout: provider
modified: '2026-08-16'
name: Secton API
nav: Providers
network: true
overview: 'Secton API publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Models API and Chat Completions API. Tagged areas include Artificial Intelligence, Inference, LLM, Chat Completions, and Generative AI.


  The Secton API catalog on APIs.io includes 1 Spectral governance ruleset.


  Secton API''s developer surface includes authentication, documentation, engineering blog, support, and 26 more developer resources.'
plans:
- name: Secton Api Plans Pricing
  plan_count: 0
  slug: secton-api-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Secton Api Rate Limits
  slug: secton-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Secton API API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: secton-api-rules
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 23
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 44.2
    developer_ergonomics: 47.0
    discoverability: 73.2
    operational_transparency: 21.1
  previous_composite: 39.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/secton-api/secton-api-2026-08-17T081749.png
security:
- kind: authentication
  name: Secton Api Authentication
  slug: secton-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Secton Api Domain Security
  slug: secton-api-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Secton Api Vulnerability Disclosure
  slug: secton-api-vulnerability-disclosure
  summary_line: Hackerone
skill_count: 2
skills:
- name: secton-api-chat-completion
  slug: secton-api-chat-completion
- name: secton-api-list-models
  slug: secton-api-list-models
slug: secton-api
tags:
- Artificial Intelligence
- Inference
- LLM
- Chat Completions
- Generative AI
- Developer Tools
- OpenAI-Compatible
- Streaming
- Machine Learning
website: https://www.secton.org/
---
