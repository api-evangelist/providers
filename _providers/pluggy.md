---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 42
  human_in_the_loop: 1
  name: Pluggy Agentic Access
  operation_count: 94
  slug: pluggy-agentic-access
  summary_line: 94 operations · 42 acting · 1 human-in-the-loop
api_count: 5
apis:
- baseURL: https://enrichment-api.pluggy.ai
  baseurl_source: declared
  description: Pluggy Enrichment API -- transaction categorization, behavior analysis, and recurring-payments detection.
  name: Pluggy Enrichment API
  slug: enrichment-api
- baseURL: https://status.pluggy.ai
  baseurl_source: declared
  description: Read the health of every Pluggy connector, product and infrastructure component plus open and past incidents (the data behind status.pluggy.ai); no authentication required.
  name: Pluggy Status API
  slug: status-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: Bank account information and management
  name: Pluggy Account API
  slug: pluggy-account-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: Authentication endpoints for API key generation and connect tokens
  name: Pluggy Auth API
  slug: pluggy-auth-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: Automatic PIX payment scheduling and management
  name: Pluggy Automatic PIX API
  slug: pluggy-automatic-pix-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: Credit card bill information
  name: Pluggy Bill API
  slug: pluggy-bill-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: Boleto payment management
  name: Pluggy Boleto Management API
  slug: pluggy-boleto-management-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: Transaction categorization and rules
  name: Pluggy Category API
  slug: pluggy-category-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: Financial institution connector management
  name: Pluggy Connector API
  slug: pluggy-connector-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: User consent management for data access
  name: Pluggy Consent API
  slug: pluggy-consent-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: User identity verification and data
  name: Pluggy Identity API
  slug: pluggy-identity-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: Investment portfolio and asset management
  name: Pluggy Investment API
  slug: pluggy-investment-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: Item management for syncing financial data
  name: Pluggy Items API
  slug: pluggy-items-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: Loan information and management
  name: Pluggy Loan API
  slug: pluggy-loan-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: Merchant and company information by CNPJ
  name: Pluggy Merchant API
  slug: pluggy-merchant-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: Payment customer management
  name: Pluggy Payment Customer API
  slug: pluggy-payment-customer-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: Payment intent processing
  name: Pluggy Payment Intent API
  slug: pluggy-payment-intent-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: Payment recipient management
  name: Pluggy Payment Recipient API
  slug: pluggy-payment-recipient-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: Payment request creation and management
  name: Pluggy Payment Request API
  slug: pluggy-payment-request-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: Payment scheduling operations
  name: Pluggy Payment Schedule API
  slug: pluggy-payment-schedule-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: Bacen's credit information system, consulted through a connected Open Finance item
  name: Pluggy SCR API
  slug: pluggy-scr-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: Smart transfer functionality
  name: Pluggy Smart Transfer API
  slug: pluggy-smart-transfer-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: Financial transaction data and operations
  name: Pluggy Transaction API
  slug: pluggy-transaction-api
- baseURL: https://api.pluggy.ai
  baseurl_source: declared
  description: Webhook configuration and management
  name: Pluggy Webhook API
  slug: pluggy-webhook-api
artifact_total: 49
asyncapis:
- description: ''
  name: Pluggy Webhooks
  slug: pluggy-webhooks
common:
- group: other
  href: https://artifacts.apis.io/pluggy/capabilities/pluggy-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/pluggy-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/pluggy/well-known/pluggy-mcp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pluggy-mcp-security.txt
- group: auth
  href: https://artifacts.apis.io/pluggy/well-known/pluggy-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pluggy-docs-security.txt
- group: agent
  href: https://artifacts.apis.io/pluggy/agentic-access/pluggy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/pluggy-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/pluggy/rate-limits/pluggy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pluggy-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/pluggy/plans/pluggy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pluggy-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/pluggy/rules/pluggy-rules.yml
  title: ''
  type: Spectral
  url: rules/pluggy-rules.yml
- group: design
  href: https://artifacts.apis.io/pluggy/json-ld/pluggy-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pluggy-context.jsonld
- group: design
  href: https://artifacts.apis.io/pluggy/vocabulary/pluggy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pluggy-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/pluggy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/pluggy/asyncapi/pluggy-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/pluggy-webhooks.yml
- group: design
  href: https://artifacts.apis.io/pluggy/data-model/pluggy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pluggy-data-model.yml
- group: design
  href: https://artifacts.apis.io/pluggy/components/pluggy-components.yml
  title: ''
  type: Components
  url: components/pluggy-components.yml
- group: operate
  href: https://artifacts.apis.io/pluggy/changelog/pluggy-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pluggy-changelog.yml
- group: design
  href: https://artifacts.apis.io/pluggy/conventions/pluggy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/pluggy-conventions.yml
- group: start
  href: https://artifacts.apis.io/pluggy/sandbox/pluggy-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/pluggy-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.pluggy.ai/legal
- group: auth
  href: https://artifacts.apis.io/pluggy/authentication/pluggy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pluggy-authentication.yml
- group: design
  href: https://artifacts.apis.io/pluggy/lifecycle/pluggy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pluggy-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/pluggy/errors/pluggy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pluggy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pluggy/conformance/pluggy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pluggy-conformance.yml
- group: other
  href: https://artifacts.apis.io/pluggy/overlays/pluggy-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pluggy-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/pluggy/llms/pluggy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pluggy-llms.txt
