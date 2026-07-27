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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 25.0
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: DataRobot's public REST API (v2) for projects, modeling, predictions, deployments, MLOps monitoring, governance, and agentic workflows. Personal API keys are sent as bearer tokens against regional bas
  name: DataRobot REST API v2
  slug: datarobot-rest-api-v2
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://datarobot.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.datarobot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datarobot.com/en/docs/api/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.datarobot.com/en/docs/api/reference/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.datarobot.com/en/docs/api/dev-learning/api-quickstart.html
- group: operate
  title: ''
  type: Support
  url: https://community.datarobot.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/datarobot
- group: commercial
  title: ''
  type: Pricing
  url: https://www.datarobot.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.datarobot.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datarobot.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.datarobot.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.datarobot.com
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/datarobot-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/datarobot-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/datarobot-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/datarobot-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/datarobot-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/datarobot-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/datarobot-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/datarobot-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/datarobot-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/datarobot-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/datarobot-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.datarobot.com/en/docs/api/reference/changelogs/index.html
- group: design
  title: ''
  type: Conformance
  url: conformance/datarobot-conformance.yml
- group: auth
  title: ''
  type: TrustCenterArtifact
  url: security/datarobot-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datarobot-domain-security.yml
created: '2026-07-17'
description: DataRobot is an enterprise AI platform for building, deploying, governing, and monitoring predictive and generative AI models and agentic workflows. It exposes a public REST API (v2), first-party Python and R clients, a `dr` command-line tool, and an MCP surface (Global MCP plus deployable standalone servers) that lets agentic coding environments call DataRobot tools and resources. Developers authenticate with personal API keys (bearer tokens) against regional endpoints (US/EU/JP), while OAuth 2.0 / OIDC via app.datarobot.com backs agent and integration auth. The platform covers AutoML, MLOps deployment and monitoring, model governance and compliance documentation, and code-first GenAI/agent development. Surfaced as a portfolio company of Norwest Venture Partners, Sapphire Ventures, and Techstars, and enriched by the API Evangelist pipeline.
image: https://www.datarobot.com/wp-content/uploads/2021/09/DataRobot-Logo.png
layout: provider
mcp_servers:
- description: ''
  name: datarobot-mcp.yml
  slug: datarobot-mcpyml
modified: '2026-07-18'
name: DataRobot
nav: Providers
network: true
overview: 'DataRobot publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine Learning, MLOps, and Data Science.


  DataRobot''s developer surface includes documentation, API reference, getting-started guide, support, pricing, changelog, CLI, and 20 more developer resources.'
random_paper: 8
scopes:
- name: Datarobot Scopes
  scope_count: 3
  slug: datarobot-scopes
  summary_line: 3 scopes
score:
  band: thin
  composite: 37.3
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 71.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 37.3
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datarobot/refs/heads/main/screenshots/datarobot-2026-07-25T211352.png
security:
- kind: authentication
  name: Datarobot Authentication
  slug: datarobot-authentication
  summary_line: http/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Datarobot Domain Security
  slug: datarobot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Datarobot Trust Center
  slug: datarobot-trust-center
  summary_line: trust center published
slug: datarobot
tags:
- Company
- Artificial Intelligence
- Machine Learning
- MLOps
- Data Science
- Agentic AI
- Predictive Analytics
- Generative AI
website: https://datarobot.com
---
