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
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 16.3
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Iniciador's regulated Open Finance Brasil API surface for payment initiation and financial data sharing (accounts, credit cards, loans, financings, investments, exchanges, and more), authorized via FA
  name: Iniciador Open Finance API
  slug: iniciador-open-finance-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/iniciador-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://iniciador.com.br
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.iniciador.com.br
- group: docs
  title: ''
  type: Documentation
  url: https://docs.iniciador.com.br
- group: docs
  title: ''
  type: APIReference
  url: https://docs.iniciador.com.br
- group: start
  title: ''
  type: Login
  url: https://accounts.iniciador.com.br/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://iniciador.com.br/iniciador-politica-privacidade-termos.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://iniciador.com.br/iniciador-politica-privacidade-termos.pdf
- group: operate
  title: ''
  type: StatusPage
  url: https://status.iniciador.com.br
- group: auth
  title: ''
  type: Compliance
  url: security/iniciador-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://iniciador.com.br/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/iniciador-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/iniciador-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/iniciador-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/iniciador-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/iniciador-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/iniciador-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iniciador-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/iniciador-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/iniciador-llms.txt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iniciador1
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@IniciadorOF
created: '2026-07-17'
description: Iniciador is a Brazilian Open Finance infrastructure company that provides the regulated rails, APIs, and managed operations banks, payment institutions, fintechs, and platforms use to participate in Brazil's Open Finance ecosystem. It operates as a Payment Initiator (Iniciadora de Pagamentos), Data Receptor, Account Holder, and Data Transmitter, reportedly processing roughly one in three Pix initiations nationally and over a billion API data calls monthly. Its product surface spans Pague com Seu Banco, Pix Inteligente, Pix Biometria, Pix Automatico, Pix por Aproximacao, agentic payments, and data products such as real-time Dados Bancarios and Cadastro Expresso one-click onboarding. The platform is a FAPI / Open Finance Brasil OAuth2 + OpenID Connect provider using private_key_jwt client authentication, mTLS-bound access tokens, pushed authorization requests (PAR), and PS256 signed request objects.
image: https://iniciador.com.br/pt/opengraph-image
layout: provider
modified: '2026-07-19'
name: Iniciador
nav: Providers
network: true
overview: 'Iniciador publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Open Finance, Open Banking, and Payments.


  Iniciador''s developer surface includes documentation, API reference, authentication, YouTube channel, and 18 more developer resources.'
random_paper: 28
scopes:
- name: Iniciador Scopes
  scope_count: 16
  slug: iniciador-scopes
  summary_line: 16 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 40.2
  delta: 10.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 29.6
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 100.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: rising
security:
- kind: authentication
  name: Iniciador Authentication
  slug: iniciador-authentication
  summary_line: oauth2/openIdConnect/mutualTLS · 3 schemes
- kind: domain-security
  name: Iniciador Domain Security
  slug: iniciador-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Iniciador Vulnerability Disclosure
  slug: iniciador-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Iniciador Trust Center
  slug: iniciador-trust-center
  summary_line: SOC 2
slug: iniciador
tags:
- Company
- Fintech
- Open Finance
- Open Banking
- Payments
- Pix
- Brazil
- FAPI
- OAuth
- Financial Services
website: https://iniciador.com.br
---
