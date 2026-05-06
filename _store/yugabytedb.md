---
aid: yugabytedb
name: YugabyteDB
description: YugabyteDB is a distributed PostgreSQL-compatible SQL database for cloud-native and mission-critical applications. It is delivered as open-source YugabyteDB Core, the fully managed YugabyteDB Aeon DBaaS, and the self-managed YugabyteDB Anywhere control plane, with REST APIs for programmatic management of accounts, projects, clusters, universes, backups, restores, read replicas, allow lists, and maintenance windows.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Database
  - Database
  - DBaaS
  - Distributed SQL
  - PostgreSQL
created: '2026-05-03'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: yugabytedb:aeon
    name: YugabyteDB Aeon REST API
    description: The YugabyteDB Aeon REST API provides programmatic access to the fully managed YugabyteDB cloud database service. It is used to deploy and manage clusters and read replicas, schedule and run on-demand backups and restores, manage IP allow lists, configure maintenance windows, and set up monitoring and alerts. All paths are scoped to an account and project, and authentication uses API keys passed as bearer tokens in the Authorization header.
    humanURL: https://docs.yugabyte.com/stable/yugabyte-cloud/managed-automation/managed-api/
    baseURL: https://cloud.yugabyte.com/api/public/v1
    tags:
      - Aeon
      - Backups
      - Clusters
      - DBaaS
      - Distributed SQL
      - Read Replicas
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/openapi/yugabytedb-aeon-openapi.yml
      - type: Documentation
        url: https://docs.yugabyte.com/stable/yugabyte-cloud/managed-automation/managed-api/
      - type: APIReference
        url: https://api-docs.yugabyte.com/docs/managed-apis/
      - type: Quickstart
        url: https://docs.yugabyte.com/stable/yugabyte-cloud/managed-automation/managed-api/managed-apikeys/
      - type: Authentication
        url: https://docs.yugabyte.com/stable/yugabyte-cloud/managed-automation/managed-api/managed-apikeys/
      - type: CLI
        url: https://github.com/yugabyte/ybm-cli
        title: YugabyteDB Aeon CLI (ybm)
      - type: Integrations
        url: https://github.com/yugabyte/terraform-provider-ybm
        title: Terraform Provider for YugabyteDB Aeon
      - type: TermsOfService
        url: https://www.yugabyte.com/yugabytedb-managed-service-terms/
  - aid: yugabytedb:anywhere
    name: YugabyteDB Anywhere REST API
    description: The YugabyteDB Anywhere REST API enables programmatic management of self-managed YugabyteDB deployments through the YugabyteDB Anywhere (YBA) control plane. It supports creating and managing cloud provider configurations, deploying and managing universes (database clusters), pausing and resuming universes, performing software upgrades, executing backups and restores, and resizing nodes. Authentication is performed via the X-AUTH-YW-API-TOKEN HTTP header.
    humanURL: https://docs.yugabyte.com/stable/yugabyte-platform/anywhere-automation/anywhere-api/
    baseURL: http://{ybaHost}/api/v1
    tags:
      - Anywhere
      - Backups
      - Distributed SQL
      - Self-Managed
      - Universes
    properties:
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/openapi/yugabytedb-anywhere-v1-universes.yaml
        title: Anywhere v1 — Universe Management
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/openapi/yugabytedb-anywhere-v1-backups-restore.yaml
        title: Anywhere v1 — Backups, Restores, and Replication
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/openapi/yugabytedb-anywhere-v1-providers-infra.yaml
        title: Anywhere v1 — Providers and Infrastructure
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/openapi/yugabytedb-anywhere-v1-alerts-monitoring.yaml
        title: Anywhere v1 — Alerts and Monitoring
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/openapi/yugabytedb-anywhere-v1-users-rbac.yaml
        title: Anywhere v1 — Users, Sessions, and RBAC
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/openapi/yugabytedb-anywhere-v1-releases-maintenance.yaml
        title: Anywhere v1 — Releases and Maintenance
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/openapi/yugabytedb-anywhere-v1-high-availability.yaml
        title: Anywhere v1 — High Availability
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/openapi/yugabytedb-anywhere-v2-openapi.yaml
        title: Anywhere v2 — Improved API
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/openapi/yugabytedb-anywhere-v1-full.yaml
        title: Anywhere v1 — Full Monolithic Spec (reference)
      - type: Documentation
        url: https://docs.yugabyte.com/stable/yugabyte-platform/anywhere-automation/anywhere-api/
      - type: APIReference
        url: https://api-docs.yugabyte.com/docs/yugabyte-platform/
      - type: Quickstart
        url: https://docs.yugabyte.com/stable/yugabyte-platform/anywhere-automation/anywhere-api/
      - type: Authentication
        url: https://docs.yugabyte.com/stable/yugabyte-platform/anywhere-automation/anywhere-api/
      - type: SDK
        url: https://github.com/yugabyte/platform-go-client
        title: YugabyteDB Anywhere Go API Client
      - type: Integrations
        url: https://github.com/yugabyte/terraform-provider-yba
        title: Terraform Provider for YugabyteDB Anywhere
      - type: Integrations
        url: https://github.com/yugabyte/yugabyte-k8s-operator
        title: YugabyteDB Kubernetes Operator
      - type: KubernetesCRD
        url: crd/yugabytedb-ybuniverse.yaml
        title: YBUniverse CRD
      - type: KubernetesCRD
        url: crd/yugabytedb-backup.yaml
        title: Backup CRD
      - type: KubernetesCRD
        url: crd/yugabytedb-backup-schedule.yaml
        title: BackupSchedule CRD
      - type: KubernetesCRD
        url: crd/yugabytedb-restore-job.yaml
        title: RestoreJob CRD
      - type: KubernetesCRD
        url: crd/yugabytedb-storage-config.yaml
        title: StorageConfig CRD
      - type: KubernetesCRD
        url: crd/yugabytedb-dr-config.yaml
        title: DrConfig CRD
      - type: KubernetesCRD
        url: crd/yugabytedb-pitr-config.yaml
        title: PitrConfig CRD
      - type: KubernetesCRD
        url: crd/yugabytedb-release.yaml
        title: Release CRD
      - type: KubernetesCRD
        url: crd/yugabytedb-support-bundle.yaml
        title: SupportBundle CRD
      - type: KubernetesCRD
        url: crd/yugabytedb-ybcertificate.yaml
        title: YBCertificate CRD
      - type: KubernetesCRD
        url: crd/yugabytedb-ybprovider.yaml
        title: YBProvider CRD
      - type: KubernetesCRD
        url: crd/yugabytedb-ybplatform.yaml
        title: YBPlatform CRD
      - type: TermsOfService
        url: https://www.yugabyte.com/yugabytedb-managed-service-terms/
