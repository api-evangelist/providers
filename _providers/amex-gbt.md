---
access_model:
  confidence: high
  label: Public OpenAPI contracts - client credentials issued only after onboarding
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - openapi
  - developer-portal
  - terms
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 97
  human_in_the_loop: 36
  name: Amex Gbt Agentic Access
  operation_count: 171
  slug: amex-gbt-agentic-access
  summary_line: 171 operations · 97 acting · 36 human-in-the-loop
api_count: 17
apis:
- description: SCIM-based user provisioning for an Egencia corporate travel programme. Egencia's own overview states the API "supports SCIM, or System for Cross-domain Identity Management, an open standard that allo
  name: Egencia User Sync API
  slug: egencia-user-sync-api
- description: 'Single sign-on entry point that carries contextual data into the Egencia booking flow at authentication time. Documented endpoints are GET /v1/newTrip and GET /v2/startTrip, which accept trip context '
  name: Egencia Context SSO API
  slug: egencia-context-sso-api
- description: Retrieves company information for an Egencia corporate account - name, display name and related detail - plus e-commerce settings and an audit view of those settings. Documented operations are GET /v1
  name: Egencia Company Details API
  slug: egencia-company-details-api
- description: 'Manages custom data fields - the client-defined fields Egencia describes as capturing "invoicing, reporting, approval, billing" detail, commonly department, billing unit, reason for travel or project '
  name: Egencia Company CDF API
  slug: egencia-company-cdf-api
- description: 'A service provider interface, not a consumable API - Egencia calls the customer. At checkout, when a traveller presses book, Egencia posts the booking payload to a web service the customer must build '
  name: Egencia Validation SPI
  slug: egencia-validation-spi
- description: Near real-time push of booking and expense data out of Egencia into a customer's expense or ERP system. Egencia describes it as an "Expense capability" that pushes a message to a connected partner web
  name: Egencia Expense SPI
  slug: egencia-expense-spi
- description: Retrieval of a booking and its individual trip items, plus the receipts attached to an item. Documented operations are GET /v1/bookings/{bookingId}, GET /v1/bookings/{bookingId}/items/{itemId}, GET an
  name: Egencia Get Booking API
  slug: egencia-get-booking-api
- description: Trip-level cancellation and deletion of bookings. Documented operations are POST /v1/bookings/{bookingId}/cancel and POST /v1/bookings/{bookingId}/delete, which act on every trip item in the booking a
  name: Egencia Expense Cancellation and Deletion API
  slug: egencia-cancellation-deletion-api
- description: Programmatic approval or denial of booking requests, at trip level and at trip-item level. Documented operations are POST /v1/bookings/{bookingId}/approve, /deny and the matching /items/{itemId}/appro
  name: Egencia Approval Workflow API
  slug: egencia-approval-workflow-api
- description: An outbound service provider interface that lets a customer decide, at checkout time, whether level one and level two approval are required for a booking and who the approvers are. Egencia calls the c
  name: Egencia Approval Customisation SPI
  slug: egencia-approval-customisation-spi
- description: Retrieval of the receipt for a booked trip item, via GET /v1/receipts/{itemId}, paired with a Receipt SPI that pushes a notification to a customer-built web service whenever a receipt is generated. Th
  name: Egencia Receipt API
  slug: egencia-receipt-api
- description: Traveller-tracking data for risk and duty-of-care programmes. Egencia documents POST https://apis.egencia.com/dutyofcare/api/v1/bookings to create a paginated query of booking data for a partner ID ov
  name: Egencia Duty of Care API
  slug: egencia-duty-of-care-api
- description: Consolidated booking transaction data out of Egencia, and the closest thing in the estate to a documented exit path. POST /v1/transactions creates a filtered report over a date range and returns pagin
  name: Egencia Reporting API (BI Transactions)
  slug: egencia-reporting-api
- description: American Express Global Business Travel BI API from American Express Global Business Travel — 14 path(s) described in OpenAPI.
  name: American Express Global Business Travel BI API
  slug: amex-gbt-service-bi-openapi
- description: American Express Global Business Travel OpenAPI definition from American Express Global Business Travel — 10 path(s) described in OpenAPI.
  name: American Express Global Business Travel OpenAPI definition (Amex Gbt Service Company)
  slug: amex-gbt-service-company-openapi
- description: American Express Global Business Travel Duty Of Care API from American Express Global Business Travel — 7 path(s) described in OpenAPI.
  name: American Express Global Business Travel Duty Of Care API
  slug: amex-gbt-service-dutyofcare-openapi
- description: American Express Global Business Travel OpenAPI definition from American Express Global Business Travel — 36 path(s) described in OpenAPI.
  name: American Express Global Business Travel OpenAPI definition (Amex Gbt Service Openconnect)
  slug: amex-gbt-service-openconnect-openapi
