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
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: flavored
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
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 65.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 62
  human_in_the_loop: 1
  name: Meow Agentic Access
  operation_count: 119
  slug: meow-agentic-access
  summary_line: 119 operations · 62 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: Access and manage accounts.
  name: Meow Accounts API
  slug: meow-accounts-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: Retrieve metadata about API keys and their accessible entities.
  name: Meow API Keys API
  slug: meow-api-keys-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: The Approvals API from Meow — 1 operation(s) for approvals.
  name: Meow Approvals API
  slug: meow-approvals-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: Retrieve account balances and available funds.
  name: Meow Balances API
  slug: meow-balances-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: View and manage bills for vendor payments.
  name: Meow Bills API
  slug: meow-bills-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: Manage virtual and physical cards, and view transactions and insights.
  name: Meow Cards API
  slug: meow-cards-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: Manage accounts for payment collection.
  name: Meow Collection Accounts API
  slug: meow-collection-accounts-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: Manage contacts for crypto and USDC transfers.
  name: Meow Contacts API
  slug: meow-contacts-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: Manage invoicing customers and their details.
  name: Meow Customers API
  slug: meow-customers-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: The Entities API from Meow — 12 operation(s) for entities.
  name: Meow Entities API
  slug: meow-entities-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: The Health API from Meow — 1 operation(s) for health.
  name: Meow Health API
  slug: meow-health-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: Create and manage invoices.
  name: Meow Invoices API
  slug: meow-invoices-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: The Limits API from Meow — 1 operation(s) for limits.
  name: Meow Limits API
  slug: meow-limits-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: Manage invoice line items.
  name: Meow Line Items API
  slug: meow-line-items-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: Onboard entities using your partner API key.
  name: Meow Partner Onboarding API
  slug: meow-partner-onboarding-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: The Partner Webhooks API from Meow — 6 operation(s) for partner webhooks.
  name: Meow Partner Webhooks API
  slug: meow-partner-webhooks-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: View available payment method types.
  name: Meow Payment Methods API
  slug: meow-payment-methods-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: Manage payment networks and routing information.
  name: Meow Payment Networks API
  slug: meow-payment-networks-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: Manage products and pricing for invoicing.
  name: Meow Products API
  slug: meow-products-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: Validate routing numbers and retrieve bank information.
  name: Meow Routing Numbers API
  slug: meow-routing-numbers-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: The Security Policies API from Meow — 1 operation(s) for security policies.
  name: Meow Security Policies API
  slug: meow-security-policies-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: 'Trigger simulated events — inbound transfers, card authorizations, application approval — to test integrations end-to-end without real money movement. **Not available in production**: these endpoints '
  name: Meow Simulations API
  slug: meow-simulations-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: Retrieve IRS tax forms (1099 family) issued for accounts.
  name: Meow Tax Forms API
  slug: meow-tax-forms-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: Retrieve account transaction history and details.
  name: Meow Transactions API
  slug: meow-transactions-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: Initiate ACH, wire, book, and crypto transfers, and retrieve transfer details.
  name: Meow Transfers API
  slug: meow-transfers-api
- baseURL: https://api.meow.com/v1
  baseurl_source: spec
  description: Manage webhook subscriptions and inspect delivery history.
  name: Meow Webhooks API
  slug: meow-webhooks-api
artifact_total: 64
asyncapis:
- description: ''
  name: Meow Webhooks
  slug: meow-webhooks
collections:
- collection_type: open
  name: Meow Accounts API
  slug: open-meow-accounts-api
- collection_type: open
  name: Meow Accounts API Keys API
  slug: open-meow-api-keys-api
- collection_type: open
  name: Meow Accounts Approvals API
  slug: open-meow-approvals-api
- collection_type: open
  name: Meow Accounts Balances API
  slug: open-meow-balances-api
- collection_type: open
  name: Meow Accounts Bills API
  slug: open-meow-bills-api
- collection_type: open
  name: Meow Accounts Cards API
  slug: open-meow-cards-api
- collection_type: open
  name: Meow Accounts Collection Accounts API
  slug: open-meow-collection-accounts-api
- collection_type: open
  name: Meow Accounts Contacts API
  slug: open-meow-contacts-api
- collection_type: open
  name: Meow Accounts Customers API
  slug: open-meow-customers-api
