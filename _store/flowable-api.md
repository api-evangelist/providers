---
aid: flowable-api
name: Flowable
description: Flowable connects systems, data, and people for faster and smarter process automation, drawing on a long heritage of open source BPM. Flowable provides a model-driven, low-code platform for end-to-end automation of BPMN, CMMN, and DMN processes, delivered through a programmatic Java Process Engine API and a packaged REST API. The Process Engine exposes RepositoryService, RuntimeService, TaskService, IdentityService, HistoryService, ManagementService, FormService, and DynamicBpmnService for managing process definitions, instances, tasks, history, and runtime behavior.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-07'
modified: '2026-04-28'
position: Consumer
tags:
  - Automation
  - BPM
  - BPMN
  - Business Process
  - CMMN
  - DMN
  - Workflows
url: https://raw.githubusercontent.com/api-evangelist/flowable-api/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: flowable-api:process-engine-api
    name: Flowable Process Engine API
    description: 'The Flowable Process Engine API is the primary programmatic interface for interacting with Flowable. From a configured ProcessEngine, applications obtain a set of services that cover the full BPM lifecycle: RepositoryService for deploying and managing process definitions, RuntimeService for starting and signaling process instances, TaskService for human task assignment and completion, IdentityService for users and groups, HistoryService for audit and reporting queries, ManagementService for jobs and engine metadata, FormService for start and task forms, and DynamicBpmnService for runtime modifications. The API supports both fluent typesafe queries and native SQL queries.'
    humanURL: https://www.flowable.com/open-source/docs/bpmn/ch04-API
    baseURL: https://www.flowable.com/open-source/docs/bpmn/
    tags:
      - BPM
      - BPMN
      - Process Engine
      - Workflows
    properties:
      - url: https://www.flowable.com/open-source/docs/bpmn/ch04-API
        type: Documentation
      - url: https://www.flowable.com/open-source/docs/
        type: DocumentationPortal
  - aid: flowable-api:rest-api
    name: Flowable REST API
    description: Flowable also ships a packaged REST API webapp that exposes the Process Engine services over HTTP. The REST API covers process definitions and deployments, process instances and variables, user tasks and forms, history, identity, and engine management, allowing non-Java clients to drive BPMN, CMMN, and DMN processes from any platform.
    humanURL: https://www.flowable.com/open-source/docs/bpmn/
    baseURL: https://www.flowable.com/open-source/docs/bpmn/
    tags:
      - BPM
      - REST
      - Workflows
    properties:
      - url: https://www.flowable.com/open-source/docs/
        type: Documentation
      - url: https://github.com/flowable/flowable-engine
        type: GitHubRepository
common:
  - type: Website
    url: https://www.flowable.com/
  - type: Documentation
    url: https://www.flowable.com/open-source/docs/
  - type: GitHubRepository
    url: https://github.com/flowable/flowable-engine
  - type: GitHubOrganization
    url: https://github.com/flowable
  - type: Blog
    url: https://blog.flowable.org/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
