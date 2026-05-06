---
aid: tripetto
name: Tripetto
description: Tripetto is a powerful form builder platform and SDK that enables developers to create smart, conversational forms and surveys with advanced conditional logic. The platform provides a JavaScript/TypeScript SDK for embedding form builders and runners into web applications, along with webhook capabilities for delivering form responses to external services and automation platforms.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Forms
  - Surveys
  - Form Builder
  - No-Code
  - SDK
  - Webhooks
url: https://raw.githubusercontent.com/api-evangelist/tripetto/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: tripetto:tripetto-form-builder-sdk
    name: Tripetto FormBuilder SDK
    description: The Tripetto FormBuilder SDK provides JavaScript and TypeScript APIs for embedding interactive form builders into web applications. Supports React, Angular, and plain JavaScript integration with a rich component model for building, running, and collecting responses from smart conversational forms.
    humanURL: https://tripetto.com/sdk/
    baseURL: https://tripetto.com
    tags:
      - Forms
      - SDK
      - JavaScript
      - TypeScript
      - React
      - Angular
    properties:
      - type: Documentation
        url: https://tripetto.com/sdk/docs/
      - type: Builder API Reference
        url: https://tripetto.com/sdk/docs/builder/api/
      - type: Getting Started
        url: https://tripetto.com/sdk/docs/builder/introduction/
      - type: npm Package
        url: https://www.npmjs.com/package/@tripetto/builder
      - type: OpenAPI
        url: openapi/tripetto-form-builder-openapi.yml
      - type: JSONSchema
        url: json-schema/tripetto-form-schema.json
      - type: JSONSchema
        url: json-schema/tripetto-response-schema.json
  - aid: tripetto:tripetto-webhooks
    name: Tripetto Webhooks
    description: Tripetto supports outbound webhooks that deliver form response data to external services and automation platforms including Make, Zapier, and Pabbly Connect. Custom webhook endpoints receive form submission payloads as HTTP POST requests with structured JSON response data.
    humanURL: https://tripetto.com/help/articles/how-to-automate-a-webhook-to-connect-to-other-services-for-each-new-result/
    baseURL: https://tripetto.com
    tags:
      - Webhooks
      - Automation
      - Forms
      - Integrations
    properties:
      - type: Documentation
        url: https://tripetto.com/help/articles/how-to-automate-a-webhook-to-connect-to-other-services-for-each-new-result/
      - type: Webhook Raw Data
        url: https://tripetto.com/help/articles/use-raw-response-data-in-webhooks/
      - type: Zapier Integration
        url: https://zapier.com/apps/tripetto/integrations
      - type: Make Integration
        url: https://www.make.com/en/integrations/tripetto
common:
  - type: Website
    url: https://tripetto.com/
  - type: Documentation
    url: https://tripetto.com/sdk/docs/
  - type: Help Center
    url: https://tripetto.com/help/
  - type: Tutorials
    url: https://tripetto.com/tutorials/
  - type: Pricing
    url: https://tripetto.com/pricing/
  - type: GitHub Organization
    url: https://gitlab.com/tripetto
  - type: npm Organization
    url: https://www.npmjs.com/org/tripetto
  - type: Login
    url: https://tripetto.com/app/sign-in/
  - type: Sign Up
    url: https://tripetto.com/app/sign-up/
  - type: OpenAPI
    url: openapi/tripetto-form-builder-openapi.yml
  - type: JSONSchema
    url: json-schema/tripetto-form-schema.json
  - type: JSONSchema
    url: json-schema/tripetto-response-schema.json
  - type: JSON Structure
    url: json-structure/tripetto-form-structure.json
  - type: JSON-LD
    url: json-ld/tripetto-context.jsonld
  - type: Spectral Rules
    url: rules/tripetto-rules.yml
  - type: Naftiko Capability
    url: capabilities/form-management.yaml
  - type: Vocabulary
    url: vocabulary/tripetto-vocabulary.yml
  - type: x-profiled
    url: 2026-05
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
