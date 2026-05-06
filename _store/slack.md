---
aid: slack
url: https://raw.githubusercontent.com/api-search/messaging/main/_apis/slack/apis.md
apis:
  - aid: slack:slack-admin-api
    name: Slack Admin API
    tags:
      - Administrative
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/admins
    properties:
      - url: https://docs.slack.dev/admins
        type: Documentation
      - url: openapi/slack-admin-openapi.yml
        type: OpenAPI
    description: The Slack Admin API is a set of privileged endpointsprimarily under admin.* with related SCIM and Audit Logs APIsthat lets Enterprise Grid owners and admins automate organizationwide management and governance.
  - aid: slack:slack-tests-api
    name: Slack Tests API
    tags:
      - Tests
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/reference/methods
    properties:
      - url: https://docs.slack.dev/reference/methods
        type: Documentation
      - url: openapi/slack-test-api-openapi.yml
        type: OpenAPI
    description: I'm not aware of an official Slack product literally called Tests API. Typically, when people say Slack Tests API, they mean using Slack's existing APIs and SDK tooling to automate tests for Slack apps. In practice, developers call Slack's Web API to set up test data (channels, users, messages), craft Events API and interactive payloads to exercise handlers, and use SDK-provided mocks to assert responses and error handling in CI.
  - aid: slack:slack-apps-api
    name: Slack Apps API
    tags:
      - Applications
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/reference/methods
    properties:
      - url: https://docs.slack.dev/reference/methods
        type: Documentation
      - url: openapi/slack-apps-openapi.yml
        type: OpenAPI
    description: The Slack Apps API is a set of platform APIs and tools that let developers build apps to extend Slack and automate work. With it, you can read and write data via the Web API (messages, channels, files, reactions), receive real-time events using the Events API or Socket Mode, and create interactive experiences with Block Kit, modals, buttons, shortcuts, and slash commands. Apps can post messages, run workflows, add custom steps to Workflow Builder, manage conversations, and act as bot users.
  - aid: slack:slack-assistant-api
    name: Slack Assistant API
    tags:
      - AI
      - Assistants
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/reference/methods
    properties:
      - url: https://docs.slack.dev/reference/methods
        type: Documentation
      - url: openapi/slack-assistant-openapi.yml
        type: OpenAPI
    description: The Slack Assistant API provides the assistant.threads.* Web API methods that let apps building AI-powered assistants manage threaded conversations in Slack. It includes methods to set the status of an assistant thread (e.g., showing a thinking indicator), set suggested prompts for users to choose from, and set the title of an assistant thread. These methods help apps set user expectations during potentially slow AI responses and guide users with contextual prompt suggestions.
  - aid: slack:slack-auth-api
    name: Slack Auth API
    tags:
      - Authentication
      - Authorization
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/authentication
    properties:
      - url: https://docs.slack.dev/authentication
        type: Documentation
      - url: openapi/slack-auth-openapi.yml
        type: OpenAPI
    description: Slack's Auth API covers the authentication and authorization pieces that let apps securely identify users and workspaces and manage access. It includes OAuth 2.0 endpoints used during app installation to request scopes and exchange authorization codes for tokens (with optional token rotation), plus OpenID Connect for Sign in with Slack so you can authenticate users and retrieve standard identity claims.
  - aid: slack:slack-bookmarks-api
    name: Slack Bookmarks API
    tags:
      - Bookmarks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/reference/methods
    properties:
      - url: https://docs.slack.dev/reference/methods
        type: Documentation
      - url: openapi/slack-bookmarks-openapi.yml
        type: OpenAPI
    description: The Slack Bookmarks API provides the ability to add, remove, edit, or list curated resources directly in public channels, private channels, direct messages, multi-person direct messages, and shared channels. Bookmarks can contain external resources such as websites, spreadsheets, dashboards, wikis, and news articles, as well as internal resources such as messages, files, or other channels within Slack.
  - aid: slack:slack-bots-api
    name: Slack Bots API
    tags:
      - Bots
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/reference/methods
    properties:
      - url: https://docs.slack.dev/reference/methods
        type: Documentation
      - url: openapi/slack-bots-openapi.yml
        type: OpenAPI
    description: Slack's bot APIs let you build apps that live in Slack and automate work by listening for events and taking actions in conversations. Using the Web API, your bot can post and schedule messages, reply in threads, manage channels, look up users, and access files or reactions; the Events API delivers message, reaction, and workflow events to your server so you can respond in real time.
  - aid: slack:slack-calls-api
    name: Slack Calls API
    tags:
      - Calls
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/reference/methods
    properties:
      - url: https://docs.slack.dev/reference/methods
        type: Documentation
      - url: openapi/slack-calls-openapi.yml
        type: OpenAPI
    description: Slack's Calls API lets apps represent thirdparty voice or video calls inside Slack by creating a call object with a join URL and metadata, so users see a rich call message with a Join button, status, and participant list in channels or DMs. Through endpoints to create, update, and end callsand to add or remove participantsan app can keep that call message in sync as people join or leave and as the call progresses.
  - aid: slack:slack-canvases-api
    name: Slack Canvases API
    tags:
      - Canvases
      - Documents
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/surfaces/canvases
    properties:
      - url: https://docs.slack.dev/surfaces/canvases
        type: Documentation
      - url: openapi/slack-canvases-openapi.yml
        type: OpenAPI
    description: The Slack Canvases API lets apps programmatically create, edit, delete, and manage access to Slack Canvases, which are rich document surfaces embedded within Slack. Key methods include canvases.create for creating standalone canvases, canvases.edit for modifying content with operations like insert, replace, and delete, canvases.delete for removing canvases, and canvases.access.set and canvases.access.delete for managing who can view or edit a canvas.
  - aid: slack:slack-chat-api
    name: Slack Chat API
    tags:
      - Chat
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/reference/methods
    properties:
      - url: https://docs.slack.dev/reference/methods
        type: Documentation
      - url: openapi/slack-chat-openapi.yml
        type: OpenAPI
      - url: json-schema/slack-message-schema.json
        type: JSONSchema
    description: The Slack Chat API is the set of chat.* methods in the Slack Web API that lets apps and bots create and manage messages in Slack workspaces. It enables posting messages to channels and DMs with Block Kit formatting, sending ephemeral messages visible only to a specific user, replying in threads, scheduling messages for later delivery, updating or deleting existing messages, retrieving permalinks, and providing custom link unfurls.
  - aid: slack:slack-conversations-api
    name: Slack Conversations API
    tags:
      - Conversations
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/apis/web-api/using-the-conversations-api
    properties:
      - url: https://docs.slack.dev/apis/web-api/using-the-conversations-api
        type: Documentation
      - url: openapi/slack-conversations-openapi.yml
        type: OpenAPI
      - url: json-schema/slack-channel-schema.json
        type: JSONSchema
    description: The Slack Conversations API is the unified Web API for working with all types of Slack conversationspublic and private channels, direct messages, and multi-person DMs. It lets apps discover and inspect conversations, list members, and read message history and threads, as well as create, join, invite, leave, and archive channels where permissions allow.
  - aid: slack:slack-dialog-api
    name: Slack Dialog API
    tags:
      - Dialog
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/reference/methods
    properties:
      - url: https://docs.slack.dev/reference/methods
        type: Documentation
      - url: openapi/slack-dialog-openapi.yml
        type: OpenAPI
    description: Slack's Dialog API lets apps open form-like popups inside Slack to collect structured input from users. Apps trigger a dialog (often from a slash command, message action, or interactive message) by calling dialog.open with a short-lived trigger_id, then present fields like text inputs, textareas, and select menus (including dynamic, server-powered options).
  - aid: slack:slack-dnd-api
    name: Slack DND API
    tags:
      - Do Not Disturb
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/reference/methods
    properties:
      - url: https://docs.slack.dev/reference/methods
        type: Documentation
      - url: openapi/slack-dnd-openapi.yml
        type: OpenAPI
    description: Slack's Do Not Disturb (DND) API lets apps read and manage users' notification quiet time so they don't get pinged when they've paused alerts. With the dnd:read and dnd:write scopes, an app can check a user's current DND state and scheduled quiet hours, retrieve team-wide DND summaries (where permitted), start or extend a snooze for a specified duration, and end snooze or active DND. Key methods include dnd.info, dnd.teamInfo, dnd.setSnooze, dnd.endSnooze, and dnd.endDnd.
  - aid: slack:slack-emoji-api
    name: Slack Emoji API
    tags:
      - Emoji
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/reference/methods
    properties:
      - url: https://docs.slack.dev/reference/methods
        type: Documentation
      - url: openapi/slack-emoji-openapi.yml
        type: OpenAPI
    description: Slack's Emoji API lets apps discover and manage a workspace's custom emoji. The core method, emoji.list (requires the emoji:read scope), returns a name-to-URL map of all custom emoji along with aliases (noted as alias:other_name) and a cache timestamp to help clients sync efficiently. Apps can also subscribe to the emoji_changed event to stay up to date when emoji are added, renamed, or removed.
  - aid: slack:slack-events-api
    name: Slack Events API
    tags:
      - Events
      - Real Time
      - Webhooks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/apis/events-api
    properties:
      - url: https://docs.slack.dev/apis/events-api
        type: Documentation
      - url: https://docs.slack.dev/apis/events-api/using-socket-mode
        type: SocketMode
      - url: https://docs.slack.dev/apis/events-api/comparing-http-socket-mode
        type: Guide
      - url: asyncapi/slack-events-asyncapi.yml
        type: AsyncAPI
    description: The Slack Events API enables apps to respond to activities in Slack by subscribing to specific event types. Rather than polling for changes, apps receive HTTP POST payloads when subscribed events occur, such as new messages, reactions, channel changes, or user updates. The Events API offers two delivery options - a public HTTP endpoint that Slack sends event payloads to, or Socket Mode which uses WebSockets for apps that cannot expose a public URL.
  - aid: slack:slack-files-api
    name: Slack Files API
    tags:
      - Files
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/reference/methods
    properties:
      - url: https://docs.slack.dev/reference/methods
        type: Documentation
      - url: openapi/slack-files-openapi.yml
        type: OpenAPI
    description: Slack's Files API lets apps programmatically upload, share, and manage files in Slack. Apps can upload binaries (images, docs, code snippets) or register links to external files, then attach them to channels, DMs, or threads with optional captions. The API supports retrieving file metadata and content, listing and filtering files, generating or revoking public share links, and deleting files, with access controlled by app scopes and channel membership.
  - aid: slack:slack-functions-api
    name: Slack Functions API
    tags:
      - Automation
      - Functions
      - Workflows
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/workflows/workflow-steps
    properties:
      - url: https://docs.slack.dev/workflows/workflow-steps
        type: Documentation
      - url: openapi/slack-functions-openapi.yml
        type: OpenAPI
    description: The Slack Functions API provides methods for managing custom functions that run as steps within Slack workflows. The key methods are functions.completeSuccess, which marks a custom function as having completed successfully and passes output data conforming to the function's defined output schema, and functions.completeError, which marks a custom function as having failed and passes an error message that surfaces to the end user via Slackbot.
  - aid: slack:slack-lists-api
    name: Slack Lists API
    tags:
      - Lists
      - Project Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/surfaces/lists
    properties:
      - url: https://docs.slack.dev/surfaces/lists
        type: Documentation
      - url: openapi/slack-lists-openapi.yml
        type: OpenAPI
    description: The Slack Lists API provides methods for programmatically creating and managing Lists, a structured data surface in Slack for tracking work items, tasks, and records. Methods include slackLists.create and slackLists.update for managing lists, slackLists.items.create, slackLists.items.update, slackLists.items.delete, and slackLists.items.deleteMultiple for managing individual records, slackLists.items.list and slackLists.items.info for retrieving records, slackLists.download.start and slackLists.
  - aid: slack:slack-migration-api
    name: Slack Migration API
    tags:
      - Migration
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/reference/methods
    properties:
      - url: https://docs.slack.dev/reference/methods
        type: Documentation
      - url: openapi/slack-migration-openapi.yml
        type: OpenAPI
    description: Slack's Migration API is a Web API used during Enterprise Grid migrations to translate legacy, workspace-scoped identifiers into their new, canonical IDs so apps keep working after a workspace moves or merges. By calling its migration.exchange method, developers and admins can map old user and channel IDs to the new values that Slack assigns in an Enterprise Grid org, allowing databases, webhooks, event subscriptions, and app configurations to be updated without losing references.
  - aid: slack:slack-oauth-api
    name: Slack OAuth API
    tags:
      - Authentication
      - Authorization
      - OAuth
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/authentication
    properties:
      - url: https://docs.slack.dev/authentication
        type: Documentation
      - url: openapi/slack-oauth-openapi.yml
        type: OpenAPI
    description: The Slack OAuth API implements the OAuth 2.0 flow that lets developers securely install Slack apps to workspaces and obtain access tokens with specific, granular scopes. An app redirects a user to Slack for consent; after approval, Slack returns an authorization code that the app exchanges for tokens (typically a bot token, and optionally a user token) to call the Web API within the granted permissions.
  - aid: slack:slack-openid-connect-api
    name: Slack OpenID Connect API
    tags:
      - Authentication
      - Identity
      - OpenID Connect
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/authentication/sign-in-with-slack
    properties:
      - url: https://docs.slack.dev/authentication/sign-in-with-slack
        type: Documentation
      - url: openapi/slack-openid-connect-openapi.yml
        type: OpenAPI
    description: The Slack OpenID Connect API implements the Sign in with Slack flow based on the OpenID Connect standard built on top of OAuth 2.0. It includes openid.connect.token for exchanging an authorization code for an access token and a standard JWT id_token, and openid.connect.userInfo for retrieving identity information about a user who has authenticated via Sign in with Slack.
  - aid: slack:slack-pins-api
    name: Slack Pins API
    tags:
      - Pins
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/reference/methods
    properties:
      - url: https://docs.slack.dev/reference/methods
        type: Documentation
      - url: openapi/slack-pins-openapi.yml
        type: OpenAPI
    description: The Slack Pins API is a set of Web API methods that let your app manage pinned items in conversations so important content is easy to find. With pins.add, pins.list, and pins.remove, you can programmatically pin or unpin messages, files, and file comments in channels, private channels, and DMs by providing the conversation ID and the message timestamp or file/comment ID.
  - aid: slack:slack-reactions-api
    name: Slack Reactions API
    tags:
      - Reactions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/reference/methods
    properties:
      - url: https://docs.slack.dev/reference/methods
        type: Documentation
      - url: openapi/slack-reactions-openapi.yml
        type: OpenAPI
    description: Slack's Reactions API lets apps programmatically manage emoji reactions on messages and files, making it easy to capture lightweight feedback like approvals, acknowledgments, or votes. Through Web API methods (reactions.add, reactions.remove, reactions.get, reactions.list) and the Events API (reaction_added and reaction_removed), apps can add or delete reactions, read which reactions are on an item, and monitor reaction activity in real time.
  - aid: slack:slack-reminders-api
    name: Slack Reminders API
    tags:
      - Reminders
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/reference/methods
    properties:
      - url: https://docs.slack.dev/reference/methods
        type: Documentation
      - url: openapi/slack-reminders-openapi.yml
        type: OpenAPI
    description: Slack's Reminders API lets apps create and manage personal reminders for Slack users, so teams can automate nudges, followups, and routine checkins without leaving Slack. Through Web API methods, an app can add reminders with natural language or timestamps (including recurring patterns like every Monday at 9am ), list a user's upcoming reminders, fetch details, and mark or delete them when done.
  - aid: slack:slack-rtm-api
    name: Slack RTM API
    tags:
      - Real Time Messaging
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/legacy/legacy-rtm-api
    properties:
      - url: https://docs.slack.dev/legacy/legacy-rtm-api
        type: Documentation
      - url: openapi/slack-rtm-openapi.yml
        type: OpenAPI
    description: The Slack Real Time Messaging (RTM) API lets an app open a WebSocket connection to Slack and receive a live stream of JSON events from a workspacesuch as new messages, edits, reactions, user presence and typing indicators, channel joins, and moreso you can build lowlatency, interactive bots and clients. Apps typically use the RTM stream for listening and the Web API for performing actions like posting or updating messages.
  - aid: slack:slack-scim-api
    name: Slack SCIM API
    tags:
      - Enterprise
      - Identity
      - Provisioning
      - SCIM
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.slack.com/scim/v1
    humanURL: https://docs.slack.dev/admins/scim-api
    properties:
      - url: https://docs.slack.dev/admins/scim-api
        type: Documentation
      - url: https://docs.slack.dev/reference/scim-api
        type: APIReference
    description: The Slack SCIM API lets teams on Plus and Enterprise plans provision and manage user accounts and groups programmatically using the SCIM (System for Cross-domain Identity Management) protocol. It supports both SCIM v1.1 and v2.0, enabling identity providers and SSO services to automate user lifecycle management including creating, updating, deactivating, and deleting users, as well as creating and managing groups.
  - aid: slack:slack-audit-logs-api
    name: Slack Audit Logs API
    tags:
      - Audit Logs
      - Compliance
      - Enterprise
      - Security
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.slack.com/audit/v1
    humanURL: https://docs.slack.dev/admins/audit-logs-api
    properties:
      - url: https://docs.slack.dev/admins/audit-logs-api
        type: Documentation
      - url: https://docs.slack.dev/reference/audit-logs-api/methods-actions-reference
        type: APIReference
    description: The Slack Audit Logs API is designed for building security information and event management (SIEM) tools for Slack Enterprise Grid organizations. It provides a read-only view of audit events happening across an entire Enterprise organization, including user actions, admin actions, app installations, file sharing, and authentication events. The primary endpoint at /audit/v1/logs returns a list of auditable actions that have occurred, with filtering by action type, actor, entity, and date range.
  - aid: slack:slack-search-api
    name: Slack Search API
    tags:
      - Search
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/reference/methods
    properties:
      - url: https://docs.slack.dev/reference/methods
        type: Documentation
      - url: openapi/slack-search-openapi.yml
        type: OpenAPI
    description: Slack's Search API lets apps programmatically find messages and files in a workspace using the same query syntax users have in Slack (e.g., in:, from:, has:, before:/after:, is:thread). Through endpoints like search.messages and search.files, it returns ranked matches with snippets and optional highlighting, plus rich metadata such as channel, timestamps, user, thread context, permalinks, and file details. You can sort by relevance or time, filter with operators, and page through results.
  - aid: slack:slack-stars-api
    name: Slack Stars API
    tags:
      - Stars
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/reference/methods
    properties:
      - url: https://docs.slack.dev/reference/methods
        type: Documentation
      - url: openapi/slack-stars-openapi.yml
        type: OpenAPI
    description: The Slack Stars API is a set of Web API methods that let apps manage a user's starred itemsSlack's legacy personal bookmarking feature. It allows adding or removing a star on items such as messages (via channel and timestamp), files, and file comments, and listing all items a user has starred, typically with pagination and basic metadata. Stars are user-specific and don't alter the underlying content; they simply mark things for quick reference.
  - aid: slack:slack-team-api
    name: Slack Team API
    tags:
      - Teams
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/reference/methods
    properties:
      - url: https://docs.slack.dev/reference/methods
        type: Documentation
      - url: openapi/slack-team-openapi.yml
        type: OpenAPI
    description: Slack's Team API is the part of the Slack Web API that lets apps read workspace-level (team) information and, for admins, certain audit and billing data. With it, apps can fetch basic workspace identity and metadata (name, domain, icon, enterprise association), discover team preferences and custom profile fields, and, where permitted, retrieve billable info plus access and integration logs for auditing and compliance use cases.
  - aid: slack:slack-user-groups-api
    name: Slack User Groups API
    tags:
      - Groups
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/reference/methods
    properties:
      - url: https://docs.slack.dev/reference/methods
        type: Documentation
      - url: openapi/slack-usergroups-openapi.yml
        type: OpenAPI
    description: Slack's User Groups API lets apps programmatically create and manage user groups (mentionable aliases like @eng or @oncall) in a workspace. It supports creating, renaming, and updating groups and their handles and descriptions; setting default channels; enabling or disabling groups; listing groups; and adding or removing members in bulk. User groups make it easy to notify the right people with a single mention and to auto-add members to specific channels via default channel settings.
  - aid: slack:slack-users-api
    name: Slack Users API
    tags:
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/reference/methods
    properties:
      - url: https://docs.slack.dev/reference/methods
        type: Documentation
      - url: openapi/slack-users-openapi.yml
        type: OpenAPI
    description: Slack's Users API is a set of Web API methods that let your app discover and work with people in a Slack workspace. It can list members, fetch details for a specific user, look up users by email, and retrieve profile data such as names, photos, status, time zones, and custom fields. Where permitted, it can also read presence and update a user's profile or photo with the proper user-level authorization.
  - aid: slack:slack-views-api
    name: Slack Views API
    tags:
      - Views
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/reference/methods
    properties:
      - url: https://docs.slack.dev/reference/methods
        type: Documentation
      - url: openapi/slack-views-openapi.yml
        type: OpenAPI
    description: The Slack Views API lets your app build and control Block Kit interfaces inside Slackprimarily modals and the App Home tab. With methods like views.open, views.update, and views.push, your app can launch multi-step modal flows in response to interactive triggers (slash commands, shortcuts, or message actions), update them in place, or push new steps onto the stack. Using views.publish, you can render a personalized, dynamic Home tab for each user.
  - aid: slack:slack-workflows-api
    name: Slack Workflows API
    tags:
      - Workflows
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/workflows
    properties:
      - url: https://docs.slack.dev/workflows
        type: Documentation
      - url: openapi/slack-workflows-openapi.yml
        type: OpenAPI
    description: Slack's Workflows API lets you automate work inside Slack by defining workflowsordered steps or functionsthat run in response to triggers like shortcuts, messages, schedules, link clicks, or webhooks. Developers can build Slacknative steps, collect inputs with forms, post messages, route approvals, and call external services, then programmatically create and manage triggers and runs.
  - aid: slack:slack-web-api
    name: Slack Web API
    tags:
      - HTTP
      - REST
      - Web API
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/apis/web-api
    properties:
      - url: https://docs.slack.dev/apis/web-api
        type: Documentation
      - url: https://docs.slack.dev/reference/methods
        type: APIReference
      - url: https://docs.slack.dev/apis/web-api/rate-limits
        type: RateLimits
      - url: openapi/slack-web-api-openapi.yml
        type: OpenAPI
      - url: json-schema/slack-message-schema.json
        type: JSONSchema
      - url: json-schema/slack-channel-schema.json
        type: JSONSchema
      - url: json-ld/slack-context.jsonld
        type: JSONLD
    description: The Slack Web API is an HTTP-based interface that provides access to all of Slack's platform features. It consists of over 200 methods organized by functional area (chat, conversations, users, files, admin, and more) that apps call over HTTPS with JSON payloads and receive JSON responses. The Web API is the primary way apps interact with Slack programmatically, covering everything from posting messages and managing channels to uploading files, managing users, and administering workspaces.
  - aid: slack:slack-incoming-webhooks-api
    name: Slack Incoming Webhooks API
    tags:
      - Messaging
      - Webhooks
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://hooks.slack.com
    humanURL: https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks
    properties:
      - url: https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks
        type: Documentation
    description: Slack Incoming Webhooks provide a simple way to post messages from external sources into Slack. Creating an incoming webhook gives you a unique URL to which you send a JSON payload with the message text and formatting options. Messages can be plain text or use Block Kit for rich formatting with interactive components.
  - aid: slack:slack-slash-commands-api
    name: Slack Slash Commands API
    tags:
      - Commands
      - Interactivity
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/interactivity/slash-commands
    properties:
      - url: https://docs.slack.dev/interactivity/slash-commands
        type: Documentation
    description: Slack Slash Commands allow users to invoke app functionality directly from the message composer box by typing a forward slash followed by a command name and optional parameters. When a user triggers a slash command, Slack sends an HTTP POST request to the app's configured Request URL with details about the command, user, channel, and any text entered. The app can respond with a message (visible to everyone or only to the invoking user), open a modal, or trigger other interactive flows.
  - aid: slack:slack-app-manifest-api
    name: Slack App Manifest API
    tags:
      - App Manifest
      - Configuration
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/app-manifests
    properties:
      - url: https://docs.slack.dev/app-manifests
        type: Documentation
      - url: https://docs.slack.dev/reference/app-manifest
        type: APIReference
    description: The Slack App Manifest API provides methods to programmatically create, configure, update, export, validate, and delete Slack apps using JSON or YAML manifest files. Key methods include apps.manifest.create for creating new apps from a manifest, apps.manifest.update for modifying existing app configurations, apps.manifest.export for exporting an app's current configuration, apps.manifest.validate for validating manifest syntax before applying changes, and apps.manifest.delete for removing apps.
  - aid: slack:slack-interactivity-api
    name: Slack Interactivity API
    tags:
      - Block Kit
      - Components
      - Interactivity
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://slack.com/api
    humanURL: https://docs.slack.dev/interactivity
    properties:
      - url: https://docs.slack.dev/interactivity
        type: Documentation
      - url: https://docs.slack.dev/interactivity/handling-user-interaction
        type: Guide
      - url: https://docs.slack.dev/block-kit
        type: BlockKit
    description: The Slack Interactivity API encompasses the mechanisms by which Slack apps handle user interactions with interactive components such as buttons, menus, date pickers, modals, shortcuts, and other Block Kit elements. When a user interacts with these components, Slack sends an interaction payload to the app's configured Request URL or via Socket Mode.
