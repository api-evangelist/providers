---
aid: google-slides
name: Google Slides
description: An API for creating, reading, and editing Google Slides presentations.
image: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
url: https://developers.google.com/slides
created: '2024-01-01'
modified: '2026-04-18'
specificationVersion: '0.19'
type: Index
tags:
  - Collaboration
  - Google Workspace
  - Presentations
  - Productivity
  - Slides
apis:
  - name: Google Slides API
    description: Create and edit presentations programmatically.
    image: https://www.gstatic.com/images/branding/product/2x/slides_2020q4_48dp.png
    humanURL: https://developers.google.com/slides
    baseURL: https://slides.googleapis.com
    tags:
      - Presentations
      - REST
      - Slides
    properties:
      - type: Documentation
        url: https://developers.google.com/slides/api/reference/rest
      - type: OpenAPI
        url: https://slides.googleapis.com/$discovery/rest?version=v1
        title: Discovery Document
      - type: OpenAPI
        url: openapi/google-slides-api-openapi.yml
      - type: JSONSchema
        url: json-schema/google-slides-presentation-schema.json
      - type: JSONLD
        url: json-ld/google-slides-context.jsonld
      - type: Authentication
        url: https://developers.google.com/slides/api/guides/authorizing
      - type: Quickstart
        url: https://developers.google.com/slides/api/quickstart/python
        title: Python Quickstart
      - type: Documentation
        url: https://developers.google.com/slides/api/guides/concepts
        title: Concepts Guide
      - type: CodeExamples
        url: https://developers.google.com/slides/api/samples
      - type: Pricing
        url: https://developers.google.com/slides/api/limits
      - type: TermsOfService
        url: https://developers.google.com/terms
      - type: Support
        url: https://developers.google.com/slides/api/support
      - type: Documentation
        url: https://developers.google.com/workspace/slides/api/guides/overview
        title: Overview
      - type: SDK
        url: https://developers.google.com/workspace/slides/api/guides/libraries
        title: Client Libraries
      - type: ReleaseNotes
        url: https://developers.google.com/workspace/slides/release-notes
      - type: Documentation
        url: https://developers.google.com/workspace/slides/api/scopes
        title: Scopes
      - type: Troubleshooting
        url: https://developers.google.com/workspace/slides/api/troubleshoot-authentication-authorization
      - type: Quickstart
        url: https://developers.google.com/slides/api/quickstart/java
        title: Java Quickstart
      - type: Quickstart
        url: https://developers.google.com/workspace/slides/api/quickstart/nodejs
        title: Node.js Quickstart
      - type: Quickstart
        url: https://developers.google.com/workspace/slides/api/quickstart/javascript
        title: JavaScript Quickstart
      - type: Quickstart
        url: https://developers.google.com/workspace/slides/api/quickstart/go
        title: Go Quickstart
      - type: Quickstart
        url: https://developers.google.com/workspace/slides/api/quickstart/apps-script
        title: Apps Script Quickstart
      - type: YouTube
        url: https://developers.google.com/workspace/slides/api/videos
      - type: GitHubRepository
        url: https://github.com/googleworkspace/slides-api
common:
  - type: Portal
    url: https://console.cloud.google.com/
  - type: Authentication
    url: https://developers.google.com/identity/protocols/oauth2
  - type: GettingStarted
    url: https://developers.google.com/slides/api/quickstart/python
  - type: StatusPage
    url: https://status.cloud.google.com/
  - type: PrivacyPolicy
    url: https://policies.google.com/privacy
  - type: TermsOfService
    url: https://policies.google.com/terms
  - type: Documentation
    url: https://developers.google.com/workspace/products
    title: Developer Products
  - type: Documentation
    url: https://developers.google.com/workspace/guides/create-credentials
    title: Credentials
  - type: Documentation
    url: https://developers.google.com/workspace/guides/enable-apis
    title: Enable APIs
  - type: Documentation
    url: https://developers.google.com/workspace/guides/configure-oauth-consent
    title: OAuth Consent Screen
  - type: Authentication
    url: https://developers.google.com/identity/protocols/oauth2/scopes
    title: OAuth Scopes
  - type: Support
    url: https://issuetracker.google.com/bookmark-groups/78025
    title: Issue Tracker
  - type: ReleaseNotes
    url: https://developers.google.com/workspace/release-notes
    title: Workspace Release Notes
  - type: Blog
    url: https://cloud.google.com/blog/products/application-development/introducing-google-slides-api
  - type: SpectralRules
    url: rules/google-slides-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/slides-api.yaml
    title: Google Slides API Shared Definition
  - type: NaftikoCapability
    url: capabilities/presentation-management.yaml
    title: Presentation Management Workflow
  - type: Features
    url: https://developers.google.com/slides
    data:
      - name: Presentation Creation
        description: Create blank or pre-configured presentations programmatically with custom titles and layouts.
      - name: Batch Updates
        description: Apply multiple changes to a presentation in a single atomic request for efficient editing.
      - name: Slide Management
        description: Add, reorder, duplicate, and delete slides within presentations.
      - name: Text and Shape Editing
        description: Insert and format text, shapes, images, videos, tables, and charts on slides.
      - name: Page Thumbnails
        description: Generate thumbnail images of individual slides for previews and exports.
      - name: Template Support
        description: Use existing presentations as templates and populate them with dynamic content.
  - type: UseCases
    url: https://developers.google.com/slides
    data:
      - name: Automated Report Generation
        description: Generate presentation reports from data sources, populating charts, tables, and text automatically.
      - name: Dynamic Presentation Templates
        description: Create branded presentations from templates, filling in customer-specific data for sales or marketing decks.
      - name: Educational Content Creation
        description: Build educational slide decks programmatically from lesson plans, quizzes, or course materials.
      - name: Meeting Preparation
        description: Automatically compile meeting agendas, status updates, and metrics into presentation format.
  - type: Integrations
    url: https://developers.google.com/slides
    data:
      - name: Google Sheets
        description: Embed live charts and data from Google Sheets into presentations for dynamic data visualization.
      - name: Google Drive
        description: Store, organize, and share presentations through Google Drive with collaboration permissions.
      - name: Google Workspace
        description: Part of the Google Workspace suite with seamless integration across Docs, Sheets, and other apps.
      - name: Google Apps Script
        description: Automate Slides workflows using Apps Script for custom macros and triggers.
      - name: Google Cloud
        description: Deploy Slides API integrations on Google Cloud Platform infrastructure.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
