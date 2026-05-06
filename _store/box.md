---
aid: box
url: https://raw.githubusercontent.com/apis-json/artisanal/main/apis/box.yml
apis:
  - aid: box:box-authorize-api
    name: Box Authorize API
    tags:
      - Authentication
      - Authorization
      - OAuth
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://account.box.com/api/oauth2
    humanURL: https://developer.box.com/reference/get-authorize
    properties:
      - url: https://developer.box.com/reference/get-authorize
        type: Documentation
      - url: openapi/authorize-openapi-original.yml
        type: OpenAPI
    description: The Box Authorize API initiates the OAuth 2.0 authorization flow by redirecting users to the Box website to grant permission for applications to act on their behalf, providing the first step in authenticating users with Box.
  - aid: box:box-oauth2-api
    name: Box Oauth2 API
    tags:
      - Authentication
      - OAuth
      - Tokens
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/oauth2
    humanURL: https://developer.box.com/reference/post-oauth2-token
    properties:
      - url: https://developer.box.com/reference/post-oauth2-token
        type: Documentation
      - url: openapi/oauth2-openapi-original.yml
        type: OpenAPI
    description: The Box OAuth2 API manages OAuth 2.0 access tokens, allowing applications to request, refresh, and revoke tokens used for authenticating API calls to the Box Platform.
  - aid: box:box-files-api
    name: Box Files API
    tags:
      - Content
      - Documents
      - Files
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-files-id-copy
    properties:
      - url: https://developer.box.com/reference/post-files-id-copy
        type: Documentation
      - url: openapi/files-openapi-original.yml
        type: OpenAPI
    description: The Box Files API provides endpoints for managing files stored in Box, including copying, getting file information, updating file details, deleting files, and managing file metadata such as thumbnails, collaborations, comments, and tasks.
  - aid: box:box-file-requests-api
    name: Box File Requests API
    tags:
      - Files
      - Requests
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-file-requests-id-copy
    properties:
      - url: https://developer.box.com/reference/post-file-requests-id-copy
        type: Documentation
      - url: openapi/file-requests-openapi-original.yml
        type: OpenAPI
    description: The Box File Requests API allows users to create, retrieve, update, and delete file requests, which enable external users to upload files to a specific Box folder through a personalized URL.
  - aid: box:box-folders-api
    name: Box Folders API
    tags:
      - Content
      - Directories
      - Folders
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-folders-id-copy
    properties:
      - url: https://developer.box.com/reference/post-folders-id-copy
        type: Documentation
      - url: openapi/folders-openapi-original.yml
        type: OpenAPI
    description: The Box Folders API provides endpoints for managing folders in Box, including creating, copying, listing items, getting folder information, updating, and deleting folders, as well as managing folder collaborations and metadata.
  - aid: box:box-folder-locks-api
    name: Box Folder Locks API
    tags:
      - Folders
      - Locks
      - Security
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-folder-locks
    properties:
      - url: https://developer.box.com/reference/post-folder-locks
        type: Documentation
      - url: openapi/folder-locks-openapi-original.yml
        type: OpenAPI
    description: The Box Folder Locks API provides endpoints for creating, listing, and deleting folder locks, which prevent folders from being moved or deleted by users other than the lock creator.
  - aid: box:box-metadata-templates-api
    name: Box Metadata Templates API
    tags:
      - Metadata
      - Schemas
      - Templates
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-metadata-templates-schema
    properties:
      - url: https://developer.box.com/reference/post-metadata-templates-schema
        type: Documentation
      - url: openapi/metadata-templates-openapi-original.yml
        type: OpenAPI
    description: The Box Metadata Templates API allows creation and management of metadata templates that define the structure and fields of metadata that can be applied to files and folders in Box for custom categorization and organization.
  - aid: box:box-metadata-cascade-policies-api
    name: Box Metadata Cascade Policies API
    tags:
      - Cascade
      - Metadata
      - Policies
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-metadata-cascade-policies
    properties:
      - url: https://developer.box.com/reference/post-metadata-cascade-policies
        type: Documentation
      - url: openapi/metadata-cascade-policies-openapi-original.yml
        type: OpenAPI
    description: The Box Metadata Cascade Policies API allows configuration of policies that automatically apply metadata templates from a parent folder to all files and subfolders within it, ensuring consistent metadata across content hierarchies.
  - aid: box:box-metadata-queries-api
    name: Box Metadata Queries API
    tags:
      - Metadata
      - Queries
      - Search
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-metadata-queries-execute-read
    properties:
      - url: https://developer.box.com/reference/post-metadata-queries-execute-read
        type: Documentation
      - url: openapi/metadata-queries-openapi-original.yml
        type: OpenAPI
    description: The Box Metadata Queries API enables executing structured queries against metadata applied to files and folders, allowing applications to search for and filter content based on custom metadata field values.
  - aid: box:box-comments-api
    name: Box Comments API
    tags:
      - Collaboration
      - Comments
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-comments
    properties:
      - url: https://developer.box.com/reference/post-comments
        type: Documentation
      - url: openapi/comments-openapi-original.yml
        type: OpenAPI
    description: The Box Comments API provides endpoints for creating, retrieving, updating, and deleting comments on files, enabling users to have threaded discussions and collaborate on content stored in Box.
  - aid: box:box-collaborations-api
    name: Box Collaborations API
    tags:
      - Collaborations
      - Permissions
      - Sharing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-collaborations
    properties:
      - url: https://developer.box.com/reference/post-collaborations
        type: Documentation
      - url: openapi/collaborations-openapi-original.yml
        type: OpenAPI
    description: The Box Collaborations API manages sharing permissions for files and folders, allowing applications to invite users, set access levels, accept or reject collaboration invitations, and list existing collaborations.
  - aid: box:box-search-api
    name: Box Search API
    tags:
      - Content Discovery
      - Search
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-metadata-queries-execute-read
    properties:
      - url: https://developer.box.com/reference/post-metadata-queries-execute-read
        type: Documentation
      - url: openapi/search-openapi-original.yml
        type: OpenAPI
    description: The Box Search API enables full-text search across content stored in Box, supporting keyword queries, metadata-based filtering, content type restrictions, date range filters, and other advanced search parameters.
  - aid: box:box-tasks-api
    name: Box Tasks API
    tags:
      - Tasks
      - Workflow
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-tasks
    properties:
      - url: https://developer.box.com/reference/post-tasks
        type: Documentation
      - url: openapi/tasks-openapi-original.yml
        type: OpenAPI
    description: The Box Tasks API allows creation and management of tasks on files, enabling assignment of review or approval workflows to content stored in Box.
  - aid: box:box-task-assignments-api
    name: Box Task Assignments API
    tags:
      - Assignments
      - Tasks
      - Workflow
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-task-assignments
    properties:
      - url: https://developer.box.com/reference/post-task-assignments
        type: Documentation
      - url: openapi/task-assignments-openapi-original.yml
        type: OpenAPI
    description: The Box Task Assignments API manages the assignment of tasks to specific users, including creating, retrieving, updating, and deleting task assignments for file review and approval workflows.
  - aid: box:box-shared-items-api
    name: Box Shared Items API
    tags:
      - Shared Links
      - Sharing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/put-files-id--add-shared-link
    properties:
      - url: https://developer.box.com/reference/put-files-id--add-shared-link
        type: Documentation
      - url: openapi/shared-items-openapi-original.yml
        type: OpenAPI
    description: The Box Shared Items API allows retrieval of file information for items accessed through shared links, enabling applications to resolve shared link URLs to their underlying file objects.
  - aid: box:box-shared-itemsfolders-api
    name: Box Shared Items#folders API
    tags:
      - Folders
      - Shared Links
      - Sharing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/put-folders-id--add-shared-link
    properties:
      - url: https://developer.box.com/reference/put-folders-id--add-shared-link
        type: Documentation
      - url: openapi/shared-itemsfolders-openapi-original.yml
        type: OpenAPI
    description: The Box Shared Items Folders API manages shared links for folders, allowing applications to create, update, retrieve, and remove shared links that provide external access to folder content.
  - aid: box:box-web-links-api
    name: Box Web Links API
    tags:
      - Bookmarks
      - Web Links
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-web-links
    properties:
      - url: https://developer.box.com/reference/post-web-links
        type: Documentation
      - url: openapi/web-links-openapi-original.yml
        type: OpenAPI
    description: The Box Web Links API manages web link (bookmark) objects in Box, allowing applications to create, retrieve, update, and delete URL bookmarks stored alongside files and folders.
  - aid: box:box-shared-itemsweb-links-api
    name: Box Shared Items#web Links API
    tags:
      - Shared Links
      - Sharing
      - Web Links
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/put-web-links-id--add-shared-link
    properties:
      - url: https://developer.box.com/reference/put-web-links-id--add-shared-link
        type: Documentation
      - url: openapi/shared-itemsweb-links-openapi-original.yml
        type: OpenAPI
    description: The Box Shared Items Web Links API manages shared links for web link objects, enabling applications to create, update, retrieve, and remove shared links that provide external access to bookmarked URLs.
  - aid: box:box-users-api
    name: Box Users API
    tags:
      - Accounts
      - Administration
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-users
    properties:
      - url: https://developer.box.com/reference/post-users
        type: Documentation
      - url: openapi/users-openapi-original.yml
        type: OpenAPI
    description: The Box Users API provides endpoints for creating, retrieving, updating, and deleting user accounts, including managed users and app users, as well as listing enterprise users and managing user settings.
  - aid: box:box-invites-api
    name: Box Invites API
    tags:
      - Invites
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-invites
    properties:
      - url: https://developer.box.com/reference/post-invites
        type: Documentation
      - url: openapi/invites-openapi-original.yml
        type: OpenAPI
    description: The Box Invites API allows inviting existing Box users to join an enterprise, managing the process of adding users to organizational accounts.
  - aid: box:box-groups-api
    name: Box Groups API
    tags:
      - Administration
      - Groups
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-groups
    properties:
      - url: https://developer.box.com/reference/post-groups
        type: Documentation
      - url: openapi/groups-openapi-original.yml
        type: OpenAPI
    description: The Box Groups API provides endpoints for creating, listing, retrieving, updating, and deleting groups within an enterprise, enabling organized management of user permissions and collaboration access.
  - aid: box:box-group-memberships-api
    name: Box Group Memberships API
    tags:
      - Groups
      - Memberships
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-group-memberships
    properties:
      - url: https://developer.box.com/reference/post-group-memberships
        type: Documentation
      - url: openapi/group-memberships-openapi-original.yml
        type: OpenAPI
    description: The Box Group Memberships API manages the relationship between users and groups, allowing applications to add users to groups, retrieve membership details, update roles, and remove members.
  - aid: box:box-webhooks-api
    name: Box Webhooks API
    tags:
      - Events
      - Notifications
      - Webhooks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-webhooks
    properties:
      - url: https://developer.box.com/reference/post-webhooks
        type: Documentation
      - url: openapi/webhooks-openapi-original.yml
        type: OpenAPI
    description: The Box Webhooks API enables applications to receive real-time notifications when events occur on files and folders in Box, such as uploads, downloads, comments, and collaboration changes.
  - aid: box:box-skill-invocations-api
    name: Box Skill Invocations API
    tags:
      - AI
      - Machine Learning
      - Skills
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-files-id-metadata-global-boxSkillsCards
    properties:
      - url: https://developer.box.com/reference/post-files-id-metadata-global-boxSkillsCards
        type: Documentation
      - url: openapi/skill-invocations-openapi-original.yml
        type: OpenAPI
    description: The Box Skill Invocations API manages Box Skills, which are custom applications that perform machine learning analysis on files uploaded to Box, applying metadata cards with extracted insights such as transcripts, topics, and key phrases.
  - aid: box:box-events-api
    name: Box Events API
    tags:
      - Activity
      - Audit
      - Events
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/options-events
    properties:
      - url: https://developer.box.com/reference/options-events
        type: Documentation
      - url: openapi/events-openapi-original.yml
        type: OpenAPI
    description: The Box Events API provides access to user and enterprise event streams, enabling applications to monitor file activity, track audit logs, and receive real-time notifications about actions taken on content in Box.
  - aid: box:box-collections-api
    name: Box Collections API
    tags:
      - Collections
      - Favorites
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/get-collections-id
    properties:
      - url: https://developer.box.com/reference/get-collections-id
        type: Documentation
      - url: openapi/collections-openapi-original.yml
        type: OpenAPI
    description: The Box Collections API manages collections such as Favorites, allowing applications to list available collections and retrieve the items within them for organizing frequently accessed content.
  - aid: box:box-recent-items-api
    name: Box Recent Items API
    tags:
      - Activity
      - Recent Items
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/get-recent-items
    properties:
      - url: https://developer.box.com/reference/get-recent-items
        type: Documentation
      - url: openapi/recent-items-openapi-original.yml
        type: OpenAPI
    description: The Box Recent Items API returns a list of files and folders that have been recently accessed by the authenticated user, enabling quick access to frequently used content.
  - aid: box:box-retention-policies-api
    name: Box Retention Policies API
    tags:
      - Governance
      - Policies
      - Retention
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-retention-policies
    properties:
      - url: https://developer.box.com/reference/post-retention-policies
        type: Documentation
      - url: openapi/retention-policies-openapi-original.yml
        type: OpenAPI
    description: The Box Retention Policies API allows creating and managing retention policies that enforce how long content must be kept in Box before it can be deleted, supporting regulatory compliance and information governance requirements.
  - aid: box:box-retention-policy-assignments-api
    name: Box Retention Policy Assignments API
    tags:
      - Assignments
      - Governance
      - Retention
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-retention-policy-assignments
    properties:
      - url: https://developer.box.com/reference/post-retention-policy-assignments
        type: Documentation
      - url: openapi/retention-policy-assignments-openapi-original.yml
        type: OpenAPI
    description: The Box Retention Policy Assignments API manages the application of retention policies to specific folders, enterprises, or metadata templates, controlling which content is subject to retention rules.
  - aid: box:box-legal-hold-policies-api
    name: Box Legal Hold Policies API
    tags:
      - Compliance
      - Legal Hold
      - Policies
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-legal-hold-policies
    properties:
      - url: https://developer.box.com/reference/post-legal-hold-policies
        type: Documentation
      - url: openapi/legal-hold-policies-openapi-original.yml
        type: OpenAPI
    description: The Box Legal Hold Policies API enables creating and managing legal hold policies that prevent content from being modified or deleted during legal proceedings, supporting e-discovery and litigation hold requirements.
  - aid: box:box-legal-hold-policy-assignments-api
    name: Box Legal Hold Policy Assignments API
    tags:
      - Assignments
      - Compliance
      - Legal Hold
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-legal-hold-policy-assignments
    properties:
      - url: https://developer.box.com/reference/post-legal-hold-policy-assignments
        type: Documentation
      - url: openapi/legal-hold-policy-assignments-openapi-original.yml
        type: OpenAPI
    description: The Box Legal Hold Policy Assignments API manages the assignment of legal hold policies to specific users, folders, or files, controlling which content is preserved under legal hold.
  - aid: box:box-file-version-retentions-api
    name: Box File Version Retentions API
    tags:
      - File Versions
      - Governance
      - Retention
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/get-file-version-retentions-id
    properties:
      - url: https://developer.box.com/reference/get-file-version-retentions-id
        type: Documentation
      - url: openapi/file-version-retentions-openapi-original.yml
        type: OpenAPI
    description: The Box File Version Retentions API provides information about file versions that are under retention, allowing applications to list and retrieve details about retained file versions and their associated policies.
  - aid: box:box-file-version-legal-holds-api
    name: Box File Version Legal Holds API
    tags:
      - Compliance
      - File Versions
      - Legal Hold
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/get-file-version-legal-holds-id
    properties:
      - url: https://developer.box.com/reference/get-file-version-legal-holds-id
        type: Documentation
      - url: openapi/file-version-legal-holds-openapi-original.yml
        type: OpenAPI
    description: The Box File Version Legal Holds API provides information about file versions currently under legal hold, enabling applications to list and retrieve details about held file versions and their associated legal hold policies.
  - aid: box:box-shield-information-barriers-api
    name: Box Shield Information Barriers API
    tags:
      - Information Barriers
      - Security
      - Shield
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-shield-information-barriers-change-status
    properties:
      - url: https://developer.box.com/reference/post-shield-information-barriers-change-status
        type: Documentation
      - url: openapi/shield-information-barriers-openapi-original.yml
        type: OpenAPI
    description: The Box Shield Information Barriers API creates and manages information barriers that prevent communication and collaboration between specific groups of users within an enterprise, supporting regulatory compliance for financial services and other regulated industries.
  - aid: box:box-shield-information-barrier-reports-api
    name: Box Shield Information Barrier Reports API
    tags:
      - Reports
      - Security
      - Shield
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-shield-information-barrier-reports
    properties:
      - url: https://developer.box.com/reference/post-shield-information-barrier-reports
        type: Documentation
      - url: openapi/shield-information-barrier-reports-openapi-original.yml
        type: OpenAPI
    description: The Box Shield Information Barrier Reports API generates and retrieves reports about information barrier configurations and violations, providing visibility into barrier effectiveness and compliance status.
  - aid: box:box-shield-information-barrier-segments-api
    name: Box Shield Information Barrier Segments API
    tags:
      - Security
      - Segments
      - Shield
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-shield-information-barrier-segments
    properties:
      - url: https://developer.box.com/reference/post-shield-information-barrier-segments
        type: Documentation
      - url: openapi/shield-information-barrier-segments-openapi-original.yml
        type: OpenAPI
    description: The Box Shield Information Barrier Segments API manages the user segments that define the boundaries of information barriers, allowing creation, retrieval, updating, and deletion of segments used in barrier policies.
  - aid: box:box-shield-information-barrier-segment-members-api
    name: Box Shield Information Barrier Segment Members API
    tags:
      - Members
      - Security
      - Segments
      - Shield
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-shield-information-barrier-segment-members
    properties:
      - url: https://developer.box.com/reference/post-shield-information-barrier-segment-members
        type: Documentation
      - url: openapi/shield-information-barrier-segment-members-openapi-original.yml
        type: OpenAPI
    description: The Box Shield Information Barrier Segment Members API manages the users assigned to information barrier segments, controlling which users belong to each restricted group within an information barrier configuration.
  - aid: box:box-shield-information-barrier-segment-restrictions-api
    name: Box Shield Information Barrier Segment Restrictions API
    tags:
      - Restrictions
      - Security
      - Shield
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-shield-information-barrier-segment-restrictions
    properties:
      - url: https://developer.box.com/reference/post-shield-information-barrier-segment-restrictions
        type: Documentation
      - url: openapi/shield-information-barrier-segment-restrictions-openapi-original.yml
        type: OpenAPI
    description: The Box Shield Information Barrier Segment Restrictions API defines the restriction rules between information barrier segments, specifying which pairs of segments are prevented from collaborating with each other.
  - aid: box:box-device-pinners-api
    name: Box Device Pinners API
    tags:
      - Devices
      - Pinning
      - Security
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/get-device-pinners-id
    properties:
      - url: https://developer.box.com/reference/get-device-pinners-id
        type: Documentation
      - url: openapi/device-pinners-openapi-original.yml
        type: OpenAPI
    description: The Box Device Pinners API manages device pinning for enterprise accounts, allowing administrators to view and remove pinned devices that users have associated with their Box accounts for enhanced security.
  - aid: box:box-enterprises-api
    name: Box Enterprises API
    tags:
      - Administration
      - Enterprises
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-users
    properties:
      - url: https://developer.box.com/reference/post-users
        type: Documentation
      - url: openapi/enterprises-openapi-original.yml
        type: OpenAPI
    description: The Box Enterprises API provides administrative endpoints for managing enterprise-level settings and configurations, including enterprise user management and organizational controls.
  - aid: box:box-terms-of-services-api
    name: Box Terms Of Services API
    tags:
      - Compliance
      - Terms of Service
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-terms-of-services
    properties:
      - url: https://developer.box.com/reference/post-terms-of-services
        type: Documentation
      - url: openapi/terms-of-services-openapi-original.yml
        type: OpenAPI
    description: The Box Terms of Services API enables creation and management of custom terms of service agreements that users must accept before accessing content in an enterprise Box account.
  - aid: box:box-terms-of-service-user-statuses-api
    name: Box Terms Of Service User Statuses API
    tags:
      - Compliance
      - Terms of Service
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-terms-of-service-user-statuses
    properties:
      - url: https://developer.box.com/reference/post-terms-of-service-user-statuses
        type: Documentation
      - url: openapi/terms-of-service-user-statuses-openapi-original.yml
        type: OpenAPI
    description: The Box Terms of Service User Statuses API tracks and manages whether individual users have accepted or rejected specific terms of service agreements within the enterprise.
  - aid: box:box-collaboration-whitelist-entries-api
    name: Box Collaboration Whitelist Entries API
    tags:
      - Collaboration
      - Domain Restrictions
      - Security
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.box.com/2.0
    humanURL: https://developer.box.com/reference/post-collaboration-whitelist-entries
    properties:
      - url: https://developer.box.com/reference/post-collaboration-whitelist-entries
        type: Documentation
      - url: openapi/collaboration-whitelist-entries-openapi-original.yml
        type: OpenAPI
    description: The Box Collaboration Whitelist Entries API manages domain restrictions for collaborations, allowing administrators to specify which external domains are allowed to collaborate with enterprise users.
  - aid: box:box-collaboration-whitelist-exempt-targets-api
    name: Box Collaboration Whitelist Exempt Targets API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.box.com/
    properties:
      - url: https://developer.box.com/
        type: Documentation
      - url: openapi/collaboration-whitelist-exempt-targets-openapi-original.yml
        type: OpenAPI
    description: Needs a description.
  - aid: box:box-storage-policies-api
    name: Box Storage Policies API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.box.com/
    properties:
      - url: https://developer.box.com/
        type: Documentation
      - url: openapi/storage-policies-openapi-original.yml
        type: OpenAPI
    description: Needs a description.
  - aid: box:box-storage-policy-assignments-api
    name: Box Storage Policy Assignments API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.box.com/
    properties:
      - url: https://developer.box.com/
        type: Documentation
      - url: openapi/storage-policy-assignments-openapi-original.yml
        type: OpenAPI
    description: Needs a description.
  - aid: box:box-zip-downloads-api
    name: Box Zip Downloads API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.box.com/
    properties:
      - url: https://developer.box.com/
        type: Documentation
      - url: openapi/zip-downloads-openapi-original.yml
        type: OpenAPI
    description: Needs a description.
  - aid: box:box-sign-requests-api
    name: Box Sign Requests API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.box.com/
    properties:
      - url: https://developer.box.com/
        type: Documentation
      - url: openapi/sign-requests-openapi-original.yml
        type: OpenAPI
    description: Needs a description.
  - aid: box:box-workflows-api
    name: Box Workflows API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.box.com/
    properties:
      - url: https://developer.box.com/
        type: Documentation
      - url: openapi/workflows-openapi-original.yml
        type: OpenAPI
    description: Needs a description.
  - aid: box:box-sign-templates-api
    name: Box Sign Templates API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.box.com/
    properties:
      - url: https://developer.box.com/
        type: Documentation
      - url: openapi/sign-templates-openapi-original.yml
        type: OpenAPI
    description: Needs a description.
  - aid: box:box-integration-mappings-api
    name: Box Integration Mappings API
    tags: []
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.box.com/
    properties:
      - url: https://developer.box.com/
        type: Documentation
      - url: openapi/integration-mappings-openapi-original.yml
        type: OpenAPI
    description: Needs a description.
