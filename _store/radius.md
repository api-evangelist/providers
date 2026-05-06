---
aid: radius
name: Radius
description: Application platform for cloud-native applications that enables developers to define, deploy, and manage applications across multiple clouds and on-premises environments using a unified model.
type: Index
url: https://raw.githubusercontent.com/api-evangelist/radius/refs/heads/main/apis.yml
tags:
  - Application Platform
  - Cloud Native
  - Infrastructure
  - Multi Cloud
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: radius:applications-core
    name: Radius Applications.Core API
    description: REST APIs for Applications.Core, providing management of applications, containers, environments, gateways, secret stores, volumes, and extenders within the Radius platform.
    humanURL: https://docs.radapp.io/reference/api/applications.core/
    baseURL: https://management.azure.com
    tags:
      - Applications
      - Containers
      - Environments
      - Gateways
      - Secret Stores
      - Volumes
    properties:
      - type: Documentation
        url: https://docs.radapp.io/reference/api/applications.core/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/radius/refs/heads/main/openapi/radius-applications-core-openapi.json
  - aid: radius:applications-dapr
    name: Radius Applications.Dapr API
    description: REST APIs for Applications.Dapr, providing management of Dapr-related building block resources for Radius applications.
    humanURL: https://docs.radapp.io/reference/api/applications.dapr/
    baseURL: https://management.azure.com
    tags:
      - Dapr
      - Building Blocks
    properties:
      - type: Documentation
        url: https://docs.radapp.io/reference/api/applications.dapr/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/radius/refs/heads/main/openapi/radius-applications-dapr-openapi.json
  - aid: radius:applications-datastores
    name: Radius Applications.Datastores API
    description: REST APIs for Applications.Datastores, providing management of database resources such as Redis, MongoDB, and SQL data stores within Radius.
    humanURL: https://docs.radapp.io/reference/api/applications.datastores/
    baseURL: https://management.azure.com
    tags:
      - Datastores
      - Databases
      - Redis
      - MongoDB
      - SQL
    properties:
      - type: Documentation
        url: https://docs.radapp.io/reference/api/applications.datastores/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/radius/refs/heads/main/openapi/radius-applications-datastores-openapi.json
  - aid: radius:applications-messaging
    name: Radius Applications.Messaging API
    description: REST APIs for Applications.Messaging, providing management of messaging service resources within the Radius application platform.
    humanURL: https://docs.radapp.io/reference/api/applications.messaging/
    baseURL: https://management.azure.com
    tags:
      - Messaging
      - Queues
    properties:
      - type: Documentation
        url: https://docs.radapp.io/reference/api/applications.messaging/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/radius/refs/heads/main/openapi/radius-applications-messaging-openapi.json
  - aid: radius:ucp
    name: Radius Universal Control Plane (UCP) API
    description: REST APIs for the Radius Universal Control Plane (UCP), the multi-cloud, multi-platform control plane that powers Radius resource management across providers.
    humanURL: https://docs.radapp.io/reference/api/ucp/
    baseURL: https://management.azure.com
    tags:
      - Control Plane
      - UCP
      - Multi Cloud
    properties:
      - type: Documentation
        url: https://docs.radapp.io/reference/api/ucp/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/radius/refs/heads/main/openapi/radius-ucp-openapi.json
common:
  - type: Documentation
    url: https://docs.radapp.io/
  - type: GettingStarted
    url: https://docs.radapp.io/getting-started/
  - type: SourceCode
    url: https://github.com/radius-project/radius
  - type: SignUp
    url: https://docs.radapp.io/installation/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
