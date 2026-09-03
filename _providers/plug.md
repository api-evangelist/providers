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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.2
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 46
  human_in_the_loop: 0
  name: Plug Agentic Access
  operation_count: 84
  slug: plug-agentic-access
  summary_line: 84 operations · 46 acting
api_count: 1
apis:
- description: GraphQL API for querying processed payment data (charges, cards, authorization rates).
  name: Malga Analytics API
  slug: malga-analytics-api
- baseURL: https://api.malga.io
  baseurl_source: declared
  description: The 3DS2 Malga API from Malga — 1 operation(s) for 3ds2 malga.
  name: Malga 3DS2 Malga API
  slug: plug-3ds2-malga-api
- baseURL: https://api.malga.io
  baseurl_source: declared
  description: '**Dados básicos de um objeto cartão** <SchemaDefinition schemaRef="#/components/schemas/Card" />'
  name: Malga Cards API
  slug: plug-cards-api
- baseURL: https://api.malga.io
  baseurl_source: declared
  description: Para realizar uma cobrança deve criar um objeto `charge`. É possível recuperar detalhes de transações individuais ou listar todas as cobranças realizadas em um determinado `merchant`. Os `charges` são
  name: Malga Charges API
  slug: plug-charges-api
- baseURL: https://api.malga.io
  baseurl_source: declared
  description: É possível criar chaves públicas de acesso temporária a API com escopo e tempo de expiração limitados. Recomendamos o uso deste tipo de chave quando você tiver que expor a chave em uma aplicação clien
  name: Malga Client-token API
  slug: plug-client-token-api
- baseURL: https://api.malga.io
  baseurl_source: declared
  description: Através da API de `customers` é possível realizar a criação, edição, listagem e exclusão de dados de compradores para uso nos serviços de tokenização de cartões, cobrança por PIX, Boleto, uso em análi
  name: Malga Customers API
  slug: plug-customers-api
- baseURL: https://api.malga.io
  baseurl_source: declared
  description: Através da API de `flows` é possível recuperar detalhes de um Fluxo ou listar todas os Fluxos cadastrados em determinado `clientId`. Os fluxos inteligentes são um recurso disponibilizado pela Malga pa
  name: Malga Flows API
  slug: plug-flows-api
- baseURL: https://api.malga.io
  baseurl_source: declared
  description: Através das APIs de `merchants` é possível realizar a criação e configuração de sub contas na Malga. Uma sub conta, ou um `merchant`, é um cadastro de estabelecimento comercial que você tenha junto há
  name: Malga Merchants API
  slug: plug-merchants-api
- baseURL: https://api.malga.io
  baseurl_source: declared
  description: 'Através das APIs de `payouts` é possível consultar o saldo disponível, listar repasses e visualizar as ordens de pagamento liquidadas para um cliente. Esses endpoints são read-only e atendem a fluxos '
  name: Malga Payouts API
  slug: plug-payouts-api
- baseURL: https://api.malga.io
  baseurl_source: declared
  description: '> **🚧 Beta** — esta API está em fase Beta. Já está disponível para clientes habilitados, mas detalhes do contrato e do fluxo podem evoluir nas próximas versões. **Antecipação avulsa de recebíveis.** P'
  name: Malga Prepayment API
  slug: plug-prepayment-api
- baseURL: https://api.malga.io
  baseurl_source: declared
  description: Através das APIs de Providers você pode realizar a edição e atualização dos provedores vinculados a um merchant já cadastrado na Malga. Essas operações permitem que você mantenha seus dados sempre atu
  name: Malga Providers API
  slug: plug-providers-api
- baseURL: https://api.malga.io
  baseurl_source: declared
  description: The Seller Documents API from Malga — 2 operation(s) for seller documents.
  name: Malga Seller Documents API
  slug: plug-seller-documents-api
- baseURL: https://api.malga.io
  baseurl_source: declared
  description: Para realizar uma cobrança com Split, antes é necessário criar um `seller`. Os `sellers` são identificados a partir de um id único. Através das APIs de `sellers` é possível realizar a criação e config
  name: Malga Sellers API
  slug: plug-sellers-api
- baseURL: https://api.malga.io
  baseurl_source: declared
  description: 'Através da API de sessões é possível criar um pedido, composto por itens, métodos de pagamento e outros atributos, que pode ser pago através de um endpoint ou integrado ao MalgaCheckout. # Fluxo de cr'
  name: Malga Sessions API
  slug: plug-sessions-api
- baseURL: https://api.malga.io
  baseurl_source: declared
  description: Através da API de `settings` é possível recuperar, criar e atualizar configurações de personalização de link de pagamento de um determinado `clientId`. É possível também configurar branding específico
  name: Malga Settings API
  slug: plug-settings-api
- baseURL: https://api.malga.io
  baseurl_source: declared
  description: Através da API de `subscriptions` é possível realizar a criação, edição, listagem e exclusão de assinaturas. **Dados básicos de um objeto do tipo subscription** <SchemaDefinition schemaRef="#/componen
  name: Malga Subscriptions API
  slug: plug-subscriptions-api
- baseURL: https://api.malga.io
  baseurl_source: declared
  description: '**Dados básicos de uma requisição de criação de card token** <SchemaDefinition schemaRef="#/components/schemas/TokenRequest" />'
  name: Malga Tokens API
  slug: plug-tokens-api