common:
  - url: https://www.yugabyte.com/
    name: YugabyteDB Website
    type: Website
  - url: https://docs.yugabyte.com/
    name: YugabyteDB Documentation
    type: Documentation
  - url: https://api-docs.yugabyte.com/
    name: YugabyteDB API Documentation Portal
    type: APIReference
  - url: https://docs.yugabyte.com/stable/quick-start-yugabytedb-managed/
    name: YugabyteDB Quick Start
    type: Quickstart
  - url: https://docs.yugabyte.com/stable/develop/
    name: YugabyteDB Developer Guide
    type: GettingStarted
  - url: https://cloud.yugabyte.com/
    name: YugabyteDB Aeon Console
    type: Console
  - url: https://cloud.yugabyte.com/signup
    name: YugabyteDB Aeon Sign Up
    type: SignUp
  - url: https://cloud.yugabyte.com/login
    name: YugabyteDB Aeon Login
    type: Login
  - url: https://www.yugabyte.com/pricing/
    name: YugabyteDB Pricing
    type: Pricing
  - url: https://docs.yugabyte.com/stable/integrations/
    name: YugabyteDB Integrations
    type: Integrations
  - url: https://www.yugabyte.com/blog/
    name: YugabyteDB Blog
    type: Blog
  - url: https://www.yugabyte.com/yugabytedb-managed-service-terms/
    name: YugabyteDB Managed Service Terms
    type: TermsOfService
  - url: https://www.yugabyte.com/privacy-policy/
    name: YugabyteDB Privacy Policy
    type: PrivacyPolicy
  - url: https://status.yugabyte.com/
    name: YugabyteDB Aeon Status Page
    type: StatusPage
  - url: https://support.yugabyte.com/
    name: Yugabyte Support Portal
    type: Support
  - url: https://forum.yugabyte.com/
    name: YugabyteDB Community Forum
    type: Support
  - url: https://docs.yugabyte.com/stable/releases/
    name: YugabyteDB Release Notes
    type: ReleaseNotes
  - url: https://university.yugabyte.com/
    name: Yugabyte University
    type: Academy
  - url: https://github.com/yugabyte
    name: Yugabyte GitHub Organization
    type: GitHubOrganization
  - url: https://github.com/yugabyte/yugabyte-db
    name: YugabyteDB Core Repository
    type: GitHubRepository
  - url: https://stackoverflow.com/questions/tagged/yugabytedb
    name: YugabyteDB on Stack Overflow
    type: StackOverflow
  - url: https://www.youtube.com/c/yugabyte
    name: YugabyteDB YouTube
    type: YouTube
  - url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/json-schema/yugabytedb-cluster-schema.json
    name: YugabyteDB Cluster JSON Schema
    type: JSONSchema
  - url: https://raw.githubusercontent.com/api-evangelist/yugabytedb/refs/heads/main/json-ld/yugabytedb-context.jsonld
    name: YugabyteDB JSON-LD Context
    type: JSON-LD
  - url: https://github.com/yugabyte/yugabytedb-mcp-server
    name: YugabyteDB MCP Server
    type: SDK
    title: MCP Server
  - url: https://github.com/yugabyte/yugabytedb-skills
    name: YugabyteDB Agent Skills
    type: SDK
    title: AI Agent Skills
  - url: https://search.maven.org/artifact/com.yugabyte/jdbc-yugabytedb
    name: YugabyteDB YSQL JDBC Driver
    type: SDK
    title: Java YSQL Smart Driver
  - url: https://github.com/yugabyte/pgx
    name: YugabyteDB YSQL Go Driver (pgx fork)
    type: SDK
    title: Go YSQL Smart Driver
  - url: https://pypi.org/project/django-yugabytedb/
    name: YugabyteDB Django Backend
    type: SDK
    title: Python Django Backend
  - url: https://github.com/yugabyte/sqlalchemy-yugabytedb
    name: YugabyteDB SQLAlchemy Dialect
    type: SDK
    title: Python SQLAlchemy Dialect
  - url: https://rubygems.org/gems/activerecord-yugabytedb-adapter
    name: YugabyteDB ActiveRecord Adapter
    type: SDK
    title: Ruby ActiveRecord Adapter
  - url: https://www.npmjs.com/package/sequelize-yugabytedb
    name: YugabyteDB Sequelize Package
    type: SDK
    title: Node.js Sequelize Package
  - url: https://github.com/yugabyte/gorm-yugabytedb
    name: YugabyteDB GORM Driver
    type: SDK
    title: Go GORM Driver
  - url: https://github.com/yugabyte/r2dbc-yugabytedb
    name: YugabyteDB R2DBC Driver
    type: SDK
    title: Java R2DBC YSQL Driver
  - url: https://pypi.org/project/langchain-yugabytedb/
    name: LangChain YugabyteDB Integration
    type: SDK
    title: Python LangChain Integration
  - url: https://github.com/yugabyte/cassandra-cpp-driver
    name: YugabyteDB YCQL C++ Driver
    type: SDK
    title: C++ YCQL Driver
  - url: https://github.com/yugabyte/cassandra-java-driver
    name: YugabyteDB YCQL Java Driver
    type: SDK
    title: Java YCQL Driver
  - url: https://github.com/yugabyte/cassandra-python-driver
    name: YugabyteDB YCQL Python Driver
    type: SDK
    title: Python YCQL Driver
  - url: https://github.com/yugabyte/cassandra-nodejs-driver
    name: YugabyteDB YCQL Node.js Driver
    type: SDK
    title: Node.js YCQL Driver
  - url: https://github.com/yugabyte/cassandra-csharp-driver
    name: YugabyteDB YCQL C# Driver
    type: SDK
    title: C# YCQL Driver
  - url: https://github.com/yugabyte/gocql
    name: YugabyteDB YCQL Go Driver (gocql fork)
    type: SDK
    title: Go YCQL Driver
  - url: https://github.com/yugabyte/spring-data-yugabytedb
    name: Spring Data YugabyteDB
    type: SDK
    title: Java Spring Data Module
  - url: https://github.com/yugabyte/yb-voyager
    name: YugabyteDB Voyager
    type: CLI
    title: Database Migration Tool (yb-voyager)
  - url: https://github.com/yugabyte/cqlsh
    name: YugabyteDB cqlsh
    type: CLI
    title: YCQL Shell (cqlsh)
  - url: https://github.com/yugabyte/yuga-bench
    name: YugabyteDB CIS Benchmark
    type: Compliance
  - url: https://github.com/yugabyte/yugabytedb-pgcompare
    name: YugabyteDB pgCompare
    type: GitHubRepository
  - url: https://github.com/yugabyte/yugabyte-prometheus-sizing-calculator
    name: Prometheus Sizing Calculator for YugabyteDB Anywhere
    type: GitHubRepository
  - url: https://github.com/yugabyte/yb-log-analyzer-py
    name: YugabyteDB Log Analyzer
    type: GitHubRepository
  - url: https://github.com/yugabyte/cbo_stat_dump
    name: YugabyteDB CBO Stat Dump
    type: GitHubRepository
  - url: https://github.com/yugabyte/yb-tools
    name: YugabyteDB Maintenance Tools
    type: GitHubRepository
  - url: https://github.com/yugabyte/yugabyte-db-action
    name: YugabyteDB GitHub Action
    type: GitHubRepository
  - url: https://github.com/yugabyte/yb-sample-apps
    name: YugabyteDB Sample Apps
    type: CodeExamples
    title: Workload Generator (Java)
  - url: https://github.com/yugabyte/blog-examples
    name: YugabyteDB Blog Examples
    type: CodeExamples
    title: Blog Demonstrations
  - url: https://github.com/yugabyte/cdc-examples
    name: YugabyteDB CDC Examples
    type: CodeExamples
    title: CDC Connector Examples
  - url: https://github.com/yugabyte/spring-boot-sample-apps
    name: Spring Boot Samples for YugabyteDB
    type: CodeExamples
    title: Spring Boot Samples
  - url: https://github.com/yugabyte/spring-data-yugabytedb-example
    name: Spring Data YugabyteDB Example
    type: CodeExamples
    title: Spring Data Sample
  - url: https://github.com/yugabyte/microservices-demo
    name: YugabyteDB Microservices Demo
    type: CodeExamples
    title: Microservices Demo (Hipster Shop fork)
  - url: https://github.com/yugabyte/yugastore
    name: Yugastore Sample E-Commerce App
    type: CodeExamples
    title: Yugastore E-Commerce App
  - url: https://github.com/yugabyte/yb-iot-fleet-management
    name: YugabyteDB IoT Fleet Management Sample
    type: CodeExamples
    title: IoT Fleet Management Sample
  - url: https://github.com/YugabyteDB-Samples/orm-examples
    name: YugabyteDB ORM Examples
    type: CodeExamples
    title: ORM Examples
  - url: https://github.com/YugabyteDB-Samples/yb-workload-simulator
    name: YugabyteDB Workload Simulator
    type: CodeExamples
    title: Workload Simulator
  - url: https://github.com/yugabyte/learn-yugabyte
    name: Learn YugabyteDB and Distributed SQL
    type: Tutorials
    title: Distributed SQL Lessons
  - url: https://github.com/yugabyte/codelabs
    name: YugabyteDB Code Labs
    type: Tutorials
    title: Code Labs
  - url: https://github.com/yugabyte/debezium-connector-yugabytedb
    name: Debezium Connector for YugabyteDB
    type: Integrations
    title: Debezium CDC Connector
  - url: https://github.com/yugabyte/charts
    name: YugabyteDB Helm Charts
    type: Integrations
    title: Helm Charts
  - url: https://github.com/yugabyte/terraform-aws-yugabyte
    name: Terraform Module for YugabyteDB on AWS
    type: Integrations
    title: Terraform AWS Module
  - url: https://github.com/yugabyte/terraform-azure-yugabyte
    name: Terraform Module for YugabyteDB on Azure
    type: Integrations
    title: Terraform Azure Module
  - url: https://github.com/yugabyte/terraform-gcp-yugabyte
    name: Terraform Module for YugabyteDB on GCP
    type: Integrations
    title: Terraform GCP Module
  - url: https://github.com/yugabyte/aws-cloudformation
    name: YugabyteDB AWS CloudFormation Template
    type: Integrations
    title: AWS CloudFormation Template
  - url: https://github.com/yugabyte/azure-resource-manager
    name: YugabyteDB Azure Resource Manager Template
    type: Integrations
    title: Azure Resource Manager Template
  - url: https://github.com/yugabyte/gcp-deployment-manager
    name: YugabyteDB GCP Deployment Manager Scripts
    type: Integrations
    title: GCP Deployment Manager
  - url: https://github.com/yugabyte/flyway-tests
    name: Flyway Plugin for YugabyteDB
    type: Integrations
    title: Flyway Plugin
  - url: https://github.com/yugabyte/hashicorp-vault-ysql-plugin
    name: Hashicorp Vault Plugin for YugabyteDB YSQL
    type: Integrations
    title: HashiCorp Vault Plugin
  - url: https://github.com/yugabyte/homebrew-tap
    name: YugabyteDB Homebrew Tap
    type: Integrations
    title: Homebrew Tap
  - url: https://github.com/yugabyte/cloud-resource-cleanup
    name: Cloud Resource Cleanup Tool
    type: GitHubRepository
  - data:
      - name: PostgreSQL Compatibility
        description: Wire-compatible YSQL API supporting PostgreSQL drivers, ORMs, stored procedures, triggers, and extensions.
      - name: Distributed SQL
        description: ACID transactions, automatic sharding, and horizontal scaling across nodes, zones, and regions.
      - name: Multi-Region Deployments
        description: Geo-distributed clusters with synchronous and asynchronous replication for disaster recovery and data residency.
      - name: Cloud Database as a Service
        description: Fully managed YugabyteDB Aeon clusters across AWS, Azure, and Google Cloud regions.
      - name: Self-Managed Control Plane
        description: YugabyteDB Anywhere for deploying and operating universes on customer infrastructure and Kubernetes.
      - name: Backups and Restores
        description: On-demand and scheduled backups, point-in-time recovery, and cross-region restore.
      - name: Read Replicas
        description: Asynchronous read replicas for low-latency reads in additional regions.
      - name: Vector Indexing
        description: Vector search capabilities for retrieval-augmented generation (RAG) and GenAI workloads.
      - name: YCQL API
        description: Cassandra-compatible API for wide-column workloads alongside the PostgreSQL-compatible YSQL API.
      - name: Connection Management
        description: Built-in connection pooling and load balancing for distributed workloads.
    name: Features
    type: Features
  - data:
      - name: Database Modernization
        description: Replace legacy monolithic RDBMS systems with a horizontally scalable, PostgreSQL-compatible alternative.
      - name: Cloud-Native Applications
        description: Power Kubernetes-deployed and microservices applications with a resilient distributed SQL backend.
      - name: Multi-Region SaaS
        description: Operate global SaaS platforms with low-latency reads and disaster-recovery-ready writes.
      - name: Financial Services
        description: Run mission-critical transaction systems requiring strong consistency and high availability.
      - name: Retail and eCommerce
        description: Handle high-throughput product catalogs, inventory, and orders across regions.
      - name: Telecommunications
        description: Support subscriber, billing, and session data at carrier scale.
      - name: GenAI and RAG
        description: Store embeddings and metadata for retrieval-augmented generation pipelines.
      - name: Edge and Streaming
        description: Provide a durable distributed SQL store for edge and streaming application data.
    name: UseCases
    type: UseCases
  - data:
      - name: Kubernetes
        description: Helm charts and a Kubernetes Operator for deploying YugabyteDB on Kubernetes clusters.
      - name: Terraform
        description: Terraform Provider for YugabyteDB Anywhere for infrastructure-as-code management of universes.
      - name: YugabyteDB Voyager
        description: Open-source migration tool for moving schema and data from PostgreSQL, Oracle, and MySQL to YugabyteDB.
      - name: AWS, Azure, and Google Cloud
        description: Native deployment targets for YugabyteDB Aeon and Anywhere across major public clouds.
      - name: PostgreSQL Drivers and ORMs
        description: Compatibility with standard PostgreSQL drivers, ORMs, and tooling via the YSQL API.
      - name: REST API
        description: Bearer-token authenticated REST APIs for both Aeon and Anywhere control planes.
    name: Integrations
    type: Integrations
  - data:
      - name: YugabyteDB Core
        description: Open-source distributed SQL database available under the Apache 2.0 license.
      - name: YugabyteDB Aeon
        description: Fully managed cloud database service operated by Yugabyte.
      - name: YugabyteDB Anywhere
        description: Self-managed control plane for operating YugabyteDB universes on customer infrastructure.
      - name: YugabyteDB Voyager
        description: Database migration service and tooling for moving to YugabyteDB.
    name: Solutions
    type: Solutions
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
