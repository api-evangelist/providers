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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.7
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: OAuth 2.0 secured REST API (OpenAPI 3.1) for Brightflag's enterprise legal management platform. Includes a Reporting API to extract key datasets and a Matter Budget API, plus operations to search invo
  name: Brightflag API
  slug: brightflag-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://brightflag.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://enterprise.brightflag.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://help.brightflag.com/hc/en-us/categories/21136642887581-API
- group: docs
  title: ''
  type: APIReference
  url: https://enterprise.brightflag.com/developer
- group: start
  title: ''
  type: GettingStarted
  url: https://help.brightflag.com/hc/en-us/articles/26006518363293-How-to-Get-an-API-Token-for-Brightflag
- group: operate
  title: ''
  type: Support
  url: https://help.brightflag.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/brightflag
- group: start
  title: ''
  type: Login
  url: https://app.brightflag.com/login
- group: operate
  title: ''
  type: StatusPage
  url: https://status.brightflag.com
- group: auth
  title: ''
  type: Compliance
  url: https://brightflag.com/security/
- group: auth
  title: ''
  type: Security
  url: https://brightflag.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/brightflag-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/brightflag-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brightflag-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brightflag-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/brightflag-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/brightflag-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brightflag-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/brightflag-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brightflag-llms.txt
created: '2026-07-17'
description: Brightflag is an AI-first enterprise legal management (ELM) platform that helps corporate legal teams control legal spend, manage matters, benchmark outside counsel, and automate invoice review. Founded in 2014 and headquartered in Dublin with a New York presence, Brightflag combines patented AI for invoice review and spend classification with e-billing, matter management, vendor management, and reporting. For developers Brightflag exposes an OAuth 2.0 secured REST API (OpenAPI 3.1) — including a Reporting API for extracting key datasets and a Matter Budget API — to integrate legal operations data with ERP, payment, and enterprise systems. This profile was enriched from Brightflag's public developer documentation and help center.
image: https://brightflag.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: brightflag-mcp.yml
  slug: brightflag-mcpyml
modified: '2026-07-18'
name: Brightflag
nav: Providers
network: true
overview: 'Brightflag publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Legal, Legal Operations, Legal Spend Management, and Enterprise Legal Management.


  Brightflag''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 15 more developer resources.'
random_paper: 90
score:
  band: thin
  composite: 29.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 29.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brightflag/refs/heads/main/screenshots/brightflag-2026-07-25T203843.png
security:
- kind: authentication
  name: Brightflag Authentication
  slug: brightflag-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Brightflag Domain Security
  slug: brightflag-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Brightflag Vulnerability Disclosure
  slug: brightflag-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Brightflag Trust Center
  slug: brightflag-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: brightflag
tags:
- Company
- Legal
- Legal Operations
- Legal Spend Management
- Enterprise Legal Management
- E-Billing
- Matter Management
- Reporting
- Artificial Intelligence
- LegalTech
website: https://brightflag.com
---
