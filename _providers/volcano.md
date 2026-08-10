---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Volcano Agentic Access
  operation_count: 20
  slug: volcano-agentic-access
  summary_line: 20 operations · 12 acting
api_count: 3
apis:
- description: Operations for managing Volcano Job (vcjob) custom resources. A Volcano Job defines a batch workload with one or more task groups, lifecycle policies, and scheduling requirements.
  name: Volcano Jobs API
  slug: volcano-jobs-api
- description: Operations for managing Volcano PodGroup custom resources. PodGroups define gang scheduling units with minimum availability requirements and queue assignment.
  name: Volcano PodGroups API
  slug: volcano-podgroups-api
- description: Operations for managing Volcano Queue cluster-scoped custom resources. Queues define scheduling namespaces with weight-based fair sharing, resource capacity, and state management for batch workloads.
  name: Volcano Queues API
  slug: volcano-queues-api
artifact_total: 19
collections:
- collection_type: open
  name: Volcano Job API
  slug: open-volcano-job
- collection_type: open
  name: Volcano PodGroup API
  slug: open-volcano-podgroup
- collection_type: open
  name: Volcano Queue API
  slug: open-volcano-queue
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/volcano-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/volcano-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/philips-volcano
- group: company
  title: ''
  type: Website
  url: https://volcano.sh/en/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/volcano-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/volcano-job-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/volcano-job-structure.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/volcano-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/volcano-rules.yml
- group: docs
  title: ''
  type: Documentation
  url: https://volcano.sh/en/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://volcano.sh/en/docs/installation/
- group: company
  title: ''
  type: Blog
  url: https://volcano.sh/en/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/volcano-sh
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/volcano-sh/volcano
- group: operate
  title: ''
  type: Community
  url: https://github.com/volcano-sh/community
created: '2026-03-16'
description: 'Volcano is a CNCF incubating batch processing and high-performance computing (HPC) scheduler for Kubernetes. It provides advanced scheduling capabilities including gang scheduling, fair-share scheduling, queue management, and job lifecycle management for batch workloads such as machine learning training, big data processing, and scientific computing. Volcano extends Kubernetes with three CRDs: Job (vcjob), Queue, and PodGroup.'
examples:
- key_count: 2
  name: Volcano Createnamespacedjob Example
  slug: volcano-createNamespacedJob-example
- key_count: 2
  name: Volcano Createnamespacedpodgroup Example
  slug: volcano-createNamespacedPodGroup-example
- key_count: 2
  name: Volcano Listqueues Example
  slug: volcano-listQueues-example
finops:
- name: Volcano Finops
  service_category: Open Source / Kubernetes Scheduler
  slug: volcano-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/volcano.png
json_schemas:
- name: Volcano Job
  property_count: 5
  slug: volcano-job
json_structures:
- name: Volcano Job Structure
  property_count: 0
  slug: volcano-job-structure
jsonld:
- class_count: 0
  name: Volcano Context
  property_count: 7
  slug: volcano-context
layout: provider
modified: '2026-05-19'
name: Volcano
nav: Providers
network: true
overview: 'Volcano publishes 3 APIs on the [APIs.io](https://apis.io/) network: Jobs API, PodGroups API, and Queues API. Tagged areas include Batch Processing, Cloud Native, HPC, Incubating, and Kubernetes.


  The Volcano catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Volcano''s developer surface includes documentation, getting-started guide, engineering blog, and 12 more developer resources.'
plans:
- name: Volcano Plans Pricing
  plan_count: 1
  slug: volcano-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 2
  name: Volcano Rate Limits
  slug: volcano-rate-limits
rules:
- name: Volcano API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: volcano-jsonschema-spectral-rules
- name: Volcano API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 4
  slug: volcano-rules
score:
  band: developing
  composite: 46.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 64.3
    developer_ergonomics: 26.1
    discoverability: 72.2
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 46.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/volcano/refs/heads/main/screenshots/volcano-2026-06-20T201130.png
security:
- kind: domain-security
  name: Volcano Domain Security
  slug: volcano-domain-security
  summary_line: TLSv1.3 · HSTS
slug: volcano
tags:
- Batch Processing
- Cloud Native
- HPC
- Incubating
- Kubernetes
- Scheduling
- Machine Learning
website: https://volcano.sh/en/
---
