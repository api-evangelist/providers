---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-09-05'
api_count: 4
apis:
- description: REST API for Deskera Books, the cloud ERP and accounting product — contacts, products, accounts, invoices, bills, quotations, sales and purchase orders, credit and debit notes, deposits, expenses, pay
  name: Deskera Books API
  slug: books
- description: REST API for Deskera Sales — contacts, deals, activities and campaigns for the CRM side of the platform. Documented on the public Deskera developer documentation site under the same x-access-token aut
  name: Deskera Sales API
  slug: sales
- description: REST API for Deskera CRM+ — a table/column/record data model that lets an application create tables, define columns and manage records inside the CRM+ workspace. Documented on the public Deskera devel
  name: Deskera CRM+ API
  slug: crmplus
- description: API for Deskera People, the HR, payroll and employee-self-service product — employees, teams, shifts, attendance, leave, expenses, bank accounts, pay schedules, pay runs, payroll components and compon
  name: Deskera People API
  slug: people
artifact_total: 8
asyncapis:
- description: ''
  name: Deskera Webhooks
  slug: deskera-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deskera-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.deskera.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://deskera.github.io/Developer-Documentation/
- group: docs
  title: ''
  type: Documentation
  url: https://deskera.github.io/Developer-Documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://deskera.github.io/Developer-Documentation/docs/books/invoiceapi
- group: start
  title: ''
  type: GettingStarted
  url: https://deskera.github.io/Developer-Documentation/docs/books/started
- group: auth
  title: ''
  type: Authentication
  url: authentication/deskera-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/deskera-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Deskera
- group: company
  title: ''
  type: Blog
  url: https://www.deskera.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.deskera.com/blog/rss/
- group: operate
  title: ''
  type: Support
  url: https://www.deskera.com/care/
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.deskera.com/care/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.deskera.com/contact-us
- group: commercial
  title: ''
  type: Pricing
  url: https://www.deskera.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.deskera.com/signup
- group: start
  title: ''
  type: Login
  url: https://auth-v2.deskera.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.deskera.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.deskera.com/privacy-policy
- group: other
  title: ''
  type: DataProtection
  url: https://www.deskera.com/data-protection-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.deskera.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/deskera-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/deskera-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/deskera-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/deskera-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/deskera-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/deskera-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/deskera-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/deskera-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/deskera-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/deskera-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/deskera-llms.txt
created: '2026-08-04'
description: Deskera is a cloud business-software suite for small and mid-sized businesses, combining ERP and accounting (Deskera Books), CRM and sales (Deskera Sales / CRM+), and HR and payroll (Deskera People) on a single platform covering purchasing, sales, stock and inventory, warehouses, manufacturing/MRP, billing, invoicing, quotations, payments, tax and financial reporting, contacts and deals, employees, attendance, leave, expenses and pay runs. Deskera publishes a public developer documentation site covering REST APIs for Books, Sales, CRM+ and People, a three-legged OAuth 2.0 authorization flow with an x-access-token bearer header, a webhook registration API with a documented event catalog, separate staging and production environments, and a Java SDK. The company operates from Singapore and the United States and also trades under the erp.ai brand for account sign-up and sign-in.
image: https://deskera.github.io/Developer-Documentation/img/deskera-logo-1.png
layout: provider
modified: '2026-08-04'
name: Deskera
nav: Providers
network: true
overview: 'Deskera publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, ERP, Accounting, CRM, and Human Resources.


  The Deskera catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Deskera''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, pricing, and 25 more developer resources.'
random_paper: 0
scopes:
- name: Deskera Scopes
  scope_count: 3
  slug: deskera-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 48.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 71.4
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 48.7
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: authentication
  name: Deskera Authentication
  slug: deskera-authentication
  summary_line: oauth2/apiKey/http · 3 schemes
- kind: domain-security
  name: Deskera Domain Security
  slug: deskera-domain-security
  summary_line: TLSv1.2 · DMARC
slug: deskera
tags:
- Company
- ERP
- Accounting
- CRM
- Human Resources
- Payroll
- Inventory
- Invoicing
- Small Business
- Software-as-a-Service
website: https://www.deskera.com/
---
