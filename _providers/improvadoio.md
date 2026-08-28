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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.4
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Programmatic access to Improvado's data extraction, transformation, and loading capabilities — data sources, connections, accounts, extraction templates, extracts, destinations, loads, data tables, re
  name: Improvado Embedded API v3
  slug: improvado-embedded-api-v3
artifact_total: 7
asyncapis:
- description: ''
  name: Improvadoio Webhooks
  slug: improvadoio-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/improvadoio-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/improvadoio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/improvadoio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://improvado.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.improvado.io
- group: docs
  title: ''
  type: Documentation
  url: https://developers.improvado.io/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.improvado.io/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.improvado.io/introduction
- group: operate
  title: ''
  type: Support
  url: https://improvado.io/help
- group: company
  title: ''
  type: Blog
  url: https://improvado.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://improvado.io/pricing
- group: start
  title: ''
  type: Login
  url: https://report.improvado.io/login
- group: start
  title: ''
  type: SignUp
  url: https://improvado.io/get-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://improvado.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://improvado.io/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.improvado.io/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.improvado.io
- group: auth
  title: ''
  type: Compliance
  url: https://trust.improvado.io
- group: auth
  title: ''
  type: Security
  url: https://improvado.io/company-legal/responsible-disclosure-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/improvadoio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/improvadoio-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/improvadoio-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/improvadoio-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/improvadoio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/improvadoio-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/improvadoio-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/improvadoio-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/improvadoio-lifecycle.yml
created: '2026-07-17'
description: Improvado is an AI-powered marketing intelligence and data platform that connects, unifies, and governs marketing data across 500+ advertising, analytics, and CRM sources. Its Embedded API v3 gives platforms and agencies programmatic control over data sources, connections, accounts, extraction templates, extracts, destinations, loads, data tables, recipes, roles, and webhooks — letting them extract, transform, and load marketing data into any destination. Improvado also ships an official MCP server exposing 84 tools (data query, discovery, extract/load management, governance, AI recipes, dashboards) so AI agents can operate the platform directly.
image: https://improvado.io/logo_light.png
layout: provider
mcp_servers:
- description: Official Improvado MCP server. A secure proxy that exposes the Improvado marketing-data platform (500+ connectors, governed transformations, real-time analytics) to AI agents. The MCP layer acts as an
  name: Improvado.io MCP Server
  slug: improvadoio-mcp-server
modified: '2026-07-19'
name: Improvado.io
nav: Providers
network: true
overview: 'Improvado.io publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Analytics, Data Integration, and ETL.


  The Improvado.io catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Improvado.io''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 17
score:
  band: developing
  composite: 49.5
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 57.1
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 49.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/improvadoio/refs/heads/main/screenshots/improvadoio-2026-07-25T222205.png
security:
- kind: authentication
  name: Improvadoio Authentication
  slug: improvadoio-authentication
  summary_line: http/apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Improvadoio Domain Security
  slug: improvadoio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Improvadoio Vulnerability Disclosure
  slug: improvadoio-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Improvadoio Trust Center
  slug: improvadoio-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: improvadoio
tags:
- Company
- Marketing
- Analytics
- Data Integration
- ETL
- Marketing Intelligence
- Data Pipeline
- MCP
- Webhook
website: https://improvado.io
---
