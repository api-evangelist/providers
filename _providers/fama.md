---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 46.2
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: v2 REST API for submitting candidate screening checks and retrieving report findings (person, profiles, posts, web content, summary, and signed PDF). Bearer-token auth; report completion via HTTP call
  name: Fama REST API
  slug: fama-rest-api
artifact_total: 7
asyncapis:
- description: ''
  name: Fama Webhooks
  slug: fama-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.fama.io
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fama.io
- group: docs
  title: ''
  type: APIReference
  url: https://developer.fama.io/reference/fama-rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.fama.io/reference/api-token
- group: operate
  title: ''
  type: Support
  url: https://fama.io/contact
- group: company
  title: ''
  type: Blog
  url: https://fama.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://fama.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.fama.io
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fama.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fama.io
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fama-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/fama-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fama-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fama-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fama-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fama-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/fama-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fama-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fama-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fama-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fama-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fama-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.fama.io/
- group: auth
  title: ''
  type: TrustCenter
  url: security/fama-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fama-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fama.io
created: '2026-07-17'
description: Fama is an AI-powered social media and online screening platform for employment decisions. Its REST API lets HR platforms and background-screening providers submit candidate checks and retrieve behavioral findings — flagged posts, web content, and social profiles — mapped to workplace-misconduct categories across 30+ languages while filtering out protected-class information for EEOC/FCRA-aligned adjudication. Reports are delivered via completion callbacks or polling as JSON or a signed PDF, powering pre-employment screening (Fama Plus), comprehensive candidate assessment (Fama 360), and ongoing employee monitoring (Fama Pulse).
image: https://cdn.prod.website-files.com/63ea1ecaf41aeda5d5045103/6622b457a4c9d4fde1e2a424_Fama%20Open%20Graph%20Image%202%201200%20x%20630.svg
layout: provider
mcp_servers:
- description: ''
  name: fama-mcp.yml
  slug: fama-mcpyml
modified: '2026-07-19'
name: Fama
nav: Providers
network: true
overview: 'Fama publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Employment Screening, Background Checks, Human Resources, and Social Media.


  The Fama catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fama''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 65
rate_limits:
- limit_count: 0
  name: Fama Rate Limits
  slug: fama-rate-limits
score:
  band: thin
  composite: 43.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 22.6
    developer_ergonomics: 73.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 43.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fama/refs/heads/main/screenshots/fama-2026-07-25T214205.png
security:
- kind: authentication
  name: Fama Authentication
  slug: fama-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Fama Domain Security
  slug: fama-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fama Trust Center
  slug: fama-trust-center
  summary_line: SOC 2 Type 1
slug: fama
tags:
- Company
- Employment Screening
- Background Checks
- Human Resources
- Social Media
- Risk
- Compliance
- Artificial Intelligence
website: https://fama.io
---
