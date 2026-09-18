---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-09-17'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Red Hat Openshift Agentic Access
  operation_count: 30
  slug: red-hat-openshift-agentic-access
  summary_line: 30 operations · 15 acting
api_count: 2
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
- baseURL: https://api.cluster.example.com:6443
  baseurl_source: declared
  description: Manage cluster add-on installations
  name: Red Hat OpenShift Add-ons API
  slug: red-hat-openshift-add-ons-api
- baseURL: https://api.cluster.example.com:6443
  baseurl_source: declared
  description: Build and BuildConfig resources for source-to-image and Dockerfile builds
  name: Red Hat OpenShift Builds API
  slug: red-hat-openshift-builds-api
- baseURL: https://api.cluster.example.com:6443
  baseurl_source: declared
  description: Manage OpenShift clusters across cloud providers
  name: Red Hat OpenShift Clusters API
  slug: red-hat-openshift-clusters-api
- baseURL: https://api.cluster.example.com:6443
  baseurl_source: declared
  description: DeploymentConfig resources for OpenShift-native deployment management
  name: Red Hat OpenShift Deployment Configs API
  slug: red-hat-openshift-deployment-configs-api
- baseURL: https://api.cluster.example.com:6443
  baseurl_source: declared
  description: Configure authentication providers for clusters
  name: Red Hat OpenShift Identity Providers API
  slug: red-hat-openshift-identity-providers-api
- baseURL: https://api.cluster.example.com:6443
  baseurl_source: declared
  description: ImageStream and ImageStreamTag resources for container image management
  name: Red Hat OpenShift Image Streams API
  slug: red-hat-openshift-image-streams-api
- baseURL: https://api.cluster.example.com:6443
  baseurl_source: declared
  description: Manage compute node pools for clusters
  name: Red Hat OpenShift Machine Pools API
  slug: red-hat-openshift-machine-pools-api
- baseURL: https://api.cluster.example.com:6443
  baseurl_source: declared
  description: OpenShift Project resources for multi-tenant workspace management
  name: Red Hat OpenShift Projects API
  slug: red-hat-openshift-projects-api
- baseURL: https://api.cluster.example.com:6443
  baseurl_source: declared
  description: Route resources for exposing services via HTTP/HTTPS hostnames
  name: Red Hat OpenShift Routes API
  slug: red-hat-openshift-routes-api
- baseURL: https://api.cluster.example.com:6443
  baseurl_source: declared
  description: SCC resources for controlling pod security permissions
  name: Red Hat OpenShift Security Context Constraints API
  slug: red-hat-openshift-security-context-constraints-api
- baseURL: https://api.cluster.example.com:6443
  baseurl_source: declared
  description: Query available OpenShift versions
  name: Red Hat OpenShift Versions API
  slug: red-hat-openshift-versions-api
- description: OAuth authentication and authorization API for OpenShift.
  name: OpenShift OAuth API
  slug: openshift-oauth-api
- description: API for managing application builds and build configurations.
  name: OpenShift Build API
  slug: openshift-build-api
- description: API for managing container images and image streams.
  name: OpenShift Image API
  slug: openshift-image-api
- description: API for managing OpenShift projects (namespace extensions).
  name: OpenShift Project API
  slug: openshift-project-api
- description: API for managing workload resources including Pods, Deployments, DeploymentConfigs, StatefulSets, Jobs, CronJobs, ReplicaSets, and DaemonSets.
  name: OpenShift Workloads API
  slug: openshift-workloads-api
- description: API for managing network configuration including Services, Endpoints, Ingress, NetworkPolicy, and EgressFirewall resources.
  name: OpenShift Network API
  slug: openshift-network-api
- description: API for managing storage resources including PersistentVolumes, PersistentVolumeClaims, StorageClasses, CSI drivers, and VolumeSnapshots.
  name: OpenShift Storage API
  slug: openshift-storage-api
