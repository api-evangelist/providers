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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Hashicorp Nomad Agentic Access
  operation_count: 38
  slug: hashicorp-nomad-agentic-access
  summary_line: 38 operations · 13 acting
api_count: 8
apis:
- description: Manage access control tokens and policies.
  name: HashiCorp Nomad ACL API
  slug: hashicorp-nomad-acl-api
- description: Inspect task-to-node allocations.
  name: HashiCorp Nomad Allocations API
  slug: hashicorp-nomad-allocations-api
- description: Track rolling updates and deployment history.
  name: HashiCorp Nomad Deployments API
  slug: hashicorp-nomad-deployments-api
- description: Inspect scheduling processes.
  name: HashiCorp Nomad Evaluations API
  slug: hashicorp-nomad-evaluations-api
- description: Manage Nomad jobs and their lifecycle.
  name: HashiCorp Nomad Jobs API
  slug: hashicorp-nomad-jobs-api
- description: Manage namespace segmentation for jobs and resources.
  name: HashiCorp Nomad Namespaces API
  slug: hashicorp-nomad-namespaces-api
- description: Manage and query client nodes in the cluster.
  name: HashiCorp Nomad Nodes API
  slug: hashicorp-nomad-nodes-api
- description: System-level cluster operations.
  name: HashiCorp Nomad System API
  slug: hashicorp-nomad-system-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: HashiCorp Nomad HTTP ACL API
  slug: open-hashicorp-nomad-acl-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Allocations API
  slug: open-hashicorp-nomad-allocations-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Deployments API
  slug: open-hashicorp-nomad-deployments-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Evaluations API
  slug: open-hashicorp-nomad-evaluations-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Jobs API
  slug: open-hashicorp-nomad-jobs-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Namespaces API
  slug: open-hashicorp-nomad-namespaces-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL Nodes API
  slug: open-hashicorp-nomad-nodes-api
- collection_type: open
  name: HashiCorp Nomad HTTP ACL System API
  slug: open-hashicorp-nomad-system-api
- collection_type: open
  name: HashiCorp Nomad HTTP API
  slug: open-hashicorp-nomad
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/hashicorp/nomad/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/hashicorp/nomad/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/hashicorp/nomad/blob/main/.github/CODE_OF_CONDUCT.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hashicorp-nomad-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hashicorp-nomad-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hashicorp-nomad-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hashicorp
- group: company
  title: ''
  type: Website
  url: https://www.nomadproject.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hashicorp.com/nomad/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hashicorp
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/hashicorp/nomad
- group: company
  title: ''
  type: Blog
  url: https://www.hashicorp.com/blog/products/nomad
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hashicorp.com/products/nomad/pricing
- group: start
  title: ''
  type: Signup
  url: https://portal.cloud.hashicorp.com/sign-up
- group: learn
  title: ''
  type: Tutorials
  url: https://developer.hashicorp.com/nomad/tutorials
created: '2026-03-26'
description: HashiCorp Nomad is a flexible workload orchestrator that enables organizations to deploy and manage containers, non-containerized applications, and batch jobs across on-premises and cloud environments. It provides a single unified workflow for scheduling diverse workloads with high availability and multi-region federation.
finops:
- name: Hashicorp Nomad Finops
  service_category: API
  slug: hashicorp-nomad-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hashicorp-nomad.png
layout: provider
modified: '2026-05-19'
name: HashiCorp Nomad
nav: Providers
network: true
overview: 'HashiCorp Nomad publishes 8 APIs on the [APIs.io](https://apis.io/) network, including ACL API, Allocations API, Deployments API, and 5 more. Tagged areas include Containers, HashiCorp, Multi-Cloud, Orchestration, and Scheduling.


  HashiCorp Nomad''s developer surface includes authentication, documentation, engineering blog, pricing, signup flow, and 10 more developer resources.'
plans:
- name: Hashicorp Nomad Plans Pricing
  plan_count: 3
  slug: hashicorp-nomad-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Hashicorp Nomad Rate Limits
  slug: hashicorp-nomad-rate-limits
score:
  band: thin
  composite: 32.9
  delta: -2.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 46.5
    developer_ergonomics: 22.6
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 34.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hashicorp-nomad/refs/heads/main/screenshots/hashicorp-nomad-2026-06-20T182531.png
security:
- kind: authentication
  name: Hashicorp Nomad Authentication
  slug: hashicorp-nomad-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Hashicorp Nomad Domain Security
  slug: hashicorp-nomad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hashicorp-nomad
tags:
- Containers
- HashiCorp
- Multi-Cloud
- Orchestration
- Scheduling
- Workloads
website: https://www.nomadproject.io/
---
