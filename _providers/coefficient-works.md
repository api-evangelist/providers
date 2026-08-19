---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.5
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 4
asyncapis:
- description: ''
  name: Coefficient Works Webhooks
  slug: coefficient-works-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coefficient-works-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coefficient.io/
- group: other
  title: ''
  type: Product
  url: https://coefficient.io/product
- group: docs
  title: ''
  type: Documentation
  url: https://help.coefficient.io/hc/en-us
- group: operate
  title: ''
  type: Support
  url: https://help.coefficient.io/hc/en-us
- group: start
  title: ''
  type: GettingStarted
  url: https://coefficient.io/get-started
- group: company
  title: ''
  type: Blog
  url: https://coefficient.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://coefficient.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://coefficient.io/get-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coefficient.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coefficient.io/privacy-policy
- group: operate
  title: ''
  type: Community
  url: https://coefficient.io/community
- group: company
  title: ''
  type: About
  url: https://coefficient.io/about
- group: operate
  title: ''
  type: ContactUs
  url: https://coefficient.io/contact
- group: company
  title: ''
  type: Careers
  url: https://coefficient.io/careers
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.atlassian.com/vendors/1220522/coefficient-works-inc
- group: other
  title: ''
  type: Templates
  url: https://coefficient.io/templates
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coefficient-works-llms.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/coefficient-works-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/coefficient-works-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/coefficient-works-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coefficient-works-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://coefficient.io/data-security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coeff
created: '2026-07-17'
description: 'Coefficient Works, Inc. (operating as Coefficient) is a San Mateo, California no-code data platform that connects live business data to Google Sheets and Microsoft Excel. Founded in 2019 by Navneet Loiwal and Tommy Tsai, the company provides point-and-click connectors to 60+ business systems including Salesforce, HubSpot, NetSuite, QuickBooks, Snowflake, MySQL, Stripe, Looker, Tableau and Google Ads, with scheduled two-way sync, spreadsheet-native alerting through Slack and email, live web dashboards, and an AI assistant that builds pivot tables, formulas, charts and data-cleaning steps from natural language. Coefficient is a consumer of other providers'' APIs rather than a producer: as of this enrichment pass it publishes no public developer API, no OpenAPI or AsyncAPI description, no client SDKs, and no developer portal, and its "Connect Any API" feature is a consumer-side HTTP client (GET/POST, bearer token / API key / basic auth, cursor, offset and page-number pagination)
  that writes third-party API responses into a sheet. The one programmatic surface Coefficient serves is an inbound webhook trigger URL, issued per import on the Pro and Enterprise plans, that an external system calls to force an immediate refresh — capped at 12 calls per hour with a five-minute minimum interval. Coefficient states it is SOC 2 compliant and provides the audit report on request. Distribution is through the Google Workspace Marketplace and Microsoft AppSource. The company is backed by Battery Ventures, Foundation Capital and S28 Capital.'
image: https://coefficient.io/wp-content/uploads/2026/02/homepage-meta-image-v2.png
layout: provider
modified: '2026-08-14'
name: Coefficient Works
nav: Providers
network: true
overview: 'Coefficient Works is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Spreadsheets, Google Sheets, Microsoft Excel, and Data Integration.


  The Coefficient Works catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Coefficient Works'' developer surface includes documentation, support, getting-started guide, engineering blog, pricing, signup flow, and 18 more developer resources.'
plans:
- name: Coefficient Works Plans Pricing
  plan_count: 4
  slug: coefficient-works-plans-pricing
random_paper: 123
rate_limits:
- limit_count: 2
  name: Coefficient Works Rate Limits
  slug: coefficient-works-rate-limits
score:
  band: developing
  composite: 45.9
  delta: -0.7
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 28.6
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 46.6
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coefficient-works/refs/heads/main/screenshots/coefficient-works-2026-07-25T205946.png
security:
- kind: domain-security
  name: Coefficient Works Domain Security
  slug: coefficient-works-domain-security
  summary_line: TLSv1.3 · DMARC
slug: coefficient-works
tags:
- Company
- Spreadsheets
- Google Sheets
- Microsoft Excel
- Data Integration
- No-Code
- Business Intelligence
- Reporting
- Revenue Operations
- SaaS
website: https://coefficient.io/
---
