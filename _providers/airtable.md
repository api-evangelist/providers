---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.5
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 36
  human_in_the_loop: 1
  name: Airtable Agentic Access
  operation_count: 56
  slug: airtable-agentic-access
  summary_line: 56 operations · 36 acting · 1 human-in-the-loop
api_count: 3
apis:
- baseURL: https://api.airtable.com
  baseurl_source: declared
  description: List and create bases, retrieve base schemas
  name: Airtable Bases API
  slug: airtable-bases-api
- baseURL: https://api.airtable.com
  baseurl_source: declared
  description: Manage comments on individual records
  name: Airtable Comments API
  slug: airtable-comments-api
- baseURL: https://api.airtable.com
  baseurl_source: declared
  description: Create and update field definitions within a table
  name: Airtable Fields API
  slug: airtable-fields-api
- baseURL: https://api.airtable.com
  baseurl_source: declared
  description: Manage user groups within the enterprise
  name: Airtable Groups API
  slug: airtable-groups-api
- baseURL: https://api.airtable.com
  baseurl_source: declared
  description: Create, read, update, and delete records in a table
  name: Airtable Records API
  slug: airtable-records-api
- baseURL: https://api.airtable.com
  baseurl_source: declared
  description: Create and update table definitions within a base
  name: Airtable Tables API
  slug: airtable-tables-api
- baseURL: https://api.airtable.com
  baseurl_source: declared
  description: Manage enterprise users, permissions, and access
  name: Airtable Users API
  slug: airtable-users-api
- baseURL: https://api.airtable.com
  baseurl_source: declared
  description: Subscribe to real-time change notifications on bases
  name: Airtable Webhooks API
  slug: airtable-webhooks-api
arazzos:
- description: Add a new table to an existing base and then add a field to that table.
  name: Airtable Add a Table with Fields
  slug: airtable-add-table-with-fields-workflow
- description: Find records matching a staleness formula and delete them.
  name: Airtable Archive Stale Records
  slug: airtable-archive-stale-records-workflow
- description: Enumerate accessible bases and inspect the schema of one of them.
  name: Airtable Audit Base Schemas
  slug: airtable-audit-base-schemas-workflow
- description: Create a batch of records in a table and verify the import landed.
  name: Airtable Bulk Import Records
  slug: airtable-bulk-import-records-workflow
- description: Confirm a record exists, then add a comment to it.
  name: Airtable Comment on Record
  slug: airtable-comment-on-record-workflow
- description: Discover a webhook and drain its payloads using cursor pagination.
  name: Airtable Consume Webhook Payloads
  slug: airtable-consume-webhook-payloads-workflow
- description: Find a SCIM user by username and then delete the resource.
  name: Airtable Deprovision a SCIM User
  slug: airtable-deprovision-scim-user-workflow
- description: Find records missing data and patch the empty fields.
  name: Airtable Enrich Records
  slug: airtable-enrich-records-workflow
- description: Rename a table and update one of its fields within an existing base.
  name: Airtable Evolve a Table Schema
  slug: airtable-evolve-table-schema-workflow
- description: Request an audit log export, poll until it is ready, then read the events.
  name: Airtable Export Audit Logs
  slug: airtable-export-audit-logs-workflow
- description: List a record's comments, edit one, then delete one.
  name: Airtable Manage Comment Thread
  slug: airtable-manage-comment-thread-workflow
- description: List a base's share links, then enable or disable a specific share.
  name: Airtable Manage Share Links
  slug: airtable-manage-share-links-workflow
- description: Page through every record in a table using the offset cursor.
  name: Airtable Paginate All Records
  slug: airtable-paginate-all-records-workflow
- description: Create a new base with its initial tables and read back the resulting schema.
  name: Airtable Provision a Base
  slug: airtable-provision-base-workflow
- description: Create a SCIM 2.0 user and read it back by its resource id.
  name: Airtable Provision a SCIM User
  slug: airtable-provision-scim-user-workflow
- description: Create a webhook on a base and confirm it was registered.
  name: Airtable Provision a Webhook
  slug: airtable-provision-webhook-workflow
- description: Create a new enterprise workspace and read back its collaborators.
  name: Airtable Provision a Workspace
  slug: airtable-provision-workspace-workflow
- description: Find a webhook on a base and extend its expiration time.
  name: Airtable Refresh a Webhook
  slug: airtable-refresh-webhook-workflow
