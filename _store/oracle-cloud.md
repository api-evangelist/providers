---
aid: oracle-cloud
name: Oracle Cloud Infrastructure
description: Collection of Oracle Cloud Infrastructure (OCI) REST APIs for managing cloud resources and services.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
url: https://raw.githubusercontent.com/api-evangelist/oracle-cloud/refs/heads/main/apis.yml
tags:
  - Cloud Computing
  - Enterprise Cloud
  - Infrastructure as a Service
  - Oracle
  - Platform as a Service
apis:
  - name: Compute API
    description: Manage compute instances, images, and related resources.
    image: https://www.oracle.com/cloud/compute/
    humanURL: https://docs.oracle.com/en-us/iaas/api/#/en/iaas/latest/Instance/
    baseURL: https://iaas.{region}.oraclecloud.com
    tags:
      - Compute
      - Instances
      - Virtual Machines
    properties:
      - type: OpenAPI
        url: openapi/oracle-cloud-compute-openapi.yaml
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Compute/home.htm
      - type: Pricing
        url: https://www.oracle.com/cloud/compute/pricing.html
      - type: JSONSchema
        url: json-schema/compute-update-instance-details-schema.json
      - type: JSONSchema
        url: json-schema/compute-volume-attachment-schema.json
      - type: JSONSchema
        url: json-schema/compute-shape-schema.json
      - type: JSONSchema
        url: json-schema/compute-image-schema.json
      - type: JSONSchema
        url: json-schema/compute-instance-schema.json
      - type: JSONSchema
        url: json-schema/compute-launch-instance-details-schema.json
      - type: JSONSchema
        url: json-schema/compute-attach-volume-details-schema.json
      - type: JSONStructure
        url: json-structure/compute-volume-attachment-structure.json
      - type: JSONStructure
        url: json-structure/compute-launch-instance-details-structure.json
      - type: JSONStructure
        url: json-structure/compute-image-structure.json
      - type: JSONStructure
        url: json-structure/compute-shape-structure.json
      - type: JSONStructure
        url: json-structure/compute-instance-structure.json
      - type: JSONStructure
        url: json-structure/compute-update-instance-details-structure.json
      - type: JSONStructure
        url: json-structure/compute-attach-volume-details-structure.json
      - type: Example
        url: examples/compute-volume-attachment-example.json
      - type: Example
        url: examples/compute-shape-example.json
      - type: Example
        url: examples/compute-image-example.json
      - type: Example
        url: examples/compute-instance-example.json
      - type: Example
        url: examples/compute-update-instance-details-example.json
      - type: Example
        url: examples/compute-attach-volume-details-example.json
      - type: Example
        url: examples/compute-launch-instance-details-example.json
  - name: Object Storage API
    description: Store and retrieve large amounts of unstructured data.
    image: https://www.oracle.com/cloud/storage/
    humanURL: https://docs.oracle.com/en-us/iaas/api/#/en/objectstorage/latest/
    baseURL: https://objectstorage.{region}.oraclecloud.com
    tags:
      - Buckets
      - Object Storage
      - Storage
    properties:
      - type: OpenAPI
        url: openapi/oracle-cloud-object-storage-openapi.yaml
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Object/home.htm
      - type: Pricing
        url: https://www.oracle.com/cloud/storage/pricing.html
      - type: JSONSchema
        url: json-schema/object-storage-object-summary-schema.json
      - type: JSONSchema
        url: json-schema/object-storage-bucket-summary-schema.json
      - type: JSONSchema
        url: json-schema/object-storage-update-bucket-details-schema.json
      - type: JSONSchema
        url: json-schema/object-storage-preauthenticated-request-summary-schema.json
      - type: JSONSchema
        url: json-schema/object-storage-preauthenticated-request-schema.json
      - type: JSONSchema
        url: json-schema/object-storage-bucket-schema.json
      - type: JSONSchema
        url: json-schema/object-storage-list-objects-schema.json
      - type: JSONSchema
        url: json-schema/object-storage-create-bucket-details-schema.json
      - type: JSONSchema
        url: json-schema/object-storage-create-preauthenticated-request-details-schema.json
      - type: JSONStructure
        url: json-structure/object-storage-create-bucket-details-structure.json
      - type: JSONStructure
        url: json-structure/object-storage-create-preauthenticated-request-details-structure.json
      - type: JSONStructure
        url: json-structure/object-storage-update-bucket-details-structure.json
      - type: JSONStructure
        url: json-structure/object-storage-object-summary-structure.json
      - type: JSONStructure
        url: json-structure/object-storage-list-objects-structure.json
      - type: JSONStructure
        url: json-structure/object-storage-preauthenticated-request-summary-structure.json
      - type: JSONStructure
        url: json-structure/object-storage-preauthenticated-request-structure.json
      - type: JSONStructure
        url: json-structure/object-storage-bucket-summary-structure.json
      - type: JSONStructure
        url: json-structure/object-storage-bucket-structure.json
      - type: Example
        url: examples/object-storage-preauthenticated-request-example.json
      - type: Example
        url: examples/object-storage-bucket-example.json
      - type: Example
        url: examples/object-storage-bucket-summary-example.json
      - type: Example
        url: examples/object-storage-preauthenticated-request-summary-example.json
      - type: Example
        url: examples/object-storage-list-objects-example.json
      - type: Example
        url: examples/object-storage-create-bucket-details-example.json
      - type: Example
        url: examples/object-storage-object-summary-example.json
      - type: Example
        url: examples/object-storage-create-preauthenticated-request-details-example.json
      - type: Example
        url: examples/object-storage-update-bucket-details-example.json
  - name: Networking API
    description: Manage virtual cloud networks, subnets, and network resources.
    image: https://www.oracle.com/cloud/networking/
    humanURL: https://docs.oracle.com/en-us/iaas/api/#/en/iaas/latest/Vcn/
    baseURL: https://iaas.{region}.oraclecloud.com
    tags:
      - Load Balancer
      - Networking
      - VCN
    properties:
      - type: OpenAPI
        url: openapi/oracle-cloud-networking-openapi.yaml
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm
      - type: JSONSchema
        url: json-schema/networking-vcn-schema.json
      - type: JSONSchema
        url: json-schema/networking-create-vcn-details-schema.json
      - type: JSONSchema
        url: json-schema/networking-create-subnet-details-schema.json
      - type: JSONSchema
        url: json-schema/networking-route-table-schema.json
      - type: JSONSchema
        url: json-schema/networking-update-vcn-details-schema.json
      - type: JSONSchema
        url: json-schema/networking-create-internet-gateway-details-schema.json
      - type: JSONSchema
        url: json-schema/networking-subnet-schema.json
      - type: JSONSchema
        url: json-schema/networking-internet-gateway-schema.json
      - type: JSONSchema
        url: json-schema/networking-security-list-schema.json
      - type: JSONStructure
        url: json-structure/networking-security-list-structure.json
      - type: JSONStructure
        url: json-structure/networking-route-table-structure.json
      - type: JSONStructure
        url: json-structure/networking-update-vcn-details-structure.json
      - type: JSONStructure
        url: json-structure/networking-subnet-structure.json
      - type: JSONStructure
        url: json-structure/networking-create-subnet-details-structure.json
      - type: JSONStructure
        url: json-structure/networking-create-internet-gateway-details-structure.json
      - type: JSONStructure
        url: json-structure/networking-vcn-structure.json
      - type: JSONStructure
        url: json-structure/networking-internet-gateway-structure.json
      - type: JSONStructure
        url: json-structure/networking-create-vcn-details-structure.json
      - type: Example
        url: examples/networking-create-internet-gateway-details-example.json
      - type: Example
        url: examples/networking-security-list-example.json
      - type: Example
        url: examples/networking-internet-gateway-example.json
      - type: Example
        url: examples/networking-update-vcn-details-example.json
      - type: Example
        url: examples/networking-vcn-example.json
      - type: Example
        url: examples/networking-create-vcn-details-example.json
      - type: Example
        url: examples/networking-subnet-example.json
      - type: Example
        url: examples/networking-create-subnet-details-example.json
      - type: Example
        url: examples/networking-route-table-example.json
  - name: Database API
    description: Manage Oracle Database Cloud Services and Autonomous Databases.
    image: https://www.oracle.com/database/
    humanURL: https://docs.oracle.com/en-us/iaas/api/#/en/database/latest/
    baseURL: https://database.{region}.oraclecloud.com
    tags:
      - Autonomous Database
      - Database
      - DBaaS
    properties:
      - type: OpenAPI
        url: openapi/oracle-cloud-database-openapi.yaml
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Database/home.htm
      - type: Pricing
        url: https://www.oracle.com/cloud/price-list.html#database
      - type: JSONSchema
        url: json-schema/database-update-autonomous-database-details-schema.json
      - type: JSONSchema
        url: json-schema/database-autonomous-database-schema.json
      - type: JSONSchema
        url: json-schema/database-db-system-schema.json
      - type: JSONSchema
        url: json-schema/database-create-autonomous-database-details-schema.json
      - type: JSONSchema
        url: json-schema/database-autonomous-database-summary-schema.json
      - type: JSONSchema
        url: json-schema/database-db-system-summary-schema.json
      - type: JSONStructure
        url: json-structure/database-create-autonomous-database-details-structure.json
      - type: JSONStructure
        url: json-structure/database-autonomous-database-summary-structure.json
      - type: JSONStructure
        url: json-structure/database-update-autonomous-database-details-structure.json
      - type: JSONStructure
        url: json-structure/database-db-system-structure.json
      - type: JSONStructure
        url: json-structure/database-autonomous-database-structure.json
      - type: JSONStructure
        url: json-structure/database-db-system-summary-structure.json
      - type: Example
        url: examples/database-db-system-summary-example.json
      - type: Example
        url: examples/database-update-autonomous-database-details-example.json
      - type: Example
        url: examples/database-create-autonomous-database-details-example.json
      - type: Example
        url: examples/database-autonomous-database-example.json
      - type: Example
        url: examples/database-db-system-example.json
      - type: Example
        url: examples/database-autonomous-database-summary-example.json
  - name: Identity and Access Management API
    description: Manage users, groups, policies, and authentication.
    image: https://www.oracle.com/security/
    humanURL: https://docs.oracle.com/en-us/iaas/api/#/en/identity/latest/
    baseURL: https://identity.{region}.oraclecloud.com
    tags:
      - Authentication
      - Authorization
      - IAM
      - Security
    properties:
      - type: OpenAPI
        url: openapi/oracle-cloud-iam-openapi.yaml
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Identity/home.htm
      - type: JSONSchema
        url: json-schema/iam-policy-schema.json
      - type: JSONSchema
        url: json-schema/iam-compartment-schema.json
      - type: JSONSchema
        url: json-schema/iam-create-policy-details-schema.json
      - type: JSONSchema
        url: json-schema/iam-create-user-details-schema.json
      - type: JSONSchema
        url: json-schema/iam-group-schema.json
      - type: JSONSchema
        url: json-schema/iam-update-user-details-schema.json
      - type: JSONSchema
        url: json-schema/iam-create-group-details-schema.json
      - type: JSONSchema
        url: json-schema/iam-user-schema.json
      - type: JSONStructure
        url: json-structure/iam-create-group-details-structure.json
      - type: JSONStructure
        url: json-structure/iam-policy-structure.json
      - type: JSONStructure
        url: json-structure/iam-create-user-details-structure.json
      - type: JSONStructure
        url: json-structure/iam-compartment-structure.json
      - type: JSONStructure
        url: json-structure/iam-update-user-details-structure.json
      - type: JSONStructure
        url: json-structure/iam-create-policy-details-structure.json
      - type: JSONStructure
        url: json-structure/iam-user-structure.json
      - type: JSONStructure
        url: json-structure/iam-group-structure.json
      - type: Example
        url: examples/iam-policy-example.json
      - type: Example
        url: examples/iam-create-policy-details-example.json
      - type: Example
        url: examples/iam-create-group-details-example.json
      - type: Example
        url: examples/iam-group-example.json
      - type: Example
        url: examples/iam-create-user-details-example.json
      - type: Example
        url: examples/iam-compartment-example.json
      - type: Example
        url: examples/iam-update-user-details-example.json
      - type: Example
        url: examples/iam-user-example.json
  - name: Container Engine for Kubernetes API
    description: Manage Kubernetes clusters and node pools.
    image: https://www.oracle.com/cloud/cloud-native/container-engine-kubernetes/
    humanURL: https://docs.oracle.com/en-us/iaas/api/#/en/containerengine/latest/
    baseURL: https://containerengine.{region}.oraclecloud.com
    tags:
      - Containers
      - Kubernetes
      - OKE
    properties:
      - type: OpenAPI
        url: openapi/oracle-cloud-oke-openapi.yaml
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/ContEng/home.htm
      - type: JSONSchema
        url: json-schema/oke-node-pool-schema.json
      - type: JSONSchema
        url: json-schema/oke-node-pool-summary-schema.json
      - type: JSONSchema
        url: json-schema/oke-create-cluster-details-schema.json
      - type: JSONSchema
        url: json-schema/oke-create-node-pool-details-schema.json
      - type: JSONSchema
        url: json-schema/oke-update-cluster-details-schema.json
      - type: JSONSchema
        url: json-schema/oke-cluster-summary-schema.json
      - type: JSONSchema
        url: json-schema/oke-cluster-schema.json
      - type: JSONStructure
        url: json-structure/oke-cluster-structure.json
      - type: JSONStructure
        url: json-structure/oke-node-pool-summary-structure.json
      - type: JSONStructure
        url: json-structure/oke-update-cluster-details-structure.json
      - type: JSONStructure
        url: json-structure/oke-create-node-pool-details-structure.json
      - type: JSONStructure
        url: json-structure/oke-node-pool-structure.json
      - type: JSONStructure
        url: json-structure/oke-create-cluster-details-structure.json
      - type: JSONStructure
        url: json-structure/oke-cluster-summary-structure.json
      - type: Example
        url: examples/oke-cluster-summary-example.json
      - type: Example
        url: examples/oke-create-cluster-details-example.json
      - type: Example
        url: examples/oke-cluster-example.json
      - type: Example
        url: examples/oke-node-pool-example.json
      - type: Example
        url: examples/oke-update-cluster-details-example.json
      - type: Example
        url: examples/oke-node-pool-summary-example.json
      - type: Example
        url: examples/oke-create-node-pool-details-example.json
  - name: Functions API
    description: Serverless platform for building and running applications.
    image: https://www.oracle.com/cloud/cloud-native/functions/
    humanURL: https://docs.oracle.com/en-us/iaas/api/#/en/functions/latest/
    baseURL: https://functions.{region}.oraclecloud.com
    tags:
      - FaaS
      - Functions
      - Serverless
    properties:
      - type: OpenAPI
        url: openapi/oracle-cloud-functions-openapi.yaml
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm
      - type: JSONSchema
        url: json-schema/functions-create-function-details-schema.json
      - type: JSONSchema
        url: json-schema/functions-create-application-details-schema.json
      - type: JSONSchema
        url: json-schema/functions-application-summary-schema.json
      - type: JSONSchema
        url: json-schema/functions-function-summary-schema.json
      - type: JSONSchema
        url: json-schema/functions-function-schema.json
      - type: JSONSchema
        url: json-schema/functions-application-schema.json
      - type: JSONStructure
        url: json-structure/functions-function-summary-structure.json
      - type: JSONStructure
        url: json-structure/functions-application-structure.json
      - type: JSONStructure
        url: json-structure/functions-create-function-details-structure.json
      - type: JSONStructure
        url: json-structure/functions-create-application-details-structure.json
      - type: JSONStructure
        url: json-structure/functions-application-summary-structure.json
      - type: JSONStructure
        url: json-structure/functions-function-structure.json
      - type: Example
        url: examples/functions-application-example.json
      - type: Example
        url: examples/functions-function-example.json
      - type: Example
        url: examples/functions-create-function-details-example.json
      - type: Example
        url: examples/functions-create-application-details-example.json
      - type: Example
        url: examples/functions-application-summary-example.json
      - type: Example
        url: examples/functions-function-summary-example.json
  - name: Monitoring API
    description: Monitor cloud resources using metrics and alarms.
    image: https://www.oracle.com/cloud/monitoring/
    humanURL: https://docs.oracle.com/en-us/iaas/api/#/en/monitoring/latest/
    baseURL: https://telemetry.{region}.oraclecloud.com
    tags:
      - Alarms
      - Metrics
      - Monitoring
    properties:
      - type: OpenAPI
        url: openapi/oracle-cloud-monitoring-openapi.yaml
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Monitoring/home.htm
      - type: JSONSchema
        url: json-schema/monitoring-metric-data-schema.json
      - type: JSONSchema
        url: json-schema/monitoring-create-alarm-details-schema.json
      - type: JSONSchema
        url: json-schema/monitoring-update-alarm-details-schema.json
      - type: JSONSchema
        url: json-schema/monitoring-summarize-metrics-data-details-schema.json
      - type: JSONSchema
        url: json-schema/monitoring-metric-schema.json
      - type: JSONSchema
        url: json-schema/monitoring-alarm-schema.json
      - type: JSONSchema
        url: json-schema/monitoring-alarm-summary-schema.json
      - type: JSONStructure
        url: json-structure/monitoring-summarize-metrics-data-details-structure.json
      - type: JSONStructure
        url: json-structure/monitoring-create-alarm-details-structure.json
      - type: JSONStructure
        url: json-structure/monitoring-alarm-structure.json
      - type: JSONStructure
        url: json-structure/monitoring-update-alarm-details-structure.json
      - type: JSONStructure
        url: json-structure/monitoring-metric-data-structure.json
      - type: JSONStructure
        url: json-structure/monitoring-alarm-summary-structure.json
      - type: JSONStructure
        url: json-structure/monitoring-metric-structure.json
      - type: Example
        url: examples/monitoring-alarm-example.json
      - type: Example
        url: examples/monitoring-metric-data-example.json
      - type: Example
        url: examples/monitoring-create-alarm-details-example.json
      - type: Example
        url: examples/monitoring-update-alarm-details-example.json
      - type: Example
        url: examples/monitoring-alarm-summary-example.json
      - type: Example
        url: examples/monitoring-summarize-metrics-data-details-example.json
      - type: Example
        url: examples/monitoring-metric-example.json
