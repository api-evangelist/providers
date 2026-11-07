---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 158
  human_in_the_loop: 120
  name: Loadsmart Agentic Access
  operation_count: 290
  slug: loadsmart-agentic-access
  summary_line: 290 operations · 158 acting · 120 human-in-the-loop
api_count: 3
apis:
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Appointments API from Loadsmart — 10 operation(s) for appointments.
  name: Loadsmart Appointments API
  slug: loadsmart-appointments-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Asset Container API from Loadsmart — 5 operation(s) for asset container.
  name: Loadsmart Asset Container API
  slug: loadsmart-asset-container-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Asset Visit API from Loadsmart — 10 operation(s) for asset visit.
  name: Loadsmart Asset Visit API
  slug: loadsmart-asset-visit-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Audit Log API from Loadsmart — 1 operation(s) for audit log.
  name: Loadsmart Audit Log API
  slug: loadsmart-audit-log-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Authentication API from Loadsmart — 4 operation(s) for authentication.
  name: Loadsmart Authentication API
  slug: loadsmart-authentication-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: This API allows third parties to create, list, retrieve and accept bids.
  name: Loadsmart Bids API
  slug: loadsmart-bids-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The BOL API from Loadsmart — 3 operation(s) for bol.
  name: Loadsmart BOL API
  slug: loadsmart-bol-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: Manages new capacity. A capacity is a truck that is empty and it's location.
  name: Loadsmart Capacity API
  slug: loadsmart-capacity-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: This API allows partners to request integration for Carriers and also manage Carrier's information. The usage of this API is detailed at https://developer.loadsmart.com/carrier-integrations/how-tos/ho
  name: Loadsmart Carrier API
  slug: loadsmart-carrier-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Carrier Companies API from Loadsmart — 2 operation(s) for carrier companies.
  name: Loadsmart Carrier Companies API
  slug: loadsmart-carrier-companies-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Carrier Users API from Loadsmart — 8 operation(s) for carrier users.
  name: Loadsmart Carrier Users API
  slug: loadsmart-carrier-users-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: Data entities store the actual values submitted through Forms. Each form submission creates multiple Data records - one for each Form Field with a value. These records maintain the relationship betwee
  name: Loadsmart Custom Forms - Data API
  slug: loadsmart-custom-forms-data-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: 'Fields are global definitions that specify fundamental attributes like data type (text, number, dropdown, etc.), validation rules, and base properties. Fields are organization-wide resources that can '
  name: Loadsmart Custom Forms - Fields API
  slug: loadsmart-custom-forms-fields-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: Flows define the sequence and logic of form presentation. Each Flow must have a primary "fromForm" and may optionally include a secondary "formTo" that appears after the first form is completed. Flows
  name: Loadsmart Custom Forms - Flows API
  slug: loadsmart-custom-forms-flows-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: Form Fields are instances of global Field definitions within a specific Form. While Fields define the data type and general properties, Form Fields customize these instances with form-specific attribu
  name: Loadsmart Custom Forms - Form Fields API
  slug: loadsmart-custom-forms-form-fields-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: 'Forms are collections of form fields that represent a complete data entry interface. Each Form belongs to a Flow and captures related data points in a structured way. Forms provide the user interface '
  name: Loadsmart Custom Forms - Forms API
  slug: loadsmart-custom-forms-forms-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: Triggers are event listeners that activate on specific API or UI events. Each Trigger is associated with exactly one Flow. When a Trigger fires, it initiates its associated Flow, which in turn present
  name: Loadsmart Custom Forms - Triggers API
  slug: loadsmart-custom-forms-triggers-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Docks API from Loadsmart — 8 operation(s) for docks.
  name: Loadsmart Docks API
  slug: loadsmart-docks-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Documents API from Loadsmart — 2 operation(s) for documents.
  name: Loadsmart Documents API
  slug: loadsmart-documents-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Gates API from Loadsmart — 1 operation(s) for gates.
  name: Loadsmart Gates API
  slug: loadsmart-gates-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The General API from Loadsmart — 3 operation(s) for general.
  name: Loadsmart General API
  slug: loadsmart-general-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: 'This API allows third parties to search and accept available Offers. ## Webhook events There are few webhook events that can be triggered related to Load Offers API. The following example refers to th'
  name: Loadsmart Load Offers API
  slug: loadsmart-load-offers-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Load Type Groups API from Loadsmart — 2 operation(s) for load type groups.
  name: Loadsmart Load Type Groups API
  slug: loadsmart-load-type-groups-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Load Types API from Loadsmart — 4 operation(s) for load types.
  name: Loadsmart Load Types API
  slug: loadsmart-load-types-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: This endpoint will be the entrypoint for our integrations. It will receive loads.
  name: Loadsmart Loads API
  slug: loadsmart-loads-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Metrics API from Loadsmart — 23 operation(s) for metrics.
  name: Loadsmart Metrics API
  slug: loadsmart-metrics-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Observations API from Loadsmart — 3 operation(s) for observations.
  name: Loadsmart Observations API
  slug: loadsmart-observations-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Orgs API from Loadsmart — 5 operation(s) for orgs.
  name: Loadsmart Orgs API
  slug: loadsmart-orgs-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: Quotes provide the price and conditions for a future shipment. To create a shipment, you need first to request a valid quote.
  name: Loadsmart Quotes API
  slug: loadsmart-quotes-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: Provides information about routing
  name: Loadsmart Routes API
  slug: loadsmart-routes-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The SAML API from Loadsmart — 5 operation(s) for saml.
  name: Loadsmart SAML API
  slug: loadsmart-saml-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Settings Metadata API from Loadsmart — 3 operation(s) for settings metadata.
  name: Loadsmart Settings Metadata API
  slug: loadsmart-settings-metadata-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: 'Our API supports fetch and change of a variety of shipments status, the main ones are responsible to move the shipment from booked to in transit and delivered, They must obey the following order: * **'
  name: Loadsmart Shipment Events API
  slug: loadsmart-shipment-events-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: Stops of a shipment
  name: Loadsmart Shipment Stops API
  slug: loadsmart-shipment-stops-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: Manage shipments
  name: Loadsmart Shipments API
  slug: loadsmart-shipments-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Shipper Accounting Info API from Loadsmart — 1 operation(s) for shipper accounting info.
  name: Loadsmart Shipper Accounting Info API
  slug: loadsmart-shipper-accounting-info-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: Manage the accounts associated with shippers. An account represents an user.
  name: Loadsmart Shipper Accounts API
  slug: loadsmart-shipper-accounts-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: Manage shippers. A shipper is a company that creates and manages loads on Loadsmart platform.
  name: Loadsmart Shippers API
  slug: loadsmart-shippers-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Storage API from Loadsmart — 2 operation(s) for storage.
  name: Loadsmart Storage API
  slug: loadsmart-storage-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Unit Limiter API from Loadsmart — 5 operation(s) for unit limiter.
  name: Loadsmart Unit Limiter API
  slug: loadsmart-unit-limiter-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Users API from Loadsmart — 6 operation(s) for users.
  name: Loadsmart Users API
  slug: loadsmart-users-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Warehouse Groups API from Loadsmart — 2 operation(s) for warehouse groups.
  name: Loadsmart Warehouse Groups API
  slug: loadsmart-warehouse-groups-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The Warehouses API from Loadsmart — 4 operation(s) for warehouses.
  name: Loadsmart Warehouses API
  slug: loadsmart-warehouses-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: Webhooks allow you to receive certain events from Loadsmart. When one of those events is triggered, we'll send an HTTP POST request to the webhook's configured URL(s). This URL(s) should be sent to Lo
  name: Loadsmart Webhooks API
  slug: loadsmart-webhooks-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The YMS - Spot API from Loadsmart — 8 operation(s) for yms - spot.
  name: Loadsmart YMS - Spot API
  slug: loadsmart-yms-spot-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The YMS - Spot Area API from Loadsmart — 2 operation(s) for yms - spot area.
  name: Loadsmart YMS - Spot Area API
  slug: loadsmart-yms-spot-area-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The YMS - Spot Assignment API from Loadsmart — 4 operation(s) for yms - spot assignment.
  name: Loadsmart YMS - Spot Assignment API
  slug: loadsmart-yms-spot-assignment-api
