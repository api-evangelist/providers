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
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Astrada Agentic Access
  operation_count: 50
  slug: astrada-agentic-access
  summary_line: 50 operations · 21 acting
api_count: 1
apis:
- baseURL: https://api.astrada.co
  baseurl_source: declared
  description: Manage connected bank accounts. Bank accounts are created automatically when a bank link enrollment is completed.
  name: Astrada bank-accounts API
  slug: astrada-bank-accounts-api
- baseURL: https://api.astrada.co
  baseurl_source: declared
  description: Manage bank enrollment links. A bank link represents an invitation for a user to connect their bank account via Plaid.
  name: Astrada bank-links API
  slug: astrada-bank-links-api
- baseURL: https://api.astrada.co
  baseurl_source: declared
  description: Manage bank subscriptions (Plaid connections). A subscription represents an active connection to a financial institution.
  name: Astrada bank-subscriptions API
  slug: astrada-bank-subscriptions-api
- baseURL: https://api.astrada.co
  baseurl_source: declared
  description: Access bank transactions synced from connected accounts. Transactions are ingested via Plaid and can be matched against card transactions.
  name: Astrada bank-transactions API
  slug: astrada-bank-transactions-api
- baseURL: https://api.astrada.co
  baseurl_source: declared
  description: BIN Lookup
  name: Astrada bin-lookup API
  slug: astrada-bin-lookup-api
- baseURL: https://api.astrada.co
  baseurl_source: declared
  description: Card resource
  name: Astrada card API
  slug: astrada-card-api
- baseURL: https://api.astrada.co
  baseurl_source: declared
  description: Card Subscription resource
  name: Astrada card-subscription API
  slug: astrada-card-subscription-api
- baseURL: https://api.astrada.co
  baseurl_source: declared
  description: Card Verification
  name: Astrada card-verification API
  slug: astrada-card-verification-api
- baseURL: https://api.astrada.co
  baseurl_source: declared
  description: Enrollment methods resource
  name: Astrada enrollment-methods API
  slug: astrada-enrollment-methods-api
- baseURL: https://api.astrada.co
  baseurl_source: declared
  description: Network bulk feed resource
  name: Astrada network-bulk-feeds API
  slug: astrada-network-bulk-feeds-api
- baseURL: https://api.astrada.co
  baseurl_source: declared
  description: Subaccount resource
  name: Astrada subaccounts API
  slug: astrada-subaccounts-api
- baseURL: https://api.astrada.co
  baseurl_source: declared
  description: Access transaction matches between bank and card transactions, including confidence scores and match reasoning.
  name: Astrada transaction-matches API
  slug: astrada-transaction-matches-api
- baseURL: https://api.astrada.co
  baseurl_source: declared
  description: Transaction messages resource
  name: Astrada transaction-messages API
  slug: astrada-transaction-messages-api
- baseURL: https://api.astrada.co
  baseurl_source: declared
  description: Transaction resource
  name: Astrada transactions API
  slug: astrada-transactions-api
- baseURL: https://api.astrada.co
  baseurl_source: declared
  description: Manage webhooks
  name: Astrada webhooks API
  slug: astrada-webhooks-api
artifact_total: 55
asyncapis:
- description: Webhook event surface for the Astrada API, generated from the documented Event Types and webhook delivery mechanics. Astrada delivers events via HTTP POST to registered HTTPS endpoints with at-least-o
  name: Astrada Webhook Events
  slug: astrada-events-asyncapi
- description: ''
  name: Astrada Webhooks
  slug: astrada-webhooks
collections:
- collection_type: postman
  name: Astrada bank-accounts API
  slug: postman-astrada-bank-accounts-api
- collection_type: postman
  name: Astrada bank-accounts bank-links API
  slug: postman-astrada-bank-links-api
- collection_type: postman
  name: Astrada bank-accounts bank-subscriptions API
  slug: postman-astrada-bank-subscriptions-api
- collection_type: postman
  name: Astrada bank-accounts bank-transactions API
  slug: postman-astrada-bank-transactions-api
- collection_type: postman
  name: Astrada bank-accounts bin-lookup API
  slug: postman-astrada-bin-lookup-api
- collection_type: postman
  name: Astrada bank-accounts card API
  slug: postman-astrada-card-api
- collection_type: postman
  name: Astrada bank-accounts card-subscription API
  slug: postman-astrada-card-subscription-api
- collection_type: postman
  name: Astrada bank-accounts card-verification API
  slug: postman-astrada-card-verification-api
- collection_type: postman
  name: Astrada bank-accounts enrollment-methods API
  slug: postman-astrada-enrollment-methods-api
- collection_type: postman
  name: Astrada bank-accounts network-bulk-feeds API
  slug: postman-astrada-network-bulk-feeds-api
- collection_type: postman
  name: Astrada bank-accounts subaccounts API
  slug: postman-astrada-subaccounts-api
- collection_type: postman
  name: Astrada bank-accounts transaction-matches API
  slug: postman-astrada-transaction-matches-api
- collection_type: postman
  name: Astrada bank-accounts transaction-messages API
  slug: postman-astrada-transaction-messages-api
- collection_type: postman
  name: Astrada bank-accounts transactions API
  slug: postman-astrada-transactions-api
