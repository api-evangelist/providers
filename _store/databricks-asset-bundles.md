---
aid: databricks-asset-bundles
url: https://raw.githubusercontent.com/api-evangelist/databricks-asset-bundles/refs/heads/main/apis.yml
apis:
- name: Databricks Asset Bundles API
  description: The Databricks Asset Bundles API provides CLI-driven endpoints for initializing, validating, deploying, running, and destroying bundles of Databricks resources. Bundles define infrastructure and workspace settings such as deployment targets, resource configurations for jobs, pipelines, apps, and other assets, enabling programmatic lifecycle management of Databricks projects across development, staging, and production environments.
  image: https://www.databricks.com/sites/default/files/2023-05/databricks-logo.png
  humanURL: https://docs.databricks.com/aws/en/dev-tools/bundles
  baseURL: https://<workspace-instance>.cloud.databricks.com/api/2.0
  tags:
  - Bundles
  - CI/CD
  - Deployment
  - Infrastructure as Code
  - Workflows
  properties:
  - type: Documentation
    url: https://docs.databricks.com/aws/en/dev-tools/bundles
  - type: Reference
    url: https://docs.databricks.com/aws/en/dev-tools/bundles/reference
  - type: Authentication
    url: https://docs.databricks.com/aws/en/dev-tools/bundles/authentication
  - type: Getting Started
    url: https://docs.databricks.com/aws/en/dev-tools/bundles/jobs-tutorial
  - type: Change Log
    url: https://docs.databricks.com/aws/en/release-notes/dev-tools/bundles
  - type: FAQ
    url: https://docs.databricks.com/aws/en/dev-tools/bundles/faqs
  contact:
  - FN: Databricks Support
    email: support@databricks.com
    url: https://help.databricks.com/
name: Databricks Asset Bundles
tags:
- CI/CD
- Data Engineering
- Databricks
- Deployment
- Infrastructure as Code
- Jobs
- Machine Learning
- MLOps
- Pipelines
- Workflows
type: Contract
image: https://www.databricks.com/sites/default/files/2023-05/databricks-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Databricks Asset Bundles (DABs) provide an infrastructure-as-code approach to managing Databricks data and AI projects. Bundles enable version control, CI/CD, deployment, and management of Databricks resources such as jobs, pipelines, apps, schemas, experiments, and model serving endpoints across workspaces using the Databricks CLI.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

