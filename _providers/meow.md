---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.0
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 63
  human_in_the_loop: 1
  name: Meow Agentic Access
  operation_count: 119
  slug: meow-agentic-access
  summary_line: 119 operations · 63 acting · 1 human-in-the-loop
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
artifact_total: 59
asyncapis:
- description: ''
  name: Meow Webhooks
  slug: meow-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/meow-capability-edges.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/meow-create-and-send-invoice.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/meow-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/meow-openapi-overlay.yaml
- group: other
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
- description: ''
  name: Meow MCP Server
  slug: meow-mcp-server
modified: '2026-07-17'
name: Meow
nav: Providers
network: true
overview: 'Meow publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, API Keys API, Approvals API, and 23 more. Tagged areas include Company and Banking.


  The Meow catalog on APIs.io includes 1 event-driven AsyncAPI specification.'
random_paper: 20
scopes:
- name: Meow Scopes
  scope_count: 0
  slug: meow-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 23
    catalog_gap: 95.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 68.7
    developer_ergonomics: 1.8
    discoverability: 44.4
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 22.6
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
    score: 31.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/meow/refs/heads/main/screenshots/meow-2026-08-07T172630.png
security:
- kind: authentication
  name: Meow Authentication
  slug: meow-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Meow Domain Security
  slug: meow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: meow
tags:
- Company
- Banking
website: http://www.meow.com
---
