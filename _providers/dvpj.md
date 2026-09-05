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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 7.9
  scored_at: '2026-09-04'
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
random_paper: 16
rate_limits:
- limit_count: 2
  name: Dvpj Rate Limits
  slug: dvpj-rate-limits
scopes:
- name: Dvpj Scopes
  scope_count: 3
  slug: dvpj-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 44.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 63.2
  previous_composite: 44.4
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: BR
      standard: lgpd
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Authentication
website: https://contaazul.com
---
