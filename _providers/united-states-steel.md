---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: United States Steel Agentic Access
  operation_count: 5
  slug: united-states-steel-agentic-access
  summary_line: 5 operations
api_count: 4
apis:
- baseURL: https://steeltrack.ussteel.com/api
  baseurl_source: declared
  description: Inventory tracking and management operations
  name: United States Steel Inventory API
  slug: united-states-steel-inventory-api
- baseURL: https://steeltrack.ussteel.com/api
  baseurl_source: declared
  description: Order status and summary reporting operations
  name: United States Steel Orders API
  slug: united-states-steel-orders-api
- baseURL: https://steeltrack.ussteel.com/api
  baseurl_source: declared
  description: Shipment history and tracking operations
  name: United States Steel Shipments API
  slug: united-states-steel-shipments-api
- baseURL: https://steeltrack.ussteel.com/api
  baseurl_source: declared
  description: Physical, mechanical, and chemical test report operations
  name: United States Steel Test Reports API
  slug: united-states-steel-test-reports-api
artifact_total: 60
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: U.S. Steel SteelTrack Inventory API
  slug: open-united-states-steel-inventory-api
- collection_type: open
  name: U.S. Steel SteelTrack Inventory Orders API
  slug: open-united-states-steel-orders-api
- collection_type: open
  name: U.S. Steel SteelTrack Inventory Shipments API
  slug: open-united-states-steel-shipments-api
- collection_type: open
  name: U.S. Steel SteelTrack API
  slug: open-united-states-steel-steeltrack
- collection_type: open
  name: U.S. Steel SteelTrack Inventory Test Reports API
  slug: open-united-states-steel-test-reports-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/united-states-steel-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/united-states-steel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/united-states-steel-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/u-s-steel
- group: company
  title: ''
  type: Website
  url: https://www.ussteel.com
- group: start
  title: ''
  type: Portal
  url: https://www.ussteel.com/customers/solutions
- group: docs
  title: ''
  type: Documentation
  url: https://www.ussteel.com/about-us/doing-business-with-u.-s.-steel
- group: design
  title: ''
  type: SpectralRules
  url: rules/united-states-steel-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/united-states-steel-vocabulary.yaml
description: United States Steel Corporation (U.S. Steel) is an integrated steel producer headquartered in Pittsburgh, Pennsylvania, with major production operations in the United States and Central Europe. The company serves customers in automotive, construction, container, energy, and industrial markets with advanced high-strength steels, coated products, hot-rolled and cold-rolled coils, electrical steel, and tubular products. U.S. Steel provides digital customer tools through the SteelTrack platform for order management, inventory tracking, shipment history, and certified test reporting.
examples:
- key_count: 10
  name: Steeltrack Inventory Item Example
  slug: steeltrack-inventory-item-example
- key_count: 2
  name: Steeltrack Inventory List Example
  slug: steeltrack-inventory-list-example
- key_count: 12
  name: Steeltrack Order Example
  slug: steeltrack-order-example
- key_count: 2
  name: Steeltrack Order List Example
  slug: steeltrack-order-list-example
- key_count: 9
  name: Steeltrack Shipment Example
  slug: steeltrack-shipment-example
- key_count: 2
  name: Steeltrack Shipment List Example
  slug: steeltrack-shipment-list-example
- key_count: 11
  name: Steeltrack Test Report Example
  slug: steeltrack-test-report-example
- key_count: 2
  name: Steeltrack Test Report List Example
  slug: steeltrack-test-report-list-example
features:
- description: Customizable reports on order availability and status across all U.S. Steel facilities.
  name: Order Status Reporting
- description: On-demand inventory reporting filterable by OP, customer, PO, and part number with flexible sorting.
  name: Inventory Tracking
- description: Load history searchable by order item, part number, and PO with optional coil-level detail.
  name: Shipment History
- description: Physical, mechanical, and chemical test reports with electronic certification signatures.
  name: Certified Test Reports
- description: SteelTrack platform operates 24 hours a day, 7 days a week with console dashboard and workflow guidance.
  name: 24/7 Availability
- description: Consolidated view across all U.S. Steel production facilities including Gary Works, Mon Valley, and Big River Steel.
  name: Multi-Facility Coverage
- description: New and updated test report information relayed throughout the day to the Test Reports System.
  name: Real-Time Updates
finops:
- name: United States Steel Finops
  service_category: API
  slug: united-states-steel-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/united-states-steel.png
integrations:
- description: SteelTrack data integrates with SAP ERP for automated purchase order management and goods receipt processing.
  name: SAP
- description: Order and inventory data connects to Oracle ERP Cloud for supply chain and procurement workflows.
  name: Oracle ERP
- description: Electronic Data Interchange for standard steel industry transaction sets including orders, shipment notices, and invoices.
  name: EDI
- description: Technology partnership with Nippon Steel Corporation following acquisition for shared manufacturing intelligence.
  name: Nippon Steel
json_schemas:
- name: InventoryItem
  property_count: 10
  slug: steeltrack-inventory-item
- name: InventoryList
  property_count: 2
  slug: steeltrack-inventory-list
- name: OrderList
  property_count: 2
  slug: steeltrack-order-list