- baseURL: https://api.loadsmart.com
  baseurl_source: declared
  description: The YMS - Yard View API from Loadsmart — 4 operation(s) for yms - yard view.
  name: Loadsmart YMS - Yard View API
  slug: loadsmart-yms-yard-view-api
artifact_total: 244
asyncapis:
- description: ''
  name: Loadsmart Webhooks
  slug: loadsmart-webhooks
collections:
- collection_type: open
  name: Opendock Nova API Documentation Appointments API
  slug: open-loadsmart-appointments-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Asset Container API
  slug: open-loadsmart-asset-container-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Asset Visit API
  slug: open-loadsmart-asset-visit-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Audit Log API
  slug: open-loadsmart-audit-log-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Authentication API
  slug: open-loadsmart-authentication-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Bids API
  slug: open-loadsmart-bids-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments BOL API
  slug: open-loadsmart-bol-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Capacity API
  slug: open-loadsmart-capacity-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Carrier API
  slug: open-loadsmart-carrier-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Carrier Companies API
  slug: open-loadsmart-carrier-companies-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Carrier Users API
  slug: open-loadsmart-carrier-users-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Custom Forms - Data API
  slug: open-loadsmart-custom-forms-data-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Custom Forms - Fields API
  slug: open-loadsmart-custom-forms-fields-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Custom Forms - Flows API
  slug: open-loadsmart-custom-forms-flows-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Custom Forms - Form Fields API
  slug: open-loadsmart-custom-forms-form-fields-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Custom Forms - Forms API
  slug: open-loadsmart-custom-forms-forms-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Custom Forms - Triggers API
  slug: open-loadsmart-custom-forms-triggers-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Docks API
  slug: open-loadsmart-docks-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Documents API
  slug: open-loadsmart-documents-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Gates API
  slug: open-loadsmart-gates-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments General API
  slug: open-loadsmart-general-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Load Offers API
  slug: open-loadsmart-load-offers-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Load Type Groups API
  slug: open-loadsmart-load-type-groups-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Load Types API
  slug: open-loadsmart-load-types-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Loads API
  slug: open-loadsmart-loads-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Metrics API
  slug: open-loadsmart-metrics-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Observations API
  slug: open-loadsmart-observations-api
