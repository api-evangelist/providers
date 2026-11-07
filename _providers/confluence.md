---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 56.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 151
  human_in_the_loop: 7
  name: Confluence Agentic Access
  operation_count: 355
  slug: confluence-agentic-access
  summary_line: 355 operations · 151 acting · 7 human-in-the-loop
api_count: 3
apis:
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Store and retrieve custom data against Confluence content.
  name: Confluence Content Properties API
  phrasing_intents:
  - id: getAttachmentContentProperties
    intent: List content properties on an attachment
    question: What custom metadata properties are stored on a Confluence attachment?
  - id: createAttachmentProperty
    intent: Add a content property to an attachment
    question: How do I store my own key-value metadata on an uploaded attachment?
  - id: getAttachmentContentPropertiesById
    intent: Get one attachment content property by id
    question: What value does a particular content property hold on an attachment?
  - id: updateAttachmentPropertyById
    intent: Update an attachment content property
    question: How do I change the value of an existing property on an attachment?
  - id: deleteAttachmentPropertyById
    intent: Delete a content property from an attachment
    question: Can I remove a stored metadata property from an attachment?
  - id: getBlogpostContentProperties
    intent: List content properties on a blog post
    question: Which content properties have apps stored on a Confluence blog post?
  - id: createBlogpostProperty
    intent: Add a content property to a blog post
    question: How do I save custom metadata against a blog post?
  - id: getBlogpostContentPropertiesById
    intent: Get one blog post content property by id
    question: What is stored in a specific property on a blog post?
  phrasing_ops: 45
  slug: confluence-content-properties-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Search for content in Confluence using CQL (Confluence Query Language).
  name: Confluence Search API
  phrasing_intents:
  - id: searchByCQL
    intent: Search Confluence with CQL
    question: How do I search across pages, blogs, spaces and attachments with a CQL query?
  - id: searchUser
    intent: Search for users with CQL
    question: Can I find Confluence users by full name with a CQL user query?
  phrasing_ops: 2
  slug: confluence-search-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Create, read, update, delete, and archive content including pages and blog posts in Confluence Cloud.
  name: Confluence Content API
  phrasing_intents:
  - id: archivePages
    intent: Archive a batch of pages
    question: How do I archive several Confluence pages at once?
  - id: publishSharedDraft
    intent: Publish a shared blueprint draft
    question: How do I publish a shared draft that was created from a blueprint?
  - id: publishLegacyDraft
    intent: Publish a legacy blueprint draft
    question: Can I still publish an old-style legacy draft made from a blueprint?
  - id: searchContentByCQL
    intent: Find content objects with a CQL query
    question: Can I get full content objects back from a Confluence Query Language query?
  - id: convertContentIdsToContentTypes
    intent: Look up the content type for content ids
    question: I only stored content ids from the v1 API; how can I find out whether each is a page, blog post or comment?
  phrasing_ops: 5
  slug: confluence-content-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Manage Confluence spaces including creation, configuration, permissions, and settings.
  name: Confluence Space API
  phrasing_intents:
  - id: getSpaces
    intent: List spaces
    question: What spaces exist on my Confluence site?
  - id: createSpace
    intent: Create a space with role assignments
    question: How do I create a space and assign roles to people at the same time?
  - id: getSpaceById
    intent: Get a space by id
    question: What details can I see for one space if I know its id?
  - id: getPagesInSpace
    intent: List pages in a space
    question: Which pages live in a particular space?
  - id: postWikiRestApiSpace
    intent: Create a space with explicit permissions
    question: How do I create a space with a key and permissions on the classic REST endpoint?
  - id: createPrivateSpace
    intent: Create a private space only I can see
    question: How do I make a personal space nobody else can view?
  - id: updateSpace
    intent: Update a space's name, description or homepage
    question: Can I rename a space or change its homepage through the API?
  - id: deleteSpace
    intent: Permanently delete a space
    question: How do I permanently delete a space without sending it to the trash?
  phrasing_ops: 8
  slug: confluence-space-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Add, remove, and manage labels on Confluence content for organization and discovery.
  name: Confluence Content Labels API
  phrasing_intents:
  - id: addLabelsToContent
    intent: Add labels to content
    question: How do I tag a page with extra labels?
  - id: removeLabelFromContentUsingQueryParameter
    intent: Remove a label by name via query
    question: How do I remove a label whose name contains a slash?
  - id: removeLabelFromContent
    intent: Remove a label from content
    question: How do I take a label off a page?
  phrasing_ops: 3
  slug: confluence-content-labels-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Retrieve analytics data including content views and viewer counts for Confluence Cloud.
  name: Confluence Analytics API
  phrasing_intents:
  - id: getViews
    intent: Count total views of content
    question: How many times has a page been viewed?
  - id: getViewers
    intent: Count distinct viewers of content
    question: How many different people have viewed a page?
  phrasing_ops: 2
  slug: confluence-analytics-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Access and manage audit log records for compliance and security tracking in Confluence Cloud.
  name: Confluence Audit API
  phrasing_intents:
  - id: getAuditRecords
    intent: Search the audit log
    question: How do I see who exported a space or changed group membership?
  - id: createAuditRecord
    intent: Write a record to the audit log
    question: Can my app add its own entry to the Confluence audit log?
  - id: exportAuditRecords
    intent: Export audit records to a file
    question: How do I download the audit log as a CSV?
  - id: getRetentionPeriod
    intent: Get the audit log retention period
    question: How long are audit records kept before they're deleted?
  - id: setRetentionPeriod
    intent: Set the audit log retention period
    question: Can I keep audit records for longer, and what's the maximum?
  - id: getAuditRecordsForTimePeriod
    intent: Get recent audit records for a time window
    question: What happened in the audit log over the last few months?
  phrasing_ops: 6
  slug: confluence-audit-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Manage content templates and blueprints for standardized page creation in Confluence Cloud.
  name: Confluence Template API
  phrasing_intents:
  - id: updateContentTemplate
    intent: Update a content template
    question: How do I edit an existing page template's body or name?
  - id: createContentTemplate
    intent: Create a content template
    question: How do I add a new page template to a space?
  - id: getBlueprintTemplates
    intent: List blueprint templates
    question: Which blueprint templates are available in a space?
  - id: getContentTemplates
    intent: List content templates
    question: What user-created page templates exist on the site?
  - id: getContentTemplate
    intent: Get a content template
    question: What is in the body of a specific template?
  - id: removeTemplate
    intent: Delete or reset a template
    question: What happens when I remove a modified blueprint template?
  phrasing_ops: 6
  slug: confluence-template-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Manage user groups and group membership in Confluence Cloud.
  name: Confluence Group API
  phrasing_intents:
  - id: getGroups
    intent: List user groups
    question: What user groups exist on my Confluence site?
  - id: createGroup
    intent: Create a user group
    question: How do I create a new user group in Confluence?
  - id: getGroupByGroupId
    intent: Get a group by its id
    question: Can I look up a group's details from its group id?
  - id: removeGroupById
    intent: Delete a user group
    question: How do I delete a user group I no longer need?
  - id: searchGroups
    intent: Search groups by partial name
    question: Can I find groups by typing just part of their name?
  - id: getGroupMembersByGroupId
    intent: List the members of a group
    question: Who are the users in a particular Confluence group?
  - id: addUserToGroupByGroupId
    intent: Add a user to a group
    question: How do I add someone to a Confluence group?
  - id: removeMemberFromGroupByGroupId
    intent: Remove a user from a group
    question: How do I take a user out of a group?
  phrasing_ops: 8
  slug: confluence-group-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Retrieve user information, manage user properties, and check permissions in Confluence Cloud.
  name: Confluence Users API
  phrasing_intents:
  - id: getUser
    intent: Look up a user by account ID
    question: How do I get someone's display name and profile picture from their account ID?
  - id: getAnonymousUser
    intent: See how anonymous users are shown
    question: What display name and avatar does Confluence show for anonymous visitors?
  - id: getCurrentUser
    intent: Get the logged-in user
    question: Who am I authenticated as in Confluence?
  - id: getGroupMembershipsForUser
    intent: List the groups a user belongs to
    question: Which groups is a given user a member of?
  - id: getBulkUserLookup
    intent: Look up several users at once
    question: Can I fetch details for many account IDs in a single request?
  - id: getPrivacyUnsafeUserEmail
    intent: Get a user's email address
    question: How do I get a user's email even if their profile hides it?
  - id: getPrivacyUnsafeUserEmailBulk
    intent: Get email addresses for several users
    question: Can I fetch email addresses for a batch of account IDs at once?
  phrasing_ops: 7
  slug: confluence-users-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Manage content workflow states such as draft, in progress, and review in Confluence Cloud.
  name: Confluence Content States API
  phrasing_intents:
  - id: getContentState
    intent: Get the status label set on a page
    question: What content state, like 'In progress' or 'Ready for review', is set on a page?
  - id: setContentState
    intent: Set a content state on a page
    question: How do I mark a page as 'Ready for review' through the API?
  - id: removeContentState
    intent: Clear the content state from a page
    question: How do I remove the status label from a page?
  - id: getAvailableContentStates
    intent: List the states a page can be set to
    question: Which content states can I choose from for this page?
  - id: getCustomContentStates
    intent: List my custom content states
    question: What custom content states have I created?
  - id: getSpaceContentStates
    intent: List a space's suggested content states
    question: Which content states does a space suggest to its authors?
  - id: getContentStateSettings
    intent: Get a space's content state settings
    question: Are content states turned on at all in a given space?
  - id: getContentsWithState
    intent: Find content in a space with a given state
    question: Which pages in a space are currently marked with a particular state?
  phrasing_ops: 8
  slug: confluence-content-states-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Manage read and update restrictions on Confluence content for access control.
  name: Confluence Content Restrictions API
  phrasing_intents:
  - id: getRestrictions
    intent: List the restrictions on content
    question: Who is restricted from viewing or editing a particular page?
  - id: updateRestrictions
    intent: Replace all restrictions on content
    question: How do I overwrite a page's existing restrictions with a new set?
  - id: addRestrictions
    intent: Add restrictions to content
    question: Can I add a restriction to a page without touching the restrictions already there?
  - id: deleteRestrictions
    intent: Remove all restrictions from content
    question: How do I clear every read and edit restriction from a page?
  - id: getRestrictionsByOperation
    intent: Get content restrictions grouped by operation
    question: Can I see a page's restrictions organised by read versus update?
  - id: getRestrictionsForOperation
    intent: Get content restrictions for one operation
    question: Who exactly is allowed to edit a restricted page?
  - id: getIndividualGroupRestrictionStatusByGroupId
    intent: Check if a group is in a content restriction
    question: Does a particular group have read access under a page's restriction?
  - id: addGroupToContentRestrictionByGroupId
    intent: Grant a group access via a content restriction
    question: How do I let one group edit a page that's otherwise restricted?
  phrasing_ops: 12
  slug: confluence-content-restrictions-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Manage permissions for Confluence spaces including user and group access levels.
  name: Confluence Space Permissions API
  phrasing_intents:
  - id: addPermissionToSpace
    intent: Grant a user or group a space permission
    question: How do I give a group permission to edit pages in a space?
  - id: addCustomContentPermissions
    intent: Grant an app's custom content permissions in a space
    question: How does my app grant permissions on its own custom content type in a space?
  - id: removePermission
    intent: Revoke a space permission
    question: How do I take a permission away from someone in a space?
  - id: getSpacePermissionsAssignments
    intent: List the permission assignments in a space
    question: Who has which permissions in a given space?
  - id: getAvailableSpacePermissions
    intent: List all possible space permissions
    question: Which space permissions exist that a role can include?
  phrasing_ops: 5
  slug: confluence-space-permissions-api
