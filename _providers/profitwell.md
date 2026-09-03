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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: REST API for managing subscription lifecycle data, retrieving SaaS financial metrics (MRR, churn, ARPU, LTV), and accessing customer and engagement data on the ProfitWell Metrics (Paddle) platform. Au
  name: ProfitWell Metrics API
  slug: metrics-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/profitwell-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/profitwell-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ProfitWell
- group: company
  title: ''
  type: Website
  url: https://www.paddle.com/profitwell-metrics
- group: docs
  title: ''
  type: Documentation
  url: https://www.paddle.com/help/profitwell-metrics
- group: start
  title: ''
  type: Signup
  url: https://www2.profitwell.com/free-subscription-analytics
- group: commercial
  title: ''
  type: Pricing
  url: https://www.paddle.com/profitwell-metrics
- group: start
  title: ''
  type: Login
  url: https://my.profitwell.com/login
- group: other
  title: ''
  type: Paddle Parent Company
  url: https://www.paddle.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.paddle.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/paddlehq/
created: '2026-05-11'
description: ProfitWell (now ProfitWell Metrics by Paddle, following Paddle's 2022 acquisition of ProfitWell) is a free subscription analytics product that delivers accurate, real-time SaaS metrics such as MRR, churn, ARPU, LTV, retention, and cohort analysis by connecting directly to billing systems like Stripe, Braintree, Chargebee, Recurly, and Paddle. The ProfitWell API at https://api.profitwell.com/v2 provides programmatic access to subscription lifecycle events, customer data, financial metrics, and engagement data, authenticated via a bare API key passed in the Authorization header (no Bearer prefix).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/profitwell.png
layout: provider
modified: '2026-05-11'
name: ProfitWell
nav: Providers
network: true
overview: 'ProfitWell publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Subscription Analytics, SaaS Metrics, Revenue Analytics, Churn, and MRR.


  ProfitWell''s developer surface includes documentation, signup flow, pricing, and 8 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 13.9
  coverage:
    artifact_dirs: 3
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 13.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/profitwell/refs/heads/main/screenshots/profitwell-2026-06-20T192141.png
security:
- kind: domain-security
  name: Profitwell Domain Security
  slug: profitwell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Profitwell Vulnerability Disclosure
  slug: profitwell-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: profitwell
tags:
- Subscription Analytics
- SaaS Metrics
- Revenue Analytics
- Churn
- MRR
- Billing
website: https://www.paddle.com/profitwell-metrics
---
