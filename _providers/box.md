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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 59.6
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 291
  human_in_the_loop: 14
  name: Box Agentic Access
  operation_count: 537
  slug: box-agentic-access
  summary_line: 537 operations · 291 acting · 14 human-in-the-loop
api_count: 81
apis:
- description: A set of endpoints used to manage user authorization process.
  name: Box Authorization API
  slug: box-authorization-api
- description: The Authorize API from Box — 1 operation(s) for authorize.
  name: Box Authorize API
  slug: box-authorize-api
- description: Classification labels are used for content that is sensitive or under security restrictions.
  name: Box Classifications API
  slug: box-classifications-api
- description: Classification labels are used for files that are sensitive or under security restrictions.
  name: Box Classifications on Files API
  slug: box-classifications-on-files-api
- description: Classification labels are used for folders that are sensitive or under security restrictions.
  name: Box Classifications on Folders API
  slug: box-classifications-on-folders-api
- description: The Collaboration Whitelist Entries API from Box — 2 operation(s) for collaboration whitelist entries.
  name: Box Collaboration Whitelist Entries API
  slug: box-collaboration-whitelist-entries-api
- description: The Collaboration Whitelist Exempt Targets API from Box — 2 operation(s) for collaboration whitelist exempt targets.
  name: Box Collaboration Whitelist Exempt Targets API
  slug: box-collaboration-whitelist-exempt-targets-api
- description: Collaborations define access permissions for users and groups to files and folders, similar to access control lists.
  name: Box Collaborations API
  slug: box-collaborations-api
- description: A set of endpoints used to retrieve file, folder, pending, and group collaborations.
  name: Box Collaborations (List) API
  slug: box-collaborations-list-api
- description: Collections are a way to group files, folders, and web links without putting them all into a folder.
  name: Box Collections API
  slug: box-collections-api
- description: Comments are messages generated users on files, allowing users to collaborate on a file, discussing any feedback they might have on the content.
  name: Box Comments API
  slug: box-comments-api
- description: Device pinners allow enterprises to control what devices can use native Box applications.
  name: Box Device Pinners API
  slug: box-device-pinners-api
- description: A set of endpoints that manage domains for which users can collaborate with files and folders in an enterprise.
  name: Box Domain Restrictions for Collaborations API
  slug: box-domain-restrictions-for-collaborations-api
- description: A set of endpoints that allow exempting users from restrictions imposed by the list of allowed collaboration domains for a specific enterprise.
  name: Box Domain Restrictions (User Exemptions) API
  slug: box-domain-restrictions-user-exemptions-api
- description: Downloads allow saving files to the application's server, or directly by the end user in a browser.
  name: Box Downloads API
  slug: box-downloads-api
- description: Email aliases provide a list of emails additional to the user's primary login email.
  name: Box Email Aliases API
  slug: box-email-aliases-api
- description: The Enterprises API from Box — 1 operation(s) for enterprises.
  name: Box Enterprises API
  slug: box-enterprises-api
- description: Events provide a way for an application to subscribe to any actions performed by any user, users, or service in an enterprise.
  name: Box Events API
  slug: box-events-api
- description: File Requests provide a fast and secure way to request files and associated metadata from anyone. Users can create new file requests based on an existing file request, update file request settings, ac
  name: Box File Requests API
  slug: box-file-requests-api
- description: A legal hold is a process that an enterprise can use to preserve all forms of potentially relevant information when litigation is pending or reasonably anticipated. A File Version Legal Hold represent
  name: Box File Version Legal Holds API
  slug: box-file-version-legal-holds-api
- description: A retention policy blocks permanent deletion of content for a specified amount of time. A file version retention is a record for a retained file.
  name: Box File Version Retentions API
  slug: box-file-version-retentions-api
- description: A set of endpoints used to manage specific versions of a file.
  name: Box File Versions API
  slug: box-file-versions-api
- description: Files, together with Folders, are at the core of the Box API. Files can be uploaded and downloaded, as well as hold important metadata information about the content.
  name: Box Files API
  slug: box-files-api
- description: Folder locks define access restrictions placed by folder owners to prevent specific folders from being moved or deleted.
  name: Box Folder Locks API
  slug: box-folder-locks-api
- description: Folders, together with Files, are at the core of the Box API. Folders can be uploaded and downloaded, as well as hold important metadata information about the content.
  name: Box Folders API
  slug: box-folders-api
- description: Group memberships signify that a user is a part of the group.
  name: Box Group Memberships API
  slug: box-group-memberships-api
- description: Groups created in an enterprise.
  name: Box Groups API
  slug: box-groups-api
