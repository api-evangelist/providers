---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 59.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Figma Agentic Access
  operation_count: 31
  slug: figma-agentic-access
  summary_line: 31 operations · 6 acting
api_count: 16
apis:
- description: Figma Files API provides access to design file data including document trees, nodes, images, version history, and file metadata. Read and export design data from Figma files programmatically.
  name: Figma Files API
  slug: figma-files-api
- description: Figma Images API provides endpoints for rendering and exporting images from Figma files in various formats including PNG, JPG, SVG, and PDF.
  name: Figma Images API
  slug: figma-images-api
- description: Figma Teams API provides endpoints for managing team-level resources including webhooks, projects, and team configuration.
  name: Figma Teams API
  slug: figma-teams-api
- description: Figma Projects API provides endpoints for listing team projects and retrieving project files.
  name: Figma Projects API
  slug: figma-projects-api
- description: Figma Me API provides the endpoint for retrieving information about the currently authenticated user.
  name: Figma Me API
  slug: figma-me-api
- description: Figma Component Sets API provides endpoints for retrieving published component set metadata from team libraries.
  name: Figma Component Sets API
  slug: figma-component-sets-api
- description: Figma Styles API provides endpoints for retrieving published style metadata including colors, text styles, and effects from team libraries.
  name: Figma Styles API
  slug: figma-styles-api
- description: Figma Activity Logs API provides endpoints for retrieving activity log events for an organization, enabling audit trail and compliance monitoring.
  name: Figma Activity Logs API
  slug: figma-activity-logs-api
- description: Figma Payments API provides endpoints for querying user payment information on plugins, widgets, and Community files.
  name: Figma Payments API
  slug: figma-payments-api
- description: Figma Dev Resources API provides endpoints for creating, updating, and deleting dev resources attached to design nodes, enabling design-to-code workflows.
  name: Figma Dev Resources API
  slug: figma-dev-resources-api
- description: Endpoints for managing comments and reactions on Figma files, including creating, listing, and deleting comments.
  name: Figma Comments API
  slug: figma-comments-api
- description: Endpoints for querying published components, component sets, and styles from team libraries.
  name: Figma Components API
  slug: figma-components-api
- description: Operations that use unique style keys for identification
  name: Figma Keys API
  slug: figma-keys-api
- description: Operations for retrieving library usage and action analytics data
  name: Figma Library Analytics API
  slug: figma-library-analytics-api
- description: Operations related to user information and authentication
  name: Figma Users API
  slug: figma-users-api
- description: Operations for managing webhook subscriptions and notifications
  name: Figma Webhooks API
  slug: figma-webhooks-api
arazzos:
- description: Confirm a file and node exist, then attach a code or doc link to that node.
  name: Figma Attach Dev Resource to Node
  slug: figma-attach-dev-resource-to-node-workflow
- description: List a team's published components, inspect one, and open its source file.
  name: Figma Audit Team Component
  slug: figma-audit-team-component-workflow
- description: Confirm the authenticated user, then list the webhooks registered for a team.
  name: Figma Audit Team Webhooks
  slug: figma-audit-team-webhooks-workflow
- description: List files in a project, open the first file, and read its comments.
  name: Figma Browse Project File Comments
  slug: figma-browse-project-file-comments-workflow
- description: Open a file and list the local published components it defines.
  name: Figma Catalog File Components
  slug: figma-catalog-file-components-workflow
- description: List a team's published component sets and pull metadata for the first one.
  name: Figma Inventory Team Component Sets
  slug: figma-inventory-team-component-sets-workflow
- description: List a team's published styles and pull full metadata for the first one.
  name: Figma Inventory Team Styles
  slug: figma-inventory-team-styles-workflow
- description: Post a new comment to a file, then read the thread back to confirm it landed.
  name: Figma Post and Verify Comment
  slug: figma-post-and-verify-comment-workflow
- description: Find the most recent comment on a file, add an emoji reaction, and list reactions.
  name: Figma React to Latest Comment
  slug: figma-react-to-latest-comment-workflow
- description: Open a file, drill into specific nodes, and render them to image URLs.
  name: Figma Render File Node Images
  slug: figma-render-file-node-images-workflow
- description: Open a library file, then pull its component or style usage analytics.
  name: Figma Report Library Usage
  slug: figma-report-library-usage-workflow
- description: Walk a team to its first project, list that project's files, and read one file's version history.
  name: Figma Snapshot Team Project Versions
  slug: figma-snapshot-team-project-versions-workflow
artifact_total: 550
asyncapis:
- description: Figma Webhooks allow applications to receive real-time notifications when events occur in Figma files and projects. Webhooks are configured at the team level and send HTTP POST requests with JSON payl
  name: Figma Webhooks
  slug: figma-webhooks-asyncapi
collections:
- collection_type: postman
  name: Figma Activity Logs API
  slug: postman-figma-activity-logs-api
- collection_type: postman
  name: Figma Analytics API
  slug: postman-figma-analytics-api
- collection_type: postman
  name: Figma API
  slug: postman-figma-api
- collection_type: postman
  name: Figma Component Sets API
  slug: postman-figma-component-sets-api
- collection_type: postman
  name: Figma Dev Resources API
  slug: postman-figma-dev-resources-api
- collection_type: postman
  name: Figma Files API
  slug: postman-figma-files-api
- collection_type: postman
  name: Figma Images API
  slug: postman-figma-images-api
- collection_type: postman
  name: Figma Me API
  slug: postman-figma-me-api
- collection_type: postman
  name: Figma Payments API
  slug: postman-figma-payments-api
- collection_type: postman
  name: Figma Projects API
  slug: postman-figma-projects-api
- collection_type: postman
  name: Figma REST API
  slug: postman-figma-rest-api
- collection_type: postman
  name: Figma Styles API
  slug: postman-figma-styles-api
- collection_type: postman
  name: Figma Teams API
  slug: postman-figma-teams-api
- collection_type: open
  name: Figma Activity Logs API
  slug: open-figma-activity-logs-api
- collection_type: open
  name: Figma Analytics API
  slug: open-figma-analytics-api
- collection_type: open
  name: Figma API
  slug: open-figma-api
- collection_type: open
  name: Figma Component Sets API
  slug: open-figma-component-sets-api
- collection_type: open
  name: Figma Dev Resources API
  slug: open-figma-dev-resources-api
- collection_type: open
  name: Figma Files API
  slug: open-figma-files-api
- collection_type: open
  name: Figma Images API
  slug: open-figma-images-api
- collection_type: open
  name: Figma Me API
  slug: open-figma-me-api
- collection_type: open
  name: Figma Payments API
  slug: open-figma-payments-api
- collection_type: open
  name: Figma Projects API
  slug: open-figma-projects-api
- collection_type: open
  name: Figma REST API
  slug: open-figma-rest-api
- collection_type: open
  name: Figma Styles API
  slug: open-figma-styles-api
- collection_type: open
  name: Figma Teams API
  slug: open-figma-teams-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/figma-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/figma-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/figma-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/figma-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/figma-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/figma-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/figma-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/figma-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/figma-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/figma-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/figma-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/figma-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/figma-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/figma-trust-center.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/figma-conventions.yml
- group: operate
  title: Changelog artifact
  type: ChangeLog
  url: changelog/figma-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/figma-cli.yml
- group: design
  title: ''
  type: Components
  url: components/figma-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/figma-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/figma-activity-logs-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/figma-analytics-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/figma-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/figma-component-sets-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/figma-dev-resources-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/figma-files-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/figma-images-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/figma-me-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/figma-payments-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/figma-projects-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/figma-rest-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/figma-styles-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/figma-teams-api-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/figma/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/figma-attach-dev-resource-to-node-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/figma-audit-team-component-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/figma-audit-team-webhooks-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/figma-browse-project-file-comments-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/figma-catalog-file-components-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/figma-inventory-team-component-sets-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/figma-inventory-team-styles-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/figma-post-and-verify-comment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/figma-react-to-latest-comment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/figma-render-file-node-images-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/figma-report-library-usage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/figma-snapshot-team-project-versions-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/figma
- group: start
  title: ''
  type: Portal
  url: https://www.figma.com/developers
