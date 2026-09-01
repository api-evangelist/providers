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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Pliant''s Pro API enables customers to access Pliant credit card data and features programmatically — issue and manage cards, apply card controls and limits, retrieve transactions and accounting data, '
  name: Pliant Pro API (Customer)
  slug: pliant-pro-api-customer
artifact_total: 6
asyncapis:
- description: ''
  name: Pliant Callbacks Webhooks
  slug: pliant-callbacks-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pliant-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.getpliant.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/pliant-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pliant-well-known.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://customer-api.getpliant.com
- group: docs
  title: ''
  type: Documentation
  url: https://customer-api.getpliant.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://customer-api.getpliant.com/reference/list-organizations
- group: start
  title: ''
  type: GettingStarted
  url: https://customer-api.getpliant.com/docs/introduction
- group: company
  title: ''
  type: Website
  url: https://www.getpliant.com/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.getpliant.com/en-us/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getpliant.com/en-us/pricing
- group: operate
  title: ''
  type: Support
  url: https://help.getpliant.com/en/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.getpliant.com/en/
- group: start
  title: ''
  type: SignUp
  url: https://www.getpliant.com/en-us/book-demo
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getpliant.com/en-us/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://customer-api.getpliant.com/page/status
- group: operate
  title: ''
  type: Deprecation
  url: https://customer-api.getpliant.com/docs/versioning
- group: operate
  title: ''
  type: ChangeLog
  url: https://customer-api.getpliant.com/changelog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pliant-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pliant-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/pliant-callbacks-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pliant-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pliant-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/pliant-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pliant-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/pliant-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pliant-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/pliant-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/pliant-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pliant-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pliant-domain-security.yml
created: '2026-07-17'
description: Pliant is a Berlin-based financial technology company offering a business credit card and spend-management platform, plus Cards-as-a-Service (CaaS) and Banking-as-a-Service (BaaS) infrastructure for banks and platforms. Its Pro API lets customers programmatically issue physical, virtual, single-use and specialized cards (travel, fleet, benefits, insurance-claim), apply card controls and advanced limits, retrieve transactions and accounting data, manage receipts, projects, teams and statements, and subscribe to real-time callbacks. Pliant is PCI DSS certified, ISO/IEC 27001:2022 certified and holds an EU e-money license, with customers including BMW, Decathlon, Deutsche Telekom and Commerzbank.
image: https://a.storyblok.com/f/169635/1200x630/92b10eaf7c/pliant-og-image.png
layout: provider
mcp_servers:
- description: 'Pliant publishes an official hosted/remote MCP server for the Pro API (Customer). It exposes direct API access to Pliant Pro API functionality, documentation search, real-time data from the connected '
  name: Pliant MCP Server
  slug: pliant-mcp-server
modified: '2026-07-20'
name: Pliant
nav: Providers
network: true
overview: 'Pliant publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Corporate Cards, Card Issuing, and Spend Management.


  The Pliant catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pliant''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, support, signup flow, and 25 more developer resources.'
random_paper: 18
score:
  band: developing
  composite: 47.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 32.9
  previous_composite: 47.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 62.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pliant/refs/heads/main/screenshots/pliant-2026-08-17T081307.png
security:
- kind: authentication
  name: Pliant Authentication
  slug: pliant-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Pliant Domain Security
  slug: pliant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pliant Vulnerability Disclosure
  slug: pliant-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pliant
tags:
- Company
- Payments
- Corporate Cards
- Card Issuing
- Spend Management
- Expense Management
- Fintech
- Cards-as-a-Service
- Banking as a Service
- Travel
- Accounting
website: https://www.getpliant.com/en-us
---
