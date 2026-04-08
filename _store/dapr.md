---
aid: dapr
url: https://raw.githubusercontent.com/api-evangelist/dapr/refs/heads/main/apis.yml
apis:
- aid: dapr:state-management
  name: Dapr State Management API
  tags:
  - Distributed Systems
  - Key Value
  - State Management
  humanURL: https://docs.dapr.io/reference/api/state_api/
  properties:
  - url: https://docs.dapr.io/reference/api/state_api/
    type: Documentation
  - url: openapi/dapr-state-management-openapi.yml
    type: OpenAPI
  - url: json-schema/state-item.json
    type: JSONSchema
  - url: https://docs.dapr.io/developing-applications/building-blocks/state-management/
    type: Reference
  - url: https://docs.dapr.io/sdks/
    type: Client Libraries
  description: The Dapr State Management API provides key/value-based state management capabilities for distributed applications. It supports saving, retrieving, deleting, and performing bulk and transactional operations on application state using pluggable state stores.
- aid: dapr:pubsub
  name: Dapr Pub/Sub API
  tags:
  - CloudEvents
  - Events
  - Messaging
  - Pub/Sub
  humanURL: https://docs.dapr.io/reference/api/pubsub_api/
  properties:
  - url: https://docs.dapr.io/reference/api/pubsub_api/
    type: Documentation
  - url: openapi/dapr-pubsub-openapi.yml
    type: OpenAPI
  - url: asyncapi/dapr-pubsub-asyncapi.yml
    type: AsyncAPI
  - url: json-schema/cloud-event.json
    type: JSONSchema
  - url: https://docs.dapr.io/developing-applications/building-blocks/pubsub/
    type: Reference
  - url: https://docs.dapr.io/sdks/
    type: Client Libraries
  description: The Dapr Pub/Sub API enables publish and subscribe messaging between applications. It supports publishing events to topics, bulk publishing, and discovering topic subscriptions using the CloudEvents 1.0 specification.
- aid: dapr:service-invocation
  name: Dapr Service Invocation API
  tags:
  - Microservices
  - Service Discovery
  - Service Invocation
  humanURL: https://docs.dapr.io/reference/api/service_invocation_api/
  properties:
  - url: https://docs.dapr.io/reference/api/service_invocation_api/
    type: Documentation
  - url: openapi/dapr-service-invocation-openapi.yml
    type: OpenAPI
  - url: https://docs.dapr.io/developing-applications/building-blocks/service-invocation/
    type: Reference
  - url: https://docs.dapr.io/sdks/
    type: Client Libraries
  description: The Dapr Service Invocation API enables applications to communicate with each other through well-known endpoints using HTTP methods. Dapr acts as a reverse proxy with built-in service discovery, distributed tracing, and error handling.
- aid: dapr:bindings
  name: Dapr Bindings API
  tags:
  - Bindings
  - Event-Driven
  - Integrations
  humanURL: https://docs.dapr.io/reference/api/bindings_api/
  properties:
  - url: https://docs.dapr.io/reference/api/bindings_api/
    type: Documentation
  - url: openapi/dapr-bindings-openapi.yml
    type: OpenAPI
  - url: json-schema/binding.json
    type: JSONSchema
  - url: https://docs.dapr.io/developing-applications/building-blocks/bindings/
    type: Reference
  - url: https://docs.dapr.io/sdks/
    type: Client Libraries
  description: The Dapr Bindings API enables applications to trigger and invoke external resources through output bindings, and receive events from external resources through input bindings. Supported bindings include Kafka, RabbitMQ, Azure Event Hubs, AWS SQS, GCP Storage, and more.
- aid: dapr:secrets
  name: Dapr Secrets API
  tags:
  - Key Management
  - Secrets
  - Security
  humanURL: https://docs.dapr.io/reference/api/secrets_api/
  properties:
  - url: https://docs.dapr.io/reference/api/secrets_api/
    type: Documentation
  - url: openapi/dapr-secrets-openapi.yml
    type: OpenAPI
  - url: json-schema/secret.json
    type: JSONSchema
  - url: https://docs.dapr.io/developing-applications/building-blocks/secrets/
    type: Reference
  - url: https://docs.dapr.io/sdks/
    type: Client Libraries
  description: The Dapr Secrets API provides a consistent way to retrieve application secrets from various secret stores, including Hashicorp Vault, AWS Secrets Manager, Azure Key Vault, GCP Secret Manager, and Kubernetes Secrets.
- aid: dapr:actors
  name: Dapr Actors API
  tags:
  - Actors
  - Distributed Systems
  - Virtual Actors
  humanURL: https://docs.dapr.io/reference/api/actors_api/
  properties:
  - url: https://docs.dapr.io/reference/api/actors_api/
    type: Documentation
  - url: openapi/dapr-actors-openapi.yml
    type: OpenAPI
  - url: json-schema/actor.json
    type: JSONSchema
  - url: https://docs.dapr.io/developing-applications/building-blocks/actors/
    type: Reference
  - url: https://docs.dapr.io/sdks/
    type: Client Libraries
  description: The Dapr Actors API provides virtual actor capabilities for distributed applications, including actor method invocation, state management, timers, and reminders with guaranteed single-threaded execution and message ordering.