name: Box
tags:
  - Cloud Storage
  - Collaboration
  - Content Management
  - Documents
  - Enterprise
  - File Sharing
image: https://www.box.com/themes/custom/box/logo.svg
common:
  - url: https://medium.com/box-developer-blog
    type: Blog
  - url: https://developer.box.com/newsletter/
    type: Newsletter
  - url: https://developer.box.com/changelog/
    type: Change Log
  - url: https://github.com/box/samples
    type: Samples
  - url: https://support.box.com/hc/en-us/community/topics/360001932973-Platform-and-Developer-Forum
    type: Forum
  - url: https://status.box.com/
    type: Status
  - url: https://pulse.box.com/forums/909778-product-feedback?category_id=330838
    type: Feedback
  - url: https://account.box.com/login
    type: Login
  - url: https://www.box.com/pricing
    type: Pricing
  - url: https://github.com/box/box-node-sdk
    type: Node SDK
  - url: https://github.com/box/box-java-sdk
    type: Java SDK
  - url: https://github.com/box/box-python-sdk
    type: Python SDK
  - url: https://github.com/box/box-windows-sdk-v2
    type: .NET SDK
  - url: https://github.com/box/box-ios-sdk
    type: iOS Content SDK
  - url: https://github.com/box/boxcli
    type: CLI
  - url: https://developer.box.com/
    type: Developer Portal
  - url: https://support.box.com/
    type: Support
  - url: https://community.box.com/
    type: Community
  - url: https://www.box.com/legal/termsofservice
    type: Terms of Service
  - url: https://www.box.com/legal/privacypolicy
    type: Privacy Policy
  - url: https://account.box.com/signup
    type: Sign Up
  - url: https://github.com/box
    type: GitHub Organization
  - url: https://www.postman.com/box
    type: Postman Collection
  - type: Features
    data:
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
    sources:
      - https://www.box.com/pricing
    updated: '2026-05-04'
created: 2023/11/09
modified: '2026-05-04'
description: Box is a cloud content management and file sharing service for businesses. Box provides a secure platform for storing, managing, and sharing files and content, with features for collaboration, workflow automation, and integration with other business applications.
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
  - FN: Box Platform Team
    email: developers@box.com
    url: https://developer.box.com/
specificationVersion: '0.16'
type: Contract
position: Consuming
access: 3rd-Party
---
