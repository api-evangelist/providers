---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 57.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 7
  name: Qonto Agentic Access
  operation_count: 33
  slug: qonto-agentic-access
  summary_line: 33 operations · 16 acting · 7 human-in-the-loop
api_count: 1
apis:
- baseURL: https://thirdparty.qonto.com/v2
  baseurl_source: declared
  description: The Cards API from Qonto — 1 operation(s) for cards.
  name: Qonto Cards API
  phrasing_intents:
  - id: listCards
    intent: List the organization's payment cards
    question: Which cards have been issued on my Qonto business account?
  - id: createCard
    intent: Issue a new virtual or physical card
    question: How do I issue a new company card for a team member?
  phrasing_ops: 2
  slug: qonto-cards-api
- baseURL: https://thirdparty.qonto.com/v2
  baseurl_source: declared
  description: The Client Invoices API from Qonto — 1 operation(s) for client invoices.
  name: Qonto Client Invoices API
  phrasing_intents:
  - id: listClientInvoices
    intent: List invoices sent to clients
    question: Which invoices have I sent to my customers from Qonto?
  - id: createClientInvoice
    intent: Create an invoice for a client
    question: What's involved in billing a customer with a new client invoice?
  phrasing_ops: 2
  slug: qonto-client-invoices-api
- baseURL: https://thirdparty.qonto.com/v2
  baseurl_source: declared
  description: The Internal Transfers API from Qonto — 1 operation(s) for internal transfers.
  name: Qonto Internal Transfers API
  phrasing_intents:
  - id: createInternalTransfer
    intent: Move money between your own accounts
    question: How do I move money between two of my own business accounts?
  phrasing_ops: 1
  slug: qonto-internal-transfers-api
- baseURL: https://thirdparty.qonto.com/v2
  baseurl_source: declared
  description: The International Transfers API from Qonto — 2 operation(s) for international transfers.
  name: Qonto International Transfers API
  phrasing_intents:
  - id: listInternationalCurrencies
    intent: List currencies available for international transfers
    question: Which currencies can I send money in abroad from Qonto?
  - id: createInternationalTransfer
    intent: Send an international transfer abroad
    question: How do I send money to a bank account outside the SEPA zone?
  phrasing_ops: 2
  slug: qonto-international-transfers-api
- baseURL: https://thirdparty.qonto.com/v2
  baseurl_source: declared
  description: The Organizations & Accounts API from Qonto — 4 operation(s) for organizations & accounts.
  name: Qonto Organizations & Accounts API
  phrasing_intents:
  - id: getOrganization
    intent: Get the organization and its bank accounts
    question: Which bank accounts does my organization have and what are their balances?
  - id: listMemberships
    intent: List members of the organization
    question: Who has access to my company's business account?
  - id: createMembership
    intent: Invite a new member to the organization
    question: Who can I add as a new member of our business account, and how?
  - id: listLabels
    intent: List transaction labels
    question: What labels has my company set up to categorize transactions?
  - id: listTeams
    intent: List teams in the organization
    question: Which teams exist in my company's account?
  - id: createTeam
    intent: Create a new team
    question: Is it possible to set up a new team to group employees?
  phrasing_ops: 6
  slug: qonto-organizations-accounts-api
- baseURL: https://thirdparty.qonto.com/v2
  baseurl_source: declared
  description: The Payment Links API from Qonto — 1 operation(s) for payment links.
  name: Qonto Payment Links API
  phrasing_intents:
  - id: listPaymentLinks
    intent: List payment links
    question: Which payment links have I created to collect money from customers?
  - id: createPaymentLink
    intent: Create a payment link to collect money
    question: Is there a way to create a link customers can use to pay me online?
  phrasing_ops: 2
  slug: qonto-payment-links-api
