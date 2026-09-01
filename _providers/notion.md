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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: documented
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Notion Agentic Access
  operation_count: 19
  slug: notion-agentic-access
  summary_line: 19 operations · 10 acting
api_count: 1
apis:
- description: Blocks are the fundamental units of content in Notion. Every page is composed of blocks, which can be paragraphs, headings, images, tables, lists, and many other types. Blocks can have children, formi
  name: Notion Blocks API
  slug: notion-blocks-api
- description: Comments allow integrations to read and create comments on pages and blocks within Notion. Comments support rich text content and are associated with discussion threads.
  name: Notion Comments API
  slug: notion-comments-api
- description: Databases are collections of Notion pages organized with a shared schema of properties. Each database defines columns (properties) that all its pages share. Databases support filtering, sorting, and q
  name: Notion Databases API
  slug: notion-databases-api
- description: Pages represent documents in Notion workspaces. They can exist as standalone pages or as entries within a database. Pages contain properties (metadata) and content composed of blocks. Use these endpoi
  name: Notion Pages API
  slug: notion-pages-api
- description: Search allows querying across all pages and databases that the integration has access to. Results can be filtered by object type and sorted by relevance or last edited time.
  name: Notion Search API
  slug: notion-search-api
- description: 'Users represent people or bots in a Notion workspace. Person users are human members of the workspace, while bot users represent API integrations. Use these endpoints to list users, retrieve specific '
  name: Notion Users API
  slug: notion-users-api
arazzos:
- description: List a page's blocks, update the first block's text, then optionally archive it based on a flag.
  name: Notion Edit and Optionally Delete a Page Block
  slug: notion-block-edit-cleanup-workflow
- description: List a page's unresolved comments, then reply into the existing discussion or start a new one.
  name: Notion Reply to an Existing Comment Thread
  slug: notion-comment-thread-reply-workflow
- description: Stand up a new Notion database under a page, add a first entry, then fill that entry with content blocks.
  name: Notion Create a Database, Seed a Page, and Add Content
  slug: notion-create-database-page-content-workflow
- description: Create a standalone page with content blocks, then retrieve that page's block children.
  name: Notion Create a Page and Read Back Its Content
  slug: notion-create-page-read-children-workflow
- description: Discover a database by title, read its schema, then add a new page row whose properties conform to it.
  name: Notion Sync a Row into a Database Data Source
  slug: notion-data-source-sync-workflow
- description: Read a database schema, query its first record, then pull that record's page content blocks.
  name: Notion Export a Database Record with Its Content
  slug: notion-database-record-export-workflow
- description: Retrieve a database, add a property to its schema, then query it back to confirm the change.
  name: Notion Evolve a Database Schema and Re-Query
  slug: notion-database-schema-evolution-workflow
- description: Retrieve a page, then fetch one named property item from it in full (including paginated values).
  name: Notion Audit a Single Page Property
  slug: notion-page-property-audit-workflow
- description: Query a database with a filter, retrieve the first matching page, then update its properties.
  name: Notion Query a Database and Update a Matched Page
  slug: notion-query-update-page-properties-workflow
- description: Search the workspace by title for a page, then leave a comment on the first matching page.
  name: Notion Search for a Page and Comment on It
  slug: notion-search-page-comment-workflow
- description: Identify the integration bot, list workspace users, then retrieve the first user in detail.
  name: Notion Resolve a Workspace User Directory
  slug: notion-user-directory-resolve-workflow
artifact_total: 71
asyncapis:
- description: AsyncAPI 2.6 description of the Notion webhooks surface. Notion delivers workspace events (page, database, data source, and comment changes) to a subscriber-hosted HTTPS endpoint via signed POST reque
  name: Notion Webhooks
  slug: notion-webhooks-asyncapi
collections:
- collection_type: postman
  name: Notion API
  slug: postman-notion
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Notion Blocks API
  slug: open-notion-blocks-api
- collection_type: open
  name: Notion Blocks Comments API
  slug: open-notion-comments-api
- collection_type: open
  name: Notion Blocks Databases API
  slug: open-notion-databases-api
- collection_type: open
  name: Notion Blocks Pages API
  slug: open-notion-pages-api
- collection_type: open
  name: Notion Blocks Search API
  slug: open-notion-search-api
- collection_type: open
  name: Notion Blocks Users API
  slug: open-notion-users-api
