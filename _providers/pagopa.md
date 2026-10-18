---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bound
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 379
  human_in_the_loop: 20
  name: Pagopa Agentic Access
  operation_count: 697
  slug: pagopa-agentic-access
  summary_line: 697 operations · 379 acting · 20 human-in-the-loop
api_count: 86
apis:
- description: SOAP (WSDL) interfaces of the pagoPA payments node (Nodo dei Pagamenti) between creditor organizations (EC/PA), payment service providers (PSP) and the node, published in the pagopa/pagopa-api reposit
  name: pagoPA - Nodo dei Pagamenti SOAP interfaces
  slug: pagopa-nodo-dei-pagamenti-soap-interfaces
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Api's for performing a debt position census
  name: PagoPA ACA API
  slug: pagopa-aca-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Activations API from PagoPA — 1 operation(s) for activations.
  name: PagoPA Activations API
  slug: pagopa-activations-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Agreements routes
  name: PagoPA Agreements API
  slug: pagopa-agreements-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Attributes routes
  name: PagoPA Attributes API
  slug: pagopa-attributes-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Api's to notify transaction outcome
  name: PagoPA b2b - pagoPA side API
  slug: pagopa-b2b-pagopa-side-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: API Group aims to get the callback.
  name: PagoPA Callback API
  slug: pagopa-callback-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The callback-cancel API from PagoPA — 1 operation(s) for callback-cancel.
  name: PagoPA Callback Cancel API
  slug: pagopa-callback-cancel-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Carts API from PagoPA — 1 operation(s) for carts.
  name: PagoPA Carts API
  slug: pagopa-carts-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: verifies the validity and existence of the input Organization id
  name: PagoPA Check API
  slug: pagopa-check-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: 'ENG: TPP integration - Citizen consent operations <br> IT: Integrazione TPP - Operazioni sui consensi del cittadino'
  name: PagoPA Citizen operation API
  slug: pagopa-citizen-operation-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Clients routes
  name: PagoPA Clients API
  slug: pagopa-clients-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Create operation.
  name: PagoPA Create API
  slug: pagopa-create-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Data Preparation API from PagoPA — 6 operation(s) for data preparation.
  name: PagoPA Data Preparation API
  slug: pagopa-data-preparation-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Debt Position Actions API API from PagoPA — 2 operation(s) for debt position actions api.
  name: PagoPA Debt Position Actions API
  slug: pagopa-debt-position-actions-api-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Debt Positions API API from PagoPA — 3 operation(s) for debt positions api.
  name: PagoPA Debt Positions API
  slug: pagopa-debt-positions-api-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Delegations routes
  name: PagoPA Delegations API
  slug: pagopa-delegations-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Delete operation.
  name: PagoPA Delete API
  slug: pagopa-delete-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Dossier API from PagoPA — 3 operation(s) for dossier.
  name: PagoPA Dossier API
  slug: pagopa-dossier-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Invocazioni per recupero dei disservizi di SEND
  name: PagoPA Downtime API
  slug: pagopa-downtime-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: E-Services routes
  name: PagoPA Eservices API
  slug: pagopa-eservices-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: E-Service Templates routes
  name: PagoPA Eservice Templates API
  slug: pagopa-eservicetemplates-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Events routes
  name: PagoPA Events API
  slug: pagopa-events-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The External APIs API from PagoPA — 3 operation(s) for external apis.
  name: PagoPA External APIs API
  slug: pagopa-external-apis-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Verify service status
  name: PagoPA Health API
  slug: pagopa-health-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Unauthenticated endpoint for checking service status
  name: PagoPA Health Check API
  slug: pagopa-health-check-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Home API from PagoPA — 1 operation(s) for home.
  name: PagoPA Home API
  slug: pagopa-home-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Invocazioni per sapere lo stato dell'E-service di PDND Interoprabilità
  name: PagoPA Interop Probing API
  slug: pagopa-interopprobing-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Keys routes
  name: PagoPA Keys API
  slug: pagopa-keys-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Invocazioni per effettuare il download degli atti opponibili a terzi
  name: PagoPA Legal Facts API
  slug: pagopa-legalfacts-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The manage API from PagoPA — 4 operation(s) for manage.
  name: PagoPA Manage API
  slug: pagopa-manage-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The manage-authorization API from PagoPA — 2 operation(s) for manage-authorization.
  name: PagoPA Manage Authorization API
  slug: pagopa-manage-authorization-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The manage-release API from PagoPA — 1 operation(s) for manage-release.
  name: PagoPA Manage Release API
  slug: pagopa-manage-release-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The manage-review API from PagoPA — 1 operation(s) for manage-review.
  name: PagoPA Manage Review API
  slug: pagopa-manage-review-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Massive operation APIs for Debt Positions - v1 API from PagoPA — 1 operation(s) for massive operation apis for debt positions - v1.
  name: PagoPA Massive operation APIs for Debt Positions - v1 API
  slug: pagopa-massive-operation-apis-for-debt-positions-v1-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Massive operation APIs for Debt Positions - v2 API from PagoPA — 1 operation(s) for massive operation apis for debt positions - v2.
  name: PagoPA Massive operation APIs for Debt Positions - v2 API
  slug: pagopa-massive-operation-apis-for-debt-positions-v2-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Massive operation observability APIs - v1 API from PagoPA — 3 operation(s) for massive operation observability apis - v1.
  name: PagoPA Massive operation observability APIs - v1 API
  slug: pagopa-massive-operation-observability-apis-v1-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Massive operation observability APIs - v2 API from PagoPA — 3 operation(s) for massive operation observability apis - v2.
  name: PagoPA Massive operation observability APIs - v2 API
  slug: pagopa-massive-operation-observability-apis-v2-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: APIs for @eBollo v1
  name: PagoPA MBD - v1 API
  slug: pagopa-mbd-v1-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: APIs for @eBollo v2
  name: PagoPA MBD - v2 API
  slug: pagopa-mbd-v2-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Messages API from PagoPA — 3 operation(s) for messages.
  name: PagoPA Messages API
  slug: pagopa-messages-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Testing network connection
  name: PagoPA Network Testing API
  slug: pagopa-network-testing-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Invocazioni per effettuare il pre-caricamento dei documenti della notifica e inviare notifiche
  name: PagoPA New Notification API
  slug: pagopa-newnotification-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Notice Generation Request APIs API from PagoPA — 7 operation(s) for notice generation request apis.
  name: PagoPA Notice Generation Request APIs API
  slug: pagopa-notice-generation-request-apis-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Notice Templates APIs API from PagoPA — 2 operation(s) for notice templates apis.
  name: PagoPA Notice Templates APIs API
  slug: pagopa-notice-templates-apis-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Annullamento di una notifica
  name: PagoPA Notification Cancellation API
  slug: pagopa-notificationcancellation-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Invocazioni per determinare il costo della notifica per il destinatario.
  name: PagoPA Notification Price API
  slug: pagopa-notificationprice-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The NotificationPriceV23 API from PagoPA — 1 operation(s) for notificationpricev23.
  name: PagoPA Notification Price V23 API
  slug: pagopa-notificationpricev23-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Organization Requests API from PagoPA — 2 operation(s) for organization requests.
  name: PagoPA Organization Requests API
  slug: pagopa-organization-requests-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: APIs for creditor institution, used for inspection of generated flows
  name: PagoPA Organizations API
  slug: pagopa-organizations-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Payment operation
  name: PagoPA Payment API
  slug: pagopa-payment-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: APIs to retrieve payment options
  name: PagoPA Payment Options API
  slug: pagopa-payment-options-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Payment Options Resource API from PagoPA — 1 operation(s) for payment options resource.
  name: PagoPA Payment Options Resource API
  slug: pagopa-payment-options-resource-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Payment Receipts REST APIs API from PagoPA — 2 operation(s) for payment receipts rest apis.
  name: PagoPA Payment Receipts REST APIs API
  slug: pagopa-payment-receipts-rest-apis-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Invocazioni per comunicare eventi di pagamento dalla PA
  name: PagoPA Payment Events API
  slug: pagopa-paymentevents-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Payments API API from PagoPA — 1 operation(s) for payments api.
  name: PagoPA Payments API
  slug: pagopa-payments-api-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Payments receipts API API from PagoPA — 2 operation(s) for payments receipts api.
  name: PagoPA Payments receipts API
  slug: pagopa-payments-receipts-api-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Producer Keychains routes
  name: PagoPA Producer Keychains API
  slug: pagopa-producerkeychains-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Operazioni relative all'elenco dei prodotti e al filtraggio
  name: PagoPA Products API
  slug: pagopa-products-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Profiles API from PagoPA — 2 operation(s) for profiles.
  name: PagoPA Profiles API
  slug: pagopa-profiles-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Pseudonymization data API from PagoPA — 2 operation(s) for pseudonymization data.
  name: PagoPA Pseudonymization data API
  slug: pagopa-pseudonymization-data-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: APIs for payment service providers, used for creation and inspection of flows
  name: PagoPA PSP API
  slug: pagopa-psp-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Purposes routes
  name: PagoPA Purposes API
  slug: pagopa-purposes-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Purpose Templates routes
  name: PagoPA Purpose Templates API
  slug: pagopa-purposetemplates-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Read operation.
  name: PagoPA Read API
  slug: pagopa-read-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The remote-content API from PagoPA — 2 operation(s) for remote-content.
  name: PagoPA Remote Content API
  slug: pagopa-remote-content-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Invocazioni utilizzabili dai mittenti per verificare lo stato delle richieste di notifica inviate e delle notifiche accettate.
  name: PagoPA Sender Read B2B API
  slug: pagopa-senderreadb2b-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The service-topics API from PagoPA — 1 operation(s) for service-topics.
  name: PagoPA Service Topics API
  slug: pagopa-service-topics-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Signals API from PagoPA — 2 operation(s) for signals.
  name: PagoPA Signals API
  slug: pagopa-signals-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Signature API from PagoPA — 2 operation(s) for signature.
  name: PagoPA Signature API
  slug: pagopa-signature-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Signature Request API from PagoPA — 5 operation(s) for signature request.
  name: PagoPA Signature Request API
  slug: pagopa-signature-request-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Signer API from PagoPA — 1 operation(s) for signer.
  name: PagoPA Signer API
  slug: pagopa-signer-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Specifiche Integrazione Messaggi Di Cortesia (Server To Server) API from PagoPA — 2 operation(s) for specifiche integrazione messaggi di cortesia (server to server).
  name: PagoPA Specifiche Integrazione Messaggi Di Cortesia (Server To Server) API
  slug: pagopa-specifiche-integrazione-messaggi-di-cortesia-server-to-server-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Lettura dello stato di SEND, API pubbliche
  name: PagoPA Status API
  slug: pagopa-status-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Gestione degli stream di eventi che PN mette a disposizione
  name: PagoPA Streams API
  slug: pagopa-streams-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Subscriptions Feed API from PagoPA — 1 operation(s) for subscriptions feed.
  name: PagoPA Subscriptions Feed API
  slug: pagopa-subscriptions-feed-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Tenants routes
  name: PagoPA Tenants API
  slug: pagopa-tenants-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Tracings service
  name: PagoPA Tracings API
  slug: pagopa-tracings-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Operazioni relative alle transazioni
  name: PagoPA Transaction API
  slug: pagopa-transaction-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Update operation.
  name: PagoPA Update API
  slug: pagopa-update-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: Users routes
  name: PagoPA Users API
  slug: pagopa-users-api
