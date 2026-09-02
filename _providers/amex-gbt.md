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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 97
  human_in_the_loop: 36
  name: Amex Gbt Agentic Access
  operation_count: 171
  slug: amex-gbt-agentic-access
  summary_line: 171 operations · 97 acting · 36 human-in-the-loop
api_count: 17
apis:
- description: The Agent Assist Notes API from American Express Global Business Travel — 1 operation(s) for agent assist notes.
  name: American Express Global Business Travel Agent Assist Notes API
  slug: amex-gbt-agent-assist-notes-api
- description: Approval interface that will get approval custom detail from external client based on the booking data passed in request
  name: American Express Global Business Travel Approval API
  slug: amex-gbt-approval-api
- description: The availability-probes-controller API from American Express Global Business Travel — 2 operation(s) for availability-probes-controller.
  name: American Express Global Business Travel Availability Probes Controller API
  slug: amex-gbt-availability-probes-controller-api
- description: The bookings v1 API from American Express Global Business Travel — 12 operation(s) for bookings v1.
  name: American Express Global Business Travel bookings v1 API
  slug: amex-gbt-bookings-v1-api
- description: The bookings v2 API from American Express Global Business Travel — 2 operation(s) for bookings v2.
  name: American Express Global Business Travel bookings v2 API
  slug: amex-gbt-bookings-v2-api
- description: The Company Details API from American Express Global Business Travel — 2 operation(s) for company details.
  name: American Express Global Business Travel Company Details API
  slug: amex-gbt-company-details-api
- description: The custom-data-field-cleanup-controller API from American Express Global Business Travel — 1 operation(s) for custom-data-field-cleanup-controller.
  name: American Express Global Business Travel Custom Data Field Cleanup Controller API
  slug: amex-gbt-custom-data-field-cleanup-controller-api
- description: CDF APIs to retrieve Definitions and Manage Values.
  name: American Express Global Business Travel Custom Data Fields (CDF) API
  slug: amex-gbt-custom-data-fields-cdf-api
- description: The doc-audit-clean-up-controller API from American Express Global Business Travel — 1 operation(s) for doc-audit-clean-up-controller.
  name: American Express Global Business Travel Doc Audit Clean Up Controller API
  slug: amex-gbt-doc-audit-clean-up-controller-api
- description: The DutyOfCare Data API from American Express Global Business Travel — 2 operation(s) for dutyofcare data.
  name: American Express Global Business Travel DutyOfCare Data API
  slug: amex-gbt-dutyofcare-data-api
- description: The ecommerce-settings-controller API from American Express Global Business Travel — 2 operation(s) for ecommerce-settings-controller.
  name: American Express Global Business Travel Ecommerce Settings Controller API
  slug: amex-gbt-ecommerce-settings-controller-api
- description: Push Expense and Subscription Operation. This is only an example. The path and the host are specific for each implementor. However, the model is fixed and versioned.
  name: American Express Global Business Travel Expense SPI API
  slug: amex-gbt-expense-spi-api
- description: The gdpr-controller API from American Express Global Business Travel — 1 operation(s) for gdpr-controller.
  name: American Express Global Business Travel Gdpr Controller API
  slug: amex-gbt-gdpr-controller-api
- description: The pos-iata-controller API from American Express Global Business Travel — 1 operation(s) for pos-iata-controller.
  name: American Express Global Business Travel Pos Iata Controller API
  slug: amex-gbt-pos-iata-controller-api
- description: The receipts API from American Express Global Business Travel — 1 operation(s) for receipts.
  name: American Express Global Business Travel Receipts API
  slug: amex-gbt-receipts-api
- description: The redirection-controller API from American Express Global Business Travel — 2 operation(s) for redirection-controller.
  name: American Express Global Business Travel Redirection Controller API
  slug: amex-gbt-redirection-controller-api
- description: The resolve-controller API from American Express Global Business Travel — 1 operation(s) for resolve-controller.
  name: American Express Global Business Travel Resolve Controller API
  slug: amex-gbt-resolve-controller-api
- description: The schemas-controller API from American Express Global Business Travel — 2 operation(s) for schemas-controller.
  name: American Express Global Business Travel Schemas Controller API
  slug: amex-gbt-schemas-controller-api
- description: SCIM 2.0 compliant user sync APIs
  name: American Express Global Business Travel SCIM User Sync V1 API
  slug: amex-gbt-scim-user-sync-v1-api
