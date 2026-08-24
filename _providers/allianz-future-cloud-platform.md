---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.9
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Allianz Future Cloud Platform Agentic Access
  operation_count: 8
  slug: allianz-future-cloud-platform-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 5
apis:
- description: Deployment lifecycle management operations
  name: Allianz Future Cloud Platform Deployments API
  slug: allianz-future-cloud-platform-deployments-api
- description: Infrastructure provisioning and management operations
  name: Allianz Future Cloud Platform Infrastructure API
  slug: allianz-future-cloud-platform-infrastructure-api
- description: Kubernetes namespace management operations
  name: Allianz Future Cloud Platform Namespaces API
  slug: allianz-future-cloud-platform-namespaces-api
- description: Monitoring, metrics, and alerting configuration operations
  name: Allianz Future Cloud Platform Observability API
  slug: allianz-future-cloud-platform-observability-api
- description: Service registration and management operations
  name: Allianz Future Cloud Platform Services API
  slug: allianz-future-cloud-platform-services-api
artifact_total: 72
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Allianz Future Cloud Platform Services Deployments API
  slug: open-allianz-future-cloud-platform-deployments-api
- collection_type: open
  name: Allianz Future Cloud Platform Services Deployments Infrastructure API
  slug: open-allianz-future-cloud-platform-infrastructure-api
- collection_type: open
  name: Allianz Future Cloud Platform Services Deployments Namespaces API
  slug: open-allianz-future-cloud-platform-namespaces-api
- collection_type: open
  name: Allianz Future Cloud Platform Services Deployments Observability API
  slug: open-allianz-future-cloud-platform-observability-api
- collection_type: open
  name: Allianz Future Cloud Platform Deployments Services API
  slug: open-allianz-future-cloud-platform-services-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/allianz-future-cloud-platform-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/allianz-future-cloud-platform-services-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/allianz-future-cloud-platform-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/allianz-future-cloud-platform-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/allianz-future-cloud-platform-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/allianz-future-cloud-platform-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/allianz-future-cloud-platform-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.allianz.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/allianz
- group: docs
  title: ''
  type: Documentation
  url: https://architecture.cncf.io/architectures/allianz/
- group: design
  title: ''
  type: SpectralRules
  url: rules/allianz-future-cloud-platform-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/allianz-future-cloud-platform-vocabulary.yaml
- group: company
  title: ''
  type: Blog
  url: https://www.allianz.com/en/press.html
- group: build
  title: ''
  type: Packages
  url: packages/allianz-future-cloud-platform-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/allianz-future-cloud-platform-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/allianz-future-cloud-platform-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/allianz-future-cloud-platform-lifecycle.yml
created: '2024-01-15'
description: The Allianz Future Cloud Platform is an internal developer platform powering cloud-native insurance microservices at Allianz. Built on Kubernetes and AWS, it provides platform engineering capabilities including service deployment, infrastructure management, observability, and GitOps automation across Allianz's global insurance operations.
examples:
- key_count: 3
  name: Platform Services Deploy Service Request Example
  slug: platform-services-deploy-service-request-example
- key_count: 9
  name: Platform Services Deployment Example
  slug: platform-services-deployment-example
- key_count: 2
  name: Platform Services Deployment List Example
  slug: platform-services-deployment-list-example
- key_count: 6
  name: Platform Services Infrastructure Resource Example
  slug: platform-services-infrastructure-resource-example
- key_count: 7
  name: Platform Services Metrics Response Example
  slug: platform-services-metrics-response-example
- key_count: 5
  name: Platform Services Namespace Example
  slug: platform-services-namespace-example
- key_count: 2
  name: Platform Services Namespace List Example
  slug: platform-services-namespace-list-example
- key_count: 4
  name: Platform Services Provision Resource Request Example
  slug: platform-services-provision-resource-request-example
- key_count: 5
  name: Platform Services Register Service Request Example
  slug: platform-services-register-service-request-example
- key_count: 4
  name: Platform Services Resource Requirements Example
  slug: platform-services-resource-requirements-example
- key_count: 10
  name: Platform Services Service Example
  slug: platform-services-service-example
- key_count: 2
  name: Platform Services Service List Example
  slug: platform-services-service-list-example
features:
- description: Internal developer platform built on Kubernetes (EKS) providing standardized deployment, scaling, and orchestration for insurance microservices.
  name: Kubernetes Platform Engineering
- description: ArgoCD and Tekton-based CI/CD pipelines enabling GitOps workflows for continuous delivery of insurance applications.
  name: GitOps Deployment
- description: Terraform and Crossplane-based infrastructure management enabling repeatable, auditable cloud resource provisioning.
  name: Infrastructure as Code
- description: Prometheus, Grafana, and OpenTelemetry based observability platform providing metrics, tracing, and alerting for platform services.
  name: Observability Stack
- description: Namespace-level multi-tenancy supporting multiple insurance product teams on shared Kubernetes infrastructure.
  name: Multi-tenant Architecture
- description: AWS MSK (Managed Kafka) for high-throughput event streaming between insurance microservices and downstream consumers.
  name: Event Streaming
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/allianz-future-cloud-platform.png
integrations:
- description: Primary cloud provider with EKS, MSK, ElastiCache Redis, and storage services powering the platform.
  name: Amazon Web Services
- description: GitOps continuous delivery for declarative application deployment and state synchronization.
  name: ArgoCD
- description: Infrastructure as code for cloud resource provisioning and management integrated with Atlantis for PR automation.
  name: Terraform
- description: Multi-cloud resource management extending Kubernetes for cloud-agnostic infrastructure provisioning.
  name: Crossplane