- description: API for managing authorization resources including SubjectAccessReview, SelfSubjectAccessReview, LocalSubjectAccessReview, and TokenReview.
  name: OpenShift Authorization API
  slug: openshift-authorization-api
- description: API for managing autoscaling resources including HorizontalPodAutoscaler, ClusterAutoscaler, and MachineAutoscaler.
  name: OpenShift Autoscale API
  slug: openshift-autoscale-api
- description: API for managing cluster configuration resources including APIServer, Authentication, Infrastructure, Ingress, Network, OAuth, and Scheduler configuration.
  name: OpenShift Config API
  slug: openshift-config-api
- description: API for managing OpenShift web console extensions including ConsoleCLIDownload, ConsoleExternalLogLink, ConsoleLink, ConsoleNotification, and ConsolePlugin.
  name: OpenShift Console API
  slug: openshift-console-api
- description: API for managing cluster-level resources including ClusterVersion, ClusterOperator, and infrastructure resources.
  name: OpenShift Cluster API
  slug: openshift-cluster-api
- description: API for managing machine resources including Machine, MachineSet, MachineHealthCheck, and MachineAutoscaler for cluster node lifecycle management.
  name: OpenShift Machine API
  slug: openshift-machine-api
- description: API for managing OpenShift operator lifecycle and configuration including Etcd, Console, Network, DNS, IngressController, and other operator resources.
  name: OpenShift Operator API
  slug: openshift-operator-api
- description: API for managing OperatorHub resources including CatalogSources, Subscriptions, InstallPlans, and ClusterServiceVersions for the Operator Lifecycle Manager.
  name: OpenShift OperatorHub API
  slug: openshift-operatorhub-api
- description: API for managing templates that provide parameterized sets of objects for creating applications and services.
  name: OpenShift Template API
  slug: openshift-template-api
- description: API for managing security resources including SecurityContextConstraints, RangeAllocation, and PodSecurityPolicyReview for controlling pod security.
  name: OpenShift Security API
  slug: openshift-security-api
- description: API for managing role-based access control resources including Roles, ClusterRoles, RoleBindings, and ClusterRoleBindings.
  name: OpenShift RBAC API
  slug: openshift-rbac-api
- description: API for managing node-level resources including Node, RuntimeClass, and node configuration.
  name: OpenShift Node API
  slug: openshift-node-api
- description: API for managing monitoring and observability resources including Prometheus, Alertmanager, ServiceMonitor, and PrometheusRule.
  name: OpenShift Monitoring API
  slug: openshift-monitoring-api
- description: API for managing bare metal and infrastructure provisioning resources including BareMetalHost, Provisioning, and hardware management.
  name: OpenShift Provisioning API
  slug: openshift-provisioning-api
- description: API for managing scheduling and quota resources including ResourceQuota, LimitRange, PriorityClass, and ClusterResourceQuota.
  name: OpenShift Schedule and Quota API
  slug: openshift-schedule-and-quota-api
- description: API for managing metadata resources including ConfigMaps, Secrets, Events, Namespaces, and ServiceAccounts.
  name: OpenShift Metadata API
  slug: openshift-metadata-api
- description: Managed service API for installing, modifying, operating, and upgrading Red Hat OpenShift clusters across cloud providers.
  name: OpenShift Cluster Manager API
  slug: openshift-cluster-manager-api
artifact_total: 106
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
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Red Hat OpenShift Container Platform Add-ons API
  slug: open-red-hat-openshift-add-ons-api
- collection_type: open
  name: Red Hat OpenShift Container Platform API
  slug: open-red-hat-openshift-api
- collection_type: open
  name: Red Hat OpenShift Container Platform Add-ons Builds API
  slug: open-red-hat-openshift-builds-api
- collection_type: open
  name: Red Hat OpenShift Cluster Manager API
  slug: open-red-hat-openshift-cluster-manager
- collection_type: open
  name: Red Hat OpenShift Container Platform Add-ons Clusters API
  slug: open-red-hat-openshift-clusters-api
