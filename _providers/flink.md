---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 2
  name: Flink Agentic Access
  operation_count: 29
  slug: flink-agentic-access
  summary_line: 29 operations · 7 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: http://localhost:8081
  baseurl_source: declared
  description: Checkpoint configuration, status, and details.
  name: Apache Flink Checkpoints API
  slug: flink-checkpoints-api
- baseURL: http://localhost:8081
  baseurl_source: declared
  description: Cluster lifecycle and configuration.
  name: Apache Flink Cluster API
  slug: flink-cluster-api
- baseURL: http://localhost:8081
  baseurl_source: declared
  description: Cluster dataset listing and deletion.
  name: Apache Flink Datasets API
  slug: flink-datasets-api
- baseURL: http://localhost:8081
  baseurl_source: declared
  description: Job lifecycle and inspection.
  name: Apache Flink Jobs API
  slug: flink-jobs-api
- baseURL: http://localhost:8081
  baseurl_source: declared
  description: JAR upload, listing, run, and delete.
  name: Apache Flink JA Rs API
  slug: flink-jars-api
- baseURL: http://localhost:8081
  baseurl_source: declared
  description: JobManager configuration, environment, logs, metrics, and threads.
  name: Apache Flink Job Manager API
  slug: flink-job-manager-api
- baseURL: http://localhost:8081
  baseurl_source: declared
  description: TaskManager listing and inspection.
  name: Apache Flink Task Managers API
  slug: flink-task-managers-api
artifact_total: 21
collections:
- collection_type: open
  name: Apache Flink REST Checkpoints API
  slug: open-flink-checkpoints-api
- collection_type: open
  name: Apache Flink REST Checkpoints Cluster API
  slug: open-flink-cluster-api
- collection_type: open
  name: Apache Flink REST Checkpoints Datasets API
  slug: open-flink-datasets-api
- collection_type: open
  name: Apache Flink REST Checkpoints JARs API
  slug: open-flink-jars-api
- collection_type: open
  name: Apache Flink REST Checkpoints JobManager API
  slug: open-flink-jobmanager-api
- collection_type: open
  name: Apache Flink REST Checkpoints Jobs API
  slug: open-flink-jobs-api
- collection_type: open
  name: Apache Flink REST Checkpoints TaskManagers API
  slug: open-flink-taskmanagers-api
common:
- group: commercial
  href: https://artifacts.apis.io/flink/plans/flink-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/flink-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/flink/rate-limits/flink-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/flink-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/flink/finops/flink-finops.yml
  title: ''
  type: FinOps
  url: finops/flink-finops.yml
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apache/flink/blob/master/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/flink/blob/master/LICENSE
- group: agent
  href: https://artifacts.apis.io/flink/agentic-access/flink-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/flink-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/flink/security/flink-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/flink-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/flink/security/flink-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/flink-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flink.apache.org/
- group: docs
  title: ''
  type: Documentation
  url: https://nightlies.apache.org/flink/flink-docs-stable/
- group: docs
  title: ''
  type: RESTAPIDocumentation
  url: https://nightlies.apache.org/flink/flink-docs-stable/docs/ops/rest_api/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/flink
- group: company
  title: ''
  type: Blog
  url: https://flink.apache.org/posts/
- group: operate
  title: ''
  type: Community
  url: https://flink.apache.org/community/
created: '2025-01-01'
description: Apache Flink is an open-source framework and distributed processing engine for stateful computations over unbounded and bounded data streams. It is designed to run in all common cluster environments and to perform computations at in-memory speed and at any scale. Flink exposes a REST API on the JobManager Dispatcher that allows external systems to query cluster status, submit and manage jobs, trigger savepoints and checkpoints, upload and run JARs, and inspect metrics, accumulators, and exception histories. The same REST endpoints power the Flink Web UI.
finops:
- has_sources: false
  method: generated
  name: Flink Finops
  primary_unit: request
  service_category: API
  slug: flink-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/flink.png
layout: provider
modified: '2026-05-19'
name: Apache Flink
nav: Providers
network: true
overview: 'Apache Flink publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Checkpoints API, Cluster API, Datasets API, and 4 more. Tagged areas include Big Data, Distributed Computing, Real-Time Analytics, Stream Processing, and Workflows.


  The Apache Flink catalog on APIs.io includes 1 Spectral governance ruleset.


  Apache Flink''s developer surface includes documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Flink Plans Pricing
  plan_count: 3
  slug: flink-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Flink Rate Limits
  slug: flink-rate-limits
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Apache Flink API Rules
  rule_count: 44
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 1
  slug: flink-rules
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 36.1
    developer_ergonomics: 14.3
    discoverability: 57.1
    operational_transparency: 23.7
  open_source:
    applies: true
    score: 40.0
  previous_composite: 24.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/flink/flink-2026-06-20T181313.png
security:
- kind: domain-security
  name: Flink Domain Security
  slug: flink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Flink Vulnerability Disclosure
  slug: flink-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: flink
tags:
- Big Data
- Distributed Computing
- Real-Time Analytics
- Stream Processing
- Workflows
website: https://flink.apache.org/
---