- group: auth
  title: ''
  type: Authentication
  url: https://developers.figma.com/docs/rest-api/authentication/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.figma.com/docs/rest-api/changelog/
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.figma.com/docs/rest-api/rate-limits/
- group: docs
  title: Figma REST API OpenAPI Specification
  type: OpenAPI
  url: https://github.com/figma/rest-api-spec
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.figma.com/docs/code-connect/quickstart-guide/
- group: start
  title: ''
  type: Signup
  url: https://www.figma.com/signup?cont=/developers/embed
- group: start
  title: ''
  type: Login
  url: https://www.figma.com/login?cont=/developers/embed
- group: commercial
  title: ''
  type: Pricing
  url: https://www.figma.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.figma.com/blog/
- group: auth
  title: ''
  type: Security
  url: https://www.figma.com/security/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.figma.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.figma.com/legal/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.figma.com/legal/privacy/
- group: company
  title: ''
  type: Partners
  url: https://www.figma.com/partners/
- group: other
  title: ''
  type: Events
  url: https://www.figma.com/events/
- group: operate
  title: ''
  type: Support
  url: https://help.figma.com/hc/en-us/
- group: operate
  title: ''
  type: Contact
  url: https://www.figma.com/contact/
- group: operate
  title: Forum
  type: Support
  url: https://forum.figma.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/figma
- group: build
  title: REST API OpenAPI Specification
  type: GitHubRepository
  url: https://github.com/figma/rest-api-spec
- group: build
  title: Code Connect
  type: GitHubRepository
  url: https://github.com/figma/code-connect
- group: build
  title: Plugin API Typings
  type: GitHubRepository
  url: https://github.com/figma/plugin-typings
- group: build
  title: Community Resources
  type: GitHubRepository
  url: https://github.com/figma/community-resources
- group: build
  title: MCP Server Guide
  type: GitHubRepository
  url: https://github.com/figma/mcp-server-guide
- group: design
  title: ''
  type: SpectralRules
  url: rules/figma-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/figma-vocabulary.yaml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/figma/community-resources
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.figma.com/llms.txt
created: '2023-11-22'
description: Figma is a collaborative interface design tool with a comprehensive REST API for accessing and manipulating design files, projects, and teams.
examples:
- key_count: 2
  name: Figma Activity Logs Activity Log Action Example
  slug: figma-activity-logs-activity-log-action-example
- key_count: 4
  name: Figma Activity Logs Activity Log Actor Example
  slug: figma-activity-logs-activity-log-actor-example
- key_count: 5
  name: Figma Activity Logs Activity Log Context Example
  slug: figma-activity-logs-activity-log-context-example
- key_count: 0
  name: Figma Activity Logs Activity Log Entity Example
  slug: figma-activity-logs-activity-log-entity-example
- key_count: 2
  name: Figma Activity Logs Activity Log Example
  slug: figma-activity-logs-activity-log-example
- key_count: 3
  name: Figma Activity Logs Activity Log File Entity Example
  slug: figma-activity-logs-activity-log-file-entity-example
- key_count: 3
  name: Figma Activity Logs Activity Log Org Entity Example
  slug: figma-activity-logs-activity-log-org-entity-example
- key_count: 3
  name: Figma Activity Logs Activity Log Project Entity Example
  slug: figma-activity-logs-activity-log-project-entity-example
- key_count: 3
  name: Figma Activity Logs Activity Log Team Entity Example
  slug: figma-activity-logs-activity-log-team-entity-example
- key_count: 4
  name: Figma Activity Logs Activity Log User Entity Example
  slug: figma-activity-logs-activity-log-user-entity-example
- key_count: 3
  name: Figma Activity Logs Activity Logs Meta Example
  slug: figma-activity-logs-activity-logs-meta-example
- key_count: 3
  name: Figma Activity Logs Error Response Payload Example
  slug: figma-activity-logs-error-response-payload-example
- key_count: 2
  name: Figma Activity Logs Get Activity Logs Response Body Example
  slug: figma-activity-logs-get-activity-logs-response-body-example
- key_count: 3
  name: Figma Analytics Error Response Payload Example
  slug: figma-analytics-error-response-payload-example
- key_count: 4
  name: Figma Analytics Get Library Analytics Usages Response Body Example
  slug: figma-analytics-get-library-analytics-usages-response-body-example
- key_count: 5
  name: Figma Analytics Library Analytics Actions By Component Example
  slug: figma-analytics-library-analytics-actions-by-component-example
- key_count: 5
  name: Figma Analytics Library Analytics Actions By Team Example
  slug: figma-analytics-library-analytics-actions-by-team-example
- key_count: 6
  name: Figma Analytics Library Analytics Style Usages By Asset Example
  slug: figma-analytics-library-analytics-style-usages-by-asset-example
- key_count: 4
  name: Figma Analytics Library Analytics Style Usages By File Example
  slug: figma-analytics-library-analytics-style-usages-by-file-example
- key_count: 7
  name: Figma Analytics Library Analytics Usages By Component Example
  slug: figma-analytics-library-analytics-usages-by-component-example
- key_count: 4
  name: Figma Analytics Library Analytics Usages By File Example
  slug: figma-analytics-library-analytics-usages-by-file-example
- key_count: 8
  name: Figma Analytics Library Analytics Variable Usages By Asset Example
  slug: figma-analytics-library-analytics-variable-usages-by-asset-example
- key_count: 4
  name: Figma Analytics Library Analytics Variable Usages By File Example
  slug: figma-analytics-library-analytics-variable-usages-by-file-example
- key_count: 2
  name: Figma Component Sets Error Response Payload With Err Example
  slug: figma-component-sets-error-response-payload-with-err-example
- key_count: 3
  name: Figma Component Sets Error Response Payload With Error Example
  slug: figma-component-sets-error-response-payload-with-error-example
- key_count: 5
  name: Figma Component Sets Frame Info Example
  slug: figma-component-sets-frame-info-example
- key_count: 2
  name: Figma Component Sets Get Component Set Response Body Example
  slug: figma-component-sets-get-component-set-response-body-example
- key_count: 8
  name: Figma Component Sets Published Component Set Example
  slug: figma-component-sets-published-component-set-example
- key_count: 3
  name: Figma Component Sets User Example
  slug: figma-component-sets-user-example
- key_count: 4
  name: Figma Dev Resources Create Dev Resource Item Example
  slug: figma-dev-resources-create-dev-resource-item-example
- key_count: 1
  name: Figma Dev Resources Create Dev Resources Request Example
  slug: figma-dev-resources-create-dev-resources-request-example
- key_count: 3
  name: Figma Dev Resources Dev Resource Create Error Example
  slug: figma-dev-resources-dev-resource-create-error-example
- key_count: 5
  name: Figma Dev Resources Dev Resource Example
  slug: figma-dev-resources-dev-resource-example
- key_count: 2
  name: Figma Dev Resources Dev Resource Update Error Example
  slug: figma-dev-resources-dev-resource-update-error-example
- key_count: 3
  name: Figma Dev Resources Error Response Payload Example
  slug: figma-dev-resources-error-response-payload-example
- key_count: 2
  name: Figma Dev Resources Post Dev Resources Response Body Example
  slug: figma-dev-resources-post-dev-resources-response-body-example
- key_count: 2
  name: Figma Dev Resources Put Dev Resources Response Body Example
  slug: figma-dev-resources-put-dev-resources-response-body-example
- key_count: 3
  name: Figma Dev Resources Update Dev Resource Item Example
  slug: figma-dev-resources-update-dev-resource-item-example
- key_count: 1
  name: Figma Dev Resources Update Dev Resources Request Example
  slug: figma-dev-resources-update-dev-resources-request-example
- key_count: 2
  name: Figma Error Response Payload Example
  slug: figma-error-response-payload-example
- key_count: 4
  name: Figma Files Branch Example
  slug: figma-files-branch-example
- key_count: 4
  name: Figma Files Canvas Node Example
  slug: figma-files-canvas-node-example
- key_count: 4
  name: Figma Files Color Example
  slug: figma-files-color-example
- key_count: 8
  name: Figma Files Comment Example
  slug: figma-files-comment-example
