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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 52.9
  scored_at: '2026-07-23'
api_count: 3
apis:
- description: The Activity API from Gray Swan — 1 operation(s) for activity.
  name: Gray Swan Activity API
  slug: gray-swan-activity-api
- description: The Cygnal API from Gray Swan — 7 operation(s) for cygnal.
  name: Gray Swan Cygnal API
  slug: gray-swan-cygnal-api
- description: The Policies API from Gray Swan — 8 operation(s) for policies.
  name: Gray Swan Policies API
  slug: gray-swan-policies-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.grayswan.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.grayswan.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.grayswan.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.grayswan.ai/api-reference
- group: start
  title: ''
  type: Quickstart
  url: https://docs.grayswan.ai/cygnal/creating-completions
- group: start
  title: ''
  type: SignUp
  url: https://platform.grayswan.ai
- group: company
  title: ''
  type: Blog
  url: https://www.grayswan.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GraySwanAI
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.grayswan.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.grayswan.ai/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/gray-swan-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gray-swan-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gray-swan-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gray-swan-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gray-swan-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gray-swan-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gray-swan-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/gray-swan-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gray-swan-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gray-swan-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/gray-swan-security.txt
- group: auth
  title: ''
  type: Security
  url: https://grayswan.ai/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gray-swan-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gray-swan-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/gray-swan-trust-center.yml
created: '2026-07-17'
description: Gray Swan AI is an AI security company that helps enterprises deploy AI with confidence. Its Cygnal product is a real-time, drop-in secure proxy that fronts LLM providers (OpenAI, Anthropic, and Gemini request formats) with input/output filtering and threat monitoring for jailbreaks and prompt injection, governed by versioned enforcement Policies managed over a REST API. Gray Swan also operates Shade (an adversarial red-teaming platform), Arena (a global adversarial red-teaming network), and adversarial model evaluations that frontier AI labs run before shipping. The company is SOC 2 Type 2 and Cyber Essentials certified.
image: https://cdn.prod.website-files.com/6614467b00e631b0f073e2b7/66886e33ca0b8f284d3b3b40_ca18847e7b3f6e2e7038dac7bd3846ce_Gray%20Swan%3DWhite%20Horizontal.svg
layout: provider
modified: '2026-07-19'
name: Gray Swan
nav: Providers
network: true
overview: 'Gray Swan publishes 3 APIs on the [APIs.io](https://apis.io/) network: Activity API, Cygnal API, and Policies API. Tagged areas include Company, Ai, AI Security, LLM Security, and Guardrails.


  Gray Swan''s developer surface includes documentation, API reference, quickstart, signup flow, engineering blog, authentication, and 20 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 0
  name: Gray Swan Rate Limits
  slug: gray-swan-rate-limits
score:
  band: developing
  composite: 45.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.6
    developer_ergonomics: 54.3
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 45.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Gray Swan Authentication
  slug: gray-swan-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Gray Swan Domain Security
  slug: gray-swan-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gray Swan Vulnerability Disclosure
  slug: gray-swan-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Gray Swan Trust Center
  slug: gray-swan-trust-center
  summary_line: SOC 2 Type 2, Cyber Essentials
slug: gray-swan
tags:
- Company
- Ai
- AI Security
- LLM Security
- Guardrails
- Red Teaming
- AI Governance
- Prompt Injection
- Model Safety
- API Security
website: https://www.grayswan.ai/
---
