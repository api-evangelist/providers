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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 58.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 114
  human_in_the_loop: 0
  name: Asaas Agentic Access
  operation_count: 213
  slug: asaas-agentic-access
  summary_line: 213 operations · 114 acting
api_count: 2
apis:
- description: Create, retrieve, update, list, and delete customers ("clientes"). The Customer object holds personal/business identifiers (CPF/CNPJ), contact details, address, default notification preferences, and S
  name: Asaas Customers API
  slug: customers
- description: Core billing endpoint for creating individual charges payable by Boleto, Pix, Credit Card, Debit Card, or "undefined" (let the payer choose). Supports capture, refund, partial refund, anticipation, fi
  name: Asaas Charges (Cobranças) API
  slug: charges
- description: Recurring-billing subscriptions with weekly, biweekly, monthly, bimonthly, quarterly, semiannual, and annual cycles. Supports end-date or open-ended schedules, automatic charge generation per cycle, v
  name: Asaas Subscriptions API
  slug: subscriptions
- description: Generate a fixed series of installment charges from a single installment plan - typical for splitting a total amount across N monthly boletos or credit-card charges.
  name: Asaas Installments (Parcelamentos) API
  slug: installments
- description: Endpoints for Pix instant payments - static and dynamic QR codes, Pix keys (CPF/CNPJ/email/phone/random), QR code decoding, transfer via Pix, and the new Pix Automático (recurring authorized Pix debit
  name: Asaas Pix API
  slug: pix
- description: Issue, retrieve, and reconcile Brazilian boleto bancário (bank slip) charges, with configurable fines, interest, discounts, and due-date updates. Includes a webhook event for cancellation of expired s
  name: Asaas Boleto API
  slug: boleto
- description: Tokenize credit cards client-side and process card charges server-side, including pre-authorization (capture later), capture, refund, and 3DS challenge handling. Supports recurring use of tokenized ca
  name: Asaas Credit Card API
  slug: credit-card
- description: Hosted checkout sessions that bundle one or more products / charges into a shareable payment URL. Supports multiple billing types, tax-document collection, and post-payment redirection.
  name: Asaas Checkout API
  slug: checkout
- description: Generate reusable payment links ("links de pagamento") for one-off or recurring collection over WhatsApp, SMS, email, or social. Each link can carry a fixed or buyer-defined amount.
  name: Asaas Payment Links API
  slug: payment-links
- description: Configure split rules on a charge so that the net amount is automatically distributed across one or more wallet IDs at settlement time - the basis for marketplaces and platforms built on Asaas.
  name: Asaas Split Payments API
  slug: split-payments
- description: 'Move funds out of the Asaas digital account: TED to external banks, Pix transfers to keys or banking details, and internal transfers between Asaas accounts, with optional scheduling.'
  name: Asaas Transfers API
  slug: transfers
- description: Pay external bills (boletos, concessionárias, GPS, DARF) from the Asaas digital account, with barcode-line lookup and scheduled execution.
  name: Asaas Bill Payments API
  slug: bill-payments
- description: Anticipate future receivables - boleto, card, and Pix - to receive funds before the original settlement date in exchange for a discount fee. Endpoints simulate, request, and list anticipations.
  name: Asaas Anticipations (Antecipação) API
  slug: anticipations
- description: Create and manage subaccounts under a master account for white-label and BaaS use cases. Supports KYC document submission, activation links, per-subaccount API keys, and consolidated reporting.
  name: Asaas Subaccounts / White-Label API
  slug: subaccounts
- description: Schedule, issue, and retrieve Brazilian electronic invoices (NFS-e) automatically tied to a charge or subscription, including municipal configuration and tax retention setup.
  name: Asaas Invoices (Nota Fiscal) API
  slug: invoices
- description: Hold funds in escrow ("contas de garantia") until a release condition is met, with API-driven release or refund. Common in marketplaces where buyer-protection windows are required.
  name: Asaas Escrow Accounts API
  slug: escrow
- description: Retrieve and dispute credit-card chargebacks, including evidence upload and status retrieval.
  name: Asaas Chargebacks API
  slug: chargebacks
- description: Retrieve the current account balance and the financial statement (extrato) of credits and debits for the Asaas digital account.
  name: Asaas Account Balance & Statement API
  slug: account-balance
- description: Top up Brazilian prepaid mobile lines by carrier and amount, debiting the Asaas account balance.
  name: Asaas Cell Phone Recharge API
  slug: cell-phone-recharge
- description: Event-driven HTTP callbacks for payment, subscription, transfer, anticipation, chargeback, account, and invoice events. Webhooks require a token (auto-generated as of Feb 2026) and Asaas signs request
  name: Asaas Webhooks API
  slug: webhooks
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Ações em sandbox API from Asaas — 3 operation(s) for ações em sandbox.
  name: Asaas Ações em sandbox API
  slug: asaas-a-es-em-sandbox-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Antecipações API from Asaas — 5 operation(s) for antecipações.
  name: Asaas Antecipações API
  slug: asaas-antecipa-es-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Anticipation API from Asaas — 1 operation(s) for anticipation.
  name: Asaas Anticipation API
  slug: asaas-anticipation-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Assinaturas API from Asaas — 8 operation(s) for assinaturas.
  name: Asaas Assinaturas API
  slug: asaas-assinaturas-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Cartão de crédito API from Asaas — 2 operation(s) for cartão de crédito.
  name: Asaas Cartão de crédito API
  slug: asaas-cart-o-de-cr-dito-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Chargeback API from Asaas — 3 operation(s) for chargeback.
  name: Asaas Chargeback API
  slug: asaas-chargeback-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Checkout API from Asaas — 2 operation(s) for checkout.
  name: Asaas Checkout API
  slug: asaas-checkout-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Clientes API from Asaas — 4 operation(s) for clientes.
  name: Asaas Clientes API
  slug: asaas-clientes-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Cobranças API from Asaas — 17 operation(s) for cobranças.
  name: Asaas Cobranças API
  slug: asaas-cobran-as-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Cobranças com dados resumidos API from Asaas — 8 operation(s) for cobranças com dados resumidos.
  name: Asaas Cobranças com dados resumidos API
  slug: asaas-cobran-as-com-dados-resumidos-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Configurações de Webhooks API from Asaas — 3 operation(s) for configurações de webhooks.
  name: Asaas Configurações de Webhooks API
  slug: asaas-configura-es-de-webhooks-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Consulta Serasa API from Asaas — 2 operation(s) for consulta serasa.
  name: Asaas Consulta Serasa API
  slug: asaas-consulta-serasa-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Conta Escrow API from Asaas — 4 operation(s) for conta escrow.
  name: Asaas Conta Escrow API
  slug: asaas-conta-escrow-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Documentos de cobranças API from Asaas — 2 operation(s) for documentos de cobranças.
  name: Asaas Documentos de cobranças API
  slug: asaas-documentos-de-cobran-as-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Envio de documentos White Label API from Asaas — 3 operation(s) for envio de documentos white label.
  name: Asaas Envio de documentos White Label API
  slug: asaas-envio-de-documentos-white-label-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Estornos API from Asaas — 2 operation(s) for estornos.
  name: Asaas Estornos API
  slug: asaas-estornos-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Extrato API from Asaas — 1 operation(s) for extrato.
  name: Asaas Extrato API
  slug: asaas-extrato-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Informações e personalização da conta API from Asaas — 7 operation(s) for informações e personalização da conta.
  name: Asaas Informações e personalização da conta API
  slug: asaas-informa-es-e-personaliza-o-da-conta-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Informações financeiras API from Asaas — 3 operation(s) for informações financeiras.
  name: Asaas Informações financeiras API
  slug: asaas-informa-es-financeiras-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Informações fiscais API from Asaas — 9 operation(s) for informações fiscais.
  name: Asaas Informações fiscais API
  slug: asaas-informa-es-fiscais-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Installment API from Asaas — 2 operation(s) for installment.
  name: Asaas Installment API
  slug: asaas-installment-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Link de pagamentos API from Asaas — 6 operation(s) for link de pagamentos.
  name: Asaas Link de pagamentos API
  slug: asaas-link-de-pagamentos-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Negativações API from Asaas — 8 operation(s) for negativações.
  name: Asaas Negativações API
  slug: asaas-negativa-es-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Notas fiscais API from Asaas — 4 operation(s) for notas fiscais.
  name: Asaas Notas fiscais API
  slug: asaas-notas-fiscais-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Notificações API from Asaas — 2 operation(s) for notificações.
  name: Asaas Notificações API
  slug: asaas-notifica-es-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Pagamento de contas API from Asaas — 4 operation(s) for pagamento de contas.
  name: Asaas Pagamento de contas API
  slug: asaas-pagamento-de-contas-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Parcelamentos API from Asaas — 6 operation(s) for parcelamentos.
  name: Asaas Parcelamentos API
  slug: asaas-parcelamentos-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Pix API from Asaas — 6 operation(s) for pix.
  name: Asaas Pix API
  slug: asaas-pix-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Pix Automático API from Asaas — 5 operation(s) for pix automático.
  name: Asaas Pix Automático API
  slug: asaas-pix-autom-tico-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Pix Recorrente API from Asaas — 5 operation(s) for pix recorrente.
  name: Asaas Pix Recorrente API
  slug: asaas-pix-recorrente-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Recargas de celular API from Asaas — 4 operation(s) for recargas de celular.
  name: Asaas Recargas de celular API
  slug: asaas-recargas-de-celular-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Registro de Recebíveis API from Asaas — 1 operation(s) for registro de recebíveis.
  name: Asaas Registro de Recebíveis API
  slug: asaas-registro-de-receb-veis-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Splits API from Asaas — 4 operation(s) for splits.
  name: Asaas Splits API
  slug: asaas-splits-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Subcontas Asaas API from Asaas — 5 operation(s) for subcontas asaas.
  name: Asaas Subcontas Asaas API
  slug: asaas-subcontas-asaas-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Transações Pix API from Asaas — 5 operation(s) for transações pix.
  name: Asaas Transações Pix API
  slug: asaas-transa-es-pix-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Transfer API from Asaas — 1 operation(s) for transfer.
  name: Asaas Transfer API
  slug: asaas-transfer-api
- baseURL: https://api.asaas.com/v3
  baseurl_source: declared
  description: The Transferências API from Asaas — 3 operation(s) for transferências.
  name: Asaas Transferências API
  slug: asaas-transfer-ncias-api
artifact_total: 94
asyncapis:
- description: ''
  name: Asaas Webhooks
  slug: asaas-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/asaas/well-known/asaas-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/asaas-status-security.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://materiais.asaas.com/developers
- group: other
  href: https://artifacts.apis.io/asaas/capabilities/asaas-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/asaas-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/asaas/agentic-access/asaas-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/asaas-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/asaas/rules/asaas-rules.yml
  title: ''
  type: Spectral
  url: rules/asaas-rules.yml
- group: design
  href: https://artifacts.apis.io/asaas/json-ld/asaas-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/asaas-context.jsonld
- group: design
  href: https://artifacts.apis.io/asaas/vocabulary/asaas-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/asaas-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/asaas/asyncapi/asaas-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/asaas-webhooks.yml
- group: design
  href: https://artifacts.apis.io/asaas/data-model/asaas-data-model.yml
  title: ''
  type: DataModel
  url: data-model/asaas-data-model.yml
- group: design
  href: https://artifacts.apis.io/asaas/errors/asaas-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/asaas-problem-types.yml
- group: design
  href: https://artifacts.apis.io/asaas/conformance/asaas-conformance.yml
  title: ''
  type: Conformance
  url: conformance/asaas-conformance.yml
- group: agent
  href: https://artifacts.apis.io/asaas/llms/asaas-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asaas-llms.txt
- group: agent
  href: https://artifacts.apis.io/asaas/mcp/asaas-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/asaas-mcp.yml
- group: agent
  href: https://artifacts.apis.io/asaas/well-known/asaas-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/asaas-well-known.yml
- group: other
  href: https://artifacts.apis.io/asaas/hosts/asaas-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asaas-hosts.yml
- group: build
  href: https://artifacts.apis.io/asaas/integrations/asaas-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/asaas-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/asaas/vendors/asaas-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asaas-vendors.yml
- group: build
  href: https://artifacts.apis.io/asaas/packages/asaas-packages.yml
  title: ''
  type: SDKs
  url: packages/asaas-packages.yml
- group: build
  href: https://artifacts.apis.io/asaas/packages/asaas-packages.yml
  title: ''
  type: Packages
  url: packages/asaas-packages.yml
- group: start
  title: ''
  type: Login
  url: https://www.asaas.com/login/auth?customerSignUpOriginChannel=HOME
- group: auth
  href: https://artifacts.apis.io/asaas/authentication/asaas-authentication.yml
  title: ''
  type: Authentication
  url: authentication/asaas-authentication.yml
- group: auth
  href: https://artifacts.apis.io/asaas/security/asaas-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asaas-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.asaas.com/
- group: start
  title: ''
  type: Signup
  url: https://www.asaas.com/cadastro
- group: docs
  title: ''
  type: Documentation
  url: https://docs.asaas.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.asaas.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.asaas.com/docs/visao-geral
- group: auth
  title: ''
  type: Authentication
  url: https://docs.asaas.com/docs/autenticacao-no-asaas
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.asaas.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.asaas.com/changelog
- group: other
  title: ''
  type: BreakingChanges
  url: https://docs.asaas.com/docs/breaking-changes
- group: operate
  title: ''
  type: StatusPage
  url: https://status.asaas.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.asaas.com/precos
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.asaas.com/termos-de-uso
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.asaas.com/politica-de-privacidade
- group: operate
  title: ''
  type: Support
  url: https://central.ajuda.asaas.com/hc/pt-br
- group: operate
  title: ''
  type: HelpCenter
  url: https://central.ajuda.asaas.com/hc/pt-br
- group: company
  title: ''
  type: Blog
  url: https://blog.asaas.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.asaas.com/llms.txt
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/asaas
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/asaas/
created: '2026-05-25'
description: Asaas is a Brazilian financial-services and payments platform headquartered in Joinville, SC. It operates as a Banco Central-authorized payment institution and simplified credit company (SCD), offering small and medium businesses a digital account ("Conta Asaas") combined with collection, billing, and receivables tooling. The Asaas API (v3) at api.asaas.com is a REST/JSON surface covering Customers, Charges (Cobranças), Subscriptions, Installments, Pix (including Pix Automático recurring), Boleto, Credit Card, Checkout sessions, Payment Links, Split Payments, Transfers, Bill Payments, Anticipation of Receivables, Subaccounts / White-label, Invoices (Nota Fiscal), Escrow, Chargeback handling, Webhooks, and supporting services like Serasa default reporting, cell-phone recharges, and SMS / WhatsApp / email notifications. A full sandbox at sandbox.asaas.com, an Atlassian-hosted status page, a Discord developer community, and an llms.txt-indexed documentation site round out the developer
  experience. Asaas does not publish a first-party SDK on a GitHub org; the ecosystem is served by third-party community SDKs in Node.js, PHP, Python, Go, and Ruby plus e-commerce plugins for WooCommerce, Magento, and Nuvemshop.
features:
- description: Free monthly Conta Asaas with Mastercard debit card and unlimited internal transfers, positioned as a banking layer for SMBs.
  name: Digital Account
- description: Recurring authorized Pix debits for subscription-style billing in BRL, publicly released January 2026 alongside webhook support.
  name: Pix Automático
- description: Native marketplace splitting that distributes settled funds across multiple wallet IDs per charge.
  name: Split Payments
- description: On-demand or automatic anticipation of boleto, card, and Pix receivables against a discount fee.
  name: Anticipation of Receivables
- description: Create and KYC subaccounts via API for white-label and BaaS platforms; each subaccount has its own API key.
  name: White-Label Subaccounts
- description: Built-in notification engine over SMS, email, WhatsApp, and voice bot to chase overdue invoices; Asaas advertises ~80% default reduction.
  name: Automated Dunning
- description: Funds-in-guarantee accounts release on API-driven conditions for marketplace buyer protection.
  name: Escrow Accounts
- description: Schedule and issue Brazilian municipal NFS-e tied to a charge or subscription with tax-retention configuration.
  name: NFS-e Issuance
- description: Optional default reporting and credit-score lookups via Serasa tied to customer records.
  name: Serasa Reporting
- description: Full-feature sandbox.asaas.com environment for end-to-end integration testing before production.
  name: Sandbox
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/asaas.png
integrations:
- description: Official Asaas plugin for WordPress / WooCommerce stores.
  name: WooCommerce
- description: Asaas extension for Magento 2 storefronts.
  name: Magento
- description: Native Asaas integration for Nuvemshop / Tiendanube Brazilian merchants.
  name: Nuvemshop
- description: No-code automation marketplace with Asaas triggers and actions for connecting to hundreds of SaaS tools.
  name: Pluga
- description: Community Zapier integrations bridge Asaas events to thousands of downstream apps.
  name: Zapier
json_schemas:
- name: PaymentGetResponseDTO
  property_count: 45
  slug: asaas-payment-get-response-dto
- name: PaymentLeanGetResponseDTO
  property_count: 34
  slug: asaas-payment-lean-get-response-dto
- name: PaymentLeanSaveWithCreditCardResponseDTO
  property_count: 35
  slug: asaas-payment-lean-save-with-credit-card-response-dto
- name: PaymentPixQrCodeResponseDTO
  property_count: 4
  slug: asaas-payment-pix-qr-code-response-dto
- name: WebhookConfigGetResponseDTO
  property_count: 11
  slug: asaas-webhook-config-get-response-dto
- name: WebhookConfigSaveRequestDTO
  property_count: 9
  slug: asaas-webhook-config-save-request-dto
jsonld:
- class_count: 120
  name: Asaas Context
  property_count: 184
  slug: asaas-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.asaas.com over HTTP.
  name: Asaas MCP Server
  slug: asaas
modified: '2026-05-25'
name: Asaas
nav: Providers
network: true
overview: 'Asaas publishes 57 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ações em sandbox API, Antecipações API, Anticipation API, and 54 more. Tagged areas include Payments, Billing, Subscription, Pix, and Boleto.


  The Asaas catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Asaas'' developer surface includes authentication, signup flow, documentation, API reference, getting-started guide, sandbox, changelog, and 34 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Asaas API Rules
  rule_count: 57
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 7
  slug: asaas-rules
score:
  band: developing
  composite: 44.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.7
  facets:
    access_clarity: 6.6
    contract_governance: 22.0
    contract_quality: 76.5
    developer_ergonomics: 53.6
    discoverability: 70.0
    operational_transparency: 42.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 43.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 37
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/asaas/asaas-2026-06-20T172451.png
security:
- kind: authentication
  name: Asaas Authentication
  slug: asaas-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Asaas Domain Security
  slug: asaas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: asaas
solutions:
- description: Free Brazilian digital account with debit card targeted at MEIs and SMBs.
  name: Conta Asaas (Digital Account)
- description: The core billing product covering boleto, Pix, and card via a single API and UI.
  name: Cobranças (Charges)
- description: Subaccount-based product for partners building branded payments experiences on top of Asaas.
  name: Whitelabel / BaaS
- description: Checkout / payment-link product for accepting payments without a full integration.
  name: Asaas Pay
tags:
- Payments
- Billing
- Subscription
- Pix
- Boleto
- Credit Cards
- Checkout
- Split Payments
- Webhook
- Digital Account
- Receivables
- Invoicing
- Brazil
- Fintech
- Small Business
use_cases:
- description: Subscriptions API plus Pix Automático, boleto, or card to bill Brazilian SaaS customers in BRL with automated dunning.
  name: Recurring SaaS Billing
- description: Split Payments + Subaccounts + Escrow let marketplaces collect, hold, and disburse to sellers natively in BRL.
  name: Marketplace Settlement
- description: Service businesses (clinics, schools, gyms) automate billing, NFS-e issuance, and overdue-payment chasing via the Asaas dunning engine.
  name: Service-Business Collections
- description: ISVs embed Asaas under their brand using Subaccounts, KYC, and per-account API keys to ship a payments product without a banking stack.
  name: White-Label / BaaS
- description: Checkout sessions and payment links plug into custom storefronts and supported plugins for one-click Pix / boleto / card.
  name: E-commerce Checkout
website: https://www.asaas.com/
---
