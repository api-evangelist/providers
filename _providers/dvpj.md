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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: 'REST/JSON API for the Conta Azul ERP, organized by functional area (Financeiro, Cobranças, Baixas, Vendas, Pessoas, Produtos, Serviços, Notas Fiscais, Contratos), secured with OAuth 2.0 Authorization '
  name: Conta Azul API
  slug: conta-azul-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://contaazul.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.contaazul.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.contaazul.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developers.contaazul.com/aboutapis
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.contaazul.com/guide
- group: auth
  title: ''
  type: Authentication
  url: authentication/dvpj-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/dvpj-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dvpj-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dvpj-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dvpj-error-codes.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dvpj-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dvpj-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.contaazul.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.contaazul.com/migration
- group: design
  title: ''
  type: Conformance
  url: conformance/dvpj-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://contaazul.com/seguranca/
- group: design
  title: ''
  type: DataModel
  url: data-model/dvpj-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dvpj-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dvpj-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://ajuda.contaazul.com/hc/pt-br
- group: operate
  title: ''
  type: HelpCenter
  url: https://ajuda.contaazul.com/hc/pt-br
- group: company
  title: ''
  type: Blog
  url: https://contaazul.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/contaazul
- group: commercial
  title: ''
  type: Pricing
  url: https://contaazul.com/planos/
- group: start
  title: ''
  type: SignUp
  url: https://contaazul.com/cadastro/
- group: start
  title: ''
  type: Login
  url: https://auth.contaazul.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contaazul.com/termos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contaazul.com/termos/privacidade/
created: '2026-07-17'
description: Conta Azul is a Brazilian financial-management and ERP platform for small and medium-sized businesses, providing cash-flow control, bank reconciliation, electronic invoicing (NF-e/NFS-e/NFC-e), sales and customer management, automatic collections, inventory, supplier management and recurring contracts. Its developer platform exposes REST/JSON APIs (api-v2.contaazul.com) secured with OAuth 2.0 (AWS Cognito, Authorization Code flow) covering Financeiro, Cobranças, Baixas, Vendas, Pessoas/Fornecedores, Produtos e Serviços, Notas Fiscais and Contratos, so partner systems (BI, CRM, e-commerce) can integrate with the ERP. Surfaced to the API Evangelist network from a 500 Global portfolio stub (originally mislabeled "DVPJ") and enriched here.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dvpj.png
layout: provider
modified: '2026-07-18'
name: Conta Azul
nav: Providers
network: true
overview: 'Conta Azul publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, ERP, Financial, Accounting, and Invoicing.


  Conta Azul''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, engineering blog, and 21 more developer resources.'
random_paper: 28
rate_limits:
- limit_count: 0
  name: Dvpj Rate Limits
  slug: dvpj-rate-limits
scopes:
- name: Dvpj Scopes
  scope_count: 3
  slug: dvpj-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 43.7
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 43.7
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 87.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dvpj/refs/heads/main/screenshots/dvpj-2026-07-25T212538.png
security:
- kind: authentication
  name: Dvpj Authentication
  slug: dvpj-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Dvpj Domain Security
  slug: dvpj-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: dvpj
tags:
- Company
- ERP
- Financial
- Accounting
- Invoicing
- Payments
- SMB
- Brazil
- OAuth
website: https://contaazul.com
---
