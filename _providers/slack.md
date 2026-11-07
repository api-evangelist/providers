---
access_model:
  confidence: medium
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 124
  human_in_the_loop: 5
  name: Slack Agentic Access
  operation_count: 218
  slug: slack-agentic-access
  summary_line: 218 operations · 124 acting · 5 human-in-the-loop
api_count: 32
apis:
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Slack Events API enables apps to respond to activities in Slack by subscribing to specific event types. Rather than polling for changes, apps receive HTTP POST payloads when subscribed events occu
  name: Slack Events API
  slug: slack-events-api
- description: The Slack SCIM API lets teams on Plus and Enterprise plans provision and manage user accounts and groups programmatically using the SCIM (System for Cross-domain Identity Management) protocol. It supp
  name: Slack SCIM API
  slug: slack-scim-api
- description: The Slack Audit Logs API is designed for building security information and event management (SIEM) tools for Slack Enterprise Grid organizations. It provides a read-only view of audit events happening
  name: Slack Audit Logs API
  slug: slack-audit-logs-api
- description: Slack Incoming Webhooks provide a simple way to post messages from external sources into Slack. Creating an incoming webhook gives you a unique URL to which you send a JSON payload with the message te
  name: Slack Incoming Webhooks API
  slug: slack-incoming-webhooks-api
- description: Slack Slash Commands allow users to invoke app functionality directly from the message composer box by typing a forward slash followed by a command name and optional parameters. When a user triggers a
  name: Slack Slash Commands API
  slug: slack-slash-commands-api
- description: The Slack App Manifest API provides methods to programmatically create, configure, update, export, validate, and delete Slack apps using JSON or YAML manifest files. Key methods include apps.manifest.
  name: Slack App Manifest API
  slug: slack-app-manifest-api
