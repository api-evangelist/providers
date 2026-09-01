---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Confluence Agentic Access
  operation_count: 27
  slug: confluence-agentic-access
  summary_line: 27 operations · 11 acting
api_count: 1
apis:
- description: Store and retrieve custom data against Confluence content.
  name: Confluence Content Properties API
  slug: confluence-content-properties-api
- description: Search for content in Confluence using CQL (Confluence Query Language).
  name: Confluence Search API
  slug: confluence-search-api
- description: Create, read, update, delete, and archive content including pages and blog posts in Confluence Cloud.
  name: Confluence Content API
  slug: confluence-content-api
- description: Manage Confluence spaces including creation, configuration, permissions, and settings.
  name: Confluence Space API
  slug: confluence-space-api
- description: Add, remove, and manage labels on Confluence content for organization and discovery.
  name: Confluence Content Labels API
  slug: confluence-content-labels-api
- description: Retrieve analytics data including content views and viewer counts for Confluence Cloud.
  name: Confluence Analytics API
  slug: confluence-analytics-api
- description: Access and manage audit log records for compliance and security tracking in Confluence Cloud.
  name: Confluence Audit API
  slug: confluence-audit-api
- description: Manage content templates and blueprints for standardized page creation in Confluence Cloud.
  name: Confluence Template API
  slug: confluence-template-api
- description: Manage user groups and group membership in Confluence Cloud.
  name: Confluence Group API
  slug: confluence-group-api
- description: Retrieve user information, manage user properties, and check permissions in Confluence Cloud.
  name: Confluence Users API
  slug: confluence-users-api
- description: Manage content workflow states such as draft, in progress, and review in Confluence Cloud.
  name: Confluence Content States API
  slug: confluence-content-states-api
- description: Manage read and update restrictions on Confluence content for access control.
  name: Confluence Content Restrictions API
  slug: confluence-content-restrictions-api
- description: Manage permissions for Confluence spaces including user and group access levels.
  name: Confluence Space Permissions API
  slug: confluence-space-permissions-api
- description: Query Confluence data using GraphQL for efficient cross-product data retrieval with field-level precision.
  name: Confluence GraphQL API
  slug: confluence-graphql-api
- description: REST API for Confluence Data Center and Server for on-premise content, space, and user management.
  name: Confluence Data Center REST API
  slug: confluence-data-center-rest-api
- description: Upload, retrieve, update, and delete file attachments on Confluence content.
  name: Confluence Content Attachments API
  slug: confluence-content-attachments-api
- description: Convert content body representations between storage, editor, view, and export formats.
  name: Confluence Content Body API
  slug: confluence-content-body-api
- description: Retrieve children and descendants of Confluence content for navigating content hierarchies.
  name: Confluence Content Children and Descendants API
  slug: confluence-content-children-and-descendants-api
- description: Retrieve the body of a macro in Confluence content by macro ID.
  name: Confluence Content Macro Body API
  slug: confluence-content-macro-body-api
- description: Check content permissions for users to determine read and update access.
  name: Confluence Content Permissions API
  slug: confluence-content-permissions-api
- description: Manage content version history including retrieval, restoration, and deletion of versions.
  name: Confluence Content Versions API
  slug: confluence-content-versions-api
- description: Manage content and space watches to receive notifications on updates.
  name: Confluence Content Watches API
  slug: confluence-content-watches-api
- description: Register and manage dynamic modules for Confluence Connect apps.
  name: Confluence Dynamic Modules API
  slug: confluence-dynamic-modules-api
- description: Experimental endpoints for Confluence Cloud that may change or be removed.
  name: Confluence Experimental API
  slug: confluence-experimental-api
- description: Retrieve information about labels used across Confluence content.
  name: Confluence Label Info API
  slug: confluence-label-info-api
- description: Monitor the status and results of long-running asynchronous tasks in Confluence.
  name: Confluence Long-Running Task API
  slug: confluence-long-running-task-api
- description: Manage relationships between Confluence entities such as content and users.
  name: Confluence Relation API
  slug: confluence-relation-api
- description: Retrieve and manage Confluence site settings and configuration.
  name: Confluence Settings API
  slug: confluence-settings-api
- description: Manage settings for individual Confluence spaces.
  name: Confluence Space Settings API
  slug: confluence-space-settings-api
- description: Retrieve theme information for Confluence spaces and the global site.
  name: Confluence Themes API
  slug: confluence-themes-api
- description: Store and retrieve custom properties associated with Confluence users.
  name: Confluence User Properties API
  slug: confluence-user-properties-api
- description: Create, retrieve, update, and delete pages using the Confluence Cloud REST API v2.
  name: Confluence V2 Page API
  slug: confluence-v2-page-api
- description: Create, retrieve, update, and delete blog posts using the Confluence Cloud REST API v2.
  name: Confluence V2 Blog Post API
  slug: confluence-v2-blog-post-api
