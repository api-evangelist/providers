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
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 53.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 112
  human_in_the_loop: 1
  name: Outline Agentic Access
  operation_count: 112
  slug: outline-agentic-access
  summary_line: 112 operations · 112 acting · 1 human-in-the-loop
api_count: 18
apis:
- description: '`AccessRequests` represent a request by a user for access to a document they do not currently have permission to view. The request can be approved or dismissed by a user with permission to share the d'
  name: Outline AccessRequests API
  slug: outline-accessrequests-api
- description: '`Attachments` represent a file uploaded to cloud storage. They are created before the upload happens from the client and store all the meta information such as file type, size, and location.'
  name: Outline Attachments API
  slug: outline-attachments-api
- description: '`Auth` represents the current API Keys authentication details. It can be used to check that a token is still valid and load the IDs for the current user and workspace.'
  name: Outline Auth API
  slug: outline-auth-api
- description: '`Collections` represent grouping of documents in the knowledge base, they offer a way to structure information in a nested hierarchy and a level at which read and write permissions can be granted to i'
  name: Outline Collections API
  slug: outline-collections-api
- description: '`Comments` represent a comment either on a selection of text in a document or on the document itself.'
  name: Outline Comments API
  slug: outline-comments-api
- description: '`DataAttributes` represent custom metadata fields that can be attached to documents. They allow workspaces to add structured data like status, priority, or any other custom properties to their documen'
  name: Outline DataAttributes API
  slug: outline-dataattributes-api
- description: '`Documents` are what everything else revolves around. A document represents a single page of information and always returns the latest version of the content. Documents are stored in [Markdown](https:'
  name: Outline Documents API
  slug: outline-documents-api
- description: '`Events` represent an artifact of an action. Whether it is creating a user, editing a document, changing permissions, or any other action – an event is created that can be used as an audit trail or ac'
  name: Outline Events API
  slug: outline-events-api
- description: '`FileOperations` represent background jobs for importing or exporting files. You can query the file operation to find the state of progress and any resulting output.'
  name: Outline FileOperations API
  slug: outline-fileoperations-api
- description: '`Groups` represent a list of users that logically belong together, for example there might be groups for each department in your organization. Groups can be granted access to collections with read or '
  name: Outline Groups API
  slug: outline-groups-api
- description: '`OAuthAuthentications` represent individual scoped authentications between Outline and an `OAuthClient`.'
  name: Outline OAuthAuthentications API
  slug: outline-oauthauthentications-api
- description: '`OAuthClients` represent OAuth clients that can be used to authenticate users with third-party services.'
  name: Outline OAuthClients API
  slug: outline-oauthclients-api
- description: '`Revisions` represent a snapshot of a document at a point in time. They are used to keep track of editing and collaboration history – a document can also be restored to a previous revision if necessar'
  name: Outline Revisions API
  slug: outline-revisions-api
- description: '`Shares` represent authorization to view a document without being a member of the workspace. Shares are created in order to give access to documents publicly. Each user that shares a document will hav'
  name: Outline Shares API
  slug: outline-shares-api
- description: '`Stars` represent a favorited document or collection in the application sidebar. Each user has their own collection of starred items.'
  name: Outline Stars API
  slug: outline-stars-api
- description: '`Templates` represent reusable document templates that can be used as a starting point when creating new documents. Templates can be scoped to a specific collection or available workspace-wide.'
  name: Outline Templates API
  slug: outline-templates-api
- description: '`Users` represent an individual with access to the knowledge base. Users can be created automatically when signing in with SSO or when a user is invited via email.'
  name: Outline Users API
  slug: outline-users-api
- description: '`Views` represent a compressed record of an individual users views of a document. Individual views are not recorded but a first, last and total is kept per user.'
  name: Outline Views API
  slug: outline-views-api
artifact_total: 178
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/outline-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/outline-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/outline-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/outline-scopes.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.getoutline.com/s/guide
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/outline/openapi/main/spec3.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/outline
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/outline/outline
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.getoutline.com/changelog
- group: operate
  title: ''
  type: Status
  url: https://status.getoutline.com/
