---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 16
  human_in_the_loop: 7
  name: Qonto Agentic Access
  operation_count: 33
  slug: qonto-agentic-access
  summary_line: 33 operations · 16 acting · 7 human-in-the-loop
api_count: 13
apis:
- description: The Cards API from Qonto — 1 operation(s) for cards.
  name: Qonto Cards API
  slug: qonto-cards-api
- description: The Client Invoices API from Qonto — 1 operation(s) for client invoices.
  name: Qonto Client Invoices API
  slug: qonto-client-invoices-api
- description: The Internal Transfers API from Qonto — 1 operation(s) for internal transfers.
  name: Qonto Internal Transfers API
  slug: qonto-internal-transfers-api
- description: The International Transfers API from Qonto — 2 operation(s) for international transfers.
  name: Qonto International Transfers API
  slug: qonto-international-transfers-api
- description: The OAuth API from Qonto — 1 operation(s) for oauth.
  name: Qonto OAuth API
  slug: qonto-oauth-api
- description: The Organizations & Accounts API from Qonto — 4 operation(s) for organizations & accounts.
  name: Qonto Organizations & Accounts API
  slug: qonto-organizations-accounts-api
- description: The Payment Links API from Qonto — 1 operation(s) for payment links.
  name: Qonto Payment Links API
  slug: qonto-payment-links-api
- description: The SEPA Direct Debit API from Qonto — 2 operation(s) for sepa direct debit.
  name: Qonto SEPA Direct Debit API
  slug: qonto-sepa-direct-debit-api
- description: The SEPA Transfers API from Qonto — 3 operation(s) for sepa transfers.
  name: Qonto SEPA Transfers API
  slug: qonto-sepa-transfers-api
- description: The Supplier Invoices API from Qonto — 2 operation(s) for supplier invoices.
  name: Qonto Supplier Invoices API
  slug: qonto-supplier-invoices-api
- description: The Terminals API from Qonto — 2 operation(s) for terminals.
  name: Qonto Terminals API
  slug: qonto-terminals-api
- description: The Transactions & Statements API from Qonto — 3 operation(s) for transactions & statements.
  name: Qonto Transactions & Statements API
  slug: qonto-transactions-statements-api
- description: The Webhooks API from Qonto — 2 operation(s) for webhooks.
  name: Qonto Webhooks API
  slug: qonto-webhooks-api
artifact_total: 51
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
  name: API Collection
  slug: open-.refine-report
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
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/qonto/overview
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/qonto-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qonto-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/qonto-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/qonto-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://qonto.com/en/security
- group: auth
  title: ''
  type: Compliance
  url: security/qonto-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qonto-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qonto-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qonto-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/qonto-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qonto-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qonto-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qonto.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/qonto-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/qonto-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qonto-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/qonto-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/qonto-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/qonto-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/qonto-packages.yml
- group: design
  title: ''
  type: Components
  url: components/qonto-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/qonto-sandbox.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/qonto-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qonto-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/qonto-well-known.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/qonto-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qonto-rate-limits.yml
- group: commercial
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
- name: Qonto Finops
  service_category: Financial Services
  slug: qonto-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qonto.png
layout: provider
mcp_servers:
- description: 'Officially supported, actively maintained Qonto MCP server. Lets an AI assistant read and act on Qonto business-banking data through a curated set of tools. Built on top of the Qonto Business API and '
  name: Qonto MCP Server
  slug: qonto-mcp-server
modified: '2026-07-17'
name: Qonto
nav: Providers
network: true
overview: 'Qonto publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Cards API, Client Invoices API, Internal Transfers API, and 10 more. Tagged areas include Business Banking, Neobank, Fintech, Payments, and SEPA.


  The Qonto catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Qonto''s developer surface includes authentication, changelog, sandbox, documentation, API reference, getting-started guide, support, and 38 more developer resources.'
plans:
- name: Qonto Plans Pricing
  plan_count: 6
  slug: qonto-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 3
  name: Qonto Rate Limits
  slug: qonto-rate-limits
scopes:
- name: Qonto Scopes
  scope_count: 35
  slug: qonto-scopes
  summary_line: 35 scopes · authorizationCode
score:
  band: exemplar
  composite: 74.6
  delta: 0.0
  facets:
    access_clarity: 86.8
    commercial_clarity: 86.8
    contract_governance: 16.7
    contract_quality: 63.0
    developer_ergonomics: 75.6
    discoverability: 68.5
    governance: 16.7
    operational_transparency: 84.2
  previous_composite: 74.6
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
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 74.7
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qonto/refs/heads/main/screenshots/qonto-2026-08-17T075403.png
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
