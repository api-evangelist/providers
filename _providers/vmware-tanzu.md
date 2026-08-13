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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Vmware Tanzu Agentic Access
  operation_count: 12
  slug: vmware-tanzu-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 5
apis:
- description: Exchange CSP API tokens for Bearer access tokens
  name: VMware Tanzu Authentication API
  slug: vmware-tanzu-authentication-api
- description: Manage Kubernetes clusters onboarded to Tanzu Service Mesh
  name: VMware Tanzu Clusters API
  slug: vmware-tanzu-clusters-api
- description: Manage global namespaces connecting workloads across clusters
  name: VMware Tanzu Global Namespaces API
  slug: vmware-tanzu-global-namespaces-api
- description: Manage resource groups for policy enforcement and monitoring
  name: VMware Tanzu Resource Groups API
  slug: vmware-tanzu-resource-groups-api
- description: Create and manage TanzuKubernetesCluster resources
  name: VMware Tanzu Tanzu Kubernetes Clusters API
  slug: vmware-tanzu-tanzu-kubernetes-clusters-api
artifact_total: 20
collections:
- collection_type: open
  name: VMware Tanzu Service Mesh API
  slug: open-vmware-tanzu-service-mesh
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vmware-tanzu-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vmware-tanzu-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vmware-tanzu-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vmware-tanzu
- group: company
  title: ''
  type: Website
  url: https://tanzu.vmware.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vmware.com/en/VMware-Tanzu/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vmware-tanzu
- group: company
  title: ''
  type: Blog
  url: https://tanzu.vmware.com/content/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://tanzu.vmware.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://tanzu.vmware.com/try
- group: docs
  title: ''
  type: Broadcom TechDocs
  url: https://techdocs.broadcom.com/us/en/vmware-tanzu.html
- group: build
  title: ''
  type: CLI
  url: https://github.com/vmware-tanzu/tanzu-cli
- group: other
  title: ''
  type: Velero
  url: https://github.com/vmware-tanzu/velero
- group: other
  title: ''
  type: Sonobuoy
  url: https://github.com/vmware-tanzu/sonobuoy
- group: other
  title: ''
  type: Cartographer
  url: https://github.com/vmware-tanzu/cartographer
crds:
- name: tanzukubernetescluster crd
  url: https://raw.githubusercontent.com/api-evangelist/vmware-tanzu/refs/heads/main/crd/tanzukubernetescluster-crd.yaml
created: '2026-03-26'
description: VMware Tanzu (now part of Broadcom) is a portfolio of products for modernizing applications and infrastructure with a common approach to building, running, and managing Kubernetes across multi-cloud environments. Key APIs include the Tanzu Service Mesh REST API for cluster and global namespace management, Kubernetes CRD-based APIs for VM Operator, Projects Operator, and NSX Operator, and the Tanzu CLI plugin runtime.
examples:
- key_count: 5
  name: Vmware Tanzu Kubernetes Grid Create Cluster Example
  slug: vmware-tanzu-kubernetes-grid-create-cluster-example
- key_count: 5
  name: Vmware Tanzu Service Mesh List Clusters Example
  slug: vmware-tanzu-service-mesh-list-clusters-example
finops:
- name: Vmware Tanzu Finops
  service_category: API
  slug: vmware-tanzu-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vmware-tanzu.png
json_schemas:
- name: Tanzu Service Mesh Cluster
  property_count: 8
  slug: vmware-tanzu-cluster
- name: Tanzu Service Mesh Global Namespace
  property_count: 9
  slug: vmware-tanzu-global-namespace
json_structures:
- name: Vmware Tanzu Cluster Structure
  property_count: 0
  slug: vmware-tanzu-cluster-structure
jsonld:
- class_count: 8
  name: Vmware Tanzu Context
  property_count: 25
  slug: vmware-tanzu-context
layout: provider
modified: '2026-05-19'
name: VMware Tanzu
nav: Providers
network: true
overview: 'VMware Tanzu publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Clusters API, Global Namespaces API, and 2 more. Tagged areas include Cloud Native, Containers, Enterprise, Kubernetes, and Multi-Cloud.


  The VMware Tanzu catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  VMware Tanzu''s developer surface includes authentication, documentation, engineering blog, pricing, signup flow, CLI, and 9 more developer resources.'
plans:
- name: Vmware Tanzu Plans Pricing
  plan_count: 3
  slug: vmware-tanzu-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 5
  name: Vmware Tanzu Rate Limits
  slug: vmware-tanzu-rate-limits
rules:
- name: VMware Tanzu API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: vmware-tanzu-jsonschema-spectral-rules
- name: VMware Tanzu API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 6
  slug: vmware-tanzu-rules
score:
  band: developing
  composite: 46.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 69.7
    developer_ergonomics: 28.3
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 46.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 80.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vmware-tanzu/refs/heads/main/screenshots/vmware-tanzu-2026-06-20T201119.png
security:
- kind: authentication
  name: Vmware Tanzu Authentication
  slug: vmware-tanzu-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Vmware Tanzu Domain Security
  slug: vmware-tanzu-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: vmware-tanzu
tags:
- Cloud Native
- Containers
- Enterprise
- Kubernetes
- Multi-Cloud
- Service Mesh
- VMware
website: https://tanzu.vmware.com/
---
