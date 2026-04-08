---
aid: zapier
url: https://raw.githubusercontent.com/api-evangelist/zapier/refs/heads/main/apis.yml
apis:
- aid: zapier:zapier
  name: Zapier
  tags:
  - Integrations
  - iPaaS
  humanURL: ' https://zapier.com/'
  properties:
  - url: ' https://zapier.com/'
    type: Documentation
  - url: https://docs.zapier.com/platform/home
    type: Documentation
  - url: https://zapier.com/developer-platform/integrations
    type: GettingStarted
  - url: https://developer.zapier.com/
    type: Portal
  - url: https://docs.zapier.com/platform/build/apikeyauth
    type: Authentication
  - url: https://github.com/zapier/zapier-platform
    type: GitHubOrg
  description: Build and ship AI workflows in minutesno IT bottlenecks, no complexity. Just results.
- aid: zapier:partner-api
  name: Zapier Partner API
  tags:
  - Embed
  - Integrations
  - iPaaS
  - Partners
  humanURL: https://zapier.com/developer-platform/workflow-api
  properties:
  - url: https://zapier.com/developer-platform/workflow-api
    type: Documentation
  - url: https://zapier.com/developer-platform/embed-tools
    type: Documentation
  - url: https://zapier.com/blog/zapier-partner-api-overview/
    type: BlogPost
  - url: https://zapier.com/developer-platform/partner-embeds
    type: UseCases
  description: The Zapier Partner API and Workflow API allow developers to embed Zapier automation directly in their products, providing complete style control over the user experience. The API supports Zap templates, user Zap management, app directory access, and embedded workflow editors with custom branding, enabling integration marketplaces and in-app automation at enterprise scale.
- aid: zapier:ai-actions-api
  name: Zapier AI Actions API
  tags:
  - AI
  - iPaaS
  - LLM
  - NaturalLanguage
  humanURL: https://actions.zapier.com/
  properties:
  - url: https://actions.zapier.com/
    type: Documentation
  - url: https://docs.zapier.com/platform/reference/ai-actions
    type: Documentation
  description: Zapier AI Actions (formerly Natural Language Actions) provides a universal natural language API optimized for AI and LLM-based experiences. It enables AI platforms and custom integrations to leverage over 20,000 searches and actions across the Zapier ecosystem, handling authentication and API integration automatically. Supported natively on platforms including GPTs, Claude, LangChain, and LlamaIndex.
- aid: zapier:mcp
  name: Zapier MCP
  tags:
  - AI
  - iPaaS
  - MCP
  - ModelContextProtocol
  humanURL: https://zapier.com/mcp
  properties:
  - url: https://zapier.com/mcp
    type: Documentation
  - url: https://docs.zapier.com/mcp/home
    type: Documentation
  - url: https://github.com/zapier/zapier-mcp
    type: GitHubOrg
  description: Zapier MCP (Model Context Protocol) connects AI tools like Claude, ChatGPT, and Cursor to over 8,000 apps using the open Model Context Protocol standard. It provides a server endpoint for connecting a Zapier account to an AI client, with meta-tools available immediately and configurable actions exposed as dedicated tools. Supports API key authentication for personal use and OAuth for multi-user applications.
name: Zapier
tags:
- Integrations
- iPaaS
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
- url: https://zapier.com/
  name: 'Zapier: Automate AI Workflows, Agents, and Apps'
  type: Website
  description: 'null'
- url: https://zapier.com/blog/
  name: Productivity Tips & Workflow Automation Guides | Zapier Blog
  type: Blog
  description: 'null'
- url: https://zapier.com/customer-stories
  name: See automation in action | Zapier customer stories
  type: Customers
  description: 'null'
- url: https://zapier.com/blog/what-are-webhooks/
  name: What are webhooks? | Zapier
  type: Webhooks
  description: 'null'
- url: https://zapier.com/resources/guides
  name: Zapier guides
  type: Guide
  description: 'null'
