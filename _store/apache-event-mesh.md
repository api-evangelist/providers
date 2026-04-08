---
aid: apache-event-mesh
url: https://raw.githubusercontent.com/api-evangelist/apache-event-mesh/refs/heads/main/apis.yml
apis:
- aid: apache-event-mesh:eventmesh-admin-api
  name: Apache EventMesh Admin API
  description: HTTP endpoints for managing the EventMesh runtime including topic management, subscription management, event publishing via HTTP, client monitoring, and runtime metrics.
  humanURL: https://eventmesh.apache.org/docs/instruction/quickstart
  baseURL: http://localhost:10106
  tags:
  - Admin
  - CloudEvents
  - REST API
  - Topics
  properties:
  - type: Documentation
    url: https://eventmesh.apache.org/docs/introduction
  - type: OpenAPI
    url: openapi/eventmesh-admin.yml
- aid: apache-event-mesh:eventmesh-messaging-api
  name: Apache EventMesh Messaging API
  description: Event-driven messaging via TCP, HTTP, and gRPC protocols. Events follow the CloudEvents specification. Supports pub-sub, request-reply, and broadcast messaging patterns.
  humanURL: https://eventmesh.apache.org/docs/sdk-java/tcp-sdk-usage
  tags:
  - CloudEvents
  - Event-Driven
  - Messaging
  - Pub-Sub
  properties:
  - type: Documentation
    url: https://eventmesh.apache.org/docs/sdk-java/tcp-sdk-usage
  - type: AsyncAPI
    url: asyncapi/eventmesh-messaging.yml
  - type: JSONSchema
    url: json-schema/cloudevent.json
name: Apache EventMesh
tags:
- Apache
- CloudEvents
- Event-Driven
- Messaging
- Open Source
- Serverless
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Apache EventMesh is a dynamic event-driven application runtime used to decouple the application and backend middleware layer, providing a serverless platform for building distributed event-driven architectures with support for CloudEvents and multiple messaging protocols.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

