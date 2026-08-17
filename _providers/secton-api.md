---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-08-17'
api_count: 2
apis:
- description: The Chat API from Secton API — 1 operation(s) for chat.
  name: Secton API Chat API
  slug: secton-api-chat-api
- description: The Models API from Secton API — 1 operation(s) for models.
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
overview: 'Secton API publishes 2 APIs on the [APIs.io](https://apis.io/) network: Chat API and Models API. Tagged areas include ai, inference, llm, chat-completions, and generative-ai.


  Secton API''s developer surface includes authentication, documentation, engineering blog, support, and 22 more developer resources.'
plans:
- name: Secton Api Plans Pricing
  plan_count: 0
  slug: secton-api-plans-pricing
random_paper: 117
rate_limits:
- limit_count: 0
  name: Secton Api Rate Limits
  slug: secton-api-rate-limits
score:
  band: developing
  composite: 42.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 44.8
    developer_ergonomics: 47.8
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 39.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
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
- ai
- inference
- llm
- chat-completions
- generative-ai
- developer-tools
- openai-compatible
- streaming
- machine-learning
- api
website: https://console.secton.org/api
---
