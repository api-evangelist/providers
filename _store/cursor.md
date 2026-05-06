---
aid: cursor
name: Cursor
description: Cursor is an AI-powered code editor built on a fork of Visual Studio Code, designed to make developers extraordinarily productive by deeply integrating large language models into the editing, navigation, refactoring, and chat experience. In addition to its consumer and team plans, Cursor exposes an Admin API for enterprise customers to programmatically manage team members, billing groups, audit logs, daily usage data, spending, repo indexing blocklists, and per-user spend limits.
url: https://raw.githubusercontent.com/api-evangelist/cursor/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI
  - AI Editor
  - Code Generation
  - Coding Assistant
  - Copilot
  - Developer Tools
  - LLM
  - Productivity
  - VSCode Fork
created: '2026-01-02'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: cursor:admin-api
    name: Cursor Admin API
    description: The Cursor Admin API allows team and enterprise administrators to programmatically manage members, billing groups, audit logs, daily usage data, spending, repository indexing blocklists, and per-user spend limits. Authentication uses HTTP Basic Authentication with the API key as the username.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://cursor.com/docs/account/teams/admin-api
    baseURL: https://api.cursor.com
    tags:
      - Admin
      - Audit Logs
      - Billing
      - Members
      - Spend
      - Teams
      - Usage
    properties:
      - type: Documentation
        url: https://cursor.com/docs/account/teams/admin-api
      - type: OpenAPI
        url: openapi/cursor-admin-api-openapi.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Website
    url: https://cursor.com
  - type: Documentation
    url: https://cursor.com/docs
  - type: Pricing
    url: https://cursor.com/pricing
  - type: Forum
    url: https://forum.cursor.com
  - type: Changelog
    url: https://cursor.com/changelog
  - type: JSON-LD
    url: json-ld/cursor-context.jsonld
  - type: JSONSchema
    url: json-schema/cursor-member-schema.json
  - type: JSONSchema
    url: json-schema/cursor-daily-usage-schema.json
  - type: JSONSchema
    url: json-schema/cursor-audit-event-schema.json
  - type: Vocabulary
    url: vocabulary/cursor-vocabulary.yml
  - type: Rules
    url: rules/cursor-admin-api-rules.yml
  - type: Capabilities
    url: capabilities/cursor-admin-api-capabilities.yml
---