- description: Retrieve and manage spaces using the Confluence Cloud REST API v2.
  name: Confluence V2 Space API
  slug: confluence-v2-space-api
- description: Create, retrieve, update, and delete comments on pages and blog posts using the v2 API.
  name: Confluence V2 Comment API
  slug: confluence-v2-comment-api
- description: Manage file attachments on content using the Confluence Cloud REST API v2.
  name: Confluence V2 Attachment API
  slug: confluence-v2-attachment-api
- description: Manage labels on content using the Confluence Cloud REST API v2.
  name: Confluence V2 Label API
  slug: confluence-v2-label-api
- description: Retrieve and manage tasks within Confluence content using the v2 API.
  name: Confluence V2 Task API
  slug: confluence-v2-task-api
- description: Create and manage whiteboards in Confluence using the v2 API.
  name: Confluence V2 Whiteboard API
  slug: confluence-v2-whiteboard-api
- description: Create and manage custom content types in Confluence using the v2 API.
  name: Confluence V2 Custom Content API
  slug: confluence-v2-custom-content-api
- description: Retrieve ancestor pages in the content hierarchy using the v2 API.
  name: Confluence V2 Ancestors API
  slug: confluence-v2-ancestors-api
- description: Retrieve child pages and content in the hierarchy using the v2 API.
  name: Confluence V2 Children API
  slug: confluence-v2-children-api
- description: Retrieve all descendant pages in the content hierarchy using the v2 API.
  name: Confluence V2 Descendants API
  slug: confluence-v2-descendants-api
- description: Manage content versions and version history using the v2 API.
  name: Confluence V2 Version API
  slug: confluence-v2-version-api
- description: Manage likes on Confluence content using the v2 API.
  name: Confluence V2 Like API
  slug: confluence-v2-like-api
- description: Manage space-level permissions using the Confluence Cloud REST API v2.
  name: Confluence V2 Space Permissions API
  slug: confluence-v2-space-permissions-api
- description: Store and retrieve custom properties on Confluence spaces using the v2 API.
  name: Confluence V2 Space Properties API
  slug: confluence-v2-space-properties-api
- description: Manage roles assigned to users and groups within Confluence spaces using the v2 API.
  name: Confluence V2 Space Roles API
  slug: confluence-v2-space-roles-api
- description: Store and manage custom properties on content using the Confluence Cloud REST API v2.
  name: Confluence V2 Content Properties API
  slug: confluence-v2-content-properties-api
- description: Create and manage folders for organizing pages in Confluence using the v2 API.
  name: Confluence V2 Folder API
  slug: confluence-v2-folder-api
- description: Create and manage databases in Confluence using the v2 API.
  name: Confluence V2 Database API
  slug: confluence-v2-database-api
- description: Manage smart links for rich content previews in Confluence using the v2 API.
  name: Confluence V2 Smart Link API
  slug: confluence-v2-smart-link-api
- description: Check permitted operations on content using the Confluence Cloud REST API v2.
  name: Confluence V2 Operation API
  slug: confluence-v2-operation-api
- description: Retrieve user information and details using the Confluence Cloud REST API v2.
  name: Confluence V2 User API
  slug: confluence-v2-user-api
- description: Store and retrieve app-specific properties in Confluence using the v2 API.
  name: Confluence V2 App Properties API
  slug: confluence-v2-app-properties-api
- description: Manage content including conversions and permissions using the Confluence Cloud REST API v2.
  name: Confluence V2 Content API
  slug: confluence-v2-content-api
- description: Retrieve data policy information for Confluence workspaces using the v2 API.
  name: Confluence V2 Data Policies API
  slug: confluence-v2-data-policies-api
- description: Manage content classification levels for data protection in Confluence using the v2 API.
  name: Confluence V2 Classification Level API
  slug: confluence-v2-classification-level-api
- description: Manage content redactions for sensitive information in Confluence using the v2 API.
  name: Confluence V2 Redactions API
  slug: confluence-v2-redactions-api
- description: Manage admin API keys for Confluence Cloud using the v2 API.
  name: Confluence V2 Admin Key API
  slug: confluence-v2-admin-key-api
- description: Manage file attachments on content
  name: Confluence Attachment API
  slug: confluence-attachment-api
- description: Create, retrieve, update, and delete blog posts
  name: Confluence Blog Post API
  slug: confluence-blog-post-api
- description: Create, retrieve, update, and delete comments on pages and blog posts
  name: Confluence Comment API
  slug: confluence-comment-api
- description: Manage labels on content
  name: Confluence Label API
  slug: confluence-label-api
- description: Create, retrieve, update, and delete pages
  name: Confluence Page API
  slug: confluence-page-api
- description: Retrieve and manage Confluence spaces
  name: Confluence Space API
  slug: confluence-space-api
