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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 64
  human_in_the_loop: 7
  name: Qargo Agentic Access
  operation_count: 114
  slug: qargo-agentic-access
  summary_line: 114 operations · 64 acting · 7 human-in-the-loop
api_count: 1
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
artifact_total: 52
asyncapis:
- description: ''
  name: Qargo Webhooks
  slug: qargo-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Qargo TMS API / Accounting API
  slug: open-qargo-api-accounting-api
- collection_type: open
  name: Qargo TMS API / Accounting API / Authentication API
  slug: open-qargo-api-authentication-api
- collection_type: open
  name: Qargo TMS API / Accounting API / Company API
  slug: open-qargo-api-company-api
- collection_type: open
  name: Qargo TMS API / Accounting API / Document API
  slug: open-qargo-api-document-api
- collection_type: open
  name: Qargo TMS API / Accounting API / Order API
  slug: open-qargo-api-order-api
- collection_type: open
  name: Qargo TMS API / Accounting API / Resource API
  slug: open-qargo-api-resource-api
- collection_type: open
  name: Qargo TMS API / Accounting API / Task API
  slug: open-qargo-api-task-api
- collection_type: open
  name: Qargo TMS API / Accounting API / Trip API
  slug: open-qargo-api-trip-api
- collection_type: open
  name: Qargo TMS API / Accounting System API
  slug: open-qargo-system-api
- collection_type: open
  name: Qargo TMS API / Accounting Use case / Accounting API
  slug: open-qargo-use-case-accounting-api
- collection_type: open
  name: Qargo TMS API / Accounting Use case / Customer portal API
  slug: open-qargo-use-case-customer-portal-api
- collection_type: open
  name: Qargo TMS API / Accounting Use case / Document import API
  slug: open-qargo-use-case-document-import-api
- collection_type: open
  name: Qargo TMS API / Accounting Use case / E-invoicing API
  slug: open-qargo-use-case-e-invoicing-api
- collection_type: open
  name: Qargo TMS API / Accounting Use case / Fleet dispatch API
  slug: open-qargo-use-case-fleet-dispatch-api
- collection_type: open
  name: Qargo TMS API / Accounting Use case / Intermodal [partner] API
  slug: open-qargo-use-case-intermodal-partner-api
- collection_type: open
  name: Qargo TMS API / Accounting Use case / Location booking API
  slug: open-qargo-use-case-location-booking-api
- collection_type: open
  name: Qargo TMS API / Accounting Use case / Master data sync API
  slug: open-qargo-use-case-master-data-sync-api
- collection_type: open
  name: Qargo TMS API / Accounting Use case / Order API
  slug: open-qargo-use-case-order-api
- collection_type: open
  name: Qargo TMS API / Accounting Use case / Subcontractor dispatch API
  slug: open-qargo-use-case-subcontractor-dispatch-api
- collection_type: open
  name: Qargo TMS API / Accounting Use case / Tracking API
  slug: open-qargo-use-case-tracking-api
- collection_type: open
  name: Qargo TMS API / Accounting Use case / Trip import API
  slug: open-qargo-use-case-trip-import-api
- collection_type: open
  name: Qargo TMS API / Accounting Use case / Visibility API
  slug: open-qargo-use-case-visibility-api
- collection_type: open
  name: Qargo TMS API / Accounting Webhooks / Inbound API
  slug: open-qargo-webhooks-inbound-api
- collection_type: open
  name: Qargo TMS API / Accounting Webhooks / Outbound API
  slug: open-qargo-webhooks-outbound-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/qargo-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/qargo-tms-overlay.yaml
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
  name: Qargo API documentation
  slug: qargo-api-documentation
modified: '2026-07-20'
name: Qargo
nav: Providers
network: true
overview: 'Qargo publishes 20 APIs on the [APIs.io](https://apis.io/) network, including API / Accounting API, API / Authentication API, API / Company API, and 17 more. Tagged areas include Company, Transport Management, Logistics, Supply Chain, and Freight.


  The Qargo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Qargo''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 23 more developer resources.'
random_paper: 13
score:
  band: developing
  composite: 45.9
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 61.7
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 46.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qargo/refs/heads/main/screenshots/qargo-2026-08-17T081412.png
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
- Webhook
website: https://www.qargo.com/
---
