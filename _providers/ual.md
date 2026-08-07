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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Ual Agentic Access
  operation_count: 5
  slug: ual-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 3
apis:
- description: The Authentication API from Ualá — 1 operation(s) for authentication.
  name: Ualá Authentication API
  slug: ual-authentication-api
- description: Payment orders (checkout)
  name: Ualá Orders API
  slug: ual-orders-api
- description: Refunds of approved orders
  name: Ualá Refunds API
  slug: ual-refunds-api
artifact_total: 8
asyncapis:
- description: ''
  name: Ual Webhooks
  slug: ual-webhooks
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ual-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://www.uala.com.ar/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.ualabis.com.ar/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.ualabis.com.ar/v2
- group: docs
  title: ''
  type: APIReference
  url: https://developers.ualabis.com.ar/v2
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.ualabis.com.ar/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Uala-Developers
- group: company
  title: ''
  type: Blog
  url: https://blog.uala.com.ar/
- group: operate
  title: ''
  type: Support
  url: https://www.uala.com.ar/preguntas-frecuentes
- group: commercial
  title: ''
  type: Pricing
  url: https://www.uala.com.ar/costos
- group: start
  title: ''
  type: Login
  url: https://web.ualabis.com.ar/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uala.com.ar/cgu
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uala.com.ar/privacidad
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ual-changelog.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ual-webhooks.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ual-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ual-conventions.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ual-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ual-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ual-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/ual-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ual-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ual-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ual-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ual-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/ual-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ual-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ual-domain-security.yml
created: '2026-07-17'
description: Ualá is a Latin American fintech founded in Argentina in 2017 by Pierpaolo Barbieri, offering a neobank super-app (prepaid and credit cards, savings, investments, loans, insurance) in Argentina and Mexico, where it operates as Ualá ABC through the acquired ABC Capital bank. Its merchant arm, Ualá Bis, provides payments acceptance — link de pago, POS, e-commerce plugins, and the API Cobros Online v2, a checkout API with hosted payment links, order retrieval and listing, refunds, and webhook status notifications, documented at developers.ualabis.com.ar with official Node.js and PHP SDKs.
image: https://developers.ualabis.com.ar/logo-large.png
layout: provider
mcp_servers:
- description: ''
  name: ual-mcp.yml
  slug: ual-mcpyml
modified: '2026-07-21'
name: Ualá
nav: Providers
network: true
overview: 'Ualá publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Orders API, and Refunds API. Tagged areas include Company, Fintech, Payments, Banking, and Neobank.


  The Ualá catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ualá''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, changelog, and 22 more developer resources.'
random_paper: 96
score:
  band: developing
  composite: 51.3
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 70.4
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 51.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Ual Authentication
  slug: ual-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ual Domain Security
  slug: ual-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ual
tags:
- Company
- Fintech
- Payments
- Banking
- Neobank
- Checkout
- Ecommerce
- Argentina
- Mexico
website: https://www.uala.com.ar/
---