- collection_type: open
  name: Red Hat OpenShift Container Platform Add-ons Deployment Configs API
  slug: open-red-hat-openshift-deployment-configs-api
- collection_type: open
  name: Red Hat OpenShift Container Platform Add-ons Identity Providers API
  slug: open-red-hat-openshift-identity-providers-api
- collection_type: open
  name: Red Hat OpenShift Container Platform Add-ons Image Streams API
  slug: open-red-hat-openshift-image-streams-api
- collection_type: open
  name: Red Hat OpenShift Container Platform Add-ons Machine Pools API
  slug: open-red-hat-openshift-machine-pools-api
- collection_type: open
  name: Red Hat OpenShift Container Platform Add-ons Projects API
  slug: open-red-hat-openshift-projects-api
- collection_type: open
  name: Red Hat OpenShift Container Platform Add-ons Routes API
  slug: open-red-hat-openshift-routes-api
- collection_type: open
  name: Red Hat OpenShift Container Platform Add-ons Security Context Constraints API
  slug: open-red-hat-openshift-security-context-constraints-api
- collection_type: open
  name: Red Hat OpenShift Container Platform Add-ons Versions API
  slug: open-red-hat-openshift-versions-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/red-hat-openshift/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-openshift/refs/heads/main/agentic-access/red-hat-openshift-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/red-hat-openshift-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-openshift/refs/heads/main/security/red-hat-openshift-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/red-hat-openshift-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-openshift/refs/heads/main/security/red-hat-openshift-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/red-hat-openshift-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-openshift/refs/heads/main/authentication/red-hat-openshift-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-openshift/refs/heads/main/openapi/_original/red-hat-openshift-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/red-hat-openshift-api-openapi.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-openshift/refs/heads/main/openapi/_original/red-hat-openshift-cluster-manager-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/red-hat-openshift-cluster-manager-openapi.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-openshift/refs/heads/main/json-ld/red-hat-openshift-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/red-hat-openshift-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-openshift/refs/heads/main/json-schema/red-hat-openshift-project-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/red-hat-openshift-project-schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-openshift/refs/heads/main/json-structure/red-hat-openshift-project-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/red-hat-openshift-project-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-openshift/refs/heads/main/rules/red-hat-openshift-rules.yml
  title: ''
  type: SpectralRuleset
  url: rules/red-hat-openshift-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/red-hat-openshift/refs/heads/main/vocabulary/red-hat-openshift-vocabulary.yml
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
modified: '2026-09-16'
name: Red Hat OpenShift
nav: Providers
network: true
overview: 'Red Hat OpenShift publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Add-ons API, Builds API, Clusters API, and 8 more. Tagged areas include Containers, Enterprise, Hybrid Cloud, Kubernetes, and Platform-as-a-Service.


  The Red Hat OpenShift catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Red Hat OpenShift''s developer surface includes authentication, documentation, pricing, engineering blog, signup flow, support, training material, and 16 more developer resources.'
plans:
- name: Red Hat Openshift Plans Pricing
  plan_count: 8
  slug: red-hat-openshift-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 2
  name: Red Hat Openshift Rate Limits
  slug: red-hat-openshift-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Red Hat OpenShift API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: red-hat-openshift-jsonschema-spectral-rules
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Red Hat OpenShift API Rules
  rule_count: 13
  severity_counts:
    error: 6
    hint: 0
    info: 3
    warn: 4
  slug: red-hat-openshift-rules
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.5
    catalog_earned_first_party: 0.0
    catalog_gap: 52.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    contract_governance: 28.8
    contract_quality: 63.9
    developer_ergonomics: 41.7
    discoverability: 68.5
    operational_transparency: 23.7
  previous_composite: 49.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- Platform-as-a-Service
- Red Hat
website: https://www.redhat.com/en/technologies/cloud-computing/openshift
---
