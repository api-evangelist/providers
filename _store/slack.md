---
---
aid: slack
url: https://raw.githubusercontent.com/api-search/messaging/main/_apis/slack/apis.md
apis:
  - aid: slack:admin
    name: Slack Admin API
    tags:
      - Administrator
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-admin-openapi.yml
        type: OpenAPI
    description: "The Slack Admin API is a set of privileged endpoints\x14primarily
      under admin.* with related SCIM and Audit Logs APIs\x14that lets
      Enterprise Grid owners and admins automate organization\x11wide management
      and governance. It covers user lifecycle (provision, suspend, assign
      roles), workspace and channel administration across workspaces (create,
      move, archive channels; manage membership and settings), app governance
      (approve/deny or allowlist/ban apps and install them to workspaces),
      invite request handling, and security/compliance controls such as
      information barriers, session and authentication policies, and
      org\x11level analytics exports. These APIs require elevated admin scopes
      and are commonly used to power automated onboarding/offboarding,
      centralized channel and app controls, and integrations with identity,
      ITSM, and compliance systems."
  - aid: slack:api
    name: Slack Tests API
    tags:
      - Tests
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-api-openapi.yml
        type: OpenAPI
    description: "I\x19m not aware of an official Slack product literally called
      \x1cTests API.\x1d Typically, when people say \x1cSlack Tests API,\x1d
      they mean using Slack\x19s existing APIs and SDK tooling to automate tests
      for Slack apps. In practice, developers call Slack\x19s Web API to set up
      test data (channels, users, messages), craft Events API and interactive
      payloads to exercise handlers, and use SDK-provided mocks to assert
      responses and error handling in CI. This approach lets teams verify
      permissions, rate-limit behavior, and message/Block Kit rendering, so
      bots, workflows, and functions behave correctly before deployment. If you
      meant a specific third-party tool or a particular Slack feature by that
      name, let me know and I can tailor the description."
  - aid: slack:apps
    name: Slack Apps API
    tags:
      - Applications
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-apps-openapi.yml
        type: OpenAPI
    description: The Slack Apps API is a set of platform APIs and tools that let
      developers build apps to extend Slack and automate work. With it, you can
      read and write data via the Web API (messages, channels, files,
      reactions), receive real-time events using the Events API or Socket Mode,
      and create interactive experiences with Block Kit, modals, buttons,
      shortcuts, and slash commands. Apps can post messages, run workflows, add
      custom steps to Workflow Builder, manage conversations, and act as bot
      users. Installation uses OAuth 2.0 with granular permission scopes and
      token types, and enterprise features are supported through admin APIs.
      Together, these capabilities connect external systems to Slack, trigger
      actions from conversations, and orchestrate end-to-end processes without
      leaving the chat.
  - aid: slack:auth
    name: Slack Auth API
    tags:
      - Authentication
      - Authorization
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-auth-openapi.yml
        type: OpenAPI
    description: "Slack\x19s Auth API covers the authentication and authorization
      pieces that let apps securely identify users and workspaces and manage
      access. It includes OAuth 2.0 endpoints used during app installation to
      request scopes and exchange authorization codes for tokens (with optional
      token rotation), plus OpenID Connect for \x1cSign in with Slack\x1d so you
      can authenticate users and retrieve standard identity claims. Within the
      Web API, methods like auth.test let you verify a token and learn which
      user and workspace it belongs to, auth.revoke allows you to invalidate
      tokens, and auth.teams.list helps enumerate the workspaces a user can use
      with your app (useful for multi-workspace and Enterprise Grid scenarios).
      Together, these capabilities ensure your app knows who is calling, what
      it\x19s allowed to do, and where, before invoking other Slack APIs."
  - aid: slack:bots
    name: Slack Bots API
    tags:
      - Bots
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-bots-openapi.yml
        type: OpenAPI
    description: "Slack\x19s bot APIs let you build apps that live in Slack and
      automate work by listening for events and taking actions in conversations.
      Using the Web API, your bot can post and schedule messages, reply in
      threads, manage channels, look up users, and access files or reactions;
      the Events API delivers message, reaction, and workflow events to your
      server so you can respond in real time. Bots can power slash commands,
      message shortcuts, and interactive UI elements (buttons, menus, modals
      built with Block Kit), and they can open modals or update messages
      dynamically. Installation and access are controlled via OAuth 2.0 scopes,
      with bot tokens used to authenticate API calls; you can receive events
      over HTTPS or via Socket Mode if you don\x19t host a public endpoint.
      Together, these capabilities let you create assistants that answer
      questions, route approvals, connect external services, and streamline team
      processes directly inside Slack."
  - aid: slack:calls
    name: Slack Calls API
    tags:
      - Calls
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-calls-openapi.yml
        type: OpenAPI
    description: "Slack\x19s Calls API lets apps represent third\x11party voice or
      video calls inside Slack by creating a \x1ccall\x1d object with a join URL
      and metadata, so users see a rich call message with a Join button, status,
      and participant list in channels or DMs. Through endpoints to create,
      update, and end calls\x14and to add or remove participants\x14an app can
      keep that call message in sync as people join or leave and as the call
      progresses. The API doesn\x19t handle the media itself; it\x19s for
      coordinating and rendering the Slack UI around calls hosted by services
      like Zoom or Webex, making it easy to start, find, and join those calls
      from Slack."
  - aid: slack:chat
    name: Slack Chat API
    tags:
      - Chat
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-chat-openapi.yml
        type: OpenAPI
    description: The Slack Chat API is the set of chat.* methods in the Slack Web
      API that lets apps and bots create and manage messages in Slack
      workspaces. It enables posting messages to channels and DMs with Block Kit
      formatting, sending ephemeral messages visible only to a specific user,
      replying in threads, scheduling messages for later delivery, updating or
      deleting existing messages, retrieving permalinks, and providing custom
      link unfurls. These methods work over HTTP with JSON payloads, use
      bot/user tokens with scopes like chat:write and chat:write.public, and
      return metadata such as channel, ts, and thread_ts. Teams use the Chat API
      to automate notifications, power interactive workflows, and deliver rich
      conversational experiences inside Slack.
  - aid: slack:conversations
    name: Slack Conversations API
    tags:
      - Conversations
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-conversations-openapi.yml
        type: OpenAPI
    description: "The Slack Conversations API is the unified Web API for working
      with all types of Slack conversations\x14public and private channels,
      direct messages, and multi-person DMs. It lets apps discover and inspect
      conversations, list members, and read message history and threads, as well
      as create, join, invite, leave, and archive channels where permissions
      allow. By consolidating the legacy channels.*, groups.*, im.*, and mpim.*
      endpoints into conversations.*, it provides consistent IDs and behavior
      across conversation types. It supports cursor-based pagination, filtering
      by conversation type, and granular OAuth scopes to ensure apps only access
      authorized data. Developers use it to find the right place to post, fetch
      context for workflows, manage membership, and build features that traverse
      messages and threads across a workspace (including Slack Connect channels
      when permitted)."
  - aid: slack:dialog
    name: Slack Dialog API
    tags:
      - Dialog
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-dialog-openapi.yml
        type: OpenAPI
    description: "Slack\x19s Dialog API lets apps open form-like popups inside Slack
      to collect structured input from users. Apps trigger a dialog (often from
      a slash command, message action, or interactive message) by calling
      dialog.open with a short-lived trigger_id, then present fields like text
      inputs, textareas, and select menus (including dynamic, server-powered
      options). When users submit or cancel, Slack sends a dialog_submission or
      dialog_cancellation payload to the app, which can validate inputs and send
      dialog_errors for inline feedback before completing the workflow. Dialogs
      are ephemeral to the user and well-suited for tasks like creating tickets,
      requesting PTO, or gathering parameters. Note: Slack now recommends using
      Block Kit modals via the Views API, which supersede legacy dialogs."
  - aid: slack:dnd
    name: Slack DND API
    tags:
      - Do Not Disturb
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-dnd-openapi.yml
        type: OpenAPI
    description: "Slack\x19s Do Not Disturb (DND) API lets apps read and manage
      users\x19 notification quiet time so they don\x19t get pinged when
      they\x19ve paused alerts. With the dnd:read and dnd:write scopes, an app
      can check a user\x19s current DND state and scheduled quiet hours,
      retrieve team-wide DND summaries (where permitted), start or extend a
      snooze for a specified duration, and end snooze or active DND. Key methods
      include dnd.info, dnd.teamInfo, dnd.setSnooze, dnd.endSnooze, and
      dnd.endDnd. Responses provide whether DND is enabled and timestamps for
      when it starts and ends, enabling apps to defer messages, schedule work,
      or adjust notification behavior. The API is designed to respect user
      preferences and workspace policies; apps should handle rate limits and
      note that they can set temporary snoozes but cannot programmatically
      change a user\x19s full DND schedule."
  - aid: slack:emoji
    name: Slack Emoji API
    tags:
      - Emoji
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-emoji-openapi.yml
        type: OpenAPI
    description: "Slack\x19s Emoji API lets apps discover and manage a
      workspace\x19s custom emoji. The core method, emoji.list (requires the
      emoji:read scope), returns a name-to-URL map of all custom emoji along
      with aliases (noted as alias:other_name) and a cache timestamp to help
      clients sync efficiently. Apps can also subscribe to the emoji_changed
      event to stay up to date when emoji are added, renamed, or removed. On
      Enterprise Grid, org admins get additional admin.emoji.* methods to
      programmatically add, rename, alias, or remove custom emoji with
      appropriate admin scopes. The API focuses on metadata and management of
      custom emoji (not standard Unicode emoji) and is separate from reactions
      APIs, which use emoji but are managed through different endpoints."
  - aid: slack:files
    name: Slack Files API
    tags:
      - Files
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-files-openapi.yml
        type: OpenAPI
    description: "Slack\x19s Files API lets apps programmatically upload, share, and
      manage files in Slack. Apps can upload binaries (images, docs, code
      snippets) or register links to external files, then attach them to
      channels, DMs, or threads with optional captions. The API supports
      retrieving file metadata and content, listing and filtering files,
      generating or revoking public share links, and deleting files, with access
      controlled by app scopes and channel membership. For large uploads, a
      two-step flow provides an upload URL before finalizing the file, and
      related Events API notifications (for example, file_created and
      file_shared) let apps react to changes. Common uses include import/export
      pipelines, compliance and archiving tools, and integrations with cloud
      storage."
  - aid: slack:migration
    name: Slack Migration API
    tags:
      - Migration
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-migration-openapi.yml
        type: OpenAPI
    description: "Slack\x19s Migration API is a Web API used during Enterprise Grid
      migrations to translate legacy, workspace-scoped identifiers into their
      new, canonical IDs so apps keep working after a workspace moves or merges.
      By calling its migration.exchange method, developers and admins can map
      old user and channel IDs to the new values that Slack assigns in an
      Enterprise Grid org, allowing databases, webhooks, event subscriptions,
      and app configurations to be updated without losing references. It
      complements Admin and SCIM APIs in a migration runbook, but it doesn\x19t
      move content or provision accounts\x14it strictly provides ID remapping to
      preserve continuity."
  - aid: slack:oauth
    name: Slack OAuth API
    tags:
      - OAuth
      - Authentication
      - Authorization
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-oauth-openapi.yml
        type: OpenAPI
    description: "The Slack OAuth API implements the OAuth 2.0 flow that lets
      developers securely install Slack apps to workspaces and obtain access
      tokens with specific, granular scopes. An app redirects a user to Slack
      for consent; after approval, Slack returns an authorization code that the
      app exchanges for tokens (typically a bot token, and optionally a user
      token) to call the Web API within the granted permissions. The OAuth
      system manages scopes, workspace and enterprise installations, admin
      approvals, reauthorization when scopes change, token rotation with refresh
      tokens, and revocation when apps are uninstalled or access is removed. For
      user sign-in, Slack also offers an OpenID Connect\x13based flow. In short,
      it provides consent-driven installation, permissioning, and token
      lifecycle management for Slack apps."
  - aid: slack:pins
    name: Slack Pins API
    tags:
      - Pins
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-pins-openapi.yml
        type: OpenAPI
    description: "The Slack Pins API is a set of Web API methods that let your app
      manage pinned items in conversations so important content is easy to find.
      With pins.add, pins.list, and pins.remove, you can programmatically pin or
      unpin messages, files, and file comments in channels, private channels,
      and DMs by providing the conversation ID and the message timestamp or
      file/comment ID. Pinned items surface in the conversation\x19s details
      panel in the Slack client, and pins.list returns the same set so your app
      can mirror or analyze it. These methods require your app to be a member of
      the conversation and have appropriate permissions, and they observe
      Slack\x19s standard rate limits."
  - aid: slack:reactions
    name: Slack Reactions API
    tags:
      - Reactions
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-reactions-openapi.yml
        type: OpenAPI
    description: "Slack\x19s Reactions API lets apps programmatically manage emoji
      reactions on messages and files, making it easy to capture lightweight
      feedback like approvals, acknowledgments, or votes. Through Web API
      methods (reactions.add, reactions.remove, reactions.get, reactions.list)
      and the Events API (reaction_added and reaction_removed), apps can add or
      delete reactions, read which reactions are on an item, and monitor
      reaction activity in real time. It works with messages (including
      threads), files, and file comments in channels, DMs, and group DMs where
      the app has access. Responses include reaction names, counts, and user
      IDs, and support both standard and custom emoji. Proper scopes
      (reactions:read and reactions:write, plus relevant conversation/file
      scopes) and channel visibility rules apply, rate limits are enforced, and
      each user can apply at most one instance of a given emoji per item."
  - aid: slack:reminders
    name: Slack Reminders API
    tags:
      - Reminders
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-reminders-openapi.yml
        type: OpenAPI
    description: "Slack\x19s Reminders API lets apps create and manage personal
      reminders for Slack users, so teams can automate nudges, follow\x11ups,
      and routine check\x11ins without leaving Slack. Through Web API methods,
      an app can add reminders with natural language or timestamps (including
      recurring patterns like \x1cevery Monday at 9am\x1d), list a user\x19s
      upcoming reminders, fetch details, and mark or delete them when done.
      It\x19s useful for workflows like task handoffs, compliance pings, or
      lightweight to\x11dos that need to surface at the right moment. Access is
      controlled with granular OAuth scopes (reminders:write and
      reminders:read), and reminders are delivered inside Slack where users
      already communicate, keeping prompts contextual and unobtrusive."
  - aid: slack:rtm
    name: Slack RTM API
    tags:
      - Real Time Messaging
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-rtm-openapi.yml
        type: OpenAPI
    description: "The Slack Real Time Messaging (RTM) API lets an app open a
      WebSocket connection to Slack and receive a live stream of JSON events
      from a workspace\x14such as new messages, edits, reactions, user presence
      and typing indicators, channel joins, and more\x14so you can build
      low\x11latency, interactive bots and clients. Apps typically use the RTM
      stream for listening and the Web API for performing actions like posting
      or updating messages. You start by calling rtm.connect (or rtm.start,
      historically) to obtain a WebSocket URL, then maintain the socket to
      process events as they happen. RTM is now considered legacy; for new apps
      Slack recommends using the Events API with the Web API, or Socket Mode if
      you can\x19t expose a public HTTP endpoint."
  - aid: slack:search
    name: Slack Search API
    tags:
      - Search
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-search-openapi.yml
        type: OpenAPI
    description: "Slack\x19s Search API lets apps programmatically find messages and
      files in a workspace using the same query syntax users have in Slack
      (e.g., in:, from:, has:, before:/after:, is:thread). Through endpoints
      like search.messages and search.files, it returns ranked matches with
      snippets and optional highlighting, plus rich metadata such as channel,
      timestamps, user, thread context, permalinks, and file details. You can
      sort by relevance or time, filter with operators, and page through
      results. All results respect the app\x19s scopes and the workspace\x19s
      permissions, retention, and data controls, and the methods are subject to
      rate limits. Teams use it to power features like knowledge lookup, linking
      related conversations, and enabling bots to retrieve relevant historical
      context."
  - aid: slack:stars
    name: Slack Stars API
    tags:
      - Stars
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-stars-openapi.yml
        type: OpenAPI
    description: "The Slack Stars API is a set of Web API methods that let apps
      manage a user\x19s starred items\x14Slack\x19s legacy personal bookmarking
      feature. It allows adding or removing a star on items such as messages
      (via channel and timestamp), files, and file comments, and listing all
      items a user has starred, typically with pagination and basic metadata.
      Stars are user-specific and don\x19t alter the underlying content; they
      simply mark things for quick reference. Note that Slack has moved toward
      Saved items and other mechanisms in the client, and the stars.* methods
      have been deprecated, so availability and support may be limited."
  - aid: slack:team
    name: Slack Team API
    tags:
      - Teams
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-team-openapi.yml
        type: OpenAPI
    description: "Slack\x19s Team API is the part of the Slack Web API that lets
      apps read workspace-level (team) information and, for admins, certain
      audit and billing data. With it, apps can fetch basic workspace identity
      and metadata (name, domain, icon, enterprise association), discover team
      preferences and custom profile fields, and, where permitted, retrieve
      billable info plus access and integration logs for auditing and compliance
      use cases. This helps apps tailor behavior to a workspace\x19s settings,
      build admin dashboards, or automate governance. Access is gated by OAuth
      scopes (for example, team:read and various admin scopes), and many methods
      are limited to workspace or org admins; it doesn\x19t handle messages or
      individual user data beyond what\x19s needed to describe the workspace."
  - aid: slack:usergroups
    name: Slack User Groups API
    tags:
      - Users
      - Groups
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-usergroups-openapi.yml
        type: OpenAPI
    description: "Slack\x19s User Groups API lets apps programmatically create and
      manage user groups (mentionable aliases like @eng or @oncall) in a
      workspace. It supports creating, renaming, and updating groups and their
      handles and descriptions; setting default channels; enabling or disabling
      groups; listing groups; and adding or removing members in bulk. User
      groups make it easy to notify the right people with a single mention and
      to auto-add members to specific channels via default channel settings.
      Teams use the API to automate org changes, sync groups from an identity
      provider, manage on-call rotations, and streamline onboarding/offboarding.
      It\x19s exposed via usergroups.* and usergroups.users.* Web API methods
      and typically requires the usergroups:read and usergroups:write scopes,
      with appropriate admin permissions and a paid Slack plan."
  - aid: slack:users
    name: Slack Users API
    tags:
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-users-openapi.yml
        type: OpenAPI
    description: "Slack\x19s Users API is a set of Web API methods that let your app
      discover and work with people in a Slack workspace. It can list members,
      fetch details for a specific user, look up users by email, and retrieve
      profile data such as names, photos, status, time zones, and custom fields.
      Where permitted, it can also read presence and update a user\x19s profile
      or photo with the proper user-level authorization. Developers use it to
      map real identities to Slack user IDs, personalize experiences, resolve
      mentions and DMs, and distinguish between human, bot, and app users.
      Access to specific data and actions depends on scopes (for example,
      users:read, users:read.email, users.profile:read/write), and certain
      capabilities like presence have additional restrictions. For provisioning
      and enterprise directory management, Slack\x19s SCIM API is used instead."
  - aid: slack:views
    name: Slack Views API
    tags:
      - Views
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-views-openapi.yml
        type: OpenAPI
    description: "The Slack Views API lets your app build and control Block Kit
      interfaces inside Slack\x14primarily modals and the App Home tab. With
      methods like views.open, views.update, and views.push, your app can launch
      multi-step modal flows in response to interactive triggers (slash
      commands, shortcuts, or message actions), update them in place, or push
      new steps onto the stack. Using views.publish, you can render a
      personalized, dynamic Home tab for each user. Submissions and closes
      generate interactivity payloads (view_submission and view_closed) that let
      you validate inputs, return per-field errors, and persist state; you can
      also pass callback_id and private_metadata to track context. Concurrency
      is handled via a view hash to avoid overwriting stale content. In short,
      the Views API provides the lifecycle and plumbing for rich, interactive
      app experiences directly in Slack."
  - aid: slack:workflows
    name: Slack Workflows API
    tags:
      - Workflows
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.example.com
    humanURL: https://developer.github.com/
    properties:
      - url: https://developer.github.com/
        type: Documentation
      - url: properties/slack-workflows-openapi.yml
        type: OpenAPI
    description: "Slack\x19s Workflows API lets you automate work inside Slack by
      defining workflows\x14ordered steps or functions\x14that run in response
      to triggers like shortcuts, messages, schedules, link clicks, or webhooks.
      Developers can build Slack\x11native steps, collect inputs with forms,
      post messages, route approvals, and call external services, then
      programmatically create and manage triggers and runs. On Slack\x19s latest
      platform, you compose workflows from reusable functions, persist data in
      datastores, and run code on Slack\x19s infrastructure; on classic Workflow
      Builder, you can add custom steps and report completion or failure via
      API. The result is secure, auditable, Slack\x11integrated automation for
      tasks such as onboarding, incident response, requests, and notifications
      without standing up a separate backend."
