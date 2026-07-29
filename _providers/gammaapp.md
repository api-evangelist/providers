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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 27.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'The Gamma Public API generates presentations, documents, websites, and social posts from text. Everything runs asynchronously: create a generation, poll for status, and retrieve the result (gammaUrl, '
  name: Gamma Public API
  slug: gamma-public-api
artifact_total: 6
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.gamma.app/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.gamma.app/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.gamma.app/generations/create-generation
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.gamma.app/get-started/understanding-the-api-options
- group: operate
  title: ''
  type: Support
  url: https://help.gamma.app/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gamma-app
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
- group: operate
  title: ''
  type: StatusPage
  url: https://status.gamma.app
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.gamma.app
- group: auth
  title: ''
  type: Compliance
  url: https://trust.gamma.app
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gammaapp-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gammaapp-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/gammaapp-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gammaapp-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gammaapp-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gammaapp-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/gammaapp-packages.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gammaapp-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gammaapp-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/gammaapp-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gammaapp-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gammaapp-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gammaapp-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gammaapp-domain-security.yml
created: '2026-07-17'
description: Gamma (Gamma Tech, Inc.) is an AI-powered platform for generating polished presentations, documents, websites, and social media posts from text prompts. Its public REST API (base https://public-api.gamma.app/v1.0) lets developers programmatically create gammas from scratch or from an existing template, poll asynchronous generation jobs, export to PDF/PPTX/PNG, manage themes and folders, retrieve document- and card-level analytics, and archive or delete documents. Gamma also runs an official hosted Model Context Protocol (MCP) server at mcp.gamma.app secured with OAuth 2.0 and Dynamic Client Registration that powers its ChatGPT and Claude connectors, alongside native Zapier, Make, and n8n integrations. API key access requires a Pro, Ultra, Teams, or Business plan and uses credit-based billing.
image: https://github.com/gamma-app.png
layout: provider
mcp_servers:
- description: ''
  name: gammaapp-mcp.yml
  slug: gammaapp-mcpyml
modified: '2026-07-19'
name: Gamma.app
nav: Providers
network: true
overview: 'Gamma.app publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Presentations, Documents, and Content Generation.


  Gamma.app''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, changelog, and 20 more developer resources.'
random_paper: 26
scopes:
- name: Gammaapp Scopes
  scope_count: 2
  slug: gammaapp-scopes
  summary_line: 2 scopes
score:
  band: thin
  composite: 39.9
  delta: 1.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 44.7
  previous_composite: 38.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gammaapp/refs/heads/main/screenshots/gammaapp-2026-07-25T215431.png
security:
- kind: authentication
  name: Gammaapp Authentication
  slug: gammaapp-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Gammaapp Domain Security
  slug: gammaapp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Gammaapp Trust Center
  slug: gammaapp-trust-center
  summary_line: SOC 2 Type II, ISO 27001, GDPR, HIPAA, PCI DSS, CSA STAR Level 1
slug: gammaapp
tags:
- Company
- Artificial Intelligence
- Presentations
- Documents
- Content Generation
- Generative AI
- Productivity
- MCP
- Websites
- Social Media
website: https://developers.gamma.app/
---
