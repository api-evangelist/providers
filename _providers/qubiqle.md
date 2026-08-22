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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.8
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Qubiqle Agentic Access
  operation_count: 53
  slug: qubiqle-agentic-access
  summary_line: 53 operations · 27 acting
api_count: 9
apis:
- description: The accounts API from Qubiqle — 3 operation(s) for accounts.
  name: Qubiqle accounts API
  slug: qubiqle-accounts-api
- description: The batch API from Qubiqle — 3 operation(s) for batch.
  name: Qubiqle batch API
  slug: qubiqle-batch-api
- description: The catalog API from Qubiqle — 12 operation(s) for catalog.
  name: Qubiqle catalog API
  slug: qubiqle-catalog-api
- description: The dimensions API from Qubiqle — 3 operation(s) for dimensions.
  name: Qubiqle dimensions API
  slug: qubiqle-dimensions-api
- description: The invoices API from Qubiqle — 11 operation(s) for invoices.
  name: Qubiqle invoices API
  slug: qubiqle-invoices-api
- description: The oauth API from Qubiqle — 1 operation(s) for oauth.
  name: Qubiqle oauth API
  slug: qubiqle-oauth-api
- description: The purchaseOrders API from Qubiqle — 3 operation(s) for purchaseorders.
  name: Qubiqle purchaseOrders API
  slug: qubiqle-purchaseorders-api
- description: The receipts API from Qubiqle — 3 operation(s) for receipts.
  name: Qubiqle receipts API
  slug: qubiqle-receipts-api
- description: The vendors API from Qubiqle — 3 operation(s) for vendors.
  name: Qubiqle vendors API
  slug: qubiqle-vendors-api
arazzos:
- description: Upload an invoice document, retrieve the created invoice, code it, then mark it exported.
  name: Invoice capture to export
  slug: qubiqle-invoice-capture-to-export
- description: Authenticate, then upsert accounting dimensions and vendors so invoices can be auto-coded and matched.
  name: Sync ERP master data into Ottimate
  slug: qubiqle-sync-erp-master-data
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API Reference accounts API
  slug: open-qubiqle-accounts-api
- collection_type: open
  name: API Reference accounts batch API
  slug: open-qubiqle-batch-api
- collection_type: open
  name: API Reference accounts catalog API
  slug: open-qubiqle-catalog-api
- collection_type: open
  name: API Reference accounts dimensions API
  slug: open-qubiqle-dimensions-api
- collection_type: open
  name: API Reference accounts invoices API
  slug: open-qubiqle-invoices-api
- collection_type: open
  name: API Reference accounts oauth API
  slug: open-qubiqle-oauth-api
- collection_type: open
  name: API Reference accounts purchaseOrders API
  slug: open-qubiqle-purchaseorders-api
- collection_type: open
  name: API Reference accounts receipts API
  slug: open-qubiqle-receipts-api
- collection_type: open
  name: API Reference accounts vendors API
  slug: open-qubiqle-vendors-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/qubiqle-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://ottimate.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ottimate.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ottimate.com/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ottimate.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ottimate.com/integration-journey
- group: auth
  title: ''
  type: Authentication
  url: authentication/qubiqle-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/qubiqle-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/qubiqle-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qubiqle-rate-limits.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/qubiqle-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qubiqle-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qubiqle-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qubiqle-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qubiqle-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ottimate.com
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.ottimate.com/releases
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/qubiqle-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qubiqle-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/qubiqle-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/qubiqle-sync-erp-master-data.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/qubiqle-invoice-capture-to-export.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qubiqle-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qubiqle-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/qubiqle-well-known.yml
- group: operate
  title: ''
  type: Support
  url: https://ottimate.com/support
- group: company
  title: ''
  type: Blog
  url: https://ottimate.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PlateIQ
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.ottimate.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ottimate.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ottimate.com/privacy-policy
created: '2026-07-17'
description: Qubiqle is an early 500 Startups (500 Global) portfolio company that became Plate IQ and today operates as Ottimate (qubiqle.com redirects to ottimate.com). Ottimate is an AI-powered accounts payable (AP) automation platform for invoice capture, GL coding and matching, approval workflows, and vendor payments, processing 40M+ invoices and $30B+ in payables annually across 30,000+ US locations. It exposes a REST/JSON V1 API (api.ottimate.com/v1, sandbox at sandbox-api.ottimate.com/v1) covering accounts, vendors, dimensions, purchase orders, receipts, invoices, catalog, and async batch processing — secured with an X-Api-Key header plus an OAuth2 client_credentials bearer token, with documented idempotency, pagination, rate limits, and a hosted docs MCP server.
image: https://ottimate.com/wp-content/uploads/2025/09/ottimate-cover-image.png
layout: provider
mcp_servers:
- description: ''
  name: qubiqle-mcp.yml
  slug: qubiqle-mcpyml
modified: '2026-07-20'
name: Qubiqle
nav: Providers
network: true
overview: 'Qubiqle publishes 9 APIs on the [APIs.io](https://apis.io/) network, including accounts API, batch API, catalog API, and 6 more. Tagged areas include Company, Accounts Payable, Invoicing, Payments, and Accounting.


  Qubiqle''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, changelog, support, and 25 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 3
  name: Qubiqle Rate Limits
  slug: qubiqle-rate-limits
scopes:
- name: Qubiqle Scopes
  scope_count: 1
  slug: qubiqle-scopes
  summary_line: 1 scope
score:
  band: strong
  composite: 54.4
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 55.4
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 73.7
  previous_composite: 54.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 54.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qubiqle/refs/heads/main/screenshots/qubiqle-2026-08-17T081428.png
security:
- kind: authentication
  name: Qubiqle Authentication
  slug: qubiqle-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Qubiqle Domain Security
  slug: qubiqle-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qubiqle
tags:
- Company
- Accounts Payable
- Invoicing
- Payments
- Accounting
- FinTech
- Automation
- Artificial Intelligence
- ERP Integration
- Procurement
website: https://ottimate.com
---
