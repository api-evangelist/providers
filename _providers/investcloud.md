---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.5
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: InvestCloud's developer platform, branded "Wealthsqope Digital Developer". Its own public landing page advertises getting-started guides, "full API docs for web services and embedded widgets", video t
  name: Wealthsqope Digital Developer Platform
  slug: wealthsqope-digital-developer-platform
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.investcloud.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.investcloud.com/
- group: start
  title: ''
  type: Login
  url: https://developer.investcloud.com/login/
- group: company
  title: ''
  type: Blog
  url: https://www.investcloud.com/resources/insights/
- group: operate
  title: ''
  type: Support
  url: https://www.investcloud.com/about-us/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.investcloud.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.investcloud.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/investcloud
- group: auth
  title: ''
  type: DomainSecurity
  url: security/investcloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/investcloud-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/investcloud-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/investcloud-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/investcloud-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/investcloud-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/investcloud-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/investcloud-rate-limits.yml
coverage:
  checked: '2026-08-23'
  detail: InvestCloud markets a full developer platform at developer.investcloud.com ("Wealthsqope Digital Developer" — API docs for web services and embedded widgets, code recipes, client libraries, application API keys) but the entire portal is a noindex WordPress site behind a username/password login, and every unauthenticated path on it returns the same 33,933-byte landing page, including a nonsense control path.
  evidence:
  - status: 200
    url: https://developer.investcloud.com/
  - status: 200
    url: https://developer.investcloud.com/login/
  - status: 200
    url: https://developer.investcloud.com/openapi.json
  - status: 404
    url: https://www.investcloud.com/openapi.json
  - status: 0
    url: https://api.investcloud.com/
  reason: partner-login
  state: gated
created: '2026-08-23'
description: InvestCloud is a wealth-management technology company that provides an AI-driven digital wealth platform connecting advisors, financial institutions, asset managers, TAMPs, RIAs and investors across the full investment lifecycle. Its product surface spans front-office advisor and client solutions, a wealth data platform ("Digital Warehouse") that aggregates custodial, market and portfolio data, managed account solutions including the Advisor Programs List (APL) and Private Markets Account, post-trade processing and settlement, revenue management, and the NaviPlan and RetireUp financial planning products acquired with Advicent. InvestCloud markets a developer platform — branded "Wealthsqope Digital Developer" — offering web-service APIs, embeddable widgets, code recipes, client libraries and application API keys, but that platform and its reference documentation sit entirely behind a portal login, and no machine-readable API contract is published publicly.
image: https://www.investcloud.com/wp-content/uploads/2025/12/cropped-ic_favicon-270x270.png
layout: provider
modified: '2026-08-23'
name: InvestCloud
nav: Providers
network: true
overview: 'InvestCloud publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wealth Management, Financial Services, Investment Management, and WealthTech.


  InvestCloud''s developer surface includes engineering blog, support, authentication, and 13 more developer resources.'
plans:
- name: Investcloud Plans Pricing
  plan_count: 0
  slug: investcloud-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Investcloud Rate Limits
  slug: investcloud-rate-limits
score:
  band: emerging
  composite: 16.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Investcloud Authentication
  slug: investcloud-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Investcloud Domain Security
  slug: investcloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: investcloud
tags:
- Company
- Wealth Management
- Financial Services
- Investment Management
- WealthTech
- Portfolio Management
- Financial Planning
- Managed Accounts
- Advisor Technology
- Data Aggregation
website: https://www.investcloud.com/
---
