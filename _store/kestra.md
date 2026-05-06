---
aid: kestra
name: Kestra
segments:
  - Workflows
description: Kestra is a declarative workflow orchestration platform where pipelines are defined in YAML, combining visual and code-first approaches.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - Data Pipelines
  - Event-Driven
  - Orchestration
  - Workflows
created: '2026-03-03'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/kestra/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: kestra:flows-api
    name: Kestra Flows API
    description: The Kestra Flows API provides programmatic access to manage workflow definitions in the Kestra orchestration platform. It enables creating, updating, retrieving, and deleting flows defined in YAML, supporting the full lifecycle of workflow management via REST endpoints.
    humanURL: https://kestra.io/docs/api-reference
    tags:
      - Flows
      - Orchestration
      - Workflows
    properties:
      - type: Documentation
        url: https://kestra.io/docs/api-reference
      - type: OpenAPI
        url: https://kestra.io/docs/api-reference/open-source
  - aid: kestra:executions-api
    name: Kestra Executions API
    description: The Kestra Executions API allows triggering workflow executions, monitoring their state, retrieving execution details including task run outputs and state transitions, and managing the lifecycle of running workflows programmatically.
    humanURL: https://kestra.io/docs/api-reference
    tags:
      - Executions
      - Orchestration
      - Workflows
    properties:
      - type: Documentation
        url: https://kestra.io/docs/api-reference
      - type: OpenAPI
        url: https://kestra.io/docs/api-reference/open-source
  - aid: kestra:namespaces-api
    name: Kestra Namespaces API
    description: The Kestra Namespaces API provides endpoints for managing namespaces, which serve as logical groupings for organizing flows, files, secrets, and key-value pairs within the Kestra platform.
    humanURL: https://kestra.io/docs/api-reference
    tags:
      - Namespaces
      - Orchestration
      - Organization
    properties:
      - type: Documentation
        url: https://kestra.io/docs/api-reference
      - type: OpenAPI
        url: https://kestra.io/docs/api-reference/open-source
  - aid: kestra:kv-store-api
    name: Kestra Key-Value Store API
    description: The Kestra Key-Value Store API enables storing and retrieving key-value pairs within namespaces, providing a simple data persistence mechanism for workflows to share state and configuration across executions.
    humanURL: https://kestra.io/docs/how-to-guides/api
    tags:
      - Key-Value Store
      - State Management
      - Storage
    properties:
      - type: Documentation
        url: https://kestra.io/docs/how-to-guides/api
      - type: OpenAPI
        url: https://kestra.io/docs/api-reference/open-source
  - aid: kestra:namespace-files-api
    name: Kestra Namespace Files API
    description: The Kestra Namespace Files API provides endpoints for listing, uploading, and downloading files within namespaces, enabling file management for workflows that need to work with scripts, configurations, or other file-based resources.
    humanURL: https://kestra.io/docs/how-to-guides/api
    tags:
      - Files
      - Namespaces
      - Storage
    properties:
      - type: Documentation
        url: https://kestra.io/docs/how-to-guides/api
      - type: OpenAPI
        url: https://kestra.io/docs/api-reference/open-source
  - aid: kestra:enterprise-api
    name: Kestra Enterprise API
    description: The Kestra Enterprise API extends the open-source API with additional endpoints for enterprise features including authentication, RBAC, audit logging, multi-tenancy, SSO, and advanced governance capabilities for production deployments.
    humanURL: https://kestra.io/docs/api-reference/enterprise
    tags:
      - Authentication
      - Enterprise
      - Governance
      - RBAC
    properties:
      - type: Documentation
        url: https://kestra.io/docs/api-reference/enterprise
      - type: Authentication
        url: https://kestra.io/docs/enterprise/auth/api
common:
  - type: Portal
    url: https://kestra.io/
    name: Kestra Website
  - type: Documentation
    url: https://kestra.io/docs
    name: Kestra Documentation
  - type: GettingStarted
    url: https://kestra.io/docs/quickstart
    name: Kestra Quickstart Guide
  - type: Tutorials
    url: https://kestra.io/docs/tutorial
    name: Kestra Tutorial
  - type: APIReference
    url: https://kestra.io/docs/api-reference
    name: Kestra API Reference
  - type: APIReference
    url: https://kestra.io/docs/api-reference/open-source
    name: Kestra Open Source API Reference
  - type: Authentication
    url: https://kestra.io/docs/enterprise/auth/api
    name: Kestra Enterprise API Authentication
  - type: SDKs
    url: https://kestra.io/docs/api-reference/kestra-sdk
    name: Kestra SDKs
  - type: Blog
    url: https://kestra.io/blogs
    name: Kestra Blog
  - type: ChangeLog
    url: https://kestra.io/docs/changelog
    name: Kestra Changelog
  - type: Pricing
    url: https://kestra.io/pricing
    name: Kestra Pricing
  - type: Support
    url: https://support.kestra.io/hc/en-us
    name: Kestra Support
  - type: Community
    url: https://kestra.io/community
    name: Kestra Community
  - type: FAQ
    url: https://kestra.io/faq
    name: Kestra FAQ
  - type: GitHubOrganization
    url: https://github.com/kestra-io
    name: Kestra GitHub Organization
  - type: GitHubRepository
    url: https://github.com/kestra-io/kestra
    name: Kestra GitHub Repository
  - type: Integrations
    url: https://kestra.io/plugins/
    name: Kestra Plugins
  - type: Terraform
    url: https://kestra.io/docs/terraform
    name: Kestra Terraform Provider
  - type: PrivacyPolicy
    url: https://kestra.io/privacy-policy
    name: Kestra Privacy Policy
  - type: TermsOfService
    url: https://kestra.io/terms-and-services
    name: Kestra Terms of Service
  - type: Contact
    url: https://kestra.io/contact-us
    name: Kestra Contact
  - type: Features
    url: https://kestra.io/features/api-first
    name: Kestra API-First Architecture
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
