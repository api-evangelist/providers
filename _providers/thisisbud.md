---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 97
  human_in_the_loop: 2
  name: Thisisbud Agentic Access
  operation_count: 216
  slug: thisisbud-agentic-access
  summary_line: 216 operations · 97 acting · 2 human-in-the-loop
api_count: 16
apis:
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Manage virtual "buckets" for grouping and aggregating transactions by their underlying categories. Use this for retrieving financial data for customers of the Assess Dashboard (where the `bucket_id` i
  name: Bud Financial Limited Aggregation Buckets API
  slug: thisisbud-aggregation-buckets-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Create, list, and revoke Client Secrets used, alongside the `client_id`, to authenticate to the Bud platform via OAuth2.
  name: Bud Financial Limited Client Secrets API
  slug: thisisbud-client-secrets-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Manipulate Transactions held on the Bud platform by finding similar transactions and submitting corrections.
  name: Bud Financial Limited Correct Financial Data API
  slug: thisisbud-correct-financial-data-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: 'Create a new connection to an Open Banking provider by using either: (i) Bud''s configurable frontend UI (__Bud Connect__), built to maximise conversion; or (ii) Bud''s individual API endpoints to help '
  name: Bud Financial Limited Create a Connection API
  slug: thisisbud-create-a-connection-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Understand and target messaging to your customers more effectively by defining your own custom insights.
  name: Bud Financial Limited Custom Insights API
  slug: thisisbud-custom-insights-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Create a link for a customer to follow, which will allow them to connect their bank accounts and submit their financial data for the application.
  name: Bud Financial Limited Customer Application Links API
  slug: thisisbud-customer-application-links-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Create, retrieve and manage financial applications for customers using the Assess product. Applications created on this platform can be viewed using the Assess Dashboard to observe application statuse
  name: Bud Financial Limited Customer Applications API
  slug: thisisbud-customer-applications-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Retrieve flags and facts calculated in real time from a customer's financial data.
  name: Bud Financial Limited Customer-Level Insights API
  slug: thisisbud-customer-level-insights-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Find information regarding your customer's debts.
  name: Bud Financial Limited Debt Collection Finder API
  slug: thisisbud-debt-collection-finder-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Create and manage campaigns — by hand, or by describing a business goal for Drive's campaign agent to build one from — track their performance, and retrieve the customer-facing banner widgets and temp
  name: Bud Financial Limited Drive Campaigns API
  slug: thisisbud-drive-campaigns-api-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Connection URLs for Drive's remote Model Context Protocol servers, for use with AI/LLM driven agents — the general Drive copilot, and dedicated servers for segments and campaigns. They authenticate th
  name: Bud Financial Limited Drive MCP API
  slug: thisisbud-drive-mcp-api-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Create and manage customer segments — Drive's V1 model (fixed customer lists, criteria copied from an existing segment) and V2 model (a recursive criteria tree of flags, segment dependencies, and logi
  name: Bud Financial Limited Drive Segments API
  slug: thisisbud-drive-segments-api-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Obtain greater context to Bud's enrichment services.
  name: Bud Financial Limited Enrichment Resources API
  slug: thisisbud-enrichment-resources-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Breakdown your customer's income and expenditure based on Bud's enrichments to help orientate their financial world.
  name: Bud Financial Limited Enrichment Totals API
  slug: thisisbud-enrichment-totals-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: A collection of frontend widgets representing customer financial data.
  name: Bud Financial Limited Frontend Widgets API
  slug: thisisbud-frontend-widgets-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Find information regarding your customer's income.
  name: Bud Financial Limited Income Finder API
  slug: thisisbud-income-finder-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Initiate the asynchronous process of pushing a customer's account information (i.e. first party data) onto the Bud platform. These asynchronous requests create a task to store the given accounts or tr
  name: Bud Financial Limited Ingest First Party Data API
  slug: thisisbud-ingest-first-party-data-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Authenticates and securely creates a new payment from a customer’s chosen account(s) using Bud's regulatory licence as a [Third Party Provider (TPP)](https://www.openbanking.org.uk/providers/third-par
  name: Bud Financial Limited Initiate Payment - Bud license API
  slug: thisisbud-initiate-payment-bud-license-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Authenticates and securely creates a new payment from a customer’s chosen account(s) using your organisation's regulatory permission as a Payment Initiation Service Provider (PISP).
  name: Bud Financial Limited Initiate Payment - Client license API
  slug: thisisbud-initiate-payment-client-license-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Find information regarding your customer's loans.
  name: Bud Financial Limited Loan Finder API
  slug: thisisbud-loan-finder-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: 'Different endpoints that allow to to manage an existing customer connection. This includes the ability to: (i) Refresh the data associated with a given connection, pulling in the latest account inform'
  name: Bud Financial Limited Manage a Connection API
  slug: thisisbud-manage-a-connection-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Manage the number of customers registered onto the Bud platform.
  name: Bud Financial Limited Manage Customers API
  slug: thisisbud-manage-customers-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Manipulate Transactions held on the Bud platform by removing data, submitting corrections, or adding tags through different rulesets.
  name: Bud Financial Limited Manage Financial Data API
  slug: thisisbud-manage-financial-data-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Manage payments to initiated through Bud's Payments API
  name: Bud Financial Limited Manage Payments API
  slug: thisisbud-manage-payments-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Create, list, rename, and delete customer-authored labels that can be attached to transactions. Labels are customer-defined strings used to group transactions in ways that are meaningful to the custom
  name: Bud Financial Limited Manage Transaction Labels API
  slug: thisisbud-manage-transaction-labels-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Allows an MCP Client to connect to Bud API endpoints as tools. Currently in beta
  name: Bud Financial Limited MCP (Model Context Protocol) API
  slug: thisisbud-mcp-model-context-protocol-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Retrieve and manage access and refresh tokens to authenticate to the Bud platform via OAuth2 protocol.
  name: Bud Financial Limited O Auth2 API
  slug: thisisbud-oauth2-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Find information regarding your customer's financial products.
  name: Bud Financial Limited Product Finder API
  slug: thisisbud-product-finder-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Find information relating to any regularity found across certain groups of transactions within your customer's accounts.
  name: Bud Financial Limited Regular Payments Finder API
  slug: thisisbud-regular-payments-finder-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Retrieve a customer's actionable insights generated from their financial data.
  name: Bud Financial Limited Retrieve Actionable Insights API
  slug: thisisbud-retrieve-actionable-insights-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Breakdown your customer's transactions by fixed/flexible spend and discretionary vs non discretionary high-level totals.
  name: Bud Financial Limited Retrieve Affordability Report API
  slug: thisisbud-retrieve-affordability-report-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: 'Breakdown your customer''s transactions by fixed/flexible spend and discretionary vs non discretionary high-level totals. Retrieve Affordability Report V2 endpoints are designed to closely reflect the '
  name: Bud Financial Limited Retrieve Affordability Report V2 API
  slug: thisisbud-retrieve-affordability-report-v2-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Retrieve a customer's report insights generated from their financial data. In contrast to the alert style actionable insights, these insights should be used more as a summary.
  name: Bud Financial Limited Retrieve Affordability Risk Insights API
  slug: thisisbud-retrieve-affordability-risk-insights-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Retrieve Characteristics associated with an individual Customer based on their financial data.
  name: Bud Financial Limited Retrieve Customer Characteristics API
  slug: thisisbud-retrieve-customer-characteristics-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Retrieve a customer's financial data from a range of sources.
  name: Bud Financial Limited Retrieve Financial Data API
  slug: thisisbud-retrieve-financial-data-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Savings goals management API V2.
  name: Bud Financial Limited Savings Goals V2 API
  slug: thisisbud-savings-goals-v2-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Spending budgets management API.
  name: Bud Financial Limited Spending Budgets API
  slug: thisisbud-spending-budgets-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Find information regarding your customer's subscriptions.
  name: Bud Financial Limited Subscription Finder API
  slug: thisisbud-subscription-finder-api
- baseURL: https://api-sandbox.thisisbud.com
  baseurl_source: declared
  description: Allows customers to search & ask questions about their financial transactions.
  name: Bud Financial Limited Transaction Search API
  slug: thisisbud-transaction-search-api
artifact_total: 58
asyncapis:
- description: ''
  name: Thisisbud Webhooks
  slug: thisisbud-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/thisisbud/well-known/thisisbud-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/thisisbud-status-security.txt
- group: start
  title: ''
  type: SignUp
  url: https://console.thisisbud.com/signup
- group: agent
  href: https://artifacts.apis.io/thisisbud/agentic-access/thisisbud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/thisisbud-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/thisisbud/rules/thisisbud-rules.yml
  title: ''
  type: Spectral
  url: rules/thisisbud-rules.yml
- group: design
  href: https://artifacts.apis.io/thisisbud/json-ld/thisisbud-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/thisisbud-context.jsonld
- group: design
  href: https://artifacts.apis.io/thisisbud/vocabulary/thisisbud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/thisisbud-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/thisisbud/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/thisisbud/asyncapi/thisisbud-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/thisisbud-webhooks.yml
- group: design
  href: https://artifacts.apis.io/thisisbud/data-model/thisisbud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/thisisbud-data-model.yml
- group: operate
  href: https://artifacts.apis.io/thisisbud/changelog/thisisbud-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/thisisbud-changelog.yml
- group: start
  href: https://artifacts.apis.io/thisisbud/sandbox/thisisbud-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/thisisbud-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/thisisbud/authentication/thisisbud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thisisbud-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.thisisbud.com/docs/versioning.md
- group: design
  href: https://artifacts.apis.io/thisisbud/lifecycle/thisisbud-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/thisisbud-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/thisisbud/errors/thisisbud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/thisisbud-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/thisisbud/llms/thisisbud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/thisisbud-llms.txt
- group: auth
  href: https://artifacts.apis.io/thisisbud/well-known/thisisbud-trust-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/thisisbud-trust-security.txt
- group: auth
  href: https://artifacts.apis.io/thisisbud/well-known/thisisbud-console-us-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/thisisbud-console-us-security.txt
- group: auth
  href: https://artifacts.apis.io/thisisbud/well-known/thisisbud-console-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/thisisbud-console-security.txt
- group: auth
  href: https://artifacts.apis.io/thisisbud/well-known/thisisbud-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/thisisbud-api-security.txt
- group: auth
  href: https://artifacts.apis.io/thisisbud/well-known/thisisbud-api-sandbox-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/thisisbud-api-sandbox-security.txt
- group: agent
  href: https://artifacts.apis.io/thisisbud/well-known/thisisbud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/thisisbud-well-known.yml
- group: other
  href: https://artifacts.apis.io/thisisbud/hosts/thisisbud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thisisbud-hosts.yml
- group: other
  href: https://artifacts.apis.io/thisisbud/vendors/thisisbud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/thisisbud-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thisisbud.com/terms-conditions
- group: operate
  title: ''
  type: Support
  url: https://support.thisisbud.com/hc/en-gb
- group: operate
  title: ''
  type: StatusPage
  url: https://status.thisisbud.com/access/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thisisbud.com/en-us/legal/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.thisisbud.com/en-us/company/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.thisisbud.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.thisisbud.com/en-us/company/blog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.thisisbud.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.thisisbud.com/docs/postman-collection
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thisisbud.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/thisisbud
- group: auth
  href: https://artifacts.apis.io/thisisbud/security/thisisbud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thisisbud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thisisbud.com/
created: '2026-10-21'
description: Bud Financial Limited is a financial technology company offering digital banking solutions, including personal and business accounts, budgeting tools, and API-driven services for developers. The company focuses on providing seamless, secure, and user-friendly financial experiences through modern APIs, enabling integration with third‑party applications and services. Bud Financial aims to empower users with real‑time insights, automated savings, and flexible payment options, positioning itself as an innovative player in the fintech ecosystem.
json_schemas:
- name: Authorisation Gateweay URL Request Payload
  property_count: 11
  slug: thisisbud-auth-gateway-urlrequestv2
- name: Get Balances Response
  property_count: 3
  slug: thisisbud-get-balances-response
- name: Get Balances Response
  property_count: 3
  slug: thisisbud-get-balances-v3-response
- name: Retrieve Financial Products V2 Response Structure
  property_count: 3
  slug: thisisbud-get-products-response-v2
- name: Patch Spending Budget
  property_count: 4
  slug: thisisbud-patch-spending-budget
- name: Transaction
  property_count: 21
  slug: thisisbud-schemas-transaction
- name: Transaction
  property_count: 21
  slug: thisisbud-transaction
- name: Authorisation Gateweay URL Request Payload
  property_count: 7
  slug: thisisbud-usauth-gateway-urlrequestv2
jsonld:
- class_count: 85
  name: Thisisbud Context
  property_count: 155
  slug: thisisbud-context
layout: provider
modified: '2026-10-21'
name: Bud Financial Limited
nav: Providers
network: true
overview: 'Bud Financial Limited publishes 39 API contracts indexed on the [APIs.io](https://apis.io/) network, including Aggregation Buckets API, Client Secrets API, Correct Financial Data API, and 36 more. Tagged areas include Company, Fintech, Digital Banking, API Platform, and Financial Services.


  The Bud Financial Limited catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Bud Financial Limited''s developer surface includes signup flow, changelog, sandbox, authentication, support, engineering blog, API reference, and 30 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Bud Financial Limited API Rules
  rule_count: 61
  severity_counts:
    error: 41
    hint: 0
    info: 5
    warn: 15
  slug: thisisbud-rules
scopes:
- name: Thisisbud Scopes
  scope_count: 0
  slug: thisisbud-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 63.8
    catalog_earned_first_party: 0.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 23.7
    contract_governance: 17.4
    contract_quality: 75.3
    developer_ergonomics: 38.7
    discoverability: 75.9
    operational_transparency: 40.8
  previous_composite: 53.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 12.8
      total: 39
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 33.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/thisisbud/thisisbud-2026-11-03T144700.png
security:
- kind: authentication
  name: Thisisbud Authentication
  slug: thisisbud-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Thisisbud Domain Security
  slug: thisisbud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: thisisbud-initiate-payment-client-license
  slug: thisisbud-initiate-payment-client-license
- name: thisisbud-initiate-payment
  slug: thisisbud-initiate-payment
- name: thisisbud-manage-customers-create-and-retrieve
  slug: thisisbud-manage-customers-create-and-retrieve
- name: thisisbud-manage-transaction-labels
  slug: thisisbud-manage-transaction-labels
slug: thisisbud
tags:
- Company
- Fintech
- Digital Banking
- API Platform
- Financial Services
website: https://thisisbud.com/
---
