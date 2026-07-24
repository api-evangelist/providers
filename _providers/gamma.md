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
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 18.3
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Programmatic creation and management of gammas (presentations, documents, websites, and social posts). Asynchronous generate-and-poll workflow plus template, export, management, and analytics endpoint
  name: Gamma Generate API
  slug: gamma-generate-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gamma-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gamma.app/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.gamma.app/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.gamma.app/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.gamma.app/get-started/understanding-the-api-options
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.gamma.app/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.gamma.app/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.gamma.app/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gamma-app
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gamma.app/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.gamma.app/reference/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://gamma.app/pricing
- group: start
  title: ''
  type: SignUp
  url: https://gamma.app/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gamma.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gamma.app/privacy
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.gamma.app/mcp
created: '2026-07-17'
description: 'Gamma (Gamma Tech, Inc.) is an AI-native productivity platform for creating presentations, documents, websites, and social posts from a prompt or from existing content. Its public Generate API lets developers programmatically produce and manage gammas: generate from scratch or from a template, poll the asynchronous generation job, list workspace themes and folders, export to PDF, PPTX, or PNG, read and manage gammas, and pull document- and card-level engagement analytics. Authentication is via an X-API-KEY header (keys begin sk-gamma-) on Pro, Ultra, Teams, and Business plans, with credit-based billing. Gamma also ships an official remote MCP server (OAuth 2.0 with Dynamic Client Registration) and native integrations for Zapier, Make, n8n, Claude, and ChatGPT.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gamma.png
layout: provider
mcp_servers:
- description: ''
  name: gamma-mcp.yml
  slug: gamma-mcpyml
- description: ''
  name: mcp
  slug: mcp
modified: '2026-07-19'
name: Gamma
nav: Providers
network: true
overview: 'Gamma publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Productivity, Presentations, Documents, and Websites.


  Gamma''s developer surface includes documentation, API reference, getting-started guide, support, changelog, pricing, signup flow, and 9 more developer resources.'
random_paper: 5
rate_limits:
- limit_count: 0
  name: Gamma Rate Limits
  slug: gamma-rate-limits
scopes:
- name: Gamma Scopes
  scope_count: 2
  slug: gamma-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: thin
  composite: 32.5
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 47.8
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 32.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Gamma Authentication
  slug: gamma-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Gamma Domain Security
  slug: gamma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gamma
tags:
- Company
- Productivity
- Presentations
- Documents
- Websites
- Artificial Intelligence
- Generative AI
- Content Generation
- Design
website: https://gamma.app/
---