- key_count: 6
  name: Figma Files Component Example
  slug: figma-files-component-example
- key_count: 5
  name: Figma Files Component Set Example
  slug: figma-files-component-set-example
- key_count: 2
  name: Figma Files Delete Dev Resource Response Body Example
  slug: figma-files-delete-dev-resource-response-body-example
- key_count: 5
  name: Figma Files Dev Resource Example
  slug: figma-files-dev-resource-example
- key_count: 4
  name: Figma Files Document Node Example
  slug: figma-files-document-node-example
- key_count: 1
  name: Figma Files Documentation Link Example
  slug: figma-files-documentation-link-example
- key_count: 3
  name: Figma Files Error Response Payload Example
  slug: figma-files-error-response-payload-example
- key_count: 5
  name: Figma Files Frame Info Example
  slug: figma-files-frame-info-example
- key_count: 1
  name: Figma Files Get Dev Resources Response Body Example
  slug: figma-files-get-dev-resources-response-body-example
- key_count: 12
  name: Figma Files Get File Response Body Example
  slug: figma-files-get-file-response-body-example
- key_count: 8
  name: Figma Files Published Component Example
  slug: figma-files-published-component-example
- key_count: 8
  name: Figma Files Published Component Set Example
  slug: figma-files-published-component-set-example
- key_count: 2
  name: Figma Files Reaction Example
  slug: figma-files-reaction-example
- key_count: 4
  name: Figma Files Style Example
  slug: figma-files-style-example
- key_count: 0
  name: Figma Files Style Type Example
  slug: figma-files-style-type-example
- key_count: 3
  name: Figma Files User Example
  slug: figma-files-user-example
- key_count: 4
  name: Figma Files Version Example
  slug: figma-files-version-example
- key_count: 0
  name: Figma Get Me Response Body Example
  slug: figma-get-me-response-body-example
- key_count: 0
  name: Figma Images Bad Request Error Example
  slug: figma-images-bad-request-error-example
- key_count: 2
  name: Figma Images Error Response Payload Example
  slug: figma-images-error-response-payload-example
- key_count: 0
  name: Figma Images Forbidden Error Example
  slug: figma-images-forbidden-error-example
- key_count: 2
  name: Figma Images Get Images Response Body Example
  slug: figma-images-get-images-response-body-example
- key_count: 0
  name: Figma Images Internal Server Error Example
  slug: figma-images-internal-server-error-example
- key_count: 0
  name: Figma Images Not Found Error Example
  slug: figma-images-not-found-error-example
- key_count: 0
  name: Figma Images Too Many Requests Error Example
  slug: figma-images-too-many-requests-error-example
- key_count: 2
  name: Figma Me Error Response Payload Example
  slug: figma-me-error-response-payload-example
- key_count: 0
  name: Figma Me Forbidden Error Example
  slug: figma-me-forbidden-error-example
- key_count: 0
  name: Figma Me Internal Server Error Example
  slug: figma-me-internal-server-error-example
- key_count: 0
  name: Figma Me Too Many Requests Error Example
  slug: figma-me-too-many-requests-error-example
- key_count: 3
  name: Figma Me User Example
  slug: figma-me-user-example
- key_count: 0
  name: Figma Me User With Email Example
  slug: figma-me-user-with-email-example
- key_count: 3
  name: Figma Payments Error Response Payload Example
  slug: figma-payments-error-response-payload-example
- key_count: 2
  name: Figma Payments Get Payments Response Body Example
  slug: figma-payments-get-payments-response-body-example
- key_count: 0
  name: Figma Payments Internal Server Error Example
  slug: figma-payments-internal-server-error-example
- key_count: 4
  name: Figma Payments Payment Information Example
  slug: figma-payments-payment-information-example
- key_count: 0
  name: Figma Payments Payment Status Example
  slug: figma-payments-payment-status-example
- key_count: 0
  name: Figma Payments Too Many Requests Error Example
  slug: figma-payments-too-many-requests-error-example
- key_count: 0
  name: Figma Payments Unauthorized Error Example
  slug: figma-payments-unauthorized-error-example
- key_count: 0
  name: Figma Projects Bad Request Error Example
  slug: figma-projects-bad-request-error-example
- key_count: 2
  name: Figma Projects Error Response Payload With Err Example
  slug: figma-projects-error-response-payload-with-err-example
- key_count: 3
  name: Figma Projects Error Response Payload With Message Example
  slug: figma-projects-error-response-payload-with-message-example
- key_count: 0
  name: Figma Projects Forbidden Error Example
  slug: figma-projects-forbidden-error-example
- key_count: 2
  name: Figma Projects Get Project Files Response Body Example
  slug: figma-projects-get-project-files-response-body-example
- key_count: 0
  name: Figma Projects Internal Server Error Example
  slug: figma-projects-internal-server-error-example
- key_count: 4
  name: Figma Projects Project File Example
  slug: figma-projects-project-file-example
- key_count: 0
  name: Figma Projects Too Many Requests Error Example
  slug: figma-projects-too-many-requests-error-example
- key_count: 4
  name: Figma Rest Branch Example
  slug: figma-rest-branch-example
- key_count: 4
  name: Figma Rest Canvas Node Example
  slug: figma-rest-canvas-node-example
- key_count: 4
  name: Figma Rest Client Meta Example
  slug: figma-rest-client-meta-example
- key_count: 4
  name: Figma Rest Color Example
  slug: figma-rest-color-example
- key_count: 8
  name: Figma Rest Comment Example
  slug: figma-rest-comment-example
- key_count: 6
  name: Figma Rest Component Example
  slug: figma-rest-component-example
- key_count: 5
  name: Figma Rest Component Set Example
  slug: figma-rest-component-set-example
- key_count: 4
  name: Figma Rest Document Node Example
  slug: figma-rest-document-node-example
- key_count: 1
  name: Figma Rest Documentation Link Example
  slug: figma-rest-documentation-link-example
- key_count: 3
  name: Figma Rest Error Response Example
  slug: figma-rest-error-response-example
- key_count: 5
  name: Figma Rest Frame Info Example
  slug: figma-rest-frame-info-example
- key_count: 1
  name: Figma Rest Get Comments Response Example
  slug: figma-rest-get-comments-response-example
- key_count: 2
  name: Figma Rest Get Component Response Example
  slug: figma-rest-get-component-response-example
- key_count: 3
  name: Figma Rest Get File Components Response Example
  slug: figma-rest-get-file-components-response-example
- key_count: 5
  name: Figma Rest Get File Nodes Response Example
  slug: figma-rest-get-file-nodes-response-example
- key_count: 12
  name: Figma Rest Get File Response Example
  slug: figma-rest-get-file-response-example
- key_count: 1
  name: Figma Rest Get File Versions Response Example
  slug: figma-rest-get-file-versions-response-example
- key_count: 3
  name: Figma Rest Get Image Fills Response Example
  slug: figma-rest-get-image-fills-response-example
- key_count: 2
  name: Figma Rest Get Images Response Example
  slug: figma-rest-get-images-response-example
- key_count: 2
  name: Figma Rest Get Project Files Response Example
  slug: figma-rest-get-project-files-response-example
- key_count: 2
  name: Figma Rest Get Reactions Response Example
  slug: figma-rest-get-reactions-response-example
- key_count: 3
  name: Figma Rest Get Team Component Sets Response Example
  slug: figma-rest-get-team-component-sets-response-example
- key_count: 3
  name: Figma Rest Get Team Components Response Example
  slug: figma-rest-get-team-components-response-example
- key_count: 2
  name: Figma Rest Get Team Projects Response Example
  slug: figma-rest-get-team-projects-response-example
- key_count: 3
  name: Figma Rest Get Team Styles Response Example
  slug: figma-rest-get-team-styles-response-example
- key_count: 2
  name: Figma Rest Pagination Example
  slug: figma-rest-pagination-example
- key_count: 2
  name: Figma Rest Post Comment Request Example
  slug: figma-rest-post-comment-request-example
- key_count: 2
  name: Figma Rest Project Example
  slug: figma-rest-project-example