- collection_type: open
  name: Opendock Nova API Documentation
  slug: open-loadsmart-opendock
- collection_type: open
  name: Opendock Nova API Documentation Appointments Orgs API
  slug: open-loadsmart-orgs-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Quotes API
  slug: open-loadsmart-quotes-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Routes API
  slug: open-loadsmart-routes-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments SAML API
  slug: open-loadsmart-saml-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Settings Metadata API
  slug: open-loadsmart-settings-metadata-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Shipment Events API
  slug: open-loadsmart-shipment-events-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Shipment Stops API
  slug: open-loadsmart-shipment-stops-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Shipments API
  slug: open-loadsmart-shipments-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Shipper Accounting Info API
  slug: open-loadsmart-shipper-accounting-info-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Shipper Accounts API
  slug: open-loadsmart-shipper-accounts-api
- collection_type: open
  name: Loadsmart API
  slug: open-loadsmart-shipperguide
- collection_type: open
  name: Opendock Nova API Documentation Appointments Shippers API
  slug: open-loadsmart-shippers-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Storage API
  slug: open-loadsmart-storage-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Unit Limiter API
  slug: open-loadsmart-unit-limiter-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Users API
  slug: open-loadsmart-users-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Warehouse Groups API
  slug: open-loadsmart-warehouse-groups-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Warehouses API
  slug: open-loadsmart-warehouses-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments Webhooks API
  slug: open-loadsmart-webhooks-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments YMS - Spot API
  slug: open-loadsmart-yms-spot-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments YMS - Spot Area API
  slug: open-loadsmart-yms-spot-area-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments YMS - Spot Assignment API
  slug: open-loadsmart-yms-spot-assignment-api
- collection_type: open
  name: Opendock Nova API Documentation Appointments YMS - Yard View API
  slug: open-loadsmart-yms-yard-view-api
common:
- group: design
  href: https://artifacts.apis.io/loadsmart/rules/loadsmart-rules.yml
  title: ''
  type: Spectral
  url: rules/loadsmart-rules.yml
- group: design
  href: https://artifacts.apis.io/loadsmart/json-ld/loadsmart-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/loadsmart-context.jsonld
- group: design
  href: https://artifacts.apis.io/loadsmart/vocabulary/loadsmart-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/loadsmart-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/loadsmart/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/loadsmart/asyncapi/loadsmart-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/loadsmart-webhooks.yml