- collection_type: open
  name: Meow Accounts Entities API
  slug: open-meow-entities-api
- collection_type: open
  name: Meow Accounts Health API
  slug: open-meow-health-api
- collection_type: open
  name: Meow Accounts Invoices API
  slug: open-meow-invoices-api
- collection_type: open
  name: Meow Accounts Limits API
  slug: open-meow-limits-api
- collection_type: open
  name: Meow Accounts Line Items API
  slug: open-meow-line-items-api
- collection_type: open
  name: Meow Accounts Partner Onboarding API
  slug: open-meow-partner-onboarding-api
- collection_type: open
  name: Meow Accounts Partner Webhooks API
  slug: open-meow-partner-webhooks-api
- collection_type: open
  name: Meow Accounts Payment Methods API
  slug: open-meow-payment-methods-api
- collection_type: open
  name: Meow Accounts Payment Networks API
  slug: open-meow-payment-networks-api
- collection_type: open
  name: Meow Accounts Products API
  slug: open-meow-products-api
- collection_type: open
  name: Meow Accounts Routing Numbers API
  slug: open-meow-routing-numbers-api
- collection_type: open
  name: Meow Accounts Security Policies API
  slug: open-meow-security-policies-api
- collection_type: open
  name: Meow Accounts Simulations API
  slug: open-meow-simulations-api
- collection_type: open
  name: Meow Accounts Tax Forms API
  slug: open-meow-tax-forms-api
- collection_type: open
  name: Meow Accounts Transactions API
  slug: open-meow-transactions-api
- collection_type: open
  name: Meow Accounts Transfers API
  slug: open-meow-transfers-api
- collection_type: open
  name: Meow Accounts Webhooks API
  slug: open-meow-webhooks-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/meow/overview
- group: company
  title: ''
  type: Blog
  url: https://www.meow.com/blog
- group: other
  href: https://artifacts.apis.io/meow/capabilities/meow-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/meow-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/meow/skills/meow-create-and-send-invoice.md
  title: ''
  type: AgentSkill
  url: skills/meow-create-and-send-invoice.md
- group: agent
  href: https://artifacts.apis.io/meow/mcp/meow-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/meow-mcp.yml
- group: other
  href: https://artifacts.apis.io/meow/overlays/meow-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/meow-openapi-overlay.yaml
- group: other
  href: https://artifacts.apis.io/meow/a2a/meow-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/meow-a2a.yml
- group: company
  title: ''
  type: Website
  url: http://www.meow.com
created: '2026-07-17'
description: 'Meow is a company surfaced as a portfolio company of qed-investors and added to the API Evangelist network as a stub for enrichment. Sector: banking. This profile is a lead awaiting the enrichment pipeline.'
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.meow.com over HTTP; 47 tools listed.
  name: Meow MCP Server
  slug: meow
modified: '2026-10-06'
name: Meow
nav: Providers
network: true
overview: 'Meow publishes 26 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, API Keys API, Approvals API, and 23 more. Tagged areas include Company, Banking, and A2A.


  The Meow catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Meow''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 115
  extends:
  - spectral:oas
  name: Meow API Rules
  rule_count: 74
  severity_counts:
    error: 61
    hint: 0
    info: 2
    warn: 11
  slug: meow-rules
scopes:
- name: Meow Scopes
  scope_count: 0
  slug: meow-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 24.5
    catalog_earned_first_party: 0.0
    catalog_gap: 90.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 62.9
    developer_ergonomics: 5.4
    discoverability: 46.7
    operational_transparency: 0.0
  previous_composite: 26.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 26
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 24.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/meow/meow-2026-08-07T172630.png
security:
- kind: authentication
  name: Meow Authentication
  slug: meow-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Meow Domain Security
  slug: meow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 5
skills:
- name: Create and send an invoice
  slug: meow-create-and-send-invoice
- name: Draft an ACH transfer for approval
  slug: meow-draft-ach-transfer
- name: Issue and manage a virtual card
  slug: meow-issue-virtual-card
- name: Onboard a business entity (KYB)
  slug: meow-onboard-business-entity
- name: Subscribe to and verify webhooks
  slug: meow-subscribe-webhooks
slug: meow
tags:
- Company
- Banking
- A2A
website: http://www.meow.com
---
