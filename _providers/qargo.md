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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 64
  human_in_the_loop: 7
  name: Qargo Agentic Access
  operation_count: 114
  slug: qargo-agentic-access
  summary_line: 114 operations · 64 acting · 7 human-in-the-loop
api_count: 26
apis:
- description: Fleet dispatch and subcontractor-specific endpoints for transportation management.
  name: Qargo Subcontractor API
  slug: qargo-subcontractor-api
- description: Customer portal endpoints for order tracking, status monitoring and customer-facing operations.
  name: Qargo Customer API
  slug: qargo-customer-api
- description: The API / Accounting API from Qargo — 33 operation(s) for api / accounting.
  name: Qargo API / Accounting API
  slug: qargo-api-accounting-api
- description: The API / Authentication API from Qargo — 1 operation(s) for api / authentication.
  name: Qargo API / Authentication API
  slug: qargo-api-authentication-api
- description: The API / Company API from Qargo — 6 operation(s) for api / company.
  name: Qargo API / Company API
  slug: qargo-api-company-api
- description: The API / Document API from Qargo — 2 operation(s) for api / document.
  name: Qargo API / Document API
  slug: qargo-api-document-api
- description: The API / Order API from Qargo — 8 operation(s) for api / order.
  name: Qargo API / Order API
  slug: qargo-api-order-api
- description: The API / Resource API from Qargo — 8 operation(s) for api / resource.
  name: Qargo API / Resource API
  slug: qargo-api-resource-api
- description: The API / Task API from Qargo — 3 operation(s) for api / task.
  name: Qargo API / Task API
  slug: qargo-api-task-api
- description: The API / Trip API from Qargo — 3 operation(s) for api / trip.
  name: Qargo API / Trip API
  slug: qargo-api-trip-api
- description: The System API from Qargo — 1 operation(s) for system.
  name: Qargo System API
  slug: qargo-system-api
- description: 'Required role: `API_ACCOUNTING`. See [Accounting](/docs/section/accounting) for more information.'
  name: Qargo Use case / Accounting API
  slug: qargo-use-case-accounting-api
- description: 'Required api role: `CUSTOMER` This is the api equivalent of our customer portal functionality. Customers can use this api to create/update/cancel orders, view charges and receive status updates. ### G'
  name: Qargo Use case / Customer portal API
  slug: qargo-use-case-customer-portal-api
- description: 'This section provides an overview of all available methods to import documents into Qargo. ![Document import paths overview](/docs/static/document_import_overview.svg) ### Document import methods Ther'
  name: Qargo Use case / Document import API
  slug: qargo-use-case-document-import-api
- description: 'Required api role: not applicable Purpose: This interface allows an external party to send e-invoices in a structured format. A [webhook](/docs/use-case-e-invoicing/e-invoicing-webhook) can be used to'
  name: Qargo Use case / E-invoicing API
  slug: qargo-use-case-e-invoicing-api
- description: 'Required api role: not applicable (push/push) Purpose: This interface allows an external party to integrate with driver apps and on board computer systems. The fleet dispatch uses a push/push model: Q'
  name: Qargo Use case / Fleet dispatch API
  slug: qargo-use-case-fleet-dispatch-api
- description: 'Note: this is currently only a specification meant as a preview. Implementation is still pending.'
  name: Qargo Use case / Intermodal [partner] API
  slug: qargo-use-case-intermodal-partner-api
- description: 'Required api role: not applicable (push/push) Purpose: This interface allows an external party to integrate with warehouse management systems and location booking platforms. The location booking uses '
  name: Qargo Use case / Location booking API
  slug: qargo-use-case-location-booking-api
- description: 'Required api role: `API_MASTER_DATA`, or `API_ACCOUNTING` for company sync only.'
  name: Qargo Use case / Master data sync API
  slug: qargo-use-case-master-data-sync-api
- description: 'Required api role: `API_ORDER` All endpoints related to order creation and status retrieval/subscription. ### Getting started See [this section](/docs/section/transport-order-creation-and-status) to g'
  name: Qargo Use case / Order API
  slug: qargo-use-case-order-api
