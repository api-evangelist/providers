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
    baseURL: https://api.zapier.com
    properties:
      - url: https://raw.githubusercontent.com/api-evangelist/zapier/refs/heads/main/openapi/zapier-partner-api.yml
        type: OpenAPI
      - url: https://api.zapier.com/schema
        type: OpenAPI
        title: Live OpenAPI
      - url: https://zapier.com/developer-platform/workflow-api
        type: Documentation
      - url: https://zapier.com/developer-platform/embed-tools
        type: Documentation
      - url: https://zapier.com/blog/zapier-partner-api-overview/
        type: BlogPost
      - url: https://zapier.com/developer-platform/partner-embeds
        type: UseCases
      - url: https://raw.githubusercontent.com/api-evangelist/zapier/refs/heads/main/json-schema/
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/zapier/refs/heads/main/json-structure/
        type: JSONStructure
      - url: https://raw.githubusercontent.com/api-evangelist/zapier/refs/heads/main/json-ld/zapier-partner-api-context.jsonld
        type: JSON-LD
      - url: https://raw.githubusercontent.com/api-evangelist/zapier/refs/heads/main/examples/
        type: Example
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
  - url: https://status.zapier.com
    name: Zapier Status
    type: StatusPage
    description: 'null'
  - url: https://community.zapier.com
    name: Zapier Community
    type: Forum
    description: 'null'
  - url: https://zapier.com/legal
    name: Legal at Zapier
    type: TermsOfService
    description: 'null'
  - url: https://zapier.com/legal/data-privacy
    name: Data Privacy Overview | Zapier
    type: PrivacyPolicy
    description: 'null'
  - url: https://zapier.com/developer-platform/tos
    name: Zapier Developer Platform Terms
    type: TermsOfService
    description: 'null'
  - url: https://zapier.com/developer-platform
    name: Zapier Developer Platform
    type: DeveloperPortal
    description: 'null'
  - url: https://zapier.com/developer-platform/partner-program
    name: Zapier Integration Partner Program
    type: PartnerProgram
    description: 'null'
  - url: https://github.com/zapier/zapier-platform
    name: Zapier Platform SDK - GitHub
    type: GitHubOrg
    description: 'null'
  - url: https://zapier.github.io/zapier-platform-schema/build/schema.html
    name: Zapier Platform Schema Documentation
    type: Schema
    description: 'null'
  - url: https://zapier.com/developer-platform/partner-embeds
    name: Zapier Partner Embed Gallery
    type: UseCases
    description: 'null'
  - url: https://raw.githubusercontent.com/api-evangelist/zapier/refs/heads/main/rules/zapier-rules.yml
    name: Zapier Spectral Ruleset
    type: SpectralRules
  - url: https://raw.githubusercontent.com/api-evangelist/zapier/refs/heads/main/vocabulary/zapier-vocabulary.yml
    name: Zapier Vocabulary
    type: Vocabulary
  - url: https://raw.githubusercontent.com/api-evangelist/zapier/refs/heads/main/capabilities/zapier-workflow.yaml
    name: Zapier Workflow Capability
    type: NaftikoCapability
  - url: https://raw.githubusercontent.com/api-evangelist/zapier/refs/heads/main/json-schema/zapier-platform-schema.json
    name: Zapier Platform Schema
    type: JSONSchema
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
      - 'Free: 100 tasks/mo, two-step Zaps, Copilot (daily limit)'
      - 'Professional at $19.99/mo: multi-step Zaps, premium apps, webhooks'
      - 'Team at $69/mo: 25 users, SAML SSO, shared Zaps'
      - 'Enterprise custom: unlimited users, advanced admin, TAM'
      - 8,000+ app integrations
      - 'Polling intervals: 15min Free, 2min Pro, 1min Team/Enterprise'
      - Task = one successful action in a Zap
      - Webhooks (Pro+)
      - Tables for data storage
      - Forms for data capture
      - Interfaces for app building (separate)
      - Chatbots and AI assistants (separate)
      - Zapier Copilot AI assistant
      - Custom integrations via Developer Platform (Zapier CLI)
      - Error handling, paths, filters, formatters
      - Webhook payload size 10 MB
    name: Features
    type: Features
    sources:
      - https://zapier.com/pricing
    updated: '2026-05-04'
created: '2025-06-06T00:00:00.000Z'
modified: '2026-05-04'
position: Consuming
segments:
  - iPaaS
  - Embedded_iPaaS
description: Zapier is an automation platform that connects different apps and services to automate workflows without requiring coding knowledge. It acts as a bridge between thousands of popular applications like Gmail, Slack, Salesforce, Google Sheets, Trello, and many others.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
