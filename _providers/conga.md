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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.3
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: The Conga Advantage Platform REST API exposes Conga's Revenue Lifecycle Management services - Contract Lifecycle Management (CLM), cart/CPQ, catalog, user management, X-Author authoring, document- and
  name: Conga Advantage Platform REST API
  slug: conga-advantage-platform-rest-api
- description: A hosted, remote Model Context Protocol server on every regional Conga Advantage Platform gateway. It answers MCP JSON-RPC over Streamable HTTP, rejects anonymous calls with an RFC 6750 bearer challen
  name: Conga Advantage Platform MCP Server
  slug: conga-advantage-platform-mcp-server
- description: A multi-tenant GraphQL API over the Conga Advantage Platform data core, with Relay-style connections, cursor pagination, SOQL-like where predicates and Server-Sent-Event subscriptions. Each tenant get
  name: Conga GraphQL API
  slug: conga-graphql-api
artifact_total: 13
asyncapis:
- description: ''
  name: Conga Webhooks
  slug: conga-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-conga-openapi-index
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/conga-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/conga-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/conga-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/conga-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/conga-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/conga-tool-crosswalk.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/conga-graphql.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/conga-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/conga-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/conga-platform-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/conga-plans-pricing.yml
- group: start
  title: ''
  type: Login
  url: https://login.conga.com/
- group: auth
  title: ''
  type: Security
  url: https://conga.com/vulnerability-disclosure
- group: company
  title: ''
  type: Website
  url: https://www.conga.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.conga.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.conga.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.conga.com/platform/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.conga.com/revenue/docs/user-authentication-to-conga-platform
- group: auth
  title: ''
  type: Authentication
  url: authentication/conga-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/conga-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/conga-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/conga-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/conga-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/conga-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.conga.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/conga-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/conga-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://conga.com/trust-compliance-center
- group: auth
  title: ''
  type: TrustCenter
  url: security/conga-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/conga-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/conga-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/conga-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/conga-sandbox.yml
- group: operate
  title: ''
  type: Support
  url: https://conga.com/support
- group: company
  title: ''
  type: Blog
  url: https://conga.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://conga.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://conga.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://conga.com/privacy
created: '2026-07-17'
description: 'Conga (formerly Apttus + Conga) is an enterprise Revenue Lifecycle Management vendor whose Conga Advantage Platform unifies Configure-Price-Quote (CPQ), Contract Lifecycle Management (CLM), document generation and e-signature, X-Author authoring, approvals, billing and incentives, and AI-assisted contract intelligence. It is one of the largest documented API surfaces in the catalog: Conga publishes a complete OpenAPI 3.0.1 definition for every operation on its ReadMe-hosted developer portal at developer.conga.com - 2,136 operations across 31 services, captured here in openapi/. The platform is regionally partitioned (NA/EU/AU), secured with OAuth 2.0 bearer tokens minted from region-specific Conga login services that publish OIDC discovery and a real per-service scope set (api.cart, api.catalog, api.quote, api.order, api.user-management, api.revenue-admin, sign, doc-gen.composer and more), and uses JSON bodies, page/limit pagination with Content-Range headers, URI filter functions
  and a JSON:API-style error envelope. Conga also runs two machine surfaces it documents nowhere: a hosted, OAuth-gated MCP server at /mcp on every regional gateway, and a multi-tenant GraphQL API evidenced only by its own first-party npm client @conga-cloud/graphql. Conga is backed by ICONIQ Capital and Insight Partners.'
image: https://conga.com/sites/default/files/styles/large/public/image/2026-03/Social%20Share%20%281%29%20%281%29.png?itok=uH7gF5iu
layout: provider
mcp_servers:
- description: ''
  name: conga-mcp.yml
  slug: conga-mcpyml
modified: '2026-08-13'
name: Conga
nav: Providers
network: true
overview: 'Conga publishes 1 API on the [APIs.io](https://apis.io/) network: Advantage Platform REST API. Tagged areas include Company, Enterprise Software, Contract Lifecycle Management, CPQ, and Revenue Lifecycle Management.


  The Conga catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Conga''s developer surface includes CLI, documentation, API reference, getting-started guide, authentication, changelog, sandbox, and 32 more developer resources.'
plans:
- name: Conga Plans Pricing
  plan_count: 0
  slug: conga-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 2
  name: Conga Rate Limits
  slug: conga-rate-limits
scopes:
- name: Conga Scopes
  scope_count: 28
  slug: conga-scopes
  summary_line: 28 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 61.9
  delta: -3.2
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 30.3
    contract_quality: 63.1
    developer_ergonomics: 66.1
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 71.1
  previous_composite: 65.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 31
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/conga/refs/heads/main/screenshots/conga-2026-07-25T210254.png
security:
- kind: authentication
  name: Conga Authentication
  slug: conga-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Conga Domain Security
  slug: conga-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Conga Vulnerability Disclosure
  slug: conga-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Conga Trust Center
  slug: conga-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2, ISO 27001, ISO 27701, HIPAA, GDPR, CCPA, PCI
slug: conga
tags:
- Company
- Enterprise Software
- Contract Lifecycle Management
- CPQ
- Revenue Lifecycle Management
- Document Automation
- E-Signature
- Contract Intelligence
- CRM
- OpenAPI
- MCP
- GraphQL
- Billing
- Approvals
website: https://www.conga.com/
---