- name: Order
  property_count: 12
  slug: steeltrack-order
- name: ShipmentList
  property_count: 2
  slug: steeltrack-shipment-list
- name: Shipment
  property_count: 9
  slug: steeltrack-shipment
- name: TestReportList
  property_count: 2
  slug: steeltrack-test-report-list
- name: TestReport
  property_count: 11
  slug: steeltrack-test-report
json_structures:
- name: Steeltrack Inventory Item Structure
  property_count: 10
  slug: steeltrack-inventory-item-structure
- name: Steeltrack Inventory List Structure
  property_count: 2
  slug: steeltrack-inventory-list-structure
- name: Steeltrack Order List Structure
  property_count: 2
  slug: steeltrack-order-list-structure
- name: Steeltrack Order Structure
  property_count: 12
  slug: steeltrack-order-structure
- name: Steeltrack Shipment List Structure
  property_count: 2
  slug: steeltrack-shipment-list-structure
- name: Steeltrack Shipment Structure
  property_count: 9
  slug: steeltrack-shipment-structure
- name: Steeltrack Test Report List Structure
  property_count: 2
  slug: steeltrack-test-report-list-structure
- name: Steeltrack Test Report Structure
  property_count: 11
  slug: steeltrack-test-report-structure
jsonld:
- class_count: 8
  name: United States Steel Steeltrack Context
  property_count: 33
  slug: united-states-steel-steeltrack-context
layout: provider
modified: '2026-05-19'
name: United States Steel
nav: Providers
network: true
overview: 'United States Steel publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Inventory API, Orders API, Shipments API, and 1 more. Tagged areas include Steel, Manufacturing, Automotive, Construction, and Energy.


  The United States Steel catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  United States Steel''s developer surface includes authentication, developer portal, documentation, and 6 more developer resources.'
plans:
- name: United States Steel Plans Pricing
  plan_count: 3
  slug: united-states-steel-plans-pricing
press:
- date: '2026-05-25'
  title: Press Releases
  url: https://www.googlecloudpresscorner.com/press-releases?o=420
- date: '2026-05-25'
  title: United States Steel Corporation Announces Strategic ...
  url: https://www.businesswire.com/news/home/20220125006271/en/United-States-Steel-Corporation-Announces-Strategic-Investment-in-Carnegie-Foundry-to-Accelerate-Advanced-Robotics-and-Autonomy-Capabilities
- date: '2026-05-25'
  title: United States Steel Corp. on Thursday announced a ...
  url: https://www.facebook.com/PghBizTimes/posts/united-states-steel-corp-on-thursday-announced-a-partnership-with-google-cloud-o/729888315817216/
- date: '2026-05-25'
  title: Media - Newsroom - www.ussteel.com
  url: https://www.ussteel.com/es/media/newsroom?p_p_id=com_liferay_blogs_web_portlet_BlogsPortlet&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&p_r_p_resetCur=false&p_r_p_categoryId=3963456&_com_liferay_blogs_web_portlet_BlogsPortlet_delta=20&_com_liferay_blogs_web_portlet_BlogsPortlet_cur=2
- date: '2026-05-25'
  title: U. S. Steel Aims to Improve Operational Efficiencies and ...
  url: https://www.ussteel.com/prereleases/-/blogs/u-s-steel-aims-to-improve-operational-efficiencies-and-employee-experiences-with-google-cloud-s-generative-ai
random_paper: 8
rate_limits:
- limit_count: 5
  name: United States Steel Rate Limits
  slug: united-states-steel-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: United States Steel API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: united-states-steel-jsonschema-spectral-rules
- effective_rule_count: 73
  extends:
  - spectral:oas
  name: United States Steel API Rules
  rule_count: 32
  severity_counts:
    error: 13
    hint: 0
    info: 6
    warn: 13
  slug: united-states-steel-spectral-rules
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 79.5
    catalog_earned_first_party: 0.0
    catalog_gap: 35.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 31.1
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 29.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 23.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/united-states-steel/refs/heads/main/screenshots/united-states-steel-2026-06-20T200102.png
security:
- kind: authentication
  name: United States Steel Authentication
  slug: united-states-steel-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: United States Steel Domain Security
  slug: united-states-steel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: united-states-steel
tags:
- Steel
- Manufacturing
- Automotive
- Construction
- Energy
- Supply Chain
- Fortune 500
use_cases:
- description: Integrate SteelTrack order and shipment data directly into customer ERP systems for automated procurement workflows.
  name: ERP Integration
- description: Automate retrieval of certified mill test reports for compliance, quality audits, and material traceability.
  name: Quality Documentation
- description: Track steel coil status from order placement through production and delivery for manufacturing planning.
  name: Supply Chain Visibility
- description: Monitor available inventory and in-transit material to optimize material release and production scheduling.
  name: Inventory Planning
- description: Access physical and chemical test data to meet automotive OEM supplier quality requirements (PPAP, IMDS).
  name: Automotive Supplier Compliance
- description: Reconcile received shipments against orders using coil-level shipping data for accounts payable processing.
  name: Shipment Reconciliation
website: https://www.ussteel.com
---
