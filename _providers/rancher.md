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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Rancher Agentic Access
  operation_count: 13
  slug: rancher-agentic-access
  summary_line: 13 operations · 4 acting
api_count: 8
apis:
- description: Helm-based applications deployed through Rancher.
  name: Rancher Apps API
  slug: rancher-apps-api
- description: Helm chart catalogs registered with Rancher.
  name: Rancher Catalogs API
  slug: rancher-catalogs-api
- description: Downstream Kubernetes clusters managed by Rancher.
  name: Rancher Clusters API
  slug: rancher-clusters-api
- description: Cluster nodes registered with Rancher.
  name: Rancher Nodes API
  slug: rancher-nodes-api
- description: Rancher projects, which group namespaces within a cluster for tenancy and policy.
  name: Rancher Projects API
  slug: rancher-projects-api
- description: Role templates and role bindings defining access policies.
  name: Rancher Roles API
  slug: rancher-roles-api
- description: API tokens used to authenticate against the Rancher API.
  name: Rancher Tokens API
  slug: rancher-tokens-api
- description: Rancher users.
  name: Rancher Users API
  slug: rancher-users-api
artifact_total: 36
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rancher Management Apps API
  slug: open-rancher-apps-api
- collection_type: open
  name: Rancher Management Apps Catalogs API
  slug: open-rancher-catalogs-api
- collection_type: open
  name: Rancher Management Apps Clusters API
  slug: open-rancher-clusters-api
- collection_type: open
  name: Rancher Management API
  slug: open-rancher-management-api
- collection_type: open
  name: Rancher Management Apps Nodes API
  slug: open-rancher-nodes-api
- collection_type: open
  name: Rancher Management Apps Projects API
  slug: open-rancher-projects-api
- collection_type: open
  name: Rancher Management Apps Roles API
  slug: open-rancher-roles-api
- collection_type: open
  name: Rancher Management Apps Tokens API
  slug: open-rancher-tokens-api
- collection_type: open
  name: Rancher Management Apps Users API
  slug: open-rancher-users-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/rancher/rancher/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rancher-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rancher-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rancher-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rancher
- group: company
  title: ''
  type: Website
  url: https://www.rancher.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ranchermanager.docs.rancher.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rancher
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/rancher/rancher
- group: company
  title: ''
  type: Blog
  url: https://www.suse.com/c/rancher/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rancher.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.rancher.com/quick-start
- group: operate
  title: ''
  type: Support
  url: https://www.rancher.com/support-maintenance-terms
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/rancher-vocabulary.yml
created: '2026-03-26'
description: Rancher is an open source container management platform built by SUSE that provides a complete software stack for teams adopting containers. It simplifies Kubernetes cluster deployment and management across any infrastructure, providing unified security, policy, and user management across all clusters. The Rancher Management API exposes these capabilities as Kubernetes-style REST resources for automation and platform engineering.
examples:
- key_count: 2
  name: Rancher Create Cluster Example
  slug: rancher-create-cluster-example
- key_count: 2
  name: Rancher List Clusters Example
  slug: rancher-list-clusters-example
- key_count: 2
  name: Rancher List Projects Example
  slug: rancher-list-projects-example
finops:
- name: Rancher Finops
  service_category: API
  slug: rancher-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rancher.png
json_schemas:
- name: Rancher Cluster
  property_count: 8
  slug: rancher-cluster
- name: Rancher Node
  property_count: 7
  slug: rancher-node
- name: Rancher Project
  property_count: 6
  slug: rancher-project
json_structures:
- name: Rancher Cluster Structure
  property_count: 0
  slug: rancher-cluster-structure
- name: Rancher Node Structure
  property_count: 0
  slug: rancher-node-structure
- name: Rancher Project Structure
  property_count: 0
  slug: rancher-project-structure
jsonld:
- class_count: 17
  name: Rancher Context
  property_count: 1
  slug: rancher-context
layout: provider
modified: '2026-05-19'
name: Rancher
nav: Providers
network: true
overview: 'Rancher publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Catalogs API, Clusters API, and 5 more. Tagged areas include Cluster Management, Containers, Kubernetes, Multi-Cluster, and Open Source.


  The Rancher catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Rancher''s developer surface includes authentication, documentation, engineering blog, pricing, signup flow, support, and 8 more developer resources.'
plans:
- name: Rancher Plans Pricing
  plan_count: 3
  slug: rancher-plans-pricing
random_paper: 143
rate_limits:
- limit_count: 5
  name: Rancher Rate Limits
  slug: rancher-rate-limits
rules:
- name: Rancher API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rancher-jsonschema-spectral-rules
- name: Rancher API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 2
    info: 0
    warn: 4
  slug: rancher-rules
score:
  band: developing
  composite: 46.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.9
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 13.2
  previous_composite: 46.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rancher/refs/heads/main/screenshots/rancher-2026-06-20T192552.png
security:
- kind: authentication
  name: Rancher Authentication
  slug: rancher-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rancher Domain Security
  slug: rancher-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rancher
tags:
- Cluster Management
- Containers
- Kubernetes
- Multi-Cluster
- Open Source
- SUSE
- Platform Engineering
website: https://www.rancher.com/
---
