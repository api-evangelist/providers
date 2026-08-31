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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 96
  human_in_the_loop: 0
  name: Facilio Agentic Access
  operation_count: 213
  slug: facilio-agentic-access
  summary_line: 213 operations · 96 acting
api_count: 1
apis:
- description: Assets represent the equipment, machines, and devices in your facilities — HVAC units, elevators, generators, fire panels, and more. Track their lifecycle, location, warranty, and maintenance history.
  name: Facilio Assets API
  slug: facilio-assets-api
- description: Buildings belong to a site and represent individual structures. Track floor count, area, and contacts for each building.
  name: Facilio Buildings API
  slug: facilio-buildings-api
- description: Individual contacts within a client organization. Manage names, emails, and phone numbers.
  name: Facilio Client Contacts API
  slug: facilio-client-contacts-api
- description: Client credit notes for refunds and transaction adjustments. Track credit amounts, line items, and approval status for client-related credits.
  name: Facilio Client Credits API
  slug: facilio-client-credits-api
- description: Clients are the organizations you provide facility services to. Manage their contact information and associate them with sites and work orders.
  name: Facilio Clients API
  slug: facilio-clients-api
- description: User profile and utility endpoints
  name: Facilio Common API
  slug: facilio-common-api
- description: Manage your organization's custom modules — record types you define for the data and workflows that are specific to your business.
  name: Facilio Custom Modules API
  slug: facilio-custom-modules-api
- description: Floors belong to a building and represent individual levels. Track floor level, area, and associated spaces.
  name: Facilio Floors API
  slug: facilio-floors-api
- description: Material requisitions linked to work orders. Request items or tools from a storeroom.
  name: Facilio Inventory Requests API
  slug: facilio-inventory-requests-api
- description: Billing records with line items, typically created from quotes. Track costs, taxes, and approval status.
  name: Facilio Invoices API
  slug: facilio-invoices-api
- description: Consumable materials in your inventory (filters, bulbs, fasteners). Manage costing, reorder thresholds, and pricing.
  name: Facilio Item Types API
  slug: facilio-item-types-api
- description: Item balances per storeroom (read-only list, detail, and bin list); non-rotating quantity changes use the item adjustment endpoint.
  name: Facilio Items API
  slug: facilio-items-api