- description: The Slack Interactivity API encompasses the mechanisms by which Slack apps handle user interactions with interactive components such as buttons, menus, date pickers, modals, shortcuts, and other Block
  name: Slack Interactivity API
  slug: slack-interactivity-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Access API from Slack — 4 operation(s) for access.
  name: Slack Access API
  phrasing_intents:
  - id: getOauthAccess
    intent: Exchange an OAuth code on the legacy v1 flow
    question: How do I exchange a code for a token with the older v1 OAuth flow for classic apps?
  - id: getOauthV2Access
    intent: Exchange an OAuth code on the v2 flow
    question: What is the call to swap a v2 OAuth code for an access token when installing my app?
  phrasing_ops: 2
  slug: slack-access-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Add API from Slack — 9 operation(s) for add.
  name: Slack Add API
  phrasing_intents:
  - id: postAdminEmojiAdd
    intent: Add a custom emoji to the workspace
    question: How do I upload a custom emoji to our Slack workspace as an admin?
  - id: calls_add
    intent: Register a new call
    question: Can my video app register a call so it shows up in a channel?
  - id: calls_participants_add
    intent: Add participants to a registered call
    question: How do I show that new people have joined a call my app registered?
  - id: postFilesRemoteAdd
    intent: Add a file from a remote service
    question: Can I add a file that lives in my own service to Slack without uploading it?
  - id: postRemindersAdd
    intent: Create a reminder
    question: Can I set a reminder for myself or a teammate?
  - id: postStarsAdd
    intent: Star a message, file or channel
    question: How do I save a message for later by starring it?
  phrasing_ops: 6
  slug: slack-add-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Administrative API from Slack — 56 operation(s) for administrative.
  name: Slack Administrative API
  phrasing_intents:
  - id: postAdminAppsApprove
    intent: Approve an app for a workspace
    question: How can an org admin approve a pending app install request in Slack?
  - id: getAdminAppsApprovedList
    intent: List approved apps
    question: Which apps have already been approved for our org?
  - id: getAdminAppsRequestsList
    intent: List pending app install requests
    question: Which app installs are users waiting on an admin to review?
  - id: postAdminAppsRestrict
    intent: Restrict an app on a workspace
    question: How do I block an app from being installed on a workspace?
  - id: getAdminAppsRestrictedList
    intent: List restricted apps
    question: Which apps are blocked from installation in our org?
  - id: postAdminConversationsArchive
    intent: Archive a channel as an admin
    question: Can an org admin archive a private channel they aren't a member of?
  - id: postAdminConversationsConverttoprivate
    intent: Convert a public channel to private
    question: Is it possible to turn a public channel into a private one?
  - id: postAdminConversationsCreate
    intent: Create a channel as an admin
    question: Can an admin create an org-wide channel in an Enterprise org?
  phrasing_ops: 55
  slug: slack-administrative-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The AI API from Slack — 3 operation(s) for ai.
  name: Slack AI API
  phrasing_intents:
  - id: postAssistantThreadsSetStatus
    intent: Show a status on an assistant thread
    question: How do I show a 'thinking' indicator while my AI assistant works on a reply?
  - id: postAssistantThreadsSetSuggestedPrompts
    intent: Offer suggested prompts in an assistant thread
    question: Can my assistant offer clickable starter prompts to the user?
  - id: postAssistantThreadsSetTitle
    intent: Title an assistant thread
    question: How do I name an AI assistant conversation so it's easy to find later?
  phrasing_ops: 3
  slug: slack-ai-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Applications API from Slack — 13 operation(s) for applications.
  name: Slack Applications API
  phrasing_intents:
  - id: getAppsEventAuthorizationsList
    intent: List app installations that can see an event
    question: Which installations of my app is a given event visible to?
  - id: getAppsPermissionsInfo
    intent: Get the permissions my app has on a team
    question: What permissions does my app currently hold on this workspace?
  - id: getAppsPermissionsRequest
    intent: Request additional scopes for my app
    question: Can my app ask a user for extra scopes after it's installed?
  - id: getAppsPermissionsResourcesList
    intent: List resource grants my app holds
    question: Which channels and other resources has my app been granted access to?
  - id: getAppsPermissionsScopesList
    intent: List scopes my app has on a team
    question: What OAuth scopes has my app been granted on this team?
  - id: getAppsPermissionsUsersList
    intent: List user grants and their scopes
    question: Which users have granted my app user-level scopes?
  - id: getAppsPermissionsUsersRequest
    intent: Ask a user to grant user-level scopes
    question: Can my app pop up a permissions modal asking one user for a user scope?
  - id: getAppsUninstall
    intent: Uninstall my app from a workspace
    question: How do I uninstall my app from a workspace programmatically?
  phrasing_ops: 8
  slug: slack-applications-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Archive API from Slack — 2 operation(s) for archive.
  name: Slack Archive API
  phrasing_intents:
  - id: postConversationsArchive
    intent: Archive a conversation
    question: Can I archive a channel that's no longer in use?
  phrasing_ops: 1
  slug: slack-archive-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: Authentication and authorization methods
  name: Slack Auth API
  phrasing_intents:
  - id: authTest
    intent: Check who a token belongs to
    question: How can I verify my Slack token works and see which user and team it's for?
  - id: authRevoke
    intent: Revoke the current access token
    question: How do I revoke the token my app is using?
  phrasing_ops: 2
  slug: slack-auth-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Authentication API from Slack — 2 operation(s) for authentication.
  name: Slack Authentication API
  phrasing_intents:
  - id: postOpenIdConnectToken
    intent: Exchange a code for OpenID Connect tokens
    question: How does Sign in with Slack turn an authorization code into an ID token?
  - id: getOpenIdConnectUserInfo
    intent: Get the signed-in user's identity
    question: What identity details do I get about someone who used Sign in with Slack?
  phrasing_ops: 2
  slug: slack-authentication-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Automation API from Slack — 5 operation(s) for automation.
  name: Slack Automation API
  phrasing_intents:
  - id: postFunctionsCompleteSuccess
    intent: Mark a custom workflow step as succeeded
    question: How does my custom function tell the workflow it finished successfully?
  - id: postFunctionsCompleteError
    intent: Mark a custom workflow step as failed
    question: What should my custom function do when it hits an error mid-workflow?
  - id: postFunctionsDistributionsPermissionsAdd
    intent: Grant users access to a custom function
    question: How do I let more people use a custom function in their workflows?
  - id: getFunctionsDistributionsPermissionsList
    intent: List who can use a custom function
    question: Who currently has permission to use my custom function?
  - id: postFunctionsDistributionsPermissionsRemove
    intent: Revoke users' access to a custom function
    question: Can I take away someone's ability to use my custom function?
  phrasing_ops: 5
  slug: slack-automation-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Bookmarks API from Slack — 4 operation(s) for bookmarks.
  name: Slack Bookmarks API
  phrasing_intents:
  - id: postBookmarksAdd
    intent: Add a bookmark to a channel
    question: How do I pin a useful link to the bookmarks bar of a channel?
  - id: postBookmarksEdit
    intent: Edit an existing channel bookmark
    question: Can I change the link or title of a bookmark that is already in a channel?
  - id: getBookmarksList
    intent: List a channel's bookmarks
    question: What bookmarks are saved in a channel?
  - id: postBookmarksRemove
    intent: Remove a bookmark from a channel
    question: How do I take an outdated bookmark off a channel?
  phrasing_ops: 4
  slug: slack-bookmarks-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Bots API from Slack — 1 operation(s) for bots.
  name: Slack Bots API
  phrasing_intents:
  - id: getBotsInfo
    intent: Get information about a bot user
    question: What app and name belong to a bot ID I saw in a message?
  phrasing_ops: 1
  slug: slack-bots-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Calls API from Slack — 6 operation(s) for calls.
  name: Slack Calls API
  phrasing_intents:
  - id: calls_end
    intent: End a call
    question: How does my app mark a Slack call as ended?
  - id: calls_info
    intent: Get details about a call
    question: What information is available about a registered call?
  - id: calls_participants_remove
    intent: Register participants who left a call
    question: How do I tell Slack that someone left a call?
  - id: calls_update
    intent: Update a call's title or join links
    question: Can I change a call's title after it started?
  phrasing_ops: 4
  slug: slack-calls-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Canvases API from Slack — 6 operation(s) for canvases.
  name: Slack Canvases API
  phrasing_intents:
  - id: postCanvasesCreate
    intent: Create a canvas
    question: How do I create a new standalone canvas in Slack?
  - id: postCanvasesDelete
    intent: Delete a canvas
    question: Can I permanently delete a canvas I no longer need?
  - id: postCanvasesEdit
    intent: Edit a canvas's content
    question: How can I insert, replace or delete sections in an existing canvas?
  - id: postCanvasesAccessDelete
    intent: Remove people's access to a canvas
    question: How do I take away someone's access to a canvas?
  - id: postCanvasesAccessSet
    intent: Grant view or edit access to a canvas
    question: Can I give a channel read-only access to a canvas?
  - id: postCanvasesSectionsLookup
    intent: Find sections in a canvas
    question: How do I locate a specific section of a canvas before editing it?
  phrasing_ops: 6
  slug: slack-canvases-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Chat API from Slack — 10 operation(s) for chat.
  name: Slack Chat API
  phrasing_intents:
  - id: postChatDelete
    intent: Delete a posted message
    question: How do I delete a message my bot already posted?
  - id: postChatDeletescheduledmessage
    intent: Cancel a scheduled message
    question: Can I cancel a message I scheduled before it gets sent?
  - id: getChatGetpermalink
    intent: Get a permalink to a message
    question: How do I get a shareable link to a specific message?
  - id: postChatMemessage
    intent: Post a /me status-style message
    question: Can I post an italic /me style action message in a channel?
  - id: postChatPostephemeral
    intent: Send a message only one user can see
    question: How do I send a message in a channel that only one person can see?
  - id: postChatPostmessage
    intent: Send a message to a channel
    question: How do I post a message to a Slack channel from my app?
  - id: postChatSchedulemessage
    intent: Schedule a message for later
    question: Can I schedule a message to post at a specific time in the future?
  - id: getChatScheduledmessagesList
    intent: List scheduled messages
    question: What messages are currently scheduled to go out?
  phrasing_ops: 10
  slug: slack-chat-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Close API from Slack — 1 operation(s) for close.
  name: Slack Close API
  phrasing_intents:
  - id: postConversationsClose
    intent: Close a direct message
    question: Can my app close a DM so it leaves the sidebar?
  phrasing_ops: 1
  slug: slack-close-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Comments API from Slack — 1 operation(s) for comments.
  name: Slack Comments API
  phrasing_intents:
  - id: postFilesCommentsDelete
    intent: Delete a comment on a file
    question: Can I remove a comment someone left on a file?
  phrasing_ops: 1
  slug: slack-comments-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Complete API from Slack — 1 operation(s) for complete.
  name: Slack Complete API
  phrasing_intents:
  - id: postRemindersComplete
    intent: Mark a reminder as complete
    question: Is there a way to mark a reminder as done?
  phrasing_ops: 1
  slug: slack-complete-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Connect API from Slack — 1 operation(s) for connect.
  name: Slack Connect API
  phrasing_intents:
  - id: getRtmConnect
    intent: Start a Real Time Messaging session
    question: What starts a Real Time Messaging websocket session for my bot?
  phrasing_ops: 1
  slug: slack-connect-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Conversations API from Slack — 36 operation(s) for conversations.
  name: Slack Conversations API
  phrasing_intents:
  - id: postConversationsCreate
    intent: Create a new channel
    question: How do I create a new Slack channel from code?
  - id: getConversationsHistory
    intent: Read a channel's message history
    question: What messages were posted in a channel over the last few days?
  - id: getConversationsInfo
    intent: Get details about a channel
    question: What are the settings and topic of a particular channel?
  - id: postConversationsInvite
    intent: Invite users to a channel
    question: How do I add several teammates to a channel at once?
  - id: postConversationsJoin
    intent: Join an existing channel
    question: Can my app join a public channel on its own?
  - id: postConversationsKick
    intent: Remove a user from a channel
    question: How do I remove someone from a channel?
  - id: postConversationsLeave
    intent: Leave a channel
    question: Can my bot leave a channel it no longer needs to be in?
  - id: getConversationsList
    intent: List channels in the workspace
    question: What channels exist in our workspace?
  phrasing_ops: 18
  slug: slack-conversations-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Create API from Slack — 7 operation(s) for create.
  name: Slack Create API
  phrasing_intents:
  - id: postUsergroupsCreate
    intent: Create a user group
    question: Can I set up a user group so people can @mention a whole team?
  phrasing_ops: 1
  slug: slack-create-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Deletes API from Slack — 5 operation(s) for deletes.
  name: Slack Deletes API
  phrasing_intents:
  - id: postFilesDelete
    intent: Delete a file
    question: How do I delete a file I uploaded to Slack?
  - id: postRemindersDelete
    intent: Delete a reminder
    question: Can I cancel a reminder I set by mistake?
  phrasing_ops: 2
  slug: slack-deletes-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Disables API from Slack — 1 operation(s) for disables.
  name: Slack Disables API
  phrasing_intents:
  - id: postUsergroupsDisable
    intent: Disable a user group
    question: Can I deactivate a user group nobody uses anymore?
  phrasing_ops: 1
  slug: slack-disables-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Disturb API from Slack — 5 operation(s) for disturb.
  name: Slack Disturb API
  phrasing_intents:
  - id: postDndEnddnd
    intent: End my Do Not Disturb session
    question: How do I turn off Do Not Disturb right now?
  - id: postDndEndsnooze
    intent: End my notification snooze
    question: Can I stop snoozing notifications before the timer runs out?
  - id: getDndInfo
    intent: Get a user's Do Not Disturb status
    question: Is a particular teammate in Do Not Disturb at the moment?
  - id: postDndSetsnooze
    intent: Snooze notifications for some minutes
    question: How do I snooze notifications for the next hour?
  - id: getDndTeaminfo
    intent: Get DND status for several users
    question: Which of my teammates are in Do Not Disturb right now?
  phrasing_ops: 5
  slug: slack-disturb-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: Do Not Disturb management
  name: Slack Dnd API
  phrasing_intents:
  - id: dndSetSnooze
    intent: Turn on Do Not Disturb for some minutes
    question: How do I snooze my notifications for the next hour?
  - id: dndInfo
    intent: Check a user's Do Not Disturb status
    question: Is a teammate in Do Not Disturb mode right now?
  phrasing_ops: 2
  slug: slack-dnd-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Emoji API from Slack — 1 operation(s) for emoji.
  name: Slack Emoji API
  phrasing_intents:
  - id: emojiList
    intent: List a team's custom emoji
    question: Which custom emoji has our workspace added?
  phrasing_ops: 1
  slug: slack-emoji-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Enables API from Slack — 1 operation(s) for enables.
  name: Slack Enables API
  phrasing_intents:
  - id: postUsergroupsEnable
    intent: Re-enable a disabled user group
    question: What does it take to turn a disabled user group back on?
  phrasing_ops: 1
  slug: slack-enables-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Exchange API from Slack — 1 operation(s) for exchange.
  name: Slack Exchange API
  phrasing_intents:
  - id: getMigrationExchange
    intent: Map local user IDs to global Enterprise Grid IDs
    question: After migrating to Enterprise Grid, how do I translate old local user IDs to global ones?
  phrasing_ops: 1
  slug: slack-exchange-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Files API from Slack — 13 operation(s) for files.
  name: Slack Files API
  phrasing_intents:
  - id: getFilesInfo
    intent: Get details about a file
    question: What are the details of a file that was uploaded, like its name, size and who shared it?
  - id: getFilesList
    intent: List files shared in the workspace
    question: Which files has a given user uploaded?
  - id: getFilesRemoteInfo
    intent: Get details about one remote file
    question: How do I look up a remote file I added from my own service?
  - id: getFilesRemoteList
    intent: List remote files added to the workspace
    question: Which remote files from external services have been added to Slack?
  - id: postFilesRemoteRemove
    intent: Remove a remote file
    question: Can I remove a remote file my app added once it is deleted on our side?
  - id: getFilesRemoteShare
    intent: Share a remote file into channels
    question: How do I post a remote file into a channel so people can see it?
  - id: postFilesRemoteUpdate
    intent: Update an existing remote file
    question: Can I change the title or URL of a remote file after adding it?
  - id: postFilesRevokepublicurl
    intent: Revoke a file's public sharing link
    question: How do I stop a file from being publicly accessible outside the workspace?
  phrasing_ops: 11
  slug: slack-files-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Get API from Slack — 76 operation(s) for get.
  name: Slack Get API
  phrasing_intents:
  - id: getAuthRevoke
    intent: Revoke an access token
    question: How do I revoke a Slack token my app no longer needs?
  - id: getAuthTest
    intent: Check a token's authentication and identity
    question: Is my bot token still valid, and which user and workspace does it belong to?
  - id: getDialogOpen
    intent: Open a legacy dialog for a user
    question: How do I pop up a dialog form after a user clicks a button or runs a slash command?
  - id: getOauthToken
    intent: Exchange an OAuth code for a workspace token
    question: How do I turn a temporary OAuth verifier code into a workspace token for a workspace app?
  - id: getRemindersInfo
    intent: Get details of one reminder
    question: What are the details of a specific reminder, like its text and when it fires?
  - id: getRemindersList
    intent: List a user's reminders
    question: Which reminders have been created by me or for me?
  - id: getStarsList
    intent: List a user's starred items
    question: What messages, files and channels have I starred?
  - id: getTeamAccesslogs
    intent: Get the workspace access logs
    question: Who has logged into our workspace, from which IPs and devices?
  phrasing_ops: 25
  slug: slack-get-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Groups API from Slack — 7 operation(s) for groups.
  name: Slack Groups API
  phrasing_intents:
  - id: postUsergroupsUpdate
    intent: Update a user group's details
    question: Can I change a user group's name, handle or description?
  - id: postUsergroupsUsersUpdate
    intent: Replace the members of a user group
    question: How do I set exactly who belongs to a user group?
  phrasing_ops: 2
  slug: slack-groups-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Lists API from Slack — 34 operation(s) for lists.
  name: Slack Lists API
  phrasing_intents:
  - id: postSlackListsCreate
    intent: Create a new Slack List
    question: How do I create a Slack List to track tasks for a team?
  - id: postSlackListsUpdate
    intent: Rename or reconfigure a list
    question: Can I rename a list after it has been created?
  - id: postSlackListsItemsCreate
    intent: Add a row to a list
    question: How do I add a new task row to an existing list?
  - id: postSlackListsItemsUpdate
    intent: Update a row in a list
    question: Can I change a field on an item that is already in a list, like marking it done?
  - id: postSlackListsItemsDelete
    intent: Delete a row from a list
    question: How do I remove a single item from a list?
  - id: getSlackListsItemsList
    intent: List the items in a list
    question: What rows are currently in a given list?
  phrasing_ops: 6
  slug: slack-lists-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Pins API from Slack — 3 operation(s) for pins.
  name: Slack Pins API
  phrasing_intents:
  - id: pinsAdd
    intent: Pin a message to a channel
    question: How do I pin an important message so everyone in the channel can find it?
  - id: pinsRemove
    intent: Unpin a message from a channel
    question: Can I unpin a message that is no longer relevant?
  - id: pinsList
    intent: List pinned items in a channel
    question: What has been pinned in a channel?
  phrasing_ops: 3
  slug: slack-pins-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Post API from Slack — 94 operation(s) for post.
  name: Slack Post API
  phrasing_intents:
  - id: postStarsRemove
    intent: Remove a star from an item
    question: How do I unstar a message I saved earlier?
  - id: postUsersDeletephoto
    intent: Delete my profile photo
    question: Can I remove my profile picture and go back to the default avatar?
  - id: postUsersProfileSet
    intent: Update a user's profile fields
    question: How do I change my status or title on my profile?
  - id: postUsersSetactive
    intent: Mark a user as active (deprecated)
    question: Does the old set-active call still do anything?
  - id: postUsersSetphoto
    intent: Set my profile photo
    question: How do I upload a new profile picture?
  - id: postUsersSetpresence
    intent: Set my presence to auto or away
    question: Can I force my status to away?
  phrasing_ops: 6
  slug: slack-post-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Reactions API from Slack — 4 operation(s) for reactions.
  name: Slack Reactions API
  phrasing_intents:
  - id: reactionsAdd
    intent: Add an emoji reaction to a message
    question: How do I react to a message with an emoji through the API?
  - id: reactionsRemove
    intent: Remove an emoji reaction
    question: Can I take back a reaction I added by mistake?
  - id: reactionsGet
    intent: Get the reactions on one item
    question: Which emoji reactions has a specific message received?
  - id: reactionsList
    intent: List reactions a user has made
    question: What has a given user reacted to lately?
  phrasing_ops: 4
  slug: slack-reactions-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: Create and manage reminders
  name: Slack Reminders API
  phrasing_intents:
  - id: remindersAdd
    intent: Create a reminder for a user
    question: How do I set a Slack reminder for a teammate?
  - id: remindersList
    intent: List all reminders
    question: What reminders do I have set?
  phrasing_ops: 2
  slug: slack-reminders-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Search API from Slack — 3 operation(s) for search.
  name: Slack Search API
  phrasing_intents:
  - id: searchMessages
    intent: Search messages
    question: How do I find messages from a certain person in a specific channel?
  - id: searchFiles
    intent: Search files
    question: Where's that spreadsheet someone shared last month?
  phrasing_ops: 2
  slug: slack-search-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: Access workspace information
  name: Slack Team API
  phrasing_intents:
  - id: teamInfo
    intent: Get information about the team
    question: What details can I pull about my current workspace?
  phrasing_ops: 1
  slug: slack-team-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Users API from Slack — 32 operation(s) for users.
  name: Slack Users API
  phrasing_intents:
  - id: usersList
    intent: List all users in the workspace
    question: How do I pull a full member directory from Slack?
  - id: usersInfo
    intent: Get information about a user
    question: What is a user's timezone and are they an admin?
  - id: usersLookupByEmail
    intent: Find a user by email address
    question: Which account belongs to a given email address?
  - id: usersGetPresence
    intent: Check whether a user is online
    question: Is a teammate active right now or away?
  phrasing_ops: 4
  slug: slack-users-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Views API from Slack — 4 operation(s) for views.
  name: Slack Views API
  phrasing_intents:
  - id: viewsOpen
    intent: Open a modal for a user
    question: How do I pop up a modal after someone runs my slash command?
  - id: viewsUpdate
    intent: Update an open modal view
    question: Can I change the contents of a modal that's already open?
  - id: viewsPublish
    intent: Publish a user's App Home tab
    question: Can my app show a custom Home tab to each user?
  phrasing_ops: 3
  slug: slack-views-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: The Workflows API from Slack — 5 operation(s) for workflows.
  name: Slack Workflows API
  phrasing_intents:
  - id: getWorkflowsStepcompleted
    intent: Report a workflow step as completed
    question: How does my app tell Workflow Builder that its step finished?
  - id: getWorkflowsStepfailed
    intent: Report a workflow step as failed
    question: What should my app call when its workflow step cannot finish?
  - id: getWorkflowsUpdatestep
    intent: Save the configuration of a workflow step
    question: How do I save the inputs a user configured for my workflow step?
  phrasing_ops: 3
  slug: slack-workflows-api
