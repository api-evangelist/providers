---
aid: websphere
url: https://raw.githubusercontent.com/api-evangelist/websphere/refs/heads/main/apis.yml
apis:
- name: WebSphere Application Server Admin API
  description: REST API for administrative operations on WebSphere Application Server including deployment, configuration, and monitoring. Starting with version 9.0.0.1, Swagger documentation can be discovered and exposed for deployed RESTful endpoints.
  image: https://www.ibm.com/brand/experience-guides/developer/b1db1ae501d522a1a4b49613fe07c9f4/01_8-bar-positive.svg
  baseURL: https://localhost:9443/ibm/api
  humanURL: https://www.ibm.com/docs/en/was
  tags:
  - Administration
  - Configuration
  - Deployment
  - Monitoring
  properties:
  - type: Documentation
    url: https://www.ibm.com/docs/en/was/9.0.5?topic=overview-administrative-rest-api
  - type: OpenAPI
    url: https://www.ibm.com/docs/en/was/9.0.5?topic=api-openapi-specification
  - type: OpenAPI
    url: openapi/websphere-admin-rest-api.yml
  - type: Authentication
    url: https://www.ibm.com/docs/en/was/9.0.5?topic=api-authentication-authorization
  - type: Getting Started
    url: https://www.ibm.com/docs/en/was-nd/9.0.5?topic=specifications-discovering-rest-api-documentation
  - type: Reference
    url: https://www.ibm.com/docs/en/was/9.0.5?topic=javadoc-apis-application-programming-interfaces
  - type: JSONSchema
    url: json-schema/application.json
  - type: JSONSchema
    url: json-schema/server.json
  - type: JSONSchema
    url: json-schema/cluster.json
  - type: JSONLD
    url: json-ld/context.jsonld
- name: WebSphere Liberty Admin REST API
  description: RESTful administrative API for WebSphere Liberty servers, providing configuration and runtime management capabilities. The Admin REST Connector enables secure remote access through HTTPS calls or Java clients.
  baseURL: https://localhost:9443/ibm/api
  humanURL: https://www.ibm.com/docs/en/was-liberty
  tags:
  - Administration
  - Configuration
  - Liberty
  - Rest Api
  properties:
  - type: Documentation
    url: https://www.ibm.com/docs/en/was-liberty/base?topic=liberty-admin-rest-api
  - type: Swagger
    url: https://localhost:9443/ibm/api/docs
  - type: OpenAPI
    url: openapi/websphere-liberty-admin-rest-api.yml
  - type: Getting Started
    url: https://www.ibm.com/docs/en/was-liberty/base?topic=api-getting-started
  - type: Reference
    url: https://openliberty.io/docs/latest/reference/feature/restConnector-2.0.html
  - type: Documentation
    url: https://www.ibm.com/docs/en/was-liberty/base?topic=center-setting-up-admin
  - type: JSONSchema
    url: json-schema/application.json
  - type: JSONSchema
    url: json-schema/server.json
  - type: JSONLD
    url: json-ld/context.jsonld
- name: WebSphere Liberty REST Connector API
  description: Secure REST-based JMX connector for remote administration of Liberty servers. Provides file transfer and JMX MBean access through HTTPS endpoints, requiring TLS for confidential communication.
  baseURL: https://localhost:9443/IBMJMXConnectorREST/api
  humanURL: https://openliberty.io/docs/latest/reference/feature/restConnector-2.0.html
  tags:
  - Jmx
  - Liberty
  - Remote Administration
  - Rest Connector
  properties:
  - type: Documentation
    url: https://openliberty.io/docs/latest/reference/feature/restConnector-2.0.html
  - type: OpenAPI
    url: openapi/websphere-liberty-rest-connector-api.yml
  - type: Reference
    url: https://openliberty.io/docs/latest/reference/api/open-liberty-apis.html
  - type: Documentation
    url: https://openliberty.io/docs/latest/configuring-jmx-connection.html
  - type: Documentation
    url: https://www.ibm.com/docs/en/was-liberty/core?topic=features-admin-rest-connector-20
  - type: JSONLD
    url: json-ld/context.jsonld
- name: WebSphere MQ REST API
  description: REST API for IBM MQ messaging operations including sending and receiving messages, queue management, and monitoring. Supports both administration and messaging endpoints for point-to-point and publish-subscribe patterns.
  baseURL: https://localhost:9443/ibmmq/rest/v2
  humanURL: https://www.ibm.com/docs/en/ibm-mq
  tags:
  - Integration
  - Messaging
  - Publish Subscribe
  - Queue Management
  properties:
  - type: Documentation
    url: https://www.ibm.com/docs/en/ibm-mq/9.3?topic=api-rest-introduction
  - type: OpenAPI
    url: openapi/websphere-mq-rest-api.yml
  - type: Reference
    url: https://www.ibm.com/docs/en/ibm-mq/9.3?topic=api-rest-reference
  - type: Authentication
    url: https://www.ibm.com/docs/en/ibm-mq/9.3?topic=api-rest-authentication
  - type: Getting Started
    url: https://developer.ibm.com/tutorials/mq-develop-mq-rest-api/
  - type: Documentation
    url: https://www.ibm.com/docs/en/ibm-mq/9.3?topic=mq-messaging-using-rest-api
  - type: JSONSchema
    url: json-schema/message-queue.json
  - type: JSONLD
    url: json-ld/context.jsonld