- description: 'Required api role: not applicable (push/push) Purpose: This interface allows an external party to integrate with 3rd party transport management systems for subcontracting. The subcontractor dispatch u'
  name: Qargo Use case / Subcontractor dispatch API
  slug: qargo-use-case-subcontractor-dispatch-api
- description: The Use case / Tracking API from Qargo — 1 operation(s) for use case / tracking.
  name: Qargo Use case / Tracking API
  slug: qargo-use-case-tracking-api
- description: 'Required api role: `API_TRIP` Purpose: This interface allows an external system (e.g. a route optimisation tool) to send fully planned trips into Qargo. When a trip payload arrives, Qargo creates or u'
  name: Qargo Use case / Trip import API
  slug: qargo-use-case-trip-import-api
- description: The Use case / Visibility API from Qargo — 2 operation(s) for use case / visibility.
  name: Qargo Use case / Visibility API
  slug: qargo-use-case-visibility-api
- description: Inbound webhooks use **Basic Authentication**, not OAuth2. See [Authentication](/docs/section/authentication) for details on how to authenticate webhook requests.
  name: Qargo Webhooks / Inbound API
  slug: qargo-webhooks-inbound-api
- description: Outbound webhooks are sent by Qargo to your system when certain events occur. Configure the receiving endpoint URL and credentials in the integration settings.
  name: Qargo Webhooks / Outbound API
  slug: qargo-webhooks-outbound-api
artifact_total: 31
asyncapis:
- description: ''
  name: Qargo Webhooks
  slug: qargo-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.qargo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.qargo.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.qargo.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.qargo.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.qargo.com/docs/section/authentication/the-api-call-to-request-tokens
- group: auth
  title: ''
  type: Authentication
  url: authentication/qargo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: authentication/qargo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qargo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qargo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qargo-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/qargo-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/qargo-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://api-docs.qargo.com/docs/section/changelog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/qargo-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/qargo-webhooks.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qargo-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qargo-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qargo-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qargo-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/qargo-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qargo-llms.txt
- group: build
  title: ''
  type: Postman
  url: postman/qargo-postman.json
- group: operate
  title: ''
  type: Support
  url: https://help.qargo.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.qargo.com/resources/news-and-blogs/
- group: start
  title: ''
  type: Login
  url: https://app.qargo.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qargo.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qargo.com/privacy-notice/
created: '2026-07-17'
description: Qargo is an intelligent transport management platform (TMS) for road carriers, freight forwarders and 3PLs, using AI to automate operational and administrative work across planning, execution, tracking and accounting. Qargo publishes a public Qargo TMS API (OpenAPI 3.1, v1.2.0, base https://api.qargo.com) exposing tenant-level integration and operational endpoints for orders, trips, companies, resources, documents, tasks and accounting, plus inbound and outbound webhooks and separate Subcontractor and Customer APIs. Service-to-service authentication uses OAuth2 client-credentials (JWT); webhooks use HTTP Basic. Qargo is a Balderton Capital portfolio company.
image: https://app.qargo.com/assets/Qargo_Icon.png
layout: provider
mcp_servers:
- description: ''
  name: qargo-mcp.yml
  slug: qargo-mcpyml
modified: '2026-07-20'
name: Qargo
nav: Providers
network: true
overview: 'Qargo publishes 24 APIs on the [APIs.io](https://apis.io/) network, including API / Accounting API, API / Authentication API, API / Company API, and 21 more. Tagged areas include Company, Transport Management, Logistics, Supply Chain, and Freight.


  The Qargo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Qargo''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 21 more developer resources.'
random_paper: 64
score:
  band: developing
  composite: 47.8
  delta: -2.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 66.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 31.6
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Qargo Authentication
  slug: qargo-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Qargo Domain Security
  slug: qargo-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: qargo
tags:
- Company
- Transport Management
- Logistics
- Supply Chain
- Freight
- TMS
- Accounting
- Webhooks
website: https://www.qargo.com/
---
