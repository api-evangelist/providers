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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 53.8
  scored_at: '2026-08-12'
api_count: 9
apis:
- description: Single API onto the SIX financial data universe - real-time, intraday, end-of-day, and historical pricing across asset classes, reference data, corporate actions, tax, and ESG datasets from 900+ price
  name: SIX Web API
  slug: six-web-api
- description: REST/JSON bulk retrieval of the entire SIX financial data catalog - corporate actions, equities and fixed income reference data, and end-of-day pricing - as full extracts or delta updates since a give
  name: SIX Bulk API
  slug: six-bulk-api
- description: Switzerland's open banking platform connecting banks and third-party service providers over RESTful JSON/XML APIs with OAuth consent flows - Account Information Services (AIS), Payment Submission Serv
  name: SIX bLink API
  slug: blink-api
- description: REST API for card issuers on the debiX debit and mobile payment platform - transaction processing, card token lifecycle, push notifications, and bulk operations - with publicly downloadable OpenAPI 3.
  name: SIX debiX API
  slug: debix-api
- description: Bidirectional authentication API pair between SIX and auth providers supporting the 3DS out-of-band (OOB) authentication flow for debiX debit cards, with publicly downloadable OpenAPI definitions cove
  name: SIX debiX Auth Provider API
  slug: debix-auth-provider-api
- description: Master data required for electronic payments in Switzerland - bank master records in JSON and CSV plus IBAN tooling - published openly on the SIX API portal; the documented production endpoints respon
  name: Swiss Bank Master API
  slug: swiss-bank-master-api
- description: Current operational status of the electronic payment services run by SIX Interbank Clearing Ltd, publicly documented with downloadable OpenAPI; GET /servicestatus on the documented production host ret
  name: SIC Service Status API
  slug: sic-service-status-api
- description: Scheduling information for the electronic payment services provided by SIX Interbank Clearing Ltd - clearing day calendar lookups - publicly documented on the SIX API portal with a downloadable OpenAP
  name: SIC Clearing Day Calendar API
  slug: sic-clearing-day-calendar-api
- description: Security settlement information reporting from the SIX custody cockpit for the Swiss market, publicly documented on the SIX API portal with a downloadable OpenAPI 3.0 definition (CC BY-ND 4.0 licensed
  name: Settlement Info Reporting API
  slug: settlement-info-reporting-api
artifact_total: 14
asyncapis:
- description: ''
  name: Six Group Debix Push Webhooks
  slug: six-group-debix-push-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/six-group-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/six-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.six-group.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.six-group.com/en/home.html
- group: docs
  title: ''
  type: Documentation
  url: https://apiportal.six-group.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/six-group
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sixgroup
- group: company
  title: ''
  type: Blog
  url: https://www.six-group.com/en/newsroom.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.six-group.com/en/services/legal/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.six-group.com/en/services/legal/privacy-statement.html
- group: operate
  title: ''
  type: Support
  url: https://www.six-group.com/en/contacts.html
- group: build
  title: ''
  type: Packages
  url: packages/six-group-packages.yml
- group: design
  title: ''
  type: Components
  url: components/six-group-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/six-group-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/six-group-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/six-group-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/six-group-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/six-group-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/six-group-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/six-group-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/six-group-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/six-group-authentication.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/six-group
- group: start
  title: ''
  type: Sandbox
  url: sandbox/six-group-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/six-group-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/six-group-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/six-group-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/six-group-debix-push-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.six-group.com/en/home.html
- group: docs
  title: ''
  type: APIReference
  url: https://apiportal.six-group.com/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.debix.six-group.com/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://apiportal.six-group.com/register
- group: build
  title: ''
  type: Postman
  url: https://docs.blink.six-group.com/docs/downloads
created: '2026-07-21'
description: SIX operates the financial market infrastructure of Switzerland and Spain, including SIX Swiss Exchange, BME, and Swiss interbank clearing and securities services, alongside SIX Financial Information, one of the largest global market data vendors. It sells real-time, intraday, end-of-day, and historical pricing, reference data, corporate actions, and regulatory/ESG datasets from more than 900 price sources, delivered via the SIX Web API (REST/JSON, GraphQL, WebSocket), the SIX Bulk API, streaming Market Data Feed, SIX Flex and Valordata Feed files, and Snowflake cloud shares. A public developer portal at developer.six-group.com fronts the bLink open banking platform, the debiX debit card API, and a shared Kong-based API catalog with Swiss interbank clearing and settlement APIs. Financial data access is enterprise and sales-gated with MTLS certificate authentication, while several Swiss payment infrastructure APIs are publicly documented with downloadable OpenAPI.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/six-group.png
layout: provider
mcp_servers:
- description: ''
  name: six-group-mcp.yml
  slug: six-group-mcpyml
modified: '2026-07-22'
name: SIX
nav: Providers
network: true
overview: 'SIX publishes 7 APIs on the [APIs.io](https://apis.io/) network, including bLink API, debiX API, debiX Auth Provider API, and 4 more. Tagged areas include Financial, Market Data, Stocks, Reference Data, and Corporate Actions.


  The SIX catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SIX''s developer surface includes developer portal, documentation, engineering blog, support, authentication, sandbox, changelog, and 27 more developer resources.'
random_paper: 102
score:
  band: developing
  composite: 51.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 63.8
    developer_ergonomics: 66.8
    discoverability: 83.3
    governance: 20.8
    operational_transparency: 47.4
  previous_composite: 51.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 39.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/six-group/refs/heads/main/screenshots/six-group-2026-07-22T202623.png
security:
- kind: authentication
  name: Six Group Authentication
  slug: six-group-authentication
  summary_line: mutualTLS/oauth2/none · 6 schemes
- kind: domain-security
  name: Six Group Domain Security
  slug: six-group-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Six Group Vulnerability Disclosure
  slug: six-group-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: six-group
tags:
- Financial
- Market Data
- Stocks
- Reference Data
- Corporate Actions
- Real-Time
- Exchange
- Open Banking
- Payments
- Switzerland
website: https://www.six-group.com/
---
