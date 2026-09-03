---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Canix Agentic Access
  operation_count: 74
  slug: canix-agentic-access
  summary_line: 74 operations · 19 acting
api_count: 1
apis:
- description: Canix's hosted Model Context Protocol server, announced 2026-07-09, connects Canix account data to AI assistants such as Claude and ChatGPT. It is published as an OAuth 2.1 protected resource at https
  name: Canix MCP Server
  slug: canix-mcp
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Audited Actions API from Canix — 1 operation(s) for audited actions.
  name: Canix Audited Actions API
  slug: canix-audited-actions-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Bill of Materials API from Canix — 2 operation(s) for bill of materials.
  name: Canix Bill of Materials API
  slug: canix-bill-of-materials-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Brands API from Canix — 1 operation(s) for brands.
  name: Canix Brands API
  slug: canix-brands-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Company API from Canix — 1 operation(s) for company.
  name: Canix Company API
  slug: canix-company-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Customers API from Canix — 3 operation(s) for customers.
  name: Canix Customers API
  slug: canix-customers-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Facilities API from Canix — 2 operation(s) for facilities.
  name: Canix Facilities API
  slug: canix-facilities-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Harvests API from Canix — 2 operation(s) for harvests.
  name: Canix Harvests API
  slug: canix-harvests-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Item Sub-Types API from Canix — 1 operation(s) for item sub-types.
  name: Canix Item Sub-Types API
  slug: canix-item-sub-types-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Item Types API from Canix — 1 operation(s) for item types.
  name: Canix Item Types API
  slug: canix-item-types-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Items API from Canix — 5 operation(s) for items.
  name: Canix Items API
  slug: canix-items-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Locations API from Canix — 3 operation(s) for locations.
  name: Canix Locations API
  slug: canix-locations-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Manufacturing Batch API from Canix — 2 operation(s) for manufacturing batch.
  name: Canix Manufacturing Batch API
  slug: canix-manufacturing-batch-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Manufacturing Run API from Canix — 2 operation(s) for manufacturing run.
  name: Canix Manufacturing Run API
  slug: canix-manufacturing-run-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Non-Cannabis Products API from Canix — 3 operation(s) for non-cannabis products.
  name: Canix Non-Cannabis Products API
  slug: canix-non-cannabis-products-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Packages API from Canix — 2 operation(s) for packages.
  name: Canix Packages API
  slug: canix-packages-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Plant Batches API from Canix — 2 operation(s) for plant batches.
  name: Canix Plant Batches API
  slug: canix-plant-batches-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Plants API from Canix — 3 operation(s) for plants.
  name: Canix Plants API
  slug: canix-plants-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Products API from Canix — 2 operation(s) for products.
  name: Canix Products API
  slug: canix-products-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Purchase Orders API from Canix — 4 operation(s) for purchase orders.
  name: Canix Purchase Orders API
  slug: canix-purchase-orders-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Sales Orders API from Canix — 7 operation(s) for sales orders.
  name: Canix Sales Orders API
  slug: canix-sales-orders-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Standard Costs API from Canix — 1 operation(s) for standard costs.
  name: Canix Standard Costs API
  slug: canix-standard-costs-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Strains API from Canix — 2 operation(s) for strains.
  name: Canix Strains API
  slug: canix-strains-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Submissions API from Canix — 1 operation(s) for submissions.
  name: Canix Submissions API
  slug: canix-submissions-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Transfer Destinations API from Canix — 2 operation(s) for transfer destinations.
  name: Canix Transfer Destinations API
  slug: canix-transfer-destinations-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Transfers API from Canix — 2 operation(s) for transfers.
  name: Canix Transfers API
  slug: canix-transfers-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The Vendors API from Canix — 2 operation(s) for vendors.
  name: Canix Vendors API
  slug: canix-vendors-api
- baseURL: https://api.canix.com/api/v1
  baseurl_source: declared
  description: The WeightUnits API from Canix — 1 operation(s) for weightunits.
  name: Canix Weight Units API
  slug: canix-weightunits-api
artifact_total: 61
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Canix Audited Actions API
  slug: open-canix-audited-actions-api
- collection_type: open
  name: Canix Bill of Materials API
  slug: open-canix-bill-of-materials-api
- collection_type: open
  name: Canix Brands API
  slug: open-canix-brands-api
- collection_type: open
  name: Canix Company API
  slug: open-canix-company-api
- collection_type: open
  name: Canix Customers API
  slug: open-canix-customers-api
- collection_type: open
  name: Canix Facilities API
  slug: open-canix-facilities-api
- collection_type: open
  name: Canix Harvests API
  slug: open-canix-harvests-api
- collection_type: open
  name: Canix Item Sub-Types API
  slug: open-canix-item-sub-types-api
