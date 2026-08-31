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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Loop Agentic Access
  operation_count: 41
  slug: loop-agentic-access
  summary_line: 41 operations · 15 acting
api_count: 2
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
artifact_total: 33
asyncapis:
- description: ''
  name: Loop Webhooks
  slug: loop-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Loop Onboarding artifacts API
  slug: open-loop-artifacts-api
- collection_type: open
  name: Loop Onboarding artifacts artifacts-schema-validated API
  slug: open-loop-artifacts-schema-validated-api
- collection_type: open
  name: Loop Onboarding artifacts business-exceptions API
  slug: open-loop-business-exceptions-api
- collection_type: open
  name: Loop Onboarding artifacts factoring-relationships API
  slug: open-loop-factoring-relationships-api
- collection_type: open
  name: Loop Onboarding artifacts invoicing-relationships API
  slug: open-loop-invoicing-relationships-api
- collection_type: open
  name: Loop Onboarding artifacts onboarding.api.loop.com API
  slug: open-loop-onboarding-api-loop-com-api
- collection_type: open
  name: Loop Onboarding artifacts organizations API
  slug: open-loop-organizations-api
- collection_type: open
  name: Loop Onboarding artifacts payable-allocations API
  slug: open-loop-payable-allocations-api
- collection_type: open
  name: Loop Onboarding artifacts payable-invoices API
  slug: open-loop-payable-invoices-api
- collection_type: open
  name: Loop Onboarding artifacts payments API
  slug: open-loop-payments-api
- collection_type: open
  name: Loop Onboarding artifacts ping API
  slug: open-loop-ping-api
- collection_type: open
  name: Loop Onboarding artifacts receivable-invoices API
  slug: open-loop-receivable-invoices-api
- collection_type: open
  name: Loop Onboarding artifacts shipment-jobs API
  slug: open-loop-shipment-jobs-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/loop-capability-edges.yml
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
- description: 'Candidate MCP tool surface derived one-to-one from Loop API operationIds. Loop publishes no official hosted MCP server as of this pass; this is a derivation to seed an agent-native surface. Auth: bear'
  name: Loop MCP Server
  slug: loop-mcp-server
modified: '2026-07-20'
name: Loop
nav: Providers
network: true
overview: 'Loop publishes 14 APIs on the [APIs.io](https://apis.io/) network, including artifacts API, artifacts-schema-validated API, business-exceptions API, and 11 more. Tagged areas include Company, Logistics, Supply Chain, Freight, and Freight Audit.


  The Loop catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Loop''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, signup flow, and 21 more developer resources.'
random_paper: 1
score:
  band: developing
  composite: 45.3
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 61.2
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 45.9
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
