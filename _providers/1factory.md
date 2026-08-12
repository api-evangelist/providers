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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: 1Factory Agentic Access
  operation_count: 38
  slug: 1factory-agentic-access
  summary_line: 38 operations · 8 acting
api_count: 7
apis:
- description: Data shared with your organization by your customers.
  name: 1Factory Customers API
  slug: 1factory-customers-api
- description: Data related to parts manufactured by your organization.
  name: 1Factory Manufacturing API
  slug: 1factory-manufacturing-api
- description: Part Master defines the part numbers, revisions and other information for parts referenced in Plans, Inspections, FAIs etc.
  name: 1Factory Part Master API
  slug: 1factory-part-master-api
- description: Data related to Quality
  name: 1Factory QMS API
  slug: 1factory-qms-api
- description: Data related to parts received by your organization.
  name: 1Factory Receiving API
  slug: 1factory-receiving-api
- description: Data shared with your organization by your suppliers, or details about your suppliers.
  name: 1Factory Suppliers API
  slug: 1factory-suppliers-api
- description: Work Orders define a list of current work order primary & secondary identifiers that may be used as identifiers on Inspections & FAIs.
  name: 1Factory Work Orders API
  slug: 1factory-work-orders-api
artifact_total: 218
collections:
- collection_type: open
  name: 1Factory API
  slug: open-1factory
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/1factory-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/1factory-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/1factory-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/1factory
- group: company
  title: ''
  type: Website
  url: https://www.1factory.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.1factory.com/api-doc/index.html
- group: auth
  title: ''
  type: Security
  url: https://www.1factory.com/technical-overview.html
- group: operate
  title: ''
  type: Support
  url: https://1factoryhelp.zendesk.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.1factory.com/resources/TOS%20May%2020%202021.pdf
- group: operate
  title: ''
  type: RateLimits
  url: https://www.1factory.com/api-doc/index.html
- group: design
  title: ''
  type: SpectralRules
  url: rules/1factory-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/1factory-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/1factory-context.jsonld
created: '2025-02-08'
description: 1Factory is a leading provider of quality management software solutions for manufacturing companies. The platform helps businesses streamline their operations, improve efficiency, and ensure product quality at every stage of the production process. Features include real-time monitoring, automated data collection, advanced analytics, and integration with ERP and PLM systems via a REST API.
examples:
- key_count: 5
  name: 1Factory Address Example
  slug: 1factory-address-example
- key_count: 3
  name: 1Factory Assembly Entry Example
  slug: 1factory-assembly-entry-example
- key_count: 3
  name: 1Factory Assembly Example
  slug: 1factory-assembly-example
- key_count: 0
  name: 1Factory Capa Example
  slug: 1factory-capa-example
- key_count: 0
  name: 1Factory Capa List Example
  slug: 1factory-capa-list-example
- key_count: 2
  name: 1Factory Certification Example
  slug: 1factory-certification-example
- key_count: 0
  name: 1Factory Closed On Example
  slug: 1factory-closed-on-example
- key_count: 0
  name: 1Factory Complaint Example
  slug: 1factory-complaint-example
- key_count: 0
  name: 1Factory Complaint List Example
  slug: 1factory-complaint-list-example
- key_count: 0
  name: 1Factory Created By Username Example
  slug: 1factory-created-by-username-example
- key_count: 0
  name: 1Factory Created On Example
  slug: 1factory-created-on-example
- key_count: 0
  name: 1Factory Customer Name Example
  slug: 1factory-customer-name-example
- key_count: 0
  name: 1Factory Fai Detail Example
  slug: 1factory-fai-detail-example
- key_count: 28
  name: 1Factory Fai Example
  slug: 1factory-fai-example
- key_count: 0
  name: 1Factory Fai List Example
  slug: 1factory-fai-list-example
- key_count: 0
  name: 1Factory Fai Type Example
  slug: 1factory-fai-type-example
- key_count: 0
  name: 1Factory Id Example
  slug: 1factory-id-example
- key_count: 0
  name: 1Factory Insp Ident 1 Example
  slug: 1factory-insp-ident-1-example
- key_count: 0
  name: 1Factory Insp Ident 2 Example
  slug: 1factory-insp-ident-2-example
- key_count: 0
  name: 1Factory Insp Ident 3 Example
  slug: 1factory-insp-ident-3-example
- key_count: 0
  name: 1Factory Inspection Detail Example
  slug: 1factory-inspection-detail-example
- key_count: 31
  name: 1Factory Inspection Example
  slug: 1factory-inspection-example
- key_count: 0
  name: 1Factory Inspection List Example
  slug: 1factory-inspection-list-example
