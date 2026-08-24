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
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 56.0
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Jira Agentic Access
  operation_count: 16
  slug: jira-agentic-access
  summary_line: 16 operations · 6 acting
api_count: 12
apis:
- description: Version 2 of the Jira Cloud platform REST API, offering the same operations as v3 but without Atlassian Document Format support.
  name: Jira Cloud Platform REST API v2
  slug: jira-cloud-platform-rest-api-v2
- description: Operations APIs for Jira Service Management covering schedules, on-call rotations, alerts, escalations, and incident management.
  name: Jira Service Management Operations REST API
  slug: jira-service-management-operations-rest-api
- description: REST API for Jira Align enterprise agile planning platform, providing access to portfolios, epics, features, and program management data.
  name: Jira Align REST API
  slug: jira-align-rest-api
- description: REST API for Atlassian Customer Service Management providing access to customers, organizations, products, and entitlements data.
  name: Jira Customer Service Management REST API
  slug: jira-customer-service-management-rest-api
- description: Manage comments on issues.
  name: Jira Issue Comments API
  slug: jira-issue-comments-api
- description: Retrieve issue priority levels.
  name: Jira Issue Priorities API
  slug: jira-issue-priorities-api
- description: Search for issues using JQL (Jira Query Language).
  name: Jira Issue Search API
  slug: jira-issue-search-api
- description: Retrieve issue statuses.
  name: Jira Issue Statuses API
  slug: jira-issue-statuses-api
- description: Retrieve and perform workflow transitions on issues.
  name: Jira Issue Transitions API
  slug: jira-issue-transitions-api
- description: Retrieve and manage issue types for projects.
  name: Jira Issue Types API
  slug: jira-issue-types-api
- description: Create, read, update, delete, and transition Jira issues.
  name: Jira Issues API
  slug: jira-issues-api
- description: Manage Jira projects including metadata, roles, and components.
  name: Jira Projects API
  slug: jira-projects-api
arazzos:
- description: Read an issue, page through its comment thread oldest-first, then add a reply.
  name: Jira Read an Issue Comment Thread and Reply
  slug: jira-comment-thread-reply-workflow
- description: Resolve project metadata, create an issue, then read back the stored issue.
  name: Jira Create an Issue and Read It Back
  slug: jira-create-issue-read-back-workflow
- description: Search for an existing issue by JQL and either comment on the duplicate or create a new issue.
  name: Jira Deduplicate Issue Intake
  slug: jira-deduplicate-issue-intake-workflow
- description: Read an issue, apply a field edit and label operations, then re-read to verify.
  name: Jira Edit an Issue and Verify the Change
  slug: jira-edit-issue-verify-workflow
- description: Cache the projects, issue types, and priorities an issue-creation surface needs.
  name: Jira Bootstrap Issue Creation Metadata
  slug: jira-issue-metadata-bootstrap-workflow
- description: Run a JQL search via GET, then drill into the first matching issue and its comments.
  name: Jira Run a JQL Report and Drill Into a Result
  slug: jira-jql-issue-report-workflow
- description: Search projects by name, read the matched project, and map its per-issue-type statuses.
  name: Jira Discover a Project and Its Workflow Statuses
  slug: jira-project-discovery-workflow
- description: Read an issue and its sub-tasks first, then delete it with an explicit sub-task decision.
  name: Jira Safely Delete an Issue
  slug: jira-safe-issue-delete-workflow
- description: Find stale issues with JQL, annotate the first match, discover its transitions, and close it.
  name: Jira Sweep a Stale Issue Through a Transition
  slug: jira-stale-issue-sweep-workflow
- description: Read an issue, discover its legal transitions, apply one, and verify the new status.
  name: Jira Transition an Issue to a New Status
  slug: jira-transition-issue-workflow
artifact_total: 217
asyncapis:
- description: Jira Cloud webhooks deliver HTTP POST payloads to a configured URL whenever specified events occur in your Jira instance. Webhooks can be registered via the Jira REST API or through the Jira administr
  name: Jira Cloud Webhooks
  slug: jira-webhooks-asyncapi
