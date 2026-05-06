---
aid: fiscalnote
url: https://raw.githubusercontent.com/api-evangelist/fiscalnote/refs/heads/main/apis.yml
name: FiscalNote
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Government
  - Legislation
  - Policy
  - Political Intelligence
  - Regulation
description: FiscalNote is a policy intelligence platform that provides legislative, regulatory, and stakeholder data spanning Congress, all 50 U.S. states, and more than 100 countries. FiscalNote expanded its PolicyNote API to eliminate AI hallucinations in compliance workflows by providing primary-source verified policy data.
created: '2026-03-24'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: fiscalnote:policynote-api
    name: FiscalNote PolicyNote API
    tags:
      - AI Agents
      - Compliance
      - Legislation
      - MCP
      - Policy
      - Regulation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.fiscalnote.com
    humanURL: https://fiscalnote.com/products/policynote-api
    properties:
      - url: https://fiscalnote.com/products/policynote-api
        type: Documentation
      - url: openapi/fiscalnote-policynote-openapi.yml
        type: OpenAPI
    description: The FiscalNote PolicyNote API delivers programmatic access to legislative, regulatory, and stakeholder intelligence datasets spanning Congress, all 50 U.S. states, and more than 100 countries through a secure, governed architecture designed for machine consumption. The API includes an MCP server enabling MCP-compatible AI agents from platforms such as Anthropic, OpenAI, Google Gemini, and Microsoft to query structured policy data, verified analysis, and real-time monitoring signals.
  - aid: fiscalnote:appdata-api
    name: FiscalNote AppData API
    tags:
      - Bills
      - Government Data
      - Legislation
      - Regulation
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.fiscalnote.com
    humanURL: https://apidocs.fiscalnote.com/apis
    properties:
      - url: https://apidocs.fiscalnote.com/apis
        type: Documentation
      - url: openapi/fiscalnote-appdata-openapi.yml
        type: OpenAPI
    description: The FiscalNote AppData API provides access to FiscalNote's data on legislation and regulations, both past and present, in the United States and globally. It also exposes organizational data from the FiscalNote platform including issues and labels. Developers can use the API to integrate legislative tracking, regulatory monitoring, and policy analysis capabilities into their own applications and workflows.
  - aid: fiscalnote:people-api
    name: FiscalNote People API
    tags:
      - Government Officials
      - Legislators
      - Politicians
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.fiscalnote.com
    humanURL: https://apidocs.fiscalnote.com/apis
    properties:
      - url: https://apidocs.fiscalnote.com/apis
        type: Documentation
      - url: openapi/fiscalnote-people-openapi.yml
        type: OpenAPI
    description: The FiscalNote People API allows developers to access FiscalNote's data on government officials in the United States and globally. The API provides structured information about legislators, elected officials, and other government personnel, enabling applications to look up representatives, track official profiles, and integrate government personnel data into political intelligence and advocacy workflows.
  - aid: fiscalnote:organization-api
    name: FiscalNote Organization API
    tags:
      - Committees
      - Federal Agencies
      - Government Organizations
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.fiscalnote.com
    humanURL: https://apidocs.fiscalnote.com/apis
    properties:
      - url: https://apidocs.fiscalnote.com/apis
        type: Documentation
      - url: openapi/fiscalnote-organization-openapi.yml
        type: OpenAPI
    description: The FiscalNote Organization API provides access to FiscalNote's data on government organizations in the United States and globally. It covers legislative committees, federal agencies, and other governmental bodies. Developers can use this API to retrieve structured information about government organizations, enabling integration of organizational data into policy tracking, compliance, and government relations applications.
common:
  - type: Website
    url: https://fiscalnote.com/
  - type: Portal
    url: https://apidocs.fiscalnote.com/
  - type: Documentation
    url: https://apidocs.fiscalnote.com/apis
  - type: Blog
    url: https://fiscalnote.com/blog
  - type: Privacy Policy
    url: https://fiscalnote.com/privacy
  - type: Terms of Service
    url: https://fiscalnote.com/terms
  - type: Login
    url: https://app.fiscalnote.com/
  - type: JSON-LD
    url: json-ld/fiscalnote-context.jsonld
  - type: JSONSchema
    url: json-schema/fiscalnote-legislation-schema.json
  - type: JSONSchema
    url: json-schema/fiscalnote-official-schema.json
  - type: JSONSchema
    url: json-schema/fiscalnote-transcript-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
