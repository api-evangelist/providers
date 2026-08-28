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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Google Cloud Trace Agentic Access
  operation_count: 5
  slug: google-cloud-trace-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- description: The Projects API from Google Cloud Trace — 4 operation(s) for projects.
  name: Google Cloud Trace Projects API
  slug: google-cloud-trace-projects-api
artifact_total: 12
collections:
- collection_type: postman
  name: Google Cloud Trace Projects API
  slug: postman-google-cloud-trace-projects-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Cloud Trace Projects API
  slug: open-google-cloud-trace-projects-api
- collection_type: open
  name: Google Cloud Trace API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-trace/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-trace-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-trace-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-trace-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/trace
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/trace/docs/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/trace/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/docs/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/trace/pricing
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
  url: https://cloud.google.com/trace/docs/support
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/json-ld.yml
- group: company
  title: ''
  type: Blog
  url: https://docs.cloud.google.com/feeds/trace-release-notes.xml
created: '2026-03-13'
description: Google Cloud Trace is a distributed tracing system that collects latency data from applications and displays it in near real-time. It helps developers understand how requests propagate through their application, identify performance bottlenecks, and analyze latency across microservices and distributed architectures running on Google Cloud.
finops:
- name: Google Cloud Trace Finops
  service_category: API
  slug: google-cloud-trace-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-trace.png
layout: provider
modified: '2026-05-19'
name: Google Cloud Trace
nav: Providers
network: true
overview: 'Google Cloud Trace publishes 1 API on the [APIs.io](https://apis.io/) network: Projects API. Tagged areas include Distributed Tracing, Google Cloud, Latency, Observability, and Performance.


  The Google Cloud Trace catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Cloud Trace''s developer surface includes developer portal, getting-started guide, documentation, authentication, pricing, support, engineering blog, and 9 more developer resources.'
plans:
- name: Google Cloud Trace Plans Pricing
  plan_count: 3
  slug: google-cloud-trace-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Google Cloud Trace Rate Limits
  slug: google-cloud-trace-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Cloud Trace API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-trace-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.7
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 9.8
    contract_quality: 55.8
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-trace/refs/heads/main/screenshots/google-cloud-trace-2026-06-20T182143.png
security:
- kind: domain-security
  name: Google Cloud Trace Domain Security
  slug: google-cloud-trace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Trace Vulnerability Disclosure
  slug: google-cloud-trace-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-trace
tags:
- Distributed Tracing
- Google Cloud
- Latency
- Observability
- Performance
- Spans
- Tracing
website: https://cloud.google.com/trace
---
