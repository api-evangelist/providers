---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 65.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Agora Data Agentic Access
  operation_count: 21
  slug: agora-data-agentic-access
  summary_line: 21 operations · 13 acting
api_count: 1
apis:
- description: 'The public Agora Data loan-data API used by dealer management system (DMS) vendors and integration partners to move Buy Here Pay Here loan portfolio data into the Agora platform. It exposes multipart '
  name: Agora Data Loan Import API
  slug: agora-data-loan-import-api
artifact_total: 7
asyncapis:
- description: ''
  name: Agora Data Webhooks
  slug: agora-data-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://agoradata.com/
- group: company
  title: ''
  type: About
  url: https://agoradata.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://agoradata.com/revenews/
- group: operate
  title: ''
  type: Support
  url: https://support.agoradata.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.agoradata.com/hc/en-us
- group: operate
  title: ''
  type: ContactUs
  url: https://agoradata.com/contact-us/
- group: start
  title: ''
  type: GettingStarted
  url: https://agoradata.com/get-started-onramp-subprime-auto-finance/
- group: start
  title: ''
  type: Login
  url: https://portal.agoradata.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.agoradata.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api.agoradata.com/redoc
- group: docs
  title: ''
  type: APIReference
  url: https://api.agoradata.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AgoraData
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agoradata.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agoradata.com/privacy-policy/
- group: company
  title: ''
  type: Careers
  url: https://agoradata.com/careers/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agora-data-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agora-data-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/agora-data-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/agora-data-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/agora-data-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agora-data-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/agora-data-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agora-data-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agora-data-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/agora-data-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/agora-data-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/agora-data-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agora-data-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/agora-data-openapi-overlay.yaml
created: '2026-08-06'
description: 'Agora Data, Inc. is an Arlington, Texas fintech that provides capital, analytics and loan-servicing technology to the non-prime and Buy Here Pay Here (BHPH) automotive finance market. Its platform lets independent auto dealers and other loan originators publish, analyze and sell their retail installment contract portfolios: AgoraCapital provides structured financing that connects originators to capital-markets funding, AgoraInsights delivers portfolio performance analytics, AgoraPortal is the originator-facing management console, and Nuron is the proprietary AI risk, pricing and fraud modeling system trained on a large non-prime auto finance dataset. Agora runs a public loan-data import API at api.agoradata.com that dealer management system (DMS) vendors and integration partners use to upload, status-check and delete loan portfolio files, plus webhook receivers for iDMS and Auto Master file delivery.'
image: https://agoradata.com/wp-content/uploads/2023/06/AgoraData_Logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: agora-data-mcp.yml
  slug: agora-data-mcpyml
modified: '2026-08-06'
name: Agora Data
nav: Providers
network: true
overview: 'Agora Data publishes 1 API on the [APIs.io](https://apis.io/) network: Loan Import API. Tagged areas include Company, Auto Finance, Automotive, Lending, and Financial Services.


  The Agora Data catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Agora Data''s developer surface includes engineering blog, support, getting-started guide, documentation, API reference, authentication, and 24 more developer resources.'
random_paper: 73
scopes:
- name: Agora Data Scopes
  scope_count: 6
  slug: agora-data-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: developing
  composite: 46.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.9
    developer_ergonomics: 67.4
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 13.2
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Agora Data Authentication
  slug: agora-data-authentication
  summary_line: apiKey/oauth2/openIdConnect · 7 schemes
- kind: domain-security
  name: Agora Data Domain Security
  slug: agora-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agora-data
tags:
- Company
- Auto Finance
- Automotive
- Lending
- Financial Services
- Fintech
- Loan Origination
- Data Analytics
- Artificial Intelligence
- Capital Markets
website: https://agoradata.com/
---