- baseURL: https://thirdparty.qonto.com/v2
  baseurl_source: declared
  description: The SEPA Direct Debit API from Qonto — 2 operation(s) for sepa direct debit.
  name: Qonto SEPA Direct Debit API
  phrasing_intents:
  - id: createSddMandate
    intent: Create a SEPA Direct Debit mandate
    question: What does it take to set up a SEPA Direct Debit mandate with a customer?
  - id: listSddCollections
    intent: List SEPA Direct Debit collections
    question: Which SEPA Direct Debit payments have I collected from customers?
  phrasing_ops: 2
  slug: qonto-sepa-direct-debit-api
- baseURL: https://thirdparty.qonto.com/v2
  baseurl_source: declared
  description: The SEPA Transfers API from Qonto — 3 operation(s) for sepa transfers.
  name: Qonto SEPA Transfers API
  phrasing_intents:
  - id: listSepaTransfers
    intent: List SEPA transfers
    question: Which SEPA transfers have gone out from my business account?
  - id: createSepaTransfer
    intent: Send a single SEPA transfer in euros
    question: What's needed to send a single euro bank transfer to a supplier?
  - id: createSepaBulkTransfer
    intent: Send a batch of SEPA transfers at once
    question: Can I pay many suppliers in one bulk SEPA transfer?
  - id: listBeneficiaries
    intent: List saved SEPA beneficiaries
    question: Which payees have I saved for SEPA transfers?
  phrasing_ops: 4
  slug: qonto-sepa-transfers-api
- baseURL: https://thirdparty.qonto.com/v2
  baseurl_source: declared
  description: The Supplier Invoices API from Qonto — 2 operation(s) for supplier invoices.
  name: Qonto Supplier Invoices API
  phrasing_intents:
  - id: listSupplierInvoices
    intent: List supplier invoices
    question: Which supplier invoices have been uploaded to my account?
  - id: createSupplierInvoices
    intent: Add supplier invoices
    question: Where do I add bills from my suppliers in Qonto?
  - id: uploadAttachment
    intent: Upload a file attachment
    question: Is there an endpoint to upload a receipt or document file?
  phrasing_ops: 3
  slug: qonto-supplier-invoices-api
- baseURL: https://thirdparty.qonto.com/v2
  baseurl_source: declared
  description: The Terminals API from Qonto — 2 operation(s) for terminals.
  name: Qonto Terminals API
  phrasing_intents:
  - id: listTerminals
    intent: List payment terminals
    question: Which card payment terminals are registered to my business?
  - id: createTerminalPayment
    intent: Start a payment on a terminal
    question: Can I charge a customer in person on a card terminal?
  phrasing_ops: 2
  slug: qonto-terminals-api
- baseURL: https://thirdparty.qonto.com/v2
  baseurl_source: declared
  description: The Webhooks API from Qonto — 2 operation(s) for webhooks.
  name: Qonto Webhooks API
  phrasing_intents:
  - id: listWebhookSubscriptions
    intent: List webhook subscriptions
    question: Which webhook subscriptions are set up on my account?
  - id: createWebhookSubscription
    intent: Subscribe to webhook events
    question: Can I get notified by webhook when a transaction happens?
  - id: deleteWebhookSubscription
    intent: Delete a webhook subscription
    question: What's the way to stop receiving a webhook I no longer need?
  phrasing_ops: 3
  slug: qonto-webhooks-api
- baseURL: https://thirdparty.qonto.com/v2
  baseurl_source: declared
  description: The OAuth API from Qonto — 1 operation(s) for oauth.
  name: Qonto O Auth API
  phrasing_intents:
  - id: createOrRefreshTokens
    intent: Get or refresh an OAuth access token
    question: How do I exchange an authorization code for an access token?
  phrasing_ops: 1
  slug: qonto-oauth-api
- baseURL: https://thirdparty.qonto.com/v2
  baseurl_source: declared
  description: The Transactions and Statements API from Qonto — 3 operation(s) for transactions and statements.
  name: Qonto Transactions and Statements API
  phrasing_intents:
  - id: listTransactions
    intent: List account transactions
    question: Which transactions hit my business account since a certain date?
  - id: getTransaction
    intent: Get one transaction's details
    question: What are the full details of a specific transaction?
  - id: listStatements
    intent: List bank statements
    question: Where can I find my monthly bank statements?
  phrasing_ops: 3
  slug: qonto-transactions-and-statements-api