arazzos:
- description: Find a blog post by title, archive it to preserve the record, and optionally delete it.
  name: Confluence Archive or Delete a Blog Post
  slug: confluence-blog-post-retire-workflow
- description: Review a page's comments, read one, then branch to redact it in place or delete it outright.
  name: Confluence Moderate a Page Comment
  slug: confluence-comment-moderation-workflow
- description: List the footer comments on a page, read the thread being answered, post a reply, and read the thread back.
  name: Confluence Reply to a Page Comment Thread
  slug: confluence-comment-thread-reply-workflow
- description: Resolve a space by its key, create a page inside it, and read the stored page back.
  name: Confluence Create a Page in a Space and Read It Back
  slug: confluence-create-page-read-back-workflow
- description: Read a page's storage body, anchor an inline comment to a text selection, and read the page's inline comments back.
  name: Confluence Anchor an Inline Comment to Page Text
  slug: confluence-inline-comment-on-page-workflow
- description: Check a page for children, archive it, and only trash or purge it when explicitly confirmed.
  name: Confluence Archive or Retire a Page
  slug: confluence-page-archive-retire-workflow
- description: List a page's attachments, inspect one in full, and delete it when the caller confirms.
  name: Confluence Audit and Prune a Page Attachment
  slug: confluence-page-attachment-audit-workflow
- description: Verify a page and a target parent, inspect the destination subtree, then reparent the page.
  name: Confluence Move a Page to a New Parent
  slug: confluence-page-move-reparent-workflow
- description: Assemble a complete portrait of a page — body, child pages, attachments, and labels — in one read-only pass.
  name: Confluence Export a Page with Its Children, Attachments, and Labels
  slug: confluence-page-tree-export-workflow
- description: Resolve a space by key, publish a blog post into it, and read the stored post back.
  name: Confluence Publish a Blog Post and Read It Back
  slug: confluence-publish-blog-post-workflow
- description: Find a blog post by title, read its current version, and publish a revised body.
  name: Confluence Find and Revise a Blog Post
  slug: confluence-revise-blog-post-workflow
- description: Resolve a space by key, read its metadata, walk its pages, and resolve the labels on a page.
  name: Confluence Inventory a Space and Its Page Labels
  slug: confluence-space-content-inventory-workflow
- description: Find a page by title within a space and update it if it exists, otherwise create it.
  name: Confluence Upsert a Page by Title
  slug: confluence-upsert-page-by-title-workflow
artifact_total: 267
asyncapis:
- description: Asynchronous event notifications from Confluence Cloud. Webhooks allow applications to receive real-time notifications when content, spaces, or other entities are created, updated, or deleted in Confl
  name: Confluence Cloud Webhooks
  slug: confluence-webhooks
collections:
- collection_type: postman
  name: Confluence Cloud REST API v2 Attachment API
  slug: postman-confluence-attachment-api
- collection_type: postman
  name: Confluence Cloud REST API v2 Attachment Blog Post API
  slug: postman-confluence-blog-post-api
- collection_type: postman
  name: Confluence Cloud REST API v2 Attachment Comment API
  slug: postman-confluence-comment-api
- collection_type: postman
  name: Confluence Cloud REST API v2 Attachment Label API
  slug: postman-confluence-label-api
- collection_type: postman
  name: Confluence Cloud REST API v2 Attachment Page API
  slug: postman-confluence-page-api
- collection_type: postman
  name: Confluence Cloud REST API v2 Attachment Space API
  slug: postman-confluence-space-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Confluence Cloud REST API v2 Attachment API
  slug: open-confluence-attachment-api
- collection_type: open
  name: Confluence Cloud REST API v2 Attachment Blog Post API
  slug: open-confluence-blog-post-api
- collection_type: open
  name: Confluence Cloud REST API v2
  slug: open-confluence-cloud-v2
- collection_type: open
  name: Confluence Cloud REST API v2 Attachment Comment API
  slug: open-confluence-comment-api
- collection_type: open
  name: Confluence Cloud REST API v2 Attachment Label API
  slug: open-confluence-label-api
- collection_type: open
  name: Confluence Cloud REST API v2 Attachment Page API
  slug: open-confluence-page-api
- collection_type: open
  name: Confluence Cloud REST API v2 Attachment Space API
  slug: open-confluence-space-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/confluence/overview
- group: build
  title: ''
  type: Packages
  url: packages/confluence-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/confluence-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/confluence-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/confluence-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/confluence-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/confluence-llms-atlassian.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/confluence-cloud-v2-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/confluence-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/confluence-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/confluence-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/confluence-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/confluence-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/confluence-cli.yml
