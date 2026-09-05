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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.7
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Internal API for activity operations including conversation creation
  name: Phasio Activity Internal API
  slug: phasio-activity-internal-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for managing addresses for customers and organizations
  name: Phasio Addresses API
  slug: phasio-addresses-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: The cart-resource API from Phasio — 4 operation(s) for cart-resource.
  name: Phasio cart-resource API
  slug: phasio-cart-resource-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: The constraint-resource API from Phasio — 4 operation(s) for constraint-resource.
  name: Phasio constraint-resource API
  slug: phasio-constraint-resource-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing customer communications and activity
  name: Phasio Customer Activity Controller API
  slug: phasio-customer-activity-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing customer shipping and billing addresses
  name: Phasio Customer Addresses API
  slug: phasio-customer-addresses-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for tracking customer analytics events
  name: Phasio Customer Analytics Controller API
  slug: phasio-customer-analytics-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for viewing assemblies
  name: Phasio Customer Assembly Controller API
  slug: phasio-customer-assembly-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Internal endpoints for managing customer authentication
  name: Phasio Customer Authentication API
  slug: phasio-customer-authentication-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing customer shopping carts
  name: Phasio Customer Cart Controller API
  slug: phasio-customer-cart-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing customer shopping cart items
  name: Phasio Customer Cart Item Controller API
  slug: phasio-customer-cart-item-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for accessing manufacturing capabilities catalog
  name: Phasio Customer Catalog Controller API
  slug: phasio-customer-catalog-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing customer information
  name: Phasio Customer Controller API
  slug: phasio-customer-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for retrieving country and jurisdiction information
  name: Phasio Customer Country Controller API
  slug: phasio-customer-country-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for customer discount operations
  name: Phasio Customer Discount Controller API
  slug: phasio-customer-discount-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for retrieving order-related documents
  name: Phasio Customer Document Controller API
  slug: phasio-customer-document-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for customers to view expenses on their orders
  name: Phasio Customer Expense Controller API
  slug: phasio-customer-expense-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for customers to retrieve information about the operator
  name: Phasio Customer Operator Controller API
  slug: phasio-customer-operator-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing customer manufacturing orders
  name: Phasio Customer Order Controller API
  slug: phasio-customer-order-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing customer organization details
  name: Phasio Customer Organisation Controller API
  slug: phasio-customer-organisation-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for customers to access their part designs
  name: Phasio Customer Part Design Controller API
  slug: phasio-customer-part-design-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing 3D part revisions and files
  name: Phasio Customer Part Revision Controller API
  slug: phasio-customer-part-revision-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing customer projects
  name: Phasio Customer Project Controller API
  slug: phasio-customer-project-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for customers to view requisitions in their orders
  name: Phasio Customer Requisition Controller API
  slug: phasio-customer-requisition-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing customer shipments and shipping calculations
  name: Phasio Customer Shipment Controller API
  slug: phasio-customer-shipment-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for customers to manage files attached to threads
  name: Phasio Customer Thread File Controller API
  slug: phasio-customer-thread-file-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: The equation-resource API from Phasio — 3 operation(s) for equation-resource.
  name: Phasio equation-resource API
  slug: phasio-equation-resource-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing 3D file analysis and processing
  name: Phasio File Analysis Controller API
  slug: phasio-file-analysis-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for handling incoming emails to the system
  name: Phasio Inbound Email Controller API
  slug: phasio-inbound-email-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing accounting system integrations
  name: Phasio Internal Accounting Controller API
  slug: phasio-internal-accounting-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for internal customer management operations
  name: Phasio Internal Customer Controller API
  slug: phasio-internal-customer-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing customer organizations from internal services
  name: Phasio Internal Customer Organisation Controller API
  slug: phasio-internal-customer-organisation-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing operator configuration and settings
  name: Phasio Internal Operator Controller API
  slug: phasio-internal-operator-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for internal order processing operations
  name: Phasio Internal Order Controller API
  slug: phasio-internal-order-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing accounting system integrations
  name: Phasio Manufacturer Accounting API
  slug: phasio-manufacturer-accounting-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing manufacturer activities and conversations
  name: Phasio Manufacturer Activity Controller API
  slug: phasio-manufacturer-activity-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Programmatic analytics endpoints for retrieving manufacturer dashboard metrics, funnel performance, revenue, production, customer and material insights.
  name: Phasio Manufacturer Analytics Controller API
  slug: phasio-manufacturer-analytics-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing assemblies
  name: Phasio Manufacturer Assembly Controller API
  slug: phasio-manufacturer-assembly-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for exporting CAMSPEC files and managing manifest mappings
  name: Phasio Manufacturer CAMSPEC Controller API
  slug: phasio-manufacturer-camspec-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for managing cart items
  name: Phasio Manufacturer Cart Item Controller API
  slug: phasio-manufacturer-cart-item-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing manufacturer catalog items
  name: Phasio Manufacturer Catalog Controller API
  slug: phasio-manufacturer-catalog-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for retrieving color options for manufactured parts
  name: Phasio Manufacturer Color Controller API
  slug: phasio-manufacturer-color-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: The Manufacturer Countries Controller API from Phasio — 2 operation(s) for manufacturer countries controller.
  name: Phasio Manufacturer Countries Controller API
  slug: phasio-manufacturer-countries-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: The Manufacturer Currencies Controller API from Phasio — 1 operation(s) for manufacturer currencies controller.
  name: Phasio Manufacturer Currencies Controller API
  slug: phasio-manufacturer-currencies-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for managing customer records and operations
  name: Phasio Manufacturer Customer Controller API
  slug: phasio-manufacturer-customer-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for managing customer organizations
  name: Phasio Manufacturer Customer Organisation Controller API
  slug: phasio-manufacturer-customer-organisation-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for managing discounts
  name: Phasio Manufacturer Discount Controller API
  slug: phasio-manufacturer-discount-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for generating and downloading various document types
  name: Phasio Manufacturer Document Controller API
  slug: phasio-manufacturer-document-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing document templates for invoices, orders, and consignment labels
  name: Phasio Manufacturer Document Template Controller API
  slug: phasio-manufacturer-document-template-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for managing order expenses
  name: Phasio Manufacturer Expense Controller API
  slug: phasio-manufacturer-expense-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing 3D printing infill options and configurations
  name: Phasio Manufacturer Infill Controller API
  slug: phasio-manufacturer-infill-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing Kanban board columns for order processing workflow
  name: Phasio Manufacturer Kanban Column Controller API
  slug: phasio-manufacturer-kanban-column-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing production lead time options for orders
  name: Phasio Manufacturer Lead Time Controller API
  slug: phasio-manufacturer-lead-time-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing manufacturing materials
  name: Phasio Manufacturer Material Controller API
  slug: phasio-manufacturer-material-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing material pricing configuration
  name: Phasio Manufacturer Material Prices Controller API
  slug: phasio-manufacturer-material-prices-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for tracking and recording system metrics and events
  name: Phasio Manufacturer Metrics Controller API
  slug: phasio-manufacturer-metrics-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing operator contact information and details
  name: Phasio Manufacturer Operator Contact Controller API
  slug: phasio-manufacturer-operator-contact-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing operator settings and information
  name: Phasio Manufacturer Operator Controller API
  slug: phasio-manufacturer-operator-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing sequential counters used by operators for numbering orders, projects, etc.
  name: Phasio Manufacturer Operator Count Controller API
  slug: phasio-manufacturer-operator-count-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for managing manufacturing orders and their lifecycle
  name: Phasio Manufacturer Order Controller API
  slug: phasio-manufacturer-order-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for managing part designs
  name: Phasio Manufacturer Part Design Controller API
  slug: phasio-manufacturer-part-design-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing part geometry revisions and 3D file analysis
  name: Phasio Manufacturer Part Revision Controller API
  slug: phasio-manufacturer-part-revision-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing part specifications and customer article references
  name: Phasio Manufacturer Part Specification Controller API
  slug: phasio-manufacturer-part-specification-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing operator payment information and settings
  name: Phasio Manufacturer Payment Information Controller API
  slug: phasio-manufacturer-payment-information-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing post-processing options for manufactured parts
  name: Phasio Manufacturer Post Processing Controller API
  slug: phasio-manufacturer-post-processing-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing precision prices for manufacturing operations
  name: Phasio Manufacturer Precision Prices Controller API
  slug: phasio-manufacturer-precision-prices-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing manufacturing process pricing configurations
  name: Phasio Manufacturer Process Prices Controller API
  slug: phasio-manufacturer-process-prices-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing production status configurations for manufacturing workflow
  name: Phasio Manufacturer Production Status Controller API
  slug: phasio-manufacturer-production-status-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing production steps in the manufacturing workflow
  name: Phasio Manufacturer Production Step Controller API
  slug: phasio-manufacturer-production-step-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing manufacturer programmatic clients
  name: Phasio Manufacturer Programmatic Client Controller API
  slug: phasio-manufacturer-programmatic-client-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: RSQL-enabled endpoints for managing projects with advanced querying and updating capabilities
  name: Phasio Manufacturer Project Controller API
  slug: phasio-manufacturer-project-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing order quotes and pricing
  name: Phasio Manufacturer Quote Controller API
  slug: phasio-manufacturer-quote-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for downloadable manufacturer reports
  name: Phasio Manufacturer Reports API
  slug: phasio-manufacturer-reports-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for managing part requisitions and production batches
  name: Phasio Manufacturer Requisition Controller API
  slug: phasio-manufacturer-requisition-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Manage routing templates on a part specification
  name: Phasio Manufacturer Routing Template Controller API
  slug: phasio-manufacturer-routing-template-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Global search across parts, orders, customers, files, catalog references, and production steps
  name: Phasio Manufacturer Search Controller API
  slug: phasio-manufacturer-search-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: This controller is responsible for managing shipments. It allows you to get rates and fetch existing shipments.
  name: Phasio Manufacturer Shipment Controller API
  slug: phasio-manufacturer-shipment-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing shipping box dimensions used for shipments
  name: Phasio Manufacturer Shipping Box Controller API
  slug: phasio-manufacturer-shipping-box-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing shipping methods available to manufacturers
  name: Phasio Manufacturer Shipping Method Controller API
  slug: phasio-manufacturer-shipping-method-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing tax components and rates
  name: Phasio Manufacturer Tax Component Controller API
  slug: phasio-manufacturer-tax-component-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing tax jurisdictions and their associated tax components
  name: Phasio Manufacturer Tax Jurisdiction Controller API
  slug: phasio-manufacturer-tax-jurisdiction-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing communication threads and projects
  name: Phasio Manufacturer Thread Controller API
  slug: phasio-manufacturer-thread-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: API for managing files attached to threads
  name: Phasio Manufacturer Thread File Controller API
  slug: phasio-manufacturer-thread-file-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing shipment tracking information
  name: Phasio Manufacturer Tracking Controller API
  slug: phasio-manufacturer-tracking-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing manufacturer user information
  name: Phasio Manufacturer User Controller API
  slug: phasio-manufacturer-user-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Manage individual work orders, including downstream routing mutations
  name: Phasio Manufacturer Work Order Controller API
  slug: phasio-manufacturer-work-order-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for tracking system metrics and events
  name: Phasio Metrics Controller API
  slug: phasio-metrics-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: The payment-term-resource API from Phasio — 2 operation(s) for payment-term-resource.
  name: Phasio payment-term-resource API
  slug: phasio-payment-term-resource-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for retrieving pre-order information
  name: Phasio Pre-Order API
  slug: phasio-pre-order-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing user authentication and multi-factor authentication
  name: Phasio User Authentication Controller API
  slug: phasio-user-authentication-controller-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: The webhook-resource API from Phasio — 2 operation(s) for webhook-resource.
  name: Phasio webhook-resource API
  slug: phasio-webhook-resource-api