- baseURL: https://api.malga.io
  baseurl_source: declared
  description: The Vendors API from Malga — 2 operation(s) for vendors.
  name: Malga Vendors API
  slug: plug-vendors-api
- baseURL: https://api.malga.io
  baseurl_source: declared
  description: A Malga utiliza o serviço de webhooks para notificar o seu sistema sobre os eventos ocorridos na nossa plataforma. Através de webhooks você consegue atualizar seu sistema sempre que um evento importan
  name: Malga Webhooks API
  slug: plug-webhooks-api
artifact_total: 42
asyncapis:
- description: ''
  name: Plug Webhooks
  slug: plug-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Documentação Malga 3DS2 Malga API
  slug: open-plug-3ds2-malga-api
- collection_type: open
  name: Documentação Malga 3DS2 Malga Cards API
  slug: open-plug-cards-api
- collection_type: open
  name: Documentação Malga 3DS2 Malga Charges API
  slug: open-plug-charges-api
- collection_type: open
  name: Documentação Malga 3DS2 Malga Client-token API
  slug: open-plug-client-token-api
- collection_type: open
  name: Documentação Malga 3DS2 Malga Customers API
  slug: open-plug-customers-api
- collection_type: open
  name: Documentação Malga 3DS2 Malga Flows API
  slug: open-plug-flows-api
- collection_type: open
  name: Documentação Malga 3DS2 Malga Merchants API
  slug: open-plug-merchants-api
- collection_type: open
  name: Documentação Malga 3DS2 Malga Payouts API
  slug: open-plug-payouts-api
- collection_type: open
  name: Documentação Malga 3DS2 Malga Prepayment API
  slug: open-plug-prepayment-api
- collection_type: open
  name: Documentação Malga 3DS2 Malga Providers API
  slug: open-plug-providers-api
- collection_type: open
  name: Documentação Malga 3DS2 Malga Seller Documents API
  slug: open-plug-seller-documents-api
- collection_type: open
  name: Documentação Malga 3DS2 Malga Sellers API
  slug: open-plug-sellers-api
- collection_type: open
  name: Documentação Malga 3DS2 Malga Sessions API
  slug: open-plug-sessions-api
- collection_type: open
  name: Documentação Malga 3DS2 Malga Settings API
  slug: open-plug-settings-api
- collection_type: open
  name: Documentação Malga 3DS2 Malga Subscriptions API
  slug: open-plug-subscriptions-api
- collection_type: open
  name: Documentação Malga 3DS2 Malga Tokens API
  slug: open-plug-tokens-api
- collection_type: open
  name: Documentação Malga 3DS2 Malga Vendors API
  slug: open-plug-vendors-api
- collection_type: open
  name: Documentação Malga 3DS2 Malga Webhooks API
  slug: open-plug-webhooks-api
common:
- group: company
  title: ''
  type: Website
  url: https://malga.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.malga.io/documentations/welcome/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.malga.io/documentations/welcome/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.malga.io/api-reference/about-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.malga.io/documentations/welcome/introduction
- group: company
  title: ''
  type: Blog
  url: https://malga.io/blog/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.malga.io/
- group: start
  title: ''
  type: Login
  url: https://dashboard.malga.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.malga.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.malga.io/release-notes
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/plughacker
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/plug-openapi-original.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/plug-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/plug-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plug-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/plug-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/plug-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/plug-cli.yml
- group: design
  title: ''
  type: Components
  url: components/plug-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/plug-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/plug-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/plug-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/plug-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/plug-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/plug-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/plug-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/plug-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/plug-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/plug-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/plug-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/plug-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/plug-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/plug-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plug-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/plug-changelog.yml
created: '2026-07-17'
description: Malga (formerly Plug / plugpagamentos.com) is a Brazilian intelligent payment infrastructure and orchestration platform. It lets companies route transactions across multiple acquirers, payment providers, methods (card, Pix, boleto, wallets such as PicPay and Apple Pay) and anti-fraud engines from a single API, with smart routing/retry flows, tokenization, 3D Secure 2, subscriptions/recurrence, split payments, sellers/payouts and a GraphQL analytics API. Malga is PCI DSS Level 1 compliant and backed by Lightspeed Venture Partners and QED Investors.
image: https://malga.io/images/malga-announcement.webp
layout: provider
modified: '2026-07-20'
name: Malga
nav: Providers
network: true
overview: 'Malga publishes 18 APIs on the [APIs.io](https://apis.io/) network, including 3DS2 Malga API, Cards API, Charges API, and 15 more. Tagged areas include Company, Payments, Payment Orchestration, Payment Gateway, and Fintech.


  The Malga catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Malga''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, changelog, authentication, and 29 more developer resources.'
random_paper: 20
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 23
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 64.8
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 43.8
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plug/refs/heads/main/screenshots/plug-2026-08-17T081311.png
security:
- kind: authentication
  name: Plug Authentication
  slug: plug-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Plug Domain Security
  slug: plug-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: plug
tags:
- Company
- Payments
- Payment Orchestration
- Payment Gateway
- Fintech
- Pix
- Tokenization
- Subscription
- Brazil
website: https://malga.io/
---
