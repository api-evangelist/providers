---
agent_readiness:
  band: agent-aware
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Weel Agentic Access
  operation_count: 51
  slug: weel-agentic-access
  summary_line: 51 operations · 27 acting
api_count: 1
apis:
- description: This group of endpoints allows you to manage GL codes (accounting codes) for your business. GL codes are used to classify expenses for bookkeeping export. Businesses with a connected accounting integr
  name: Weel Accounting Codes API
  slug: weel-accounting-codes-api
- description: This group of endpoints allows you to retrieve and manage budget member data, including listing budget members and fetching individual budget member details.
  name: Weel Budget Members API
  slug: weel-budget-members-api
- description: This group of endpoints allows you to retrieve and manage budget owners. A budget owner is a user (or pending invite) who can approve spend, top up, and otherwise manage the budget. A budget must alwa
  name: Weel Budget Owners API
  slug: weel-budget-owners-api
- description: This group of endpoints allows you to retrieve and create budget topups. Topups are used to increase or decrease the available amount of a budget or budget member. Topups will be automatically approve
  name: Weel Budget Topups API
  slug: weel-budget-topups-api
- description: This group of endpoints allows you to retrieve and manage budget data, including listing budgets and fetching individual budget details. Budgets are organised in a hierarchy where a budget can have mu
  name: Weel Budgets API
  slug: weel-budgets-api
- description: 'This group of endpoints allow you to manage expense categories for your business. Categories classify transactions. System-defined categories (`custom: false`) can only have their `enabled` state togg'
  name: Weel Categories API
  slug: weel-categories-api
- description: This group of endpoints allows you to link custom fields to budgets, controlling which budgets have a custom field assigned.
  name: Weel Custom Field Budgets API
  slug: weel-custom-field-budgets-api
- description: This group of endpoints allows you to manage the list options for a `LIST` type custom field. Options created via the Public API can be disabled or deleted.
  name: Weel Custom Field Options API
  slug: weel-custom-field-options-api
- description: 'This group of endpoints allows you to create and manage custom fields (dimensions/cost centres) for your business. Custom fields can be of type `LIST` (with predefined options) or `FREE_TEXT`. Custom '
  name: Weel Custom Fields API
  slug: weel-custom-fields-api
- description: This group of endpoints allows you to create, list, and cancel pending user invitations. An invite exists until the recipient accepts it, at which point they appear as a user in the Users endpoints.
  name: Weel Invites API
  slug: weel-invites-api
- description: This group of endpoints allows you to retrieve the roles available within a business and the permissions assigned to each role.
  name: Weel Roles API
  slug: weel-roles-api
- description: This group of endpoints allows you to retrieve a list of balances for the required period for a given business.
  name: Weel Statements API
  slug: weel-statements-api
- description: This group of endpoints allows you to retrieve the tax rates configured for your business. Tax rates are read-only via the Public API. For businesses with a connected accounting integration (Xero, MYO
  name: Weel Tax Rates API
  slug: weel-tax-rates-api
- description: This group of endpoints allows you to retrieve and manage transaction data, including listing transactions with various filters and fetching individual transaction details.
  name: Weel Transactions API
  slug: weel-transactions-api
- description: This group of endpoints allows you to retrieve and manage user data, including listing users and fetching individual user details.
  name: Weel Users API
  slug: weel-users-api
artifact_total: 22
collections:
- collection_type: open
  name: Weel OpenAPI
  slug: open-weel
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/weel-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/weel-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/weel-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/weel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/weel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/weel-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://letsweel.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.letsweel.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.letsweel.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.letsweel.com/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.letsweel.com/getting-started/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://letsweel.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://letsweel.com/product-updates
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.letsweel.com/
- group: auth
  title: ''
  type: Compliance
  url: security/weel-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/weel-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/weel-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/weel-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/weel-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/weel-changelog.yml
- group: operate
  title: ''
  type: Support
  url: https://help.letsweel.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://letsweel.com/resources/the-weelhouse
- group: commercial
  title: ''
  type: TermsOfService
  url: https://letsweel.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://letsweel.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.letsweel.com/app/business-signup
created: '2026-07-24'
description: Weel (formerly DiviPay, operated by Weel Pty Ltd) is a Melbourne-based all-in-one spend management platform for finance teams in Australia and New Zealand, serving over 4,000 finance teams and 60,000+ card holders. Weel issues virtual and physical Visa debit cards with real-time limits and controls, and layers accounts payable automation, expense management, reimbursements, subscription management, budgets, and approval policies on top. Rather than operating payment rails directly, Weel sits on the spend and AP/AR seam, syncing approved spend into Xero, QuickBooks, MYOB, and NetSuite. On the API posture, Weel ships a genuine public developer portal at developer.letsweel.com (Redocly-based) documenting a single RESTful "Weel Open API" that both reads and writes budgets, users, transactions, custom fields, accounting codes, categories, invites, and top-ups, authenticated with a bearer API key generated in-app. API access is an Enterprise-tier capability. No public webhooks, Postman
  collection, or OAuth flow are documented as of this review.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: Weel MCP Server
  slug: weel-mcp-server
modified: '2026-07-24'
name: Weel
nav: Providers
network: true
overview: 'Weel publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Accounting Codes API, Budget Members API, Budget Owners API, and 12 more. Tagged areas include Payments, Australia, Spend Management, Expense Management, and Corporate Cards.


  Weel''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, changelog, support, and 19 more developer resources.'
random_paper: 9
score:
  band: strong
  composite: 55.0
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 57.4
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 55.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/weel/refs/heads/main/screenshots/weel-2026-08-17T082857.png
security:
- kind: authentication
  name: Weel Authentication
  slug: weel-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Weel Domain Security
  slug: weel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Weel Vulnerability Disclosure
  slug: weel-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Weel Trust Center
  slug: weel-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2, ISO 27001:2022
slug: weel
tags:
- Payments
- Australia
- Spend Management
- Expense Management
- Corporate Cards
- Accounts Payable
- Card Issuing
- Reimbursement
- Budgets
- Fintech
website: https://letsweel.com/
---
