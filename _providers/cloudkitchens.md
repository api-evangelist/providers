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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 59
  human_in_the_loop: 0
  name: Cloudkitchens Agentic Access
  operation_count: 80
  slug: cloudkitchens-agentic-access
  summary_line: 80 operations · 59 acting
api_count: 1
apis:
- description: The CloudKitchens Public API is a resource-oriented REST API over JSON secured with OAuth 2.0, used by integration partners — ordering channels, POS and kitchen systems, delivery networks and reportin
  name: CloudKitchens Public API
  slug: cloudkitchens-public-api
artifact_total: 9
asyncapis:
- description: ''
  name: Cloudkitchens Webhooks
  slug: cloudkitchens-webhooks
collections:
- collection_type: open
  name: Public API
  slug: open-cloudkitchens-public-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cloudkitchens-mcp.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloudkitchens.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cloudkitchens.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer-guides.cloudkitchens.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developer-guides.cloudkitchens.com/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer-guides.cloudkitchens.com/docs/onboard-application/
- group: operate
  title: ''
  type: Support
  url: https://support.cloudkitchens.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://cloudkitchens.com/faq
- group: company
  title: ''
  type: Blog
  url: https://cloudkitchens.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloudkitchens.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloudkitchens.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudkitchens-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/cloudkitchens-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cloudkitchens-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cloudkitchens-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cloudkitchens-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cloudkitchens-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloudkitchens-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cloudkitchens-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer-guides.cloudkitchens.com/api-reference/
- group: design
  title: ''
  type: Conformance
  url: conformance/cloudkitchens-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cloudkitchens-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cloudkitchens-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cloudkitchens-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/cloudkitchens-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/cloudkitchens-public-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cloudkitchens-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudkitchens-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudkitchens-domain-security.yml
created: '2026-08-01'
description: 'CloudKitchens, operated by City Storage Systems, builds and runs delivery-only "ghost kitchen" facilities and the restaurant technology stack that runs them, with sites across roughly 30 countries. For integration partners it publishes the CloudKitchens Public API — an OpenAPI 3.0.1 contract of 80 operations and 27 webhook events, secured with OAuth 2.0 across 29 scopes and two flows (client credentials and authorization code), backed by an OpenID Connect identity provider at iam.cloudkitchens.com. The API spans order injection and fulfillment, menu upsert and publishing, storefront pause/resume, delivery dispatch callbacks, finance and payout reporting, inventory, reviews, loyalty, and organization/brand/store pairing. Access is partner-gated rather than self-serve: applications, webhook endpoints, and stores are onboarded manually by a CloudKitchens Account Representative, who issues the Application ID and Client Secret for the production and staging environments and provisions
  the partner-specific API base URL.'
image: https://developer.cloudkitchens.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: CloudKitchens MCP Server
  slug: cloudkitchens-mcp-server
modified: '2026-08-01'
name: CloudKitchens
nav: Providers
network: true
overview: 'CloudKitchens publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Restaurant, Ghost Kitchens, Food Delivery, Order Management, and Menu Management.


  The CloudKitchens catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  CloudKitchens'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, sandbox, and 23 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 3
  name: Cloudkitchens Rate Limits
  slug: cloudkitchens-rate-limits
scopes:
- name: Cloudkitchens Scopes
  scope_count: 31
  slug: cloudkitchens-scopes
  summary_line: 31 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 42.5
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 58.0
    developer_ergonomics: 39.9
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 39.5
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudkitchens/refs/heads/main/screenshots/cloudkitchens-2026-08-07T163508.png
security:
- kind: authentication
  name: Cloudkitchens Authentication
  slug: cloudkitchens-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cloudkitchens Domain Security
  slug: cloudkitchens-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: cloudkitchens
tags:
- Restaurant
- Ghost Kitchens
- Food Delivery
- Order Management
- Menu Management
- Storefront
- Delivery
- Reporting
- Loyalty
- Real-Estate
website: https://www.cloudkitchens.com/
---
