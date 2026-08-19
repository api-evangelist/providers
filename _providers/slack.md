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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.4
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 145
  human_in_the_loop: 5
  name: Slack Agentic Access
  operation_count: 252
  slug: slack-agentic-access
  summary_line: 252 operations · 145 acting · 5 human-in-the-loop
api_count: 115
apis:
- description: The Slack Events API enables apps to respond to activities in Slack by subscribing to specific event types. Rather than polling for changes, apps receive HTTP POST payloads when subscribed events occu
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
- description: The Access API from Slack — 4 operation(s) for access.
  name: Slack Access API
  slug: slack-access-api
- description: The Add API from Slack — 9 operation(s) for add.
  name: Slack Add API
  slug: slack-add-api
- description: The Administrative API from Slack — 56 operation(s) for administrative.
  name: Slack Administrative API
  slug: slack-administrative-api
- description: The AI API from Slack — 3 operation(s) for ai.
  name: Slack AI API
  slug: slack-ai-api
- description: The Applications API from Slack — 13 operation(s) for applications.
  name: Slack Applications API
  slug: slack-applications-api
- description: The Approve API from Slack — 2 operation(s) for approve.
  name: Slack Approve API
  slug: slack-approve-api
- description: The Approved API from Slack — 2 operation(s) for approved.
  name: Slack Approved API
  slug: slack-approved-api
- description: The Archive API from Slack — 2 operation(s) for archive.
  name: Slack Archive API
  slug: slack-archive-api
- description: The Assign API from Slack — 1 operation(s) for assign.
  name: Slack Assign API
  slug: slack-assign-api
- description: The Assistants API from Slack — 3 operation(s) for assistants.
  name: Slack Assistants API
  slug: slack-assistants-api
- description: Authentication and authorization methods
  name: Slack Auth API
  slug: slack-auth-api
- description: The Authentication API from Slack — 2 operation(s) for authentication.
  name: Slack Authentication API
  slug: slack-authentication-api
- description: The Authorization API from Slack — 1 operation(s) for authorization.
  name: Slack Authorization API
  slug: slack-authorization-api
- description: The Automation API from Slack — 5 operation(s) for automation.
  name: Slack Automation API
  slug: slack-automation-api
- description: The Bookmarks API from Slack — 4 operation(s) for bookmarks.
  name: Slack Bookmarks API
  slug: slack-bookmarks-api
- description: The Bots API from Slack — 1 operation(s) for bots.
  name: Slack Bots API
  slug: slack-bots-api
- description: The Calls API from Slack — 6 operation(s) for calls.
  name: Slack Calls API
  slug: slack-calls-api
- description: The Canvases API from Slack — 6 operation(s) for canvases.
  name: Slack Canvases API
  slug: slack-canvases-api
- description: The Chat API from Slack — 10 operation(s) for chat.
  name: Slack Chat API
  slug: slack-chat-api
- description: The Close API from Slack — 1 operation(s) for close.
  name: Slack Close API
  slug: slack-close-api
- description: The Comments API from Slack — 1 operation(s) for comments.
  name: Slack Comments API
  slug: slack-comments-api
- description: The Complete API from Slack — 1 operation(s) for complete.
  name: Slack Complete API
  slug: slack-complete-api
- description: The Connect API from Slack — 1 operation(s) for connect.
  name: Slack Connect API
  slug: slack-connect-api
- description: The Conversations API from Slack — 36 operation(s) for conversations.
  name: Slack Conversations API
  slug: slack-conversations-api
- description: The Create API from Slack — 7 operation(s) for create.
  name: Slack Create API
  slug: slack-create-api
- description: The Delete API from Slack — 3 operation(s) for delete.
  name: Slack Delete API
  slug: slack-delete-api
- description: The Deletes API from Slack — 5 operation(s) for deletes.
  name: Slack Deletes API
  slug: slack-deletes-api
- description: The Deny API from Slack — 1 operation(s) for deny.
  name: Slack Deny API
  slug: slack-deny-api
- description: The Disables API from Slack — 1 operation(s) for disables.
  name: Slack Disables API
  slug: slack-disables-api
- description: The Disturb API from Slack — 5 operation(s) for disturb.
  name: Slack Disturb API
  slug: slack-disturb-api
- description: Do Not Disturb management
  name: Slack Dnd API
  slug: slack-dnd-api