- key_count: 5
  name: Figma Rest Project File Example
  slug: figma-rest-project-file-example
- key_count: 8
  name: Figma Rest Published Component Example
  slug: figma-rest-published-component-example
- key_count: 8
  name: Figma Rest Published Component Set Example
  slug: figma-rest-published-component-set-example
- key_count: 10
  name: Figma Rest Published Style Example
  slug: figma-rest-published-style-example
- key_count: 2
  name: Figma Rest Reaction Example
  slug: figma-rest-reaction-example
- key_count: 5
  name: Figma Rest Style Example
  slug: figma-rest-style-example
- key_count: 2
  name: Figma Rest Success Response Example
  slug: figma-rest-success-response-example
- key_count: 4
  name: Figma Rest User Example
  slug: figma-rest-user-example
- key_count: 4
  name: Figma Rest Version Example
  slug: figma-rest-version-example
- key_count: 0
  name: Figma Styles Bad Request Error Example
  slug: figma-styles-bad-request-error-example
- key_count: 2
  name: Figma Styles Error Response Payload With Err Example
  slug: figma-styles-error-response-payload-with-err-example
- key_count: 3
  name: Figma Styles Error Response Payload With Message Example
  slug: figma-styles-error-response-payload-with-message-example
- key_count: 0
  name: Figma Styles Forbidden Error Example
  slug: figma-styles-forbidden-error-example
- key_count: 2
  name: Figma Styles Get Style Response Body Example
  slug: figma-styles-get-style-response-body-example
- key_count: 0
  name: Figma Styles Internal Server Error Example
  slug: figma-styles-internal-server-error-example
- key_count: 0
  name: Figma Styles Not Found Error Example
  slug: figma-styles-not-found-error-example
- key_count: 9
  name: Figma Styles Published Style Example
  slug: figma-styles-published-style-example
- key_count: 0
  name: Figma Styles Style Type Example
  slug: figma-styles-style-type-example
- key_count: 0
  name: Figma Styles Too Many Requests Error Example
  slug: figma-styles-too-many-requests-error-example
- key_count: 3
  name: Figma Styles User Example
  slug: figma-styles-user-example
- key_count: 2
  name: Figma Teams Error Response Payload Example
  slug: figma-teams-error-response-payload-example
- key_count: 0
  name: Figma Teams Forbidden Error Example
  slug: figma-teams-forbidden-error-example
- key_count: 1
  name: Figma Teams Get Team Webhooks Response Body Example
  slug: figma-teams-get-team-webhooks-response-body-example
- key_count: 0
  name: Figma Teams Internal Server Error Example
  slug: figma-teams-internal-server-error-example
- key_count: 0
  name: Figma Teams Not Found Error Example
  slug: figma-teams-not-found-error-example
- key_count: 0
  name: Figma Teams Too Many Requests Error Example
  slug: figma-teams-too-many-requests-error-example
- key_count: 0
  name: Figma Teams Webhook V2 Event Example
  slug: figma-teams-webhook-v2-event-example
- key_count: 6
  name: Figma Teams Webhook V2 Example
  slug: figma-teams-webhook-v2-example
- key_count: 0
  name: Figma Teams Webhook V2 Status Example
  slug: figma-teams-webhook-v2-status-example
- key_count: 3
  name: Figma User Example
  slug: figma-user-example
features:
- Starter free with unlimited drafts and 150-500 AI credits/mo
- Professional at $16/full-seat/mo with team libraries and MCP Server
- Organization at $55/full-seat/mo with shared libraries and centralized admin
- Enterprise at $90/full-seat/mo with design system APIs and SCIM
- REST API for files, projects, components, comments
- Plugin API for in-editor extensions
- Widget API for FigJam interactive widgets
- Variables API for design token management
- Webhooks v2 for file and library updates
- OAuth 2.0 with granular scopes
- Personal access tokens for scripts/automation
- Dev Mode for handoff and code generation
- Dev Mode MCP Server for AI design integration
- FigJam whiteboarding included
- Variables and modes for design system theming (Enterprise)
- Branching and merging on Organization+
finops:
- name: Figma Finops
  service_category: Design
  slug: figma-finops
graphqls:
- description: Figma does not offer a native public GraphQL API. The Figma platform exposes all programmatic access through a comprehensive REST API available at `https://api.figma.com/v1/`. The REST API covers file
  name: Figma GraphQL
  slug: figma-graphql
image: https://www.figma.com/favicon.ico
json_schemas:
- name: ActivityLogAction
  property_count: 2
  slug: figma-activity-logs-activity-log-action
- name: ActivityLogActor
  property_count: 4
  slug: figma-activity-logs-activity-log-actor
- name: ActivityLogContext
  property_count: 5
  slug: figma-activity-logs-activity-log-context
- name: ActivityLogEntity
  property_count: 0
  slug: figma-activity-logs-activity-log-entity
- name: ActivityLogFileEntity
  property_count: 3
  slug: figma-activity-logs-activity-log-file-entity
- name: ActivityLogOrgEntity
  property_count: 3
  slug: figma-activity-logs-activity-log-org-entity
- name: ActivityLogProjectEntity
  property_count: 3
  slug: figma-activity-logs-activity-log-project-entity
- name: ActivityLog
  property_count: 2
  slug: figma-activity-logs-activity-log
- name: ActivityLogTeamEntity
  property_count: 3
  slug: figma-activity-logs-activity-log-team-entity
- name: ActivityLogUserEntity
  property_count: 4
  slug: figma-activity-logs-activity-log-user-entity
- name: ActivityLogsMeta
  property_count: 3
  slug: figma-activity-logs-activity-logs-meta
- name: ErrorResponsePayload
  property_count: 3
  slug: figma-activity-logs-error-response-payload
- name: GetActivityLogsResponseBody
  property_count: 2
  slug: figma-activity-logs-get-activity-logs-response-body
- name: ErrorResponsePayload
  property_count: 3
  slug: figma-analytics-error-response-payload
- name: GetLibraryAnalyticsUsagesResponseBody
  property_count: 4
  slug: figma-analytics-get-library-analytics-usages-response-body
- name: LibraryAnalyticsActionsByComponent
  property_count: 5
  slug: figma-analytics-library-analytics-actions-by-component
- name: LibraryAnalyticsActionsByTeam
  property_count: 5
  slug: figma-analytics-library-analytics-actions-by-team
- name: LibraryAnalyticsStyleUsagesByAsset
  property_count: 6
  slug: figma-analytics-library-analytics-style-usages-by-asset
- name: LibraryAnalyticsStyleUsagesByFile
  property_count: 4
  slug: figma-analytics-library-analytics-style-usages-by-file
- name: LibraryAnalyticsUsagesByComponent
  property_count: 7
  slug: figma-analytics-library-analytics-usages-by-component
- name: LibraryAnalyticsUsagesByFile
  property_count: 4
  slug: figma-analytics-library-analytics-usages-by-file
- name: LibraryAnalyticsVariableUsagesByAsset
  property_count: 8
  slug: figma-analytics-library-analytics-variable-usages-by-asset
- name: LibraryAnalyticsVariableUsagesByFile
  property_count: 4
  slug: figma-analytics-library-analytics-variable-usages-by-file
- name: Figma Published Component
  property_count: 12
  slug: figma-component
- name: ErrorResponsePayloadWithErr
  property_count: 2
  slug: figma-component-sets-error-response-payload-with-err
- name: ErrorResponsePayloadWithError
  property_count: 3
  slug: figma-component-sets-error-response-payload-with-error
- name: FrameInfo
  property_count: 5
  slug: figma-component-sets-frame-info
- name: GetComponentSetResponseBody
  property_count: 2
  slug: figma-component-sets-get-component-set-response-body
- name: PublishedComponentSet
  property_count: 8
  slug: figma-component-sets-published-component-set
- name: User
  property_count: 3
  slug: figma-component-sets-user
- name: CreateDevResourceItem
  property_count: 4
  slug: figma-dev-resources-create-dev-resource-item
- name: CreateDevResourcesRequest
  property_count: 1
  slug: figma-dev-resources-create-dev-resources-request
- name: DevResourceCreateError
  property_count: 3
  slug: figma-dev-resources-dev-resource-create-error
