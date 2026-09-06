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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: v2 REST API for submitting candidate screening checks and retrieving report findings (person, profiles, posts, web content, summary, and signed PDF). Bearer-token auth; report completion via HTTP call
  name: Fama REST API
  slug: fama-rest-api
artifact_total: 6
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
  type: X-MCPServerCandidate
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
modified: '2026-07-19'
name: Fama
nav: Providers
network: true
overview: 'Fama publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Employment Screening, Background Checks, Human Resources, and Social-Media.


  The Fama catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fama''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 1
  name: Fama Rate Limits
  slug: fama-rate-limits
score:
  band: developing
  composite: 45.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 44.4
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Social-Media
- Risk
- Compliance
- Artificial Intelligence
website: https://fama.io
---