- url: https://zapier.com/resources/events
  name: Webinars & events | Zapier
  type: Webinars
  description: 'null'
- url: https://help.zapier.com/hc/en-us
  name: Zapier
  type: Support
  description: 'null'
- url: https://zapier.com/experts
  name: Experts Directory
  type: Partners
  description: 'null'
- url: https://zapier.com/l/support
  name: Zapier Customer Support
  type: Support
  description: 'null'
- url: https://zapier.com/l/support-services
  name: Support Services | Zapier
  type: Support
  description: 'null'
- url: https://docs.zapier.com/platform/home
  name: Welcome - Zapier
  type: Documentation
  description: 'null'
- url: https://docs.zapier.com/platform/quickstart/build-integration
  name: Build your integration on Zapier - Zapier
  type: GettingStarted
  description: 'null'
- url: https://docs.zapier.com/platform/quickstart/glossary
  name: Zapier Glossary - Zapier
  type: Glossary
  description: 'null'
- url: https://docs.zapier.com/platform/build-cli/overview
  name: Build with CLI - Zapier
  type: CLI
  description: 'null'
- url: https://docs.zapier.com/platform/reference/forms-app
  name: Zapier integration structure for a forms app - Zapier
  type: UseCases
  description: 'null'
- url: https://zapier.com/app/login?next=%2Fapp%2Fdeveloper%2F
  name: Login | Zapier
  type: Login
  description: 'null'
- url: https://zapier.com/sign-up?next=%2Fapp%2Fdeveloper%2F
  name: Sign up | Zapier
  type: SignUp
  description: 'null'
- url: https://zapier.com/pricing
  name: Plans & Pricing | Zapier
  type: Pricing
  description: 'null'
- data:
  - name: Customer support
  - name: Data management
  - name: Lead management
  - name: Marketing campaigns
  - name: Project management
  - name: Sales pipeline
  - name: Tickets and incidents
  name: Use Cases
  type: UseCases
- data:
  - name: Action Restrictions
  - name: Advanced Admin Permissions
  - name: AI by Zapier
  - name: AI Code Steps
  - name: AI Custom Actions
  - name: AI Troubleshooting
  - name: Alerts
  - name: Analytics
  - name: Annual Task Limits
  - name: App Restriction
  - name: Approval Requests
  - name: Audit Log
  - name: Autoreplay
  - name: Compare Versions
  - name: Copilot
  - name: Custom Data Retention
  - name: Custom Test Records
  - name: Customized Error Settings
  - name: Customized Polling Time
  - name: Domain Capture
  - name: Drafts
  - name: Email Support
  - name: Filters & Paths
  - name: Flood Protection Settings
  - name: Folder Permissions
  - name: Formatter
  - name: Formatter With AI
  - name: Global Variables
  - name: Live Chat
  - name: Observability API
  - name: Owner Access
  - name: Pay-Per-Task Billing
  - name: Polling Time
  - name: Premier Support
  - name: Saml Single Sign-on (SSO)
  - name: Seats
  - name: Shared App Connections
  - name: Shared Zaps
  - name: Static IP
  - name: Steps
  - name: Super Admin
  - name: Technical Account Manager
  - name: Two-Factor Authentication
  - name: Unlimited Premium Apps
  - name: Unlimited Zaps
  - name: User Provisioning (Scim)
  - name: Versions
  - name: Visual Editor
  - name: Webhooks
  - name: Zapier Agents
  - name: Zapier Canvas
  - name: Zapier Chatbots
  - name: Zapier Interfaces
  - name: Zapier Mcp
  - name: Zapier Tables
  name: Features
  type: Features
created: '2025-06-06T00:00:00.000Z'
modified: '2026-04-07'
position: Consuming
description: Zapier is an automation platform that connects different apps and services to automate workflows without requiring coding knowledge. It acts as a bridge between thousands of popular applications like Gmail, Slack, Salesforce, Google Sheets, Trello, and many others.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