- name: DevResource
  property_count: 5
  slug: figma-dev-resources-dev-resource
- name: DevResourceUpdateError
  property_count: 2
  slug: figma-dev-resources-dev-resource-update-error
- name: ErrorResponsePayload
  property_count: 3
  slug: figma-dev-resources-error-response-payload
- name: PostDevResourcesResponseBody
  property_count: 2
  slug: figma-dev-resources-post-dev-resources-response-body
- name: PutDevResourcesResponseBody
  property_count: 2
  slug: figma-dev-resources-put-dev-resources-response-body
- name: UpdateDevResourceItem
  property_count: 3
  slug: figma-dev-resources-update-dev-resource-item
- name: UpdateDevResourcesRequest
  property_count: 1
  slug: figma-dev-resources-update-dev-resources-request
- name: ErrorResponsePayload
  property_count: 2
  slug: figma-error-response-payload
- name: Figma File
  property_count: 13
  slug: figma-file
- name: Branch
  property_count: 4
  slug: figma-files-branch
- name: CanvasNode
  property_count: 4
  slug: figma-files-canvas-node
- name: Color
  property_count: 4
  slug: figma-files-color
- name: Comment
  property_count: 8
  slug: figma-files-comment
- name: Component
  property_count: 6
  slug: figma-files-component
- name: ComponentSet
  property_count: 5
  slug: figma-files-component-set
- name: DeleteDevResourceResponseBody
  property_count: 2
  slug: figma-files-delete-dev-resource-response-body
- name: DevResource
  property_count: 5
  slug: figma-files-dev-resource
- name: DocumentNode
  property_count: 4
  slug: figma-files-document-node
- name: DocumentationLink
  property_count: 1
  slug: figma-files-documentation-link
- name: ErrorResponsePayload
  property_count: 3
  slug: figma-files-error-response-payload
- name: FrameInfo
  property_count: 5
  slug: figma-files-frame-info
- name: GetDevResourcesResponseBody
  property_count: 1
  slug: figma-files-get-dev-resources-response-body
- name: GetFileResponseBody
  property_count: 12
  slug: figma-files-get-file-response-body
- name: PublishedComponent
  property_count: 8
  slug: figma-files-published-component
- name: PublishedComponentSet
  property_count: 8
  slug: figma-files-published-component-set
- name: Reaction
  property_count: 2
  slug: figma-files-reaction
- name: Style
  property_count: 4
  slug: figma-files-style
- name: StyleType
  property_count: 0
  slug: figma-files-style-type
- name: User
  property_count: 3
  slug: figma-files-user
- name: Version
  property_count: 4
  slug: figma-files-version
- name: GetMeResponseBody
  property_count: 0
  slug: figma-get-me-response-body
- name: BadRequestError
  property_count: 0
  slug: figma-images-bad-request-error
- name: ErrorResponsePayload
  property_count: 2
  slug: figma-images-error-response-payload
- name: ForbiddenError
  property_count: 0
  slug: figma-images-forbidden-error
- name: GetImagesResponseBody
  property_count: 2
  slug: figma-images-get-images-response-body
- name: InternalServerError
  property_count: 0
  slug: figma-images-internal-server-error
- name: NotFoundError
  property_count: 0
  slug: figma-images-not-found-error
- name: TooManyRequestsError
  property_count: 0
  slug: figma-images-too-many-requests-error
- name: ErrorResponsePayload
  property_count: 2
  slug: figma-me-error-response-payload
- name: ForbiddenError
  property_count: 0
  slug: figma-me-forbidden-error
- name: InternalServerError
  property_count: 0
  slug: figma-me-internal-server-error
- name: TooManyRequestsError
  property_count: 0
  slug: figma-me-too-many-requests-error
- name: User
  property_count: 3
  slug: figma-me-user
- name: UserWithEmail
  property_count: 0
  slug: figma-me-user-with-email
- name: ErrorResponsePayload
  property_count: 3
  slug: figma-payments-error-response-payload
- name: GetPaymentsResponseBody
  property_count: 2
  slug: figma-payments-get-payments-response-body
- name: InternalServerError
  property_count: 0
  slug: figma-payments-internal-server-error
- name: PaymentInformation
  property_count: 4
  slug: figma-payments-payment-information
- name: PaymentStatus
  property_count: 0
  slug: figma-payments-payment-status
- name: TooManyRequestsError
  property_count: 0
  slug: figma-payments-too-many-requests-error
- name: UnauthorizedError
  property_count: 0
  slug: figma-payments-unauthorized-error
- name: BadRequestError
  property_count: 0
  slug: figma-projects-bad-request-error
- name: ErrorResponsePayloadWithErr
  property_count: 2
  slug: figma-projects-error-response-payload-with-err
- name: ErrorResponsePayloadWithMessage
  property_count: 3
  slug: figma-projects-error-response-payload-with-message
- name: ForbiddenError
  property_count: 0
  slug: figma-projects-forbidden-error
- name: GetProjectFilesResponseBody
  property_count: 2
  slug: figma-projects-get-project-files-response-body
- name: InternalServerError
  property_count: 0
  slug: figma-projects-internal-server-error
- name: ProjectFile
  property_count: 4
  slug: figma-projects-project-file
- name: TooManyRequestsError
  property_count: 0
  slug: figma-projects-too-many-requests-error
- name: Branch
  property_count: 4
  slug: figma-rest-branch
- name: CanvasNode
  property_count: 4
  slug: figma-rest-canvas-node
- name: ClientMeta
  property_count: 4
  slug: figma-rest-client-meta
- name: Color
  property_count: 4
  slug: figma-rest-color
- name: Comment
  property_count: 8
  slug: figma-rest-comment
- name: Component
  property_count: 6
  slug: figma-rest-component
- name: ComponentSet
  property_count: 5
  slug: figma-rest-component-set
- name: DocumentNode
  property_count: 4
  slug: figma-rest-document-node
- name: DocumentationLink
  property_count: 1
  slug: figma-rest-documentation-link
- name: ErrorResponse
  property_count: 3
  slug: figma-rest-error-response
- name: FrameInfo
  property_count: 5
  slug: figma-rest-frame-info
- name: GetCommentsResponse
  property_count: 1
  slug: figma-rest-get-comments-response
- name: GetComponentResponse
  property_count: 2
  slug: figma-rest-get-component-response
- name: GetFileComponentsResponse
  property_count: 3
  slug: figma-rest-get-file-components-response
- name: GetFileNodesResponse
  property_count: 5
  slug: figma-rest-get-file-nodes-response
- name: GetFileResponse
  property_count: 12
  slug: figma-rest-get-file-response
- name: GetFileVersionsResponse
  property_count: 1
  slug: figma-rest-get-file-versions-response
- name: GetImageFillsResponse
  property_count: 3
  slug: figma-rest-get-image-fills-response
- name: GetImagesResponse
  property_count: 2
  slug: figma-rest-get-images-response
- name: GetProjectFilesResponse
  property_count: 2
  slug: figma-rest-get-project-files-response
- name: GetReactionsResponse
  property_count: 2
  slug: figma-rest-get-reactions-response
- name: GetTeamComponentSetsResponse
  property_count: 3
  slug: figma-rest-get-team-component-sets-response
- name: GetTeamComponentsResponse
  property_count: 3
  slug: figma-rest-get-team-components-response
- name: GetTeamProjectsResponse
  property_count: 2
  slug: figma-rest-get-team-projects-response
- name: GetTeamStylesResponse
  property_count: 3
  slug: figma-rest-get-team-styles-response
- name: Pagination
  property_count: 2
  slug: figma-rest-pagination
- name: PostCommentRequest
  property_count: 2
  slug: figma-rest-post-comment-request
- name: ProjectFile
  property_count: 5
  slug: figma-rest-project-file
- name: Project
  property_count: 2
  slug: figma-rest-project
- name: PublishedComponent
  property_count: 8
  slug: figma-rest-published-component
- name: PublishedComponentSet
  property_count: 8
  slug: figma-rest-published-component-set
- name: PublishedStyle
  property_count: 10
  slug: figma-rest-published-style