- description: Find a webhook on a base and delete it.
  name: Airtable Teardown a Webhook
  slug: airtable-teardown-webhook-workflow
- description: Find a record by a key field and update it if it exists, otherwise create it.
  name: Airtable Upsert a Record
  slug: airtable-upsert-record-workflow
- description: Confirm the token's identity and scopes, then list the bases it can reach.
  name: Airtable Verify Token Access
  slug: airtable-verify-token-access-workflow
artifact_total: 161
asyncapis:
- description: The Airtable Webhooks API delivers lightweight change notifications to a subscriber's notification URL whenever data within a base or table changes. Airtable sends a small "ping" via HTTP POST identif
  name: Airtable Webhooks API
  slug: airtable-webhooks-asyncapi
collections:
- collection_type: postman
  name: Airtable API
  slug: postman-airtable-airtable-api
- collection_type: postman
  name: Airtable Audit Logs API
  slug: postman-airtable-audit-logs-api
- collection_type: postman
  name: Airtable Enterprise API
  slug: postman-airtable-enterprise-api
- collection_type: postman
  name: Airtable Metadata API
  slug: postman-airtable-metadata-api
- collection_type: postman
  name: Airtable SCIM API
  slug: postman-airtable-scim-api
- collection_type: postman
  name: Airtable Shares API
  slug: postman-airtable-shares-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Airtable API
  slug: open-airtable-airtable-api
- collection_type: open
  name: Airtable Audit Logs API
  slug: open-airtable-audit-logs-api
- collection_type: open
  name: Airtable Audit Logs Bases API
  slug: open-airtable-bases-api
- collection_type: open
  name: Airtable Audit Logs Comments API
  slug: open-airtable-comments-api
- collection_type: open
  name: Airtable Audit Logs Enterprise API
  slug: open-airtable-enterprise-api
- collection_type: open
  name: Airtable Audit Logs Fields API
  slug: open-airtable-fields-api
- collection_type: open
  name: Airtable Audit Logs Groups API
  slug: open-airtable-groups-api
- collection_type: open
  name: Airtable Metadata API
  slug: open-airtable-metadata-api
- collection_type: open
  name: Airtable Audit Logs Records API
  slug: open-airtable-records-api
- collection_type: open
  name: Airtable SCIM API
  slug: open-airtable-scim-api
- collection_type: open
  name: Airtable Audit Logs Shares API
  slug: open-airtable-shares-api
- collection_type: open
  name: Airtable Audit Logs Tables API
  slug: open-airtable-tables-api
- collection_type: open
  name: Airtable Audit Logs Users API
  slug: open-airtable-users-api
- collection_type: open
  name: Airtable Audit Logs Webhooks API
  slug: open-airtable-webhooks-api
- collection_type: open
  name: Airtable Audit Logs Workspaces API
  slug: open-airtable-workspaces-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.airtable.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/agentic-access/airtable-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/airtable-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/security/airtable-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/airtable-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/security/airtable-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airtable-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/authentication/airtable-authentication.yml
  title: ''
  type: Authentication
  url: authentication/airtable-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/airtable/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-add-table-with-fields-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-add-table-with-fields-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-archive-stale-records-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-archive-stale-records-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-audit-base-schemas-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-audit-base-schemas-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-audit-enterprise-users-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-audit-enterprise-users-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-bulk-import-records-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-bulk-import-records-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-comment-on-record-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-comment-on-record-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-consume-webhook-payloads-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-consume-webhook-payloads-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-deprovision-scim-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-deprovision-scim-user-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-enrich-records-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-enrich-records-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-evolve-table-schema-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-evolve-table-schema-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-export-audit-logs-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-export-audit-logs-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-manage-comment-thread-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-manage-comment-thread-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-manage-share-links-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-manage-share-links-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-offboard-enterprise-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-offboard-enterprise-user-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-onboard-enterprise-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-onboard-enterprise-user-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-paginate-all-records-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-paginate-all-records-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-provision-base-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-provision-base-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-provision-scim-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-provision-scim-user-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-provision-webhook-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-provision-webhook-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-provision-workspace-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-provision-workspace-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-refresh-webhook-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-refresh-webhook-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-teardown-webhook-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-teardown-webhook-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-upsert-record-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-upsert-record-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/arazzo/airtable-verify-token-access-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/airtable-verify-token-access-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://airtable.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://airtable.com/developers/web/api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://www.airtable.com/guides/scale/using-airtable-api