common:
  - type: Portal
    url: https://cloud.oracle.com/
  - type: Console
    url: https://console.oracle.com/
  - type: Documentation
    url: https://docs.oracle.com/en-us/iaas/Content/home.htm
  - type: Authentication
    url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdk_authentication_methods.htm
  - type: SDK
    url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdks.htm
  - type: CLI
    url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cliconcepts.htm
  - type: StatusPage
    url: https://ocistatus.oraclecloud.com/
  - type: Support
    url: https://www.oracle.com/support/
  - type: Pricing
    url: https://www.oracle.com/cloud/price-list.html
  - type: TermsOfService
    url: https://www.oracle.com/legal/terms.html
  - type: PrivacyPolicy
    url: https://www.oracle.com/legal/privacy/
  - type: GettingStarted
    url: https://docs.oracle.com/en-us/iaas/Content/GSG/Concepts/baremetalintro.htm
  - type: Blog
    url: https://blogs.oracle.com/cloud-infrastructure/
  - type: GitHubOrganization
    url: https://github.com/oracle
  - type: ReleaseNotes
    url: https://docs.oracle.com/en-us/iaas/releasenotes/index.htm
  - type: SignUp
    url: https://www.oracle.com/cloud/free/
  - type: Training
    url: https://www.oracle.com/cloud/training/
  - type: ChangeLog
    url: https://docs.oracle.com/en-us/iaas/Content/servicechanges.htm
  - type: Features
    data:
      - name: Compute
        description: Bare metal, virtual machine, and GPU compute instances with flexible shapes and autoscaling
      - name: Object Storage
        description: Highly durable and scalable object storage for unstructured data with S3 compatibility
      - name: Autonomous Database
        description: Self-driving, self-securing, self-repairing database with automated patching and tuning
      - name: Container Engine for Kubernetes
        description: Managed Kubernetes service for deploying and managing containerized applications
      - name: Virtual Cloud Networks
        description: Software-defined networking with private subnets, security lists, and network security groups
      - name: Identity and Access Management
        description: Fine-grained access control with policies, compartments, and identity federation
      - name: Serverless Functions
        description: Event-driven serverless compute platform based on Fn Project
      - name: Load Balancing
        description: Layer 4 and Layer 7 load balancing with SSL termination and health checks
      - name: Monitoring and Alarms
        description: Real-time metrics collection, dashboards, and automated alarm notifications
      - name: Cloud Guard
        description: Automated security monitoring and threat detection across OCI resources
      - name: Vault and Key Management
        description: Hardware security module-backed encryption key management and secret storage
      - name: Disaster Recovery
        description: Automated disaster recovery orchestration for complex multi-tier applications
      - name: Generative AI
        description: Large language model hosting and inference with customizable foundation models
      - name: Data Science
        description: Managed Jupyter notebooks and ML model lifecycle management platform
  - type: UseCases
    data:
      - name: Cloud Migration
        description: Migrate on-premises workloads to OCI with tools for assessment, planning, and execution
      - name: High Performance Computing
        description: Run HPC workloads with bare metal instances, RDMA networking, and cluster networking
      - name: Data Warehousing
        description: Build scalable data warehouses with Autonomous Database and integrated analytics
      - name: DevOps and CI/CD
        description: Automate build, test, and deployment pipelines with OCI DevOps and Container Engine
      - name: Disaster Recovery
        description: Implement business continuity with cross-region replication and automated failover
      - name: AI and Machine Learning
        description: Train and deploy ML models using GPU instances, Data Science, and Generative AI services
      - name: Hybrid Cloud
        description: Extend on-premises infrastructure with Cloud@Customer and dedicated regions
      - name: SaaS Extension
        description: Extend Oracle SaaS applications with custom APIs and integrations on OCI
      - name: IoT and Edge Computing
        description: Process IoT data at scale with streaming, functions, and edge infrastructure
      - name: Multi-Cloud Networking
        description: Connect OCI with AWS, Azure, and Google Cloud using FastConnect and partnerships
  - type: Integrations
    data:
      - name: Terraform
        description: Infrastructure as Code provisioning with the OCI Terraform Provider
      - name: Ansible
        description: Configuration management and automation with OCI Ansible Collection
      - name: Grafana
        description: Metrics visualization with the OCI Grafana Plugin for Monitoring data
      - name: Kubernetes
        description: Container orchestration with managed OKE clusters and Helm chart support
      - name: Visual Studio
        description: IDE integration with OCI Tools for Visual Studio
      - name: VS Code
        description: IDE integration with OCI Toolkit for Visual Studio Code
      - name: Eclipse
        description: IDE integration with OCI Toolkit for Eclipse
      - name: GitHub Actions
        description: CI/CD automation with OCI GitHub Actions for deployment pipelines
      - name: Oracle Integration Cloud
        description: Pre-built connectors for SaaS and on-premises application integration
      - name: Microsoft Azure
        description: Oracle Database@Azure for running Oracle databases on Azure infrastructure
  - type: SDK
    url: https://github.com/oracle/oci-java-sdk
    title: Java SDK
  - type: SDK
    url: https://github.com/oracle/oci-python-sdk
    title: Python SDK
  - type: SDK
    url: https://github.com/oracle/oci-typescript-sdk
    title: TypeScript SDK
  - type: SDK
    url: https://github.com/oracle/oci-dotnet-sdk
    title: .NET SDK
  - type: SDK
    url: https://github.com/oracle/oci-go-sdk
    title: Go SDK
  - type: SDK
    url: https://github.com/oracle/oci-ruby-sdk
    title: Ruby SDK
  - type: SDK
    url: https://github.com/oracle/oci-powershell-modules
    title: PowerShell Modules
  - type: GitHubRepository
    url: https://github.com/oracle/oci-cli
    title: OCI CLI Repository
  - type: GitHubRepository
    url: https://github.com/oracle/terraform-provider-oci
    title: Terraform Provider
  - type: SpectralRules
    url: rules/oracle-cloud-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/oracle-cloud-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/data-platform.yaml
  - type: NaftikoCapability
    url: capabilities/cloud-native-development.yaml
  - type: NaftikoCapability
    url: capabilities/infrastructure-management.yaml
  - type: NaftikoCapability
    url: capabilities/security-and-compliance.yaml
  - type: JSONLD
    url: json-ld/oracle-cloud-iam-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-database-create-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-monitoring-summarize-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-iam-update-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-oke-create-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-oke-node-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-functions-function-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-networking-update-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-database-db-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-functions-application-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-functions-create-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-object-storage-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-compute-update-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-database-autonomous-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-oke-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-monitoring-update-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-networking-route-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-compute-launch-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-compute-volume-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-monitoring-create-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-monitoring-metric-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-compute-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-functions-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-oke-cluster-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-networking-internet-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-monitoring-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-compute-attach-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-iam-create-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-database-update-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-networking-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-networking-create-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-oke-update-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-networking-security-context.jsonld
  - type: JSONLD
    url: json-ld/oracle-cloud-monitoring-alarm-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
include: []
---
