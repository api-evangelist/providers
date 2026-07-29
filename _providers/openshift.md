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
- acting_count: 22
  human_in_the_loop: 0
  name: Openshift Agentic Access
  operation_count: 42
  slug: openshift-agentic-access
  summary_line: 42 operations · 22 acting
api_count: 31
apis:
- description: OAuth authentication and authorization API for OpenShift.
  name: OpenShift OAuth API
  slug: openshift-oauth-api
- description: API for managing application routes and ingress.
  name: OpenShift Routes API
  slug: openshift-routes-api
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
- description: Manage build configuration templates that define how to transform source code into container images using Source, Docker, or Custom build strategies with configurable triggers.
  name: OpenShift BuildConfigs API
  slug: openshift-buildconfigs-api
- description: Manage builds and build configurations for source-to-image, Docker, and custom build strategies. Builds compile source code into runnable container images.
  name: OpenShift Builds API
  slug: openshift-builds-api
- description: Manage OpenShift DeploymentConfigs which provide declarative deployment lifecycle management with rolling, recreate, and custom strategies, plus automatic rollback and deployment triggers.
  name: OpenShift DeploymentConfigs API
  slug: openshift-deploymentconfigs-api
- description: Request creation of new projects. ProjectRequests are the mechanism through which users provision new projects subject to cluster policy.
  name: OpenShift ProjectRequests API
  slug: openshift-projectrequests-api
- description: Manage OpenShift projects which extend Kubernetes namespaces with additional metadata, access controls, and resource isolation for multi-tenant environments.
  name: OpenShift Projects API
  slug: openshift-projects-api
- description: Manage application routes that expose services at a hostname. Routes provide external access to services via HTTP/HTTPS, with support for TLS termination strategies including edge, passthrough, and re
  name: OpenShift Routes API
  slug: openshift-routes-api
artifact_total: 277
collections:
- collection_type: postman
  name: openshift-rest-api BuildConfigs API
  slug: postman-openshift-buildconfigs-api
- collection_type: postman
  name: openshift-rest-api BuildConfigs Builds API
  slug: postman-openshift-builds-api
- collection_type: postman
  name: openshift-rest-api BuildConfigs DeploymentConfigs API
  slug: postman-openshift-deploymentconfigs-api
- collection_type: postman
  name: openshift-rest-api BuildConfigs ProjectRequests API
  slug: postman-openshift-projectrequests-api
- collection_type: postman
  name: openshift-rest-api BuildConfigs Projects API
  slug: postman-openshift-projects-api
- collection_type: postman
  name: openshift-rest-api BuildConfigs Routes API
  slug: postman-openshift-routes-api
- collection_type: open
  name: openshift-rest-api
  slug: open-openshift-rest-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/openshift/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openshift-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openshift-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openshift-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/red-hat-openshift
- group: start
  title: ''
  type: GettingStarted
  url: https://www.openshift.com/try
- group: company
  title: ''
  type: Blog
  url: https://www.openshift.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openshift
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.redhat.com/en/about/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.redhat.com/en/about/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/release_notes/ocp-4-17-release-notes
- group: start
  title: ''
  type: Login
  url: https://console.redhat.com/openshift
created: '2024-01-01'
description: A comprehensive API definition for Red Hat OpenShift, the enterprise Kubernetes platform.
examples:
- key_count: 2
  name: Openshift Rest Build Config Example
  slug: openshift-rest-build-config-example
- key_count: 3
  name: Openshift Rest Build Config List Example
  slug: openshift-rest-build-config-list-example
- key_count: 7
  name: Openshift Rest Build Config Spec Example
  slug: openshift-rest-build-config-spec-example
- key_count: 2
  name: Openshift Rest Build Config Status Example
  slug: openshift-rest-build-config-status-example
- key_count: 2
  name: Openshift Rest Build Example
  slug: openshift-rest-build-example
- key_count: 3
  name: Openshift Rest Build List Example
  slug: openshift-rest-build-list-example
- key_count: 1
  name: Openshift Rest Build Output Example
  slug: openshift-rest-build-output-example
- key_count: 4
  name: Openshift Rest Build Request Example
  slug: openshift-rest-build-request-example
