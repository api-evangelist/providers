---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The CafeX Audit Events API allows the retrieval of audit event data for CafeX tenants. Events can be filtered by a required time range and by optional service, event type, action, user, app, workspace
  name: CafeX Audit Events API
  slug: audit-events
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cafex-communications-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cafex.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://support.cafex.com/support/solutions
- group: docs
  title: ''
  type: APIReference
  url: https://support.cafex.com/support/solutions/articles/73000645442-accessing-audit-information-programmatically
- group: start
  title: ''
  type: GettingStarted
  url: https://support.cafex.com/support/solutions/articles/73000646926-building-your-first-app
- group: operate
  title: ''
  type: Support
  url: https://support.cafex.com/support/home
- group: company
  title: ''
  type: Blog
  url: https://cafex.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cafexcomms
- group: start
  title: ''
  type: Login
  url: https://app.cafex.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cafex.ai/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.cafex.ai/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cafex.ai/
- group: auth
  title: ''
  type: TrustCenter
  url: security/cafex-communications-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.cafex.ai/
- group: auth
  title: ''
  type: Authentication
  url: authentication/cafex-communications-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cafex-communications-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cafex-communications-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cafex-communications-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cafex-communications-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/cafex-communications-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cafex-communications-llms.txt
created: '2026-08-08'
description: CafeX Communications, Inc. is a US-headquartered software company (founded 2013) that builds a low-code platform for developing intelligent applications and agentic systems for regulated industries — banking, insurance, healthcare and government. The current CafeX AI platform is delivered as a multi-tenant SaaS at app.cafex.com and is organised into App Studio (App Builder, Flow Builder, Rule Builder, Data Tables and API Lab), Data Studio (Data AI, Data Gateway, Data Visualizer) and Agent Studio (Agent Builder, LM Insights). CafeX began life as a WebRTC and embedded-communications vendor (Fusion Client, Live Assist, CafeX Meetings, later the Challo collaboration workspace) and has since repositioned around AI workflow and process automation. Its one publicly documented, publicly callable API is the CafeX Audit Events API, a tenant-scoped REST search endpoint for audit event data secured with OAuth 2.0 client credentials.
image: https://cafex.ai/asset/svg/logo/dark/lockup-wide.svg
layout: provider
modified: '2026-08-08'
name: CafeX Communications
nav: Providers
network: true
overview: 'CafeX Communications publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Low-Code, Workflow Automation, Agentic AI, and Audit and Compliance.


  CafeX Communications'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 15 more developer resources.'
random_paper: 140
score:
  band: thin
  composite: 29.4
  delta: -2.2
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 31.6
  provenance:
    conformance: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Cafex Communications Authentication
  slug: cafex-communications-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Cafex Communications Domain Security
  slug: cafex-communications-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Cafex Communications Trust Center
  slug: cafex-communications-trust-center
  summary_line: ISO 27001, SOC 2, ISO 42001
slug: cafex-communications
tags:
- Company
- Low-Code
- Workflow Automation
- Agentic AI
- Audit and Compliance
- Collaboration
- Enterprise Software
- Regulated Industries
- Process Automation
website: https://cafex.ai/
---