- collection_type: open
  name: Notion API
  slug: open-notion
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/makenotion/notion-sdk-js/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/makenotion/notion-sdk-js/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/makenotion/notion-sdk-js/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/notion/overview
- group: build
  title: ''
  type: Packages
  url: packages/notion-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/notion-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/notion-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/notion-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/notion-security.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/notion-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/notion-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/notion-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/notion-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/notion-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/notion-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/notion-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/notion-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/notion-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/notion-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/notion-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/notion-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/notion-authentication.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/notion-block-edit-cleanup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/notion-comment-thread-reply-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/notion-create-database-page-content-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/notion-create-page-read-children-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/notion-data-source-sync-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/notion-database-record-export-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/notion-database-schema-evolution-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/notion-page-property-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/notion-query-update-page-properties-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/notion-search-page-comment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/notion-user-directory-resolve-workflow.yml
- group: docs
  title: ''
  type: Guide
  url: https://developers.notion.com/docs/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/intro
- group: company
  title: ''
  type: Blog
  url: https://www.notion.com/blog
- group: build
  title: ''
  type: Examples
  url: https://developers.notion.com/page/examples
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.notion.com/page/changelog
- group: design
  title: ''
  type: Versioning
  url: https://developers.notion.com/reference/versioning
- group: design
  title: ''
  type: ErrorCodes
  url: https://developers.notion.com/reference/status-codes
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.notion.com/reference/request-limits
- group: design
  title: ''
  type: Webhooks
  url: https://developers.notion.com/reference/webhooks
- group: other
  title: ''
  type: ''
  url: https://www.postman.com/notionhq/notion-s-api-workspace/overview
- group: auth
  title: ''
  type: Authentication
  url: https://developers.notion.com/reference/authentication
- group: auth
  title: ''
  type: Authorization
  url: https://developers.notion.com/docs/authorization
- group: operate
  title: ''
  type: FAQ
  url: https://developers.notion.com/page/frequently-asked-questions
- group: docs
  title: ''
  type: Guide
  url: https://developers.notion.com/docs/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.notion.com/docs/create-a-notion-integration
- group: docs
  title: ''
  type: Guide
  url: https://developers.notion.com/docs/publishing-integrations-to-notions-integration-gallery
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/capabilities
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.notion.com/reference/changes-by-version
- group: docs
  title: ''
  type: OpenAPI
  url: https://developers.notion.com/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.notion.so/Developer-Terms-ba4131408d0844e08330da2cbb225c20
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.notion.so/terms
- group: auth
  title: ''
  type: Security
  url: https://www.notion.com/security
- group: auth
  title: ''
  type: Security
  url: https://www.notion.com/help/security-and-privacy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacycenter.notion.so/policies
- group: commercial
  title: ''
  type: Pricing
  url: https://www.notion.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.notion.so/
- group: build
  title: ''
  type: IntegrationGallery
  url: https://www.notion.com/integrations
- group: start
  title: ''
  type: Portal
  url: https://www.notion.so/my-integrations
- group: build
  title: ''
  type: SDKs
  url: https://github.com/makenotion/notion-sdk-js
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@notionhq/client
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/makenotion/notion-mcp-server
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/makenotion
- group: company
  title: ''
  type: Partners
  url: https://www.notion.com/lp/technology-partner-program
- group: operate
  title: ''
  type: Support
  url: https://www.notion.com/help
- group: operate
  title: ''
  type: Community
  url: https://www.notion.com/community
- group: other
  title: ''
  type: X
  url: https://x.com/NotionAPI
- group: other
  title: ''
  type: X
  url: https://x.com/NotionHQ
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/notion-api
- group: docs
  title: ''
  type: Guide
  url: https://developers.notion.com/docs/working-with-databases
- group: docs
  title: ''
  type: Guide
  url: https://developers.notion.com/docs/working-with-page-content
- group: docs
  title: ''
  type: Guide
  url: https://developers.notion.com/docs/working-with-comments
- group: docs
  title: ''
  type: Guide
  url: https://developers.notion.com/docs/working-with-files-and-media
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/search-optimizations-and-limitations
- group: docs
  title: ''
  type: Guide
  url: https://developers.notion.com/guides/link-previews/link-previews
- group: docs
  title: ''
  type: Documentation
  url: https://www.notion.com/help/provision-users-and-groups-with-scim
