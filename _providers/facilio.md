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
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 96
  human_in_the_loop: 0
  name: Facilio Agentic Access
  operation_count: 213
  slug: facilio-agentic-access
  summary_line: 213 operations · 96 acting
api_count: 35
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
artifact_total: 41
common:
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
- description: ''
  name: facilio-mcp.yml
  slug: facilio-mcpyml
modified: '2026-07-19'
name: Facilio
nav: Providers
network: true
overview: 'Facilio publishes 35 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Buildings API, Client Contacts API, and 32 more. Tagged areas include Company, Ai, Facility Management, CMMS, and Property Operations.


  Facilio''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, support, signup flow, and 25 more developer resources.'
random_paper: 31
scopes:
- name: Facilio Scopes
  scope_count: 7
  slug: facilio-scopes
  summary_line: 7 scopes · authorizationCode/password
score:
  band: developing
  composite: 49.4
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 56.5
    developer_ergonomics: 58.2
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 10.5
  previous_composite: 49.4
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
  schema_version: 0.9.1
  scored_at: '2026-08-10'
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
- Ai
- Facility Management
- CMMS
- Property Operations
- Maintenance
- Asset Management
- Real Estate
- IoT
- Buildings
website: https://facilio.com
---