- aid: dapr:workflow
  name: Dapr Workflow API
  tags:
  - Distributed Systems
  - Orchestration
  - Workflows
  humanURL: https://docs.dapr.io/reference/api/workflow_api/
  properties:
  - url: https://docs.dapr.io/reference/api/workflow_api/
    type: Documentation
  - url: openapi/dapr-workflow-openapi.yml
    type: OpenAPI
  - url: json-schema/workflow.json
    type: JSONSchema
  - url: https://docs.dapr.io/developing-applications/building-blocks/workflow/
    type: Reference
  - url: https://docs.dapr.io/sdks/
    type: Client Libraries
  description: The Dapr Workflow API provides the ability to manage workflow instances, including starting, getting status, pausing, resuming, terminating, purging, and raising events to workflows.
- aid: dapr:configuration
  name: Dapr Configuration API
  tags:
  - Configuration
  - Distributed Systems
  - Subscriptions
  humanURL: https://docs.dapr.io/reference/api/configuration_api/
  properties:
  - url: https://docs.dapr.io/reference/api/configuration_api/
    type: Documentation
  - url: openapi/dapr-configuration-openapi.yml
    type: OpenAPI
  - url: json-schema/configuration-item.json
    type: JSONSchema
  - url: https://docs.dapr.io/developing-applications/building-blocks/configuration/
    type: Reference
  - url: https://docs.dapr.io/sdks/
    type: Client Libraries
  description: The Dapr Configuration API enables applications to retrieve and subscribe to configuration items from supported configuration stores, allowing applications to react to configuration changes in real time.
- aid: dapr:distributed-lock
  name: Dapr Distributed Lock API
  tags:
  - Concurrency
  - Coordination
  - Distributed Lock
  humanURL: https://docs.dapr.io/reference/api/distributed_lock_api/
  properties:
  - url: https://docs.dapr.io/reference/api/distributed_lock_api/
    type: Documentation
  - url: openapi/dapr-distributed-lock-openapi.yml
    type: OpenAPI
  - url: https://docs.dapr.io/developing-applications/building-blocks/distributed-lock/
    type: Reference
  - url: https://docs.dapr.io/sdks/
    type: Client Libraries
  description: The Dapr Distributed Lock API enables applications to acquire and release locks on shared resources, ensuring mutual exclusion across multiple application instances using a lease-based locking mechanism.
- aid: dapr:cryptography
  name: Dapr Cryptography API
  tags:
  - Cryptography
  - Encryption
  - Security
  humanURL: https://docs.dapr.io/reference/api/cryptography_api/
  properties:
  - url: https://docs.dapr.io/reference/api/cryptography_api/
    type: Documentation
  - url: openapi/dapr-cryptography-openapi.yml
    type: OpenAPI
  - url: https://docs.dapr.io/developing-applications/building-blocks/cryptography/
    type: Reference
  - url: https://docs.dapr.io/sdks/
    type: Client Libraries
  description: The Dapr Cryptography API enables applications to perform cryptographic operations such as encrypting and decrypting data using configured cryptography components, without exposing cryptographic keys to the application.
- aid: dapr:jobs
  name: Dapr Jobs API
  tags:
  - Cron
  - Jobs
  - Scheduling
  humanURL: https://docs.dapr.io/reference/api/jobs_api/
  properties:
  - url: https://docs.dapr.io/reference/api/jobs_api/
    type: Documentation
  - url: openapi/dapr-jobs-openapi.yml
    type: OpenAPI
  - url: json-schema/job.json
    type: JSONSchema
  - url: https://docs.dapr.io/developing-applications/building-blocks/jobs/
    type: Reference
  - url: https://docs.dapr.io/sdks/
    type: Client Libraries
  description: The Dapr Jobs API enables applications to schedule, retrieve, and delete jobs for future execution at specific times or intervals using cron expressions or duration specifications.
- aid: dapr:health
  name: Dapr Health API
  tags:
  - Health
  - Kubernetes
  - Monitoring
  humanURL: https://docs.dapr.io/reference/api/health_api/
  properties:
  - url: https://docs.dapr.io/reference/api/health_api/
    type: Documentation
  - url: openapi/dapr-health-openapi.yml
    type: OpenAPI
  - url: https://docs.dapr.io/operations/observability/healthchecks/
    type: Reference
  description: The Dapr Health API provides health check endpoints for the Dapr sidecar, usable with container orchestrators like Kubernetes for readiness and liveness probes.
- aid: dapr:metadata
  name: Dapr Metadata API
  tags:
  - Metadata
  - Observability
  - Runtime
  humanURL: https://docs.dapr.io/reference/api/metadata_api/
  properties:
  - url: https://docs.dapr.io/reference/api/metadata_api/
    type: Documentation
  - url: openapi/dapr-metadata-openapi.yml
    type: OpenAPI
  - url: json-schema/metadata.json
    type: JSONSchema
  - url: https://docs.dapr.io/operations/observability/
    type: Reference
  description: The Dapr Metadata API provides information about the Dapr sidecar, including application connection details, registered components, active subscriptions, and HTTP endpoints. It also allows setting custom metadata attributes.
name: Dapr
tags:
- Distributed Systems
- Microservices
- Platform
- Pub/Sub
- State Management
- Workflows
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-07'
position: Consumer
description: Dapr (Distributed Application Runtime) is a portable, event-driven runtime that makes it easy for developers to build resilient, stateless, and stateful applications that run on the cloud and edge. It provides building block APIs for state management, pub/sub messaging, service invocation, bindings, actors, workflows, secrets, configuration, distributed locks, cryptography, jobs scheduling, health checks, and metadata.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

