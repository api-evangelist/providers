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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 44
  human_in_the_loop: 0
  name: Atlar Agentic Access
  operation_count: 106
  slug: atlar-agentic-access
  summary_line: 106 operations · 44 acting
api_count: 2
apis:
- baseURL: https://api.atlar.com
  baseurl_source: declared
  description: Accounts are financial accounts held by your organization.
  name: Atlar Accounts API
  slug: atlar-accounts-api
- baseURL: https://api.atlar.com
  baseurl_source: declared
  description: Audit logs for IAM-related user events, such as login, logout, and password reset.
  name: Atlar Audit logs API
  slug: atlar-audit-logs-api
- baseURL: https://api.atlar.com
  baseurl_source: declared
  description: Connections represent your technical connections set up by Atlar to your third-party providers such as banks, PSPs, and ERPs.
  name: Atlar Connections API
  slug: atlar-connections-api
- baseURL: https://api.atlar.com
  baseurl_source: declared
  description: Counterparties are entities that the account holder has a relationship with.
  name: Atlar Counterparties API
  slug: atlar-counterparties-api
- baseURL: https://api.atlar.com
  baseurl_source: declared
  description: Credit transfers are payments initiated by a debtor to transfer funds to a creditor's account.
  name: Atlar Credit Transfers API
  slug: atlar-credit-transfers-api
- baseURL: https://api.atlar.com
  baseurl_source: declared
  description: Direct debits are payments initiated by a creditor to collect funds from a debtor's account.
  name: Atlar Direct Debits API
  slug: atlar-direct-debits-api
- baseURL: https://api.atlar.com
  baseurl_source: declared
  description: Documents represent accounting transactions from your ERP system. Such as invoices, payments, credit memos, and journal entries.
  name: Atlar Documents API
  slug: atlar-documents-api
- baseURL: https://api.atlar.com
  baseurl_source: declared
  description: Entities are legal entities, e.g. companies.
  name: Atlar Entities API
  slug: atlar-entities-api
- baseURL: https://api.atlar.com
  baseurl_source: declared
  description: Webhooks are automated notifications sent to a specified URL in response to events or changes.
  name: Atlar Events (webhooks) API
  slug: atlar-events-webhooks-api
- baseURL: https://api.atlar.com
  baseurl_source: declared
  description: External accounts are financial accounts held by counterparties at financial institutions.
  name: Atlar External Accounts API
  slug: atlar-external-accounts-api
- baseURL: https://api.atlar.com
  baseurl_source: declared
  description: Forecasted transactions are transactions that are expected to occur in the future. They can be used to predict future cash flows.
  name: Atlar Forecasted Transactions API
  slug: atlar-forecasted-transactions-api
- baseURL: https://api.atlar.com
  baseurl_source: declared
  description: A GL account represents a general ledger account in your ERP system.
  name: Atlar GL Accounts API
  slug: atlar-gl-accounts-api
- baseURL: https://api.atlar.com
  baseurl_source: declared
  description: A GL entity represents a legal entity in your ERP system. It can have a one-to-one relationship with an Atlar Entity.
  name: Atlar GL Entities API
  slug: atlar-gl-entities-api
- baseURL: https://api.atlar.com
  baseurl_source: declared
  description: Investments are financial assets held by your organization.
  name: Atlar Investments API
  slug: atlar-investments-api
- baseURL: https://api.atlar.com
  baseurl_source: declared
  description: Mandates are authorizations given by a debtor to a creditor to collect funds from the account.
  name: Atlar Mandates API
  slug: atlar-mandates-api
- baseURL: https://api.atlar.com
  baseurl_source: declared
  description: OAuth 2.0 endpoints.
  name: Atlar OAuth API
  slug: atlar-oauth-api
- baseURL: https://api.atlar.com
  baseurl_source: declared
  description: Pending transactions are indications of movement of funds that may be booked on an account.
  name: Atlar Pending Transactions API
  slug: atlar-pending-transactions-api
- baseURL: https://api.atlar.com
  baseurl_source: declared
  description: Regulatory reporting codes required for cross-border payments to certain countries.
  name: Atlar Regulatory Reporting API
  slug: atlar-regulatory-reporting-api
- baseURL: https://api.atlar.com
  baseurl_source: declared
  description: Transactions are movements of funds that have been booked on an account.
  name: Atlar Transactions API
  slug: atlar-transactions-api
- baseURL: https://api.atlar.com
  baseurl_source: declared
  description: Webhook configuration.
  name: Atlar Webhooks API
  slug: atlar-webhooks-api
