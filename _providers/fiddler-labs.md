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
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.6
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Fiddler REST API (v3) is organized around resource-oriented URLs with JSON request/response bodies, Bearer-token authentication, and standard HTTP verbs and status codes. Resource groups include P
  name: Fiddler REST API
  slug: fiddler-rest-api
artifact_total: 7
asyncapis:
- description: ''
  name: Fiddler Labs Webhooks
  slug: fiddler-labs-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/fiddler-labs-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fiddler-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fiddler.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.fiddler.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fiddler.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fiddler.ai/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fiddler.ai/first-steps/getting-started-with-agentic-monitoring
- group: company
  title: ''
  type: Blog
  url: https://www.fiddler.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fiddler-labs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fiddler.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.fiddler.ai/trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fiddler.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fiddler.ai/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.fiddler.ai/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.fiddler.ai/security
- group: auth
  title: ''
  type: Authentication
  url: authentication/fiddler-labs-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fiddler-labs-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fiddler-labs-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fiddler-labs-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.fiddler.ai/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fiddler-labs-changelog.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fiddler-labs-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fiddler-labs-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/fiddler-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fiddler-labs-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fiddler-labs-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fiddler-labs-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fiddler-labs-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fiddler-labs-webhooks.yml
created: '2026-07-17'
description: Fiddler Labs (Fiddler AI) is an enterprise AI Observability and Security platform that provides unified visibility, context, and control across AI agents, LLM and GenAI applications, and traditional ML models. The Fiddler platform delivers standardized telemetry, evaluation, continuous monitoring, real-time guardrails, and auditable governance from development through production. Developers integrate through a REST API (v3), an official Python client (fiddler-client), framework SDKs (LangChain, LangGraph, OpenTelemetry, Google ADK, Strands, Evals), and a hosted Model Context Protocol (MCP) server that exposes GenAI observability data to AI assistants. Capabilities include model and application onboarding, production event ingestion, drift and integrity detection, custom metrics, segments, alerting, explainability, LLM gateway routing, and trace/span-level agentic observability.
image: https://www.fiddler.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: fiddler-labs-mcp.yml
  slug: fiddler-labs-mcpyml
modified: '2026-07-19'
name: Fiddler Labs
nav: Providers
network: true
overview: 'Fiddler Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Observability, ML Monitoring, LLM Observability, and Agentic AI.


  The Fiddler Labs catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fiddler Labs'' developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, authentication, and 22 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 2
  name: Fiddler Labs Rate Limits
  slug: fiddler-labs-rate-limits
score:
  band: strong
  composite: 55.0
  delta: -1.9
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 66.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 56.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fiddler-labs/refs/heads/main/screenshots/fiddler-labs-2026-07-25T214410.png
security:
- kind: authentication
  name: Fiddler Labs Authentication
  slug: fiddler-labs-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fiddler Labs Domain Security
  slug: fiddler-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fiddler Labs Trust Center
  slug: fiddler-labs-trust-center
  summary_line: SOC 2, HIPAA
slug: fiddler-labs
tags:
- Company
- AI Observability
- ML Monitoring
- LLM Observability
- Agentic AI
- AI Security
- AI Governance
- Model Monitoring
- Explainability
- Guardrails
website: https://www.fiddler.ai/
---