artifact_total: 59
asyncapis:
- description: ''
  name: Qonto Webhooks
  slug: qonto-webhooks
collections:
- collection_type: postman
  name: Qonto Business Cards API
  slug: postman-qonto-cards-api
- collection_type: postman
  name: Qonto Business Cards Client Invoices API
  slug: postman-qonto-client-invoices-api
- collection_type: postman
  name: Qonto Business Cards Internal Transfers API
  slug: postman-qonto-internal-transfers-api
- collection_type: postman
  name: Qonto Business Cards International Transfers API
  slug: postman-qonto-international-transfers-api
- collection_type: postman
  name: Qonto Business Cards OAuth API
  slug: postman-qonto-oauth-api
- collection_type: postman
  name: Qonto Business Cards Organizations & Accounts API
  slug: postman-qonto-organizations-accounts-api
- collection_type: postman
  name: Qonto Business Cards Payment Links API
  slug: postman-qonto-payment-links-api
- collection_type: postman
  name: Qonto Business Cards SEPA Direct Debit API
  slug: postman-qonto-sepa-direct-debit-api
- collection_type: postman
  name: Qonto Business Cards SEPA Transfers API
  slug: postman-qonto-sepa-transfers-api
- collection_type: postman
  name: Qonto Business Cards Supplier Invoices API
  slug: postman-qonto-supplier-invoices-api
- collection_type: postman
  name: Qonto Business Cards Terminals API
  slug: postman-qonto-terminals-api
- collection_type: postman
  name: Qonto Business Cards Transactions & Statements API
  slug: postman-qonto-transactions-statements-api
- collection_type: postman
  name: Qonto Business Cards Webhooks API
  slug: postman-qonto-webhooks-api
- collection_type: open
  name: Qonto Business Cards API
  slug: open-qonto-cards-api
- collection_type: open
  name: Qonto Business Cards Client Invoices API
  slug: open-qonto-client-invoices-api
- collection_type: open
  name: Qonto Business Cards Internal Transfers API
  slug: open-qonto-internal-transfers-api
- collection_type: open
  name: Qonto Business Cards International Transfers API
  slug: open-qonto-international-transfers-api
- collection_type: open
  name: Qonto Business Cards OAuth API
  slug: open-qonto-oauth-api
- collection_type: open
  name: Qonto Business Cards Organizations & Accounts API
  slug: open-qonto-organizations-accounts-api
- collection_type: open
  name: Qonto Business Cards Payment Links API
  slug: open-qonto-payment-links-api
- collection_type: open
  name: Qonto Business Cards SEPA Direct Debit API
  slug: open-qonto-sepa-direct-debit-api
- collection_type: open
  name: Qonto Business Cards SEPA Transfers API
  slug: open-qonto-sepa-transfers-api
- collection_type: open
  name: Qonto Business Cards Supplier Invoices API
  slug: open-qonto-supplier-invoices-api
- collection_type: open
  name: Qonto Business Cards Terminals API
  slug: open-qonto-terminals-api
- collection_type: open
  name: Qonto Business Cards Transactions & Statements API
  slug: open-qonto-transactions-statements-api
- collection_type: open
  name: Qonto Business Cards Webhooks API
  slug: open-qonto-webhooks-api
common:
- group: design
  href: https://artifacts.apis.io/qonto/rules/qonto-rules.yml
  title: ''
  type: Spectral
  url: rules/qonto-rules.yml
- group: design
  href: https://artifacts.apis.io/qonto/json-ld/qonto-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/qonto-context.jsonld
- group: design
  href: https://artifacts.apis.io/qonto/vocabulary/qonto-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/qonto-vocabulary.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.qonto.com/get-started/general/versioning