- description: Query Confluence data using GraphQL for efficient cross-product data retrieval with field-level precision.
  name: Confluence GraphQL API
  slug: confluence-graphql-api
- description: REST API for Confluence Data Center and Server for on-premise content, space, and user management.
  name: Confluence Data Center REST API
  slug: confluence-data-center-rest-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Upload, retrieve, update, and delete file attachments on Confluence content.
  name: Confluence Content Attachments API
  phrasing_intents:
  - id: createOrUpdateAttachments
    intent: Upload a file, replacing it if it already exists
    question: How do I upload a file to a page and have it create a new version if one with that name already exists?
  - id: createAttachment
    intent: Attach a new file to a page
    question: How do I add a brand-new attachment to a Confluence page without touching existing ones?
  - id: updateAttachmentProperties
    intent: Rename or move an attachment
    question: How do I rename an attachment or change its media type without re-uploading it?
  - id: updateAttachmentData
    intent: Replace the file contents of an attachment
    question: How do I upload a new version of an existing attachment by its ID?
  - id: downloadAttatchment
    intent: Download an attachment
    question: How do I download a file attached to a Confluence page?
  phrasing_ops: 5
  slug: confluence-content-attachments-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Convert content body representations between storage, editor, view, and export formats.
  name: Confluence Content Body API
  phrasing_intents:
  - id: asyncConvertContentBodyRequest
    intent: Start converting a content body to another format
    question: How do I convert storage format into a rendered view in the background?
  - id: asyncConvertContentBodyResponse
    intent: Get the result of a body conversion task
    question: Is my content body conversion finished yet?
  - id: bulkAsyncConvertContentBodyRequest
    intent: Start bulk content body conversions
    question: How do I convert several content bodies in one request?
  - id: bulkAsyncConvertContentBodyResponse
    intent: Get results of several body conversion tasks
    question: Can I check many conversion tasks at once?
  phrasing_ops: 4
  slug: confluence-content-body-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Retrieve children and descendants of Confluence content for navigating content hierarchies.
  name: Confluence Content Children and Descendants API
  phrasing_intents:
  - id: movePage
    intent: Move a page in the page tree
    question: How do I move a page under a different parent?
  - id: getContentDescendants
    intent: Get all descendants of content
    question: What's everything nested under a page at every level?
  - id: getDescendantsOfType
    intent: List descendants of a given type
    question: Which comments or attachments exist anywhere below a page?
  - id: copyPageHierarchy
    intent: Copy a page and all its descendants
    question: How do I duplicate a whole page tree under a new parent?
  - id: copyPage
    intent: Copy a single page
    question: How do I copy just one page, without its children?
  phrasing_ops: 5
  slug: confluence-content-children-and-descendants-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Retrieve the body of a macro in Confluence content by macro ID.
  name: Confluence Content Macro Body API
  phrasing_intents:
  - id: getMacroBodyByMacroId
    intent: Get a macro's body in storage format
    question: How can I read the raw storage-format body and parameters of a macro on a page?
  - id: getAndConvertMacroBodyByMacroId
    intent: Convert a macro body to another format now
    question: Can I get a macro rendered as view HTML instead of storage format in a single call?
  - id: getAndAsyncConvertMacroBodyByMacroId
    intent: Start an async conversion of a macro body
    question: How do I convert a large macro in the background and fetch the result later?
  phrasing_ops: 3
  slug: confluence-content-macro-body-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Check content permissions for users to determine read and update access.
  name: Confluence Content Permissions API
  phrasing_intents:
  - id: checkContentPermission
    intent: Check if someone can act on content
    question: Can a given user edit a specific page?
  phrasing_ops: 1
  slug: confluence-content-permissions-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Manage content version history including retrieval, restoration, and deletion of versions.
  name: Confluence Content Versions API
  phrasing_intents:
  - id: restoreContentVersion
    intent: Restore an earlier content version
    question: How do I roll a page back to an older version?
  - id: deleteContentVersion
    intent: Delete a historical content version
    question: Can I delete an old version from a page's history?
  phrasing_ops: 2
  slug: confluence-content-versions-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Manage content and space watches to receive notifications on updates.
  name: Confluence Content Watches API
  phrasing_intents:
  - id: getWatchesForPage
    intent: List who is watching a page
    question: Who gets notified when a particular Confluence page is updated?
  - id: getWatchesForSpace
    intent: List space watches for the space a page is in
    question: Starting from a page, how do I find who watches the space it lives in?
  - id: getWatchersForSpace
    intent: List the watchers of a space by key
    question: Who is watching a space when I know its space key?
  - id: getContentWatchStatus
    intent: Check whether a user watches a piece of content
    question: Am I watching a specific page right now?
  - id: addContentWatcher
    intent: Start watching a piece of content
    question: How do I subscribe to updates on a single Confluence page?
  - id: removeContentWatcher
    intent: Stop watching a piece of content
    question: How do I stop getting notifications for one page?
  - id: isWatchingLabel
    intent: Check whether a user watches a label
    question: Am I following a particular label?
  - id: addLabelWatcher
    intent: Start watching a label
    question: How do I get notified about content tagged with a certain label?
  phrasing_ops: 12
  slug: confluence-content-watches-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Register and manage dynamic modules for Confluence Connect apps.
  name: Confluence Dynamic Modules API
  phrasing_intents:
  - id: getModules
    intent: List an app's dynamically registered modules
    question: Which modules has my Connect app registered at runtime?
  - id: registerModules
    intent: Register dynamic modules for an app
    question: How do I register Connect modules at runtime instead of in the descriptor?
  - id: removeModules
    intent: Remove dynamically registered modules
    question: How do I unregister a dynamic module my app added?
  phrasing_ops: 3
  slug: confluence-dynamic-modules-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Experimental endpoints for Confluence Cloud that may change or be removed.
  name: Confluence Experimental API
  phrasing_intents:
  - id: deletePageTree
    intent: Trash a page and all its descendants
    question: How do I move a whole page tree, including every child page, to the trash?
  - id: getLabelsForSpace
    intent: List a space's labels by space key
    question: How do I see the labels on a space when I only know its key?
  - id: addLabelsToSpace
    intent: Add labels to a space
    question: How do I tag a space with new labels without removing its existing ones?
  - id: deleteLabelFromSpace
    intent: Remove a label from a space
    question: How do I untag a space?
  phrasing_ops: 4
  slug: confluence-experimental-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Retrieve information about labels used across Confluence content.
  name: Confluence Label Info API
  phrasing_intents:
  - id: getAllLabelContent
    intent: Get a label and the content tagged with it
    question: What pages and blog posts are tagged with a particular label?
  phrasing_ops: 1
  slug: confluence-label-info-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Monitor the status and results of long-running asynchronous tasks in Confluence.
  name: Confluence Long-Running Task API
  phrasing_intents:
  - id: getTasks
    intent: List active long-running tasks
    question: Which long-running jobs, like space exports, are running on my site right now?
  - id: getTask
    intent: Check progress of a long-running task
    question: What percentage of my space export has completed?
  phrasing_ops: 2
  slug: confluence-long-running-task-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Manage relationships between Confluence entities such as content and users.
  name: Confluence Relation API
  phrasing_intents:
  - id: findTargetFromSource
    intent: Find what an entity is related to
    question: How do I list all the pages a user has marked as favourite?
  - id: getRelationship
    intent: Check if a relationship exists between two entities
    question: Has a user favourited a specific page?
  - id: createRelationship
    intent: Create a relationship such as a favourite
    question: How do I mark a page as a favourite for a user through the API?
  - id: deleteRelationship
    intent: Remove a relationship between two entities
    question: How do I unfavourite a page for a user?
  - id: findSourcesForTarget
    intent: Find who is related to a target entity
    question: Which users have a 'collaborator' relationship to a page?
  phrasing_ops: 5
  slug: confluence-relation-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Retrieve and manage Confluence site settings and configuration.
  name: Confluence Settings API
  phrasing_intents:
  - id: getLookAndFeelSettings
    intent: Get look and feel settings
    question: What color scheme and styling does my site or a space use?
  - id: updateLookAndFeel
    intent: Choose which look and feel a space uses
    question: How do I switch a space between global, custom and theme styling?
  - id: updateLookAndFeelSettings
    intent: Customize look and feel colors and styles
    question: How do I change heading, link and menu colors for my site?
  - id: resetLookAndFeelSettings
    intent: Reset custom look and feel to defaults
    question: How do I undo my custom styling and go back to the defaults?
  - id: getSystemInfo
    intent: Get system info for the Confluence tenant
    question: What system information does my Confluence Cloud tenant report?
  phrasing_ops: 5
  slug: confluence-settings-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Manage settings for individual Confluence spaces.
  name: Confluence Space Settings API
  phrasing_intents:
  - id: getSpaceSettings
    intent: Get a space's settings
    question: What settings are configured for a particular space?
  - id: updateSpaceSettings
    intent: Update a space's settings
    question: How do I turn route override on or off for a space?
  phrasing_ops: 2
  slug: confluence-space-settings-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Retrieve theme information for Confluence spaces and the global site.
  name: Confluence Themes API
  phrasing_intents:
  - id: getThemes
    intent: List the installed themes
    question: What themes are installed on my Confluence site?
  - id: getGlobalTheme
    intent: Get the site-wide theme
    question: Which theme is set globally for the whole site?
  - id: getTheme
    intent: Get a theme by key
    question: What's the name, description and icon of a particular theme?
  - id: getSpaceTheme
    intent: Get the theme set on a space
    question: Which theme is a space using?
  - id: setSpaceTheme
    intent: Apply a theme to a space
    question: How do I change the theme of a single space?
  - id: resetSpaceTheme
    intent: Reset a space to the global theme
    question: How do I make a space go back to the site's default look and feel?
  phrasing_ops: 6
  slug: confluence-themes-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Store and retrieve custom properties associated with Confluence users.
  name: Confluence User Properties API
  phrasing_intents:
  - id: getUserProperties
    intent: List a user's property keys
    question: What properties has an app stored against a Confluence user?
  - id: getUserProperty
    intent: Get a user property by key
    question: What value is saved under a specific property key for a user?
  - id: updateUserProperty
    intent: Update a user property's value
    question: How do I change the value of an existing user property?
  - id: createUserProperty
    intent: Create a user property
    question: How do I store a new custom setting on a user account?
  - id: deleteUserProperty
    intent: Delete a user property
    question: Can I remove a stored property from a user?
  phrasing_ops: 5
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
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Manage file attachments on content
  name: Confluence Attachment API
  phrasing_intents:
  - id: getAttachmentById
    intent: Get an attachment by id
    question: What details can I get about a single Confluence attachment?
  - id: deleteAttachment
    intent: Delete an attachment
    question: How do I delete a file attachment from Confluence?
  - id: getPageAttachments
    intent: List attachments on a page
    question: Which files are attached to a specific page?
  - id: getAttachments
    intent: List all attachments across the site
    question: How do I list every attachment on my Confluence site?
  - id: getBlogpostAttachments
    intent: List attachments on a blog post
    question: What files are attached to a particular blog post?
  - id: getCustomContentAttachments
    intent: List attachments on custom content
    question: Which attachments belong to a custom content item?
  - id: getLabelAttachments
    intent: List attachments carrying a label
    question: Which attachments have been tagged with a given label?
  - id: getAttachmentThumbnailById
    intent: Download an attachment's thumbnail image
    question: How do I get a preview thumbnail for an attachment?
  phrasing_ops: 8
  slug: confluence-attachment-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Create, retrieve, update, and delete blog posts
  name: Confluence Blog Post API
  phrasing_intents:
  - id: getBlogPosts
    intent: List blog posts across the site
    question: How do I list every blog post on my Confluence site?
  - id: createBlogPost
    intent: Publish a blog post
    question: How do I write a new blog post in a space?
  - id: getBlogPostById
    intent: Get a blog post
    question: How do I read a specific blog post with its content?
  - id: updateBlogPost
    intent: Edit a blog post
    question: How do I edit an existing blog post?
  - id: deleteBlogPost
    intent: Delete a blog post
    question: Can I delete a blog post I no longer need?
  - id: getLabelBlogPosts
    intent: List blog posts with a label
    question: Which blog posts are tagged with a given label?
  - id: getBlogPostsInSpace
    intent: List the blog posts in a space
    question: What blog posts have been published in a particular space?
  phrasing_ops: 7
  slug: confluence-blog-post-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Create, retrieve, update, and delete comments on pages and blog posts
  name: Confluence Comment API
  phrasing_intents:
  - id: getFooterComments
    intent: List the footer comments on a page
    question: How do I read the comments left at the bottom of a Confluence page?
  - id: getInlineComments
    intent: List the inline comments on a page
    question: Where can I see the comments people highlighted inside a specific page's text?
  - id: createFooterComment
    intent: Add a footer comment to a page or blog post
    question: How do I post a comment at the bottom of a Confluence page?
  - id: getFooterComments
    intent: List footer comments across the whole site
    question: Can I pull every footer comment across the site, not just one page?
  - id: createInlineComment
    intent: Add an inline comment to selected text
    question: How do I comment on a specific highlighted sentence in a page?
  - id: getInlineComments
    intent: List inline comments across the whole site
    question: Can I get every inline comment in the site in one list?
  - id: getCommentById
    intent: Get a comment by its id
    question: How do I look up a single comment when I only know its id, without knowing if it is footer or inline?
  - id: updateComment
    intent: Edit a comment through the generic comments endpoint
    question: How do I change the text of a comment by id when the version number must go up?
  phrasing_ops: 22
  slug: confluence-comment-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Manage labels on content
  name: Confluence Label API
  phrasing_intents:
  - id: getPageLabels
    intent: List the labels on a page
    question: What labels are tagged on a specific Confluence page?
  - id: getLabelById
    intent: Get a label by its id
    question: How do I look up a label's name when all I have is its id?
  - id: getAttachmentLabels
    intent: List the labels on an attachment
    question: Which labels are applied to an uploaded file?
  - id: getBlogPostLabels
    intent: List the labels on a blog post
    question: What labels does a given blog post carry?
  - id: getCustomContentLabels
    intent: List the labels on custom content
    question: Which labels are attached to an app's custom content item?
  - id: getLabels
    intent: List every label on the site
    question: What labels exist across the whole Confluence site?
  - id: getSpaceLabels
    intent: List the labels on a space itself
    question: Which labels are applied to a space as a whole, not its pages?
  - id: getSpaceContentLabels
    intent: List labels used on content in a space
    question: What labels are used across the pages and blog posts inside a space?
  phrasing_ops: 8
  slug: confluence-label-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Create, retrieve, update, and delete pages
  name: Confluence Page API
  phrasing_intents:
  - id: getPages
    intent: List pages across the site
    question: How do I list all pages on my Confluence site?
  - id: createPage
    intent: Create a page
    question: How do I create a new Confluence page in a space?
  - id: getPageById
    intent: Get a page
    question: How do I fetch a single page with its content?
  - id: updatePage
    intent: Update a page's content
    question: How do I edit the body of an existing page?
  - id: deletePage
    intent: Delete a page
    question: What happens when I delete a page — does it go to the trash?
  - id: getChildPages
    intent: List a page's direct child pages
    question: Which pages sit directly under a given page?
  - id: getPagesInSpace
    intent: List the pages in a space
    question: What pages does a particular space contain?
  - id: getLabelPages
    intent: List pages with a label
    question: Which pages have been tagged with a particular label?
  phrasing_ops: 9
  slug: confluence-page-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: Retrieve and manage Confluence spaces
  name: Confluence Space API
  phrasing_intents:
  - id: getSpaces
    intent: List spaces
    question: What spaces exist on my Confluence site?
  - id: createSpace
    intent: Create a space with role assignments
    question: How do I create a space and assign roles to people at the same time?
  - id: getSpaceById
    intent: Get a space by id
    question: What details can I see for one space if I know its id?
  - id: getPagesInSpace
    intent: List pages in a space
    question: Which pages live in a particular space?
  - id: postWikiRestApiSpace
    intent: Create a space with explicit permissions
    question: How do I create a space with a key and permissions on the classic REST endpoint?
  - id: createPrivateSpace
    intent: Create a private space only I can see
    question: How do I make a personal space nobody else can view?
  - id: updateSpace
    intent: Update a space's name, description or homepage
    question: Can I rename a space or change its homepage through the API?
  - id: deleteSpace
    intent: Permanently delete a space
    question: How do I permanently delete a space without sending it to the trash?
  phrasing_ops: 8
  slug: confluence-space-api
