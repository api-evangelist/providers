---
aid: google-sheets
name: Google Sheets
description: API for reading, writing, and formatting data in Google Sheets.
image: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
url: https://developers.google.com/sheets/api
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
type: Index
apis:
  - name: Google Sheets API v4
    description: The Google Sheets API lets you read, write, and format Google Sheets data.
    image: https://www.gstatic.com/images/branding/product/2x/sheets_2020q4_48dp.png
    humanURL: https://developers.google.com/sheets/api
    baseURL: https://sheets.googleapis.com/v4
    properties:
      - type: Documentation
        url: https://developers.google.com/sheets/api/reference/rest
      - type: OpenAPI
        url: openapi/google-sheets-openapi.yml
      - type: Authentication
        url: https://developers.google.com/sheets/api/guides/authorizing
      - type: Quickstart
        url: https://developers.google.com/sheets/api/quickstart/python
      - type: GettingStarted
        url: https://developers.google.com/workspace/sheets/api/guides/concepts
      - type: APIReference
        url: https://developers.google.com/workspace/sheets/api/reference/rest
      - type: SDK
        url: https://developers.google.com/workspace/sheets/api/guides/libraries
      - type: ChangeLog
        url: https://developers.google.com/workspace/sheets/release-notes
      - type: CodeExamples
        url: https://developers.google.com/workspace/sheets/api/samples
      - type: RateLimits
        url: https://developers.google.com/workspace/sheets/api/limits
      - type: Errors
        url: https://developers.google.com/workspace/sheets/api/troubleshoot-api-errors
      - type: JSONSchema
        url: json-schema/google-sheets-spreadsheet-schema.json
      - type: JSONLD
        url: json-ld/google-sheets-context.jsonld
    contact:
      - type: Support
        url: https://support.google.com/developers/
      - type: StackOverflow
        url: https://stackoverflow.com/questions/tagged/google-sheets-api
    tags:
      - Collaboration
      - Data
      - Google
      - Productivity
      - Spreadsheets
  - name: Google Apps Script Spreadsheet Service
    description: The built-in Google Apps Script Spreadsheet Service allows creation, access, and modification of Google Sheets files directly from Apps Script with performance bundling and numerous classes for formatting, data sources, structure, and content.
    image: https://www.gstatic.com/images/branding/product/2x/apps_script_48dp.png
    humanURL: https://developers.google.com/apps-script/reference/spreadsheet
    properties:
      - type: Documentation
        url: https://developers.google.com/apps-script/reference/spreadsheet
      - type: GettingStarted
        url: https://developers.google.com/apps-script
      - type: APIReference
        url: https://developers.google.com/apps-script/reference
      - type: ReleaseNotes
        url: https://developers.google.com/apps-script/release-notes
    contact:
      - type: StackOverflow
        url: https://stackoverflow.com/questions/tagged/google-apps-script
    tags:
      - Apps Script
      - Automation
      - Google
      - Scripting
      - Spreadsheets
maintainers:
  - name: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
common:
  - type: Portal
    url: https://developers.google.com/workspace/sheets/api
  - type: Documentation
    url: https://developers.google.com/workspace/sheets/api/reference/rest
  - type: Blog
    url: https://workspace.google.com/blog/developers-practitioners
  - type: GitHubOrganization
    url: https://github.com/googleapis
  - type: Support
    url: https://developers.google.com/sheets/api/support
  - type: StatusPage
    url: https://www.google.com/appsstatus/dashboard/
  - type: TermsOfService
    url: https://developers.google.com/terms
  - type: PrivacyPolicy
    url: https://policies.google.com/privacy
  - type: SignUp
    url: https://console.cloud.google.com/
  - type: Login
    url: https://console.cloud.google.com/
  - type: StackOverflow
    url: https://stackoverflow.com/questions/tagged/google-sheets-api
  - type: YouTube
    url: https://developers.google.com/workspace/sheets/api/videos
  - type: GettingStarted
    url: https://developers.google.com/workspace/sheets/api/guides/concepts
  - type: Authentication
    url: https://developers.google.com/sheets/api/guides/authorizing
  - type: SDK
    url: https://developers.google.com/workspace/sheets/api/guides/libraries
  - type: ReleaseNotes
    url: https://developers.google.com/workspace/sheets/release-notes
  - type: Pricing
    url: https://developers.google.com/workspace/sheets/api/limits
  - type: RateLimits
    url: https://developers.google.com/workspace/sheets/api/limits
  - type: SpectralRules
    url: rules/google-sheets-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/google-sheets.yaml
    title: Google Sheets API Shared Definition
  - type: NaftikoCapability
    url: capabilities/spreadsheet-data-management.yaml
    title: Spreadsheet Data Management Workflow
  - type: Features
    data:
      - name: Spreadsheet Management
        description: Create, read, update, and delete spreadsheets programmatically with full control over properties and metadata.
      - name: Cell Value Operations
        description: Read and write individual cell values, ranges, and batch operations across multiple ranges.
      - name: Formatting
        description: Apply rich formatting to cells including fonts, colors, borders, alignment, and number formats.
      - name: Sheet Management
        description: Add, remove, copy, and configure individual sheets within a spreadsheet.
      - name: Developer Metadata
        description: Attach custom metadata to spreadsheets, sheets, rows, and columns for application-specific data.
      - name: Data Validation
        description: Set validation rules on cells to enforce data quality and consistency.
      - name: Conditional Formatting
        description: Apply conditional formatting rules based on cell values and formulas.
      - name: Charts and Graphs
        description: Create and manage embedded charts within spreadsheets.
      - name: Named Ranges
        description: Define and manage named ranges for easier formula references.
      - name: Batch Operations
        description: Execute multiple read and write operations in a single API call for efficiency.
  - type: UseCases
    data:
      - name: Data Collection and Reporting
        description: Collect data from various sources and generate automated reports in Google Sheets.
      - name: Database Backend
        description: Use Google Sheets as a lightweight database for web applications and prototypes.
      - name: Workflow Automation
        description: Automate data entry, processing, and distribution workflows using the API.
      - name: Data Integration
        description: Synchronize data between Google Sheets and other business applications.
      - name: Dashboard Creation
        description: Build interactive dashboards and visualizations from spreadsheet data.
  - type: Integrations
    data:
      - name: Google Workspace
        description: Deep integration with Google Docs, Slides, Forms, and other Workspace applications.
      - name: Google Apps Script
        description: Extend Sheets functionality with custom functions, menus, and automation scripts.
      - name: Google Cloud Platform
        description: Connect to BigQuery, Cloud Functions, and other GCP services for advanced data processing.
      - name: Zapier
        description: Connect Google Sheets to thousands of apps through Zapier automation workflows.
      - name: Slack
        description: Send notifications and updates to Slack channels based on spreadsheet changes.
tags:
  - Google Workspace
  - Productivity
  - Spreadsheets
---
