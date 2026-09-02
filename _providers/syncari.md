---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: REST API for embedding and automating Syncari. Covers instance provisioning, synapse create/test/activate, entity and field pipeline authoring, validation and publishing, Quick Start install, schema (
  name: Syncari Embed API
  slug: syncari-embed-api
- description: Hosted remote MCP server that connects Claude (web and desktop) and ChatGPT to a customer's unified Syncari data. Documented capabilities include listing the datasets in an instance, running analytica
  name: Syncari MCP Server
  slug: syncari-mcp-server
artifact_total: 11
asyncapis:
- description: ''
  name: Syncari Notifications Webhooks
  slug: syncari-notifications-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/syncari-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://syncari.com/
- group: docs
  title: ''
  type: Documentation
  url: https://support.syncari.com/hc/en-us/sections/4417407653012-Get-Started-Syncari-API
- group: docs
  title: ''
  type: APIReference
  url: https://support.syncari.com/hc/en-us/sections/18707940523028-API-Reference
- group: start
  title: ''
  type: GettingStarted
  url: https://support.syncari.com/hc/en-us/articles/18707752819476-Sending-Your-First-Syncari-Embed-Request
- group: operate
  title: ''
  type: Support
  url: https://support.syncari.com/
- group: company
  title: ''
  type: Blog
  url: https://syncari.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://syncari.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://syncari.com/trial/
- group: start
  title: ''
  type: Login
  url: https://app.syncari.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://syncari.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://syncari.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.syncari.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.syncari.com/hc/en-us/sections/46253295331092-2026-Release-Notes
- group: auth
  title: ''
  type: Compliance
  url: https://syncari.com/security-overview/
- group: auth
  title: ''
  type: TrustCenter
  url: https://syncari.com/product/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/syncari-trust-center.yml
- group: build
  title: ''
  type: SDKs
  url: packages/syncari-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/syncari-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/syncari-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/syncari-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/syncari-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/syncari-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/syncari-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/syncari-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/syncari-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/syncari-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/syncari-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/syncari-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/syncari-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/syncari-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/syncari-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/syncari-notifications-webhooks.yml
created: '2026-08-29'
description: 'Syncari is an agentic master data management (MDM) and data unification platform that syncs, cleans, governs and activates business data across CRM, marketing, finance, support and warehouse systems from a single unified data model. Its multidirectional stateful sync engine connects 50+ prebuilt "Synapse" connectors plus a Python custom connector SDK, and orchestrates data through no-code entity and field pipelines, schema studio, merge/dedupe, reference datasets and insights. Syncari exposes two public developer surfaces: the Syncari Embed REST API (https://api.syncari.com/api/v1) for programmatically provisioning instances, synapses, pipelines, entities, datasets, users and roles inside an embedding product, and a hosted remote MCP server at https://mcp.syncari.com/mcp that lets Claude and ChatGPT query a customer''s unified data and trigger Syncari actions over OAuth.'
image: https://syncari.com/wp-content/themes/syncaroo/img/syncari.svg
layout: provider
mcp_servers:
- description: Syncari publishes a first-party hosted remote MCP server that exposes a customer's unified Syncari data and actions to MCP clients. Syncari documents setup for Anthropic Claude (web and desktop, Pro/M
  name: Syncari MCP Server
  slug: syncari-mcp-server
- description: ''
  name: Syncari MCP Server
  slug: syncari-mcp-server-2
modified: '2026-08-29'
name: Syncari
nav: Providers
network: true
overview: 'Syncari publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Master Data Management, data-unification, Data Integration, and iPaaS.


  The Syncari catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Syncari''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Syncari Plans Pricing
  plan_count: 0
  slug: syncari-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Syncari Rate Limits
  slug: syncari-rate-limits
scopes:
- name: Syncari Scopes
  scope_count: 0
  slug: syncari-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 60.5
  previous_composite: 51.4
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Syncari Authentication
  slug: syncari-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Syncari Domain Security
  slug: syncari-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Syncari Trust Center
  slug: syncari-trust-center
  summary_line: SOC 2 Type II, HIPAA, GDPR, CCPA, Standard Contractual Clauses (SCCs), EU-US Privacy Shield, GLBA
slug: syncari
tags:
- Company
- Master Data Management
- data-unification
- Data Integration
- iPaaS
- Data Quality
- Data Governance
- embedded-integration
- MCP
- agent-native
- Revenue Operations
- Data Synchronization
website: https://syncari.com/
---
