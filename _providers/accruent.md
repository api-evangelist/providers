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
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 128
  human_in_the_loop: 0
  name: Accruent Agentic Access
  operation_count: 255
  slug: accruent-agentic-access
  summary_line: 255 operations · 128 acting
api_count: 1
apis:
- description: REST API for Accruent Siterra, the wireless/telecom site and project lifecycle management product, fronted by the Accruent Developer Network on Azure API Management. Subscription-key auth via the accr
  name: Siterra API
  slug: siterra-api
- description: REST APIs for Accruent Meridian Cloud engineering document management — asset APIs, relationship APIs and contractor package APIs used by PowerWeb, Meridian Portal, Meridian Explorer and Meridian Mobi
  name: Meridian Cloud API
  slug: meridian-cloud-api
- description: RESTful API layer for Accruent EMS space and event scheduling, documented as a Platform as a Service surface with JWT authentication. The Swagger UI ships with the deployment rather than on a public h
  name: EMS Platform Services
  slug: ems-platform-services
- description: RESTful API for Accruent Lucernex IWMS / lease accounting. Documented on the public customer help site, but the schema browser and console are served from the customer's own tenancy at {tenant-url}/en
  name: Lucernex REST API
  slug: lucernex-rest-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The AssetDocuments API from Accruent — 4 operation(s) for assetdocuments.
  name: Accruent Asset Documents API
  slug: accruent-assetdocuments-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The AssetImages API from Accruent — 4 operation(s) for assetimages.
  name: Accruent Asset Images API
  slug: accruent-assetimages-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The AssetMeterHistory API from Accruent — 6 operation(s) for assetmeterhistory.
  name: Accruent Asset Meter History API
  slug: accruent-assetmeterhistory-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The Assets API from Accruent — 2 operation(s) for assets.
  name: Accruent Assets API
  slug: accruent-assets-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The AssetSpecifications API from Accruent — 4 operation(s) for assetspecifications.
  name: Accruent Asset Specifications API
  slug: accruent-assetspecifications-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The Classifications API from Accruent — 2 operation(s) for classifications.
  name: Accruent Classifications API
  slug: accruent-classifications-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The Companies API from Accruent — 2 operation(s) for companies.
  name: Accruent Companies API
  slug: accruent-companies-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The ExternalInterface API from Accruent — 2 operation(s) for externalinterface.
  name: Accruent External Interface API
  slug: accruent-externalinterface-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The Invoices API from Accruent — 4 operation(s) for invoices.
  name: Accruent Invoices API
  slug: accruent-invoices-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The Labors API from Accruent — 2 operation(s) for labors.
  name: Accruent Labors API
  slug: accruent-labors-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The Log API from Accruent — 2 operation(s) for log.
  name: Accruent Log API
  slug: accruent-log-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The LookupTableValues API from Accruent — 4 operation(s) for lookuptablevalues.
  name: Accruent Lookup Table Values API
  slug: accruent-lookuptablevalues-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The PartDocuments API from Accruent — 4 operation(s) for partdocuments.
  name: Accruent Part Documents API
  slug: accruent-partdocuments-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The PartLocations API from Accruent — 4 operation(s) for partlocations.
  name: Accruent Part Locations API
  slug: accruent-partlocations-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The Parts API from Accruent — 2 operation(s) for parts.
  name: Accruent Parts API
  slug: accruent-parts-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The PartTransactions API from Accruent — 4 operation(s) for parttransactions.
  name: Accruent Part Transactions API
  slug: accruent-parttransactions-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The PartVendors API from Accruent — 6 operation(s) for partvendors.
  name: Accruent Part Vendors API
  slug: accruent-partvendors-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The PurchaseOrderNote API from Accruent — 3 operation(s) for purchaseordernote.
  name: Accruent Purchase Order Note API
  slug: accruent-purchaseordernote-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The PurchaseOrderStatusUpdates API from Accruent — 1 operation(s) for purchaseorderstatusupdates.
  name: Accruent Purchase Order Status Updates API
  slug: accruent-purchaseorderstatusupdates-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The ReceiptLineItems API from Accruent — 4 operation(s) for receiptlineitems.
  name: Accruent Receipt Line Items API
  slug: accruent-receiptlineitems-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The Receipts API from Accruent — 4 operation(s) for receipts.
  name: Accruent Receipts API
  slug: accruent-receipts-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The Schema API from Accruent — 1 operation(s) for schema.
  name: Accruent Schema API
  slug: accruent-schema-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The SpecificationAssetSpecifications API from Accruent — 2 operation(s) for specificationassetspecifications.
  name: Accruent Specification Asset Specifications API
  slug: accruent-specificationassetspecifications-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The Specifications API from Accruent — 2 operation(s) for specifications.
  name: Accruent Specifications API
  slug: accruent-specifications-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The WorkOrderAssignments API from Accruent — 4 operation(s) for workorderassignments.
  name: Accruent Work Order Assignments API
  slug: accruent-workorderassignments-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The WorkOrderDocuments API from Accruent — 4 operation(s) for workorderdocuments.
  name: Accruent Work Order Documents API
  slug: accruent-workorderdocuments-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The WorkOrderImages API from Accruent — 4 operation(s) for workorderimages.
  name: Accruent Work Order Images API
  slug: accruent-workorderimages-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The WorkOrderLaborCostActuals API from Accruent — 4 operation(s) for workorderlaborcostactuals.
  name: Accruent Work Order Labor Cost Actuals API
  slug: accruent-workorderlaborcostactuals-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The WorkOrderLaborCostEstimates API from Accruent — 4 operation(s) for workorderlaborcostestimates.
  name: Accruent Work Order Labor Cost Estimates API
  slug: accruent-workorderlaborcostestimates-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The WorkOrderMiscCostActuals API from Accruent — 4 operation(s) for workordermisccostactuals.
  name: Accruent Work Order Misc Cost Actuals API
  slug: accruent-workordermisccostactuals-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The WorkOrderMiscCostEstimates API from Accruent — 4 operation(s) for workordermisccostestimates.
  name: Accruent Work Order Misc Cost Estimates API
  slug: accruent-workordermisccostestimates-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The WorkOrderPartActuals API from Accruent — 4 operation(s) for workorderpartactuals.
  name: Accruent Work Order Part Actuals API
  slug: accruent-workorderpartactuals-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The WorkOrderPartEstimates API from Accruent — 4 operation(s) for workorderpartestimates.
  name: Accruent Work Order Part Estimates API
  slug: accruent-workorderpartestimates-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The WorkOrderStatusUpdates API from Accruent — 1 operation(s) for workorderstatusupdates.
  name: Accruent Work Order Status Updates API
  slug: accruent-workorderstatusupdates-api
