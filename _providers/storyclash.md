---
access_model:
  confidence: high
  label: Enterprise, contact sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.storyclash.com/pricing
  - https://www.storyclash.com/integrations/api-integration
  - https://storyclash.notion.site/Storyclash-API-Documentation-1266dc2ddd0880a79cf9e3d34c19fa01
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: 'Enterprise REST API for the Storyclash influencer marketing platform. Three documented endpoints under https://app.storyclash.com/external-api/: GET /campaigns lists the authenticated customer''s campa'
  name: Storyclash API
  slug: storyclash-api
artifact_total: 6
asyncapis:
- description: ''
  name: Storyclash Webhooks
  slug: storyclash-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.storyclash.com/integrations/api-integration
- group: docs
  title: ''
  type: Documentation
  url: https://storyclash.notion.site/Storyclash-API-Documentation-1266dc2ddd0880a79cf9e3d34c19fa01
- group: commercial
  title: ''
  type: Pricing
  url: https://www.storyclash.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.storyclash.com/blog/en
- group: start
  title: ''
  type: Login
  url: https://app.storyclash.com/login
- group: operate
  title: ''
  type: Support
  url: https://help.storyclash.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.storyclash.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.storyclash.com/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://status.storyclash.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/storyclash-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/storyclash-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/storyclash-webhooks.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/storyclash-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/storyclash-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/storyclash-domain-security.yml
- group: docs
  title: ''
  type: APIReference
  url: https://storyclash.notion.site/Storyclash-API-Documentation-1266dc2ddd0880a79cf9e3d34c19fa01
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/storyclash
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.storyclash.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.storyclash.com/request-demo
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/storyclash-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/storyclash-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/storyclash-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/storyclash-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/storyclash-examples.yml
- group: build
  title: ''
  type: Packages
  url: packages/storyclash-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/storyclash-conformance.yml
created: '2026-07-17'
description: 'Storyclash is an AI-powered influencer marketing software platform used by brands and agencies to discover creators, analyze brand and competitor strategies, manage collaborations in a purpose-built CRM, and measure campaign performance and revenue ROI across Instagram, TikTok, YouTube, and Facebook. Its AI-driven creator discovery includes neural visual search over 120M+ creators, letting teams match on a reference image or product URL rather than keywords alone. Storyclash exposes an enterprise REST API with token-based authentication and real-time webhooks that streams campaign KPIs (50+ metrics per campaign), creator profiles, content performance, and revenue attribution as structured JSON into BI tools such as Power BI, Tableau, and Looker Studio. The documented API surface is small and enterprise-gated: three endpoints under https://app.storyclash.com/external-api/ authenticated by a per-customer token passed as a query parameter, with a single outbound webhook that reports
  the outcome of a bulk creator import. The company, headquartered in Linz, Austria, was surfaced as a portfolio company of Speedinvest and has since been acquired by Kolsquare, a team.blue brand, and now trades as "Storyclash by Kolsquare".'
image: https://www.storyclash.com/favicon.ico
layout: provider
modified: '2026-08-13'
name: Storyclash
nav: Providers
network: true
overview: 'Storyclash publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Influencer Marketing, Creator Economy, Social Media Analytics, and Marketing Analytics.


  The Storyclash catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Storyclash''s developer surface includes documentation, pricing, engineering blog, support, authentication, API reference, signup flow, and 19 more developer resources.'
plans:
- name: Storyclash Plans Pricing
  plan_count: 3
  slug: storyclash-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Storyclash Rate Limits
  slug: storyclash-rate-limits
score:
  band: developing
  composite: 53.9
  coverage:
    artifact_dirs: 17
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 49.3
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 53.9
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/storyclash/refs/heads/main/screenshots/storyclash-2026-08-17T082126.png
security:
- kind: authentication
  name: Storyclash Authentication
  slug: storyclash-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Storyclash Domain Security
  slug: storyclash-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: storyclash
tags:
- Company
- Influencer Marketing
- Creator Economy
- Social Media Analytics
- Marketing Analytics
- Campaign Management
- Business Intelligence
- REST API
- Webhook
website: https://www.storyclash.com/integrations/api-integration
---
