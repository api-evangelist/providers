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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: RESTful API for storing, searching, updating, and deleting regulated records inside a selected country's borders, authenticated with OAuth2 client-credentials and encrypted with AES-GCM. Supports sing
  name: InCountry REST API
  slug: incountry-rest-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://incountry.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.incountry.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://docs.incountry.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.incountry.com/rest-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.incountry.com/data-residency-as-a-service/tutorial/
- group: company
  title: ''
  type: Blog
  url: https://incountry.com/news-blog/
- group: operate
  title: ''
  type: Support
  url: https://incountry.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://incountry.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://portal.incountry.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://incountry.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://incountry.com/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.incountry.com/
- group: build
  title: ''
  type: Postman
  url: https://docs.incountry.com/assets/files/RestAPI_Demo_oAuth.postman_collection-e8b012cac5488563ba466e6ea44c309c.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/incountry-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/incountry-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/incountry-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/incountry-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/incountry-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/incountry-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/incountry-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/incountry-error-codes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/incountry-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://incountry.com/resource/security-and-compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: security/incountry-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/incountry-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/incountry-llms.txt
created: '2026-07-17'
description: InCountry is a data-residency-as-a-service (DRaaS) platform that lets companies store, process, and comply with the data-localization and privacy laws of specific countries without building in-country infrastructure. Its OAuth2-secured REST API stores regulated records (PII, financial, and health data) inside a chosen country's borders using AES-GCM 256-bit encryption, exposing CRUD, batch, search, aggregate, clone, and attachment operations keyed by country and record key. InCountry also operates AgentCloak, a hosted Model Context Protocol (MCP) server that anonymizes (cloaks) and restores (uncloaks) personally identifiable information for AI agents. The platform supports data residency across 90+ jurisdictions and is certified against SOC 2 Type II, ISO 27001, ISO 27701, PCI DSS, and HIPAA.
image: https://incountry.com/wp-content/uploads/2019/07/logo.png
layout: provider
mcp_servers:
- description: ''
  name: incountry-mcp.yml
  slug: incountry-mcpyml
modified: '2026-07-19'
name: InCountry
nav: Providers
network: true
overview: 'InCountry publishes 1 API on the [APIs.io](https://apis.io/) network: REST API. Tagged areas include Company, Data Residency, Data Localization, Compliance, and Privacy.


  InCountry''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, authentication, and 19 more developer resources.'
random_paper: 43
score:
  band: thin
  composite: 39.6
  delta: -0.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 71.7
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 39.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/incountry/refs/heads/main/screenshots/incountry-2026-07-25T222340.png
security:
- kind: authentication
  name: Incountry Authentication
  slug: incountry-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Incountry Domain Security
  slug: incountry-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Incountry Trust Center
  slug: incountry-trust-center
  summary_line: SOC 1 Type II, SOC 2 Type II, SOC 3, ISO/IEC 27001:2022, ISO 27017, ISO 27018, ISO 27701, PCI DSS, HIPAA, CSA STAR Level 2, GxP
slug: incountry
tags:
- Company
- Data Residency
- Data Localization
- Compliance
- Privacy
- Data Security
- Encryption
- PII
- GDPR
- Data Sovereignty
- MCP
website: https://incountry.com/
---