- description: Integration Mappings allow the users to manage where content from partner apps is stored in Box.
  name: Box Integration Mappings API
  slug: box-integration-mappings-api
- description: Invites are used to invite the user to an enterprise.
  name: Box Invites API
  slug: box-invites-api
- description: A legal hold is a process that an enterprise can use to preserve all forms of potentially relevant information when litigation is pending or reasonably anticipated.
  name: Box Legal Hold Policies API
  slug: box-legal-hold-policies-api
- description: A Legal Hold Policy Assignment is a relation between a policy and custodian. In this case, as custodian can be a user, folder, file, or file version.
  name: Box Legal Hold Policy Assignments API
  slug: box-legal-hold-policy-assignments-api
- description: A metadata cascade policy describes how metadata instances applied to a folder should be applied to any item within that folder.
  name: Box Metadata Cascade Policies API
  slug: box-metadata-cascade-policies-api
- description: A metadata instance describes the relation between a template and a file, including the values that are assigned for every field.
  name: Box Metadata Instances (Files) API
  slug: box-metadata-instances-files-api
- description: A metadata instance describes the relation between a template and a folder, including the values that are assigned for every field.
  name: Box Metadata Instances (Folders) API
  slug: box-metadata-instances-folders-api
- description: The Metadata Queries API from Box — 1 operation(s) for metadata queries.
  name: Box Metadata Queries API
  slug: box-metadata-queries-api
- description: A metadata template describes a reusable set of key/value pairs that can be assigned to a file.
  name: Box Metadata Templates API
  slug: box-metadata-templates-api
- description: The Oauth2 API from Box — 3 operation(s) for oauth2.
  name: Box Oauth2 API
  slug: box-oauth2-api
- description: Recent items represent items such as files or folders that the user accessed recently.
  name: Box Recent Items API
  slug: box-recent-items-api
- description: A retention policy blocks permanent deletion of content for a specified amount of time. Admins can create retention policies and then assign them to specific folders or their entire enterprise.
  name: Box Retention Policies API
  slug: box-retention-policies-api
- description: A Retention Policy Assignment is a relation between a policy and folder or enterprise. Creating an assignment puts a retention on all the file versions that belong to that folder or enterprise.
  name: Box Retention Policy Assignments API
  slug: box-retention-policy-assignments-api
- description: The Box API provides a way to find content in Box using full-text search queries.
  name: Box Search API
  slug: box-search-api
- description: Session termination API is used to validate the roles and permissions of the group, and creates asynchronous jobs to terminate the group's sessions.
  name: Box Session Termination API
  slug: box-session-termination-api
- description: The Shared Items API from Box — 1 operation(s) for shared items.
  name: Box Shared Items API
  slug: box-shared-items-api
- description: The Shared Items#folders API from Box — 1 operation(s) for shared items#folders.
  name: Box Shared Items#folders API
  slug: box-shared-items-folders-api
- description: The Shared Items#web Links API from Box — 1 operation(s) for shared items#web links.
  name: Box Shared Items#web Links API
  slug: box-shared-items-web-links-api
- description: Files shared links are URLs that are generated for files stored in Box, which provide direct, read-only access to the resource.
  name: Box Shared Links (Files) API
  slug: box-shared-links-files-api
- description: Folders shared links are URLs that are generated for folders stored in Box, which provide direct, read-only access to the resource.
  name: Box Shared Links (Folders) API
  slug: box-shared-links-folders-api
- description: Web links for files are URLs that are generated for web links in Box, which provide direct, read-only access to the resource.
  name: Box Shared Links (Web Links) API
  slug: box-shared-links-web-links-api
- description: Shield information barrier reports contain information on what existing collaborations will be removed permanently when the information barrier is enabled.
  name: Box Shield Information Barrier Reports API
  slug: box-shield-information-barrier-reports-api
- description: Shield information barrier segment member represents a user that is assigned to a specific segment.
  name: Box Shield Information Barrier Segment Members API
  slug: box-shield-information-barrier-segment-members-api
- description: Shield information barrier segment restriction is an access restriction based on the content (file or folder) owner.
  name: Box Shield Information Barrier Segment Restrictions API
  slug: box-shield-information-barrier-segment-restrictions-api
- description: Shield information barrier segment represents a defined group of users. A user can be a member of only one segment, which makes segments different from groups.
  name: Box Shield Information Barrier Segments API
  slug: box-shield-information-barrier-segments-api
- description: Shield information barrier in Box defines an ethical wall. An ethical wall is a mechanism that prevents exchanges or communication that could lead to conflicts of interest and therefore result in busi
  name: Box Shield Information Barriers API
  slug: box-shield-information-barriers-api
