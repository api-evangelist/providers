---
aid: automation-anywhere
url: https://raw.githubusercontent.com/api-evangelist/automation-anywhere/refs/heads/main/apis.yml
apis:
- aid: automation-anywhere:control-room-api
  name: Automation Anywhere Control Room API
  tags:
  - Automation
  - Bot Management
  - Enterprise
  - REST
  - RPA
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://automationanywhere-be-prod.automationanywhere.com
  humanURL: https://docs.automationanywhere.com/bundle/enterprise-v2019/page/enterprise-cloud/topics/control-room/control-room-api/cloud-control-room-apis.html
  properties:
  - url: https://docs.automationanywhere.com/bundle/enterprise-v2019/page/enterprise-cloud/topics/control-room/control-room-api/cloud-control-room-apis.html
    type: Documentation
  - url: openapi/automation-anywhere-control-room-openapi.yml
    type: OpenAPI
  description: The Automation Anywhere Control Room API is a comprehensive set of RESTful APIs that enable programmatic management and administration of the Automation 360 RPA platform. It provides endpoints across multiple versioned groups covering authentication, user management, credential vault, repository management, device pools, licensing, policy management, and scheduled automations.
- aid: automation-anywhere:bot-deploy-api
  name: Automation Anywhere Bot Deploy API
  tags:
  - Automation
  - Bot Deployment
  - Enterprise
  - Orchestration
  - RPA
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://automationanywhere-be-prod.automationanywhere.com
  humanURL: https://docs.automationanywhere.com/bundle/enterprise-v2019/page/deploy-api-supported-v4.html
  properties:
  - url: https://docs.automationanywhere.com/bundle/enterprise-v2019/page/deploy-api-supported-v4.html
    type: Documentation
  - url: openapi/automation-anywhere-bot-deploy-openapi.yml
    type: OpenAPI
  - url: json-schema/automation-anywhere-deployment-schema.json
    type: JSONSchema
  description: The Automation Anywhere Bot Deploy API (v3/v4) enables external applications and workflows to programmatically trigger the deployment of bots to unattended Bot Runner devices. It supports deploying bots from the public workspace, specifying target devices or device pools, and passing input variables at runtime. This API is typically combined with the Authentication API to obtain a JWT token before invoking deployment endpoints.
- aid: automation-anywhere:workload-management-api
  name: Automation Anywhere Workload Management API
  tags:
  - Automation
  - Queues
  - RPA
  - Work Items
  - Workload Management
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://automationanywhere-be-prod.automationanywhere.com
  humanURL: https://docs.automationanywhere.com/bundle/enterprise-v2019/page/wlm-api-supported-v4.html
  properties:
  - url: https://docs.automationanywhere.com/bundle/enterprise-v2019/page/wlm-api-supported-v4.html
    type: Documentation
  - url: openapi/automation-anywhere-workload-management-openapi.yml
    type: OpenAPI
  - url: json-schema/automation-anywhere-work-item-schema.json
    type: JSONSchema
  description: The Automation Anywhere Workload Management API provides programmatic control over work item queues used to distribute high-volume automation workloads across multiple Bot Runner devices. Developers can create and manage work item models and queues, add or update individual work items, and retrieve queue status and processing results. This API enables enterprise systems such as ERP, CRM, and BPM platforms to feed structured data into RPA queues and track processing outcomes in real time.
- aid: automation-anywhere:bot-insight-api
  name: Automation Anywhere Bot Insight API
  tags:
  - Analytics
  - Bot Monitoring
  - Business Intelligence
  - Reporting
  - RPA
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://automationanywhere-be-prod.automationanywhere.com
  humanURL: https://docs.automationanywhere.com/bundle/enterprise-v11.3/page/enterprise/topics/bot-insight/user/bot-insight-apis.html
  properties:
  - url: https://docs.automationanywhere.com/bundle/enterprise-v11.3/page/enterprise/topics/bot-insight/user/bot-insight-apis.html
    type: Documentation
  - url: openapi/automation-anywhere-bot-insight-openapi.yml
    type: OpenAPI
  description: The Automation Anywhere Bot Insight API exposes real-time business process analytics and operational intelligence data collected during bot execution. It allows developers to retrieve KPIs, bot run histories, performance rankings, and failure analytics from the Control Room programmatically. Results are paginated in sets of 1000 records and can be filtered by date ranges in ISO 8601 format.
