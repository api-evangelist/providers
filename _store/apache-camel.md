---
aid: apache-camel
name: Apache Camel
description: Apache Camel is an open-source integration framework developed by the Apache Software Foundation that implements Enterprise Integration Patterns (EIPs) for connecting systems, services, and data. It provides a domain-specific language (DSL) in Java, XML, YAML, and Kotlin for defining routes between components. Camel ships with over 300 components for connecting to messaging systems, databases, cloud services, APIs, and file formats. Camel K extends this with a Kubernetes-native integration runtime and operator with a REST management API.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - Enterprise Integration
  - Integration
  - Messaging
  - Open Source
  - Routing
created: '2025-06-05'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-camel/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-camel:apache-camel-java-dsl
    name: Apache Camel Java DSL API
    description: The Apache Camel Java DSL provides a fluent API for defining integration routes using Enterprise Integration Patterns. Developers define RouteBuilder subclasses to connect Camel components via endpoints, processors, and transformers.
    humanURL: https://camel.apache.org/manual/java-dsl.html
    tags:
      - DSL
      - Integration
      - Java
      - Routing
    properties:
      - type: Documentation
        url: https://camel.apache.org/manual/java-dsl.html
      - type: APIReference
        url: https://camel.apache.org/manual/camelcontext.html
      - type: GettingStarted
        url: https://camel.apache.org/manual/getting-started.html
  - aid: apache-camel:apache-camel-rest-dsl
    name: Apache Camel REST DSL API
    description: The Apache Camel REST DSL provides a concise syntax for exposing and consuming RESTful services within Camel routes. It supports both REST service definition and REST proxy/consumer patterns.
    humanURL: https://camel.apache.org/manual/rest-dsl.html
    tags:
      - DSL
      - REST
      - Routing
    properties:
      - type: Documentation
        url: https://camel.apache.org/manual/rest-dsl.html
  - aid: apache-camel:apache-camel-k-operator-api
    name: Apache Camel K Operator API
    description: The Apache Camel K Operator exposes a Kubernetes Custom Resource API for deploying and managing Camel integrations as cloud-native serverless workloads on Kubernetes and OpenShift.
    humanURL: https://camel.apache.org/camel-k/next/apis/operator/
    tags:
      - Kubernetes
      - Operator
      - Serverless
    properties:
      - type: Documentation
        url: https://camel.apache.org/camel-k/next/apis/operator/
      - type: GettingStarted
        url: https://camel.apache.org/camel-k/next/installation/installation.html
  - aid: apache-camel:apache-camel-quarkus-api
    name: Apache Camel Quarkus API
    description: Apache Camel Quarkus provides native compilation and fast startup of Camel routes on Quarkus, enabling serverless and microservice deployments with Camel's integration components.
    humanURL: https://camel.apache.org/camel-quarkus/next/index.html
    tags:
      - Quarkus
      - Serverless
    properties:
      - type: Documentation
        url: https://camel.apache.org/camel-quarkus/next/index.html
common:
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/camel
  - type: Documentation
    url: https://camel.apache.org/docs/
  - type: GettingStarted
    url: https://camel.apache.org/manual/getting-started.html
  - type: Tutorials
    url: https://camel.apache.org/manual/camel-example-main.html
  - type: Support
    url: https://camel.apache.org/community/support/
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: ChangeLog
    url: https://github.com/apache/camel/releases
  - type: FAQ
    url: https://camel.apache.org/manual/faq/index.html
  - type: SDK
    url: https://search.maven.org/artifact/org.apache.camel/camel-core
    title: Java SDK (Maven)
  - type: Vocabulary
    url: vocabulary/apache-camel-vocabulary.yaml
  - type: Features
    data:
      - name: Enterprise Integration Patterns
        description: Implementation of 65+ EIPs including splitter, aggregator, content-based router, message translator, and dead letter channel.
      - name: 300+ Components
        description: Pre-built connectors for messaging (Kafka, ActiveMQ, RabbitMQ), cloud (AWS, Azure, GCP), databases, REST, SOAP, and file formats.
      - name: Multi-DSL Support
        description: Define routes in Java, XML, YAML, Kotlin, or Groovy DSL with full feature parity across languages.
      - name: REST DSL
        description: Concise DSL for exposing and consuming RESTful services with OpenAPI/Swagger integration.
      - name: Camel K Kubernetes Operator
        description: Deploy Camel integrations as cloud-native serverless workloads on Kubernetes and OpenShift.
      - name: Camel Quarkus
        description: Native compilation of Camel routes with Quarkus for fast startup and low memory serverless deployments.
      - name: Data Formats
        description: Built-in support for 50+ data format conversions including JSON, XML, CSV, Avro, Protobuf, and EDI.
      - name: Route Templates
        description: Parameterized route templates for building reusable integration patterns.
      - name: Saga Pattern
        description: Distributed transaction support using the saga pattern with compensating actions.
      - name: Observability
        description: Built-in metrics, tracing (OpenTelemetry), and health check endpoints for Camel routes.
  - type: UseCases
    data:
      - name: System Integration
        description: Connect disparate enterprise systems including ERP, CRM, databases, and cloud services using EIP patterns.
      - name: API Gateway
        description: Build lightweight API gateways for routing, transformation, and protocol mediation using the REST DSL.
      - name: Event-Driven Architecture
        description: Implement event-driven integrations with Kafka, ActiveMQ, and other messaging platforms.
      - name: Data Pipeline
        description: Build ETL pipelines transforming and routing data between storage systems and data formats.
      - name: Microservice Integration
        description: Wire microservices together using Camel K serverless integrations on Kubernetes.
      - name: Legacy Modernization
        description: Bridge legacy SOAP, FTP, and EDI systems with modern REST and cloud-native services.
  - type: Integrations
    data:
      - name: Apache Kafka
        description: Camel Kafka component for producing and consuming Kafka topic messages in integration routes.
      - name: Apache ActiveMQ
        description: Camel ActiveMQ component for JMS messaging with Apache ActiveMQ Classic and Artemis.
      - name: AWS Services
        description: Camel AWS components for S3, SQS, SNS, DynamoDB, Lambda, and other AWS services.
      - name: Kubernetes
        description: Camel K Operator for deploying integrations as native Kubernetes Custom Resources.
      - name: OpenAPI
        description: Camel REST DSL generates OpenAPI specifications and can create routes from OpenAPI contracts.
      - name: Spring Boot
        description: Camel Spring Boot starter for integrating Camel into Spring Boot applications.
      - name: Quarkus
        description: Camel Quarkus extensions for native compilation and serverless deployment of integration routes.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
