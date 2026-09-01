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
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 1
  human_in_the_loop: 1
  name: Scalable Infrastructure Agentic Access
  operation_count: 2
  slug: scalable-infrastructure-agentic-access
  summary_line: 2 operations · 1 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The Terraform Registry API provides access to infrastructure-as-code (IaC) modules and providers. HashiCorp Terraform is the leading IaC tool for provisioning and managing cloud infrastructure in a de
  name: Terraform Registry API
  slug: terraform-registry-api
- description: Pulumi is a modern infrastructure as code platform that uses general-purpose programming languages (TypeScript, Python, Go, C#, Java, YAML). The Pulumi Cloud API manages stacks, deployments, environme
  name: Pulumi Cloud API
  slug: pulumi-cloud-api
- description: The EC2 API from Scalable Infrastructure — 1 operation(s) for ec2.
  name: Scalable Infrastructure EC2 API
  slug: scalable-infrastructure-ec2-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon EC2 API
  slug: open-scalable-infrastructure-ec2-api
- collection_type: open
  name: Amazon EC2 API
  slug: open-scalable-infrastructure
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/scalable-infrastructure-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scalable-infrastructure-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scalable-infrastructure-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hashicorp
- group: other
  title: ''
  type: CNCF Landscape
  url: https://landscape.cncf.io/card-mode?category=provisioning
- group: company
  title: ''
  type: Blog
  url: https://www.cncf.io/blog/
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/scalable-infrastructure/main/json-schema/scalable-infrastructure-compute-instance-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/scalable-infrastructure/main/json-schema/scalable-infrastructure-kubernetes-cluster-schema.json
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/scalable-infrastructure/main/json-ld/scalable-infrastructure-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/scalable-infrastructure/main/vocabulary/scalable-infrastructure-vocabulary.yml
created: '2024-01-15'
description: A subject-matter collection covering APIs, tools, and platforms for building and managing scalable cloud infrastructure. This topic encompasses compute, storage, networking, container orchestration, infrastructure as code (IaC), monitoring, and the major cloud providers (AWS, Azure, GCP, DigitalOcean) that power modern scalable systems.
examples:
- key_count: 15
  name: Scalable Infrastructure Compute Instance Example
  slug: scalable-infrastructure-compute-instance-example
- key_count: 13
  name: Scalable Infrastructure Kubernetes Cluster Example
  slug: scalable-infrastructure-kubernetes-cluster-example
finops:
- name: Scalable Infrastructure Finops
  service_category: API
  slug: scalable-infrastructure-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scalable-infrastructure.png
json_schemas:
- name: Compute Instance
  property_count: 17
  slug: scalable-infrastructure-compute-instance
- name: Kubernetes Cluster
  property_count: 13
  slug: scalable-infrastructure-kubernetes-cluster
json_structures:
- name: Scalable Infrastructure Compute Instance Structure
  property_count: 0
  slug: scalable-infrastructure-compute-instance-structure
- name: Scalable Infrastructure Kubernetes Cluster Structure
  property_count: 0
  slug: scalable-infrastructure-kubernetes-cluster-structure
jsonld:
- class_count: 21
  name: Scalable Infrastructure Context
  property_count: 6
  slug: scalable-infrastructure-context
layout: provider
modified: '2026-05-02'
name: Scalable Infrastructure
nav: Providers
network: true
overview: 'Scalable Infrastructure publishes 1 API on the [APIs.io](https://apis.io/) network: EC2 API. Tagged areas include Cloud Infrastructure, Compute, DevOps, Infrastructure as Code, and Kubernetes.


  The Scalable Infrastructure catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Scalable Infrastructure''s developer surface includes authentication, engineering blog, and 8 more developer resources.'
plans:
- name: Scalable Infrastructure Plans Pricing
  plan_count: 3
  slug: scalable-infrastructure-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Scalable Infrastructure Rate Limits
  slug: scalable-infrastructure-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Scalable Infrastructure API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: scalable-infrastructure-jsonschema-spectral-rules
score:
  band: developing
  composite: 41.2
  coverage:
    artifact_dirs: 16
    catalog_gap: 62.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 25.0
    contract_quality: 58.5
    developer_ergonomics: 59.5
    discoverability: 50.0
    governance: 25.0
    operational_transparency: 10.5
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scalable-infrastructure/refs/heads/main/screenshots/scalable-infrastructure-2026-06-20T193459.png
security:
- kind: authentication
  name: Scalable Infrastructure Authentication
  slug: scalable-infrastructure-authentication
  summary_line: apiKey · 1 scheme
slug: scalable-infrastructure
tags:
- Cloud Infrastructure
- Compute
- DevOps
- Infrastructure as Code
- Kubernetes
- Networking
- Scalability
- Storage
---
