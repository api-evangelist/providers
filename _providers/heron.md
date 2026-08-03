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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Heron's REST API for document intake, parsing, enrichment, cashflow underwriting, webhooks, and broker/funder submission flows.
  name: Heron API
  slug: heron-api
artifact_total: 8
asyncapis:
- description: 'Heron sends webhook notifications about the progress of asynchronous processes (end-user processing/review and PDF document parsing) to a URL you configure in the Heron dashboard (Settings tab). Each '
  name: Heron Webhooks
  slug: heron-webhooks-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://www.herondata.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.herondata.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.herondata.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.herondata.io/api-reference/authentication
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.herondata.io/
- group: start
  title: ''
  type: Login
  url: https://dashboard.herondata.io/auth/signin
- group: company
  title: ''
  type: Blog
  url: https://www.herondata.io/blog
- group: operate
  title: ''
  type: Support
  url: mailto:hello@herondata.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.herondata.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.herondata.io/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.herondata.io/
- group: auth
  title: ''
  type: TrustCenter
  url: security/heron-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.herondata.io/security
- group: auth
  title: ''
  type: Security
  url: https://www.herondata.io/disclosure
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/heron-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heron-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/heron-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/heron-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/heron-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/heron-rate-limits.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/heron-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/heron-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/heron-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/heron-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/heron-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/heron-mcp.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/heron-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/heron-data-model.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/heron-well-known.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Heron (Heron Data) is a financial-services document-automation and cashflow-underwriting platform. Its API and AI platform handle document intake, classification, parsing and validation, enrichment, policy/rule evaluation, and CRM sync across 50+ document types (bank statements, tax returns, financial statements, ACORD forms). Lenders, MCA funders, brokers, and insurers upload documents for an "end user" (company), then read back parsed transactions, a Heron Score, scorecards, cashflow P&L, anomaly/fraud checks, and decline analytics. The REST API authenticates with an x-api-key header, signals rate limits via x-ratelimit-* headers, and pushes async progress through webhooks. Backed by Insight Partners.
image: https://cdn.prod.website-files.com/675862616b5e61c9450cfef0/677e4fc1e48ddcd5917c71ca_home-og-img.jpg
layout: provider
mcp_servers:
- description: ''
  name: heron-mcp.yml
  slug: heron-mcpyml
modified: '2026-07-19'
name: Heron
nav: Providers
network: true
overview: 'Heron publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Document Automation, Underwriting, and Lending.


  The Heron catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Heron''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, authentication, sandbox, and 23 more developer resources.'
random_paper: 65
rate_limits:
- limit_count: 1
  name: Heron Rate Limits
  slug: heron-rate-limits
score:
  band: developing
  composite: 51.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 50.6
    developer_ergonomics: 62.5
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 55.3
  previous_composite: 51.9
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 54.5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/heron/refs/heads/main/screenshots/heron-2026-07-25T221032.png
security:
- kind: authentication
  name: Heron Authentication
  slug: heron-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Heron Domain Security
  slug: heron-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Heron Vulnerability Disclosure
  slug: heron-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Heron Trust Center
  slug: heron-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2, GDPR, CCPA
slug: heron
tags:
- Company
- Financial Services
- Document Automation
- Underwriting
- Lending
- Cashflow Analytics
- Fintech
- Data Enrichment
website: https://www.herondata.io/
---
