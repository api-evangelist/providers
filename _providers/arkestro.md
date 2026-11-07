---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.1
  scored_at: '2026-11-06'
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
- baseURL: https://api.arkestro.com/api/v2/mcp
  baseurl_source: declared
  description: '# Verifying webhook signatures Arkestro signs **every** outbound webhook with **HMAC-SHA256**. The instructions below apply to all webhook events. Before you trust a delivery, verify the signature so '
  name: Arkestro Webhooks API
  slug: arkestro-webhooks-api
artifact_total: 26
asyncapis:
- description: ''
  name: Arkestro Webhooks
  slug: arkestro-webhooks
collections:
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
  href: https://artifacts.apis.io/arkestro/capabilities/arkestro-capability-edges.yml
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
  href: https://artifacts.apis.io/arkestro/security/arkestro-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/arkestro-trust-center.yml
- group: design
  href: https://artifacts.apis.io/arkestro/asyncapi/arkestro-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/arkestro-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/arkestro/mcp/arkestro-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arkestro-mcp.yml
- group: auth
  href: https://artifacts.apis.io/arkestro/scopes/arkestro-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/arkestro-scopes.yml
- group: auth
  href: https://artifacts.apis.io/arkestro/authentication/arkestro-authentication.yml
  title: ''
  type: Authentication
  url: authentication/arkestro-authentication.yml
- group: design
  href: https://artifacts.apis.io/arkestro/conventions/arkestro-conventions.yml
  title: ''
  type: Conventions
  url: conventions/arkestro-conventions.yml
- group: design
  href: https://artifacts.apis.io/arkestro/errors/arkestro-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/arkestro-problem-types.yml
- group: design
  href: https://artifacts.apis.io/arkestro/lifecycle/arkestro-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/arkestro-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/arkestro/conformance/arkestro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arkestro-conformance.yml
- group: design
  href: https://artifacts.apis.io/arkestro/data-model/arkestro-data-model.yml
  title: ''
  type: DataModel
  url: data-model/arkestro-data-model.yml
- group: agent
  href: https://artifacts.apis.io/arkestro/well-known/arkestro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arkestro-well-known.yml
- group: build
  href: https://artifacts.apis.io/arkestro/packages/arkestro-packages.yml
  title: ''
  type: Packages
  url: packages/arkestro-packages.yml
- group: agent
  href: https://artifacts.apis.io/arkestro/llms/arkestro-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arkestro-llms.txt
- group: agent
  href: https://artifacts.apis.io/arkestro/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/arkestro/agentic-access/arkestro-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/arkestro-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/arkestro/security/arkestro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arkestro-domain-security.yml
- group: other
  href: https://artifacts.apis.io/arkestro/overlays/arkestro-api-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/arkestro-api-v2-overlay.yaml
- group: build
  href: https://artifacts.apis.io/arkestro/mcp/arkestro-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/arkestro-tool-crosswalk.yml
created: '2026-08-06'
description: Arkestro is a predictive procurement orchestration platform for enterprise sourcing teams, applying negotiation science, supplier science and process science to run competitive sourcing events at scale. The platform covers sourcing events and their schedules, supplier organizations and contacts, corporate item and category catalogs, purchase orders, document and quote submissions, awards, and event analytics. It serves automotive, oil and gas, high-tech manufacturing, construction, financial services and food and beverage buyers. Arkestro publishes a public OpenAPI 3.1.1 contract for its API V2 at api.arkestro.com and operates an OAuth 2.1 remote MCP server, though its developer documentation portal sits behind a customer sign-in wall.
image: https://arkestro.com/wp-content/uploads/arkestro_logo_featured_default.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at api.arkestro.com over HTTP.
  name: Arkestro MCP Server
  slug: arkestro
modified: '2026-08-06'
name: Arkestro
nav: Providers
network: true
overview: 'Arkestro publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Webhooks API, and 1 more. Tagged areas include Procurement, Sourcing, Supply Chain, Spend Management, and eSourcing.


  The Arkestro catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Arkestro''s developer surface includes documentation, API reference, support, engineering blog, authentication, and 26 more developer resources.'
random_paper: 11
scopes:
- name: Arkestro Scopes
  scope_count: 3
  slug: arkestro-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 45.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    contract_governance: 4.5
    contract_quality: 48.7
    developer_ergonomics: 47.0
    discoverability: 75.0
    operational_transparency: 26.3
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/arkestro/arkestro-2026-08-17T122406.png
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
skill_count: 4
skills:
- name: Pull Arkestro event analytics incrementally
  slug: arkestro-pull-event-analytics
- name: Run an Arkestro sourcing event
  slug: arkestro-run-a-sourcing-event
- name: Sync suppliers and the spend catalog into Arkestro
  slug: arkestro-sync-suppliers-and-spend-catalog
- name: Verify and handle Arkestro webhooks
  slug: arkestro-verify-webhooks
slug: arkestro
tags:
- Procurement
- Sourcing
- Supply Chain
- Spend Management
- eSourcing
- Supplier Management
- Purchase Orders
- procurement-analytics
- Enterprise Software
- predictive-procurement
- MCP
- Webhook
website: https://arkestro.com/
---
