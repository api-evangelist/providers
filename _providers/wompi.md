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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 3
  name: Wompi Agentic Access
  operation_count: 11
  slug: wompi-agentic-access
  summary_line: 11 operations · 6 acting · 3 human-in-the-loop
api_count: 7
apis:
- description: Server-to-server webhook notifications (HTTP POST) for transaction and payment-source state changes, validated with an asymmetric integrity checksum carried in the X-Event-Checksum header and the even
  name: Wompi Events (Webhooks)
  slug: wompi-events-webhooks
- description: Merchant info and presigned acceptance tokens.
  name: Wompi Merchants API
  slug: wompi-merchants-api
- description: Hosted, shareable payment links.
  name: Wompi Payment Links API
  slug: wompi-payment-links-api
- description: Reusable payment sources for recurring charges.
  name: Wompi Payment Sources API
  slug: wompi-payment-sources-api
- description: PSE financial institution catalog.
  name: Wompi PSE API
  slug: wompi-pse-api
- description: Tokenize cards and Nequi accounts.
  name: Wompi Tokenization API
  slug: wompi-tokenization-api
- description: Create and track payment transactions.
  name: Wompi Transactions API
  slug: wompi-transactions-api
artifact_total: 30
asyncapis:
- description: ''
  name: Wompi Webhooks
  slug: wompi-webhooks
collections:
- collection_type: postman
  name: Wompi Merchants API
  slug: postman-wompi-merchants-api
- collection_type: postman
  name: Wompi Merchants Payment Links API
  slug: postman-wompi-payment-links-api
- collection_type: postman
  name: Wompi Merchants Payment Sources API
  slug: postman-wompi-payment-sources-api
- collection_type: postman
  name: Wompi Merchants PSE API
  slug: postman-wompi-pse-api
- collection_type: postman
  name: Wompi Merchants Tokenization API
  slug: postman-wompi-tokenization-api
- collection_type: postman
  name: Wompi Merchants Transactions API
  slug: postman-wompi-transactions-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wompi Merchants API
  slug: open-wompi-merchants-api
- collection_type: open
  name: Wompi Merchants Payment Links API
  slug: open-wompi-payment-links-api
- collection_type: open
  name: Wompi Merchants Payment Sources API
  slug: open-wompi-payment-sources-api
- collection_type: open
  name: Wompi Merchants PSE API
  slug: open-wompi-pse-api
- collection_type: open
  name: Wompi Merchants Tokenization API
  slug: open-wompi-tokenization-api
- collection_type: open
  name: Wompi Merchants Transactions API
  slug: open-wompi-transactions-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/wompi/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wompi-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/wompi-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wompi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wompi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wompi-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://wompi.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wompi.co/
- group: commercial
  title: ''
  type: Plans
  url: plans/wompi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wompi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wompi-finops.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/wompi-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wompi-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/wompi-components.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wompi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wompi-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/wompi-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wompi-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://wompi.statuspage.io/
- group: design
  title: ''
  type: Conformance
  url: conformance/wompi-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/wompi-trust-center.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wompi-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wompi-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wompi-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/wompi-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/wompi-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://comercios.wompi.co/developers
- group: docs
  title: ''
  type: APIReference
  url: https://docs.wompi.co/en/docs/colombia/referencia/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.wompi.co/en/docs/colombia/inicio-rapido/
- group: start
  title: ''
  type: SignUp
  url: https://comercios.wompi.co/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wompi.co/es/co/terminos-y-condiciones
- group: build
  title: ''
  type: Postman
  url: collections/wompi.postman_collection.json
created: '2026-07-17'
description: Wompi is the payment gateway of Grupo Bancolombia, serving Colombia (COP). Its REST API creates and tracks transactions across local payment methods - CARD, NEQUI (mobile wallet), PSE (online bank debit), and Bancolombia Transfer / Collect - plus card and Nequi tokenization, reusable payment sources, and hosted payment links. Public-key endpoints are browser-safe; private-key endpoints are server-side.
finops:
- name: Wompi Finops
  service_category: Payments
  slug: wompi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wompi.png
layout: provider
mcp_servers:
- description: ''
  name: wompi-mcp.yml
  slug: wompi-mcpyml
modified: '2026-07-17'
name: Wompi
nav: Providers
network: true
overview: 'Wompi publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Merchants API, Payment Links API, Payment Sources API, and 3 more. Tagged areas include Payments, Fintech, Colombia, LatAm, and Payment Gateway.


  The Wompi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Wompi''s developer surface includes authentication, documentation, sandbox, API reference, getting-started guide, signup flow, and 27 more developer resources.'
plans:
- name: Wompi Plans Pricing
  plan_count: 2
  slug: wompi-plans-pricing
random_paper: 109
rate_limits:
- limit_count: 1
  name: Wompi Rate Limits
  slug: wompi-rate-limits
score:
  band: strong
  composite: 58.2
  delta: 1.5
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 16.7
    contract_quality: 63.5
    developer_ergonomics: 54.2
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 44.7
  previous_composite: 56.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wompi/refs/heads/main/screenshots/wompi-2026-08-17T082934.png
security:
- kind: authentication
  name: Wompi Authentication
  slug: wompi-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Wompi Domain Security
  slug: wompi-domain-security
  summary_line: HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wompi Vulnerability Disclosure
  slug: wompi-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Wompi Trust Center
  slug: wompi-trust-center
  summary_line: PCI DSS, Grupo Bancolombia security & risk controls
slug: wompi
tags:
- Payments
- Fintech
- Colombia
- LatAm
- Payment Gateway
- PSE
- Nequi
website: https://wompi.co/
---