- baseURL: https://m-api.eu.phas.io/api/manufacturer/v1
  baseurl_source: declared
  description: Endpoints for managing webhooks
  name: Phasio Webhooks API
  slug: phasio-webhooks-api
artifact_total: 189
asyncapis:
- description: ''
  name: Phasio Webhooks
  slug: phasio-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Phasio Activity Internal API
  slug: open-phasio-activity-internal-api
- collection_type: open
  name: Phasio Activity Internal Addresses API
  slug: open-phasio-addresses-api
- collection_type: open
  name: Phasio Activity Internal cart-resource API
  slug: open-phasio-cart-resource-api
- collection_type: open
  name: Phasio Activity Internal constraint-resource API
  slug: open-phasio-constraint-resource-api
- collection_type: open
  name: Phasio Activity Internal Customer Activity Controller API
  slug: open-phasio-customer-activity-controller-api
- collection_type: open
  name: Phasio Activity Internal Customer Addresses API
  slug: open-phasio-customer-addresses-api
- collection_type: open
  name: Phasio Activity Internal Customer Analytics Controller API
  slug: open-phasio-customer-analytics-controller-api
- collection_type: open
  name: Phasio Activity Internal Customer Assembly Controller API
  slug: open-phasio-customer-assembly-controller-api
- collection_type: open
  name: Phasio Activity Internal Customer Authentication API
  slug: open-phasio-customer-authentication-api
