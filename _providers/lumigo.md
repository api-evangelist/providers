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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.3
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Programmatic access to the Lumigo observability platform, authenticated with an API token (x-api-key header) generated in Lumigo Settings. Host confirmed live (returns 401 without credentials); no pub
  name: Lumigo API
  slug: lumigo-api
artifact_total: 6
asyncapis:
- description: ''
  name: Lumigo Webhooks
  slug: lumigo-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://lumigo.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lumigo.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lumigo.io/
- group: company
  title: ''
  type: Blog
  url: https://lumigo.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://lumigo.io/pricing/
- group: start
  title: ''
  type: Login
  url: https://platform.lumigo.io/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lumigo.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lumigo.io/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://lumigo.io/security/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lumigo-io
- group: operate
  title: ''
  type: Support
  url: https://lumigo.io/contact/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lumigo.io/
- group: auth
  title: ''
  type: Compliance
  url: https://lumigo.io/security/
- group: build
  title: ''
  type: Packages
  url: packages/lumigo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lumigo-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/lumigo-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lumigo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lumigo-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lumigo-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lumigo-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lumigo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lumigo-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/lumigo-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/lumigo-changelog.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/lumigo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lumigo-domain-security.yml
created: '2026-07-17'
description: Lumigo is an observability and troubleshooting platform for microservices and serverless environments. It provides distributed tracing, logs, and metrics with automatic, no-code instrumentation for AWS Lambda, Amazon ECS, AWS AppSync, API Gateway, Kubernetes, and OpenTelemetry workloads. Lumigo captures full request/response payloads for end-to-end traces, maps service dependencies, and offers an AI Copilot (with an IDE MCP server) to investigate and resolve production issues. First-party tracers and OpenTelemetry distributions ship for Node.js, Python, Java, Go, and .NET, alongside a CLI, a Serverless Framework plugin, CDK constructs, and a Kubernetes operator. Lumigo was surfaced as a portfolio company of Wing Venture Capital.
image: https://avatars.githubusercontent.com/u/38886022?v=4
layout: provider
mcp_servers:
- description: ''
  name: lumigo-mcp.yml
  slug: lumigo-mcpyml
modified: '2026-07-20'
name: Lumigo
nav: Providers
network: true
overview: 'Lumigo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Observability, Monitoring, Serverless, and Distributed Tracing.


  The Lumigo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lumigo''s developer surface includes documentation, engineering blog, pricing, support, CLI, authentication, changelog, and 19 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 47.2
  delta: -5.4
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 42.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 52.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/lumigo/refs/heads/main/screenshots/lumigo-2026-07-25T225711.png
security:
- kind: authentication
  name: Lumigo Authentication
  slug: lumigo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lumigo Domain Security
  slug: lumigo-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Lumigo Trust Center
  slug: lumigo-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: lumigo
tags:
- Company
- Observability
- Monitoring
- Serverless
- Distributed Tracing
- OpenTelemetry
- AWS Lambda
- Microservices
- Logs
website: https://lumigo.io/
---