- name: Reaction
  property_count: 2
  slug: figma-rest-reaction
- name: Style
  property_count: 5
  slug: figma-rest-style
- name: SuccessResponse
  property_count: 2
  slug: figma-rest-success-response
- name: User
  property_count: 4
  slug: figma-rest-user
- name: Version
  property_count: 4
  slug: figma-rest-version
- name: BadRequestError
  property_count: 0
  slug: figma-styles-bad-request-error
- name: ErrorResponsePayloadWithErr
  property_count: 2
  slug: figma-styles-error-response-payload-with-err
- name: ErrorResponsePayloadWithMessage
  property_count: 3
  slug: figma-styles-error-response-payload-with-message
- name: ForbiddenError
  property_count: 0
  slug: figma-styles-forbidden-error
- name: GetStyleResponseBody
  property_count: 2
  slug: figma-styles-get-style-response-body
- name: InternalServerError
  property_count: 0
  slug: figma-styles-internal-server-error
- name: NotFoundError
  property_count: 0
  slug: figma-styles-not-found-error
- name: PublishedStyle
  property_count: 9
  slug: figma-styles-published-style
- name: StyleType
  property_count: 0
  slug: figma-styles-style-type
- name: TooManyRequestsError
  property_count: 0
  slug: figma-styles-too-many-requests-error
- name: User
  property_count: 3
  slug: figma-styles-user
- name: ErrorResponsePayload
  property_count: 2
  slug: figma-teams-error-response-payload
- name: ForbiddenError
  property_count: 0
  slug: figma-teams-forbidden-error
- name: GetTeamWebhooksResponseBody
  property_count: 1
  slug: figma-teams-get-team-webhooks-response-body
- name: InternalServerError
  property_count: 0
  slug: figma-teams-internal-server-error
- name: NotFoundError
  property_count: 0
  slug: figma-teams-not-found-error
- name: TooManyRequestsError
  property_count: 0
  slug: figma-teams-too-many-requests-error
- name: WebhookV2Event
  property_count: 0
  slug: figma-teams-webhook-v2-event
- name: WebhookV2
  property_count: 6
  slug: figma-teams-webhook-v2
- name: WebhookV2Status
  property_count: 0
  slug: figma-teams-webhook-v2-status
- name: User
  property_count: 3
  slug: figma-user
json_structures:
- name: Figma Activity Logs Activity Log Action Structure
  property_count: 2
  slug: figma-activity-logs-activity-log-action-structure
- name: Figma Activity Logs Activity Log Actor Structure
  property_count: 4
  slug: figma-activity-logs-activity-log-actor-structure
- name: Figma Activity Logs Activity Log Context Structure
  property_count: 5
  slug: figma-activity-logs-activity-log-context-structure
- name: Figma Activity Logs Activity Log Entity Structure
  property_count: 0
  slug: figma-activity-logs-activity-log-entity-structure
- name: Figma Activity Logs Activity Log File Entity Structure
  property_count: 3
  slug: figma-activity-logs-activity-log-file-entity-structure
- name: Figma Activity Logs Activity Log Org Entity Structure
  property_count: 3
  slug: figma-activity-logs-activity-log-org-entity-structure
- name: Figma Activity Logs Activity Log Project Entity Structure
  property_count: 3
  slug: figma-activity-logs-activity-log-project-entity-structure
- name: Figma Activity Logs Activity Log Structure
  property_count: 2
  slug: figma-activity-logs-activity-log-structure
- name: Figma Activity Logs Activity Log Team Entity Structure
  property_count: 3
  slug: figma-activity-logs-activity-log-team-entity-structure
- name: Figma Activity Logs Activity Log User Entity Structure
  property_count: 4
  slug: figma-activity-logs-activity-log-user-entity-structure
- name: Figma Activity Logs Activity Logs Meta Structure
  property_count: 3
  slug: figma-activity-logs-activity-logs-meta-structure
- name: Figma Activity Logs Error Response Payload Structure
  property_count: 3
  slug: figma-activity-logs-error-response-payload-structure
- name: Figma Activity Logs Get Activity Logs Response Body Structure
  property_count: 2
  slug: figma-activity-logs-get-activity-logs-response-body-structure
- name: Figma Analytics Error Response Payload Structure
  property_count: 3
  slug: figma-analytics-error-response-payload-structure
- name: Figma Analytics Get Library Analytics Usages Response Body Structure
  property_count: 4
  slug: figma-analytics-get-library-analytics-usages-response-body-structure
- name: Figma Analytics Library Analytics Actions By Component Structure
  property_count: 5
  slug: figma-analytics-library-analytics-actions-by-component-structure
- name: Figma Analytics Library Analytics Actions By Team Structure
  property_count: 5
  slug: figma-analytics-library-analytics-actions-by-team-structure
- name: Figma Analytics Library Analytics Style Usages By Asset Structure
  property_count: 6
  slug: figma-analytics-library-analytics-style-usages-by-asset-structure
- name: Figma Analytics Library Analytics Style Usages By File Structure
  property_count: 4
  slug: figma-analytics-library-analytics-style-usages-by-file-structure
- name: Figma Analytics Library Analytics Usages By Component Structure
  property_count: 7
  slug: figma-analytics-library-analytics-usages-by-component-structure
- name: Figma Analytics Library Analytics Usages By File Structure
  property_count: 4
  slug: figma-analytics-library-analytics-usages-by-file-structure
- name: Figma Analytics Library Analytics Variable Usages By Asset Structure
  property_count: 8
  slug: figma-analytics-library-analytics-variable-usages-by-asset-structure
- name: Figma Analytics Library Analytics Variable Usages By File Structure
  property_count: 4
  slug: figma-analytics-library-analytics-variable-usages-by-file-structure
- name: Figma Component Sets Error Response Payload With Err Structure
  property_count: 2
  slug: figma-component-sets-error-response-payload-with-err-structure
- name: Figma Component Sets Error Response Payload With Error Structure
  property_count: 3
  slug: figma-component-sets-error-response-payload-with-error-structure
- name: Figma Component Sets Frame Info Structure
  property_count: 5
  slug: figma-component-sets-frame-info-structure
- name: Figma Component Sets Get Component Set Response Body Structure
  property_count: 2
  slug: figma-component-sets-get-component-set-response-body-structure
- name: Figma Component Sets Published Component Set Structure
  property_count: 8
  slug: figma-component-sets-published-component-set-structure
- name: Figma Component Sets User Structure
  property_count: 3
  slug: figma-component-sets-user-structure
- name: Figma Dev Resources Create Dev Resource Item Structure
  property_count: 4
  slug: figma-dev-resources-create-dev-resource-item-structure
- name: Figma Dev Resources Create Dev Resources Request Structure
  property_count: 1
  slug: figma-dev-resources-create-dev-resources-request-structure
- name: Figma Dev Resources Dev Resource Create Error Structure
  property_count: 3
  slug: figma-dev-resources-dev-resource-create-error-structure
- name: Figma Dev Resources Dev Resource Structure
  property_count: 5
  slug: figma-dev-resources-dev-resource-structure
- name: Figma Dev Resources Dev Resource Update Error Structure
  property_count: 2
  slug: figma-dev-resources-dev-resource-update-error-structure
- name: Figma Dev Resources Error Response Payload Structure
  property_count: 3
  slug: figma-dev-resources-error-response-payload-structure
- name: Figma Dev Resources Post Dev Resources Response Body Structure
  property_count: 2
  slug: figma-dev-resources-post-dev-resources-response-body-structure
- name: Figma Dev Resources Put Dev Resources Response Body Structure
  property_count: 2
  slug: figma-dev-resources-put-dev-resources-response-body-structure
- name: Figma Dev Resources Update Dev Resource Item Structure
  property_count: 3
  slug: figma-dev-resources-update-dev-resource-item-structure
- name: Figma Dev Resources Update Dev Resources Request Structure
  property_count: 1
  slug: figma-dev-resources-update-dev-resources-request-structure
- name: Figma Error Response Payload Structure
  property_count: 2
  slug: figma-error-response-payload-structure
- name: Figma Files Branch Structure
  property_count: 4
  slug: figma-files-branch-structure