- baseURL: https://slack.com/api
  baseurl_source: declared
  description: Manage user groups
  name: Slack User Groups API
  slug: slack-user-groups-api
arazzos:
- description: Add a link bookmark to a channel and post a message about it.
  name: Slack Add a Channel Bookmark and Announce It
  slug: slack-add-bookmark-announce-workflow
- description: Create a reminder for a user and read it back to confirm.
  name: Slack Add a Reminder and Confirm It
  slug: slack-add-reminder-for-user-workflow
- description: Post a final notice to a channel and then archive it.
  name: Slack Announce and Archive a Channel
  slug: slack-archive-channel-announce-workflow
- description: List the workspace channels and post a summary message to a channel.
  name: Slack Audit Channels and Post a Summary
  slug: slack-audit-channels-post-summary-workflow
- description: Create a new channel, invite a set of users, and post a kickoff message.
  name: Slack Create Channel, Invite Members, and Announce
  slug: slack-create-channel-invite-announce-workflow
- description: Create a user group, assign members, and confirm the membership list.
  name: Slack Create a User Group and Assign Members
  slug: slack-create-usergroup-assign-members-workflow
- description: Look up a user by email, open a direct message channel, and post a message.
  name: Slack Find User by Email and Direct Message Them
  slug: slack-find-user-dm-message-workflow
