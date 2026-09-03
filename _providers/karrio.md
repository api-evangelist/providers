---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 60
  human_in_the_loop: 0
  name: Karrio Agentic Access
  operation_count: 95
  slug: karrio-agentic-access
  summary_line: 95 operations · 60 acting
api_count: 1
apis:
- baseURL: https://{karrio-instance-host}/
  baseurl_source: declared
  description: This is an object representing your Karrio shipping address. You can retrieve all addresses related to your Karrio account. Address objects are linked to your shipment history, and can be used for rec
  name: Karrio Addresses API
  slug: karrio-addresses-api
- baseURL: https://{karrio-instance-host}/
  baseurl_source: declared
  description: API instance metadata resources.
  name: Karrio API
  slug: karrio-api-api
- baseURL: https://{karrio-instance-host}/
  baseurl_source: declared
  description: API authentication resources.
  name: Karrio Auth API
  slug: karrio-auth-api
- baseURL: https://{karrio-instance-host}/
  baseurl_source: declared
  description: This is an object representing your Karrio batch operation. You can retrieve all batch operations historically for your Karrio account.
  name: Karrio Batches API
  slug: karrio-batches-api
- baseURL: https://{karrio-instance-host}/
  baseurl_source: declared
  description: This is an object representing your Karrio carrier extension. You can retrieve all supported carrier extensions available.
  name: Karrio Carriers API
  slug: karrio-carriers-api
- baseURL: https://{karrio-instance-host}/
  baseurl_source: declared
  description: This is an object representing your Karrio carrier connections. You can retrieve all carrier connections available to your account. The `carrier_id` is a friendly name you assign to your connection.
  name: Karrio Connections API
  slug: karrio-connections-api
- baseURL: https://{karrio-instance-host}/
  baseurl_source: declared
  description: This is an object representing your Karrio document upload record. A Document upload record keep traces of shipping trade documents uploaded to carriers to fast track customs and border processing.
  name: Karrio Documents API
  slug: karrio-documents-api
- baseURL: https://{karrio-instance-host}/
  baseurl_source: declared
  description: 'This is an object representing your Karrio manifest details. Some carriers require manifests to be created after labels are generated. A manifest is a summary of all the shipments that are being sent '
  name: Karrio Manifests API
  slug: karrio-manifests-api
- baseURL: https://{karrio-instance-host}/
  baseurl_source: declared
  description: This is an object representing your Karrio order. You can create Karrio orders to organize your shipments and ship line items separately.
  name: Karrio Orders API
  slug: karrio-orders-api
- baseURL: https://{karrio-instance-host}/
  baseurl_source: declared
  description: This is an object representing your Karrio shipping parcel. Parcel objects are linked to your shipment history, and can be used for recurring shipping using the same packaging.
  name: Karrio Parcels API
  slug: karrio-parcels-api
- baseURL: https://{karrio-instance-host}/
  baseurl_source: declared
  description: This is an object representing your Karrio pickup booking. You can retrieve all pickup booked historically for your Karrio account shipments.
  name: Karrio Pickups API
  slug: karrio-pickups-api
- baseURL: https://{karrio-instance-host}/
  baseurl_source: declared
  description: This is an object representing your Karrio product template. Product templates are reusable commodity definitions that can be used in customs declarations and shipment items for recurring shipments of
  name: Karrio Products API
  slug: karrio-products-api
- baseURL: https://{karrio-instance-host}/
  baseurl_source: declared
  description: In some scenarios, all we need is to send request to a carrier using the Karrio unified API. The Proxy API comes handy for that as it turn Karrio into a simple middleware that converts and validate yo
  name: Karrio Proxy API
  slug: karrio-proxy-api
- baseURL: https://{karrio-instance-host}/
  baseurl_source: declared
  description: This is an object representing your Karrio shipment. A Shipment guides you through process of preparing and purchasing a label for an order. A Shipment transitions through multiple statuses throughout
  name: Karrio Shipments API
  slug: karrio-shipments-api