- collection_type: postman
  name: Astrada bank-accounts webhooks API
  slug: postman-astrada-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Astrada bank-accounts API
  slug: open-astrada-bank-accounts-api
- collection_type: open
  name: Astrada bank-accounts bank-links API
  slug: open-astrada-bank-links-api
- collection_type: open
  name: Astrada bank-accounts bank-subscriptions API
  slug: open-astrada-bank-subscriptions-api
- collection_type: open
  name: Astrada bank-accounts bank-transactions API
  slug: open-astrada-bank-transactions-api
- collection_type: open
  name: Astrada bank-accounts bin-lookup API
  slug: open-astrada-bin-lookup-api
- collection_type: open
  name: Astrada bank-accounts card API
  slug: open-astrada-card-api
- collection_type: open
  name: Astrada bank-accounts card-subscription API
  slug: open-astrada-card-subscription-api
- collection_type: open
  name: Astrada bank-accounts card-verification API
  slug: open-astrada-card-verification-api
- collection_type: open
  name: Astrada bank-accounts enrollment-methods API
  slug: open-astrada-enrollment-methods-api
- collection_type: open
  name: Astrada bank-accounts network-bulk-feeds API
  slug: open-astrada-network-bulk-feeds-api
- collection_type: open
  name: Astrada bank-accounts subaccounts API
  slug: open-astrada-subaccounts-api
- collection_type: open
  name: Astrada bank-accounts transaction-matches API
  slug: open-astrada-transaction-matches-api
- collection_type: open
  name: Astrada bank-accounts transaction-messages API
  slug: open-astrada-transaction-messages-api
- collection_type: open
  name: Astrada bank-accounts transactions API
  slug: open-astrada-transactions-api
- collection_type: open
  name: Astrada bank-accounts webhooks API
  slug: open-astrada-webhooks-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/astrada-openapi-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/astrada/overview
- group: company
  title: ''
  type: Website
  url: https://astrada.co/
- group: start
  title: ''
  type: Portal
  url: https://docs.astrada.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.astrada.co/docs/home
- group: docs
  title: ''
  type: APIReference
  url: https://docs.astrada.co/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.astrada.co/docs/getting-started-1
- group: company
  title: ''
  type: Blog
  url: https://astrada.co/blog
- group: operate
  title: ''
  type: Support
  url: https://astrada.co/company/contact
- group: start
  title: ''
  type: SignUp
  url: https://astrada.co/company/contact
- group: operate
  title: ''
  type: StatusPage
  url: https://status.astrada.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://astrada.co/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://astrada.co/legal
- group: auth
  title: ''
  type: Security
  url: https://astrada.co/security
- group: auth
  title: ''
  type: Compliance
  url: https://astrada.co/security
- group: auth
  title: ''
  type: Authentication
  url: authentication/astrada-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/astrada-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/astrada-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/astrada-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/astrada-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/astrada-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/astrada-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/astrada-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/astrada-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/astrada-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/astrada-conformance.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/astrada-events-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/astrada-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/astrada-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/astrada-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/astrada-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/astrada-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/astrada-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/astrada-trust-center.yml
created: '2026-07-17'
description: Astrada is the data layer for autonomous finance, providing real-time, structured card transaction data pulled directly from the card networks rather than relying on delayed bank feeds. Its Transaction Data API lets expense management, travel, and accounting/ERP platforms enroll corporate cards (with 3DS cardholder verification), receive real-time transaction messages and enriched transactions, link bank accounts, and auto-reconcile card-to-bank activity. Founded in 2024 by Salman Syed (ex-Mastercard, Marqeta, Fidel API), Astrada is PCI DSS v4 Level 1 certified, a Mastercard Start Path and Visa Ventures portfolio company, and is backed by QED Investors.
image: https://files.readme.io/45785f4-brandmark-blue.svg
layout: provider
mcp_servers:
- description: ''
  name: Astrada MCP Server
  slug: astrada-mcp-server
modified: '2026-07-18'
name: Astrada
nav: Providers
network: true
overview: 'Astrada publishes 15 APIs on the [APIs.io](https://apis.io/) network, including bank-accounts API, bank-links API, bank-subscriptions API, and 12 more. Tagged areas include Company, Fintech, Payments, Card Data, and Transaction Data.


  The Astrada catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Astrada''s developer surface includes developer portal, documentation, API reference, getting-started guide, engineering blog, support, signup flow, and 28 more developer resources.'
random_paper: 1
scopes:
- name: Astrada Scopes
  scope_count: 34
  slug: astrada-scopes
  summary_line: 34 scopes · implicit
score:
  band: strong
  composite: 61.2
  coverage:
    artifact_dirs: 23
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 63.4
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 61.2
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
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 84.4
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/astrada/refs/heads/main/screenshots/astrada-2026-07-25T201455.png
security:
- kind: authentication
  name: Astrada Authentication
  slug: astrada-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Astrada Domain Security
  slug: astrada-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Astrada Vulnerability Disclosure
  slug: astrada-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Astrada Trust Center
  slug: astrada-trust-center
  summary_line: PCI DSS v4 Level 1 Service Provider, GDPR, CCPA
slug: astrada
tags:
- Company
- Fintech
- Payments
- Card Data
- Transaction Data
- Reconciliation
- Expense Management
- Data Infrastructure
website: https://astrada.co/
---
