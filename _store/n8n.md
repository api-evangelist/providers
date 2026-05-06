---
aid: n8n
name: N8n
description: Build with the precision of code or the speed of drag-n-drop. Host with on-prem control or in-the-cloud convenience. n8n gives you more freedom to implement multi-step AI agents and integrate apps than any other tool.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/n8n/refs/heads/main/apis.yml
created: '2025-06-06'
modified: '2026-05-04'
specificationVersion: '0.19'
tags:
  - Agents
  - Artificial Intelligence
  - Integrations
apis:
  - aid: n8n:n8n
    name: N8n
    tags:
      - Agents
      - Artificial Intelligence
      - Integrations
    humanURL: https://n8n.io/
    properties:
      - url: https://n8n.io/
        type: Documentation
    description: Build with the precision of code or the speed of drag-n-drop. Host with on-prem control or in-the-cloud convenience. n8n gives you more freedom to implement multi-step AI agents and integrate apps than any other tool.
  - aid: n8n:n8n-rest-api
    name: N8n REST API
    tags:
      - Automation
      - Credentials
      - Executions
      - Workflows
    humanURL: https://docs.n8n.io/api/
    baseURL: https://app.n8n.cloud/api/v1
    properties:
      - url: https://docs.n8n.io/api/
        type: Documentation
      - url: https://docs.n8n.io/api/api-reference/
        type: Reference
      - url: https://docs.n8n.io/api/authentication/
        type: Authentication
      - url: https://raw.githubusercontent.com/api-evangelist/n8n/refs/heads/main/openapi/n8n-openapi.yml
        type: OpenAPI
    description: The n8n public REST API provides programmatic access to n8n instance resources including workflows, executions, credentials, users, tags, and variables.
common:
  - url: https://n8n.io/
    type: Portal
  - url: https://docs.n8n.io/
    type: Documentation
  - url: https://docs.n8n.io/try-it-out/quickstart/
    type: Getting Started
  - url: https://app.n8n.cloud/login
    type: Login
  - url: https://app.n8n.cloud/magic-link
    type: Sign Up
  - url: https://n8n.io/pricing/
    type: Pricing
  - url: https://blog.n8n.io/
    type: Blog
  - url: https://docs.n8n.io/release-notes/
    type: Change Log
  - url: https://community.n8n.io/
    type: Community
  - url: https://github.com/n8n-io
    type: GitHub Organization
  - url: https://n8n.io/legal/privacy/
    type: Privacy Policy
  - url: https://n8n.io/legal/
    type: Terms of Service
  - url: https://n8n.io/legal/security/
    type: Security
  - type: Features
    data:
      - 'Starter €20/mo: 2,500 executions, unlimited users, 1 project'
      - 'Pro €50/mo: 10K executions, 3 projects, admin roles, 7-day insights'
      - 'Business €667/mo: 40K executions, SSO/SAML/LDAP, git, self-hosted'
      - 'Enterprise custom: unlimited projects, 200+ concurrent, 365-day insights'
      - 'REST API: 60 req/min/workspace'
      - Webhook trigger and concurrent execution scale with tier
      - 1,200+ pre-built integrations
      - Visual node-based workflow editor
      - Code nodes (JavaScript, Python via Pyodide)
      - AI Workflow Builder for natural-language workflow creation
      - AI Agent nodes (LangChain integration)
      - Self-hosted Community Edition (free)
      - Self-hosted Enterprise Edition (paid Business+)
      - Webhooks (in/out), schedule triggers, manual triggers
      - Multi-environment (dev/stage/prod) on Business+
      - Git-based version control on Business+
    sources:
      - https://n8n.io/pricing/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