- description: The Do API from Slack — 5 operation(s) for do.
  name: Slack Do API
  slug: slack-do-api
- description: The Documents API from Slack — 3 operation(s) for documents.
  name: Slack Documents API
  slug: slack-documents-api
- description: The Edit API from Slack — 2 operation(s) for edit.
  name: Slack Edit API
  slug: slack-edit-api
- description: The Emoji API from Slack — 1 operation(s) for emoji.
  name: Slack Emoji API
  slug: slack-emoji-api
- description: The Enables API from Slack — 1 operation(s) for enables.
  name: Slack Enables API
  slug: slack-enables-api
- description: The End API from Slack — 3 operation(s) for end.
  name: Slack End API
  slug: slack-end-api
- description: The Events API from Slack — 1 operation(s) for events.
  name: Slack Events API
  slug: slack-events-api
- description: The Exchange API from Slack — 1 operation(s) for exchange.
  name: Slack Exchange API
  slug: slack-exchange-api
- description: The Files API from Slack — 13 operation(s) for files.
  name: Slack Files API
  slug: slack-files-api
- description: The Functions API from Slack — 5 operation(s) for functions.
  name: Slack Functions API
  slug: slack-functions-api
- description: The Get API from Slack — 76 operation(s) for get.
  name: Slack Get API
  slug: slack-get-api
- description: The Groups API from Slack — 7 operation(s) for groups.
  name: Slack Groups API
  slug: slack-groups-api
- description: The History API from Slack — 1 operation(s) for history.
  name: Slack History API
  slug: slack-history-api
- description: The Identity API from Slack — 3 operation(s) for identity.
  name: Slack Identity API
  slug: slack-identity-api
- description: The Info API from Slack — 11 operation(s) for info.
  name: Slack Info API
  slug: slack-info-api
- description: The Information API from Slack — 1 operation(s) for information.
  name: Slack Information API
  slug: slack-information-api
- description: The Invalidate API from Slack — 1 operation(s) for invalidate.
  name: Slack Invalidate API
  slug: slack-invalidate-api
- description: The Invites API from Slack — 3 operation(s) for invites.
  name: Slack Invites API
  slug: slack-invites-api
- description: The Items API from Slack — 4 operation(s) for items.
  name: Slack Items API
  slug: slack-items-api
- description: The Join API from Slack — 1 operation(s) for join.
  name: Slack Join API
  slug: slack-join-api
- description: The Kick API from Slack — 1 operation(s) for kick.
  name: Slack Kick API
  slug: slack-kick-api
- description: The Leave API from Slack — 1 operation(s) for leave.
  name: Slack Leave API
  slug: slack-leave-api
- description: The Lists API from Slack — 34 operation(s) for lists.
  name: Slack Lists API
  slug: slack-lists-api
- description: The Lookup API from Slack — 1 operation(s) for lookup.
  name: Slack Lookup API
  slug: slack-lookup-api
- description: The Mark API from Slack — 1 operation(s) for mark.
  name: Slack Mark API
  slug: slack-mark-api
- description: The Members API from Slack — 1 operation(s) for members.
  name: Slack Members API
  slug: slack-members-api
- description: The Messages API from Slack — 1 operation(s) for messages.
  name: Slack Messages API
  slug: slack-messages-api
- description: The Migrations API from Slack — 1 operation(s) for migrations.
  name: Slack Migrations API
  slug: slack-migrations-api
- description: The Oauth API from Slack — 3 operation(s) for oauth.
  name: Slack Oauth API
  slug: slack-oauth-api
- description: The Open API from Slack — 3 operation(s) for open.
  name: Slack Open API
  slug: slack-open-api
- description: The OpenID Connect API from Slack — 2 operation(s) for openid connect.
  name: Slack OpenID Connect API
  slug: slack-openid-connect-api
- description: The Owners API from Slack — 1 operation(s) for owners.
  name: Slack Owners API
  slug: slack-owners-api
- description: The Participants API from Slack — 2 operation(s) for participants.
  name: Slack Participants API
  slug: slack-participants-api
- description: The Permissions API from Slack — 9 operation(s) for permissions.
  name: Slack Permissions API
  slug: slack-permissions-api
- description: The Pins API from Slack — 3 operation(s) for pins.
  name: Slack Pins API
  slug: slack-pins-api
