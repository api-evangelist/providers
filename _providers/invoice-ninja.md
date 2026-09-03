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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Invoice Ninja Agentic Access
  operation_count: 44
  slug: invoice-ninja-agentic-access
  summary_line: 44 operations · 29 acting
api_count: 1
apis:
- baseURL: https://invoicing.co
  baseurl_source: declared
  description: The Activities API from Invoice Ninja — 3 operation(s) for activities.
  name: Invoice Ninja Activities API
  slug: invoice-ninja-activities-api
- baseURL: https://invoicing.co
  baseurl_source: declared
  description: The Authentication API from Invoice Ninja — 2 operation(s) for authentication.
  name: Invoice Ninja Authentication API
  slug: invoice-ninja-authentication-api
- baseURL: https://invoicing.co
  baseurl_source: declared
  description: The Bank Integrations API from Invoice Ninja — 3 operation(s) for bank integrations.
  name: Invoice Ninja Bank Integrations API
  slug: invoice-ninja-bank-integrations-api
- baseURL: https://invoicing.co
  baseurl_source: declared
  description: The Bank Transaction Rules API from Invoice Ninja — 2 operation(s) for bank transaction rules.
  name: Invoice Ninja Bank Transaction Rules API
  slug: invoice-ninja-bank-transaction-rules-api
- baseURL: https://invoicing.co
  baseurl_source: declared
  description: The Bank Transactions API from Invoice Ninja — 3 operation(s) for bank transactions.
  name: Invoice Ninja Bank Transactions API
  slug: invoice-ninja-bank-transactions-api
- baseURL: https://invoicing.co
  baseurl_source: declared
  description: The Charts API from Invoice Ninja — 4 operation(s) for charts.
  name: Invoice Ninja Charts API
  slug: invoice-ninja-charts-api
- baseURL: https://invoicing.co
  baseurl_source: declared
  description: The Client Gateway Tokens API from Invoice Ninja — 2 operation(s) for client gateway tokens.
  name: Invoice Ninja Client Gateway Tokens API
  slug: invoice-ninja-client-gateway-tokens-api
- baseURL: https://invoicing.co
  baseurl_source: declared
  description: The Companies API from Invoice Ninja — 4 operation(s) for companies.
  name: Invoice Ninja Companies API
  slug: invoice-ninja-companies-api
- baseURL: https://invoicing.co
  baseurl_source: declared
  description: The Company Gateways API from Invoice Ninja — 2 operation(s) for company gateways.
  name: Invoice Ninja Company Gateways API
  slug: invoice-ninja-company-gateways-api
- baseURL: https://invoicing.co
  baseurl_source: declared
  description: The Settings API from Invoice Ninja — 1 operation(s) for settings.
  name: Invoice Ninja Settings API
  slug: invoice-ninja-settings-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Invoice Ninja v5 Activities API
  slug: open-invoice-ninja-activities-api
- collection_type: open
  name: Invoice Ninja v5 Activities Authentication API
  slug: open-invoice-ninja-authentication-api
- collection_type: open
  name: Invoice Ninja v5 Activities Bank Integrations API
  slug: open-invoice-ninja-bank-integrations-api
- collection_type: open
  name: Invoice Ninja v5 Activities Bank Transaction Rules API
  slug: open-invoice-ninja-bank-transaction-rules-api
- collection_type: open
  name: Invoice Ninja v5 Activities Bank Transactions API
  slug: open-invoice-ninja-bank-transactions-api
- collection_type: open
  name: Invoice Ninja v5 Activities Charts API
  slug: open-invoice-ninja-charts-api
- collection_type: open
  name: Invoice Ninja v5 Activities Client Gateway Tokens API
  slug: open-invoice-ninja-client-gateway-tokens-api
- collection_type: open
  name: Invoice Ninja v5 Activities Companies API
  slug: open-invoice-ninja-companies-api
- collection_type: open
  name: Invoice Ninja v5 Activities Company Gateways API
  slug: open-invoice-ninja-company-gateways-api
- collection_type: open
  name: Invoice Ninja v5 Activities Settings API
  slug: open-invoice-ninja-settings-api
- collection_type: open
  name: Invoice Ninja v5 API
  slug: open-invoice-ninja
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/invoice-ninja-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/invoice-ninja-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/invoice-ninja-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.invoiceninja.com/blog/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/invoice-ninja
- group: company
  title: ''
  type: Website
  url: https://www.invoiceninja.com
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.invoicing.co
- group: commercial
  title: ''
  type: Pricing
  url: https://www.invoiceninja.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://app.invoicing.co/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/invoiceninja
- group: build
  title: ''
  type: Source Code
  url: https://github.com/invoiceninja/invoiceninja
created: '2026-05-11'
description: Invoice Ninja is an open-source invoicing, billing, payments, and expense tracking platform for freelancers and small businesses, available both as a self-hosted application and a managed SaaS at invoicing.co. The Invoice Ninja v5 REST API exposes full CRUD access to clients, invoices, quotes, payments, products, recurring invoices, expenses, projects, and tasks, authenticated with an API token (plus an optional secret) passed via HTTP headers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/invoice-ninja.png
layout: provider
modified: '2026-05-11'
name: Invoice Ninja
nav: Providers
network: true
overview: 'Invoice Ninja publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Authentication API, Bank Integrations API, and 7 more. Tagged areas include Invoicing, Billing, Payments, Accounting, and Open-Source.


  Invoice Ninja''s developer surface includes authentication, engineering blog, documentation, pricing, signup flow, and 6 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 53.6
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 29.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/invoice-ninja/refs/heads/main/screenshots/invoice-ninja-2026-06-20T183523.png
security:
- kind: authentication
  name: Invoice Ninja Authentication
  slug: invoice-ninja-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Invoice Ninja Domain Security
  slug: invoice-ninja-domain-security
  summary_line: TLSv1.3 · DMARC
slug: invoice-ninja
tags:
- Invoicing
- Billing
- Payments
- Accounting
- Open-Source
- Freelancers
- SMB
website: https://www.invoiceninja.com
---
