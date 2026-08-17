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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The Advisor API connects advisor applications to Wealth.com, exposing client, asset, document, contact, quiz, AI-notes, client-group and top-account resources over JSON HTTPS, with OAuth2 (authorizati
  name: Wealth.com Advisor API
  slug: wealthcom-advisor-api
artifact_total: 7
asyncapis:
- description: ''
  name: Wealthcom Webhooks
  slug: wealthcom-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.wealth.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.wealth.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.wealth.com/advisor
- group: docs
  title: ''
  type: APIReference
  url: https://developer.wealth.com/advisor
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.wealth.com/advisor/authentication
- group: auth
  title: ''
  type: Authentication
  url: authentication/wealthcom-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wealthcom-scopes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wealthcom-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wealthcom-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wealthcom-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wealthcom-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wealth.com
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wealthcom-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wealthcom-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wealthcom-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.wealth.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/wealthcom-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wealthcom-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wealthcom-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wealthcom-llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wealth.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.wealth.com/login
- group: start
  title: ''
  type: Login
  url: https://app.wealth.com/login
- group: operate
  title: ''
  type: Support
  url: https://wealth.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.wealth.com/resources/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wealth.com/legal-policies/#tos-content
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wealth.com/legal-policies/#privacy-content
created: '2026-07-17'
description: Wealth.com is the industry-leading estate and tax planning platform for financial advisors, unifying estate document creation, tax intelligence, and its proprietary Ester AI assistant to help advisors deliver sophisticated planning at scale. For developers, Wealth.com publishes an Advisor API (OAuth2, JSON over HTTPS) that connects advisor applications to the platform for managing clients, assets, documents, contacts, quizzes, and AI notes, plus a webhook surface for real-time events and an Onboarding API for partner-referred client onboarding. A separate SFTP interface supports bulk data exchange. The company is backed by GV (Google Ventures) and integrates with Salesforce, Orion, Redtail, Wealthbox, Addepar, eMoney, and other advisor tools.
image: https://www.wealth.com/favicon.ico
layout: provider
modified: '2026-07-21'
name: Wealth.com
nav: Providers
network: true
overview: 'Wealth.com publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Estate Planning, Tax Planning, and Wealth Management.


  The Wealth.com catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Wealth.com''s developer surface includes documentation, API reference, getting-started guide, authentication, pricing, signup flow, support, and 20 more developer resources.'
random_paper: 70
rate_limits:
- limit_count: 1
  name: Wealthcom Rate Limits
  slug: wealthcom-rate-limits
scopes:
- name: Wealthcom Scopes
  scope_count: 3
  slug: wealthcom-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 50.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 52.2
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 44.7
  previous_composite: 50.3
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Wealthcom Authentication
  slug: wealthcom-authentication
  summary_line: oauth2/publicKey · 3 schemes
- kind: domain-security
  name: Wealthcom Domain Security
  slug: wealthcom-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Wealthcom Trust Center
  slug: wealthcom-trust-center
  summary_line: SOC 2 Type 2
slug: wealthcom
tags:
- Company
- Enterprise
- Estate Planning
- Tax Planning
- Wealth Management
- Financial Advisors
- Fintech
- Artificial Intelligence
website: https://www.wealth.com
---