- collection_type: open
  name: Phasio Activity Internal Customer Cart Controller API
  slug: open-phasio-customer-cart-controller-api
- collection_type: open
  name: Phasio Activity Internal Customer Cart Item Controller API
  slug: open-phasio-customer-cart-item-controller-api
- collection_type: open
  name: Phasio Activity Internal Customer Catalog Controller API
  slug: open-phasio-customer-catalog-controller-api
- collection_type: open
  name: Phasio Activity Internal Customer Controller API
  slug: open-phasio-customer-controller-api
- collection_type: open
  name: Phasio Activity Internal Customer Country Controller API
  slug: open-phasio-customer-country-controller-api
- collection_type: open
  name: Phasio Activity Internal Customer Discount Controller API
  slug: open-phasio-customer-discount-controller-api
- collection_type: open
  name: Phasio Activity Internal Customer Document Controller API
  slug: open-phasio-customer-document-controller-api
- collection_type: open
  name: Phasio Activity Internal Customer Expense Controller API
  slug: open-phasio-customer-expense-controller-api
- collection_type: open
  name: Phasio Activity Internal Customer Operator Controller API
  slug: open-phasio-customer-operator-controller-api
- collection_type: open
  name: Phasio Activity Internal Customer Order Controller API
  slug: open-phasio-customer-order-controller-api
