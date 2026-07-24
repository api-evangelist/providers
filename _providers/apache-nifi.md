---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 7
  human_in_the_loop: 3
  name: Apache Nifi Agentic Access
  operation_count: 11
  slug: apache-nifi-agentic-access
  summary_line: 11 operations · 7 acting · 3 human-in-the-loop
api_count: 6
apis:
- description: NiFi Registry provides a central location for storage and management of shared NiFi flow resources, enabling versioned flows across NiFi environments. It provides its own REST API for managing buckets
  name: Apache NiFi Registry
  slug: apache-nifi-registry
- description: MiNiFi is a lightweight agent for edge data collection that is a subproject of NiFi. MiNiFi C++ (nifi-minifi-cpp) provides a small-footprint agent for IoT edge data collection with local processing an
  name: Apache MiNiFi
  slug: apache-minifi
- description: Authentication and access token management
  name: Apache NiFi Access API
  slug: apache-nifi-access-api
- description: Manage connections between processors
  name: Apache NiFi Connections API
  slug: apache-nifi-connections-api
- description: Manage shared controller services
  name: Apache NiFi Controller Services API
  slug: apache-nifi-controller-services-api
- description: Read overall flow status and process group hierarchy
  name: Apache NiFi Flow API
  slug: apache-nifi-flow-api
artifact_total: 38
collections:
- collection_type: open
  name: Apache NiFi REST API
  slug: open-apache-nifi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-nifi-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-nifi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-nifi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apache-nifi-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apache-nifi
- group: start
  title: ''
  type: Portal
  url: https://nifi.apache.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/nifi
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/nifi-minifi-cpp
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/nifi-api
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/nifi-site
- group: other
  title: ''
  type: Wiki
  url: https://cwiki.apache.org/confluence/display/NIFI
- group: operate
  title: ''
  type: IssueTracker
  url: https://issues.apache.org/jira/browse/NIFI
- group: operate
  title: ''
  type: Slack
  url: https://join.slack.com/t/apachenifi/shared_invite/zt-11njbtkdx-ZRU8FKYSWoEHRJetidy0zA
- group: company
  title: ''
  type: Blog
  url: https://nifi.apache.org/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
created: '2026-03-16'
description: Apache NiFi is a dataflow management system designed to automate the flow of data between systems. It provides a web-based user interface for designing, controlling, and monitoring data flows with real-time operational control, data provenance tracking, and support for hundreds of processors. NiFi Version 2 is the current major version with enhanced security and performance.
features:
- description: Browser-based drag-and-drop interface for designing, controlling, and monitoring data flows without coding.
  name: Visual Dataflow Designer
- description: Complete lineage tracking of every piece of data that flows through the system from ingestion to destination.
  name: Data Provenance Tracking
- description: Extensive library of processors for data ingestion, transformation, routing, and delivery to diverse systems and cloud platforms.
  name: Hundreds of Built-in Processors
- description: Loss-tolerant and guaranteed delivery options with configurable prioritization and backpressure control.
  name: Guaranteed Delivery
- description: Comprehensive JWT-authenticated REST API for programmatic management of all NiFi resources and operations.
  name: REST API
- description: Version control for data flows via NiFi Registry, enabling flow promotion across development, test, and production environments.
  name: Flow Versioning
- description: Fine-grained multi-tenant authorization with HTTPS, TLS, and SSH support for secure deployments.
  name: Multi-Tenant Security
- description: Zero-master cluster architecture for high-availability and load-balanced dataflow execution.
  name: Clustering
- description: Externalize configuration using parameter contexts that can be applied across multiple processors and process groups.
  name: Parameter Contexts
- description: Lightweight MiNiFi agents for edge data collection at IoT endpoints, managed centrally from NiFi.
  name: MiNiFi Edge Agents
finops:
- name: Apache Nifi Finops
  service_category: API
  slug: apache-nifi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-nifi.png
integrations:
- description: Native ConsumeKafka and PublishKafka processors for streaming data between NiFi and Kafka topics.
  name: Apache Kafka
- description: PutS3Object and FetchS3Object processors for reading and writing data to AWS S3 buckets.
  name: Amazon S3
- description: PutAzureBlobStorage and FetchAzureBlobStorage processors for Azure cloud storage integration.
  name: Azure Blob Storage
- description: Native GCS processors for reading and writing Google Cloud Storage objects.
  name: Google Cloud Storage
- description: PutMongo and GetMongo processors for reading and writing documents to MongoDB collections.
  name: MongoDB
- description: PutElasticsearchRecord and FetchElasticsearch processors for indexing and querying Elasticsearch.
  name: Elasticsearch
- description: Native Salesforce processors for querying and publishing data to Salesforce CRM.
  name: Salesforce
- description: ConsumeMQTT and PublishMQTT processors for IoT messaging protocol support.
  name: Apache MQTT
layout: provider
modified: '2026-04-19'
name: Apache NiFi
nav: Providers
network: true
overview: 'Apache NiFi publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Access API, Connections API, Controller Services API, and 1 more. Tagged areas include Data Integration, Dataflow, ETL, IoT, and Streaming.


  Apache NiFi''s developer surface includes authentication, developer portal, engineering blog, and 13 more developer resources.'
plans:
- name: Apache Nifi Plans Pricing
  plan_count: 3
  slug: apache-nifi-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Apache Nifi Rate Limits
  slug: apache-nifi-rate-limits
score:
  band: thin
  composite: 38.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.3
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-nifi/refs/heads/main/screenshots/apache-nifi-2026-06-20T172124.png
security:
- kind: authentication
  name: Apache Nifi Authentication
  slug: apache-nifi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apache Nifi Domain Security
  slug: apache-nifi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Nifi Vulnerability Disclosure
  slug: apache-nifi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-nifi
tags:
- Data Integration
- Dataflow
- ETL
- IoT
- Streaming
- Data Pipeline
use_cases:
- description: Build pipelines ingesting data from files, databases, message queues, cloud storage, and APIs into data lakes and warehouses.
  name: Data Ingestion Pipelines
- description: Collect and route security telemetry, logs, and threat intelligence feeds for SIEM and analytics platforms.
  name: Cybersecurity Data Collection
- description: Deploy MiNiFi agents at IoT edge locations to collect, filter, and forward sensor data to central NiFi clusters.
  name: IoT Edge Data Collection
- description: Build event streaming pipelines consuming from Kafka, Kinesis, and other message brokers for real-time data processing.
  name: Real-Time Event Streaming
- description: Build data preparation and vector database ingestion pipelines for generative AI and RAG applications.
  name: Generative AI Data Pipelines
- description: Move and transform data between AWS, Azure, and GCP services with built-in cloud processor libraries.
  name: Cloud Data Integration
website: https://nifi.apache.org/
---
