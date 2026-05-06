---
name: Salesforce Flow
description: The Salesforce Flow API enables developers to interact with and manage Salesforce Flow automation processes programmatically. This includes creating, updating, querying, and executing flows within Salesforce using the REST API, Tooling API, and Invocable Actions framework.
image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_flow.htm
created: 2024-01-15T00:00:00.000Z
modified: '2026-05-02'
specificationVersion: '0.18'
tags:
  - Automation
  - Business Process
  - CRM
  - Flow
  - Process Builder
  - Salesforce
  - Workflow
apis:
  - name: Salesforce Flow REST API
    description: REST API for managing and executing Salesforce Flows programmatically. Enables creating, updating, querying, and executing flow automation processes, flow interviews, and invocable actions within Salesforce.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
    humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_flow.htm
    baseURL: https://yourInstance.salesforce.com/services/data/v59.0
    tags:
      - Automation
      - Flow
      - REST
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_flow.htm
      - type: OpenAPI
        url: openapi/salesforce-flow-rest-api-openapi.yml
      - type: Authentication
        url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm
    contact:
      - type: Support
        url: https://help.salesforce.com/
  - name: Salesforce Tooling API (Flow)
    description: Tooling API endpoints for managing Flow definitions and metadata. Supports deployment, retrieval, and management of Flow versions.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
    humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/
    baseURL: https://yourInstance.salesforce.com/services/data/v59.0/tooling
    tags:
      - Flow Definition
      - Metadata
      - Tooling
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.api_tooling.meta/api_tooling/tooling_api_objects_flow.htm
  - name: Salesforce Flow Interviews API
    description: API for executing and managing Flow interviews (instances). Provides endpoints to start, resume, pause, and monitor flow execution state.
    image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
    humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_actions_invocable_flow.htm
    baseURL: https://yourInstance.salesforce.com/services/data/v59.0/actions/custom/flow
    tags:
      - Execution
      - Flow Interview
      - Runtime
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_actions_invocable_flow.htm
common:
  - type: Portal
    url: https://developer.salesforce.com/
  - type: Getting Started
    url: https://trailhead.salesforce.com/content/learn/modules/flow-builder
  - type: Authentication
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm
  - type: Rate Limits
    url: https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm
  - type: Status
    url: https://status.salesforce.com/
  - type: Terms of Service
    url: https://www.salesforce.com/company/legal/agreements/
  - type: Privacy Policy
    url: https://www.salesforce.com/company/privacy/
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.flow.meta/flow/
  - type: Trailhead Learning
    url: https://trailhead.salesforce.com/content/learn/modules/flow-builder
  - type: GitHub Organization
    url: https://github.com/salesforce
  - type: Spectral Rules
    url: rules/salesforce-flow-rules.yml
  - type: Capabilities
    url: capabilities/flow-automation.yaml
  - type: JSON Schema
    url: json-schema/salesforce-flow-flow-definition-schema.json
    title: Flow Definition Schema
  - type: JSON Schema
    url: json-schema/salesforce-flow-flow-interview-schema.json
    title: Flow Interview Schema
  - type: JSON-LD Context
    url: json-ld/salesforce-flow-context.jsonld
  - type: Vocabulary
    url: vocabulary/salesforce-flow-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
include: []
---
