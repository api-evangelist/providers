---
aid: openshift
name: OpenShift
description: A comprehensive API definition for Red Hat OpenShift, the enterprise Kubernetes platform.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.18'
url: https://raw.githubusercontent.com/api-evangelist/openshift/refs/heads/main/apis.yml
type: Index
position: Consumer
access: 3rd-Party
tags:
  - CI/CD
  - Cloud Native
  - Containers
  - DevOps
  - Enterprise
  - Kubernetes
  - PaaS
apis:
  - aid: openshift:openshift-rest-api
    name: OpenShift REST API
    description: Main REST API for managing OpenShift clusters, projects, and resources.
    humanURL: https://docs.openshift.com/
    baseURL: https://api.openshift.com
    tags:
      - Cloud
      - Containers
      - Kubernetes
      - Platform
    properties:
      - type: Documentation
        url: https://docs.openshift.com/container-platform/latest/rest_api/index.html
      - type: OpenAPI
        url: https://api.openshift.com/api/swagger.json
      - type: Authentication
        url: https://docs.openshift.com/container-platform/latest/authentication/index.html
      - type: Pricing
        url: https://www.redhat.com/en/technologies/cloud-computing/openshift/pricing
      - type: Support
        url: https://access.redhat.com/support
      - type: Status
        url: https://status.openshift.com/
      - type: SDK
        url: https://github.com/openshift/client-go
      - type: RateLimits
        url: https://docs.openshift.com/container-platform/latest/rest_api/understanding-api-support-tiers.html
      - type: GettingStarted
        url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/release_notes/index
  - aid: openshift:openshift-oauth-api
    name: OpenShift OAuth API
    description: OAuth authentication and authorization API for OpenShift.
    humanURL: https://docs.openshift.com/container-platform/latest/authentication/understanding-authentication.html
    baseURL: https://oauth-openshift.apps.openshift.com
    tags:
      - Authentication
      - OAuth
      - Security
    properties:
      - type: Documentation
        url: https://docs.openshift.com/container-platform/latest/authentication/understanding-authentication.html
  - aid: openshift:openshift-routes-api
    name: OpenShift Routes API
    description: API for managing application routes and ingress.
    humanURL: https://docs.openshift.com/container-platform/latest/networking/routes/route-configuration.html
    baseURL: https://api.openshift.com/apis/route.openshift.io/v1
    tags:
      - Ingress
      - Networking
      - Routing
    properties:
      - type: Documentation
        url: https://docs.openshift.com/container-platform/latest/networking/routes/route-configuration.html
  - aid: openshift:openshift-build-api
    name: OpenShift Build API
    description: API for managing application builds and build configurations.
    humanURL: https://docs.openshift.com/container-platform/latest/cicd/builds/understanding-builds.html
    baseURL: https://api.openshift.com/apis/build.openshift.io/v1
    tags:
      - Builds
      - CI/CD
      - Source-To-Image
    properties:
      - type: Documentation
        url: https://docs.openshift.com/container-platform/latest/cicd/builds/understanding-builds.html
  - aid: openshift:openshift-image-api
    name: OpenShift Image API
    description: API for managing container images and image streams.
    humanURL: https://docs.openshift.com/container-platform/latest/openshift_images/index.html
    baseURL: https://api.openshift.com/apis/image.openshift.io/v1
    tags:
      - Containers
      - Images
      - Registry
    properties:
      - type: Documentation
        url: https://docs.openshift.com/container-platform/latest/openshift_images/index.html
  - aid: openshift:openshift-project-api
    name: OpenShift Project API
    description: API for managing OpenShift projects (namespace extensions).
    humanURL: https://docs.openshift.com/container-platform/latest/applications/projects/working-with-projects.html
    baseURL: https://api.openshift.com/apis/project.openshift.io/v1
    tags:
      - Multi-Tenancy
      - Namespaces
      - Projects
    properties:
      - type: Documentation
        url: https://docs.openshift.com/container-platform/latest/applications/projects/working-with-projects.html
  - aid: openshift:openshift-workloads-api
    name: OpenShift Workloads API
    description: API for managing workload resources including Pods, Deployments, DeploymentConfigs, StatefulSets, Jobs, CronJobs, ReplicaSets, and DaemonSets.
    humanURL: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/workloads_apis/workloads-apis
    baseURL: https://api.openshift.com/apis/apps/v1
    tags:
      - Deployments
      - Jobs
      - Pods
      - StatefulSets
      - Workloads
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/workloads_apis/workloads-apis
  - aid: openshift:openshift-network-api
    name: OpenShift Network API
    description: API for managing network configuration including Services, Endpoints, Ingress, NetworkPolicy, and EgressFirewall resources.
    humanURL: https://docs.openshift.com/container-platform/4.17/rest_api/network_apis/network-apis-index.html
    baseURL: https://api.openshift.com/apis/network.openshift.io/v1
    tags:
      - Ingress
      - Networking
      - NetworkPolicy
    properties:
      - type: Documentation
        url: https://docs.openshift.com/container-platform/4.17/rest_api/network_apis/network-apis-index.html
  - aid: openshift:openshift-storage-api
    name: OpenShift Storage API
    description: API for managing storage resources including PersistentVolumes, PersistentVolumeClaims, StorageClasses, CSI drivers, and VolumeSnapshots.
    humanURL: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/storage_apis/persistentvolume-v1
    baseURL: https://api.openshift.com/api/v1
    tags:
      - CSI
      - PersistentVolumes
      - Storage
      - StorageClasses
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/storage_apis/persistentvolume-v1
  - aid: openshift:openshift-authorization-api
    name: OpenShift Authorization API
    description: API for managing authorization resources including SubjectAccessReview, SelfSubjectAccessReview, LocalSubjectAccessReview, and TokenReview.
    humanURL: https://docs.openshift.com/container-platform/4.17/rest_api/authorization_apis/selfsubjectreview-authentication-k8s-io-v1.html
    baseURL: https://api.openshift.com/apis/authorization.k8s.io/v1
    tags:
      - Access Control
      - Authorization
      - Security
    properties:
      - type: Documentation
        url: https://docs.openshift.com/container-platform/4.17/rest_api/authorization_apis/selfsubjectreview-authentication-k8s-io-v1.html
  - aid: openshift:openshift-autoscale-api
    name: OpenShift Autoscale API
    description: API for managing autoscaling resources including HorizontalPodAutoscaler, ClusterAutoscaler, and MachineAutoscaler.
    humanURL: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/autoscale_apis/horizontalpodautoscaler-autoscaling-v2
    baseURL: https://api.openshift.com/apis/autoscaling/v2
    tags:
      - Autoscaling
      - ClusterAutoscaler
      - HPA
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/autoscale_apis/horizontalpodautoscaler-autoscaling-v2
  - aid: openshift:openshift-config-api
    name: OpenShift Config API
    description: API for managing cluster configuration resources including APIServer, Authentication, Infrastructure, Ingress, Network, OAuth, and Scheduler configuration.
    humanURL: https://docs.openshift.com/container-platform/4.17/rest_api/config_apis/infrastructure-config-openshift-io-v1.html
    baseURL: https://api.openshift.com/apis/config.openshift.io/v1
    tags:
      - Cluster Settings
      - Configuration
      - Infrastructure
    properties:
      - type: Documentation
        url: https://docs.openshift.com/container-platform/4.17/rest_api/config_apis/infrastructure-config-openshift-io-v1.html
  - aid: openshift:openshift-console-api
    name: OpenShift Console API
    description: API for managing OpenShift web console extensions including ConsoleCLIDownload, ConsoleExternalLogLink, ConsoleLink, ConsoleNotification, and ConsolePlugin.
    humanURL: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html-single/console_apis/index
    baseURL: https://api.openshift.com/apis/console.openshift.io/v1
    tags:
      - Console
      - Extensions
      - Plugins
      - Web UI
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html-single/console_apis/index
  - aid: openshift:openshift-cluster-api
    name: OpenShift Cluster API
    description: API for managing cluster-level resources including ClusterVersion, ClusterOperator, and infrastructure resources.
    humanURL: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/cluster_apis/cluster-apis
    baseURL: https://api.openshift.com/apis/config.openshift.io/v1
    tags:
      - Cluster
      - ClusterVersion
      - Infrastructure
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/cluster_apis/cluster-apis
  - aid: openshift:openshift-machine-api
    name: OpenShift Machine API
    description: API for managing machine resources including Machine, MachineSet, MachineHealthCheck, and MachineAutoscaler for cluster node lifecycle management.
    humanURL: https://docs.openshift.com/container-platform/4.9/rest_api/machine_apis/machineconfig-machineconfiguration-openshift-io-v1.html
    baseURL: https://api.openshift.com/apis/machine.openshift.io/v1beta1
    tags:
      - Autoscaling
      - Infrastructure
      - Machines
      - Nodes
    properties:
      - type: Documentation
        url: https://docs.openshift.com/container-platform/4.9/rest_api/machine_apis/machineconfig-machineconfiguration-openshift-io-v1.html
  - aid: openshift:openshift-operator-api
    name: OpenShift Operator API
    description: API for managing OpenShift operator lifecycle and configuration including Etcd, Console, Network, DNS, IngressController, and other operator resources.
    humanURL: https://docs.openshift.com/container-platform/4.8/rest_api/operator_apis/operator-apis-index.html
    baseURL: https://api.openshift.com/apis/operator.openshift.io/v1
    tags:
      - Cluster Services
      - Lifecycle Management
      - Operators
    properties:
      - type: Documentation
        url: https://docs.openshift.com/container-platform/4.8/rest_api/operator_apis/operator-apis-index.html
  - aid: openshift:openshift-operatorhub-api
    name: OpenShift OperatorHub API
    description: API for managing OperatorHub resources including CatalogSources, Subscriptions, InstallPlans, and ClusterServiceVersions for the Operator Lifecycle Manager.
    humanURL: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html-single/operators/index
    baseURL: https://api.openshift.com/apis/operators.coreos.com/v1alpha1
    tags:
      - Catalog
      - OLM
      - OperatorHub
      - Subscriptions
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html-single/operators/index
  - aid: openshift:openshift-template-api
    name: OpenShift Template API
    description: API for managing templates that provide parameterized sets of objects for creating applications and services.
    humanURL: https://docs.openshift.com/container-platform/4.17/rest_api/template_apis/template-template-openshift-io-v1.html
    baseURL: https://api.openshift.com/apis/template.openshift.io/v1
    tags:
      - Application Deployment
      - Parameterization
      - Templates
    properties:
      - type: Documentation
        url: https://docs.openshift.com/container-platform/4.17/rest_api/template_apis/template-template-openshift-io-v1.html
  - aid: openshift:openshift-security-api
    name: OpenShift Security API
    description: API for managing security resources including SecurityContextConstraints, RangeAllocation, and PodSecurityPolicyReview for controlling pod security.
    humanURL: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/authentication_and_authorization/managing-pod-security-policies
    baseURL: https://api.openshift.com/apis/security.openshift.io/v1
    tags:
      - Access Control
      - Pod Security
      - SCC
      - Security
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/authentication_and_authorization/managing-pod-security-policies
  - aid: openshift:openshift-rbac-api
    name: OpenShift RBAC API
    description: API for managing role-based access control resources including Roles, ClusterRoles, RoleBindings, and ClusterRoleBindings.
    humanURL: https://docs.openshift.com/container-platform/4.8/authentication/using-rbac.html
    baseURL: https://api.openshift.com/apis/rbac.authorization.k8s.io/v1
    tags:
      - Access Control
      - Authorization
      - RBAC
      - Roles
    properties:
      - type: Documentation
        url: https://docs.openshift.com/container-platform/4.8/authentication/using-rbac.html
  - aid: openshift:openshift-node-api
    name: OpenShift Node API
    description: API for managing node-level resources including Node, RuntimeClass, and node configuration.
    humanURL: https://docs.openshift.com/container-platform/4.17/rest_api/node_apis/node-apis-index.html
    baseURL: https://api.openshift.com/api/v1
    tags:
      - Infrastructure
      - Nodes
      - Runtime
    properties:
      - type: Documentation
        url: https://docs.openshift.com/container-platform/4.17/rest_api/node_apis/node-apis-index.html
  - aid: openshift:openshift-monitoring-api
    name: OpenShift Monitoring API
    description: API for managing monitoring and observability resources including Prometheus, Alertmanager, ServiceMonitor, and PrometheusRule.
    humanURL: https://docs.openshift.com/container-platform/4.17/observability/monitoring/accessing-third-party-monitoring-apis.html
    baseURL: https://api.openshift.com/apis/monitoring.coreos.com/v1
    tags:
      - Alerting
      - Monitoring
      - Observability
      - Prometheus
    properties:
      - type: Documentation
        url: https://docs.openshift.com/container-platform/4.17/observability/monitoring/accessing-third-party-monitoring-apis.html
  - aid: openshift:openshift-provisioning-api
    name: OpenShift Provisioning API
    description: API for managing bare metal and infrastructure provisioning resources including BareMetalHost, Provisioning, and hardware management.
    humanURL: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/provisioning_apis/index
    baseURL: https://api.openshift.com/apis/metal3.io/v1alpha1
    tags:
      - Bare Metal
      - Hardware
      - Infrastructure
      - Provisioning
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/provisioning_apis/index
  - aid: openshift:openshift-schedule-and-quota-api
    name: OpenShift Schedule and Quota API
    description: API for managing scheduling and quota resources including ResourceQuota, LimitRange, PriorityClass, and ClusterResourceQuota.
    humanURL: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/schedule_and_quota_apis/schedule-and-quota-apis
    baseURL: https://api.openshift.com/api/v1
    tags:
      - LimitRanges
      - Quotas
      - Resource Management
      - Scheduling
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/schedule_and_quota_apis/schedule-and-quota-apis
  - aid: openshift:openshift-metadata-api
    name: OpenShift Metadata API
    description: API for managing metadata resources including ConfigMaps, Secrets, Events, Namespaces, and ServiceAccounts.
    humanURL: https://docs.openshift.com/container-platform/4.7/rest_api/metadata_apis/metadata-apis-index.html
    baseURL: https://api.openshift.com/api/v1
    tags:
      - ConfigMaps
      - Events
      - Metadata
      - Secrets
    properties:
      - type: Documentation
        url: https://docs.openshift.com/container-platform/4.7/rest_api/metadata_apis/metadata-apis-index.html
  - aid: openshift:openshift-cluster-manager-api
    name: OpenShift Cluster Manager API
    description: Managed service API for installing, modifying, operating, and upgrading Red Hat OpenShift clusters across cloud providers.
    humanURL: https://docs.redhat.com/en/documentation/openshift_cluster_manager/1-latest/html/managing_clusters/assembly-managing-clusters
    baseURL: https://api.openshift.com/api/clusters_mgmt/v1
    tags:
      - Cluster Management
      - Managed Service
      - Multi-Cloud
      - ROSA
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/openshift_cluster_manager/1-latest/html/managing_clusters/assembly-managing-clusters
      - type: GitHubOrganization
        url: https://github.com/openshift-online/ocm-api-model