name: Slack
tags:
  - Bots
  - Chat
  - Collaboration
  - Messaging
  - Productivity
  - T1
  - Team Communication
type: Contract
access: 3rd-Party
common:
  - url: https://slack-status.com/
    name: Status
    type: StatusPage
  - url: https://api.slack.com/
    name: Unlock your productivity potential with Slack Platform | Slack
    type: Portal
    description: 'null'
  - url: https://api.slack.com/automation/quickstart
    name: Quickstart guide for developing automations | Slack
    type: GettingStarted
    description: 'null'
  - url: https://api.slack.com/samples
    name: Samples and templates | Slack
    type: CodeExamples
    description: 'null'
  - url: https://api.slack.com/docs/developer-sandbox
    name: Developer sandboxes | Slack
    type: Sandbox
    description: 'null'
  - url: https://api.slack.com/authentication
    name: Authentication | Slack
    type: Authentication
    description: 'null'
  - url: https://api.slack.com/tutorials
    name: Guided tutorials | Slack
    type: Tutorials
    description: 'null'
  - url: https://api.slack.com/developer-policy
    name: Slack App Developer Policy | Slack
    type: TermsOfService
    description: 'null'
  - url: https://slack.com/intl/en-gb/terms-of-service/api-updated?_gl=1*1yvqubm*_gcl_au*ODQ0OTgxOTg3LjE3MzU5NDg2ODY.*_ga*MTk4NzA1NTA3Ny4xNzM1OTQ4Njg3*_ga_QTJQME5M5D*MTczNTk0ODY4NS4xLjEuMTczNTk0ODk4My41LjAuMA..
    name: Slack API Terms of Service | Legal | Slack
    type: TermsOfService
    description: 'null'
  - url: https://slack.com/intl/en-gb/blog
    name: Slack blog | Slack
    type: Blog
    description: 'null'
  - url: https://slack.com/pricing
    data:
      url: https://slack.com/pricing
      data:
        - id: free
          name: Free
          entries:
            - geo: US
              unit: 1
              label: User
              limit: 1
              price: Free
              metric: user
              timeFrame: month
              description: Usage based pricing.
          elements:
            - name: 90 days of message history
            - name: Up to 10 apps
            - name: 1:1 meetings
            - name: 1:1 external messages
            - name: Message and file history
            - name: Channels
            - name: Search
            - name: Audio and video clips
            - name: Slack Connect
            - name: Huddles
            - name: Canvases
            - name: 10 Integrations with other apps
            - name: Data encryption at rest and in transit
            - name: Two-factor authentication
            - name: Session duration
            - name: Native device management
            - name: 1 Year Data retention policies
            - name: 1 Workspaces
            - name: Manage channel posting permissions
          description: A simpler way to chat and collaborate.
        - id: pro
          name: Pro
          entries:
            - geo: US
              unit: 1
              label: User
              limit: 1
              price: $4.38
              metric: user
              timeFrame: month
              description: Usage based pricing.
          elements:
            - name: Unlimited message history
            - name: Unlimited app integrations
            - name: Group meetings
            - name: Group external messages
            - name: Message and file history
            - name: Channels
            - name: Search
            - name: Audio and video clips
            - name: Slack Connect
            - name: Huddles
            - name: Canvases
            - name: Lists
            - name: Customizable sections
            - name: Templates
            - name: Thread and channel summaries
            - name: Huddles notes
            - name: AI assistant apps
            - name: Integrations with other apps
            - name: Workflow Builder
            - name: Custom workflow steps
            - name: Deploy apps to Slack infrastructure
            - name: Data encryption at rest and in transit
            - name: Two-factor authentication
            - name: Session duration
            - name: Native device management
            - name: Access logs
            - name: Single sign-on (SSO)
            - name: OAuth with Google
            - name: Data retention policies
            - name: 1 Workspace
            - name: Manage channel posting permissions
            - name: Admin analytics dashboards
            - name: 24/7 Customer support
          description: Drive productivity in one place.
        - id: business
          name: Business
          entries:
            - geo: US
              unit: 1
              label: User
              limit: 1
              price: $9.00
              metric: user
              timeFrame: month
              description: Usage based pricing.
          elements:
            - name: Unlimited message history
            - name: Unlimited app integrations
            - name: Group meetings
            - name: Group external messages
            - name: AI conversation summaries
            - name: AI workflow generation
            - name: AI search
            - name: AI daily recaps
            - name: AI file summaries
            - name: SAML-based single sign-on
            - name: SCIM user management
            - name: Message and file history
            - name: Channels
            - name: Search
            - name: Audio and video clips
            - name: Slack Connect
            - name: Huddles
            - name: Canvases
            - name: Lists
            - name: Customizable sections
            - name: Templates
            - name: Slack Atlas
            - name: Thread and channel summaries
            - name: Huddles notes
            - name: AI assistant apps
            - name: Daily recaps
            - name: File summaries
            - name: AI language translations
            - name: AI workflow generation
            - name: AI steps in Workflow Builder
            - name: AI search
            - name: Integrations with other apps
            - name: Workflow Builder
            - name: Custom workflow steps
            - name: Deploy apps to Slack infrastructure
            - name: Data encryption at rest and in transit
            - name: Two-factor authentication
            - name: Session duration
            - name: Native device management
            - name: Access logs
            - name: Single sign-on (SSO)
            - name: OAuth with Google
            - name: SAML-based
            - name: Supports Multi-SAML
            - name: Data retention policies
            - name: Data residency
            - name: Workspaces
            - name: Manage channel posting permissions
            - name: Admin analytics dashboards
            - name: SCIM user management
            - name: Supports guests
            - name: Admin analytics API
            - name: Message activity analytics
            - name: Custom user groups
            - name: Manually manage
          description: Scale with AI-powered work.
        - id: enterprise
          name: Enterprise
          entries:
            - geo: US
              unit: 1
              label: User
              limit: 1
              price: Contact Sales
              metric: user
              timeFrame: month
              description: Usage based pricing.
          elements:
            - name: Unlimited message history
            - name: Unlimited app integrations
            - name: Group meetings
            - name: Group external messages
            - name: AI conversation summaries
            - name: AI workflow generation
            - name: AI search
            - name: AI daily recaps
            - name: AI file summaries
            - name: SAML-based single sign-on
            - name: SCIM user management
            - name: Message and file history
            - name: Channels
            - name: Search
            - name: Audio and video clips
            - name: Slack Connect
            - name: Huddles
            - name: Canvases
            - name: Lists
            - name: Customizable sections
            - name: Templates
            - name: Slack Atlas
            - name: Thread and channel summaries
            - name: Huddles notes
            - name: AI assistant apps
            - name: Daily recaps
            - name: File summaries
            - name: AI language translations
            - name: AI workflow generation
            - name: AI steps in Workflow Builder
            - name: AI search
            - name: Enterprise search
            - name: Integrations with other apps
            - name: Workflow Builder
            - name: Custom workflow steps
            - name: Deploy apps to Slack infrastructure
            - name: Data encryption at rest and in transit
            - name: Two-factor authentication
            - name: Session duration
            - name: Native device management
            - name: Access logs
            - name: Single sign-on (SSO)
            - name: OAuth with Google
            - name: SAML-based
            - name: Supports Multi-SAML
            - name: Slack Enterprise Key Management
            - name: Add-on
            - name: Integration with Enterprise Mobility Management
            - name: Anomaly Event Response
            - name: Data retention policies
            - name: Data residency
            - name: Data exports for all messages
            - name: Data exports for all messages from a single user
            - name: Native data loss prevention
            - name: Information barriers
            - name: Legal holds
            - name: Discovery API
            - name: Audit logs
            - name: Support for HIPAA compliance
            - name: Workspaces
            - name: Manage channel posting permissions
            - name: Admin analytics dashboards
            - name: SCIM user management
            - name: Supports guests
            - name: Admin analytics API
            - name: Message activity analytics
            - name: Custom user groups
            - name: Manually manageSync via identity provider
            - name: Domain claiming
            - name: Custom terms of service
            - name: Granular roles
            - name: Manage flagged content
            - name: Access to customer support
          description: Scale with AI-powered work.
      name: Plans
      type: Plans
    name: Plans
    type: Plans
  - url: https://api.slack.com/authentication/oauth-v2
    type: OAuth
  - url: https://slack.com/apps
    type: Marketplace
  - url: https://api.slack.com/community
    type: Community
  - url: https://api.slack.com/support
    type: Support
  - url: https://slack.com/privacy-policy
    type: PrivacyPolicy
  - url: https://api.slack.com/changelog
    type: ChangeLog
  - url: https://api.slack.com/tools
    type: SDK
  - url: https://docs.slack.dev/apis/web-api/rate-limits
    type: RateLimits
  - url: https://docs.slack.dev/security
    type: Security
  - url: https://docs.slack.dev/reference/scopes
    type: Scopes
  - url: https://docs.slack.dev/block-kit
    type: BlockKit
  - url: https://docs.slack.dev/messaging/sending-messages-using-incoming-webhooks
    type: Webhooks
  - url: https://docs.slack.dev/apis/events-api
    type: EventsAPI
  - url: https://docs.slack.dev/apis/events-api/using-socket-mode
    type: SocketMode
  - url: https://docs.slack.dev/apis/slack-connect
    type: SlackConnect
  - url: https://github.com/slackapi/slack-api-specs
    type: OpenAPISpecs
  - url: https://github.com/slackapi
    type: GitHubOrganization
  - url: https://github.com/slackapi/python-slack-sdk
    type: SDK
    title: Python SDK
  - url: https://github.com/slackapi/node-slack-sdk
    type: SDK
    title: Node.js SDK
  - url: https://github.com/slackapi/java-slack-sdk
    type: SDK
    title: Java SDK
  - url: https://github.com/slackapi/bolt-python
    type: SDK
    title: Bolt for Python
  - url: https://github.com/slackapi/bolt-js
    type: SDK
    title: Bolt for JavaScript
  - url: https://github.com/slackapi/deno-slack-sdk
    type: SDK
    title: Deno SDK
  - url: https://github.com/slackapi/slack-mcp-plugin
    type: Resources
    title: MCP Plugin
  - url: https://github.com/slackapi/slack-github-action
    type: Resources
    title: GitHub Action
  - url: https://github.com/slackapi/manifest-schema
    type: Resources
    title: Manifest Schema
  - url: https://api.slack.com/developer-program
    type: DeveloperProgram
  - url: https://api.slack.com/apps
    type: ApplicationManagement
  - url: https://docs.slack.dev/slack-marketplace/distributing-your-app-in-the-slack-marketplace
    type: Marketplace
  - url: https://docs.slack.dev/authentication/best-practices-for-security
    type: SecurityBestPractices
  - url: https://docs.slack.dev/reference/methods
    type: APIReference
  - url: https://docs.slack.dev/quickstart
    type: GettingStarted
  - url: https://docs.slack.dev/tools/slack-cli
    type: CLI
  - url: https://docs.slack.dev/tools/deno-slack-sdk
    type: DenoSDK
  - url: https://docs.slack.dev/tools/java-slack-sdk
    type: BoltJavaSDK
  - url: https://docs.slack.dev/app-manifests
    type: AppManifest
  - url: https://docs.slack.dev/interactivity
    type: Interactivity
  - url: https://docs.slack.dev/faq
    type: FAQ
  - url: https://docs.slack.dev/developer-support
    type: DeveloperSupport
  - url: https://api.slack.com/developer-program/join
    type: SignUp
  - url: https://slack.com/terms-of-service/api
    type: TermsOfService
  - url: https://docs.slack.dev/changelog
    type: DeveloperChangelog
  - url: https://slack.dev
    type: DeveloperBlog
  - url: https://docs.slack.dev/interactivity/slash-commands
    type: SlashCommands
  - url: https://docs.slack.dev/reference/block-kit
    type: BlockKitReference
  - url: https://docs.slack.dev/reference/audit-logs-api/methods-actions-reference
    type: AuditLogsAPIReference
  - url: https://docs.slack.dev/reference/scim-api
    type: SCIMAPIReference
  - type: Features
    data:
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
    sources:
      - https://slack.com/pricing
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: DevOps teams automating deployment notifications and incident response
      - name: Customer support teams routing tickets and managing escalations
      - name: HR teams onboarding employees with automated workflows and reminders
      - name: Sales teams receiving CRM alerts and managing deal updates in channels
      - name: Engineering teams integrating CI/CD pipelines and code review notifications
      - name: IT admins provisioning users and managing workspace security at scale
      - name: Product teams collecting feedback with interactive surveys and polls
  - type: Integrations
    data:
      - name: Python Slack SDK for building bots and web API clients
      - name: Node.js Bolt framework for rapid app development
      - name: Java Slack SDK for enterprise Java applications
      - name: Deno Slack SDK for serverless Slack functions
      - name: Slack CLI for local development and app deployment
      - name: Incoming Webhooks for simple message posting from external systems
      - name: SCIM API for identity provider integration and user provisioning
  - url: rules/slack-spectral-rules.yml
    type: SpectralRules
  - url: vocabulary/slack-vocabulary.yaml
    type: Vocabulary
  - url: capabilities/messaging-communication.yaml
    type: NaftikoCapability
    title: Messaging and Communication
  - url: capabilities/workspace-administration.yaml
    type: NaftikoCapability
    title: Workspace Administration
  - url: capabilities/app-platform.yaml
    type: NaftikoCapability
    title: App Platform
created: '2024-04-04'
modified: '2026-05-04'
position: Consuming
description: Slack is a cloud-based team collaboration platform that provides chat, file sharing, and integrations with other tools and services.
maintainers:
  - FN: Kin Lane
    url: https://apievangelist.com
    email: kin@apievangelist.com
  - FN: Slack
    email: feedback@slack.com
    url: https://slack.com
specificationVersion: '0.18'
image: https://a.slack-edge.com/80588/marketing/img/meta/slack_hash_256.png
---