- collection_type: open
  name: Canix Item Types API
  slug: open-canix-item-types-api
- collection_type: open
  name: Canix Items API
  slug: open-canix-items-api
- collection_type: open
  name: Canix Locations API
  slug: open-canix-locations-api
- collection_type: open
  name: Canix Manufacturing Batch API
  slug: open-canix-manufacturing-batch-api
- collection_type: open
  name: Canix Manufacturing Run API
  slug: open-canix-manufacturing-run-api
- collection_type: open
  name: Canix Non-Cannabis Products API
  slug: open-canix-non-cannabis-products-api
- collection_type: open
  name: Canix Packages API
  slug: open-canix-packages-api
- collection_type: open
  name: Canix Plant Batches API
  slug: open-canix-plant-batches-api
- collection_type: open
  name: Canix Plants API
  slug: open-canix-plants-api
- collection_type: open
  name: Canix Products API
  slug: open-canix-products-api
- collection_type: open
  name: Canix Purchase Orders API
  slug: open-canix-purchase-orders-api
- collection_type: open
  name: Canix Sales Orders API
  slug: open-canix-sales-orders-api
- collection_type: open
  name: Canix Standard Costs API
  slug: open-canix-standard-costs-api
- collection_type: open
  name: Canix Strains API
  slug: open-canix-strains-api
- collection_type: open
  name: Canix Submissions API
  slug: open-canix-submissions-api
- collection_type: open
  name: Canix Transfer Destinations API
  slug: open-canix-transfer-destinations-api
- collection_type: open
  name: Canix Transfers API
  slug: open-canix-transfers-api
- collection_type: open
  name: Canix Vendors API
  slug: open-canix-vendors-api
- collection_type: open
  name: Canix Weight Units API
  slug: open-canix-weightunits-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/canix-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/canix-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/canix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.canix.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.canix.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://api.canix.com/api-docs-swagger/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://api.canix.com/api-docs-swagger/index.html
- group: operate
  title: ''
  type: Support
  url: https://help.canix.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.canix.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.canix.com/campaign/schedule-a-demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.canix.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.canix.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.canix.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/canix-openapi-original.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/canix-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/canix-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/canix-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/canix-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/canix-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/canix-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/canix-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/canix-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/canix-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/canix-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/canix-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/canix-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/canix-create-and-fulfill-sales-order.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/canix-sync-inventory-and-compliance.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/canix-purchasing-and-manufacturing-costs.md
created: '2026-08-09'
description: Canix is a cannabis enterprise resource planning (ERP) and seed-to-sale platform used by licensed cultivators, manufacturers and distributors to run cultivation, processing, inventory, sales and compliance operations. The product covers plant and plant-batch tracking, harvests, packages, bills of materials, manufacturing batches and runs, purchase orders, sales orders, customers, vendors, standard costing and business intelligence reporting, with deep Metrc and BioTrack track-and-trace synchronization plus RFID and scale hardware support. Canix publishes a public OpenAPI 3.0.3 contract for its REST API at api.canix.com, and in July 2026 launched a hosted Model Context Protocol (MCP) server that lets AI assistants query Canix sales and inventory data in natural language.
image: https://assets.website-files.com/5ee52a0f4be6ffc2aaeb52cd/5ee52a0f4be6ff20e7eb534f_canix-logo.svg
layout: provider
mcp_servers:
- description: Canix operates a first-party hosted MCP server, announced 2026-07-09, that connects a Canix account to AI assistants such as Claude and ChatGPT. The endpoint was not published in the announcement post
  name: Canix MCP Server
  slug: canix-mcp-server
modified: '2026-08-09'
name: Canix
nav: Providers
network: true
overview: 'Canix publishes 27 APIs on the [APIs.io](https://apis.io/) network, including Audited Actions API, Bill of Materials API, Brands API, and 24 more. Tagged areas include Cannabis, ERP, Seed-to-Sale, Compliance, and Inventory Management.


  Canix''s developer surface includes documentation, API reference, support, engineering blog, signup flow, authentication, and 24 more developer resources.'
random_paper: 6
scopes:
- name: Canix Scopes
  scope_count: 1
  slug: canix-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 60.0
    developer_ergonomics: 47.0
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/canix/refs/heads/main/screenshots/canix-2026-08-17T080801.png
security:
- kind: authentication
  name: Canix Authentication
  slug: canix-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Canix Domain Security
  slug: canix-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: canix
tags:
- Cannabis
- ERP
- Seed-to-Sale
- Compliance
- Inventory Management
- Supply Chain
- Track and Trace
- Manufacturing
- Agriculture
- Metrc
- Cultivation
- Distribution
website: https://www.canix.com/
---