- group: design
  href: https://artifacts.apis.io/loadsmart/data-model/loadsmart-data-model.yml
  title: ''
  type: DataModel
  url: data-model/loadsmart-data-model.yml
- group: operate
  href: https://artifacts.apis.io/loadsmart/changelog/loadsmart-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/loadsmart-changelog.yml
- group: design
  href: https://artifacts.apis.io/loadsmart/errors/loadsmart-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/loadsmart-problem-types.yml
- group: design
  href: https://artifacts.apis.io/loadsmart/conformance/loadsmart-conformance.yml
  title: ''
  type: Conformance
  url: conformance/loadsmart-conformance.yml
- group: agent
  href: https://artifacts.apis.io/loadsmart/llms/loadsmart-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/loadsmart-llms.txt
- group: agent
  href: https://artifacts.apis.io/loadsmart/mcp/loadsmart-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/loadsmart-mcp.yml
- group: agent
  href: https://artifacts.apis.io/loadsmart/well-known/loadsmart-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/loadsmart-well-known.yml
- group: other
  href: https://artifacts.apis.io/loadsmart/hosts/loadsmart-hosts.yml
  title: ''
  type: Hosts
  url: hosts/loadsmart-hosts.yml
- group: other
  href: https://artifacts.apis.io/loadsmart/vendors/loadsmart-vendors.yml
  title: ''
  type: Vendors
  url: vendors/loadsmart-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.loadsmart.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://subscriptions.statuspage.io/slack_authentication/kickoff?page_code=v03v69pvxm8n
- group: auth
  title: ''
  type: Security
  url: https://lp.loadsmart.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://loadsmart.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://loadsmart.com/login/
- group: other
  href: https://artifacts.apis.io/loadsmart/capabilities/loadsmart-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/loadsmart-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/loadsmart/agentic-access/loadsmart-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/loadsmart-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/loadsmart/security/loadsmart-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/loadsmart-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/loadsmart/authentication/loadsmart-authentication.yml
  title: ''
  type: Authentication
  url: authentication/loadsmart-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://loadsmart.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.loadsmart.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.loadsmart.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.loadsmart.com/docs/shipperguide/api-reference
- group: docs
  title: ''
  type: OpenAPI
  url: https://developer.loadsmart.com/api/openapi.yaml
- group: company
  title: ''
  type: About
  url: https://loadsmart.com/about/
- group: company
  title: ''
  type: Careers
  url: https://loadsmart.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://loadsmart.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://blog.loadsmart.com/
- group: operate
  title: ''
  type: Community
  url: https://community.loadsmart.com/
- group: docs
  title: ''
  type: ShipperGuide
  url: https://loadsmart.com/shippers/shipperguide-tms/
- group: other
  title: ''
  type: ManagedTransportation
  url: https://loadsmart.com/shippers/managed-transportation/
- group: other
  title: ''
  type: FreightIntelAI
  url: https://loadsmart.com/freightintel-ai/
- group: other
  title: ''
  type: PrivateFleetOptimizer
  url: https://loadsmart.com/shippers/private-fleet-optimizer/
- group: other
  title: ''
  type: FlatbedMessenger
  url: https://loadsmart.com/flatbed-messenger/
- group: other
  title: ''
  type: CarrierLoadboard
  url: https://loadsmart.com/carriers/loadboard/
- group: docs
  title: ''
  type: CarrierGuide
  url: https://loadsmart.com/carriers/carrierguide-tms/
- group: other
  title: ''
  type: Factoring
  url: https://loadsmart.com/carriers/factoring/
- group: other
  title: ''
  type: Opendock
  url: https://opendock.com/
- group: other
  title: ''
  type: NavTrac
  url: https://loadsmart.com/warehouse/navtrac/
- group: build
  title: ''
  type: OracleIntegration
  url: https://loadsmart.com/integrations/oracle/
- group: build
  title: ''
  type: MercuryGateIntegration
  url: https://loadsmart.com/integrations/mercury-gate/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/loadsmart
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/LoadSmartUS
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/loadsmart
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCN-pkKcoMargmyL0Br3-H5w
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/loadsmart
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/loadsmartUS
- group: commercial
  href: https://artifacts.apis.io/loadsmart/plans/loadsmart-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/loadsmart-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/loadsmart/rate-limits/loadsmart-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/loadsmart-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/loadsmart/finops/loadsmart-finops.yml
  title: ''
  type: FinOps
  url: finops/loadsmart-finops.yml
