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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: inFakt's REST API (v3) for automating invoicing and accounting. Resources are addressed with a .json extension under /api/v3/ and authenticated with a per-account API key sent in the X-inFakt-ApiKey h
  name: inFakt API v3
  slug: infakt-api-v3
artifact_total: 6
asyncapis:
- description: ''
  name: Infakt Webhooks
  slug: infakt-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/infakt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infakt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.infakt.pl
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.infakt.pl/api/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.infakt.pl/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.infakt.pl/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.infakt.pl/integracje-z-infakt-za-pomoca-api/
- group: operate
  title: ''
  type: Support
  url: https://pomoc.infakt.pl/hc/pl
- group: company
  title: ''
  type: Blog
  url: https://www.infakt.pl/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.infakt.pl/cennik/
- group: start
  title: ''
  type: SignUp
  url: https://konto.infakt.pl/rejestracja
- group: start
  title: ''
  type: Login
  url: https://konto.infakt.pl/zaloguj
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.infakt.pl/owu/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.infakt.pl/polityka-prywatnosci/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.infakt.pl/
- group: auth
  title: ''
  type: Security
  url: https://www.infakt.pl/bugbounty/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.infakt.pl/historia-zmian-w-aplikacji-infakt/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/infakt-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/infakt-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/infakt-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/infakt-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/infakt-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/infakt-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/infakt-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/infakt-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/infakt-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/infakt-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/infakt-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/infakt-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/infakt-changelog.yml
created: '2026-07-17'
description: inFakt is a Polish fintech platform that combines invoicing software, online accounting, and dedicated bookkeeper services for sole proprietors (JDG), limited-liability companies (sp. z o.o.), foundations and other business types operating in Poland. Used by over 460,000 companies and headquartered in Kraków, inFakt offers a web app, iOS/Android mobile apps, deep KSeF (Poland's National e-Invoice System) integration, and a REST API (v3, JSON) for third-party integrations. The API exposes invoices, clients, products, costs, bank accounts, VAT exemptions, payment methods and business-activity data so e-commerce shops, CRMs and accounting tools can automate invoicing, cost booking and tax compliance. inFakt also publishes a hosted MCP server so AI agents can operate a company's accounting through Claude and other MCP clients.
image: https://www.infakt.pl/images/logo-infakt.png
layout: provider
mcp_servers:
- description: ''
  name: infakt-mcp.yml
  slug: infakt-mcpyml
modified: '2026-07-19'
name: inFakt
nav: Providers
network: true
overview: 'inFakt publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Accounting, Invoicing, Fintech, and Bookkeeping.


  The inFakt catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  inFakt''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
random_paper: 70
score:
  band: developing
  composite: 50.9
  delta: 7.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 67.4
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 50.0
  previous_composite: 43.8
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/infakt/refs/heads/main/screenshots/infakt-2026-07-25T222350.png
security:
- kind: authentication
  name: Infakt Authentication
  slug: infakt-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Infakt Domain Security
  slug: infakt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Infakt Vulnerability Disclosure
  slug: infakt-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: infakt
tags:
- Company
- Accounting
- Invoicing
- Fintech
- Bookkeeping
- e-Invoicing
- KSeF
- Tax
- Poland
- SMB
website: https://www.infakt.pl
---
