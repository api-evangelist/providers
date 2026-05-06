---
aid: relay-app
name: Relay App
description: Relay.app is an AI-powered workflow automation platform that converts plain language into reliable visual workflows across 200+ app integrations. It supports webhook triggers, custom HTTP requests, scheduled automation, human-in-the-loop approval workflows, and MCP server tooling for AI agent integration. Developer features include API-triggered workflows, custom JavaScript execution, and integration with OpenAI, Anthropic, and other AI providers.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automation
  - Workflow
  - Integration
  - No-Code
  - AI
  - Webhooks
url: https://raw.githubusercontent.com/api-evangelist/relay-app/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: relay-app:relay-app-api
    name: Relay App Automation API
    description: The Relay.app API enables programmatic triggering of workflows via webhooks, custom HTTP requests to external APIs, and scheduled automation runs. Developers can use webhook endpoints to trigger workflow runs, pass JSON payloads, configure deduplication, and receive custom response codes. The API supports GET and POST HTTP methods with configurable headers and payloads.
    humanURL: https://docs.relay.app/
    baseURL: https://api.relay.app
    tags:
      - Webhook
      - Automation
      - Workflow Triggers
      - HTTP
      - Integration
    properties:
      - type: Documentation
        url: https://docs.relay.app/
      - type: Webhook Documentation
        url: https://docs.relay.app/triggers/webhook-trigger
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/relay-app/refs/heads/main/openapi/relay-app-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/relay-app/refs/heads/main/json-schema/relay-app-workflow-schema.json
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/relay-app/refs/heads/main/json-schema/relay-app-workflow-run-schema.json
      - type: JSONStructure
        url: https://raw.githubusercontent.com/api-evangelist/relay-app/refs/heads/main/json-structure/relay-app-workflow-structure.json
common:
  - type: Website
    url: https://www.relay.app
  - type: Documentation
    url: https://docs.relay.app/
  - type: Integrations
    url: https://www.relay.app/apps
  - type: Blog
    url: https://www.relay.app/blog
  - type: Features
    url: https://www.relay.app/features
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/relay-app/refs/heads/main/json-ld/relay-app-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/relay-app/refs/heads/main/vocabulary/relay-app-vocabulary.yml
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/relay-app/refs/heads/main/rules/relay-app-rules.yml
  - type: NaftikoCapability
    url: https://raw.githubusercontent.com/api-evangelist/relay-app/refs/heads/main/capabilities/workflow-automation.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