- description: The Atlassian GraphQL gateway. Anonymous introspection succeeds and returns 27,710 types, of which 1,113 are Confluence-prefixed, across 3,369 Query fields; executing most Confluence fields requires a
  name: Confluence Cloud GraphQL API
  slug: confluence-cloud-graphql-api
- description: Atlassian's official remote Model Context Protocol server. The Confluence permission groups (read_confluence, write_confluence, search_confluence) expose 60 named tools over streamable HTTP at https:/
  name: Atlassian Rovo MCP Server (Confluence tools)
  slug: atlassian-rovo-mcp-server
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The [Admin Key feature](https://support.atlassian.com/confluence-cloud/docs/bypass-access-restrictions-on-a-page-with-admin-key/) is only offered with Confluence Cloud Premium and Enterprise to organi
  name: Confluence Admin Key API
  phrasing_intents:
  - id: getAdminKey
    intent: Check my current admin key
    question: Do I currently have an admin key enabled on this site?
  - id: enableAdminKey
    intent: Enable an admin key
    question: How do I turn on an admin key for elevated access?
  - id: disableAdminKey
    intent: Disable my admin key
    question: How do I switch off my admin key before it expires?
  phrasing_ops: 3
  slug: confluence-admin-key-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Analytics API from Confluence — 2 operation(s) for analytics.
  name: Confluence Analytics API
  phrasing_intents:
  - id: getViews
    intent: Count total views of content
    question: How many times has a page been viewed?
  - id: getViewers
    intent: Count distinct viewers of content
    question: How many different people have viewed a page?
  phrasing_ops: 2
  slug: confluence-analytics-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Ancestors API from Confluence — 5 operation(s) for ancestors.
  name: Confluence Ancestors API
  phrasing_intents:
  - id: getWhiteboardAncestors
    intent: List a whiteboard's ancestors
    question: Where does a whiteboard sit in the content tree?
  - id: getDatabaseAncestors
    intent: List a database's ancestors
    question: What content sits above a Confluence database in the tree?
  - id: getSmartLinkAncestors
    intent: List a Smart Link's ancestors
    question: Where is an embedded Smart Link located in the content tree?
  - id: getFolderAncestors
    intent: List a folder's ancestors
    question: Which folders and pages contain a given folder?
  - id: getPageAncestors
    intent: List a page's ancestors
    question: What are the parent pages of a page, all the way to the top?
  phrasing_ops: 5
  slug: confluence-ancestors-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The App Properties API from Confluence — 2 operation(s) for app properties.
  name: Confluence App Properties API
  phrasing_intents:
  - id: getForgeAppProperties
    intent: List my Forge app's stored properties
    question: How does my Forge app read all the properties it has stored in Confluence?
  - id: getForgeAppProperty
    intent: Read one Forge app property
    question: How do I fetch a single stored value for my Forge app by key?
  - id: putForgeAppProperty
    intent: Save a Forge app property
    question: How does my Forge app store a setting in Confluence?
  - id: deleteForgeAppProperty
    intent: Delete a Forge app property
    question: How do I clear a stored setting from my Forge app?
  phrasing_ops: 4
  slug: confluence-app-properties-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Audit API from Confluence — 4 operation(s) for audit.
  name: Confluence Audit API
  phrasing_intents:
  - id: getAuditRecords
    intent: Search the audit log
    question: How do I see who exported a space or changed group membership?
  - id: createAuditRecord
    intent: Write a record to the audit log
    question: Can my app add its own entry to the Confluence audit log?
  - id: exportAuditRecords
    intent: Export audit records to a file
    question: How do I download the audit log as a CSV?
  - id: getRetentionPeriod
    intent: Get the audit log retention period
    question: How long are audit records kept before they're deleted?
  - id: setRetentionPeriod
    intent: Set the audit log retention period
    question: Can I keep audit records for longer, and what's the maximum?
  - id: getAuditRecordsForTimePeriod
    intent: Get recent audit records for a time window
    question: What happened in the audit log over the last few months?
  phrasing_ops: 6
  slug: confluence-audit-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Children API from Confluence — 7 operation(s) for children.
  name: Confluence Children API
  phrasing_intents:
  - id: getWhiteboardDirectChildren
    intent: List direct children of a whiteboard
    question: What content sits directly beneath a whiteboard in the content tree?
  - id: getDatabaseDirectChildren
    intent: List direct children of a database
    question: Which items are nested one level under a Confluence database?
  - id: getSmartLinkDirectChildren
    intent: List direct children of a Smart Link
    question: What content is nested directly under a Smart Link in the page tree?
  - id: getFolderDirectChildren
    intent: List direct children of a folder
    question: What pages and items are directly inside a folder?
  - id: getChildPages
    intent: List child pages of a page
    question: How do I list only the child pages under a parent page?
  - id: getChildCustomContent
    intent: List child custom content
    question: Which custom content items are children of another custom content item?
  - id: getPageDirectChildren
    intent: List all direct children of a page
    question: What content of every type sits directly under a page, including folders and whiteboards?
  phrasing_ops: 7
  slug: confluence-children-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Classification Level API from Confluence — 10 operation(s) for classification level.
  name: Confluence Classification Level API
  phrasing_intents:
  - id: getClassificationLevels
    intent: List available classification levels
    question: Which data classification levels are available on my Confluence site?
  - id: getSpaceDefaultClassificationLevel
    intent: Get a space's default classification level
    question: What classification level do new pages in a space get by default?
  - id: putSpaceDefaultClassificationLevel
    intent: Set a space's default classification level
    question: How do I change the default classification level for a whole space?
  - id: deleteSpaceDefaultClassificationLevel
    intent: Remove a space's default classification level
    question: Can I clear the default classification level from a space?
  - id: getPageClassificationLevel
    intent: Get a page's classification level
    question: What classification level is a specific page marked with?
  - id: putPageClassificationLevel
    intent: Set a page's classification level
    question: How do I mark a single page as confidential?
  - id: postPageClassificationLevel
    intent: Reset a page to the space default classification
    question: How do I make a page go back to its space's default classification?
  - id: getBlogPostClassificationLevel
    intent: Get a blog post's classification level
    question: What classification level does a blog post carry?
  phrasing_ops: 16
  slug: confluence-classification-level-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Content API from Confluence — 4 operation(s) for content.
  name: Confluence Content API
  phrasing_intents:
  - id: archivePages
    intent: Archive a batch of pages
    question: How do I archive several Confluence pages at once?
  - id: publishSharedDraft
    intent: Publish a shared blueprint draft
    question: How do I publish a shared draft that was created from a blueprint?
  - id: publishLegacyDraft
    intent: Publish a legacy blueprint draft
    question: Can I still publish an old-style legacy draft made from a blueprint?
  - id: searchContentByCQL
    intent: Find content objects with a CQL query
    question: Can I get full content objects back from a Confluence Query Language query?
  - id: convertContentIdsToContentTypes
    intent: Look up the content type for content ids
    question: I only stored content ids from the v1 API; how can I find out whether each is a page, blog post or comment?
  phrasing_ops: 5
  slug: confluence-content-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Content - attachments API from Confluence — 4 operation(s) for content - attachments.
  name: Confluence Content - attachments API
  phrasing_intents:
  - id: createOrUpdateAttachments
    intent: Upload a file, replacing it if it already exists
    question: How do I upload a file to a page and have it create a new version if one with that name already exists?
  - id: createAttachment
    intent: Attach a new file to a page
    question: How do I add a brand-new attachment to a Confluence page without touching existing ones?
  - id: updateAttachmentProperties
    intent: Rename or move an attachment
    question: How do I rename an attachment or change its media type without re-uploading it?
  - id: updateAttachmentData
    intent: Replace the file contents of an attachment
    question: How do I upload a new version of an existing attachment by its ID?
  - id: downloadAttatchment
    intent: Download an attachment
    question: How do I download a file attached to a Confluence page?
  phrasing_ops: 5
  slug: confluence-content-attachments-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Content body API from Confluence — 3 operation(s) for content body.
  name: Confluence Content body API
  phrasing_intents:
  - id: asyncConvertContentBodyRequest
    intent: Start converting a content body to another format
    question: How do I convert storage format into a rendered view in the background?
  - id: asyncConvertContentBodyResponse
    intent: Get the result of a body conversion task
    question: Is my content body conversion finished yet?
  - id: bulkAsyncConvertContentBodyRequest
    intent: Start bulk content body conversions
    question: How do I convert several content bodies in one request?
  - id: bulkAsyncConvertContentBodyResponse
    intent: Get results of several body conversion tasks
    question: Can I check many conversion tasks at once?
  phrasing_ops: 4
  slug: confluence-content-body-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Content - children and descendants API from Confluence — 5 operation(s) for content - children and descendants.
  name: Confluence Content - children and descendants API
  phrasing_intents:
  - id: movePage
    intent: Move a page in the page tree
    question: How do I move a page under a different parent?
  - id: getContentDescendants
    intent: Get all descendants of content
    question: What's everything nested under a page at every level?
  - id: getDescendantsOfType
    intent: List descendants of a given type
    question: Which comments or attachments exist anywhere below a page?
  - id: copyPageHierarchy
    intent: Copy a page and all its descendants
    question: How do I duplicate a whole page tree under a new parent?
  - id: copyPage
    intent: Copy a single page
    question: How do I copy just one page, without its children?
  phrasing_ops: 5
  slug: confluence-content-children-and-descendants-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Content labels API from Confluence — 2 operation(s) for content labels.
  name: Confluence Content labels API
  phrasing_intents:
  - id: addLabelsToContent
    intent: Add labels to content
    question: How do I tag a page with extra labels?
  - id: removeLabelFromContentUsingQueryParameter
    intent: Remove a label by name via query
    question: How do I remove a label whose name contains a slash?
  - id: removeLabelFromContent
    intent: Remove a label from content
    question: How do I take a label off a page?
  phrasing_ops: 3
  slug: confluence-content-labels-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Content - macro body API from Confluence — 3 operation(s) for content - macro body.
  name: Confluence Content - macro body API
  phrasing_intents:
  - id: getMacroBodyByMacroId
    intent: Get a macro's body in storage format
    question: How can I read the raw storage-format body and parameters of a macro on a page?
  - id: getAndConvertMacroBodyByMacroId
    intent: Convert a macro body to another format now
    question: Can I get a macro rendered as view HTML instead of storage format in a single call?
  - id: getAndAsyncConvertMacroBodyByMacroId
    intent: Start an async conversion of a macro body
    question: How do I convert a large macro in the background and fetch the result later?
  phrasing_ops: 3
  slug: confluence-content-macro-body-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Content permissions API from Confluence — 1 operation(s) for content permissions.
  name: Confluence Content permissions API
  phrasing_intents:
  - id: checkContentPermission
    intent: Check if someone can act on content
    question: Can a given user edit a specific page?
  phrasing_ops: 1
  slug: confluence-content-permissions-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Content Properties API from Confluence — 18 operation(s) for content properties.
  name: Confluence Content Properties API
  phrasing_intents:
  - id: getAttachmentContentProperties
    intent: List content properties on an attachment
    question: What custom metadata properties are stored on a Confluence attachment?
  - id: createAttachmentProperty
    intent: Add a content property to an attachment
    question: How do I store my own key-value metadata on an uploaded attachment?
  - id: getAttachmentContentPropertiesById
    intent: Get one attachment content property by id
    question: What value does a particular content property hold on an attachment?
  - id: updateAttachmentPropertyById
    intent: Update an attachment content property
    question: How do I change the value of an existing property on an attachment?
  - id: deleteAttachmentPropertyById
    intent: Delete a content property from an attachment
    question: Can I remove a stored metadata property from an attachment?
  - id: getBlogpostContentProperties
    intent: List content properties on a blog post
    question: Which content properties have apps stored on a Confluence blog post?
  - id: createBlogpostProperty
    intent: Add a content property to a blog post
    question: How do I save custom metadata against a blog post?
  - id: getBlogpostContentPropertiesById
    intent: Get one blog post content property by id
    question: What is stored in a specific property on a blog post?
  phrasing_ops: 45
  slug: confluence-content-properties-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Content restrictions API from Confluence — 5 operation(s) for content restrictions.
  name: Confluence Content restrictions API
  phrasing_intents:
  - id: getRestrictions
    intent: List the restrictions on content
    question: Who is restricted from viewing or editing a particular page?
  - id: updateRestrictions
    intent: Replace all restrictions on content
    question: How do I overwrite a page's existing restrictions with a new set?
  - id: addRestrictions
    intent: Add restrictions to content
    question: Can I add a restriction to a page without touching the restrictions already there?
  - id: deleteRestrictions
    intent: Remove all restrictions from content
    question: How do I clear every read and edit restriction from a page?
  - id: getRestrictionsByOperation
    intent: Get content restrictions grouped by operation
    question: Can I see a page's restrictions organised by read versus update?
  - id: getRestrictionsForOperation
    intent: Get content restrictions for one operation
    question: Who exactly is allowed to edit a restricted page?
  - id: getIndividualGroupRestrictionStatusByGroupId
    intent: Check if a group is in a content restriction
    question: Does a particular group have read access under a page's restriction?
  - id: addGroupToContentRestrictionByGroupId
    intent: Grant a group access via a content restriction
    question: How do I let one group edit a page that's otherwise restricted?
  phrasing_ops: 12
  slug: confluence-content-restrictions-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Content states API from Confluence — 6 operation(s) for content states.
  name: Confluence Content states API
  phrasing_intents:
  - id: getContentState
    intent: Get the status label set on a page
    question: What content state, like 'In progress' or 'Ready for review', is set on a page?
  - id: setContentState
    intent: Set a content state on a page
    question: How do I mark a page as 'Ready for review' through the API?
  - id: removeContentState
    intent: Clear the content state from a page
    question: How do I remove the status label from a page?
  - id: getAvailableContentStates
    intent: List the states a page can be set to
    question: Which content states can I choose from for this page?
  - id: getCustomContentStates
    intent: List my custom content states
    question: What custom content states have I created?
  - id: getSpaceContentStates
    intent: List a space's suggested content states
    question: Which content states does a space suggest to its authors?
  - id: getContentStateSettings
    intent: Get a space's content state settings
    question: Are content states turned on at all in a given space?
  - id: getContentsWithState
    intent: Find content in a space with a given state
    question: Which pages in a space are currently marked with a particular state?
  phrasing_ops: 8
  slug: confluence-content-states-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Content versions API from Confluence — 2 operation(s) for content versions.
  name: Confluence Content versions API
  phrasing_intents:
  - id: restoreContentVersion
    intent: Restore an earlier content version
    question: How do I roll a page back to an older version?
  - id: deleteContentVersion
    intent: Delete a historical content version
    question: Can I delete an old version from a page's history?
  phrasing_ops: 2
  slug: confluence-content-versions-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Content watches API from Confluence — 6 operation(s) for content watches.
  name: Confluence Content watches API
  phrasing_intents:
  - id: getWatchesForPage
    intent: List who is watching a page
    question: Who gets notified when a particular Confluence page is updated?
  - id: getWatchesForSpace
    intent: List space watches for the space a page is in
    question: Starting from a page, how do I find who watches the space it lives in?
  - id: getWatchersForSpace
    intent: List the watchers of a space by key
    question: Who is watching a space when I know its space key?
  - id: getContentWatchStatus
    intent: Check whether a user watches a piece of content
    question: Am I watching a specific page right now?
  - id: addContentWatcher
    intent: Start watching a piece of content
    question: How do I subscribe to updates on a single Confluence page?
  - id: removeContentWatcher
    intent: Stop watching a piece of content
    question: How do I stop getting notifications for one page?
  - id: isWatchingLabel
    intent: Check whether a user watches a label
    question: Am I following a particular label?
  - id: addLabelWatcher
    intent: Start watching a label
    question: How do I get notified about content tagged with a certain label?
  phrasing_ops: 12
  slug: confluence-content-watches-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Custom Content API from Confluence — 5 operation(s) for custom content.
  name: Confluence Custom Content API
  phrasing_intents:
  - id: getCustomContentByTypeInBlogPost
    intent: List custom content of a type in a blog post
    question: What custom content of a given type is attached to a blog post?
  - id: getCustomContentByType
    intent: List custom content of a type
    question: How do I find all custom content of a given type across the site?
  - id: createCustomContent
    intent: Create custom content
    question: How do I create a custom content item for my app?
  - id: getCustomContentById
    intent: Get a custom content item
    question: How do I fetch one custom content item by its ID?
  - id: updateCustomContent
    intent: Update a custom content item
    question: How do I edit an existing custom content item?
  - id: deleteCustomContent
    intent: Delete a custom content item
    question: Does deleting custom content send it to the trash or remove it for good?
  - id: getCustomContentByTypeInPage
    intent: List custom content of a type in a page
    question: What custom content of a given type lives inside a page?
  - id: getCustomContentByTypeInSpace
    intent: List custom content of a type in a space
    question: Which custom content items of a type belong to a space?
  phrasing_ops: 8
  slug: confluence-custom-content-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Data Policies API from Confluence — 2 operation(s) for data policies.
  name: Confluence Data Policies API
  phrasing_intents:
  - id: getDataPolicyMetadata
    intent: Get workspace data policy metadata
    question: Does my Confluence workspace have any data policies that block app access?
  - id: getDataPolicySpaces
    intent: List spaces with their data policy status
    question: Which spaces are affected by data policies that restrict apps?
  phrasing_ops: 2
  slug: confluence-data-policies-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Database API from Confluence — 2 operation(s) for database.
  name: Confluence Database API
  phrasing_intents:
  - id: createDatabase
    intent: Create a database in a space
    question: How do I create a new Confluence database in a space?
  - id: getDatabaseById
    intent: Get a database by id
    question: How do I fetch the details of a specific Confluence database?
  - id: deleteDatabase
    intent: Move a database to the trash
    question: How do I delete a Confluence database?
  phrasing_ops: 3
  slug: confluence-database-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Descendants API from Confluence — 5 operation(s) for descendants.
  name: Confluence Descendants API
  phrasing_intents:
  - id: getWhiteboardDescendants
    intent: List all descendants of a whiteboard
    question: What content is nested anywhere beneath a whiteboard?
  - id: getDatabaseDescendants
    intent: List all descendants of a database
    question: Which items sit at any level underneath a database in the content tree?
  - id: getSmartLinkDescendants
    intent: List all descendants of a Smart Link
    question: What content is nested at any depth under a Smart Link?
  - id: getFolderDescendants
    intent: List all descendants of a folder
    question: How do I see everything inside a folder, including nested subfolders?
  - id: getPageDescendants
    intent: List all descendants of a page
    question: Which pages and items are nested at any level below a page?
  phrasing_ops: 5
  slug: confluence-descendants-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Dynamic modules API from Confluence — 1 operation(s) for dynamic modules.
  name: Confluence Dynamic modules API
  phrasing_intents:
  - id: getModules
    intent: List an app's dynamically registered modules
    question: Which modules has my Connect app registered at runtime?
  - id: registerModules
    intent: Register dynamic modules for an app
    question: How do I register Connect modules at runtime instead of in the descriptor?
  - id: removeModules
    intent: Remove dynamically registered modules
    question: How do I unregister a dynamic module my app added?
  phrasing_ops: 3
  slug: confluence-dynamic-modules-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: APIs in this section can change without any prior deprecation notice.
  name: Confluence Experimental API
  phrasing_intents:
  - id: deletePageTree
    intent: Trash a page and all its descendants
    question: How do I move a whole page tree, including every child page, to the trash?
  - id: getLabelsForSpace
    intent: List a space's labels by space key
    question: How do I see the labels on a space when I only know its key?
  - id: addLabelsToSpace
    intent: Add labels to a space
    question: How do I tag a space with new labels without removing its existing ones?
  - id: deleteLabelFromSpace
    intent: Remove a label from a space
    question: How do I untag a space?
  phrasing_ops: 4
  slug: confluence-experimental-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Folder API from Confluence — 2 operation(s) for folder.
  name: Confluence Folder API
  phrasing_intents:
  - id: createFolder
    intent: Create a folder in a space
    question: How do I create a folder to organize pages in a Confluence space?
  - id: getFolderById
    intent: Get a folder by id
    question: What details can I get about a specific folder?
  - id: deleteFolder
    intent: Move a folder to the trash
    question: Can I restore a folder after deleting it?
  phrasing_ops: 3
  slug: confluence-folder-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: '**[WARNING](https://support.atlassian.com/user-management/docs/create-and-update-groups/) The standard Atlassian group names are default names only and can be edited or deleted.** For example, an admi'
  name: Confluence Group API
  phrasing_intents:
  - id: getGroups
    intent: List user groups
    question: What user groups exist on my Confluence site?
  - id: createGroup
    intent: Create a user group
    question: How do I create a new user group in Confluence?
  - id: getGroupByGroupId
    intent: Get a group by its id
    question: Can I look up a group's details from its group id?
  - id: removeGroupById
    intent: Delete a user group
    question: How do I delete a user group I no longer need?
  - id: searchGroups
    intent: Search groups by partial name
    question: Can I find groups by typing just part of their name?
  - id: getGroupMembersByGroupId
    intent: List the members of a group
    question: Who are the users in a particular Confluence group?
  - id: addUserToGroupByGroupId
    intent: Add a user to a group
    question: How do I add someone to a Confluence group?
  - id: removeMemberFromGroupByGroupId
    intent: Remove a user from a group
    question: How do I take a user out of a group?
  phrasing_ops: 8
  slug: confluence-group-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Label info API from Confluence — 1 operation(s) for label info.
  name: Confluence Label info API
  phrasing_intents:
  - id: getAllLabelContent
    intent: Get a label and the content tagged with it
    question: What pages and blog posts are tagged with a particular label?
  phrasing_ops: 1
  slug: confluence-label-info-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Like API from Confluence — 8 operation(s) for like.
  name: Confluence Like API
  phrasing_intents:
  - id: getBlogPostLikeCount
    intent: Count likes on a blog post
    question: How many likes has a blog post received?
  - id: getBlogPostLikeUsers
    intent: List who liked a blog post
    question: Who liked a particular blog post?
  - id: getPageLikeCount
    intent: Count likes on a page
    question: How many likes does a Confluence page have?
  - id: getPageLikeUsers
    intent: List who liked a page
    question: Who has liked a specific page?
  - id: getFooterLikeCount
    intent: Count likes on a footer comment
    question: How many likes did a footer comment at the bottom of a page get?
  - id: getFooterLikeUsers
    intent: List who liked a footer comment
    question: Who liked a footer comment on a page?
  - id: getInlineLikeCount
    intent: Count likes on an inline comment
    question: How many likes does an inline comment on highlighted text have?
  - id: getInlineLikeUsers
    intent: List who liked an inline comment
    question: Who liked an inline comment?
  phrasing_ops: 8
  slug: confluence-like-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Long-running task API from Confluence — 2 operation(s) for long-running task.
  name: Confluence Long-running task API
  phrasing_intents:
  - id: getTasks
    intent: List active long-running tasks
    question: Which long-running jobs, like space exports, are running on my site right now?
  - id: getTask
    intent: Check progress of a long-running task
    question: What percentage of my space export has completed?
  phrasing_ops: 2
  slug: confluence-long-running-task-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Operation API from Confluence — 11 operation(s) for operation.
  name: Confluence Operation API
  phrasing_intents:
  - id: getAttachmentOperations
    intent: See what I can do with an attachment
    question: Which actions am I allowed to take on an uploaded file?
  - id: getBlogPostOperations
    intent: See what I can do with a blog post
    question: Am I allowed to edit or delete a given blog post?
  - id: getCustomContentOperations
    intent: See what I can do with custom content
    question: Which actions are permitted on an app's custom content item?
  - id: getPageOperations
    intent: See what I can do with a page
    question: Am I allowed to edit a particular Confluence page?
  - id: getWhiteboardOperations
    intent: See what I can do with a whiteboard
    question: Which actions am I permitted to take on a whiteboard?
  - id: getDatabaseOperations
    intent: See what I can do with a database
    question: Which operations can I perform on a Confluence database?
  - id: getSmartLinkOperations
    intent: See what I can do with a Smart Link
    question: Which actions am I permitted on a Smart Link in the content tree?
  - id: getFolderOperations
    intent: See what I can do with a folder
    question: Which operations are permitted on a Confluence folder?
  phrasing_ops: 11
  slug: confluence-operation-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Redactions API from Confluence — 2 operation(s) for redactions.
  name: Confluence Redactions API
  phrasing_intents:
  - id: postRedactPage
    intent: Redact sensitive text in a page
    question: How do I black out sensitive text on a Confluence page?
  - id: postRedactBlog
    intent: Redact sensitive text in a blog post
    question: How do I redact confidential details from a blog post?
  phrasing_ops: 2
  slug: confluence-redactions-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Relation API from Confluence — 3 operation(s) for relation.
  name: Confluence Relation API
  phrasing_intents:
  - id: findTargetFromSource
    intent: Find what an entity is related to
    question: How do I list all the pages a user has marked as favourite?
  - id: getRelationship
    intent: Check if a relationship exists between two entities
    question: Has a user favourited a specific page?
  - id: createRelationship
    intent: Create a relationship such as a favourite
    question: How do I mark a page as a favourite for a user through the API?
  - id: deleteRelationship
    intent: Remove a relationship between two entities
    question: How do I unfavourite a page for a user?
  - id: findSourcesForTarget
    intent: Find who is related to a target entity
    question: Which users have a 'collaborator' relationship to a page?
  phrasing_ops: 5
  slug: confluence-relation-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Search API from Confluence — 2 operation(s) for search.
  name: Confluence Search API
  phrasing_intents:
  - id: searchByCQL
    intent: Search Confluence with CQL
    question: How do I search across pages, blogs, spaces and attachments with a CQL query?
  - id: searchUser
    intent: Search for users with CQL
    question: Can I find Confluence users by full name with a CQL user query?
  phrasing_ops: 2
  slug: confluence-search-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Settings API from Confluence — 3 operation(s) for settings.
  name: Confluence Settings API
  phrasing_intents:
  - id: getLookAndFeelSettings
    intent: Get look and feel settings
    question: What color scheme and styling does my site or a space use?
  - id: updateLookAndFeel
    intent: Choose which look and feel a space uses
    question: How do I switch a space between global, custom and theme styling?
  - id: updateLookAndFeelSettings
    intent: Customize look and feel colors and styles
    question: How do I change heading, link and menu colors for my site?
  - id: resetLookAndFeelSettings
    intent: Reset custom look and feel to defaults
    question: How do I undo my custom styling and go back to the defaults?
  - id: getSystemInfo
    intent: Get system info for the Confluence tenant
    question: What system information does my Confluence Cloud tenant report?
  phrasing_ops: 5
  slug: confluence-settings-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Smart Link API from Confluence — 2 operation(s) for smart link.
  name: Confluence Smart Link API
  phrasing_intents:
  - id: createSmartLink
    intent: Add a Smart Link to a space's content tree
    question: How do I add an external URL as a Smart Link in a space's page tree?
  - id: getSmartLinkById
    intent: Get a Smart Link by id
    question: How do I look up a Smart Link in the content tree?
  - id: deleteSmartLink
    intent: Move a Smart Link to the trash
    question: How do I remove a Smart Link from the content tree?
  phrasing_ops: 3
  slug: confluence-smart-link-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Space Permission Transition API from Confluence — 4 operation(s) for space permission transition.
  name: Confluence Space Permission Transition API
  phrasing_intents:
  - id: listSpacePermissionCombinations
    intent: List unassigned space permission combinations
    question: Which space permission combinations still are not mapped to a space role?
  - id: generateSpacePermissionCombinations
    intent: Refresh space permission combinations
    question: How do I scan the site for every unique space permission combination?
  - id: bulkAssignSpacePermissionRoles
    intent: Bulk assign roles to permission combinations
    question: How do I map old space permission combinations to roles in bulk?
  - id: bulkRemoveSpacePermissionAccess
    intent: Bulk remove access for permission combinations
    question: Can I strip all space permissions for certain permission combinations at once?
  - id: getSpacePermissionTransitionTaskStatus
    intent: Check a permission transition task's status
    question: Has my bulk role assignment or access removal finished yet?
  phrasing_ops: 5
  slug: confluence-space-permission-transition-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Space permissions API from Confluence — 5 operation(s) for space permissions.
  name: Confluence Space permissions API
  phrasing_intents:
  - id: addPermissionToSpace
    intent: Grant a user or group a space permission
    question: How do I give a group permission to edit pages in a space?
  - id: addCustomContentPermissions
    intent: Grant an app's custom content permissions in a space
    question: How does my app grant permissions on its own custom content type in a space?
  - id: removePermission
    intent: Revoke a space permission
    question: How do I take a permission away from someone in a space?
  - id: getSpacePermissionsAssignments
    intent: List the permission assignments in a space
    question: Who has which permissions in a given space?
  - id: getAvailableSpacePermissions
    intent: List all possible space permissions
    question: Which space permissions exist that a role can include?
  phrasing_ops: 5
  slug: confluence-space-permissions-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Space Properties API from Confluence — 2 operation(s) for space properties.
  name: Confluence Space Properties API
  phrasing_intents:
  - id: getSpaceProperties
    intent: List a space's properties
    question: What key-value properties are stored on a space?
  - id: createSpaceProperty
    intent: Add a property to a space
    question: How do I store custom key-value data on a space?
  - id: getSpacePropertyById
    intent: Get a space property
    question: How do I read one space property by its ID?
  - id: updateSpacePropertyById
    intent: Update a space property
    question: How do I change the value of an existing space property?
  - id: deleteSpacePropertyById
    intent: Delete a space property
    question: Can I remove a property I stored on a space?
  phrasing_ops: 5
  slug: confluence-space-properties-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Space Roles API from Confluence — 4 operation(s) for space roles.
  name: Confluence Space Roles API
  phrasing_intents:
  - id: getAvailableSpaceRoles
    intent: List the available space roles
    question: What space roles can I assign people in Confluence?
  - id: createSpaceRole
    intent: Create a custom space role
    question: How do I define a new space role with its own set of permissions?
  - id: getSpaceRolesById
    intent: Get a space role by id
    question: What permissions does a particular space role include?
  - id: updateSpaceRole
    intent: Update a space role
    question: How do I change the permissions in an existing space role?
  - id: deleteSpaceRole
    intent: Delete a space role
    question: How do I remove a custom space role I no longer need?
  - id: getSpaceRoleMode
    intent: Check the site's space role mode
    question: Is my Confluence site using role-based access control for spaces?
  - id: getSpaceRoleAssignments
    intent: List who holds which role in a space
    question: Who has which role in a particular space?
  - id: setSpaceRoleAssignments
    intent: Assign or remove roles for people in a space
    question: How do I give users or groups a role in a space in one call?
  phrasing_ops: 8
  slug: confluence-space-roles-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Space settings API from Confluence — 1 operation(s) for space settings.
  name: Confluence Space settings API
  phrasing_intents:
  - id: getSpaceSettings
    intent: Get a space's settings
    question: What settings are configured for a particular space?
  - id: updateSpaceSettings
    intent: Update a space's settings
    question: How do I turn route override on or off for a space?
  phrasing_ops: 2
  slug: confluence-space-settings-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Task API from Confluence — 2 operation(s) for task.
  name: Confluence Task API
  phrasing_intents:
  - id: getTasks
    intent: List tasks
    question: What tasks are assigned to me across Confluence?
  - id: getTaskById
    intent: Get a task
    question: How do I look up a single task by its ID?
  - id: updateTask
    intent: Mark a task complete or incomplete
    question: How do I tick off a task?
  phrasing_ops: 3
  slug: confluence-task-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Template API from Confluence — 4 operation(s) for template.
  name: Confluence Template API
  phrasing_intents:
  - id: updateContentTemplate
    intent: Update a content template
    question: How do I edit an existing page template's body or name?
  - id: createContentTemplate
    intent: Create a content template
    question: How do I add a new page template to a space?
  - id: getBlueprintTemplates
    intent: List blueprint templates
    question: Which blueprint templates are available in a space?
  - id: getContentTemplates
    intent: List content templates
    question: What user-created page templates exist on the site?
  - id: getContentTemplate
    intent: Get a content template
    question: What is in the body of a specific template?
  - id: removeTemplate
    intent: Delete or reset a template
    question: What happens when I remove a modified blueprint template?
  phrasing_ops: 6
  slug: confluence-template-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Themes API from Confluence — 4 operation(s) for themes.
  name: Confluence Themes API
  phrasing_intents:
  - id: getThemes
    intent: List the installed themes
    question: What themes are installed on my Confluence site?
  - id: getGlobalTheme
    intent: Get the site-wide theme
    question: Which theme is set globally for the whole site?
  - id: getTheme
    intent: Get a theme by key
    question: What's the name, description and icon of a particular theme?
  - id: getSpaceTheme
    intent: Get the theme set on a space
    question: Which theme is a space using?
  - id: setSpaceTheme
    intent: Apply a theme to a space
    question: How do I change the theme of a single space?
  - id: resetSpaceTheme
    intent: Reset a space to the global theme
    question: How do I make a space go back to the site's default look and feel?
  phrasing_ops: 6
  slug: confluence-themes-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The User API from Confluence — 3 operation(s) for user.
  name: Confluence User API
  phrasing_intents:
  - id: createBulkUserLookup
    intent: Look up several users by account id
    question: How can I get profile details for a batch of account ids at once?
  - id: checkAccessByEmail
    intent: Check which emails lack site access
    question: Which people on my list don't have access to the Confluence site yet?
  - id: inviteByEmail
    intent: Invite people to the site by email
    question: How do I invite a list of people to Confluence by email address?
  phrasing_ops: 3
  slug: confluence-user-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The User properties API from Confluence — 2 operation(s) for user properties.
  name: Confluence User properties API
  phrasing_intents:
  - id: getUserProperties
    intent: List a user's property keys
    question: What properties has an app stored against a Confluence user?
  - id: getUserProperty
    intent: Get a user property by key
    question: What value is saved under a specific property key for a user?
  - id: updateUserProperty
    intent: Update a user property's value
    question: How do I change the value of an existing user property?
  - id: createUserProperty
    intent: Create a user property
    question: How do I store a new custom setting on a user account?
  - id: deleteUserProperty
    intent: Delete a user property
    question: Can I remove a stored property from a user?
  phrasing_ops: 5
  slug: confluence-user-properties-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Users API from Confluence — 7 operation(s) for users.
  name: Confluence Users API
  phrasing_intents:
  - id: getUser
    intent: Look up a user by account ID
    question: How do I get someone's display name and profile picture from their account ID?
  - id: getAnonymousUser
    intent: See how anonymous users are shown
    question: What display name and avatar does Confluence show for anonymous visitors?
  - id: getCurrentUser
    intent: Get the logged-in user
    question: Who am I authenticated as in Confluence?
  - id: getGroupMembershipsForUser
    intent: List the groups a user belongs to
    question: Which groups is a given user a member of?
  - id: getBulkUserLookup
    intent: Look up several users at once
    question: Can I fetch details for many account IDs in a single request?
  - id: getPrivacyUnsafeUserEmail
    intent: Get a user's email address
    question: How do I get a user's email even if their profile hides it?
  - id: getPrivacyUnsafeUserEmailBulk
    intent: Get email addresses for several users
    question: Can I fetch email addresses for a batch of account IDs at once?
  phrasing_ops: 7
  slug: confluence-users-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Version API from Confluence — 12 operation(s) for version.
  name: Confluence Version API
  phrasing_intents:
  - id: getAttachmentVersions
    intent: List an attachment's versions
    question: How do I see every uploaded version of an attachment?
  - id: getAttachmentVersionDetails
    intent: Get one version of an attachment
    question: What changed in a specific version of an attachment?
  - id: getBlogPostVersions
    intent: List a blog post's versions
    question: Which edits have been made to a blog post over time?
  - id: getBlogPostVersionDetails
    intent: Get one version of a blog post
    question: Who made a specific revision to a blog post?
  - id: getPageVersions
    intent: List a page's versions
    question: How do I see the full edit history of a Confluence page?
  - id: getPageVersionDetails
    intent: Get one version of a page
    question: Who made a particular revision to a page, and what was the message?
  - id: getCustomContentVersions
    intent: List a custom content item's versions
    question: What's the revision history of a custom content item?
  - id: getCustomContentVersionDetails
    intent: Get one version of custom content
    question: Who changed a custom content item in a given version?
  phrasing_ops: 12
  slug: confluence-version-api
- baseURL: https://your-domain.atlassian.net/wiki/rest/api
  baseurl_source: declared
  description: The Whiteboard API from Confluence — 2 operation(s) for whiteboard.
  name: Confluence Whiteboard API
  phrasing_intents:
  - id: createWhiteboard
    intent: Create a whiteboard in a space
    question: How do I create a new Confluence whiteboard in a space?
  - id: getWhiteboardById
    intent: Get a whiteboard by id
    question: How do I fetch a specific whiteboard's details?
  - id: deleteWhiteboard
    intent: Move a whiteboard to the trash
    question: How do I delete a whiteboard?
  phrasing_ops: 3
  slug: confluence-whiteboard-api
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
artifact_total: 318
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
- group: commercial
  href: https://artifacts.apis.io/confluence/plans/confluence-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/confluence-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/confluence/finops/confluence-finops.yml
  title: ''
  type: FinOps
  url: finops/confluence-finops.yml
- group: other
  href: https://artifacts.apis.io/confluence/capabilities/confluence-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/confluence-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/confluence/overlays/confluence-rest-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/confluence-rest-v2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/confluence/overlays/confluence-rest-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/confluence-rest-v1-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/confluence/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/confluence/mcp/confluence-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/confluence-tool-crosswalk.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.atlassian.com/cloud/confluence/rest/v2/intro/
- group: operate
  title: ''
  type: Community
  url: https://community.atlassian.com/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.atlassian.com/roadmap/cloud
- group: start
  title: ''
  type: SignUp
  url: https://www.atlassian.com/try/cloud/signup?bundle=confluence
- group: build
  title: ''
  type: Postman
  url: https://developer.atlassian.com/cloud/confluence/confcloud.2.postman.json
- group: company
  title: ''
  type: Website
  url: https://www.atlassian.com/software/confluence
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/confluence/overview
- group: build
  href: https://artifacts.apis.io/confluence/packages/confluence-packages.yml
  title: ''
  type: Packages
  url: packages/confluence-packages.yml
- group: agent
  href: https://artifacts.apis.io/confluence/well-known/confluence-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/confluence-well-known.yml
- group: auth
  href: https://artifacts.apis.io/confluence/well-known/confluence-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/confluence-security.txt
- group: agent
  href: https://artifacts.apis.io/confluence/mcp/confluence-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/confluence-mcp.yml
- group: agent
  href: https://artifacts.apis.io/confluence/llms/confluence-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/confluence-llms.txt
- group: agent
  href: https://artifacts.apis.io/confluence/llms/confluence-llms-atlassian.txt
  title: ''
  type: LLMsTxt
  url: llms/confluence-llms-atlassian.txt
- group: other
  href: https://artifacts.apis.io/confluence/overlays/confluence-cloud-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/confluence-cloud-v2-overlay.yaml
- group: design
  href: https://artifacts.apis.io/confluence/conformance/confluence-conformance.yml
  title: ''
  type: Conformance
  url: conformance/confluence-conformance.yml
- group: design
  href: https://artifacts.apis.io/confluence/errors/confluence-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/confluence-problem-types.yml
- group: design
  href: https://artifacts.apis.io/confluence/lifecycle/confluence-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/confluence-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/confluence/conventions/confluence-conventions.yml
  title: ''
  type: Conventions
  url: conventions/confluence-conventions.yml
- group: operate
  href: https://artifacts.apis.io/confluence/changelog/confluence-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/confluence-changelog.yml
- group: build
  href: https://artifacts.apis.io/confluence/cli/confluence-cli.yml
  title: ''
  type: CLI
  url: cli/confluence-cli.yml
- group: design
  href: https://artifacts.apis.io/confluence/components/confluence-components.yml
  title: ''
  type: Components
  url: components/confluence-components.yml
- group: design
  href: https://artifacts.apis.io/confluence/data-model/confluence-data-model.yml
  title: ''
  type: DataModel
  url: data-model/confluence-data-model.yml
- group: start
  href: https://artifacts.apis.io/confluence/sandbox/confluence-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/confluence-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/confluence/agentic-access/confluence-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/confluence-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/confluence/security/confluence-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/confluence-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/confluence/security/confluence-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/confluence-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/confluence/security/confluence-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/confluence-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/confluence/authentication/confluence-authentication.yml
  title: ''
  type: Authentication
  url: authentication/confluence-authentication.yml
- group: auth
  href: https://artifacts.apis.io/confluence/scopes/confluence-scopes.yml
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
  href: https://artifacts.apis.io/confluence/openapi/_original/confluence-cloud-v2.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/confluence-cloud-v2.yml
- group: docs
  title: ''
  type: OpenAPI
  url: https://dac-static.atlassian.com/cloud/confluence/swagger.v3.json
- group: docs
  href: https://artifacts.apis.io/confluence/asyncapi/confluence-webhooks.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/confluence-webhooks.yml
- group: docs
  href: https://artifacts.apis.io/confluence/json-schema/confluence-page-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/confluence-page-schema.json
- group: docs
  href: https://artifacts.apis.io/confluence/json-schema/confluence-space-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/confluence-space-schema.json
- group: design
  href: https://artifacts.apis.io/confluence/json-ld/confluence-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/confluence-context.jsonld
- group: design
  href: https://artifacts.apis.io/confluence/json-ld/confluence-cloud-v2-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/confluence-cloud-v2-context.jsonld
- group: design
  href: https://artifacts.apis.io/confluence/arazzo/confluence-blog-post-retire-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/confluence-blog-post-retire-workflow.yml
- group: design
  href: https://artifacts.apis.io/confluence/arazzo/confluence-comment-moderation-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/confluence-comment-moderation-workflow.yml
- group: design
  href: https://artifacts.apis.io/confluence/arazzo/confluence-comment-thread-reply-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/confluence-comment-thread-reply-workflow.yml
- group: design
  href: https://artifacts.apis.io/confluence/arazzo/confluence-create-page-read-back-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/confluence-create-page-read-back-workflow.yml
- group: design
  href: https://artifacts.apis.io/confluence/arazzo/confluence-inline-comment-on-page-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/confluence-inline-comment-on-page-workflow.yml
- group: design
  href: https://artifacts.apis.io/confluence/arazzo/confluence-page-archive-retire-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/confluence-page-archive-retire-workflow.yml
- group: design
  href: https://artifacts.apis.io/confluence/arazzo/confluence-page-attachment-audit-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/confluence-page-attachment-audit-workflow.yml
- group: design
  href: https://artifacts.apis.io/confluence/arazzo/confluence-page-move-reparent-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/confluence-page-move-reparent-workflow.yml
- group: design
  href: https://artifacts.apis.io/confluence/arazzo/confluence-page-tree-export-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/confluence-page-tree-export-workflow.yml
- group: design
  href: https://artifacts.apis.io/confluence/arazzo/confluence-publish-blog-post-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/confluence-publish-blog-post-workflow.yml
- group: design
  href: https://artifacts.apis.io/confluence/arazzo/confluence-revise-blog-post-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/confluence-revise-blog-post-workflow.yml
- group: design
  href: https://artifacts.apis.io/confluence/arazzo/confluence-space-content-inventory-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/confluence-space-content-inventory-workflow.yml
- group: design
  href: https://artifacts.apis.io/confluence/arazzo/confluence-upsert-page-by-title-workflow.yml
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
- has_sources: true
  method: derived
  name: Confluence Finops
  primary_unit: user
  service_category: ''
  slug: confluence-finops
  template: false
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
  slug: atlassian-rovo-mcp
modified: '2026-06-20'
name: Confluence
nav: Providers
network: true
overview: 'Confluence publishes 117 API contracts indexed on the [APIs.io](https://apis.io/) network, including Content Properties API, Search API, Content API, and 114 more. Tagged areas include Collaboration, Content Management, Documentation, Knowledge Base, and Wiki.


  The Confluence catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 3 Spectral governance rulesets.


  Confluence''s developer surface includes API reference, signup flow, changelog, CLI, sandbox, authentication, developer portal, and 87 more developer resources.'
plans:
- name: Confluence Plans Pricing
  plan_count: 4
  slug: confluence-plans-pricing
- name: Confluence Price Estimates
  plan_count: 0
  slug: confluence-price-estimates
random_paper: 2
rate_limits:
- limit_count: 2
  name: Confluence Rate Limits
  slug: confluence-rate-limits
rules:
- authorship: generated
  effective_rule_count: 37
  extends:
  - spectral:asyncapi
  name: Confluence — asyncapi rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 8
  slug: confluence-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Confluence — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: confluence-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 59
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
  band: exemplar
  composite: 78.0
  coverage:
    artifact_dirs: 40
    catalog_earned: 61.5
    catalog_earned_first_party: 12.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 86.8
    contract_governance: 18.2
    contract_quality: 70.7
    developer_ergonomics: 94.6
    discoverability: 78.3
    operational_transparency: 55.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 76.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 10.9
      derived: 0
      marker_coverage: 90.9
      total: 55
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 43.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/confluence/confluence-2026-06-20T174854.png
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
- Knowledge Management
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
website: https://www.atlassian.com/software/confluence
---