collections:
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments API
  slug: postman-jira-issue-comments-api
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments Issue Priorities API
  slug: postman-jira-issue-priorities-api
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments Issue Search API
  slug: postman-jira-issue-search-api
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments Issue Statuses API
  slug: postman-jira-issue-statuses-api
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments Issue Transitions API
  slug: postman-jira-issue-transitions-api
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments Issue Types API
  slug: postman-jira-issue-types-api
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments Issues API
  slug: postman-jira-issues-api
- collection_type: postman
  name: Jira Cloud Platform REST Issue Comments Projects API
  slug: postman-jira-projects-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Jira Cloud Platform REST API
  slug: open-jira-cloud-platform-rest-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments API
  slug: open-jira-issue-comments-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments Issue Priorities API
  slug: open-jira-issue-priorities-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments Issue Search API
  slug: open-jira-issue-search-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments Issue Statuses API
  slug: open-jira-issue-statuses-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments Issue Transitions API
  slug: open-jira-issue-transitions-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments Issue Types API
  slug: open-jira-issue-types-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments Issues API
  slug: open-jira-issues-api
- collection_type: open
  name: Jira Cloud Platform REST Issue Comments Projects API
  slug: open-jira-projects-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/jira/overview
- group: build
  title: ''
  type: Packages
  url: packages/jira-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jira-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/jira-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/jira-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jira-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/jira-cloud-platform-rest-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/jira-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/jira-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/jira-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/jira-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/jira-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/jira-cli.yml
- group: design
  title: ''
  type: Components
  url: components/jira-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/jira-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jira-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/jira-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jira-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jira-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/jira-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/jira-scopes.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jira-comment-thread-reply-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jira-create-issue-read-back-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jira-deduplicate-issue-intake-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jira-edit-issue-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jira-issue-metadata-bootstrap-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jira-jql-issue-report-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jira-project-discovery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jira-safe-issue-delete-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jira-stale-issue-sweep-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/jira-transition-issue-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.atlassian.com/cloud/jira/platform/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.atlassian.com/cloud/jira/platform/getting-started/
- group: build
  title: ''
  type: SDKs
  url: https://developer.atlassian.com/cloud/jira/platform/libraries/
- group: auth
  title: OAuth 2.0
  type: Authentication
  url: https://developer.atlassian.com/cloud/jira/platform/oauth-2-3lo-apps/
- group: operate
  title: ''
  type: Support
  url: https://support.atlassian.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.atlassian.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.atlassian.com/legal/cloud-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.atlassian.com/legal/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.atlassian.com/changelog/
- group: company
  title: ''
  type: Blog
  url: https://www.atlassian.com/blog/developer
- group: other
  title: ''
  type: Marketplace
  url: https://developer.atlassian.com/platform/marketplace/getting-started/
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.atlassian.com/cloud/jira/platform/rate-limiting/
- group: auth
  title: ''
  type: Security
  url: https://developer.atlassian.com/cloud/jira/platform/security-overview/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/jira-issue-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/jira-project-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/jira-context.jsonld
created: '2024'
description: APIs for Atlassian Jira project management and issue tracking platform.
examples:
- key_count: 3
  name: Jira Cloud Platform Rest Atlassian Document Format Example
  slug: jira-cloud-platform-rest-atlassian-document-format-example
- key_count: 8
  name: Jira Cloud Platform Rest Attachment Example
  slug: jira-cloud-platform-rest-attachment-example
- key_count: 4
  name: Jira Cloud Platform Rest Avatar Urls Example
  slug: jira-cloud-platform-rest-avatar-urls-example
- key_count: 3
  name: Jira Cloud Platform Rest Change History Example
  slug: jira-cloud-platform-rest-change-history-example
- key_count: 7
  name: Jira Cloud Platform Rest Change Item Example
  slug: jira-cloud-platform-rest-change-item-example
- key_count: 4
  name: Jira Cloud Platform Rest Changelog Example
  slug: jira-cloud-platform-rest-changelog-example
- key_count: 6
  name: Jira Cloud Platform Rest Comment Example
  slug: jira-cloud-platform-rest-comment-example