- description: Sign requests are used to submit a file for signature.
  name: Box Sign Requests API
  slug: box-sign-requests-api
- description: Sign templates allow you to use a predefined Box Sign template when creating a sign request. The template includes placeholders that are automatically populated with data when creating the request.
  name: Box Sign Templates API
  slug: box-sign-templates-api
- description: The Skill Invocations API from Box — 1 operation(s) for skill invocations.
  name: Box Skill Invocations API
  slug: box-skill-invocations-api
- description: Box Skills are designed to allow custom processing of files uploaded to Box, with the intent of enhancing the underlying metadata of the file.
  name: Box Skills API
  slug: box-skills-api
- description: Storage policy assignment represents the storage zone for items in a given enterprise.
  name: Box Standard and Zones Storage Policies API
  slug: box-standard-and-zones-storage-policies-api
- description: Storage policy assignment represents the relation between storage zone and the assigned item (for example a file stored in a specific zone).
  name: Box Standard and Zones Storage Policy Assignments API
  slug: box-standard-and-zones-storage-policy-assignments-api
- description: The Storage Policies API from Box — 2 operation(s) for storage policies.
  name: Box Storage Policies API
  slug: box-storage-policies-api
- description: The Storage Policy Assignments API from Box — 2 operation(s) for storage policy assignments.
  name: Box Storage Policy Assignments API
  slug: box-storage-policy-assignments-api
- description: A task assignment defines which task is assigned to which user to complete.
  name: Box Task Assignments API
  slug: box-task-assignments-api
- description: Tasks allow users to request collaborators on a file to review a file or complete a piece of work. Tasks can be used by developers to create file-centric workflows.
  name: Box Tasks API
  slug: box-tasks-api
- description: A set of endpoints used to manage terms of service agreements.
  name: Box Terms of Service API
  slug: box-terms-of-service-api
- description: A set of endpoints used to manage the status of terms of service for a particular user.
  name: Box Terms of Service User Statuses API
  slug: box-terms-of-service-user-statuses-api
- description: The Terms of Services API from Box — 2 operation(s) for terms of services.
  name: Box Terms of Services API
  slug: box-terms-of-services-api
- description: API designed to move all of the items (files, folders and workflows) owned by a user into another user's account.
  name: Box Transfer Folders API
  slug: box-transfer-folders-api
- description: Files that were deleted and are in trash.
  name: Box Trashed Files API
  slug: box-trashed-files-api
- description: Folders that were deleted and are in trash.
  name: Box Trashed Folders API
  slug: box-trashed-folders-api
- description: Items that were deleted and are in trash.
  name: Box Trashed Items API
  slug: box-trashed-items-api
- description: Web links that were deleted and are in trash.
  name: Box Trashed Web Links API
  slug: box-trashed-web-links-api
- description: The direct file upload API supports files up to 50MB in size and sends all the binary data to the Box API in 1 API request.
  name: Box Uploads API
  slug: box-uploads-api
- description: The chunked upload endpoints support files from 20MB in size and allow an application to upload the file in parts, allowing for more control to catch any errors and retry parts individually.
  name: Box Uploads (Chunked) API
  slug: box-uploads-chunked-api
- description: User avatars are JPG or PNG files uploaded to Box to represent the user image. They are then displayed in the user account.
  name: Box User Avatars API
  slug: box-user-avatars-api
- description: Box API supports a variety of users, ranging from real employees logging in with their Managed User account, to applications using App Users to drive powerful automation workflows.
  name: Box Users API
  slug: box-users-api
- description: A watermark is a semi-transparent overlay on an embedded file preview that displays a viewer's email address or user ID and the time of access over the file.
  name: Box Watermarks (Files) API
  slug: box-watermarks-files-api
- description: A watermark is a semi-transparent overlay on an embedded folder preview that displays a viewer's email address or user ID and the time of access over the folder content.
  name: Box Watermarks (Folders) API
  slug: box-watermarks-folders-api
- description: Web links are objects that point to URLs. These objects are also known as bookmarks within the Box web application.
  name: Box Web Links API
  slug: box-web-links-api
- description: Webhooks allow you to monitor Box content for events, and receive notifications to a URL of your choice when they occur. For example, a workflow may include waiting for a file to be downloaded to dele
  name: Box Webhooks API
  slug: box-webhooks-api
- description: Box Relay Workflows are objects that represent a named collection of flows.
  name: Box Workflows API
  slug: box-workflows-api
- description: Zip downloads represent a successful request to create a ZIP archive with files and folders.
  name: Box Zip Downloads API
  slug: box-zip-downloads-api
