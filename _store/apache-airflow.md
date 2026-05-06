---
aid: apache-airflow
name: Apache Airflow
description: Apache Airflow is an open-source platform to programmatically author, schedule, and monitor workflows, developed by the Apache Software Foundation. It allows you to define workflows as Directed Acyclic Graphs (DAGs) in Python code, making them maintainable, versionable, testable, and collaborative. Airflow provides a stable REST API for managing DAGs, DAG runs, tasks, connections, variables, pools, and users, along with a web-based UI for monitoring and managing pipeline execution.
type: Index
position: Consumer
access: 3rd-Party
image: https://airflow.apache.org/images/feature-image.png
tags:
  - Apache
  - DAG
  - Data Pipeline
  - ETL
  - Open Source
  - Orchestration
  - Python
  - Scheduling
  - Workflow
created: '2024-01-15'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-airflow/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-airflow:apache-airflow-rest-api
    name: Apache Airflow REST API
    description: The stable public REST API for interacting with Apache Airflow programmatically, allowing management of DAGs, DAG runs, task instances, connections, variables, pools, roles, users, and monitoring resources.
    humanURL: https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html
    baseURL: http://localhost:8080/api/v1
    tags:
      - DAGs
      - REST
      - Tasks
      - Workflow
    properties:
      - type: Documentation
        url: https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html
      - type: OpenAPI
        url: openapi/apache-airflow-openapi.yaml
      - type: Authentication
        url: https://airflow.apache.org/docs/apache-airflow/stable/security/api.html
      - type: ChangeLog
        url: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html
  - aid: apache-airflow:apache-airflow-experimental-api
    name: Apache Airflow Experimental API (Deprecated)
    description: The experimental API that preceded the stable REST API. This is deprecated and should not be used for new implementations.
    humanURL: https://airflow.apache.org/docs/apache-airflow/stable/deprecated-rest-api-ref.html
    baseURL: http://localhost:8080/api/experimental
    tags:
      - Deprecated
      - Legacy
      - REST
    properties:
      - type: Documentation
        url: https://airflow.apache.org/docs/apache-airflow/stable/deprecated-rest-api-ref.html
common:
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/airflow
  - type: Documentation
    url: https://airflow.apache.org/
  - type: GettingStarted
    url: https://airflow.apache.org/docs/apache-airflow/stable/start.html
  - type: Tutorials
    url: https://airflow.apache.org/docs/apache-airflow/stable/tutorial/index.html
  - type: SDK
    url: https://pypi.org/project/apache-airflow/
    title: Python Package (PyPI)
  - type: SDK
    url: https://hub.docker.com/r/apache/airflow
    title: Docker Image
  - type: Security
    url: https://airflow.apache.org/docs/apache-airflow/stable/security/
  - type: Blog
    url: https://airflow.apache.org/blog/
  - type: Support
    url: https://airflow.apache.org/community/
  - type: ChangeLog
    url: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html
  - type: SpectralRules
    url: rules/apache-airflow-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-airflow-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/airflow-orchestration.yaml
  - type: Features
    data:
      - name: DAG-as-Code
        description: Define workflows as Python code (Directed Acyclic Graphs) for version control, testing, and collaboration.
      - name: Stable REST API
        description: Full-featured REST API for programmatic management of DAGs, runs, tasks, connections, variables, pools, and users.
      - name: Dynamic Pipeline Generation
        description: Generate DAGs dynamically using Python, supporting complex conditional and parametric pipelines.
      - name: Extensible Providers
        description: Rich ecosystem of provider packages for integrating with AWS, GCP, Azure, databases, and hundreds of external services.
      - name: Rich Web UI
        description: Browser-based dashboard for monitoring DAG runs, task statuses, logs, and Gantt charts.
      - name: Resource Pools
        description: Control concurrency and resource allocation across tasks using configurable pools.
      - name: Cross-DAG Dependencies
        description: Define dependencies between DAGs using sensors, dataset-driven scheduling, and external task sensors.
      - name: Pluggable Executors
        description: Supports Sequential, Local, Celery, Kubernetes, and DASK executors for flexible deployment.
      - name: SLA Monitoring
        description: Define and track Service Level Agreements on task and DAG completion times.
      - name: Variable and Connection Management
        description: Centrally manage environment-specific configuration via Airflow variables and connections.
  - type: UseCases
    data:
      - name: ETL Pipeline Orchestration
        description: Schedule and manage extract, transform, load pipelines with dependency management and retry logic.
      - name: Machine Learning Workflows
        description: Orchestrate ML training, validation, and deployment pipelines with data dependency tracking.
      - name: Data Warehouse Loading
        description: Coordinate data ingestion from multiple sources into data warehouses like BigQuery, Redshift, and Snowflake.
      - name: Batch Report Generation
        description: Schedule periodic batch reporting jobs with email notification on completion or failure.
      - name: Multi-Cloud Data Movement
        description: Move data between AWS, GCP, and Azure using provider integrations with dependency control.
      - name: CI/CD Pipeline Orchestration
        description: Trigger and monitor software deployment pipelines with upstream/downstream task dependencies.
  - type: Integrations
    data:
      - name: Apache Spark
        description: Native Spark submit and Livy operator integration for distributed data processing.
      - name: Google Cloud
        description: Comprehensive GCP provider for BigQuery, Cloud Storage, Dataflow, Dataproc, and more.
      - name: Amazon Web Services
        description: AWS provider for S3, Redshift, EMR, Glue, Lambda, and other services.
      - name: Microsoft Azure
        description: Azure provider for Blob Storage, Data Factory, HDInsight, and Databricks.
      - name: dbt
        description: dbt operator for running dbt transformations within Airflow pipelines.
      - name: Kubernetes
        description: KubernetesPodOperator for running tasks in isolated Kubernetes pods.
      - name: Docker
        description: DockerOperator for running tasks in Docker containers with isolated environments.
      - name: Apache Kafka
        description: Kafka producers and consumers as Airflow tasks via the Kafka provider.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