- key_count: 5
  name: Openshift Rest Build Source Example
  slug: openshift-rest-build-source-example
- key_count: 4
  name: Openshift Rest Build Spec Example
  slug: openshift-rest-build-spec-example
- key_count: 10
  name: Openshift Rest Build Status Example
  slug: openshift-rest-build-status-example
- key_count: 1
  name: Openshift Rest Build Strategy Example
  slug: openshift-rest-build-strategy-example
- key_count: 1
  name: Openshift Rest Build Trigger Cause Example
  slug: openshift-rest-build-trigger-cause-example
- key_count: 4
  name: Openshift Rest Build Trigger Policy Example
  slug: openshift-rest-build-trigger-policy-example
- key_count: 8
  name: Openshift Rest Container Example
  slug: openshift-rest-container-example
- key_count: 3
  name: Openshift Rest Custom Build Strategy Example
  slug: openshift-rest-custom-build-strategy-example
- key_count: 3
  name: Openshift Rest Custom Deployment Strategy Params Example
  slug: openshift-rest-custom-deployment-strategy-params-example
- key_count: 6
  name: Openshift Rest Deployment Condition Example
  slug: openshift-rest-deployment-condition-example
- key_count: 2
  name: Openshift Rest Deployment Config Example
  slug: openshift-rest-deployment-config-example
- key_count: 3
  name: Openshift Rest Deployment Config List Example
  slug: openshift-rest-deployment-config-list-example
- key_count: 4
  name: Openshift Rest Deployment Config Rollback Example
  slug: openshift-rest-deployment-config-rollback-example
- key_count: 7
  name: Openshift Rest Deployment Config Spec Example
  slug: openshift-rest-deployment-config-spec-example
- key_count: 8
  name: Openshift Rest Deployment Config Status Example
  slug: openshift-rest-deployment-config-status-example
- key_count: 2
  name: Openshift Rest Deployment Strategy Example
  slug: openshift-rest-deployment-strategy-example
- key_count: 2
  name: Openshift Rest Deployment Trigger Policy Example
  slug: openshift-rest-deployment-trigger-policy-example
- key_count: 5
  name: Openshift Rest Docker Build Strategy Example
  slug: openshift-rest-docker-build-strategy-example
- key_count: 2
  name: Openshift Rest Env Var Example
  slug: openshift-rest-env-var-example
- key_count: 4
  name: Openshift Rest List Meta Example
  slug: openshift-rest-list-meta-example
- key_count: 11
  name: Openshift Rest Object Meta Example
  slug: openshift-rest-object-meta-example
- key_count: 4
  name: Openshift Rest Object Reference Example
  slug: openshift-rest-object-reference-example
- key_count: 6
  name: Openshift Rest Owner Reference Example
  slug: openshift-rest-owner-reference-example
- key_count: 6
  name: Openshift Rest Pod Spec Example
  slug: openshift-rest-pod-spec-example
- key_count: 0
  name: Openshift Rest Pod Template Spec Example
  slug: openshift-rest-pod-template-spec-example
- key_count: 8
  name: Openshift Rest Probe Example
  slug: openshift-rest-probe-example
- key_count: 2
  name: Openshift Rest Project Example
  slug: openshift-rest-project-example
- key_count: 3
  name: Openshift Rest Project List Example
  slug: openshift-rest-project-list-example
- key_count: 4
  name: Openshift Rest Project Request Example
  slug: openshift-rest-project-request-example
- key_count: 1
  name: Openshift Rest Project Spec Example
  slug: openshift-rest-project-spec-example
- key_count: 2
  name: Openshift Rest Project Status Example
  slug: openshift-rest-project-status-example
- key_count: 1
  name: Openshift Rest Recreate Deployment Strategy Params Example
  slug: openshift-rest-recreate-deployment-strategy-params-example
- key_count: 2
  name: Openshift Rest Resource Requirements Example
  slug: openshift-rest-resource-requirements-example
- key_count: 5
  name: Openshift Rest Rolling Deployment Strategy Params Example
  slug: openshift-rest-rolling-deployment-strategy-params-example