- description: Distributed tracing and metrics collection across microservices for observability and performance analysis.
  name: OpenTelemetry
- description: AWS MSK for event-driven communication between insurance microservices and downstream systems.
  name: Apache Kafka
json_schemas:
- name: DeployServiceRequest
  property_count: 3
  slug: platform-services-deploy-service-request
- name: DeploymentList
  property_count: 2
  slug: platform-services-deployment-list
- name: Deployment
  property_count: 9
  slug: platform-services-deployment
- name: InfrastructureResource
  property_count: 6
  slug: platform-services-infrastructure-resource
- name: MetricsResponse
  property_count: 7
  slug: platform-services-metrics-response
- name: NamespaceList
  property_count: 2
  slug: platform-services-namespace-list
- name: Namespace
  property_count: 5
  slug: platform-services-namespace
- name: ProvisionResourceRequest
  property_count: 4
  slug: platform-services-provision-resource-request
- name: RegisterServiceRequest
  property_count: 5
  slug: platform-services-register-service-request
- name: ResourceRequirements
  property_count: 4
  slug: platform-services-resource-requirements
- name: ServiceList
  property_count: 2
  slug: platform-services-service-list
- name: Service
  property_count: 10
  slug: platform-services-service
json_structures:
- name: Platform Services Deploy Service Request Structure
  property_count: 3
  slug: platform-services-deploy-service-request-structure
- name: Platform Services Deployment List Structure
  property_count: 2
  slug: platform-services-deployment-list-structure
- name: Platform Services Deployment Structure
  property_count: 9
  slug: platform-services-deployment-structure
- name: Platform Services Infrastructure Resource Structure
  property_count: 6
  slug: platform-services-infrastructure-resource-structure
- name: Platform Services Metrics Response Structure
  property_count: 7
  slug: platform-services-metrics-response-structure
- name: Platform Services Namespace List Structure
  property_count: 2
  slug: platform-services-namespace-list-structure
- name: Platform Services Namespace Structure
  property_count: 5
  slug: platform-services-namespace-structure
- name: Platform Services Provision Resource Request Structure
  property_count: 4
  slug: platform-services-provision-resource-request-structure
- name: Platform Services Register Service Request Structure
  property_count: 5
  slug: platform-services-register-service-request-structure
- name: Platform Services Resource Requirements Structure
  property_count: 4
  slug: platform-services-resource-requirements-structure
- name: Platform Services Service List Structure
  property_count: 2
  slug: platform-services-service-list-structure
- name: Platform Services Service Structure
  property_count: 10
  slug: platform-services-service-structure
jsonld:
- class_count: 12
  name: Allianz Future Cloud Platform Context
  property_count: 35
  slug: allianz-future-cloud-platform-context
layout: provider
mcp_servers:
- description: ''
  name: Allianz Future Cloud Platform MCP Server
  slug: allianz-future-cloud-platform-mcp-server
modified: '2026-06-20'
name: Allianz Future Cloud Platform
nav: Providers
network: true
overview: 'Allianz Future Cloud Platform publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Deployments API, Infrastructure API, Namespaces API, and 2 more. Tagged areas include Cloud Platform, Enterprise, Financial-Services, Insurance, and Platform Engineering.


  The Allianz Future Cloud Platform catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Allianz Future Cloud Platform''s developer surface includes authentication, documentation, engineering blog, and 14 more developer resources.'
random_paper: 13
rules:
- effective_rule_count: 5
  extends: []
  name: Allianz Future Cloud Platform API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: allianz-future-cloud-platform-jsonschema-spectral-rules
- effective_rule_count: 73
  extends:
  - spectral:oas
  name: Allianz Future Cloud Platform API Rules
  rule_count: 32
  severity_counts:
    error: 15
    hint: 0
    info: 3
    warn: 14
  slug: allianz-future-cloud-platform-spectral-rules
scopes:
- name: Allianz Future Cloud Platform Scopes
  scope_count: 6
  slug: allianz-future-cloud-platform-scopes
  summary_line: 6 scopes · clientCredentials
score:
  band: thin
  composite: 31.5
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 45.5
    contract_quality: 29.8
    developer_ergonomics: 23.8
    discoverability: 81.5
    governance: 45.5
    operational_transparency: 5.3
  previous_composite: 31.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 60.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/allianz-future-cloud-platform/refs/heads/main/screenshots/allianz-future-cloud-platform-2026-07-25T195701.png
security:
- kind: authentication
  name: Allianz Future Cloud Platform Authentication
  slug: allianz-future-cloud-platform-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Allianz Future Cloud Platform Domain Security
  slug: allianz-future-cloud-platform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Allianz Future Cloud Platform Vulnerability Disclosure
  slug: allianz-future-cloud-platform-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: allianz-future-cloud-platform
tags:
- Cloud Platform
- Enterprise
- Financial-Services
- Insurance
- Platform Engineering
- Kubernetes
use_cases:
- description: Deploy and manage Kotlin and Java insurance microservices on the platform with standardized CI/CD pipelines and GitOps workflows.
  name: Insurance Microservice Deployment
- description: Onboard new insurance product teams onto the shared Kubernetes platform with pre-configured namespaces and RBAC policies.
  name: Platform Onboarding
- description: Configure monitoring dashboards and alerting for insurance services using the platform's built-in Prometheus and Grafana stack.
  name: Observability and Monitoring
- description: Provision cloud infrastructure resources using Terraform and Crossplane through the platform's infrastructure API.
  name: Infrastructure Provisioning
website: https://www.allianz.com/
---
