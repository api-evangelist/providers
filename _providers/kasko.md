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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 34.6
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: REST API for the KASKO insurance platform. All platform functionality and data is accessible via the API, covering the Quote, Offer, Payment and Policy insurance transaction flow plus a Data API for d
  name: KASKO REST API
  slug: kasko-rest-api
artifact_total: 5
asyncapis:
- description: ''
  name: Kasko Webhooks
  slug: kasko-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.kasko.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.kasko.io/kasko-api-documentation/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kasko.io/kasko-api-documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kasko.io/kasko-api-documentation/rest-api/introduction.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kasko.io/kasko-api-documentation/rest-api/getting-started.md
- group: company
  title: ''
  type: Blog
  url: https://www.kasko.io/insights
- group: operate
  title: ''
  type: Support
  url: https://www.kasko.io/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.kasko.io/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.kasko.io/privacy-notice
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kasko-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kasko-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kasko-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kasko-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kasko-problem-types.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/kasko-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/kasko-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kasko-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kasko-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.kasko.io
- group: design
  title: ''
  type: DataModel
  url: data-model/kasko-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kasko-domain-security.yml
created: '2026-07-17'
description: KASKO is an InsurTech-as-a-Service provider offering a modular, no-/low-code platform that helps insurers, MGAs, reinsurers, and brokers design, launch, and operate digital insurance products end to end. Its full insurance operating stack exposes platform functionality and data through a REST API (Quote, Offer, Payment, Policy and Data resources), an embeddable KASKO JS widget for front-end distribution, and account-level signed webhooks. KASKO also provides EU/UK market-access and licensing support, advisory, and recruitment services, and is ISO 27001 certified and co-funded by the European Union.
image: https://static.wixstatic.com/media/660ad6_7730ccc446d245348dc0376d978ac52f~mv2.png
layout: provider
mcp_servers:
- description: ''
  name: KASKO Site MCP (Wix) manifest
  slug: kasko-site-mcp-wix-manifest
modified: '2026-07-19'
name: Kasko
nav: Providers
network: true
overview: 'Kasko publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, InsurTech, Insurance API, and Policy Management.


  The Kasko catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kasko''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 14 more developer resources.'
random_paper: 61
score:
  band: thin
  composite: 39.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 22.6
    developer_ergonomics: 67.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 39.7
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kasko/refs/heads/main/screenshots/kasko-2026-07-25T223521.png
security:
- kind: authentication
  name: Kasko Authentication
  slug: kasko-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Kasko Domain Security
  slug: kasko-domain-security
  summary_line: TLSv1.3 · DMARC
slug: kasko
tags:
- Company
- Insurance
- InsurTech
- Insurance API
- Policy Management
- Payments
- Webhooks
- Embedded Insurance
- No-Code
website: https://www.kasko.io
---