- baseURL: https://api.platform.pagopa.it/bizevents/service/v1
  baseurl_source: declared
  description: The Utility API from PagoPA — 1 operation(s) for utility.
  name: PagoPA Utility API
  slug: pagopa-utility-api
artifact_total: 189
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/capabilities/pagopa-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/pagopa-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/agentic-access/pagopa-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pagopa-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/rate-limits/pagopa-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pagopa-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/rules/pagopa-rules.yml
  title: ''
  type: Spectral
  url: rules/pagopa-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/rules/pagopa-pn-mandate-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/pagopa-pn-mandate-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/rules/pagopa-interop-be-monorepo-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/pagopa-interop-be-monorepo-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/json-ld/pagopa-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pagopa-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/vocabulary/pagopa-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pagopa-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/data-model/pagopa-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pagopa-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/changelog/pagopa-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pagopa-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/conventions/pagopa-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/pagopa-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/conventions/pagopa-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pagopa-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/sandbox/pagopa-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/pagopa-sandbox.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://api.notifichedigitali.it/status
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/lifecycle/pagopa-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pagopa-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/errors/pagopa-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pagopa-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/conformance/pagopa-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pagopa-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/overlays/pagopa-aca-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pagopa-aca-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/llms/pagopa-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pagopa-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/mcp/pagopa-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/pagopa-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/mcp/pagopa-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pagopa-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/hosts/pagopa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pagopa-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/vendors/pagopa-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pagopa-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/packages/pagopa-packages.yml
  title: ''
  type: SDKs
  url: packages/pagopa-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/packages/pagopa-packages.yml
  title: ''
  type: Packages
  url: packages/pagopa-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.pagopa.it/it/send/guides/manuale-operativo/v1.1.4/mittente/funzionario-autorizzato-del-mittente/richiesta-di-onboarding-processo-di-adesione
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/scopes/pagopa-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/pagopa-scopes.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/authentication/pagopa-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pagopa-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/security/pagopa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pagopa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pagopa.it/it/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.pagopa.it/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pagopa.it/home
- group: operate
  title: ''
  type: Support
  url: https://centroassistenza.pagopa.it/hc
