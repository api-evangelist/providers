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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Invoice Ninja Agentic Access
  operation_count: 44
  slug: invoice-ninja-agentic-access
  summary_line: 44 operations · 29 acting
api_count: 10
apis:
- description: The Activities API from Invoice Ninja — 3 operation(s) for activities.
  name: Invoice Ninja Activities API
  slug: invoice-ninja-activities-api
- description: The Authentication API from Invoice Ninja — 2 operation(s) for authentication.
  name: Invoice Ninja Authentication API
  slug: invoice-ninja-authentication-api
- description: The Bank Integrations API from Invoice Ninja — 3 operation(s) for bank integrations.
  name: Invoice Ninja Bank Integrations API
  slug: invoice-ninja-bank-integrations-api
- description: The Bank Transaction Rules API from Invoice Ninja — 2 operation(s) for bank transaction rules.
  name: Invoice Ninja Bank Transaction Rules API
  slug: invoice-ninja-bank-transaction-rules-api
- description: The Bank Transactions API from Invoice Ninja — 3 operation(s) for bank transactions.
  name: Invoice Ninja Bank Transactions API
  slug: invoice-ninja-bank-transactions-api
- description: The Charts API from Invoice Ninja — 4 operation(s) for charts.
  name: Invoice Ninja Charts API
  slug: invoice-ninja-charts-api
- description: The Client Gateway Tokens API from Invoice Ninja — 2 operation(s) for client gateway tokens.
  name: Invoice Ninja Client Gateway Tokens API
  slug: invoice-ninja-client-gateway-tokens-api
- description: The Companies API from Invoice Ninja — 4 operation(s) for companies.
  name: Invoice Ninja Companies API
  slug: invoice-ninja-companies-api
- description: The Company Gateways API from Invoice Ninja — 2 operation(s) for company gateways.
  name: Invoice Ninja Company Gateways API
  slug: invoice-ninja-company-gateways-api
- description: The Settings API from Invoice Ninja — 1 operation(s) for settings.
  name: Invoice Ninja Settings API
  slug: invoice-ninja-settings-api
artifact_total: 14
collections:
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
overview: 'Invoice Ninja publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Authentication API, Bank Integrations API, and 7 more. Tagged areas include Invoicing, Billing, Payments, Accounting, and Open Source.


  Invoice Ninja''s developer surface includes authentication, engineering blog, documentation, pricing, signup flow, and 6 more developer resources.'
random_paper: 46
score:
  band: thin
  composite: 29.2
  delta: 1.8
  facets:
    commercial_clarity: 23.7
    contract_quality: 55.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 27.4
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
  schema_version: 0.11.0
  scored_at: '2026-08-11'
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
- Open Source
- Freelancers
- SMB
website: https://www.invoiceninja.com
---
