---
aid: apache-servicemix
name: Apache ServiceMix
description: Apache ServiceMix is a flexible, open-source integration container that unifies the features and functionality of Apache ActiveMQ, Camel, CXF, and Karaf into a powerful runtime for building enterprise integration solutions.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Enterprise Integration
  - ESB
  - Integration
  - Messaging
  - OSGi
  - Apache
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-servicemix/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-servicemix:apache-servicemix
    name: Apache ServiceMix
    description: ServiceMix provides an OSGi-based ESB with JBI API support, integrating Camel for routing, CXF for web services, and ActiveMQ for messaging, with programmatic service deployment and management APIs.
    humanURL: https://servicemix.apache.org/docs/7.x/
    tags:
      - Enterprise Integration
      - ESB
      - REST
      - Apache
      - Open Source
    properties:
      - type: Documentation
        url: https://servicemix.apache.org/docs/7.x/
      - type: Documentation
        url: https://servicemix.apache.org/
      - type: OpenAPI
        url: openapi/apache-servicemix-rest-api.yaml
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: GitHubOrganization
    url: https://github.com/apache/servicemix
  - type: Documentation
    url: https://servicemix.apache.org/
  - type: SpectralRules
    url: rules/apache-servicemix-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-servicemix-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/servicemix-workflow.yaml
  - type: JSON-LD
    url: json-ld/apache-servicemix-context.jsonld
  - type: Features
    data:
      - name: OSGi Container
        description: Apache Karaf-based OSGi container for modular deployment
      - name: Apache Camel Routes
        description: Rich integration routing with 300+ Camel components
      - name: Apache CXF
        description: SOAP and REST web service hosting with CXF
      - name: ActiveMQ Messaging
        description: Built-in JMS messaging with Apache ActiveMQ
      - name: Hot Deployment
        description: Dynamic deployment of bundles and routes without restart
      - name: Enterprise Patterns
        description: Support for EIP patterns including routing, transformation, and mediation
  - type: UseCases
    data:
      - name: Legacy System Integration
        description: Connect legacy SOAP services with modern REST APIs
      - name: Message Routing
        description: Route JMS messages between queues and topics
      - name: Service Orchestration
        description: Orchestrate multiple services into composite workflows
      - name: Protocol Mediation
        description: Transform between HTTP, JMS, JDBC, and file protocols
  - type: Integrations
    data:
      - name: Apache Camel
        description: Core integration framework providing routing and mediation
      - name: Apache CXF
        description: SOAP and REST web service framework
      - name: Apache ActiveMQ
        description: JMS message broker for asynchronous messaging
      - name: Apache Karaf
        description: OSGi container and runtime
      - name: Spring Framework
        description: Spring integration for bean management and transactions
---