- group: operate
  title: ''
  type: Contact
  url: https://www.pagopa.it/it/contatti/
- group: company
  title: ''
  type: Blog
  url: https://medium.com/pagopa-spa
- group: company
  title: ''
  type: Newsroom
  url: https://www.pagopa.it/it/media
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pagopa
- group: start
  title: ''
  type: Login
  url: https://selfcare.pagopa.it/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.pagopa.it/it/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.pagopa.it/it/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.pagopa.it/it/responsible-disclosure-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.pagopa.it/it/certificazioni/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pagopa
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/pagopa/interop-be-monorepo/blob/7ab5d3041fd1be18a145be0e2831b9778e3ada5e/.spectral.yaml
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/pagopa/pn-mandate/blob/eb556d63cdf6e017dfe1ec63bfd2eb0e58fd0b02/.spectral.yml
created: '2026-10-09'
description: PagoPA S.p.A. is the Italian state-owned company (owned by the State through the Ministry of Economy and Finance, supervised by the Presidency of the Council of Ministers) whose mission is to design and build the State's digital infrastructure for public digital services. Its products include the pagoPA payments platform, the IO public services app, SEND (digital notifications), the National Digital Data Platform (PDND Interoperability), PARI, Check IBAN and the European Digital Identity Wallet, with APIs and guides published on its Developer Portal (developer.pagopa.it) and docs.pagopa.it.
image: https://avatars.githubusercontent.com/u/57742367?v=4
json_schemas:
- name: AccessControlAllowOrigin
  property_count: 0
  slug: pagopa-access-control-allow-origin
