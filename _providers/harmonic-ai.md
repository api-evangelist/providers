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
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: 'REST API for company search, enrichment, saved searches, list management, and bulk operations, plus a full GraphQL endpoint for flexible queries across companies, people, investors, lists, and custom '
  name: Harmonic REST & GraphQL API
  slug: harmonic-rest-graphql-api
- description: Hosted, agent-native MCP server exposing 40+ tools for enrichment, search, saved searches, lists, investors, network mapping, batch lookup, custom fields, and team. Listed in the Claude Connector stor
  name: Harmonic MCP Server
  slug: harmonic-mcp-server
artifact_total: 6
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.harmonic.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://console.harmonic.ai/docs/api-reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://console.harmonic.ai/docs/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://console.harmonic.ai/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.harmonic.ai/
- group: company
  title: ''
  type: Blog
  url: https://harmonic.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/harmonic-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://harmonic.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.harmonic.ai/signup
- group: start
  title: ''
  type: Login
  url: https://console.harmonic.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://harmonic.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://harmonic.ai/legal/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/harmonic-ai/harmonic/overview
- group: operate
  title: ''
  type: StatusPage
  url: https://status.harmonic.ai
- group: operate
  title: ''
  type: ChangeLog
  url: https://console.harmonic.ai/docs/changelog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/harmonic-ai-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/harmonic-ai-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/harmonic-ai-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/harmonic-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/harmonic-ai-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/harmonic-ai-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/harmonic-ai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/harmonic-ai-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/harmonic-ai-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-22'
description: Startup discovery and intelligence platform built on a proprietary database of 30M+ companies and 200M+ people, offering real-time funding data, headcount/traction metrics, team composition, and investor relationships via REST, GraphQL, and a hosted MCP server. Used by venture capital, growth equity, corporate development, and go-to-market teams to find, research, and qualify startups programmatically or through the console web app, Chrome extension, bulk data exports (BigQuery/Snowflake/S3), and CRM integrations (Salesforce/HubSpot/Affinity).
image: https://cdn.prod.website-files.com/6107b1101d4d3e748743f234/65f31ad2b4ac6cf0cb8bd691_og-img.png
layout: provider
mcp_servers:
- description: ''
  name: harmonic-ai-mcp.yml
  slug: harmonic-ai-mcpyml
modified: '2026-07-22'
name: Harmonic.ai
nav: Providers
network: true
overview: 'Harmonic.ai publishes 1 API on the [APIs.io](https://apis.io/) network: Harmonic REST & GraphQL API. Tagged areas include startup-intelligence, venture-capital, company-data, people-data, and investor-data.


  Harmonic.ai''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 18 more developer resources.'
random_paper: 56
scopes:
- name: Harmonic Ai Scopes
  scope_count: 2
  slug: harmonic-ai-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 45.8
  delta: -0.2
  facets:
    commercial_clarity: 44.7
    contract_quality: 32.3
    developer_ergonomics: 66.8
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 36.8
  previous_composite: 46.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/harmonic-ai/refs/heads/main/screenshots/harmonic-ai-2026-07-25T220821.png
security:
- kind: authentication
  name: Harmonic Ai Authentication
  slug: harmonic-ai-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Harmonic Ai Domain Security
  slug: harmonic-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: harmonic-ai
tags:
- startup-intelligence
- venture-capital
- company-data
- people-data
- investor-data
- funding-data
- data-enrichment
- sales-intelligence
- market-intelligence
- graphql
- mcp
- agent-native
website: https://console.harmonic.ai/
---
