---
aid: apache-oozie
name: Apache Oozie
description: Apache Oozie is a workflow scheduler system for managing Apache Hadoop jobs. It enables users to define workflows as directed acyclic graphs (DAGs) of actions including MapReduce, Pig, Hive, Sqoop, and custom Java/shell steps. Coordinator jobs trigger workflows based on time schedules or data availability, while bundle jobs group multiple coordinators. Oozie provides a REST API for job submission, lifecycle management, monitoring, and system administration. Governed by the Apache Software Foundation under the Apache License 2.0, written in Java.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Workflow
  - Hadoop
  - Orchestration
  - Scheduling
  - Big Data
  - Apache
  - Java
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-oozie/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-oozie:apache-oozie-rest-api
    name: Apache Oozie REST API
    description: The Oozie Web Services API provides REST endpoints for submitting, managing, and monitoring workflow, coordinator, and bundle jobs on Apache Hadoop. Supports full job lifecycle management (submit, start, suspend, resume, kill, rerun), log and status retrieval, DAG visualization, SLA management, and system administration. Available at /oozie/v1 and /oozie/v2 with JSON responses.
    humanURL: https://oozie.apache.org/docs/5.2.1/WebServicesAPI.html
    baseURL: http://localhost:11000/oozie
    tags:
      - REST
      - Hadoop
      - Workflow Management
      - Job Scheduling
    properties:
      - type: Documentation
        url: https://oozie.apache.org/docs/5.2.1/WebServicesAPI.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/apache-oozie/refs/heads/main/openapi/apache-oozie-openapi.yaml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-oozie/refs/heads/main/json-schema/apache-oozie-job-info-schema.json
        title: Job Info Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-oozie/refs/heads/main/json-schema/apache-oozie-job-list-schema.json
        title: Job List Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-oozie/refs/heads/main/json-schema/apache-oozie-job-id-schema.json
        title: Job ID Schema
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-oozie/refs/heads/main/json-schema/apache-oozie-system-status-schema.json
        title: System Status Schema
common:
  - type: GitHubRepository
    url: https://github.com/apache/oozie
    title: Apache Oozie GitHub Repository
  - type: GitHubOrganization
    url: https://github.com/apache
    title: Apache Software Foundation GitHub
  - type: Documentation
    url: https://oozie.apache.org/docs/5.2.1/
    title: Apache Oozie Documentation
  - type: GettingStarted
    url: https://oozie.apache.org/docs/5.2.1/DG_QuickStart.html
    title: Oozie Quick Start Guide
  - type: Tutorials
    url: https://oozie.apache.org/docs/5.2.1/DG_Examples.html
    title: Oozie Examples
  - type: ReleaseNotes
    url: https://github.com/apache/oozie/blob/master/release-log.txt
    title: Oozie Release Log
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
    title: Apache License 2.0
  - type: Support
    url: https://oozie.apache.org/mailing-lists.html
    title: Mailing Lists
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/oozie
    title: Oozie on Stack Overflow
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/apache-oozie/refs/heads/main/rules/apache-oozie-spectral-rules.yml
    title: Apache Oozie Spectral Rules
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/apache-oozie/refs/heads/main/capabilities/apache-oozie-workflow-orchestration.yaml
    title: Apache Oozie Workflow Orchestration
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/apache-oozie/refs/heads/main/vocabulary/apache-oozie-vocabulary.yaml
    title: Apache Oozie Vocabulary
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/apache-oozie/refs/heads/main/json-ld/apache-oozie-context.jsonld
    title: Apache Oozie JSON-LD Context
  - type: Features
    data:
      - name: Directed Acyclic Graph Workflows
        description: Define complex data processing pipelines as DAGs of actions executed on Apache Hadoop.
      - name: Coordinator Jobs
        description: Schedule recurring workflows triggered by time intervals or data availability conditions in HDFS.
      - name: Bundle Jobs
        description: Group multiple coordinator jobs into a single bundle for coordinated lifecycle management.
      - name: REST API Management
        description: Full REST API for job submission, lifecycle control, monitoring, and system administration.
      - name: Native Hadoop Action Types
        description: Built-in support for MapReduce, Pig, Hive, Sqoop, Distcp, and custom Java/shell actions.
      - name: SLA Management
        description: Define and monitor service level agreements on workflow and coordinator actions with alert capabilities.
      - name: DAG Visualization
        description: Generate PNG, SVG, or DOT graph visualizations of workflow DAGs for debugging and documentation.
      - name: Log Retrieval
        description: Retrieve execution logs, error logs, and audit trails for jobs via REST API with filtering support.
      - name: High Availability
        description: Built-in HA support with multiple Oozie server instances and distributed state management.
      - name: Shared Library Support
        description: Manage shared Hadoop libraries across workflows for consistent classpath management.
  - type: UseCases
    data:
      - name: ETL Pipeline Orchestration
        description: Orchestrate multi-step ETL pipelines combining Hive queries, MapReduce jobs, and data transfers on Hadoop.
      - name: Scheduled Data Processing
        description: Run recurring Hadoop batch jobs on time-based schedules using coordinator jobs.
      - name: Data-Triggered Workflows
        description: Trigger workflows automatically when new data arrives in HDFS using coordinator data-in conditions.
      - name: Machine Learning Pipeline Automation
        description: Automate ML model training and evaluation pipelines on Hadoop with dependency chaining.
      - name: Data Migration and Archival
        description: Orchestrate large-scale data migration, compaction, and archival workflows across Hadoop clusters.
      - name: Multi-Cluster Coordination
        description: Coordinate workflows that span multiple Hadoop clusters using Distcp and remote actions.
  - type: Integrations
    data:
      - name: Apache Hadoop
        description: Core integration with HDFS for data storage and YARN for resource management.
      - name: Apache Hive
        description: Native Hive action type for executing HiveQL queries as workflow steps.
      - name: Apache Pig
        description: Native Pig action type for data transformation scripts in workflow pipelines.
      - name: Apache Sqoop
        description: Native Sqoop action type for importing and exporting data between Hadoop and RDBMS.
      - name: Apache Spark
        description: Spark action type for running Spark jobs within Oozie workflows.
      - name: Apache MapReduce
        description: Native MapReduce action type as the foundational Hadoop computation framework.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
