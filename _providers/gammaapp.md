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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 17.6
  scored_at: '2026-09-01'
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
  name: Gamma.app MCP Server
  slug: gammaapp-mcp-server
modified: '2026-07-19'
name: Gamma.app
nav: Providers
network: true
overview: 'Gamma.app publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Presentations, Documents, and Content Generation.


  Gamma.app''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, changelog, and 20 more developer resources.'
random_paper: 17
scopes:
- name: Gammaapp Scopes
  scope_count: 2
  slug: gammaapp-scopes
  summary_line: 2 scopes
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 33.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Social-Media
website: https://developers.gamma.app/
---
