---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: REST API for the Koalaboox / Cegid Click & Finance invoicing and invoice-financing platform. Resource-oriented URLs, JSON-encoded requests and responses, standard HTTP status codes, and OAuth 2.0 auth
  name: Cegid Click & Finance API
  slug: cegid-click-finance-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/koalaboox-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://vdp.cegid.com/p/Policy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/koalaboox-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/koalaboox-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/koalaboox-well-known.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cegid.be/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cegid.be/
- group: company
  title: ''
  type: Website
  url: https://www.cegid.com/be/fr/produits/cegid-invoice-financing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/koalaboox
- group: commercial
  title: ''
  type: Pricing
  url: https://www.invoice-financing.cegid.com/v3/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.invoice-financing.cegid.com/v3/pricing
- group: start
  title: ''
  type: Login
  url: https://www.invoice-financing.cegid.com/v3/login
- group: operate
  title: ''
  type: Support
  url: https://www.cegid.com/fr/assistance-clients/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cegid.com/fr/mentions-legales/
- group: commercial
  title: ''
  type: Plans
  url: plans/koalaboox-plans.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/koalaboox-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/koalaboox-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/koalaboox-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/koalaboox-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/koalaboox-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/koalaboox-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/koalaboox-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/koalaboox-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/koalaboox-llms.txt
created: '2026-07-17'
description: Koalaboox is a Belgian cloud invoicing and cash-flow platform for small businesses, self-employed professionals and their accountants, now operating as Cegid Invoice & Financing — API brand Cegid Click & Finance — following its acquisition by Cegid. The platform covers sales invoicing, quotes, purchase-invoice management, recurring invoices, dynamic dashboards, bank-account connections and Peppol-based electronic invoicing for the Belgian 2026 e-invoicing mandate, sold in Belgium and Spain. Alongside the SaaS it offers invoice financing — cash advances against outstanding invoices — underwritten by Cegid Fin Belgium. Koalaboox exposes a public REST API at connect.koalaboox.com secured with OAuth 2.0 authorization-code grants, documented on a Stoplight developer portal, with a first-party Laravel reference architecture published on GitHub.
image: https://raw.githubusercontent.com/koalaboox/static/main/CEGID_Logo_Bleu.png
layout: provider
mcp_servers:
- description: ''
  name: koalaboox-mcp.yml
  slug: koalaboox-mcpyml
modified: '2026-07-19'
name: Koalaboox
nav: Providers
network: true
overview: 'Koalaboox publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Invoicing, Electronic Invoicing, Peppol, and Accounting.


  Koalaboox''s developer surface includes documentation, pricing, signup flow, support, authentication, and 19 more developer resources.'
plans:
- name: Koalaboox Plans
  plan_count: 4
  slug: koalaboox-plans
random_paper: 32
score:
  band: thin
  composite: 32.4
  delta: 0.0
  facets:
    commercial_clarity: 65.8
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 15.8
  previous_composite: 32.4
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/koalaboox/refs/heads/main/screenshots/koalaboox-2026-07-25T224027.png
security:
- kind: authentication
  name: Koalaboox Authentication
  slug: koalaboox-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Koalaboox Domain Security
  slug: koalaboox-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Koalaboox Vulnerability Disclosure
  slug: koalaboox-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: koalaboox
tags:
- Company
- Invoicing
- Electronic Invoicing
- Peppol
- Accounting
- Invoice Financing
- Working Capital
- Small Business
- Fintech
- Belgium
- Spain
- OAuth
website: https://www.cegid.com/be/fr/produits/cegid-invoice-financing/
---
