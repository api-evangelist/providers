---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.9
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: The REST API for Relay by Flume Health. Manages Accounts, Account Contracts, Connections, Endpoints and their per-protocol secrets and tests (API, cloud storage, database, SFTP, Snowflake, Flume Lakeh
  name: Flume Console API
  slug: flume-console-api
- description: A remote Model Context Protocol endpoint served by the Flume Console at /api/v1/context/mcp. It is protected by OAuth 2.0 and advertises RFC 9728 protected-resource metadata, returning a 401 with a WW
  name: Flume Context MCP Server
  slug: flume-context-mcp-server
artifact_total: 10
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/flume-health-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.flumehealth.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.flumehealth.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flumehealth.com/
- group: docs
  title: ''
  type: APIReference
  url: https://console.flumehealth.com/api/docs
- group: operate
  title: ''
  type: Support
  url: https://support.flumehealth.com/portal/en/home
- group: operate
  title: ''
  type: StatusPage
  url: https://status.flumehealth.com/
- group: start
  title: ''
  type: Login
  url: https://console.flumehealth.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flumehealth.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flumehealth.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flumehealth
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/flume-health-console-api-openapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/flume-health-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/flume-health-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/flume-health-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/flume-health-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/flume-health-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flume-health-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/flume-health-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/flume-health-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flume-health-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flume-health-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/flume-health-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flume-health-domain-security.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/flume-health-console-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flume-health-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/flume-health-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/flume-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/flume-health-rate-limits.yml
created: '2026-08-16'
description: Flume Health is a New York based healthcare data platform for the payer ecosystem. Its Relay product is an integration platform (iPaaS) that maps eligibility, claims, and other health plan data between source and destination Endpoints — SFTP, cloud storage, databases, Snowflake, and APIs — through a canonical Flume Data Model, with Connections, Shards, Transactions, and mapping jobs managed from the Flume Console. A newer Context layer adds a knowledge graph over a customer's data estate, natural-language query, and domain agents for actuarial, claims, coding, and compliance work, exposed to AI clients through an OAuth-protected Model Context Protocol endpoint. The public Flume Console API is a 153-operation Swagger 2.0 contract served from console.flumehealth.com, authenticated with OpenID Connect / OAuth 2.0 at auth.flumehealth.com. Flume sold its third-party administrator operations to Vitori Health in 2023 to focus on the software platform.
image: https://flumehealth.com/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: Flume Context MCP Server
  slug: flume-context-mcp-server
- description: ''
  name: Flume Health MCP Server
  slug: flume-health-mcp-server
modified: '2026-08-16'
name: Flume Health
nav: Providers
network: true
overview: 'Flume Health publishes 1 API on the [APIs.io](https://apis.io/) network: Flume Console API. Tagged areas include Healthcare, Health Plans, Payers, Healthcare Data, and Data Integration.


  Flume Health''s developer surface includes documentation, API reference, support, authentication, and 26 more developer resources.'
plans:
- name: Flume Health Plans Pricing
  plan_count: 0
  slug: flume-health-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Flume Health Rate Limits
  slug: flume-health-rate-limits
scopes:
- name: Flume Health Scopes
  scope_count: 14
  slug: flume-health-scopes
  summary_line: 14 scopes · implicit
score:
  band: developing
  composite: 49.7
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 30.3
    contract_quality: 49.2
    developer_ergonomics: 44.6
    discoverability: 68.5
    governance: 30.3
    operational_transparency: 18.4
  previous_composite: 49.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 65.0
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flume-health/refs/heads/main/screenshots/flume-health-2026-08-17T080932.png
security:
- kind: authentication
  name: Flume Health Authentication
  slug: flume-health-authentication
  summary_line: oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: Flume Health Domain Security
  slug: flume-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Flume Health Trust Center
  slug: flume-health-trust-center
  summary_line: SOC 2 Type II, HITRUST CSF, HIPAA
slug: flume-health
tags:
- Healthcare
- Health Plans
- Payers
- Healthcare Data
- Data Integration
- iPaaS
- Eligibility
- Claims
- Knowledge Graph
- MCP
- agent-native
- Authentication
- Data Engineering
- Interoperability
website: https://www.flumehealth.com/
---
