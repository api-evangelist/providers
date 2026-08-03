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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: REST API to embed IRS-authorized income-tax preparation and e-filing. Create a Column Tax user, obtain a short-lived authenticated URL to launch the embedded filing UI, list a user's tax returns and j
  name: Column Tax API
  slug: column-tax-api
artifact_total: 5
asyncapis:
- description: ''
  name: Column Tax Webhooks
  slug: column-tax-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/column-tax-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.columntax.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.columntax.com/docs/welcome
- group: docs
  title: ''
  type: Documentation
  url: https://docs.columntax.com/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://docs.columntax.com/v1.1/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.columntax.com/docs/quick-start
- group: start
  title: ''
  type: Quickstart
  url: https://docs.columntax.com/docs/quick-start
- group: auth
  title: ''
  type: Authentication
  url: https://docs.columntax.com/reference/authentication
- group: operate
  title: ''
  type: Support
  url: https://www.columntax.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.columntax.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/column-tax
- group: operate
  title: ''
  type: StatusPage
  url: https://status.columntax.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.columntax.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.columntax.com/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/column-tax-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/column-tax-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/column-tax-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/column-tax-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/column-tax-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/column-tax-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/column-tax-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/column-tax-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/column-tax-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/column-tax-mcp.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/column-tax-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/column-tax-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/column-tax-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/column-tax-components.yml
created: '2026-07-17'
description: Column Tax is an IRS-authorized, API-first tax filing platform that lets banks, brokerages, neobanks, and SMB/freelancer fintech apps embed a full white-label income-tax preparation and e-file experience directly inside their own product. Partners create a Column Tax user via a server-side REST call, receive a short-lived authenticated URL, and launch the Column Tax UI (web loader or native iOS, Android, and React Native SDKs) embedded in their app, while webhooks report each user through the filing lifecycle. Column Tax offers DIY Filing and Expert Review products, is a SOC 2-certified and IRS-authorized e-file provider, and reports outcomes such as higher retention and direct-deposit switching for embedded partners.
image: https://cdn.prod.website-files.com/6262ffa3aeadc15ee876298b/627bf917c708fc0ec6460fcb_Text_Image.png
layout: provider
mcp_servers:
- description: ''
  name: column-tax-mcp.yml
  slug: column-tax-mcpyml
modified: '2026-07-18'
name: Column Tax
nav: Providers
network: true
overview: 'Column Tax publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Tax, Tax Filing, and Embedded Finance.


  The Column Tax catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Column Tax''s developer surface includes documentation, API reference, getting-started guide, quickstart, authentication, support, engineering blog, and 21 more developer resources.'
random_paper: 82
score:
  band: developing
  composite: 45.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 51.6
    developer_ergonomics: 67.4
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 28.9
  previous_composite: 45.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 46.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/column-tax/refs/heads/main/screenshots/column-tax-2026-07-25T210102.png
security:
- kind: authentication
  name: Column Tax Authentication
  slug: column-tax-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Column Tax Domain Security
  slug: column-tax-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: column-tax
tags:
- Company
- Fintech
- Tax
- Tax Filing
- Embedded Finance
- E-File
- Financial Services
- Banking
- API First
website: https://www.columntax.com/
---
