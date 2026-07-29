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
  band: agent-aware
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
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for retrieving public company org charts, prospecting positions/people, and monitoring credit usage. Metered in credits; authenticated with an X-Api-Key header.
  name: The Org API
  slug: the-org-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://theorg.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.theorg.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.theorg.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://developers.theorg.com/api/endpoints/company-api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.theorg.com/api/get-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.theorg.com/api/change-log
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/theorg-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/theorg-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/theorg-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/theorg-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/theorg-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/theorg-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/theorg-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/theorg-components.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/theorg-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/theorg-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/theorg-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/theorg-domain-security.yml
- group: start
  title: ''
  type: Login
  url: https://theorg.com/subscription
- group: commercial
  title: ''
  type: TermsOfService
  url: https://theorg.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://theorg.com/privacy
created: '2026-07-17'
description: The Org operates the world's largest network of public organizational charts, mapping companies, their teams, and reporting hierarchies. Its developer platform exposes a metered REST API and an official MCP server for retrieving a company's public org chart by domain or LinkedIn URL, prospecting positions and people with rich filters, resolving a person's manager, and monitoring credit usage. Authentication is via an account-scoped X-Api-Key header over HTTPS, usage is metered in monthly credits, and the same key powers a Model Context Protocol endpoint exposing get_org_chart, get_manager, get_usage, and find_positions tools for agent-native access. Originally added to the API Evangelist network as a portfolio company of Balderton Capital.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/theorg.png
layout: provider
mcp_servers:
- description: ''
  name: theorg-mcp.yml
  slug: theorg-mcpyml
modified: '2026-07-21'
name: The Org
nav: Providers
network: true
overview: 'The Org publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Organizational Charts, People Data, Sales Intelligence, and Prospecting.


  The Org''s developer surface includes documentation, API reference, getting-started guide, changelog, authentication, and 17 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 0
  name: Theorg Rate Limits
  slug: theorg-rate-limits
score:
  band: thin
  composite: 28.1
  delta: -2.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 56.0
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 15.8
  previous_composite: 30.3
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Theorg Authentication
  slug: theorg-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Theorg Domain Security
  slug: theorg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: theorg
tags:
- Company
- Organizational Charts
- People Data
- Sales Intelligence
- Prospecting
- Org Chart
- B2B Data
- MCP
website: https://theorg.com/
---
