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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: 'The Middleware Public API provides programmatic access to observability data including metrics, logs, traces, events, alerts, and dashboards, enabling integration of monitoring and observability into '
  name: Middleware API
  slug: middleware-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/middleware-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/middleware-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/middleware-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://middleware.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.middleware.io
- group: docs
  title: ''
  type: API Documentation
  url: https://docs.middleware.io/public-api/api
- group: company
  title: ''
  type: Blog
  url: https://middleware.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://middleware.io/pricing
- group: build
  title: ''
  type: GitHub
  url: https://github.com/middleware-labs
- group: start
  title: ''
  type: Login
  url: https://app.middleware.io
- group: start
  title: ''
  type: Signup
  url: https://app.middleware.io/auth/signup
- group: operate
  title: ''
  type: Support
  url: https://middleware.io/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/middleware-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://middleware.io/llms.txt
created: '2026-03-26'
description: Middleware is a cloud-native observability platform that provides full-stack monitoring including infrastructure, APM, log management, real user monitoring, database monitoring, container monitoring, synthetic monitoring, serverless monitoring, and LLM observability with AI-powered insights and auto-instrumentation across 200+ integrations.
finops:
- name: Middleware Finops
  service_category: API
  slug: middleware-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/middleware.png
jsonld:
- class_count: 3
  name: Middleware Context
  property_count: 1
  slug: middleware-context
layout: provider
modified: '2026-04-28'
name: Middleware
nav: Providers
network: true
overview: 'Middleware publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Operations, APM, API Monitoring, Container Monitoring, and Database Monitoring.


  The Middleware catalog on APIs.io includes 1 JSON-LD context.


  Middleware''s developer surface includes documentation, engineering blog, pricing, GitHub presence, signup flow, support, and 8 more developer resources.'
plans:
- name: Middleware Plans Pricing
  plan_count: 3
  slug: middleware-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Middleware Rate Limits
  slug: middleware-rate-limits
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 8
    catalog_gap: 64.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 40.8
    commercial_clarity: 40.8
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 31.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 25.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/middleware/refs/heads/main/screenshots/middleware-2026-06-20T185551.png
security:
- kind: domain-security
  name: Middleware Domain Security
  slug: middleware-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Middleware Vulnerability Disclosure
  slug: middleware-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Middleware Trust Center
  slug: middleware-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: middleware
tags:
- AI Operations
- APM
- API Monitoring
- Container Monitoring
- Database Monitoring
- Infrastructure Monitoring
- LLM Observability
- Log Management
- Observability
- Real User Monitoring
- Synthetic Monitoring
website: https://middleware.io
---
