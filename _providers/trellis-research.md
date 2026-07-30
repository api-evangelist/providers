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
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST Data API (V2, May 2024) for programmatic access to U.S. state and federal trial court data — Search (Boolean/query over Cases, Documents, Rulings with filtering and sorting), Rulings, Judges, Usa
  name: Trellis Trial Court Data API
  slug: trellis-trial-court-data-api
artifact_total: 5
asyncapis:
- description: ''
  name: Trellis Research Webhooks
  slug: trellis-research-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://trellis.law/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.trellis.law/trellis-api
- group: docs
  title: ''
  type: Documentation
  url: https://support.trellis.law/
- group: docs
  title: ''
  type: APIReference
  url: https://support.trellis.law/trellis-api
- group: company
  title: ''
  type: Blog
  url: https://blog.trellis.law/
- group: operate
  title: ''
  type: Support
  url: https://support.trellis.law/
- group: start
  title: ''
  type: SignUp
  url: https://trellis.law/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trellis.law/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trellis.law/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.trellis.law/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trellis-research-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trellis-research-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/trellis-research-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/trellis-research-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trellis-research-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/trellis-research-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/trellis-research-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/trellis-research-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trellis-research-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trellis-research-domain-security.yml
created: '2026-07-17'
description: Trellis (trellis.law) is an AI-powered state and federal court research and litigation analytics platform built by litigators for legal teams. It aggregates the most extensive U.S. trial court data available — State Trial, Federal, District, Appellate, Supreme Court, and Bankruptcy cases across all 50 states plus DC — and exposes it through Smart Search, a REST Data API (V2, with federal and PACER integration), and a remote OAuth-secured MCP server. Capabilities include case/docket search, document retrieval, tentative rulings, verdict records, judge and firm analytics, party and expert search, case/topic alerts, and webhook notifications for docket refreshes.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trellis-research.png
layout: provider
mcp_servers:
- description: ''
  name: trellis-research-mcp.yml
  slug: trellis-research-mcpyml
modified: '2026-07-21'
name: Trellis Research
nav: Providers
network: true
overview: 'Trellis Research publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Legal, Legal Research, Court Records, and Litigation Analytics.


  The Trellis Research catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Trellis Research''s developer surface includes documentation, API reference, engineering blog, support, signup flow, authentication, changelog, and 13 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 45.1
  delta: 8.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 50.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 39.5
  previous_composite: 36.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: authentication
  name: Trellis Research Authentication
  slug: trellis-research-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Trellis Research Domain Security
  slug: trellis-research-domain-security
  summary_line: TLSv1.3 · DMARC
slug: trellis-research
tags:
- Company
- Legal
- Legal Research
- Court Records
- Litigation Analytics
- Judicial Analytics
- Legal Data
- API
- MCP
website: https://trellis.law/
---