artifact_total: 24
asyncapis:
- description: ''
  name: Amex Gbt Webhooks
  slug: amex-gbt-webhooks
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amex-gbt-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amex-gbt-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amex-gbt-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/amex-gbt-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amex-gbt-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/amex-gbt-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amex-gbt-error-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amex-gbt-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amex-gbt-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: changelog/amex-gbt-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/amex-gbt-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://apis.egencia.com/bi/v1/api-info
- group: design
  title: ''
  type: Conformance
  url: conformance/amex-gbt-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/amex-gbt-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/amex-gbt-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/amex-gbt-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/amex-gbt-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amex-gbt-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amex-gbt-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amex-gbt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://amexgbt.responsibledisclosure.com/hc/en-us
- group: other
  title: ''
  type: Overlay
  url: overlays/amex-gbt-reporting-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/amex-gbt-user-sync-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/amex-gbt-service-openconnect-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.amexglobalbusinesstravel.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.amexglobalbusinesstravel.com/egencia-developer-center/
- group: docs
  title: ''
  type: Documentation
  url: https://www.amexglobalbusinesstravel.com/egencia-developer-center/api-overview
- group: docs
  title: ''
  type: APIReference
  url: https://apis.egencia.com/openconnect/docs/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://apis.egencia.com/bi/v1/api-info
- group: operate
  title: ''
  type: Support
  url: https://www.egencia.com/en/contact-questions
- group: company
  title: ''
  type: Blog
  url: https://www.amexglobalbusinesstravel.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amexglobalbusinesstravel.com/terms-of-service/
- group: commercial
  title: ''
  type: TermsOfUse
  url: https://www.amexglobalbusinesstravel.com/egencia/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amexglobalbusinesstravel.com/egencia/privacy/
- group: auth
  title: ''
  type: Authentication
  url: https://apis.egencia.com/auth/v1/token
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/amex-gbt-service-openconnect-openapi.json
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/amex-gbt-service-bi-openapi.json
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/amex-gbt-service-dutyofcare-openapi.json
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/amex-gbt-service-company-openapi.json
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/egenciaapi/egencia-api/collection/n9n3gk7/egencia-api
- group: other
  title: ''
  type: Company
  url: https://www.amexglobalbusinesstravel.com/about/
- group: other
  title: ''
  type: Egencia
  url: https://www.amexglobalbusinesstravel.com/egencia/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/american-express-global-business-travel/
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.amexglobalbusinesstravel.com/
created: '2026-07-28'
description: American Express Global Business Travel (Amex GBT, NYSE GBTG, headquartered in New York) is the largest business-to-business travel platform in the world, operating in more than 140 countries under the Amex GBT, Egencia and Ovation brands, with CWT acquired in September 2025. Its home market is the United States. In the travel distribution chain Amex GBT is an intermediary rather than a supplier - a travel management company that aggregates air, hotel, rail, car and ground content sourced through the GDS layer, through NDC and through direct supplier connections, then resells it to corporate travel programmes with policy, approval, duty-of-care and reporting wrapped around it. It holds no inventory of its own, but it does hold the booking record, and that is where the switching cost lives. Its API posture is genuinely open at the documentation layer and firmly closed at the runtime layer. The Egencia Developer Center publishes thirteen named APIs and SPIs, and every one of them
  serves a real, anonymously retrievable OpenAPI 3.1.0 document from apis.egencia.com - no login, no key, no click-through. The identity surface is standards-based (SCIM 2.0 user provisioning over OAuth 2.0 client credentials); the booking, approval, expense, receipt, duty-of-care and reporting surfaces are proprietary Egencia shapes with no OpenTravel, HTNG or IATA NDC schema anywhere in them. Runtime access is customer-account gated - Egencia's own documentation states that "the values for client id and client secret will be provided to the Client after on-boarding to Egencia API platform", and every production endpoint returns 401 to an anonymous caller. So - public contracts, gated runtime, a real documented bulk data export in the BI Transactions API, and API terms Egencia reserves the right to change in its sole discretion.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: amex-gbt-mcp.yml
  slug: amex-gbt-mcpyml
modified: '2026-07-28'
name: American Express Global Business Travel
nav: Providers
network: true
overview: 'American Express Global Business Travel publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Egencia User Sync API, Egencia Context SSO API, Egencia Company Details API, and 14 more. Tagged areas include Travel, United States, Corporate Travel, Travel Management, and Business Travel.


  The American Express Global Business Travel catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  American Express Global Business Travel''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, support, and 38 more developer resources.'
random_paper: 69
scopes:
- name: Amex Gbt Scopes
  scope_count: 0
  slug: amex-gbt-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 61.5
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 42.1
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Amex Gbt Authentication
  slug: amex-gbt-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Amex Gbt Domain Security
  slug: amex-gbt-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Amex Gbt Vulnerability Disclosure
  slug: amex-gbt-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: amex-gbt
tags:
- Travel
- United States
- Corporate Travel
- Travel Management
- Business Travel
- Distribution
- Booking
- Aviation
- Hotels
- Rail
- Car Rental
- Expense
- Duty of Care
- Reporting
website: https://www.amexglobalbusinesstravel.com/
---