- group: design
  title: ''
  type: Components
  url: components/confluence-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/confluence-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/confluence-sandbox.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/confluence-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/confluence-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/confluence-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/confluence-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/confluence-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/confluence-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.atlassian.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.atlassian.com/software/confluence
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.atlassian.com/cloud/confluence/getting-started/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.atlassian.com/cloud/confluence/
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.atlassian.com/cloud/confluence/rate-limiting/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.atlassian.com/cloud/confluence/changelog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.atlassian.com/changelog/
- group: operate
  title: ''
  type: Support
  url: https://support.atlassian.com/
- group: operate
  title: ''
  type: Support
  url: https://community.atlassian.com/
- group: operate
  title: ''
  type: Support
  url: https://community.developer.atlassian.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.atlassian.com/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.atlassian.com/cloud/confluence/security-overview/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.atlassian.com/cloud/confluence/oauth-2-3lo-apps/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.atlassian.com/cloud/confluence/scopes-for-oauth-2-3LO-and-forge-apps/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.atlassian.com/cloud/confluence/basic-auth-for-rest-apis/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.atlassian.com/cloud/confluence/using-webhooks/
- group: build
  title: ''
  type: CodeExamples
  url: https://developer.atlassian.com/cloud/confluence/rest-api-examples/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.atlassian.com/cloud/confluence/using-the-rest-api/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.atlassian.com/cloud/confluence/advanced-searching-using-cql/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.atlassian.com/cloud/confluence/deprecation-notice-user-privacy-api-migration-guide/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.atlassian.com/platform/forge/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atlassian.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atlassian.com/legal/cloud-terms-of-service
- group: company
  title: ''
  type: Blog
  url: https://www.atlassian.com/blog/confluence
- group: company
  title: ''
  type: Blog
  url: https://www.atlassian.com/blog/developer
- group: start
  title: ''
  type: Signup
  url: https://www.atlassian.com/try/cloud/signup?bundle=confluence&edition=free
- group: start
  title: ''
  type: Login
  url: https://id.atlassian.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.atlassian.com/software/confluence/pricing
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.atlassian.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atlassian
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Atlassian
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/atlassian-confluence
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/atlassian
- group: other
  title: ''
  type: X
  url: https://twitter.com/Atlassian
- group: build
  title: ''
  type: SDKs
  url: https://developer.atlassian.com/server/framework/atlassian-sdk/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/atlassian-api/atlassian-python-api
- group: build
  title: ''
  type: SDKs
  url: https://mrrefactoring.github.io/confluence.js/
- group: build
  title: ''
  type: SDKs
  url: https://www.postman.com/api-evangelist/atlassian-confluence/collection/k3y2x73/atlassian-confluence-cloud
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/confluence-cloud-v2.yml
- group: docs
  title: ''
  type: OpenAPI
  url: https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/confluence-webhooks.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/confluence-page-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/confluence-space-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/confluence-context.jsonld
- group: design
  title: ''
  type: JSONLD
  url: json-ld/confluence-cloud-v2-context.jsonld
- group: design
  title: ''
  type: Arazzo
  url: arazzo/confluence-blog-post-retire-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/confluence-comment-moderation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/confluence-comment-thread-reply-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/confluence-create-page-read-back-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/confluence-inline-comment-on-page-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/confluence-page-archive-retire-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/confluence-page-attachment-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/confluence-page-move-reparent-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/confluence-page-tree-export-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/confluence-publish-blog-post-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/confluence-revise-blog-post-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/confluence-space-content-inventory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/confluence-upsert-page-by-title-workflow.yml
created: '2024'
description: APIs for Atlassian Confluence - team collaboration and knowledge management software.
examples:
- key_count: 1
  name: Confluence Cloud V2 Attachment Bulk Example
  slug: confluence-cloud-v2-attachment-bulk-example
- key_count: 11
  name: Confluence Cloud V2 Attachment Example
  slug: confluence-cloud-v2-attachment-example
- key_count: 1
  name: Confluence Cloud V2 Blog Post Bulk Example
  slug: confluence-cloud-v2-blog-post-bulk-example
- key_count: 3
  name: Confluence Cloud V2 Blog Post Create Request Example
  slug: confluence-cloud-v2-blog-post-create-request-example
- key_count: 6
  name: Confluence Cloud V2 Blog Post Example
  slug: confluence-cloud-v2-blog-post-example
- key_count: 3
  name: Confluence Cloud V2 Blog Post Update Request Example
  slug: confluence-cloud-v2-blog-post-update-request-example
- key_count: 0
  name: Confluence Cloud V2 Body Example
  slug: confluence-cloud-v2-body-example
- key_count: 2
  name: Confluence Cloud V2 Body Representation Example
  slug: confluence-cloud-v2-body-representation-example
- key_count: 2
  name: Confluence Cloud V2 Body Write Example
  slug: confluence-cloud-v2-body-write-example
- key_count: 1
  name: Confluence Cloud V2 Comment Bulk Example
  slug: confluence-cloud-v2-comment-bulk-example
