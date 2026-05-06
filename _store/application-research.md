---
aid: application-research
name: Application Research
description: 'Application Research is a topic collection focused on specifications for declaring application service integration dependencies. It covers five specification formats: Score (platform-agnostic workload specs), Cloud Native Application Bundle (CNAB), Open Component Model (OCM), Open Resource Discovery (ORD), and Radius — all aimed at enabling deployment teams to understand what services (APIs, databases, caches, message buses, blob stores) an application requires.'
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Application Dependencies
  - Cloud Native
  - Integration
  - Research
  - Specifications
  - Workload Specifications
url: https://raw.githubusercontent.com/api-evangelist/application-research/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - name: Score Workload Specification API
    description: Score is a platform-agnostic workload specification that enables developers to define their workloads once and deploy them across multiple platforms including Kubernetes, Docker, and Helm. The API manages workload spec lifecycle and platform translations.
    humanURL: https://score.dev
    baseURL: https://api.score.dev/v1
    tags:
      - Platform Agnostic
      - Score
      - Workload Specification
    properties:
      - type: Documentation
        url: https://docs.score.dev
      - type: OpenAPI
        url: openapi/score-openapi.yml
      - type: JSONSchema
        url: json-schema/score.yml
      - type: CodeExamples
        url: examples/score-ecommerce.yml
        title: E-Commerce Example
      - type: CodeExamples
        url: examples/score-ai-ml-inference-platform.yml
        title: AI/ML Inference Example
      - type: CodeExamples
        url: examples/score-data-processing-pipeline.yml
        title: Data Processing Example
  - name: Cloud Native Application Bundle API
    description: CNAB (Cloud Native Application Bundle) is a specification for packaging and distributing cloud-native applications. The API manages bundle lifecycle including installation, upgrading, and uninstalling bundled applications across cloud environments.
    humanURL: https://cnab.io
    baseURL: https://api.cnab.io/v1
    tags:
      - Application Bundles
      - Cloud Native
      - Distribution
    properties:
      - type: Documentation
        url: https://cnab.io/docs
      - type: OpenAPI
        url: openapi/cloud-native-application-bundle-openapi.yml
      - type: JSONSchema
        url: json-schema/cloud-native-application-bundle-schema.yml
      - type: CodeExamples
        url: examples/cloud-native-application-bundle-example-wordpress.yml
        title: WordPress Bundle Example
      - type: CodeExamples
        url: examples/cloud-native-application-bundle-example-cassandra-cluster.yml
        title: Cassandra Cluster Example
  - name: Open Component Model API
    description: Open Component Model (OCM) provides a standard for describing software components in a supply chain, enabling teams to track, reference, and verify software artifacts.
    humanURL: https://ocm.software
    baseURL: https://ocm.software/api/v1
    tags:
      - Component Model
      - Software Supply Chain
      - Software Components
    properties:
      - type: Documentation
        url: https://ocm.software/docs
      - type: OpenAPI
        url: openapi/open-component-model-openapi.yml
      - type: JSONSchema
        url: json-schema/open-component-model.yml
      - type: CodeExamples
        url: examples/open-component-model-example-web-application.yml
        title: Web Application Example
  - name: Open Resource Discovery API
    description: Open Resource Discovery (ORD) is a protocol for machine-readable resource and capability discovery, enabling API management platforms to automatically discover what services and APIs an application exposes.
    humanURL: https://sap.github.io/open-resource-discovery/
    baseURL: https://api.open-resource-discovery.org/v1
    tags:
      - API Discovery
      - Metadata
      - Resource Discovery
    properties:
      - type: Documentation
        url: https://sap.github.io/open-resource-discovery/
      - type: OpenAPI
        url: openapi/open-resource-discovery-openapi.yml
      - type: JSONSchema
        url: json-schema/open-resource-discovery.yml
      - type: CodeExamples
        url: examples/open-resource-discovery-ecommerce.yml
        title: E-Commerce Discovery Example
  - name: Radius Application Platform API
    description: Radius is an open-source, cloud-agnostic application platform that enables developers to define and deploy applications with their dependencies in a portable, declarative way across cloud providers.
    humanURL: https://radapp.io
    baseURL: https://api.radapp.io/v1
    tags:
      - Application Platform
      - Cloud Agnostic
      - Radius
    properties:
      - type: Documentation
        url: https://docs.radapp.io
      - type: OpenAPI
        url: openapi/radius-openapi.yml
      - type: JSONSchema
        url: json-schema/radius.yml
      - type: CodeExamples
        url: examples/radius-ecommerce-microservice.yml
        title: E-Commerce Microservice Example
common:
  - type: GitHubOrganization
    url: https://github.com/api-evangelist
  - type: JSONLD
    url: json-ld/application-research-context.jsonld
  - type: SpectralRules
    url: rules/application-research-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/application-research-vocabulary.yaml
  - type: Features
    data:
      - name: Platform-Agnostic Workload Specs
        description: Score enables defining workloads once and deploying across multiple platforms
      - name: Application Bundle Packaging
        description: CNAB provides standardized packaging and distribution of cloud-native applications
      - name: Software Supply Chain Tracking
        description: OCM enables tracking and verifying software components through delivery pipelines
      - name: Automatic API Discovery
        description: ORD enables machines to discover what resources and APIs an application exposes
      - name: Cloud-Agnostic Dependency Declarations
        description: Radius enables portable application definitions with dependency declarations across clouds
  - type: UseCases
    data:
      - name: Multi-Platform Deployment
        description: Define an application once and deploy it across Kubernetes, Docker, or cloud platforms
      - name: Dependency Documentation
        description: Explicitly declare all required services (databases, caches, queues) for an application
      - name: Software Supply Chain Security
        description: Track and verify software component provenance and integrity
      - name: API Landscape Discovery
        description: Enable API management platforms to automatically discover application capabilities
      - name: Cloud Migration
        description: Move applications between cloud providers without rewriting configuration
  - type: Integrations
    data:
      - name: Kubernetes
        description: Primary deployment target for Score, CNAB, OCM, and Radius specs
      - name: Helm
        description: Score and CNAB support Helm-based deployment and chart generation
      - name: Docker
        description: Score workloads can be compiled to Docker Compose files
      - name: Terraform
        description: Radius integrates with Terraform for infrastructure provisioning
      - name: ArgoCD
        description: GitOps-based deployment of Score and CNAB bundles via ArgoCD
      - name: Backstage
        description: ORD integrations enable Backstage service catalog population
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