- group: design
  title: ''
  type: Webhooks
  url: https://docs.getoutline.com/s/47305ccd-9f29-4edf-b48a-21c239bd625e
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getoutline.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/outline-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/outline-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/outline-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.getoutline.com/changelog
created: '2026-06-13'
description: Outline is an open-source team knowledge base and wiki with a fully featured RPC-style REST API for programmatically managing documents, collections, teams, users, groups, comments, shares, attachments, and importing or exporting organizational knowledge. The main application itself is built on the same API it exposes publicly.
examples:
- key_count: 6
  name: Accessrequestsapprove
  slug: accessRequestsApprove
- key_count: 6
  name: Accessrequestscreate
  slug: accessRequestsCreate
- key_count: 6
  name: Accessrequestsdismiss
  slug: accessRequestsDismiss
- key_count: 6
  name: Accessrequestsinfo
  slug: accessRequestsInfo
- key_count: 6
  name: Attachmentscreate
  slug: attachmentsCreate
- key_count: 6
  name: Attachmentsdelete
  slug: attachmentsDelete
- key_count: 6
  name: Attachmentsredirect
  slug: attachmentsRedirect
- key_count: 5
  name: Authconfig
  slug: authConfig
- key_count: 5
  name: Authinfo
  slug: authInfo
- key_count: 6
  name: Collectionsaddgroup
  slug: collectionsAddGroup
- key_count: 6
  name: Collectionsadduser
  slug: collectionsAddUser
- key_count: 6
  name: Collectionscreate
  slug: collectionsCreate
- key_count: 6
  name: Collectionsdelete
  slug: collectionsDelete
- key_count: 6
  name: Collectionsdocuments
  slug: collectionsDocuments
- key_count: 6
  name: Collectionsexport
  slug: collectionsExport
- key_count: 6
  name: Collectionsexportall
  slug: collectionsExportAll
- key_count: 6
  name: Collectionsgroupmemberships
  slug: collectionsGroupMemberships
- key_count: 6
  name: Collectionsinfo
  slug: collectionsInfo
- key_count: 6
  name: Collectionslist
  slug: collectionsList
- key_count: 6
  name: Collectionsmemberships
  slug: collectionsMemberships
- key_count: 6
  name: Collectionsremovegroup
  slug: collectionsRemoveGroup
- key_count: 6
  name: Collectionsremoveuser
  slug: collectionsRemoveUser
- key_count: 6
  name: Collectionsupdate
  slug: collectionsUpdate
- key_count: 6
  name: Commentscreate
  slug: commentsCreate
- key_count: 6
  name: Commentsdelete
  slug: commentsDelete
- key_count: 6
  name: Commentsinfo
  slug: commentsInfo
- key_count: 6
  name: Commentslist
  slug: commentsList
- key_count: 6
  name: Commentsupdate
  slug: commentsUpdate
- key_count: 6
  name: Dataattributescreate
  slug: dataAttributesCreate
- key_count: 6
  name: Dataattributesdelete
  slug: dataAttributesDelete
- key_count: 6
  name: Dataattributesinfo
  slug: dataAttributesInfo
- key_count: 6
  name: Dataattributeslist
  slug: dataAttributesList
- key_count: 6
  name: Dataattributesupdate
  slug: dataAttributesUpdate
- key_count: 6
  name: Documentsaddgroup
  slug: documentsAddGroup
- key_count: 6
  name: Documentsadduser
  slug: documentsAddUser
- key_count: 6
  name: Documentsanswerquestion
  slug: documentsAnswerQuestion
- key_count: 6
  name: Documentsarchive
  slug: documentsArchive
- key_count: 6
  name: Documentsarchived
  slug: documentsArchived
- key_count: 6
  name: Documentscreate
  slug: documentsCreate
- key_count: 6
  name: Documentsdelete
  slug: documentsDelete
- key_count: 6
  name: Documentsdeleted
  slug: documentsDeleted
- key_count: 6
  name: Documentsdocuments
  slug: documentsDocuments
- key_count: 6
  name: Documentsdrafts
  slug: documentsDrafts
- key_count: 6
  name: Documentsduplicate
  slug: documentsDuplicate
- key_count: 5
  name: Documentsemptytrash
  slug: documentsEmptyTrash
- key_count: 6
  name: Documentsexport
  slug: documentsExport
- key_count: 6
  name: Documentsgroupmemberships
  slug: documentsGroupMemberships
- key_count: 6
  name: Documentsimport
  slug: documentsImport
- key_count: 6
  name: Documentsinfo
  slug: documentsInfo
