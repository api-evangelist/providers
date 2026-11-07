---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 96
  human_in_the_loop: 0
  name: Facilio Agentic Access
  operation_count: 213
  slug: facilio-agentic-access
  summary_line: 213 operations · 96 acting
api_count: 1
apis:
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Assets represent the equipment, machines, and devices in your facilities — HVAC units, elevators, generators, fire panels, and more. Track their lifecycle, location, warranty, and maintenance history.
  name: Facilio Assets API
  slug: facilio-assets-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Buildings belong to a site and represent individual structures. Track floor count, area, and contacts for each building.
  name: Facilio Buildings API
  slug: facilio-buildings-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Individual contacts within a client organization. Manage names, emails, and phone numbers.
  name: Facilio Client Contacts API
  slug: facilio-client-contacts-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Client credit notes for refunds and transaction adjustments. Track credit amounts, line items, and approval status for client-related credits.
  name: Facilio Client Credits API
  slug: facilio-client-credits-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Clients are the organizations you provide facility services to. Manage their contact information and associate them with sites and work orders.
  name: Facilio Clients API
  slug: facilio-clients-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: User profile and utility endpoints
  name: Facilio Common API
  slug: facilio-common-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Manage your organization's custom modules — record types you define for the data and workflows that are specific to your business.
  name: Facilio Custom Modules API
  slug: facilio-custom-modules-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Floors belong to a building and represent individual levels. Track floor level, area, and associated spaces.
  name: Facilio Floors API
  slug: facilio-floors-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Material requisitions linked to work orders. Request items or tools from a storeroom.
  name: Facilio Inventory Requests API
  slug: facilio-inventory-requests-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Billing records with line items, typically created from quotes. Track costs, taxes, and approval status.
  name: Facilio Invoices API
  slug: facilio-invoices-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Consumable materials in your inventory (filters, bulbs, fasteners). Manage costing, reorder thresholds, and pricing.
  name: Facilio Item Types API
  slug: facilio-item-types-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Item balances per storeroom (read-only list, detail, and bin list); non-rotating quantity changes use the item adjustment endpoint.
  name: Facilio Items API
  slug: facilio-items-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Retrieve picklist values for enum and system lookup fields. Use these to discover valid values for fields like status, priority, category, and type. Custom picklist fields can also be queried using `G
  name: Facilio Picklists API
  slug: facilio-picklists-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Vendor purchase orders with line items; track ordered and received quantities.
  name: Facilio Purchase Orders API
  slug: facilio-purchase-orders-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Internal requisitions for materials or services, with line items. Line items on PATCH represent the full desired state.
  name: Facilio Purchase Requests API
  slug: facilio-purchase-requests-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Pricing proposals with line items. Line items on PATCH represent the full desired state — omitted items are deleted.
  name: Facilio Quotes API
  slug: facilio-quotes-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: One receiving record per purchase order; list, read, and drive receipts through action endpoints.
  name: Facilio Receivables API
  slug: facilio-receivables-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Attach photos and documents to service requests, such as screenshots of issues or supporting evidence from reporters.
  name: Facilio Service Request Attachments API
  slug: facilio-service-request-attachments-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Add notes and status updates to service requests to keep requesters and assignees informed.
  name: Facilio Service Request Comments API
  slug: facilio-service-request-comments-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Service requests capture facility issues reported by occupants, tenants, or staff. They typically flow through triage, assignment, and resolution — and can be converted into work orders when maintenan
  name: Facilio Service Requests API
  slug: facilio-service-requests-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Labor and service offerings (cleaning, inspection, calibration). Define buying/selling prices, duration, and payment type.
  name: Facilio Services API
  slug: facilio-services-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Sites are the top-level locations in your portfolio — campuses, office buildings, warehouses, or any physical facility you manage. Each site can contain buildings, floors, and spaces.
  name: Facilio Sites API
  slug: facilio-sites-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Spaces are the rooms, zones, and areas within your buildings — conference rooms, lobbies, server rooms, parking areas, and more. Track occupancy, area, and category.
  name: Facilio Spaces API
  slug: facilio-spaces-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Warehouse locations where inventory is stored. Each storeroom belongs to a site and can serve multiple sites.
  name: Facilio Storerooms API
  slug: facilio-storerooms-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Individual contacts within a tenant organization.
  name: Facilio Tenant Contacts API
  slug: facilio-tenant-contacts-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Manage tenant unit (space) assignments.
  name: Facilio Tenant Units API
  slug: facilio-tenant-units-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Tenants are the organizations or individuals who occupy space in your facilities. Manage lease-related contacts, tenant types, and unit assignments.
  name: Facilio Tenants API
  slug: facilio-tenants-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Reusable equipment tracked in your inventory (drills, multimeters, ladders). Manage quantities, pricing, and approvals.
  name: Facilio Tool Types API
  slug: facilio-tool-types-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Tool balances per storeroom (read-only list, detail, and bin list); non-rotating quantity changes use the tool adjustment endpoint.
  name: Facilio Tools API
  slug: facilio-tools-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Individual contacts within a vendor organization.
  name: Facilio Vendor Contacts API
  slug: facilio-vendor-contacts-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Vendor credit notes for refunds and transaction adjustments. Track credit amounts, line items, and approval status for vendor-related credits.
  name: Facilio Vendor Credits API
  slug: facilio-vendor-credits-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Vendors are the external service providers and contractors who perform work at your facilities. Manage their contact details and associate them with work orders.
  name: Facilio Vendors API
  slug: facilio-vendors-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Attach photos, documents, invoices, and other files to work orders. Useful for before/after photos, inspection reports, and supporting documentation.
  name: Facilio Work Order Attachments API
  slug: facilio-work-order-attachments-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Add notes and updates to work orders. Comments provide an audit trail of communication between technicians, managers, and requesters.
  name: Facilio Work Order Comments API
  slug: facilio-work-order-comments-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Work orders represent maintenance tasks, repairs, and scheduled jobs across your facilities. Track them from creation through assignment, execution, and closure. Assign to staff or teams, set prioriti
  name: Facilio Work Orders API
  slug: facilio-work-orders-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Amenities are the perks a facility offers (projector, catering, whiteboard, ...), referenced from a facility's `amenities` list.
  name: Facilio Amenities API
  slug: facilio-amenities-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Deliveries track packages received on-site for employees, including carrier, tracking number, and delivery status.
  name: Facilio Deliveries API
  slug: facilio-deliveries-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Delivery areas are the drop-off locations packages are received at, referenced by deliveries.
  name: Facilio Delivery Areas API
  slug: facilio-delivery-areas-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Departments are organizational units used to group employees and desks, with rollup counts of each.
  name: Facilio Departments API
  slug: facilio-departments-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Desks are individual workstations within a space, assignable to employees and departments for hot-desking or fixed seating.
  name: Facilio Desks API
  slug: facilio-desks-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Attach documents and photos to an employee record.
  name: Facilio Employee Attachments API
  slug: facilio-employee-attachments-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Notes on an employee record.
  name: Facilio Employee Comments API
  slug: facilio-employee-comments-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Employee records — your internal staff (a People-extended module) with name, contact details, designation, and department — used for assignment and directory lookups.
  name: Facilio Employees API
  slug: facilio-employees-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Facilities are bookable resources configured for slot-based booking — conference rooms, hot-desk pools, or parking areas — with pricing, capacity, and availability rules.
  name: Facilio Facilities API
  slug: facilio-facilities-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Facility bookings reserve one or more facility slots, with attendee tracking, cancellation, and an approval/state-flow lifecycle.
  name: Facilio Facility Bookings API
  slug: facilio-facility-bookings-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Facility slots are the pre-generated, bookable time windows for a facility, produced by a scheduled job. Read-only — browse availability, then reference a slot when creating a facility booking.
  name: Facilio Facility Slots API
  slug: facilio-facility-slots-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Date-range overrides on a facility's normal availability — an extra window or a blackout, optionally at a special cost.
  name: Facilio Facility Special Availability API
  slug: facilio-facility-special-availability-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: A facility's recurring weekly availability windows (e.g. "Mondays 9am-5pm"), used with the nightly slot-generation job to produce bookable slots.
  name: Facilio Facility Weekday Availability API
  slug: facilio-facility-weekday-availability-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Indoor floor plans are the visual maps of a floor, mapping desks, rooms, and other spaces to on-screen coordinates for the floor plan viewer and booking UI.
  name: Facilio Indoor Floor Plans API
  slug: facilio-indoor-floor-plans-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Attach reference documents, SOPs, and diagrams to a job plan.
  name: Facilio Job Plan Attachments API
  slug: facilio-job-plan-attachments-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Notes and discussion on a job plan.
  name: Facilio Job Plan Comments API
  slug: facilio-job-plan-comments-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Job plans are reusable task templates — ordered checklists of work — that drive preventive maintenance and inspections. Each plan holds task sections with input-type tasks (readings, text, numeric, op
  name: Facilio Job Plans API
  slug: facilio-job-plans-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Lockers are storage units within a space, assignable to employees.
  name: Facilio Lockers API
  slug: facilio-lockers-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Parking stalls are individual parking spaces within a site, categorized by parking type and mode, and optionally assignable to employees.
  name: Facilio Parking Stalls API
  slug: facilio-parking-stalls-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Read-only view of item purchase batches — per-batch quantity, remaining stock, unit cost, and serial tracking. Records are produced by the inventory receipt and purchase-order flows, not created direc
  name: Facilio Purchased Items API
  slug: facilio-purchased-items-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Rooms are a specialized space type — meeting rooms, phone rooms, wellness rooms, and more — categorized by room type.
  name: Facilio Rooms API
  slug: facilio-rooms-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Space bookings reserve a space, desk, or parking stall for a time window, with attendee tracking and a booking lifecycle (pending, booked, checked in, checked out, cancelled).
  name: Facilio Space Bookings API
  slug: facilio-space-bookings-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Attach method statements, risk assessments, photos, and supporting documents to a work permit.
  name: Facilio Work Permit Attachments API
  slug: facilio-work-permit-attachments-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: The safety checklist items on a permit — filled and reviewed through its lifecycle — plus the read-only permit-type checklist templates and categories they are generated from.
  name: Facilio Work Permit Checklists API
  slug: facilio-work-permit-checklists-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Notes and the communication trail on a work permit between requesters, issuers, and reviewers.
  name: Facilio Work Permit Comments API
  slug: facilio-work-permit-comments-api
- baseURL: https://us.facilioapis.com/maintenance/api/v5
  baseurl_source: declared
  description: Work permits authorize and control high-risk work (hot work, confined space, working at height, and similar). A permit is raised against a permit type, auto-populated with a safety checklist, and adva
  name: Facilio Work Permits API
  slug: facilio-work-permits-api
artifact_total: 108
collections:
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
- group: commercial
  href: https://artifacts.apis.io/facilio/plans/facilio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/facilio-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://facilio.com/blog/rss/
- group: other
  href: https://artifacts.apis.io/facilio/capabilities/facilio-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/facilio-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/facilio/security/facilio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/facilio-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/facilio/agentic-access/facilio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/facilio-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/facilio/scopes/facilio-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/facilio-scopes.yml
- group: auth
  href: https://artifacts.apis.io/facilio/authentication/facilio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/facilio-authentication.yml
- group: agent
  href: https://artifacts.apis.io/facilio/mcp/facilio-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/facilio-mcp.yml
- group: agent
  href: https://artifacts.apis.io/facilio/well-known/facilio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/facilio-well-known.yml
- group: other
  href: https://artifacts.apis.io/facilio/well-known/facilio-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/facilio-api-catalog.json
- group: agent
  href: https://artifacts.apis.io/facilio/llms/facilio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/facilio-llms.txt
- group: design
  href: https://artifacts.apis.io/facilio/conventions/facilio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/facilio-conventions.yml
- group: design
  href: https://artifacts.apis.io/facilio/errors/facilio-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/facilio-problem-types.yml
- group: design
  href: https://artifacts.apis.io/facilio/lifecycle/facilio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/facilio-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/facilio/conformance/facilio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/facilio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://facilio.com/ai-suite/mcp/
- group: design
  href: https://artifacts.apis.io/facilio/data-model/facilio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/facilio-data-model.yml
- group: build
  href: https://artifacts.apis.io/facilio/packages/facilio-packages.yml
  title: ''
  type: Packages
  url: packages/facilio-packages.yml
- group: build
  href: https://artifacts.apis.io/facilio/packages/facilio-packages.yml
  title: ''
  type: SDKs
  url: packages/facilio-packages.yml
- group: design
  href: https://artifacts.apis.io/facilio/components/facilio-components.yml
  title: ''
  type: Components
  url: components/facilio-components.yml
- group: other
  href: https://artifacts.apis.io/facilio/overlays/facilio-v5-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/facilio-v5-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/facilio/security/facilio-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/facilio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://facilio.com/security/
- group: agent
  href: https://artifacts.apis.io/facilio/skills/_index.yml
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
finops:
- has_sources: true
  method: derived
  name: Facilio Finops
  primary_unit: ''
  service_category: ''
  slug: facilio-finops
  template: true
image: https://facilio.com/images/homepage-v2/facilio-og.png
layout: provider
mcp_servers:
- description: Connected operations platform for facility, property, and asset management. The Facilio MCP server lets agents query and act on work orders, assets, service requests, tenants, vendors, and portfolio d
  name: Facilio
  slug: facilio
modified: '2026-10-06'
name: Facilio
nav: Providers
network: true
overview: 'Facilio publishes 61 API contracts indexed on the [APIs.io](https://apis.io/) network, including Assets API, Buildings API, Client Contacts API, and 58 more. Tagged areas include Company, Artificial Intelligence, Facility Management, CMMS, and Property Operations.


  The Facilio catalog on APIs.io includes 1 Spectral governance ruleset.


  Facilio''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, support, signup flow, and 28 more developer resources.'
plans:
- name: Facilio Plans Pricing
  plan_count: 3
  slug: facilio-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 112
  extends:
  - spectral:oas
  name: Facilio API Rules
  rule_count: 71
  severity_counts:
    error: 59
    hint: 0
    info: 4
    warn: 8
  slug: facilio-rules
scopes:
- name: Facilio Scopes
  scope_count: 7
  slug: facilio-scopes
  summary_line: 7 scopes · authorizationCode/password
score:
  band: strong
  composite: 59.6
  coverage:
    artifact_dirs: 29
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 84.2
    contract_governance: 31.8
    contract_quality: 52.5
    developer_ergonomics: 54.2
    discoverability: 75.0
    operational_transparency: 10.5
  previous_composite: 58.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 62.9
      total: 97
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/facilio/facilio-2026-07-25T214135.png
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
skill_count: 3
skills:
- name: Create and track a maintenance work order
  slug: facilio-create-work-order
- name: Sync assets with an external system
  slug: facilio-sync-assets
- name: Triage a tenant service request
  slug: facilio-triage-service-request
slug: facilio
tags:
- Company
- Artificial Intelligence
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
