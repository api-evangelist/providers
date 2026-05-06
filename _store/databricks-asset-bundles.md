---
aid: databricks-asset-bundles
name: Databricks Asset Bundles
description: Databricks Asset Bundles (DABs) provide an infrastructure-as-code approach to managing Databricks data and AI projects. Bundles enable version control, CI/CD, deployment, and management of Databricks resources such as jobs, pipelines, apps, schemas, experiments, and model serving endpoints across workspaces using the Databricks CLI.
type: Index
image: https://www.databricks.com/sites/default/files/2023-05/databricks-logo.png
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
url: https://raw.githubusercontent.com/api-evangelist/databricks-asset-bundles/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
xType: company
position: Consumer
access: 3rd-Party
apis:
  - aid: databricks-asset-bundles:databricks-asset-bundles-api
    name: Databricks Asset Bundles API
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
      - type: JSONSchema
        url: json-schema/bundle.json
    contact:
      - FN: Databricks Support
        email: support@databricks.com
        url: https://help.databricks.com/
common:
  - type: Portal
    url: https://docs.databricks.com/aws/en/dev-tools/bundles
  - type: Getting Started
    url: https://docs.databricks.com/aws/en/dev-tools/bundles/jobs-tutorial
  - type: Documentation
    url: https://docs.databricks.com/aws/en/dev-tools/bundles/settings
  - type: Reference
    url: https://docs.databricks.com/aws/en/dev-tools/bundles/reference
  - type: Tutorials
    url: https://docs.databricks.com/aws/en/dev-tools/bundles/tutorials
  - type: CLI Reference
    url: https://docs.databricks.com/aws/en/dev-tools/cli/bundle-commands
  - type: Authentication
    url: https://docs.databricks.com/aws/en/dev-tools/bundles/authentication
  - type: Resources
    url: https://docs.databricks.com/aws/en/dev-tools/bundles/resources
  - type: Templates
    url: https://docs.databricks.com/aws/en/dev-tools/bundles/templates
  - type: Configuration Examples
    url: https://docs.databricks.com/aws/en/dev-tools/bundles/examples
  - type: Permissions
    url: https://docs.databricks.com/aws/en/dev-tools/bundles/permissions
  - type: Variables
    url: https://docs.databricks.com/aws/en/dev-tools/bundles/variables
  - type: Deployment Modes
    url: https://docs.databricks.com/aws/en/dev-tools/bundles/deployment-modes
  - type: Library Dependencies
    url: https://docs.databricks.com/aws/en/dev-tools/bundles/library-dependencies
  - type: Python Wheel
    url: https://docs.databricks.com/aws/en/dev-tools/bundles/python-wheel
  - type: Python Configuration
    url: https://docs.databricks.com/aws/en/dev-tools/bundles/python
  - type: CI/CD
    url: https://docs.databricks.com/aws/en/dev-tools/bundles/ci-cd-bundles
  - type: Migration Guide
    url: https://docs.databricks.com/aws/en/dev-tools/bundles/migrate-resources
  - type: FAQ
    url: https://docs.databricks.com/aws/en/dev-tools/bundles/faqs
  - type: Change Log
    url: https://docs.databricks.com/aws/en/release-notes/dev-tools/bundles
  - type: GitHub Repository
    url: https://github.com/databricks/cli
  - type: GitHub Examples
    url: https://github.com/databricks/bundle-examples
  - type: GitHub Action
    url: https://github.com/databricks/setup-cli
  - type: Pricing
    url: https://www.databricks.com/product/pricing
  - type: Status
    url: https://status.databricks.com/
  - type: Support
    url: https://help.databricks.com/
  - type: Community
    url: https://community.databricks.com/
  - type: Blog
    url: https://www.databricks.com/blog
  - type: Website
    url: https://www.databricks.com/
  - type: Login
    url: https://login.databricks.com/
  - type: Sign Up
    url: https://www.databricks.com/try-databricks
  - type: Terms of Service
    url: https://www.databricks.com/legal/terms-of-use
  - type: Privacy Policy
    url: https://www.databricks.com/legal/privacynotice
  - type: Security
    url: https://www.databricks.com/trust
  - type: GitHub Organization
    url: https://github.com/databricks
  - type: Training
    url: https://www.databricks.com/learn/training/home
  - type: Contact
    url: https://www.databricks.com/company/contact
  - type: JSON-LD
    url: json-ld/databricks-asset-bundles-context.jsonld
  - type: Vocabulary
    url: vocabulary/databricks-asset-bundles-vocabulary.yml
  - type: Capabilities
    url: capabilities/databricks-asset-bundles-capabilities.yml
  - type: Rules
    url: rules/databricks-asset-bundles-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
