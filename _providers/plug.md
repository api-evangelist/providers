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
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: documented
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 57.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 46
  human_in_the_loop: 0
  name: Plug Agentic Access
  operation_count: 84
  slug: plug-agentic-access
  summary_line: 84 operations · 46 acting
api_count: 19
apis:
- description: GraphQL API for querying processed payment data (charges, cards, authorization rates).
  name: Malga Analytics API
  slug: malga-analytics-api
- description: The 3DS2 Malga API from Malga — 1 operation(s) for 3ds2 malga.
  name: Malga 3DS2 Malga API
  slug: plug-3ds2-malga-api
- description: '**Dados básicos de um objeto cartão** <SchemaDefinition schemaRef="#/components/schemas/Card" />'
  name: Malga Cards API
  slug: plug-cards-api
- description: Para realizar uma cobrança deve criar um objeto `charge`. É possível recuperar detalhes de transações individuais ou listar todas as cobranças realizadas em um determinado `merchant`. Os `charges` são
  name: Malga Charges API
  slug: plug-charges-api
- description: É possível criar chaves públicas de acesso temporária a API com escopo e tempo de expiração limitados. Recomendamos o uso deste tipo de chave quando você tiver que expor a chave em uma aplicação clien
  name: Malga Client-token API
  slug: plug-client-token-api
- description: Através da API de `customers` é possível realizar a criação, edição, listagem e exclusão de dados de compradores para uso nos serviços de tokenização de cartões, cobrança por PIX, Boleto, uso em análi
  name: Malga Customers API
  slug: plug-customers-api
- description: Através da API de `flows` é possível recuperar detalhes de um Fluxo ou listar todas os Fluxos cadastrados em determinado `clientId`. Os fluxos inteligentes são um recurso disponibilizado pela Malga pa
  name: Malga Flows API
  slug: plug-flows-api
- description: Através das APIs de `merchants` é possível realizar a criação e configuração de sub contas na Malga. Uma sub conta, ou um `merchant`, é um cadastro de estabelecimento comercial que você tenha junto há
  name: Malga Merchants API
  slug: plug-merchants-api
- description: 'Através das APIs de `payouts` é possível consultar o saldo disponível, listar repasses e visualizar as ordens de pagamento liquidadas para um cliente. Esses endpoints são read-only e atendem a fluxos '
  name: Malga Payouts API
  slug: plug-payouts-api
- description: '> **🚧 Beta** — esta API está em fase Beta. Já está disponível para clientes habilitados, mas detalhes do contrato e do fluxo podem evoluir nas próximas versões. **Antecipação avulsa de recebíveis.** P'
  name: Malga Prepayment API
  slug: plug-prepayment-api
- description: Através das APIs de Providers você pode realizar a edição e atualização dos provedores vinculados a um merchant já cadastrado na Malga. Essas operações permitem que você mantenha seus dados sempre atu
  name: Malga Providers API
  slug: plug-providers-api
- description: The Seller Documents API from Malga — 2 operation(s) for seller documents.
  name: Malga Seller Documents API
  slug: plug-seller-documents-api
- description: Para realizar uma cobrança com Split, antes é necessário criar um `seller`. Os `sellers` são identificados a partir de um id único. Através das APIs de `sellers` é possível realizar a criação e config
  name: Malga Sellers API
  slug: plug-sellers-api
- description: 'Através da API de sessões é possível criar um pedido, composto por itens, métodos de pagamento e outros atributos, que pode ser pago através de um endpoint ou integrado ao MalgaCheckout. # Fluxo de cr'
  name: Malga Sessions API
  slug: plug-sessions-api
- description: Através da API de `settings` é possível recuperar, criar e atualizar configurações de personalização de link de pagamento de um determinado `clientId`. É possível também configurar branding específico
  name: Malga Settings API
  slug: plug-settings-api
- description: Através da API de `subscriptions` é possível realizar a criação, edição, listagem e exclusão de assinaturas. **Dados básicos de um objeto do tipo subscription** <SchemaDefinition schemaRef="#/componen
  name: Malga Subscriptions API
  slug: plug-subscriptions-api
- description: '**Dados básicos de uma requisição de criação de card token** <SchemaDefinition schemaRef="#/components/schemas/TokenRequest" />'
  name: Malga Tokens API
  slug: plug-tokens-api
- description: The Vendors API from Malga — 2 operation(s) for vendors.
  name: Malga Vendors API
  slug: plug-vendors-api
- description: A Malga utiliza o serviço de webhooks para notificar o seu sistema sobre os eventos ocorridos na nossa plataforma. Através de webhooks você consegue atualizar seu sistema sempre que um evento importan
  name: Malga Webhooks API
  slug: plug-webhooks-api
artifact_total: 24
asyncapis:
- description: ''
  name: Plug Webhooks
  slug: plug-webhooks
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
  url: openapi/plug-openapi-original.yml
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
  type: MCPServer
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
mcp_servers:
- description: ''
  name: plug-mcp.yml
  slug: plug-mcpyml
modified: '2026-07-20'
name: Malga
nav: Providers
network: true
overview: 'Malga publishes 18 APIs on the [APIs.io](https://apis.io/) network, including 3DS2 Malga API, Cards API, Charges API, and 15 more. Tagged areas include Company, Payments, Payment Orchestration, Payment Gateway, and Fintech.


  The Malga catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Malga''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, changelog, authentication, and 29 more developer resources.'
random_paper: 35
score:
  band: developing
  composite: 51.9
  delta: -1.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 65.2
    developer_ergonomics: 71.2
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 52.6
  previous_composite: 52.9
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
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
- Subscriptions
- Brazil
website: https://malga.io/
---