created: '2026-05-25'
description: Loadsmart is a digital freight technology company and 4PL that connects shippers, carriers, warehouses, and dock operations on a single platform. Founded in 2014 by Felipe Capella and Ricardo Salgado and headquartered in Chicago (with significant New York presence), Loadsmart raised more than $346M from investors including BlackRock, SoftBank Latin America Fund, Maersk Growth, TFI International, CSX, Ports America, and Connor Capital, reaching a reported $1.3B valuation. The platform spans full and partial truckload, less-than-truckload, drayage, expedited, flatbed (via Flatbed Messenger), and multimodal freight, plus the ShipperGuide TMS for procurement, planning, and execution; CarrierGuide TMS and a carrier loadboard with factoring; Opendock for dock appointment scheduling and the Nova warehouse API; and NavTrac for yard management and computer-vision gate/yard visibility. FreightIntel AI provides machine-learning powered freight recommendations across the suite. Loadsmart
  exposes a public Developer Portal with two production OpenAPI surfaces — the ShipperGuide API (api.loadsmart.com, JWT/RS256 authentication, with quote, book, tender, track, and webhook lanes) and the Opendock Nova / Neutron API (neutron.opendock.com, JWT bearer authentication) — and ships a Postman collection plus partner integrations with Oracle Transportation Management, MercuryGate, Blue Yonder, SAP, NetSuite, and other TMS/ERP platforms.
features:
- ShipperGuide TMS for freight procurement, planning, and execution across modes
- Managed Transportation (4PL) services for enterprise shippers
- FreightIntel AI machine-learning recommendations for rate, mode, and lane decisions
- Private Fleet Optimizer for fleet-running shippers
- Flatbed Messenger marketplace for flatbed freight
- CarrierGuide TMS, Carrier Loadboard, and Factoring services for motor carriers
- Opendock Nova for dock appointment scheduling, hours of operation, gates, and yards
- Subspace real-time WebSocket API streaming dock appointment events
- Appointment Validation API for verifying PO numbers before scheduling
- NavTrac yard management and computer-vision asset tracking
- Public ShipperGuide REST API (50 paths) for quote, book, tender, track, and webhooks
- Public Opendock Nova/Neutron REST API (151 paths) for warehouse, dock, and appointment ops
- JWT/RS256 authentication for ShipperGuide; JWT bearer for Opendock Nova
- Sandbox environments for both API surfaces
- Webhook surface for quote, shipment, load, bid, and carrier lifecycle events
- Integrations with Oracle Transportation Management, MercuryGate, and other TMS/ERPs
- Postman collections for both ShipperGuide and Opendock Nova
finops:
- has_sources: true
  method: generated
  name: Loadsmart Finops
  primary_unit: shipment
  service_category: Logistics and Supply Chain
  slug: loadsmart-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loadsmart.png
json_schemas:
- name: AddCarrierFavoriteWarehouseDto
  property_count: 0
  slug: loadsmart-add-carrier-favorite-warehouse-dto
- name: AppEnvironmentDto
  property_count: 3
  slug: loadsmart-app-environment-dto
- name: AppointmentCountResponseDto
  property_count: 0
  slug: loadsmart-appointment-count-response-dto
- name: AppointmentListItemDto
  property_count: 33
  slug: loadsmart-appointment-list-item-dto
- name: AppointmentMetricsListDto
  property_count: 10
  slug: loadsmart-appointment-metrics-list-dto
- name: AppointmentMetricsListV2Dto
  property_count: 9
  slug: loadsmart-appointment-metrics-list-v2-dto
- name: AssetContainerEvent
  property_count: 7
  slug: loadsmart-asset-container-event
- name: AssetContainer
  property_count: 15
  slug: loadsmart-asset-container
- name: AssetVisitExcelExportDto
  property_count: 7
  slug: loadsmart-asset-visit-excel-export-dto
- name: AssetVisitMetricsListDto
  property_count: 9
  slug: loadsmart-asset-visit-metrics-list-dto
- name: AssetVisit
  property_count: 17
  slug: loadsmart-asset-visit
- name: AuditLog
  property_count: 0
  slug: loadsmart-audit-log