- baseURL: https://api.maintenanceconnection.com/v8
  baseurl_source: declared
  description: The WorkOrderTasks API from Accruent — 4 operation(s) for workordertasks.
  name: Accruent Work Order Tasks API
  slug: accruent-workordertasks-api
- baseURL: https://api.accruent.com/siterra/us/
  baseurl_source: declared
  description: The Lookup Tables API from Accruent — 2 operation(s) for lookup tables.
  name: Accruent Lookup Tables API
  slug: accruent-lookup-tables-api
- baseURL: https://api.accruent.com/siterra/us/
  baseurl_source: declared
  description: The Purchase Order Line Items API from Accruent — 4 operation(s) for purchase order line items.
  name: Accruent Purchase Order Line Items API
  slug: accruent-purchase-order-line-items-api
- baseURL: https://api.accruent.com/siterra/us/
  baseurl_source: declared
  description: The Purchase Orders API from Accruent — 2 operation(s) for purchase orders.
  name: Accruent Purchase Orders API
  slug: accruent-purchase-orders-api
- baseURL: https://api.accruent.com/siterra/us/
  baseurl_source: declared
  description: The Work Orders API from Accruent — 2 operation(s) for work orders.
  name: Accruent Work Orders API
  slug: accruent-work-orders-api
artifact_total: 56
common:
- group: other
  href: https://artifacts.apis.io/accruent/capabilities/accruent-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/accruent-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/accruent/security/accruent-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accruent-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/accruent/agentic-access/accruent-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/accruent-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.accruent.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.accruent.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.accruent.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.maintenanceconnection.com/v8/help/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.accruent.com/wiki/siterra/gettingstarted
- group: operate
  title: ''
  type: Support
  url: https://www.accruent.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.accruent.com/resources/blog-posts
- group: company
  title: ''
  type: BlogRSS
  url: https://www.accruent.com/resources/blog-posts/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Accruent
- group: commercial
  title: ''
  type: Pricing
  url: https://www.accruent.com/product-pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.accruent.com/products/maintenance-connection/free-trial
- group: start
  title: ''
  type: Login
  url: https://developer.accruent.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.accruent.com/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.accruent.com/privacy-notice
- group: operate
  title: ''
  type: StatusPage
  url: https://status.accruent.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.accruent.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.accruent.com/security-compliance-certifications
- group: operate
  href: https://artifacts.apis.io/accruent/changelog/accruent-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/accruent-changelog.yml
- group: design
  href: https://artifacts.apis.io/accruent/lifecycle/accruent-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/accruent-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/accruent/authentication/accruent-authentication.yml
  title: ''
  type: Authentication
  url: authentication/accruent-authentication.yml
