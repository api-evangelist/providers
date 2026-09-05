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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-09-04'
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
random_paper: 1
scopes:
- name: Iniciador Scopes
  scope_count: 16
  slug: iniciador-scopes
  summary_line: 16 scopes · authorizationCode/clientCredentials
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 35.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: BR
      standard: lgpd
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 84.8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iniciador/refs/heads/main/screenshots/iniciador-2026-07-25T222443.png
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
- Authentication
- Financial-Services
website: https://iniciador.com.br
---
