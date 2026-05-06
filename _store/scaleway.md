---
aid: scaleway
name: Scaleway
description: Scaleway is a European cloud provider offering a full suite of compute, storage, networking, AI, and serverless infrastructure services. Scaleway provides a comprehensive REST API for programmatic management of all cloud resources including Instances, Kubernetes clusters (Kapsule and Kosmos), managed databases, load balancers, VPC networking, object storage, secret management, serverless containers, serverless functions, IAM, generative AI inference, and more. The Scaleway API uses X-Auth-Token header authentication and provides OpenAPI specifications for every product via the developer portal.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - Cloud Computing
  - Containers
  - Database
  - European Cloud
  - Infrastructure
  - Kubernetes
  - Serverless
  - Storage
url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: scaleway:scaleway-instance-api
    name: Scaleway Instance API
    description: The Scaleway Instance API allows you to create, manage, and delete virtual machine instances, manage IP addresses, security groups, images, snapshots, volumes, and other compute resources across Scaleway's infrastructure zones.
    humanURL: https://www.scaleway.com/en/developers/api/instances/
    tags:
      - Compute
      - Images
      - Instances
      - Security Groups
      - Snapshots
      - Virtual Machines
    properties:
      - type: Documentation
        url: https://www.scaleway.com/en/developers/api/instances/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/openapi/scaleway-instance-openapi.yml
  - aid: scaleway:scaleway-kubernetes-api
    name: Scaleway Kubernetes API
    description: The Scaleway Kubernetes API (Kapsule and Kosmos) allows you to create and manage fully-managed Kubernetes clusters on Scaleway infrastructure, including cluster lifecycle management, node pool configuration, maintenance windows, and upgrades.
    humanURL: https://www.scaleway.com/en/developers/api/kubernetes/
    tags:
      - Containers
      - Kapsule
      - Kubernetes
      - Node Pools
      - Orchestration
    properties:
      - type: Documentation
        url: https://www.scaleway.com/en/developers/api/kubernetes/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/openapi/scaleway-kubernetes-openapi.yml
  - aid: scaleway:scaleway-iam-api
    name: Scaleway IAM API
    description: The Scaleway IAM API provides identity and access management for Scaleway organizations. Manage API keys, users, groups, applications, policies, and permission sets to control access to Scaleway resources.
    humanURL: https://www.scaleway.com/en/developers/api/iam/
    tags:
      - Access Control
      - API Keys
      - Groups
      - IAM
      - Identity
      - Permissions
      - Policies
    properties:
      - type: Documentation
        url: https://www.scaleway.com/en/developers/api/iam/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/openapi/scaleway-iam-openapi.yml
  - aid: scaleway:scaleway-load-balancer-api
    name: Scaleway Load Balancer API
    description: The Scaleway Load Balancer API allows you to create and manage highly available load balancers that distribute incoming traffic across multiple backend servers. Supports TCP, HTTP, and HTTPS load balancing with health checks, SSL termination, and session persistence.
    humanURL: https://www.scaleway.com/en/developers/api/load-balancer/zoned-api/
    tags:
      - Backend
      - Health Checks
      - Load Balancing
      - Networking
      - SSL
    properties:
      - type: Documentation
        url: https://www.scaleway.com/en/developers/api/load-balancer/zoned-api/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/openapi/scaleway-load-balancer-openapi.yml
  - aid: scaleway:scaleway-database-api
    name: Scaleway Managed Database API
    description: The Scaleway Managed Database API provides access to fully managed PostgreSQL, MySQL, and Redis database services. Create and manage database instances, backups, read replicas, and snapshots with automated patch management.
    humanURL: https://www.scaleway.com/en/developers/api/managed-databases-for-postgresql-and-mysql/
    tags:
      - Backup
      - Database
      - MySQL
      - PostgreSQL
      - Redis
      - Relational Database
    properties:
      - type: Documentation
        url: https://www.scaleway.com/en/developers/api/managed-databases-for-postgresql-and-mysql/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/openapi/scaleway-database-openapi.yml
  - aid: scaleway:scaleway-vpc-api
    name: Scaleway VPC API
    description: The Scaleway VPC API enables creation and management of Virtual Private Clouds and regional Private Networks for interconnecting Scaleway resources such as Instances, Load Balancers, and Managed Databases within a private L2 network.
    humanURL: https://www.scaleway.com/en/developers/api/vpc/
    tags:
      - Network Isolation
      - Networking
      - Private Networks
      - VPC
      - Virtual Private Cloud
    properties:
      - type: Documentation
        url: https://www.scaleway.com/en/developers/api/vpc/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/openapi/scaleway-vpc-openapi.yml
  - aid: scaleway:scaleway-serverless-containers-api
    name: Scaleway Serverless Containers API
    description: The Scaleway Serverless Containers API allows deployment of containerized applications as serverless workloads. Manage namespaces, containers, CRON triggers, and domains with pay-per-use pricing.
    humanURL: https://www.scaleway.com/en/developers/api/serverless-containers/
    tags:
      - Containers
      - CRON
      - Docker
      - Serverless
    properties:
      - type: Documentation
        url: https://www.scaleway.com/en/developers/api/serverless-containers/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/openapi/scaleway-serverless-containers-openapi.yml
  - aid: scaleway:scaleway-serverless-functions-api
    name: Scaleway Serverless Functions API
    description: The Scaleway Serverless Functions API enables deployment of function-as-a-service workloads. Manage function namespaces, functions, triggers, CRON schedules, and custom domains with event-driven execution.
    humanURL: https://www.scaleway.com/en/developers/api/serverless-functions/
    tags:
      - Event-Driven
      - FaaS
      - Functions
      - Serverless
    properties:
      - type: Documentation
        url: https://www.scaleway.com/en/developers/api/serverless-functions/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/openapi/scaleway-serverless-functions-openapi.yml
  - aid: scaleway:scaleway-secret-manager-api
    name: Scaleway Secret Manager API
    description: The Scaleway Secret Manager API provides secure storage and access management for secrets such as API keys, passwords, and certificates. Manage secrets, their versions, and access policies within Scaleway projects.
    humanURL: https://www.scaleway.com/en/developers/api/secret-manager/
    tags:
      - Certificates
      - Credentials
      - Secrets
      - Security
      - Vault
    properties:
      - type: Documentation
        url: https://www.scaleway.com/en/developers/api/secret-manager/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/openapi/scaleway-secret-manager-openapi.yml
  - aid: scaleway:scaleway-transactional-email-api
    name: Scaleway Transactional Email API
    description: The Scaleway Transactional Email API (TEM) provides reliable transactional email delivery services. Manage domains, send emails, track statistics, and monitor email delivery for application notifications and alerts.
    humanURL: https://www.scaleway.com/en/developers/api/transactional-email/
    tags:
      - Email
      - Messaging
      - Notifications
      - SMTP
      - Transactional Email
    properties:
      - type: Documentation
        url: https://www.scaleway.com/en/developers/api/transactional-email/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/openapi/scaleway-transactional-email-openapi.yml
  - aid: scaleway:scaleway-generative-apis
    name: Scaleway Generative APIs
    description: Scaleway Generative APIs provide access to AI language models and generative AI services hosted on Scaleway's European cloud infrastructure. Compatible with the OpenAI API format for easy integration.
    humanURL: https://www.scaleway.com/en/docs/generative-apis/
    tags:
      - AI
      - Artificial Intelligence
      - Generative AI
      - Language Models
      - LLM
    properties:
      - type: Documentation
        url: https://www.scaleway.com/en/docs/generative-apis/
      - type: Getting Started
        url: https://www.scaleway.com/en/docs/generative-apis/quickstart/
      - type: OpenAI Compatibility
        url: https://www.scaleway.com/en/docs/managed-inference/reference-content/openai-compatibility/