- name: WebSphere Application Server JMX API
  description: Java Management Extensions (JMX) API for programmatic management and monitoring of WebSphere Application Server. Provides MBean access for server configuration, performance monitoring, and resource management.
  baseURL: service:jmx:rmi:///jndi/rmi://localhost:2809/jmxrmi
  humanURL: https://www.ibm.com/docs/en/was
  tags:
  - Jmx
  - Management
  - Mbeans
  - Monitoring
  properties:
  - type: Documentation
    url: https://www.ibm.com/docs/en/was/9.0.5?topic=api-using-jmx
  - type: Reference
    url: https://www.ibm.com/docs/en/was/9.0.5?topic=reference-javadoc
  - type: Documentation
    url: https://www.ibm.com/docs/en/was/9.0.5?topic=api-jmx-examples
  - type: JSONSchema
    url: json-schema/server.json
  - type: JSONLD
    url: json-ld/context.jsonld
- name: WebSphere Liberty Collective Controller REST API
  description: API for managing Liberty collective environments, including member management, scaling, and centralized administration. Supports subscription-based notifications for API changes across collective members.
  baseURL: https://localhost:9443/ibm/api/collective
  humanURL: https://www.ibm.com/docs/en/was-liberty
  tags:
  - Clustering
  - Collective
  - Liberty
  - Management
  properties:
  - type: Documentation
    url: https://www.ibm.com/docs/en/was-liberty/base?topic=liberty-collective-rest-api
  - type: OpenAPI
    url: openapi/websphere-liberty-collective-controller-rest-api.yml
  - type: Reference
    url: https://www.ibm.com/docs/en/was-liberty/base?topic=api-collective-reference
  - type: Documentation
    url: https://www.ibm.com/docs/en/was-liberty/base?topic=deploying-applications-in-liberty
  - type: JSONSchema
    url: json-schema/cluster.json
  - type: JSONSchema
    url: json-schema/server.json
  - type: JSONLD
    url: json-ld/context.jsonld
- name: WebSphere Automation REST API
  description: API for WebSphere Automation capabilities including vulnerability management, automated patching, and health monitoring. Accessible through the Swagger UI on OpenShift Container Platform deployments.
  baseURL: https://automation-api.example.com/v1
  humanURL: https://www.ibm.com/docs/en/ws-automation
  tags:
  - Automation
  - Health Monitoring
  - Patching
  - Vulnerability Management
  properties:
  - type: Documentation
    url: https://www.ibm.com/docs/en/ws-automation?topic=apis
  - type: OpenAPI
    url: openapi/websphere-automation-rest-api.yml
  - type: Reference
    url: https://www.ibm.com/docs/en/ws-automation?topic=reference-rest-api
  - type: Documentation
    url: https://www.ibm.com/docs/en/ws-automation?topic=viewing-rest-api
  - type: JSONSchema
    url: json-schema/server.json
  - type: JSONLD
    url: json-ld/context.jsonld
- name: Open Liberty APIs
  description: Open Liberty provides application programming interfaces that extend and complement Jakarta EE and MicroProfile APIs. Includes APIs for security, admin connectors, batch processing, messaging, and more.
  baseURL: https://localhost:9443/ibm/api
  humanURL: https://openliberty.io/docs/latest/reference/api/open-liberty-apis.html
  tags:
  - Cloud Native
  - Jakarta Ee
  - Microprofile
  - Open Liberty
  properties:
  - type: Documentation
    url: https://openliberty.io/docs/latest/reference/api/open-liberty-apis.html
  - type: OpenAPI
    url: openapi/open-liberty-apis.yml
  - type: Reference
    url: https://openliberty.io/docs/latest/documentation-openapi.html
  - type: Getting Started
    url: https://openliberty.io/guides/rest-intro.html
  - type: Documentation
    url: https://openliberty.io/docs/latest/microprofile.html
  - type: Blog
    url: https://openliberty.io/blog/
  - type: JSONSchema
    url: json-schema/application.json
  - type: JSONSchema
    url: json-schema/server.json
  - type: JSONLD
    url: json-ld/context.jsonld
name: IBM WebSphere
tags:
- Application Server
- Cloud Native
- Enterprise Java
- J2EE
- Microservices
- Middleware
type: Contract
image: https://www.ibm.com/brand/experience-guides/developer/b1db1ae501d522a1a4b49613fe07c9f4/01_8-bar-positive.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: IBM WebSphere is a family of enterprise software products that provide middleware and application server capabilities for building, deploying, and managing enterprise applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

