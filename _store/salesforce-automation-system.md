---
aid: salesforce-automation-system
name: Salesforce Automation System
description: Salesforce Automation System refers to the collection of APIs and tools within Salesforce for automating business processes, including Flow Builder, approval processes, Process Builder, and Workflow Rules. These capabilities enable organizations to automate CRM, sales, marketing, and customer service workflows programmatically via the Salesforce REST API.
type: Index
x-type: company
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Approval Process
  - Automation
  - CRM
  - Flow
  - Process Builder
  - Salesforce
  - Workflow
url: https://raw.githubusercontent.com/api-evangelist/salesforce-automation-system/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: salesforce-automation-system:salesforce-flow-automation-api
    name: Salesforce Flow Automation API
    description: REST API for querying Salesforce Flow definitions via the Tooling API, invoking autolaunched flows as REST actions, and managing approval process submissions and decisions.
    humanURL: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_actions_invocable.htm
    baseURL: https://{instance}.salesforce.com/services/data/v59.0
    tags:
      - Approval Process
      - Automation
      - CRM
      - Flow
      - Salesforce
      - Workflow
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_actions_invocable.htm
      - type: OpenAPI
        url: openapi/salesforce-automation-flow-openapi.yml
      - type: JSONSchema
        url: json-schema/salesforce-flow-definition-schema.json
      - type: JSONSchema
        url: json-schema/salesforce-approval-request-schema.json
      - type: JSONLD
        url: json-ld/salesforce-automation-system-context.jsonld
      - type: SpectralRules
        url: rules/salesforce-automation-system-rules.yml
      - type: Capabilities
        url: capabilities/process-automation.yaml
      - type: Vocabulary
        url: vocabulary/salesforce-automation-system-vocabulary.yml
  - aid: salesforce-automation-system:salesforce-flow-builder
    name: Salesforce Flow Builder
    description: Visual automation tool for building screen flows, autolaunched flows, record-triggered flows, and scheduled flows without code.
    humanURL: https://developer.salesforce.com/docs/atlas.en-us.flow.meta/flow/flow_intro.htm
    tags:
      - Automation
      - Flow
      - No-Code
      - Salesforce
    properties:
      - type: Documentation
        url: https://developer.salesforce.com/docs/atlas.en-us.flow.meta/flow/flow_intro.htm
      - type: Getting Started
        url: https://trailhead.salesforce.com/content/learn/trails/automate_business_processes
  - aid: salesforce-automation-system:salesforce-approval-processes
    name: Salesforce Approval Processes
    description: Multi-step approval automation for routing records through review chains with configurable criteria, approvers, and post-approval actions.
    humanURL: https://help.salesforce.com/s/articleView?id=sf.approvals_landing_page.htm
    tags:
      - Approval
      - Automation
      - CRM
      - Salesforce
    properties:
      - type: Documentation
        url: https://help.salesforce.com/s/articleView?id=sf.approvals_landing_page.htm
      - type: API Reference
        url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_process_approvals.htm
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Developer Portal
    url: https://developer.salesforce.com/
  - type: Documentation
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/
  - type: Trailhead
    url: https://trailhead.salesforce.com/content/learn/trails/automate_business_processes
  - type: Authentication
    url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm
  - type: Blog
    url: https://developer.salesforce.com/blogs
  - type: Status
    url: https://status.salesforce.com/
  - type: Support
    url: https://help.salesforce.com/
  - type: Terms of Service
    url: https://www.salesforce.com/company/legal/agreements/
  - type: Privacy Policy
    url: https://www.salesforce.com/company/privacy/
  - type: GitHub Organization
    url: https://github.com/salesforce
  - type: Community
    url: https://trailhead.salesforce.com/trailblazer-community/topics/salesforcedeveloper
---
