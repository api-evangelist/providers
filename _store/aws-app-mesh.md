---
aid: aws-app-mesh
url: https://raw.githubusercontent.com/api-evangelist/aws-app-mesh/refs/heads/main/apis.yml
apis:
- aid: aws-app-mesh:aws-app-mesh-api
  name: AWS App Mesh API
  description: API for creating and managing App Mesh service meshes, virtual services, virtual nodes, virtual routers, and routes.
  humanURL: https://aws.amazon.com/app-mesh/
  baseURL: https://appmesh.amazonaws.com
  tags:
  - Deprecated
  - Microservices
  - Networking
  - Service Mesh
  properties:
  - type: Documentation
    url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/Welcome.html
  - type: OpenAPI
    url: https://api.apis.guru/v2/specs/amazonaws.com/appmesh/2019-01-25/openapi.yaml
  - type: Reference
    url: https://docs.aws.amazon.com/app-mesh/latest/APIReference/Welcome.html
  - type: Authentication
    url: https://docs.aws.amazon.com/app-mesh/latest/userguide/security-iam.html
  - type: Quickstart
    url: https://docs.aws.amazon.com/app-mesh/latest/userguide/getting-started-ecs.html
  - type: Deprecation Notice
    url: https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect/
name: AWS App Mesh
tags:
- AWS
- Microservices
- Networking
- Service Mesh
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: AWS App Mesh is a service mesh that provides application-level networking to make it easy for your services to communicate with each other across multiple types of compute infrastructure. App Mesh standardizes how your services communicate, giving you end-to-end visibility and helping to ensure high availability for your applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

