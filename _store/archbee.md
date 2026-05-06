---
aid: archbee
name: Archbee
description: Archbee is a documentation platform for software teams that enables creating, managing, and publishing technical documentation, API references, and knowledge bases. It provides tools for writing developer docs, API documentation, and internal wikis with collaborative editing and version control.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Documentation
  - Documentation Platform
  - Knowledge Base
  - Technical Writing
  - Developer Docs
url: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: archbee:archbee-api
    name: Archbee API
    description: The Archbee API enables programmatic management of documentation spaces, pages, and content within the Archbee documentation platform.
    humanURL: https://www.archbee.com/
    baseURL: https://api.archbee.com
    tags:
      - API Documentation
      - Documentation Management
      - Knowledge Base
      - Technical Writing
    properties:
      - type: Documentation
        url: https://docs.archbee.com/
      - type: GettingStarted
        url: https://docs.archbee.com/getting-started
      - type: APIReference
        url: https://docs.archbee.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/openapi/archbee-api.yaml
common:
  - type: Portal
    url: https://www.archbee.com/
  - type: Documentation
    url: https://docs.archbee.com/
  - type: Blog
    url: https://www.archbee.com/blog
  - type: SignUp
    url: https://app.archbee.com/signup
  - type: Login
    url: https://app.archbee.com/login
  - type: Pricing
    url: https://www.archbee.com/pricing
  - type: GitHubOrganization
    url: https://github.com/archbee
  - type: TermsOfService
    url: https://www.archbee.com/terms
  - type: PrivacyPolicy
    url: https://www.archbee.com/privacy
  - type: StatusPage
    url: https://status.archbee.com/
  - type: Support
    url: https://www.archbee.com/contact
  - type: Features
    data:
      - name: API Documentation
        description: Create and publish beautiful API reference documentation with OpenAPI/Swagger support.
      - name: Collaborative Editing
        description: Real-time collaborative editing for documentation teams with version control.
      - name: Developer Portal
        description: Build customizable developer portals with branded documentation sites.
      - name: Knowledge Base
        description: Internal and external knowledge base creation with powerful search.
      - name: Version Control
        description: Document versioning and change history for tracking documentation evolution.
      - name: Integrations
        description: Integrations with GitHub, Slack, Jira, and other developer tools.
      - name: AI Writing Assistant
        description: AI-powered writing assistance for faster technical documentation creation.
      - name: Custom Domains
        description: Host documentation on custom domains with SSL included.
  - type: UseCases
    data:
      - name: API Documentation
        description: Create comprehensive API reference docs with code samples, SDKs, and interactive API explorers.
      - name: Developer Portal
        description: Build a unified developer portal for all your APIs, SDKs, and developer resources.
      - name: Internal Wiki
        description: Create an internal knowledge base for engineering teams with runbooks, architecture docs, and processes.
      - name: Customer Documentation
        description: Publish customer-facing help documentation and user guides with powerful search.
      - name: Product Documentation
        description: Create and maintain product documentation for software products with versioning.
  - type: Integrations
    data:
      - name: GitHub
        description: Sync documentation with GitHub repositories for version-controlled docs-as-code workflows.
      - name: Slack
        description: Slack integration for documentation notifications and knowledge base search within Slack.
      - name: Jira
        description: Link documentation pages to Jira issues for requirement traceability.
      - name: Intercom
        description: Embed Archbee knowledge base in Intercom for customer support.
      - name: Segment
        description: Analytics integration for tracking documentation usage and engagement.
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/rules/archbee-spectral-rules.yml
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/vocabulary/archbee-vocabulary.yaml
  - type: JSONLD
    url: https://raw.githubusercontent.com/api-evangelist/archbee/refs/heads/main/json-ld/archbee-api-context.jsonld
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