- group: auth
  title: ''
  type: Authentication
  url: https://airtable.com/developers/web/api/oauth-reference
- group: auth
  title: ''
  type: Authentication
  url: https://airtable.com/developers/web/api/scopes
- group: auth
  title: ''
  type: Authentication
  url: https://support.airtable.com/docs/creating-personal-access-tokens
- group: design
  title: ''
  type: ErrorCodes
  url: https://airtable.com/developers/web/api/errors
- group: operate
  title: ''
  type: RateLimits
  url: https://airtable.com/developers/web/api/rate-limits
- group: operate
  title: ''
  type: RateLimits
  url: https://support.airtable.com/docs/managing-api-call-limits-in-airtable
- group: operate
  title: ''
  type: ChangeLog
  url: https://airtable.com/developers/web/api/changelog
- group: other
  title: ''
  type: Policies
  url: https://support.airtable.com/docs/airtable-api-deprecation-guidelines
- group: docs
  title: ''
  type: Documentation
  url: https://airtable.com/developers/web/api/cursor-pagination
- group: docs
  title: ''
  type: Documentation
  url: https://airtable.com/developers/web/api/field-model
- group: docs
  title: ''
  type: Documentation
  url: https://airtable.com/developers/web/api/change-events
- group: company
  title: ''
  type: Blog
  url: https://blog.airtable.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.airtable.com
- group: operate
  title: ''
  type: Support
  url: https://support.airtable.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://airtable.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airtable.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://airtable.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/airtable
- group: operate
  title: ''
  type: Community
  url: https://community.airtable.com
- group: operate
  title: ''
  type: Forums
  url: https://community.airtable.com/c/developers/55
- group: start
  title: ''
  type: Portal
  url: https://www.airtable.com
- group: start
  title: ''
  type: Portal
  url: https://airtable.com/login
- group: start
  title: ''
  type: Signup
  url: https://airtable.com/signup
- group: company
  title: ''
  type: Newsletter
  url: http://eepurl.com/gVD-df
- group: docs
  title: ''
  type: Documentation
  url: https://airtable.com/developers/extensions
- group: docs
  title: ''
  type: Documentation
  url: https://airtable.com/developers/scripting/api
- group: docs
  title: ''
  type: Documentation
  url: https://support.airtable.com/docs/airtable-enterprise-api
- group: docs
  title: ''
  type: AsyncAPI
  url: https://support.airtable.com/docs/airtable-webhooks-api-overview
- group: docs
  title: ''
  type: Documentation
  url: https://airtable.com/developers/web/guides/webhooks-api
- group: docs
  title: ''
  type: Documentation
  url: https://support.airtable.com/docs/airtable-resources-for-developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.airtable.com/whatsnew
- group: company
  title: ''
  type: Twitter
  url: https://x.com/airtable
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airtable
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@AirtableApp
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/airtable
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Airtable/airtable.js
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/airtable
- group: design
  title: Airtable Spectral Rules
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/rules/airtable-spectral-rules.yml
- group: design
  title: Airtable Vocabulary
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/vocabulary/airtable-vocabulary.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Airtable/airtable-mcp-cli
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/Airtable/skills
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/ai-catalog/airtable-ai-catalog.yml
  title: ''
  type: AICatalog
  url: ai-catalog/airtable-ai-catalog.yml
created: '2023-11-21T00:00:00.000Z'
description: Airtable is a cloud-based collaboration service that combines the simplicity of a spreadsheet with the complexity of a database. It provides APIs for managing bases, tables, records, and more.
examples:
- key_count: 9
  name: Airtable Audit Log Event Example
  slug: airtable-audit-log-event-example
- key_count: 4
  name: Airtable Base Example
  slug: airtable-base-example
- key_count: 5
  name: Airtable Comment Example
  slug: airtable-comment-example
- key_count: 5
  name: Airtable Field Example
  slug: airtable-field-example
- key_count: 3
  name: Airtable Record Example
  slug: airtable-record-example
- key_count: 9
  name: Airtable Share Example
  slug: airtable-share-example
- key_count: 6
  name: Airtable Table Example
  slug: airtable-table-example
- key_count: 8
  name: Airtable User Example
  slug: airtable-user-example
