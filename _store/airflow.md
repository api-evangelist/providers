---
aid: airflow
name: Apache Airflow
description: Apache Airflow is an open-source platform to programmatically author, schedule, and monitor workflows. Airflow uses directed acyclic graphs (DAGs) to manage workflow orchestration. The Airflow REST API provides programmatic access to DAGs, DAG runs, tasks, connections, variables, pools, and monitoring for both Airflow OSS and cloud-managed deployments.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Workflow Orchestration
  - Data Pipeline
  - Open Source
  - Apache
  - DAG
  - Scheduling
  - ETL
  - Data Engineering
created: '2026-01-02'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/airflow/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: airflow:airflow
    name: Apache Airflow API
    description: The Apache Airflow REST API (v2) provides stable, backward-compatible endpoints for managing workflows (DAGs), DAG runs, task instances, connections, variables, XComs, pools, and plugins. Available at /api/v2 on any Airflow deployment.
    humanURL: https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html
    tags:
      - Workflow Orchestration
      - DAG
      - Scheduling
      - Data Pipeline
      - Open Source
    properties:
      - url: https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html
        type: Documentation
      - url: https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html
        type: APIReference
      - url: https://raw.githubusercontent.com/api-evangelist/airflow/refs/heads/main/openapi/airflow-openapi.yml
        type: OpenAPI
      - url: https://airflow.apache.org/docs/apache-airflow/stable/security/api.html
        type: Authentication
      - url: https://pypi.org/project/apache-airflow/
        type: SDK
        title: PyPI Package
      - url: https://pypi.org/project/apache-airflow-client/
        type: SDK
        title: Python Client SDK
      - url: https://github.com/apache/airflow
        type: SDK
        title: GitHub Repository
    baseURL: http://localhost:8080/api/v2
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - url: https://airflow.apache.org
    type: Portal
  - url: https://airflow.apache.org/docs/
    type: GettingStarted
  - url: https://github.com/apache/airflow
    type: GitHubOrganization
  - url: https://github.com/apache/airflow
    type: GitHubRepository
  - url: https://airflow.apache.org/blog/
    type: Blog
  - url: https://stackoverflow.com/questions/tagged/airflow
    type: StackOverflow
  - url: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html
    type: ChangeLog
  - url: https://issues.apache.org/jira/projects/AIRFLOW
    type: IssueTracker
  - url: https://hub.docker.com/r/apache/airflow
    type: SDK
    title: Docker Image
  - url: https://artifacthub.io/packages/helm/airflow-helm/airflow
    type: SDK
    title: Helm Chart
  - type: Features
    data:
      - name: DAG Authoring
        description: Define workflows as Python code using Directed Acyclic Graphs (DAGs).
      - name: Dynamic DAG Generation
        description: Programmatically generate DAGs and tasks based on configuration or data.
      - name: Rich Operator Library
        description: Pre-built operators for databases, cloud services, APIs, and data tools.
      - name: REST API v2
        description: Stable REST API for programmatic management of DAGs, runs, tasks, and infrastructure.
      - name: Web UI
        description: Built-in web interface for monitoring, triggering, and debugging workflows.
      - name: Scheduler
        description: Robust scheduler with support for CRON and timed triggers.
      - name: Extensible
        description: Plugin system and provider packages for extending functionality.
      - name: Multi-Cloud Support
        description: Provider packages for AWS, GCP, Azure, and other cloud platforms.
      - name: Managed Services
        description: Available as managed service from AWS (MWAA), GCP (Cloud Composer), and Astronomer.
  - type: UseCases
    data:
      - name: ETL Pipeline Orchestration
        description: Schedule and monitor extract, transform, load data pipelines.
      - name: ML Pipeline Management
        description: Orchestrate machine learning training, evaluation, and deployment workflows.
      - name: Data Quality Checks
        description: Schedule data validation and quality check jobs.
      - name: Report Generation
        description: Automate periodic report generation and distribution.
      - name: API Orchestration
        description: Coordinate calls to multiple APIs in complex workflows.
      - name: Database Operations
        description: Schedule database maintenance, migrations, and backup jobs.
  - type: Integrations
    data:
      - name: Apache Spark
        description: Run Spark jobs from Airflow DAGs.
      - name: dbt
        description: Orchestrate dbt model runs via the dbt operator.
      - name: Kubernetes
        description: Run tasks in Kubernetes pods with the KubernetesPodOperator.
      - name: AWS
        description: Provider package for S3, Redshift, EMR, Lambda, and other AWS services.
      - name: Google Cloud
        description: Provider package for BigQuery, Dataflow, GCS, and other GCP services.
      - name: Azure
        description: Provider package for Azure Data Factory, Blob Storage, and other Azure services.
      - name: Snowflake
        description: SnowflakeOperator for running SQL in Snowflake data warehouse.
      - name: Airbyte
        description: Trigger Airbyte syncs from Airflow DAGs.
  - url: https://raw.githubusercontent.com/api-evangelist/airflow/refs/heads/main/rules/airflow-spectral-rules.yml
    type: SpectralRules
    title: Airflow Spectral Rules
  - url: https://raw.githubusercontent.com/api-evangelist/airflow/refs/heads/main/capabilities/workflow-orchestration.yaml
    type: NaftikoCapability
    title: Workflow Orchestration
  - url: https://raw.githubusercontent.com/api-evangelist/airflow/refs/heads/main/vocabulary/airflow-vocabulary.yaml
    type: Vocabulary
    title: Airflow Vocabulary
---
