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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: 'Cora''s transactional banking API for Direct Integration: registered boleto and carnê (installment) issuance, Pix QR codes, account data, balance and statement queries, payment and transfer initiation '
  name: Cora API
  slug: cora-api
artifact_total: 4
asyncapis:
- description: ''
  name: Cora Webhooks
  slug: cora-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.cora.com.br/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cora.com.br/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cora.com.br/docs/instrucoes-iniciais
- group: docs
  title: ''
  type: APIReference
  url: https://developers.cora.com.br/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cora.com.br/docs/instrucoes-iniciais
- group: auth
  title: ''
  type: Authentication
  url: authentication/cora-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.cora.com.br/changelog/welcome-to-cora-api
- group: company
  title: ''
  type: Blog
  url: https://www.cora.com.br/blog/
- group: operate
  title: ''
  type: Support
  url: https://meajuda.cora.com.br/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cora.com.br/integracoes/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cora.com.br/termos-e-condicoes-de-apis/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cora.com.br/politica-de-privacidade/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/corabank/cora-s-public-workspace/documentation/ppi1okk/api-cora
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cora-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cora-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cora-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/cora-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/cora-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cora-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/cora-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cora-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cora-domain-security.yml
created: '2026-07-17'
description: Cora is a Brazilian digital bank (conta PJ) for small and medium businesses, offering fee-free business checking, Pix, boletos, transfers, payment initiation and financial management. Its developer platform exposes REST APIs for registered boleto and carnê issuance, Pix QR code generation, account data, balance and statement queries, payment and transfer initiation (including DARF and GPS tax payments), webhook notifications, and municipal service invoice (NFS-e) issuance. Cora offers two integration modalities — Direct Integration (mutual-TLS certificate plus OAuth2 client-credentials) and Cora Partnership — with a Stage sandbox for testing. Backed by QED Investors and Ribbit Capital.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cora.png
layout: provider
modified: '2026-07-18'
name: Cora
nav: Providers
network: true
overview: 'Cora publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Brazil, Payments, and Pix.


  The Cora catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cora''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, engineering blog, support, and 15 more developer resources.'
random_paper: 73
score:
  band: developing
  composite: 42.1
  delta: -2.1
  facets:
    commercial_clarity: 31.6
    contract_quality: 51.6
    developer_ergonomics: 63.0
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 23.7
  previous_composite: 44.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cora/refs/heads/main/screenshots/cora-2026-07-25T210413.png
security:
- kind: authentication
  name: Cora Authentication
  slug: cora-authentication
  summary_line: oauth2/mutualTLS · 2 schemes
- kind: domain-security
  name: Cora Domain Security
  slug: cora-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cora
tags:
- Company
- Banking
- Brazil
- Payments
- Pix
- Boleto
- Invoicing
- SMB
- Fintech
- Banking-as-a-Service
website: https://www.cora.com.br/
---