- key_count: 3
  name: Confluence Cloud V2 Comment Create Request Example
  slug: confluence-cloud-v2-comment-create-request-example
- key_count: 9
  name: Confluence Cloud V2 Comment Example
  slug: confluence-cloud-v2-comment-example
- key_count: 1
  name: Confluence Cloud V2 Comment Links Example
  slug: confluence-cloud-v2-comment-links-example
- key_count: 0
  name: Confluence Cloud V2 Comment Update Request Example
  slug: confluence-cloud-v2-comment-update-request-example
- key_count: 1
  name: Confluence Cloud V2 Content Links Example
  slug: confluence-cloud-v2-content-links-example
- key_count: 1
  name: Confluence Cloud V2 Content Property Array Example
  slug: confluence-cloud-v2-content-property-array-example
- key_count: 3
  name: Confluence Cloud V2 Content Property Example
  slug: confluence-cloud-v2-content-property-example
- key_count: 3
  name: Confluence Cloud V2 Error Example
  slug: confluence-cloud-v2-error-example
- key_count: 2
  name: Confluence Cloud V2 Inline Comment Create Request Example
  slug: confluence-cloud-v2-inline-comment-create-request-example
- key_count: 2
  name: Confluence Cloud V2 Inline Comment Properties Example
  slug: confluence-cloud-v2-inline-comment-properties-example
- key_count: 1
  name: Confluence Cloud V2 Label Array Example
  slug: confluence-cloud-v2-label-array-example
- key_count: 3
  name: Confluence Cloud V2 Label Example
  slug: confluence-cloud-v2-label-example
- key_count: 1
  name: Confluence Cloud V2 Like Array Example
  slug: confluence-cloud-v2-like-array-example
- key_count: 1
  name: Confluence Cloud V2 Like Example
  slug: confluence-cloud-v2-like-example
- key_count: 1
  name: Confluence Cloud V2 Operation Array Example
  slug: confluence-cloud-v2-operation-array-example
- key_count: 2
  name: Confluence Cloud V2 Operation Example
  slug: confluence-cloud-v2-operation-example
- key_count: 1
  name: Confluence Cloud V2 Page Bulk Example
  slug: confluence-cloud-v2-page-bulk-example
- key_count: 4
  name: Confluence Cloud V2 Page Create Request Example
  slug: confluence-cloud-v2-page-create-request-example
- key_count: 11
  name: Confluence Cloud V2 Page Example
  slug: confluence-cloud-v2-page-example
- key_count: 3
  name: Confluence Cloud V2 Page Links Example
  slug: confluence-cloud-v2-page-links-example
- key_count: 5
  name: Confluence Cloud V2 Page Update Request Example
  slug: confluence-cloud-v2-page-update-request-example
- key_count: 2
  name: Confluence Cloud V2 Pagination Links Example
  slug: confluence-cloud-v2-pagination-links-example
- key_count: 1
  name: Confluence Cloud V2 Space Bulk Example
  slug: confluence-cloud-v2-space-bulk-example
- key_count: 0
  name: Confluence Cloud V2 Space Description Example
  slug: confluence-cloud-v2-space-description-example
- key_count: 8
  name: Confluence Cloud V2 Space Example
  slug: confluence-cloud-v2-space-example
- key_count: 2
  name: Confluence Cloud V2 Space Icon Example
  slug: confluence-cloud-v2-space-icon-example
- key_count: 1
  name: Confluence Cloud V2 Space Links Example
  slug: confluence-cloud-v2-space-links-example
- key_count: 1
  name: Confluence Cloud V2 Space Permission Array Example
  slug: confluence-cloud-v2-space-permission-array-example
- key_count: 2
  name: Confluence Cloud V2 Space Permission Example
  slug: confluence-cloud-v2-space-permission-example
- key_count: 1
  name: Confluence Cloud V2 Space Property Array Example
  slug: confluence-cloud-v2-space-property-array-example
- key_count: 1
  name: Confluence Cloud V2 Version Array Example
  slug: confluence-cloud-v2-version-array-example
- key_count: 5
  name: Confluence Cloud V2 Version Example
  slug: confluence-cloud-v2-version-example
- key_count: 2
  name: Confluence Cloud V2 Version Write Example
  slug: confluence-cloud-v2-version-write-example
features:
- 'Free: up to 10 users, 2 GB storage'
- 'Standard: $6.05/user/mo with 250 GB storage'
- 'Premium: $11.55/user/mo with unlimited storage and analytics'
- Enterprise typically $23-$25/user/mo with AI, 99.95% uptime
- REST API at api.atlassian.com/wiki
- Rate limit ~10 req/sec/app/user
- Bulk operations max 100 items/request
- Pages, blog posts, comments, attachments, spaces APIs
- Webhooks for content changes
- OAuth 2.0 (3LO) and API tokens
- CQL (Confluence Query Language) for search
- Atlassian Connect framework for marketplace apps
- Forge for serverless app development
- Atlassian Intelligence (Enterprise)
- Page tree, macros, templates, smart links
- External collaboration via guest access
finops:
- name: Confluence Finops
  service_category: Wiki
  slug: confluence-finops
