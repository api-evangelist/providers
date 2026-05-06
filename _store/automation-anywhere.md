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
common:
  - type: Portal
    url: https://developer.automationanywhere.com
  - type: Website
    url: https://www.automationanywhere.com
  - type: Documentation
    url: https://docs.automationanywhere.com
  - type: Authentication
    url: https://docs.automationanywhere.com/bundle/enterprise-v2019/page/enterprise-cloud/topics/control-room/control-room-api/cloud-authentication.html
  - type: TermsOfService
    url: https://www.automationanywhere.com/legal/terms
  - type: PrivacyPolicy
    url: https://www.automationanywhere.com/legal/privacy-policy
  - type: Support
    url: https://support.automationanywhere.com
  - type: Blog
    url: https://www.automationanywhere.com/blog
  - type: JSON-LD
    url: json-ld/automation-anywhere-context.jsonld
  - type: JSONSchema
    url: json-schema/automation-anywhere-bot-schema.json
  - type: JSONSchema
    url: json-schema/automation-anywhere-deployment-schema.json
  - type: JSONSchema
    url: json-schema/automation-anywhere-work-item-schema.json
  - type: Features
    data:
      - name: JWT Authentication
        description: All Control Room APIs use JWT-based authentication. Tokens are obtained via the Authentication API and passed in the X-Authorization or Authorization Bearer header. OAuth 2.0 is supported from v.27 onwards.
      - name: Versioned API Endpoints
        description: APIs are versioned (v1, v2, v3, v4) with backwards compatibility maintained for at least two years. Deprecated endpoints are announced with at least one additional year of availability.
      - name: Swagger UI Explorer
        description: Each Control Room instance exposes a Swagger UI at /swagger/ for interactive API exploration and testing with live credentials.
      - name: API Task Execution
        description: API Tasks allow RPA bots to be exposed as synchronous REST endpoints, enabling external applications to call bots as microservices with input/output parameter exchange.
      - name: Workload Queuing
        description: Work item queues allow high-volume data to be fed into RPA pipelines from ERP, CRM, and BPM systems with status tracking and result retrieval.
  - type: UseCases
    data:
      - name: DevOps Bot Pipeline
        description: Automate bot deployment across dev, test, and production environments using the Bot Deploy and Repository Management APIs in CI/CD pipelines.
      - name: Enterprise System Integration
        description: Connect ERP, CRM, and BPM systems to RPA workload queues to distribute and process high-volume transactional data with Automation Anywhere bots.
      - name: Bot Performance Monitoring
        description: Feed Bot Insight API data into Tableau, Power BI, or Splunk for real-time RPA operational dashboards and business KPI tracking.
      - name: Credential Governance
        description: Programmatically provision and rotate bot credentials in the Credential Vault from enterprise secrets management systems like CyberArk or HashiCorp Vault.
      - name: Custom Action Packages
        description: Build proprietary Java action packages using the Package SDK to extend Automation 360 with custom connectors for legacy or specialized systems.
  - type: Integrations
    data:
      - name: SAP
        description: Pre-built SAP integration package for Automation 360 enabling bots to interact with SAP GUI, SAP BAPIs, and S/4HANA REST APIs.
      - name: Salesforce
        description: Automation Anywhere connector for Salesforce CRM enabling bots to create, update, and query Salesforce records via REST APIs.
      - name: ServiceNow
        description: Integration with ServiceNow for IT service automation including incident creation, ticket routing, and CMDB updates from RPA bots.
      - name: Microsoft Office 365
        description: Action packages for interacting with Microsoft 365 services including Outlook, SharePoint, Teams, and Excel via Microsoft Graph API.
      - name: Blue Prism and UiPath
        description: Migration APIs for moving automations from other RPA platforms to Automation 360 with bot conversion and compatibility tooling.
modified: '2026-04-19'
description: Automation Anywhere is an enterprise robotic process automation (RPA) platform that enables organizations to automate business processes using software bots. Their developer platform, centered around the Automation 360 Control Room, provides a comprehensive suite of REST APIs for managing bot deployment, workload queues, credentials, repositories, and analytics, as well as an SDK for building custom action packages.
---
