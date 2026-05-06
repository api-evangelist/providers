---
aid: apache-dolphinscheduler
name: Apache DolphinScheduler
description: Apache DolphinScheduler is a modern distributed and extensible data orchestration platform governed by the Apache Software Foundation. It provides a DAG-based visual workflow designer, multi-master/multi-worker architecture for horizontal scaling, and a comprehensive REST API for programmatic control. It supports dozens of task types (Shell, Spark, Flink, SQL, Python, HTTP, etc.), multi-cloud deployments, multi-tenancy, backfill, and a Python SDK (PyDolphinScheduler).
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Apache
  - DAG
  - Data Pipeline
  - Open Source
  - Orchestration
  - Python
  - Scheduling
  - Workflow
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-dolphinscheduler/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-dolphinscheduler:apache-dolphinscheduler-rest-api
    name: Apache DolphinScheduler REST API
    description: The DolphinScheduler REST API enables programmatic management of projects, workflow definitions (DAGs), workflow instances, task types, schedules, resources, data sources, alerts, tenants, and users. Authentication is via API token. A Swagger UI is available at /dolphinscheduler/swagger-ui/index.html.
    humanURL: https://dolphinscheduler.apache.org/en-us/docs/latest/user_doc/guide/open-api.html
    tags:
      - Alerts
      - DAG
      - Data Sources
      - Projects
      - REST
      - Resources
      - Scheduling
      - Tasks
      - Tenants
      - Workflow
    properties:
      - type: Documentation
        url: https://dolphinscheduler.apache.org/en-us/docs/latest/user_doc/guide/open-api.html
      - type: GettingStarted
        url: https://dolphinscheduler.apache.org/en-us/docs/latest/user_doc/start/quick-start.html
      - type: GitHubRepository
        url: https://github.com/apache/dolphinscheduler
      - type: SDK
        url: https://pypi.org/project/apache-airflow-providers-apache-dolphinscheduler/
        title: Python SDK (PyDolphinScheduler)
      - type: Tools
        url: https://hub.docker.com/r/apache/dolphinscheduler-standalone-server
        title: Docker Image
      - type: Tools
        url: https://github.com/apache/dolphinscheduler-operator
        title: Kubernetes Operator
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-dolphinscheduler/refs/heads/main/json-schema/apache-dolphinscheduler-schedule-schema.json
        title: Schedule
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-dolphinscheduler/refs/heads/main/json-schema/apache-dolphinscheduler-task-definition-schema.json
        title: Task Definition
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-dolphinscheduler/refs/heads/main/json-schema/apache-dolphinscheduler-workflow-definition-schema.json
        title: Workflow Definition
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/apache-dolphinscheduler/refs/heads/main/json-schema/apache-dolphinscheduler-workflow-instance-schema.json
        title: Workflow Instance
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-dolphinscheduler/refs/heads/main/json-structure/apache-dolphinscheduler-schedule-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-dolphinscheduler/refs/heads/main/json-structure/apache-dolphinscheduler-task-definition-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-dolphinscheduler/refs/heads/main/json-structure/apache-dolphinscheduler-workflow-definition-structure.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/apache-dolphinscheduler/refs/heads/main/json-structure/apache-dolphinscheduler-workflow-instance-structure.json
      - type: JSONLD
        url: https://raw.githubusercontent.com/api-evangelist/apache-dolphinscheduler/refs/heads/main/json-ld/apache-dolphinscheduler-context.jsonld
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-dolphinscheduler/refs/heads/main/examples/apache-dolphinscheduler-schedule-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-dolphinscheduler/refs/heads/main/examples/apache-dolphinscheduler-task-definition-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-dolphinscheduler/refs/heads/main/examples/apache-dolphinscheduler-workflow-definition-example.json
      - type: Example
        url: https://raw.githubusercontent.com/api-evangelist/apache-dolphinscheduler/refs/heads/main/examples/apache-dolphinscheduler-workflow-instance-example.json
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
common:
  - type: Portal
    url: https://dolphinscheduler.apache.org/
  - type: Documentation
    url: https://dolphinscheduler.apache.org/en-us/docs/latest/
  - type: GettingStarted
    url: https://dolphinscheduler.apache.org/en-us/docs/latest/user_doc/start/quick-start.html
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/dolphinscheduler
  - type: SDK
    url: https://github.com/apache/dolphinscheduler-sdk-python
    title: PyDolphinScheduler Python SDK
  - type: Features
    data:
      - name: DAG Visual Workflow Designer
        description: Web-based drag-and-drop interface for building directed acyclic graph (DAG) workflows with real-time execution visualization.
      - name: REST Open API
        description: Comprehensive REST API for all platform operations including workflow management, scheduling, resource management, and administration.
      - name: Multi-Master/Worker Architecture
        description: Decentralized architecture with horizontal scaling support, capable of processing tens of millions of tasks per day.
      - name: Rich Task Types
        description: Built-in task types including Shell, Spark, Flink, SQL, Python, HTTP, DataX, Seatunnel, Jupyter, and custom task plugins.
      - name: Multi-Tenancy
        description: Supports multiple tenants with isolated resource quotas, permissions, and workflow namespaces.
      - name: Workflow Versioning
        description: Version control for workflow definitions and instances, enabling rollback and auditing of workflow changes.
      - name: Data Source Management
        description: Unified data source management supporting MySQL, PostgreSQL, Hive, Trino, Spark, ClickHouse, and many other databases.
      - name: Python SDK
        description: PyDolphinScheduler allows defining and managing workflows programmatically in Python with code-first workflow authoring.
  - type: UseCases
    data:
      - name: Data Pipeline Orchestration
        description: Orchestrate complex ETL/ELT data pipelines with dependencies, retries, and monitoring across distributed systems.
      - name: Machine Learning Workflows
        description: Schedule and manage ML model training, evaluation, and deployment pipelines with task dependencies.
      - name: Multi-Cloud Data Workflows
        description: Orchestrate workflows spanning multiple cloud providers and data centers with unified scheduling.
      - name: SQL and Analytics Scheduling
        description: Schedule recurring SQL queries, reports, and analytics jobs against multiple data sources.
      - name: DevOps and CI/CD Pipelines
        description: Automate deployment workflows, data quality checks, and operational tasks with DolphinScheduler DAGs.
  - type: Integrations
    data:
      - name: Apache Spark
        description: Native Spark task type for submitting Spark batch and streaming jobs from DolphinScheduler workflows.
      - name: Apache Flink
        description: Native Flink task type for submitting Flink stream processing jobs.
      - name: Apache Hive
        description: Hive data source and task type for SQL-on-Hadoop workloads.
      - name: Kubernetes
        description: Kubernetes deployment mode and K8s task type for container-native workflow execution.
      - name: Docker
        description: Official Docker images and Docker Compose configuration for rapid deployment.
      - name: DataX / SeaTunnel
        description: Native task types for DataX and SeaTunnel data integration frameworks.
      - name: Apache Airflow
        description: An Airflow provider package allows triggering DolphinScheduler workflows from Airflow DAGs.
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/apache-dolphinscheduler/refs/heads/main/vocabulary/apache-dolphinscheduler-vocabulary.yaml
---
