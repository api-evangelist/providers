---
aid: atlassian-confluence
name: Atlassian Confluence
description: |
  Atlassian Confluence is a team collaboration and wiki platform for creating, organizing, and discussing work with your team. It provides REST APIs (v1 and v2) and a GraphQL API for managing content, spaces, pages, users, labels, and search across Confluence Cloud deployments, enabling automation, app development, and integration with enterprise workflows.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Atlassian
  - Collaboration
  - Content Management
  - Documentation
  - Knowledge Management
  - Wiki
url: https://raw.githubusercontent.com/api-evangelist/atlassian-confluence/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: atlassian-confluence:confluence-cloud-rest-api
    name: Confluence Cloud REST API
    description: The primary REST API for Confluence Cloud, providing access to content, spaces, users, and more.
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/
    baseURL: https://your-domain.atlassian.net/wiki/rest/api
    tags:
      - Content
      - Pages
      - REST
      - Spaces
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v1/intro/
      - type: OpenAPI
        url: https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json
      - type: Authentication
        url: https://developer.atlassian.com/cloud/confluence/authentication/
      - type: GettingStarted
        url: https://developer.atlassian.com/cloud/confluence/getting-started/
  - aid: atlassian-confluence:confluence-cloud-rest-api-v2
    name: Confluence Cloud REST API V2
    description: The next generation REST API for Confluence Cloud with improved performance and new capabilities.
    humanURL: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/
    baseURL: https://your-domain.atlassian.net/wiki/api/v2
    tags:
      - Content
      - Pages
      - REST
      - Spaces
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/
      - type: OpenAPI
        url: https://dac-static.atlassian.com/cloud/confluence/openapi-v2.v3.json
  - aid: atlassian-confluence:confluence-cloud-graphql-api
    name: Confluence Cloud GraphQL API
    description: |
      The Confluence Cloud GraphQL API provides flexible querying and mutation capabilities for Confluence content, spaces, pages, and user data using OAuth 2.0 authentication.
    humanURL: https://developer.atlassian.com/cloud/confluence/graphql/
    baseURL: https://api.atlassian.com/graphql
    tags:
      - Content
      - GraphQL
      - Pages
      - Spaces
    properties:
      - type: Documentation
        url: https://developer.atlassian.com/cloud/confluence/graphql/
common:
  - type: Website
    url: https://www.atlassian.com/software/confluence
  - type: Documentation
    url: https://developer.atlassian.com/cloud/confluence/
  - type: Getting Started
    url: https://developer.atlassian.com/cloud/confluence/getting-started/
  - type: Authentication
    url: https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/
  - type: Change Log
    url: https://developer.atlassian.com/cloud/confluence/changelog/
  - type: Status
    url: https://status.atlassian.com/
  - type: Support
    url: https://support.atlassian.com/
  - type: Community
    url: https://community.atlassian.com/
  - type: Terms of Service
    url: https://www.atlassian.com/legal/cloud-terms-of-service
  - type: Privacy Policy
    url: https://www.atlassian.com/legal/privacy-policy
  - type: GitHub Organization
    url: https://github.com/atlassian
  - type: RateLimits
    url: https://developer.atlassian.com/cloud/confluence/rate-limiting/
  - type: Blog
    url: https://developer.atlassian.com/blog/
  - type: Pricing
    url: https://www.atlassian.com/software/confluence/pricing
  - type: SignUp
    url: https://www.atlassian.com/software/confluence
  - type: SDK
    url: https://developer.atlassian.com/platform/forge/
  - type: Features
    data:
      - name: Content Management API
        description: Create, read, update, and delete Confluence pages, blog posts, and spaces programmatically via REST or GraphQL.
      - name: CQL Search
        description: Execute powerful content searches using Confluence Query Language (CQL) to find pages, users, and spaces.
      - name: User and Group Management
        description: Manage Confluence users, groups, and permissions programmatically using the REST API.
      - name: Forge App Development
        description: Build Confluence apps with the Atlassian Forge platform using serverless functions and UI extensions.
      - name: Webhook Support
        description: Subscribe to Confluence events via webhooks to trigger workflows on content creation, update, and deletion.
      - name: OAuth 2.0 Authentication
        description: Secure API access via OAuth 2.0 three-legged authorization for user-facing integrations.
  - type: UseCases
    data:
      - name: Documentation Automation
        description: Automatically create and update Confluence pages from CI/CD pipelines, JIRA data, or external documentation sources.
      - name: Content Migration
        description: Migrate content from other wikis and knowledge bases into Confluence using the REST API bulk import capabilities.
      - name: Enterprise Search Integration
        description: Index and search Confluence content from enterprise search platforms using the CQL search API.
      - name: Custom App Development
        description: Build custom Confluence apps and macros using Forge to extend the platform with team-specific workflows.
      - name: Reporting and Analytics
        description: Extract page views, space statistics, and content metadata for custom analytics and reporting dashboards.
  - type: Integrations
    data:
      - name: Jira
        description: Deep native integration linking Confluence pages to Jira issues, projects, and sprints for unified project documentation.
      - name: Slack
        description: Confluence Slack integration for notifications, page previews, and content sharing within Slack channels.
      - name: Microsoft Teams
        description: Share and preview Confluence pages within Microsoft Teams with native connector support.
      - name: Trello
        description: Link Trello boards to Confluence spaces for project documentation aligned with Kanban workflows.
      - name: Bitbucket
        description: Embed Bitbucket code snippets and repository information in Confluence pages using Smart Links.
  - type: Solutions
    data:
      - name: Team Knowledge Base
        description: Create a structured team knowledge base with organized spaces, nested pages, and templates for documentation.
      - name: Technical Documentation
        description: Maintain living technical documentation alongside development workflows with API-driven updates.
      - name: Project Collaboration
        description: Facilitate project planning, retrospectives, and cross-team collaboration with integrated Jira and Confluence workspaces.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