- key_count: 6
  name: Documentsinsights
  slug: documentsInsights
- key_count: 6
  name: Documentslist
  slug: documentsList
- key_count: 6
  name: Documentsmemberships
  slug: documentsMemberships
- key_count: 6
  name: Documentsmove
  slug: documentsMove
- key_count: 6
  name: Documentsremovegroup
  slug: documentsRemoveGroup
- key_count: 6
  name: Documentsremoveuser
  slug: documentsRemoveUser
- key_count: 6
  name: Documentsrestore
  slug: documentsRestore
- key_count: 6
  name: Documentssearch
  slug: documentsSearch
- key_count: 6
  name: Documentssearchtitles
  slug: documentsSearchTitles
- key_count: 6
  name: Documentstemplatize
  slug: documentsTemplatize
- key_count: 6
  name: Documentsunpublish
  slug: documentsUnpublish
- key_count: 6
  name: Documentsupdate
  slug: documentsUpdate
- key_count: 6
  name: Documentsusers
  slug: documentsUsers
- key_count: 6
  name: Documentsviewed
  slug: documentsViewed
- key_count: 6
  name: Eventslist
  slug: eventsList
- key_count: 6
  name: Fileoperationsdelete
  slug: fileOperationsDelete
- key_count: 6
  name: Fileoperationsinfo
  slug: fileOperationsInfo
- key_count: 6
  name: Fileoperationslist
  slug: fileOperationsList
- key_count: 6
  name: Fileoperationsredirect
  slug: fileOperationsRedirect
- key_count: 6
  name: Groupsadduser
  slug: groupsAddUser
- key_count: 6
  name: Groupscreate
  slug: groupsCreate
- key_count: 6
  name: Groupsdelete
  slug: groupsDelete
- key_count: 6
  name: Groupsinfo
  slug: groupsInfo
- key_count: 6
  name: Groupslist
  slug: groupsList
- key_count: 6
  name: Groupsmemberships
  slug: groupsMemberships
- key_count: 6
  name: Groupsremoveuser
  slug: groupsRemoveUser
- key_count: 6
  name: Groupsupdate
  slug: groupsUpdate
- key_count: 6
  name: Oauthauthenticationsdelete
  slug: oauthAuthenticationsDelete
- key_count: 6
  name: Oauthauthenticationslist
  slug: oauthAuthenticationsList
- key_count: 6
  name: Oauthclientscreate
  slug: oauthClientsCreate
- key_count: 6
  name: Oauthclientsdelete
  slug: oauthClientsDelete
- key_count: 6
  name: Oauthclientsinfo
  slug: oauthClientsInfo
- key_count: 6
  name: Oauthclientslist
  slug: oauthClientsList
- key_count: 6
  name: Oauthclientsrotatesecret
  slug: oauthClientsRotateSecret
- key_count: 6
  name: Oauthclientsupdate
  slug: oauthClientsUpdate
- key_count: 6
  name: Revisionsinfo
  slug: revisionsInfo
- key_count: 6
  name: Revisionslist
  slug: revisionsList
- key_count: 6
  name: Sharescreate
  slug: sharesCreate
- key_count: 6
  name: Sharesinfo
  slug: sharesInfo
- key_count: 6
  name: Shareslist
  slug: sharesList
- key_count: 6
  name: Sharesrevoke
  slug: sharesRevoke
- key_count: 6
  name: Sharesupdate
  slug: sharesUpdate
- key_count: 6
  name: Starscreate
  slug: starsCreate
- key_count: 6
  name: Starsdelete
  slug: starsDelete
- key_count: 6
  name: Starslist
  slug: starsList
- key_count: 6
  name: Starsupdate
  slug: starsUpdate
- key_count: 6
  name: Templatescreate
  slug: templatesCreate
- key_count: 6
  name: Templatesdelete
  slug: templatesDelete
- key_count: 6
  name: Templatesduplicate
  slug: templatesDuplicate
- key_count: 6
  name: Templatesinfo
  slug: templatesInfo
- key_count: 6
  name: Templateslist
  slug: templatesList
- key_count: 6
  name: Templatesrestore
  slug: templatesRestore
- key_count: 6
  name: Templatesupdate
  slug: templatesUpdate
- key_count: 6
  name: Usersactivate
  slug: usersActivate
- key_count: 6
  name: Usersdelete
  slug: usersDelete
