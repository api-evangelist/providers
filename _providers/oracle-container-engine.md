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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Oracle Container Engine Agentic Access
  operation_count: 15
  slug: oracle-container-engine-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 6
apis:
- description: Cluster add-on management
  name: Oracle Container Engine for Kubernetes Add-ons API
  slug: oracle-container-engine-add-ons-api
- description: Kubernetes cluster lifecycle management
  name: Oracle Container Engine for Kubernetes Clusters API
  slug: oracle-container-engine-clusters-api
- description: Kubeconfig and cluster credentials
  name: Oracle Container Engine for Kubernetes Credentials API
  slug: oracle-container-engine-credentials-api
- description: Worker node pool management
  name: Oracle Container Engine for Kubernetes Node Pools API
  slug: oracle-container-engine-node-pools-api
- description: Serverless virtual node pool management
  name: Oracle Container Engine for Kubernetes Virtual Node Pools API
  slug: oracle-container-engine-virtual-node-pools-api
- description: Asynchronous operation tracking
  name: Oracle Container Engine for Kubernetes Work Requests API
  slug: oracle-container-engine-work-requests-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Oracle Container Engine for Kubernetes (OKE) Add-ons API
  slug: open-oracle-container-engine-add-ons-api
- collection_type: open
  name: Oracle Container Engine for Kubernetes (OKE) Add-ons Clusters API
  slug: open-oracle-container-engine-clusters-api
- collection_type: open
  name: Oracle Container Engine for Kubernetes (OKE) Add-ons Credentials API
  slug: open-oracle-container-engine-credentials-api
- collection_type: open
  name: Oracle Container Engine for Kubernetes (OKE) Add-ons Node Pools API
  slug: open-oracle-container-engine-node-pools-api
- collection_type: open
  name: Oracle Container Engine for Kubernetes (OKE) Add-ons Virtual Node Pools API
  slug: open-oracle-container-engine-virtual-node-pools-api
- collection_type: open
  name: Oracle Container Engine for Kubernetes (OKE) Add-ons Work Requests API
  slug: open-oracle-container-engine-work-requests-api
- collection_type: open
  name: Oracle Container Engine for Kubernetes (OKE) API
  slug: open-oracle-container-engine
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/oracle/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/oracle-container-engine-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-container-engine-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oracle-container-engine-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.oracle.com/cloud/cloud-native/container-engine-kubernetes/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en-us/iaas/Content/ContEng/home.htm
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengoverview.htm
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oracle.com/cloud/cloud-native/container-engine-kubernetes/pricing/
- group: company
  title: ''
  type: Blog
  url: https://blogs.oracle.com/cloud-infrastructure/
- group: operate
  title: ''
  type: StatusPage
  url: https://ocistatus.oraclecloud.com/
- group: start
  title: ''
  type: Signup
  url: https://www.oracle.com/cloud/free/
created: '2026-03-26'
description: Oracle Container Engine for Kubernetes (OKE) is a managed Kubernetes service that simplifies the deployment, management, and scaling of containerized applications on Oracle Cloud Infrastructure with built-in security, high availability, and integration with OCI services.
finops:
- name: Oracle Container Engine Finops
  service_category: API
  slug: oracle-container-engine-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle-container-engine.png
layout: provider
modified: '2026-08-21'
name: Oracle Container Engine for Kubernetes
nav: Providers
network: true
overview: 'Oracle Container Engine for Kubernetes publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Add-ons API, Clusters API, Credentials API, and 3 more. Tagged areas include Cloud, Containers, Kubernetes, Oracle, and Orchestration.


  Oracle Container Engine for Kubernetes'' developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, signup flow, and 6 more developer resources.'
plans:
- name: Oracle Container Engine Plans Pricing
  plan_count: 3
  slug: oracle-container-engine-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Oracle Container Engine Rate Limits
  slug: oracle-container-engine-rate-limits
score:
  band: developing
  composite: 40.8
  delta: 1.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 54.1
    developer_ergonomics: 42.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 39.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-container-engine/refs/heads/main/screenshots/oracle-container-engine-2026-06-20T191124.png
security:
- kind: authentication
  name: Oracle Container Engine Authentication
  slug: oracle-container-engine-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Oracle Container Engine Domain Security
  slug: oracle-container-engine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: oracle-container-engine
tags:
- Cloud
- Containers
- Kubernetes
- Oracle
- Orchestration
website: https://www.oracle.com/cloud/cloud-native/container-engine-kubernetes/
---