artifact_total: 319
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/box-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/box-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/box-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/box-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/box
- group: company
  title: ''
  type: Blog
  url: https://medium.com/box-developer-blog
- group: company
  title: ''
  type: BlogRSS
  url: https://medium.com/feed/box-developer-blog
- group: company
  title: ''
  type: Newsletter
  url: https://developer.box.com/newsletter/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.box.com/changelog/
- group: build
  title: ''
  type: Samples
  url: https://github.com/box/samples
- group: operate
  title: ''
  type: Forums
  url: https://support.box.com/hc/en-us/community/topics/360001932973-Platform-and-Developer-Forum
- group: operate
  title: ''
  type: StatusPage
  url: https://status.box.com/
- group: other
  title: ''
  type: Feedback
  url: https://pulse.box.com/forums/909778-product-feedback?category_id=330838
- group: start
  title: ''
  type: Login
  url: https://account.box.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.box.com/pricing
- group: build
  title: ''
  type: Node SDK
  url: https://github.com/box/box-node-sdk
- group: build
  title: ''
  type: Java SDK
  url: https://github.com/box/box-java-sdk
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/box/box-python-sdk
- group: build
  title: ''
  type: .NET SDK
  url: https://github.com/box/box-windows-sdk-v2
- group: build
  title: ''
  type: iOS Content SDK
  url: https://github.com/box/box-ios-sdk
- group: build
  title: ''
  type: CLI
  url: https://github.com/box/boxcli
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.box.com/
- group: operate
  title: ''
  type: Support
  url: https://support.box.com/
- group: operate
  title: ''
  type: Community
  url: https://community.box.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.box.com/legal/termsofservice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.box.com/legal/privacypolicy
- group: start
  title: ''
  type: Signup
  url: https://account.box.com/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/box
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/box
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/box/mcp-server-box-remote
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/box/box-skills-kit-nodejs
created: 2023/11/09
description: Box is a cloud content management and file sharing service for businesses. Box provides a secure platform for storing, managing, and sharing files and content, with features for collaboration, workflow automation, and integration with other business applications.
examples:
- key_count: 6
  name: Box Get Files Idget Shared Link Example
  slug: box-get-files-idget-shared-link-example
- key_count: 6
  name: Box Get Folders Idget Shared Link Example
  slug: box-get-folders-idget-shared-link-example
- key_count: 6
  name: Box Get Web Links Idget Shared Link Example
  slug: box-get-web-links-idget-shared-link-example
- key_count: 6
  name: Box Post Zip Downloads Example
  slug: box-post-zip-downloads-example
- key_count: 6
  name: Box Put Files Idadd Shared Link Example
  slug: box-put-files-idadd-shared-link-example
- key_count: 6
  name: Box Put Files Idremove Shared Link Example
  slug: box-put-files-idremove-shared-link-example
- key_count: 6
  name: Box Put Files Idupdate Shared Link Example
  slug: box-put-files-idupdate-shared-link-example
- key_count: 6
  name: Box Put Folders Idadd Shared Link Example
  slug: box-put-folders-idadd-shared-link-example
- key_count: 6
  name: Box Put Folders Idremove Shared Link Example
  slug: box-put-folders-idremove-shared-link-example
- key_count: 6
  name: Box Put Folders Idupdate Shared Link Example
  slug: box-put-folders-idupdate-shared-link-example
- key_count: 6
  name: Box Put Web Links Idadd Shared Link Example
  slug: box-put-web-links-idadd-shared-link-example
- key_count: 6
  name: Box Put Web Links Idremove Shared Link Example
  slug: box-put-web-links-idremove-shared-link-example
- key_count: 6
  name: Box Put Web Links Idupdate Shared Link Example
  slug: box-put-web-links-idupdate-shared-link-example
features:
- Individual Free with 10 GB and 5 Box Sign requests/mo
- Business at unlimited storage, 50K API calls/mo, integrated Box AI
- Business Plus with unlimited external collaborators
- Enterprise with 1K AI Units/mo, 100K API calls, FedRAMP/HIPAA
- Enterprise Plus with 2K AI Units, 24-hr enhanced support
- Enterprise Advanced (35-user min) with 20K AI Units, 200K API calls, Box Agent
- REST API for files, folders, users, collaborations, metadata
- Box Sign API for e-signatures
- Box AI API for content Q&A and generation
- Per-user 1,000 req/min cap
- 100 concurrent upload sessions
- Webhooks v2 for content events
- OAuth 2.0, JWT app auth, CCG (Client Credentials Grant)
- Box Skills for AI-powered metadata extraction
- Box Relay for workflow automation
- 1,500+ integrations on Business+
finops:
- name: Box Finops
  service_category: Content Cloud
  slug: box-finops
