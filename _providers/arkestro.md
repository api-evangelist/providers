---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 22
  human_in_the_loop: 0
  name: Arkestro Agentic Access
  operation_count: 46
  slug: arkestro-agentic-access
  summary_line: 46 operations · 22 acting
api_count: 1
apis:
- description: Remote Model Context Protocol server operated by Arkestro, authorized with OAuth 2.1 authorization code flow and mandatory PKCE S256 against the mcp:read, mcp:write and offline_access scopes. The endp
  name: Arkestro MCP Server
  slug: arkestro-mcp-server
- description: The awards API from Arkestro — 1 operation(s) for awards.
  name: Arkestro Awards API
  slug: arkestro-awards-api
- description: The business unit API from Arkestro — 1 operation(s) for business unit.
  name: Arkestro business unit API
  slug: arkestro-business-unit-api
- description: Categories represent item or service groupings used in various reports and programs
  name: Arkestro corporate categories API
  slug: arkestro-corporate-categories-api
- description: Items represent goods or services under agreement in Arkestro.
  name: Arkestro corporate items API
  slug: arkestro-corporate-items-api
- description: Purchase Orders for an organization
  name: Arkestro corporate purchase orders API
  slug: arkestro-corporate-purchase-orders-api
- description: Vendor document submissions for an event
  name: Arkestro document submissions API
  slug: arkestro-document-submissions-api
- description: The event analytics API from Arkestro — 6 operation(s) for event analytics.
  name: Arkestro event analytics API
  slug: arkestro-event-analytics-api
- description: Documents attached to an event for supplier review or submission
  name: Arkestro event documents API
  slug: arkestro-event-documents-api
- description: The events API from Arkestro — 2 operation(s) for events.
  name: Arkestro Events API
  slug: arkestro-events-api
- description: Quote submissions from suppliers on events
  name: Arkestro quote submissions API
  slug: arkestro-quote-submissions-api
- description: The schedules API from Arkestro — 1 operation(s) for schedules.
  name: Arkestro Schedules API
  slug: arkestro-schedules-api
- description: Contacts represent an individual at a supplier organization
  name: Arkestro supplier contacts API
  slug: arkestro-supplier-contacts-api
- description: Supplier organizations represent external companies that supply goods or services
  name: Arkestro supplier organizations API
  slug: arkestro-supplier-organizations-api
artifact_total: 35
asyncapis:
- description: ''
  name: Arkestro Webhooks
  slug: arkestro-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: V2 Awards API
  slug: open-arkestro-awards-api
- collection_type: open
  name: V2 business unit API
  slug: open-arkestro-business-unit-api
- collection_type: open
  name: V2 corporate categories API
  slug: open-arkestro-corporate-categories-api
- collection_type: open
  name: V2 corporate items API
  slug: open-arkestro-corporate-items-api
- collection_type: open
  name: V2 corporate purchase orders API
  slug: open-arkestro-corporate-purchase-orders-api
- collection_type: open
  name: V2 document submissions API
  slug: open-arkestro-document-submissions-api
- collection_type: open
  name: V2 event analytics API
  slug: open-arkestro-event-analytics-api
- collection_type: open
  name: V2 event documents API
  slug: open-arkestro-event-documents-api
- collection_type: open
  name: V2 Events API
  slug: open-arkestro-events-api
- collection_type: open
  name: V2 quote submissions API
  slug: open-arkestro-quote-submissions-api
- collection_type: open
  name: V2 Schedules API
  slug: open-arkestro-schedules-api
- collection_type: open
  name: V2 supplier contacts API
  slug: open-arkestro-supplier-contacts-api
- collection_type: open
  name: V2 supplier organizations API
  slug: open-arkestro-supplier-organizations-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/arkestro-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://arkestro.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.arkestro.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.arkestro.com/api-docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.arkestro.com/
- group: start
  title: ''
  type: Login
  url: https://app.arkestro.com/login
- group: operate
  title: ''
  type: Support
  url: https://arkestro.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://arkestro.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bid-ops-development
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arkestro.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arkestro.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.arkestrostatus.com/
- group: auth
  title: ''
  type: Compliance
  url: https://arkestro.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/arkestro-trust-center.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/arkestro-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/arkestro-mcp.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/arkestro-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/arkestro-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/arkestro-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/arkestro-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/arkestro-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/arkestro-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/arkestro-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/arkestro-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/arkestro-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/arkestro-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/arkestro-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/arkestro-domain-security.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/arkestro-api-v2-overlay.yaml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/arkestro-tool-crosswalk.yml
created: '2026-08-06'
description: Arkestro is a predictive procurement orchestration platform for enterprise sourcing teams, applying negotiation science, supplier science and process science to run competitive sourcing events at scale. The platform covers sourcing events and their schedules, supplier organizations and contacts, corporate item and category catalogs, purchase orders, document and quote submissions, awards, and event analytics. It serves automotive, oil and gas, high-tech manufacturing, construction, financial services and food and beverage buyers. Arkestro publishes a public OpenAPI 3.1.1 contract for its API V2 at api.arkestro.com and operates an OAuth 2.1 remote MCP server, though its developer documentation portal sits behind a customer sign-in wall.
image: https://arkestro.com/wp-content/uploads/arkestro_logo_featured_default.jpg
layout: provider
mcp_servers:
- description: ''
  name: Arkestro MCP Server
  slug: arkestro-mcp-server
modified: '2026-08-06'
name: Arkestro
nav: Providers
network: true
overview: 'Arkestro publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Awards API, business unit API, corporate categories API, and 10 more. Tagged areas include Procurement, sourcing, Supply Chain, spend-management, and e-sourcing.


  The Arkestro catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Arkestro''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 26 more developer resources.'
random_paper: 14
scopes:
- name: Arkestro Scopes
  scope_count: 3
  slug: arkestro-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 45.6
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 63.9
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 46.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/arkestro/refs/heads/main/screenshots/arkestro-2026-08-17T122406.png
security:
- kind: authentication
  name: Arkestro Authentication
  slug: arkestro-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Arkestro Domain Security
  slug: arkestro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Arkestro Trust Center
  slug: arkestro-trust-center
  summary_line: ISO 27001:2022, SOC 2 Type II
slug: arkestro
tags:
- Procurement
- sourcing
- Supply Chain
- spend-management
- e-sourcing
- supplier-management
- purchase-orders
- procurement-analytics
- enterprise-software
- predictive-procurement
- MCP
- Webhook
website: https://arkestro.com/
---
