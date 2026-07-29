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
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: verified
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.6
  scored_at: '2026-07-28'
api_count: 9
apis:
- description: The accounts API from PlateIQ — 3 operation(s) for accounts.
  name: PlateIQ accounts API
  slug: plateiq-accounts-api
- description: The batch API from PlateIQ — 3 operation(s) for batch.
  name: PlateIQ batch API
  slug: plateiq-batch-api
- description: The catalog API from PlateIQ — 12 operation(s) for catalog.
  name: PlateIQ catalog API
  slug: plateiq-catalog-api
- description: The dimensions API from PlateIQ — 3 operation(s) for dimensions.
  name: PlateIQ dimensions API
  slug: plateiq-dimensions-api
- description: The invoices API from PlateIQ — 11 operation(s) for invoices.
  name: PlateIQ invoices API
  slug: plateiq-invoices-api
- description: The oauth API from PlateIQ — 1 operation(s) for oauth.
  name: PlateIQ oauth API
  slug: plateiq-oauth-api
- description: The purchaseOrders API from PlateIQ — 3 operation(s) for purchaseorders.
  name: PlateIQ purchaseOrders API
  slug: plateiq-purchaseorders-api
- description: The receipts API from PlateIQ — 3 operation(s) for receipts.
  name: PlateIQ receipts API
  slug: plateiq-receipts-api
- description: The vendors API from PlateIQ — 3 operation(s) for vendors.
  name: PlateIQ vendors API
  slug: plateiq-vendors-api
artifact_total: 15
common:
- group: company
  title: ''
  type: Website
  url: https://ottimate.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ottimate.com/welcome
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
- group: company
  title: ''
  type: Blog
  url: https://ottimate.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://ottimate.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ottimate.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ottimate.com/terms-of-service/
- group: operate
  title: ''
  type: StatusPage
  url: lifecycle/plateiq-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/plateiq-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/plateiq-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/plateiq-changelog.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/plateiq-openapi.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/plateiq-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/plateiq-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/plateiq-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/plateiq-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/plateiq-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/plateiq-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/plateiq-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/plateiq-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/plateiq-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plateiq-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/plateiq-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/plateiq-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/plateiq-conformance.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/plateiq-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plateiq-domain-security.yml
created: '2026-07-17'
description: Ottimate (formerly Plate IQ) is an AI-powered accounts payable automation platform for restaurants, hospitality, and multi-location businesses. It captures and GL-codes invoices with high accuracy via its InstantCapture engine, automates approval workflows and PO/receipt matching in Core AP, and sends vendor payments via ACH, check, or virtual card through VendorPay. Ottimate exposes a partner-provisioned REST API (OpenAPI 3.1) over JSON with OAuth2 client-credentials plus API-key auth, idempotent writes, bulk and asynchronous operations, and ERP integrations for QuickBooks, NetSuite, Sage Intacct, Acumatica, and Microsoft Dynamics.
image: https://ottimate.com/wp-content/uploads/2025/09/ottimate-cover-image.png
layout: provider
mcp_servers:
- description: ''
  name: plateiq-mcp.yml
  slug: plateiq-mcpyml
modified: '2026-07-20'
name: PlateIQ
nav: Providers
network: true
overview: 'PlateIQ publishes 9 APIs on the [APIs.io](https://apis.io/) network, including accounts API, batch API, catalog API, and 6 more. Tagged areas include Company, Enterprise Saas, Accounts Payable, Invoice Automation, and Payments.


  PlateIQ''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 23 more developer resources.'
random_paper: 59
rate_limits:
- limit_count: 0
  name: Plateiq Rate Limits
  slug: plateiq-rate-limits
scopes:
- name: Plateiq Scopes
  scope_count: 0
  slug: plateiq-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.2
  delta: -2.5
  facets:
    commercial_clarity: 36.8
    contract_quality: 53.9
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 39.5
  previous_composite: 55.7
  provenance:
    conformance: first-party
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
    score: 62.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Plateiq Authentication
  slug: plateiq-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Plateiq Domain Security
  slug: plateiq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Plateiq Trust Center
  slug: plateiq-trust-center
  summary_line: SOC 2 Type II, ISO 27001
slug: plateiq
tags:
- Company
- Enterprise Saas
- Accounts Payable
- Invoice Automation
- Payments
- Fintech
- Restaurants
- Procurement
- Spend Management
- ERP Integration
website: https://ottimate.com/
---