- key_count: 0
  name: 1Factory Inspection Type Example
  slug: 1factory-inspection-type-example
- key_count: 32
  name: 1Factory Issue Example
  slug: 1factory-issue-example
- key_count: 0
  name: 1Factory Lot Size Example
  slug: 1factory-lot-size-example
- key_count: 0
  name: 1Factory Machines Example
  slug: 1factory-machines-example
- key_count: 0
  name: 1Factory Ncr Example
  slug: 1factory-ncr-example
- key_count: 0
  name: 1Factory Ncr List Example
  slug: 1factory-ncr-list-example
- key_count: 8
  name: 1Factory New Fai Example
  slug: 1factory-new-fai-example
- key_count: 7
  name: 1Factory New Inspection Example
  slug: 1factory-new-inspection-example
- key_count: 0
  name: 1Factory New Mfg Inspection Example
  slug: 1factory-new-mfg-inspection-example
- key_count: 15
  name: 1Factory New Part Master Example
  slug: 1factory-new-part-master-example
- key_count: 0
  name: 1Factory New Rec Inspection Example
  slug: 1factory-new-rec-inspection-example
- key_count: 0
  name: 1Factory Number Of Parts Example
  slug: 1factory-number-of-parts-example
- key_count: 0
  name: 1Factory Operation Example
  slug: 1factory-operation-example
- key_count: 0
  name: 1Factory Owner Example
  slug: 1factory-owner-example
- key_count: 4
  name: 1Factory Part Data Example
  slug: 1factory-part-data-example
- key_count: 0
  name: 1Factory Part Description Example
  slug: 1factory-part-description-example
- key_count: 24
  name: 1Factory Part Master Example
  slug: 1factory-part-master-example
- key_count: 0
  name: 1Factory Part Master List Example
  slug: 1factory-part-master-list-example
- key_count: 0
  name: 1Factory Part Number Example
  slug: 1factory-part-number-example
- key_count: 0
  name: 1Factory Parts Failed Example
  slug: 1factory-parts-failed-example
- key_count: 0
  name: 1Factory Parts Passed Example
  slug: 1factory-parts-passed-example
- key_count: 19
  name: 1Factory Plan Detail Example
  slug: 1factory-plan-detail-example
- key_count: 18
  name: 1Factory Plan Example
  slug: 1factory-plan-example
- key_count: 0
  name: 1Factory Plan List Example
  slug: 1factory-plan-list-example
- key_count: 0
  name: 1Factory Project Identifier Example
  slug: 1factory-project-identifier-example
- key_count: 4
  name: 1Factory Qualification Example
  slug: 1factory-qualification-example
- key_count: 0
  name: 1Factory Rev Example
  slug: 1factory-rev-example
- key_count: 4
  name: 1Factory Spec Inspection Type Example
  slug: 1factory-spec-inspection-type-example
- key_count: 19
  name: 1Factory Specification Example
  slug: 1factory-specification-example
- key_count: 0
  name: 1Factory Status Example
  slug: 1factory-status-example
- key_count: 0
  name: 1Factory Sub Part List Example
  slug: 1factory-sub-part-list-example
- key_count: 26
  name: 1Factory Super Inspection Example
  slug: 1factory-super-inspection-example
- key_count: 18
  name: 1Factory Supplier Example
  slug: 1factory-supplier-example
- key_count: 0
  name: 1Factory Supplier List Example
  slug: 1factory-supplier-list-example
- key_count: 0
  name: 1Factory Supplier Name Example
  slug: 1factory-supplier-name-example
- key_count: 0
  name: 1Factory Supplier Number Example
  slug: 1factory-supplier-number-example
- key_count: 0
  name: 1Factory Updated On Example
  slug: 1factory-updated-on-example
- key_count: 3
  name: 1Factory User Example
  slug: 1factory-user-example
- key_count: 0
  name: 1Factory Work Order List Example
  slug: 1factory-work-order-list-example
features:
- description: Factory floor quality control, inspection planning, and statistical process control (SPC)
  name: Manufacturing Quality Control
- description: Document control, training management, audits, and compliance workflows
  name: Quality Management System (QMS)
- description: Vendor oversight, incoming inspection management, and supplier corrective actions
  name: Supplier Quality Management
- description: Automated drawing ballooning and AS9102-compliant first article inspection
  name: First Article Inspection (FAI)
- description: Real-time quality analytics and audit-ready reporting dashboards
  name: Real-Time Analytics
- description: Automatic import of CMM measurement data with SPC analysis
  name: CMM Data Integration
- description: API-based integration with ERP and PLM systems for part and work order sync
  name: ERP/PLM Integration
