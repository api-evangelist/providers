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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 81.7
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 80
  human_in_the_loop: 0
  name: Coperniq Agentic Access
  operation_count: 155
  slug: coperniq-agentic-access
  summary_line: 155 operations · 80 acting
api_count: 28
apis:
- description: The accounts API from Coperniq — 3 operation(s) for accounts.
  name: Coperniq accounts API
  slug: coperniq-accounts-api
- description: The ahJs API from Coperniq — 2 operation(s) for ahjs.
  name: Coperniq ahJs API
  slug: coperniq-ahjs-api
- description: The appointments API from Coperniq — 2 operation(s) for appointments.
  name: Coperniq appointments API
  slug: coperniq-appointments-api
- description: The assets API from Coperniq — 2 operation(s) for assets.
  name: Coperniq assets API
  slug: coperniq-assets-api
- description: The authentication API from Coperniq — 1 operation(s) for authentication.
  name: Coperniq authentication API
  slug: coperniq-authentication-api
- description: The bills API from Coperniq — 3 operation(s) for bills.
  name: Coperniq bills API
  slug: coperniq-bills-api
- description: The calls API from Coperniq — 3 operation(s) for calls.
  name: Coperniq calls API
  slug: coperniq-calls-api
- description: The catalogItems API from Coperniq — 2 operation(s) for catalogitems.
  name: Coperniq catalogItems API
  slug: coperniq-catalogitems-api
- description: The contacts API from Coperniq — 2 operation(s) for contacts.
  name: Coperniq contacts API
  slug: coperniq-contacts-api
- description: The files API from Coperniq — 6 operation(s) for files.
  name: Coperniq files API
  slug: coperniq-files-api
- description: The forms API from Coperniq — 4 operation(s) for forms.
  name: Coperniq forms API
  slug: coperniq-forms-api
- description: The formTemplates API from Coperniq — 2 operation(s) for formtemplates.
  name: Coperniq formTemplates API
  slug: coperniq-formtemplates-api
- description: The invoices API from Coperniq — 4 operation(s) for invoices.
  name: Coperniq invoices API
  slug: coperniq-invoices-api
- description: The labels API from Coperniq — 2 operation(s) for labels.
  name: Coperniq labels API
  slug: coperniq-labels-api
- description: The lineItems API from Coperniq — 2 operation(s) for lineitems.
  name: Coperniq lineItems API
  slug: coperniq-lineitems-api
- description: The notes API from Coperniq — 5 operation(s) for notes.
  name: Coperniq notes API
  slug: coperniq-notes-api
- description: The opportunities API from Coperniq — 3 operation(s) for opportunities.
  name: Coperniq opportunities API
  slug: coperniq-opportunities-api
- description: The payments API from Coperniq — 4 operation(s) for payments.
  name: Coperniq payments API
  slug: coperniq-payments-api
- description: The projects API from Coperniq — 3 operation(s) for projects.
  name: Coperniq projects API
  slug: coperniq-projects-api
- description: The properties API from Coperniq — 1 operation(s) for properties.
  name: Coperniq properties API
  slug: coperniq-properties-api
- description: The quotes API from Coperniq — 5 operation(s) for quotes.
  name: Coperniq quotes API
  slug: coperniq-quotes-api
- description: The reminders API from Coperniq — 4 operation(s) for reminders.
  name: Coperniq reminders API
  slug: coperniq-reminders-api
- description: The sites API from Coperniq — 3 operation(s) for sites.
  name: Coperniq sites API
  slug: coperniq-sites-api
- description: The taxes API from Coperniq — 1 operation(s) for taxes.
  name: Coperniq taxes API
  slug: coperniq-taxes-api
- description: The users API from Coperniq — 3 operation(s) for users.
  name: Coperniq users API
  slug: coperniq-users-api
- description: The vendors API from Coperniq — 4 operation(s) for vendors.
  name: Coperniq vendors API
  slug: coperniq-vendors-api
- description: The workflows API from Coperniq — 2 operation(s) for workflows.
  name: Coperniq workflows API
  slug: coperniq-workflows-api
- description: The workOrders API from Coperniq — 9 operation(s) for workorders.
  name: Coperniq workOrders API
  slug: coperniq-workorders-api
artifact_total: 34
asyncapis:
- description: ''
  name: Coperniq Webhooks
  slug: coperniq-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.coperniq.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coperniq.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.coperniq.io/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.coperniq.io/coperniq-api/quick-start
- group: auth
  title: ''
  type: Authentication
  url: authentication/coperniq-authentication.yml
- group: build
  title: ''
  type: SDKs
  url: packages/coperniq-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/coperniq-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coperniq-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coperniq-agentic-access.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/coperniq-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/coperniq-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/coperniq-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coperniq-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coperniq-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.coperniq.io/coperniq-api/introduction
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/coperniq-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coperniq-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/coperniq-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/coperniq-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/coperniq-api-catalog.json
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coperniq-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coperniq-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://support.coperniq.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coperniq
- group: operate
  title: ''
  type: Roadmap
  url: https://coperniq.canny.io/feature-requests
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coperniq.io/pricing
- group: start
  title: ''
  type: Login
  url: https://app.coperniq.io/
- group: start
  title: ''
  type: SignUp
  url: https://app.coperniq.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coperniq.io/msa
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coperniq.io/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.coperniq.io/
created: '2026-07-17'
description: 'Coperniq is an AI-powered operating system for residential and commercial contractors across solar, storage, HVAC, electrical, plumbing, and roofing trades, consolidating sales, project management, service operations, dispatch, and cashflow into one system. Its REST API (https://api.coperniq.io/v1) lets developers automate projects, opportunities, accounts, contacts, sites, assets, work orders, forms, quotes, invoices, bills, payments, and more, with API-key authentication, page-based pagination, per-key rate limiting, and outbound automation webhooks. Coperniq was surfaced as a portfolio company of Initialized Capital (sector: climate) and enriched into the API Evangelist network from its public developer surface.'
image: https://framerusercontent.com/assets/f2W0W5l9aLIr0KH47O4tLLBZnE.png
layout: provider
mcp_servers:
- description: ''
  name: coperniq-mcp.yml
  slug: coperniq-mcpyml
modified: '2026-07-18'
name: Coperniq
nav: Providers
network: true
overview: 'Coperniq publishes 28 APIs on the [APIs.io](https://apis.io/) network, including accounts API, ahJs API, appointments API, and 25 more. Tagged areas include Company, Climate, Solar, Construction, and Field Service Management.


  The Coperniq catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Coperniq''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, support, pricing, and 25 more developer resources.'
random_paper: 49
rate_limits:
- limit_count: 2
  name: Coperniq Rate Limits
  slug: coperniq-rate-limits
score:
  band: developing
  composite: 57.5
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 64.1
    developer_ergonomics: 71.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 63.2
  previous_composite: 57.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Coperniq Authentication
  slug: coperniq-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Coperniq Domain Security
  slug: coperniq-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: coperniq
tags:
- Company
- Climate
- Solar
- Construction
- Field Service Management
- Project Management
- Contractors
- CRM
- Energy
website: https://www.coperniq.io/
---