- description: Resolve a user by email, invite them to a channel, and welcome them.
  name: Slack Look Up a User and Invite Them to a Channel
  slug: slack-lookup-invite-to-channel-workflow
- description: Get a message permalink and send it to a user in a direct message.
  name: Slack Share a Message Permalink in a Direct Message
  slug: slack-permalink-share-to-dm-workflow
- description: Post a message, seed two reaction options, and read back the reaction tally.
  name: Slack Post a Poll Message, Seed Reactions, and Read Tally
  slug: slack-post-message-get-reactions-workflow
- description: Post a message to a channel, add a reaction emoji, and pin it.
  name: Slack Post a Message, React, and Pin It
  slug: slack-post-react-pin-workflow
- description: Post a parent message and then post a threaded reply under it.
  name: Slack Post a Message and Reply in Thread
  slug: slack-post-thread-reply-workflow
- description: Post an initial status message and then edit it in place with an update.
  name: Slack Post a Message and Update It Later
  slug: slack-post-update-message-workflow
- description: Fetch a channel's recent history and mark the channel read up to the latest message.
  name: Slack Read Channel History and Mark It Read
  slug: slack-read-history-mark-read-workflow
- description: Resolve a user by email, remove them from a channel, and log the change.
  name: Slack Remove a Member from a Channel and Log It
  slug: slack-remove-member-announce-workflow
- description: Rename a channel and post a message announcing the new name.
  name: Slack Rename a Channel and Announce the Change
  slug: slack-rename-channel-announce-workflow
- description: Schedule a future message to a channel and confirm it appears in the queue.
  name: Slack Schedule a Message and Verify It
  slug: slack-schedule-message-verify-workflow
- description: Search messages for a query and add a reaction to the best match.
  name: Slack Search Messages and React to the Top Match
  slug: slack-search-message-react-workflow
- description: Set a channel's topic and purpose, then announce the update.
  name: Slack Set Channel Topic and Purpose
  slug: slack-set-channel-topic-purpose-workflow
- description: Set a custom status, snooze do not disturb, and post a heads up message.
  name: Slack Set Status, Snooze Notifications, and Notify a Channel
  slug: slack-set-status-snooze-notify-workflow
- description: Upload a file to a channel and post a follow up message referencing it.
  name: Slack Upload a File and Announce It
  slug: slack-upload-file-share-workflow
- description: Fetch a user's profile, open a DM, and post a personalized greeting.
  name: Slack Look Up a User and Send a Personalized Greeting
  slug: slack-user-info-dm-greeting-workflow
artifact_total: 309
asyncapis:
- description: The Slack Events API enables apps to respond to activities in Slack by subscribing to specific event types. Rather than polling for changes, apps receive HTTP POST payloads when subscribed events occu
  name: Slack Events API
  slug: slack-events-asyncapi
collections:
- collection_type: postman
  name: Slack Admin API
  slug: postman-slack-admin
- collection_type: postman
  name: Slack Apps API
  slug: postman-slack-apps