finops:
- name: 1Factory Finops
  service_category: API
  slug: 1factory-finops
image: /assets/icons/1factory.png
integrations:
- description: Sync part master data, work orders, and inspection records with ERP platforms
  name: ERP Systems
- description: Connect with PLM systems for design-to-manufacturing quality continuity
  name: PLM Systems
- description: Auto-import measurement data from CMM equipment directly into inspections
  name: CMM Equipment
json_schemas:
- name: Address
  property_count: 5
  slug: 1factory-address
- name: AssemblyEntry
  property_count: 3
  slug: 1factory-assembly-entry
- name: Assembly
  property_count: 3
  slug: 1factory-assembly
- name: CapaList
  property_count: 0
  slug: 1factory-capa-list
- name: Capa
  property_count: 0
  slug: 1factory-capa
- name: Certification
  property_count: 2
  slug: 1factory-certification
- name: closed_on
  property_count: 0
  slug: 1factory-closed-on
- name: ComplaintList
  property_count: 0
  slug: 1factory-complaint-list
- name: Complaint
  property_count: 0
  slug: 1factory-complaint
- name: created_by_username
  property_count: 0
  slug: 1factory-created-by-username
- name: created_on
  property_count: 0
  slug: 1factory-created-on
- name: customer_name
  property_count: 0
  slug: 1factory-customer-name
- name: FaiDetail
  property_count: 0
  slug: 1factory-fai-detail
- name: FaiList
  property_count: 0
  slug: 1factory-fai-list
- name: Fai
  property_count: 28
  slug: 1factory-fai
- name: fai_type
  property_count: 0
  slug: 1factory-fai-type
- name: ID
  property_count: 0
  slug: 1factory-id
- name: insp_ident_1
  property_count: 0
  slug: 1factory-insp-ident-1
- name: insp_ident_2
  property_count: 0
  slug: 1factory-insp-ident-2
- name: insp_ident_3
  property_count: 0
  slug: 1factory-insp-ident-3
- name: InspectionDetail
  property_count: 0
  slug: 1factory-inspection-detail
- name: InspectionList
  property_count: 0
  slug: 1factory-inspection-list
- name: Inspection
  property_count: 31
  slug: 1factory-inspection
- name: inspection_type
  property_count: 0
  slug: 1factory-inspection-type
- name: Issue
  property_count: 32
  slug: 1factory-issue
- name: lot_size
  property_count: 0
  slug: 1factory-lot-size
- name: machines
  property_count: 0
  slug: 1factory-machines
- name: NcrList
  property_count: 0
  slug: 1factory-ncr-list
- name: Ncr
  property_count: 0
  slug: 1factory-ncr
- name: NewFai
  property_count: 8
  slug: 1factory-new-fai
- name: NewInspection
  property_count: 7
  slug: 1factory-new-inspection
- name: NewMfgInspection
  property_count: 0
  slug: 1factory-new-mfg-inspection
- name: NewPartMaster
  property_count: 15
  slug: 1factory-new-part-master
- name: NewRecInspection
  property_count: 0
  slug: 1factory-new-rec-inspection
- name: number_of_parts
  property_count: 0
  slug: 1factory-number-of-parts
- name: operation
  property_count: 0
  slug: 1factory-operation
- name: owner
  property_count: 0
  slug: 1factory-owner
- name: PartData
  property_count: 4
  slug: 1factory-part-data
- name: part_description
  property_count: 0
  slug: 1factory-part-description
- name: PartMasterList
  property_count: 0
  slug: 1factory-part-master-list
- name: PartMaster
  property_count: 24
  slug: 1factory-part-master
- name: part_number
  property_count: 0
  slug: 1factory-part-number
- name: parts_failed
  property_count: 0
  slug: 1factory-parts-failed
- name: parts_passed
  property_count: 0
  slug: 1factory-parts-passed
- name: PlanDetail
  property_count: 19
  slug: 1factory-plan-detail
- name: PlanList
  property_count: 0
  slug: 1factory-plan-list
- name: Plan
  property_count: 18
  slug: 1factory-plan
- name: project_identifier
  property_count: 0
  slug: 1factory-project-identifier
- name: Qualification
  property_count: 4
  slug: 1factory-qualification
- name: rev
  property_count: 0
  slug: 1factory-rev
- name: SpecInspectionType
  property_count: 4
  slug: 1factory-spec-inspection-type
- name: Specification
  property_count: 19
  slug: 1factory-specification
- name: status
  property_count: 0
  slug: 1factory-status
- name: SubPartList
  property_count: 0
  slug: 1factory-sub-part-list
- name: SuperInspection
  property_count: 26
  slug: 1factory-super-inspection
