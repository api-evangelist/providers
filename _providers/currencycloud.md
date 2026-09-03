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
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.2
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 55
  human_in_the_loop: 0
  name: Currencycloud Agentic Access
  operation_count: 111
  slug: currencycloud-agentic-access
  summary_line: 111 operations · 55 acting
api_count: 2
apis:
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: The Account Usage API from Currencycloud — 1 operation(s) for account usage.
  name: Currencycloud Account Usage API
  slug: currencycloud-account-usage-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Create, search and update your Currencycloud account and any associated sub-accounts. Also provides you with the ability to use your own reference IDs for easy reconciliation with your internal system
  name: Currencycloud Accounts API
  slug: currencycloud-accounts-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Authenticate to gain access to the API. Log in to your Currencycloud account using your API Key and log out to terminate your session.
  name: Currencycloud Authenticate API
  slug: currencycloud-authenticate-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Provides access to view balance information. View the balances that you currently hold in different currencies on your Currencycloud account.
  name: Currencycloud Balances API
  slug: currencycloud-balances-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Create, search and manage the list of individuals or companies that you send payments to.
  name: Currencycloud Beneficiaries API
  slug: currencycloud-beneficiaries-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: The Business Information API from Currencycloud — 1 operation(s) for business information.
  name: Currencycloud Business Information API
  slug: currencycloud-business-information-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Create, search and manage the list of users that have access in your Currencycloud account or associated sub-accounts.
  name: Currencycloud Contacts API
  slug: currencycloud-contacts-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Find, retrieve and create a live currency conversion. You can also create and manage the live conversion of funds between two currencies.
  name: Currencycloud Conversions API
  slug: currencycloud-conversions-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: The Country API from Currencycloud — 2 operation(s) for country.
  name: Currencycloud Country API
  slug: currencycloud-country-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: The Currency API from Currencycloud — 1 operation(s) for currency.
  name: Currencycloud Currency API
  slug: currencycloud-currency-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Requests that are only available in the Demo environment.
  name: Currencycloud Demo API
  slug: currencycloud-demo-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: The Document Images API from Currencycloud — 2 operation(s) for document images.
  name: Currencycloud Document Images API
  slug: currencycloud-document-images-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: The Documents API from Currencycloud — 2 operation(s) for documents.
  name: Currencycloud Documents API
  slug: currencycloud-documents-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: The Form API from Currencycloud — 3 operation(s) for form.
  name: Currencycloud Form API
  slug: currencycloud-form-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Find funding accounts that can be used to settle and collect funds in each available currency.
  name: Currencycloud Funding API
  slug: currencycloud-funding-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: View information relating to the 'payer' for a payment that has been initiated through the platform.
  name: Currencycloud Payers API
  slug: currencycloud-payers-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Create, search, manage and action all of your domestic and international payments through this API.
  name: Currencycloud Payments API
  slug: currencycloud-payments-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: The People API from Currencycloud — 2 operation(s) for people.
  name: Currencycloud People API
  slug: currencycloud-people-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Create new quotes to use for held rates conversions.
  name: Currencycloud Quotes API
  slug: currencycloud-quotes-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Super fast real-time access to live foreign exchange rates through the Currencycloud platform.
  name: Currencycloud Rates API
  slug: currencycloud-rates-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Easy access to view important data relevant to your Currencycloud account including beneficiary details, conversion dates, available currencies, payer required details, payment dates and settlement de
  name: Currencycloud Reference API
  slug: currencycloud-reference-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Ability to create and retrieve reports.
  name: Currencycloud Reporting API
  slug: currencycloud-reporting-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Sender of funds.
  name: Currencycloud Sender API
  slug: currencycloud-sender-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: The Transaction Approval API from Currencycloud — 1 operation(s) for transaction approval.
  name: Currencycloud Transaction Approval API
  slug: currencycloud-transaction-approval-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: View balances and all pending and completed transactions in your Currencycloud account, as well as associated sub-account balances and transactions.
  name: Currencycloud Transactions API
  slug: currencycloud-transactions-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Search, retrieve and create a transfer of funds between your Currencycloud account and associated sub-accounts.
  name: Currencycloud Transfers API
  slug: currencycloud-transfers-api
- baseURL: https://api.currencycloud.com/v2
  baseurl_source: declared
  description: Manage withdrawal accounts
  name: Currencycloud Withdrawal Accounts API
  slug: currencycloud-withdrawal-accounts-api
artifact_total: 88
asyncapis:
- description: ''
  name: Currencycloud Webhooks
  slug: currencycloud-webhooks
collections:
- collection_type: postman
  name: api-onboarding Account Usage API
  slug: postman-currencycloud-account-usage-api
- collection_type: postman
  name: api-onboarding Account Usage Accounts API
  slug: postman-currencycloud-accounts-api
