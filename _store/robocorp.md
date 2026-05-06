---
aid: robocorp
name: Robocorp
description: Robocorp is an open source RPA and workflow automation platform for building Python-based automation bots. The platform provides the Control Room API for managing workspaces, workers, processes, work items, assets, vaults, webhooks, and task packages. Robocorp also provides the RPA Framework, an open-source collection of Python libraries for robotic process automation including browser, desktop, email, Excel, PDF, and cloud service automation. The platform has evolved toward Sema4 AI for AI-powered automation actions.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - RPA
  - Workflow Automation
  - Python
  - Open Source
  - Automation
url: https://raw.githubusercontent.com/api-evangelist/robocorp/refs/heads/main/apis.yml
created: '2026-03-27'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: robocorp:control-room-api
    name: Robocorp Control Room API
    description: The Robocorp Control Room API provides programmatic access to the orchestration platform for RPA automations. It supports workspace management, worker lifecycle, worker group organization, process definition and execution, process run monitoring, step run outputs, work item management, asset storage, vault secrets, webhook configuration, and task package deployment. Authentication uses API keys with the RC-WSKEY prefix.
    humanURL: https://robocorp.com/api
    baseURL: https://cloud.robocorp.com/api/v1
    tags:
      - RPA
      - Automation
      - Orchestration
      - Workflow
      - Workers
    properties:
      - url: https://robocorp.com/api
        type: Documentation
      - url: https://robocorp.com/docs/control-room/apis-and-webhooks
        type: Guide
      - url: https://robocorp.com/api/openapi.json
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/robocorp/refs/heads/main/openapi/robocorp-control-room-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/robocorp/refs/heads/main/rules/robocorp-control-room-rules.yml
        type: SpectralRules
      - url: https://raw.githubusercontent.com/api-evangelist/robocorp/refs/heads/main/capabilities/automation-orchestration.yaml
        type: NaftikoCapabilities
      - url: https://raw.githubusercontent.com/api-evangelist/robocorp/refs/heads/main/json-schema/robocorp-process-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/robocorp/refs/heads/main/json-schema/robocorp-work-item-schema.json
        type: JSONSchema
    contact:
      - FN: Robocorp Support
        url: https://robocorp.com/docs
    features:
      - Workspace Management
      - Worker Management
      - Worker Group Management
      - Process Definition
      - Process Execution
      - Process Run Monitoring
      - Step Run Outputs
      - Work Item Management
      - Asset Storage
      - Vault Secrets
      - Webhook Configuration
      - Task Package Deployment
      - Link Token Generation
    useCases:
      - RPA bot orchestration
      - Automation workflow scheduling
      - Work item queue management
      - Secret credential management
      - Process monitoring and debugging
      - CI/CD pipeline integration
    solutions:
      - RPA Orchestration
      - Workflow Automation
      - Bot Management
  - aid: robocorp:rpa-framework
    name: RPA Framework
    description: The RPA Framework is an open-source collection of Python libraries for robotic process automation designed for use with Robot Framework and Python. It includes libraries for browser automation, desktop automation, Excel, email, PDF, Windows UI, cloud service integrations, and more.
    humanURL: https://rpaframework.org/
    tags:
      - RPA
      - Python
      - Open Source
      - Libraries
    properties:
      - url: https://rpaframework.org/
        type: Documentation
      - url: https://github.com/robocorp/rpaframework
        type: GitHub
common:
  - type: Website
    url: https://robocorp.com
  - type: Documentation
    url: https://robocorp.com/docs
  - type: GitHub
    url: https://github.com/robocorp
  - type: PyPI
    url: https://pypi.org/project/robocorp/
  - type: Blog
    url: https://robocorp.com/blog
  - type: PrivacyPolicy
    url: https://robocorp.com/privacy-policy
  - type: TermsOfService
    url: https://robocorp.com/terms-of-service
  - type: Status
    url: https://status.robocorp.com
  - type: Changelog
    url: https://robocorp.com/docs/changelog
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/robocorp/refs/heads/main/json-ld/robocorp-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/robocorp/refs/heads/main/vocabulary/robocorp-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
