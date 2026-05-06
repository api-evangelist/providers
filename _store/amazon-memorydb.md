---
aid: amazon-memorydb
name: Amazon MemoryDB
description: Amazon MemoryDB for Redis is a durable, in-memory database service that delivers ultra-fast performance. It is Redis-compatible and provides microsecond reads, low single-digit millisecond writes, and enterprise-grade security.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AWS
  - Broadcasting
  - Media Processing
  - Media
url: https://raw.githubusercontent.com/api-evangelist/amazon-memorydb/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: amazon-memorydb:memorydb-api
    name: Amazon MemoryDB API
    description: Amazon MemoryDB for Redis is a durable, in-memory database service that delivers ultra-fast performance. It is Redis-compatible and provides microsecond reads, low single-digit millisecond writes, and enterprise-grade security.
    humanURL: https://aws.amazon.com/memorydb/
    baseURL: https://memory-db.us-east-1.amazonaws.com
    tags:
      - Broadcasting
      - Media Processing
      - Media
    properties:
      - type: Documentation
        url: https://docs.aws.amazon.com/memorydb/
      - type: OpenAPI
        url: openapi/amazon-memorydb-openapi-original.yml
      - type: GettingStarted
        url: https://aws.amazon.com/memorydb/getting-started/
      - type: Pricing
        url: https://aws.amazon.com/memorydb/pricing/
      - type: FAQ
        url: https://aws.amazon.com/memorydb/faqs/
common:
  - type: Portal
    url: https://aws.amazon.com/memorydb/
  - type: Documentation
    url: https://docs.aws.amazon.com/memorydb/
  - type: TermsOfService
    url: https://aws.amazon.com/service-terms/
  - type: PrivacyPolicy
    url: https://aws.amazon.com/privacy/
  - type: Support
    url: https://aws.amazon.com/premiumsupport/
  - type: Blog
    url: https://aws.amazon.com/blogs/media/
  - type: GitHubOrganization
    url: https://github.com/aws
  - type: Console
    url: https://console.aws.amazon.com/memorydb/
  - type: SignUp
    url: https://portal.aws.amazon.com/billing/signup
  - type: StatusPage
    url: https://health.aws.amazon.com/health/status
  - type: Contact
    url: https://aws.amazon.com/contact-us/
  - type: SpectralRules
    url: rules/amazon-memorydb-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amazon-memorydb-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amazon-memorydb-media-workflow.yaml
  - type: Features
    data:
      - name: Redis Compatibility
        description: Fully compatible with Redis and Memcached data structures, APIs, and commands.
      - name: Durable In-Memory Storage
        description: Multi-AZ transactional log ensures data durability without sacrificing performance.
      - name: Ultra-Fast Performance
        description: Microsecond read and low single-digit millisecond write latency at scale.
      - name: Cluster Management
        description: Create and manage MemoryDB clusters, shards, and replicas with ease.
      - name: Snapshot and Restore
        description: Create point-in-time snapshots for backup and restore operations.
      - name: Access Control Lists
        description: Fine-grained access control with user-based ACLs for security.
      - name: Multi-Region Clusters
        description: Deploy clusters across multiple AWS regions for global low-latency access.
  - type: UseCases
    data:
      - name: Microservices Session Management
        description: Store session data with ultra-low latency for modern microservices applications.
      - name: Real-Time Leaderboards
        description: Maintain sorted sets for gaming leaderboards and ranking systems.
      - name: Caching Layer
        description: Use as a durable caching layer to reduce database load and improve response times.
      - name: Pub/Sub Messaging
        description: Build real-time messaging and event streaming with Redis pub/sub patterns.
  - type: Integrations
    data:
      - name: Amazon VPC
        description: Deploy MemoryDB clusters within a VPC for network isolation.
      - name: AWS KMS
        description: Encrypt data at rest using AWS Key Management Service keys.
      - name: Amazon CloudWatch
        description: Monitor cluster metrics including cache hits, memory usage, and connections.
      - name: AWS IAM
        description: Control access using IAM policies and roles.
      - name: Amazon ElastiCache
        description: Migrate from ElastiCache Redis to MemoryDB for durable storage.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
