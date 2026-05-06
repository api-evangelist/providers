---
aid: stacker
name: Stacker
description: Stacker is a no-code platform that enables organizations to build custom business applications, internal tools, and customer portals on top of their existing data sources — including Airtable, Google Sheets, SQL databases, and Salesforce — without writing code. Its drag-and-drop interface, role-based access controls, and Open API enable teams to create data-driven portals, automate workflows, and integrate with third-party services.
url: https://raw.githubusercontent.com/api-evangelist/stacker/refs/heads/main/apis.yml
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Application Development
  - Low-Code
  - No-Code
  - Portals
  - Workflow Automation
type: Index
access: 3rd-Party
created: '2025-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: stacker:stacker-api
    name: Stacker API
    description: The Stacker API provides programmatic access to objects, records, accounts, and stacks within the Stacker platform. It enables external integrations, automation workflows, and data operations across Stacker applications using token-based authentication.
    humanURL: https://docs.stackerhq.com/stacker/ai-and-automations/open-api-overview
    baseURL: https://api.go.stackerhq.com
    tags:
      - No-Code
      - Records
      - Application Development
    properties:
      - type: Documentation
        url: https://docs.stackerhq.com/stacker/ai-and-automations/open-api-overview
      - type: Authentication
        url: https://docs.stackerhq.com/stacker/ai-and-automations/open-api-overview/authentication
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/stacker/refs/heads/main/openapi/stacker-openapi.yml
common:
  - type: Website
    url: https://stacker.ai/
    name: Stacker - No-Code Platform
  - type: Documentation
    url: https://docs.stackerhq.com/
    name: Stacker Documentation
  - type: GettingStarted
    url: https://docs.stackerhq.com/stacker/ai-and-automations/open-api-overview
    name: Open API Overview
  - type: Authentication
    url: https://docs.stackerhq.com/stacker/ai-and-automations/open-api-overview/authentication
    name: API Authentication
  - type: Pricing
    url: https://stacker.ai/pricing
    name: Stacker Pricing
  - type: Blog
    url: https://stacker.ai/blog
    name: Stacker Blog
  - type: Login
    url: https://app.stackerhq.com/
    name: Stacker App Login
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