graphqls:
- description: This directory contains a conceptual GraphQL schema for the Box cloud content management platform. Box exposes a REST API (v2) at `https://api.box.com/2.0`. The schema in `box-schema.graphql` translat
  name: Box GraphQL Schema
  slug: box-graphql
image: https://www.box.com/themes/custom/box/logo.svg
json_schemas:
- name: Access token
  property_count: 6
  slug: box-accesstoken
- name: Classification
  property_count: 8
  slug: box-classification
- name: Classification Template
  property_count: 8
  slug: box-classificationtemplate
- name: Client error
  property_count: 7
  slug: box-clienterror
- name: Collaboration
  property_count: 14
  slug: box-collaboration
- name: Allowed collaboration domains
  property_count: 0
  slug: box-collaborationallowlistentries
- name: Allowed collaboration domain
  property_count: 6
  slug: box-collaborationallowlistentry
- name: Allowed collaboration domains user exemption
  property_count: 6
  slug: box-collaborationallowlistexempttarget
- name: Allowed collaboration domains user exemptions
  property_count: 0
  slug: box-collaborationallowlistexempttargets
- name: Collaborations
  property_count: 0
  slug: box-collaborations
- name: Collection
  property_count: 4
  slug: box-collection
- name: Collections
  property_count: 0
  slug: box-collections
- name: Comment (Base)
  property_count: 2
  slug: box-comment-base
- name: Comment (Full)
  property_count: 0
  slug: box-comment-full
- name: Comment
  property_count: 0
  slug: box-comment
- name: Comments
  property_count: 0
  slug: box-comments
- name: Conflict error
  property_count: 0
  slug: box-conflicterror
- name: Device pinner
  property_count: 4
  slug: box-devicepinner
- name: Device pinners
  property_count: 4
  slug: box-devicepinners
- name: Email alias
  property_count: 4
  slug: box-emailalias
- name: Email aliases
  property_count: 2
  slug: box-emailaliases
- name: Enterprise (Base)
  property_count: 2
  slug: box-enterprise-base
- name: Event
  property_count: 9
  slug: box-event
- name: Events
  property_count: 3
  slug: box-events
- name: Event source
  property_count: 6
  slug: box-eventsource
- name: File (Base)
  property_count: 3
  slug: box-file-base
- name: File (Full)
  property_count: 0
  slug: box-file-full
- name: File (Mini)
  property_count: 0
  slug: box-file-mini
- name: File
  property_count: 0
  slug: box-file
- name: File (Conflict)
  property_count: 0
  slug: box-fileconflict
- name: File or folder scope
  property_count: 2
  slug: box-fileorfolderscope
- name: File Request
  property_count: 15
  slug: box-filerequest
- name: File Request (Copy)
  property_count: 0
  slug: box-filerequestcopyrequest
- name: File Request (Update)
  property_count: 6
  slug: box-filerequestupdaterequest
- name: Files
  property_count: 2
  slug: box-files
- name: Files under retention
  property_count: 0
  slug: box-filesunderretention
- name: File version (Base)
  property_count: 2
  slug: box-fileversion-base
- name: File version (Full)
  property_count: 0
  slug: box-fileversion-full
- name: File version (Mini)
  property_count: 0
  slug: box-fileversion-mini
- name: File version
  property_count: 0
  slug: box-fileversion
- name: File version legal hold
  property_count: 6
  slug: box-fileversionlegalhold
- name: File version legal holds
  property_count: 0
  slug: box-fileversionlegalholds
- name: File version retention
  property_count: 7
  slug: box-fileversionretention
- name: File version retentions
  property_count: 0
  slug: box-fileversionretentions
- name: File versions
  property_count: 0
  slug: box-fileversions
- name: Folder (Base)
  property_count: 3
  slug: box-folder-base
- name: Folder (Full)
  property_count: 0
  slug: box-folder-full
- name: Folder (Mini)
  property_count: 0
  slug: box-folder-mini
- name: Folder
  property_count: 0
  slug: box-folder
- name: Folder Lock
  property_count: 7
  slug: box-folderlock
- name: Folder Locks
  property_count: 3
  slug: box-folderlocks
- name: Generic source
  property_count: 0
  slug: box-genericsource
- name: Group (Base)
  property_count: 2
  slug: box-group-base
- name: Group (Full)
  property_count: 0
  slug: box-group-full
- name: Group (Mini)
  property_count: 0
  slug: box-group-mini
- name: Group
  property_count: 0
  slug: box-group
