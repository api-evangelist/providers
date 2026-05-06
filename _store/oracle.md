---
aid: oracle
name: Oracle
description: Collection of Oracle's APIs and developer resources across cloud infrastructure, databases, AI services, SaaS applications, and platform services.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/oracle/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-04'
specificationVersion: '0.19'
tags:
  - Cloud
  - Database
  - Enterprise
  - Infrastructure
  - SaaS
apis:
  - name: Oracle Cloud Infrastructure REST API
    description: APIs for managing Oracle Cloud Infrastructure resources.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/api/
    baseURL: https://iaas.{region}.oraclecloud.com
    tags:
      - Cloud
      - IaaS
      - Infrastructure
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/api/
      - type: OpenAPI
        url: https://docs.oracle.com/en-us/iaas/api/
      - type: Authentication
        url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm
      - type: GettingStarted
        url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/usingapi.htm
      - type: SDK
        url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdks.htm
      - type: CLI
        url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cliconcepts.htm
  - name: Oracle Database REST APIs
    description: REST APIs for Oracle Autonomous Database.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en/database/oracle/oracle-database/
    baseURL: https://{host}:{port}/ords/
    tags:
      - Database
      - ORDS
      - SQL
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/
      - type: GettingStarted
        url: https://www.oracle.com/database/technologies/appdev/rest.html
      - type: APIReference
        url: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/25.3/orrst/index.html
      - type: BestPractices
        url: https://www.oracle.com/database/technologies/appdev/rest/best-practices/
      - type: FAQ
        url: https://www.oracle.com/tools/technologies/faq-rest-data-services.html
  - name: Oracle Integration Cloud API
    description: APIs for Oracle Integration Cloud services.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en/cloud/paas/integration-cloud/
    baseURL: https://{instance}.integration.ocp.oraclecloud.com
    tags:
      - Cloud
      - Integration
      - iPaaS
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/paas/integration-cloud/rest-api/
      - type: APIReference
        url: https://docs.oracle.com/en/cloud/paas/integration-cloud/integration-cloud-api/
  - name: Oracle Fusion Cloud Applications API
    description: REST APIs for Oracle Fusion Applications.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en/cloud/saas/
    baseURL: https://{instance}.oraclecloud.com
    tags:
      - CX
      - ERP
      - HCM
      - SaaS
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/applications-common/
      - type: APIReference
        url: https://docs.oracle.com/en/cloud/saas/index.html
  - name: Oracle Fusion Cloud Financials REST API
    description: REST APIs for viewing and managing data stored in Oracle Fusion Cloud Financials, including ERP processes, integrations, payables, receivables, general ledger, and fixed assets.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
    baseURL: https://{instance}.fa.{region}.oraclecloud.com
    tags:
      - Accounting
      - ERP
      - Financials
      - SaaS
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/financials/26a/farfa/index.html
      - type: APIReference
        url: https://docs.oracle.com/en/cloud/saas/financials/24c/farfa/rest-endpoints.html
      - type: GettingStarted
        url: https://docs.oracle.com/en/cloud/saas/financials/25a/farfa/Quick_Start.html
  - name: Oracle Fusion Cloud HCM REST API
    description: REST APIs for viewing and managing human capital management data including workers, talent management, payroll, recruiting, benefits, and workforce compensation in Oracle Fusion Cloud HCM.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en/cloud/saas/human-resources/farws/index.html
    baseURL: https://{instance}.fa.{region}.oraclecloud.com/hcmRestApi
    tags:
      - HCM
      - Human Resources
      - Payroll
      - SaaS
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/human-resources/farws/index.html
      - type: APIReference
        url: https://docs.oracle.com/en/cloud/saas/human-resources/24d/farws/rest-endpoints.html
      - type: GettingStarted
        url: https://docs.oracle.com/en/cloud/saas/human-resources/22b/farws/Quick_Start.html
  - name: Oracle Fusion Cloud CX Sales and Service REST API
    description: REST APIs for managing sales and service data in Oracle Fusion Cloud Customer Experience, including accounts, contacts, opportunities, leads, cases, interactions, and service requests.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en/cloud/saas/sales/faaps/index.html
    baseURL: https://{instance}.fa.{region}.oraclecloud.com/crmRestApi
    tags:
      - CX
      - SaaS
      - Sales
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/sales/faaps/index.html
      - type: APIReference
        url: https://docs.oracle.com/en/cloud/saas/sales/faaps/rest-endpoints.html
      - type: GettingStarted
        url: https://docs.oracle.com/en/cloud/saas/sales/21a/faaps/Quick_Start.html
  - name: Oracle Fusion Cloud SCM REST API
    description: REST APIs for viewing and managing supply chain management data in Oracle Fusion Cloud SCM, including inventory, manufacturing, order management, procurement, and logistics.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/24b/fasrp/index.html
    baseURL: https://{instance}.fa.{region}.oraclecloud.com/fscmRestApi
    tags:
      - Manufacturing
      - SaaS
      - SCM
      - Supply Chain
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/24b/fasrp/index.html
      - type: APIReference
        url: https://docs.oracle.com/en/cloud/saas/supply-chain-and-manufacturing/24c/fasrp/rest-endpoints.html
  - name: Oracle Fusion Cloud Procurement REST API
    description: REST APIs for managing procurement data in Oracle Fusion Cloud including purchase orders, purchase requisitions, suppliers, sourcing, and change orders.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en/cloud/saas/procurement/26a/fapra/index.html
    baseURL: https://{instance}.fa.{region}.oraclecloud.com/fscmRestApi
    tags:
      - Procurement
      - Purchasing
      - SaaS
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/procurement/26a/fapra/index.html
      - type: APIReference
        url: https://docs.oracle.com/en/cloud/saas/procurement/26a/fapra/rest-endpoints.html
  - name: Oracle Content Management API
    description: REST APIs for Oracle Content Management.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en/cloud/paas/content-cloud/
    baseURL: https://{instance}.ocecdn.oraclecloud.com
    tags:
      - CMS
      - Content Management
      - Digital Assets
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/paas/content-cloud/rest-api-documents/
      - type: SDK
        url: https://www.oracle.com/content-management/developers/
  - name: OCI Generative AI API
    description: Fully managed service providing customizable large language models for chat, text generation, summarization, reranking, and text embeddings, accessible via REST API and SDKs.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm
    baseURL: https://generativeai.{region}.oci.oraclecloud.com
    tags:
      - Artificial Intelligence
      - Generative AI
      - LLM
      - Machine Learning
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/generative-ai/home.htm
      - type: GettingStarted
        url: https://docs.oracle.com/en-us/iaas/Content/generative-ai/overview.htm
      - type: Authentication
        url: https://docs.oracle.com/en-us/iaas/Content/generative-ai/api-keys.htm
  - name: OCI AI Vision API
    description: Serverless AI service for image analysis and document understanding, supporting object detection, image classification, text recognition, and document analysis via pretrained and custom models.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/vision/using/overview.htm
    baseURL: https://vision.aiservice.{region}.oci.oraclecloud.com
    tags:
      - Artificial Intelligence
      - Computer Vision
      - Document AI
      - Image Analysis
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/vision/using/overview.htm
      - type: GettingStarted
        url: https://docs.oracle.com/en-us/iaas/Content/vision/using/api_models.htm
  - name: OCI AI Language API
    description: Serverless cloud AI service for sophisticated text analysis at scale, including sentiment analysis, named entity recognition, key phrase extraction, language detection, text classification, translation, and PII detection.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/language/using/overview.htm
    baseURL: https://language.aiservice.{region}.oci.oraclecloud.com
    tags:
      - Artificial Intelligence
      - Natural Language Processing
      - Sentiment Analysis
      - Text Analysis
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/language/using/overview.htm
  - name: OCI AI Speech API
    description: AI service for converting audio and media files to accurate text transcriptions in JSON and SRT formats using automatic speech recognition, with support for real-time transcription, speaker diarization, and text-to-speech synthesis.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/speech/using/speech.htm
    baseURL: https://speech.aiservice.{region}.oci.oraclecloud.com
    tags:
      - Artificial Intelligence
      - Speech Recognition
      - Text to Speech
      - Transcription
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/speech/using/speech.htm
  - name: OCI API Gateway
    description: Service for creating managed API gateways that publish APIs with private or public endpoints, routing traffic from API clients to back-end services with authentication, rate limiting, CORS, and request transformation.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Concepts/apigatewayoverview.htm
    baseURL: https://apigateway.{region}.oci.oraclecloud.com
    tags:
      - API Management
      - Cloud
      - Gateway
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/APIGateway/home.htm
      - type: GettingStarted
        url: https://docs.oracle.com/en-us/iaas/Content/APIGateway/Tasks/apigatewaycreatinggateway.htm
  - name: OCI Container Engine for Kubernetes API
    description: Fully managed Kubernetes service for deploying and managing containerized applications, supporting virtual nodes for serverless operation, managed nodes, and self-managed nodes with GPU and high-performance networking.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengoverview.htm
    baseURL: https://containerengine.{region}.oci.oraclecloud.com
    tags:
      - Cloud Native
      - Containers
      - Kubernetes
      - Orchestration
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengoverview.htm
      - type: GettingStarted
        url: https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengclustersnodes.htm
  - name: OCI Functions API
    description: Fully managed, serverless Functions-as-a-Service platform built on the open source Fn Project engine, supporting Java, Python, Node, Go, Ruby, C#, and custom Docker containers with automatic scaling and pay-per-use pricing.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/functionsoverview.htm
    baseURL: https://functions.{region}.oci.oraclecloud.com
    tags:
      - Cloud Native
      - FaaS
      - Functions
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/functionsoverview.htm
  - name: OCI DevOps API
    description: End-to-end CI/CD platform for building, testing, and deploying software on Oracle Cloud, with private Git repositories, build pipelines, and deployment strategies including blue-green and canary deployments.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/devops/using/devops_overview.htm
    baseURL: https://devops.{region}.oci.oraclecloud.com
    tags:
      - Build
      - CI/CD
      - Deployment
      - DevOps
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/devops/using/devops_overview.htm
      - type: GettingStarted
        url: https://docs.oracle.com/en-us/iaas/Content/devops/using/getting_started.htm
  - name: OCI Data Science API
    description: Fully managed serverless platform for data science teams to build, train, deploy, and manage machine learning models with notebook sessions, jobs, pipelines, and model deployment as HTTP endpoints.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/data-science/using/overview.htm
    baseURL: https://datascience.{region}.oci.oraclecloud.com
    tags:
      - AI
      - Data Science
      - Machine Learning
      - Model Deployment
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/data-science/using/overview.htm
  - name: Oracle Analytics Cloud REST API
    description: REST APIs for automating processes and programmatically accessing Oracle Analytics Cloud features including workbooks, datasets, data flows, connections, snapshots, and semantic models.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en/cloud/paas/analytics-cloud/acapi/index.html
    baseURL: https://{instance}.analytics.ocp.oraclecloud.com
    tags:
      - Analytics
      - Business Intelligence
      - Data Visualization
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/paas/analytics-cloud/acapi/index.html
      - type: APIReference
        url: https://docs.oracle.com/en/cloud/paas/analytics-cloud/acapi/rest-endpoints.html
      - type: GettingStarted
        url: https://docs.oracle.com/en/cloud/paas/analytics-cloud/acapi/quick-start.html
  - name: Oracle Digital Assistant REST API
    description: REST APIs for managing Oracle Digital Assistant instances, skills, digital assistants, channels, conversation logs, and dynamic entities for building conversational AI experiences.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en/cloud/paas/digital-assistant/
    baseURL: https://{instance}.digitalassistant.oci.oraclecloud.com
    tags:
      - Chatbot
      - Conversational AI
      - Digital Assistant
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/paas/digital-assistant/rest-api-oci/index.html
      - type: SDK
        url: https://docs.oracle.com/en/cloud/paas/digital-assistant/sdks.html
  - name: OCI Identity and Access Management API
    description: REST APIs for managing identities, groups, policies, and access to Oracle Cloud Infrastructure resources, including SCIM 2.0 compliant identity domain endpoints for user and application management.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/overview.htm
    baseURL: https://identity.{region}.oci.oraclecloud.com
    tags:
      - Access Management
      - IAM
      - Identity
      - Security
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/overview.htm
      - type: APIReference
        url: https://docs.oracle.com/en/cloud/paas/iam-domains-rest-api/index.html
      - type: GettingStarted
        url: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-get-started.htm
  - name: OCI Object Storage API
    description: REST APIs for managing scalable and durable object storage in Oracle Cloud Infrastructure, including bucket management, object upload and download, multipart uploads, and pre-authenticated requests.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorageoverview.htm
    baseURL: https://objectstorage.{region}.oraclecloud.com
    tags:
      - Cloud
      - Object Storage
      - Storage
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorageoverview.htm
  - name: OCI Monitoring API
    description: APIs for actively and passively monitoring cloud resources using metrics and alarms, with support for custom metrics, metric aggregation, and alarm notifications across 80+ OCI services.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm
    baseURL: https://telemetry.{region}.oci.oraclecloud.com
    tags:
      - Alarms
      - Metrics
      - Monitoring
      - Observability
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Monitoring/Concepts/monitoringoverview.htm
  - name: OCI Notifications API
    description: Publish and subscribe messaging service for setting up communication channels using topics and subscriptions, delivering messages via email, SMS, HTTPS endpoints, Slack, PagerDuty, and OCI Functions.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/notificationoverview.htm
    baseURL: https://notification.{region}.oci.oraclecloud.com
    tags:
      - Messaging
      - Notifications
      - Pub/Sub
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Notification/Concepts/notificationoverview.htm
  - name: OCI Streaming API
    description: Managed messaging service for ingesting and consuming high-volume data streams in real time, compatible with the Apache Kafka API for seamless integration with existing Kafka applications.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/accessing-streaming.htm
    baseURL: https://streaming.{region}.oci.oraclecloud.com
    tags:
      - Event Streaming
      - Kafka
      - Messaging
      - Streaming
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Streaming/Concepts/accessing-streaming.htm
  - name: OCI Queue API
    description: Serverless messaging service for decoupling application components with reliable message delivery, supporting RESTful API with Open API specification and STOMP protocol for publishing and consuming messages.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/queue/overview.htm
    baseURL: https://queue.{region}.oci.oraclecloud.com
    tags:
      - Messaging
      - Queue
      - Serverless
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/queue/overview.htm
  - name: OCI Vault API
    description: APIs for managing encryption keys and secrets to securely access Oracle Cloud Infrastructure resources, with support for hardware security modules, external key management, and secret lifecycle management.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/keyoverview.htm
    baseURL: https://kms.{region}.oraclecloud.com
    tags:
      - Encryption
      - Key Management
      - Secrets
      - Security
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/keyoverview.htm
  - name: OCI Logging API
    description: APIs for centralized log management across Oracle Cloud Infrastructure, enabling ingestion, search, and analysis of logs from OCI resources, custom applications, and on-premises environments.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/loggingoverview.htm
    baseURL: https://logging.{region}.oci.oraclecloud.com
    tags:
      - Log Management
      - Logging
      - Observability
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/loggingoverview.htm
      - type: APIReference
        url: https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/using_the_api_searchlogs.htm
  - name: OCI Autonomous Database REST API
    description: REST APIs for provisioning, managing, and operating Oracle Autonomous Databases including serverless and dedicated infrastructure options, with built-in Oracle REST Data Services for developing RESTful services.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/rest-apis.html
    baseURL: https://database.{region}.oraclecloud.com
    tags:
      - Autonomous Database
      - Cloud
      - Database
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/rest-apis.html
      - type: GettingStarted
        url: https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/ords-autonomous-database.html
  - name: OCI MySQL HeatWave API
    description: APIs for managing MySQL Database Service with HeatWave in-memory query accelerator on Oracle Cloud Infrastructure, supporting database system provisioning, backups, and REST endpoint configuration.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/mysql-database/doc/overview-mysql-heatwave-service.html
    baseURL: https://mysql.{region}.oraclecloud.com
    tags:
      - Database
      - HeatWave
      - MySQL
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/mysql-database/home.htm
      - type: GettingStarted
        url: https://docs.oracle.com/en-us/iaas/mysql-database/doc/getting-started-mysql-heatwave-service.html
  - name: OCI Events API
    description: APIs for tracking resource changes across Oracle Cloud Infrastructure by defining rules that match emitted events and triggering actions such as invoking functions, publishing to streams, or sending notifications.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/Events/Concepts/eventsoverview.htm
    baseURL: https://events.{region}.oci.oraclecloud.com
    tags:
      - Automation
      - Cloud
      - Events
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Events/Concepts/eventsoverview.htm
  - name: OCI Logging Analytics API
    description: Cloud-based log analytics service for indexing, enriching, and aggregating log data from applications and infrastructure, with machine learning powered insights and REST API based log collection from endpoint URLs.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/logging-analytics/index.html
    baseURL: https://loganalytics.{region}.oci.oraclecloud.com
    tags:
      - Analytics
      - Log Management
      - Logging
      - Observability
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/logging-analytics/index.html
      - type: GettingStarted
        url: https://docs.oracle.com/en-us/iaas/logging-analytics/doc/set-rest-api-log-collection.html
  - name: Oracle Cloud Infrastructure Process Automation API
    description: REST APIs for automating business processes in Oracle Cloud Infrastructure, enabling workflow design, task management, and process orchestration.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en/cloud/paas/process-automation/rest-api-proca/index.html
    baseURL: https://{instance}.process.oci.oraclecloud.com
    tags:
      - BPM
      - Process Automation
      - Workflow
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/paas/process-automation/rest-api-proca/index.html
  - name: OCI Compute API
    description: REST APIs for managing compute instances in Oracle Cloud Infrastructure, including launching, managing, and terminating virtual machine and bare metal instances, managing instance configurations, pools, and custom images.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/computeoverview.htm
    baseURL: https://iaas.{region}.oraclecloud.com
    tags:
      - Bare Metal
      - Cloud
      - Compute
      - Virtual Machines
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/computeoverview.htm
      - type: APIReference
        url: https://docs.oracle.com/en-us/iaas/api/
      - type: OpenAPI
        url: openapi/oci-compute-api-openapi.yml
      - type: JSONSchema
        url: json-schema/oracle-compute-instance-schema.json
      - type: JSONLD
        url: json-ld/oracle-context.jsonld
  - name: OCI Networking API
    description: REST APIs for managing virtual cloud networks, subnets, security lists, route tables, internet gateways, NAT gateways, service gateways, and other networking resources in Oracle Cloud Infrastructure.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm
    baseURL: https://iaas.{region}.oraclecloud.com
    tags:
      - Cloud
      - Infrastructure
      - Networking
      - VCN
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm
      - type: APIReference
        url: https://docs.oracle.com/en-us/iaas/api/
  - name: OCI Block Volume API
    description: REST APIs for provisioning and managing block storage volumes that can be attached to compute instances, including volume backups, volume groups, boot volumes, and cross-region replication.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm
    baseURL: https://iaas.{region}.oraclecloud.com
    tags:
      - Block Volume
      - Cloud
      - Storage
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm
      - type: APIReference
        url: https://docs.oracle.com/en-us/iaas/api/
  - name: OCI File Storage API
    description: REST APIs for managing durable, scalable, and secure network file systems that can be connected to from any compute instance in a virtual cloud network, supporting NFS protocol and snapshots.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/File/Concepts/filestorageoverview.htm
    baseURL: https://filestorage.{region}.oraclecloud.com
    tags:
      - Cloud
      - File Storage
      - NFS
      - Storage
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/File/Concepts/filestorageoverview.htm
      - type: APIReference
        url: https://docs.oracle.com/en-us/iaas/api/
  - name: OCI Load Balancer API
    description: REST APIs for managing load balancers that distribute traffic across backend servers, supporting HTTP, HTTPS, and TCP protocols with features including SSL termination, session persistence, and health checks.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/balanceoverview.htm
    baseURL: https://iaas.{region}.oraclecloud.com
    tags:
      - Cloud
      - Load Balancer
      - Networking
      - Traffic Management
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Balance/Concepts/balanceoverview.htm
      - type: APIReference
        url: https://docs.oracle.com/en-us/iaas/api/
  - name: OCI DNS API
    description: REST APIs for managing DNS zones, records, steering policies, and resolvers in Oracle Cloud Infrastructure, with support for DNSSEC, traffic management, and health checks.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm
    baseURL: https://dns.{region}.oci.oraclecloud.com
    tags:
      - Cloud
      - DNS
      - Networking
      - Traffic Management
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm
      - type: APIReference
        url: https://docs.oracle.com/en-us/iaas/api/
  - name: OCI Web Application Firewall API
    description: REST APIs for managing web application firewall policies that protect applications from malicious and unwanted internet traffic, supporting protection against SQL injection, cross-site scripting, and other OWASP threats.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/overview.htm
    baseURL: https://waf.{region}.oci.oraclecloud.com
    tags:
      - Cloud
      - Firewall
      - Security
      - WAF
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/WAF/Concepts/overview.htm
      - type: GettingStarted
        url: https://docs.oracle.com/en-us/iaas/Content/WAF/Policies/getting_started_with_waf-policies.htm
  - name: OCI Email Delivery API
    description: REST APIs for sending high-volume and application-generated emails through Oracle Cloud Infrastructure, with support for SMTP and HTTPS submission, email domain management, DKIM configuration, and suppression lists.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/Email/Concepts/overview.htm
    baseURL: https://email.{region}.oci.oraclecloud.com
    tags:
      - Cloud
      - Email
      - Messaging
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Email/home.htm
      - type: GettingStarted
        url: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/gettingstarted_topic-Begin_sending_email.htm
  - name: OCI Container Registry API
    description: REST APIs for managing Docker container images in Oracle Cloud Infrastructure Container Registry, a managed Docker v2 compliant registry service for storing, sharing, and managing container images.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registryoverview.htm
    baseURL: https://ocir.{region}.oci.oraclecloud.com
    tags:
      - Cloud Native
      - Containers
      - Docker
      - Registry
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Registry/Concepts/registryoverview.htm
      - type: APIReference
        url: https://docs.oracle.com/en-us/iaas/api/
  - name: OCI Data Integration API
    description: REST APIs for organizing data integration projects, creating data flows, pipelines, and tasks to extract, transform, and load data across cloud and on-premises data sources.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/data-integration/home.htm
    baseURL: https://dataintegration.{region}.oci.oraclecloud.com
    tags:
      - Cloud
      - Data Integration
      - Data Pipeline
      - ETL
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/data-integration/home.htm
  - name: OCI Data Flow API
    description: REST APIs for running Apache Spark applications at any scale without deploying or managing infrastructure, with fully managed Spark clusters for batch processing, streaming, and machine learning workloads.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/data-flow/using/home.htm
    baseURL: https://dataflow.{region}.oci.oraclecloud.com
    tags:
      - Apache Spark
      - Big Data
      - Cloud
      - Data Processing
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/data-flow/using/home.htm
  - name: OCI Data Catalog API
    description: REST APIs for managing a metadata catalog of data assets, enabling data discovery, governance, and understanding of data lineage across Oracle Cloud and external data sources.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/data-catalog/home.htm
    baseURL: https://datacatalog.{region}.oci.oraclecloud.com
    tags:
      - Cloud
      - Data Catalog
      - Data Governance
      - Metadata
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/data-catalog/home.htm
      - type: GettingStarted
        url: https://docs.oracle.com/en-us/iaas/Content/data-catalog/using/setup-source.htm
  - name: OCI Search with OpenSearch API
    description: REST APIs for managing OCI Search Service with OpenSearch, a managed service for building in-application search solutions enabling full-text search, log analytics, and real-time application monitoring.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/search-opensearch/home.htm
    baseURL: https://search-opensearch.{region}.oci.oraclecloud.com
    tags:
      - Cloud
      - Full-Text Search
      - OpenSearch
      - Search
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/search-opensearch/home.htm
  - name: OCI Resource Manager API
    description: REST APIs for automating infrastructure provisioning using Terraform configurations in Oracle Cloud Infrastructure, with support for stacks, jobs, drift detection, and resource discovery.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm
    baseURL: https://resourcemanager.{region}.oci.oraclecloud.com
    tags:
      - Automation
      - Cloud
      - Infrastructure as Code
      - Terraform
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm
      - type: APIReference
        url: https://docs.oracle.com/en-us/iaas/api/
  - name: OCI Bastion API
    description: REST APIs for managing bastion sessions that provide restricted and time-limited access to target resources in private subnets that cannot otherwise be reached from the internet.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en-us/iaas/Content/Bastion/Concepts/bastionoverview.htm
    baseURL: https://bastion.{region}.oci.oraclecloud.com
    tags:
      - Access Control
      - Bastion
      - Cloud
      - Security
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en-us/iaas/Content/Bastion/Concepts/bastionoverview.htm
      - type: APIReference
        url: https://docs.oracle.com/en-us/iaas/api/
  - name: Oracle APEX REST API
    description: REST APIs for Oracle Application Express (APEX), a low-code development platform for building scalable and secure enterprise applications with RESTful web services and REST-enabled SQL.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en/cloud/paas/apex/rest-apis.html
    baseURL: https://{instance}.adb.{region}.oraclecloudapps.com/ords
    tags:
      - APEX
      - Application Development
      - Low-Code
      - REST
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/paas/apex/rest-apis.html
      - type: APIReference
        url: https://apex.oracle.com/api/
  - name: Oracle Visual Builder REST API
    description: REST APIs for managing Oracle Visual Builder resources including applications, business objects, data import and export, and tenant-level credentials for building web and mobile applications.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en/cloud/paas/app-builder-cloud/vb-rest-apis/index.html
    baseURL: https://{instance}.builder.ocp.oraclecloud.com
    tags:
      - Application Development
      - Cloud
      - Low-Code
      - Visual Builder
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/paas/app-builder-cloud/vb-rest-apis/index.html
  - name: Oracle CX for Industries API
    description: REST APIs and schema documentation for Oracle Customer Experience for Industries, providing industry-specific solutions for communications, media, utilities, and financial services.
    image: https://www.oracle.com/asset/web/favicons/favicon-192.png
    humanURL: https://docs.oracle.com/en/cloud/saas/industries/api.html
    baseURL: https://{instance}.oraclecloud.com
    tags:
      - CX
      - Industries
      - SaaS
    properties:
      - type: Documentation
        url: https://docs.oracle.com/en/cloud/saas/industries/api.html
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Portal
    url: https://developer.oracle.com
  - type: DeveloperPortal
    url: https://developer.oracle.com
  - type: Documentation
    url: https://docs.oracle.com/
  - type: Blog
    url: https://blogs.oracle.com/
  - type: Support
    url: https://www.oracle.com/support/
  - type: StatusPage
    url: https://ocistatus.oraclecloud.com/
  - type: TermsOfService
    url: https://www.oracle.com/legal/terms.html
  - type: PrivacyPolicy
    url: https://www.oracle.com/legal/privacy/
  - type: GettingStarted
    url: https://docs.oracle.com/en-us/iaas/Content/GSG/Concepts/baremetalintro.htm
  - type: SDK
    url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdks.htm
  - type: GitHubOrganization
    url: https://github.com/oracle
  - type: SignUp
    url: https://www.oracle.com/cloud/free/
  - type: Login
    url: https://www.oracle.com/cloud/sign-in.html
  - type: Pricing
    url: https://www.oracle.com/cloud/compute/pricing/
  - type: ReleaseNotes
    url: https://docs.oracle.com/en-us/iaas/releasenotes/
  - type: ChangeLog
    url: https://docs.oracle.com/en-us/iaas/Content/servicechanges.htm
  - type: Authentication
    url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/apisigningkey.htm
  - type: CLI
    url: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/cliconcepts.htm
  - type: Console
    url: https://cloud.oracle.com
  - type: YouTube
    url: https://www.youtube.com/user/Oracle
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/oracle-cloud-infrastructure
  - type: OpenAPI
    url: openapi/oci-compute-api-openapi.yml
  - type: JSONSchema
    url: json-schema/oracle-compute-instance-schema.json
  - type: JSONLD
    url: json-ld/oracle-context.jsonld
  - type: SpectralRules
    url: rules/oracle-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/oracle-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/cloud-compute.yaml
  - type: Features
    data:
      - 'Oracle (OCI + Database + Apps): hundreds of services across Cloud + Database + ERP'
      - 'Detailed pricing: see https://www.oracle.com/cloud/price-list/'
      - 'Service: Oracle Cloud Infrastructure (OCI) Compute'
      - 'Service: OCI Object Storage'
      - 'Service: OCI Block Storage'
      - 'Service: Autonomous Database'
      - 'Service: Oracle Database (cloud and on-prem)'
      - 'Service: Exadata Cloud'
      - 'Service: OCI Functions'
      - 'Service: OCI Container Engine'
      - 'Service: OCI API Gateway'
      - 'Service: Fusion Cloud Apps (ERP, HCM, SCM, CX)'
      - 'Service: NetSuite ERP'
      - 'Service: Oracle Generative AI'
      - 'Service: OCI Speech / Vision / Document Understanding'
    sources:
      - https://www.oracle.com/cloud/price-list/
      - https://focus.finops.org/
    updated: '2026-05-04'
  - type: UseCases
    data:
      - Migrating enterprise workloads to Oracle Cloud Infrastructure
      - Building and deploying AI-powered applications with OCI AI services
      - Automating financial and procurement processes with Fusion Cloud
      - Managing human capital and payroll with HCM REST APIs
      - Running big data analytics with Data Flow and Data Science
      - Building low-code applications with APEX and Visual Builder
      - Monitoring and observability across cloud infrastructure
      - Securing applications with WAF, IAM, and Vault services
  - type: Integrations
    data:
      - Terraform for infrastructure as code provisioning
      - Apache Kafka compatibility via OCI Streaming
      - Docker and Kubernetes for containerized workloads
      - Apache Spark via OCI Data Flow
      - OpenSearch for full-text search and log analytics
      - Slack and PagerDuty via OCI Notifications
      - SCIM 2.0 for identity management integration
      - REST Data Services (ORDS) for database API access
---
