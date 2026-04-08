---
aid: mintlify
url: https://raw.githubusercontent.com/api-evangelist/mintlify/refs/heads/main/apis.yml
apis:
- aid: mintlify:mintlify
  name: Mintlify
  tags:
  - Documentation
  humanURL: ' https://www.mintlify.com/'
  properties:
  - url: ' https://www.mintlify.com/'
    type: Documentation
  - url: https://www.mintlify.com/docs/api/introduction
    type: APIReferenceDocumentation
  description: Mintlify is a developer documentation platform that helps product and engineering teams create, maintain, and host modern docs. It uses a docs‑as‑code workflow (Markdown in your repo) with a rich component library and GitHub integration. Mintlify can generate polished API references from OpenAPI/Swagger or Postman, add interactive “Try it” requests and dynamic code samples/SDKs, and includes AI tools (like its Doc Writer) to draft and update docs from your code.
- aid: mintlify:update-api
  name: Mintlify Update API
  tags:
  - Deployment
  - Documentation
  humanURL: https://www.mintlify.com/docs/api/update/trigger
  properties:
  - url: https://www.mintlify.com/docs/api/update/trigger
    type: APIReferenceDocumentation
  description: The Mintlify Update API allows you to programmatically trigger deployment updates for your documentation project and check update status. You can queue a deployment update from your configured deployment branch by calling the trigger endpoint, and then monitor its progress using the status endpoint. This is useful for integrating documentation updates into CI/CD pipelines after updating your OpenAPI document or documentation source. Authentication requires an admin API key with the mint_ prefix.
- aid: mintlify:agent-api
  name: Mintlify Agent API
  tags:
  - AI
  - Automation
  - Documentation
  humanURL: https://www.mintlify.com/docs/api/agent/create-agent-job
  properties:
  - url: https://www.mintlify.com/docs/api/agent/create-agent-job
    type: APIReferenceDocumentation
  description: The Mintlify Agent API enables you to programmatically automate documentation editing through agent jobs. You can create agent jobs that generate and edit documentation based on provided messages and branch information, retrieve the details and current progress of a specific job, or list all jobs for a domain. The agent monitors your codebase, detects changes, and proposes documentation updates automatically. Authentication requires an admin API key with the mint_ prefix.
- aid: mintlify:assistant-api
  name: Mintlify Assistant API
  tags:
  - AI
  - Documentation
  - Search
  humanURL: https://www.mintlify.com/docs/api/assistant/create-assistant-message-v2
  properties:
  - url: https://www.mintlify.com/docs/api/assistant/create-assistant-message-v2
    type: APIReferenceDocumentation
  - url: https://www.mintlify.com/docs/api/assistant/search
    type: APIReferenceDocumentation
  description: The Mintlify Assistant API allows you to embed the AI chat experience grounded in your documentation into any application. You can generate assistant messages trained on your docs and perform semantic and keyword searches across your documentation with configurable filtering and pagination. Responses include citations pointing users to the relevant documentation pages. Authentication requires an assistant API key with the mint_dsc_ prefix, which is safe for frontend implementation.
- aid: mintlify:analytics-api
  name: Mintlify Analytics API
  tags:
  - Analytics
  - Documentation
  humanURL: https://www.mintlify.com/docs/api/introduction
  properties:
  - url: https://www.mintlify.com/docs/api/introduction
    type: APIReferenceDocumentation
  description: The Mintlify Analytics API enables you to export user feedback and assistant conversation history from your documentation for external analysis. You can retrieve user feedback responses and AI assistant chat interaction logs to gain deeper insights into how users engage with your documentation. Authentication requires an admin API key with the mint_ prefix.
name: Mintlify
tags:
- Documentation
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-01-05'
modified: '2026-04-07'
position: Consuming
description: Mintlify is an AI-native intelligent documentation platform designed for the next generation of technical documentation, combining beautiful out-of-the-box design with advanced collaboration and AI capabilities.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
common:
- name: Mintlify - The Intelligent Documentation Platform
  description: 'null'
  url: https://www.mintlify.com/
  type: Website
- name: Customers - Mintlify
  description: 'null'
  url: https://www.mintlify.com/customers
  type: Customers
- name: Blog - Mintlify
  description: 'null'
  url: https://www.mintlify.com/blog
  type: Blog
- name: Pricing - Mintlify
  description: 'null'
  url: https://www.mintlify.com/pricing
  type: Pricing
- name: Introduction - Mintlify Guides
  description: 'null'
  url: https://www.mintlify.com/guides/introduction
  type: Guide
- name: Introduction - Mintlify
  description: 'null'
  url: https://www.mintlify.com/docs/api/introduction
  type: Documentation
- name: Product updates - Mintlify
  description: 'null'
  url: https://www.mintlify.com/docs/changelog
  type: ChangeLog
---