- collection_type: postman
  name: Slack Assistant API
  slug: postman-slack-assistant
- collection_type: postman
  name: Slack Auth API
  slug: postman-slack-auth
- collection_type: postman
  name: Slack Bookmarks API
  slug: postman-slack-bookmarks
- collection_type: postman
  name: Slack Bots API
  slug: postman-slack-bots
- collection_type: postman
  name: Slack Calls API
  slug: postman-slack-calls
- collection_type: postman
  name: Slack Canvases API
  slug: postman-slack-canvases
- collection_type: postman
  name: Slack Chat API
  slug: postman-slack-chat
- collection_type: postman
  name: Slack Conversations API
  slug: postman-slack-conversations
- collection_type: postman
  name: Slack Dialog API
  slug: postman-slack-dialog
- collection_type: postman
  name: Slack DND API
  slug: postman-slack-dnd
- collection_type: postman
  name: Slack Emoji API
  slug: postman-slack-emoji
- collection_type: postman
  name: Slack Files API
  slug: postman-slack-files
- collection_type: postman
  name: Slack Functions API
  slug: postman-slack-functions
- collection_type: postman
  name: Slack Lists API
  slug: postman-slack-lists
- collection_type: postman
  name: Slack Migration API
  slug: postman-slack-migration
- collection_type: postman
  name: Slack OAuth API
  slug: postman-slack-oauth
- collection_type: postman
  name: Slack OpenID Connect API
  slug: postman-slack-openid-connect
- collection_type: postman
  name: Slack Pins API
  slug: postman-slack-pins
- collection_type: postman
  name: Slack Reactions API
  slug: postman-slack-reactions
- collection_type: postman
  name: Slack Reminders API
  slug: postman-slack-reminders
- collection_type: postman
  name: Slack RTM API
  slug: postman-slack-rtm
- collection_type: postman
  name: Slack Search API
  slug: postman-slack-search
- collection_type: postman
  name: Slack Stars API
  slug: postman-slack-stars
- collection_type: postman
  name: Slack Team API
  slug: postman-slack-team
- collection_type: postman
  name: Slack Tests API
  slug: postman-slack-test-api
- collection_type: postman
  name: Slack User Groups API
  slug: postman-slack-usergroups
- collection_type: postman
  name: Slack Users API
  slug: postman-slack-users
- collection_type: postman
  name: Slack Views API
  slug: postman-slack-views
- collection_type: postman
  name: Slack Web API
  slug: postman-slack-web-api
- collection_type: postman
  name: Slack Workflows
  slug: postman-slack-workflows
- collection_type: open
  name: Slack Admin Access API
  slug: open-slack-access-api
- collection_type: open
  name: Slack Admin Access Add API
  slug: open-slack-add-api
- collection_type: open
  name: Slack Admin API
  slug: open-slack-admin
- collection_type: open
  name: Slack Admin Access Administrative API
  slug: open-slack-administrative-api
- collection_type: open
  name: Slack Admin Access AI API
  slug: open-slack-ai-api
- collection_type: open
  name: Slack Admin Access Applications API
  slug: open-slack-applications-api
- collection_type: open
  name: Slack Admin Access Approve API
  slug: open-slack-approve-api
- collection_type: open
  name: Slack Admin Access Approved API
  slug: open-slack-approved-api
- collection_type: open
  name: Slack Apps API
  slug: open-slack-apps
- collection_type: open
  name: Slack Admin Access Archive API
  slug: open-slack-archive-api
- collection_type: open
  name: Slack Admin Access Assign API
  slug: open-slack-assign-api
- collection_type: open
  name: Slack Assistant API
  slug: open-slack-assistant
- collection_type: open
  name: Slack Admin Access Assistants API
  slug: open-slack-assistants-api
- collection_type: open
  name: Slack Admin Access Auth API
  slug: open-slack-auth-api
- collection_type: open
  name: Slack Auth API
  slug: open-slack-auth
- collection_type: open
  name: Slack Admin Access Authentication API
  slug: open-slack-authentication-api
- collection_type: open
  name: Slack Admin Access Authorization API
  slug: open-slack-authorization-api
- collection_type: open
  name: Slack Admin Access Automation API
  slug: open-slack-automation-api
- collection_type: open
  name: Slack Admin Access Bookmarks API
  slug: open-slack-bookmarks-api
- collection_type: open
  name: Slack Bookmarks API
  slug: open-slack-bookmarks
- collection_type: open
  name: Slack Admin Access Bots API
  slug: open-slack-bots-api
- collection_type: open
  name: Slack Bots API
  slug: open-slack-bots
- collection_type: open
  name: Slack Admin Access Calls API
  slug: open-slack-calls-api
- collection_type: open
  name: Slack Calls API
  slug: open-slack-calls
- collection_type: open
  name: Slack Admin Access Canvases API
  slug: open-slack-canvases-api
- collection_type: open
  name: Slack Canvases API
  slug: open-slack-canvases
- collection_type: open
  name: Slack Admin Access Chat API
  slug: open-slack-chat-api
- collection_type: open
  name: Slack Chat API
  slug: open-slack-chat
- collection_type: open
  name: Slack Admin Access Close API
  slug: open-slack-close-api
- collection_type: open
  name: Slack Admin Access Comments API
  slug: open-slack-comments-api
- collection_type: open
  name: Slack Admin Access Complete API
  slug: open-slack-complete-api
- collection_type: open
  name: Slack Admin Access Connect API
  slug: open-slack-connect-api
- collection_type: open
  name: Slack Admin Access Conversations API
  slug: open-slack-conversations-api
- collection_type: open
  name: Slack Conversations API
  slug: open-slack-conversations
- collection_type: open
  name: Slack Admin Access Create API
  slug: open-slack-create-api
- collection_type: open
  name: Slack Admin Access Delete API
  slug: open-slack-delete-api
- collection_type: open
  name: Slack Admin Access Deletes API
  slug: open-slack-deletes-api
- collection_type: open
  name: Slack Admin Access Deny API
  slug: open-slack-deny-api
- collection_type: open
  name: Slack Dialog API
  slug: open-slack-dialog
- collection_type: open
  name: Slack Admin Access Disables API
  slug: open-slack-disables-api
- collection_type: open
  name: Slack Admin Access Disturb API
  slug: open-slack-disturb-api
- collection_type: open
  name: Slack Admin Access Dnd API
  slug: open-slack-dnd-api
- collection_type: open
  name: Slack DND API
  slug: open-slack-dnd
- collection_type: open
  name: Slack Admin Access Do API
  slug: open-slack-do-api
- collection_type: open
  name: Slack Admin Access Documents API
  slug: open-slack-documents-api
- collection_type: open
  name: Slack Admin Access Edit API
  slug: open-slack-edit-api
- collection_type: open
  name: Slack Admin Access Emoji API
  slug: open-slack-emoji-api
- collection_type: open
  name: Slack Emoji API
  slug: open-slack-emoji
- collection_type: open
  name: Slack Admin Access Enables API
  slug: open-slack-enables-api
- collection_type: open
  name: Slack Admin Access End API
  slug: open-slack-end-api
- collection_type: open
  name: Slack Admin Access Events API
  slug: open-slack-events-api
- collection_type: open
  name: Slack Admin Access Exchange API
  slug: open-slack-exchange-api
- collection_type: open
  name: Slack Admin Access Files API
  slug: open-slack-files-api
- collection_type: open
  name: Slack Files API
  slug: open-slack-files