- name: Figma Files Canvas Node Structure
  property_count: 4
  slug: figma-files-canvas-node-structure
- name: Figma Files Color Structure
  property_count: 4
  slug: figma-files-color-structure
- name: Figma Files Comment Structure
  property_count: 8
  slug: figma-files-comment-structure
- name: Figma Files Component Set Structure
  property_count: 5
  slug: figma-files-component-set-structure
- name: Figma Files Component Structure
  property_count: 6
  slug: figma-files-component-structure
- name: Figma Files Delete Dev Resource Response Body Structure
  property_count: 2
  slug: figma-files-delete-dev-resource-response-body-structure
- name: Figma Files Dev Resource Structure
  property_count: 5
  slug: figma-files-dev-resource-structure
- name: Figma Files Document Node Structure
  property_count: 4
  slug: figma-files-document-node-structure
- name: Figma Files Documentation Link Structure
  property_count: 1
  slug: figma-files-documentation-link-structure
- name: Figma Files Error Response Payload Structure
  property_count: 3
  slug: figma-files-error-response-payload-structure
- name: Figma Files Frame Info Structure
  property_count: 5
  slug: figma-files-frame-info-structure
- name: Figma Files Get Dev Resources Response Body Structure
  property_count: 1
  slug: figma-files-get-dev-resources-response-body-structure
- name: Figma Files Get File Response Body Structure
  property_count: 12
  slug: figma-files-get-file-response-body-structure
- name: Figma Files Published Component Set Structure
  property_count: 8
  slug: figma-files-published-component-set-structure
- name: Figma Files Published Component Structure
  property_count: 8
  slug: figma-files-published-component-structure
- name: Figma Files Reaction Structure
  property_count: 2
  slug: figma-files-reaction-structure
- name: Figma Files Style Structure
  property_count: 4
  slug: figma-files-style-structure
- name: Figma Files Style Type Structure
  property_count: 0
  slug: figma-files-style-type-structure
- name: Figma Files User Structure
  property_count: 3
  slug: figma-files-user-structure
- name: Figma Files Version Structure
  property_count: 4
  slug: figma-files-version-structure
- name: Figma Get Me Response Body Structure
  property_count: 0
  slug: figma-get-me-response-body-structure
- name: Figma Images Bad Request Error Structure
  property_count: 0
  slug: figma-images-bad-request-error-structure
- name: Figma Images Error Response Payload Structure
  property_count: 2
  slug: figma-images-error-response-payload-structure
- name: Figma Images Forbidden Error Structure
  property_count: 0
  slug: figma-images-forbidden-error-structure
- name: Figma Images Get Images Response Body Structure
  property_count: 2
  slug: figma-images-get-images-response-body-structure
- name: Figma Images Internal Server Error Structure
  property_count: 0
  slug: figma-images-internal-server-error-structure
- name: Figma Images Not Found Error Structure
  property_count: 0
  slug: figma-images-not-found-error-structure
- name: Figma Images Too Many Requests Error Structure
  property_count: 0
  slug: figma-images-too-many-requests-error-structure
- name: Figma Me Error Response Payload Structure
  property_count: 2
  slug: figma-me-error-response-payload-structure
- name: Figma Me Forbidden Error Structure
  property_count: 0
  slug: figma-me-forbidden-error-structure
- name: Figma Me Internal Server Error Structure
  property_count: 0
  slug: figma-me-internal-server-error-structure
- name: Figma Me Too Many Requests Error Structure
  property_count: 0
  slug: figma-me-too-many-requests-error-structure
- name: Figma Me User Structure
  property_count: 3
  slug: figma-me-user-structure
- name: Figma Me User With Email Structure
  property_count: 0
  slug: figma-me-user-with-email-structure
- name: Figma Payments Error Response Payload Structure
  property_count: 3
  slug: figma-payments-error-response-payload-structure
- name: Figma Payments Get Payments Response Body Structure
  property_count: 2
  slug: figma-payments-get-payments-response-body-structure
- name: Figma Payments Internal Server Error Structure
  property_count: 0
  slug: figma-payments-internal-server-error-structure
- name: Figma Payments Payment Information Structure
  property_count: 4
  slug: figma-payments-payment-information-structure
- name: Figma Payments Payment Status Structure
  property_count: 0
  slug: figma-payments-payment-status-structure
- name: Figma Payments Too Many Requests Error Structure
  property_count: 0
  slug: figma-payments-too-many-requests-error-structure
- name: Figma Payments Unauthorized Error Structure
  property_count: 0
  slug: figma-payments-unauthorized-error-structure
- name: Figma Projects Bad Request Error Structure
  property_count: 0
  slug: figma-projects-bad-request-error-structure
- name: Figma Projects Error Response Payload With Err Structure
  property_count: 2
  slug: figma-projects-error-response-payload-with-err-structure
- name: Figma Projects Error Response Payload With Message Structure
  property_count: 3
  slug: figma-projects-error-response-payload-with-message-structure
- name: Figma Projects Forbidden Error Structure
  property_count: 0
  slug: figma-projects-forbidden-error-structure
- name: Figma Projects Get Project Files Response Body Structure
  property_count: 2
  slug: figma-projects-get-project-files-response-body-structure
- name: Figma Projects Internal Server Error Structure
  property_count: 0
  slug: figma-projects-internal-server-error-structure
- name: Figma Projects Project File Structure
  property_count: 4
  slug: figma-projects-project-file-structure
- name: Figma Projects Too Many Requests Error Structure
  property_count: 0
  slug: figma-projects-too-many-requests-error-structure
- name: Figma Rest Branch Structure
  property_count: 4
  slug: figma-rest-branch-structure
- name: Figma Rest Canvas Node Structure
  property_count: 4
  slug: figma-rest-canvas-node-structure
- name: Figma Rest Client Meta Structure
  property_count: 4
  slug: figma-rest-client-meta-structure
- name: Figma Rest Color Structure
  property_count: 4
  slug: figma-rest-color-structure
- name: Figma Rest Comment Structure
  property_count: 8
  slug: figma-rest-comment-structure
- name: Figma Rest Component Set Structure
  property_count: 5
  slug: figma-rest-component-set-structure
- name: Figma Rest Component Structure
  property_count: 6
  slug: figma-rest-component-structure
- name: Figma Rest Document Node Structure
  property_count: 4
  slug: figma-rest-document-node-structure
- name: Figma Rest Documentation Link Structure
  property_count: 1
  slug: figma-rest-documentation-link-structure
- name: Figma Rest Error Response Structure
  property_count: 3
  slug: figma-rest-error-response-structure
- name: Figma Rest Frame Info Structure
  property_count: 5
  slug: figma-rest-frame-info-structure
- name: Figma Rest Get Comments Response Structure
  property_count: 1
  slug: figma-rest-get-comments-response-structure
- name: Figma Rest Get Component Response Structure
  property_count: 2
  slug: figma-rest-get-component-response-structure
- name: Figma Rest Get File Components Response Structure
  property_count: 3
  slug: figma-rest-get-file-components-response-structure
- name: Figma Rest Get File Nodes Response Structure
  property_count: 5
  slug: figma-rest-get-file-nodes-response-structure
- name: Figma Rest Get File Response Structure
  property_count: 12
  slug: figma-rest-get-file-response-structure
- name: Figma Rest Get File Versions Response Structure
  property_count: 1
  slug: figma-rest-get-file-versions-response-structure
- name: Figma Rest Get Image Fills Response Structure
  property_count: 3
  slug: figma-rest-get-image-fills-response-structure
- name: Figma Rest Get Images Response Structure
  property_count: 2
  slug: figma-rest-get-images-response-structure
- name: Figma Rest Get Project Files Response Structure
  property_count: 2
  slug: figma-rest-get-project-files-response-structure
- name: Figma Rest Get Reactions Response Structure
  property_count: 2
  slug: figma-rest-get-reactions-response-structure
- name: Figma Rest Get Team Component Sets Response Structure
  property_count: 3
  slug: figma-rest-get-team-component-sets-response-structure
- name: Figma Rest Get Team Components Response Structure
  property_count: 3
  slug: figma-rest-get-team-components-response-structure
