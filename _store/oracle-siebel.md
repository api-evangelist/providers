---
aid: oracle-siebel
url: https://raw.githubusercontent.com/api-evangelist/oracle-siebel/refs/heads/main/apis.yml
apis:
- name: Oracle Siebel REST API
  description: RESTful API for accessing Siebel business objects, business services, and repository objects. The Siebel REST API supports standard CRUD operations using HTTP verbs (GET, POST, PUT, DELETE) and is compatible with OpenAPI 3.0 specifications for integration with modern applications and mobile devices.
  image: https://www.oracle.com/a/ocom/img/siebel-logo.png
  humanURL: https://docs.oracle.com/cd/E95904_01/books/RestAPI/overview-of-using-the-siebel-rest-api.html
  baseURL: https://{siebel-server}/siebel/v1.0
  tags:
  - CRM
  - Customer Management
  - Integration
  - REST
  - Sales
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/E95904_01/books/RestAPI/overview-of-using-the-siebel-rest-api.html
  - type: OpenAPI
    url: https://{siebel-server}/siebel/v1.0/swagger.json
  - type: Authentication
    url: https://docs.oracle.com/cd/F26413_26/books/Secur/single-sign-on-authentication.html
  - type: Getting Started
    url: https://docs.oracle.com/cd/E95904_01/books/RestAPI/getting-started-with-the-siebel-rest-api.html
- name: Oracle Siebel SOAP Web Services
  description: SOAP-based web services for enterprise integration with Siebel CRM, supporting complex business operations and workflows. Siebel provides both inbound web services for external clients to access Siebel functionality and outbound web services for Siebel to call external applications.
  image: https://www.oracle.com/a/ocom/img/siebel-logo.png
  humanURL: https://docs.oracle.com/cd/F26413_08/books/CRMWeb/siebel-crm-web-services-overview.html
  baseURL: https://{siebel-server}/siebel/app/soap/services
  tags:
  - CRM
  - Enterprise Integration
  - SOAP
  - Web Services
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/F26413_08/books/CRMWeb/siebel-crm-web-services-overview.html
  - type: WSDL
    url: https://{siebel-server}/siebel/app/soap/services?WSDL
  - type: Reference
    url: https://docs.oracle.com/cd/F26413_16/books/CRMWeb/crm-web-services-reference.pdf
- name: Oracle Siebel Business Service API
  description: APIs for creating and consuming custom business services within the Siebel platform for specialized business logic. Business services encapsulate reusable business logic that can be invoked through scripting, workflows, REST, or SOAP interfaces.
  image: https://www.oracle.com/a/ocom/img/siebel-logo.png
  humanURL: https://docs.oracle.com/cd/F26413_13/books/OIRef/siebel-object-interfaces-reference.html
  tags:
  - Business Services
  - Custom Logic
  - Integration
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/F26413_13/books/OIRef/siebel-object-interfaces-reference.html
- name: Oracle Siebel EAI (Enterprise Application Integration)
  description: Integration services for connecting Siebel with external systems using various protocols and data formats. Siebel EAI provides bidirectional, real-time, and batch integration solutions with pre-built adapters, enterprise connectors, and support for XML, HTTP, IBM MQSeries, and MSMQ transports.
  image: https://www.oracle.com/a/ocom/img/siebel-logo.png
  humanURL: https://docs.oracle.com/cd/F26413_25/books/EAI1/overview-of-siebel-eai.html
  tags:
  - Data Exchange
  - EAI
  - Integration
  - Middleware
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/F26413_25/books/EAI1/overview-of-siebel-eai.html
  - type: Reference
    url: https://docs.oracle.com/cd/F26413_32/books/EAI2/toc.htm
- name: Oracle Siebel Object Interfaces API
  description: Programmatic interfaces for accessing Siebel business objects, business components, and application objects using Siebel eScript, Siebel Visual Basic, or the Siebel Java Data Bean. The Object Interfaces API provides methods for querying, inserting, updating, and deleting records, as well as invoking business services and managing application state.
  image: https://www.oracle.com/a/ocom/img/siebel-logo.png
  humanURL: https://docs.oracle.com/cd/F26413_13/books/OIRef/siebel-object-interfaces-reference.html
  tags:
  - Business Components
  - Java Data Bean
  - Object Interfaces
  - Scripting
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/F26413_13/books/OIRef/siebel-object-interfaces-reference.html
  - type: Reference
    url: https://docs.oracle.com/cd/F26413_25/books/EAI3/integrating-siebel-crm-with-java-applications.html
- name: Oracle Siebel Open UI JavaScript API
  description: Client-side JavaScript API for customizing the Siebel Open UI user interface. The API provides well-defined customization points for styling, layout, and user interface design, allowing developers to integrate Siebel Open UI objects such as views and applets into third-party user interfaces and include external content in the Siebel Open UI client.
  image: https://www.oracle.com/a/ocom/img/siebel-logo.png
  humanURL: https://docs.oracle.com/cd/F26413_26/books/ConfigOpenUI/configuring-siebel-open-ui-guide.pdf
  tags:
  - Customization
  - JavaScript
  - Open UI
  - User Interface
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/F26413_26/books/ConfigOpenUI/configuring-siebel-open-ui-guide.pdf
  - type: Reference
    url: https://docs.oracle.com/cd/F26413_17/books/DeployOpenUI/features-of-siebel-open-ui.html
- name: Oracle Siebel Event Pub/Sub API
  description: Event-driven integration framework enabling real-time communication between Siebel CRM and external systems using Apache Kafka. The Event Pub/Sub API supports publishing events from Siebel to Kafka topics and consuming events from Kafka into Siebel, with support for Avro serialization, OAuth 2.0 security, and Kafka partitioning for scalability.
  image: https://www.oracle.com/a/ocom/img/siebel-logo.png
  humanURL: https://docs.oracle.com/cd/F26413_50/books/SystAdm/c-Overview-of-Siebel-CRM-Event-Publication-and-Subscription.html
  tags:
  - Event-Driven
  - Kafka
  - Pub/Sub
  - Real-Time Integration
  properties:
  - type: Documentation
    url: https://docs.oracle.com/cd/F26413_50/books/SystAdm/c-Overview-of-Siebel-CRM-Event-Publication-and-Subscription.html
name: Oracle Siebel
tags:
- CRM
- Customer Management
- Enterprise Software
- Marketing Automation
- Oracle
- Sales Automation
- Service Automation
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Oracle Siebel CRM APIs provide programmatic access to customer relationship management functionality including sales, marketing, and service automation capabilities. Siebel CRM offers REST, SOAP, scripting, and event-driven integration interfaces for building integrations with enterprise systems.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