- collection_type: open
  name: Phasio Activity Internal Customer Organisation Controller API
  slug: open-phasio-customer-organisation-controller-api
- collection_type: open
  name: Phasio Activity Internal Customer Part Design Controller API
  slug: open-phasio-customer-part-design-controller-api
- collection_type: open
  name: Phasio Activity Internal Customer Part Revision Controller API
  slug: open-phasio-customer-part-revision-controller-api
- collection_type: open
  name: Phasio Activity Internal Customer Project Controller API
  slug: open-phasio-customer-project-controller-api
- collection_type: open
  name: Phasio Activity Internal Customer Requisition Controller API
  slug: open-phasio-customer-requisition-controller-api
- collection_type: open
  name: Phasio Activity Internal Customer Shipment Controller API
  slug: open-phasio-customer-shipment-controller-api
- collection_type: open
  name: Phasio Activity Internal Customer Thread File Controller API
  slug: open-phasio-customer-thread-file-controller-api
- collection_type: open
  name: Phasio Activity Internal equation-resource API
  slug: open-phasio-equation-resource-api
- collection_type: open
  name: Phasio Activity Internal File Analysis Controller API
  slug: open-phasio-file-analysis-controller-api
- collection_type: open
  name: Phasio Activity Internal Inbound Email Controller API
  slug: open-phasio-inbound-email-controller-api
