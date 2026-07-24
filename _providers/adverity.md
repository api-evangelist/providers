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
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: The Adverity Management API provides programmatic access to the Adverity platform for managing datastreams, authorizations, fetches, transformations, data mappings, destinations, workspaces, and users
  name: Adverity Management API
  slug: adverity-management-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.adverity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.adverity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.adverity.com/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.adverity.com/guides/management-api/introduction-management-api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.adverity.com/guides/management-api/introduction-management-api.html
- group: operate
  title: ''
  type: Support
  url: https://www.adverity.com/resources/product-support
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.adverity.com/updates/adverity-help-center
- group: company
  title: ''
  type: Blog
  url: https://www.adverity.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.adverity.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adverity.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adverity.com/privacy-notice
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/4861982/SWT7CKex
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.adverity.com/reference/release-notes/release-notes.html
- group: operate
  title: ''
  type: StatusPage
  url: https://docs.adverity.com/reference/release-notes/incidents.html
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/adverity-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adverity-lifecycle.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.adverity.com/analytics-platform/data-security
- group: agent
  title: ''
  type: MCPServer
  url: mcp/adverity-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adverity-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adverity-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adverity-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adverity-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adverity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.adverity.com/analytics-platform/data-security
- group: agent
  title: ''
  type: WellKnown
  url: well-known/adverity-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adverity-llms.txt
created: '2026-07-17'
description: Adverity is a marketing data intelligence platform that integrates, harmonizes, transforms, and analyzes marketing and advertising data from hundreds of sources (Google Ads, Facebook Ads, LinkedIn Ads, and more) into a single, governed data foundation for reporting, dashboards, and downstream data warehouses. Adverity exposes a programmatic Management API (legacy /api/ plus a newer /api/v1/ surface) for managing datastreams, authorizations, fetches, transformations, destinations, workspaces, and users, and ships an Adverity Atlas Model Context Protocol (MCP) server (beta) so AI assistants can monitor, configure, and control data pipelines in natural language. The company is ISO/IEC 27001 certified (TUV Austria), SOC 2 Type 2 audited, and GDPR/UK GDPR/CCPA/HIPAA compliant.
image: https://www.adverity.com/hubfs/7.%20Webpages/adverity-banner.png
layout: provider
mcp_servers:
- description: ''
  name: adverity-mcp.yml
  slug: adverity-mcpyml
modified: '2026-07-17'
name: Adverity
nav: Providers
network: true
overview: 'Adverity publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Analytics, Marketing Analytics, Data Integration, and ETL.


  Adverity''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 19 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 36.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 65.2
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 50.0
  previous_composite: 36.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Adverity Authentication
  slug: adverity-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Adverity Domain Security
  slug: adverity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adverity Vulnerability Disclosure
  slug: adverity-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: adverity
tags:
- Company
- Data Analytics
- Marketing Analytics
- Data Integration
- ETL
- Business Intelligence
- Marketing Intelligence
- MCP
website: https://www.adverity.com/
---