- aid: automation-anywhere:api-task-execution-api
  name: Automation Anywhere API Task Execution API
  tags:
  - API Task
  - Automation
  - Bot Execution
  - Integration
  - RPA
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://automationanywhere-be-prod.automationanywhere.com
  humanURL: https://docs.automationanywhere.com/bundle/enterprise-v2019/page/api-task-real-time-endpoint.html
  properties:
  - url: https://docs.automationanywhere.com/bundle/enterprise-v2019/page/api-task-real-time-endpoint.html
    type: Documentation
  - url: openapi/automation-anywhere-api-task-execution-openapi.yml
    type: OpenAPI
  description: The Automation Anywhere API Task Execution API enables developers to invoke API Tasks — a specialized type of bot designed to be called synchronously from external applications like a REST service. It generates execution URLs and tokens that allow applications to trigger a bot task, pass input parameters, and receive output values in a single request-response cycle.
- aid: automation-anywhere:credential-vault-api
  name: Automation Anywhere Credential Vault API
  tags:
  - Credentials
  - Enterprise
  - RPA
  - Secrets Management
  - Security
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://automationanywhere-be-prod.automationanywhere.com
  humanURL: https://docs.automationanywhere.com/bundle/enterprise-v2019/page/cv-api-supported.html
  properties:
  - url: https://docs.automationanywhere.com/bundle/enterprise-v2019/page/cv-api-supported.html
    type: Documentation
  - url: openapi/automation-anywhere-credential-vault-openapi.yml
    type: OpenAPI
  description: The Automation Anywhere Credential Vault API provides programmatic access to the Control Room's centralized secrets management system. It supports creating, reading, updating, and deleting credentials, credential attributes, Lockers, and Locker Keys used by bots during execution. Credentials stored in the Vault are encrypted and access-controlled through role-based permissions, ensuring bots can retrieve sensitive values such as passwords and API keys without exposing them in automation scripts.
- aid: automation-anywhere:package-sdk
  name: Automation Anywhere Package SDK
  tags:
  - Bot Development
  - Custom Packages
  - Extensions
  - Java
  - SDK
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.example.com
  humanURL: https://docs.automationanywhere.com/bundle/enterprise-v2019/page/enterprise-cloud/topics/developer/cloud-create-package-overview.html
  properties:
  - url: https://docs.automationanywhere.com/bundle/enterprise-v2019/page/enterprise-cloud/topics/developer/cloud-create-package-overview.html
    type: Documentation
  description: The Automation Anywhere Package SDK is a Java-based development toolkit that enables developers to build custom action packages and triggers for the Automation 360 bot editor. Developers use the SDK in a Java IDE to implement custom actions, compile the code into a JAR file, and upload the resulting package to the Control Room for use in bot workflows.
- aid: automation-anywhere:repository-management-api
  name: Automation Anywhere Repository Management API
  tags:
  - Bot Lifecycle
  - DevOps
  - File Management
  - Repository
  - RPA
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://automationanywhere-be-prod.automationanywhere.com
  humanURL: https://docs.automationanywhere.com/bundle/enterprise-v2019/page/repository-management-api.html
  properties:
  - url: https://docs.automationanywhere.com/bundle/enterprise-v2019/page/repository-management-api.html
    type: Documentation
  - url: openapi/automation-anywhere-repository-management-openapi.yml
    type: OpenAPI
  - url: json-schema/automation-anywhere-bot-schema.json
    type: JSONSchema
  description: The Automation Anywhere Repository Management API provides programmatic access to the Control Room's bot and file repository. It allows developers and administrators to list, search, upload, and manage bots, folders, and dependent files stored in both the public and private workspaces. This API supports bot lifecycle management use cases including automated promotion of bots between environments, bulk file operations, and integration with source control systems.
name: Automation Anywhere
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The Automation Anywhere Control Room provides APIs that enable you to customize how you (and your automations) interact with Automation Anywhere.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