common:
  - type: GettingStarted
    url: https://www.openshift.com/try
  - type: Blog
    url: https://www.openshift.com/blog
  - type: GitHubOrganization
    url: https://github.com/openshift
  - type: TermsOfService
    url: https://www.redhat.com/en/about/terms-use
  - type: PrivacyPolicy
    url: https://www.redhat.com/en/about/privacy-policy
  - type: ChangeLog
    url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.17/html/release_notes/ocp-4-17-release-notes
  - type: Login
    url: https://console.redhat.com/openshift
  - type: Features
    data:
      - name: Enterprise Kubernetes
        description: Production-grade Kubernetes platform with built-in security, monitoring, and lifecycle management.
      - name: Source-to-Image Builds
        description: Automated container image builds directly from source code repositories.
      - name: Operator Framework
        description: Lifecycle management for complex applications through Kubernetes Operators and OperatorHub.
      - name: Multi-Cluster Management
        description: Centralized management of multiple OpenShift clusters across cloud providers.
      - name: Built-in Monitoring
        description: Integrated Prometheus, Alertmanager, and Grafana for cluster and application observability.
  - type: UseCases
    data:
      - name: Application Modernization
        description: Migrate monolithic applications to containerized microservices on Kubernetes.
      - name: CI/CD Pipelines
        description: Automate build, test, and deployment workflows with integrated pipeline capabilities.
      - name: Edge Computing
        description: Deploy and manage applications at edge locations with lightweight OpenShift deployments.
      - name: Hybrid Cloud Deployment
        description: Run consistent workloads across on-premise, public cloud, and edge environments.
  - type: Integrations
    data:
      - name: Cloud Providers
        description: Native integration with AWS (ROSA), Azure (ARO), GCP, and IBM Cloud for managed deployments.
      - name: CI/CD Tools
        description: Integration with Jenkins, Tekton, GitLab CI, and GitHub Actions for automated pipelines.
      - name: Service Mesh
        description: Integration with Istio-based service mesh for traffic management, security, and observability.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