- name: Agreement
  property_count: 15
  slug: pagopa-agreement
- name: AlreadyPaidPaymentOptionModel
  property_count: 1
  slug: pagopa-already-paid-payment-option-model
- name: AppInfo
  property_count: 3
  slug: pagopa-app-info
- name: AsynchronousSepaRequestToPayResponseResource
  property_count: 3
  slug: pagopa-asynchronous-sepa-request-to-pay-response-resource
- name: AuthBarCodePaymentDTO
  property_count: 3
  slug: pagopa-auth-bar-code-payment-dto
- name: AuthPaymentResponseDTO
  property_count: 12
  slug: pagopa-auth-payment-response-dto
- name: AuthRequestDynamic
  property_count: 0
  slug: pagopa-auth-request-dynamic
- name: BrokerInstitutionsResponse
  property_count: 2
  slug: pagopa-broker-institutions-response
- name: CartRequest
  property_count: 5
  slug: pagopa-cart-request
- name: CIIbansResponse
  property_count: 2
  slug: pagopa-ciibans-response
- name: CitizenConsentResponseDTO
  property_count: 2
  slug: pagopa-citizen-consent-response-dto
- name: CreateDossierBody
  property_count: 3
  slug: pagopa-create-dossier-body
- name: CreateFlowRequest
  property_count: 9
  slug: pagopa-create-flow-request
