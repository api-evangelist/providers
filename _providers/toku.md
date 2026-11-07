---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 90
  human_in_the_loop: 0
  name: Toku Agentic Access
  operation_count: 137
  slug: toku-agentic-access
  summary_line: 137 operations · 90 acting
api_count: 2
apis:
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: El objeto `Adjustment Document` es una nota de crédito o factura de proveedor que la organización puede aplicar como saldo a favor al momento del cobro. Si está ligado a una Invoice (`id_origin_invoic
  name: Toku Adjustment Documents API
  slug: toku-adjustment-documents-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: Emisión y validación de tokens de acceso, resolución de API keys, verificación de reCAPTCHA y políticas de acceso por Organization.
  name: Toku Auth API
  slug: toku-auth-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: 'Alta y mantención de los Beneficiaries: las personas o empresas que reciben un pago. Un Beneficiary agrupa los datos de identidad y una o más Beneficiary Accounts.'
  name: Toku Beneficiaries API
  slug: toku-beneficiaries-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: 'Consulta y mantención de las Beneficiary Accounts: las cuentas bancarias asociadas a un Beneficiary, junto con su verificación bancaria y su flujo de aprobación.'
  name: Toku Beneficiary Accounts API
  slug: toku-beneficiary-accounts-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: 'Emissão de boleto bancário no Brasil e acompanhamento do seu ciclo de vida: registro no banco, consulta do PDF, baixa quando o pagamento é confirmado e cancelamento. Nesta seção, as operações disponív'
  name: Toku Boleto API
  slug: toku-boleto-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: 'Ciclo de vida de una Checkout Session: creación, consulta, actualización de su vencimiento y expiración. Incluye las operaciones que consume el portal de pago de Toku y las que ejecutan procesos inter'
  name: Toku Checkout Session API
  slug: toku-checkout-session-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: 'API server-to-server con la que la organización consulta qué consintió una persona, para decidir qué pedirle antes de anunciar. Se autentica igual que los intents: la llama su backend con la api-key d'
  name: Toku Consulta de consentimientos API
  slug: toku-consulta-de-consentimientos-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: Cuentas bancarias que un Customer deja registradas para que se le cobre por PAC o domiciliación bancaria.
  name: Toku Customer Collection Accounts API
  slug: toku-customer-collection-accounts-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: 'Endpoints que sostienen el Customer Portal de Toku: el portal web donde un Customer revisa sus Invoices y Subscriptions, inscribe medios de pago y paga. La mayoría de estas operaciones las consume el '
  name: Toku Customer Portal API
  slug: toku-customer-portal-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: Consulta de la información de un Customer asociada a sus medios de pago, y asociación de un Payment Method con una Subscription.
  name: Toku Customers API
  slug: toku-customers-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: 'Cobrança de Subscriptions por Débito Automático no Brasil: cadastro das contas bancárias que o pagador autorizou no banco, geração dos arquivos de remessa enviados ao banco e processamento dos arquivo'
  name: Toku Débito Automático API
  slug: toku-d-bito-autom-tico-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: The Debt Reconciliation Public API from Toku — 1 operation(s) for debt reconciliation public.
  name: Toku Debt Reconciliation Public API
  slug: toku-debt-reconciliation-public-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: The Efectivo API from Toku — 2 operation(s) for efectivo.
  name: Toku Efectivo API
  slug: toku-efectivo-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: Creación de Documents para firma electrónica, consulta de su estado y descarga del documento firmado.
  name: Toku Electronic Signature API
  slug: toku-electronic-signature-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: 'Facturación electrónica en México. Cubre las dos mitades del flujo: los datos de facturación que se guardan sobre un Customer o un Invoice, y la emisión de los billing documents (CFDI) que se derivan '
  name: Toku Facturación API
  slug: toku-facturaci-n-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: 'Integración con Forum: configuración de la ventana de envío de cada organización, despacho de los Webhooks que informan los pagos y generación de los reportes diarios que los respaldan.'
  name: Toku Forum API
  slug: toku-forum-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: API server-to-server con la que la organización anuncia cada consentimiento que va a pedir, antes de renderizar su formulario. La llama su backend con la api-key de Toku, y el gateway le entrega al se
  name: Toku Intents de consentimiento API
  slug: toku-intents-de-consentimiento-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: Una `Invoice` contiene la información de una deuda. Para crearla se necesita el identificador público del `Customer` al que pertenece, que se obtiene al crearlo en Toku y tiene la forma `cus_ejC08yLqO
  name: Toku Invoices API
  slug: toku-invoices-api
- baseURL: https://secure.api.trytoku.com
  baseurl_source: declared
  description: Generación de las llaves con las que encriptas los datos de tarjeta antes de enviarlos. Toku soporta RSA 2048 con PKCS1_OAEP y AES 256 en modo CBC.
  name: Toku Llaves de encriptación API
  slug: toku-llaves-de-encriptaci-n-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: 'Medios de pago con cargo automático a una cuenta bancaria en Chile: PAC y los catálogos bancarios asociados.'
  name: Toku PAC API
  slug: toku-pac-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: 'Administración de los Payment Methods de una Account: creación, consulta, edición, eliminación y carga masiva, además de la invalidación de los medios de pago que dejaron de estar vigentes.'
  name: Toku Payment Methods API
  slug: toku-payment-methods-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: 'Consulta y gestión de Payouts: listado, detalle, aprobación, rechazo, edición de monto, comprobantes, actualización de estado y etapas de creación y ejecución en lote.'
  name: Toku Payout API
  slug: toku-payout-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: Ingesta de Account Payables para crear un Payout Request —enviándolas por API o depositando archivos CSV en el SFTP de la organización— y avance de las filas resultantes hacia el servicio de payouts.
  name: Toku Payout Request Ingestion API
  slug: toku-payout-request-ingestion-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: Seguimiento y cierre de los Payout Request Items, las filas individuales que quedaron registradas al ingestar un Payout Request.
  name: Toku Payout Request Items API
  slug: toku-payout-request-items-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: 'Operações de cobrança Pix integradas diretamente com os PSPs brasileiros: criação da cobrança, cadastro da chave Pix, cancelamento e recebimento das notificações de pagamento enviadas pelo PSP. Nesta '
  name: Toku Pix API
  slug: toku-pix-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: 'Cobrança recorrente por Pix Automático no Brasil: cadastro da recorrência no banco do pagador, cobrança das Invoices de cada ciclo, retentativas e cancelamento. Nesta seção, as operações disponíveis p'
  name: Toku Pix Automático API
  slug: toku-pix-autom-tico-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: 'Registro y administración de los terminales POS de la cuenta. Un terminal es el dispositivo físico donde se cobra, y queda asociado al adquirente con el que se registró: ese adquirente no se elige en '
  name: Toku POS Terminals API
  slug: toku-pos-terminals-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: Comprobantes de una operación y documentos tributarios asociados. Agrupa la generación del comprobante, su descarga mediante URL firmada, la configuración con que se despliega y la emisión del documen
  name: Toku Receipts API
  slug: toku-receipts-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: Devoluciones de dinero sobre un pago ya realizado. Toku registra cada devolución como una Transaction propia de tipo `REVERSED`, ligada al pago original, y la aplica sobre las Invoices que ese pago ha
  name: Toku Refunds API
  slug: toku-refunds-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: 'Motor de reportes por entidad: consulta de columnas y hojas disponibles, generación del reporte completo y procesamiento por partes de los reportes grandes.'
  name: Toku Reports API
  slug: toku-reports-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: 'Execution of risk validators: starting one, the state it is in, and the progress of its steps.'
  name: Toku Risk flow validator executions API
  slug: toku-risk-flow-validator-executions-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: El objeto `Subscription` define el cobro recurrente de un `Customer`.
  name: Toku Subscriptions API
  slug: toku-subscriptions-api
- baseURL: https://secure.api.trytoku.com
  baseurl_source: declared
  description: Endpoints que reciben datos de tarjeta, ya sea para cobrar una vez, para inscribir la tarjeta como medio de pago recurrente o para guardarla como PaymentInstrument sin cobrarla. El campo `card_informa
  name: Toku Tarjetas API
  slug: toku-tarjetas-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: Cobro y registro de Transactions sobre Invoices. Una Transaction agrupa el monto cobrado, el medio de pago usado y los Invoices que salda, e incluye tanto los cobros que procesa Toku como los pagos re
  name: Toku Transactions API
  slug: toku-transactions-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: Bancos con los que un pagador puede pagar por transferencia en Chile, y con qué producto se paga en cada uno.
  name: Toku Transferencias 🇨🇱 API
  slug: toku-transferencias-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: 'Verificación de titularidad de cuentas bancarias mexicanas (CLABE). Se confirma que una cuenta existe y que pertenece a la persona declarada realizando una micro transferencia por SPEI a través de un '
  name: Toku Validación de Cuenta Clabe API
  slug: toku-validaci-n-de-cuenta-clabe-api
- baseURL: https://api.trytoku.com
  baseurl_source: declared
  description: El objeto `Webhook Endpoint` registra una url y los eventos que deben ser notificados a traves de esta, para un cliente especifico.
  name: Toku Webhook Endpoints API
  slug: toku-webhook-endpoints-api
artifact_total: 51
common:
- group: agent
  href: https://artifacts.apis.io/toku/agentic-access/toku-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/toku-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/toku/rules/toku-rules.yml
  title: ''
  type: Spectral
  url: rules/toku-rules.yml
- group: design
  href: https://artifacts.apis.io/toku/json-ld/toku-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/toku-context.jsonld
- group: design
  href: https://artifacts.apis.io/toku/vocabulary/toku-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/toku-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/toku/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/toku/data-model/toku-data-model.yml
  title: ''
  type: DataModel
  url: data-model/toku-data-model.yml
- group: design
  href: https://artifacts.apis.io/toku/conventions/toku-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/toku-conventions.yml
- group: design
  href: https://artifacts.apis.io/toku/conventions/toku-conventions.yml
  title: ''
  type: Conventions
  url: conventions/toku-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.trytoku.com/
- group: design
  href: https://artifacts.apis.io/toku/errors/toku-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/toku-problem-types.yml
- group: design
  href: https://artifacts.apis.io/toku/conformance/toku-conformance.yml
  title: ''
  type: Conformance
  url: conformance/toku-conformance.yml
- group: agent
  href: https://artifacts.apis.io/toku/llms/toku-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/toku-llms.txt
- group: agent
  href: https://artifacts.apis.io/toku/mcp/toku-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/toku-mcp.yml
- group: agent
  href: https://artifacts.apis.io/toku/well-known/toku-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/toku-well-known.yml
- group: other
  href: https://artifacts.apis.io/toku/hosts/toku-hosts.yml
  title: ''
  type: Hosts
  url: hosts/toku-hosts.yml
- group: other
  href: https://artifacts.apis.io/toku/vendors/toku-vendors.yml
  title: ''
  type: Vendors
  url: vendors/toku-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.trytoku.com/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/toku/authentication/toku-authentication.yml
  title: ''
  type: Authentication
  url: authentication/toku-authentication.yml
- group: auth
  href: https://artifacts.apis.io/toku/security/toku-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/toku-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/toku/security/toku-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/toku-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trytoku.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trytoku.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.trytoku.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.trytoku.com/
- group: operate
  title: ''
  type: Support
  url: https://trytoku.com/support
- group: company
  title: ''
  type: Blog
  url: https://trytoku.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://trytoku.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trytoku.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trytoku.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://trytoku.com/signup
created: '2026-10-29'
description: Toku is a Chile‑based fintech platform that provides B2B payment and collection solutions powered by intelligent AI agents. The platform automates invoicing, executes payments, reconciles transactions, and reduces delinquency, enabling businesses to increase cash flow and streamline financial operations. Backed by Gradient Ventures, Toku serves enterprises across Latin America.
image: https://trytoku.com/og/home.jpg
json_schemas:
- name: CheckoutSessionRequestV2Decryption
  property_count: 20
  slug: toku-checkout-session-request-v2-decryption
- name: CreatedCheckoutSessionResponse
  property_count: 29
  slug: toku-created-checkout-session-response
- name: PublicCheckoutSessionResponse
  property_count: 28
  slug: toku-public-checkout-session-response
- name: UpdateWebhookEndpointPayload
  property_count: 5
  slug: toku-update-webhook-endpoint-payload
- name: WebhookEndpointPayload
  property_count: 5
  slug: toku-webhook-endpoint-payload
- name: WebhookEndpoint
  property_count: 7
  slug: toku-webhook-endpoint
jsonld:
- class_count: 120
  name: Toku Context
  property_count: 260
  slug: toku-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.trytoku.com.
  name: Toku MCP Server
  slug: toku-mcp-yml
modified: '2026-10-29'
name: Toku
nav: Providers
network: true
overview: 'Toku publishes 37 API contracts indexed on the [APIs.io](https://apis.io/) network, including Adjustment Documents API, Auth API, Beneficiaries API, and 34 more. Tagged areas include Fintech, Payments, B2B, Automation, and Chile.


  The Toku catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Toku''s developer surface includes getting-started guide, authentication, documentation, API reference, support, engineering blog, pricing, and 23 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Toku API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 2
  slug: toku-rules
score:
  band: developing
  composite: 47.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 71.6
    developer_ergonomics: 41.0
    discoverability: 75.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - chile
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 56.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 37
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/toku/toku-2026-11-03T144842.png
security:
- kind: authentication
  name: Toku Authentication
  slug: toku-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Toku Domain Security
  slug: toku-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Toku Trust Center
  slug: toku-trust-center
  summary_line: PCI DSS
skill_count: 1
skills:
- name: create-card-transaction
  slug: toku-create-card-transaction
slug: toku
tags:
- Fintech
- Payments
- B2B
- Automation
- Chile
website: https://trytoku.com/
---
