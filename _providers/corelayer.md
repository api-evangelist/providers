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
    agent_skills: derived
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
  score: 40.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Corelayer v1 REST API (api/v1) provides programmatic access to issues, groups, integrations, events, anomaly configs, deep research, API keys, and settings. It uses API-key authentication with rol
  name: Corelayer API
  slug: corelayer-api
artifact_total: 6
asyncapis:
- description: ''
  name: Corelayer Webhooks
  slug: corelayer-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.corelayer.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.corelayer.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.corelayer.com/cli/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.corelayer.com/cli/overview
- group: company
  title: ''
  type: Blog
  url: https://www.corelayer.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/corelayer-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://corelayer.statuspage.io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.corelayer.com/roi
- group: start
  title: ''
  type: SignUp
  url: https://app.corelayer.com/signin
- group: start
  title: ''
  type: Login
  url: https://app.corelayer.com/signin
- group: operate
  title: ''
  type: Support
  url: mailto:support@corelayer.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.corelayer.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.corelayer.com/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.corelayer.com
- group: auth
  title: ''
  type: Compliance
  url: https://trust.corelayer.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/corelayer-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/corelayer-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/corelayer-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/corelayer-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/corelayer-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/corelayer-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/corelayer-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/corelayer-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/corelayer-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/corelayer-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/corelayer-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/corelayer-well-known.yml
- group: company
  title: ''
  type: Twitter
  url: https://x.com/CorelayerAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/corelayerai
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@CorelayerAI
created: '2026-07-17'
description: Corelayer is an AI-native platform for production software support and maintenance — an AI SRE / AI on-call engineer for engineering teams. It continuously monitors alerts, logs, infrastructure, and underlying data for issues, uses AI agents to investigate and root-cause incidents, and works to prevent them before they impact users. Purpose-built for complex, data-intensive, and regulated environments like finance, fintech, healthcare, and insurance, Corelayer connects to the whole production environment — code, databases, deployments, and observability — with on-prem/BYOC deployment, configurable PII masking, and confidential compute. It exposes a v1 REST API, a first-party CLI, an MCP server, an installable agent skill, custom-webhook ingestion, and a metrics SDK. Backed by Y Combinator (W26); operated by Sevvy AI, Inc.
image: https://www.corelayer.com/opengraph-image
layout: provider
mcp_servers:
- description: ''
  name: corelayer-mcp.yml
  slug: corelayer-mcpyml
modified: '2026-07-18'
name: Corelayer
nav: Providers
network: true
overview: 'Corelayer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, SRE, Incident Response, and Observability.


  The Corelayer catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Corelayer''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, pricing, signup flow, and 24 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 50.3
  delta: -4.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 54.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/corelayer/refs/heads/main/screenshots/corelayer-2026-07-25T210427.png
security:
- kind: authentication
  name: Corelayer Authentication
  slug: corelayer-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Corelayer Domain Security
  slug: corelayer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Corelayer Trust Center
  slug: corelayer-trust-center
  summary_line: SOC 2 Type II
slug: corelayer
tags:
- Company
- AI
- SRE
- Incident Response
- Observability
- Production Support
- Root Cause Analysis
- Anomaly Detection
- DevOps
- Agent Native
- MCP
- Fintech
website: https://docs.corelayer.com
---