- key_count: 7
  name: Jira Cloud Platform Rest Component Example
  slug: jira-cloud-platform-rest-component-example
- key_count: 4
  name: Jira Cloud Platform Rest Created Issue Example
  slug: jira-cloud-platform-rest-created-issue-example
- key_count: 2
  name: Jira Cloud Platform Rest Entity Property Example
  slug: jira-cloud-platform-rest-entity-property-example
- key_count: 3
  name: Jira Cloud Platform Rest Error Collection Example
  slug: jira-cloud-platform-rest-error-collection-example
- key_count: 5
  name: Jira Cloud Platform Rest Field Update Operation Example
  slug: jira-cloud-platform-rest-field-update-operation-example
- key_count: 8
  name: Jira Cloud Platform Rest Issue Bean Example
  slug: jira-cloud-platform-rest-issue-bean-example
- key_count: 4
  name: Jira Cloud Platform Rest Issue Create Request Example
  slug: jira-cloud-platform-rest-issue-create-request-example
- key_count: 17
  name: Jira Cloud Platform Rest Issue Fields Example
  slug: jira-cloud-platform-rest-issue-fields-example
- key_count: 2
  name: Jira Cloud Platform Rest Issue Link Example
  slug: jira-cloud-platform-rest-issue-link-example
- key_count: 5
  name: Jira Cloud Platform Rest Issue Link Type Example
  slug: jira-cloud-platform-rest-issue-link-type-example
- key_count: 4
  name: Jira Cloud Platform Rest Issue Ref Example
  slug: jira-cloud-platform-rest-issue-ref-example
- key_count: 3
  name: Jira Cloud Platform Rest Issue Transition Request Example
  slug: jira-cloud-platform-rest-issue-transition-request-example
- key_count: 8
  name: Jira Cloud Platform Rest Issue Type Details Example
  slug: jira-cloud-platform-rest-issue-type-details-example
- key_count: 5
  name: Jira Cloud Platform Rest Issue Type With Status Example
  slug: jira-cloud-platform-rest-issue-type-with-status-example
- key_count: 4
  name: Jira Cloud Platform Rest Issue Update Request Example
  slug: jira-cloud-platform-rest-issue-update-request-example
- key_count: 7
  name: Jira Cloud Platform Rest Page Bean Project Example
  slug: jira-cloud-platform-rest-page-bean-project-example
- key_count: 4
  name: Jira Cloud Platform Rest Page Of Comments Example
  slug: jira-cloud-platform-rest-page-of-comments-example
- key_count: 4
  name: Jira Cloud Platform Rest Page Of Worklogs Example
  slug: jira-cloud-platform-rest-page-of-worklogs-example
- key_count: 6
  name: Jira Cloud Platform Rest Priority Example
  slug: jira-cloud-platform-rest-priority-example
- key_count: 4
  name: Jira Cloud Platform Rest Project Category Example
  slug: jira-cloud-platform-rest-project-category-example
- key_count: 17
  name: Jira Cloud Platform Rest Project Example
  slug: jira-cloud-platform-rest-project-example
- key_count: 5
  name: Jira Cloud Platform Rest Project Ref Example
  slug: jira-cloud-platform-rest-project-ref-example
- key_count: 4
  name: Jira Cloud Platform Rest Resolution Example
  slug: jira-cloud-platform-rest-resolution-example
- key_count: 1
  name: Jira Cloud Platform Rest Scope Example
  slug: jira-cloud-platform-rest-scope-example
- key_count: 8
  name: Jira Cloud Platform Rest Search Request Example
  slug: jira-cloud-platform-rest-search-request-example
- key_count: 8
  name: Jira Cloud Platform Rest Search Results Example
  slug: jira-cloud-platform-rest-search-results-example
- key_count: 5
  name: Jira Cloud Platform Rest Status Category Example
  slug: jira-cloud-platform-rest-status-category-example
- key_count: 5
  name: Jira Cloud Platform Rest Status Details Example
  slug: jira-cloud-platform-rest-status-details-example
- key_count: 7
  name: Jira Cloud Platform Rest Transition Example
  slug: jira-cloud-platform-rest-transition-example
