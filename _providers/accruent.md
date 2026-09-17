---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.6
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 131
  human_in_the_loop: 0
  name: Accruent Agentic Access
  operation_count: 255
  slug: accruent-agentic-access
  summary_line: 255 operations · 131 acting
api_count: 2
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
artifact_total: 50
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/accruent/refs/heads/main/security/accruent-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accruent-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/accruent/refs/heads/main/agentic-access/accruent-agentic-access.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/accruent/refs/heads/main/changelog/accruent-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/accruent-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accruent/refs/heads/main/lifecycle/accruent-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/accruent-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/accruent/refs/heads/main/authentication/accruent-authentication.yml
  title: ''
  type: Authentication
  url: authentication/accruent-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accruent/refs/heads/main/conventions/accruent-conventions.yml
  title: ''
  type: Conventions
  url: conventions/accruent-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accruent/refs/heads/main/conformance/accruent-conformance.yml
  title: ''
  type: Conformance
  url: conformance/accruent-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accruent/refs/heads/main/errors/accruent-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/accruent-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accruent/refs/heads/main/data-model/accruent-data-model.yml
  title: ''
  type: DataModel
  url: data-model/accruent-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/accruent/refs/heads/main/rate-limits/accruent-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/accruent-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/accruent/refs/heads/main/plans/accruent-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/accruent-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/accruent/refs/heads/main/packages/accruent-packages.yml
  title: ''
  type: Packages
  url: packages/accruent-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/accruent/refs/heads/main/mcp/accruent-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/accruent-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/accruent/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/accruent/refs/heads/main/llms/accruent-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/accruent-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/accruent/refs/heads/main/overlays/accruent-maintenance-connection-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/accruent-maintenance-connection-overlay.yaml
created: '2026-09-06'
description: Accruent is a workplace, facilities and asset management software company serving more than 10,000 customers in over 150 countries, with a portfolio spanning CMMS/EAM (Maintenance Connection), engineering document management (Meridian), IWMS and lease accounting (Lucernex), space and event scheduling (EMS), telecom and wireless site management (Siterra), and IoT condition monitoring (Observe). Its public API surface is an Azure API Management developer network at developer.accruent.com plus per-product REST APIs; the Maintenance Connection Web API is the only contract published without a login — a Swagger 2.0 document describing 255 operations across assets, work orders, parts, purchasing, labor and lookup tables. Every other product API (Siterra, Meridian Cloud, EMS Platform Services, Lucernex) is documented publicly but its machine-readable definition sits behind developer-program approval or a customer tenancy.
image: https://www.accruent.com/hubfs/accruent-social-share.png
layout: provider
mcp_servers:
- description: ''
  name: Accruent MCP Server
  slug: accruent-mcp-server
modified: '2026-09-06'
name: Accruent
nav: Providers
network: true
overview: 'Accruent publishes 39 APIs on the [APIs.io](https://apis.io/) network, including Asset Documents API, Asset Images API, Asset Meter History API, and 36 more. Tagged areas include Facilities Management, Asset Management, CMMS, EAM, and Maintenance.


  Accruent''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Accruent Plans Pricing
  plan_count: 8
  slug: accruent-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Accruent Rate Limits
  slug: accruent-rate-limits
score:
  band: strong
  composite: 54.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 52.0
    catalog_earned_first_party: 20.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 37.3
    developer_ergonomics: 66.1
    discoverability: 59.3
    operational_transparency: 47.4
  previous_composite: 53.7
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
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- Real-Estate
website: https://www.accruent.com/
---