- name: Group membership
  property_count: 7
  slug: box-groupmembership
- name: Group memberships
  property_count: 0
  slug: box-groupmemberships
- name: Groups
  property_count: 0
  slug: box-groups
- name: Integration mapping (Base)
  property_count: 2
  slug: box-integrationmapping-base
- name: Integration mapping (Mini)
  property_count: 0
  slug: box-integrationmapping-mini
- name: Integration mapping
  property_count: 0
  slug: box-integrationmapping
- name: Integration mapping Box item schema for type Slack
  property_count: 2
  slug: box-integrationmappingboxitemslack
- name: Integration mapping mapped item schema for type Slack
  property_count: 4
  slug: box-integrationmappingpartneritemslack
- name: Integration mappings
  property_count: 0
  slug: box-integrationmappings
- name: Create integration mapping request
  property_count: 3
  slug: box-integrationmappingslackcreaterequest
- name: Integration mapping options for type Slack
  property_count: 1
  slug: box-integrationmappingslackoptions
- name: Invite
  property_count: 8
  slug: box-invite
- name: Items
  property_count: 0
  slug: box-items
- name: Keyword Skill Card
  property_count: 7
  slug: box-keywordskillcard
- name: Legal hold policies
  property_count: 0
  slug: box-legalholdpolicies
- name: Legal hold policy (Mini)
  property_count: 2
  slug: box-legalholdpolicy-mini
- name: Legal hold policy
  property_count: 0
  slug: box-legalholdpolicy
- name: Legal hold policy assignment (Base)
  property_count: 2
  slug: box-legalholdpolicyassignment-base
- name: Legal hold policy assignment
  property_count: 0
  slug: box-legalholdpolicyassignment
- name: Legal hold policy assignments
  property_count: 0
  slug: box-legalholdpolicyassignments
- name: Metadata instance (Base)
  property_count: 4
  slug: box-metadata-base
- name: Metadata instance (Full)
  property_count: 0
  slug: box-metadata-full
- name: Metadata instance
  property_count: 0
  slug: box-metadata
- name: Metadata cascade policies
  property_count: 0
  slug: box-metadatacascadepolicies
- name: Metadata cascade policy
  property_count: 6
  slug: box-metadatacascadepolicy
- name: Metadata field filter (date range)
  property_count: 0
  slug: box-metadatafieldfilterdaterange
- name: Metadata field filter (float)
  property_count: 0
  slug: box-metadatafieldfilterfloat
- name: Metadata field filter (float range)
  property_count: 0
  slug: box-metadatafieldfilterfloatrange
- name: Metadata field filter (multi-select)
  property_count: 0
  slug: box-metadatafieldfiltermultiselect
- name: Metadata field filter (string)
  property_count: 0
  slug: box-metadatafieldfilterstring
- name: Metadata filter
  property_count: 3
  slug: box-metadatafilter
- name: Metadata query search request
  property_count: 8
  slug: box-metadataquery
- name: Metadata query index
  property_count: 4
  slug: box-metadataqueryindex
- name: Metadata query search results
  property_count: 3
  slug: box-metadataqueryresults
- name: Metadata instances
  property_count: 2
  slug: box-metadatas
- name: Metadata template
  property_count: 8
  slug: box-metadatatemplate
- name: Metadata templates
  property_count: 0
  slug: box-metadatatemplates
- name: OAuth 2.0 error
  property_count: 2
  slug: box-oauth2error
- name: Token revocation request
  property_count: 3
  slug: box-postoauth2revoke
- name: Refresh access token
  property_count: 4
  slug: box-postoauth2token-refreshaccesstoken
- name: Token request
  property_count: 15
  slug: box-postoauth2token
- name: Real-time server
  property_count: 5
  slug: box-realtimeserver
- name: Real-time servers
  property_count: 2
  slug: box-realtimeservers
- name: Recent item
  property_count: 5
  slug: box-recentitem
- name: Recent items
  property_count: 0
  slug: box-recentitems
- name: Retention policies
  property_count: 0
  slug: box-retentionpolicies
- name: Retention policy (Base)
  property_count: 2
  slug: box-retentionpolicy-base
- name: Retention policy (Mini)
  property_count: 0
  slug: box-retentionpolicy-mini
- name: Retention policy
  property_count: 0
  slug: box-retentionpolicy
- name: Retention policy assignment (Base)
  property_count: 2
  slug: box-retentionpolicyassignment-base
- name: Retention policy assignment
  property_count: 8
  slug: box-retentionpolicyassignment
- name: Retention policy assignments
  property_count: 0
  slug: box-retentionpolicyassignments
- name: Search Results
  property_count: 0
  slug: box-searchresults
