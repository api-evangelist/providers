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
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 35
  human_in_the_loop: 3
  name: Chariot Agentic Access
  operation_count: 86
  slug: chariot-agentic-access
  summary_line: 86 operations · 35 acting · 3 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: Bank account information and balances
  name: Chariot Accounts API
  slug: chariot-accounts-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The Authorization Tokens API from Chariot — 4 operation(s) for authorization tokens.
  name: Chariot Authorization Tokens API
  slug: chariot-authorization-tokens-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The Connects API from Chariot — 2 operation(s) for connects.
  name: Chariot Connects API
  slug: chariot-connects-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: Account contact and holder information
  name: Chariot Contact API
  slug: chariot-contact-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: Account customer (organization) identity
  name: Chariot Customers API
  slug: chariot-customers-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The deposits API from Chariot — 2 operation(s) for deposits.
  name: Chariot Deposits API
  slug: chariot-deposits-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The disbursements API from Chariot — 9 operation(s) for disbursements.
  name: Chariot Disbursements API
  slug: chariot-disbursements-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The donations API from Chariot — 2 operation(s) for donations.
  name: Chariot Donations API
  slug: chariot-donations-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The Donor Accounts API from Chariot — 4 operation(s) for donor accounts.
  name: Chariot Donor Accounts API
  slug: chariot-donor-accounts-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The Donor Advised Funds API from Chariot — 2 operation(s) for donor advised funds.
  name: Chariot Donor Advised Funds API
  slug: chariot-donor-advised-funds-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The Event Subscriptions API from Chariot — 2 operation(s) for event subscriptions.
  name: Chariot Event Subscriptions API
  slug: chariot-event-subscriptions-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The Events API from Chariot — 2 operation(s) for events.
  name: Chariot Events API
  slug: chariot-events-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The financial_accounts API from Chariot — 3 operation(s) for financial_accounts.
  name: Chariot Financial Accounts API
  slug: chariot-financial-accounts-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The Giving Pools API from Chariot — 2 operation(s) for giving pools.
  name: Chariot Giving Pools API
  slug: chariot-giving-pools-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The Grant Requests API from Chariot — 4 operation(s) for grant requests.
  name: Chariot Grant Requests API
  slug: chariot-grant-requests-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The Grants API from Chariot — 4 operation(s) for grants.
  name: Chariot Grants API
  slug: chariot-grants-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The inboundTransfers API from Chariot — 5 operation(s) for inboundtransfers.
  name: Chariot Inbound Transfers API
  slug: chariot-inboundtransfers-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The mailbox API from Chariot — 2 operation(s) for mailbox.
  name: Chariot Mailbox API
  slug: chariot-mailbox-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The nonprofitAddresses API from Chariot — 1 operation(s) for nonprofitaddresses.
  name: Chariot Nonprofit Addresses API
  slug: chariot-nonprofitaddresses-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The nonprofitContacts API from Chariot — 1 operation(s) for nonprofitcontacts.
  name: Chariot Nonprofit Contacts API
  slug: chariot-nonprofitcontacts-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The Organizations API from Chariot — 3 operation(s) for organizations.
  name: Chariot Organizations API
  slug: chariot-organizations-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The Programs API from Chariot — 2 operation(s) for programs.
  name: Chariot Programs API
  slug: chariot-programs-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The properties API from Chariot — 4 operation(s) for properties.
  name: Chariot Properties API
  slug: chariot-properties-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The recurring_grants API from Chariot — 2 operation(s) for recurring_grants.
  name: Chariot Recurring Grants API
  slug: chariot-recurring-grants-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: Account statements and statement documents
  name: Chariot Statements API
  slug: chariot-statements-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: Account transaction history
  name: Chariot Transactions API
  slug: chariot-transactions-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The unintegrated_grants API from Chariot — 2 operation(s) for unintegrated_grants.
  name: Chariot Unintegrated Grants API
  slug: chariot-unintegrated-grants-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The Payment Sources API from Chariot — 2 operation(s) for payment sources.
  name: Chariot Payment Sources API
  slug: chariot-payment-sources-api
- baseURL: https://api.givechariot.com
  baseurl_source: declared
  description: The Verification Requests API from Chariot — 2 operation(s) for verification requests.
  name: Chariot Verification Requests API
  slug: chariot-verification-requests-api
artifact_total: 99
asyncapis:
- description: ''
  name: Chariot Webhooks
  slug: chariot-webhooks
