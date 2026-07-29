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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API (v3) for the Fiddler AI Observability platform — projects, models, applications, events, traces/sessions/spans, evaluators, alert rules, guardrails, custom metrics, and jobs. Resource-oriente
  name: Fiddler REST API
  slug: fiddler-rest-api
artifact_total: 6
asyncapis:
- description: ''
  name: Fiddlerai Alerts Webhooks
  slug: fiddlerai-alerts-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fiddlerai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fiddler.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.fiddler.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fiddler.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fiddler.ai/api/rest-api/rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fiddler.ai/product-guide/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.fiddler.ai/contact-sales
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
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fiddler.ai/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fiddler.ai/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.fiddler.ai/changelog/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fiddlerai-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/fiddlerai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fiddlerai-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fiddlerai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fiddlerai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fiddlerai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fiddlerai-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.fiddler.ai/changelog/python-sdk
- group: design
  title: ''
  type: Conformance
  url: conformance/fiddlerai-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.fiddler.ai/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust-center.fiddler.ai
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fiddlerai-alerts-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fiddlerai-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fiddlerai-llms.txt
created: '2026-07-17'
description: Fiddler AI is an enterprise AI Observability and Security platform — an "AI Control Plane" for AI agents, LLM applications, and traditional ML models. It delivers unified monitoring, real-time guardrails (safety, hallucination/faithfulness, and PII/sensitive-data detection), evaluation and experiments, drift and performance tracking, LLM-as-a-Judge custom evaluators, alerting, and governance/compliance across the AI lifecycle. Fiddler exposes a REST API (v3), an official Python client (fiddler-client), OpenTelemetry-native ingestion, and a remote MCP server for agent-native access to observability data.
image: https://www.fiddler.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: fiddlerai-mcp.yml
  slug: fiddlerai-mcpyml
modified: '2026-07-19'
name: fiddler.ai
nav: Providers
network: true
overview: 'fiddler.ai publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Observability, Machine Learning, LLM, and Model Monitoring.


  The fiddler.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  fiddler.ai''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 20 more developer resources.'
random_paper: 41
score:
  band: developing
  composite: 49.7
  delta: 7.1
  facets:
    commercial_clarity: 47.4
    contract_quality: 51.6
    developer_ergonomics: 67.4
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 36.8
  previous_composite: 42.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/fiddlerai/refs/heads/main/screenshots/fiddlerai-2026-07-25T214413.png
security:
- kind: authentication
  name: Fiddlerai Authentication
  slug: fiddlerai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Fiddlerai Domain Security
  slug: fiddlerai-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: trust-center
  name: Fiddlerai Trust Center
  slug: fiddlerai-trust-center
  summary_line: SOC 2 Type II, HIPAA
slug: fiddlerai
tags:
- Company
- AI Observability
- Machine Learning
- LLM
- Model Monitoring
- Guardrails
- MLOps
- AI Governance
- Explainability
- Agent Observability
- AI Security
website: https://www.fiddler.ai/
---
