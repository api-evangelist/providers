---
aid: salesforce-flow
url: https://raw.githubusercontent.com/api-evangelist/salesforce-flow/refs/heads/main/apis.yml
apis:
- name: Salesforce Flow REST API
  description: REST API for managing and executing Salesforce Flows.
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
  - type: Authentication
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm
  contact:
  - type: Support
    url: https://help.salesforce.com/
- name: Salesforce Tooling API (Flow)
  description: Tooling API endpoints for managing Flow definitions and metadata.
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
  description: API for executing and managing Flow interviews (instances).
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
name: Salesforce Flow
tags:
- Automation
- Business Process
- CRM
- Flow
- Process Builder
- Salesforce
- Workflow
type: Contract
image: https://www.salesforce.com/content/dam/web/en_us/www/images/nav/logo-salesforce.svg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The Salesforce Flow API enables developers to interact with and manage Salesforce Flow automation processes programmatically. This includes creating, updating, querying, and executing flows within Salesforce.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

