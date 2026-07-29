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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Programmatic access to Ema AI Employees. REST (HTTP/JSON) quickstart plus a gRPC-Web path for advanced endpoints, covering Chat, Workflows, Dashboards, Document Generation, Templates, Triggers and ten
  name: Ema Builder Platform API
  slug: ema-builder-platform-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.ema.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://builder.ema.ai
- group: docs
  title: ''
  type: Documentation
  url: https://builder.ema.ai
- group: docs
  title: ''
  type: APIReference
  url: https://builder.ema.ai/api-reference/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://builder.ema.ai/api-reference/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.ema.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://support.ema.ai
- group: start
  title: ''
  type: Login
  url: https://app.ema.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ema.ai/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.ema.ai/
- group: auth
  title: ''
  type: Authentication
  url: authentication/ema-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ema-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/ema-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ema-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ema-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ema-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ema-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ema-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://ema.co/.well-known/security.txt
created: '2026-07-17'
description: Ema is an enterprise "AI Employee" platform that builds autonomous agents to automate cross-functional workflows across HR, IT, Finance, customer support and healthcare operations. Its Autopilot builder turns plain-language descriptions into working AI Employees, EmaFusion combines 100+ AI models to optimize accuracy, cost and latency, and 1,000+ prebuilt connectors integrate with enterprise systems. Ema exposes a Builder Platform API (REST/JSON plus a gRPC-Web path) covering AI Employee, Chat, Workflow, Dashboard, Document Generation and tenant-management operations, secured by a two-step API-key to short-lived JWT flow, along with an Embeddable Chat SDK. The company is backed by Accel and Prosus Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ema.png
layout: provider
modified: '2026-07-19'
name: Ema
nav: Providers
network: true
overview: 'Ema publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Agents, AI Employees, and Automation.


  Ema''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, and 13 more developer resources.'
random_paper: 64
score:
  band: emerging
  composite: 26.8
  delta: -0.6
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 27.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ema/refs/heads/main/screenshots/ema-2026-07-25T213219.png
security:
- kind: authentication
  name: Ema Authentication
  slug: ema-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ema Domain Security
  slug: ema-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ema Vulnerability Disclosure
  slug: ema-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Ema Trust Center
  slug: ema-trust-center
  summary_line: trust center published
slug: ema
tags:
- Company
- AI
- Agents
- AI Employees
- Automation
- Enterprise
- Workflow Automation
- Conversational AI
website: https://www.ema.ai
---