- name: CreateMbdRequestV2
  property_count: 2
  slug: pagopa-create-mbd-request-v2
- name: CreateSignatureRequestBody
  property_count: 4
  slug: pagopa-create-signature-request-body
- name: CtReceiptModelResponse
  property_count: 28
  slug: pagopa-ct-receipt-model-response
- name: DataPreparationResponse
  property_count: 0
  slug: pagopa-data-preparation-response
- name: DatapreparationTemplate
  property_count: 1
  slug: pagopa-datapreparation-template
- name: DebtPositionResponse
  property_count: 14
  slug: pagopa-debt-position-response
- name: DossierDetailView
  property_count: 6
  slug: pagopa-dossier-detail-view
- name: EServiceDescriptor
  property_count: 15
  slug: pagopa-eservice-descriptor
- name: EServiceTemplateVersion
  property_count: 11
  slug: pagopa-eservice-template-version
- name: FileIdListResponse
  property_count: 0
  slug: pagopa-file-id-list-response
- name: FlowList
  property_count: 0
  slug: pagopa-flow-list
- name: GetCartResponse
  property_count: 3
  slug: pagopa-get-cart-response
- name: GetGenerationRequestStatusResource
  property_count: 3
  slug: pagopa-get-generation-request-status-resource
- name: GetMbdRequest
  property_count: 3
  slug: pagopa-get-mbd-request
- name: GetMdbReceipt
  property_count: 1
  slug: pagopa-get-mdb-receipt
- name: GetSignedUrlResource
  property_count: 1
  slug: pagopa-get-signed-url-resource
- name: GetTracingErrorsResponse
  property_count: 2
  slug: pagopa-get-tracing-errors-response
- name: InputMessage
  property_count: 1
  slug: pagopa-input-message
- name: InvoiceDTO
  property_count: 2
  slug: pagopa-invoice-dto
- name: ListCitizenConsentResponseDTO
  property_count: 0
  slug: pagopa-list-citizen-consent-response-dto
- name: NewDebtPositionRequest
  property_count: 13
  slug: pagopa-new-debt-position-request
- name: NewNotificationRequest
  property_count: 16
  slug: pagopa-new-notification-request
- name: NewNotificationRequestV21
  property_count: 18
  slug: pagopa-new-notification-request-v21
- name: NewNotificationRequestV23
  property_count: 18
  slug: pagopa-new-notification-request-v23
- name: NewNotificationRequestV24
  property_count: 19
  slug: pagopa-new-notification-request-v24
- name: NewNotificationRequestV25
  property_count: 19
  slug: pagopa-new-notification-request-v25
- name: NewNotificationRequestV26
  property_count: 20
  slug: pagopa-new-notification-request-v26
- name: NoticeGenerationMassiveRequest
  property_count: 1
  slug: pagopa-notice-generation-massive-request
- name: NoticeGenerationMassiveResource
  property_count: 1
  slug: pagopa-notice-generation-massive-resource
- name: NoticeGenerationRequestItem
  property_count: 2
  slug: pagopa-notice-generation-request-item
- name: NotificationPayload
  property_count: 12
  slug: pagopa-notification-payload