- name: AuthProfileResponseDto
  property_count: 26
  slug: loadsmart-auth-profile-response-dto
- name: AvailabilityDto
  property_count: 2
  slug: loadsmart-availability-dto
- name: AvailabilityFromLoadTypeDto
  property_count: 2
  slug: loadsmart-availability-from-load-type-dto
- name: ChangePasswordDto
  property_count: 0
  slug: loadsmart-change-password-dto
- name: Company
  property_count: 4
  slug: loadsmart-company
- name: CreateAppointmentDto
  property_count: 15
  slug: loadsmart-create-appointment-dto
- name: CreateAssetContainerDto
  property_count: 10
  slug: loadsmart-create-asset-container-dto
- name: CreateAssetContainerEventDto
  property_count: 4
  slug: loadsmart-create-asset-container-event-dto
- name: CreateAssetVisitDto
  property_count: 15
  slug: loadsmart-create-asset-visit-dto
- name: CreateBolRequestDto
  property_count: 2
  slug: loadsmart-create-bol-request-dto
- name: CreateBolResponseDto
  property_count: 1
  slug: loadsmart-create-bol-response-dto
- name: CreateCarrierDto
  property_count: 3
  slug: loadsmart-create-carrier-dto
- name: CreateCompanyDto
  property_count: 5
  slug: loadsmart-create-company-dto
- name: CreateDockDto
  property_count: 12
  slug: loadsmart-create-dock-dto
- name: CreateFieldDto
  property_count: 6
  slug: loadsmart-create-field-dto
- name: CreateFlowDto
  property_count: 5
  slug: loadsmart-create-flow-dto
- name: CreateFormDto
  property_count: 4
  slug: loadsmart-create-form-dto
- name: CreateFormFieldDto
  property_count: 6
  slug: loadsmart-create-form-field-dto
- name: CreateLoadTypeDto
  property_count: 11
  slug: loadsmart-create-load-type-dto
- name: CreateLoadTypeGroupDto
  property_count: 1
  slug: loadsmart-create-load-type-group-dto
- name: CreateLoadTypesCustomFormsDto
  property_count: 3
  slug: loadsmart-create-load-types-custom-forms-dto
- name: CreateManyCustomFormDataDto
  property_count: 1
  slug: loadsmart-create-many-custom-form-data-dto
- name: CreateRecurringAppointmentsDto
  property_count: 5
  slug: loadsmart-create-recurring-appointments-dto
- name: CreateReportSearchDto
  property_count: 0
  slug: loadsmart-create-report-search-dto
- name: CreateReserveDto
  property_count: 4
  slug: loadsmart-create-reserve-dto
- name: CreateSingleCustomFormDataDto
  property_count: 6
  slug: loadsmart-create-single-custom-form-data-dto
- name: CreateSpotAreaDto
  property_count: 4
  slug: loadsmart-create-spot-area-dto
- name: CreateSpotDto
  property_count: 5
  slug: loadsmart-create-spot-dto
- name: CreateSpotManyDto
  property_count: 6
  slug: loadsmart-create-spot-many-dto
- name: CreateTriggerDto
  property_count: 7
  slug: loadsmart-create-trigger-dto
- name: CreateWarehouseDto
  property_count: 22
  slug: loadsmart-create-warehouse-dto
- name: CreateWarehouseGroupDto
  property_count: 3
  slug: loadsmart-create-warehouse-group-dto
- name: CustomFormData
  property_count: 12
  slug: loadsmart-custom-form-data
- name: DeleteLoadTypeGroupDto
  property_count: 1
  slug: loadsmart-delete-load-type-group-dto
- name: Dock
  property_count: 19
  slug: loadsmart-dock
- name: DockSortResponseDto
  property_count: 3
  slug: loadsmart-dock-sort-response-dto
- name: DocumentListDto
  property_count: 2
  slug: loadsmart-document-list-dto
- name: Field
  property_count: 10
  slug: loadsmart-field
- name: Flow
  property_count: 12
  slug: loadsmart-flow
- name: FormField
  property_count: 9
  slug: loadsmart-form-field
- name: Form
  property_count: 6
  slug: loadsmart-form
- name: GatesByWarehouseDto
  property_count: 1
  slug: loadsmart-gates-by-warehouse-dto
