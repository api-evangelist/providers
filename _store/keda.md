---
aid: keda
name: KEDA
description: KEDA (Kubernetes Event Driven Autoscaling) is a CNCF graduated application autoscaler that drives scaling of any container in Kubernetes based on the number of events needing to be processed. It extends Kubernetes with custom resources for defining scaling behavior and supports over 50 built-in scalers for event sources including Kafka, RabbitMQ, AWS SQS, Azure Service Bus, and Prometheus.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Autoscaling
  - CNCF
  - Event-Driven
  - Graduated
  - Kubernetes
url: https://raw.githubusercontent.com/api-evangelist/keda/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-03-18'
specificationVersion: '0.19'
apis:
  - aid: keda:keda-metrics-api
    name: KEDA Metrics API
    description: External metrics API server that exposes event-driven metrics from configured scalers to the Kubernetes Horizontal Pod Autoscaler. It implements the Kubernetes external metrics API interface, allowing the HPA controller to query scaler-derived metrics when making scaling decisions.
    humanURL: https://keda.sh/docs/latest/operate/metrics-server/
    tags:
      - External Metrics
      - HPA
      - Kubernetes
      - Metrics
    properties:
      - type: Documentation
        url: https://keda.sh/docs/latest/operate/metrics-server/
      - type: Getting Started
        url: https://keda.sh/docs/latest/deploy/
      - type: Reference
        url: https://keda.sh/docs/latest/concepts/
      - type: OpenAPI
        url: openapi/keda-metrics-api-openapi.yml
  - aid: keda:keda-scaled-object-api
    name: KEDA ScaledObject API
    description: The ScaledObject custom resource defines the mapping between an event source and a Kubernetes Deployment, StatefulSet, or custom resource that should be scaled based on event metrics. It specifies trigger scalers, scaling thresholds, min/max replica counts, and cooldown periods for workload-based autoscaling.
    humanURL: https://keda.sh/docs/latest/concepts/scaling-deployments/
    tags:
      - Autoscaling
      - CRD
      - Kubernetes
      - ScaledObject
    properties:
      - type: Documentation
        url: https://keda.sh/docs/latest/concepts/scaling-deployments/
      - type: JSONSchema
        url: scaled-object.json
      - type: JSONSchema
        url: json-schema/keda-scaled-object-schema.json
      - type: JSON-LD
        url: keda-context.jsonld
      - type: Reference
        url: https://keda.sh/docs/latest/reference/scaledobject-spec/
  - aid: keda:keda-scaled-job-api
    name: KEDA ScaledJob API
    description: The ScaledJob custom resource defines the mapping between an event source and Kubernetes Jobs that should be created in response to events. Unlike ScaledObject, ScaledJob creates new Job instances to process each unit of work rather than scaling existing long-running deployments, making it suited for batch workloads.
    humanURL: https://keda.sh/docs/latest/concepts/scaling-jobs/
    tags:
      - Autoscaling
      - CRD
      - Jobs
      - Kubernetes
    properties:
      - type: Documentation
        url: https://keda.sh/docs/latest/concepts/scaling-jobs/
      - type: JSONSchema
        url: scaled-job.json
      - type: JSON-LD
        url: keda-context.jsonld
      - type: Reference
        url: https://keda.sh/docs/latest/reference/scaledjob-spec/
  - aid: keda:keda-trigger-authentication-api
    name: KEDA TriggerAuthentication API
    description: The TriggerAuthentication and ClusterTriggerAuthentication custom resources define authentication parameters for KEDA trigger scalers, allowing credentials to be sourced from Kubernetes Secrets, environment variables, pod identity providers such as AWS IRSA or Azure Workload Identity, or HashiCorp Vault without embedding them in the ScaledObject.
    humanURL: https://keda.sh/docs/latest/concepts/authentication/
    tags:
      - Authentication
      - CRD
      - Kubernetes
      - Security
    properties:
      - type: Documentation
        url: https://keda.sh/docs/latest/concepts/authentication/
      - type: JSONSchema
        url: trigger-authentication.json
      - type: JSON-LD
        url: keda-context.jsonld
      - type: Reference
        url: https://keda.sh/docs/latest/reference/triggerauthentication-spec/
  - aid: keda:keda-cloud-event-source-api
    name: KEDA CloudEventSource API
    description: The CloudEventSource and ClusterCloudEventSource custom resources define HTTP or Azure Event Grid destinations where KEDA delivers CloudEvents when scaling events occur. Events follow the CloudEvents specification v1.0 and carry reason codes and messages for events such as ScalerError, ScaledObjectReady, ScaledObjectDeleted, and AuthenticationFailed. Optional event type filters allow consumers to subscribe to only the events they care about.
    humanURL: https://keda.sh/docs/latest/operate/cloud-events/
    tags:
      - CloudEvents
      - CRD
      - Events
      - Kubernetes
      - Webhooks
    properties:
      - type: Documentation
        url: https://keda.sh/docs/latest/operate/cloud-events/
      - type: AsyncAPI
        url: asyncapi/keda-cloud-events-asyncapi.yml
      - type: JSONSchema
        url: json-schema/keda-cloud-event-schema.json
common:
  - type: Website
    url: https://keda.sh/
  - type: Documentation
    url: https://keda.sh/docs/latest/
  - type: Getting Started
    url: https://keda.sh/docs/latest/deploy/
  - type: GitHub Organization
    url: https://github.com/kedacore
  - type: GitHubRepository
    url: https://github.com/kedacore/keda
  - type: Blog
    url: https://keda.sh/blog/
  - type: Community
    url: https://keda.sh/community/
  - type: Slack
    url: https://kubernetes.slack.com/archives/CKZJ36A5D
  - type: Change Log
    url: https://github.com/kedacore/keda/blob/main/CHANGELOG.md
  - type: Security
    url: https://github.com/kedacore/keda/blob/main/SECURITY.md
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/keda
  - type: JSON-LD
    url: keda-context.jsonld
  - type: JSON-LD
    url: json-ld/keda-context.jsonld
  - type: JSONSchema
    url: json-schema/keda-scaled-object-schema.json
  - type: JSONSchema
    url: json-schema/keda-cloud-event-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
