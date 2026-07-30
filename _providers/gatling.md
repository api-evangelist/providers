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
api_count: 2
apis:
- description: Gatling is an open source load and performance testing framework for web applications and APIs with a Scala-based DSL and detailed HTML reports.
  name: Gatling
  slug: gatling
- description: The Gatling Enterprise Edition public API enables you to trigger runs or fetch run results and metrics, including run metadata and performance percentile summaries.
  name: Gatling Enterprise Public API
  slug: gatling-enterprise
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/gatling-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gatling-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gatling
- group: company
  title: ''
  type: Website
  url: https://gatling.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gatling.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gatling
- group: other
  title: ''
  type: Products
  url: https://gatling.io/products/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.gatling.io/llms.txt
created: '2026-03-25'
description: Gatling is an open source load and performance testing framework for web applications and APIs with a Scala-based DSL and detailed HTML reports. The Gatling Enterprise Edition exposes a public REST API for triggering runs and fetching run results and metrics.
finops:
- name: Gatling Finops
  service_category: API
  slug: gatling-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gatling.png
layout: provider
modified: '2026-04-28'
name: Gatling
nav: Providers
network: true
overview: 'Gatling publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Load Testing, Performance Testing, and Testing.


  Gatling''s developer surface includes documentation and 7 more developer resources.'
plans:
- name: Gatling Plans Pricing
  plan_count: 3
  slug: gatling-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Gatling Rate Limits
  slug: gatling-rate-limits
score:
  band: emerging
  composite: 21.0
  delta: -1.8
  facets:
    commercial_clarity: 47.4
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 22.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gatling/refs/heads/main/screenshots/gatling-2026-06-20T181654.png
security:
- kind: domain-security
  name: Gatling Domain Security
  slug: gatling-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Gatling Trust Center
  slug: gatling-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: gatling
tags:
- Load Testing
- Performance Testing
- Testing
website: https://gatling.io
---