- key_count: 6
  name: Usersinfo
  slug: usersInfo
- key_count: 6
  name: Usersinvite
  slug: usersInvite
- key_count: 6
  name: Userslist
  slug: usersList
- key_count: 6
  name: Userssuspend
  slug: usersSuspend
- key_count: 6
  name: Usersupdate
  slug: usersUpdate
- key_count: 6
  name: Usersupdaterole
  slug: usersUpdateRole
- key_count: 6
  name: Viewscreate
  slug: viewsCreate
- key_count: 6
  name: Viewslist
  slug: viewsList
finops:
- name: Outline Finops
  service_category: ''
  slug: outline-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/outline.png
json_schemas:
- name: Ability
  property_count: 0
  slug: ability
- name: AccessRequest
  property_count: 11
  slug: accessrequest
- name: Attachment
  property_count: 6
  slug: attachment
- name: Auth
  property_count: 2
  slug: auth
- name: Collection
  property_count: 20
  slug: collection
- name: CollectionGroupMembership
  property_count: 6
  slug: collectiongroupmembership
- name: CollectionStatus
  property_count: 0
  slug: collectionstatus
- name: Comment
  property_count: 13
  slug: comment
- name: DataAttribute
  property_count: 9
  slug: dataattribute
- name: DataAttributeDataType
  property_count: 0
  slug: dataattributedatatype
- name: DataAttributeOptions
  property_count: 2
  slug: dataattributeoptions
- name: Document
  property_count: 23
  slug: document
- name: DocumentDataAttribute
  property_count: 3
  slug: documentdataattribute
- name: DocumentInsight
  property_count: 8
  slug: documentinsight
- name: Error
  property_count: 5
  slug: error
- name: Event
  property_count: 12
  slug: event
- name: FileOperation
  property_count: 12
  slug: fileoperation
- name: Group
  property_count: 9
  slug: group
- name: GroupMembership
  property_count: 6
  slug: groupmembership
- name: Invite
  property_count: 3
  slug: invite
- name: Membership
  property_count: 8
  slug: membership
- name: NavigationNode
  property_count: 4
  slug: navigationnode
- name: OAuthAuthentication
  property_count: 7
  slug: oauthauthentication
- name: OAuthClient
  property_count: 14
  slug: oauthclient
- name: Pagination
  property_count: 2
  slug: pagination
- name: Permission
  property_count: 0
  slug: permission
- name: Policy
  property_count: 2
  slug: policy
- name: Revision
  property_count: 13
  slug: revision
- name: SearchResult
  property_count: 5
  slug: searchresult
- name: Share
  property_count: 23
  slug: share
- name: Sorting
  property_count: 2
  slug: sorting
- name: Star
  property_count: 6
  slug: star
- name: Team
  property_count: 19
  slug: team
- name: Template
  property_count: 15
  slug: template
- name: TextEditMode
  property_count: 0
  slug: texteditmode
- name: User
  property_count: 12
  slug: user
- name: UserRole
  property_count: 0
  slug: userrole
- name: View
  property_count: 7
  slug: view
jsonld:
- class_count: 0
  name: Outline Api Context
  property_count: 0
  slug: outline-api
- class_count: 16
  name: Outline Context
  property_count: 0
  slug: outline-context
layout: provider
modified: '2026-06-13'
name: Outline
nav: Providers
network: true
overview: 'Outline publishes 18 APIs on the [APIs.io](https://apis.io/) network, including AccessRequests API, Attachments API, Auth API, and 15 more. Tagged areas include Knowledge Base, Wiki, Documents, Collaboration, and Open Source.


  The Outline catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Outline''s developer surface includes authentication, documentation, changelog, status page, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Outline Plans Pricing
  plan_count: 4
  slug: outline-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Outline Rate Limits
  slug: outline-rate-limits
rules:
- name: Outline API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: outline-jsonschema-spectral-rules
scopes:
- name: Outline Scopes
  scope_count: 2
  slug: outline-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 53.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.9
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 28.9
  previous_composite: 53.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/outline/refs/heads/main/screenshots/outline-2026-06-20T191231.png
security:
- kind: authentication
  name: Outline Authentication
  slug: outline-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Outline Domain Security
  slug: outline-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: outline
tags:
- Knowledge Base
- Wiki
- Documents
- Collaboration
- Open Source
- Team
---
