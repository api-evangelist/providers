---
aid: apache-zeppelin
name: Apache Zeppelin
description: Apache Zeppelin is a web-based notebook that enables data-driven, interactive data analytics and collaborative documents with SQL, Scala, Python, R, and more. It provides built-in data visualization, collaboration features, and interpreter integration with Apache Spark, JDBC, Python, R, Shell, and 20+ other backends. Zeppelin exposes a REST API for notebook management, interpreter configuration, and job execution. It is maintained by the Apache Software Foundation.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Analytics
  - Interactive Computing
  - Notebook
  - Visualization
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-zeppelin/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-zeppelin:apache-zeppelin-rest-api
    name: Apache Zeppelin REST API
    description: 'The Zeppelin REST API provides HTTP endpoints for managing notebooks, notes, paragraphs, interpreters, and credentials. Key endpoints include: GET/POST /api/notebook for notebook CRUD, GET/POST /api/notebook/{noteId}/paragraph for paragraph management, POST /api/notebook/job/{noteId} for running all paragraphs, GET /api/interpreter/setting for interpreter listing, and POST /api/interpreter/setting/restart for restarting interpreters. Returns JSON responses with status codes.'
    humanURL: https://zeppelin.apache.org/docs/latest/usage/rest_api/notebook.html
    tags:
      - REST
      - Notebooks
      - Paragraphs
      - Interpreter
    properties:
      - type: Documentation
        url: https://zeppelin.apache.org/docs/latest/usage/rest_api/notebook.html
      - type: Documentation
        url: https://zeppelin.apache.org/docs/latest/usage/rest_api/interpreter.html
common:
  - type: GitHubRepository
    url: https://github.com/apache/zeppelin
  - type: Documentation
    url: https://zeppelin.apache.org/docs/latest/
  - type: Portal
    url: https://zeppelin.apache.org/
  - type: GettingStarted
    url: https://zeppelin.apache.org/docs/latest/quickstart/install.html
  - type: ReleaseNotes
    url: https://github.com/apache/zeppelin/releases
  - type: Support
    url: https://zeppelin.apache.org/community.html
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: Features
    data:
      - name: Multi-Language Support
        description: Execute code in Scala, Python, R, SQL, Shell, and 20+ languages in the same notebook.
      - name: Built-In Visualization
        description: Bar, line, pie, scatter, and map charts from query results without additional tools.
      - name: Collaborative Notebooks
        description: Real-time collaborative editing of notebooks with user management and permissions.
      - name: Spark Integration
        description: Native Apache Spark interpreter for Scala, Python (PySpark), and SQL queries.
      - name: JDBC Interpreter
        description: Universal JDBC interpreter for any SQL database including MySQL, PostgreSQL, Hive.
      - name: Paragraph Scheduling
        description: Schedule notebook paragraphs with cron expressions for automated execution.
      - name: Dynamic Forms
        description: Interactive input forms within notebook paragraphs for parameterized execution.
  - type: UseCases
    data:
      - name: Interactive Data Exploration
        description: Exploratory data analysis with Spark SQL, Python, and R in a collaborative notebook.
      - name: Data Science Prototyping
        description: Rapid ML prototyping and model development with live results visualization.
      - name: SQL Analytics
        description: Interactive SQL queries against Hive, Spark SQL, or any JDBC database.
      - name: Automated Reporting
        description: Scheduled notebook execution for automated data report generation.
  - type: Integrations
    data:
      - name: Apache Spark
        description: Native Spark interpreter for Scala, PySpark, and SparkSQL workloads.
      - name: Apache Hive
        description: Hive JDBC and HiveQL interpreter for Hive data warehouse queries.
      - name: Apache Flink
        description: Apache Flink interpreter for stream processing in Zeppelin notebooks.
      - name: Kubernetes
        description: Zeppelin on Kubernetes with per-notebook pod isolation for interpreter processes.
      - name: Elasticsearch
        description: Elasticsearch interpreter for indexing and querying Elasticsearch data.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