- collection_type: postman
  name: api-onboarding Account Usage Authenticate API
  slug: postman-currencycloud-authenticate-api
- collection_type: postman
  name: api-onboarding Account Usage Balances API
  slug: postman-currencycloud-balances-api
- collection_type: postman
  name: api-onboarding Account Usage Beneficiaries API
  slug: postman-currencycloud-beneficiaries-api
- collection_type: postman
  name: api-onboarding Account Usage Business Information API
  slug: postman-currencycloud-business-information-api
- collection_type: postman
  name: api-onboarding Account Usage Contacts API
  slug: postman-currencycloud-contacts-api
- collection_type: postman
  name: api-onboarding Account Usage Conversions API
  slug: postman-currencycloud-conversions-api
- collection_type: postman
  name: api-onboarding Account Usage Country API
  slug: postman-currencycloud-country-api
- collection_type: postman
  name: api-onboarding Account Usage Currency API
  slug: postman-currencycloud-currency-api
- collection_type: postman
  name: api-onboarding Account Usage Demo API
  slug: postman-currencycloud-demo-api
- collection_type: postman
  name: api-onboarding Account Usage Document Images API
  slug: postman-currencycloud-document-images-api
- collection_type: postman
  name: api-onboarding Account Usage Documents API
  slug: postman-currencycloud-documents-api
- collection_type: postman
  name: api-onboarding Account Usage Form API
  slug: postman-currencycloud-form-api
- collection_type: postman
  name: api-onboarding Account Usage Funding API
  slug: postman-currencycloud-funding-api
- collection_type: postman
  name: api-onboarding Account Usage Payers API
  slug: postman-currencycloud-payers-api
- collection_type: postman
  name: api-onboarding Account Usage Payments API
  slug: postman-currencycloud-payments-api
- collection_type: postman
  name: api-onboarding Account Usage People API
  slug: postman-currencycloud-people-api
- collection_type: postman
  name: api-onboarding Account Usage Quotes API
  slug: postman-currencycloud-quotes-api
- collection_type: postman
  name: api-onboarding Account Usage Rates API
  slug: postman-currencycloud-rates-api
- collection_type: postman
  name: api-onboarding Account Usage Reference API
  slug: postman-currencycloud-reference-api
- collection_type: postman
  name: api-onboarding Account Usage Reporting API
  slug: postman-currencycloud-reporting-api
- collection_type: postman
  name: api-onboarding Account Usage Sender API
  slug: postman-currencycloud-sender-api
- collection_type: postman
  name: api-onboarding Account Usage Transaction Approval API
  slug: postman-currencycloud-transaction-approval-api
- collection_type: postman
  name: api-onboarding Account Usage Transactions API
  slug: postman-currencycloud-transactions-api
- collection_type: postman
  name: api-onboarding Account Usage Transfers API
  slug: postman-currencycloud-transfers-api
- collection_type: postman
  name: api-onboarding Account Usage Withdrawal Accounts API
  slug: postman-currencycloud-withdrawal-accounts-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: api-onboarding Account Usage API
  slug: open-currencycloud-account-usage-api
- collection_type: open
  name: api-onboarding Account Usage Accounts API
  slug: open-currencycloud-accounts-api
- collection_type: open
  name: api-onboarding Account Usage Authenticate API
  slug: open-currencycloud-authenticate-api
- collection_type: open
  name: api-onboarding Account Usage Balances API
  slug: open-currencycloud-balances-api
- collection_type: open
  name: api-onboarding Account Usage Beneficiaries API
  slug: open-currencycloud-beneficiaries-api
- collection_type: open
  name: api-onboarding Account Usage Business Information API
  slug: open-currencycloud-business-information-api
- collection_type: open
  name: api-onboarding Account Usage Contacts API
  slug: open-currencycloud-contacts-api
- collection_type: open
  name: api-onboarding Account Usage Conversions API
  slug: open-currencycloud-conversions-api
- collection_type: open
  name: api-onboarding Account Usage Country API
  slug: open-currencycloud-country-api
- collection_type: open
  name: api-onboarding Account Usage Currency API
  slug: open-currencycloud-currency-api
- collection_type: open
  name: api-onboarding Account Usage Demo API
  slug: open-currencycloud-demo-api
- collection_type: open
  name: api-onboarding Account Usage Document Images API
  slug: open-currencycloud-document-images-api
- collection_type: open
  name: api-onboarding Account Usage Documents API
  slug: open-currencycloud-documents-api
- collection_type: open
  name: api-onboarding Account Usage Form API
  slug: open-currencycloud-form-api
- collection_type: open
  name: api-onboarding Account Usage Funding API
  slug: open-currencycloud-funding-api
- collection_type: open
  name: api-onboarding Account Usage Payers API
  slug: open-currencycloud-payers-api
- collection_type: open
  name: api-onboarding Account Usage Payments API
  slug: open-currencycloud-payments-api
