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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: AI-powered conversational interface over your production systems.
  name: Deeptrace Chat API
  slug: deeptrace-chat-api
- description: Trigger and retrieve asynchronous root-cause investigations.
  name: Deeptrace Investigations API
  slug: deeptrace-investigations-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://deeptrace.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.deeptrace.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.deeptrace.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.deeptrace.com/integrations
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.deeptrace.com
- group: commercial
  title: ''
  type: Pricing
  url: https://deeptrace.com/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.deeptrace.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.deeptrace.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deeptrace.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deeptrace.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.deeptrace.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.deeptrace.com/changelog
- group: auth
  title: ''
  type: Authentication
  url: authentication/deeptrace-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/deeptrace-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/deeptrace-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/deeptrace-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/deeptrace-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/deeptrace-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/deeptrace-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/deeptrace-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deeptrace-domain-security.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/deeptrace-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deeptrace-ai
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/deeptraceai
created: '2026-07-17'
description: Deeptrace is an AI SRE (site reliability engineering) agent that automatically investigates and root-causes production alerts by reasoning across logs, traces, metrics, and code. It triages and prioritizes alerts, produces evidence-backed root cause analyses in a couple of minutes, answers natural-language questions about production from Slack or the web app, and can auto-generate remediation such as pull requests and GitHub Actions. Deeptrace connects to the existing toolchain — Datadog, Grafana, New Relic, Sentry, Honeycomb, Coralogix, AWS CloudWatch, PagerDuty, GitHub, Linear, and Slack — to cut mean time to resolution. It exposes a REST API to trigger investigations, poll results, and drive AI chat programmatically. Founded 2025 and backed by Felicis, Matrix, and Y Combinator.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deeptrace.png
layout: provider
mcp_servers:
- description: ''
  name: deeptrace-mcp.yml
  slug: deeptrace-mcpyml
modified: '2026-07-18'
name: Deeptrace
nav: Providers
network: true
overview: 'Deeptrace publishes 2 APIs on the [APIs.io](https://apis.io/) network: Chat API and Investigations API. Tagged areas include Company, AIOps, Site Reliability Engineering, Observability, and Incident Management.


  Deeptrace''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, changelog, authentication, and 18 more developer resources.'
random_paper: 72
score:
  band: developing
  composite: 47.8
  delta: -2.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 63.3
    developer_ergonomics: 49.5
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 31.6
  previous_composite: 50.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deeptrace/refs/heads/main/screenshots/deeptrace-2026-07-25T211610.png
security:
- kind: authentication
  name: Deeptrace Authentication
  slug: deeptrace-authentication
  summary_line: apiKey/http-bearer · 2 schemes
- kind: domain-security
  name: Deeptrace Domain Security
  slug: deeptrace-domain-security
  summary_line: TLSv1.3 · HSTS
slug: deeptrace
tags:
- Company
- AIOps
- Site Reliability Engineering
- Observability
- Incident Management
- Root Cause Analysis
- Monitoring
- DevOps
- AI Agent
website: https://deeptrace.com
---
