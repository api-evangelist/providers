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
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 64.4
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Windfall Agentic Access
  operation_count: 1
  slug: windfall-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The Windfall API API from Windfall — 1 operation(s) for windfall api.
  name: Windfall Windfall API API
  slug: windfall-windfall-api-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.windfall.com
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
- group: company
  title: ''
  type: Blog
  url: https://www.windfall.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.windfall.com/contact
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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/windfalldata
- group: auth
  title: ''
  type: Compliance
  url: https://www.windfall.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/windfall-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/windfall-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/windfall-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/windfall-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/windfall-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/windfall-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/windfall-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/windfall-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/windfall-enrich-person-record.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/windfall-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/windfall-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/windfall-domain-security.yml
created: '2026-07-17'
description: Windfall is an AI-powered people intelligence platform that helps go-to-market teams personalize workflows with wealth and career data, serving 1,500+ organizations across finance, retail, education, healthcare, and nonprofits. The Windfall API delivers enriched household (net worth, Windfall ID, confidence) and career (LinkedIn URL, job title, confidence) data for a single person record in real time — submit basic PII and receive JSON in one HTTPS request. US coverage only; data refreshed weekly; rate limited to 5 requests/second; and a non-billed sandbox with deterministic fictitious personas mirrors production for integration testing.
image: https://api-docs.windfall.com/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: windfall-mcp.yml
  slug: windfall-mcpyml
modified: '2026-07-21'
name: Windfall
nav: Providers
network: true
overview: 'Windfall publishes 1 API on the [APIs.io](https://apis.io/) network: Windfall API API. Tagged areas include Company, Fintech, Data Enrichment, Wealth Data, and People Intelligence.


  Windfall''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 17 more developer resources.'
random_paper: 33
rate_limits:
- limit_count: 0
  name: Windfall Rate Limits
  slug: windfall-rate-limits
score:
  band: developing
  composite: 49.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 60.2
    developer_ergonomics: 73.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 49.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Windfall Authentication
  slug: windfall-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Windfall Domain Security
  slug: windfall-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Windfall Trust Center
  slug: windfall-trust-center
  summary_line: SOC 2 Type 2
slug: windfall
tags:
- Company
- Fintech
- Data Enrichment
- Wealth Data
- People Intelligence
- Career Data
- Identity Resolution
- Sales Intelligence
- Marketing
website: https://www.windfall.com
---