- description: The Post API from Slack — 94 operation(s) for post.
  name: Slack Post API
  slug: slack-post-api
- description: The Profile API from Slack — 3 operation(s) for profile.
  name: Slack Profile API
  slug: slack-profile-api
- description: The Project Management API from Slack — 6 operation(s) for project management.
  name: Slack Project Management API
  slug: slack-project-management-api
- description: The Prompts API from Slack — 1 operation(s) for prompts.
  name: Slack Prompts API
  slug: slack-prompts-api
- description: The Publish API from Slack — 1 operation(s) for publish.
  name: Slack Publish API
  slug: slack-publish-api
- description: The Push API from Slack — 1 operation(s) for push.
  name: Slack Push API
  slug: slack-push-api
- description: The Reactions API from Slack — 4 operation(s) for reactions.
  name: Slack Reactions API
  slug: slack-reactions-api
- description: Create and manage reminders
  name: Slack Reminders API
  slug: slack-reminders-api
- description: The Remote API from Slack — 6 operation(s) for remote.
  name: Slack Remote API
  slug: slack-remote-api
- description: The Remove API from Slack — 8 operation(s) for remove.
  name: Slack Remove API
  slug: slack-remove-api
- description: The Rename API from Slack — 3 operation(s) for rename.
  name: Slack Rename API
  slug: slack-rename-api
- description: The Replies API from Slack — 1 operation(s) for replies.
  name: Slack Replies API
  slug: slack-replies-api
- description: The Requests API from Slack — 3 operation(s) for requests.
  name: Slack Requests API
  slug: slack-requests-api
- description: The Reset API from Slack — 1 operation(s) for reset.
  name: Slack Reset API
  slug: slack-reset-api
- description: The Resources API from Slack — 1 operation(s) for resources.
  name: Slack Resources API
  slug: slack-resources-api
- description: The Restrict API from Slack — 1 operation(s) for restrict.
  name: Slack Restrict API
  slug: slack-restrict-api
- description: The Restricted API from Slack — 1 operation(s) for restricted.
  name: Slack Restricted API
  slug: slack-restricted-api
- description: The Revoke API from Slack — 1 operation(s) for revoke.
  name: Slack Revoke API
  slug: slack-revoke-api
- description: The Scopes API from Slack — 1 operation(s) for scopes.
  name: Slack Scopes API
  slug: slack-scopes-api
- description: The Search API from Slack — 3 operation(s) for search.
  name: Slack Search API
  slug: slack-search-api
- description: The Sections API from Slack — 1 operation(s) for sections.
  name: Slack Sections API
  slug: slack-sections-api
- description: The Sessions API from Slack — 2 operation(s) for sessions.
  name: Slack Sessions API
  slug: slack-sessions-api
- description: The Set API from Slack — 1 operation(s) for set.
  name: Slack Set API
  slug: slack-set-api
- description: The Sets API from Slack — 1 operation(s) for sets.
  name: Slack Sets API
  slug: slack-sets-api
- description: The Settings API from Slack — 6 operation(s) for settings.
  name: Slack Settings API
  slug: slack-settings-api
- description: The Share API from Slack — 1 operation(s) for share.
  name: Slack Share API
  slug: slack-share-api
- description: The Snooze API from Slack — 2 operation(s) for snooze.
  name: Slack Snooze API
  slug: slack-snooze-api
- description: The Status API from Slack — 1 operation(s) for status.
  name: Slack Status API
  slug: slack-status-api
- description: Access workspace information
  name: Slack Team API
  slug: slack-team-api
- description: The Teams API from Slack — 16 operation(s) for teams.
  name: Slack Teams API
  slug: slack-teams-api
- description: The Tests API from Slack — 2 operation(s) for tests.
  name: Slack Tests API
  slug: slack-tests-api
- description: The Titles API from Slack — 1 operation(s) for titles.
  name: Slack Titles API
  slug: slack-titles-api
- description: The Tokens API from Slack — 1 operation(s) for tokens.
  name: Slack Tokens API
  slug: slack-tokens-api
- description: The Unarchive API from Slack — 2 operation(s) for unarchive.
  name: Slack Unarchive API
  slug: slack-unarchive-api
- description: The Unfurl API from Slack — 1 operation(s) for unfurl.
  name: Slack Unfurl API
  slug: slack-unfurl-api
