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
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: REST API for managing organizations, contacts, items, invoices, estimates, credit notes, recurring invoices, expenses, projects, time entries, and customer payments. Authentication is OAuth 2.0 with O
  name: Zoho Invoice API
  slug: api
- baseURL: https://www.zohoapis.com/invoice/v3
  baseurl_source: declared
  description: The Contacts API from Zoho Invoice — 3 operation(s) for contacts.
  name: Zoho Invoice Contacts API
  slug: zoho-invoice-contacts-api
- baseURL: https://www.zohoapis.com/invoice/v3
  baseurl_source: declared
  description: The Credit Notes API from Zoho Invoice — 2 operation(s) for credit notes.
  name: Zoho Invoice Credit Notes API
  slug: zoho-invoice-credit-notes-api
- baseURL: https://www.zohoapis.com/invoice/v3
  baseurl_source: declared
  description: The Estimates API from Zoho Invoice — 2 operation(s) for estimates.
  name: Zoho Invoice Estimates API
  slug: zoho-invoice-estimates-api
- baseURL: https://www.zohoapis.com/invoice/v3
  baseurl_source: declared
  description: The Invoices API from Zoho Invoice — 6 operation(s) for invoices.
  name: Zoho Invoice Invoices API
  slug: zoho-invoice-invoices-api
- baseURL: https://www.zohoapis.com/invoice/v3
  baseurl_source: declared
  description: The Organizations API from Zoho Invoice — 1 operation(s) for organizations.
  name: Zoho Invoice Organizations API
  slug: zoho-invoice-organizations-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zoho Invoice Contacts API
  slug: open-zoho-invoice-contacts-api
- collection_type: open
  name: Zoho Invoice Credit Notes API
  slug: open-zoho-invoice-credit-notes-api
- collection_type: open
  name: Zoho Invoice Estimates API
  slug: open-zoho-invoice-estimates-api
- collection_type: open
  name: Zoho Invoice Invoices API
  slug: open-zoho-invoice-invoices-api
- collection_type: open
  name: Zoho Invoice Organizations API
  slug: open-zoho-invoice-organizations-api
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoho-invoice-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoho-invoice-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zoho
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/invoice
- group: docs
  title: ''
  type: Documentation
  url: https://www.zoho.com/invoice/api/v3
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoho.com/invoice/pricing.html
- group: start
  title: ''
  type: Signup
  url: https://www.zoho.com/invoice/signup
- group: start
  title: ''
  type: Console
  url: https://api-console.zoho.com
- group: company
  title: ''
  type: Blog
  url: https://www.zoho.com/invoice/blog/feed/
created: '2026-05-11'
description: Zoho Invoice is a cloud-based invoicing application for small businesses and freelancers that supports customer management, estimates, invoices, recurring billing, expense tracking, time tracking, and online payment collection. The Zoho Invoice REST API provides full CRUD access to organizations, contacts, items, invoices, estimates, credit notes, expenses, projects, time entries, and customer payments. Authentication uses OAuth 2.0 with region-specific data center domains (.com, .eu, .in, .com.au, .jp, .ca, .com.cn, .sa).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zoho-invoice.png
layout: provider
modified: '2026-05-11'
name: Zoho Invoice
nav: Providers
network: true
overview: 'Zoho Invoice publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, Credit Notes API, Estimates API, and 2 more. Tagged areas include Invoicing, Accounting, Small Business, Billing, and Expense Tracking.


  Zoho Invoice''s developer surface includes documentation, pricing, signup flow, developer console, engineering blog, and 4 more developer resources.'
random_paper: 3
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 5
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 28.5
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zoho-invoice/refs/heads/main/screenshots/zoho-invoice-2026-06-20T201940.png
security:
- kind: domain-security
  name: Zoho Invoice Domain Security
  slug: zoho-invoice-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoho Invoice Vulnerability Disclosure
  slug: zoho-invoice-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zoho-invoice
tags:
- Invoicing
- Accounting
- Small Business
- Billing
- Expense Tracking
- Software-as-a-Service
website: https://www.zoho.com/invoice
---