- group: other
  href: https://artifacts.apis.io/qonto/a2a/qonto-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/qonto-a2a.yml
- group: other
  href: https://artifacts.apis.io/qonto/hosts/qonto-hosts.yml
  title: ''
  type: Hosts
  url: hosts/qonto-hosts.yml
- group: build
  href: https://artifacts.apis.io/qonto/integrations/qonto-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/qonto-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/qonto/vendors/qonto-vendors.yml
  title: ''
  type: Vendors
  url: vendors/qonto-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://qonto.com/en/press
- group: other
  title: ''
  type: Leadership
  url: https://qonto.com/en/team
- group: other
  href: https://artifacts.apis.io/qonto/capabilities/qonto-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/qonto-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/qonto/overview
- group: auth
  href: https://artifacts.apis.io/qonto/scopes/qonto-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/qonto-scopes.yml
- group: agent
  href: https://artifacts.apis.io/qonto/agentic-access/qonto-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/qonto-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/qonto/security/qonto-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/qonto-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/qonto/security/qonto-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/qonto-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://qonto.com/en/security
- group: auth
  href: https://artifacts.apis.io/qonto/security/qonto-trust-center.yml
  title: ''
  type: Compliance
  url: security/qonto-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/qonto/security/qonto-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/qonto-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/qonto/authentication/qonto-authentication.yml
  title: ''
  type: Authentication
  url: authentication/qonto-authentication.yml
- group: design
  href: https://artifacts.apis.io/qonto/conventions/qonto-conventions.yml
  title: ''
  type: Conventions
  url: conventions/qonto-conventions.yml
- group: design
  href: https://artifacts.apis.io/qonto/conventions/qonto-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/qonto-conventions.yml
- group: design
  href: https://artifacts.apis.io/qonto/errors/qonto-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/qonto-problem-types.yml
- group: design
  href: https://artifacts.apis.io/qonto/lifecycle/qonto-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/qonto-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qonto.com/
- group: operate
  href: https://artifacts.apis.io/qonto/changelog/qonto-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/qonto-changelog.yml
- group: design
  href: https://artifacts.apis.io/qonto/conformance/qonto-conformance.yml
  title: ''
  type: Conformance
  url: conformance/qonto-conformance.yml
- group: design
  href: https://artifacts.apis.io/qonto/data-model/qonto-data-model.yml
  title: ''
  type: DataModel
  url: data-model/qonto-data-model.yml
- group: design
  href: https://artifacts.apis.io/qonto/asyncapi/qonto-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/qonto-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/qonto/mcp/qonto-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/qonto-mcp.yml
- group: agent
  href: https://artifacts.apis.io/qonto/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/qonto/packages/qonto-packages.yml
  title: ''
  type: Packages
  url: packages/qonto-packages.yml
- group: build
  href: https://artifacts.apis.io/qonto/packages/qonto-packages.yml
  title: ''
  type: SDKs
  url: packages/qonto-packages.yml
- group: design
  href: https://artifacts.apis.io/qonto/components/qonto-components.yml
  title: ''
  type: Components
  url: components/qonto-components.yml
- group: start
  href: https://artifacts.apis.io/qonto/sandbox/qonto-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/qonto-sandbox.yml
- group: other
  href: https://artifacts.apis.io/qonto/overlays/qonto-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/qonto-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/qonto/llms/qonto-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/qonto-llms.txt
- group: agent
  href: https://artifacts.apis.io/qonto/well-known/qonto-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/qonto-well-known.yml
- group: auth
  href: https://artifacts.apis.io/qonto/well-known/qonto-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/qonto-security.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qonto
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qonto
- group: company
  title: ''
  type: Website
  url: https://qonto.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.qonto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qonto.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.qonto.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.qonto.com/get-started/business-api/overview
- group: operate
  title: ''
  type: Support
  url: https://help.qonto.com/
- group: build
  href: https://artifacts.apis.io/qonto/collections/qonto.postman_collection.json
  title: ''
  type: Postman
  url: collections/qonto.postman_collection.json
