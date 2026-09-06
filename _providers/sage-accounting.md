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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-05'
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
random_paper: 16
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 4
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 38.1
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 30.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Authentication
website: https://www.sage.com/en-gb/products/sage-accounting/
---