- key_count: 1
  name: Jira Cloud Platform Rest Transition Ref Example
  slug: jira-cloud-platform-rest-transition-ref-example
- key_count: 2
  name: Jira Cloud Platform Rest Transitions Example
  slug: jira-cloud-platform-rest-transitions-example
- key_count: 7
  name: Jira Cloud Platform Rest User Details Example
  slug: jira-cloud-platform-rest-user-details-example
- key_count: 10
  name: Jira Cloud Platform Rest Version Example
  slug: jira-cloud-platform-rest-version-example
- key_count: 3
  name: Jira Cloud Platform Rest Visibility Example
  slug: jira-cloud-platform-rest-visibility-example
- key_count: 3
  name: Jira Cloud Platform Rest Votes Example
  slug: jira-cloud-platform-rest-votes-example
- key_count: 3
  name: Jira Cloud Platform Rest Watches Example
  slug: jira-cloud-platform-rest-watches-example
- key_count: 7
  name: Jira Cloud Platform Rest Worklog Example
  slug: jira-cloud-platform-rest-worklog-example
features:
- 'Free: up to 10 users'
- 'Standard: $7.91-$9.05/user/mo (volume tiered)'
- 'Premium: $14.54-$18.30/user/mo with Advanced Roadmaps'
- 'Enterprise custom: Atlassian Intelligence, 99.95% uptime, data residency'
- 'Volume discount: rates drop above 100 users (max 50K)'
- REST API v3 at api.atlassian.com
- GraphQL API for some products
- Token-bucket rate limit ~10 req/sec/app/user
- Bulk operations max 100 items/request
- Webhooks v3 for issue/project events
- OAuth 2.0 (3LO) and API tokens
- Atlassian Connect framework for marketplace apps
- Forge for serverless app development
- JQL (Jira Query Language) for advanced search
- Atlassian Intelligence AI assistant (Enterprise)
- Cross-product Analytics + Atlas integrations
finops:
- name: Jira Finops
  service_category: Project Management
  slug: jira-finops
graphqls:
- description: ''
  name: Jira GraphQL API
  slug: jira-graphql
image: https://www.atlassian.com/dam/jcr:e33efd9e-e0b8-4d61-a24d-68a48ef9bbe4/jira-icon-blue.svg
integrations:
- description: Link Jira issues to Confluence pages for seamless knowledge management and documentation alongside project tracking.
  name: Confluence
- description: Connect code repositories to Jira issues for automated status updates, smart commits, and development tracking.
  name: Bitbucket
- description: Link GitHub pull requests, branches, and commits to Jira issues for end-to-end development visibility.
  name: GitHub
- description: Create and manage Jira issues from Slack channels with bi-directional notifications and status updates.
  name: Slack
- description: Receive Jira notifications and manage issues directly from Microsoft Teams conversations.
  name: Microsoft Teams
json_schemas:
- name: AtlassianDocumentFormat
  property_count: 3
  slug: jira-cloud-platform-rest-atlassian-document-format
- name: Attachment
  property_count: 8
  slug: jira-cloud-platform-rest-attachment
- name: AvatarUrls
  property_count: 4
  slug: jira-cloud-platform-rest-avatar-urls
- name: ChangeHistory
  property_count: 3
  slug: jira-cloud-platform-rest-change-history
- name: ChangeItem
  property_count: 7
  slug: jira-cloud-platform-rest-change-item
- name: Changelog
  property_count: 4
  slug: jira-cloud-platform-rest-changelog
- name: Comment
  property_count: 6
  slug: jira-cloud-platform-rest-comment
- name: Component
  property_count: 7
  slug: jira-cloud-platform-rest-component
- name: CreatedIssue
  property_count: 4
  slug: jira-cloud-platform-rest-created-issue
- name: EntityProperty
  property_count: 2
  slug: jira-cloud-platform-rest-entity-property
- name: ErrorCollection
  property_count: 3
  slug: jira-cloud-platform-rest-error-collection
- name: FieldUpdateOperation
  property_count: 5
  slug: jira-cloud-platform-rest-field-update-operation
- name: IssueBean
  property_count: 8
  slug: jira-cloud-platform-rest-issue-bean