graphqls:
- description: Query Confluence data using GraphQL for efficient cross-product data retrieval with field-level precision.
  name: Confluence GraphQL API
  slug: confluence-graphql
image: https://www.atlassian.com/dam/jcr:5d1374c2-276f-4bca-9ce4-b3f5e2dd5d6c/confluence-icon-gradient-blue.svg
integrations:
- description: Link Confluence pages to Jira issues for seamless project management workflows.
  name: Jira
- description: Receive Confluence notifications and preview pages directly in Slack channels.
  name: Slack
- description: Collaborate on Confluence content within Microsoft Teams conversations.
  name: Microsoft Teams
- description: Embed Trello boards in Confluence pages and link cards to documentation.
  name: Trello
- description: Embed code snippets and link repositories to Confluence documentation.
  name: GitHub
json_schemas:
- name: AttachmentBulk
  property_count: 1
  slug: confluence-cloud-v2-attachment-bulk
- name: Attachment
  property_count: 11
  slug: confluence-cloud-v2-attachment
- name: BlogPostBulk
  property_count: 1
  slug: confluence-cloud-v2-blog-post-bulk
- name: BlogPostCreateRequest
  property_count: 3
  slug: confluence-cloud-v2-blog-post-create-request
- name: BlogPost
  property_count: 6
  slug: confluence-cloud-v2-blog-post
- name: BlogPostUpdateRequest
  property_count: 3
  slug: confluence-cloud-v2-blog-post-update-request
- name: BodyRepresentation
  property_count: 2
  slug: confluence-cloud-v2-body-representation
- name: Body
  property_count: 0
  slug: confluence-cloud-v2-body
- name: BodyWrite
  property_count: 2
  slug: confluence-cloud-v2-body-write
- name: CommentBulk
  property_count: 1
  slug: confluence-cloud-v2-comment-bulk
- name: CommentCreateRequest
  property_count: 3
  slug: confluence-cloud-v2-comment-create-request
- name: CommentLinks
  property_count: 1
  slug: confluence-cloud-v2-comment-links
- name: Comment
  property_count: 9
  slug: confluence-cloud-v2-comment
- name: CommentUpdateRequest
  property_count: 0
  slug: confluence-cloud-v2-comment-update-request
- name: ContentLinks
  property_count: 1
  slug: confluence-cloud-v2-content-links
- name: ContentPropertyArray
  property_count: 1
  slug: confluence-cloud-v2-content-property-array
- name: ContentProperty
  property_count: 3
  slug: confluence-cloud-v2-content-property
- name: Error
  property_count: 3
  slug: confluence-cloud-v2-error
- name: InlineCommentCreateRequest
  property_count: 2
  slug: confluence-cloud-v2-inline-comment-create-request
- name: InlineCommentProperties
  property_count: 2
  slug: confluence-cloud-v2-inline-comment-properties
- name: LabelArray
  property_count: 1
  slug: confluence-cloud-v2-label-array
- name: Label
  property_count: 3
  slug: confluence-cloud-v2-label
- name: LikeArray
  property_count: 1
  slug: confluence-cloud-v2-like-array
- name: Like
  property_count: 1
  slug: confluence-cloud-v2-like
- name: OperationArray
  property_count: 1
  slug: confluence-cloud-v2-operation-array
- name: Operation
  property_count: 2
  slug: confluence-cloud-v2-operation
- name: PageBulk
  property_count: 1
  slug: confluence-cloud-v2-page-bulk
- name: PageCreateRequest
  property_count: 4
  slug: confluence-cloud-v2-page-create-request
- name: PageLinks
  property_count: 3
  slug: confluence-cloud-v2-page-links
- name: Page
  property_count: 11
  slug: confluence-cloud-v2-page
- name: PageUpdateRequest
  property_count: 5
  slug: confluence-cloud-v2-page-update-request
- name: PaginationLinks
  property_count: 2
  slug: confluence-cloud-v2-pagination-links
- name: SpaceBulk
  property_count: 1
  slug: confluence-cloud-v2-space-bulk
- name: SpaceDescription
  property_count: 0
  slug: confluence-cloud-v2-space-description
- name: SpaceIcon
  property_count: 2
  slug: confluence-cloud-v2-space-icon
- name: SpaceLinks
  property_count: 1
  slug: confluence-cloud-v2-space-links
- name: SpacePermissionArray
  property_count: 1
  slug: confluence-cloud-v2-space-permission-array
