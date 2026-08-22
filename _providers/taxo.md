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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: 'White-label REST API for electronic invoicing integrated with Ecuador''s SRI: issue invoices, credit notes and retentions as JSON, with OAuth 2.0 auth, asynchronous webhooks for authorization status, a'
  name: Taxo API (Ecuador)
  slug: taxo-api-ecuador
artifact_total: 5
asyncapis:
- description: ''
  name: Taxo Webhooks
  slug: taxo-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://taxo.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.taxo.ws
- group: docs
  title: ''
  type: Documentation
  url: https://docs.taxo.ws/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.taxo.ws
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.taxo.ws/getting-started
- group: company
  title: ''
  type: Blog
  url: https://taxo.co/ec/blog
- group: operate
  title: ''
  type: Support
  url: https://taxo.co/ec/ayuda
- group: start
  title: ''
  type: SignUp
  url: https://app.taxo.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://taxo.co/ec/terminos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://taxo.co/ec/privacidad
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/taxo-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/taxo-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/taxo-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/taxo-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/taxo-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/taxo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/taxo-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/taxo-domain-security.yml
created: '2026-07-17'
description: 'Taxo (Contadores del Futuro) is an AI-powered tax and accounting automation platform for accountants and firms (despachos) in Ecuador and Mexico, used by 2,000+ practices. It automates fiscal work across two regional hubs: Ecuador (integrated with the SRI) and Mexico (integrated with the SAT). Products include bulk invoice/CFDI download bots, AI-assisted tax declarations, electronic invoicing (facturación electrónica / CFDI 4.0 timbrado), invoicing by WhatsApp, batch and mass issuance, and white-label REST APIs (Taxo API, SRI API, SAT API) for embedding electronic invoicing and tax-authority queries into fintechs, e-commerce, ERPs and marketplaces. Backed by 500 Global.'
image: https://storage.googleapis.com/gpt-engineer-file-uploads/attachments/og-images/257114fb-6f8f-4ec9-b1ae-795da7ce8772
layout: provider
mcp_servers:
- description: ''
  name: taxo-mcp.yml
  slug: taxo-mcpyml
modified: '2026-07-21'
name: TAXO
nav: Providers
network: true
overview: 'TAXO publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Accounting, Tax, Fintech, and Electronic Invoicing.


  The TAXO catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TAXO''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 11 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 34.7
  delta: -6.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 50.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 40.7
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
security:
- kind: authentication
  name: Taxo Authentication
  slug: taxo-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Taxo Domain Security
  slug: taxo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: taxo
tags:
- Company
- Accounting
- Tax
- Fintech
- Electronic Invoicing
- Facturación Electrónica
- CFDI
- SRI
- SAT
- Artificial Intelligence
- Ecuador
- Mexico
- API
website: https://taxo.co
---
