---
access_model:
  confidence: high
  label: Paid seats with a free trial; API metered by a purchased quota pack
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - authentication
  - https://www.fxiaoke.com/ap/market-price/
  - https://developer.fxiaoke.com/openapi_v2/start/guide/rate.html
  trial: true
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.8
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The Fxiaoke Open API v2 exposes CRM business objects (accounts, contacts, leads, opportunities, products, orders) and common services (approval workflows, directory/contact sync, business-data sync) a
  name: Fxiaoke Open API v2
  slug: fxiaoke-open-api-v2
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: http://www.fxiaoke.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://open.fxiaoke.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fxiaoke.com/openapi_v2/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.fxiaoke.com/openapi_v2/object/CommoditiesAndProducts/ProductObj/add.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.fxiaoke.com/openapi_v2/start/quickstart/start.html
- group: operate
  title: ''
  type: Support
  url: https://help.fxiaoke.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fxiaoke.com/ap/market-price/
- group: company
  title: ''
  type: Blog
  url: https://www.fxiaoke.com/crm/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fxiaoke.com/protocols/index.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fxiaoke.com/secure/index.html
- group: auth
  title: ''
  type: Authentication
  url: authentication/fxiaoke-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fxiaoke-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fxiaoke-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fxiaoke-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fxiaoke-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fxiaoke-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fxiaoke-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fxiaoke-domain-security.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.fxiaoke.com/ap/reg/
- group: start
  title: ''
  type: Login
  url: https://www.fxiaoke.com/XV/User/Login
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.fxiaoke.com/
- group: build
  title: ''
  type: Packages
  url: packages/fxiaoke-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fxiaoke-packages.yml
- group: design
  title: ''
  type: Components
  url: components/fxiaoke-components.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fxiaoke-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/fxiaoke-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fxiaoke-data-model.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fxiaoke-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/fxiaoke-trust-center.yml
created: '2026-07-17'
description: Fxiaoke (纷享销客 / Fenxiang) is a Chinese enterprise SaaS company providing a connected, AI-driven "Agentic CRM" platform that spans marketing, sales, and customer service for 6,000+ enterprise customers across manufacturing, consumer goods, healthcare, and technology. Its Open API v2 platform (developer.fxiaoke.com) exposes CRM business objects (accounts, contacts, leads, opportunities, products, orders) and common services such as approval workflows, contact/directory sync, and business-data sync over a JSON/HTTP RPC interface hosted at open.fxiaoke.com. Authentication uses a self-built enterprise application (appId + appSecret + permanentCode) exchanged for a corp/app access token, alongside a modern OAuth 2.1 authorization server (PKCE, dynamic client registration) discoverable via RFC 8414 metadata. Backed by DCM Ventures and Qiming Venture Partners.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fxiaoke.png
layout: provider
modified: '2026-08-13'
name: Fxiaoke
nav: Providers
network: true
overview: 'Fxiaoke publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, CRM, Sales, and Marketing.


  Fxiaoke''s developer surface includes documentation, API reference, getting-started guide, support, pricing, engineering blog, authentication, and 22 more developer resources.'
plans:
- name: Fxiaoke Plans Pricing
  plan_count: 3
  slug: fxiaoke-plans-pricing
random_paper: 147
rate_limits:
- limit_count: 4
  name: Fxiaoke Rate Limits
  slug: fxiaoke-rate-limits
scopes:
- name: Fxiaoke Scopes
  scope_count: 0
  slug: fxiaoke-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.5
  delta: 17.5
  facets:
    commercial_clarity: 92.1
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 27.0
  provenance:
    conformance: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/fxiaoke/refs/heads/main/screenshots/fxiaoke-2026-07-25T215341.png
security:
- kind: authentication
  name: Fxiaoke Authentication
  slug: fxiaoke-authentication
  summary_line: oauth2/custom-token · 4 schemes
- kind: domain-security
  name: Fxiaoke Domain Security
  slug: fxiaoke-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Fxiaoke Trust Center
  slug: fxiaoke-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27701, ISO/IEC 20000-1, ISO 9001, MLPS / 等级保护, SOC 1, SOC 2
slug: fxiaoke
tags:
- Company
- Enterprise
- CRM
- Sales
- Marketing
- Customer Service
- SaaS
- China
- PaaS
website: http://www.fxiaoke.com/
---