- name: PaginatedFlowsCreatedResponse
  property_count: 3
  slug: pagopa-paginated-flows-created-response
- name: PaginatedFlowsPublishedResponse
  property_count: 3
  slug: pagopa-paginated-flows-published-response
- name: PaginatedFlowsResponse
  property_count: 3
  slug: pagopa-paginated-flows-response
- name: PaginatedPaymentsResponse
  property_count: 3
  slug: pagopa-paginated-payments-response
- name: PaymentOptionsResponse
  property_count: 5
  slug: pagopa-payment-options-response
- name: PaymentPositionModelBaseResponse
  property_count: 12
  slug: pagopa-payment-position-model-base-response
- name: PaymentPositionModelResponseV3
  property_count: 10
  slug: pagopa-payment-position-model-response-v3
- name: PaymentPositionModel
  property_count: 21
  slug: pagopa-payment-position-model
- name: PaymentPositionModelV3
  property_count: 7
  slug: pagopa-payment-position-model-v3
- name: PaymentPositionsInfo
  property_count: 2
  slug: pagopa-payment-positions-info
- name: PaymentPositionsInfoV3
  property_count: 2
  slug: pagopa-payment-positions-info-v3
- name: PaymentsModelResponse
  property_count: 23
  slug: pagopa-payments-model-response
- name: PreviewPaymentRequestV2DTO
  property_count: 2
  slug: pagopa-preview-payment-request-v2-dto
- name: PreviewPaymentResponseV2DTO
  property_count: 9
  slug: pagopa-preview-payment-response-v2-dto
- name: Problem
  property_count: 6
  slug: pagopa-problem
- name: PseudonymizationResponse
  property_count: 2
  slug: pagopa-pseudonymization-response
- name: Purpose
  property_count: 17
  slug: pagopa-purpose
- name: PurposeTemplate
  property_count: 13
  slug: pagopa-purpose-template
- name: RateLimitLimit
  property_count: 0
  slug: pagopa-rate-limit-limit
- name: RateLimitReset
  property_count: 0
  slug: pagopa-rate-limit-reset
- name: ReceiptsInfo
  property_count: 1
  slug: pagopa-receipts-info
- name: RecoverTracingRequest
  property_count: 1
  slug: pagopa-recover-tracing-request
- name: RetrievaIdResponseDTO
  property_count: 1
  slug: pagopa-retrieva-id-response-dto
- name: RetrievalRequestDTO
  property_count: 3
  slug: pagopa-retrieval-request-dto
- name: RetrievalResponseDTO
  property_count: 6
  slug: pagopa-retrieval-response-dto
- name: RetryAfter
  property_count: 0
  slug: pagopa-retry-after
- name: Richiesta
  property_count: 1
  slug: pagopa-richiesta
- name: SepaRequestToPayCancellationResponseResource
  property_count: 3
  slug: pagopa-sepa-request-to-pay-cancellation-response-resource
- name: SignalPayload
  property_count: 5
  slug: pagopa-signal-payload
- name: SignalPullResponse
  property_count: 2
  slug: pagopa-signal-pull-response
- name: SignalPushResponse
  property_count: 1
  slug: pagopa-signal-push-response
- name: SignatureField
  property_count: 2
  slug: pagopa-signature-field
- name: SignatureRequestDetailView
  property_count: 14
  slug: pagopa-signature-request-detail-view
- name: SignatureRequestList
  property_count: 2
  slug: pagopa-signature-request-list
- name: SingleFlowCreatedResponse
  property_count: 15
  slug: pagopa-single-flow-created-response
- name: SingleFlowResponse
  property_count: 16
  slug: pagopa-single-flow-response
- name: SubmitTracingRequest
  property_count: 2
  slug: pagopa-submit-tracing-request
- name: SuccessResponseSignature
  property_count: 1
  slug: pagopa-success-response-signature
- name: TemplateResource
  property_count: 3
  slug: pagopa-template-resource
- name: TokenResponse
  property_count: 3
  slug: pagopa-token-response