- name: IssueCreateRequest
  property_count: 4
  slug: jira-cloud-platform-rest-issue-create-request
- name: IssueFields
  property_count: 17
  slug: jira-cloud-platform-rest-issue-fields
- name: IssueLink
  property_count: 2
  slug: jira-cloud-platform-rest-issue-link
- name: IssueLinkType
  property_count: 5
  slug: jira-cloud-platform-rest-issue-link-type
- name: IssueRef
  property_count: 4
  slug: jira-cloud-platform-rest-issue-ref
- name: IssueTransitionRequest
  property_count: 3
  slug: jira-cloud-platform-rest-issue-transition-request
- name: IssueTypeDetails
  property_count: 8
  slug: jira-cloud-platform-rest-issue-type-details
- name: IssueTypeWithStatus
  property_count: 5
  slug: jira-cloud-platform-rest-issue-type-with-status
- name: IssueUpdateRequest
  property_count: 4
  slug: jira-cloud-platform-rest-issue-update-request
- name: PageBeanProject
  property_count: 7
  slug: jira-cloud-platform-rest-page-bean-project
- name: PageOfComments
  property_count: 4
  slug: jira-cloud-platform-rest-page-of-comments
- name: PageOfWorklogs
  property_count: 4
  slug: jira-cloud-platform-rest-page-of-worklogs
- name: Priority
  property_count: 6
  slug: jira-cloud-platform-rest-priority
- name: ProjectCategory
  property_count: 4
  slug: jira-cloud-platform-rest-project-category
- name: ProjectRef
  property_count: 5
  slug: jira-cloud-platform-rest-project-ref
- name: Project
  property_count: 17
  slug: jira-cloud-platform-rest-project
- name: Resolution
  property_count: 4
  slug: jira-cloud-platform-rest-resolution
- name: Scope
  property_count: 1
  slug: jira-cloud-platform-rest-scope
- name: SearchRequest
  property_count: 8
  slug: jira-cloud-platform-rest-search-request
- name: SearchResults
  property_count: 8
  slug: jira-cloud-platform-rest-search-results
- name: StatusCategory
  property_count: 5
  slug: jira-cloud-platform-rest-status-category
- name: StatusDetails
  property_count: 5
  slug: jira-cloud-platform-rest-status-details
- name: TransitionRef
  property_count: 1
  slug: jira-cloud-platform-rest-transition-ref
- name: Transition
  property_count: 7
  slug: jira-cloud-platform-rest-transition
- name: Transitions
  property_count: 2
  slug: jira-cloud-platform-rest-transitions
- name: UserDetails
  property_count: 7
  slug: jira-cloud-platform-rest-user-details
- name: Version
  property_count: 10
  slug: jira-cloud-platform-rest-version
- name: Visibility
  property_count: 3
  slug: jira-cloud-platform-rest-visibility
- name: Votes
  property_count: 3
  slug: jira-cloud-platform-rest-votes
- name: Watches
  property_count: 3
  slug: jira-cloud-platform-rest-watches
- name: Worklog
  property_count: 7
  slug: jira-cloud-platform-rest-worklog
- name: Jira Issue
  property_count: 10
  slug: jira-issue
- name: Jira Project
  property_count: 22
  slug: jira-project
json_structures:
- name: Jira Cloud Platform Rest Atlassian Document Format Structure
  property_count: 3
  slug: jira-cloud-platform-rest-atlassian-document-format-structure
- name: Jira Cloud Platform Rest Attachment Structure
  property_count: 8
  slug: jira-cloud-platform-rest-attachment-structure
- name: Jira Cloud Platform Rest Avatar Urls Structure
  property_count: 4
  slug: jira-cloud-platform-rest-avatar-urls-structure
- name: Jira Cloud Platform Rest Change History Structure
  property_count: 3
  slug: jira-cloud-platform-rest-change-history-structure
- name: Jira Cloud Platform Rest Change Item Structure
  property_count: 7
  slug: jira-cloud-platform-rest-change-item-structure
- name: Jira Cloud Platform Rest Changelog Structure
  property_count: 4
  slug: jira-cloud-platform-rest-changelog-structure