- baseURL: https://{karrio-instance-host}/
  baseurl_source: declared
  description: This is an object representing your Karrio shipment tracker. A shipment tracker is an object attached to a shipment by it's tracking number. The tracker provide the latest tracking status and events a
  name: Karrio Trackers API
  slug: karrio-trackers-api
- baseURL: https://{karrio-instance-host}/
  baseurl_source: declared
  description: This is an object representing your Karrio webhook. You can configure webhook endpoints via the API to be notified about events happen in your Karrio account.
  name: Karrio Webhooks API
  slug: karrio-webhooks-api
artifact_total: 26
asyncapis:
- description: ''
  name: Karrio Webhooks
  slug: karrio-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/karrio-capability-edges.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/karrio-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://karrio.io/
- group: docs
  title: ''
  type: Documentation
  url: https://karrio.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://karrio.io/docs/api-reference
- group: company
  title: ''
  type: Blog
  url: https://karrio.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/karrioapi
- group: operate
  title: ''
  type: Support
  url: https://github.com/orgs/karrioapi/discussions
- group: commercial
  title: ''
  type: Pricing
  url: https://karrio.io/platform
- group: commercial
  title: ''
  type: TermsOfService
  url: https://karrio.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://karrio.io/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/karrioapi
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/karrio-api-openapi.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/karrio-graphql-schema.json
- group: other
  title: ''
  type: Overlay
  url: overlays/karrio-api-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/karrio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/karrio-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/karrio-cli.yml
- group: design
  title: ''
  type: Components
  url: components/karrio-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/karrio-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/karrio-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/karrio-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/karrio-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/karrio-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/karrio-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/karrio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/karrio-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/karrio-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/karrio-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/karrio-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/karrio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/karrio-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/karrio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/karrio-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/karrio-finops.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/karrio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/karrio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/karrio-authentication.yml
created: '2024-03-30'
description: Karrio is an open-source, headless multi-carrier shipping platform for developers and logistics teams. Its unified REST API and GraphQL management API abstract more than thirty carrier integrations behind one resource-oriented interface covering live rating, label generation and purchase, package tracking, pickups, manifests, orders, customs documents and webhooks. Karrio can be self-hosted from the Apache-2.0 source, run as the managed Karrio Platform, or embedded and white-labelled under a commercial license.
finops:
- name: Karrio Finops
  service_category: API
  slug: karrio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/karrio.png
layout: provider
mcp_servers:
- description: 'Karrio ships a first-party MCP server, @karrio/mcp, that exposes its multi-carrier shipping surface to MCP clients. It is a local server: it runs on the operator''s machine (stdio) or as a self-run Str'
  name: Karrio MCP Server
  slug: karrio-mcp-server
modified: '2026-08-27'
name: Karrio
nav: Providers
network: true
overview: 'Karrio publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Addresses API, Auth API, and 14 more. Tagged areas include Shipping, Logistics, Label Generation, Package Tracking, and Carriers.


  The Karrio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Karrio''s developer surface includes documentation, API reference, engineering blog, support, pricing, CLI, changelog, and 32 more developer resources.'
plans:
- name: Karrio Plans Pricing
  plan_count: 3
  slug: karrio-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Karrio Rate Limits
  slug: karrio-rate-limits
scopes:
- name: Karrio Scopes
  scope_count: 3
  slug: karrio-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: strong
  composite: 58.9
  coverage:
    artifact_dirs: 29
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 71.1
    commercial_clarity: 71.1
    contract_governance: 4.5
    contract_quality: 60.5
    developer_ergonomics: 58.9
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 36.8
  previous_composite: 58.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 66.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/karrio/refs/heads/main/screenshots/karrio-2026-06-20T183922.png
security:
- kind: authentication
  name: Karrio Authentication
  slug: karrio-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Karrio Domain Security
  slug: karrio-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Karrio Vulnerability Disclosure
  slug: karrio-vulnerability-disclosure
  summary_line: disclosure policy published
slug: karrio
tags:
- Shipping
- Logistics
- Label Generation
- Package Tracking
- Carriers
- Fulfillment
- Open-Source
- Multi-Carrier
- Rating
- Webhook
website: https://karrio.io/
---
