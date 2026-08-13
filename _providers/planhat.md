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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.2
  scored_at: '2026-08-12'
api_count: 2
apis:
- description: Planhat's REST API for reading and writing every core Customer Platform object — companies, end users, licenses, conversations, notes, tasks, opportunities, deals, sales, invoices, assets, issues, tic
  name: Planhat REST API
  slug: planhat-rest-api
- description: High-throughput tracking endpoint for pushing user activities and product usage metrics into Planhat. Addressed by tenant UUID in the URL path (open / tenant-scoped), separate from the main authentica
  name: Planhat Analytics API
  slug: planhat-analytics-api
artifact_total: 8
asyncapis:
- description: ''
  name: Planhat Webhooks
  slug: planhat-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/planhat-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/planhat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.planhat.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.planhat.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.planhat.com/developers/api/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://www.planhat.com/developers/api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://www.planhat.com/developers/api/introduction
- group: operate
  title: ''
  type: Support
  url: https://help.planhat.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.planhat.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.planhat.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.planhat.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/planhat
- group: commercial
  title: ''
  type: Pricing
  url: https://www.planhat.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.planhat.com/legal/acceptable-use-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.planhat.com/legal/cookie-policy
- group: auth
  title: ''
  type: Compliance
  url: https://trust.planhat.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/planhat-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/planhat-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/planhat-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/planhat-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/planhat-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/planhat-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/planhat-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/planhat-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/planhat-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/planhat-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/planhat-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/planhat-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/planhat-sandbox.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/planhat-llms.txt
created: '2026-07-17'
description: Planhat is a Customer Platform that unifies customer success, product usage, revenue and post-sales operations for B2B SaaS companies. It centralizes companies, end users, licenses, conversations, NPS, health scores and time-series usage metrics, then drives playbooks, automations and revenue workflows on top of that data. Planhat exposes a REST API (api.planhat.com), a separate high-throughput analytics/tracking endpoint (analytics.planhat.com), bulk upsert, an OAuth authorization server, and a remote MCP server (api.planhat.com/v1/mcp) for AI agents. Backed by Creandum and added to the API Evangelist network; this profile was enriched from Planhat's public developer surface.
image: https://www.planhat.com/
layout: provider
mcp_servers:
- description: ''
  name: planhat-mcp.yml
  slug: planhat-mcpyml
modified: '2026-07-20'
name: Planhat
nav: Providers
network: true
overview: 'Planhat publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Saas, Customer Success, Customer Platform, and CRM.


  The Planhat catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Planhat''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, pricing, and 23 more developer resources.'
random_paper: 24
rate_limits:
- limit_count: 5
  name: Planhat Rate Limits
  slug: planhat-rate-limits
score:
  band: developing
  composite: 54.9
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 51.6
    developer_ergonomics: 67.4
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 76.3
  previous_composite: 54.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Planhat Authentication
  slug: planhat-authentication
  summary_line: http/oauth2 · 4 schemes
- kind: domain-security
  name: Planhat Domain Security
  slug: planhat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Planhat Trust Center
  slug: planhat-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: planhat
tags:
- Company
- Saas
- Customer Success
- Customer Platform
- CRM
- Customer Data
- Analytics
- Revenue
- MCP
website: https://www.planhat.com/
---