- group: design
  href: https://artifacts.apis.io/accruent/conventions/accruent-conventions.yml
  title: ''
  type: Conventions
  url: conventions/accruent-conventions.yml
- group: design
  href: https://artifacts.apis.io/accruent/conformance/accruent-conformance.yml
  title: ''
  type: Conformance
  url: conformance/accruent-conformance.yml
- group: design
  href: https://artifacts.apis.io/accruent/errors/accruent-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/accruent-problem-types.yml
- group: design
  href: https://artifacts.apis.io/accruent/data-model/accruent-data-model.yml
  title: ''
  type: DataModel
  url: data-model/accruent-data-model.yml
- group: operate
  href: https://artifacts.apis.io/accruent/rate-limits/accruent-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/accruent-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/accruent/plans/accruent-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/accruent-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/accruent/packages/accruent-packages.yml
  title: ''
  type: Packages
  url: packages/accruent-packages.yml
- group: agent
  href: https://artifacts.apis.io/accruent/mcp/accruent-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/accruent-mcp.yml
- group: agent
  href: https://artifacts.apis.io/accruent/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/accruent/llms/accruent-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/accruent-llms.txt
- group: other
  href: https://artifacts.apis.io/accruent/overlays/accruent-maintenance-connection-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/accruent-maintenance-connection-overlay.yaml
created: '2026-09-06'
description: Accruent is a workplace, facilities and asset management software company serving more than 10,000 customers in over 150 countries, with a portfolio spanning CMMS/EAM (Maintenance Connection), engineering document management (Meridian), IWMS and lease accounting (Lucernex), space and event scheduling (EMS), telecom and wireless site management (Siterra), and IoT condition monitoring (Observe). Its public API surface is an Azure API Management developer network at developer.accruent.com plus per-product REST APIs; the Maintenance Connection Web API is the only contract published without a login — a Swagger 2.0 document describing 255 operations across assets, work orders, parts, purchasing, labor and lookup tables. Every other product API (Siterra, Meridian Cloud, EMS Platform Services, Lucernex) is documented publicly but its machine-readable definition sits behind developer-program approval or a customer tenancy.
finops:
- has_sources: true
  method: derived
  name: Accruent Finops
  primary_unit: user
  service_category: ''
  slug: accruent-finops
  template: false
image: https://www.accruent.com/hubfs/accruent-social-share.png
layout: provider
mcp_servers:
- description: MCP server requiring an API key; 172 tools listed. A candidate, not confirmed as published by the provider.
  name: Accruent MCP Server
  slug: accruent-maintenance-connection
modified: '2026-09-06'
name: Accruent
nav: Providers
network: true
overview: 'Accruent publishes 43 API contracts indexed on the [APIs.io](https://apis.io/) network, including Asset Documents API, Asset Images API, Asset Meter History API, and 40 more. Tagged areas include Facilities Management, Asset Management, CMMS, EAM, and Maintenance.


  The Accruent catalog on APIs.io includes 1 Spectral governance ruleset.


  Accruent''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 27 more developer resources.'
plans:
- name: Accruent Plans Pricing
  plan_count: 8
  slug: accruent-plans-pricing
- name: Accruent Price Estimates
  plan_count: 0
  slug: accruent-price-estimates
random_paper: 13
rate_limits:
- limit_count: 1
  name: Accruent Rate Limits
  slug: accruent-rate-limits
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Accruent API Rules
  rule_count: 42
  severity_counts:
    error: 37
    hint: 0
    info: 2
    warn: 3
  slug: accruent-rules
score:
  band: strong
  composite: 59.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 59.5
    catalog_earned_first_party: 20.0
    catalog_gap: 55.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 35.7
    developer_ergonomics: 66.1
    discoverability: 57.1
    operational_transparency: 47.4
  previous_composite: 59.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 39
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/accruent/accruent-2026-10-11T092543.png
security:
- kind: authentication
  name: Accruent Authentication
  slug: accruent-authentication
  summary_line: http/apiKey · 4 schemes
- kind: domain-security
  name: Accruent Domain Security
  slug: accruent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Accruent Trust Center
  slug: accruent-trust-center
  summary_line: ISO/IEC 27001, SOC 2, SOC 1
skill_count: 3
skills:
- name: Read the asset register and post meter readings
  slug: accruent-asset-register-and-meters
- name: Create and dispatch a Maintenance Connection work order
  slug: accruent-create-and-dispatch-work-order
- name: Run purchasing from order to receipt to invoice
  slug: accruent-procure-to-receipt
slug: accruent
tags:
- Facilities Management
- Asset Management
- CMMS
- EAM
- Maintenance
- Work Orders
- IWMS
- Space Management
- Engineering Document Management
- Built Environment
- Enterprise Software
- Real Estate
website: https://www.accruent.com/
---