collections:
- collection_type: postman
  name: Chariot FDX Accounts API
  slug: postman-chariot-accounts-api
- collection_type: postman
  name: Chariot FDX Accounts Authorization Tokens API
  slug: postman-chariot-authorization-tokens-api
- collection_type: postman
  name: Chariot FDX Accounts Connects API
  slug: postman-chariot-connects-api
- collection_type: postman
  name: Chariot FDX Accounts Contact API
  slug: postman-chariot-contact-api
- collection_type: postman
  name: Chariot FDX Accounts Customers API
  slug: postman-chariot-customers-api
- collection_type: postman
  name: Chariot FDX Accounts deposits API
  slug: postman-chariot-deposits-api
- collection_type: postman
  name: Chariot FDX Accounts disbursements API
  slug: postman-chariot-disbursements-api
- collection_type: postman
  name: Chariot FDX Accounts donations API
  slug: postman-chariot-donations-api
- collection_type: postman
  name: Chariot FDX Accounts Donor Accounts API
  slug: postman-chariot-donor-accounts-api
- collection_type: postman
  name: Chariot FDX Accounts Donor Advised Funds API
  slug: postman-chariot-donor-advised-funds-api
- collection_type: postman
  name: Chariot FDX Accounts Event Subscriptions API
  slug: postman-chariot-event-subscriptions-api
- collection_type: postman
  name: Chariot FDX Accounts Events API
  slug: postman-chariot-events-api
- collection_type: postman
  name: Chariot FDX Accounts financial_accounts API
  slug: postman-chariot-financial-accounts-api
- collection_type: postman
  name: Chariot FDX Accounts Giving Pools API
  slug: postman-chariot-giving-pools-api
- collection_type: postman
  name: Chariot FDX Accounts Grant Requests API
  slug: postman-chariot-grant-requests-api
- collection_type: postman
  name: Chariot FDX Accounts Grants API
  slug: postman-chariot-grants-api
- collection_type: postman
  name: Chariot FDX Accounts inboundTransfers API
  slug: postman-chariot-inboundtransfers-api
- collection_type: postman
  name: Chariot FDX Accounts mailbox API
  slug: postman-chariot-mailbox-api
- collection_type: postman
  name: Chariot FDX Accounts nonprofitAddresses API
  slug: postman-chariot-nonprofitaddresses-api
- collection_type: postman
  name: Chariot FDX Accounts nonprofitContacts API
  slug: postman-chariot-nonprofitcontacts-api
- collection_type: postman
  name: Chariot FDX Accounts Organizations API
  slug: postman-chariot-organizations-api
- collection_type: postman
  name: Chariot FDX Accounts paymentSources API
  slug: postman-chariot-paymentsources-api
- collection_type: postman
  name: Chariot FDX Accounts Programs API
  slug: postman-chariot-programs-api
- collection_type: postman
  name: Chariot FDX Accounts properties API
  slug: postman-chariot-properties-api
- collection_type: postman
  name: Chariot FDX Accounts recurring_grants API
  slug: postman-chariot-recurring-grants-api
- collection_type: postman
  name: Chariot FDX Accounts Statements API
  slug: postman-chariot-statements-api
- collection_type: postman
  name: Chariot FDX Accounts Transactions API
  slug: postman-chariot-transactions-api
- collection_type: postman
  name: Chariot FDX Accounts unintegrated_grants API
  slug: postman-chariot-unintegrated-grants-api
- collection_type: postman
  name: Chariot FDX Accounts verificationRequests API
  slug: postman-chariot-verificationrequests-api
- collection_type: open
  name: Chariot FDX Accounts API
  slug: open-chariot-accounts-api
- collection_type: open
  name: Chariot FDX Accounts Authorization Tokens API
  slug: open-chariot-authorization-tokens-api
- collection_type: open
  name: Chariot FDX Accounts Connects API
  slug: open-chariot-connects-api
- collection_type: open
  name: Chariot FDX Accounts Contact API
  slug: open-chariot-contact-api
- collection_type: open
  name: Chariot FDX Accounts Customers API
  slug: open-chariot-customers-api
- collection_type: open
  name: Chariot FDX Accounts Deposits API
  slug: open-chariot-deposits-api
- collection_type: open
  name: Chariot FDX Accounts Disbursements API
  slug: open-chariot-disbursements-api
