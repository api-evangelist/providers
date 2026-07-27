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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Google Cloud Monitoring Agentic Access
  operation_count: 14
  slug: google-cloud-monitoring-agentic-access
  summary_line: 14 operations · 7 acting
api_count: 1
apis:
- description: The Projects API from Google Cloud Monitoring — 7 operation(s) for projects.
  name: Google Cloud Monitoring Projects API
  slug: google-cloud-monitoring-projects-api
artifact_total: 9
collections:
- collection_type: open
  name: Google Cloud Monitoring API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-monitoring-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-monitoring-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-monitoring-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/monitoring
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/monitoring/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/monitoring/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/monitoring/docs/access-control
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/monitoring/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/monitoring/docs/support
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/json-ld.yml
created: '2026-03-13'
description: Google Cloud Monitoring provides comprehensive monitoring and observability for cloud infrastructure and applications. It collects metrics, events, and metadata from Google Cloud services, hosted uptime probes, and application instrumentation, enabling dashboards, alerting, uptime monitoring, and service level objective tracking.
finops:
- name: Google Cloud Monitoring Finops
  service_category: API
  slug: google-cloud-monitoring-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-monitoring.png
layout: provider
modified: '2026-05-19'
name: Google Cloud Monitoring
nav: Providers
network: true
overview: 'Google Cloud Monitoring publishes 1 API on the [APIs.io](https://apis.io/) network: Projects API. Tagged areas include Alerting, Dashboards, Google Cloud, Metrics, and Monitoring.


  The Google Cloud Monitoring catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Cloud Monitoring''s developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, and 8 more developer resources.'
plans:
- name: Google Cloud Monitoring Plans Pricing
  plan_count: 3
  slug: google-cloud-monitoring-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 5
  name: Google Cloud Monitoring Rate Limits
  slug: google-cloud-monitoring-rate-limits
rules:
- name: Google Cloud Monitoring API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-cloud-monitoring-jsonschema-spectral-rules
score:
  band: strong
  composite: 61.8
  delta: 4.6
  facets:
    commercial_clarity: 71.1
    contract_quality: 55.8
    developer_ergonomics: 43.5
    discoverability: 92.5
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 57.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-monitoring/refs/heads/main/screenshots/google-cloud-monitoring-2026-06-20T182121.png
security:
- kind: domain-security
  name: Google Cloud Monitoring Domain Security
  slug: google-cloud-monitoring-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Monitoring Vulnerability Disclosure
  slug: google-cloud-monitoring-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-monitoring
tags:
- Alerting
- Dashboards
- Google Cloud
- Metrics
- Monitoring
- Observability
- SLO
- Uptime
website: https://cloud.google.com/monitoring
---