- name: SupplierList
  property_count: 0
  slug: 1factory-supplier-list
- name: supplier_name
  property_count: 0
  slug: 1factory-supplier-name
- name: supplier_number
  property_count: 0
  slug: 1factory-supplier-number
- name: Supplier
  property_count: 18
  slug: 1factory-supplier
- name: updated_on
  property_count: 0
  slug: 1factory-updated-on
- name: User
  property_count: 3
  slug: 1factory-user
- name: WorkOrderList
  property_count: 0
  slug: 1factory-work-order-list
json_structures:
- name: 1Factory Address Structure
  property_count: 5
  slug: 1factory-address-structure
- name: 1Factory Assembly Entry Structure
  property_count: 3
  slug: 1factory-assembly-entry-structure
- name: 1Factory Assembly Structure
  property_count: 3
  slug: 1factory-assembly-structure
- name: 1Factory Capa List Structure
  property_count: 0
  slug: 1factory-capa-list-structure
- name: 1Factory Capa Structure
  property_count: 0
  slug: 1factory-capa-structure
- name: 1Factory Certification Structure
  property_count: 2
  slug: 1factory-certification-structure
- name: 1Factory Closed On Structure
  property_count: 0
  slug: 1factory-closed-on-structure
- name: 1Factory Complaint List Structure
  property_count: 0
  slug: 1factory-complaint-list-structure
- name: 1Factory Complaint Structure
  property_count: 0
  slug: 1factory-complaint-structure
- name: 1Factory Created By Username Structure
  property_count: 0
  slug: 1factory-created-by-username-structure
- name: 1Factory Created On Structure
  property_count: 0
  slug: 1factory-created-on-structure
- name: 1Factory Customer Name Structure
  property_count: 0
  slug: 1factory-customer-name-structure
- name: 1Factory Fai Detail Structure
  property_count: 0
  slug: 1factory-fai-detail-structure
- name: 1Factory Fai List Structure
  property_count: 0
  slug: 1factory-fai-list-structure
- name: 1Factory Fai Structure
  property_count: 28
  slug: 1factory-fai-structure
- name: 1Factory Fai Type Structure
  property_count: 0
  slug: 1factory-fai-type-structure
- name: 1Factory Id Structure
  property_count: 0
  slug: 1factory-id-structure
- name: 1Factory Insp Ident 1 Structure
  property_count: 0
  slug: 1factory-insp-ident-1-structure
- name: 1Factory Insp Ident 2 Structure
  property_count: 0
  slug: 1factory-insp-ident-2-structure
- name: 1Factory Insp Ident 3 Structure
  property_count: 0
  slug: 1factory-insp-ident-3-structure
- name: 1Factory Inspection Detail Structure
  property_count: 0
  slug: 1factory-inspection-detail-structure
- name: 1Factory Inspection List Structure
  property_count: 0
  slug: 1factory-inspection-list-structure
- name: 1Factory Inspection Structure
  property_count: 31
  slug: 1factory-inspection-structure
- name: 1Factory Inspection Type Structure
  property_count: 0
  slug: 1factory-inspection-type-structure
- name: 1Factory Issue Structure
  property_count: 32
  slug: 1factory-issue-structure
- name: 1Factory Lot Size Structure
  property_count: 0
  slug: 1factory-lot-size-structure
- name: 1Factory Machines Structure
  property_count: 0
  slug: 1factory-machines-structure
- name: 1Factory Ncr List Structure
  property_count: 0
  slug: 1factory-ncr-list-structure
- name: 1Factory Ncr Structure
  property_count: 0
  slug: 1factory-ncr-structure
- name: 1Factory New Fai Structure
  property_count: 8
  slug: 1factory-new-fai-structure
- name: 1Factory New Inspection Structure
  property_count: 7
  slug: 1factory-new-inspection-structure
- name: 1Factory New Mfg Inspection Structure
  property_count: 0
  slug: 1factory-new-mfg-inspection-structure
- name: 1Factory New Part Master Structure
  property_count: 15
  slug: 1factory-new-part-master-structure
- name: 1Factory New Rec Inspection Structure
  property_count: 0
  slug: 1factory-new-rec-inspection-structure
- name: 1Factory Number Of Parts Structure
  property_count: 0
  slug: 1factory-number-of-parts-structure
- name: 1Factory Operation Structure
  property_count: 0
  slug: 1factory-operation-structure
- name: 1Factory Owner Structure
  property_count: 0
  slug: 1factory-owner-structure
- name: 1Factory Part Data Structure
  property_count: 4
  slug: 1factory-part-data-structure
