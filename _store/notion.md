---
aid: notion
url: https://raw.githubusercontent.com/api-evangelist/notion/refs/heads/main/apis.yml
apis:
  - aid: notion:notion
    name: Notion API
    tags:
      - Collaboration
      - Ideas
      - Projects
      - Tasks
    humanURL: https://developers.notion.com
    properties:
      - url: https://developers.notion.com
        type: Documentation
      - url: openapi/notion-openapi.yml
        type: OpenAPI
      - url: json-schema/notion-page-schema.json
        type: JSONSchema
      - url: json-schema/notion-database-schema.json
        type: JSONSchema
      - url: json-schema/notion-block-schema.json
        type: JSONSchema
      - url: json-ld/notion-context.jsonld
        type: JSONLD
      - url: https://developers.notion.com/reference/authentication
        type: Authentication
      - url: https://developers.notion.com/docs/authorization
        type: Authorization
      - url: https://developers.notion.com/docs/getting-started
        type: GettingStarted
      - url: https://github.com/makenotion/notion-sdk-js
        type: GitHubRepo
      - url: https://api.notion.com
        type: BaseURL
      - url: https://developers.notion.com/reference/intro
        type: IntroductionAPI
      - url: https://developers.notion.com/reference/create-a-database
        type: DatabaseCreateAPI
      - url: https://developers.notion.com/reference/retrieve-a-database
        type: DatabaseRetrieveAPI
      - url: https://developers.notion.com/reference/update-a-database
        type: DatabaseUpdateAPI
      - url: https://developers.notion.com/reference/post-database-query
        type: DatabaseQueryAPI
      - url: https://developers.notion.com/reference/post-page
        type: PageCreateAPI
      - url: https://developers.notion.com/reference/retrieve-a-page
        type: PageRetrieveAPI
      - url: https://developers.notion.com/reference/patch-page
        type: PageUpdateAPI
      - url: https://developers.notion.com/reference/archive-a-page
        type: PageTrashAPI
      - url: https://developers.notion.com/reference/move-page
        type: PageMoveAPI
      - url: https://developers.notion.com/reference/retrieve-a-page-property
        type: PagePropertyRetrieveAPI
      - url: https://developers.notion.com/reference/retrieve-page-markdown
        type: PageMarkdownRetrieveAPI
      - url: https://developers.notion.com/reference/update-page-markdown
        type: PageMarkdownUpdateAPI
      - url: https://developers.notion.com/reference/retrieve-a-block
        type: BlockRetrieveAPI
      - url: https://developers.notion.com/reference/update-a-block
        type: BlockUpdateAPI
      - url: https://developers.notion.com/reference/delete-a-block
        type: BlockDeleteAPI
      - url: https://developers.notion.com/reference/get-block-children
        type: BlockChildrenRetrieveAPI
      - url: https://developers.notion.com/reference/patch-block-children
        type: BlockChildrenAppendAPI
      - url: https://developers.notion.com/reference/get-users
        type: UsersListAPI
      - url: https://developers.notion.com/reference/get-user
        type: UserRetrieveAPI
      - url: https://developers.notion.com/reference/get-self
        type: UserBotRetrieveAPI
      - url: https://developers.notion.com/reference/create-a-comment
        type: CommentCreateAPI
      - url: https://developers.notion.com/reference/list-comments
        type: CommentsListAPI
      - url: https://developers.notion.com/reference/retrieve-comment
        type: CommentRetrieveAPI
      - url: https://developers.notion.com/reference/post-search
        type: SearchAPI
      - url: https://developers.notion.com/reference/create-a-data-source
        type: DataSourceCreateAPI
      - url: https://developers.notion.com/reference/retrieve-a-data-source
        type: DataSourceRetrieveAPI
      - url: https://developers.notion.com/reference/update-a-data-source
        type: DataSourceUpdateAPI
      - url: https://developers.notion.com/reference/query-a-data-source
        type: DataSourceQueryAPI
      - url: https://developers.notion.com/reference/list-data-source-templates
        type: DataSourceTemplatesListAPI
      - url: https://developers.notion.com/reference/create-a-file-upload
        type: FileUploadCreateAPI
      - url: https://developers.notion.com/reference/send-a-file-upload
        type: FileUploadSendAPI
      - url: https://developers.notion.com/reference/complete-a-file-upload
        type: FileUploadCompleteAPI
      - url: https://developers.notion.com/reference/retrieve-a-file-upload
        type: FileUploadRetrieveAPI
      - url: https://developers.notion.com/reference/list-file-uploads
        type: FileUploadsListAPI
      - url: https://developers.notion.com/reference/create-a-token
        type: TokenCreateAPI
      - url: https://developers.notion.com/reference/introspect-token
        type: TokenIntrospectAPI
      - url: https://developers.notion.com/reference/refresh-a-token
        type: TokenRefreshAPI
      - url: https://developers.notion.com/reference/revoke-token
        type: TokenRevokeAPI
    description: Notion API provides developers with the tools and resources to seamlessly integrate Notion, a popular productivity and collaboration tool, with other applications and services. With Notion API, developers can create custom integrations, automate workflows, and access data stored in Notion databases. This enables users to leverage the full potential of Notion by connecting it to their existing software stack and simplifying cross-platform collaboration.