- name: Search Results (including Shared Links)
  property_count: 0
  slug: box-searchresultswithsharedlinks
- name: Search Result (including Shared Link)
  property_count: 3
  slug: box-searchresultwithsharedlink
- name: Session termination message
  property_count: 1
  slug: box-sessionterminationmessage
- name: Shield information barrier (Base)
  property_count: 2
  slug: box-shieldinformationbarrier-base
- name: Shield information barrier
  property_count: 10
  slug: box-shieldinformationbarrier
- name: Shield information barrier reference
  property_count: 1
  slug: box-shieldinformationbarrierreference
- name: Shield information barrier report (Base)
  property_count: 2
  slug: box-shieldinformationbarrierreport-base
- name: Shield information barrier report
  property_count: 0
  slug: box-shieldinformationbarrierreport
- name: Shield information barrier report details
  property_count: 1
  slug: box-shieldinformationbarrierreportdetails
- name: List of Shield Information Barrier Reports
  property_count: 0
  slug: box-shieldinformationbarrierreports
- name: List of Shield Information Barriers
  property_count: 0
  slug: box-shieldinformationbarriers
- name: Shield information barrier segment
  property_count: 9
  slug: box-shieldinformationbarriersegment
- name: Shield information barrier segment member (Base)
  property_count: 2
  slug: box-shieldinformationbarriersegmentmember-base
- name: Shield information barrier segment member (Mini)
  property_count: 0
  slug: box-shieldinformationbarriersegmentmember-mini
- name: Shield information barrier segment member
  property_count: 0
  slug: box-shieldinformationbarriersegmentmember
- name: List of Shield Information Barrier Segment Members
  property_count: 0
  slug: box-shieldinformationbarriersegmentmembers
- name: Shield information barrier segment restriction (Base)
  property_count: 2
  slug: box-shieldinformationbarriersegmentrestriction-base
- name: Shield information barrier segment restriction (Mini)
  property_count: 0
  slug: box-shieldinformationbarriersegmentrestriction-mini
- name: Shield information barrier segment restriction
  property_count: 0
  slug: box-shieldinformationbarriersegmentrestriction
- name: List of Shield Information Barrier Segment Restrictions
  property_count: 0
  slug: box-shieldinformationbarriersegmentrestrictions
- name: List of Shield Information Barrier Segments
  property_count: 0
  slug: box-shieldinformationbarriersegments
- name: Sign Request (Base)
  property_count: 13
  slug: box-signrequest-base
- name: Sign Request
  property_count: 0
  slug: box-signrequest
- name: Create a sign request
  property_count: 0
  slug: box-signrequestcreaterequest
- name: Signer fields for Create Sign Request
  property_count: 11
  slug: box-signrequestcreatesigner
- name: Sign Request Prefill Tag
  property_count: 4
  slug: box-signrequestprefilltag
- name: Box Sign
  property_count: 0
  slug: box-signrequests
- name: Signer fields for GET Sign Request response
  property_count: 0
  slug: box-signrequestsigner
- name: Sign Request Signer Input
  property_count: 0
  slug: box-signrequestsignerinput
- name: Box Sign template
  property_count: 0
  slug: box-signtemplate
- name: Box Sign templates
  property_count: 0
  slug: box-signtemplates
- name: Skills metadata instance
  property_count: 9
  slug: box-skillcardsmetadata
- name: Skill webhook payload
  property_count: 10
  slug: box-skillinvocation
- name: Status Skill Card
  property_count: 7
  slug: box-statusskillcard
- name: Storage policies
  property_count: 0
  slug: box-storagepolicies
- name: Storage policy (Mini)
  property_count: 2
  slug: box-storagepolicy-mini
- name: Storage policy
  property_count: 0
  slug: box-storagepolicy
- name: Storage policy assignment
  property_count: 4
  slug: box-storagepolicyassignment
- name: Storage policy assignments
  property_count: 0
  slug: box-storagepolicyassignments
- name: Task
  property_count: 11
  slug: box-task
- name: Task assignment
  property_count: 10
  slug: box-taskassignment
- name: Task assignments
  property_count: 2
  slug: box-taskassignments
- name: Tasks
  property_count: 2
  slug: box-tasks
- name: Signer fields for Templates
  property_count: 0
  slug: box-templatesigner
- name: Template Signer Input
  property_count: 0
  slug: box-templatesignerinput
- name: Terms of service (Base)
  property_count: 2
  slug: box-termsofservice-base
- name: Terms of service
  property_count: 0
  slug: box-termsofservice
- name: Terms of services
  property_count: 2
  slug: box-termsofservices