- key_count: 2
  name: Openshift Rest Route Example
  slug: openshift-rest-route-example
- key_count: 5
  name: Openshift Rest Route Ingress Condition Example
  slug: openshift-rest-route-ingress-condition-example
- key_count: 4
  name: Openshift Rest Route Ingress Example
  slug: openshift-rest-route-ingress-example
- key_count: 3
  name: Openshift Rest Route List Example
  slug: openshift-rest-route-list-example
- key_count: 1
  name: Openshift Rest Route Port Example
  slug: openshift-rest-route-port-example
- key_count: 5
  name: Openshift Rest Route Spec Example
  slug: openshift-rest-route-spec-example
- key_count: 1
  name: Openshift Rest Route Status Example
  slug: openshift-rest-route-status-example
- key_count: 3
  name: Openshift Rest Route Target Reference Example
  slug: openshift-rest-route-target-reference-example
- key_count: 4
  name: Openshift Rest Scale Example
  slug: openshift-rest-scale-example
- key_count: 4
  name: Openshift Rest Source Build Strategy Example
  slug: openshift-rest-source-build-strategy-example
- key_count: 6
  name: Openshift Rest Status Example
  slug: openshift-rest-status-example
- key_count: 6
  name: Openshift Rest Tls Config Example
  slug: openshift-rest-tls-config-example
features:
- description: Production-grade Kubernetes platform with built-in security, monitoring, and lifecycle management.
  name: Enterprise Kubernetes
- description: Automated container image builds directly from source code repositories.
  name: Source-to-Image Builds
- description: Lifecycle management for complex applications through Kubernetes Operators and OperatorHub.
  name: Operator Framework
- description: Centralized management of multiple OpenShift clusters across cloud providers.
  name: Multi-Cluster Management
- description: Integrated Prometheus, Alertmanager, and Grafana for cluster and application observability.
  name: Built-in Monitoring
finops:
- name: Openshift Finops
  service_category: Application Platform / Containers
  slug: openshift-finops
image: /assets/icons/openshift.png
integrations:
- description: Native integration with AWS (ROSA), Azure (ARO), GCP, and IBM Cloud for managed deployments.
  name: Cloud Providers
- description: Integration with Jenkins, Tekton, GitLab CI, and GitHub Actions for automated pipelines.
  name: CI/CD Tools
- description: Integration with Istio-based service mesh for traffic management, security, and observability.
  name: Service Mesh
json_schemas:
- name: Build
  property_count: 5
  slug: openshift-build
- name: BuildConfig
  property_count: 5
  slug: openshift-buildconfig
- name: BuildConfigList
  property_count: 4
  slug: openshift-buildconfiglist
- name: BuildConfigSpec
  property_count: 11
  slug: openshift-buildconfigspec
- name: BuildConfigStatus
  property_count: 2
  slug: openshift-buildconfigstatus
- name: BuildList
  property_count: 4
  slug: openshift-buildlist
- name: BuildOutput
  property_count: 2
  slug: openshift-buildoutput
- name: BuildRequest
  property_count: 5
  slug: openshift-buildrequest
- name: BuildSource
  property_count: 5
  slug: openshift-buildsource
- name: BuildSpec
  property_count: 8
  slug: openshift-buildspec
- name: BuildStatus
  property_count: 11
  slug: openshift-buildstatus
- name: BuildStrategy
  property_count: 4
  slug: openshift-buildstrategy
- name: BuildTriggerCause
  property_count: 1
  slug: openshift-buildtriggercause
- name: BuildTriggerPolicy
  property_count: 4
  slug: openshift-buildtriggerpolicy
- name: Container
  property_count: 11
  slug: openshift-container
- name: CustomBuildStrategy
  property_count: 4
  slug: openshift-custombuildstrategy
- name: CustomDeploymentStrategyParams
  property_count: 3
  slug: openshift-customdeploymentstrategyparams
- name: DeploymentCondition
  property_count: 6
  slug: openshift-deploymentcondition
- name: DeploymentConfig
  property_count: 5
  slug: openshift-deploymentconfig
- name: DeploymentConfigList
  property_count: 4
  slug: openshift-deploymentconfiglist
