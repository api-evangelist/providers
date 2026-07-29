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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 22.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Contalink Agentic Access
  operation_count: 13
  slug: contalink-agentic-access
  summary_line: 13 operations · 7 acting
api_count: 8
apis:
- description: Obtiene la balanza de comprobación según los parámetros enviados
  name: Contalink Balanza de comprobación API
  slug: contalink-balanza-de-comprobaci-n-api
- description: Carga un documento fiscal al sistema
  name: Contalink Cargar un documento fiscal API
  slug: contalink-cargar-un-documento-fiscal-api
- description: Realiza la conciliación por medio del UUID de la factura proporcionada.
  name: Contalink Conciliación API
  slug: contalink-conciliaci-n-api
- description: Obtiene un listado de los documentos fiscales que correspondan a los filtros enviados
  name: Contalink Listado de documentos fiscales API
  slug: contalink-listado-de-documentos-fiscales-api
- description: Gestiona altas y bajas de los movimientos que se dan en los bancos, tarjetas, cajas, etc.
  name: Contalink Movimientos bancarios API
  slug: contalink-movimientos-bancarios-api
- description: Gestiona altas, bajas y cambios de las pólizas manuales.
  name: Contalink Pólizas manuales API
  slug: contalink-p-lizas-manuales-api
- description: Obtiene el saldo de una cuenta contable
  name: Contalink Saldo de una cuenta API
  slug: contalink-saldo-de-una-cuenta-api
- description: Valida los status de vigencia y pago de un documento fiscal
  name: Contalink Status de documentos fiscales API
  slug: contalink-status-de-documentos-fiscales-api
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://contalink.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.contalink.com
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.contalink.com
- group: docs
  title: ''
  type: Documentation
  url: https://tutoriales.contalink.com/es/
- group: start
  title: ''
  type: GettingStarted
  url: https://tutoriales.contalink.com/es/articles/8569647-configuracion-api
- group: operate
  title: ''
  type: Support
  url: https://tutoriales.contalink.com/es/
- group: company
  title: ''
  type: Blog
  url: https://www.contalink.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.contalink.com/precios
- group: start
  title: ''
  type: SignUp
  url: https://contalink.com/empezarahora
- group: start
  title: ''
  type: Login
  url: https://app.contalink.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contalink.com/terms-conditions
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Contalink
- group: operate
  title: ''
  type: StatusPage
  url: https://estatus.contalink.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/contalink-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/contalink-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/contalink-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/contalink-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/contalink-agentic-access.yml
created: '2026-07-17'
description: 'Contalink is a Mexican cloud accounting and payroll platform ("contabilidad en la nube") built for independent accountants, accounting firms (despachos) and SMEs. It automates repetitive Mexican fiscal work — bulk CFDI download and classification, electronic accounting, DIOT preparation, treasury and bank reconciliation, invoicing (facturación) and payroll (nómina) with digital stamping — across multiple companies and users. Contalink also exposes a REST API that lets external systems read and post accounting data: trial balance (balanza de comprobación), account balances, manual accounting policies (pólizas manuales), invoice reconciliation (conciliación), bank transactions (movimientos bancarios) and CFDI fiscal-document listing, upload and status checks. The API authenticates with a per-company API key sent in the Authorization header. Backed by 500 Global.'
image: https://www.contalink.com/favicon.ico
layout: provider
modified: '2026-07-18'
name: Contalink
nav: Providers
network: true
overview: 'Contalink publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Balanza de comprobación API, Cargar un documento fiscal API, Conciliación API, and 5 more. Tagged areas include Company, Accounting, Bookkeeping, Payroll, and Tax.


  Contalink''s developer surface includes API reference, documentation, getting-started guide, support, engineering blog, pricing, signup flow, and 11 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 41.0
  delta: 1.2
  facets:
    commercial_clarity: 34.2
    contract_quality: 50.0
    developer_ergonomics: 41.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/contalink/refs/heads/main/screenshots/contalink-2026-07-25T210322.png
security:
- kind: authentication
  name: Contalink Authentication
  slug: contalink-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Contalink Domain Security
  slug: contalink-domain-security
  summary_line: TLSv1.3 · DMARC
slug: contalink
tags:
- Company
- Accounting
- Bookkeeping
- Payroll
- Tax
- Fintech
- Invoicing
- CFDI
- Mexico
- SaaS
website: https://contalink.com
---
