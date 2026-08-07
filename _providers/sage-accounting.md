---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
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
  score: 16.2
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: REST API for Sage Business Cloud Accounting providing access to contacts, sales invoices, sales credit notes, purchase invoices, purchase credit notes, ledger accounts, journals, products, services, t
  name: Sage Accounting v3.1 REST API
  slug: accounting-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sage-accounting-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sage-accounting-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.sage.com/en-gb/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Sage
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sage-software
- group: company
  title: ''
  type: Website
  url: https://www.sage.com/en-gb/products/sage-accounting/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.sage.com/accounting/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sage.com/accounting/reference/
- group: docs
  title: ''
  type: Guides
  url: https://developer.sage.com/accounting/guides/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sage.com/en-gb/products/sage-accounting/pricing/
- group: start
  title: ''
  type: Signup
  url: https://developer.sage.com/accounting/guides/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://www.sage.com/en-gb/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sage.com
- group: operate
  title: ''
  type: Community
  url: https://www.sagecity.com
created: '2026-05-11'
description: Sage Accounting (formerly Sage Business Cloud Accounting and Sage One) is Sage's cloud-based accounting software for UK and international small and medium businesses, covering invoicing, expenses, banking, VAT, payroll integration, and financial reporting. Its REST API at https://api.accounting.sage.com/v3.1 provides programmatic access to contacts, sales and purchase invoices, ledger accounts, journals, tax rates, bank accounts, and attachments. Authentication uses OAuth 2.0 with the authorization endpoint at https://www.sageone.com/oauth2/auth/central and the token endpoint at https://oauth.accounting.sage.com/token; access tokens expire after five minutes and refresh tokens after 31 days, and the X-Business header selects the target business.
graphqls:
- description: 'This GraphQL schema represents the Sage Accounting (formerly Sage Business Cloud Accounting / Sage One) REST API surface as a typed GraphQL interface. Sage Accounting is Sage''s cloud-based accounting '
  name: Sage Accounting GraphQL Schema
  slug: sage-accounting-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sage-accounting.png
layout: provider
modified: '2026-05-11'
name: Sage Accounting
nav: Providers
network: true
overview: 'Sage Accounting publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Accounting, Bookkeeping, Invoicing, Small Business, and VAT.


  Sage Accounting''s developer surface includes engineering blog, documentation, pricing, signup flow, support, and 9 more developer resources.'
random_paper: 59
score:
  band: thin
  composite: 28.5
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 48.1
    developer_ergonomics: 23.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 28.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: domain-security
  name: Sage Accounting Domain Security
  slug: sage-accounting-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sage Accounting Vulnerability Disclosure
  slug: sage-accounting-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sage-accounting
tags:
- Accounting
- Bookkeeping
- Invoicing
- Small Business
- VAT
- Sage
- UK
- OAuth 2.0
website: https://www.sage.com/en-gb/products/sage-accounting/
---
