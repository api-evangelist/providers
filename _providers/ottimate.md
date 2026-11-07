---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.4
  scored_at: '2026-11-06'
api_count: 10
apis:
- baseURL: https://api.ottimate.com/v1
  baseurl_source: declared
  description: The accounts API from Ottimate — 3 operation(s) for accounts.
  name: Ottimate Accounts API
  slug: ottimate-accounts-api
- baseURL: https://api.ottimate.com/v1
  baseurl_source: declared
  description: The batch API from Ottimate — 3 operation(s) for batch.
  name: Ottimate Batch API
  slug: ottimate-batch-api
- baseURL: https://api.ottimate.com/v1
  baseurl_source: declared
  description: The catalog API from Ottimate — 12 operation(s) for catalog.
  name: Ottimate Catalog API
  slug: ottimate-catalog-api
- baseURL: https://api.ottimate.com/v1
  baseurl_source: declared
  description: The dimensions API from Ottimate — 3 operation(s) for dimensions.
  name: Ottimate Dimensions API
  slug: ottimate-dimensions-api
- baseURL: https://api.ottimate.com/v1
  baseurl_source: declared
  description: The invoices API from Ottimate — 11 operation(s) for invoices.
  name: Ottimate Invoices API
  slug: ottimate-invoices-api
- baseURL: https://api.ottimate.com/v1
  baseurl_source: declared
  description: The oauth API from Ottimate — 1 operation(s) for oauth.
  name: Ottimate OAuth API
  slug: ottimate-oauth-api
- baseURL: https://api.ottimate.com/v1
  baseurl_source: declared
  description: The receipts API from Ottimate — 3 operation(s) for receipts.
  name: Ottimate Receipts API
  slug: ottimate-receipts-api
- baseURL: https://api.ottimate.com/v1
  baseurl_source: declared
  description: The vendors API from Ottimate — 3 operation(s) for vendors.
  name: Ottimate Vendors API
  slug: ottimate-vendors-api
- baseURL: https://api.ottimate.com/v1
  baseurl_source: declared
  description: The Purchase Orders API from Ottimate — 3 operation(s) for purchase orders.
  name: Ottimate Purchase Orders API
  slug: ottimate-purchase-orders-api
artifact_total: 27
collections:
- collection_type: open
  name: API Reference accounts API
  slug: open-plateiq-accounts-api
- collection_type: open
  name: API Reference accounts batch API
  slug: open-plateiq-batch-api
- collection_type: open
  name: API Reference accounts catalog API
  slug: open-plateiq-catalog-api
- collection_type: open
  name: API Reference accounts dimensions API
  slug: open-plateiq-dimensions-api
- collection_type: open
  name: API Reference accounts invoices API
  slug: open-plateiq-invoices-api
- collection_type: open
  name: API Reference accounts oauth API
  slug: open-plateiq-oauth-api
- collection_type: open
  name: API Reference accounts purchaseOrders API
  slug: open-plateiq-purchaseorders-api
- collection_type: open
  name: API Reference accounts receipts API
  slug: open-plateiq-receipts-api
- collection_type: open
  name: API Reference accounts vendors API
  slug: open-plateiq-vendors-api
common:
- group: other
  href: https://artifacts.apis.io/ottimate/capabilities/ottimate-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/ottimate-capability-edges.yml
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
  href: https://artifacts.apis.io/ottimate/lifecycle/plateiq-lifecycle.yml
  title: ''
  type: StatusPage
  url: lifecycle/plateiq-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/ottimate/lifecycle/plateiq-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/plateiq-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ottimate/lifecycle/plateiq-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/plateiq-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/ottimate/changelog/plateiq-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/plateiq-changelog.yml
- group: docs
  href: https://artifacts.apis.io/ottimate/openapi/_original/plateiq-openapi.yaml
  title: ''
  type: OpenAPI
  url: openapi/_original/plateiq-openapi.yaml
- group: auth
  href: https://artifacts.apis.io/ottimate/authentication/plateiq-authentication.yml
  title: ''
  type: Authentication
  url: authentication/plateiq-authentication.yml
- group: auth
  href: https://artifacts.apis.io/ottimate/scopes/plateiq-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/plateiq-scopes.yml