artifact_total: 34
asyncapis:
- description: ''
  name: Atlar Webhooks
  slug: atlar-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/agentic-access/atlar-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/atlar-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/rules/atlar-rules.yml
  title: ''
  type: Spectral
  url: rules/atlar-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/json-ld/atlar-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/atlar-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/vocabulary/atlar-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/atlar-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/errors/atlar-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/atlar-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/hosts/atlar-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atlar-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/vendors/atlar-vendors.yml
  title: ''
  type: Vendors
  url: vendors/atlar-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/security/atlar-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/atlar-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/security/atlar-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atlar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.atlar.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.atlar.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.atlar.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.atlar.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.atlar.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.atlar.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.atlar.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.atlar.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.atlar.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.atlar.com/docs/migrate-from-v1-to-v2
- group: commercial
  title: ''
  type: Pricing
  url: https://www.atlar.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.atlar.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atlar.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atlar.com/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://www.atlar.com/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/authentication/atlar-authentication.yml
  title: ''
  type: Authentication
  url: authentication/atlar-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/well-known/atlar-oauth-authorization-server.json
  title: ''
  type: OAuthAuthorizationServer
  url: well-known/atlar-oauth-authorization-server.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/well-known/atlar-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/atlar-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/mcp/atlar-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/atlar-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/llms/atlar-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/atlar-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/conventions/atlar-conventions.yml
  title: ''
  type: Conventions
  url: conventions/atlar-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/conventions/atlar-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/atlar-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/errors/atlar-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/atlar-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/asyncapi/atlar-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/atlar-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/lifecycle/atlar-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/atlar-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/changelog/atlar-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/atlar-changelog.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/sandbox/atlar-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/atlar-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/conformance/atlar-conformance.yml
  title: ''
  type: Conformance
  url: conformance/atlar-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/data-model/atlar-data-model.yml
  title: ''
  type: DataModel
  url: data-model/atlar-data-model.yml
created: '2026-07-17'
description: Atlar is a treasury and payment operations platform that centralizes cash management, payments, forecasting, bank reconciliation, and debt and investment management for finance teams. It connects to banks and ERPs (NetSuite, SAP, Dynamics 365, Workday) across 100+ countries and exposes a resource-oriented JSON REST API grouped into product namespaces — financial-data (accounts, balances, transactions), payments (credit transfers, direct debits, counterparties, mandates), connectivity, IAM, analytics/forecasting and accounting. The platform is AI-native, offering a hosted MCP server, signed webhooks, OAuth 2.0 client-credentials auth, idempotency keys, cursor pagination and ETag optimistic concurrency. Atlar is SOC 2 and ISO 27001 certified. It is headquartered in Stockholm and backed by Index Ventures and General Catalyst.
image: https://cdn.prod.website-files.com/656f3c6489ea21aff4dfcf78/692571712cc755c88534f173_atlar-treasury-meta-comp.png
json_schemas:
- name: AuditLogEntry
  property_count: 11
  slug: atlar-audit-log-entry
- name: CreateDocumentRequest
  property_count: 19
  slug: atlar-create-document-request
- name: CreditTransfer
  property_count: 30
  slug: atlar-credit-transfer
- name: Document
  property_count: 28
  slug: atlar-document
- name: PendingTransaction
  property_count: 23
  slug: atlar-pending-transaction
- name: Transaction
  property_count: 26
  slug: atlar-transaction
jsonld:
- class_count: 120
  name: Atlar Context
  property_count: 161
  slug: atlar-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.atlar.com over HTTP.
  name: Atlar MCP Server
  slug: atlar
modified: '2026-07-18'
name: Atlar
nav: Providers
network: true
overview: 'Atlar publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Audit logs API, Connections API, and 17 more. Tagged areas include Company, Fintech, Treasury, Payments, and Banking.


  The Atlar catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Atlar''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, pricing, and 31 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Atlar API Rules
  rule_count: 14
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 4
  slug: atlar-rules
score:
  band: strong
  composite: 57.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 13.0
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 74.2
    developer_ergonomics: 45.2
    discoverability: 75.0
    operational_transparency: 43.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 44.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 20
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 23.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/atlar/refs/heads/main/screenshots/atlar-2026-07-25T201542.png
security:
- kind: authentication
  name: Atlar Authentication
  slug: atlar-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Atlar Domain Security
  slug: atlar-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Atlar Trust Center
  slug: atlar-trust-center
  summary_line: SOC 2, ISO 27001
slug: atlar
tags:
- Company
- Fintech
- Treasury
- Payments
- Banking
- Cash Management
- Financial Operations
- ERP Integration
website: https://www.atlar.com/
---