- name: Jira Cloud Platform Rest Comment Structure
  property_count: 6
  slug: jira-cloud-platform-rest-comment-structure
- name: Jira Cloud Platform Rest Component Structure
  property_count: 7
  slug: jira-cloud-platform-rest-component-structure
- name: Jira Cloud Platform Rest Created Issue Structure
  property_count: 4
  slug: jira-cloud-platform-rest-created-issue-structure
- name: Jira Cloud Platform Rest Entity Property Structure
  property_count: 2
  slug: jira-cloud-platform-rest-entity-property-structure
- name: Jira Cloud Platform Rest Error Collection Structure
  property_count: 3
  slug: jira-cloud-platform-rest-error-collection-structure
- name: Jira Cloud Platform Rest Field Update Operation Structure
  property_count: 5
  slug: jira-cloud-platform-rest-field-update-operation-structure
- name: Jira Cloud Platform Rest Issue Bean Structure
  property_count: 8
  slug: jira-cloud-platform-rest-issue-bean-structure
- name: Jira Cloud Platform Rest Issue Create Request Structure
  property_count: 4
  slug: jira-cloud-platform-rest-issue-create-request-structure
- name: Jira Cloud Platform Rest Issue Fields Structure
  property_count: 17
  slug: jira-cloud-platform-rest-issue-fields-structure
- name: Jira Cloud Platform Rest Issue Link Structure
  property_count: 2
  slug: jira-cloud-platform-rest-issue-link-structure
- name: Jira Cloud Platform Rest Issue Link Type Structure
  property_count: 5
  slug: jira-cloud-platform-rest-issue-link-type-structure
- name: Jira Cloud Platform Rest Issue Ref Structure
  property_count: 4
  slug: jira-cloud-platform-rest-issue-ref-structure
- name: Jira Cloud Platform Rest Issue Transition Request Structure
  property_count: 3
  slug: jira-cloud-platform-rest-issue-transition-request-structure
- name: Jira Cloud Platform Rest Issue Type Details Structure
  property_count: 8
  slug: jira-cloud-platform-rest-issue-type-details-structure
- name: Jira Cloud Platform Rest Issue Type With Status Structure
  property_count: 5
  slug: jira-cloud-platform-rest-issue-type-with-status-structure
- name: Jira Cloud Platform Rest Issue Update Request Structure
  property_count: 4
  slug: jira-cloud-platform-rest-issue-update-request-structure
- name: Jira Cloud Platform Rest Page Bean Project Structure
  property_count: 7
  slug: jira-cloud-platform-rest-page-bean-project-structure
- name: Jira Cloud Platform Rest Page Of Comments Structure
  property_count: 4
  slug: jira-cloud-platform-rest-page-of-comments-structure
- name: Jira Cloud Platform Rest Page Of Worklogs Structure
  property_count: 4
  slug: jira-cloud-platform-rest-page-of-worklogs-structure
- name: Jira Cloud Platform Rest Priority Structure
  property_count: 6
  slug: jira-cloud-platform-rest-priority-structure
- name: Jira Cloud Platform Rest Project Category Structure
  property_count: 4
  slug: jira-cloud-platform-rest-project-category-structure
- name: Jira Cloud Platform Rest Project Ref Structure
  property_count: 5
  slug: jira-cloud-platform-rest-project-ref-structure
- name: Jira Cloud Platform Rest Project Structure
  property_count: 17
  slug: jira-cloud-platform-rest-project-structure
- name: Jira Cloud Platform Rest Resolution Structure
  property_count: 4
  slug: jira-cloud-platform-rest-resolution-structure
- name: Jira Cloud Platform Rest Scope Structure
  property_count: 1
  slug: jira-cloud-platform-rest-scope-structure
- name: Jira Cloud Platform Rest Search Request Structure
  property_count: 8
  slug: jira-cloud-platform-rest-search-request-structure
- name: Jira Cloud Platform Rest Search Results Structure
  property_count: 8
  slug: jira-cloud-platform-rest-search-results-structure
- name: Jira Cloud Platform Rest Status Category Structure
  property_count: 5
  slug: jira-cloud-platform-rest-status-category-structure