- description: SCIM 2.0 compliant user sync APIs version 2.
  name: American Express Global Business Travel SCIM User Sync V2 API
  slug: amex-gbt-scim-user-sync-v2-api
- description: SCIM 2.0 compliant user sync APIs version 3.
  name: American Express Global Business Travel SCIM User Sync V3 API
  slug: amex-gbt-scim-user-sync-v3-api
- description: SCIM 2.0 compliant admin-users sync APIs
  name: American Express Global Business Travel SCIM V1 Admin Users API
  slug: amex-gbt-scim-v1-admin-users-api
- description: The Third Party Acknowledgement API from American Express Global Business Travel — 1 operation(s) for third party acknowledgement.
  name: American Express Global Business Travel Third Party Acknowledgement API
  slug: amex-gbt-third-party-acknowledgement-api
- description: Transaction data operations
  name: American Express Global Business Travel Transaction Service Controller API
  slug: amex-gbt-transaction-service-controller-api
- description: Validation interface that will request authorization of booking based on the data provided at checkout time.This is only an example. The path and the host are specific for each implementor. However, t
  name: American Express Global Business Travel Validation API
  slug: amex-gbt-validation-api
- description: The version-controller API from American Express Global Business Travel — 1 operation(s) for version-controller.
  name: American Express Global Business Travel Version Controller API
  slug: amex-gbt-version-controller-api
artifact_total: 50
asyncapis:
- description: ''
  name: Amex Gbt Webhooks
  slug: amex-gbt-webhooks
collections:
- collection_type: open
  name: Openconnect Approval Service
  slug: open-amex-gbt-approval-customisation-spi
- collection_type: open
  name: Egencia Approval Workflow API
  slug: open-amex-gbt-approval-workflow-api
- collection_type: open
  name: Egencia Get Booking API
  slug: open-amex-gbt-booking-api
- collection_type: open
  name: Egencia Cancellation/Deletion API
  slug: open-amex-gbt-cancellation-deletion-api
- collection_type: open
  name: Egencia Company CDF API
  slug: open-amex-gbt-company-cdf-api
- collection_type: open
  name: Company Details API
  slug: open-amex-gbt-company-info-api
- collection_type: open
  name: Duty Of Care API
  slug: open-amex-gbt-duty-of-care-api
- collection_type: open
  name: Expense SPI
  slug: open-amex-gbt-expense-spi
- collection_type: open
  name: Egencia Receipt API
  slug: open-amex-gbt-receipt-api
- collection_type: open
  name: BI API
  slug: open-amex-gbt-reporting-api
- collection_type: open
  name: BI API
  slug: open-amex-gbt-service-bi
- collection_type: open
  name: OpenAPI definition
  slug: open-amex-gbt-service-company
- collection_type: open
  name: Duty Of Care API
  slug: open-amex-gbt-service-dutyofcare
- collection_type: open
  name: OpenAPI definition
  slug: open-amex-gbt-service-openconnect
- collection_type: open
  name: SSO Context API
  slug: open-amex-gbt-sso-context-api
- collection_type: open
  name: Egencia User Sync API
  slug: open-amex-gbt-user-sync-api
- collection_type: open
  name: Validation SPI
  slug: open-amex-gbt-validation-spi
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/amex-gbt-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/amex-gbt-sso-context-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/amex-gbt-company-info-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/amex-gbt-company-cdf-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/amex-gbt-validation-spi-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/amex-gbt-expense-spi-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/amex-gbt-booking-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/amex-gbt-cancellation-deletion-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/amex-gbt-approval-workflow-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/amex-gbt-approval-customisation-spi-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/amex-gbt-receipt-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/amex-gbt-duty-of-care-api-overlay.yaml
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
  name: American Express Global Business Travel MCP Server
  slug: american-express-global-business-travel-mcp-server
modified: '2026-07-28'
name: American Express Global Business Travel
nav: Providers
network: true
overview: 'American Express Global Business Travel publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Agent Assist Notes API, Approval API, Availability Probes Controller API, and 23 more. Tagged areas include Travel, United States, Corporate Travel, Travel Management, and Business Travel.


  The American Express Global Business Travel catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  American Express Global Business Travel''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, support, and 50 more developer resources.'
random_paper: 12
scopes:
- name: Amex Gbt Scopes
  scope_count: 0
  slug: amex-gbt-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.5
  coverage:
    artifact_dirs: 23
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 59.6
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 26
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
