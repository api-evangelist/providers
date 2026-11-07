---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Kubeflow Pipelines Agentic Access
  operation_count: 13
  slug: kubeflow-pipelines-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 1
apis:
- description: Python SDK for building, compiling, and submitting ML pipelines. Provides decorators and utilities to define pipeline components and workflows using Python.
  name: Kubeflow Pipelines Python SDK
  slug: python-sdk
- description: Go client library for interacting with the Kubeflow Pipelines API programmatically from Go applications.
  name: Kubeflow Pipelines Go Client
  slug: go-client
- description: API for tracking and managing metadata about ML artifacts, executions, and lineage information throughout the ML pipeline lifecycle, backed by ML Metadata (MLMD).
  name: Kubeflow Pipelines Metadata API
  slug: metadata-api
- baseURL: https://your-kubeflow-host/pipeline
  baseurl_source: declared
  description: Group runs and recurring jobs into experiments
  name: Kubeflow Pipelines Experiments API
  slug: kubeflow-pipelines-experiments-api
- baseURL: https://your-kubeflow-host/pipeline
  baseurl_source: declared
  description: Health and auth checks
  name: Kubeflow Pipelines Health API
  slug: kubeflow-pipelines-health-api
- baseURL: https://your-kubeflow-host/pipeline
  baseurl_source: declared
  description: Manage pipeline definitions
  name: Kubeflow Pipelines API
  slug: kubeflow-pipelines-pipelines-api
- baseURL: https://your-kubeflow-host/pipeline
  baseurl_source: declared
  description: Pipeline runs
  name: Kubeflow Pipelines Runs API
  slug: kubeflow-pipelines-runs-api
- baseURL: https://pypi.org/project/kfp/
  baseurl_source: declared
  description: Manage versions of pipelines
  name: Kubeflow Pipelines Pipeline Versions API
  slug: kubeflow-pipelines-pipeline-versions-api
artifact_total: 21
collections:
- collection_type: open
  name: Kubeflow Pipelines REST Experiments API
  slug: open-kubeflow-pipelines-experiments-api
- collection_type: open
  name: Kubeflow Pipelines REST Experiments Health API
  slug: open-kubeflow-pipelines-health-api
- collection_type: open
  name: Kubeflow REST Experiments Pipelines API
  slug: open-kubeflow-pipelines-pipelines-api
- collection_type: open
  name: Kubeflow Pipelines REST Experiments PipelineVersions API
  slug: open-kubeflow-pipelines-pipelineversions-api
- collection_type: open
  name: Kubeflow Pipelines REST Experiments Runs API
  slug: open-kubeflow-pipelines-runs-api
- collection_type: open
  name: Kubeflow Pipelines REST API
  slug: open-kubeflow-pipelines
common:
- group: commercial
  href: https://artifacts.apis.io/kubeflow-pipelines/plans/kubeflow-pipelines-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kubeflow-pipelines-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/kubeflow-pipelines/rate-limits/kubeflow-pipelines-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kubeflow-pipelines-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/kubeflow-pipelines/finops/kubeflow-pipelines-finops.yml
  title: ''
  type: FinOps
  url: finops/kubeflow-pipelines-finops.yml
- group: other
  href: https://artifacts.apis.io/kubeflow-pipelines/capabilities/kubeflow-pipelines-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/kubeflow-pipelines-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/kubeflow/pipelines/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/kubeflow/pipelines/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/kubeflow/pipelines/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/kubeflow/pipelines/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/kubeflow/pipelines/blob/master/LICENSE
- group: agent
  href: https://artifacts.apis.io/kubeflow-pipelines/agentic-access/kubeflow-pipelines-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kubeflow-pipelines-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/kubeflow-pipelines/security/kubeflow-pipelines-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kubeflow-pipelines-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/kubeflow-pipelines/authentication/kubeflow-pipelines-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kubeflow-pipelines-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kubeflow
- group: company
  title: ''
  type: Website
  url: https://www.kubeflow.org/docs/components/pipelines/
- group: docs
  title: ''
  type: Documentation
  url: https://www.kubeflow.org/docs/components/pipelines/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.kubeflow.org/docs/components/pipelines/getting-started/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/kubeflow
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/kubeflow/pipelines
- group: company
  title: ''
  type: Blog
  url: https://blog.kubeflow.org/
- group: operate
  title: ''
  type: Community
  url: https://www.kubeflow.org/docs/about/community/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/kubeflow/pipelines/releases
created: '2024-01-01'
description: Kubeflow Pipelines is a platform for building and deploying portable, scalable machine learning workflows based on Docker containers. It provides a way to orchestrate complex ML workflows with dependencies, enabling data scientists and ML engineers to deploy production-ready ML systems on Kubernetes.
finops:
- has_sources: false
  method: generated
  name: Kubeflow Pipelines Finops
  primary_unit: request
  service_category: API
  slug: kubeflow-pipelines-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kubeflow-pipelines.png
layout: provider
modified: '2026-09-16'
name: Kubeflow Pipelines
nav: Providers
network: true
overview: 'Kubeflow Pipelines publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Experiments API, Health API, and 6 more. Tagged areas include Data Science, Kubernetes, Machine Learning, MLOps, and Orchestration.


  The Kubeflow Pipelines catalog on APIs.io includes 1 Spectral governance ruleset.


  Kubeflow Pipelines'' developer surface includes authentication, documentation, getting-started guide, engineering blog, changelog, and 16 more developer resources.'
plans:
- name: Kubeflow Pipelines Plans Pricing
  plan_count: 3
  slug: kubeflow-pipelines-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Kubeflow Pipelines Rate Limits
  slug: kubeflow-pipelines-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: Kubeflow Pipelines API Rules
  rule_count: 62
  severity_counts:
    error: 60
    hint: 0
    info: 1
    warn: 1
  slug: kubeflow-pipelines-rules
score:
  band: thin
  composite: 38.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.5
    catalog_earned_first_party: 0.0
    catalog_gap: 72.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 45.6
    developer_ergonomics: 38.1
    discoverability: 57.1
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 100.0
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/kubeflow-pipelines/kubeflow-pipelines-2026-06-20T184205.png
security:
- kind: authentication
  name: Kubeflow Pipelines Authentication
  slug: kubeflow-pipelines-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kubeflow Pipelines Domain Security
  slug: kubeflow-pipelines-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: kubeflow-pipelines
tags:
- Data Science
- Kubernetes
- Machine Learning
- MLOps
- Orchestration
- Pipelines
- Workflows
website: https://www.kubeflow.org/docs/components/pipelines/
---
