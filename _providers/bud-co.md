---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 60.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 66
  human_in_the_loop: 1
  name: Bud Co Agentic Access
  operation_count: 153
  slug: bud-co-agentic-access
  summary_line: 153 operations · 66 acting · 1 human-in-the-loop
api_count: 32
apis:
- description: Manage virtual "buckets" for grouping and aggregating transactions by their underlying categories. Use this for retrieving financial data for customers of the Assess Dashboard (where the `bucket_id` i
  name: Bud Financial Aggregation Buckets API
  slug: bud-co-aggregation-buckets-api
- description: Manipulate Transactions held on the Bud platform by finding similar transactions and submitting corrections.
  name: Bud Financial Correct Financial Data API
  slug: bud-co-correct-financial-data-api
- description: 'Create a new connection to an Open Banking provider by using either: (i) Bud''s configurable frontend UI (__Bud Connect__), built to maximise conversion; or (ii) Bud''s individual API endpoints to help '
  name: Bud Financial Create a Connection API
  slug: bud-co-create-a-connection-api
- description: Understand and target messaging to your customers more effectively by defining your own custom insights.
  name: Bud Financial Custom Insights API
  slug: bud-co-custom-insights-api
- description: Create a link for a customer to follow, which will allow them to connect their bank accounts and submit their financial data for the application.
  name: Bud Financial Customer Application Links API
  slug: bud-co-customer-application-links-api
- description: Create, retrieve and manage financial applications for customers using the Assess product. Applications created on this platform can be viewed using the Assess Dashboard to observe application statuse
  name: Bud Financial Customer Applications API
  slug: bud-co-customer-applications-api
- description: Find information regarding your customer's debts.
  name: Bud Financial Debt Collection Finder API
  slug: bud-co-debt-collection-finder-api
- description: Obtain greater context to Bud's enrichment services.
  name: Bud Financial Enrichment Resources API
  slug: bud-co-enrichment-resources-api
- description: Breakdown your customer's income and expenditure based on Bud's enrichments to help orientate their financial world.
  name: Bud Financial Enrichment Totals API
  slug: bud-co-enrichment-totals-api
- description: A collection of frontend widgets representing customer financial data.
  name: Bud Financial Frontend Widgets API
  slug: bud-co-frontend-widgets-api
- description: Find information regarding your customer's income.
  name: Bud Financial Income Finder API
  slug: bud-co-income-finder-api
- description: Initiate the asynchronous process of pushing a customer's account information (i.e. first party data) onto the Bud platform. These asynchronous requests create a task to store the given accounts or tr
  name: Bud Financial Ingest First Party Data API
  slug: bud-co-ingest-first-party-data-api
- description: Authenticates and securely creates a new payment from a customer’s chosen account(s) using Bud's regulatory licence as a [Third Party Provider (TPP)](https://www.openbanking.org.uk/providers/third-par
  name: Bud Financial Initiate Payment - Bud license API
  slug: bud-co-initiate-payment-bud-license-api
- description: Authenticates and securely creates a new payment from a customer’s chosen account(s) using your organisation's regulatory permission as a Payment Initiation Service Provider (PISP).
  name: Bud Financial Initiate Payment - Client license API
  slug: bud-co-initiate-payment-client-license-api
- description: Find information regarding your customer's loans.
  name: Bud Financial Loan Finder API
  slug: bud-co-loan-finder-api
- description: 'Different endpoints that allow to to manage an existing customer connection. This includes the ability to: (i) Refresh the data associated with a given connection, pulling in the latest account inform'
  name: Bud Financial Manage a Connection API
  slug: bud-co-manage-a-connection-api
- description: Manage the number of customers registered onto the Bud platform.
  name: Bud Financial Manage Customers API
  slug: bud-co-manage-customers-api
- description: Manipulate Transactions held on the Bud platform by removing data, submitting corrections, or adding tags through different rulesets.
  name: Bud Financial Manage Financial Data API
  slug: bud-co-manage-financial-data-api
- description: Manage payments to initiated through Bud's Payments API
  name: Bud Financial Manage Payments API
  slug: bud-co-manage-payments-api
- description: Retrieve and manage access and refresh tokens to authenticate to the Bud platform via OAuth2 protocol.
  name: Bud Financial OAuth2 API
  slug: bud-co-oauth2-api
- description: Find information regarding your customer's financial products.
  name: Bud Financial Product Finder API
  slug: bud-co-product-finder-api
- description: Find information relating to any regularity found across certain groups of transactions within your customer's accounts.
  name: Bud Financial Regular Payments Finder API
  slug: bud-co-regular-payments-finder-api
- description: Retrieve a customer's actionable insights generated from their financial data.
  name: Bud Financial Retrieve Actionable Insights API
  slug: bud-co-retrieve-actionable-insights-api
- description: Breakdown your customer's transactions by fixed/flexible spend and discretionary vs non discretionary high-level totals.
  name: Bud Financial Retrieve Affordability Report API
  slug: bud-co-retrieve-affordability-report-api
- description: 'Breakdown your customer''s transactions by fixed/flexible spend and discretionary vs non discretionary high-level totals. Retrieve Affordability Report V2 endpoints are designed to closely reflect the '
  name: Bud Financial Retrieve Affordability Report V2 API
  slug: bud-co-retrieve-affordability-report-v2-api
- description: Retrieve a customer's report insights generated from their financial data. In contrast to the alert style actionable insights, these insights should be used more as a summary.
  name: Bud Financial Retrieve Affordability Risk Insights API
  slug: bud-co-retrieve-affordability-risk-insights-api
- description: Retrieve Characteristics associated with an individual Customer based on their financial data.
  name: Bud Financial Retrieve Customer Characteristics API
  slug: bud-co-retrieve-customer-characteristics-api
- description: Retrieve a customer's financial data from a range of sources.
  name: Bud Financial Retrieve Financial Data API
  slug: bud-co-retrieve-financial-data-api
- description: Savings goals management API V2.
  name: Bud Financial Savings Goals V2 API
  slug: bud-co-savings-goals-v2-api
- description: Spending budgets management API.
  name: Bud Financial Spending Budgets API
  slug: bud-co-spending-budgets-api
- description: Find information regarding your customer's subscriptions.
  name: Bud Financial Subscription Finder API
  slug: bud-co-subscription-finder-api
- description: Allows customers to search & ask questions about their financial transactions.
  name: Bud Financial Transaction Search API
  slug: bud-co-transaction-search-api
artifact_total: 47
collections:
- collection_type: open
  name: 'Bud API Services: Documentation'
  slug: open-bud-platform
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bud-co-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bud-co-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bud-co-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bud-co-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://bud.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.thisisbud.com
- group: start
  title: ''
  type: Console
  url: https://console.thisisbud.com
- group: operate
  title: ''
  type: Support
  url: https://support.thisisbud.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bud-financial/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/thisisbud/bud-public-developer-resources
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.thisisbud.com/llms.txt
created: '2026-05-25'
description: Bud Financial (formerly Bud, thisisbud.com) is a UK-based fintech infrastructure company providing AI-driven Open Banking aggregation, transaction enrichment, categorization, affordability assessment, and payment initiation APIs. The Bud platform unifies Open Banking connections to UK and EU ASPSPs behind a single REST API and layers AI/ML-powered enrichment, categorization, merchant identification, affordability scoring, income/expenditure analysis, and actionable financial insights on top of raw transaction data. Banks, lenders, and consumer fintechs use Bud for KYC/AML checks, lending decisions, money management, and embedded payments.
examples:
- key_count: 7
  name: Bud Affordability Report Example
  slug: bud-affordability-report-example
- key_count: 16
  name: Bud Transaction Example
  slug: bud-transaction-example
finops:
- name: Bud Co Finops
  service_category: Financial Services - Open Banking and Enrichment
  slug: bud-co-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bud-co.png
json_schemas:
- name: Bud Account
  property_count: 17
  slug: bud-account
- name: Bud Enriched Transaction
  property_count: 16
  slug: bud-transaction
jsonld:
- class_count: 0
  name: Bud Co Context
  property_count: 8
  slug: bud-co-context
layout: provider
modified: '2026-05-25'
name: Bud Financial
nav: Providers
network: true
overview: 'Bud Financial publishes 32 APIs on the [APIs.io](https://apis.io/) network, including Aggregation Buckets API, Correct Financial Data API, Create a Connection API, and 29 more. Tagged areas include Open Banking, Transaction Enrichment, Categorization, Affordability, and Payments.


  The Bud Financial catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Bud Financial''s developer surface includes authentication, documentation, developer console, support, GitHub presence, and 6 more developer resources.'
plans:
- name: Bud Co Plans Pricing
  plan_count: 5
  slug: bud-co-plans-pricing
random_paper: 106
rate_limits:
- limit_count: 0
  name: Bud Co Rate Limits
  slug: bud-co-rate-limits
rules:
- name: Bud Financial API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bud-co-jsonschema-spectral-rules
- name: Bud Financial API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 1
    info: 0
    warn: 4
  slug: bud-co-rules
scopes:
- name: Bud Co Scopes
  scope_count: 0
  slug: bud-co-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 68.5
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 47.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 32
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 48.1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bud-co/refs/heads/main/screenshots/bud-co-2026-06-20T173739.png
security:
- kind: authentication
  name: Bud Co Authentication
  slug: bud-co-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Bud Co Domain Security
  slug: bud-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bud-co
tags:
- Open Banking
- Transaction Enrichment
- Categorization
- Affordability
- Payments
- AISP
- PISP
- Financial Data
- FinTech
- UK
- AI
- Machine Learning
website: https://bud.co
---
