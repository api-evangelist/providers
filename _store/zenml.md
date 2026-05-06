---
aid: zenml
name: ZenML
description: ZenML is an open-source MLOps and LLMOps framework that unifies machine learning and generative AI workflows through a single orchestration, versioning, and governance layer. It provides a Python SDK, CLI, REST API, and server for managing pipelines, stacks, artifacts, models, and deployments across any infrastructure backend, with 60+ integrations spanning orchestrators, ML frameworks, GenAI tools, cloud storage, and experiment tracking platforms.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - Machine Learning
  - MLOps
  - LLMOps
  - Pipelines
  - Open Source
  - Python
created: '2025-02-08'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/zenml/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: zenml:zenml-oss-api
    name: ZenML OSS REST API
    description: The ZenML open-source REST API exposes endpoints for managing ML pipelines, stacks, components, artifacts, models, deployments, runs, schedules, secrets, users, and projects in a self-hosted ZenML server. It is consumed by the Python SDK and CLI and can be called directly for automation and integration with CI/CD systems and MLOps workflows.
    humanURL: https://docs.zenml.io/api-reference/oss-api
    tags:
      - MLOps
      - Pipelines
      - Open Source
    properties:
      - type: Documentation
        url: https://docs.zenml.io/api-reference/oss-api
      - type: APIReference
        url: https://docs.zenml.io/api-reference/oss-api
      - type: OpenAPI
        url: openapi/zenml-openapi.yml
      - type: GettingStarted
        url: https://docs.zenml.io/getting-started/installation
      - type: Authentication
        url: https://docs.zenml.io/getting-started/deploying-zenml
      - type: SDK
        url: https://docs.zenml.io/sdk-reference
      - type: GitHubRepository
        url: https://github.com/zenml-io/zenml
      - type: JSONSchema
        url: json-schema/zenml-pipeline-schema.json
      - type: JSONSchema
        url: json-schema/zenml-pipeline-run-schema.json
      - type: JSONSchema
        url: json-schema/zenml-stack-schema.json
      - type: JSONSchema
        url: json-schema/zenml-model-schema.json
      - type: JSONSchema
        url: json-schema/zenml-artifact-schema.json
      - type: CodeExamples
        url: examples/zenml-list-pipelines-example.json
      - type: CodeExamples
        url: examples/zenml-get-pipeline-run-example.json
      - type: CodeExamples
        url: examples/zenml-create-stack-example.json
  - aid: zenml:zenml-pro-api
    name: ZenML Pro REST API
    description: The ZenML Pro REST API extends the OSS API with managed control-plane features for teams, including organization and tenant management, role-based access control, audit logs, and enterprise governance.
    humanURL: https://docs.zenml.io/api-reference/pro-api
    tags:
      - MLOps
      - Enterprise
      - Governance
    properties:
      - type: Documentation
        url: https://docs.zenml.io/api-reference/pro-api
      - type: APIReference
        url: https://docs.zenml.io/api-reference/pro-api
      - type: Authentication
        url: https://docs.zenml.io/pro/core-concepts/access-control
common:
  - url: https://www.zenml.io/
    name: ZenML - The AI Control Plane
    type: Portal
  - url: https://docs.zenml.io/
    name: ZenML Documentation
    type: Documentation
  - url: https://docs.zenml.io/getting-started/installation
    name: Get Started with ZenML
    type: GettingStarted
  - url: https://docs.zenml.io/changelog/server-sdk
    name: ZenML Server & SDK Changelog
    type: ChangeLog
  - url: https://github.com/zenml-io/zenml
    name: ZenML GitHub Repository
    type: GitHubRepository
  - url: https://github.com/zenml-io
    name: ZenML GitHub Organization
    type: GitHubOrganization
  - url: https://www.zenml.io/pro
    name: ZenML Pro - Managed MLOps
    type: Pricing
  - url: https://www.zenml.io/integrations
    name: ZenML Integrations
    type: Integrations
  - url: https://www.zenml.io/blog
    name: ZenML Blog
    type: Blog
  - url: https://status.zenml.io/
    name: ZenML Status Page
    type: StatusPage
  - url: https://www.zenml.io/careers
    name: ZenML Careers
    type: Resources
  - url: https://www.zenml.io/terms-of-service
    name: ZenML Terms of Service
    type: TermsOfService
  - url: https://www.zenml.io/privacy-policy
    name: ZenML Privacy Policy
    type: PrivacyPolicy
  - url: https://pypi.org/project/zenml/
    name: ZenML on PyPI
    type: SDK
  - url: https://docs.zenml.io/sdk-reference
    name: ZenML Python SDK Reference
    type: SDK
  - url: https://github.com/zenml-io/zenml/releases
    name: ZenML Releases
    type: ReleaseNotes
  - url: json-ld/zenml-context.jsonld
    name: ZenML JSON-LD Context
    type: JSONLD
  - url: vocabulary/zenml-vocabulary.yml
    name: ZenML Vocabulary
    type: Resources
  - url: rules/zenml-rules.yml
    name: ZenML Spectral Rules
    type: Resources
  - url: capabilities/pipeline-lifecycle.yaml
    name: ZenML Pipeline Lifecycle Capability
    type: Resources
  - url: capabilities/model-promotion.yaml
    name: ZenML Model Promotion Capability
    type: Resources
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