- name: 1Factory Part Description Structure
  property_count: 0
  slug: 1factory-part-description-structure
- name: 1Factory Part Master List Structure
  property_count: 0
  slug: 1factory-part-master-list-structure
- name: 1Factory Part Master Structure
  property_count: 24
  slug: 1factory-part-master-structure
- name: 1Factory Part Number Structure
  property_count: 0
  slug: 1factory-part-number-structure
- name: 1Factory Parts Failed Structure
  property_count: 0
  slug: 1factory-parts-failed-structure
- name: 1Factory Parts Passed Structure
  property_count: 0
  slug: 1factory-parts-passed-structure
- name: 1Factory Plan Detail Structure
  property_count: 19
  slug: 1factory-plan-detail-structure
- name: 1Factory Plan List Structure
  property_count: 0
  slug: 1factory-plan-list-structure
- name: 1Factory Plan Structure
  property_count: 18
  slug: 1factory-plan-structure
- name: 1Factory Project Identifier Structure
  property_count: 0
  slug: 1factory-project-identifier-structure
- name: 1Factory Qualification Structure
  property_count: 4
  slug: 1factory-qualification-structure
- name: 1Factory Rev Structure
  property_count: 0
  slug: 1factory-rev-structure
- name: 1Factory Spec Inspection Type Structure
  property_count: 4
  slug: 1factory-spec-inspection-type-structure
- name: 1Factory Specification Structure
  property_count: 19
  slug: 1factory-specification-structure
- name: 1Factory Status Structure
  property_count: 0
  slug: 1factory-status-structure
- name: 1Factory Sub Part List Structure
  property_count: 0
  slug: 1factory-sub-part-list-structure
- name: 1Factory Super Inspection Structure
  property_count: 26
  slug: 1factory-super-inspection-structure
- name: 1Factory Supplier List Structure
  property_count: 0
  slug: 1factory-supplier-list-structure
- name: 1Factory Supplier Name Structure
  property_count: 0
  slug: 1factory-supplier-name-structure
- name: 1Factory Supplier Number Structure
  property_count: 0
  slug: 1factory-supplier-number-structure
- name: 1Factory Supplier Structure
  property_count: 18
  slug: 1factory-supplier-structure
- name: 1Factory Updated On Structure
  property_count: 0
  slug: 1factory-updated-on-structure
- name: 1Factory User Structure
  property_count: 3
  slug: 1factory-user-structure
- name: 1Factory Work Order List Structure
  property_count: 0
  slug: 1factory-work-order-list-structure
jsonld:
- class_count: 29
  name: 1Factory Context
  property_count: 127
  slug: 1factory-context
layout: provider
modified: '2026-05-19'
name: 1Factory
nav: Providers
network: true
overview: '1Factory publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Customers API, Manufacturing API, Part Master API, and 4 more. Tagged areas include Analytics, Data Collection, Manufacturing, Monitoring, and Quality.


  The 1Factory catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  1Factory''s developer surface includes authentication, documentation, support, and 10 more developer resources.'
plans:
- name: 1Factory Plans Pricing
  plan_count: 3
  slug: 1factory-plans-pricing
random_paper: 113
rate_limits:
- limit_count: 5
  name: 1Factory Rate Limits
  slug: 1factory-rate-limits
rules:
- name: 1Factory API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: 1factory-jsonschema-spectral-rules
- name: 1Factory API Rules
  rule_count: 32
  severity_counts:
    error: 13
    hint: 0
    info: 4
    warn: 15
  slug: 1factory-spectral-rules
score:
  band: developing
  composite: 46.7
  delta: -8.6
  facets:
    commercial_clarity: 26.3
    contract_quality: 74.6
    developer_ergonomics: 23.9
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 18.4
  previous_composite: 55.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/1factory/refs/heads/main/screenshots/1factory-2026-06-20T162434.png
security:
- kind: authentication
  name: 1Factory Authentication
  slug: 1factory-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: 1Factory Domain Security
  slug: 1factory-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: 1factory
tags:
- Analytics
- Data Collection
- Manufacturing
- Monitoring
- Quality
use_cases:
- description: Create and track manufacturing inspections with measurement data and SPC analysis
  name: Manufacturing Inspection
- description: Manage supplier certifications, conduct receiving inspections, and track supplier CAPAs
  name: Supplier Qualification
- description: Log, track, and resolve non-conformances, CAPAs, and customer complaints
  name: Non-Conformance Management
- description: Conduct and document AS9102 first article inspections for aerospace and defense
  name: First Article Inspection
- description: Synchronize part master data, work orders, and inspection results with ERP systems
  name: ERP Data Sync
website: https://www.1factory.com/
---
