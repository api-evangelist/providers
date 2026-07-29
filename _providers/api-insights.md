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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'API Insights analyzes OpenAPI specifications (OAS v3, JSON or YAML) and produces detailed scorecards across AI Readiness, Design, Performance, and Security dimensions. Each category receives a letter '
  name: API Insights Analysis
  slug: api-insights-analysis
artifact_total: 16
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/api-insights-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apiinsights.io/
- group: operate
  title: ''
  type: Support
  url: mailto:support@apiinsights.io
created: '2025-01-08'
description: API Insights is a free online tool powered by Treblle that provides advanced API analysis and monitoring by evaluating OpenAPI specifications across multiple dimensions including AI readiness, design quality, performance, and security. It scores APIs against industry benchmarks and provides actionable recommendations for improvement.
features:
- description: Evaluates schema descriptions, operation IDs, parameter documentation, and response descriptions to ensure APIs are well-structured for AI integration.
  name: AI Readiness Scoring
- description: Checks contact information, operation documentation, code examples, HTTP method variety, URL versioning, endpoint naming consistency, and rate-limiting headers.
  name: Design Analysis
- description: Assesses compression support, response sizes, HTTP/2 usage, load times, caching policies, and CDN implementation targeting 500ms or less.
  name: Performance Analysis
- description: Checks authentication enforcement, IDOR vulnerability risks, security scheme definitions, and HTTP security headers including HSTS, X-Frame-Options, and Content-Security-Policy.
  name: Security Analysis
- description: Scores APIs against industry peers with percentile rankings such as Top 10% in your industry.
  name: Industry Benchmarking
- description: Accepts OpenAPI v3 specifications via file upload or URL for instant analysis.
  name: OpenAPI Upload and URL Input
finops:
- name: Api Insights Finops
  service_category: API
  slug: api-insights-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/api-insights.png
layout: provider
modified: '2026-04-19'
name: API Insights
nav: Providers
network: true
overview: 'API Insights publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Readiness, Analysis, Analytics, API Design, and Dashboards.


  API Insights'' developer surface includes support and 2 more developer resources.'
plans:
- name: Api Insights Plans Pricing
  plan_count: 3
  slug: api-insights-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 5
  name: Api Insights Rate Limits
  slug: api-insights-rate-limits
score:
  band: emerging
  composite: 18.8
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 20.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/api-insights/refs/heads/main/screenshots/api-insights-2026-06-20T172210.png
security:
- kind: domain-security
  name: Api Insights Domain Security
  slug: api-insights-domain-security
  summary_line: TLSv1.3 · HSTS
slug: api-insights
tags:
- AI Readiness
- Analysis
- Analytics
- API Design
- Dashboards
- Insights
- Monitoring
- OpenAPI
- Platform
- Security
- Treblle
use_cases:
- description: Validate API design quality before publishing by running specifications through automated scoring checks.
  name: API Quality Assurance
- description: Identify authentication gaps, IDOR risks, and missing security headers before deployment.
  name: Security Compliance Review
- description: Ensure APIs are well-documented and structured for consumption by AI agents and LLM-based tools.
  name: AI Integration Readiness
- description: Detect missing compression, caching, or CDN configurations that degrade API performance.
  name: Performance Optimization
- description: Establish baseline design quality standards across API portfolios using industry benchmark scores.
  name: API Governance
website: https://apiinsights.io/
---
