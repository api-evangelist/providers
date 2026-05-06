---
aid: red-hat-openshift
name: Red Hat OpenShift
description: Red Hat OpenShift is an enterprise Kubernetes platform that provides a consistent hybrid cloud foundation for building, deploying, and scaling containerized applications. OpenShift extends Kubernetes with developer productivity tools, built-in CI/CD pipelines, integrated monitoring and logging, automated cluster management, role-based access control, and security policies. It supports deployments on bare metal, virtual machines, public clouds, and managed OpenShift services (ROSA, ARO, RHOIC). The OpenShift REST API exposes hundreds of Kubernetes and OpenShift-specific resource types organized into API groups for workload management, networking, storage, security, builds, pipelines, and cluster configuration.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Containers
  - Enterprise
  - Hybrid Cloud
  - Kubernetes
  - PaaS
  - Red Hat
url: https://raw.githubusercontent.com/api-evangelist/red-hat-openshift/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: red-hat-openshift:openshift-api
    name: Red Hat OpenShift Container Platform API
    description: The OpenShift Container Platform REST API is a Kubernetes-compatible REST API that extends the core Kubernetes API with OpenShift-specific resources. It provides programmatic access to manage workloads (Pods, Deployments, DeploymentConfigs, StatefulSets), networking (Routes, Ingress, Services, NetworkPolicies), storage (PersistentVolumes, StorageClasses), builds (BuildConfigs, ImageStreams), pipelines (Tekton Pipelines, PipelineRuns), security (SecurityContextConstraints, OAuth, RoleBindings), and cluster configuration. The API is versioned and organized into API groups served at /apis/{group}/{version}.
    humanURL: https://docs.openshift.com/container-platform/latest/rest_api/index.html
    baseURL: https://api.cluster.example.com:6443
    tags:
      - Builds
      - Cluster Management
      - Containers
      - Kubernetes
      - Networking
      - Workloads
    properties:
      - type: Documentation
        url: https://docs.openshift.com/container-platform/latest/rest_api/index.html
      - type: Getting Started
        url: https://developers.redhat.com/products/openshift/getting-started
      - type: OpenAPI
        url: openapi/red-hat-openshift-api-openapi.yml
  - aid: red-hat-openshift:openshift-cluster-manager-api
    name: Red Hat OpenShift Cluster Manager API
    description: The OpenShift Cluster Manager (OCM) API provides programmatic access to the Red Hat Hybrid Cloud Console for managing OpenShift clusters at scale. Operations include creating, updating, and deleting clusters; managing cluster add-ons; configuring identity providers and role bindings; monitoring cluster health and metrics; and managing subscriptions and quotas. The API is used by the OCM CLI and web console.
    humanURL: https://api.openshift.com/
    baseURL: https://api.openshift.com
    tags:
      - Cluster Management
      - Cloud
      - Hybrid Cloud
      - Multi-Cluster
      - Subscriptions
    properties:
      - type: Documentation
        url: https://api.openshift.com/
      - type: OpenAPI
        url: https://api.openshift.com/openapi
      - type: OpenAPI
        url: openapi/red-hat-openshift-cluster-manager-openapi.yml
  - aid: red-hat-openshift:openshift-pipelines-api
    name: Red Hat OpenShift Pipelines (Tekton) API
    description: OpenShift Pipelines is a cloud-native CI/CD solution based on Tekton that runs pipelines as Kubernetes-native CRDs. The API provides resources for defining Tasks (individual steps), Pipelines (task graphs), PipelineRuns (pipeline executions), TaskRuns, Workspaces, TriggerTemplates, and EventListeners for event-driven pipeline automation. All pipeline resources are managed through the Kubernetes API server using the tekton.dev API group.
    humanURL: https://docs.openshift.com/container-platform/latest/cicd/pipelines/understanding-openshift-pipelines.html
    baseURL: https://api.cluster.example.com:6443/apis/tekton.dev/v1
    tags:
      - CI/CD
      - Kubernetes
      - Pipelines
      - Tekton
    properties:
      - type: Documentation
        url: https://docs.openshift.com/container-platform/latest/cicd/pipelines/understanding-openshift-pipelines.html
      - type: GitHub
        url: https://github.com/openshift/pipelines-as-code
  - aid: red-hat-openshift:openshift-gitops-api
    name: Red Hat OpenShift GitOps (ArgoCD) API
    description: OpenShift GitOps is built on Argo CD and provides a GitOps continuous delivery solution for OpenShift clusters. The API exposes Application, AppProject, ApplicationSet, and Repository CRD resources for declarative cluster state management from Git repositories. The ArgoCD API also includes a REST gRPC-gateway API for direct interaction with the ArgoCD server.
    humanURL: https://docs.openshift.com/container-platform/latest/cicd/gitops/understanding-openshift-gitops.html
    baseURL: https://api.cluster.example.com:6443/apis/argoproj.io/v1alpha1
    tags:
      - ArgoCD
      - CI/CD
      - GitOps
      - Kubernetes
    properties:
      - type: Documentation
        url: https://docs.openshift.com/container-platform/latest/cicd/gitops/understanding-openshift-gitops.html
      - type: GitHub
        url: https://github.com/openshift/gitops-operator
  - aid: red-hat-openshift:openshift-service-mesh-api
    name: Red Hat OpenShift Service Mesh API
    description: Red Hat OpenShift Service Mesh, based on Istio, Kiali, Jaeger, and Prometheus, provides traffic management, security, and observability for microservices. The Service Mesh API exposes Istio CRDs including VirtualService, DestinationRule, ServiceEntry, Gateway, PeerAuthentication, AuthorizationPolicy, and Telemetry resources for configuring service-to-service communication, mutual TLS, and distributed tracing policies.
    humanURL: https://docs.openshift.com/container-platform/latest/service_mesh/v2x/ossm-about.html
    baseURL: https://api.cluster.example.com:6443/apis/networking.istio.io/v1beta1
    tags:
      - Istio
      - Kubernetes
      - Service Mesh
      - Traffic Management
    properties:
      - type: Documentation
        url: https://docs.openshift.com/container-platform/latest/service_mesh/v2x/ossm-about.html
  - aid: red-hat-openshift:openshift-serverless-api
    name: Red Hat OpenShift Serverless (Knative) API
    description: OpenShift Serverless, based on Knative, enables deploying and managing event-driven serverless workloads on OpenShift. The Serverless API exposes Knative Serving resources (Service, Route, Configuration, Revision) for auto-scaling workloads and Knative Eventing resources (Broker, Trigger, Channel, Subscription, EventSource) for event-driven architectures. Resources are managed through the serving.knative.dev and eventing.knative.dev API groups.
    humanURL: https://docs.openshift.com/serverless/latest/about/about-serverless.html
    baseURL: https://api.cluster.example.com:6443/apis/serving.knative.dev/v1
    tags:
      - Event-Driven
      - Knative
      - Kubernetes
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.openshift.com/serverless/latest/about/about-serverless.html
  - aid: red-hat-openshift:rosa-api
    name: Red Hat OpenShift Service on AWS (ROSA) API
    description: Red Hat OpenShift Service on AWS (ROSA) is a fully managed OpenShift service co-managed by Red Hat and AWS. The ROSA API, exposed through the OCM service, provides operations for creating and managing ROSA clusters, configuring machine pools, managing identity providers, setting up private link connectivity, and monitoring cluster status. ROSA clusters also expose the full OpenShift API endpoint after provisioning.
    humanURL: https://docs.openshift.com/rosa/rosa_architecture/rosa-understanding.html
    baseURL: https://api.openshift.com/api/clusters_mgmt/v1
    tags:
      - AWS
      - Cloud
      - Managed Service
      - OpenShift
    properties:
      - type: Documentation
        url: https://docs.openshift.com/rosa/rosa_architecture/rosa-understanding.html
      - type: Getting Started
        url: https://docs.openshift.com/rosa/rosa_getting_started/rosa-getting-started-iam-prerequisites.html