- collection_type: open
  name: Slack Admin Access Functions API
  slug: open-slack-functions-api
- collection_type: open
  name: Slack Functions API
  slug: open-slack-functions
- collection_type: open
  name: Slack Admin Access Get API
  slug: open-slack-get-api
- collection_type: open
  name: Slack Admin Access Groups API
  slug: open-slack-groups-api
- collection_type: open
  name: Slack Admin Access History API
  slug: open-slack-history-api
- collection_type: open
  name: Slack Admin Access Identity API
  slug: open-slack-identity-api
- collection_type: open
  name: Slack Admin Access Info API
  slug: open-slack-info-api
- collection_type: open
  name: Slack Admin Access Information API
  slug: open-slack-information-api
- collection_type: open
  name: Slack Admin Access Invalidate API
  slug: open-slack-invalidate-api
- collection_type: open
  name: Slack Admin Access Invites API
  slug: open-slack-invites-api
- collection_type: open
  name: Slack Admin Access Items API
  slug: open-slack-items-api
- collection_type: open
  name: Slack Admin Access Join API
  slug: open-slack-join-api
- collection_type: open
  name: Slack Admin Access Kick API
  slug: open-slack-kick-api
- collection_type: open
  name: Slack Admin Access Leave API
  slug: open-slack-leave-api
- collection_type: open
  name: Slack Admin Access Lists API
  slug: open-slack-lists-api
- collection_type: open
  name: Slack Lists API
  slug: open-slack-lists
- collection_type: open
  name: Slack Admin Access Lookup API
  slug: open-slack-lookup-api
- collection_type: open
  name: Slack Admin Access Mark API
  slug: open-slack-mark-api
- collection_type: open
  name: Slack Admin Access Members API
  slug: open-slack-members-api
- collection_type: open
  name: Slack Admin Access Messages API
  slug: open-slack-messages-api
- collection_type: open
  name: Slack Migration API
  slug: open-slack-migration
- collection_type: open
  name: Slack Admin Access Migrations API
  slug: open-slack-migrations-api
- collection_type: open
  name: Slack Admin Access Oauth API
  slug: open-slack-oauth-api
- collection_type: open
  name: Slack OAuth API
  slug: open-slack-oauth
- collection_type: open
  name: Slack Admin Access Open API
  slug: open-slack-open-api
- collection_type: open
  name: Slack Admin Access OpenID Connect API
  slug: open-slack-openid-connect-api
- collection_type: open
  name: Slack OpenID Connect API
  slug: open-slack-openid-connect
- collection_type: open
  name: Slack Admin Access Owners API
  slug: open-slack-owners-api
- collection_type: open
  name: Slack Admin Access Participants API
  slug: open-slack-participants-api
- collection_type: open
  name: Slack Admin Access Permissions API
  slug: open-slack-permissions-api
- collection_type: open
  name: Slack Admin Access Pins API
  slug: open-slack-pins-api
- collection_type: open
  name: Slack Pins API
  slug: open-slack-pins
- collection_type: open
  name: Slack Admin Access Post API
  slug: open-slack-post-api
- collection_type: open
  name: Slack Admin Access Profile API
  slug: open-slack-profile-api
- collection_type: open
  name: Slack Admin Access Project Management API
  slug: open-slack-project-management-api
- collection_type: open
  name: Slack Admin Access Prompts API
  slug: open-slack-prompts-api
- collection_type: open
  name: Slack Admin Access Publish API
  slug: open-slack-publish-api
- collection_type: open
  name: Slack Admin Access Push API
  slug: open-slack-push-api
- collection_type: open
  name: Slack Admin Access Reactions API
  slug: open-slack-reactions-api
- collection_type: open
  name: Slack Reactions API
  slug: open-slack-reactions
- collection_type: open
  name: Slack Admin Access Reminders API
  slug: open-slack-reminders-api
- collection_type: open
  name: Slack Reminders API
  slug: open-slack-reminders
- collection_type: open
  name: Slack Admin Access Remote API
  slug: open-slack-remote-api
- collection_type: open
  name: Slack Admin Access Remove API
  slug: open-slack-remove-api
- collection_type: open
  name: Slack Admin Access Rename API
  slug: open-slack-rename-api
- collection_type: open
  name: Slack Admin Access Replies API
  slug: open-slack-replies-api
- collection_type: open
  name: Slack Admin Access Requests API
  slug: open-slack-requests-api
- collection_type: open
  name: Slack Admin Access Reset API
  slug: open-slack-reset-api
- collection_type: open
  name: Slack Admin Access Resources API
  slug: open-slack-resources-api
- collection_type: open
  name: Slack Admin Access Restrict API
  slug: open-slack-restrict-api
- collection_type: open
  name: Slack Admin Access Restricted API
  slug: open-slack-restricted-api
- collection_type: open
  name: Slack Admin Access Revoke API
  slug: open-slack-revoke-api
- collection_type: open
  name: Slack RTM API
  slug: open-slack-rtm
- collection_type: open
  name: Slack Admin Access Scopes API
  slug: open-slack-scopes-api
- collection_type: open
  name: Slack Admin Access Search API
  slug: open-slack-search-api
- collection_type: open
  name: Slack Search API
  slug: open-slack-search
- collection_type: open
  name: Slack Admin Access Sections API
  slug: open-slack-sections-api
- collection_type: open
  name: Slack Admin Access Sessions API
  slug: open-slack-sessions-api
- collection_type: open
  name: Slack Admin Access Set API
  slug: open-slack-set-api
- collection_type: open
  name: Slack Admin Access Sets API
  slug: open-slack-sets-api
- collection_type: open
  name: Slack Admin Access Settings API
  slug: open-slack-settings-api
- collection_type: open
  name: Slack Admin Access Share API
  slug: open-slack-share-api
- collection_type: open
  name: Slack Admin Access Snooze API
  slug: open-slack-snooze-api
- collection_type: open
  name: Slack Stars API
  slug: open-slack-stars
- collection_type: open
  name: Slack Admin Access Status API
  slug: open-slack-status-api
- collection_type: open
  name: Slack Admin Access Team API
  slug: open-slack-team-api
- collection_type: open
  name: Slack Team API
  slug: open-slack-team
- collection_type: open
  name: Slack Admin Access Teams API
  slug: open-slack-teams-api
- collection_type: open
  name: Slack Tests API
  slug: open-slack-test-api
- collection_type: open
  name: Slack Admin Access Tests API
  slug: open-slack-tests-api
- collection_type: open
  name: Slack Admin Access Titles API
  slug: open-slack-titles-api
- collection_type: open
  name: Slack Admin Access Tokens API
  slug: open-slack-tokens-api
- collection_type: open
  name: Slack Admin Access Unarchive API
  slug: open-slack-unarchive-api
- collection_type: open
  name: Slack Admin Access Unfurl API
  slug: open-slack-unfurl-api
- collection_type: open
  name: Slack Admin Access Uninstall API
  slug: open-slack-uninstall-api
- collection_type: open
  name: Slack Admin Access Update API
  slug: open-slack-update-api
- collection_type: open
  name: Slack Admin Access Upload API
  slug: open-slack-upload-api
- collection_type: open
  name: Slack Admin Access Usergroups API
  slug: open-slack-usergroups-api
- collection_type: open
  name: Slack User Groups API
  slug: open-slack-usergroups
- collection_type: open
  name: Slack Admin Access Users API
  slug: open-slack-users-api