- name: Jira Cloud Platform Rest Status Details Structure
  property_count: 5
  slug: jira-cloud-platform-rest-status-details-structure
- name: Jira Cloud Platform Rest Transition Ref Structure
  property_count: 1
  slug: jira-cloud-platform-rest-transition-ref-structure
- name: Jira Cloud Platform Rest Transition Structure
  property_count: 7
  slug: jira-cloud-platform-rest-transition-structure
- name: Jira Cloud Platform Rest Transitions Structure
  property_count: 2
  slug: jira-cloud-platform-rest-transitions-structure
- name: Jira Cloud Platform Rest User Details Structure
  property_count: 7
  slug: jira-cloud-platform-rest-user-details-structure
- name: Jira Cloud Platform Rest Version Structure
  property_count: 10
  slug: jira-cloud-platform-rest-version-structure
- name: Jira Cloud Platform Rest Visibility Structure
  property_count: 3
  slug: jira-cloud-platform-rest-visibility-structure
- name: Jira Cloud Platform Rest Votes Structure
  property_count: 3
  slug: jira-cloud-platform-rest-votes-structure
- name: Jira Cloud Platform Rest Watches Structure
  property_count: 3
  slug: jira-cloud-platform-rest-watches-structure
- name: Jira Cloud Platform Rest Worklog Structure
  property_count: 7
  slug: jira-cloud-platform-rest-worklog-structure
jsonld:
- class_count: 0
  name: Jira Cloud Platform Rest Context
  property_count: 0
  slug: jira-cloud-platform-rest-context
- class_count: 0
  name: Jira Context
  property_count: 15
  slug: jira-context
layout: provider
mcp_servers:
- description: ''
  name: Atlassian Rovo MCP Server
  slug: atlassian-rovo-mcp-server
modified: '2026-06-20'
name: Jira
nav: Providers
network: true
overview: 'Jira publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Issue Comments API, Issue Priorities API, Issue Search API, and 5 more. Tagged areas include Agile, Issue Tracking, ITSM, Project Management, and Service Management.


  The Jira catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 3 Spectral governance rulesets.


  Jira''s developer surface includes changelog, CLI, authentication, developer portal, getting-started guide, support, engineering blog, and 40 more developer resources.'
plans:
- name: Jira Plans Pricing
  plan_count: 4
  slug: jira-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Jira Rate Limits
  slug: jira-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Jira API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 4
  slug: jira-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Jira API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: jira-jsonschema-spectral-rules
- effective_rule_count: 58
  extends:
  - spectral:oas
  name: Jira API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 7
  slug: jira-spectral-rules
scopes:
- name: Jira Scopes
  scope_count: 5
  slug: jira-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: strong
  composite: 59.1
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 30.3
    contract_quality: 80.3
    developer_ergonomics: 59.5
    discoverability: 90.7
    governance: 30.3
    operational_transparency: 50.0
  previous_composite: 59.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jira/refs/heads/main/screenshots/jira-2026-06-20T183734.png
security:
- kind: authentication
  name: Jira Authentication
  slug: jira-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Jira Domain Security
  slug: jira-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Jira Vulnerability Disclosure
  slug: jira-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Jira Trust Center
  slug: jira-trust-center
  summary_line: FedRAMP
slug: jira
tags:
- Agile
- Issue Tracking
- ITSM
- Project Management
- Service Management
use_cases:
- description: Automate issue creation, assignment, and transitions based on external events from CI/CD pipelines, monitoring tools, or customer feedback systems.
  name: Issue Tracking Automation
- description: Programmatically manage sprints, backlogs, and board configurations for automated agile workflow orchestration.
  name: Sprint Management
- description: Integrate customer support channels with Jira Service Management for automated ticket creation and SLA tracking.
  name: Service Desk Integration
- description: Automate incident response workflows with on-call scheduling, alert routing, and escalation management.
  name: Incident Management
- description: Connect portfolio planning tools with Jira Align for cross-team dependency tracking and program-level reporting.
  name: Enterprise Agile Planning
website: https://developer.atlassian.com/cloud/jira/platform/
---