common:
  - type: Portal
    url: https://www.scaleway.com/en/developers/
  - type: Documentation
    url: https://www.scaleway.com/en/docs/
  - type: API Reference
    url: https://www.scaleway.com/en/developers/api/
  - type: GitHub
    url: https://github.com/scaleway
  - type: SDK
    url: https://github.com/scaleway/scaleway-sdk-go
  - type: SDK
    url: https://github.com/scaleway/scaleway-sdk-js
  - type: SDK
    url: https://github.com/scaleway/scaleway-sdk-python
  - type: CLI
    url: https://github.com/scaleway/scaleway-cli
  - type: Terraform Provider
    url: https://github.com/scaleway/terraform-provider-scaleway
  - type: Postman
    url: https://www.scaleway.com/en/docs/tutorials/postman-api/
  - type: Pricing
    url: https://www.scaleway.com/en/pricing/
  - type: Status
    url: https://status.scaleway.com/
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/vocabulary/scaleway-vocabulary.yml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/json-schema/scaleway-instance-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/json-schema/scaleway-cluster-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/json-schema/scaleway-secret-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/json-ld/scaleway-context.jsonld
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/rules/scaleway-rules.yml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/capabilities/cloud-infrastructure.yaml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/capabilities/networking.yaml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/capabilities/serverless.yaml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/capabilities/identity-and-access.yaml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/scaleway/refs/heads/main/capabilities/database-management.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
