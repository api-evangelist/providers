---
aid: apache-activemq
name: Apache ActiveMQ
description: Apache ActiveMQ is an open-source, high-performance message broker written in Java, developed by the Apache Software Foundation. It implements the Jakarta Messaging (JMS) API and supports multiple messaging protocols including AMQP, STOMP, MQTT, OpenWire, and HTTP/WebSocket, enabling reliable asynchronous messaging between distributed applications and microservices. ActiveMQ provides features such as network of brokers, message persistence (KahaDB, JDBC), high availability, message scheduling, and a web console with REST and Jolokia management APIs.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AMQP
  - Apache
  - Java
  - JMS
  - Message Broker
  - Messaging
  - MQTT
  - Open Source
  - STOMP
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-activemq/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-activemq:apache-activemq-rest-api
    name: Apache ActiveMQ REST API
    description: The ActiveMQ REST API provides HTTP-based access to messaging operations, allowing clients to produce and consume messages from queues and topics without a native JMS client. It supports sending messages via POST, receiving via GET, and subscribing with client IDs for persistent consumption.
    humanURL: https://activemq.apache.org/components/classic/documentation/rest
    baseURL: http://localhost:8161/api/message
    tags:
      - Messaging
      - REST
    properties:
      - type: Documentation
        url: https://activemq.apache.org/components/classic/documentation/rest
      - type: OpenAPI
        url: openapi/apache-activemq-rest-openapi.yaml
  - aid: apache-activemq:apache-activemq-jolokia-api
    name: Apache ActiveMQ Jolokia Management API
    description: The Jolokia JMX-HTTP bridge API provides HTTP access to JMX metrics and management operations for the ActiveMQ broker, enabling monitoring of broker health, queue depths, consumer counts, and other operational metrics without requiring a JMX client.
    humanURL: https://activemq.apache.org/components/classic/documentation/web-console
    baseURL: http://localhost:8161/api/jolokia
    tags:
      - Management
      - Monitoring
      - JMX
    properties:
      - type: Documentation
        url: https://activemq.apache.org/components/classic/documentation/web-console
  - aid: apache-activemq:apache-activemq-broker
    name: Apache ActiveMQ Broker
    description: The ActiveMQ Classic broker provides high-performance asynchronous messaging through multiple protocol interfaces including OpenWire, AMQP, STOMP, and MQTT. It includes a web-based management console, message persistence, network of brokers for load distribution, and high availability configurations.
    humanURL: https://activemq.apache.org/components/classic/documentation
    tags:
      - Broker
      - Messaging
    properties:
      - type: Documentation
        url: https://activemq.apache.org/components/classic/documentation
      - type: GettingStarted
        url: https://activemq.apache.org/components/classic/documentation/getting-started
common:
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/activemq
  - type: Documentation
    url: https://activemq.apache.org/
  - type: GettingStarted
    url: https://activemq.apache.org/components/classic/documentation/getting-started
  - type: FAQ
    url: https://activemq.apache.org/faq
  - type: Support
    url: https://activemq.apache.org/support
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: ChangeLog
    url: https://activemq.apache.org/components/classic/download
  - type: Features
    data:
      - name: Multi-Protocol Support
        description: Supports AMQP, STOMP, MQTT, OpenWire, JMS, Jakarta Messaging, HTTP, and WebSocket protocols for broad client compatibility.
      - name: Message Persistence
        description: Provides KahaDB and JDBC-based message persistence options to ensure message durability across broker restarts.
      - name: Network of Brokers
        description: Enables distributed messaging topologies by linking multiple brokers in a network for load balancing and failover.
      - name: High Availability
        description: Supports shared storage and master-slave configurations for high availability deployments.
      - name: Message Scheduling
        description: Built-in message scheduling capabilities allow delayed or recurring message delivery.
      - name: REST Messaging API
        description: HTTP-based REST API for producing and consuming messages from queues and topics without native JMS clients.
      - name: Jolokia Management API
        description: JMX-over-HTTP bridge via Jolokia for broker monitoring and management.
      - name: Web Console
        description: HTML5 web-based management console accessible at /admin for queue and topic management, subscriber monitoring, and message browsing.
      - name: Docker Support
        description: Official Docker image apache/activemq-classic available on Docker Hub for containerized deployments.
      - name: Embeddable Broker
        description: ActiveMQ can be embedded directly into Java applications for in-process messaging.
  - type: UseCases
    data:
      - name: Microservices Messaging
        description: Decouple microservices using asynchronous message queues and topics for event-driven architectures.
      - name: Enterprise Integration
        description: Connect disparate enterprise systems and applications using standard messaging protocols.
      - name: IoT Messaging
        description: Use MQTT protocol support for IoT device communication and telemetry data pipelines.
      - name: Workload Distribution
        description: Distribute work items across consumer pools using competing consumers on queues.
      - name: Event Streaming
        description: Publish events to topics and fan out to multiple subscriber applications.
      - name: Legacy JMS Integration
        description: Bridge legacy JMS-based applications with modern services using OpenWire and JMS API support.
  - type: Integrations
    data:
      - name: Spring Framework
        description: Deep integration with Spring and Spring Boot via spring-boot-starter-activemq.
      - name: Apache Camel
        description: Native Apache Camel ActiveMQ component for enterprise integration patterns.
      - name: Docker
        description: Official Docker Hub image apache/activemq-classic for containerized deployments.
      - name: Kubernetes
        description: Deployable on Kubernetes using the official Docker image and StatefulSets.
      - name: Hawtio
        description: HTML5 management console integration via hawtio for advanced broker management.
      - name: RHQ
        description: Operational monitoring integration with RHQ for enterprise monitoring.
      - name: Apache Karaf
        description: OSGi integration with Apache Karaf for modular enterprise deployments.
  - type: OpenAPI
    url: openapi/apache-activemq-rest-openapi.yaml
  - type: SpectralRules
    url: rules/apache-activemq-spectral-rules.yml
  - type: JSONSchema
    url: json-schema/rest-jolokia-response-schema.json
  - type: JSONSchema
    url: json-schema/rest-jolokia-error-schema.json
  - type: JSONLD
    url: json-ld/apache-activemq-rest-context.jsonld
  - type: Vocabulary
    url: vocabulary/apache-activemq-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/activemq-messaging.yaml
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
