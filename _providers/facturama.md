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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: REST API for generating, stamping, downloading, and cancelling CFDI 4.0 electronic invoices, payroll receipts, payment complements, and related Mexican tax documents, plus management of clients, produ
  name: Facturama API
  slug: facturama-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://facturama.mx
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apisandbox.facturama.mx/Docs
- group: docs
  title: ''
  type: Documentation
  url: https://apisandbox.facturama.mx/Docs
- group: docs
  title: ''
  type: APIReference
  url: https://apisandbox.facturama.mx/Docs
- group: start
  title: ''
  type: GettingStarted
  url: https://apisandbox.facturama.mx/guias
- group: operate
  title: ''
  type: Support
  url: https://soporte.facturama.mx/hc/es-mx
- group: company
  title: ''
  type: Blog
  url: https://facturama.mx/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Facturama
- group: commercial
  title: ''
  type: Pricing
  url: https://facturama.mx/api-facturacion-electronica
- group: start
  title: ''
  type: SignUp
  url: https://app.facturama.mx/web/registro
- group: start
  title: ''
  type: Login
  url: https://dev.facturama.mx/api/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cdnfacturama.azureedge.net/content/docs/Facturama-terminos-y-condiciones-del-servicio.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cdnfacturama.azureedge.net/content/docs/Aviso-De-Privacidad.pdf
- group: build
  title: ''
  type: Postman
  url: https://github.com/Facturama/facturama-postman-sdk
- group: build
  title: ''
  type: Packages
  url: packages/facturama-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/facturama-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/facturama-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/facturama-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/facturama-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/facturama-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/facturama-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/facturama-domain-security.yml
created: '2026-07-17'
description: 'Facturama is a cloud-based Mexican electronic invoicing (CFDI) platform that lets businesses generate, stamp, download, and cancel digital tax receipts (Comprobante Fiscal Digital por Internet) through a REST API. It serves 55,000+ clients — mostly SMEs and startups — and exposes two API products: API Web (single issuer, tied to a Facturama account) and API Multiemisor (multi-issuer, for platforms that invoice on behalf of many taxpayers). The API supports CFDI 4.0 invoices, payroll receipts (nómina), payment complements (complemento de pago), credit notes, Carta Porte (cargo/transport), foreign trade (comercio exterior), and donation receipts, plus management of clients, products/services, branch offices, series, and SAT catalogs (postal codes, currencies, payment methods, tax regimes). Authentication is HTTP Basic. A sandbox environment and 15 free test invoices during a 30-day trial are available, along with first-party SDKs for PHP, Java, .NET, Node.js, JavaScript, Python,
  and Ruby and a public Postman collection.'
image: https://facturama.mx/img/home/plataforma-facturama.webp
layout: provider
modified: '2026-07-19'
name: Facturama
nav: Providers
network: true
overview: 'Facturama publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Electronic Invoicing, CFDI, E-Invoicing, and Mexico.


  Facturama''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 15 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 33.3
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/facturama/refs/heads/main/screenshots/facturama-2026-07-25T214144.png
security:
- kind: authentication
  name: Facturama Authentication
  slug: facturama-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Facturama Domain Security
  slug: facturama-domain-security
  summary_line: TLSv1.3 · DMARC
slug: facturama
tags:
- Company
- Electronic Invoicing
- CFDI
- E-Invoicing
- Mexico
- Tax Compliance
- SAT
- Billing
- Payroll
- Finance
- REST API
website: https://facturama.mx
---
