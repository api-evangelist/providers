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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: REST API for text analysis including sentiment analysis, keyword extraction, topic classification, and custom ML model training. Supports classifiers and extractors with Token-based authentication.
  name: MonkeyLearn API
  slug: monkeylearn-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monkeylearn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://monkeylearn.com/
- group: docs
  title: ''
  type: Documentation
  url: https://monkeylearn.com/api/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/monkeylearn
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/monkeylearn
- group: company
  title: ''
  type: Blog
  url: https://monkeylearn.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://monkeylearn.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.monkeylearn.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/monkeylearn
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/monkeylearn/refs/heads/main/plans/plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/monkeylearn/refs/heads/main/rate-limits/rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/monkeylearn/refs/heads/main/finops/finops.yml
created: '2026-06-13'
description: Machine learning text analysis platform with REST APIs for sentiment analysis, keyword extraction, topic classification, and custom ML model training on text data. Now part of Medallia's experience management platform.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/monkeylearn.png
layout: provider
modified: '2026-06-13'
name: MonkeyLearn
nav: Providers
network: true
overview: 'MonkeyLearn publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Text Analysis, Machine Learning, Sentiment Analysis, Natural Language Processing, and Text Classification.


  MonkeyLearn''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 146
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 26.1
  delta: -3.7
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 28.2
    developer_ergonomics: 2.4
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 29.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/monkeylearn/refs/heads/main/screenshots/monkeylearn-2026-06-20T185730.png
security:
- kind: domain-security
  name: Monkeylearn Domain Security
  slug: monkeylearn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: monkeylearn
tags:
- Text Analysis
- Machine Learning
- Sentiment Analysis
- Natural Language Processing
- Text Classification
- Keyword Extraction
- Artificial Intelligence
website: https://monkeylearn.com/
---
