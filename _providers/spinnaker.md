---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bound
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Spinnaker Agentic Access
  operation_count: 23
  slug: spinnaker-agentic-access
  summary_line: 23 operations · 7 acting
api_count: 1
apis:
- description: Application management operations for Spinnaker application lifecycle including creation, retrieval, and pipeline access
  name: Spinnaker Applications API
  slug: spinnaker-applications-api
- description: CI build service integration for discovering build masters, jobs, and build artifacts
  name: Spinnaker Build Services API
  slug: spinnaker-build-services-api
- description: Cloud cluster and server group operations for managing deployment targets across cloud providers
  name: Spinnaker Clusters API
  slug: spinnaker-clusters-api
- description: Cloud image discovery and management across cloud providers and regions
  name: Spinnaker Images API
  slug: spinnaker-images-api
- description: Load balancer management operations for cloud load balancing resources across supported cloud providers
  name: Spinnaker Load Balancers API
  slug: spinnaker-load-balancers-api
- description: Pipeline definition and execution management including saving pipeline configurations, triggering runs, and controlling execution state
  name: Spinnaker Pipelines API
  slug: spinnaker-pipelines-api
- description: Spinnaker project management for grouping applications and pipelines into organizational units
  name: Spinnaker Projects API
  slug: spinnaker-projects-api
- description: Cross-entity search for finding applications, clusters, and other Spinnaker-managed resources
  name: Spinnaker Search API
  slug: spinnaker-search-api
- description: Task management for tracking long-running Spinnaker operations and checking their completion status
  name: Spinnaker Tasks API
  slug: spinnaker-tasks-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Spinnaker Gate Applications API
  slug: open-spinnaker-applications-api
- collection_type: open
  name: Spinnaker Gate Applications Build Services API
  slug: open-spinnaker-build-services-api
- collection_type: open
  name: Spinnaker Gate Applications Clusters API
  slug: open-spinnaker-clusters-api
- collection_type: open
  name: Spinnaker Gate API
  slug: open-spinnaker-gate
- collection_type: open
  name: Spinnaker Gate Applications Images API
  slug: open-spinnaker-images-api
- collection_type: open
  name: Spinnaker Gate Applications Load Balancers API
  slug: open-spinnaker-load-balancers-api
- collection_type: open
  name: Spinnaker Gate Applications Pipelines API
  slug: open-spinnaker-pipelines-api
- collection_type: open
  name: Spinnaker Gate Applications Projects API
  slug: open-spinnaker-projects-api
- collection_type: open
  name: Spinnaker Gate Applications Search API
  slug: open-spinnaker-search-api
- collection_type: open
  name: Spinnaker Gate Applications Tasks API
  slug: open-spinnaker-tasks-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/spinnaker/gate/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/spinnaker/gate/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/spinnaker/.github/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/spinnaker/.github/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/spinnaker/gate/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spinnaker-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spinnaker-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spinnaker-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/spinnaker-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spinnaker-cd
- group: company
  title: ''
  type: Website
  url: https://spinnaker.io/
- group: docs
  title: ''
  type: Documentation
  url: https://spinnaker.io/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spinnaker
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/spinnaker/spinnaker
- group: operate
  title: ''
  type: Community
  url: https://spinnaker.io/community/
- group: operate
  title: ''
  type: Slack
  url: https://join.spinnaker.io/
- group: company
  title: ''
  type: Blog
  url: https://spinnaker.io/blog/
- group: operate
  title: ''
  type: RoadMap
  url: https://github.com/spinnaker/governance/tree/master/rfc
- group: operate
  title: ''
  type: ChangeLog
  url: https://spinnaker.io/changelogs/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/spinnaker-gate-openapi.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/spinnaker-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/spinnaker-vocabulary.yml
created: '2026-03-26'
description: Spinnaker is an open source multi-cloud continuous delivery platform for releasing software changes with high velocity and confidence. Originally developed at Netflix and Google, Spinnaker provides a deployment platform supporting AWS, GCP, Azure, Kubernetes, and other cloud providers. The Gate API is the primary REST interface for all Spinnaker operations.
examples:
- key_count: 2
  name: Spinnaker Invoke Pipeline Example
  slug: spinnaker-invoke-pipeline-example
- key_count: 2
  name: Spinnaker List Applications Example
  slug: spinnaker-list-applications-example
finops:
- name: Spinnaker Finops
  service_category: API
  slug: spinnaker-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spinnaker.png
json_schemas:
- name: Spinnaker Pipeline Execution
  property_count: 8
  slug: spinnaker-pipeline
json_structures:
- name: Spinnaker Pipeline Structure
  property_count: 0
  slug: spinnaker-pipeline-structure
jsonld:
- class_count: 8
  name: Spinnaker Context
  property_count: 12
  slug: spinnaker-context
layout: provider
modified: '2026-05-19'
name: Spinnaker
nav: Providers
network: true
overview: 'Spinnaker publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Applications API, Build Services API, Clusters API, and 6 more. Tagged areas include Continuous Delivery, Containers, DevOps, Multi-Cloud, and Pipelines.


  The Spinnaker catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Spinnaker''s developer surface includes authentication, documentation, engineering blog, changelog, and 18 more developer resources.'
plans:
- name: Spinnaker Plans Pricing
  plan_count: 3
  slug: spinnaker-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Spinnaker Rate Limits
  slug: spinnaker-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Spinnaker API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: spinnaker-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Spinnaker API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 5
  slug: spinnaker-rules
scopes:
- name: Spinnaker Scopes
  scope_count: 3
  slug: spinnaker-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 17
    catalog_gap: 53.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 57.1
    developer_ergonomics: 23.8
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 15.8
  open_source:
    applies: true
    score: 65.0
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spinnaker/refs/heads/main/screenshots/spinnaker-2026-06-20T194321.png
security:
- kind: authentication
  name: Spinnaker Authentication
  slug: spinnaker-authentication
  summary_line: mutualTLS/oauth2 · 2 schemes
- kind: domain-security
  name: Spinnaker Domain Security
  slug: spinnaker-domain-security
  summary_line: TLSv1.3 · HSTS
slug: spinnaker
tags:
- Continuous Delivery
- Containers
- DevOps
- Multi-Cloud
- Pipelines
website: https://spinnaker.io/
---