- name: SpacePermission
  property_count: 2
  slug: confluence-cloud-v2-space-permission
- name: SpacePropertyArray
  property_count: 1
  slug: confluence-cloud-v2-space-property-array
- name: Space
  property_count: 8
  slug: confluence-cloud-v2-space
- name: VersionArray
  property_count: 1
  slug: confluence-cloud-v2-version-array
- name: Version
  property_count: 5
  slug: confluence-cloud-v2-version
- name: VersionWrite
  property_count: 2
  slug: confluence-cloud-v2-version-write
- name: Confluence Page
  property_count: 19
  slug: confluence-page
- name: Confluence Space
  property_count: 15
  slug: confluence-space
json_structures:
- name: Confluence Cloud V2 Attachment Bulk Structure
  property_count: 1
  slug: confluence-cloud-v2-attachment-bulk-structure
- name: Confluence Cloud V2 Attachment Structure
  property_count: 11
  slug: confluence-cloud-v2-attachment-structure
- name: Confluence Cloud V2 Blog Post Bulk Structure
  property_count: 1
  slug: confluence-cloud-v2-blog-post-bulk-structure
- name: Confluence Cloud V2 Blog Post Create Request Structure
  property_count: 3
  slug: confluence-cloud-v2-blog-post-create-request-structure
- name: Confluence Cloud V2 Blog Post Structure
  property_count: 6
  slug: confluence-cloud-v2-blog-post-structure
- name: Confluence Cloud V2 Blog Post Update Request Structure
  property_count: 3
  slug: confluence-cloud-v2-blog-post-update-request-structure
- name: Confluence Cloud V2 Body Representation Structure
  property_count: 2
  slug: confluence-cloud-v2-body-representation-structure
- name: Confluence Cloud V2 Body Structure
  property_count: 0
  slug: confluence-cloud-v2-body-structure
- name: Confluence Cloud V2 Body Write Structure
  property_count: 2
  slug: confluence-cloud-v2-body-write-structure
- name: Confluence Cloud V2 Comment Bulk Structure
  property_count: 1
  slug: confluence-cloud-v2-comment-bulk-structure
- name: Confluence Cloud V2 Comment Create Request Structure
  property_count: 3
  slug: confluence-cloud-v2-comment-create-request-structure
- name: Confluence Cloud V2 Comment Links Structure
  property_count: 1
  slug: confluence-cloud-v2-comment-links-structure
- name: Confluence Cloud V2 Comment Structure
  property_count: 9
  slug: confluence-cloud-v2-comment-structure
- name: Confluence Cloud V2 Comment Update Request Structure
  property_count: 0
  slug: confluence-cloud-v2-comment-update-request-structure
- name: Confluence Cloud V2 Content Links Structure
  property_count: 1
  slug: confluence-cloud-v2-content-links-structure
- name: Confluence Cloud V2 Content Property Array Structure
  property_count: 1
  slug: confluence-cloud-v2-content-property-array-structure
- name: Confluence Cloud V2 Content Property Structure
  property_count: 3
  slug: confluence-cloud-v2-content-property-structure
- name: Confluence Cloud V2 Error Structure
  property_count: 3
  slug: confluence-cloud-v2-error-structure
- name: Confluence Cloud V2 Inline Comment Create Request Structure
  property_count: 2
  slug: confluence-cloud-v2-inline-comment-create-request-structure
- name: Confluence Cloud V2 Inline Comment Properties Structure
  property_count: 2
  slug: confluence-cloud-v2-inline-comment-properties-structure
- name: Confluence Cloud V2 Label Array Structure
  property_count: 1
  slug: confluence-cloud-v2-label-array-structure
- name: Confluence Cloud V2 Label Structure
  property_count: 3
  slug: confluence-cloud-v2-label-structure
- name: Confluence Cloud V2 Like Array Structure
  property_count: 1
  slug: confluence-cloud-v2-like-array-structure
- name: Confluence Cloud V2 Like Structure
  property_count: 1
  slug: confluence-cloud-v2-like-structure
- name: Confluence Cloud V2 Operation Array Structure
  property_count: 1
  slug: confluence-cloud-v2-operation-array-structure
- name: Confluence Cloud V2 Operation Structure
  property_count: 2
  slug: confluence-cloud-v2-operation-structure
- name: Confluence Cloud V2 Page Bulk Structure
  property_count: 1
  slug: confluence-cloud-v2-page-bulk-structure
- name: Confluence Cloud V2 Page Create Request Structure
  property_count: 4
  slug: confluence-cloud-v2-page-create-request-structure
- name: Confluence Cloud V2 Page Links Structure
  property_count: 3
  slug: confluence-cloud-v2-page-links-structure
- name: Confluence Cloud V2 Page Structure
  property_count: 11
  slug: confluence-cloud-v2-page-structure