- collection_type: open
  name: Chariot FDX Accounts Donations API
  slug: open-chariot-donations-api
- collection_type: open
  name: Chariot FDX Accounts Donor Accounts API
  slug: open-chariot-donor-accounts-api
- collection_type: open
  name: Chariot FDX Accounts Donor Advised Funds API
  slug: open-chariot-donor-advised-funds-api
- collection_type: open
  name: Chariot FDX Accounts Event Subscriptions API
  slug: open-chariot-event-subscriptions-api
- collection_type: open
  name: Chariot FDX Accounts Events API
  slug: open-chariot-events-api
- collection_type: open
  name: Chariot FDX Accounts Financial Accounts API
  slug: open-chariot-financial-accounts-api
- collection_type: open
  name: Chariot FDX Accounts Giving Pools API
  slug: open-chariot-giving-pools-api
- collection_type: open
  name: Chariot FDX Accounts Grant Requests API
  slug: open-chariot-grant-requests-api
- collection_type: open
  name: Chariot FDX Accounts Grants API
  slug: open-chariot-grants-api
- collection_type: open
  name: Chariot FDX Accounts Inbound Transfers API
  slug: open-chariot-inboundtransfers-api
- collection_type: open
  name: Chariot FDX Accounts Mailbox API
  slug: open-chariot-mailbox-api
- collection_type: open
  name: Chariot FDX Accounts Nonprofit Addresses API
  slug: open-chariot-nonprofitaddresses-api
- collection_type: open
  name: Chariot FDX Accounts Nonprofit Contacts API
  slug: open-chariot-nonprofitcontacts-api
- collection_type: open
  name: Chariot FDX Accounts Organizations API
  slug: open-chariot-organizations-api
- collection_type: open
  name: Chariot FDX Accounts Payment Sources API
  slug: open-chariot-paymentsources-api
- collection_type: open
  name: Chariot FDX Accounts Programs API
  slug: open-chariot-programs-api
- collection_type: open
  name: Chariot FDX Accounts Properties API
  slug: open-chariot-properties-api
- collection_type: open
  name: Chariot FDX Accounts Recurring Grants API
  slug: open-chariot-recurring-grants-api
- collection_type: open
  name: Chariot FDX Accounts Statements API
  slug: open-chariot-statements-api
- collection_type: open
  name: Chariot FDX Accounts Transactions API
  slug: open-chariot-transactions-api
- collection_type: open
  name: Chariot FDX Accounts Unintegrated Grants API
  slug: open-chariot-unintegrated-grants-api
- collection_type: open
  name: Chariot FDX Accounts Verification Requests API
  slug: open-chariot-verificationrequests-api
common:
- group: commercial
  href: https://artifacts.apis.io/chariot/plans/chariot-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chariot-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.givechariot.com/
- group: other
  href: https://artifacts.apis.io/chariot/capabilities/chariot-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/chariot-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/chariot/overlays/chariot-fdx-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/chariot-fdx-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/chariot/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.givechariot.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.givechariot.com/chariot-documentation
- group: docs
  title: ''
  type: APIReference
  url: https://docs.givechariot.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.givechariot.com/guides
- group: operate
  title: ''
  type: Support
  url: https://help.givechariot.com/
- group: company
  title: ''
  type: Blog
  url: https://www.givechariot.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chariot-giving
- group: commercial
  title: ''
  type: Pricing
  url: https://www.givechariot.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.givechariot.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.givechariot.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.givechariot.com/legal-nonprofit
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.givechariot.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.givechariot.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.givechariot.com/changelog
- group: build
  title: ''
  type: Postman
  url: https://raw.githubusercontent.com/chariot-giving/chariot-openapi/main/postman/collections/Chariot%20API.json
- group: auth
  href: https://artifacts.apis.io/chariot/authentication/chariot-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chariot-authentication.yml
- group: auth
  href: https://artifacts.apis.io/chariot/scopes/chariot-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/chariot-scopes.yml
- group: auth
  href: https://artifacts.apis.io/chariot/security/chariot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chariot-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/chariot/agentic-access/chariot-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/chariot-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/chariot/packages/chariot-packages.yml
  title: ''
  type: Packages
  url: packages/chariot-packages.yml
- group: build
  href: https://artifacts.apis.io/chariot/packages/chariot-packages.yml
  title: ''
  type: SDKs
  url: packages/chariot-packages.yml