- key_count: 5
  name: Airtable View Example
  slug: airtable-view-example
- key_count: 9
  name: Airtable Webhook Example
  slug: airtable-webhook-example
- key_count: 4
  name: Airtable Workspace Example
  slug: airtable-workspace-example
features:
- 'Free plan: small-team building blocks'
- Team at $20/user/mo annual with enhanced capacity
- Business at $45/user/mo with advanced customization
- Enterprise Scale with up to 100M records and unlimited workspaces
- REST API with 5 req/sec per base hard cap
- 10 records per write, 100 per read
- Webhooks for record/cell changes
- Airtable Sync for cross-base data flow
- Interface Designer for custom apps
- Automations with multi-step workflows
- Extensions marketplace for embedded apps
- OAuth 2.0 and personal access tokens
- Metadata API for schema discovery
- Attachments via S3-backed file uploads
- Linked records and lookups across bases
- AI features (Cobuilder, Field AI) on paid plans
finops:
- name: Airtable Finops
  service_category: Low-Code Database
  slug: airtable-finops
image: https://www.airtable.com/images/logo.png
json_schemas:
- name: Airtable Audit Log Event
  property_count: 9
  slug: airtable-audit-log-event
- name: AuditLogEvent
  property_count: 9
  slug: airtable-auditlogevent
- name: AuditLogEventList
  property_count: 2
  slug: airtable-auditlogeventlist
- name: AuditLogRequest
  property_count: 6
  slug: airtable-auditlogrequest
- name: Airtable Base
  property_count: 4
  slug: airtable-base
- name: BaseList
  property_count: 2
  slug: airtable-baselist
- name: BaseSchema
  property_count: 3
  slug: airtable-baseschema
- name: BaseSummary
  property_count: 3
  slug: airtable-basesummary
- name: Airtable Comment
  property_count: 5
  slug: airtable-comment
- name: CommentList
  property_count: 2
  slug: airtable-commentlist
- name: CreateAuditLogRequestBody
  property_count: 1
  slug: airtable-createauditlogrequestbody
- name: CreateBaseRequest
  property_count: 3
  slug: airtable-createbaserequest
- name: CreateFieldRequest
  property_count: 4
  slug: airtable-createfieldrequest
- name: CreateTableRequest
  property_count: 3
  slug: airtable-createtablerequest
- name: EnterpriseAccount
  property_count: 6
  slug: airtable-enterpriseaccount
- name: EnterpriseUser
  property_count: 8
  slug: airtable-enterpriseuser
- name: Error
  property_count: 1
  slug: airtable-error
- name: Airtable Field
  property_count: 5
  slug: airtable-field
- name: FieldSchema
  property_count: 5
  slug: airtable-fieldschema
- name: FieldValues
  property_count: 0
  slug: airtable-fieldvalues
- name: ManageUsersResponse
  property_count: 1
  slug: airtable-manageusersresponse
- name: Airtable Record
  property_count: 3
  slug: airtable-record
- name: RecordDeleted
  property_count: 2
  slug: airtable-recorddeleted
- name: RecordList
  property_count: 2
  slug: airtable-recordlist
- name: ScimError
  property_count: 4
  slug: airtable-scimerror
- name: ScimGroup
  property_count: 5
  slug: airtable-scimgroup
- name: ScimGroupCreateRequest
  property_count: 3
  slug: airtable-scimgroupcreaterequest
- name: ScimGroupListResponse
  property_count: 5
  slug: airtable-scimgrouplistresponse
- name: ScimMeta
  property_count: 3
  slug: airtable-scimmeta
- name: ScimPatchRequest
  property_count: 2
  slug: airtable-scimpatchrequest
- name: ScimUser
  property_count: 8
  slug: airtable-scimuser
- name: ScimUserCreateRequest
  property_count: 6
  slug: airtable-scimusercreaterequest
- name: ScimUserListResponse
  property_count: 5
  slug: airtable-scimuserlistresponse
- name: Airtable Share
  property_count: 9
  slug: airtable-share
- name: Airtable Table
  property_count: 6
  slug: airtable-table
- name: TableSchema
  property_count: 6
  slug: airtable-tableschema
- name: Airtable User
  property_count: 8
  slug: airtable-user
- name: UserGroup
  property_count: 5
  slug: airtable-usergroup
- name: UserRemoved
  property_count: 3
  slug: airtable-userremoved
