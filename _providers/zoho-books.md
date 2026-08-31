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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.2
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: The Contacts API from Zoho Books — 4 operation(s) for contacts.
  name: Zoho Books Contacts API
  slug: zoho-books-contacts-api
- description: The Invoices API from Zoho Books — 5 operation(s) for invoices.
  name: Zoho Books Invoices API
  slug: zoho-books-invoices-api
- description: The Items API from Zoho Books — 2 operation(s) for items.
  name: Zoho Books Items API
  slug: zoho-books-items-api
- description: The Organizations API from Zoho Books — 1 operation(s) for organizations.
  name: Zoho Books Organizations API
  slug: zoho-books-organizations-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zoho Books Contacts API
  slug: open-zoho-books-contacts-api
- collection_type: open
  name: Zoho Books Invoices API
  slug: open-zoho-books-invoices-api
- collection_type: open
  name: Zoho Books Items API
  slug: open-zoho-books-items-api
- collection_type: open
  name: Zoho Books Organizations API
  slug: open-zoho-books-organizations-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/zoho-books-capability-edges.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoho-books-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoho-books-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zoho
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/zoho-books
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/books/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zoho.com/books/api/v3/introduction/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoho.com/books/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.zoho.com/books/signup/
- group: start
  title: ''
  type: Login
  url: https://books.zoho.com/app/login
- group: operate
  title: ''
  type: Support
  url: https://www.zoho.com/books/support/
- group: company
  title: ''
  type: Blog
  url: https://www.zoho.com/books/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zoho.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zoho.com/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zoho.com/terms.html
- group: start
  title: ''
  type: Console
  url: https://api-console.zoho.com/
created: '2026-05-11'
description: Zoho Books is online accounting software for small and growing businesses that handles invoicing, expenses, banking, projects, inventory, vendor bills, reporting, and end-to-end GST/VAT compliance. It is part of the Zoho Finance suite and integrates with the rest of the Zoho One platform alongside payment gateways, banks, and tax authorities. The Zoho Books REST API exposes the full accounting data model — contacts, invoices, estimates, expenses, bills, banking, items, taxes, and reports — using OAuth 2.0 (Zoho-oauthtoken) for authentication and per-region data center base URLs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zoho-books.png
layout: provider
modified: '2026-05-11'
name: Zoho Books
nav: Providers
network: true
overview: 'Zoho Books publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, Invoices API, Items API, and 1 more. Tagged areas include Accounting, Bookkeeping, Invoicing, Expenses, and Banking.


  Zoho Books'' developer surface includes documentation, pricing, signup flow, support, engineering blog, developer console, and 10 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 35.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 37.6
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 32.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zoho-books/refs/heads/main/screenshots/zoho-books-2026-06-20T201932.png
security:
- kind: domain-security
  name: Zoho Books Domain Security
  slug: zoho-books-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoho Books Vulnerability Disclosure
  slug: zoho-books-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zoho-books
tags:
- Accounting
- Bookkeeping
- Invoicing
- Expenses
- Banking
- Small Business
- GST
- VAT
- Zoho
website: https://www.zoho.com/books/
---