name: Notion
tags:
  - Collaboration
  - Database
  - Ideas
  - Notes
  - Productivity
  - Projects
  - T1
  - Tasks
  - Wiki
  - Workspace
type: Index
image: https://www.notion.so/images/meta/default.png
access: 3rd-Party
common:
  - url: https://developers.notion.com/docs/getting-started
    name: Notion API Overview
    type: Guide
    description: 'null'
  - url: https://developers.notion.com/reference/intro
    name: Introduction
    type: Documentation
    description: 'null'
  - url: https://www.notion.com/blog
    name: Tools & Craft  Notion Blog
    type: Blog
    description: 'null'
  - url: https://developers.notion.com/page/examples
    name: Examples
    type: Examples
    description: 'null'
  - url: https://developers.notion.com/page/changelog
    name: Changelog
    type: ChangeLog
    description: 'null'
  - url: https://developers.notion.com/reference/versioning
    name: Versioning
    type: Versioning
    description: 'null'
  - url: https://developers.notion.com/reference/status-codes
    name: Status codes
    type: Errors
    description: 'null'
  - url: https://developers.notion.com/reference/request-limits
    name: Request limits
    type: RateLimits
    description: 'null'
  - url: https://developers.notion.com/reference/webhooks
    name: Webhooks
    type: Webhooks
  - url: https://www.postman.com/notionhq/notion-s-api-workspace/overview
    name: PostmanWorkspace
  - url: https://developers.notion.com/reference/authentication
    name: Authentication
    type: Authentication
    description: 'null'
  - url: https://developers.notion.com/docs/authorization
    name: Authorization
    type: Authorization
    description: 'null'
  - url: https://developers.notion.com/page/frequently-asked-questions
    name: Frequently Asked Questions
    type: FAQ
    description: 'null'
  - url: https://developers.notion.com/docs/mcp
    name: Notion MCP
    type: Guide
    description: 'null'
  - url: https://developers.notion.com/docs/create-a-notion-integration
    name: Build Your First Integration
    type: GettingStarted
    description: 'null'
  - url: https://developers.notion.com/docs/publishing-integrations-to-notions-integration-gallery
    name: Publishing to Integration Gallery
    type: Guide
    description: 'null'
  - url: https://developers.notion.com/reference/capabilities
    name: Integration Capabilities
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/changes-by-version
    name: Changes by Version
    type: ChangeLog
    description: 'null'
  - url: https://developers.notion.com/openapi.json
    name: OpenAPI Specification
    type: OpenAPI
    description: 'null'
  - url: https://www.notion.so/Developer-Terms-ba4131408d0844e08330da2cbb225c20
    name: Developer Terms
    type: TermsOfService
    description: 'null'
  - url: https://www.notion.so/terms
    name: Terms of Service
    type: TermsOfService
    description: 'null'
  - url: https://www.notion.com/security
    name: Security
    type: Security
    description: 'null'
  - url: https://www.notion.com/help/security-and-privacy
    name: Security and Privacy Practices
    type: Security
    description: 'null'
  - url: https://privacycenter.notion.so/policies
    name: Privacy Policy
    type: PrivacyPolicy
    description: 'null'
  - url: https://www.notion.com/pricing
    name: Pricing
    type: Pricing
    description: 'null'
  - url: https://status.notion.so/
    name: Status
    type: StatusPage
    description: 'null'
  - url: https://www.notion.com/integrations
    name: Integrations Gallery
    type: IntegrationGallery
    description: 'null'
  - url: https://www.notion.so/my-integrations
    name: My Integrations
    type: Portal
    description: 'null'
  - url: https://github.com/makenotion/notion-sdk-js
    name: Notion JavaScript SDK
    type: SDK
    description: 'null'
  - url: https://www.npmjs.com/package/@notionhq/client
    name: Notion JavaScript SDK (npm)
    type: SDK
    description: 'null'
  - url: https://github.com/makenotion/notion-mcp-server
    name: Notion MCP Server
    type: GitHubRepo
    description: 'null'
  - url: https://github.com/makenotion
    name: GitHub Organization
    type: GitHubOrg
    description: 'null'
  - url: https://www.notion.com/lp/technology-partner-program
    name: Technology Partner Program
    type: Partners
    description: 'null'
  - url: https://www.notion.com/help
    name: Help Center
    type: Support
    description: 'null'
  - url: https://www.notion.com/community
    name: Community
    type: Community
    description: 'null'
  - url: https://x.com/NotionAPI
    name: '@NotionAPI'
    type: X
    description: 'null'
  - url: https://x.com/NotionHQ
    name: '@NotionHQ'
    type: X
    description: 'null'
  - url: https://stackoverflow.com/questions/tagged/notion-api
    name: Stack Overflow
    type: StackOverflow
    description: 'null'
  - url: https://developers.notion.com/docs/working-with-databases
    name: Working with Databases
    type: Guide
    description: 'null'
  - url: https://developers.notion.com/docs/working-with-page-content
    name: Working with Page Content
    type: Guide
    description: 'null'
  - url: https://developers.notion.com/docs/working-with-comments
    name: Working with Comments
    type: Guide
    description: 'null'
  - url: https://developers.notion.com/docs/working-with-files-and-media
    name: Working with Files and Media
    type: Guide
    description: 'null'
  - url: https://developers.notion.com/reference/search-optimizations-and-limitations
    name: Search Optimizations and Limitations
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/guides/link-previews/link-previews
    name: Link Previews
    type: Guide
    description: 'null'
  - url: https://www.notion.com/help/provision-users-and-groups-with-scim
    name: SCIM Provisioning
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/docs/upgrade-guide-2025-09-03
    name: Upgrade Guide for Version 2025-09-03
    type: Guide
    description: 'null'
  - url: https://developers.notion.com/reference/database
    name: Database Object Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/data-source
    name: Data Source Object Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/page
    name: Page Object Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/block
    name: Block Object Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/user
    name: User Object Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/comment-object
    name: Comment Object Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/rich-text
    name: Rich Text Object Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/file-object
    name: File Object Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/file-upload
    name: File Upload Object Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/emoji-object
    name: Emoji Object Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/parent-object
    name: Parent Object Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/page-property-values
    name: Page Properties Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/property-item-object
    name: Page Property Items Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/property-object
    name: Data Source Properties Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/update-property-schema-object
    name: Update Database Properties Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/update-data-source-properties
    name: Update Data Source Properties Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/post-database-query-filter
    name: Filter Database Entries Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/post-database-query-sort
    name: Sort Database Entries Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/filter-data-source-entries
    name: Filter Data Source Entries Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/sort-data-source-entries
    name: Sort Data Source Entries Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/comment-attachment
    name: Comment Attachment Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/comment-display-name
    name: Comment Display Name Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/unfurl-attribute-object
    name: Unfurl Attribute (Link Previews) Reference
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/create-a-token
    name: Create a Token
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/introspect-token
    name: Introspect a Token
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/refresh-a-token
    name: Refresh a Token
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/revoke-token
    name: Revoke a Token
    type: Documentation
    description: 'null'
  - url: https://developers.notion.com/reference/webhooks-events-delivery
    name: Webhooks Event Types and Delivery
    type: Webhooks
    description: 'null'
  - url: https://developers.notion.com/llms.txt
    name: LLMs Documentation Index
    type: Documentation
    description: 'null'
  - url: https://www.notion.com/releases
    name: Product Releases
    type: ChangeLog
    description: 'null'
  - url: https://www.linkedin.com/company/notionhq
    name: LinkedIn
    type: LinkedIn
    description: 'null'
  - url: https://www.reddit.com/r/Notion/
    name: Reddit
    type: Reddit
    description: 'null'
  - url: https://github.com/ramnes/notion-sdk-py
    name: Notion Python SDK (Community)
    type: SDK
    description: 'null'
  - type: Features
    data:
      - Free plan with trial AI, basic forms/sites, 7-day page history
      - Plus at $10/member/mo with unlimited file uploads and 30-day history
      - Business at $20/member/mo with Notion Agent, SAML SSO, AI Meeting Notes
      - Enterprise with SCIM, audit log, zero-retention with LLM providers
      - REST API for pages, databases, blocks, users, comments, search
      - 'Rate limit: ~3 req/sec average per integration'
      - Webhooks for page and database changes
      - Notion AI integrated across editor and search
      - Notion Calendar and Notion Mail
      - Database queries with filters, sorts, and rollups
      - Custom forms and public sites
      - Up to 1,000 blocks per request
      - OAuth 2.0 for public integrations; internal integration tokens
      - Synced blocks for multi-page content reuse
      - Comments and mentions across pages
      - Page version history (7/30/90 days/unlimited by tier)
    sources:
      - https://www.notion.com/pricing
    updated: '2026-05-04'
created: '2025-01-08'
modified: '2026-05-04'
position: Consumer
description: Notion is an all-in-one workspace that combines notes, tasks, wikis, and databases. The Notion API allows developers to integrate Notion with other tools and build custom applications on top of Notion's platform.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