- collection_type: open
  name: Slack Users API
  slug: open-slack-users
- collection_type: open
  name: Slack Admin Access Views API
  slug: open-slack-views-api
- collection_type: open
  name: Slack Views API
  slug: open-slack-views
- collection_type: open
  name: Slack Web API
  slug: open-slack-web-api
- collection_type: open
  name: Slack Admin Access Workflows API
  slug: open-slack-workflows-api
- collection_type: open
  name: Slack Workflows
  slug: open-slack-workflows
common:
- group: commercial
  href: https://artifacts.apis.io/slack/plans/slack-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/slack-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/slack/finops/slack-finops.yml
  title: ''
  type: FinOps
  url: finops/slack-finops.yml
- group: other
  href: https://artifacts.apis.io/slack/vendor-facets/slack-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/slack-vendor-facets.yml
- group: company
  title: ''
  type: Website
  url: https://slack.dev
- group: other
  href: https://artifacts.apis.io/slack/capabilities/slack-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/slack-capability-edges.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/salesforce/
- group: agent
  href: https://artifacts.apis.io/slack/agentic-access/slack-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/slack-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/slack/security/slack-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/slack-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/slack/security/slack-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/slack-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/slack/security/slack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/slack-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/slack/authentication/slack-authentication.yml
  title: ''
  type: Authentication
  url: authentication/slack-authentication.yml
- group: auth
  href: https://artifacts.apis.io/slack/scopes/slack-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/slack-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/slack/overview
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-add-bookmark-announce-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-add-bookmark-announce-workflow.yml
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-add-reminder-for-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-add-reminder-for-user-workflow.yml
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-archive-channel-announce-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-archive-channel-announce-workflow.yml
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-audit-channels-post-summary-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-audit-channels-post-summary-workflow.yml
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-create-channel-invite-announce-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-create-channel-invite-announce-workflow.yml
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-create-usergroup-assign-members-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-create-usergroup-assign-members-workflow.yml
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-find-user-dm-message-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-find-user-dm-message-workflow.yml
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-lookup-invite-to-channel-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-lookup-invite-to-channel-workflow.yml
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-permalink-share-to-dm-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-permalink-share-to-dm-workflow.yml
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-post-message-get-reactions-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-post-message-get-reactions-workflow.yml
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-post-react-pin-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-post-react-pin-workflow.yml
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-post-thread-reply-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-post-thread-reply-workflow.yml
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-post-update-message-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-post-update-message-workflow.yml
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-read-history-mark-read-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-read-history-mark-read-workflow.yml
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-remove-member-announce-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-remove-member-announce-workflow.yml
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-rename-channel-announce-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-rename-channel-announce-workflow.yml
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-schedule-message-verify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-schedule-message-verify-workflow.yml
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-search-message-react-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-search-message-react-workflow.yml
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-set-channel-topic-purpose-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-set-channel-topic-purpose-workflow.yml
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-set-status-snooze-notify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-set-status-snooze-notify-workflow.yml
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-upload-file-share-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-upload-file-share-workflow.yml
- group: design
  href: https://artifacts.apis.io/slack/arazzo/slack-user-info-dm-greeting-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/slack-user-info-dm-greeting-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tiny-spec-inc
- group: operate
  title: ''
  type: StatusPage
  url: https://slack-status.com/
- group: start
  title: ''
  type: Portal
  url: https://api.slack.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.slack.com/automation/quickstart
- group: build
  title: ''
  type: CodeExamples
  url: https://api.slack.com/samples
- group: start
  title: ''
  type: Sandbox
  url: https://api.slack.com/docs/developer-sandbox
- group: auth
  title: ''
  type: Authentication
  url: https://api.slack.com/authentication
- group: learn
  title: ''
  type: Tutorials
  url: https://api.slack.com/tutorials
- group: commercial
  title: ''
  type: TermsOfService
  url: https://api.slack.com/developer-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://slack.com/intl/en-gb/terms-of-service/api-updated
- group: company
  title: ''
  type: Blog
  url: https://slack.com/intl/en-gb/blog
- group: commercial
  title: ''
  type: Plans
  url: https://slack.com/pricing
- group: auth
  title: ''
  type: OAuth
  url: https://api.slack.com/authentication/oauth-v2
- group: other
  title: ''
  type: Marketplace
  url: https://slack.com/apps
- group: operate
  title: ''
  type: Community
  url: https://api.slack.com/community
- group: operate
  title: ''
  type: Support
  url: https://api.slack.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://slack.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.slack.com/changelog
- group: build
  title: ''
  type: SDKs
  url: https://api.slack.com/tools
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.slack.dev/apis/web-api/rate-limits
- group: auth
  title: ''
  type: Security
  url: https://docs.slack.dev/security
- group: auth
  title: ''
  type: Scopes
  url: https://docs.slack.dev/reference/scopes
- group: other
  title: ''
  type: BlockKit
  url: https://docs.slack.dev/block-kit
- group: design
  title: ''
  type: Webhooks
  url: https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks
- group: other
  title: ''
  type: EventsAPI
  url: https://docs.slack.dev/apis/events-api
- group: other
  title: ''
  type: SocketMode
  url: https://docs.slack.dev/apis/events-api/using-socket-mode
- group: operate
  title: ''
  type: SlackConnect
  url: https://docs.slack.dev/apis/slack-connect
- group: docs
  title: ''
  type: OpenAPISpecs
  url: https://github.com/slackapi/slack-api-specs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/slackapi
- group: build
  title: Python SDK
  type: SDKs
  url: https://github.com/slackapi/python-slack-sdk
- group: build
  title: Node.js SDK
  type: SDKs
  url: https://github.com/slackapi/node-slack-sdk
- group: build
  title: Java SDK
  type: SDKs
  url: https://github.com/slackapi/java-slack-sdk
- group: build
  title: Bolt for Python
  type: SDKs
  url: https://github.com/slackapi/bolt-python
- group: build
  title: Bolt for JavaScript
  type: SDKs
  url: https://github.com/slackapi/bolt-js
- group: build
  title: Deno SDK
  type: SDKs
  url: https://github.com/slackapi/deno-slack-sdk
- group: other
  title: MCP Plugin
  type: Resources
  url: https://github.com/slackapi/slack-mcp-plugin
- group: other
  title: GitHub Action
  type: Resources
  url: https://github.com/slackapi/slack-github-action
- group: other
  title: Manifest Schema
  type: Resources
  url: https://github.com/slackapi/manifest-schema
- group: other
  title: ''
  type: DeveloperProgram
  url: https://api.slack.com/developer-program
- group: other
  title: ''
  type: ApplicationManagement
  url: https://api.slack.com/apps
- group: other
  title: ''
  type: Marketplace
  url: https://docs.slack.dev/slack-marketplace/distributing-your-app-in-the-slack-marketplace
- group: auth
  title: ''
  type: SecurityBestPractices
  url: https://docs.slack.dev/authentication/best-practices-for-security
- group: docs
  title: ''
  type: APIReference
  url: https://docs.slack.dev/reference/methods
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.slack.dev/quickstart
- group: build
  title: ''
  type: CLI
  url: https://docs.slack.dev/tools/slack-cli
- group: build
  title: ''
  type: DenoSDK
  url: https://docs.slack.dev/tools/deno-slack-sdk
- group: build
  title: ''
  type: BoltJavaSDK
  url: https://docs.slack.dev/tools/java-slack-sdk
- group: other
  title: ''
  type: AppManifest
  url: https://docs.slack.dev/app-manifests