- name: DeploymentConfigRollback
  property_count: 4
  slug: openshift-deploymentconfigrollback
- name: DeploymentConfigSpec
  property_count: 9
  slug: openshift-deploymentconfigspec
- name: DeploymentConfigStatus
  property_count: 8
  slug: openshift-deploymentconfigstatus
- name: DeploymentStrategy
  property_count: 6
  slug: openshift-deploymentstrategy
- name: DeploymentTriggerPolicy
  property_count: 2
  slug: openshift-deploymenttriggerpolicy
- name: DockerBuildStrategy
  property_count: 6
  slug: openshift-dockerbuildstrategy
- name: EnvVar
  property_count: 2
  slug: openshift-envvar
- name: ListMeta
  property_count: 4
  slug: openshift-listmeta
- name: ObjectMeta
  property_count: 11
  slug: openshift-objectmeta
- name: ObjectReference
  property_count: 4
  slug: openshift-objectreference
- name: OwnerReference
  property_count: 6
  slug: openshift-ownerreference
- name: PodSpec
  property_count: 6
  slug: openshift-podspec
- name: PodTemplateSpec
  property_count: 2
  slug: openshift-podtemplatespec
- name: Probe
  property_count: 8
  slug: openshift-probe
- name: Project
  property_count: 5
  slug: openshift-project
- name: ProjectList
  property_count: 4
  slug: openshift-projectlist
- name: ProjectRequest
  property_count: 5
  slug: openshift-projectrequest
- name: ProjectSpec
  property_count: 1
  slug: openshift-projectspec
- name: ProjectStatus
  property_count: 2
  slug: openshift-projectstatus
- name: RecreateDeploymentStrategyParams
  property_count: 1
  slug: openshift-recreatedeploymentstrategyparams
- name: ResourceRequirements
  property_count: 2
  slug: openshift-resourcerequirements
- name: BuildConfigList
  property_count: 3
  slug: openshift-rest-build-config-list
- name: BuildConfig
  property_count: 2
  slug: openshift-rest-build-config
- name: BuildConfigSpec
  property_count: 7
  slug: openshift-rest-build-config-spec
- name: BuildConfigStatus
  property_count: 2
  slug: openshift-rest-build-config-status
- name: BuildList
  property_count: 3
  slug: openshift-rest-build-list
- name: BuildOutput
  property_count: 1
  slug: openshift-rest-build-output
- name: BuildRequest
  property_count: 4
  slug: openshift-rest-build-request
- name: Build
  property_count: 2
  slug: openshift-rest-build
- name: BuildSource
  property_count: 5
  slug: openshift-rest-build-source
- name: BuildSpec
  property_count: 4
  slug: openshift-rest-build-spec
- name: BuildStatus
  property_count: 10
  slug: openshift-rest-build-status
- name: BuildStrategy
  property_count: 1
  slug: openshift-rest-build-strategy
- name: BuildTriggerCause
  property_count: 1
  slug: openshift-rest-build-trigger-cause
- name: BuildTriggerPolicy
  property_count: 4
  slug: openshift-rest-build-trigger-policy
- name: Container
  property_count: 8
  slug: openshift-rest-container
- name: CustomBuildStrategy
  property_count: 3
  slug: openshift-rest-custom-build-strategy
- name: CustomDeploymentStrategyParams
  property_count: 3
  slug: openshift-rest-custom-deployment-strategy-params
- name: DeploymentCondition
  property_count: 6
  slug: openshift-rest-deployment-condition
- name: DeploymentConfigList
  property_count: 3
  slug: openshift-rest-deployment-config-list
- name: DeploymentConfigRollback
  property_count: 4
  slug: openshift-rest-deployment-config-rollback
- name: DeploymentConfig
  property_count: 2
  slug: openshift-rest-deployment-config
- name: DeploymentConfigSpec
  property_count: 7
  slug: openshift-rest-deployment-config-spec
- name: DeploymentConfigStatus
  property_count: 8
  slug: openshift-rest-deployment-config-status
- name: DeploymentStrategy
  property_count: 2
  slug: openshift-rest-deployment-strategy