- name: Confluence Cloud V2 Page Update Request Structure
  property_count: 5
  slug: confluence-cloud-v2-page-update-request-structure
- name: Confluence Cloud V2 Pagination Links Structure
  property_count: 2
  slug: confluence-cloud-v2-pagination-links-structure
- name: Confluence Cloud V2 Space Bulk Structure
  property_count: 1
  slug: confluence-cloud-v2-space-bulk-structure
- name: Confluence Cloud V2 Space Description Structure
  property_count: 0
  slug: confluence-cloud-v2-space-description-structure
- name: Confluence Cloud V2 Space Icon Structure
  property_count: 2
  slug: confluence-cloud-v2-space-icon-structure
- name: Confluence Cloud V2 Space Links Structure
  property_count: 1
  slug: confluence-cloud-v2-space-links-structure
- name: Confluence Cloud V2 Space Permission Array Structure
  property_count: 1
  slug: confluence-cloud-v2-space-permission-array-structure
- name: Confluence Cloud V2 Space Permission Structure
  property_count: 2
  slug: confluence-cloud-v2-space-permission-structure
- name: Confluence Cloud V2 Space Property Array Structure
  property_count: 1
  slug: confluence-cloud-v2-space-property-array-structure
- name: Confluence Cloud V2 Space Structure
  property_count: 8
  slug: confluence-cloud-v2-space-structure
- name: Confluence Cloud V2 Version Array Structure
  property_count: 1
  slug: confluence-cloud-v2-version-array-structure
- name: Confluence Cloud V2 Version Structure
  property_count: 5
  slug: confluence-cloud-v2-version-structure
- name: Confluence Cloud V2 Version Write Structure
  property_count: 2
  slug: confluence-cloud-v2-version-write-structure
jsonld:
- class_count: 0
  name: Confluence Cloud V2 Context
  property_count: 0
  slug: confluence-cloud-v2-context
- class_count: 0
  name: Confluence Context
  property_count: 8
  slug: confluence-context
layout: provider
mcp_servers:
- description: Official Atlassian Rovo MCP Server — a cloud-hosted (Cloudflare) remote MCP server that bridges Atlassian Cloud (Confluence, Jira, Jira Service Management, Bitbucket, Compass) to AI clients. Confluenc
  name: Confluence MCP Server
  slug: confluence-mcp-server
modified: '2026-06-20'
name: Confluence
nav: Providers
network: true
overview: 'Confluence publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Space API, Attachment API, Blog Post API, and 4 more. Tagged areas include Collaboration, Content Management, Documentation, Knowledge Base, and Wiki.


  The Confluence catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 3 Spectral governance rulesets.


  Confluence''s developer surface includes changelog, CLI, sandbox, authentication, developer portal, documentation, getting-started guide, and 74 more developer resources.'
plans:
- name: Confluence Plans Pricing
  plan_count: 4
  slug: confluence-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 2
  name: Confluence Rate Limits
  slug: confluence-rate-limits
rules:
- effective_rule_count: 37
  extends:
  - spectral:asyncapi
  name: Confluence API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 8
  slug: confluence-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Confluence API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: confluence-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Confluence API Rules
  rule_count: 18
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 9
  slug: confluence-spectral-rules
scopes:
- name: Confluence Scopes
  scope_count: 9
  slug: confluence-scopes
  summary_line: 9 scopes · authorizationCode
score:
  band: strong
  composite: 63.8
  coverage:
    artifact_dirs: 35
    catalog_gap: 68.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 56.6
    commercial_clarity: 56.6
    contract_governance: 18.2
    contract_quality: 79.0
    developer_ergonomics: 92.9
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 63.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/confluence/refs/heads/main/screenshots/confluence-2026-06-20T174854.png
security:
- kind: authentication
  name: Confluence Authentication
  slug: confluence-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Confluence Domain Security
  slug: confluence-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Confluence Vulnerability Disclosure
  slug: confluence-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Confluence Trust Center
  slug: confluence-trust-center
  summary_line: SOC 2 Type II, SOC 3, ISO 27001, ISO 27017, ISO 27018, ISO 27701, PCI DSS, FedRAMP, HIPAA, CSA STAR, GDPR
slug: confluence
tags:
- Collaboration
- Content Management
- Documentation
- Knowledge Base
- Wiki
use_cases:
- description: Build and maintain internal knowledge bases for teams with structured content and search.
  name: Knowledge Base
- description: Create and collaborate on project documentation with version tracking and approvals.
  name: Project Documentation
- description: Programmatically migrate content between Confluence instances or from other platforms.
  name: Content Migration
- description: Track content changes, manage access controls, and maintain audit trails.
  name: Compliance and Auditing
- description: Generate and publish content programmatically from CI/CD pipelines or other systems.
  name: Automated Publishing
website: https://developer.atlassian.com/cloud/confluence/
---