- name: Figma Rest Get Team Projects Response Structure
  property_count: 2
  slug: figma-rest-get-team-projects-response-structure
- name: Figma Rest Get Team Styles Response Structure
  property_count: 3
  slug: figma-rest-get-team-styles-response-structure
- name: Figma Rest Pagination Structure
  property_count: 2
  slug: figma-rest-pagination-structure
- name: Figma Rest Post Comment Request Structure
  property_count: 2
  slug: figma-rest-post-comment-request-structure
- name: Figma Rest Project File Structure
  property_count: 5
  slug: figma-rest-project-file-structure
- name: Figma Rest Project Structure
  property_count: 2
  slug: figma-rest-project-structure
- name: Figma Rest Published Component Set Structure
  property_count: 8
  slug: figma-rest-published-component-set-structure
- name: Figma Rest Published Component Structure
  property_count: 8
  slug: figma-rest-published-component-structure
- name: Figma Rest Published Style Structure
  property_count: 10
  slug: figma-rest-published-style-structure
- name: Figma Rest Reaction Structure
  property_count: 2
  slug: figma-rest-reaction-structure
- name: Figma Rest Style Structure
  property_count: 5
  slug: figma-rest-style-structure
- name: Figma Rest Success Response Structure
  property_count: 2
  slug: figma-rest-success-response-structure
- name: Figma Rest User Structure
  property_count: 4
  slug: figma-rest-user-structure
- name: Figma Rest Version Structure
  property_count: 4
  slug: figma-rest-version-structure
- name: Figma Styles Bad Request Error Structure
  property_count: 0
  slug: figma-styles-bad-request-error-structure
- name: Figma Styles Error Response Payload With Err Structure
  property_count: 2
  slug: figma-styles-error-response-payload-with-err-structure
- name: Figma Styles Error Response Payload With Message Structure
  property_count: 3
  slug: figma-styles-error-response-payload-with-message-structure
- name: Figma Styles Forbidden Error Structure
  property_count: 0
  slug: figma-styles-forbidden-error-structure
- name: Figma Styles Get Style Response Body Structure
  property_count: 2
  slug: figma-styles-get-style-response-body-structure
- name: Figma Styles Internal Server Error Structure
  property_count: 0
  slug: figma-styles-internal-server-error-structure
- name: Figma Styles Not Found Error Structure
  property_count: 0
  slug: figma-styles-not-found-error-structure
- name: Figma Styles Published Style Structure
  property_count: 9
  slug: figma-styles-published-style-structure
- name: Figma Styles Style Type Structure
  property_count: 0
  slug: figma-styles-style-type-structure
- name: Figma Styles Too Many Requests Error Structure
  property_count: 0
  slug: figma-styles-too-many-requests-error-structure
- name: Figma Styles User Structure
  property_count: 3
  slug: figma-styles-user-structure
- name: Figma Teams Error Response Payload Structure
  property_count: 2
  slug: figma-teams-error-response-payload-structure
- name: Figma Teams Forbidden Error Structure
  property_count: 0
  slug: figma-teams-forbidden-error-structure
- name: Figma Teams Get Team Webhooks Response Body Structure
  property_count: 1
  slug: figma-teams-get-team-webhooks-response-body-structure
- name: Figma Teams Internal Server Error Structure
  property_count: 0
  slug: figma-teams-internal-server-error-structure
- name: Figma Teams Not Found Error Structure
  property_count: 0
  slug: figma-teams-not-found-error-structure
- name: Figma Teams Too Many Requests Error Structure
  property_count: 0
  slug: figma-teams-too-many-requests-error-structure
- name: Figma Teams Webhook V2 Event Structure
  property_count: 0
  slug: figma-teams-webhook-v2-event-structure
- name: Figma Teams Webhook V2 Status Structure
  property_count: 0
  slug: figma-teams-webhook-v2-status-structure
- name: Figma Teams Webhook V2 Structure
  property_count: 6
  slug: figma-teams-webhook-v2-structure
- name: Figma User Structure
  property_count: 3
  slug: figma-user-structure
jsonld:
- class_count: 0
  name: Figma Activity Logs Context
  property_count: 0
  slug: figma-activity-logs-context
- class_count: 0
  name: Figma Analytics Context
  property_count: 0
  slug: figma-analytics-context
- class_count: 0
  name: Figma Component Sets Context
  property_count: 0
  slug: figma-component-sets-context
- class_count: 0
  name: Figma Context
  property_count: 0
  slug: figma-context
- class_count: 0
  name: Figma Dev Resources Context
  property_count: 0
  slug: figma-dev-resources-context
- class_count: 0
  name: Figma Files Context
  property_count: 0
  slug: figma-files-context
- class_count: 0
  name: Figma Images Context
  property_count: 0
  slug: figma-images-context
- class_count: 0
  name: Figma Me Context
  property_count: 0
  slug: figma-me-context
- class_count: 0
  name: Figma Payments Context
  property_count: 0
  slug: figma-payments-context
- class_count: 0
  name: Figma Projects Context
  property_count: 0
  slug: figma-projects-context
- class_count: 0
  name: Figma Rest Context
  property_count: 0
  slug: figma-rest-context
- class_count: 0
  name: Figma Styles Context
  property_count: 0
  slug: figma-styles-context
- class_count: 0
  name: Figma Teams Context
  property_count: 0
  slug: figma-teams-context
layout: provider
mcp_servers:
- description: ''
  name: figma-mcp.yml
  slug: figma-mcpyml
modified: '2026-06-20'
name: Figma
nav: Providers
network: true
overview: 'Figma publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Files API, Images API, Teams API, and 13 more. Tagged areas include Collaboration, Design, Graphics, Interfaces, and Prototypes.


  The Figma catalog on APIs.io includes 1 event-driven AsyncAPI specification, 13 JSON-LD contexts, and 3 Spectral governance rulesets.


  Figma''s developer surface includes authentication, changelog, CLI, developer portal, getting-started guide, signup flow, pricing, and 68 more developer resources.'
plans:
- name: Figma Plans Pricing
  plan_count: 4
  slug: figma-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 3
  name: Figma Rate Limits
  slug: figma-rate-limits
rules:
- name: Figma API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: figma-asyncapi-spectral-rules
- name: Figma API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: figma-jsonschema-spectral-rules
- name: Figma API Rules
  rule_count: 19
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 10
  slug: figma-spectral-rules
scopes:
- name: Figma Scopes
  scope_count: 9
  slug: figma-scopes
  summary_line: 9 scopes · authorizationCode
score:
  band: exemplar
  composite: 76.5
  delta: -1.2
  facets:
    commercial_clarity: 92.1
    contract_quality: 84.3
    developer_ergonomics: 56.5
    discoverability: 77.8
    governance: 63.5
    operational_transparency: 78.9
  previous_composite: 77.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/figma/refs/heads/main/screenshots/figma-2026-06-20T181157.png
security:
- kind: authentication
  name: Figma Authentication
  slug: figma-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Figma Domain Security
  slug: figma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Figma Vulnerability Disclosure
  slug: figma-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Figma Trust Center
  slug: figma-trust-center
  summary_line: SOC 2 Type II, SOC 3, ISO 27001, ISO 27017, ISO 27018, ISO 27701, ISO 42001, FedRAMP Moderate, EU Cloud Code of Conduct (Level 2), GDPR
slug: figma
tags:
- Collaboration
- Design
- Graphics
- Interfaces
- Prototypes
- Prototyping
- UI/UX
use_cases:
- description: Build, publish, and track adoption of shared component libraries across product teams.
  name: Design System Management
- description: Programmatically export design assets for build pipelines and content delivery workflows.
  name: Automated Asset Export
- description: Attach code references to design nodes using dev resources for seamless developer handoff.
  name: Design-to-Code Handoff
- description: Extend Figma with custom plugins and widgets using the Plugin API and Widget API.
  name: Plugin and Widget Development
- description: Monitor organization activity logs for security compliance and access auditing.
  name: Compliance and Audit
- description: Programmatically back up file data and version history for disaster recovery.
  name: Design File Backup
website: https://www.figma.com/developers
---