- name: TppNetworkConnectionResponse
  property_count: 2
  slug: pagopa-tpp-network-connection-response
- name: TransactionBarCodeResponse
  property_count: 8
  slug: pagopa-transaction-bar-code-response
- name: TransactionResultRequest
  property_count: 4
  slug: pagopa-transaction-result-request
- name: TransactionResultResponse
  property_count: 2
  slug: pagopa-transaction-result-response
- name: UpdateTransferIbanMassiveResponse
  property_count: 2
  slug: pagopa-update-transfer-iban-massive-response
- name: UploadReportDTO
  property_count: 0
  slug: pagopa-upload-report-dto
- name: UploadReport
  property_count: 6
  slug: pagopa-upload-report
- name: UploadStatus
  property_count: 0
  slug: pagopa-upload-status
- name: VerificaCodiceFiscale
  property_count: 3
  slug: pagopa-verifica-codice-fiscale
- name: VerificaOrganizationId
  property_count: 11
  slug: pagopa-verifica-organization-id
- name: VerificationResponse
  property_count: 2
  slug: pagopa-verification-response
jsonld:
- class_count: 120
  name: Pagopa Context
  property_count: 271
  slug: pagopa-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.pagopa.it over streamable HTTP; 3 tools listed.
  name: PagoPA MCP Server
  slug: docs-pagopa-it-home-gitbook-mcp
modified: '2026-10-09'
name: PagoPA
nav: Providers
network: true
overview: 'PagoPA publishes 82 API contracts indexed on the [APIs.io](https://apis.io/) network, including ACA API, Activations API, Agreements API, and 79 more. Tagged areas include Company, Payments, Government, Public Sector, and Digital Identity.


  The PagoPA catalog on APIs.io includes 1 JSON-LD context and 3 Spectral governance rulesets.


  PagoPA''s developer surface includes changelog, sandbox, getting-started guide, authentication, documentation, support, engineering blog, and 39 more developer resources.'
plans:
- name: Pagopa Plans Pricing
  plan_count: 0
  slug: pagopa-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Pagopa Rate Limits
  slug: pagopa-rate-limits
rules:
- authorship: provider
  effective_rule_count: 0
  extends:
  - https://github.com/italia/api-oas-checker-rules/releases/download/1.1/spectral-modi.yml
  name: PagoPA — interop be monorepo rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: pagopa-interop-be-monorepo-spectral-rules
- authorship: provider
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: PagoPA — pn mandate rules
  rule_count: 60
  severity_counts:
    error: 24
    hint: 12
    info: 6
    warn: 18
  slug: pagopa-pn-mandate-spectral-rules
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: PagoPA API Rules
  rule_count: 15
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 10
  slug: pagopa-rules
scopes:
- name: Pagopa Scopes
  scope_count: 6
  slug: pagopa-scopes
  summary_line: 6 scopes · clientCredentials
score:
  band: exemplar
  composite: 69.0
  coverage:
    artifact_dirs: 32
    catalog_earned: 82.3
    catalog_earned_first_party: 26.0
    catalog_gap: 32.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.1
  facets:
    access_clarity: 42.1
    contract_governance: 62.9
    contract_quality: 68.5
    developer_ergonomics: 66.1
    discoverability: 73.3
    operational_transparency: 68.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - italy
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - italy-southern-europe
  previous_composite: 64.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 98.8
      derived: 0
      marker_coverage: 0.0
      total: 81
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 39.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/pagopa/refs/heads/main/screenshots/pagopa-2026-10-11T112310.png
security:
- kind: authentication
  name: Pagopa Authentication
  slug: pagopa-authentication
  summary_line: apiKey/http/oauth2 · 7 schemes
- kind: domain-security
  name: Pagopa Domain Security
  slug: pagopa-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pagopa
tags:
- Company
- Payments
- Government
- Public Sector
- Digital Identity
- Interoperability
- Notification
- Italy
website: https://www.pagopa.it/it/
---
