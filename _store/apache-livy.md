---
aid: apache-livy
name: Apache Livy
description: Apache Livy is a service that enables easy interaction with a Spark cluster over a REST interface. It allows submitting Spark jobs or snippets of Spark code, retrieving results synchronously or asynchronously, and managing Spark contexts across multiple users. Licensed under Apache 2.0.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Big Data
  - Interactive Computing
  - Open Source
  - REST
  - Spark
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-livy/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-livy:rest-api
    name: Apache Livy REST API
    description: The Livy REST API provides endpoints for creating and managing interactive Spark sessions, submitting batch Spark jobs, executing code statements (Python, Scala, R, SQL), and retrieving job results and logs.
    humanURL: https://livy.apache.org/docs/latest/rest-api.html
    tags:
      - Batch Jobs
      - REST
      - Sessions
      - Spark
    properties:
      - type: Documentation
        url: https://livy.apache.org/docs/latest/rest-api.html
      - type: OpenAPI
        url: openapi/apache-livy-rest-api.yaml
common:
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/incubator-livy
  - type: Documentation
    url: https://livy.apache.org/docs/latest/
  - type: GettingStarted
    url: https://livy.apache.org/get-started/
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Versioning
    url: https://livy.apache.org/download/
  - type: SpectralRules
    url: rules/apache-livy-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/apache-livy-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/spark-job-management.yaml
  - type: Features
    data:
      - name: Interactive Spark Sessions
        description: Create persistent Spark contexts for interactive code execution in Python, Scala, R, and SQL.
      - name: Batch Job Submission
        description: Submit batch Spark jobs without creating an interactive session.
      - name: Multi-Language Support
        description: Execute code in PySpark, Spark (Scala), SparkR, and SQL.
      - name: Multi-User Impersonation
        description: Proxy user support for multi-tenant Spark cluster access.
      - name: Asynchronous Execution
        description: Submit jobs and poll for results asynchronously.
      - name: Log Access
        description: Retrieve driver and executor logs for debugging.
      - name: REST Interface
        description: Simple HTTP REST API for Spark cluster interaction without native clients.
  - type: UseCases
    data:
      - name: Notebook Integration
        description: Power Jupyter, Zeppelin, and other notebooks with Spark backends via Livy.
      - name: Data Engineering Pipelines
        description: Submit Spark batch jobs from orchestration tools like Airflow and Oozie.
      - name: Interactive Data Exploration
        description: Execute ad-hoc Spark code for exploratory data analysis.
      - name: Multi-Tenant Spark Access
        description: Enable multiple users to share a Spark cluster with isolation via Livy sessions.
  - type: Integrations
    data:
      - name: Apache Spark
        description: Livy requires a Spark cluster and acts as the REST gateway to Spark.
      - name: Apache Zeppelin
        description: Zeppelin notebook backend using Livy for distributed Spark execution.
      - name: Jupyter Notebook
        description: Jupyter sparkmagic extension uses Livy for remote Spark kernel access.
      - name: Apache Airflow
        description: Airflow LivyOperator for submitting Spark batch jobs from DAGs.
      - name: Amazon EMR
        description: Livy is available as an EMR application for REST-based Spark access.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