- name: GetBolResponseDto
  property_count: 4
  slug: loadsmart-get-bol-response-dto
- name: GetManyFieldResponseDto
  property_count: 5
  slug: loadsmart-get-many-field-response-dto
- name: GetManyFlowResponseDto
  property_count: 5
  slug: loadsmart-get-many-flow-response-dto
- name: GetManyFormFieldResponseDto
  property_count: 5
  slug: loadsmart-get-many-form-field-response-dto
- name: GetManyFormResponseDto
  property_count: 5
  slug: loadsmart-get-many-form-response-dto
- name: GetManySpotAreaResponseDto
  property_count: 5
  slug: loadsmart-get-many-spot-area-response-dto
- name: GetManySpotAssignmentResponseDto
  property_count: 5
  slug: loadsmart-get-many-spot-assignment-response-dto
- name: GetPreviewAsCarrierResponseDto
  property_count: 0
  slug: loadsmart-get-preview-as-carrier-response-dto
- name: InviteDto
  property_count: 0
  slug: loadsmart-invite-dto
- name: LinkUnplannedCheckinToAppointmentDto
  property_count: 4
  slug: loadsmart-link-unplanned-checkin-to-appointment-dto
- name: ListSpotDto
  property_count: 3
  slug: loadsmart-list-spot-dto
- name: LoadType
  property_count: 14
  slug: loadsmart-load-type
- name: LoginDto
  property_count: 2
  slug: loadsmart-login-dto
- name: LoginResponseDto
  property_count: 2
  slug: loadsmart-login-response-dto
- name: MetricsAppointmentVolumeByLoadTypeResponse
  property_count: 1
  slug: loadsmart-metrics-appointment-volume-by-load-type-response
- name: MetricsCarrierStatusPercentageResponse
  property_count: 1
  slug: loadsmart-metrics-carrier-status-percentage-response
- name: ObservationCreateAssetVisitDto
  property_count: 1
  slug: loadsmart-observation-create-asset-visit-dto
- name: ObservationCreateAssetVisitResponse
  property_count: 0
  slug: loadsmart-observation-create-asset-visit-response
- name: OrgCarrierSettingsDto
  property_count: 0
  slug: loadsmart-org-carrier-settings-dto
- name: Org
  property_count: 10
  slug: loadsmart-org
- name: PaginatedDto
  property_count: 7
  slug: loadsmart-paginated-dto
- name: ReassignSpotDto
  property_count: 5
  slug: loadsmart-reassign-spot-dto
- name: ReportSearchResponseDto
  property_count: 0
  slug: loadsmart-report-search-response-dto
- name: ResponseLoadTypeGroupDto
  property_count: 0
  slug: loadsmart-response-load-type-group-dto
- name: SortFormFieldDto
  property_count: 1
  slug: loadsmart-sort-form-field-dto
- name: SpotArea
  property_count: 5
  slug: loadsmart-spot-area
- name: SpotAssignment
  property_count: 8
  slug: loadsmart-spot-assignment
- name: SpotEvent
  property_count: 10
  slug: loadsmart-spot-event
- name: Spot
  property_count: 8
  slug: loadsmart-spot
- name: StorageDto
  property_count: 2
  slug: loadsmart-storage-dto
- name: ToggleSpotReserveDto
  property_count: 5
  slug: loadsmart-toggle-spot-reserve-dto
- name: Trigger
  property_count: 11
  slug: loadsmart-trigger
- name: UnitLimitConfigurationWriteDTO
  property_count: 1
  slug: loadsmart-unit-limit-configuration-write-dto
- name: UnitLimitCount
  property_count: 4
  slug: loadsmart-unit-limit-count
- name: UnitLimit
  property_count: 4
  slug: loadsmart-unit-limit
- name: UnitLimitValidateDTO
  property_count: 7
  slug: loadsmart-unit-limit-validate-dto
- name: UpdateAppointmentDto
  property_count: 18
  slug: loadsmart-update-appointment-dto
- name: UpdateAssetContainerDto
  property_count: 9
  slug: loadsmart-update-asset-container-dto
- name: UpdateAssetVisitDto
  property_count: 7
  slug: loadsmart-update-asset-visit-dto
- name: UpdateCustomFormDataDto
  property_count: 2
  slug: loadsmart-update-custom-form-data-dto