- name: DeploymentTriggerPolicy
  property_count: 2
  slug: openshift-rest-deployment-trigger-policy
- name: DockerBuildStrategy
  property_count: 5
  slug: openshift-rest-docker-build-strategy
- name: EnvVar
  property_count: 2
  slug: openshift-rest-env-var
- name: ListMeta
  property_count: 4
  slug: openshift-rest-list-meta
- name: ObjectMeta
  property_count: 11
  slug: openshift-rest-object-meta
- name: ObjectReference
  property_count: 4
  slug: openshift-rest-object-reference
- name: OwnerReference
  property_count: 6
  slug: openshift-rest-owner-reference
- name: PodSpec
  property_count: 6
  slug: openshift-rest-pod-spec
- name: PodTemplateSpec
  property_count: 0
  slug: openshift-rest-pod-template-spec
- name: Probe
  property_count: 8
  slug: openshift-rest-probe
- name: ProjectList
  property_count: 3
  slug: openshift-rest-project-list
- name: ProjectRequest
  property_count: 4
  slug: openshift-rest-project-request
- name: Project
  property_count: 2
  slug: openshift-rest-project
- name: ProjectSpec
  property_count: 1
  slug: openshift-rest-project-spec
- name: ProjectStatus
  property_count: 2
  slug: openshift-rest-project-status
- name: RecreateDeploymentStrategyParams
  property_count: 1
  slug: openshift-rest-recreate-deployment-strategy-params
- name: ResourceRequirements
  property_count: 2
  slug: openshift-rest-resource-requirements
- name: RollingDeploymentStrategyParams
  property_count: 5
  slug: openshift-rest-rolling-deployment-strategy-params
- name: RouteIngressCondition
  property_count: 5
  slug: openshift-rest-route-ingress-condition
- name: RouteIngress
  property_count: 4
  slug: openshift-rest-route-ingress
- name: RouteList
  property_count: 3
  slug: openshift-rest-route-list
- name: RoutePort
  property_count: 1
  slug: openshift-rest-route-port
- name: Route
  property_count: 2
  slug: openshift-rest-route
- name: RouteSpec
  property_count: 5
  slug: openshift-rest-route-spec
- name: RouteStatus
  property_count: 1
  slug: openshift-rest-route-status
- name: RouteTargetReference
  property_count: 3
  slug: openshift-rest-route-target-reference
- name: Scale
  property_count: 4
  slug: openshift-rest-scale
- name: SourceBuildStrategy
  property_count: 4
  slug: openshift-rest-source-build-strategy
- name: Status
  property_count: 6
  slug: openshift-rest-status
- name: TLSConfig
  property_count: 6
  slug: openshift-rest-tls-config
- name: RollingDeploymentStrategyParams
  property_count: 5
  slug: openshift-rollingdeploymentstrategyparams
- name: OpenShift Route
  property_count: 5
  slug: openshift-route
- name: RouteIngress
  property_count: 4
  slug: openshift-routeingress
- name: RouteIngressCondition
  property_count: 5
  slug: openshift-routeingresscondition
- name: RouteList
  property_count: 4
  slug: openshift-routelist
- name: RoutePort
  property_count: 1
  slug: openshift-routeport
- name: RouteSpec
  property_count: 8
  slug: openshift-routespec
- name: RouteStatus
  property_count: 1
  slug: openshift-routestatus
- name: RouteTargetReference
  property_count: 3
  slug: openshift-routetargetreference
- name: Scale
  property_count: 5
  slug: openshift-scale
- name: SourceBuildStrategy
  property_count: 5
  slug: openshift-sourcebuildstrategy
- name: Status
  property_count: 7
  slug: openshift-status
- name: TLSConfig
  property_count: 6
  slug: openshift-tlsconfig
json_structures:
- name: Openshift Rest Build Config List Structure
  property_count: 3
  slug: openshift-rest-build-config-list-structure
- name: Openshift Rest Build Config Spec Structure
  property_count: 7
  slug: openshift-rest-build-config-spec-structure
- name: Openshift Rest Build Config Status Structure
  property_count: 2
  slug: openshift-rest-build-config-status-structure
