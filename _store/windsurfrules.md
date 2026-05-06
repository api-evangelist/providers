---
aid: windsurfrules
name: Windsurf
description: Windsurf (formerly Codeium) is an AI-native code editor featuring Cascade, an autonomous AI agent that can plan multi-step code changes, execute terminal commands, read linter output, and modify files across entire projects. The .windsurfrules file format provides project-specific configuration for the Cascade AI assistant, defining coding conventions, standards, and behavioral instructions. Windsurf offers an Enterprise API for querying code completion analytics, Cascade AI usage, billing configuration, and team management.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Agents
  - AI Copilot
  - Coding Standards
  - Developer Workflow
  - IDE
  - Windsurf
created: '2025'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/windsurfrules/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: windsurfrules:windsurf-enterprise-api
    name: Windsurf Enterprise API
    description: The Windsurf Enterprise API provides programmatic access to analytics, usage data, billing configuration, and team management for enterprise customers. It enables teams to query code completion usage, Cascade AI analytics, billing configurations, and credit balances. Available for Enterprise plans only. Authentication uses service keys.
    humanURL: https://docs.windsurf.com/plugins/accounts/api-reference/api-introduction
    baseURL: https://server.codeium.com/api/v1
    tags:
      - AI Analytics
      - Enterprise
      - Billing
      - Teams
    properties:
      - type: Documentation
        url: https://docs.windsurf.com/plugins/accounts/api-reference/api-introduction
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/windsurfrules/refs/heads/main/openapi/windsurf-enterprise-openapi.yml
common:
  - type: Website
    url: https://windsurf.com
  - type: Documentation
    url: https://docs.windsurf.com
  - type: APIReference
    url: https://docs.windsurf.com/plugins/accounts/api-reference/api-introduction
  - type: Changelog
    url: https://windsurf.com/changelog
  - type: Blog
    url: https://windsurf.com/blog
  - type: Pricing
    url: https://windsurf.com/pricing
  - type: Download
    url: https://windsurf.com/download
  - type: GitHubOrg
    url: https://github.com/Exafunction
  - type: GitHubRepo
    url: https://github.com/Exafunction/windsurf.nvim
  - type: VSCodeExtension
    url: https://marketplace.visualstudio.com/items?itemName=Codeium.CodeiumVS
  - type: X
    url: https://x.com/codeiumdev
  - type: Discord
    url: https://discord.gg/3XFf78nAx5
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/windsurfrules/refs/heads/main/json-ld/windsurfrules-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/windsurfrules/refs/heads/main/vocabulary/windsurfrules-vocabulary.yml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/windsurfrules/refs/heads/main/capabilities/analytics-and-billing.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
