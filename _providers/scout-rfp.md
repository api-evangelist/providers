---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Scout Rfp Agentic Access
  operation_count: 25
  slug: scout-rfp-agentic-access
  summary_line: 25 operations · 11 acting
api_count: 16
apis:
- description: Manage sourcing events including RFPs, RFIs, and reverse auctions. Supports creating events from templates, updating event details, managing supplier invitations, worksheets, line items, and bid colle
  name: Events API
  slug: events-api
- description: Manage supplier companies and contacts in the Workday Strategic Sourcing platform. Supports creating, updating, and querying supplier records with version 1.1 of the API.
  name: Suppliers API
  slug: suppliers-api
- description: Manage contracts within the strategic sourcing platform, including creation, retrieval, and updates. Version 1.1 of the API.
  name: Contracts API
  slug: contracts-api
- description: Manage sourcing award decisions for completed events, tracking supplier selection outcomes and award values. Version 1.1.
  name: Awards API
  slug: awards-api
- description: Upload and manage file attachments associated with sourcing events, contracts, and other procurement objects. Version 1.0.
  name: Attachments API
  slug: attachments-api
- description: Manage payment records associated with procurement transactions and contract fulfillment. Version 1.0.
  name: Payments API
  slug: payments-api
- description: Manage procurement projects that organize and group related sourcing events and activities. Version 1.0.
  name: Projects API
  slug: projects-api
- description: Access procurement analytics and reporting data from the Workday Strategic Sourcing platform. Version 1.0.
  name: Reports API
  slug: reports-api
- description: Manage users in the Workday Strategic Sourcing platform using the SCIM 2.0 standard, enabling integration with identity providers for automated user provisioning and deprovisioning.
  name: SCIM Users API
  slug: scim-api
- description: Manage spend category taxonomies used to classify procurement spending within the Workday Strategic Sourcing platform. Version 1.0.
  name: Spend Categories API
  slug: spend-categories-api
- description: The Bids API from Scout RFP — 5 operation(s) for bids.
  name: Scout RFP Bids API
  slug: scout-rfp-bids-api
- description: The Event Suppliers API from Scout RFP — 2 operation(s) for event suppliers.
  name: Scout RFP Event Suppliers API
  slug: scout-rfp-event-suppliers-api
- description: The Event Templates API from Scout RFP — 2 operation(s) for event templates.
  name: Scout RFP Event Templates API
  slug: scout-rfp-event-templates-api
- description: The Events API from Scout RFP — 3 operation(s) for events.
  name: Scout RFP Events API
  slug: scout-rfp-events-api
- description: The Line Items API from Scout RFP — 3 operation(s) for line items.
  name: Scout RFP Line Items API
  slug: scout-rfp-line-items-api
- description: The Worksheets API from Scout RFP — 2 operation(s) for worksheets.
  name: Scout RFP Worksheets API
  slug: scout-rfp-worksheets-api
artifact_total: 46
collections:
- collection_type: open
  name: Workday Strategic Sourcing Events API
  slug: open-scout-rfp-events
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scout-rfp-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scout-rfp-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scout-rfp-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ScoutRFP
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scout-rfp
created: '2026-05-02'
description: Scout RFP is a cloud-based strategic sourcing and procurement platform that streamlines the RFP (Request for Proposal) process for procurement teams. Founded in 2014 and acquired by Workday, Scout RFP is now known as Workday Strategic Sourcing. The platform provides REST APIs for managing sourcing events, suppliers, contracts, awards, attachments, and spend categories, enabling integrations with ERP, CRM, and procurement systems.
examples:
- key_count: 3
  name: Scout Rfp List Events Example
  slug: scout-rfp-list-events-example
finops:
- name: Scout Rfp Finops
  service_category: Procurement / Sourcing SaaS
  slug: scout-rfp-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scout-rfp.png
json_schemas:
- name: BidResponse
  property_count: 1
  slug: scout-rfp-bidresponse
- name: BidsListResponse
  property_count: 1
  slug: scout-rfp-bidslistresponse
- name: Scout RFP Sourcing Event
  property_count: 4
  slug: scout-rfp-event
- name: EventCreateRequest
  property_count: 1
  slug: scout-rfp-eventcreaterequest
- name: EventResponse
  property_count: 1
  slug: scout-rfp-eventresponse
- name: EventsListResponse
  property_count: 3
  slug: scout-rfp-eventslistresponse
- name: EventTemplateResponse
  property_count: 1
  slug: scout-rfp-eventtemplateresponse
- name: EventTemplatesListResponse
  property_count: 1
  slug: scout-rfp-eventtemplateslistresponse
- name: EventUpdateRequest
  property_count: 1
  slug: scout-rfp-eventupdaterequest
- name: LineItem
  property_count: 3
  slug: scout-rfp-lineitem
- name: LineItemCreateRequest
  property_count: 1
  slug: scout-rfp-lineitemcreaterequest
- name: LineItemResponse
  property_count: 1
  slug: scout-rfp-lineitemresponse
- name: LineItemsListResponse
  property_count: 1
  slug: scout-rfp-lineitemslistresponse
- name: LineItemUpdateRequest
  property_count: 1
  slug: scout-rfp-lineitemupdaterequest
- name: SupplierRelationshipRequest
  property_count: 1
  slug: scout-rfp-supplierrelationshiprequest
- name: WorksheetResponse
  property_count: 1
  slug: scout-rfp-worksheetresponse
- name: WorksheetsListResponse
  property_count: 1
  slug: scout-rfp-worksheetslistresponse
json_structures:
- name: Scout Rfp Event Structure
  property_count: 0
  slug: scout-rfp-event-structure
- name: Scout Rfp Structure
  property_count: 0
  slug: scout-rfp-structure
jsonld:
- class_count: 2
  name: Scout Rfp Context
  property_count: 16
  slug: scout-rfp-context
layout: provider
modified: '2026-05-19'
name: Scout RFP
nav: Providers
network: true
overview: 'Scout RFP publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Bids API, Event Suppliers API, Event Templates API, and 3 more. Tagged areas include Procurement, Sourcing, RFP, Supply Chain, and Workday.


  The Scout RFP catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Scout RFP''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Scout Rfp Plans Pricing
  plan_count: 1
  slug: scout-rfp-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 1
  name: Scout Rfp Rate Limits
  slug: scout-rfp-rate-limits
rules:
- name: Scout RFP API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: scout-rfp-jsonschema-spectral-rules
- name: Scout RFP API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 3
    warn: 5
  slug: scout-rfp-rules
score:
  band: developing
  composite: 42.2
  delta: -3.9
  facets:
    commercial_clarity: 28.9
    contract_quality: 69.2
    developer_ergonomics: 10.9
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scout-rfp/refs/heads/main/screenshots/scout-rfp-2026-06-20T193553.png
security:
- kind: authentication
  name: Scout Rfp Authentication
  slug: scout-rfp-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Scout Rfp Domain Security
  slug: scout-rfp-domain-security
  summary_line: TLSv1.3
slug: scout-rfp
tags:
- Procurement
- Sourcing
- RFP
- Supply Chain
- Workday
---
