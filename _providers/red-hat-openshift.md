---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Red Hat Openshift Agentic Access
  operation_count: 30
  slug: red-hat-openshift-agentic-access
  summary_line: 30 operations · 15 acting
api_count: 16
apis:
- description: OpenShift Pipelines is a cloud-native CI/CD solution based on Tekton that runs pipelines as Kubernetes-native CRDs. The API provides resources for defining Tasks (individual steps), Pipelines (task gr
  name: Red Hat OpenShift Pipelines (Tekton) API
  slug: openshift-pipelines-api
- description: OpenShift GitOps is built on Argo CD and provides a GitOps continuous delivery solution for OpenShift clusters. The API exposes Application, AppProject, ApplicationSet, and Repository CRD resources fo
  name: Red Hat OpenShift GitOps (ArgoCD) API
  slug: openshift-gitops-api
- description: Red Hat OpenShift Service Mesh, based on Istio, Kiali, Jaeger, and Prometheus, provides traffic management, security, and observability for microservices. The Service Mesh API exposes Istio CRDs inclu
  name: Red Hat OpenShift Service Mesh API
  slug: openshift-service-mesh-api
- description: OpenShift Serverless, based on Knative, enables deploying and managing event-driven serverless workloads on OpenShift. The Serverless API exposes Knative Serving resources (Service, Route, Configurati
  name: Red Hat OpenShift Serverless (Knative) API
  slug: openshift-serverless-api
- description: Red Hat OpenShift Service on AWS (ROSA) is a fully managed OpenShift service co-managed by Red Hat and AWS. The ROSA API, exposed through the OCM service, provides operations for creating and managing
  name: Red Hat OpenShift Service on AWS (ROSA) API
  slug: rosa-api
- description: Manage cluster add-on installations
  name: Red Hat OpenShift Add-ons API
  slug: red-hat-openshift-add-ons-api
- description: Build and BuildConfig resources for source-to-image and Dockerfile builds
  name: Red Hat OpenShift Builds API
  slug: red-hat-openshift-builds-api
- description: Manage OpenShift clusters across cloud providers
  name: Red Hat OpenShift Clusters API
  slug: red-hat-openshift-clusters-api
- description: DeploymentConfig resources for OpenShift-native deployment management
  name: Red Hat OpenShift Deployment Configs API
  slug: red-hat-openshift-deployment-configs-api
- description: Configure authentication providers for clusters
  name: Red Hat OpenShift Identity Providers API
  slug: red-hat-openshift-identity-providers-api
- description: ImageStream and ImageStreamTag resources for container image management
  name: Red Hat OpenShift Image Streams API
  slug: red-hat-openshift-image-streams-api
- description: Manage compute node pools for clusters
  name: Red Hat OpenShift Machine Pools API
  slug: red-hat-openshift-machine-pools-api
- description: OpenShift Project resources for multi-tenant workspace management
  name: Red Hat OpenShift Projects API
  slug: red-hat-openshift-projects-api
- description: Route resources for exposing services via HTTP/HTTPS hostnames
  name: Red Hat OpenShift Routes API
  slug: red-hat-openshift-routes-api
- description: SCC resources for controlling pod security permissions
  name: Red Hat OpenShift Security Context Constraints API
  slug: red-hat-openshift-security-context-constraints-api
- description: Query available OpenShift versions
  name: Red Hat OpenShift Versions API
  slug: red-hat-openshift-versions-api
artifact_total: 70
collections:
- collection_type: postman
  name: Red Hat OpenShift Container Platform Add-ons API
  slug: postman-red-hat-openshift-add-ons-api
- collection_type: postman
  name: Red Hat OpenShift Container Platform Add-ons Builds API
  slug: postman-red-hat-openshift-builds-api
- collection_type: postman
  name: Red Hat OpenShift Container Platform Add-ons Clusters API
  slug: postman-red-hat-openshift-clusters-api
- collection_type: postman
  name: Red Hat OpenShift Container Platform Add-ons Deployment Configs API
  slug: postman-red-hat-openshift-deployment-configs-api
- collection_type: postman
  name: Red Hat OpenShift Container Platform Add-ons Identity Providers API
  slug: postman-red-hat-openshift-identity-providers-api
- collection_type: postman
  name: Red Hat OpenShift Container Platform Add-ons Image Streams API
  slug: postman-red-hat-openshift-image-streams-api
- collection_type: postman
  name: Red Hat OpenShift Container Platform Add-ons Machine Pools API
  slug: postman-red-hat-openshift-machine-pools-api
- collection_type: postman
  name: Red Hat OpenShift Container Platform Add-ons Projects API
  slug: postman-red-hat-openshift-projects-api
- collection_type: postman
  name: Red Hat OpenShift Container Platform Add-ons Routes API
  slug: postman-red-hat-openshift-routes-api
- collection_type: postman
  name: Red Hat OpenShift Container Platform Add-ons Security Context Constraints API
  slug: postman-red-hat-openshift-security-context-constraints-api
- collection_type: postman
  name: Red Hat OpenShift Container Platform Add-ons Versions API
  slug: postman-red-hat-openshift-versions-api
- collection_type: open
  name: Red Hat OpenShift Container Platform API
  slug: open-red-hat-openshift-api
- collection_type: open
  name: Red Hat OpenShift Cluster Manager API
  slug: open-red-hat-openshift-cluster-manager
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/red-hat-openshift/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/red-hat-openshift-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/red-hat-openshift-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/red-hat-openshift-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/red-hat-openshift-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.redhat.com/en/technologies/cloud-computing/openshift
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openshift.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.redhat.com/en/technologies/cloud-computing/openshift/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.redhat.com/en/blog/channel/red-hat-openshift
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openshift
- group: start
  title: ''
  type: Signup
  url: https://www.redhat.com/en/technologies/cloud-computing/openshift/try-it
- group: operate
  title: ''
  type: StatusPage
  url: https://status.redhat.com/
- group: operate
  title: ''
  type: Support
  url: https://access.redhat.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.redhat.com/en/about/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.redhat.com/en/about/agreements
- group: learn
  title: ''
  type: Training
  url: https://www.redhat.com/en/services/training-and-certification
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/red-hat-openshift-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/red-hat-openshift-cluster-manager-openapi.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/red-hat-openshift-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/red-hat-openshift-project-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/red-hat-openshift-project-structure.json
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/red-hat-openshift-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/red-hat-openshift-vocabulary.yml
created: '2026-03-26'
description: Red Hat OpenShift is an enterprise Kubernetes platform that provides a consistent hybrid cloud foundation for building, deploying, and scaling containerized applications. OpenShift extends Kubernetes with developer productivity tools, built-in CI/CD pipelines, integrated monitoring and logging, automated cluster management, role-based access control, and security policies. It supports deployments on bare metal, virtual machines, public clouds, and managed OpenShift services (ROSA, ARO, RHOIC). The OpenShift REST API exposes hundreds of Kubernetes and OpenShift-specific resource types organized into API groups for workload management, networking, storage, security, builds, pipelines, and cluster configuration.
examples:
- key_count: 2
  name: Red Hat Openshift Create Project Example
  slug: red-hat-openshift-create-project-example
- key_count: 2
  name: Red Hat Openshift Create Route Example
  slug: red-hat-openshift-create-route-example
finops:
- name: Red Hat Openshift Finops
  service_category: Container Platform
  slug: red-hat-openshift-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/red-hat-openshift.png
json_schemas:
- name: AddOnInstallation
  property_count: 4
  slug: red-hat-openshift-addoninstallation
- name: AddOnInstallationList
  property_count: 1
  slug: red-hat-openshift-addoninstallationlist
- name: Build
  property_count: 4
  slug: red-hat-openshift-build
- name: BuildConfig
  property_count: 4
  slug: red-hat-openshift-buildconfig
- name: BuildConfigList
  property_count: 1
  slug: red-hat-openshift-buildconfiglist
- name: BuildList
  property_count: 1
  slug: red-hat-openshift-buildlist
- name: Cluster
  property_count: 15
  slug: red-hat-openshift-cluster
- name: ClusterList
  property_count: 5
  slug: red-hat-openshift-clusterlist
- name: ClusterPatch
  property_count: 2
  slug: red-hat-openshift-clusterpatch
- name: DeploymentConfig
  property_count: 5
  slug: red-hat-openshift-deploymentconfig
- name: DeploymentConfigList
  property_count: 1
  slug: red-hat-openshift-deploymentconfiglist
- name: Error
  property_count: 5
  slug: red-hat-openshift-error
- name: IdentityProvider
  property_count: 4
  slug: red-hat-openshift-identityprovider
- name: IdentityProviderList
  property_count: 1
  slug: red-hat-openshift-identityproviderlist
- name: ImageStream
  property_count: 5
  slug: red-hat-openshift-imagestream
- name: ImageStreamList
  property_count: 1
  slug: red-hat-openshift-imagestreamlist
- name: MachinePool
  property_count: 7
  slug: red-hat-openshift-machinepool
- name: MachinePoolList
  property_count: 1
  slug: red-hat-openshift-machinepoollist
- name: ObjectMeta
  property_count: 7
  slug: red-hat-openshift-objectmeta
- name: Red Hat OpenShift Project
  property_count: 5
  slug: red-hat-openshift-project
- name: ProjectList
  property_count: 4
  slug: red-hat-openshift-projectlist
- name: Route
  property_count: 5
  slug: red-hat-openshift-route
- name: RouteList
  property_count: 1
  slug: red-hat-openshift-routelist
- name: SecurityContextConstraints
  property_count: 7
  slug: red-hat-openshift-securitycontextconstraints
- name: SecurityContextConstraintsList
  property_count: 1
  slug: red-hat-openshift-securitycontextconstraintslist
- name: Status
  property_count: 6
  slug: red-hat-openshift-status
- name: VersionList
  property_count: 1
  slug: red-hat-openshift-versionlist
json_structures:
- name: Red Hat Openshift Project Structure
  property_count: 0
  slug: red-hat-openshift-project-structure
- name: Red Hat Openshift Structure
  property_count: 0
  slug: red-hat-openshift-structure
jsonld:
- class_count: 3
  name: Red Hat Openshift Context
  property_count: 20
  slug: red-hat-openshift-context
layout: provider
modified: '2026-05-19'
name: Red Hat OpenShift
nav: Providers
network: true
overview: 'Red Hat OpenShift publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Add-ons API, Builds API, Clusters API, and 8 more. Tagged areas include Containers, Enterprise, Hybrid Cloud, Kubernetes, and PaaS.


  The Red Hat OpenShift catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Red Hat OpenShift''s developer surface includes authentication, documentation, pricing, engineering blog, signup flow, support, training material, and 16 more developer resources.'
plans:
- name: Red Hat Openshift Plans Pricing
  plan_count: 8
  slug: red-hat-openshift-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 2
  name: Red Hat Openshift Rate Limits
  slug: red-hat-openshift-rate-limits
rules:
- name: Red Hat OpenShift API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: red-hat-openshift-jsonschema-spectral-rules
- name: Red Hat OpenShift API Rules
  rule_count: 13
  severity_counts:
    error: 6
    hint: 0
    info: 3
    warn: 4
  slug: red-hat-openshift-rules
score:
  band: strong
  composite: 56.8
  delta: -4.6
  facets:
    commercial_clarity: 71.1
    contract_quality: 61.6
    developer_ergonomics: 30.4
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 42.1
  previous_composite: 61.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/red-hat-openshift/refs/heads/main/screenshots/red-hat-openshift-2026-06-20T192719.png
security:
- kind: authentication
  name: Red Hat Openshift Authentication
  slug: red-hat-openshift-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Red Hat Openshift Domain Security
  slug: red-hat-openshift-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Red Hat Openshift Vulnerability Disclosure
  slug: red-hat-openshift-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: red-hat-openshift
tags:
- Containers
- Enterprise
- Hybrid Cloud
- Kubernetes
- PaaS
- Red Hat
website: https://www.redhat.com/en/technologies/cloud-computing/openshift
---
