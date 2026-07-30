---
access_model:
  confidence: medium
  label: Partner · Registration required (Okta OIDC)
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - developer-portal
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
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-07-28'
api_count: 7
apis:
- description: The Custody API in the Northern Trust API Store gives institutional clients programmatic access to global custody data — holdings, positions, safekept assets, settlements, and account-level custody in
  name: Northern Trust Custody API
  slug: custody-api
- description: The Fund Accounting API exposes Northern Trust's fund accounting and net asset value (NAV) servicing data to institutional and fund clients — book of record accounting, valuations, income, expenses, a
  name: Northern Trust Fund Accounting API
  slug: fund-accounting-api
- description: The Transfer Agency API provides programmatic access to Northern Trust's transfer agency servicing — shareholder registers, investor transactions, subscriptions and redemptions, dealing, and related t
  name: Northern Trust Transfer Agency API
  slug: transfer-agency-api
- description: The Middle Office API surfaces Northern Trust's whole-office and middle-office outsourcing data — trade lifecycle, post-trade processing, position keeping, reconciliation, and investment operations da
  name: Northern Trust Middle Office API
  slug: middle-office-api
- description: The Data Management API delivers consolidated investment and reference data from Northern Trust's data services — investment book of record, aggregated holdings, reference and market data, and cross-d
  name: Northern Trust Data Management API
  slug: data-management-api
- description: The Risk and Performance API exposes Northern Trust's investment risk and performance measurement data — performance returns, attribution, benchmarks, and risk analytics produced by the firm's perform
  name: Northern Trust Risk and Performance API
  slug: risk-and-performance-api
- description: The Event Notification service in the Northern Trust API Store lets registered clients subscribe to and receive asynchronous notifications about events across their custody and servicing data — a webh
  name: Northern Trust Event Notification API
  slug: event-notification-api
artifact_total: 11
asyncapis:
- description: ''
  name: Northern Trust Event Notification Webhooks
  slug: northern-trust-event-notification-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.northerntrust.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ntrs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ntrs.com/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ntrs.com/get-started
- group: start
  title: ''
  type: SignUp
  url: https://developer.ntrs.com/get-started
- group: operate
  title: ''
  type: Support
  url: https://developer.ntrs.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.ntrs.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.ntrs.com/global-privacy-standards
- group: company
  title: ''
  type: Blog
  url: https://www.northerntrust.com/united-states/insights-research
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/northern-trust
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/northern-trust
- group: auth
  title: ''
  type: DomainSecurity
  url: security/northern-trust-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/northern-trust-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/northern-trust-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/northern-trust-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/northern-trust-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/northern-trust-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/northern-trust-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/northern-trust-llms.txt
created: '2026-03-21'
description: 'Northern Trust is a Fortune 500 global financial services firm providing asset servicing, asset management, wealth management, and banking to corporations, institutions, family offices, and individuals worldwide. Its first-party developer program, the Northern Trust API Store at developer.ntrs.com, exposes asset-servicing capabilities as REST APIs across custody, fund accounting, transfer agency, middle office, data management, and risk and performance, plus an event-notification service. The catalog is a partner/registration surface: browsing product domains is public, but API reference specifications (downloadable as spec.json) and live access sit behind Okta-based OIDC login. Northern Trust does not publish a public consumer open-banking API; retail account connectivity is reached indirectly through data aggregators.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/northern-trust.png
layout: provider
modified: '2026-07-23'
name: Northern Trust
nav: Providers
network: true
overview: 'Northern Trust publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Banking, Wealth Management, Asset Servicing, and Asset Management.


  The Northern Trust catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Northern Trust''s developer surface includes documentation, getting-started guide, signup flow, support, engineering blog, authentication, and 13 more developer resources.'
press:
- date: '2026-05-25'
  title: 'Stewardship in Focus: Artificial Intelligence'
  url: https://www.northerntrust.com/content/dam/northerntrust/pws/nt/documents/asset-management/stewardship-in-focus-artificial-intelligence.pdf
- date: '2026-05-25'
  title: Party Like It's 2026 | The View from Here
  url: https://www.northerntrust.com/japan/insights-research/2026/the-view-from-here/party-like-its-2026
- date: '2026-05-25'
  title: AI's Evolution in Financial Services and Its Impact on the ...
  url: https://www.northerntrust.com/united-states/insights-research/2025/asset-servicing/ai-evolution-financial-services-impact-on-future
- date: '2026-05-25'
  title: Northern Trust Asset Management Forecasts AI-Driven ...
  url: https://www.businesswire.com/news/home/20260114204324/en/Northern-Trust-Asset-Management-Forecasts-AI-Driven-Strength-in-Private-Markets-United-States-Japan-and-Australia-to-Lead-Equity-Returns-over-Next-Decade
- date: '2026-05-25'
  title: Uncovering Alpha In The Networked Economy
  url: https://www.northerntrust.com/content/dam/northerntrust/pws/nt/documents/asset-management/uncovering-alpha-in-the-networked-economy.pdf
random_paper: 27
scopes:
- name: Northern Trust Scopes
  scope_count: 10
  slug: northern-trust-scopes
  summary_line: 10 scopes · authorizationCode
score:
  band: developing
  composite: 43.4
  delta: 4.5
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 45.7
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 38.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 60.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/northern-trust/refs/heads/main/screenshots/northern-trust-2026-06-20T190416.png
security:
- kind: authentication
  name: Northern Trust Authentication
  slug: northern-trust-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Northern Trust Domain Security
  slug: northern-trust-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: northern-trust
tags:
- Fortune 500
- Banking
- Wealth Management
- Asset Servicing
- Asset Management
- Financial Services
- United States
website: https://www.northerntrust.com
---