- collection_type: open
  name: Phasio Activity Internal Internal Accounting Controller API
  slug: open-phasio-internal-accounting-controller-api
- collection_type: open
  name: Phasio Activity Internal Internal Customer Controller API
  slug: open-phasio-internal-customer-controller-api
- collection_type: open
  name: Phasio Activity Internal Internal Customer Organisation Controller API
  slug: open-phasio-internal-customer-organisation-controller-api
- collection_type: open
  name: Phasio Activity Internal Internal Operator Controller API
  slug: open-phasio-internal-operator-controller-api
- collection_type: open
  name: Phasio Activity Internal Internal Order Controller API
  slug: open-phasio-internal-order-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Accounting API
  slug: open-phasio-manufacturer-accounting-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Activity Controller API
  slug: open-phasio-manufacturer-activity-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Analytics Controller API
  slug: open-phasio-manufacturer-analytics-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Assembly Controller API
  slug: open-phasio-manufacturer-assembly-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer CAMSPEC Controller API
  slug: open-phasio-manufacturer-camspec-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Cart Item Controller API
  slug: open-phasio-manufacturer-cart-item-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Catalog Controller API
  slug: open-phasio-manufacturer-catalog-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Color Controller API
  slug: open-phasio-manufacturer-color-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Countries Controller API
  slug: open-phasio-manufacturer-countries-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Currencies Controller API
  slug: open-phasio-manufacturer-currencies-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Customer Controller API
  slug: open-phasio-manufacturer-customer-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Customer Organisation Controller API
  slug: open-phasio-manufacturer-customer-organisation-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Discount Controller API
  slug: open-phasio-manufacturer-discount-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Document Controller API
  slug: open-phasio-manufacturer-document-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Document Template Controller API
  slug: open-phasio-manufacturer-document-template-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Expense Controller API
  slug: open-phasio-manufacturer-expense-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Infill Controller API
  slug: open-phasio-manufacturer-infill-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Kanban Column Controller API
  slug: open-phasio-manufacturer-kanban-column-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Lead Time Controller API
  slug: open-phasio-manufacturer-lead-time-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Material Controller API
  slug: open-phasio-manufacturer-material-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Material Prices Controller API
  slug: open-phasio-manufacturer-material-prices-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Metrics Controller API
  slug: open-phasio-manufacturer-metrics-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Operator Contact Controller API
  slug: open-phasio-manufacturer-operator-contact-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Operator Controller API
  slug: open-phasio-manufacturer-operator-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Operator Count Controller API
  slug: open-phasio-manufacturer-operator-count-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Order Controller API
  slug: open-phasio-manufacturer-order-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Part Design Controller API
  slug: open-phasio-manufacturer-part-design-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Part Revision Controller API
  slug: open-phasio-manufacturer-part-revision-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Part Specification Controller API
  slug: open-phasio-manufacturer-part-specification-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Payment Information Controller API
  slug: open-phasio-manufacturer-payment-information-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Post Processing Controller API
  slug: open-phasio-manufacturer-post-processing-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Precision Prices Controller API
  slug: open-phasio-manufacturer-precision-prices-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Process Prices Controller API
  slug: open-phasio-manufacturer-process-prices-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Production Status Controller API
  slug: open-phasio-manufacturer-production-status-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Production Step Controller API
  slug: open-phasio-manufacturer-production-step-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Programmatic Client Controller API
  slug: open-phasio-manufacturer-programmatic-client-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Project Controller API
  slug: open-phasio-manufacturer-project-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Quote Controller API
  slug: open-phasio-manufacturer-quote-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Reports API
  slug: open-phasio-manufacturer-reports-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Requisition Controller API
  slug: open-phasio-manufacturer-requisition-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Routing Template Controller API
  slug: open-phasio-manufacturer-routing-template-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Search Controller API
  slug: open-phasio-manufacturer-search-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Shipment Controller API
  slug: open-phasio-manufacturer-shipment-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Shipping Box Controller API
  slug: open-phasio-manufacturer-shipping-box-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Shipping Method Controller API
  slug: open-phasio-manufacturer-shipping-method-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Tax Component Controller API
  slug: open-phasio-manufacturer-tax-component-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Tax Jurisdiction Controller API
  slug: open-phasio-manufacturer-tax-jurisdiction-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Thread Controller API
  slug: open-phasio-manufacturer-thread-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Thread File Controller API
  slug: open-phasio-manufacturer-thread-file-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Tracking Controller API
  slug: open-phasio-manufacturer-tracking-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer User Controller API
  slug: open-phasio-manufacturer-user-controller-api
