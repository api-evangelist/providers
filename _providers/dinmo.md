---
access_model:
  confidence: high
  label: Paid plans from 350 EUR/month, annual commitment, 30-day trial
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - https://www.dinmo.com/pricing
  - plans/dinmo-plans-pricing.yml
  - https://docs.dinmo.io/customer-hub/profiles-api.md
  trial: true
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.5
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Real-time read API for retrieving an activated model record (customer profile and its mapped activation attributes) by lookup key, for personalization use cases in apps and websites. Authenticated wit
  name: DinMo Personalization API
  slug: dinmo-personalization-api
artifact_total: 7
asyncapis:
- description: ''
  name: Dinmo Webhooks
  slug: dinmo-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.dinmo.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.dinmo.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dinmo.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dinmo.io/customer-hub/profiles-api/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dinmo.io/guides/get-started-with-dinmo
- group: operate
  title: ''
  type: Support
  url: https://www.dinmo.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.dinmo.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://news.dinmo.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dinmo.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.dinmo.io/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dinmo.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dinmo.com/legals/privacy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dinmo-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/dinmo-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dinmo-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dinmo-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dinmo-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/dinmo-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dinmo-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dinmo-mcp.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dinmo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dinmo-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dinmo-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/dinmo-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dinmo-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/dinmo-webhooks.yml
- group: learn
  title: ''
  type: Tutorials
  url: https://www.dinmo.com/tutorials/
- group: other
  title: ''
  type: CaseStudies
  url: https://www.dinmo.com/customer-stories/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dinmo-io/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@DinMoTube
created: '2026-07-17'
description: DinMo is a composable Customer Data Platform (CDP) that turns a cloud data warehouse into a marketing activation engine. It connects directly to Snowflake, Google BigQuery, Databricks, Amazon Redshift, PostgreSQL, Microsoft Fabric, and ClickHouse, lets non-technical teams model customer data and build no-code segments, and activates those audiences to more than a hundred destination platforms (ad networks, CRMs, marketing and messaging tools) via Reverse ETL with a zero-data-copy architecture built for GDPR and FADP compliance. DinMo also exposes a Personalization API for retrieving activated model records in real time, plus AI predictions (LTV, churn), identity resolution, a Customer Hub, and event tracking. The company is Paris-based and backed by Seedcamp.
image: https://www.dinmo.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: dinmo-mcp.yml
  slug: dinmo-mcpyml
modified: '2026-08-13'
name: DinMo
nav: Providers
network: true
overview: 'DinMo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Customer Data Platform, CDP, Reverse ETL, and Data Activation.


  The DinMo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  DinMo''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, pricing, and 23 more developer resources.'
plans:
- name: Dinmo Plans Pricing
  plan_count: 4
  slug: dinmo-plans-pricing
random_paper: 88
rate_limits:
- limit_count: 1
  name: Dinmo Rate Limits
  slug: dinmo-rate-limits
score:
  band: strong
  composite: 55.1
  delta: -0.4
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 57.1
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 55.5
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dinmo/refs/heads/main/screenshots/dinmo-2026-07-25T212055.png
security:
- kind: authentication
  name: Dinmo Authentication
  slug: dinmo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dinmo Domain Security
  slug: dinmo-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dinmo
tags:
- Company
- Customer Data Platform
- CDP
- Reverse ETL
- Data Activation
- Data Warehouse
- Audience Segmentation
- Marketing
- Personalization
- MarTech
website: https://www.dinmo.com
---