name: Slack
tags:
  - Messaging
  - Chat
  - Bots
  - Productivity
  - T1
type: Contract
access: 3rd-Party
common:
  - url: https://slack-status.com/
    name: Status
    type: Status
  - url: https://api.slack.com/
    name: Unlock your productivity potential with Slack Platform | Slack
    type: Portal
    description: "null"
  - url: https://api.slack.com/automation/quickstart
    name: Quickstart guide for developing automations | Slack
    type: GettingStarted
    description: "null"
  - url: https://api.slack.com/samples
    name: Samples and templates | Slack
    type: Templates
    description: "null"
  - url: https://api.slack.com/docs/developer-sandbox
    name: Developer sandboxes | Slack
    type: Sandbox
    description: "null"
  - url: https://api.slack.com/authentication
    name: Authentication | Slack
    type: Authentication
    description: "null"
  - url: https://api.slack.com/tutorials
    name: Guided tutorials | Slack
    type: Tutorials
    description: "null"
  - url: https://api.slack.com/developer-policy
    name: Slack App Developer Policy | Slack
    type: TermsOfService
    description: "null"
  - url: https://slack.com/intl/en-gb/terms-of-service/api-updated?_gl=1*1yvqubm*_gcl_au*ODQ0OTgxOTg3LjE3MzU5NDg2ODY.*_ga*MTk4NzA1NTA3Ny4xNzM1OTQ4Njg3*_ga_QTJQME5M5D*MTczNTk0ODY4NS4xLjEuMTczNTk0ODk4My41LjAuMA..
    name: Slack API Terms of Service | Legal | Slack
    type: TermsOfService
    description: "null"
  - url: https://slack.com/intl/en-gb/blog
    name: Slack blog | Slack
    type: Blog
    description: "null"
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
created: 2024/04/14
modified: 2025-10-18
position: Consuming
description: Slack is a cloud-based freemium cross-platform instant messaging
  service created by Slack Technologies and currently owned by Salesforce. While
  initially developed for professional and organizational communications, it has
  also been adopted as a community platform.
maintainers:
  - FN: API Evangelist
    url: https://apievangelisgt.com
    email: info@apievangelist.com
specificationVersion: "0.18"
---