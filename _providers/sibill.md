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
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 25
  human_in_the_loop: 25
  name: Sibill Agentic Access
  operation_count: 48
  slug: sibill-agentic-access
  summary_line: 48 operations · 25 acting · 25 human-in-the-loop
api_count: 12
apis:
- description: The Account API from Sibill — 2 operation(s) for account.
  name: Sibill Account API
  slug: sibill-account-api
- description: The Category API from Sibill — 2 operation(s) for category.
  name: Sibill Category API
  slug: sibill-category-api
- description: The Company API from Sibill — 1 operation(s) for company.
  name: Sibill Company API
  slug: sibill-company-api
- description: The Counterpart API from Sibill — 3 operation(s) for counterpart.
  name: Sibill Counterpart API
  slug: sibill-counterpart-api
- description: The Document API from Sibill — 5 operation(s) for document.
  name: Sibill Document API
  slug: sibill-document-api
- description: The DocumentSectional API from Sibill — 2 operation(s) for documentsectional.
  name: Sibill DocumentSectional API
  slug: sibill-documentsectional-api
- description: The Flow API from Sibill — 2 operation(s) for flow.
  name: Sibill Flow API
  slug: sibill-flow-api
- description: The Payment API from Sibill — 2 operation(s) for payment.
  name: Sibill Payment API
  slug: sibill-payment-api
- description: The Product API from Sibill — 2 operation(s) for product.
  name: Sibill Product API
  slug: sibill-product-api
- description: The Reconciliation API from Sibill — 2 operation(s) for reconciliation.
  name: Sibill Reconciliation API
  slug: sibill-reconciliation-api
- description: The Subcategory API from Sibill — 2 operation(s) for subcategory.
  name: Sibill Subcategory API
  slug: sibill-subcategory-api
- description: The Transaction API from Sibill — 2 operation(s) for transaction.
  name: Sibill Transaction API
  slug: sibill-transaction-api
artifact_total: 31
asyncapis:
- description: ''
  name: Sibill Webhooks
  slug: sibill-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sibill Integration Account API
  slug: open-sibill-account-api
- collection_type: open
  name: Sibill Integration Account Category API
  slug: open-sibill-category-api
- collection_type: open
  name: Sibill Integration Account Company API
  slug: open-sibill-company-api
- collection_type: open
  name: Sibill Integration Account Counterpart API
  slug: open-sibill-counterpart-api
- collection_type: open
  name: Sibill Integration Account Document API
  slug: open-sibill-document-api
- collection_type: open
  name: Sibill Integration Account DocumentSectional API
  slug: open-sibill-documentsectional-api
- collection_type: open
  name: Sibill Integration Account Flow API
  slug: open-sibill-flow-api
- collection_type: open
  name: Sibill Integration Account Payment API
  slug: open-sibill-payment-api
- collection_type: open
  name: Sibill Integration Account Product API
  slug: open-sibill-product-api
- collection_type: open
  name: Sibill Integration Account Reconciliation API
  slug: open-sibill-reconciliation-api
- collection_type: open
  name: Sibill Integration Account Subcategory API
  slug: open-sibill-subcategory-api
- collection_type: open
  name: Sibill Integration Account Transaction API
  slug: open-sibill-transaction-api
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.sibill.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sibill.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.sibill.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sibill.com/quickstarts/quickstarts-step-by-step
- group: operate
  title: ''
  type: Support
  url: https://docs.sibill.com/faqs
- group: company
  title: ''
  type: Blog
  url: https://sibill.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://sibill.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.sibill.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.sibill.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sibill.com/termini-e-condizioni/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.iubenda.com/privacy-policy/16454324
- group: auth
  title: ''
  type: Authentication
  url: authentication/sibill-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sibill-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sibill-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sibill-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sibill-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sibill-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sibill-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sibill-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sibill-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sibill-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sibill-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/sibill-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sibill-openapi-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sibill-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sibill-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sibill-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sibill-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://sibill.com/
created: '2026-07-17'
description: Sibill is an Italian fintech platform that centralizes financial and administrative management for small and medium-sized businesses (PMI). It unifies electronic invoicing (submitted to the Agenzia delle Entrate SDI), treasury and cash-flow monitoring, payments, business accounts and debit cards, and AI-assisted reconciliation of bank transactions against invoices and deadlines. The Sibill Integration API exposes companies, bank accounts, categories, counterparts, documents, payment flows, reconciliations, products and transactions over a REST interface secured with Bearer API keys, with cursor pagination, field expansion, and Document/Flow webhooks. Backed by Creandum.
image: https://sibill.com/wp-content/uploads/2025/10/monogramma_purple.jpg
layout: provider
mcp_servers:
- description: ''
  name: sibill-mcp.yml
  slug: sibill-mcpyml
modified: '2026-07-21'
name: Sibill
nav: Providers
network: true
overview: 'Sibill publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Account API, Category API, Company API, and 9 more. Tagged areas include Company, Fintech, Invoicing, Payments, and Reconciliation.


  The Sibill catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sibill''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
random_paper: 43
rate_limits:
- limit_count: 1
  name: Sibill Rate Limits
  slug: sibill-rate-limits
score:
  band: developing
  composite: 51.5
  delta: 2.6
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 16.7
    contract_quality: 58.5
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 44.7
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sibill/refs/heads/main/screenshots/sibill-2026-08-17T081842.png
security:
- kind: authentication
  name: Sibill Authentication
  slug: sibill-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sibill Domain Security
  slug: sibill-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sibill
tags:
- Company
- Fintech
- Invoicing
- Payments
- Reconciliation
- Accounting
- Banking
- SME
- Open Banking
- Electronic Invoicing
- Italy
website: https://sibill.com/
---
