---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 65.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Faturapdf Brazilian Invoice Receipt Pdf Api Agentic Access
  operation_count: 3
  slug: faturapdf-brazilian-invoice-receipt-pdf-api-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- description: Geração de fatura/recibo em PDF
  name: FaturaPDF — Brazilian Invoice & Receipt PDF API Documents API
  slug: faturapdf-brazilian-invoice-receipt-pdf-api-documents-api
artifact_total: 10
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://faturapdf.com/
- group: docs
  title: ''
  type: Documentation
  url: https://faturapdf.com/guides/
- group: docs
  title: ''
  type: APIReference
  url: https://faturapdf.com/openapi.yaml
- group: start
  title: ''
  type: GettingStarted
  url: https://faturapdf.com/guides/generate-invoice-pdf-nodejs/
- group: operate
  title: ''
  type: Support
  url: https://rapidapi.com/leosanchees2014/api/brazilian-invoice-receipt-pdf-api-cpf-cnpj
- group: commercial
  title: ''
  type: Pricing
  url: https://faturapdf.com/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://rapidapi.com/leosanchees2014/api/brazilian-invoice-receipt-pdf-api-cpf-cnpj
- group: commercial
  title: ''
  type: TermsOfService
  url: https://faturapdf.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://faturapdf.com/terms/#what-happens-to-the-data-you-send
- group: operate
  title: ''
  type: StatusPage
  url: https://faturapdf.com/health
- group: auth
  title: ''
  type: Security
  url: https://faturapdf.com/.well-known/security.txt
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/faturapdf-brazilian-invoice-receipt-pdf-api-openapi-original.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/faturapdf-brazilian-invoice-receipt-pdf-api-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/faturapdf-brazilian-invoice-receipt-pdf-api-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/faturapdf-brazilian-invoice-receipt-pdf-api-security.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/faturapdf-brazilian-invoice-receipt-pdf-api-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/faturapdf-brazilian-invoice-receipt-pdf-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/faturapdf-brazilian-invoice-receipt-pdf-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/faturapdf-brazilian-invoice-receipt-pdf-api-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/faturapdf-brazilian-invoice-receipt-pdf-api-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/faturapdf-brazilian-invoice-receipt-pdf-api-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/faturapdf-brazilian-invoice-receipt-pdf-api-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/faturapdf-brazilian-invoice-receipt-pdf-api-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/faturapdf-brazilian-invoice-receipt-pdf-api-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/faturapdf-brazilian-invoice-receipt-pdf-api-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/faturapdf-brazilian-invoice-receipt-pdf-api-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/faturapdf-brazilian-invoice-receipt-pdf-api-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/faturapdf-brazilian-invoice-receipt-pdf-api-openapi-overlay.yaml
- group: build
  title: ''
  type: Examples
  url: examples/faturapdf-brazilian-invoice-receipt-pdf-api-generate-invoice-example.json
- group: commercial
  title: ''
  type: Plans
  url: plans/faturapdf-brazilian-invoice-receipt-pdf-api-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/faturapdf-brazilian-invoice-receipt-pdf-api-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-07'
description: 'HTTP API that converts a JSON payload into a Brazilian invoice (fatura) or receipt (recibo) PDF. Fiscal-native features include mod-11 checksum-validated CPF/CNPJ, BRL formatting (R$ 1.234,56 computed in integer cents), DD/MM/AAAA dates, the total spelled out in Portuguese, and optional rendering of a caller-supplied PIX BR Code as a scannable QR. Rendered with a pure-JS engine (pdf-lib), no headless browser. Explicitly NOT an NF-e/NFS-e fiscal issuer — it produces a formatted commercial document, not a tax-authority-authorized record. Consumed through the RapidAPI gateway (the origin host is not directly callable) and metered per document, with a free tier of 20 documents a month and no credit card. The provider also publishes free, keyless, client-side tools: an invoice/receipt generator, a CPF/CNPJ generator-validator and a PIX BR Code builder, two of them embeddable as iframes.'
examples:
- key_count: 8
  name: Faturapdf Brazilian Invoice Receipt Pdf Api Error Example
  slug: faturapdf-brazilian-invoice-receipt-pdf-api-error-example
- key_count: 7
  name: Faturapdf Brazilian Invoice Receipt Pdf Api Generate Invoice Example
  slug: faturapdf-brazilian-invoice-receipt-pdf-api-generate-invoice-example
- key_count: 7
  name: Faturapdf Brazilian Invoice Receipt Pdf Api Generate Receipt Example
  slug: faturapdf-brazilian-invoice-receipt-pdf-api-generate-receipt-example
image: https://faturapdf.com/og-cover.png
layout: provider
modified: '2026-08-09'
name: FaturaPDF — Brazilian Invoice & Receipt PDF API
nav: Providers
network: true
overview: 'FaturaPDF — Brazilian Invoice & Receipt PDF API publishes 1 API on the [APIs.io](https://apis.io/) network: Documents API. Tagged areas include Invoices, Receipts, PDF Generation, Documents, and Brazil.


  FaturaPDF — Brazilian Invoice & Receipt PDF API''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 25 more developer resources.'
plans:
- name: Faturapdf Brazilian Invoice Receipt Pdf Api Plans
  plan_count: 4
  slug: faturapdf-brazilian-invoice-receipt-pdf-api-plans
random_paper: 87
rate_limits:
- limit_count: 7
  name: Faturapdf Brazilian Invoice Receipt Pdf Api Rate Limits
  slug: faturapdf-brazilian-invoice-receipt-pdf-api-rate-limits
score:
  band: strong
  composite: 61.7
  facets:
    commercial_clarity: 76.3
    contract_quality: 60.5
    developer_ergonomics: 63.0
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 57.9
  schema_version: 0.9.1
  scored_at: '2026-08-10'
security:
- kind: authentication
  name: Faturapdf Brazilian Invoice Receipt Pdf Api Authentication
  slug: faturapdf-brazilian-invoice-receipt-pdf-api-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Faturapdf Brazilian Invoice Receipt Pdf Api Domain Security
  slug: faturapdf-brazilian-invoice-receipt-pdf-api-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Faturapdf Brazilian Invoice Receipt Pdf Api Vulnerability Disclosure
  slug: faturapdf-brazilian-invoice-receipt-pdf-api-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: faturapdf-brazilian-invoice-receipt-pdf-api
tags:
- Invoices
- Receipts
- PDF Generation
- Documents
- Brazil
- Billing
- CPF Validation
- CNPJ Validation
- PIX
- Fintech
- Data Validation
website: https://faturapdf.com/
---
