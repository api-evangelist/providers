---
aid: apache-superset
name: Apache Superset
description: Apache Superset is a modern data exploration and visualization platform designed to be visual, intuitive, and interactive. It provides a rich set of data visualizations, a no-code chart builder, and a SQL editor with support for most SQL-speaking databases. Superset exposes a comprehensive REST API for programmatic access to dashboards, charts, datasets, databases, and user management. It is an Apache Software Foundation top-level project.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - BI
  - Dashboard
  - Data Visualization
  - SQL
  - Open Source
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-superset/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-superset:apache-superset-rest-api
    name: Apache Superset REST API
    description: The Superset REST API v1 provides programmatic access to all Superset resources including dashboards (28 endpoints), charts (20 endpoints), datasets (19 endpoints), databases (30 endpoints), SQL Lab queries (7 endpoints), saved queries (17 endpoints), tags, annotation layers, CSS templates, themes, row-level security, and user management. Authentication uses JWT Bearer tokens obtained via POST /api/v1/security/login.
    humanURL: https://superset.apache.org/developer-docs/api
    tags:
      - REST
      - Dashboards
      - Charts
      - Datasets
      - SQL
      - Analytics
    properties:
      - type: Documentation
        url: https://superset.apache.org/developer-docs/api
      - type: APIReference
        url: https://superset.apache.org/docs/api
common:
  - type: GitHubRepository
    url: https://github.com/apache/superset
  - type: Documentation
    url: https://superset.apache.org/docs/intro
  - type: Portal
    url: https://superset.apache.org/
  - type: GettingStarted
    url: https://superset.apache.org/docs/quickstart
  - type: ReleaseNotes
    url: https://github.com/apache/superset/releases
  - type: Support
    url: https://github.com/apache/superset/discussions
  - type: TermsOfService
    url: https://www.apache.org/licenses/
  - type: SDK
    url: https://pypi.org/project/apache-superset/
    title: Python Package
  - type: Features
    data:
      - name: No-Code Chart Builder
        description: Drag-and-drop chart builder with 40+ visualization types requiring no coding.
      - name: SQL Lab
        description: Browser-based SQL editor with query history, saved queries, and result export.
      - name: Dashboard Builder
        description: Interactive dashboard composition with filters, tabs, and layout customization.
      - name: Semantic Layer
        description: Centralized dataset definitions with virtual columns, metrics, and certification.
      - name: Row-Level Security
        description: Fine-grained data access control with row-level security rules.
      - name: Embedded Dashboards
        description: Embed Superset dashboards in external applications via iframe or SDK.
      - name: Alerts and Reports
        description: Scheduled PDF/image reports and threshold-based alerts via email or Slack.
      - name: Database Connectivity
        description: 40+ database connectors via SQLAlchemy including BigQuery, Snowflake, and Redshift.
  - type: UseCases
    data:
      - name: Business Intelligence Dashboards
        description: Self-service BI dashboards for business users across operational and analytical data.
      - name: Data Exploration
        description: Ad-hoc data exploration and visualization for data analysts.
      - name: Embedded Analytics
        description: White-label analytics embedded in SaaS products and internal applications.
      - name: SQL-Based Reporting
        description: Custom SQL-based reports and scheduled distribution.
  - type: Integrations
    data:
      - name: PostgreSQL
        description: Native PostgreSQL support as both metadata database and data source.
      - name: Apache Druid
        description: Druid connector for sub-second OLAP queries on time-series data.
      - name: BigQuery
        description: Google BigQuery connector for cloud data warehouse analytics.
      - name: Snowflake
        description: Snowflake connector for cloud analytics platform.
      - name: Apache Spark SQL
        description: Spark SQL via Hive Thrift Server for distributed data analysis.
      - name: Slack
        description: Slack integration for alerts and scheduled report delivery.
      - name: Apache Airflow
        description: Airflow integration for orchestrating data pipeline and report schedules.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
