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
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: The Cloud Dynamics API (formerly the Intricately API) provides access to cloud adoption, usage, and spend data on companies, products, applications, and domains. Requests authenticate with an X-API-KE
  name: Cloud Dynamics API (Intricately)
  slug: cloud-dynamics-api-intricately
artifact_total: 5
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.intricately.com/
- group: docs
  title: ''
  type: Documentation
  url: https://kb.intricately.com/
- group: operate
  title: ''
  type: Support
  url: https://help.intricately.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.intricately.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://help.intricately.com/hc/en-us/articles/4416133622285-Request-an-API-Key
- group: start
  title: ''
  type: SignUp
  url: https://content.intricately.com/demo
- group: agent
  title: ''
  type: LLMsTxt
  url: https://kb.intricately.com/llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intricately-domain-security.yml
created: '2026-07-17'
description: Intricately is a cloud and technology spend intelligence platform that tracks the adoption, usage, and spend of more than 15,000 cloud products across millions of companies worldwide, giving sales and marketing teams the signals they need to find accounts, spot active sales cycles, and predict churn. Founded in 2014 in San Francisco and backed by Bloomberg Beta, GitHub, Susa Ventures, and Singtel Innov8, Intricately was acquired by HG Insights in March 2022 and its data product is now delivered as the Cloud Dynamics API. The REST API (https://api.intricately.com/api/v2) authenticates with an X-API-KEY header and centers on asynchronous Bulk Jobs that enrich lists of domains with cloud adoption, product signatures, revenue, and digital-relationship data. API access is available on Enterprise plans.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/intricately.png
layout: provider
mcp_servers:
- description: ''
  name: intricately-mcp.yml
  slug: intricately-mcpyml
modified: '2026-07-19'
name: Intricately
nav: Providers
network: true
overview: 'Intricately publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API, Sales Intelligence, Cloud Intelligence, and Technographics.


  Intricately''s developer surface includes documentation, support, pricing, signup flow, and 4 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 0
  name: Intricately Rate Limits
  slug: intricately-rate-limits
score:
  band: emerging
  composite: 20.4
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 20.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Intricately Authentication
  slug: intricately-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Intricately Domain Security
  slug: intricately-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: intricately
tags:
- Company
- API
- Sales Intelligence
- Cloud Intelligence
- Technographics
- Data Enrichment
- Cloud Spend
- Market Intelligence
website: https://developers.intricately.com/
---
