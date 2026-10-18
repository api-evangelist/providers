---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bound
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Clarafintech Agentic Access
  operation_count: 29
  slug: clarafintech-agentic-access
  summary_line: 29 operations · 11 acting
api_count: 1
apis:
- baseURL: https://public-api.mx.clara.com
  baseurl_source: declared
  description: Create, cancel, and track Pix payments from the Clara digital account. Brazil only.
  name: Clarafintech Accounts Payable API
  slug: clarafintech-accounts-payable-api
- baseURL: https://public-api.mx.clara.com
  baseurl_source: declared
  description: OAuth token exchange. Requests also require mutual TLS.
  name: Clarafintech Authentication API
  slug: clarafintech-authentication-api
- baseURL: https://public-api.mx.clara.com
  baseurl_source: declared
  description: Retrieve billing statements and statement transactions for reconciliation.
  name: Clarafintech Billing Statements API
  slug: clarafintech-billing-statements-api
- baseURL: https://public-api.mx.clara.com
  baseurl_source: declared
  description: Create, list, retrieve, lock, unlock, update, and cancel corporate cards.
  name: Clarafintech Cards API
  slug: clarafintech-cards-api
- baseURL: https://public-api.mx.clara.com
  baseurl_source: declared
  description: Brazil-only digital account movement search.
  name: Clarafintech Digital Account API
  slug: clarafintech-digital-account-api
- baseURL: https://public-api.mx.clara.com
  baseurl_source: declared
  description: Retrieve structured invoice, receipt, and other document data extracted from transactions.
  name: Clarafintech Extracted Documents API
  slug: clarafintech-extracted-documents-api
- baseURL: https://public-api.mx.clara.com
  baseurl_source: declared
  description: Retrieve Mexico CFDI invoice metadata linked to transactions.
  name: Clarafintech Invoices API
  slug: clarafintech-invoices-api
- baseURL: https://public-api.mx.clara.com
  baseurl_source: declared
  description: Retrieve reimbursement data for out-of-pocket expenses.
  name: Clarafintech Reimbursements API
  slug: clarafintech-reimbursements-api
- baseURL: https://public-api.mx.clara.com
  baseurl_source: declared
  description: Search card transactions and retrieve linked documents or fiscal data.
  name: Clarafintech Transactions API
  slug: clarafintech-transactions-api
- baseURL: https://public-api.mx.clara.com
  baseurl_source: declared
  description: Create, update, retrieve, delete, and filter users by identity, role, status, manager, or location.
  name: Clarafintech Users API
  slug: clarafintech-users-api
artifact_total: 24
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clarafintech/refs/heads/main/agentic-access/clarafintech-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clarafintech-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/clarafintech/refs/heads/main/plans/clarafintech-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clarafintech-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clarafintech/refs/heads/main/rules/clarafintech-rules.yml
  title: ''
  type: Spectral
  url: rules/clarafintech-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clarafintech/refs/heads/main/json-ld/clarafintech-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clarafintech-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clarafintech/refs/heads/main/vocabulary/clarafintech-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clarafintech-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clarafintech/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clarafintech/refs/heads/main/data-model/clarafintech-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clarafintech-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/clarafintech/refs/heads/main/sandbox/clarafintech-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/clarafintech-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.clara.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clarafintech/refs/heads/main/authentication/clarafintech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clarafintech-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clarafintech/refs/heads/main/errors/clarafintech-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clarafintech-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clarafintech/refs/heads/main/conformance/clarafintech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clarafintech-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clarafintech/refs/heads/main/llms/clarafintech-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clarafintech-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clarafintech/refs/heads/main/a2a/clarafintech-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/clarafintech-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clarafintech/refs/heads/main/mcp/clarafintech-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clarafintech-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clarafintech/refs/heads/main/well-known/clarafintech-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clarafintech-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clarafintech/refs/heads/main/hosts/clarafintech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clarafintech-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clarafintech/refs/heads/main/vendors/clarafintech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clarafintech-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clara.com/global/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clara.com/
- group: auth
  title: ''
  type: Security
  url: https://www.clara.com/platform/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clara.com/global/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.clara.com/resources/newsroom
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clarafintech/refs/heads/main/security/clarafintech-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/clarafintech-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clarafintech/refs/heads/main/security/clarafintech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clarafintech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clara.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.clara.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.clara.team
- group: docs
  title: ''
  type: APIReference
  url: https://www.clara.com/products/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.clara.com/resources/switch
- group: operate
  title: ''
  type: Support
  url: https://trust.clara.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clara.com/pricing
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://developers.clara.team/openapi.json
  - status: null
    url: https://developers.clara.team/mcp
  - status: 401
    url: https://api.clara.team/mcp
  - status: 403
    url: https://trust.clara.com/mcp
  - status: 200
    url: https://www.clara.com
  - status: 403
    url: https://equityzen.com/company/clarafintech
  reason: partner-login
  state: gated
created: '2026-10-08'
description: Clarafintech provides spend management and financial automation solutions for businesses in Latin America. The platform offers corporate cards, vendor payments, expense reporting, and AI‑driven insights to help companies control costs, improve compliance, and streamline financial operations across Brazil, Colombia, Mexico and other markets.
image: https://cdn.prod.website-files.com/68ffa900bd486e7d9f3183da/6a29c454934463f06d822c93_Share_Clara%20Global%201200.png
json_schemas:
- name: CardV3
  property_count: 10
  slug: clarafintech-card-v3
- name: CreatePixPaymentRequestV3
  property_count: 5
  slug: clarafintech-create-pix-payment-request-v3
- name: PixPaymentV3
  property_count: 11
  slug: clarafintech-pix-payment-v3
- name: ReimbursementV3
  property_count: 12
  slug: clarafintech-reimbursement-v3
- name: TransactionV3
  property_count: 16
  slug: clarafintech-transaction-v3
- name: UpdateUserRequestV3
  property_count: 13
  slug: clarafintech-update-user-request-v3
jsonld:
- class_count: 50
  name: Clarafintech Context
  property_count: 114
  slug: clarafintech-context
layout: provider
mcp_servers:
- description: Remote MCP server at developers.clara.team.
  name: Clarafintech MCP Server
  slug: clarafintech-mcp-yml
modified: '2026-10-08'
name: Clarafintech
nav: Providers
network: true
overview: 'Clarafintech publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts Payable API, Authentication API, Billing Statements API, and 7 more. Tagged areas include Fintech, Spend Management, Latin America, Corporate Cards, and Financial Automation.


  The Clarafintech catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clarafintech''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, support, pricing, and 25 more developer resources.'
plans:
- name: Clarafintech Plans Pricing
  plan_count: 2
  slug: clarafintech-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: Clarafintech API Rules
  rule_count: 17
  severity_counts:
    error: 12
    hint: 0
    info: 4
    warn: 1
  slug: clarafintech-rules
score:
  band: strong
  composite: 63.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 35.6
    contract_quality: 68.4
    developer_ergonomics: 63.7
    discoverability: 76.7
    operational_transparency: 26.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 33.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 27.8
security:
- kind: authentication
  name: Clarafintech Authentication
  slug: clarafintech-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Clarafintech Domain Security
  slug: clarafintech-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Clarafintech Trust Center
  slug: clarafintech-trust-center
  summary_line: ISO 27001, PCI DSS
slug: clarafintech
tags:
- Fintech
- Spend Management
- Latin America
- Corporate Cards
- Financial Automation
- Company
website: https://www.clara.com
---
