---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://api.secton.org
  baseurl_source: declared
  description: The Chat API from Secton API — 1 operation(s) for chat.
  name: Secton API Chat API
  slug: secton-api-chat-api
- baseURL: https://api.secton.org
  baseurl_source: declared
  description: The Models API from Secton API — 1 operation(s) for models.
  name: Secton API Models API
  slug: secton-api-models-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/secton-api-domain-security.yml
- group: auth
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
  title: ''
  type: Packages
  url: packages/secton-api-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/secton-api-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/secton-api-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.secton.org
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/secton-api-lifecycle.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/secton-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/secton-api-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/secton-api-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/secton-api-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/secton-api-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/secton-api-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/secton-api-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/secton-api-plans-pricing.yml
- group: operate
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
overview: 'Secton API publishes 2 APIs on the [APIs.io](https://apis.io/) network: Chat API and Models API. Tagged areas include Artificial Intelligence, Inference, LLM, Chat Completions, and Generative AI.


  Secton API''s developer surface includes authentication, documentation, engineering blog, support, and 22 more developer resources.'
plans:
- name: Secton Api Plans Pricing
  plan_count: 0
  slug: secton-api-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Secton Api Rate Limits
  slug: secton-api-rate-limits
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 44.2
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 21.1
  previous_composite: 36.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/secton-api/refs/heads/main/screenshots/secton-api-2026-08-17T081749.png
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
- Machine-Learning
website: https://console.secton.org/api
---