common:
  - type: Website
    url: https://www.redhat.com/en/technologies/cloud-computing/openshift
  - type: Documentation
    url: https://docs.openshift.com/
  - type: Pricing
    url: https://www.redhat.com/en/technologies/cloud-computing/openshift/pricing
  - type: Blog
    url: https://www.redhat.com/en/blog/channel/red-hat-openshift
  - type: GitHub Organization
    url: https://github.com/openshift
  - type: Sign Up
    url: https://www.redhat.com/en/technologies/cloud-computing/openshift/try-it
  - type: Status
    url: https://status.redhat.com/
  - type: Support
    url: https://access.redhat.com/support
  - type: Privacy Policy
    url: https://www.redhat.com/en/about/privacy-policy
  - type: Terms of Service
    url: https://www.redhat.com/en/about/agreements
  - type: Training
    url: https://www.redhat.com/en/services/training-and-certification
  - type: OpenAPI
    url: openapi/red-hat-openshift-api-openapi.yml
  - type: OpenAPI
    url: openapi/red-hat-openshift-cluster-manager-openapi.yml
  - type: JSONLDContext
    url: json-ld/red-hat-openshift-context.jsonld
  - type: JSONSchema
    url: json-schema/red-hat-openshift-project-schema.json
  - type: JSONStructure
    url: json-structure/red-hat-openshift-project-structure.json
  - type: SpectralRuleset
    url: rules/red-hat-openshift-rules.yml
  - type: NaftikoCapability
    url: capabilities/cluster-management.yaml
  - type: Vocabulary
    url: vocabulary/red-hat-openshift-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