- collection_type: open
  name: api-onboarding Account Usage People API
  slug: open-currencycloud-people-api
- collection_type: open
  name: api-onboarding Account Usage Quotes API
  slug: open-currencycloud-quotes-api
- collection_type: open
  name: api-onboarding Account Usage Rates API
  slug: open-currencycloud-rates-api
- collection_type: open
  name: api-onboarding Account Usage Reference API
  slug: open-currencycloud-reference-api
- collection_type: open
  name: api-onboarding Account Usage Reporting API
  slug: open-currencycloud-reporting-api
- collection_type: open
  name: api-onboarding Account Usage Sender API
  slug: open-currencycloud-sender-api
- collection_type: open
  name: api-onboarding Account Usage Transaction Approval API
  slug: open-currencycloud-transaction-approval-api
- collection_type: open
  name: api-onboarding Account Usage Transactions API
  slug: open-currencycloud-transactions-api
- collection_type: open
  name: api-onboarding Account Usage Transfers API
  slug: open-currencycloud-transfers-api
- collection_type: open
  name: api-onboarding Account Usage Withdrawal Accounts API
  slug: open-currencycloud-withdrawal-accounts-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/currencycloud-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/currencycloud-reference-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/currencycloud/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.currencycloud.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.currencycloud.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.currencycloud.com/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.currencycloud.com/guides/getting-started/getting-started-with-the-api/
- group: auth
  title: ''
  type: Authentication
  url: authentication/currencycloud-authentication.yml
- group: start
  title: ''
  type: SignUp
  url: https://developer.currencycloud.com/register-for-an-api-key/
- group: operate
  title: ''
  type: Support
  url: https://support.currencycloud.com/hc/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.currencycloud.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.visa.co.uk/legal/global-privacy-notice.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CurrencyCloud
- group: operate
  title: ''
  type: StatusPage
  url: https://status.currencycloud.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.currencycloud.com/guides/platform-specifics/deprecation-policy/
- group: build
  title: ''
  type: Postman
  url: https://github.com/CurrencyCloud/postman
- group: build
  title: ''
  type: SDKs
  url: packages/currencycloud-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/currencycloud-packages.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/currencycloud-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/currencycloud-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/currencycloud-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/currencycloud-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/currencycloud-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/currencycloud-trust-center.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/currencycloud-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/currencycloud-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/currencycloud-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/currencycloud-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/currencycloud-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/currencycloud-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/currencycloud-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/currencycloud-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/currencycloud-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/currencycloud-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/currencycloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.currencycloud.com
created: '2026-07-17'
description: 'Currencycloud is a cross-border payments and foreign-exchange platform, part of Visa, that provides a robust, predictable REST API for converting money between currencies, holding multi-currency balances, and making payments around the world. Its API v2 spans 18 domains — authentication, accounts and sub-accounts, balances, beneficiaries, contacts, conversions, funding, payers, payments, quotes, rates, reference data, reporting, transactions, transfers and withdrawal accounts — and lets businesses dynamically register sub-accounts to offer white-labelled money-transfer services to their own customers. Currencycloud is an FCA-authorised Electronic Money Institution (registration #900199) and a FinCEN-registered money transmitter, and publishes official SDKs for JavaScript, Python, Ruby, PHP, Java and .NET.'
image: https://raw.githubusercontent.com/CurrencyCloud/currencycloud-swagger/master/apps/website/public/images/introduction-header.png
layout: provider
modified: '2026-07-18'
name: Currencycloud
nav: Providers
network: true
overview: 'Currencycloud publishes 27 APIs on the [APIs.io](https://apis.io/) network, including Account Usage API, Accounts API, Authenticate API, and 24 more. Tagged areas include Company, Fintech, Payments, Foreign Exchange, and Cross-Border Payments.


  The Currencycloud catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Currencycloud''s developer surface includes documentation, API reference, getting-started guide, authentication, signup flow, support, changelog, and 30 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 5
  name: Currencycloud Rate Limits
  slug: currencycloud-rate-limits
score:
  band: strong
  composite: 59.5
  coverage:
    artifact_dirs: 23
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 58.6
    developer_ergonomics: 75.6
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 81.6
  previous_composite: 59.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: psd2
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 38.0
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/currencycloud/refs/heads/main/screenshots/currencycloud-2026-07-25T210947.png
security:
- kind: authentication
  name: Currencycloud Authentication
  slug: currencycloud-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Currencycloud Domain Security
  slug: currencycloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Currencycloud Trust Center
  slug: currencycloud-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 27018, PCI DSS Level 1, SOC 1, SOC 2, SOC 3, FIPS, GDPR, UK DPA
slug: currencycloud
tags:
- Company
- Fintech
- Payments
- Foreign Exchange
- Cross-Border Payments
- Money Transfer
- Currency Conversion
- Banking
website: https://www.currencycloud.com
---