- name: UpdateCustomTagsDto
  property_count: 0
  slug: loadsmart-update-custom-tags-dto
- name: UpdateDockDto
  property_count: 15
  slug: loadsmart-update-dock-dto
- name: UpdateFieldDto
  property_count: 7
  slug: loadsmart-update-field-dto
- name: UpdateFlowDto
  property_count: 4
  slug: loadsmart-update-flow-dto
- name: UpdateFormDto
  property_count: 3
  slug: loadsmart-update-form-dto
- name: UpdateFormFieldDto
  property_count: 5
  slug: loadsmart-update-form-field-dto
- name: UpdateLoadTypeDto
  property_count: 13
  slug: loadsmart-update-load-type-dto
- name: UpdateLoadTypeGroupDto
  property_count: 1
  slug: loadsmart-update-load-type-group-dto
- name: UpdateLoadTypesCustomFormsDto
  property_count: 3
  slug: loadsmart-update-load-types-custom-forms-dto
- name: UpdateOrgDto
  property_count: 4
  slug: loadsmart-update-org-dto
- name: UpdateReportSearchDto
  property_count: 0
  slug: loadsmart-update-report-search-dto
- name: UpdateSamlConfigDto
  property_count: 0
  slug: loadsmart-update-saml-config-dto
- name: UpdateSpotAreaDto
  property_count: 2
  slug: loadsmart-update-spot-area-dto
- name: UpdateTriggerDto
  property_count: 7
  slug: loadsmart-update-trigger-dto
- name: UpdateUserDto
  property_count: 9
  slug: loadsmart-update-user-dto
- name: UpdateWarehouseDto
  property_count: 26
  slug: loadsmart-update-warehouse-dto
- name: UpdateWarehouseGroupDto
  property_count: 3
  slug: loadsmart-update-warehouse-group-dto
- name: User
  property_count: 11
  slug: loadsmart-user
- name: VehicleObservation
  property_count: 4
  slug: loadsmart-vehicle-observation
- name: VersionDto
  property_count: 4
  slug: loadsmart-version-dto
- name: WarehouseGroup
  property_count: 4
  slug: loadsmart-warehouse-group
- name: Warehouse
  property_count: 28
  slug: loadsmart-warehouse
jsonld:
- class_count: 120
  name: Loadsmart Context
  property_count: 241
  slug: loadsmart-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.loadsmart.com over HTTP.
  name: Loadsmart MCP Server
  slug: loadsmart
modified: '2026-05-25'
name: Loadsmart
nav: Providers
network: true
overview: 'Loadsmart publishes 48 API contracts indexed on the [APIs.io](https://apis.io/) network, including Appointments API, Asset Container API, Asset Visit API, and 45 more. Tagged areas include Freight, Logistics, Transportation, Supply Chain, and Digital Freight.


  The Loadsmart catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Loadsmart''s developer surface includes changelog, authentication, documentation, API reference, engineering blog, YouTube channel, and 48 more developer resources.'
plans:
- name: Loadsmart Plans Pricing
  plan_count: 6
  slug: loadsmart-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Loadsmart Rate Limits
  slug: loadsmart-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Loadsmart API Rules
  rule_count: 12
  severity_counts:
    error: 6
    hint: 0
    info: 4
    warn: 2
  slug: loadsmart-rules
score:
  band: developing
  composite: 53.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 73.8
    catalog_earned_first_party: 0.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 69.6
    developer_ergonomics: 54.2
    discoverability: 80.0
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 58.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 29.2
      total: 48
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 21.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/loadsmart/loadsmart-2026-06-20T184627.png
security:
- kind: authentication
  name: Loadsmart Authentication
  slug: loadsmart-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Loadsmart Domain Security
  slug: loadsmart-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: loadsmart-assign-driver
  slug: loadsmart-assign-driver
- name: loadsmart-create-and-retrieve-bol
  slug: loadsmart-create-and-retrieve-bol
- name: loadsmart-shipper-account-management
  slug: loadsmart-shipper-account-management
slug: loadsmart
tags:
- Freight
- Logistics
- Transportation
- Supply Chain
- Digital Freight
- Freight Brokerage
- Truckload
- LTL
- Drayage
- Flatbed
- Multi-Modal
- TMS
- Dock Scheduling
- Yard Management
- Warehouse
- 4PL
- FreightTech
website: https://loadsmart.com
---