- name: Openshift Rest Build Config Structure
  property_count: 2
  slug: openshift-rest-build-config-structure
- name: Openshift Rest Build List Structure
  property_count: 3
  slug: openshift-rest-build-list-structure
- name: Openshift Rest Build Output Structure
  property_count: 1
  slug: openshift-rest-build-output-structure
- name: Openshift Rest Build Request Structure
  property_count: 4
  slug: openshift-rest-build-request-structure
- name: Openshift Rest Build Source Structure
  property_count: 5
  slug: openshift-rest-build-source-structure
- name: Openshift Rest Build Spec Structure
  property_count: 4
  slug: openshift-rest-build-spec-structure
- name: Openshift Rest Build Status Structure
  property_count: 10
  slug: openshift-rest-build-status-structure
- name: Openshift Rest Build Strategy Structure
  property_count: 1
  slug: openshift-rest-build-strategy-structure
- name: Openshift Rest Build Structure
  property_count: 2
  slug: openshift-rest-build-structure
- name: Openshift Rest Build Trigger Cause Structure
  property_count: 1
  slug: openshift-rest-build-trigger-cause-structure
- name: Openshift Rest Build Trigger Policy Structure
  property_count: 4
  slug: openshift-rest-build-trigger-policy-structure
- name: Openshift Rest Container Structure
  property_count: 8
  slug: openshift-rest-container-structure
- name: Openshift Rest Custom Build Strategy Structure
  property_count: 3
  slug: openshift-rest-custom-build-strategy-structure
- name: Openshift Rest Custom Deployment Strategy Params Structure
  property_count: 3
  slug: openshift-rest-custom-deployment-strategy-params-structure
- name: Openshift Rest Deployment Condition Structure
  property_count: 6
  slug: openshift-rest-deployment-condition-structure
- name: Openshift Rest Deployment Config List Structure
  property_count: 3
  slug: openshift-rest-deployment-config-list-structure
- name: Openshift Rest Deployment Config Rollback Structure
  property_count: 4
  slug: openshift-rest-deployment-config-rollback-structure
- name: Openshift Rest Deployment Config Spec Structure
  property_count: 7
  slug: openshift-rest-deployment-config-spec-structure
- name: Openshift Rest Deployment Config Status Structure
  property_count: 8
  slug: openshift-rest-deployment-config-status-structure
- name: Openshift Rest Deployment Config Structure
  property_count: 2
  slug: openshift-rest-deployment-config-structure
- name: Openshift Rest Deployment Strategy Structure
  property_count: 2
  slug: openshift-rest-deployment-strategy-structure
- name: Openshift Rest Deployment Trigger Policy Structure
  property_count: 2
  slug: openshift-rest-deployment-trigger-policy-structure
- name: Openshift Rest Docker Build Strategy Structure
  property_count: 5
  slug: openshift-rest-docker-build-strategy-structure
- name: Openshift Rest Env Var Structure
  property_count: 2
  slug: openshift-rest-env-var-structure
- name: Openshift Rest List Meta Structure
  property_count: 4
  slug: openshift-rest-list-meta-structure
- name: Openshift Rest Object Meta Structure
  property_count: 11
  slug: openshift-rest-object-meta-structure
- name: Openshift Rest Object Reference Structure
  property_count: 4
  slug: openshift-rest-object-reference-structure
- name: Openshift Rest Owner Reference Structure
  property_count: 6
  slug: openshift-rest-owner-reference-structure
- name: Openshift Rest Pod Spec Structure
  property_count: 6
  slug: openshift-rest-pod-spec-structure
- name: Openshift Rest Pod Template Spec Structure
  property_count: 0
  slug: openshift-rest-pod-template-spec-structure
- name: Openshift Rest Probe Structure
  property_count: 8
  slug: openshift-rest-probe-structure
- name: Openshift Rest Project List Structure
  property_count: 3
  slug: openshift-rest-project-list-structure
- name: Openshift Rest Project Request Structure
  property_count: 4
  slug: openshift-rest-project-request-structure
- name: Openshift Rest Project Spec Structure
  property_count: 1
  slug: openshift-rest-project-spec-structure
