---
aid: rundeck
name: Rundeck
description: Rundeck is an open source runbook automation service with a web console, command line tools, and a REST WebAPI. It enables IT teams to easily run automation tasks across a set of nodes, providing self-service operations, job scheduling, and execution history. Rundeck is developed by PagerDuty and supports enterprise runbook automation with role-based access control, multi-tenant project management, and integrations with popular DevOps tools including Jenkins, Ansible, Chef, and Puppet. The REST API is versioned and supports authentication via API tokens, password-based session tokens, and JWT (commercial).
type: Index
position: Consumer
access: 3rd-Party
image: https://www.rundeck.com/hubfs/Assets/Images/logos/rundeck-logo-black.png
tags:
  - Automation
  - DevOps
  - Job Scheduling
  - Orchestration
  - Workflow
  - Runbook
  - Open Source
  - IT Operations
url: https://raw.githubusercontent.com/api-evangelist/rundeck/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: rundeck:rundeck-api
    name: Rundeck API
    description: The Rundeck REST API provides programmatic access to job execution, project management, node management, execution history, user management, ACL policies, system administration, cluster operations, and log storage. The current API version is 58, with a base URL of $RUNDECK_SERVER_URL/api/58. Authentication is performed via X-Rundeck-Auth-Token header or authtoken query parameter. The API returns JSON responses and supports webhook integrations for event-driven automation workflows.
    humanURL: https://docs.rundeck.com/docs/api/
    baseURL: http://localhost:4440/api
    tags:
      - Automation
      - DevOps
      - Job Scheduling
      - Orchestration
      - Workflow
      - Projects
      - Executions
      - Jobs
      - Nodes
    properties:
      - type: Documentation
        url: https://docs.rundeck.com/docs/api/
      - type: OpenAPI
        url: openapi/rundeck-openapi.yml
      - type: Authentication
        url: https://docs.rundeck.com/docs/api/#authentication
      - type: Versioning
        url: https://docs.rundeck.com/docs/api/#api-versioning
      - type: GitHub Repository
        url: https://github.com/rundeck/rundeck-api-specs
      - type: Spectral Rules
        url: rules/rundeck-rules.yml
      - type: Vocabulary
        url: vocabulary/rundeck-vocabulary.yml
      - type: JSONSchema
        url: json-schema/rundeck-job-schema.json
      - type: JSONStructure
        url: json-structure/rundeck-job-structure.json
      - type: JSONLD
        url: json-ld/rundeck-context.jsonld
      - type: NaftikoCapability
        url: capabilities/runbook-automation.yaml
common:
  - type: Website
    url: https://www.rundeck.com
  - type: Documentation
    url: https://docs.rundeck.com
  - type: GitHub Organization
    url: https://github.com/rundeck
  - type: GitHub Repository
    url: https://github.com/rundeck/rundeck
  - type: Blog
    url: https://www.rundeck.com/blog
  - type: Community
    url: https://community.rundeck.com
  - type: Download
    url: https://www.rundeck.com/downloads
  - type: Support
    url: https://www.rundeck.com/support
  - type: Pricing
    url: https://www.rundeck.com/pricing
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
