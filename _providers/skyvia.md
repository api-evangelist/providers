---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
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
    well_known_catalog: true
  schema_version: 0.2
  score: 56.3
  scored_at: '2026-08-12'
api_count: 4
apis:
- description: REST management API for the Skyvia platform. Programmatically read and control account users and invitations, workspaces and workspace membership, on-premise agents, data-source connections, data inte
  name: Skyvia Public API
  slug: skyvia-public-api
- description: Hosted Model Context Protocol server that publishes any Skyvia connection — 200+ cloud apps and databases — as a set of MCP tools an AI assistant can call. Each customer endpoint is served from mcp.sk
  name: Skyvia Connect MCP Endpoint
  slug: skyvia-connect-mcp-endpoint
- description: Connectivity-as-a-service layer that exposes a Skyvia connection as a secured web API without writing code. An endpoint can be published as an OData v4 service (consumable from Power BI, Excel, Tablea
  name: Skyvia Connect OData & SQL Endpoints
  slug: skyvia-connect-odata-sql-endpoints
- description: Inbound webhook surface for Skyvia Automation. Each automation with a Webhook trigger is assigned a Skyvia-issued base URL plus a user-defined event name; an external application POSTs its event paylo
  name: Skyvia Automation Webhook Triggers
  slug: skyvia-automation-webhook-triggers
artifact_total: 13
asyncapis:
- description: ''
  name: Skyvia Automation Webhooks
  slug: skyvia-automation-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://skyvia.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.skyvia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.skyvia.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.skyvia.com/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.skyvia.com/concepts.html
- group: operate
  title: ''
  type: Support
  url: https://skyvia.com/support
- group: company
  title: ''
  type: Blog
  url: https://skyvia.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://skyvia.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.skyvia.com/#/signup
- group: start
  title: ''
  type: Login
  url: https://app.skyvia.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://skyvia.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://skyvia.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.skyvia.com/recent-releases/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/skyvia-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://skyvia.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/skyvia-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/skyvia-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/skyvia-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/skyvia-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/skyvia-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/skyvia-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/skyvia-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/skyvia-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/skyvia-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/skyvia-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skyvia-domain-security.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/skyvia-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/skyvia-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/skyvia-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/skyvia-automation-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/skyvia-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/skyvia-packages.yml
created: '2026-08-12'
description: 'Skyvia is a no-code cloud data platform from Devart covering five products on one account: Data Integration (import, export, replication, synchronization, data flow and control flow across 200+ cloud apps and databases), Automation (trigger-driven business process automation with schedule, polling-connection and HMAC-verified webhook triggers), Backup (cloud-to-cloud snapshot backup and restore), Query (an online SQL client and visual query builder), and Connect (a connectivity-as-a-service layer that publishes any connected data source as an OData endpoint, a SQL endpoint, or an MCP endpoint for AI agents). Skyvia also ships a public REST management API at api.skyvia.com that lets you drive accounts, workspaces, agents, connections, integrations, automations, backups and Connect endpoints programmatically with a scoped, expiring API token.'
image: https://skyvia.com/assets/img/meta-img/meta-image.png
layout: provider
mcp_servers:
- description: ''
  name: skyvia-mcp.yml
  slug: skyvia-mcpyml
- description: ''
  name: mcp
  slug: mcp
modified: '2026-08-12'
name: Skyvia
nav: Providers
network: true
overview: 'Skyvia publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include data-integration, ipaas, etl, elt, and data-replication.


  The Skyvia catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Skyvia''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Skyvia Plans Pricing
  plan_count: 0
  slug: skyvia-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 0
  name: Skyvia Rate Limits
  slug: skyvia-rate-limits
scopes:
- name: Skyvia Scopes
  scope_count: 0
  slug: skyvia-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 55.9
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 80.4
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 23.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
security:
- kind: authentication
  name: Skyvia Authentication
  slug: skyvia-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Skyvia Domain Security
  slug: skyvia-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Skyvia Trust Center
  slug: skyvia-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: skyvia
tags:
- data-integration
- ipaas
- etl
- elt
- data-replication
- cloud-backup
- odata
- sql
- workflow-automation
- no-code
- connectors
- data-management
- mcp
- agent-native
- data-access
website: https://skyvia.com/
---
