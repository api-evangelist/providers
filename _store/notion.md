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
created: '2025-01-08'
modified: '2026-04-07'
position: Consumer
description: Notion is an all-in-one workspace that combines notes, tasks, wikis, and databases. The Notion API allows developers to integrate Notion with other tools and build custom applications on top of Notion's platform.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

