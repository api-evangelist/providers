---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.7
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 33
  human_in_the_loop: 0
  name: Salsify Agentic Access
  operation_count: 43
  slug: salsify-agentic-access
  summary_line: 43 operations · 33 acting
api_count: 3
apis:
- description: 'The Salsify REST API gives programmatic access to everything in a Salsify organization: products, records, properties, digital assets, list membership, imports and export runs. All request and respons'
  name: Salsify REST API
  slug: rest
- description: Early-access public GraphQL API for operating on Salsify accounts, organizations, configuration manifests and organization provisioning requests. Authenticated with a bearer API token; introspection r
  name: Salsify GraphQL API
  slug: graphql
- description: First-party remote Model Context Protocol server hosted by Salsify at app.salsify.com/mcp. Streamable HTTP transport, protected by OAuth 2.1 with RFC 9728 protected-resource metadata pointing at the a
  name: Salsify MCP Server
  slug: mcp
artifact_total: 13
asyncapis:
- description: ''
  name: Salsify Webhooks
  slug: salsify-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/salsify-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.salsify.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.salsify.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.salsify.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developers.salsify.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.salsify.com/docs/integration-with-salsify
- group: auth
  title: ''
  type: Authentication
  url: authentication/salsify-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/salsify-scopes.yml
- group: operate
  title: ''
  type: Support
  url: https://help.salsify.com/ProductXM/s/
- group: company
  title: ''
  type: Blog
  url: https://www.salsify.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/salsify
- group: start
  title: ''
  type: SignUp
  url: https://www.salsify.com/demo
- group: start
  title: ''
  type: Login
  url: https://app.salsify.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.salsify.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salsify.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.salsify.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.salsify.com/security-and-reliability
- group: auth
  title: ''
  type: TrustCenter
  url: security/salsify-trust-center.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/salsify-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/salsify-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/salsify-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/salsify-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/salsify-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/salsify-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/salsify-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/salsify-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/salsify-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/salsify-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/salsify-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/salsify-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salsify-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://www.salsify.com/responsible-disclosure
- group: other
  title: ''
  type: Overlay
  url: overlays/salsify-api-settings-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/salsify-write-operations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/salsify-non-v1-endpoints-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/salsify-llms.txt
created: '2026-08-02'
description: Salsify is a product experience management (PXM) and supplier experience management (SXM) platform used by brands, distributors and retailers to centralize product content, digital assets and syndication to the digital shelf. The Salsify platform exposes a REST API at app.salsify.com/api/v1/orgs covering products, records, properties, digital assets, list membership, imports and export runs, an early-access GraphQL API at api.salsify.com/graphql for accounts, organizations and configuration manifests, a webhook surface for product, digital asset, channel and import events with X.509/SHA-256 signature verification, and an OAuth 2.0 authorization server plus a first-party Model Context Protocol server at app.salsify.com/mcp.
graphqls:
- description: 'updatedAt: 2026-05-19T13:41:04.000Z'
  name: GraphQL Schema Overview
  slug: salsify-graphql-schema-overview
image: https://www.salsify.com/hubfs/Salsify%20-%20Product%20Experience%20Management%20PXM%20-%20Feature%20Image.png
layout: provider
mcp_servers:
- description: ''
  name: salsify-mcp.yml
  slug: salsify-mcpyml
modified: '2026-08-02'
name: Salsify
nav: Providers
network: true
overview: 'Salsify publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Company, Product Experience Management, Product Information Management, Digital Asset Management, and Commerce.


  The Salsify catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Salsify''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, signup flow, and 30 more developer resources.'
random_paper: 85
rate_limits:
- limit_count: 2
  name: Salsify Rate Limits
  slug: salsify-rate-limits
scopes:
- name: Salsify Scopes
  scope_count: 2
  slug: salsify-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: strong
  composite: 60.4
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 66.7
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 76.3
  previous_composite: 60.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Salsify Authentication
  slug: salsify-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Salsify Domain Security
  slug: salsify-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Salsify Vulnerability Disclosure
  slug: salsify-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Salsify Trust Center
  slug: salsify-trust-center
  summary_line: SOC 2 Type II, ISO 27001:2013
slug: salsify
tags:
- Company
- Product Experience Management
- Product Information Management
- Digital Asset Management
- Commerce
- Retail
- Syndication
- Data Management
- SaaS
website: https://www.salsify.com/
---
