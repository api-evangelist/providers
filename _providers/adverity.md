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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: The Adverity Management API provides programmatic access to the Adverity platform for managing datastreams, authorizations, fetches, transformations, data mappings, destinations, workspaces, and users
  name: Adverity Management API
  slug: adverity-management-api
- description: The Adverity MCP server is a hosted, remote Model Context Protocol endpoint that connects an AI assistant to an Adverity instance so it can monitor, configure, and control data pipelines in natural la
  name: Adverity MCP Server
  slug: adverity-mcp-server
artifact_total: 10
asyncapis:
- description: ''
  name: Adverity Webhooks
  slug: adverity-webhooks
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
- group: start
  title: ''
  type: Login
  url: https://app.adverity.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.adverity.com/reference/release-notes/release-notes.html
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/adverity-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://docs.adverity.com/reference/release-notes/incidents.html
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
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/adverity-tool-crosswalk.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/adverity-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/adverity-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/adverity-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/adverity-plans-pricing.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/adverity-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/adverity-data-model.yml
created: '2026-07-17'
description: Adverity is a marketing data intelligence platform that integrates, harmonizes, transforms, and analyzes marketing and advertising data from hundreds of sources (Google Ads, Facebook Ads, LinkedIn Ads, and more) into a single, governed data foundation for reporting, dashboards, and downstream data warehouses. Adverity exposes a programmatic Management API across three surfaces (legacy /api/, /api/v1/ for cross-workspace operations, and /api/v2/ for multi-range smart-pulling) for managing datastreams, authorizations, fetches, transformations, destinations, workspaces, and users, plus a UI-configured webhook surface with three events. It also runs a hosted remote Model Context Protocol (MCP) server at https://mcp.eu.adverity.com/mcp (beta, 12 tools, OAuth 2.0 with PKCE and dynamic client registration) so AI assistants can monitor, configure, and control data pipelines in natural language. No OpenAPI is published; the REST contract is a documented endpoint table plus a public Postman
  collection, and API keys carry per-resource read/write scopes. The company is ISO/IEC 27001 certified (TUV Austria), SOC 2 Type 2 audited, and GDPR/UK GDPR/CCPA/HIPAA compliant.
image: https://www.adverity.com/hubfs/7.%20Webpages/adverity-banner.png
layout: provider
mcp_servers:
- description: ''
  name: Adverity MCP
  slug: adverity-mcp
modified: '2026-08-13'
name: Adverity
nav: Providers
network: true
overview: 'Adverity publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Analytics, Marketing Analytics, Data Integration, and ETL.


  The Adverity catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Adverity''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 27 more developer resources.'
plans:
- name: Adverity Plans Pricing
  plan_count: 0
  slug: adverity-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Adverity Rate Limits
  slug: adverity-rate-limits
scopes:
- name: Adverity Scopes
  scope_count: 0
  slug: adverity-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.7
  delta: 0.0
  facets:
    access_clarity: 46.1
    commercial_clarity: 46.1
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 61.9
    discoverability: 79.6
    governance: 18.2
    operational_transparency: 71.1
  previous_composite: 51.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adverity/refs/heads/main/screenshots/adverity-2026-07-25T181708.png
security:
- kind: authentication
  name: Adverity Authentication
  slug: adverity-authentication
  summary_line: apiKey/oauth2 · 3 schemes
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
