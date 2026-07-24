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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 65.4
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Windfall Data Agentic Access
  operation_count: 1
  slug: windfall-data-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The Windfall API API from Windfall Data — 1 operation(s) for windfall api.
  name: Windfall Data Windfall API API
  slug: windfall-data-windfall-api-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://windfall.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.windfall.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.windfall.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.windfall.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.windfall.com/quickstart/
- group: auth
  title: ''
  type: Authentication
  url: authentication/windfall-data-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/windfall-data-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/windfall-data-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/windfall-data-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/windfall-data-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/windfall-data-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/windfall-data-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/windfall-data-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/windfall-data-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.windfall.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/windfall-data-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/windfall-data-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/windfall-data-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/windfalldata
- group: start
  title: ''
  type: Login
  url: https://login.windfalldata.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.windfall.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.windfall.com/privacy
created: '2026-07-17'
description: 'Windfall (windfall.com, formerly windfalldata.com) is a people-intelligence and AI platform that personalizes go-to-market workflows with wealth and career data. Its developer-facing Windfall API delivers enriched household and career data on a single-record basis in real time: submit a person record with basic PII and receive that individual''s household net worth, a stable Windfall ID, and career signals such as a LinkedIn URL and title, returned as JSON in one sub-second request. Coverage is United States, data is refreshed weekly, and the API is used for real-time lead routing and grading, marketing enrichment, and analytics scoring. Authentication is a Windfall-issued header token with a dedicated sandbox environment of deterministic test personas. Windfall is SOC 2 Type 2 certified.'
image: https://api-docs.windfall.com/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: windfall-data-mcp.yml
  slug: windfall-data-mcpyml
modified: '2026-07-21'
name: Windfall Data
nav: Providers
network: true
overview: 'Windfall Data publishes 1 API on the [APIs.io](https://apis.io/) network: Windfall API API. Tagged areas include Company, Data, Data Enrichment, Wealth Data, and People Intelligence.


  Windfall Data''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, and 18 more developer resources.'
random_paper: 29
score:
  band: developing
  composite: 48.5
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.2
    developer_ergonomics: 67.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 48.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Windfall Data Authentication
  slug: windfall-data-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Windfall Data Domain Security
  slug: windfall-data-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Windfall Data Trust Center
  slug: windfall-data-trust-center
  summary_line: SOC 2 Type 2
slug: windfall-data
tags:
- Company
- Data
- Data Enrichment
- Wealth Data
- People Intelligence
- Net Worth
- Identity Resolution
- Marketing
- Sales
website: https://windfall.com
---
