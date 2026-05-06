---
aid: conductor
name: Conductor
description: Conductor allows you to build a complex application using simple and granular tasks that do not need to be aware of or keep track of the state of your application's execution flow. Conductor keeps track of the state, calls tasks in the right order (sequentially or in parallel, as defined by you), retry calls if needed, handle failure scenarios gracefully, and outputs the final result.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/conductor/refs/heads/main/apis.yml
tags:
  - Automation
  - Orchestration
  - State
  - Tasks
  - Workflows
type: Contract
access: 3rd-Party
created: '2025-01-08'
modified: '2026-04-18'
specificationVersion: '0.19'
position: Consuming
apis:
  - aid: conductor:conductor
    name: Conductor
    description: Conductor allows you to build a complex application using simple and granular tasks that do not need to be aware of or keep track of the state of your application's execution flow. Conductor keeps track of the state, calls tasks in the right order (sequentially or in parallel, as defined by you), retry calls if needed, handle failure scenarios gracefully, and outputs the final result.
    humanURL: https://conductor-oss.github.io/conductor/documentation/api/workflow.html
    tags:
      - Automation
      - Orchestration
      - State
      - Tasks
    properties:
      - type: Documentation
        url: https://conductor-oss.github.io/conductor/documentation/api/workflow.html
      - type: OpenAPI
        url: openapi/conductor-conductor-openapi.yml
      - type: AsyncAPI
        url: asyncapi/conductor-conductor-asyncapi.yml
      - type: JSONSchema
        url: json-schema/workflow-def.json
      - type: JSONSchema
        url: json-schema/task-def.json
      - type: JSONSchema
        url: json-schema/workflow-execution.json
      - type: JSONSchema
        url: json-schema/event-handler.json
      - type: JSONLD
        url: json-ld/conductor-context.jsonld
      - type: JSONLD
        url: json-ld/conductor-conductor-context.jsonld
common:
  - type: GitHubRepository
    url: https://github.com/conductor-oss/conductor
  - type: SpectralRules
    url: rules/conductor-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/conductor-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/workflow-orchestration.yaml
  - type: Features
    data:
      - name: Workflow Orchestration
        description: Define and execute complex workflows with sequential and parallel task execution.
      - name: Task Management
        description: Register, poll, and update granular task definitions with timeout and retry policies.
      - name: Event Handling
        description: Create event handlers to trigger workflows or tasks based on external events.
      - name: Workflow Search
        description: Search and filter workflow executions by status, type, and custom parameters.
      - name: Fault Tolerance
        description: Automatic retries, pause/resume, and graceful failure handling for long-running workflows.
      - name: Workflow Lifecycle Control
        description: Pause, resume, restart, retry, and terminate workflows programmatically.
  - type: UseCases
    data:
      - name: Microservices Orchestration
        description: Coordinate complex business processes across distributed microservices without tight coupling.
      - name: Data Pipeline Automation
        description: Build and manage ETL and data processing pipelines with dependency tracking and error recovery.
      - name: Order Processing
        description: Manage multi-step order fulfillment workflows including payment, inventory, and shipping.
      - name: CI/CD Pipelines
        description: Orchestrate build, test, and deployment workflows with conditional logic and parallel execution.
  - type: Integrations
    data:
      - name: Apache Kafka
        description: Trigger workflows and tasks from Kafka events using event handler subscriptions.
      - name: Amazon SQS
        description: Integrate with SQS for message-driven workflow initiation and task completion.
      - name: Docker
        description: Run Conductor server and workers in containerized environments for scalable deployment.
      - name: Orkes Cloud
        description: Use managed Conductor service from Orkes for enterprise-grade orchestration without infrastructure management.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
