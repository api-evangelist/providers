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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.5
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Loop Agentic Access
  operation_count: 41
  slug: loop-agentic-access
  summary_line: 41 operations · 15 acting
api_count: 14
apis:
- description: The artifacts API from Loop — 6 operation(s) for artifacts.
  name: Loop artifacts API
  slug: loop-artifacts-api
- description: The artifacts-schema-validated API from Loop — 6 operation(s) for artifacts-schema-validated.
  name: Loop artifacts-schema-validated API
  slug: loop-artifacts-schema-validated-api
- description: The business-exceptions API from Loop — 3 operation(s) for business-exceptions.
  name: Loop business-exceptions API
  slug: loop-business-exceptions-api
- description: The factoring-relationships API from Loop — 2 operation(s) for factoring-relationships.
  name: Loop factoring-relationships API
  slug: loop-factoring-relationships-api
- description: The invoicing-relationships API from Loop — 2 operation(s) for invoicing-relationships.
  name: Loop invoicing-relationships API
  slug: loop-invoicing-relationships-api
- description: The onboarding.api.loop.com API from Loop — 1 operation(s) for onboarding.api.loop.com.
  name: Loop onboarding.api.loop.com API
  slug: loop-onboarding-api-loop-com-api
- description: The organizations API from Loop — 3 operation(s) for organizations.
  name: Loop organizations API
  slug: loop-organizations-api
- description: The payable-allocations API from Loop — 2 operation(s) for payable-allocations.
  name: Loop payable-allocations API
  slug: loop-payable-allocations-api
- description: The payable-invoice-reviews API from Loop — 2 operation(s) for payable-invoice-reviews.
  name: Loop payable-invoice-reviews API
  slug: loop-payable-invoice-reviews-api
- description: The payable-invoices API from Loop — 2 operation(s) for payable-invoices.
  name: Loop payable-invoices API
  slug: loop-payable-invoices-api
- description: The payments API from Loop — 2 operation(s) for payments.
  name: Loop payments API
  slug: loop-payments-api
- description: The ping API from Loop — 1 operation(s) for ping.
  name: Loop ping API
  slug: loop-ping-api
- description: The receivable-invoices API from Loop — 3 operation(s) for receivable-invoices.
  name: Loop receivable-invoices API
  slug: loop-receivable-invoices-api
- description: The shipment-jobs API from Loop — 2 operation(s) for shipment-jobs.
  name: Loop shipment-jobs API
  slug: loop-shipment-jobs-api
artifact_total: 19
asyncapis:
- description: ''
  name: Loop Webhooks
  slug: loop-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loop-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/loop-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/loop-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://loop.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.loop.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.loop.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.loop.com/developers/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.loop.com/integration/
- group: company
  title: ''
  type: Blog
  url: https://loop.com/engineering-blog
- group: start
  title: ''
  type: SignUp
  url: https://app.loop.com
- group: start
  title: ''
  type: Login
  url: https://app.loop.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.loop.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://loop.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://loop.com/legal/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.loop.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/loop-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/loop-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/loop-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/loop-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/loop-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/loop-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/loop-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/loop-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/loop-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/loop-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Loop is a full-stack, AI-powered logistics data platform that unifies the fragmented operational and financial data of the physical economy. Founded by former Uber Freight leaders Matt McKinney and Shaosu Liu, Loop began in freight audit and payment and has expanded into an intelligence layer spanning freight audit, parcel and carrier-invoice auditing, real-time shipment visibility, parcel contract optimization, carrier payments, and autonomous exception management (DUX and the Exception Agent). The Loop developer platform exposes a REST API (api.loop.com/v1) for ingesting artifacts (invoices, shipment records, purchase orders), resolving business exceptions, managing organizations and factoring/invoicing relationships, and reading payable/receivable invoices and payments, plus a separate Onboarding API and Svix-based webhooks. Loop has raised $210M total, including a $95M Series C, from Valor Equity Partners, 8VC, Founders Fund, Index Ventures, J.P. Morgan Growth Equity, and
  others.
image: https://cdn.prod.website-files.com/668bb14a7a97da320e5022ed/66c70f294893e981b7a38704_OG%20Image.webp
layout: provider
mcp_servers:
- description: ''
  name: loop-mcp.yml
  slug: loop-mcpyml
modified: '2026-07-20'
name: Loop
nav: Providers
network: true
overview: 'Loop publishes 14 APIs on the [APIs.io](https://apis.io/) network, including artifacts API, artifacts-schema-validated API, business-exceptions API, and 11 more. Tagged areas include Company, Logistics, Supply Chain, Freight, and Freight Audit.


  The Loop catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Loop''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, and 20 more developer resources.'
random_paper: 94
score:
  band: developing
  composite: 49.1
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 68.3
    developer_ergonomics: 51.6
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 23.7
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loop/refs/heads/main/screenshots/loop-2026-07-25T225523.png
security:
- kind: authentication
  name: Loop Authentication
  slug: loop-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Loop Domain Security
  slug: loop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: loop
tags:
- Company
- Logistics
- Supply Chain
- Freight
- Freight Audit
- Payments
- Transportation
- Artificial Intelligence
- Data Platform
website: https://loop.com
---
