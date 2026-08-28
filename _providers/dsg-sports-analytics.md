---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: The DSG Sports Data API exposes live scores, statistics, historical data, player and team information, fixtures, results, and odds across 80-plus sports through a per-sport documentation tree at dsg-a
  name: DSG Sports Data API
  slug: sports-data-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dsg-sports-analytics-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/data-sports-group
- group: company
  title: ''
  type: Website
  url: https://datasportsgroup.com/
- group: other
  title: ''
  type: Products
  url: https://datasportsgroup.com/products-api/
- group: other
  title: ''
  type: Widgets
  url: https://datasportsgroup.com/sports-data-widgets-showcase/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datasportsgroup.com/privacy-policy/
- group: docs
  title: ''
  type: APIReference
  url: https://dsg-api.com/
- group: company
  title: ''
  type: Blog
  url: https://datasportsgroup.com/news-press/
created: '2025-03-01'
description: DSG Sports Analytics, operated by Data Sports Group, is a sports data provider offering live scores, statistics, historical data, fixtures, player and team information, and odds across more than 80 sports including soccer, basketball, American football, cricket, tennis, ice hockey, e-sports, and Olympic disciplines. The DSG Sports Data API delivers this content in JSON and XML over HTTPS using credential-based authentication.
finops:
- name: Dsg Sports Analytics Finops
  service_category: API
  slug: dsg-sports-analytics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dsg-sports-analytics.png
layout: provider
modified: '2026-04-28'
name: DSG Sports Analytics
nav: Providers
network: true
overview: 'DSG Sports Analytics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Analysis, Insights, Sports, Sports Data, and Live Scores.


  DSG Sports Analytics'' developer surface includes API reference, engineering blog, and 6 more developer resources.'
plans:
- name: Dsg Sports Analytics Plans Pricing
  plan_count: 3
  slug: dsg-sports-analytics-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Dsg Sports Analytics Rate Limits
  slug: dsg-sports-analytics-rate-limits
score:
  band: emerging
  composite: 16.8
  delta: 3.2
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 13.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dsg-sports-analytics/refs/heads/main/screenshots/dsg-sports-analytics-2026-06-20T180255.png
security:
- kind: domain-security
  name: Dsg Sports Analytics Domain Security
  slug: dsg-sports-analytics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dsg-sports-analytics
tags:
- Analysis
- Insights
- Sports
- Sports Data
- Live Scores
- Statistics
website: https://datasportsgroup.com/
---
