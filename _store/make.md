---
aid: make
name: Make
segments:
  - Workflows
description: Make (formerly Integromat) is a visual scenario-based automation builder with advanced data transformation and routing logic.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - Integration
  - iPaaS
  - No-Code
  - Scenarios
  - Workflows
created: '2026-03-03'
modified: '2026-05-04'
url: https://raw.githubusercontent.com/api-evangelist/make/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: make:make-api
    name: Make API
    description: The Make REST API allows using HTTP requests to access Make data and control the Make platform without opening its graphical interface. It provides endpoints for managing scenarios, connections, organizations, teams, users, webhooks, data stores, data structures, custom functions, templates, AI agents, and more.
    humanURL: https://developers.make.com/api-documentation
    baseURL: https://us1.make.com/api/v2
    tags:
      - Automation
      - REST API
      - Scenarios
      - Workflows
    properties:
      - type: Documentation
        url: https://developers.make.com/api-documentation
      - type: GettingStarted
        url: https://developers.make.com/api-documentation/getting-started
      - type: APIReference
        url: https://developers.make.com/api-documentation/api-reference
  - aid: make:custom-apps
    name: Make Custom Apps
    description: The Make Custom Apps platform enables developers to create their own applications for the Make automation platform using the Apps Editor or the VS Code extension. It provides documentation for building modules, connections, webhooks, RPCs, and functions for custom integrations.
    humanURL: https://developers.make.com/custom-apps-documentation
    tags:
      - Custom Apps
      - Extensions
      - Integrations
      - SDK
    properties:
      - type: Documentation
        url: https://developers.make.com/custom-apps-documentation
  - aid: make:mcp-server
    name: Make MCP Server
    description: The Make MCP Server allows AI systems such as large language models to run scenarios and manage the contents of a Make account using the Model Context Protocol (MCP) standard. It is available as a cloud-hosted server running via Streamable HTTP and Server-Sent Events.
    humanURL: https://developers.make.com/mcp-server
    tags:
      - Agents
      - AI
      - Automation
      - MCP
    properties:
      - type: Documentation
        url: https://developers.make.com/mcp-server
  - aid: make:white-label
    name: Make White Label
    description: Make White Label provides OEM customers with the ability to manage and administrate their own white-labeled instance of Make, including rebranding appearance, managing user access roles, creating organizations and teams, and configuring custom domains.
    humanURL: https://developers.make.com/white-label-documentation
    tags:
      - Enterprise
      - OEM
      - White Label
    properties:
      - type: Documentation
        url: https://developers.make.com/white-label-documentation
common:
  - type: Portal
    url: https://developers.make.com/
  - type: GettingStarted
    url: https://developers.make.com/api-documentation/getting-started
  - type: Blog
    url: https://www.make.com/en/blog
  - type: Login
    url: https://www.make.com/en/login
  - type: SignUp
    url: https://www.make.com/en/register
  - type: Pricing
    url: https://www.make.com/en/pricing
  - type: HelpCenter
    url: https://help.make.com/
  - type: StatusPage
    url: https://status.make.com/
  - type: Security
    url: https://www.make.com/en/security
  - type: PrivacyPolicy
    url: https://www.make.com/en/privacy-notice
  - type: TermsOfService
    url: https://www.make.com/en/terms-and-conditions
  - type: Community
    url: https://community.make.com/
  - type: Academy
    url: https://academy.make.com/
  - type: GitHubOrg
    url: https://github.com/integromat
  - type: TypeScriptSDK
    url: https://github.com/integromat/make-typescript-sdk
  - type: VSCodeExtension
    url: https://github.com/integromat/vscode-apps-sdk
  - type: GDPR
    url: https://www.make.com/en/privacy-and-gdpr
  - type: Features
    data:
      - 'Free: 1,000 ops/month, 15-min minimum scheduling'
      - 'Core $12/mo: 10K ops, unlimited scenarios, minute scheduling'
      - 'Pro $21/mo: priority execution, custom variables, log search'
      - 'Teams $38/mo: team roles, shared templates'
      - 'Enterprise: custom functions, advanced security, 24/7 support'
      - 3,000+ pre-built apps
      - Visual scenario builder with routers and filters
      - Make API on Core+ at 60 req/min/org
      - 'Webhook scenarios: 100 req/sec'
      - Make AI Tools (formerly Make Apps Cloud)
      - Make Bridge for embedded iPaaS
      - Custom apps via Make App Builder
      - Conditional logic (routers, filters, iterators)
      - Aggregators for batched processing
      - Error handlers per module
      - OAuth + API tokens
    sources:
      - https://www.make.com/en/pricing
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
