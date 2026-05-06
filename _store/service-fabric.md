---
aid: service-fabric
name: Service Fabric
description: Azure Service Fabric is an open-source distributed systems platform for packaging, deploying, and managing scalable and reliable microservices and containers. Service Fabric powers many Microsoft Azure core services, and thousands of services at scale including Azure SQL Database, Azure Cosmos DB, Skype for Business, and Cortana. Service Fabric provides a programming model for building stateful and stateless microservices, reliable collections, and actor-based services. The Service Fabric REST API enables cluster management, application lifecycle, and service configuration.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Distributed Systems
  - Microservices
  - Containers
  - Cloud Native
  - Kubernetes
  - Azure
  - Open Source
url: https://raw.githubusercontent.com/api-evangelist/service-fabric/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: service-fabric:service-fabric-cluster-api
    name: Service Fabric Cluster Management API
    description: The Service Fabric Cluster Management REST API enables management of Service Fabric clusters, nodes, applications, services, partitions, replicas, and health states. Provides operations for application lifecycle management (provision, create, upgrade, delete) and cluster health monitoring.
    humanURL: https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-rest-based-model
    baseURL: http://{cluster-endpoint}:19080
    tags:
      - Distributed Systems
      - Cluster Management
      - Application Lifecycle
      - Health Monitoring
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-rest-based-model
      - type: Reference
        url: https://docs.microsoft.com/en-us/rest/api/servicefabric/
      - type: GitHub
        url: https://github.com/microsoft/service-fabric
      - type: OpenAPI
        url: openapi/service-fabric-cluster-openapi.yml
      - type: JSONSchema
        url: json-schema/service-fabric-application-schema.json
      - type: JSONStructure
        url: json-structure/service-fabric-application-structure.json
      - type: SpectralRules
        url: rules/service-fabric-rules.yml
      - type: Capabilities
        url: capabilities/cluster-management.yaml
  - aid: service-fabric:service-fabric-sdk
    name: Service Fabric SDK
    description: Service Fabric SDK provides client libraries for .NET, Java, and Go for building Service Fabric services and interacting with the cluster. The SDK includes Reliable Collections, Reliable Actors, and the Reliable Services programming model.
    humanURL: https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-get-started
    tags:
      - SDK
      - .NET
      - Java
      - Microservices
      - Reliable Collections
    properties:
      - type: Documentation
        url: https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-get-started
      - type: NuGet
        url: https://www.nuget.org/packages/Microsoft.ServiceFabric/
      - type: Maven
        url: https://mvnrepository.com/artifact/com.microsoft.servicefabric/sf-actors
common:
  - type: Website
    url: https://docs.microsoft.com/en-us/azure/service-fabric/
  - type: GitHub
    url: https://github.com/microsoft/service-fabric
  - type: Documentation
    url: https://docs.microsoft.com/en-us/azure/service-fabric/
  - type: GettingStarted
    url: https://docs.microsoft.com/en-us/azure/service-fabric/service-fabric-get-started
  - type: Reference
    url: https://docs.microsoft.com/en-us/rest/api/servicefabric/
  - type: ChangeLog
    url: https://github.com/microsoft/service-fabric/releases
  - type: License
    url: https://github.com/microsoft/service-fabric/blob/master/LICENSE
  - type: JSONSchema
    url: json-schema/service-fabric-application-schema.json
  - type: JSONStructure
    url: json-structure/service-fabric-application-structure.json
  - type: JSONLDContext
    url: json-ld/service-fabric-context.jsonld
  - type: Examples
    url: examples/service-fabric-create-application-example.json
  - type: Examples
    url: examples/service-fabric-get-cluster-health-example.json
  - type: Vocabulary
    url: vocabulary/service-fabric-vocabulary.yml
  - type: SpectralRules
    url: rules/service-fabric-rules.yml
  - type: Capabilities
    url: capabilities/cluster-management.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