- name: Airtable View
  property_count: 5
  slug: airtable-view
- name: ViewSchema
  property_count: 5
  slug: airtable-viewschema
- name: Airtable Webhook
  property_count: 9
  slug: airtable-webhook
- name: WebhookCreateRequest
  property_count: 2
  slug: airtable-webhookcreaterequest
- name: WebhookCreateResponse
  property_count: 3
  slug: airtable-webhookcreateresponse
- name: WebhookPayload
  property_count: 5
  slug: airtable-webhookpayload
- name: WebhookPayloadList
  property_count: 3
  slug: airtable-webhookpayloadlist
- name: WebhookSpecification
  property_count: 1
  slug: airtable-webhookspecification
- name: Airtable Workspace
  property_count: 4
  slug: airtable-workspace
- name: WorkspaceCollaborators
  property_count: 2
  slug: airtable-workspacecollaborators
json_structures:
- name: Airtable Audit Log Event Structure
  property_count: 9
  slug: airtable-audit-log-event-structure
- name: Airtable Base Structure
  property_count: 4
  slug: airtable-base-structure
- name: Airtable Comment Structure
  property_count: 5
  slug: airtable-comment-structure
- name: Airtable Field Structure
  property_count: 5
  slug: airtable-field-structure
- name: Airtable Record Structure
  property_count: 3
  slug: airtable-record-structure
- name: Airtable Share Structure
  property_count: 9
  slug: airtable-share-structure
- name: Airtable Structure
  property_count: 0
  slug: airtable-structure
- name: Airtable Table Structure
  property_count: 6
  slug: airtable-table-structure
- name: Airtable User Structure
  property_count: 8
  slug: airtable-user-structure
- name: Airtable View Structure
  property_count: 5
  slug: airtable-view-structure
- name: Airtable Webhook Structure
  property_count: 9
  slug: airtable-webhook-structure
- name: Airtable Workspace Structure
  property_count: 4
  slug: airtable-workspace-structure
jsonld:
- class_count: 1
  name: Airtable Context
  property_count: 14
  slug: airtable-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Airtable
nav: Providers
network: true
overview: 'Airtable publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Bases API, Comments API, Fields API, and 5 more. Tagged areas include Application, Collaboration, Data, Database, and Low-Code.


  The Airtable catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Airtable''s developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, engineering blog, support, and 68 more developer resources.'
plans:
- name: Airtable Plans Pricing
  plan_count: 4
  slug: airtable-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Airtable Rate Limits
  slug: airtable-rate-limits
rules:
- effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Airtable API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: airtable-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Airtable API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: airtable-jsonschema-spectral-rules
- effective_rule_count: 79
  extends:
  - spectral:oas
  name: Airtable API Rules
  rule_count: 38
  severity_counts:
    error: 9
    hint: 0
    info: 13
    warn: 16
  slug: airtable-spectral-rules
score:
  band: strong
  composite: 63.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 70.0
    catalog_earned_first_party: 0.0
    catalog_gap: 45.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 60.5
    contract_governance: 27.3
    contract_quality: 77.6
    developer_ergonomics: 71.9
    discoverability: 65.0
    operational_transparency: 44.7
  previous_composite: 62.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/airtable/refs/heads/main/screenshots/airtable-2026-06-20T171430.png
security:
- kind: authentication
  name: Airtable Authentication
  slug: airtable-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Airtable Domain Security
  slug: airtable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Airtable Vulnerability Disclosure
  slug: airtable-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 3
skills:
- name: airtable-cli
  slug: airtable-cli
- name: airtable-filters
  slug: airtable-filters
- name: airtable-overview
  slug: airtable-overview
slug: airtable
tags:
- Application
- Collaboration
- Data
- Database
- Low-Code
- Productivity
- Spreadsheets
use_cases:
- description: Track tasks, milestones, and team assignments in structured databases.
  name: Project Management
- description: Build custom CRM systems for tracking contacts, deals, and pipelines.
  name: CRM
- description: Manage editorial calendars, content assets, and publishing workflows.
  name: Content Management
- description: Track inventory, orders, and supply chain data.
  name: Inventory Management
- description: Coordinate event logistics, attendees, and schedules.
  name: Event Planning
- description: Manage job applicants, employee records, and onboarding processes.
  name: HR & Recruiting
website: https://www.airtable.com/
---