- group: agent
  href: https://artifacts.apis.io/chariot/well-known/chariot-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chariot-well-known.yml
- group: agent
  href: https://artifacts.apis.io/chariot/mcp/chariot-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/chariot-mcp.yml
- group: agent
  href: https://artifacts.apis.io/chariot/llms/chariot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chariot-llms.txt
- group: design
  href: https://artifacts.apis.io/chariot/conformance/chariot-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chariot-conformance.yml
- group: design
  href: https://artifacts.apis.io/chariot/errors/chariot-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/chariot-problem-types.yml
- group: design
  href: https://artifacts.apis.io/chariot/lifecycle/chariot-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/chariot-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/chariot/conventions/chariot-conventions.yml
  title: ''
  type: Conventions
  url: conventions/chariot-conventions.yml
- group: design
  href: https://artifacts.apis.io/chariot/conventions/chariot-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/chariot-conventions.yml
- group: operate
  href: https://artifacts.apis.io/chariot/changelog/chariot-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/chariot-changelog.yml
- group: design
  href: https://artifacts.apis.io/chariot/asyncapi/chariot-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/chariot-webhooks.yml
- group: design
  href: https://artifacts.apis.io/chariot/data-model/chariot-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chariot-data-model.yml
- group: start
  href: https://artifacts.apis.io/chariot/sandbox/chariot-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/chariot-sandbox.yml
- group: design
  href: https://artifacts.apis.io/chariot/components/chariot-components.yml
  title: ''
  type: Components
  url: components/chariot-components.yml
- group: agent
  href: https://artifacts.apis.io/chariot/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Chariot is the leading payments platform for charitable giving, best known for DAFpay — the first donor-advised fund (DAF) payment option, named one of TIME's Best Inventions of 2025. Its REST API lets nonprofits, fundraising platforms, and grantmakers connect donor-advised funds, accept DAF donations through the embeddable Chariot Connect flow, move grant money via disbursements and inbound transfers, subscribe to webhook events, and read connected bank-account data through a Financial Data Exchange (FDX) v6 open-banking API. Chariot is building financial infrastructure for the multi-hundred-billion-dollar donor-advised fund market, the fastest-growing segment of philanthropy.
finops:
- has_sources: true
  method: derived
  name: Chariot Finops
  primary_unit: ''
  service_category: ''
  slug: chariot-finops
  template: true
image: https://givechariot.com/api/media/file/daf-giving-simplified-1200x630.png
layout: provider
mcp_servers:
- description: 'Chariot publishes a hosted MCP server over its documentation surface (Fern/Mintlify-style docs MCP) for AI clients such as Claude Code and Cursor. It exposes the Chariot docs and API reference as MCP '
  name: Chariot MCP Server
  slug: chariot-docs
modified: '2026-07-18'
name: Chariot
nav: Providers
network: true
overview: 'Chariot publishes 29 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Authorization Tokens API, Connects API, and 26 more. Tagged areas include Payments, Donor-Advised Funds, Charitable Giving, Non-Profit, and Fintech.


  The Chariot catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Chariot''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 33 more developer resources.'
plans:
- name: Chariot Plans Pricing
  plan_count: 0
  slug: chariot-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 116
  extends:
  - spectral:oas
  name: Chariot API Rules
  rule_count: 75
  severity_counts:
    error: 56
    hint: 0
    info: 8
    warn: 11
  slug: chariot-rules
scopes:
- name: Chariot Scopes
  scope_count: 4
  slug: chariot-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: strong
  composite: 58.5
  coverage:
    artifact_dirs: 33
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 10.0
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 60.8
    developer_ergonomics: 78.0
    discoverability: 71.7
    operational_transparency: 34.2
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 17.2
      total: 29
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 39.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/chariot/chariot-2026-07-25T205102.png
security:
- kind: authentication
  name: Chariot Authentication
  slug: chariot-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Chariot Domain Security
  slug: chariot-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: Accept a DAF donation with Chariot Connect
  slug: chariot-accept-daf-donation
- name: Create and approve a disbursement
  slug: chariot-create-disbursement
- name: Subscribe to Chariot webhooks
  slug: chariot-subscribe-events
slug: chariot
tags:
- Payments
- Donor-Advised Funds
- Charitable Giving
- Non-Profit
- Fintech
- DAFpay
- Grants
- Disbursements
- Open Banking
- FDX
- Webhook
- Company
website: https://www.givechariot.com/
---
