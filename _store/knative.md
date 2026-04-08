---
aid: knative
url: https://raw.githubusercontent.com/api-evangelist/knative/refs/heads/main/apis.yml
apis:
- aid: knative:knative-serving-api
  name: Knative Serving API
  description: Knative Serving extends the Kubernetes API with custom resources for deploying serverless workloads. The Service, Route, Configuration, and Revision resources enable automatic scaling including scale-to-zero, traffic splitting between revisions, and progressive rollouts. Serving handles container lifecycle, networking, and autoscaling automatically.
  humanURL: https://knative.dev/docs/serving/
  properties:
  - type: Documentation
    url: https://knative.dev/docs/serving/
  - type: Reference
    url: https://knative.dev/docs/serving/reference/serving-api/
  - type: GitHubRepository
    url: https://github.com/knative/serving
  - type: OpenAPI
    url: openapi/knative-serving-api-openapi.yml
  - type: JSONSchema
    url: json-schema/knative-serving-schema.json
  tags:
  - Auto-Scaling
  - Serverless
  - Serving
- aid: knative:knative-eventing-api
  name: Knative Eventing API
  description: Knative Eventing provides a set of Kubernetes custom resources for building event-driven architectures. It includes Broker and Trigger resources for event routing, Channel and Subscription for pub/sub messaging, and source resources for connecting external event producers to the eventing mesh. Events conform to the CloudEvents specification.
  humanURL: https://knative.dev/docs/eventing/
  properties:
  - type: Documentation
    url: https://knative.dev/docs/eventing/
  - type: Reference
    url: https://knative.dev/docs/eventing/reference/eventing-api/
  - type: GitHubRepository
    url: https://github.com/knative/eventing
  - type: OpenAPI
    url: openapi/knative-eventing-api-openapi.yml
  - type: AsyncAPI
    url: asyncapi/knative-cloudevents-asyncapi.yml
  - type: JSONSchema
    url: json-schema/knative-eventing-schema.json
  tags:
  - Event-Driven
  - Events
  - Pub/Sub
- aid: knative:knative-functions
  name: Knative Functions
  description: Knative Functions enables developers to create, build, and deploy stateless, event-driven functions as Knative Services using the func CLI or the kn func plugin. Functions can be written in multiple languages and are automatically deployed as auto-scaling Knative Services that respond to HTTP requests or CloudEvents.
  humanURL: https://knative.dev/docs/functions/
  properties:
  - type: Documentation
    url: https://knative.dev/docs/functions/
  - type: Getting Started
    url: https://knative.dev/docs/getting-started/about-knative-functions/
  - type: GitHubRepository
    url: https://github.com/knative/func
  tags:
  - CLI
  - Event-Driven
  - Functions
  - Serverless
- aid: knative:knative-cli
  name: Knative CLI (kn)
  description: The Knative CLI (kn) provides a command-line interface for creating and managing Knative resources including Services, Revisions, Routes, event sources, and Brokers. It simplifies tasks like traffic splitting and autoscaling configuration without requiring direct YAML editing.
  humanURL: https://knative.dev/docs/client/
  properties:
  - type: Documentation
    url: https://knative.dev/docs/client/
  - type: GitHubRepository
    url: https://github.com/knative/client
  tags:
  - CLI
  - Developer Tools
  - Kubernetes
name: Knative
tags:
- Auto-Scaling
- Cloud Native
- Event-Driven
- Graduated
- Kubernetes
- Serverless
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Knative is a CNCF graduated platform that extends Kubernetes to provide serverless capabilities. It consists of Serving for deploying and scaling serverless workloads with automatic scale-to-zero, and Eventing for building event-driven architectures with declarative event routing and delivery. Knative abstracts away infrastructure complexity so developers can focus on writing code.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

