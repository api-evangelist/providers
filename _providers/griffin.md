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
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 42
  human_in_the_loop: 1
  name: Griffin Agentic Access
  operation_count: 97
  slug: griffin-agentic-access
  summary_line: 97 operations · 42 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: The `api-key-secret` field is only shown once when you create an API key. We cannot recover the value, so you should store it securely. Pass an `Authorization` header with `GriffinAPIKey api-key-secre
  name: Griffin API keys API
  slug: griffin-api-keys-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: The Bank account holds API from Griffin — 2 operation(s) for bank account holds.
  name: Griffin Bank account holds API
  slug: griffin-bank-account-holds-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: Restrictions prevent payments on a bank account. A `freeze` blocks outbound payments while still allowing inbound payments. A `block` prevents both inbound and outbound payments. Restrictions can be a
  name: Griffin Bank account restrictions API
  slug: griffin-bank-account-restrictions-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: Bank accounts are used for managing funds. Every bank account is opened against a [bank product](/docs/guides/bank-products), which determines the account's behaviour (type, pooled vs dedicated, inter
  name: Griffin Bank accounts API
  slug: griffin-bank-accounts-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: 'A [claim](/docs/terms/claim) is an unverified data point or series of data points attached to a [legal person](#tag/Legal-persons). Claims are verified by running a [verification](#tag/Verifications) '
  name: Griffin Claims API
  slug: griffin-claims-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: The Companies House API from Griffin — 1 operation(s) for companies house.
  name: Griffin Companies House API
  slug: griffin-companies-house-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: The Confirmation of payee API from Griffin — 2 operation(s) for confirmation of payee.
  name: Griffin Confirmation of payee API
  slug: griffin-confirmation-of-payee-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: The Connectivity API from Griffin — 1 operation(s) for connectivity.
  name: Griffin Connectivity API
  slug: griffin-connectivity-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: The Decisions API from Griffin — 1 operation(s) for decisions.
  name: Griffin Decisions API
  slug: griffin-decisions-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: The Events API from Griffin — 2 operation(s) for events.
  name: Griffin Events API
  slug: griffin-events-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: Invitations enable [users](#tag/Users) to create new [memberships](#tag/Memberships) for their [organization](#tag/Organizations). The new membership is only created once when the invitation is accept
  name: Griffin Invitations API
  slug: griffin-invitations-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: The Legal person history API from Griffin — 1 operation(s) for legal person history.
  name: Griffin Legal person history API
  slug: griffin-legal-person-history-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: In the Griffin API, your organization and your customers are all represented by [legal persons](/docs/terms/legal-person). When you sign up with Griffin, your organization will be automatically assign
  name: Griffin Legal persons API
  slug: griffin-legal-persons-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: Memberships represents the relationship between a [user](#tag/Users) and an [organization](#tag/Organizations). A membership must have at least one [role](#tag/Roles) assigned to it.
  name: Griffin Memberships API
  slug: griffin-memberships-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: 'Message Signatures confirm the identity of the sender and integrity of request messages. Key points: - Uses Ed25519 algorithm - Requires registering a public key with Griffin - Signatures cover specif'
  name: Griffin Message Signatures API
  slug: griffin-message-signatures-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: The Navigation API from Griffin — 1 operation(s) for navigation.
  name: Griffin Navigation API
  slug: griffin-navigation-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: Open banking allows regulated third-party providers (TPPs) to access your customers' account data or initiate payments on their behalf. Griffin partners with [tell.money](https://tell.money/) to provi
  name: Griffin Open banking API
  slug: griffin-open-banking-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: The organization resource represents your company and acts as a container for the majority of other resources, including [legal persons](#tag/Legal-Persons) and [bank accounts](#tag/Bank-accounts). Wh
  name: Griffin Organizations API
  slug: griffin-organizations-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: A payee is the person or business to whom you are paying money. When you create a payee, you need to provide their name (`"account-holder"`), and their bank account number (`"account-number"`) and sor
  name: Griffin Payees API
  slug: griffin-payees-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: A payment captures the intent to move funds from a bank account to another bank account. Outbound payments can be made from your [bank account](#tag/Bank-accounts) to a [payee](#tag/Payees). Griffin a
  name: Griffin Payments API
  slug: griffin-payments-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: The Pooled account membership API from Griffin — 2 operation(s) for pooled account membership.
  name: Griffin Pooled account membership API
  slug: griffin-pooled-account-membership-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: Reliance onboarding allows you to create and submit an application on behalf of your customer, using information about them you have already collected. For more information, checkout our [onboarding g
  name: Griffin Reliance onboarding API
  slug: griffin-reliance-onboarding-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: A role represents a pre-defined set of capabilities that can be assigned to a [user](#tag/Users) via their [membership](#tag/Memberships) in an [organization](#tag/Organization). By default, the first
  name: Griffin Roles API
  slug: griffin-roles-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: A transaction represents funds deposited or withdrawn from a bank account. Read more about transactions [in our guides](/docs/guides/transactions).
  name: Griffin Transactions API
  slug: griffin-transactions-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: Users represent individuals who use the Griffin platform. A user must have a [membership](#tag/Memberships) in at least one [organization](#tag/Organizations), and may have memberships in multiple org
  name: Griffin Users API
  slug: griffin-users-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: The Verifications API from Griffin — 4 operation(s) for verifications.
  name: Griffin Verifications API
  slug: griffin-verifications-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: The Webhooks API from Griffin — 5 operation(s) for webhooks.
  name: Griffin Webhooks API
  slug: griffin-webhooks-api
- baseURL: https://api.griffin.com/v0
  baseurl_source: declared
  description: A [workflow](/docs/terms/workflow) determines which checks will be run against a [legal person](#tag/Legal-persons) as part of a [verification](#tag/Verifications)
  name: Griffin Workflows API
  slug: griffin-workflows-api
artifact_total: 62
asyncapis:
- description: ''
  name: Griffin Webhooks
  slug: griffin-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: The Griffin API keys API
  slug: open-griffin-api-keys-api
- collection_type: open
  name: The Griffin API keys Bank account holds API
  slug: open-griffin-bank-account-holds-api
- collection_type: open
  name: The Griffin API keys Bank account restrictions API
  slug: open-griffin-bank-account-restrictions-api
- collection_type: open
  name: The Griffin API keys Bank accounts API
  slug: open-griffin-bank-accounts-api
- collection_type: open
  name: The Griffin API keys Claims API
  slug: open-griffin-claims-api
- collection_type: open
  name: The Griffin API keys Companies House API
  slug: open-griffin-companies-house-api
- collection_type: open
  name: The Griffin API keys Confirmation of payee API
  slug: open-griffin-confirmation-of-payee-api
- collection_type: open
  name: The Griffin API keys Connectivity API
  slug: open-griffin-connectivity-api
- collection_type: open
  name: The Griffin API keys Decisions API
  slug: open-griffin-decisions-api
- collection_type: open
  name: The Griffin API keys Events API
  slug: open-griffin-events-api
- collection_type: open
  name: The Griffin API keys Invitations API
  slug: open-griffin-invitations-api
- collection_type: open
  name: The Griffin API keys Legal person history API
  slug: open-griffin-legal-person-history-api
- collection_type: open
  name: The Griffin API keys Legal persons API
  slug: open-griffin-legal-persons-api
- collection_type: open
  name: The Griffin API keys Memberships API
  slug: open-griffin-memberships-api
- collection_type: open
  name: The Griffin API keys Message Signatures API
  slug: open-griffin-message-signatures-api
- collection_type: open
  name: The Griffin API keys Navigation API
  slug: open-griffin-navigation-api
- collection_type: open
  name: The Griffin API keys Open banking API
  slug: open-griffin-open-banking-api
- collection_type: open
  name: The Griffin API keys Organizations API
  slug: open-griffin-organizations-api
- collection_type: open
  name: The Griffin API keys Payees API
  slug: open-griffin-payees-api
- collection_type: open
  name: The Griffin API keys Payments API
  slug: open-griffin-payments-api
- collection_type: open
  name: The Griffin API keys Pooled account membership API
  slug: open-griffin-pooled-account-membership-api
- collection_type: open
  name: The Griffin API keys Reliance onboarding API
  slug: open-griffin-reliance-onboarding-api
- collection_type: open
  name: The Griffin API keys Roles API
  slug: open-griffin-roles-api
- collection_type: open
  name: The Griffin API keys Transactions API
  slug: open-griffin-transactions-api
- collection_type: open
  name: The Griffin API keys Users API
  slug: open-griffin-users-api
- collection_type: open
  name: The Griffin API keys Verifications API
  slug: open-griffin-verifications-api
- collection_type: open
  name: The Griffin API keys Webhooks API
  slug: open-griffin-webhooks-api
- collection_type: open
  name: The Griffin API keys Workflows API
  slug: open-griffin-workflows-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/griffin-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://griffin.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.griffin.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.griffin.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.griffin.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.griffin.com/docs/guides/get-started-with-the-api
- group: commercial
  title: ''
  type: Pricing
  url: https://griffin.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.griffin.com/register
- group: start
  title: ''
  type: Login
  url: https://app.griffin.com
- group: company
  title: ''
  type: Blog
  url: https://griffin.com/blog
- group: operate
  title: ''
  type: Support
  url: https://docs.griffin.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/griffinbank
- group: commercial
  title: ''
  type: TermsOfService
  url: https://griffin.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://griffin.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.griffin.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://updates.griffin.com/
- group: build
  title: ''
  type: Postman
  url: https://github.com/griffinbank/griffin-postman
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/griffin-openapi-original.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/griffin-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/griffin-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/griffin-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/griffin-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/griffin-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/griffin-sandbox.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/griffin-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/griffin-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/griffin-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/griffin-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/griffin-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/griffin-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/griffin-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/griffin-api-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/griffin-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/griffin-domain-security.yml
created: '2026-07-17'
description: Griffin is a UK-regulated bank (Financial Conduct Authority authorised, Prudential Regulation Authority regulated) offering Banking-as-a-Service via a REST API. Fintechs and businesses embed FSCS-eligible bank accounts, payments (Faster Payments, BACS, CHAPS, book transfers, Confirmation of Payee), automated KYC/KYB onboarding (Verify), client-money and safeguarding accounts, savings accounts, and open banking directly into their own products. The v0 API uses API-key authentication with mandatory HTTP message signatures in live, documented webhooks, a full sandbox, and a first-party MCP server.
image: https://griffin.com/social.png
layout: provider
mcp_servers:
- description: ''
  name: Griffin MCP Server
  slug: griffin-mcp-server
modified: '2026-07-19'
name: Griffin
nav: Providers
network: true
overview: 'Griffin publishes 28 APIs on the [APIs.io](https://apis.io/) network, including API keys API, Bank account holds API, Bank account restrictions API, and 25 more. Tagged areas include Company, Fintech, Banking, Banking as a Service, and Payments.


  The Griffin catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Griffin''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, support, and 28 more developer resources.'
random_paper: 6
score:
  band: developing
  composite: 54.0
  coverage:
    artifact_dirs: 22
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 63.6
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 28
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/griffin/refs/heads/main/screenshots/griffin-2026-07-25T220332.png
security:
- kind: authentication
  name: Griffin Authentication
  slug: griffin-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Griffin Domain Security
  slug: griffin-domain-security
  summary_line: TLSv1.2 · DMARC
slug: griffin
tags:
- Company
- Fintech
- Banking
- Banking as a Service
- Payments
- KYC
- Open Banking
- Bank Accounts
- Financial-Services
website: https://griffin.com/
---
