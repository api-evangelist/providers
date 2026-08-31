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
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: Cloud Monitoring API (v3) collects metrics, events, and metadata from Google Cloud, AWS, and application instrumentation, and exposes them for dashboards, uptime checks, alerting policies, and time-se
  name: Cloud Monitoring API
  slug: cloud-monitoring-api
- description: Cloud Logging API (v2) writes, stores, searches, and manages log entries and log-based metrics across Google Cloud and multi-cloud resources.
  name: Cloud Logging API
  slug: cloud-logging-api
- description: Cloud Trace API (v2) ingests and retrieves distributed-trace spans to analyze request latency across microservices.
  name: Cloud Trace API
  slug: cloud-trace-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/stackdriver-google-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://g.co/vrp
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stackdriver-google-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/stackdriver-google-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/stackdriver-google-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/stackdriver-google-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/stackdriver-google-packages.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stackdriver-google-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://cloud.google.com/terms/deprecation
- group: company
  title: ''
  type: Website
  url: https://cloud.google.com/products/operations
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cloud.google.com/stackdriver/docs
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/stackdriver/docs
- group: docs
  title: ''
  type: APIReference
  url: https://cloud.google.com/monitoring/api/ref_v3/rest
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/monitoring/docs/monitoring-overview
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/stackdriver/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/blog/products/management-tools
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleapis
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/support
- group: start
  title: ''
  type: SignUp
  url: https://console.cloud.google.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
created: '2026-07-17'
description: Stackdriver is the former name of the Google Cloud Operations suite, Google's integrated observability platform for applications and infrastructure running on Google Cloud, hybrid, and multi-cloud environments. Rebranded to Google Cloud Operations in 2020, the suite bundles Cloud Monitoring (metrics, dashboards, uptime checks, and alerting), Cloud Logging (centralized log storage, search, and analysis), Cloud Trace (distributed tracing), Error Reporting (automatic error aggregation), and Cloud Profiler (continuous CPU and memory profiling). Each capability is exposed as a REST API (Cloud Monitoring API v3, Cloud Logging API v2, Cloud Trace API v2, Error Reporting API, Cloud Profiler API) with first-party client libraries across Python, Node.js, Go, Java, Ruby, PHP, and .NET, and is governed by Google Cloud's authentication, IAM, deprecation, and status-page practices.
image: https://cloud.google.com/_static/cloud/images/social-icon-google-cloud-1200-630.png
layout: provider
modified: '2026-07-21'
name: Stackdriver (Google)
nav: Providers
network: true
overview: 'Stackdriver (Google) publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Infrastructure, Observability, Monitoring, and Logging.


  Stackdriver (Google)''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, signup flow, and 15 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 29.0
  coverage:
    artifact_dirs: 5
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 52.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 29.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Stackdriver Google Domain Security
  slug: stackdriver-google-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Stackdriver Google Vulnerability Disclosure
  slug: stackdriver-google-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: stackdriver-google
tags:
- Company
- Ai Infrastructure
- Observability
- Monitoring
- Logging
- Tracing
- Cloud Operations
- Google Cloud
website: https://cloud.google.com/products/operations
---
