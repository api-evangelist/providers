---
aid: apache-airflow
url: https://raw.githubusercontent.com/api-evangelist/apache-airflow/refs/heads/main/apis.yml
apis:
- name: Apache Airflow REST API
  description: The stable public REST API for interacting with Apache Airflow programmatically, allowing management of DAGs, tasks, connections, and more.
  image: https://airflow.apache.org/images/feature-image.png
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
    url: https://airflow.apache.org/docs/apache-airflow/stable/_api/openapi.json
  - type: Authentication
    url: https://airflow.apache.org/docs/apache-airflow/stable/security/api.html
  - type: Changelog
    url: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html
  contact:
  - type: Email
    url: mailto:dev@airflow.apache.org
  - type: Slack
    url: https://apache-airflow.slack.com/
- name: Apache Airflow Experimental API (Deprecated)
  description: The experimental API that preceded the stable REST API. This is deprecated and should not be used for new implementations.
  image: https://airflow.apache.org/images/feature-image.png
  humanURL: https://airflow.apache.org/docs/apache-airflow/stable/deprecated-rest-api-ref.html
  baseURL: http://localhost:8080/api/experimental
  tags:
  - Deprecated
  - Legacy
  - REST
  properties:
  - type: Documentation
    url: https://airflow.apache.org/docs/apache-airflow/stable/deprecated-rest-api-ref.html
  - type: Deprecation Notice
    url: https://airflow.apache.org/docs/apache-airflow/stable/deprecated-rest-api-ref.html#deprecation-notice
name: Apache Airflow
tags:
- DAG
- Data Pipeline
- ETL
- Orchestration
- Scheduling
- Workflow
type: Contract
image: https://airflow.apache.org/images/feature-image.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Apache Airflow is an open-source platform to programmatically author, schedule, and monitor workflows. It allows you to define workflows as code, making them maintainable, versionable, testable, and collaborative.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

