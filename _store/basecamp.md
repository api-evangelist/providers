---
aid: basecamp
url: https://raw.githubusercontent.com/api-evangelist/basecamp/refs/heads/main/apis.yml
name: Basecamp
tags:
  - Collaboration
  - Project Management
  - REST
  - SaaS
  - Team Communication
modified: '2026-04-21'
description: Basecamp is a project management and team collaboration platform developed by 37signals. The Basecamp REST API (bc3-api) provides programmatic access to projects, to-do lists, messages, documents, schedules, and team members. OAuth2 authentication via the 37signals Launchpad is required. The API returns JSON and is documented on GitHub at github.com/basecamp/bc3-api.
apis:
  - aid: basecamp:basecamp-api
    name: Basecamp API
    tags:
      - Collaboration
      - Project Management
      - REST
      - Team Communication
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://3.basecampapi.com
    humanURL: https://github.com/basecamp/bc3-api
    properties:
      - url: https://github.com/basecamp/bc3-api
        type: Documentation
      - url: openapi/basecamp-api-openapi.yml
        type: OpenAPI
    description: The Basecamp API is a REST API providing programmatic access to Basecamp's project management platform. Manage projects, to-do lists, messages, documents, schedules, and team members. Uses OAuth 2.0 for authentication and returns JSON.
  - aid: basecamp:basecamp-webhooks
    name: Basecamp Webhooks
    tags:
      - Events
      - Notifications
      - Project Management
      - Webhooks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://3.basecampapi.com
    humanURL: https://github.com/basecamp/bc3-api/blob/master/sections/webhooks.md
    properties:
      - url: https://github.com/basecamp/bc3-api/blob/master/sections/webhooks.md
        type: Documentation
      - url: asyncapi/basecamp-webhooks-asyncapi.yml
        type: AsyncAPI
    description: Basecamp Webhooks deliver real-time HTTP notifications when events occur within a project. Configure webhooks per project with an HTTPS payload URL and resource types.
  - aid: basecamp:basecamp-oauth
    name: Basecamp OAuth
    tags:
      - Authentication
      - Authorization
      - OAuth
      - Security
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://launchpad.37signals.com
    humanURL: https://github.com/basecamp/bc3-api/blob/master/sections/authentication.md
    properties:
      - url: https://github.com/basecamp/bc3-api/blob/master/sections/authentication.md
        type: Documentation
      - url: openapi/basecamp-oauth-openapi.yml
        type: OpenAPI
    description: OAuth 2.0 authentication for Basecamp API access via the 37signals Launchpad. Register at launchpad.37signals.com for a client ID and secret, then implement the authorization code flow to obtain access tokens.
common:
  - type: Website
    url: https://basecamp.com/
    name: Basecamp
  - type: Documentation
    url: https://github.com/basecamp/bc3-api
    name: Basecamp API Documentation
  - type: SignUp
    url: https://launchpad.37signals.com/
    name: 37signals Launchpad (App Registration)
  - type: Blog
    url: https://basecamp.com/blog
    name: Basecamp Blog
  - type: TermsOfService
    url: https://basecamp.com/about/policies/terms
    name: Terms of Service
  - type: PrivacyPolicy
    url: https://basecamp.com/about/policies/privacy
    name: Privacy Policy
  - type: SpectralRules
    url: rules/basecamp-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/basecamp-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/project-management.yaml
  - type: JSON-LD
    url: json-ld/basecamp-context.jsonld
  - name: Features
    type: Features
    data:
      - name: Project Management
        description: Create and manage projects with team access controls.
      - name: To-Do Lists
        description: Hierarchical to-do lists with assignments, due dates, and completion tracking.
      - name: Message Boards
        description: Threaded message boards for team discussion and announcements.
      - name: Campfire Chat
        description: Real-time group chat within projects.
      - name: Schedules
        description: Project calendars with events and milestones.
      - name: File Storage
        description: Document and file storage with version history.
      - name: Webhooks
        description: Real-time event notifications for project activity.
      - name: OAuth2 API
        description: Full REST API with OAuth2 authentication for third-party integrations.
  - name: Use Cases
    type: UseCases
    data:
      - name: Software Development
        description: Track sprints, bugs, and feature development with to-do lists.
      - name: Client Projects
        description: Manage client deliverables, approvals, and communications.
      - name: Remote Team Collaboration
        description: Asynchronous team communication and project coordination.
      - name: Project Automation
        description: Automate project workflows and reporting via REST API.
      - name: Agency Project Management
        description: Multi-client project organization for agencies and consultancies.
  - name: Integrations
    type: Integrations
    data:
      - name: Zapier
      - name: Make (Integromat)
      - name: Slack
      - name: GitHub
      - name: Harvest
      - name: Clockify
created: '2024-01-01'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