- group: other
  title: ''
  type: Interactivity
  url: https://docs.slack.dev/interactivity
- group: operate
  title: ''
  type: FAQ
  url: https://docs.slack.dev/faq
- group: operate
  title: ''
  type: DeveloperSupport
  url: https://docs.slack.dev/developer-support
- group: start
  title: ''
  type: Signup
  url: https://api.slack.com/developer-program/join
- group: commercial
  title: ''
  type: TermsOfService
  url: https://slack.com/terms-of-service/api
- group: operate
  title: ''
  type: DeveloperChangelog
  url: https://docs.slack.dev/changelog
- group: company
  title: ''
  type: DeveloperBlog
  url: https://slack.dev
- group: operate
  title: ''
  type: SlashCommands
  url: https://docs.slack.dev/interactivity/slash-commands
- group: docs
  title: ''
  type: BlockKitReference
  url: https://docs.slack.dev/reference/block-kit
- group: docs
  title: ''
  type: AuditLogsAPIReference
  url: https://docs.slack.dev/reference/audit-logs-api/methods-actions-reference
- group: docs
  title: ''
  type: SCIMAPIReference
  url: https://docs.slack.dev/reference/scim-api
- group: design
  href: https://artifacts.apis.io/slack/rules/slack-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/slack-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/slack/vocabulary/slack-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/slack-vocabulary.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/slackapi/slack-mcp-plugin
- group: agent
  title: ''
  type: LlmsText
  url: https://api.slack.com/llms.txt
created: '2024-04-04'
description: Slack is a cloud-based team collaboration platform that provides chat, file sharing, and integrations with other tools and services.
examples:
- key_count: 31
  name: Slack Web Channel Example
  slug: slack-web-channel-example
- key_count: 3
  name: Slack Web Error Response Example
  slug: slack-web-error-response-example
- key_count: 28
  name: Slack Web File Example
  slug: slack-web-file-example
- key_count: 20
  name: Slack Web Message Example
  slug: slack-web-message-example
- key_count: 1
  name: Slack Web Response Metadata Example
  slug: slack-web-response-metadata-example
- key_count: 20
  name: Slack Web User Example
  slug: slack-web-user-example
features:
- Web API for messaging, channel, and user management
- Events API for real-time event subscription (30k events/hr/workspace cap)
- RTM API (legacy) for WebSocket-based event streaming
- Slack Bolt SDK for Python, JavaScript, Java
- Workflow Builder for no-code automation
- Slash commands and shortcuts
- Block Kit for rich message formatting
- Modals and views for interactive UI
- OAuth 2.0 with granular scopes
- Free plan with 90-day message history
- Pro plan at $7.25/user/mo annual with unlimited history
- Business+ at $15/user/mo with SSO, compliance, full AI
- Enterprise Grid with custom pricing for 500+ users
- Per-method tiered rate limits (Tier 1-4)
- chat.postMessage limited to 1/sec/channel with burst allowance
- Apps directory and Slack Connect for cross-org channels
finops:
- has_sources: true
  method: derived
  name: Slack Finops
  primary_unit: user
  service_category: ''
  slug: slack-finops
  template: false
image: https://a.slack-edge.com/80588/marketing/img/meta/slack_hash_256.png
integrations:
- name: Python Slack SDK for building bots and web API clients
- name: Node.js Bolt framework for rapid app development
- name: Java Slack SDK for enterprise Java applications
- name: Deno Slack SDK for serverless Slack functions
- name: Slack CLI for local development and app deployment
- name: Incoming Webhooks for simple message posting from external systems
- name: SCIM API for identity provider integration and user provisioning
json_schemas:
- name: Slack Channel
  property_count: 41
  slug: slack-channel
- name: Slack Message
  property_count: 30
  slug: slack-message
- name: Channel
  property_count: 31
  slug: slack-web-channel
- name: ErrorResponse
  property_count: 3
  slug: slack-web-error-response
- name: File
  property_count: 28
  slug: slack-web-file
- name: Message
  property_count: 20
  slug: slack-web-message
- name: ResponseMetadata
  property_count: 1
  slug: slack-web-response-metadata
- name: User
  property_count: 20
  slug: slack-web-user
json_structures:
- name: Slack Web Channel Structure
  property_count: 31
  slug: slack-web-channel-structure
- name: Slack Web Error Response Structure
  property_count: 3
  slug: slack-web-error-response-structure
- name: Slack Web File Structure
  property_count: 28
  slug: slack-web-file-structure
- name: Slack Web Message Structure
  property_count: 20
  slug: slack-web-message-structure
- name: Slack Web Response Metadata Structure
  property_count: 1
  slug: slack-web-response-metadata-structure
- name: Slack Web User Structure
  property_count: 20
  slug: slack-web-user-structure
jsonld:
- class_count: 0
  name: Slack Context
  property_count: 8
  slug: slack-context
- class_count: 0
  name: Slack Web Context
  property_count: 0
  slug: slack-web-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-09-16'
name: Slack
nav: Providers
network: true
overview: 'Slack publishes 48 API contracts indexed on the [APIs.io](https://apis.io/) network, including Events API, Access API, Add API, and 45 more. Tagged areas include Bots, Chat, Collaboration, Messaging, and Productivity.


  The Slack catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 3 Spectral governance rulesets.


  Slack''s developer surface includes authentication, developer portal, getting-started guide, code examples, sandbox, engineering blog, support, and 91 more developer resources.'
plans:
- name: Slack Plans Pricing
  plan_count: 6
  slug: slack-plans-pricing
- name: Slack Price Estimates
  plan_count: 0
  slug: slack-price-estimates
random_paper: 22
rate_limits:
- limit_count: 6
  name: Slack Rate Limits
  slug: slack-rate-limits
rules:
- authorship: generated
  effective_rule_count: 30
  extends:
  - spectral:asyncapi
  name: Slack — asyncapi rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: slack-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Slack — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: slack-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Slack API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 7
  slug: slack-spectral-rules
scopes:
- name: Slack Scopes
  scope_count: 13
  slug: slack-scopes
  summary_line: 13 scopes · authorizationCode
score:
  band: exemplar
  composite: 74.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 76.0
    catalog_earned_first_party: 12.0
    catalog_gap: 39.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 81.6
    contract_governance: 27.3
    contract_quality: 62.4
    developer_ergonomics: 89.3
    discoverability: 68.3
    operational_transparency: 63.2
  previous_composite: 73.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 48.8
      derived: 0
      marker_coverage: 0.0
      total: 41
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/slack/slack-2026-06-20T165933.png
security:
- kind: authentication
  name: Slack Authentication
  slug: slack-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Slack Domain Security
  slug: slack-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Slack Vulnerability Disclosure
  slug: slack-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Slack Trust Center
  slug: slack-trust-center
  summary_line: FedRAMP, GDPR
slug: slack
tags:
- Bots
- Chat
- Collaboration
- Messaging
- Productivity
- T1
- Team Communication
- Slack
- Real-Time
use_cases:
- name: DevOps teams automating deployment notifications and incident response
- name: Customer support teams routing tickets and managing escalations
- name: HR teams onboarding employees with automated workflows and reminders
- name: Sales teams receiving CRM alerts and managing deal updates in channels
- name: Engineering teams integrating CI/CD pipelines and code review notifications
- name: IT admins provisioning users and managing workspace security at scale
- name: Product teams collecting feedback with interactive surveys and polls
website: https://slack.dev
---