- group: build
  href: https://artifacts.apis.io/pluggy/mcp/pluggy-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/pluggy-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/pluggy/mcp/pluggy-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pluggy-mcp.yml
- group: agent
  href: https://artifacts.apis.io/pluggy/well-known/pluggy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pluggy-well-known.yml
- group: other
  href: https://artifacts.apis.io/pluggy/hosts/pluggy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pluggy-hosts.yml
- group: other
  href: https://artifacts.apis.io/pluggy/vendors/pluggy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pluggy-vendors.yml
- group: build
  href: https://artifacts.apis.io/pluggy/packages/pluggy-packages.yml
  title: ''
  type: SDKs
  url: packages/pluggy-packages.yml
- group: build
  href: https://artifacts.apis.io/pluggy/packages/pluggy-packages.yml
  title: ''
  type: Packages
  url: packages/pluggy-packages.yml
- group: company
  title: ''
  type: Website
  url: https://www.pluggy.ai
- group: auth
  href: https://artifacts.apis.io/pluggy/security/pluggy-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/pluggy-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/pluggy/security/pluggy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pluggy-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pluggy.ai/en
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pluggy.ai/en/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pluggy.ai/en/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.pluggy.ai/en/docs/get-started/contact
- group: company
  title: ''
  type: Blog
  url: https://www.pluggy.ai/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.pluggy.ai/en/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pluggy.ai/en/pricing
- group: build
  title: ''
  type: Postman
  url: https://docs.pluggy.ai/en/docs/developer-tools/postman
- group: start
  title: ''
  type: Sandbox
  url: https://sandbox.pluggy.ai/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pluggy.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pluggyai
- group: start
  title: ''
  type: Login
  url: https://dashboard.pluggy.ai/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pluggy.ai/docs/termos-e-condicoes-de-uso.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pluggy.ai/docs/politica-de-privacidade.pdf
- group: commercial
  title: ''
  type: Legal
  url: https://www.pluggy.ai/legal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pluggyai
created: '2026-10-18'
description: Pluggy is a Brazilian Open Finance infrastructure company (pluggy.ai) offering APIs to connect bank data, collect payments and move money across Brazilian financial institutions. Its platform aggregates accounts, transactions, investments, credit card bills and identity data through direct and regulated Open Finance connectors, with the Pluggy Connect drop-in widget, a sandbox environment, a developer dashboard and an MCP server for developer tooling.
image: https://www.pluggy.ai/opengraph-image
json_schemas:
- name: ConnectorIncidents
  property_count: 2
  slug: pluggy-connector-incidents
- name: IdentityResponse
  property_count: 30
  slug: pluggy-identity-response
- name: Investment
  property_count: 44
  slug: pluggy-investment
- name: Item
  property_count: 18
  slug: pluggy-item
- name: Loan
  property_count: 27
  slug: pluggy-loan
- name: PaymentRequest
  property_count: 19
  slug: pluggy-payment-request
- name: StatusSnapshot
  property_count: 6
  slug: pluggy-status-snapshot
- name: StatusSummary
  property_count: 4
  slug: pluggy-status-summary
- name: Transaction
  property_count: 23
  slug: pluggy-transaction
jsonld:
- class_count: 120
  name: Pluggy Context
  property_count: 462
  slug: pluggy-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.pluggy.ai over streamable HTTP requiring OAuth; 34 tools listed.
  name: Pluggy MCP Server
  slug: pluggy-docs
modified: '2026-10-18'
name: Pluggy
nav: Providers
network: true
overview: 'Pluggy publishes 24 API contracts indexed on the [APIs.io](https://apis.io/) network, including Enrichment API, Status API, Account API, and 21 more. Tagged areas include Company, Open Finance, Banking, Financial Data, and Payments.


  The Pluggy catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Pluggy''s developer surface includes changelog, sandbox, authentication, documentation, API reference, getting-started guide, support, and 42 more developer resources.'
plans:
- name: Pluggy Plans Pricing
  plan_count: 2
  slug: pluggy-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 24
  name: Pluggy Rate Limits
  slug: pluggy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Pluggy API Rules
  rule_count: 17
  severity_counts:
    error: 9
    hint: 0
    info: 3
    warn: 5
  slug: pluggy-rules
scopes:
- name: Pluggy Scopes
  scope_count: 0
  slug: pluggy-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 72.4
  coverage:
    artifact_dirs: 33
    catalog_earned: 85.8
    catalog_earned_first_party: 20.0
    catalog_gap: 29.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 81.6
    contract_governance: 22.0
    contract_quality: 76.0
    developer_ergonomics: 68.5
    discoverability: 70.0
    operational_transparency: 86.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 37.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Pluggy Authentication
  slug: pluggy-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Pluggy Domain Security
  slug: pluggy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pluggy Trust Center
  slug: pluggy-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 5
skills:
- name: pluggy-check-connector-health
  slug: pluggy-check-connector-health
- name: pluggy-connect-and-sync-an-item
  slug: pluggy-connect-and-sync-an-item
- name: pluggy-enrich-transactions
  slug: pluggy-enrich-transactions
- name: pluggy-initiate-a-pix-payment
  slug: pluggy-initiate-a-pix-payment
- name: pluggy-read-open-finance-data
  slug: pluggy-read-open-finance-data
slug: pluggy
tags:
- Company
- Open Finance
- Banking
- Financial Data
- Payments
- Brazil
- Fintech
website: https://www.pluggy.ai
---