- name: Openshift Rest Project Status Structure
  property_count: 2
  slug: openshift-rest-project-status-structure
- name: Openshift Rest Project Structure
  property_count: 2
  slug: openshift-rest-project-structure
- name: Openshift Rest Recreate Deployment Strategy Params Structure
  property_count: 1
  slug: openshift-rest-recreate-deployment-strategy-params-structure
- name: Openshift Rest Resource Requirements Structure
  property_count: 2
  slug: openshift-rest-resource-requirements-structure
- name: Openshift Rest Rolling Deployment Strategy Params Structure
  property_count: 5
  slug: openshift-rest-rolling-deployment-strategy-params-structure
- name: Openshift Rest Route Ingress Condition Structure
  property_count: 5
  slug: openshift-rest-route-ingress-condition-structure
- name: Openshift Rest Route Ingress Structure
  property_count: 4
  slug: openshift-rest-route-ingress-structure
- name: Openshift Rest Route List Structure
  property_count: 3
  slug: openshift-rest-route-list-structure
- name: Openshift Rest Route Port Structure
  property_count: 1
  slug: openshift-rest-route-port-structure
- name: Openshift Rest Route Spec Structure
  property_count: 5
  slug: openshift-rest-route-spec-structure
- name: Openshift Rest Route Status Structure
  property_count: 1
  slug: openshift-rest-route-status-structure
- name: Openshift Rest Route Structure
  property_count: 2
  slug: openshift-rest-route-structure
- name: Openshift Rest Route Target Reference Structure
  property_count: 3
  slug: openshift-rest-route-target-reference-structure
- name: Openshift Rest Scale Structure
  property_count: 4
  slug: openshift-rest-scale-structure
- name: Openshift Rest Source Build Strategy Structure
  property_count: 4
  slug: openshift-rest-source-build-strategy-structure
- name: Openshift Rest Status Structure
  property_count: 6
  slug: openshift-rest-status-structure
- name: Openshift Rest Tls Config Structure
  property_count: 6
  slug: openshift-rest-tls-config-structure
- name: Openshift Structure
  property_count: 0
  slug: openshift-structure
jsonld:
- class_count: 0
  name: Openshift Context
  property_count: 16
  slug: openshift-context
- class_count: 0
  name: Openshift Rest Context
  property_count: 0
  slug: openshift-rest-context
layout: provider
modified: '2026-05-19'
name: OpenShift
nav: Providers
network: true
overview: 'OpenShift publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Routes API, BuildConfigs API, Builds API, and 4 more. Tagged areas include CI/CD, Cloud Native, Containers, DevOps, and Enterprise.


  The OpenShift catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  OpenShift''s developer surface includes authentication, getting-started guide, engineering blog, changelog, and 8 more developer resources.'
plans:
- name: Openshift Plans Pricing
  plan_count: 8
  slug: openshift-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Openshift Rate Limits
  slug: openshift-rate-limits
rules:
- name: OpenShift API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: openshift-jsonschema-spectral-rules
- name: OpenShift API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 6
  slug: openshift-spectral-rules
score:
  band: strong
  composite: 57.7
  delta: -3.8
  facets:
    commercial_clarity: 73.7
    contract_quality: 68.1
    developer_ergonomics: 28.3
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 61.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openshift/refs/heads/main/screenshots/openshift-2026-06-20T191034.png
security:
- kind: authentication
  name: Openshift Authentication
  slug: openshift-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Openshift Domain Security
  slug: openshift-domain-security
  summary_line: TLSv1.3
slug: openshift
tags:
- CI/CD
- Cloud Native
- Containers
- DevOps
- Enterprise
- Kubernetes
- PaaS
use_cases:
- description: Migrate monolithic applications to containerized microservices on Kubernetes.
  name: Application Modernization
- description: Automate build, test, and deployment workflows with integrated pipeline capabilities.
  name: CI/CD Pipelines
- description: Deploy and manage applications at edge locations with lightweight OpenShift deployments.
  name: Edge Computing
- description: Run consistent workloads across on-premise, public cloud, and edge environments.
  name: Hybrid Cloud Deployment
---
