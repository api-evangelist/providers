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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: User identification, company grouping, and event ingestion
  name: Userlens Events API
  slug: userlens-events-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/userlens-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://userlens.io
- group: docs
  title: ''
  type: Documentation
  url: https://userlens.gitbook.io/userlens-analytics
- group: docs
  title: ''
  type: APIReference
  url: https://userlens.gitbook.io/userlens-analytics/guides/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://userlens.gitbook.io/userlens-analytics/getting-started/http-api
- group: commercial
  title: ''
  type: Pricing
  url: https://userlens.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://userlens.io/blog
- group: start
  title: ''
  type: Login
  url: https://app.userlens.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://userlens.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://userlens.io/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wudpecker
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/userlens-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/userlens-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/userlens-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/userlens-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/userlens-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/userlens-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://userlens.io/llms.txt
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/userlens-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/userlens-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/userlens-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/userlens-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/userlens-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Userlens is an AI-native customer success platform for B2B SaaS that deploys LLM-powered agents to monitor every customer account, predict churn from actual product usage, and surface expansion opportunities. It ingests product analytics, CRM data, and business context for AI health scores, account-level analytics, and proactive alerts, and exposes a Write-Code-authenticated Events API (identify, group, track, and batched SDK event forwarding) plus JavaScript SDKs for instrumentation. Founded in 2025 (Y Combinator Spring 2026 batch), based in San Francisco and Helsinki.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/userlens.png
layout: provider
mcp_servers:
- description: ''
  name: userlens-mcp.yml
  slug: userlens-mcpyml
modified: '2026-07-21'
name: Userlens
nav: Providers
network: true
overview: 'Userlens publishes 1 API on the [APIs.io](https://apis.io/) network: Events API. Tagged areas include Company, Customer Success, Product Analytics, AI Agents, and Churn Prediction.


  Userlens'' developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, authentication, and 18 more developer resources.'
random_paper: 26
score:
  band: thin
  composite: 36.4
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 16.3
    developer_ergonomics: 49.5
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 5.3
  previous_composite: 36.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Userlens Authentication
  slug: userlens-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Userlens Domain Security
  slug: userlens-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: userlens
tags:
- Company
- Customer Success
- Product Analytics
- AI Agents
- Churn Prediction
- Event Tracking
- B2B SaaS
- Account Intelligence
website: https://userlens.io
---
