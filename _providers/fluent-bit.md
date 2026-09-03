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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Fluent Bit Agentic Access
  operation_count: 12
  slug: fluent-bit-agentic-access
  summary_line: 12 operations · 2 acting
api_count: 1
apis:
- baseURL: http://127.0.0.1:2020
  baseurl_source: declared
  description: The Build API from Fluent Bit — 1 operation(s) for build.
  name: Fluent Bit Build API
  slug: fluent-bit-build-api
- baseURL: http://127.0.0.1:2020
  baseurl_source: declared
  description: The Health API from Fluent Bit — 2 operation(s) for health.
  name: Fluent Bit Health API
  slug: fluent-bit-health-api
- baseURL: http://127.0.0.1:2020
  baseurl_source: declared
  description: The Metrics API from Fluent Bit — 4 operation(s) for metrics.
  name: Fluent Bit Metrics API
  slug: fluent-bit-metrics-api
- baseURL: http://127.0.0.1:2020
  baseurl_source: declared
  description: The Reload API from Fluent Bit — 1 operation(s) for reload.
  name: Fluent Bit Reload API
  slug: fluent-bit-reload-api
- baseURL: http://127.0.0.1:2020
  baseurl_source: declared
  description: The Storage API from Fluent Bit — 1 operation(s) for storage.
  name: Fluent Bit Storage API
  slug: fluent-bit-storage-api
- baseURL: http://127.0.0.1:2020
  baseurl_source: declared
  description: The Uptime API from Fluent Bit — 1 operation(s) for uptime.
  name: Fluent Bit Uptime API
  slug: fluent-bit-uptime-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fluent Bit Monitoring HTTP Build API
  slug: open-fluent-bit-build-api
- collection_type: open
  name: Fluent Bit Monitoring HTTP Build Health API
  slug: open-fluent-bit-health-api
- collection_type: open
  name: Fluent Bit Monitoring HTTP Build Metrics API
  slug: open-fluent-bit-metrics-api
- collection_type: open
  name: Fluent Bit Monitoring HTTP API
  slug: open-fluent-bit-monitoring
- collection_type: open
  name: Fluent Bit Monitoring HTTP Build Reload API
  slug: open-fluent-bit-reload-api
- collection_type: open
  name: Fluent Bit Monitoring HTTP Build Storage API
  slug: open-fluent-bit-storage-api
- collection_type: open
  name: Fluent Bit Monitoring HTTP Build Uptime API
  slug: open-fluent-bit-uptime-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/fluent/fluent-bit/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/fluent/fluent-bit/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/fluent/fluent-bit/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/fluent/fluent-bit/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/fluent/fluent-bit/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/fluent/fluent-bit/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fluent-bit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fluent-bit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fluentbit.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fluentbit.io
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/fluent/fluent-bit
- group: operate
  title: ''
  type: Slack
  url: https://launchpass.com/fluent-all
- group: operate
  title: ''
  type: Community
  url: https://fluentbit.io/community/
- group: company
  title: ''
  type: Blog
  url: https://fluentbit.io/blog/index.xml
created: '2026-03-25'
description: Fluent Bit is an open source lightweight log processor and forwarder for collecting, parsing, and routing logs and metrics at scale. It exposes an embedded HTTP monitoring server with v1 and v2 endpoints for build info, uptime, internal metrics (JSON, Prometheus, cmetrics), storage stats, health checks, and hot reload.
finops:
- name: Fluent Bit Finops
  service_category: API
  slug: fluent-bit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fluent-bit.png
layout: provider
modified: '2026-05-19'
name: Fluent Bit
nav: Providers
network: true
overview: 'Fluent Bit publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Build API, Health API, Metrics API, and 3 more. Tagged areas include Logging, Observability, Metrics, and Open-Source.


  Fluent Bit''s developer surface includes documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Fluent Bit Plans Pricing
  plan_count: 3
  slug: fluent-bit-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Fluent Bit Rate Limits
  slug: fluent-bit-rate-limits
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 39.7
    developer_ergonomics: 14.3
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 34.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fluent-bit/refs/heads/main/screenshots/fluent-bit-2026-06-20T181333.png
security:
- kind: domain-security
  name: Fluent Bit Domain Security
  slug: fluent-bit-domain-security
  summary_line: TLSv1.3 · HSTS
slug: fluent-bit
tags:
- Logging
- Observability
- Metrics
- Open-Source
website: https://fluentbit.io
---
