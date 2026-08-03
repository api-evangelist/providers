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
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: GraphQL API for fetching feedback entries and group taxonomy, batch-importing feedback, and building classification groups. Authenticated with a personal API key sent as an HTTP Bearer token, scoped t
  name: Unwrap GraphQL API
  slug: unwrap-graphql-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/unwrap-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unwrap-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unwrap.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.unwrap.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unwrap.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.unwrap.ai/collections/6774268412-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.unwrap.ai/articles/6140971517-getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.unwrap.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.unwrap.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.unwrap.ai
- group: start
  title: ''
  type: Login
  url: https://app.unwrap.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.unwrap.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.unwrap.ai/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unwrap-nlp
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.unwrap.ai/collections/1750160942-unwrap_changelog
- group: auth
  title: ''
  type: Authentication
  url: authentication/unwrap-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/unwrap-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/unwrap-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/unwrap-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/unwrap-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unwrap-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/unwrap-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/unwrap-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/unwrap-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.unwrap.ai/why-unwrap
- group: agent
  title: ''
  type: WellKnown
  url: well-known/unwrap-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/unwrap-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/unwrap-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/unwrap-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/unwrap-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Unwrap is an AI-powered customer intelligence platform, founded by ex-Amazon Alexa product leaders, that aggregates customer feedback from every channel (support tickets, surveys, app reviews, sales calls, social) and uses custom NLP to auto-tag, cluster and surface actionable product insights without manual analysis. It ships a GraphQL data API (Bearer API key) for fetching feedback entries and taxonomy, batch-importing feedback, and building groups, plus a read-only remote MCP server (OAuth 2.0) and a first-party Surveys mobile SDK for iOS and Android. Unwrap is SOC 2 Type II and GDPR compliant.
image: https://cdn.prod.website-files.com/67c5e65b5323e6f7f216d5e7/67ddb0f28d559f418b033a59_unwrap-og-image.jpg
layout: provider
mcp_servers:
- description: ''
  name: unwrap-mcp.yml
  slug: unwrap-mcpyml
modified: '2026-07-21'
name: Unwrap
nav: Providers
network: true
overview: 'Unwrap publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Apps, Customer Feedback, Customer Intelligence, and Product Analytics.


  Unwrap''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 24 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 4
  name: Unwrap Rate Limits
  slug: unwrap-rate-limits
scopes:
- name: Unwrap Scopes
  scope_count: 5
  slug: unwrap-scopes
  summary_line: 5 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 42.1
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 64.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 52.6
  previous_composite: 42.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Unwrap Authentication
  slug: unwrap-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Unwrap Domain Security
  slug: unwrap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Unwrap Trust Center
  slug: unwrap-trust-center
  summary_line: SOC 2, GDPR
slug: unwrap
tags:
- Company
- Ai Apps
- Customer Feedback
- Customer Intelligence
- Product Analytics
- Voice of Customer
- NLP
- GraphQL
- MCP
website: https://www.unwrap.ai/
---