- group: docs
  title: ''
  type: Guide
  url: https://developers.notion.com/docs/upgrade-guide-2025-09-03
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/database
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/data-source
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/page
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/block
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/user
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/comment-object
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/rich-text
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/file-object
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/file-upload
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/emoji-object
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/parent-object
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/page-property-values
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/property-item-object
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/property-object
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/update-property-schema-object
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/update-data-source-properties
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/post-database-query-filter
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/post-database-query-sort
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/filter-data-source-entries
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/sort-data-source-entries
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/comment-attachment
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/comment-display-name
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/unfurl-attribute-object
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/create-a-token
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/introspect-token
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/refresh-a-token
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/reference/revoke-token
- group: design
  title: ''
  type: Webhooks
  url: https://developers.notion.com/reference/webhooks-events-delivery
- group: docs
  title: ''
  type: Documentation
  url: https://developers.notion.com/llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.notion.com/releases
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/notionhq
- group: other
  title: ''
  type: Reddit
  url: https://www.reddit.com/r/Notion/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/ramnes/notion-sdk-py
created: '2025-01-08'
description: Notion is an all-in-one workspace that combines notes, tasks, wikis, and databases. The Notion API allows developers to integrate Notion with other tools and build custom applications on top of Notion's platform.
features:
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
finops:
- name: Notion Finops
  service_category: Productivity
  slug: notion-finops
graphqls:
- description: Notion does not expose a public GraphQL endpoint. Notion's public API is a versioned REST API (`api.notion.com/v1`). The GraphQL schema in `notion-schema.graphql` is a comprehensive conceptual model d
  name: Notion GraphQL
  slug: notion-graphql
image: https://www.notion.so/images/meta/default.png
json_schemas:
- name: Notion Block
  property_count: 43
  slug: notion-block
- name: Comment
  property_count: 8
  slug: notion-comment
- name: Notion Database
  property_count: 18
  slug: notion-database
- name: Emoji
  property_count: 2
  slug: notion-emoji
- name: Error
  property_count: 5
  slug: notion-error
- name: ExternalFile
  property_count: 2
  slug: notion-externalfile
- name: File
  property_count: 5
  slug: notion-file
- name: Notion Page
  property_count: 15
  slug: notion-page
- name: PaginatedList
  property_count: 6
  slug: notion-paginatedlist
- name: Parent
  property_count: 5
  slug: notion-parent
- name: PartialUser
  property_count: 2
  slug: notion-partialuser
- name: PropertySchema
  property_count: 3
  slug: notion-propertyschema
- name: RichText
  property_count: 7
  slug: notion-richtext
- name: User
  property_count: 7
  slug: notion-user
json_structures:
- name: Notion Structure
  property_count: 0
  slug: notion-structure
jsonld:
- class_count: 0
  name: Notion Context
  property_count: 12
  slug: notion-context
layout: provider
mcp_servers:
- description: ''
  name: Notion MCP Server
  slug: notion-mcp-server
modified: '2026-06-20'
name: Notion
nav: Providers
network: true
overview: 'Notion publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Blocks API, Comments API, Databases API, and 3 more. Tagged areas include Collaboration, Database, Ideas, Notes, and Productivity.


  The Notion catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Notion''s developer surface includes changelog, CLI, authentication, documentation, engineering blog, code examples, FAQ, and 105 more developer resources.'
plans:
- name: Notion Plans Pricing
  plan_count: 4
  slug: notion-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Notion Rate Limits
  slug: notion-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Notion API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: notion-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Notion API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: notion-jsonschema-spectral-rules
score:
  band: strong
  composite: 62.4
  coverage:
    artifact_dirs: 34
    catalog_gap: 54.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 81.9
    developer_ergonomics: 78.6
    discoverability: 61.1
    governance: 18.2
    operational_transparency: 63.2
  open_source:
    applies: true
    score: 50.0
  previous_composite: 62.4
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
screenshot: https://raw.githubusercontent.com/api-evangelist/notion/refs/heads/main/screenshots/notion-2026-06-20T190428.png
security:
- kind: authentication
  name: Notion Authentication
  slug: notion-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Notion Domain Security
  slug: notion-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Notion Vulnerability Disclosure
  slug: notion-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Notion Trust Center
  slug: notion-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, GDPR
slug: notion
tags:
- Collaboration
- Database
- Ideas
- Notes
- Productivity
- Project
- T1
- Task
- Wiki
- Workspace
website: https://www.notion.so/my-integrations
---