- description: Retrieve picklist values for enum and system lookup fields. Use these to discover valid values for fields like status, priority, category, and type. Custom picklist fields can also be queried using `G
  name: Facilio Picklists API
  slug: facilio-picklists-api
- description: Vendor purchase orders with line items; track ordered and received quantities.
  name: Facilio Purchase Orders API
  slug: facilio-purchase-orders-api
- description: Internal requisitions for materials or services, with line items. Line items on PATCH represent the full desired state.
  name: Facilio Purchase Requests API
  slug: facilio-purchase-requests-api
- description: Pricing proposals with line items. Line items on PATCH represent the full desired state — omitted items are deleted.
  name: Facilio Quotes API
  slug: facilio-quotes-api
- description: One receiving record per purchase order; list, read, and drive receipts through action endpoints.
  name: Facilio Receivables API
  slug: facilio-receivables-api
- description: Attach photos and documents to service requests, such as screenshots of issues or supporting evidence from reporters.
  name: Facilio Service Request Attachments API
  slug: facilio-service-request-attachments-api
- description: Add notes and status updates to service requests to keep requesters and assignees informed.
  name: Facilio Service Request Comments API
  slug: facilio-service-request-comments-api
- description: Service requests capture facility issues reported by occupants, tenants, or staff. They typically flow through triage, assignment, and resolution — and can be converted into work orders when maintenan
  name: Facilio Service Requests API
  slug: facilio-service-requests-api
- description: Labor and service offerings (cleaning, inspection, calibration). Define buying/selling prices, duration, and payment type.
  name: Facilio Services API
  slug: facilio-services-api
- description: Sites are the top-level locations in your portfolio — campuses, office buildings, warehouses, or any physical facility you manage. Each site can contain buildings, floors, and spaces.
  name: Facilio Sites API
  slug: facilio-sites-api
- description: Spaces are the rooms, zones, and areas within your buildings — conference rooms, lobbies, server rooms, parking areas, and more. Track occupancy, area, and category.
  name: Facilio Spaces API
  slug: facilio-spaces-api
- description: Warehouse locations where inventory is stored. Each storeroom belongs to a site and can serve multiple sites.
  name: Facilio Storerooms API
  slug: facilio-storerooms-api
- description: Individual contacts within a tenant organization.
  name: Facilio Tenant Contacts API
  slug: facilio-tenant-contacts-api
- description: Manage tenant unit (space) assignments.
  name: Facilio Tenant Units API
  slug: facilio-tenant-units-api
- description: Tenants are the organizations or individuals who occupy space in your facilities. Manage lease-related contacts, tenant types, and unit assignments.
  name: Facilio Tenants API
  slug: facilio-tenants-api
- description: Reusable equipment tracked in your inventory (drills, multimeters, ladders). Manage quantities, pricing, and approvals.
  name: Facilio Tool Types API
  slug: facilio-tool-types-api
- description: Tool balances per storeroom (read-only list, detail, and bin list); non-rotating quantity changes use the tool adjustment endpoint.
  name: Facilio Tools API
  slug: facilio-tools-api
- description: Individual contacts within a vendor organization.
  name: Facilio Vendor Contacts API
  slug: facilio-vendor-contacts-api
- description: Vendor credit notes for refunds and transaction adjustments. Track credit amounts, line items, and approval status for vendor-related credits.
  name: Facilio Vendor Credits API
  slug: facilio-vendor-credits-api
- description: Vendors are the external service providers and contractors who perform work at your facilities. Manage their contact details and associate them with work orders.
  name: Facilio Vendors API
  slug: facilio-vendors-api
- description: Attach photos, documents, invoices, and other files to work orders. Useful for before/after photos, inspection reports, and supporting documentation.
  name: Facilio Work Order Attachments API
  slug: facilio-work-order-attachments-api
- description: Add notes and updates to work orders. Comments provide an audit trail of communication between technicians, managers, and requesters.
  name: Facilio Work Order Comments API
  slug: facilio-work-order-comments-api
- description: Work orders represent maintenance tasks, repairs, and scheduled jobs across your facilities. Track them from creation through assignment, execution, and closure. Assign to staff or teams, set prioriti
  name: Facilio Work Orders API
  slug: facilio-work-orders-api
artifact_total: 77
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Facilio REST Assets API
  slug: open-facilio-assets-api
- collection_type: open
  name: Facilio REST Assets Buildings API
  slug: open-facilio-buildings-api
- collection_type: open
  name: Facilio REST Assets Client Contacts API
  slug: open-facilio-client-contacts-api
- collection_type: open
  name: Facilio REST Assets Client Credits API
  slug: open-facilio-client-credits-api
- collection_type: open
  name: Facilio REST Assets Clients API
  slug: open-facilio-clients-api
- collection_type: open
  name: Facilio REST Assets Common API
  slug: open-facilio-common-api
- collection_type: open
  name: Facilio REST Assets Custom Modules API
  slug: open-facilio-custom-modules-api
- collection_type: open
  name: Facilio REST Assets Floors API
  slug: open-facilio-floors-api
- collection_type: open
  name: Facilio REST Assets Inventory Requests API
  slug: open-facilio-inventory-requests-api
- collection_type: open
  name: Facilio REST Assets Invoices API
  slug: open-facilio-invoices-api
- collection_type: open
  name: Facilio REST Assets Item Types API
  slug: open-facilio-item-types-api
- collection_type: open
  name: Facilio REST Assets Items API
  slug: open-facilio-items-api
- collection_type: open
  name: Facilio REST Assets Picklists API
  slug: open-facilio-picklists-api
- collection_type: open
  name: Facilio REST Assets Purchase Orders API
  slug: open-facilio-purchase-orders-api
- collection_type: open
  name: Facilio REST Assets Purchase Requests API
  slug: open-facilio-purchase-requests-api
- collection_type: open
  name: Facilio REST Assets Quotes API
  slug: open-facilio-quotes-api
- collection_type: open
  name: Facilio REST Assets Receivables API
  slug: open-facilio-receivables-api
- collection_type: open
  name: Facilio REST Assets Service Request Attachments API
  slug: open-facilio-service-request-attachments-api
- collection_type: open
  name: Facilio REST Assets Service Request Comments API
  slug: open-facilio-service-request-comments-api
- collection_type: open
  name: Facilio REST Assets Service Requests API
  slug: open-facilio-service-requests-api
- collection_type: open
  name: Facilio REST Assets Services API
  slug: open-facilio-services-api
- collection_type: open
  name: Facilio REST Assets Sites API
  slug: open-facilio-sites-api
- collection_type: open
  name: Facilio REST Assets Spaces API
  slug: open-facilio-spaces-api
- collection_type: open
  name: Facilio REST Assets Storerooms API
  slug: open-facilio-storerooms-api
- collection_type: open
  name: Facilio REST Assets Tenant Contacts API
  slug: open-facilio-tenant-contacts-api
- collection_type: open
  name: Facilio REST Assets Tenant Units API
  slug: open-facilio-tenant-units-api
- collection_type: open
  name: Facilio REST Assets Tenants API
  slug: open-facilio-tenants-api
- collection_type: open
  name: Facilio REST Assets Tool Types API
  slug: open-facilio-tool-types-api
- collection_type: open
  name: Facilio REST Assets Tools API
  slug: open-facilio-tools-api
- collection_type: open
  name: Facilio REST Assets Vendor Contacts API
  slug: open-facilio-vendor-contacts-api
- collection_type: open
  name: Facilio REST Assets Vendor Credits API
  slug: open-facilio-vendor-credits-api
- collection_type: open
  name: Facilio REST Assets Vendors API
  slug: open-facilio-vendors-api
- collection_type: open
  name: Facilio REST Assets Work Order Attachments API
  slug: open-facilio-work-order-attachments-api
- collection_type: open
  name: Facilio REST Assets Work Order Comments API
  slug: open-facilio-work-order-comments-api
- collection_type: open
  name: Facilio REST Assets Work Orders API
  slug: open-facilio-work-orders-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/facilio-capability-edges.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/facilio-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/facilio-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/facilio-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/facilio-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/facilio-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/facilio-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/facilio-api-catalog.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/facilio-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/facilio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/facilio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/facilio-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/facilio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://facilio.com/ai-suite/mcp/
- group: design
  title: ''
  type: DataModel
  url: data-model/facilio-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/facilio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/facilio-packages.yml
- group: design
  title: ''
  type: Components
  url: components/facilio-components.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/facilio-v5-overlay.yaml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/facilio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://facilio.com/security/
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://facilio.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://facilio.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://facilio.com/developers/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://facilio.com/developers/docs/api-reference/
- group: commercial
  title: ''
  type: Pricing
  url: https://facilio.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://facilio.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://facilio.com/contact/
- group: operate
  title: ''
  type: HelpCenter
  url: https://facilio.com/help/
- group: start
  title: ''
  type: SignUp
  url: https://facilio.com/request-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://facilio.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://facilio.com/privacy-policy/
created: '2026-07-17'
description: Facilio is a connected operations platform for facility, property, and asset management, built around an AI-powered CMMS (Computerized Maintenance Management System). It unifies maintenance teams, vendors, tenants, and building systems so operators can run work orders, service requests, assets, inventory, purchasing, and portfolio data across multi-site real estate at scale. The platform spans Connected CMMS, the Atom AI suite, Connected Buildings (energy and sustainability), and Connected Refrigeration (IoT monitoring). Facilio exposes a versioned REST API (v5), a FOQL SQL-like query language, embeddable Connected Apps, and a hosted Model Context Protocol (MCP) server so ERP, accounting, BMS, IoT, CRM, and reporting systems — and AI agents — can query and act on operational data using the caller's existing Facilio permissions. Facilio serves retail chains, healthcare, commercial real estate portfolios, FM service providers, and education across US, EU, UK, AU, AE, and SA regions.
image: https://facilio.com/images/homepage-v2/facilio-og.png
layout: provider
mcp_servers:
- description: Connected operations platform for facility, property, and asset management. The Facilio MCP server lets agents query and act on work orders, assets, service requests, tenants, vendors, and portfolio d
  name: Facilio
  slug: facilio
modified: '2026-07-19'
name: Facilio
nav: Providers
network: true
overview: 'Facilio publishes 35 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Buildings API, Client Contacts API, and 32 more. Tagged areas include Company, Artificial Intelligence, Facility Management, CMMS, and Property Operations.


  Facilio''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, support, signup flow, and 26 more developer resources.'
random_paper: 13
scopes:
- name: Facilio Scopes
  scope_count: 7
  slug: facilio-scopes
  summary_line: 7 scopes · authorizationCode/password
score:
  band: developing
  composite: 46.2
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 54.7
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 35
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/facilio/refs/heads/main/screenshots/facilio-2026-07-25T214135.png
security:
- kind: authentication
  name: Facilio Authentication
  slug: facilio-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Facilio Domain Security
  slug: facilio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Facilio Vulnerability Disclosure
  slug: facilio-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: facilio
tags:
- Company
- Artificial Intelligence
- Facility Management
- CMMS
- Property Operations
- Maintenance
- Asset Management
- Real-Estate
- IoT
- Buildings
website: https://facilio.com
---