- group: commercial
  title: ''
  type: Pricing
  url: https://qonto.com/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.qonto.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.qonto.com/en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.qonto.com/en
- group: commercial
  href: https://artifacts.apis.io/qonto/plans/qonto-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/qonto-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/qonto/rate-limits/qonto-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/qonto-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/qonto/finops/qonto-finops.yml
  title: ''
  type: FinOps
  url: finops/qonto-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://qonto.com/en/blog
created: '2026-07-17'
description: Qonto is a European business banking / neobank platform for freelancers and SMEs, founded in Paris in 2016 and operating on an EU-passported payment institution licence. Its Business API and Onboarding API give programmatic access to business accounts, EUR transactions, SEPA and international transfers, cards, client and supplier invoices, SEPA Direct Debit, payment links, terminals, webhooks, and partner-led company onboarding, authenticated by a login+secret-key API key or OAuth 2.0.
finops:
- has_sources: true
  method: derived
  name: Qonto Finops
  primary_unit: account
  service_category: ''
  slug: qonto-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qonto.png
json_schemas:
- name: SepaTransferRequest
  property_count: 8
  slug: qonto-sepa-transfer-request
- name: TokenSet
  property_count: 6
  slug: qonto-token-set
jsonld:
- class_count: 2
  name: Qonto Context
  property_count: 14
  slug: qonto-context
layout: provider
mcp_servers:
- description: 'Officially supported, actively maintained Qonto MCP server. Lets an AI assistant read and act on Qonto business-banking data through a curated set of tools. Built on top of the Qonto Business API and '
  name: Qonto MCP Server
  slug: qonto
modified: '2026-10-12'
name: Qonto
nav: Providers
network: true
overview: 'Qonto publishes 13 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cards API, Client Invoices API, Internal Transfers API, and 10 more. Tagged areas include Business Banking, Neobank, Fintech, Payments, and SEPA.


  The Qonto catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Qonto''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, support, and 49 more developer resources.'
plans:
- name: Qonto Plans Pricing
  plan_count: 10
  slug: qonto-plans-pricing
- name: Qonto Price Estimates
  plan_count: 0
  slug: qonto-price-estimates
random_paper: 9
rate_limits:
- limit_count: 3
  name: Qonto Rate Limits
  slug: qonto-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Qonto API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: qonto-rules
scopes:
- name: Qonto Scopes
  scope_count: 35
  slug: qonto-scopes
  summary_line: 35 scopes · authorizationCode
score:
  band: exemplar
  composite: 73.2
  coverage:
    artifact_dirs: 40
    catalog_earned: 83.2
    catalog_earned_first_party: 24.0
    catalog_gap: 31.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.6
  facets:
    access_clarity: 86.8
    contract_governance: 22.0
    contract_quality: 65.7
    developer_ergonomics: 72.0
    discoverability: 76.7
    operational_transparency: 88.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 73.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 46.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/qonto/qonto-2026-08-17T075403.png
security:
- kind: authentication
  name: Qonto Authentication
  slug: qonto-authentication
  summary_line: apiKey/oauth2/mtls · 3 schemes
- kind: domain-security
  name: Qonto Domain Security
  slug: qonto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Qonto Vulnerability Disclosure
  slug: qonto-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Qonto Trust Center
  slug: qonto-trust-center
  summary_line: GDPR
skill_count: 4
skills:
- name: qonto-create-sepa-transfer
  slug: qonto-create-sepa-transfer
- name: qonto-issue-card
  slug: qonto-issue-card
- name: qonto-list-and-reconcile-transactions
  slug: qonto-list-and-reconcile-transactions
- name: qonto-send-client-invoice
  slug: qonto-send-client-invoice
slug: qonto
tags:
- Business Banking
- Neobank
- Fintech
- Payments
- SEPA
- Open Banking
- EUR
- Europe
website: https://qonto.com/
---