- description: The Uninstall API from Slack — 1 operation(s) for uninstall.
  name: Slack Uninstall API
  slug: slack-uninstall-api
- description: The Update API from Slack — 8 operation(s) for update.
  name: Slack Update API
  slug: slack-update-api
- description: The Upload API from Slack — 1 operation(s) for upload.
  name: Slack Upload API
  slug: slack-upload-api
- description: Manage user groups
  name: Slack Usergroups API
  slug: slack-usergroups-api
- description: The Users API from Slack — 32 operation(s) for users.
  name: Slack Users API
  slug: slack-users-api
- description: The Views API from Slack — 4 operation(s) for views.
  name: Slack Views API
  slug: slack-views-api
- description: The Workflows API from Slack — 5 operation(s) for workflows.
  name: Slack Workflows API
  slug: slack-workflows-api
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
artifact_total: 377
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
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/slack-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/slack-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/slack-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/slack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/slack-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/slack-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/slack/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slack-add-bookmark-announce-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slack-add-reminder-for-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slack-archive-channel-announce-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slack-audit-channels-post-summary-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slack-create-channel-invite-announce-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slack-create-usergroup-assign-members-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slack-find-user-dm-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slack-lookup-invite-to-channel-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slack-permalink-share-to-dm-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slack-post-message-get-reactions-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slack-post-react-pin-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slack-post-thread-reply-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slack-post-update-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slack-read-history-mark-read-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slack-remove-member-announce-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slack-rename-channel-announce-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slack-schedule-message-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slack-search-message-react-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slack-set-channel-topic-purpose-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slack-set-status-snooze-notify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/slack-upload-file-share-workflow.yml
- group: design
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
  url: https://slack.com/intl/en-gb/terms-of-service/api-updated?_gl=1*1yvqubm*_gcl_au*ODQ0OTgxOTg3LjE3MzU5NDg2ODY.*_ga*MTk4NzA1NTA3Ny4xNzM1OTQ4Njg3*_ga_QTJQME5M5D*MTczNTk0ODY4NS4xLjEuMTczNTk0ODk4My41LjAuMA..
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
  title: ''
  type: SpectralRules
  url: rules/slack-spectral-rules.yml
- group: design
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
- name: Slack Finops
  service_category: Collaboration
  slug: slack-finops
graphqls:
- description: 'Slack does not expose a native public GraphQL endpoint. The Slack platform APIs are REST-based: the Web API (https://slack.com/api/*) is an HTTP/JSON interface, the Events API delivers webhook payload'
  name: Slack GraphQL
  slug: slack-graphql
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
modified: '2026-05-19'
name: Slack
nav: Providers
network: true
overview: 'Slack publishes 109 APIs on the [APIs.io](https://apis.io/) network, including Events API, Access API, Add API, and 106 more. Tagged areas include Bots, Chat, Collaboration, Messaging, and Productivity.


  The Slack catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 3 Spectral governance rulesets.


  Slack''s developer surface includes authentication, developer portal, getting-started guide, code examples, sandbox, engineering blog, support, and 85 more developer resources.'
plans:
- name: Slack Plans Pricing
  plan_count: 4
  slug: slack-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 6
  name: Slack Rate Limits
  slug: slack-rate-limits
rules:
- effective_rule_count: 30
  extends:
  - spectral:asyncapi
  name: Slack API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 2
  slug: slack-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Slack API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: slack-jsonschema-spectral-rules
- effective_rule_count: 56
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
  band: strong
  composite: 61.8
  delta: -3.3
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 26.5
    contract_quality: 67.6
    developer_ergonomics: 76.2
    discoverability: 66.7
    governance: 26.5
    operational_transparency: 63.2
  previous_composite: 65.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 108
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/slack/refs/heads/main/screenshots/slack-2026-06-20T165933.png
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
use_cases:
- name: DevOps teams automating deployment notifications and incident response
- name: Customer support teams routing tickets and managing escalations
- name: HR teams onboarding employees with automated workflows and reminders
- name: Sales teams receiving CRM alerts and managing deal updates in channels
- name: Engineering teams integrating CI/CD pipelines and code review notifications
- name: IT admins provisioning users and managing workspace security at scale
- name: Product teams collecting feedback with interactive surveys and polls
website: https://api.slack.com/
---