- collection_type: open
  name: Phasio Activity Internal Manufacturer Work Order Controller API
  slug: open-phasio-manufacturer-work-order-controller-api
- collection_type: open
  name: Phasio Activity Internal Metrics Controller API
  slug: open-phasio-metrics-controller-api
- collection_type: open
  name: Phasio Activity Internal payment-term-resource API
  slug: open-phasio-payment-term-resource-api
- collection_type: open
  name: Phasio Activity Internal Pre-Order API
  slug: open-phasio-pre-order-api
- collection_type: open
  name: Phasio Activity Internal User Authentication Controller API
  slug: open-phasio-user-authentication-controller-api
- collection_type: open
  name: Phasio Activity Internal webhook-resource API
  slug: open-phasio-webhook-resource-api
- collection_type: open
  name: Phasio Activity Internal Webhooks API
  slug: open-phasio-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/phasio-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/phasio-manufacturer-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://phas.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.phas.io/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.phas.io/developers
- group: docs
  title: ''
  type: APIReference
  url: https://docs.phas.io/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.phas.io/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://phas.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://phas.io/post
- group: start
  title: ''
  type: SignUp
  url: https://auth.phas.io/create
- group: start
  title: ''
  type: Login
  url: https://app.phas.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://phas.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://phas.io/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://phas.io/contact
- group: auth
  title: ''
  type: Authentication
  url: authentication/phasio-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/phasio-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/phasio-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/phasio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/phasio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/phasio-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/phasio-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/phasio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://phas.io/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/phasio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/phasio-domain-security.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/phasio-webhooks.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/phasio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/phasio-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/phasio-create-and-track-order.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/phasio-subscribe-to-webhooks.md
created: '2026-07-17'
description: Phasio is an operating platform for manufacturing service providers that unifies intelligent quoting, production operations, connected back-office/ERP integration, part intelligence, and white-labeled customer storefronts. It serves contract manufacturers across additive manufacturing, CNC machining, and injection molding, generating CAD-based quotes in seconds and managing shop-floor routing and scheduling. The Phasio Manufacturer API (v1) is an OpenAPI 3.1 REST API of 481 operations across 85 controllers covering orders, quotes, requisitions, part specifications and revisions, shipments, production steps, discounts, expenses, taxes, and webhooks, secured with OAuth 2.0 client-credentials Bearer JWTs.
image: https://phas.io/icon.svg
layout: provider
modified: '2026-07-20'
name: Phasio
nav: Providers
network: true
overview: 'Phasio publishes 92 APIs on the [APIs.io](https://apis.io/) network, including Activity Internal API, Addresses API, cart-resource API, and 89 more. Tagged areas include Company, Manufacturing, Additive Manufacturing, 3D Printing, and CNC Machining.


  The Phasio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Phasio''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, signup flow, support, and 23 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 50.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 63.4
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 50.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 92
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/phasio/refs/heads/main/screenshots/phasio-2026-08-17T081204.png
security:
- kind: authentication
  name: Phasio Authentication
  slug: phasio-authentication
  summary_line: http/oauth2 · 1 scheme
- kind: domain-security
  name: Phasio Domain Security
  slug: phasio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Phasio Trust Center
  slug: phasio-trust-center
  summary_line: SOC 2, GDPR
slug: phasio
tags:
- Company
- Manufacturing
- Additive Manufacturing
- 3D Printing
- CNC Machining
- Quoting
- Production Operations
- Manufacturing Execution
website: https://phas.io
---
