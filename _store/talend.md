---
aid: talend
name: Talend
description: Talend (now part of Qlik) provides data integration, quality, and API management capabilities through cloud-native APIs for ETL, data pipelines, and application integration. The Qlik Talend Cloud platform exposes REST APIs for orchestrating tasks and plans, executing data integration jobs, managing remote engines, configuring connections, monitoring execution history, and administering identities, workspaces, and environments.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Management
  - Data Integration
  - Data Quality
  - ETL
  - Orchestration
  - Pipelines
created: '2026-03-16'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: talend:talend-orchestration-api
    name: Talend Cloud Orchestration API
    description: Manages tasks, plans, schedules, workspaces, environments, connections, artifacts, promotions, and resources in Qlik Talend Cloud. Use this API to automate data integration pipeline management, configure execution schedules, and manage workspace resources via Bearer token authentication.
    humanURL: https://talend.qlik.dev/apis/orchestration/2021-03/
    baseURL: https://api.{region}.cloud.talend.com
    tags:
      - Artifacts
      - Connections
      - ETL
      - Orchestration
      - Plans
      - Tasks
      - Workspaces
    properties:
      - type: Documentation
        url: https://talend.qlik.dev/apis/orchestration/2021-03/
      - type: Getting Started
        url: https://talend.qlik.dev/getting-started/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/openapi/talend-orchestration-openapi.yml
  - aid: talend:talend-processing-api
    name: Talend Cloud Processing API
    description: Manages task and plan executions, remote engines and clusters, and run profiles in Qlik Talend Cloud. Use this API to trigger and monitor data integration job runs, manage remote engine lifecycles, and configure execution profiles.
    humanURL: https://talend.qlik.dev/apis/processing/2021-03/
    baseURL: https://api.{region}.cloud.talend.com
    tags:
      - ETL
      - Execution
      - Monitoring
      - Remote Engine
      - Run Profiles
    properties:
      - type: Documentation
        url: https://talend.qlik.dev/apis/processing/2021-03/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/openapi/talend-processing-openapi.yml
  - aid: talend:talend-identities-api
    name: Talend Cloud Identities Management API
    description: Manages user, group, and role identity information for Talend Cloud accounts. Supports SCIM v2 for automated provisioning from enterprise identity providers.
    humanURL: https://talend.qlik.dev/apis/identities-management/2021-03/
    baseURL: https://api.{region}.cloud.talend.com
    tags:
      - Identity Management
      - SCIM
      - User Provisioning
    properties:
      - type: Documentation
        url: https://talend.qlik.dev/apis/identities-management/2021-03/
  - aid: talend:talend-audit-logs-api
    name: Talend Cloud Audit Logs API
    description: Load account audit logs for monitoring activities on Talend Cloud applications, ensuring data security and regulatory compliance.
    humanURL: https://talend.qlik.dev/apis/audit-logs/2021-03/
    baseURL: https://api.{region}.cloud.talend.com
    tags:
      - Audit
      - Compliance
      - Monitoring
    properties:
      - type: Documentation
        url: https://talend.qlik.dev/apis/audit-logs/2021-03/
  - aid: talend:talend-connections-api
    name: Talend Cloud Connections API
    description: Administers connections used by datasets and crawlers to retrieve data at scale.
    humanURL: https://talend.qlik.dev/apis/connections/2021-03/
    baseURL: https://api.{region}.cloud.talend.com
    tags:
      - Connections
      - Data Sources
    properties:
      - type: Documentation
        url: https://talend.qlik.dev/apis/connections/2021-03/
  - aid: talend:talend-execution-logs-api
    name: Talend Cloud Execution Logs API
    description: Retrieve logs about task runs for debugging and monitoring data integration pipeline executions.
    humanURL: https://talend.qlik.dev/apis/execution-logs/2021-03/
    baseURL: https://api.{region}.cloud.talend.com
    tags:
      - Execution Logs
      - Monitoring
    properties:
      - type: Documentation
        url: https://talend.qlik.dev/apis/execution-logs/2021-03/
common:
  - type: Portal
    url: https://talend.qlik.dev/
  - type: Documentation
    url: https://talend.qlik.dev/
  - type: APIs
    url: https://talend.qlik.dev/apis/
  - type: Getting Started
    url: https://talend.qlik.dev/getting-started/
  - type: Website
    url: https://www.talend.com/
  - type: Qlik Data Fabric
    url: https://www.qlik.com/us/products/talend-data-fabric
  - type: GitHub Org
    url: https://github.com/Talend
  - type: Help
    url: https://help.qlik.com/en-US/cloud-services/Content/Sense_Helpsites/Home-talend-cloud.htm
  - type: JSON Schema
    url: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/json-schema/talend-task-schema.json
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/talend/refs/heads/main/vocabulary/talend-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
