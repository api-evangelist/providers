---
aid: google-apps-script
name: Google Apps Script
description: The Apps Script API provides programmatic access to manage Google Apps Script projects, deployments, and executions. It enables creating and updating script projects, managing project versions and deployments, monitoring script processes, and remotely executing Apps Script functions. The API is essential for automating Apps Script project management and integrating script execution into external applications.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/google-apps-script/refs/heads/main/apis.yml
created: '2026-03-13'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - Apps Script
  - Automation
  - Deployments
  - Google
  - Google Workspace
  - Scripting
apis:
  - aid: google-apps-script:google-apps-script
    name: Google Apps Script API
    description: The Apps Script API manages Google Apps Script projects, deployments, versions, and processes. It supports creating script projects, updating content, managing deployments, monitoring execution processes, and remotely running script functions.
    humanURL: https://developers.google.com/apps-script/api/concepts
    baseURL: https://script.googleapis.com
    properties:
      - type: OpenAPI
        url: openapi/openapi.yml
      - type: JSONSchema
        url: json-schema/json-schema.yml
      - type: JSONLD
        url: json-ld/json-ld.jsonld
    tags:
      - Automation
      - Deployments
      - Projects
      - Scripting
common:
  - type: GettingStarted
    url: https://developers.google.com/apps-script/api/concepts
  - type: Pricing
    url: https://developers.google.com/apps-script/guides/services/quotas
  - type: JSONLD
    url: json-ld/json-ld.jsonld
  - type: GitHubOrganization
    url: https://github.com/googleworkspace
  - type: SDK
    url: https://developers.google.com/apps-script/api/quickstart/nodejs
  - type: CLI
    url: https://developers.google.com/apps-script/guides/clasp
  - type: Documentation
    url: https://developers.google.com/apps-script/reference
  - type: Support
    url: https://developers.google.com/apps-script/support
  - type: Blog
    url: https://developers.google.com/apps-script/updates
  - type: Features
    data:
      - Create and manage Apps Script projects programmatically
      - Deploy script projects as web apps, add-ons, and API executables
      - Remotely execute Apps Script functions from external applications
      - Monitor script execution processes and metrics
      - Version management with immutable snapshots of script code
  - type: UseCases
    data:
      - Automating Google Workspace workflows across Sheets, Docs, and Gmail
      - Building custom add-ons and integrations for Google Workspace
      - Managing script deployments across development and production environments
      - Monitoring script execution health and performance metrics
      - Integrating Apps Script automation into CI/CD pipelines
  - type: Integrations
    data:
      - Google Workspace apps including Sheets, Docs, Slides, Gmail, and Calendar
      - Google Cloud Platform services for extended functionality
      - External REST APIs via Apps Script UrlFetchApp service
      - Google Drive for document and file management automation
      - clasp CLI for local development and version control workflows
  - type: Rules
    url: rules/google-apps-script-spectral-rules.yml
  - type: Capabilities
    url: capabilities/shared/apps-script.yaml
  - type: Capabilities
    url: capabilities/workspace-automation.yaml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