- group: design
  href: https://artifacts.apis.io/ottimate/conventions/plateiq-conventions.yml
  title: ''
  type: Conventions
  url: conventions/plateiq-conventions.yml
- group: design
  href: https://artifacts.apis.io/ottimate/conventions/plateiq-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/plateiq-conventions.yml
- group: operate
  href: https://artifacts.apis.io/ottimate/rate-limits/plateiq-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/plateiq-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/ottimate/errors/plateiq-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/plateiq-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ottimate/data-model/plateiq-data-model.yml
  title: ''
  type: DataModel
  url: data-model/plateiq-data-model.yml
- group: start
  href: https://artifacts.apis.io/ottimate/sandbox/plateiq-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/plateiq-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/ottimate/mcp/plateiq-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/plateiq-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ottimate/llms/plateiq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/plateiq-llms.txt
- group: other
  href: https://artifacts.apis.io/ottimate/overlays/plateiq-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/plateiq-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/ottimate/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/ottimate/conformance/plateiq-conformance.yml
  title: ''
  type: Conformance
  url: conformance/plateiq-conformance.yml
- group: auth
  href: https://artifacts.apis.io/ottimate/conformance/plateiq-conformance.yml
  title: ''
  type: Compliance
  url: conformance/plateiq-conformance.yml
- group: auth
  href: https://artifacts.apis.io/ottimate/security/plateiq-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/plateiq-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/ottimate/security/plateiq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/plateiq-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PlateIQ
created: '2026-07-17'
description: Ottimate (formerly Plate IQ) is an AI-powered accounts payable automation platform for restaurants, hospitality, and multi-location businesses. It captures and GL-codes invoices with high accuracy via its InstantCapture engine, automates approval workflows and PO/receipt matching in Core AP, and sends vendor payments via ACH, check, or virtual card through VendorPay. Ottimate exposes a partner-provisioned REST API (OpenAPI 3.1) over JSON with OAuth2 client-credentials plus API-key auth, idempotent writes, bulk and asynchronous operations, and ERP integrations for QuickBooks, NetSuite, Sage Intacct, Acumatica, and Microsoft Dynamics.
image: https://ottimate.com/wp-content/uploads/2025/09/ottimate-cover-image.png
layout: provider
mcp_servers:
- description: Official hosted MCP server advertised by Ottimate for AI client integration (Claude Code, Cursor, etc.). Backed by Fern's docs MCP; it exposes the Ottimate developer documentation as a searchable tool
  name: Ottimate Docs MCP Server
  slug: ottimate-docs-mcp-server
modified: '2026-07-20'
name: Ottimate
nav: Providers
network: true
overview: 'Ottimate publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Batch API, Catalog API, and 6 more. Tagged areas include Company, Enterprise Saas, Accounts Payable, Invoice Automation, and Payments.


  The Ottimate catalog on APIs.io includes 1 Spectral governance ruleset.


  Ottimate''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, authentication, and 25 more developer resources.'
random_paper: 7
rate_limits:
- limit_count: 3
  name: Plateiq Rate Limits
  slug: plateiq-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Ottimate API Rules
  rule_count: 57
  severity_counts:
    error: 47
    hint: 0
    info: 3
    warn: 7
  slug: ottimate-rules
scopes:
- name: Plateiq Scopes
  scope_count: 1
  slug: plateiq-scopes
  summary_line: 1 scope · client_credentials
score:
  band: strong
  composite: 61.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 36.8
    contract_governance: 31.8
    contract_quality: 51.6
    developer_ergonomics: 66.1
    discoverability: 76.7
    operational_transparency: 73.7
  previous_composite: 61.6
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
    score: 35.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/ottimate/plateiq-2026-08-17T081300.png
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
skill_count: 2
skills:
- name: plateiq-invoice-capture-and-export
  slug: plateiq-invoice-capture-and-export
- name: plateiq-sync-erp-master-data
  slug: plateiq-sync-erp-master-data
slug: ottimate
tags:
- Company
- Enterprise Saas
- Accounts Payable
- Invoice Automation
- Payments
- Fintech
- Restaurant
- Procurement
- Spend Management
- ERP Integration
website: https://ottimate.com/
---