- name: Terms of service user status
  property_count: 7
  slug: box-termsofserviceuserstatus
- name: Terms of service user statuses
  property_count: 2
  slug: box-termsofserviceuserstatuses
- name: Timeline Skill Card
  property_count: 8
  slug: box-timelineskillcard
- name: Tracking code
  property_count: 3
  slug: box-trackingcode
- name: Transcript Skill Card
  property_count: 8
  slug: box-transcriptskillcard
- name: Trashed File
  property_count: 22
  slug: box-trashfile
- name: Trashed File (Restored)
  property_count: 22
  slug: box-trashfilerestored
- name: Trashed Folder
  property_count: 21
  slug: box-trashfolder
- name: Trashed Folder (Restored)
  property_count: 21
  slug: box-trashfolderrestored
- name: Trashed Web Link
  property_count: 18
  slug: box-trashweblink
- name: Trashed Web Link (Restored)
  property_count: 18
  slug: box-trashweblinkrestored
- name: Uploaded part
  property_count: 1
  slug: box-uploadedpart
- name: Upload part (Mini)
  property_count: 3
  slug: box-uploadpart-mini
- name: Upload part
  property_count: 0
  slug: box-uploadpart
- name: Upload parts
  property_count: 0
  slug: box-uploadparts
- name: Upload session
  property_count: 7
  slug: box-uploadsession
- name: Upload URL
  property_count: 2
  slug: box-uploadurl
- name: User (Base)
  property_count: 2
  slug: box-user-base
- name: User (Collaborations)
  property_count: 0
  slug: box-user-collaborations
- name: User (Full)
  property_count: 0
  slug: box-user-full
- name: User (Mini)
  property_count: 0
  slug: box-user-mini
- name: User
  property_count: 0
  slug: box-user
- name: User avatar
  property_count: 1
  slug: box-useravatar
- name: User (Integration Mappings)
  property_count: 0
  slug: box-userintegrationmappings
- name: Users
  property_count: 0
  slug: box-users
- name: Watermark
  property_count: 1
  slug: box-watermark
- name: Webhook (Mini)
  property_count: 3
  slug: box-webhook-mini
- name: Webhook
  property_count: 0
  slug: box-webhook
- name: Webhook (V2) payload
  property_count: 7
  slug: box-webhookinvocation
- name: Webhooks
  property_count: 0
  slug: box-webhooks
- name: Web link (Base)
  property_count: 3
  slug: box-weblink-base
- name: Web link (Mini)
  property_count: 0
  slug: box-weblink-mini
- name: Web link
  property_count: 0
  slug: box-weblink
- name: Workflow (Full)
  property_count: 0
  slug: box-workflow-full
- name: Workflow (Mini)
  property_count: 5
  slug: box-workflow-mini
- name: Workflow
  property_count: 0
  slug: box-workflow
- name: Workflows
  property_count: 0
  slug: box-workflows
- name: Zip download
  property_count: 4
  slug: box-zipdownload
- name: Create a `zip` archive
  property_count: 2
  slug: box-zipdownloadrequest
- name: Zip download status
  property_count: 5
  slug: box-zipdownloadstatus
json_structures:
- name: Box Structure
  property_count: 0
  slug: box-structure
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Box
nav: Providers
network: true
overview: 'Box publishes 81 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Authorize API, Classifications API, and 78 more. Tagged areas include Cloud Storage, Collaboration, Content Management, Documents, and Enterprise.


  The Box catalog on APIs.io includes 2 Spectral governance rulesets.


  Box''s developer surface includes authentication, engineering blog, changelog, pricing, CLI, support, signup flow, and 24 more developer resources.'
plans:
- name: Box Plans Pricing
  plan_count: 8
  slug: box-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 5
  name: Box Rate Limits
  slug: box-rate-limits
rules:
- name: Box API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: box-jsonschema-spectral-rules
- name: Box API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 9
  slug: box-spectral-rules
scopes:
- name: Box Scopes
  scope_count: 9
  slug: box-scopes
  summary_line: 9 scopes · authorizationCode
score:
  band: strong
  composite: 66.7
  delta: 0.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 49.8
    developer_ergonomics: 52.2
    discoverability: 92.5
    governance: 73.7
    operational_transparency: 68.4
  previous_composite: 66.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/box/refs/heads/main/screenshots/box-2026-06-20T173623.png
security:
- kind: authentication
  name: Box Authentication
  slug: box-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Box Domain Security
  slug: box-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: box
tags:
- Cloud Storage
- Collaboration
- Content Management
- Documents
- Enterprise
- File Sharing
website: https://developer.box.com/
---
