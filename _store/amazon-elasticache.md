---
name: Amazon ElastiCache
description: Amazon ElastiCache is a fully managed in-memory caching service supporting Redis and Memcached. ElastiCache makes it easy to deploy, operate, and scale popular open-source compatible in-memory data stores, improving the performance of web applications.
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
url: https://aws.amazon.com/elasticache/
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - Amazon Web Services
  - AWS
  - Caching
  - Database
  - ElastiCache
  - In-Memory
  - Memcached
  - Redis
apis:
  - name: Amazon ElastiCache API
    description: API for managing Amazon ElastiCache clusters, replication groups, parameter groups, and related caching infrastructure resources.
    humanURL: https://aws.amazon.com/elasticache/
    baseURL: https://elasticache.amazonaws.com
    tags:
      - Caching
      - Database
      - In-Memory
      - Redis
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/
      - type: OpenAPI
        url: openapi/amazon-elasticache-openapi.yml
      - type: APIReference
        url: https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/
      - type: GettingStarted
        url: https://aws.amazon.com/elasticache/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/elasticache/pricing/
      - type: FAQ
        url: https://aws.amazon.com/elasticache/faqs/
      - type: JSONSchema
        url: json-schema/amazon-elasticache-cache-cluster-schema.json
      - type: JSONSchema
        url: json-schema/amazon-elasticache-cachecluster-schema.json
      - type: JSONSchema
        url: json-schema/amazon-elasticache-create-cache-cluster-result-schema.json
      - type: JSONLD
        url: json-ld/amazon-elasticache-context.jsonld
common:
  - type: Portal
    url: https://aws.amazon.com/
  - type: DeveloperPortal
    url: https://aws.amazon.com/elasticache/
  - type: Documentation
    url: https://docs.aws.amazon.com/elasticache/
  - type: Blog
    url: https://aws.amazon.com/blogs/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/elasticache/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: Login
    url: https://signin.aws.amazon.com/
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Support
    url: https://aws.amazon.com/support/
  - type: FAQ
    url: https://aws.amazon.com/elasticache/faqs/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Compliance
    url: https://aws.amazon.com/compliance/
  - type: Security
    url: https://aws.amazon.com/security/
  - type: YouTube
    url: https://www.youtube.com/user/AmazonWebServices
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/elasticache
  - type: KnowledgeCenter
    url: https://repost.aws/knowledge-center
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-elasticache-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/amazon-elasticache-capability.yaml
  - type: NaftikoCapability
    url: capabilities/shared/api.yaml
  - type: Vocabulary
    url: vocabulary/amazon-elasticache-vocabulary.yaml
  - type: Features
    data:
      - name: Redis Support
        description: Fully managed Redis with replication, clustering, and persistence
      - name: Memcached Support
        description: Fully managed Memcached for simple distributed caching
      - name: Multi-AZ Replication
        description: Automatic failover with Multi-AZ replication groups
      - name: Encryption
        description: Encryption at-rest and in-transit for compliance requirements
      - name: Automatic Backups
        description: Scheduled automatic backups with point-in-time recovery
  - type: UseCases
    data:
      - name: Session Management
        description: Store and manage user session data for web applications
      - name: Database Query Caching
        description: Cache expensive database queries to reduce latency
      - name: Real-Time Analytics
        description: Process and cache real-time data streams for analytics dashboards
      - name: Leaderboards and Gaming
        description: Build real-time leaderboards and gaming backends with Redis sorted sets
  - type: Integrations
    data:
      - name: Amazon EC2
        description: Connect ElastiCache clusters to EC2-hosted applications
      - name: Amazon RDS
        description: Cache RDS query results to reduce database load
      - name: Amazon Lambda
        description: Access ElastiCache from serverless Lambda functions
      - name: Amazon EKS
        description: Use ElastiCache as shared cache for Kubernetes workloads
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
