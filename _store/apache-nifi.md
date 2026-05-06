---
aid: apache-nifi
name: Apache NiFi
description: Apache NiFi is a dataflow management system designed to automate the flow of data between systems. It provides a web-based user interface for designing, controlling, and monitoring data flows with real-time operational control, data provenance tracking, and support for hundreds of processors. NiFi Version 2 is the current major version with enhanced security and performance.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Integration
  - Dataflow
  - ETL
  - IoT
  - Streaming
  - Data Pipeline
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-nifi/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-nifi:apache-nifi-rest-api
    name: Apache NiFi REST API
    description: The NiFi REST API provides comprehensive JWT-authenticated endpoints for managing processors, connections, controller services, process groups, reporting tasks, provenance, flow versions, system diagnostics, access control, parameter contexts, and data transfer. Base URL is http://nifi-host:8080/nifi-api. OpenAPI spec available at /nifi-docs/swagger.yaml.
    humanURL: https://nifi.apache.org/components/
    tags:
      - Dataflow
      - Flow Management
      - REST
      - JWT
    properties:
      - type: Documentation
        url: https://nifi.apache.org/components/
      - type: OpenAPI
        url: https://nifi.apache.org/nifi-docs/swagger.yaml
      - type: GettingStarted
        url: https://nifi.apache.org/documentation/guides/
      - type: GitHubRepository
        url: https://github.com/apache/nifi
  - aid: apache-nifi:apache-nifi-registry
    name: Apache NiFi Registry
    description: NiFi Registry provides a central location for storage and management of shared NiFi flow resources, enabling versioned flows across NiFi environments. It provides its own REST API for managing buckets, flows, versions, and users.
    humanURL: https://nifi.apache.org/documentation/
    tags:
      - Flow Versioning
      - Registry
      - REST
    properties:
      - type: Documentation
        url: https://nifi.apache.org/documentation/
      - type: GitHubRepository
        url: https://github.com/apache/nifi
  - aid: apache-nifi:apache-minifi
    name: Apache MiNiFi
    description: MiNiFi is a lightweight agent for edge data collection that is a subproject of NiFi. MiNiFi C++ (nifi-minifi-cpp) provides a small-footprint agent for IoT edge data collection with local processing and a remote NiFi parent instance for management.
    humanURL: https://nifi.apache.org/minifi/
    tags:
      - Edge Computing
      - IoT
      - Lightweight Agent
    properties:
      - type: Documentation
        url: https://nifi.apache.org/minifi/
      - type: GitHubRepository
        url: https://github.com/apache/nifi-minifi-cpp
common:
  - type: Portal
    url: https://nifi.apache.org/
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/nifi
  - type: GitHubRepository
    url: https://github.com/apache/nifi-minifi-cpp
  - type: GitHubRepository
    url: https://github.com/apache/nifi-api
  - type: GitHubRepository
    url: https://github.com/apache/nifi-site
  - type: Wiki
    url: https://cwiki.apache.org/confluence/display/NIFI
  - type: IssueTracker
    url: https://issues.apache.org/jira/browse/NIFI
  - type: Slack
    url: https://join.slack.com/t/apachenifi/shared_invite/zt-11njbtkdx-ZRU8FKYSWoEHRJetidy0zA
  - type: Blog
    url: https://nifi.apache.org/blog/
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Features
    data:
      - name: Visual Dataflow Designer
        description: Browser-based drag-and-drop interface for designing, controlling, and monitoring data flows without coding.
      - name: Data Provenance Tracking
        description: Complete lineage tracking of every piece of data that flows through the system from ingestion to destination.
      - name: Hundreds of Built-in Processors
        description: Extensive library of processors for data ingestion, transformation, routing, and delivery to diverse systems and cloud platforms.
      - name: Guaranteed Delivery
        description: Loss-tolerant and guaranteed delivery options with configurable prioritization and backpressure control.
      - name: REST API
        description: Comprehensive JWT-authenticated REST API for programmatic management of all NiFi resources and operations.
      - name: Flow Versioning
        description: Version control for data flows via NiFi Registry, enabling flow promotion across development, test, and production environments.
      - name: Multi-Tenant Security
        description: Fine-grained multi-tenant authorization with HTTPS, TLS, and SSH support for secure deployments.
      - name: Clustering
        description: Zero-master cluster architecture for high-availability and load-balanced dataflow execution.
      - name: Parameter Contexts
        description: Externalize configuration using parameter contexts that can be applied across multiple processors and process groups.
      - name: MiNiFi Edge Agents
        description: Lightweight MiNiFi agents for edge data collection at IoT endpoints, managed centrally from NiFi.
  - type: UseCases
    data:
      - name: Data Ingestion Pipelines
        description: Build pipelines ingesting data from files, databases, message queues, cloud storage, and APIs into data lakes and warehouses.
      - name: Cybersecurity Data Collection
        description: Collect and route security telemetry, logs, and threat intelligence feeds for SIEM and analytics platforms.
      - name: IoT Edge Data Collection
        description: Deploy MiNiFi agents at IoT edge locations to collect, filter, and forward sensor data to central NiFi clusters.
      - name: Real-Time Event Streaming
        description: Build event streaming pipelines consuming from Kafka, Kinesis, and other message brokers for real-time data processing.
      - name: Generative AI Data Pipelines
        description: Build data preparation and vector database ingestion pipelines for generative AI and RAG applications.
      - name: Cloud Data Integration
        description: Move and transform data between AWS, Azure, and GCP services with built-in cloud processor libraries.
  - type: Integrations
    data:
      - name: Apache Kafka
        description: Native ConsumeKafka and PublishKafka processors for streaming data between NiFi and Kafka topics.
      - name: Amazon S3
        description: PutS3Object and FetchS3Object processors for reading and writing data to AWS S3 buckets.
      - name: Azure Blob Storage
        description: PutAzureBlobStorage and FetchAzureBlobStorage processors for Azure cloud storage integration.
      - name: Google Cloud Storage
        description: Native GCS processors for reading and writing Google Cloud Storage objects.
      - name: MongoDB
        description: PutMongo and GetMongo processors for reading and writing documents to MongoDB collections.
      - name: Elasticsearch
        description: PutElasticsearchRecord and FetchElasticsearch processors for indexing and querying Elasticsearch.
      - name: Salesforce
        description: Native Salesforce processors for querying and publishing data to Salesforce CRM.
      - name: Apache MQTT
        description: ConsumeMQTT and PublishMQTT processors for IoT messaging protocol support.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
