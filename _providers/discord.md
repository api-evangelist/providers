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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 167
  human_in_the_loop: 2
  name: Discord Agentic Access
  operation_count: 298
  slug: discord-agentic-access
  summary_line: 298 operations · 167 acting · 2 human-in-the-loop
api_count: 29
apis:
- description: The Discord Gateway API provides persistent, stateful WebSocket connections between your client and Discord servers. These connections are used for sending and receiving real-time events your client c
  name: Discord Gateway API
  slug: discord-gateway-api
- description: The Discord Interactions API enables applications to create and respond to application commands (slash commands), message components, and modals. It supports both Gateway-based and webhook-based inter
  name: Discord Interactions API
  slug: discord-interactions-api
- description: The Discord OAuth2 API enables application developers to build applications that utilize authentication and data from the Discord API. Discord supports the authorization code grant, the implicit grant
  name: Discord OAuth2 API
  slug: discord-oauth2-api
- description: The Discord Webhook Events API provides HTTP-based outgoing webhook events that allow applications to receive notifications for specific events without maintaining a persistent connection. Supported e
  name: Discord Webhook Events API
  slug: discord-webhook-events-api
- description: 'The Discord Embedded App SDK lets you build rich, multiplayer experiences as Activities inside Discord. It handles RPC calls between your application and Discord, enabling interactive activities like '
  name: Discord Embedded App SDK
  slug: discord-embedded-app-sdk
- description: The Discord Voice API provides the protocol for establishing and managing voice connections between clients and Discord voice servers. It handles UDP-based voice data transmission, encryption with XSa
  name: Discord Voice API
  slug: discord-voice-api
- description: The Discord Social SDK allows game developers to add rich social features into their games across desktop, mobile, and console platforms. It supports features like account linking, rich presence, lobb
  name: Discord Social SDK
  slug: discord-social-sdk
- description: Manage global and guild application commands
  name: Discord Application Commands API
  slug: discord-application-commands-api
- description: The Applications API from Discord — 12 operation(s) for applications.
  name: Discord Applications API
  slug: discord-applications-api
- description: Operations on guild audit logs
  name: Discord Audit Log API
  slug: discord-audit-log-api
- description: Operations on auto moderation rules
  name: Discord Auto Moderation API
  slug: discord-auto-moderation-api
- description: The Channels API from Discord — 26 operation(s) for channels.
  name: Discord Channels API
  slug: discord-channels-api
- description: Operations on guild emojis
  name: Discord Emojis API
  slug: discord-emojis-api
- description: The Gateway API from Discord — 2 operation(s) for gateway.
  name: Discord Gateway API
  slug: discord-gateway-api
- description: The Guilds API from Discord — 45 operation(s) for guilds.
  name: Discord Guilds API
  slug: discord-guilds-api
- description: Respond to interactions received from Discord
  name: Discord Interaction Responses API
  slug: discord-interaction-responses-api
- description: The Invites API from Discord — 3 operation(s) for invites.
  name: Discord Invites API
  slug: discord-invites-api
- description: Operations on guild members
  name: Discord Members API
  slug: discord-members-api
- description: Operations on messages within channels
  name: Discord Messages API
  slug: discord-messages-api
- description: Manage application role connection metadata
  name: Discord Role Connections API
  slug: discord-role-connections-api
- description: Operations on guild roles
  name: Discord Roles API
  slug: discord-roles-api
- description: Operations on guild scheduled events
  name: Discord Scheduled Events API
  slug: discord-scheduled-events-api
- description: The Stage Instances API from Discord — 2 operation(s) for stage instances.
  name: Discord Stage Instances API
  slug: discord-stage-instances-api
- description: The Sticker Packs API from Discord — 1 operation(s) for sticker packs.
  name: Discord Sticker Packs API
  slug: discord-sticker-packs-api
- description: The Stickers API from Discord — 3 operation(s) for stickers.
  name: Discord Stickers API
  slug: discord-stickers-api
- description: Retrieve current user information via OAuth2
  name: Discord User Identity API
  slug: discord-user-identity-api
- description: The Users API from Discord — 9 operation(s) for users.
  name: Discord Users API
  slug: discord-users-api
- description: The Voice API from Discord — 1 operation(s) for voice.
  name: Discord Voice API
  slug: discord-voice-api
- description: The Webhooks API from Discord — 8 operation(s) for webhooks.
  name: Discord Webhooks API
  slug: discord-webhooks-api
artifact_total: 550
asyncapis:
- description: The Discord Gateway API provides persistent, stateful WebSocket connections between your client and Discord servers. These connections are used for sending and receiving real-time events your client c
  name: Discord Gateway API
  slug: discord-gateway-api-asyncapi
- description: The Discord Voice API provides the protocol for establishing and managing voice connections between clients and Discord voice servers. It handles UDP-based voice data transmission, encryption with XSa
  name: Discord Voice API
  slug: discord-voice-api-asyncapi
collections:
- collection_type: postman
  name: Discord Interactions Application Commands API
  slug: postman-discord-application-commands-api
- collection_type: postman
  name: Discord Interactions Application Commands Applications API
  slug: postman-discord-applications-api
- collection_type: postman
  name: Discord Interactions Application Commands Audit Log API
  slug: postman-discord-audit-log-api
- collection_type: postman
  name: Discord Interactions Application Commands Auto Moderation API
  slug: postman-discord-auto-moderation-api
- collection_type: postman
  name: Discord Interactions Application Commands Channels API
  slug: postman-discord-channels-api
- collection_type: postman
  name: Discord Interactions Application Commands Emojis API
  slug: postman-discord-emojis-api
- collection_type: postman
  name: Discord Interactions Application Commands Gateway API
  slug: postman-discord-gateway-api
- collection_type: postman
  name: Discord Interactions Application Commands Guilds API
  slug: postman-discord-guilds-api
- collection_type: postman
  name: Discord Interactions Application Commands Interaction Responses API
  slug: postman-discord-interaction-responses-api
- collection_type: postman
  name: Discord Application Commands Interactions API
  slug: postman-discord-interactions-api
- collection_type: postman
  name: Discord Interactions Application Commands Invites API
  slug: postman-discord-invites-api
- collection_type: postman
  name: Discord Interactions Application Commands Members API
  slug: postman-discord-members-api
- collection_type: postman
  name: Discord Interactions Application Commands Messages API
  slug: postman-discord-messages-api
- collection_type: postman
  name: Discord Interactions Application Commands OAuth2 API
  slug: postman-discord-oauth2-api
- collection_type: postman
  name: Discord Interactions Application Commands Role Connections API
  slug: postman-discord-role-connections-api
- collection_type: postman
  name: Discord Interactions Application Commands Roles API
  slug: postman-discord-roles-api
- collection_type: postman
  name: Discord Interactions Application Commands Scheduled Events API
  slug: postman-discord-scheduled-events-api
- collection_type: postman
  name: Discord Interactions Application Commands Stage Instances API
  slug: postman-discord-stage-instances-api
- collection_type: postman
  name: Discord Interactions Application Commands Sticker Packs API
  slug: postman-discord-sticker-packs-api
- collection_type: postman
  name: Discord Interactions Application Commands Stickers API
  slug: postman-discord-stickers-api
- collection_type: postman
  name: Discord Interactions Application Commands User Identity API
  slug: postman-discord-user-identity-api
- collection_type: postman
  name: Discord Interactions Application Commands Users API
  slug: postman-discord-users-api
- collection_type: postman
  name: Discord Interactions Application Commands Voice API
  slug: postman-discord-voice-api
- collection_type: postman
  name: Discord Interactions Application Commands Webhook Events API
  slug: postman-discord-webhook-events-api
- collection_type: postman
  name: Discord Interactions Application Commands Webhooks API
  slug: postman-discord-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Discord Interactions Application Commands API
  slug: open-discord-application-commands-api
- collection_type: open
  name: Discord Interactions Application Commands Applications API
  slug: open-discord-applications-api
- collection_type: open
  name: Discord Interactions Application Commands Audit Log API
  slug: open-discord-audit-log-api
- collection_type: open
  name: Discord Interactions Application Commands Auto Moderation API
  slug: open-discord-auto-moderation-api
- collection_type: open
  name: Discord Interactions Application Commands Channels API
  slug: open-discord-channels-api
- collection_type: open
  name: Discord Interactions Application Commands Emojis API
  slug: open-discord-emojis-api
- collection_type: open
  name: Discord Interactions Application Commands Gateway API
  slug: open-discord-gateway-api
- collection_type: open
  name: Discord Interactions Application Commands Guilds API
  slug: open-discord-guilds-api
- collection_type: open
  name: Discord Interactions Application Commands Interaction Responses API
  slug: open-discord-interaction-responses-api
- collection_type: open
  name: Discord Application Commands Interactions API
  slug: open-discord-interactions-api
- collection_type: open
  name: Discord Interactions Application Commands Invites API
  slug: open-discord-invites-api
- collection_type: open
  name: Discord Linked Roles API
  slug: open-discord-linked-roles-api
- collection_type: open
  name: Discord Interactions Application Commands Members API
  slug: open-discord-members-api
- collection_type: open
  name: Discord Interactions Application Commands Messages API
  slug: open-discord-messages-api
- collection_type: open
  name: Discord Interactions Application Commands OAuth2 API
  slug: open-discord-oauth2-api
- collection_type: open
  name: Discord REST API
  slug: open-discord-rest-api
- collection_type: open
  name: Discord Interactions Application Commands Role Connections API
  slug: open-discord-role-connections-api
- collection_type: open
  name: Discord Interactions Application Commands Roles API
  slug: open-discord-roles-api
- collection_type: open
  name: Discord Interactions Application Commands Scheduled Events API
  slug: open-discord-scheduled-events-api
- collection_type: open
  name: Discord Interactions Application Commands Stage Instances API
  slug: open-discord-stage-instances-api
- collection_type: open
  name: Discord Interactions Application Commands Sticker Packs API
  slug: open-discord-sticker-packs-api
- collection_type: open
  name: Discord Interactions Application Commands Stickers API
  slug: open-discord-stickers-api
- collection_type: open
  name: Discord Interactions Application Commands User Identity API
  slug: open-discord-user-identity-api
- collection_type: open
  name: Discord Interactions Application Commands Users API
  slug: open-discord-users-api
- collection_type: open
  name: Discord Interactions Application Commands Voice API
  slug: open-discord-voice-api
- collection_type: open
  name: Discord Interactions Application Commands Webhook Events API
  slug: open-discord-webhook-events-api
- collection_type: open
  name: Discord Interactions Application Commands Webhooks API
  slug: open-discord-webhooks-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/discord/embedded-app-sdk/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/discord/embedded-app-sdk/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/discord/embedded-app-sdk/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/discord/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/discord-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/discord-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/discord-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/discord-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/discord-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/discord
- group: start
  title: ''
  type: Portal
  url: https://discord.com/developers/applications
- group: commercial
  title: ''
  type: TermsOfService
  url: https://discord.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://discord.com/privacy
- group: commercial
  title: ''
  type: Developer Terms
  url: https://discord.com/developers/docs/policies-and-agreements/developer-terms-of-service
- group: docs
  title: ''
  type: Community Guidelines
  url: https://discord.com/guidelines
- group: company
  title: ''
  type: Blog
  url: https://discord.com/blog
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/discord
- group: docs
  title: ''
  type: Documentation
  url: https://discord.com/developers/docs/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://discord.com/developers/docs/quick-start/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://discord.com/developers/docs/change-log
- group: operate
  title: ''
  type: StatusPage
  url: https://discordstatus.com/
- group: operate
  title: ''
  type: Support
  url: https://support-dev.discord.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/discord
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/discord/discord-api-docs
- group: docs
  title: ''
  type: OpenAPI
  url: https://github.com/discord/discord-api-spec
- group: operate
  title: ''
  type: RateLimits
  url: https://discord.com/developers/docs/topics/rate-limits
- group: other
  title: ''
  type: Permissions
  url: https://discord.com/developers/docs/topics/permissions
- group: auth
  title: ''
  type: Authentication
  url: https://discord.com/developers/docs/topics/oauth2
- group: design
  title: ''
  type: ErrorCodes
  url: https://discord.com/developers/docs/topics/opcodes-and-status-codes
- group: operate
  title: ''
  type: CommunityResources
  url: https://discord.com/developers/docs/developer-tools/community-resources
- group: docs
  title: ''
  type: Documentation
  url: https://discord.com/developers/docs/topics/threads
- group: docs
  title: ''
  type: Documentation
  url: https://discord.com/developers/docs/topics/teams
- group: docs
  title: ''
  type: Documentation
  url: https://discord.com/developers/docs/topics/voice-connections
- group: other
  title: ''
  type: Monetization
  url: https://discord.com/developers/docs/monetization/overview
- group: other
  title: ''
  type: Discovery
  url: https://discord.com/developers/docs/discovery/overview
- group: other
  title: ''
  type: RichPresence
  url: https://discord.com/developers/docs/rich-presence/overview
- group: other
  title: ''
  type: Branding
  url: https://discord.com/branding
- group: operate
  title: ''
  type: Community
  url: https://discord.com/invite/discord-developers
- group: other
  title: ''
  type: DeveloperPolicy
  url: https://discord.com/developers/docs/policies/developer-policy
- group: commercial
  title: ''
  type: DeveloperTermsOfService
  url: https://discord.com/developers/docs/policies/developer-terms-of-service
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/discord-api
- group: build
  title: ''
  type: Game SDK
  url: https://discord.com/developers/docs/game-sdk/sdk-starter-guide
- group: learn
  title: ''
  type: Tutorials
  url: https://discord.com/developers/docs/tutorials/hosting-on-cloudflare-workers
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/discord
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Discord
- group: other
  title: ''
  type: Safety
  url: https://discord.com/safety
- group: other
  title: ''
  type: Developer Policy
  url: https://discord.com/developers/docs/policies-and-agreements/developer-policy
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/discord-guild-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/discord-channel-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/discord-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/discord-user-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/discord-role-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/discord-emoji-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/discord-webhook-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/discord-context.jsonld
created: '2024-04-14'
description: Discord is a voice, video and text communication service used by hundreds of millions of people to hang out and talk with their communities and friends.
features:
- Free Discord with 25 MB upload limit and unlimited servers
- Nitro Basic at $2.99/mo or $29.99/yr with 50 MB uploads
- Nitro at $9.99/mo or $99.99/yr with 500 MB uploads and 2 server boosts
- Discord Bot API free for developers
- 'Global bot rate limit: 50 req/sec'
- Per-route bucket-based rate limits with X-RateLimit-Bucket headers
- 'Webhook execute: 5 req per 2 seconds'
- 'Identify (gateway): 1 per 5 seconds, 1,000 per day'
- 'Invalid request limit: 10,000 per 10 minutes per IP'
- REST API at discord.com/api/v10
- Gateway WebSocket for realtime events
- Voice gateway for voice/video
- Slash commands and interactions API
- Application commands (chat, user, message)
- OAuth 2.0 with bot/identify/guilds scopes
- Custom embeds, components, modals
finops:
- name: Discord Finops
  service_category: Communities
  slug: discord-finops
graphqls:
- description: Discord does not expose a native public GraphQL API. Its developer platform is built on a REST API (discord.com/api/v10), a WebSocket Gateway for real-time events, and an HTTP Webhook Events endpoint.
  name: Discord GraphQL
  slug: discord-graphql
image: https://discord.com/assets/fc0b01fe10a0b8c602fb0106d8189d9b.png
json_schemas:
- name: AccessTokenResponse
  property_count: 7
  slug: discord-accesstokenresponse
- name: AccountResponse
  property_count: 2
  slug: discord-accountresponse
- name: ActionRow
  property_count: 2
  slug: discord-actionrow
- name: AfkTimeouts
  property_count: 0
  slug: discord-afktimeouts
- name: AllowedMentionTypes
  property_count: 0
  slug: discord-allowedmentiontypes
- name: Application
  property_count: 8
  slug: discord-application
- name: ApplicationAuthorizedData
  property_count: 4
  slug: discord-applicationauthorizeddata
- name: ApplicationCommand
  property_count: 14
  slug: discord-applicationcommand
- name: ApplicationCommandAttachmentOption
  property_count: 6
  slug: discord-applicationcommandattachmentoption
- name: ApplicationCommandAttachmentOptionResponse
  property_count: 8
  slug: discord-applicationcommandattachmentoptionresponse
- name: ApplicationCommandAutocompleteCallbackRequest
  property_count: 2
  slug: discord-applicationcommandautocompletecallbackrequest
- name: ApplicationCommandBooleanOption
  property_count: 6
  slug: discord-applicationcommandbooleanoption
- name: ApplicationCommandBooleanOptionResponse
  property_count: 8
  slug: discord-applicationcommandbooleanoptionresponse
- name: ApplicationCommandChannelOption
  property_count: 7
  slug: discord-applicationcommandchanneloption
- name: ApplicationCommandChannelOptionResponse
  property_count: 9
  slug: discord-applicationcommandchanneloptionresponse
- name: ApplicationCommandCreateRequest
  property_count: 8
  slug: discord-applicationcommandcreaterequest
- name: ApplicationCommandIntegerOption
  property_count: 10
  slug: discord-applicationcommandintegeroption
- name: ApplicationCommandIntegerOptionResponse
  property_count: 12
  slug: discord-applicationcommandintegeroptionresponse
- name: ApplicationCommandMentionableOption
  property_count: 6
  slug: discord-applicationcommandmentionableoption
- name: ApplicationCommandMentionableOptionResponse
  property_count: 8
  slug: discord-applicationcommandmentionableoptionresponse
- name: ApplicationCommandNumberOption
  property_count: 10
  slug: discord-applicationcommandnumberoption
- name: ApplicationCommandNumberOptionResponse
  property_count: 12
  slug: discord-applicationcommandnumberoptionresponse
- name: ApplicationCommandOption
  property_count: 14
  slug: discord-applicationcommandoption
- name: ApplicationCommandOptionChoice
  property_count: 3
  slug: discord-applicationcommandoptionchoice
- name: ApplicationCommandOptionIntegerChoice
  property_count: 3
  slug: discord-applicationcommandoptionintegerchoice
- name: ApplicationCommandOptionIntegerChoiceResponse
  property_count: 4
  slug: discord-applicationcommandoptionintegerchoiceresponse
- name: ApplicationCommandOptionNumberChoice
  property_count: 3
  slug: discord-applicationcommandoptionnumberchoice
- name: ApplicationCommandOptionNumberChoiceResponse
  property_count: 4
  slug: discord-applicationcommandoptionnumberchoiceresponse
- name: ApplicationCommandOptionStringChoice
  property_count: 3
  slug: discord-applicationcommandoptionstringchoice
- name: ApplicationCommandOptionStringChoiceResponse
  property_count: 4
  slug: discord-applicationcommandoptionstringchoiceresponse
- name: ApplicationCommandOptionType
  property_count: 0
  slug: discord-applicationcommandoptiontype
- name: ApplicationCommandPatchRequestPartial
  property_count: 7
  slug: discord-applicationcommandpatchrequestpartial
- name: ApplicationCommandPermission
  property_count: 3
  slug: discord-applicationcommandpermission
- name: ApplicationCommandPermissionType
  property_count: 0
  slug: discord-applicationcommandpermissiontype
- name: ApplicationCommandResponse
  property_count: 15
  slug: discord-applicationcommandresponse
- name: ApplicationCommandRoleOption
  property_count: 6
  slug: discord-applicationcommandroleoption
- name: ApplicationCommandRoleOptionResponse
  property_count: 8
  slug: discord-applicationcommandroleoptionresponse
- name: ApplicationCommandStringOption
  property_count: 10
  slug: discord-applicationcommandstringoption
- name: ApplicationCommandStringOptionResponse
  property_count: 12
  slug: discord-applicationcommandstringoptionresponse
- name: ApplicationCommandSubcommandGroupOption
  property_count: 7
  slug: discord-applicationcommandsubcommandgroupoption
- name: ApplicationCommandSubcommandGroupOptionResponse
  property_count: 9
  slug: discord-applicationcommandsubcommandgroupoptionresponse
- name: ApplicationCommandSubcommandOption
  property_count: 7
  slug: discord-applicationcommandsubcommandoption
- name: ApplicationCommandSubcommandOptionResponse
  property_count: 9
  slug: discord-applicationcommandsubcommandoptionresponse
- name: ApplicationCommandType
  property_count: 0
  slug: discord-applicationcommandtype
- name: ApplicationCommandUpdateRequest
  property_count: 9
  slug: discord-applicationcommandupdaterequest
- name: ApplicationCommandUserOption
  property_count: 6
  slug: discord-applicationcommanduseroption
- name: ApplicationCommandUserOptionResponse
  property_count: 8
  slug: discord-applicationcommanduseroptionresponse
- name: ApplicationFormPartial
  property_count: 12
  slug: discord-applicationformpartial
- name: ApplicationIncomingWebhookResponse
  property_count: 8
  slug: discord-applicationincomingwebhookresponse
- name: ApplicationOAuth2InstallParams
  property_count: 2
  slug: discord-applicationoauth2installparams
- name: ApplicationOAuth2InstallParamsResponse
  property_count: 2
  slug: discord-applicationoauth2installparamsresponse
- name: ApplicationResponse
  property_count: 21
  slug: discord-applicationresponse
- name: ApplicationRoleConnection
  property_count: 3
  slug: discord-applicationroleconnection
- name: ApplicationRoleConnectionMetadata
  property_count: 6
  slug: discord-applicationroleconnectionmetadata
- name: ApplicationRoleConnectionsMetadataItemRequest
  property_count: 6
  slug: discord-applicationroleconnectionsmetadataitemrequest
- name: ApplicationRoleConnectionsMetadataItemResponse
  property_count: 6
  slug: discord-applicationroleconnectionsmetadataitemresponse
- name: ApplicationTypes
  property_count: 0
  slug: discord-applicationtypes
- name: ApplicationUserRoleConnectionResponse
  property_count: 3
  slug: discord-applicationuserroleconnectionresponse
- name: Attachment
  property_count: 10
  slug: discord-attachment
- name: AuditLog
  property_count: 6
  slug: discord-auditlog
- name: AuditLogActionTypes
  property_count: 0
  slug: discord-auditlogactiontypes
- name: AuditLogEntryResponse
  property_count: 7
  slug: discord-auditlogentryresponse
- name: AuditLogObjectChangeResponse
  property_count: 3
  slug: discord-auditlogobjectchangeresponse
- name: AuthorizationInformation
  property_count: 4
  slug: discord-authorizationinformation
- name: AutomodActionType
  property_count: 0
  slug: discord-automodactiontype
- name: AutoModerationRule
  property_count: 11
  slug: discord-automoderationrule
- name: AutomodEventType
  property_count: 0
  slug: discord-automodeventtype
- name: AutomodKeywordPresetType
  property_count: 0
  slug: discord-automodkeywordpresettype
- name: AutomodTriggerType
  property_count: 0
  slug: discord-automodtriggertype
- name: AvailableLocalesEnum
  property_count: 0
  slug: discord-availablelocalesenum
- name: Ban
  property_count: 2
  slug: discord-ban
- name: BaseCreateMessageCreateRequest
  property_count: 7
  slug: discord-basecreatemessagecreaterequest
- name: BasicApplicationResponse
  property_count: 8
  slug: discord-basicapplicationresponse
- name: BasicMessageResponse
  property_count: 32
  slug: discord-basicmessageresponse
- name: BlockMessageAction
  property_count: 2
  slug: discord-blockmessageaction
- name: BlockMessageActionMetadata
  property_count: 1
  slug: discord-blockmessageactionmetadata
- name: BlockMessageActionMetadataResponse
  property_count: 1
  slug: discord-blockmessageactionmetadataresponse
- name: BlockMessageActionResponse
  property_count: 2
  slug: discord-blockmessageactionresponse
- name: BotAccountPatchRequest
  property_count: 3
  slug: discord-botaccountpatchrequest
- name: BulkBanUsersResponse
  property_count: 2
  slug: discord-bulkbanusersresponse
- name: Button
  property_count: 8
  slug: discord-button
- name: ButtonStyleTypes
  property_count: 0
  slug: discord-buttonstyletypes
- name: Discord Channel
  property_count: 28
  slug: discord-channel
- name: ChannelFollowerResponse
  property_count: 2
  slug: discord-channelfollowerresponse
- name: ChannelFollowerWebhookResponse
  property_count: 10
  slug: discord-channelfollowerwebhookresponse
- name: ChannelPermissionOverwriteRequest
  property_count: 4
  slug: discord-channelpermissionoverwriterequest
- name: ChannelPermissionOverwriteResponse
  property_count: 4
  slug: discord-channelpermissionoverwriteresponse
- name: ChannelPermissionOverwrites
  property_count: 0
  slug: discord-channelpermissionoverwrites
- name: ChannelSelect
  property_count: 8
  slug: discord-channelselect
- name: ChannelSelectDefaultValue
  property_count: 2
  slug: discord-channelselectdefaultvalue
- name: ChannelTypes
  property_count: 0
  slug: discord-channeltypes
- name: CommandPermissionResponse
  property_count: 3
  slug: discord-commandpermissionresponse
- name: CommandPermissionsResponse
  property_count: 4
  slug: discord-commandpermissionsresponse
- name: Component
  property_count: 12
  slug: discord-component
- name: ConnectedAccountGuildResponse
  property_count: 3
  slug: discord-connectedaccountguildresponse
- name: ConnectedAccountIntegrationResponse
  property_count: 4
  slug: discord-connectedaccountintegrationresponse
- name: ConnectedAccountProviders
  property_count: 0
  slug: discord-connectedaccountproviders
- name: ConnectedAccountResponse
  property_count: 10
  slug: discord-connectedaccountresponse
- name: ConnectedAccountVisibility
  property_count: 0
  slug: discord-connectedaccountvisibility
- name: Connection
  property_count: 9
  slug: discord-connection
- name: CreateApplicationCommandRequest
  property_count: 9
  slug: discord-createapplicationcommandrequest
- name: CreateAutoModerationRuleRequest
  property_count: 8
  slug: discord-createautomoderationrulerequest
- name: CreateChannelRequest
  property_count: 13
  slug: discord-createchannelrequest
- name: CreatedThreadResponse
  property_count: 21
  slug: discord-createdthreadresponse
- name: CreateEntitlementRequestData
  property_count: 3
  slug: discord-createentitlementrequestdata
- name: CreateForumThreadRequest
  property_count: 5
  slug: discord-createforumthreadrequest
- name: CreateGroupDMInviteRequest
  property_count: 1
  slug: discord-creategroupdminviterequest
- name: CreateGuildChannelRequest
  property_count: 18
  slug: discord-createguildchannelrequest
- name: CreateGuildInviteRequest
  property_count: 7
  slug: discord-createguildinviterequest
- name: CreateGuildRequest
  property_count: 11
  slug: discord-createguildrequest
- name: CreateGuildRequestChannelItem
  property_count: 19
  slug: discord-createguildrequestchannelitem
- name: CreateGuildRequestRoleItem
  property_count: 7
  slug: discord-createguildrequestroleitem
- name: CreateInviteRequest
  property_count: 7
  slug: discord-createinviterequest
- name: CreateMessageInteractionCallbackRequest
  property_count: 2
  slug: discord-createmessageinteractioncallbackrequest
- name: CreateMessageRequest
  property_count: 4
  slug: discord-createmessagerequest
- name: CreateOrUpdateThreadTagRequest
  property_count: 4
  slug: discord-createorupdatethreadtagrequest
- name: CreatePrivateChannelRequest
  property_count: 3
  slug: discord-createprivatechannelrequest
- name: CreateRoleRequest
  property_count: 7
  slug: discord-createrolerequest
- name: CreateScheduledEventRequest
  property_count: 9
  slug: discord-createscheduledeventrequest
- name: CreateTextThreadWithMessageRequest
  property_count: 3
  slug: discord-createtextthreadwithmessagerequest
- name: CreateTextThreadWithoutMessageRequest
  property_count: 5
  slug: discord-createtextthreadwithoutmessagerequest
- name: DefaultKeywordListTriggerMetadata
  property_count: 2
  slug: discord-defaultkeywordlisttriggermetadata
- name: DefaultKeywordListTriggerMetadataResponse
  property_count: 2
  slug: discord-defaultkeywordlisttriggermetadataresponse
- name: DefaultKeywordListUpsertRequest
  property_count: 8
  slug: discord-defaultkeywordlistupsertrequest
- name: DefaultKeywordListUpsertRequestPartial
  property_count: 8
  slug: discord-defaultkeywordlistupsertrequestpartial
- name: DefaultKeywordRuleResponse
  property_count: 11
  slug: discord-defaultkeywordruleresponse
- name: DefaultReactionEmojiResponse
  property_count: 2
  slug: discord-defaultreactionemojiresponse
- name: DiscordIntegrationResponse
  property_count: 8
  slug: discord-discordintegrationresponse
- name: EditApplicationCommandRequest
  property_count: 6
  slug: discord-editapplicationcommandrequest
- name: EditMessageRequest
  property_count: 3
  slug: discord-editmessagerequest
- name: Embed
  property_count: 5
  slug: discord-embed
- name: Discord Emoji
  property_count: 8
  slug: discord-emoji
- name: EmojiResponse
  property_count: 8
  slug: discord-emojiresponse
- name: Entitlement
  property_count: 9
  slug: discord-entitlement
- name: EntitlementCreateData
  property_count: 9
  slug: discord-entitlementcreatedata
- name: EntitlementOwnerTypes
  property_count: 0
  slug: discord-entitlementownertypes
- name: EntitlementResponse
  property_count: 12
  slug: discord-entitlementresponse
- name: EntitlementTenantFulfillmentStatusResponse
  property_count: 0
  slug: discord-entitlementtenantfulfillmentstatusresponse
- name: EntitlementTypes
  property_count: 0
  slug: discord-entitlementtypes
- name: EntityMetadataExternal
  property_count: 1
  slug: discord-entitymetadataexternal
- name: EntityMetadataExternalResponse
  property_count: 1
  slug: discord-entitymetadataexternalresponse
- name: EntityMetadataStageInstance
  property_count: 0
  slug: discord-entitymetadatastageinstance
- name: EntityMetadataStageInstanceResponse
  property_count: 0
  slug: discord-entitymetadatastageinstanceresponse
- name: EntityMetadataVoice
  property_count: 0
  slug: discord-entitymetadatavoice
- name: EntityMetadataVoiceResponse
  property_count: 0
  slug: discord-entitymetadatavoiceresponse
- name: Error
  property_count: 2
  slug: discord-error
- name: ErrorDetails
  property_count: 0
  slug: discord-errordetails
- name: ErrorResponse
  property_count: 0
  slug: discord-errorresponse
- name: ExecuteWebhookRequest
  property_count: 9
  slug: discord-executewebhookrequest
- name: ExternalConnectionIntegrationResponse
  property_count: 14
  slug: discord-externalconnectionintegrationresponse
- name: ExternalScheduledEventCreateRequest
  property_count: 9
  slug: discord-externalscheduledeventcreaterequest
- name: ExternalScheduledEventPatchRequestPartial
  property_count: 10
  slug: discord-externalscheduledeventpatchrequestpartial
- name: ExternalScheduledEventResponse
  property_count: 17
  slug: discord-externalscheduledeventresponse
- name: FlagToChannelAction
  property_count: 2
  slug: discord-flagtochannelaction
- name: FlagToChannelActionMetadata
  property_count: 1
  slug: discord-flagtochannelactionmetadata
- name: FlagToChannelActionMetadataResponse
  property_count: 1
  slug: discord-flagtochannelactionmetadataresponse
- name: FlagToChannelActionResponse
  property_count: 2
  slug: discord-flagtochannelactionresponse
- name: ForumLayout
  property_count: 0
  slug: discord-forumlayout
- name: ForumTagResponse
  property_count: 5
  slug: discord-forumtagresponse
- name: FriendInviteResponse
  property_count: 12
  slug: discord-friendinviteresponse
- name: GatewayBotResponse
  property_count: 3
  slug: discord-gatewaybotresponse
- name: GatewayBotSessionStartLimitResponse
  property_count: 4
  slug: discord-gatewaybotsessionstartlimitresponse
- name: GatewayResponse
  property_count: 1
  slug: discord-gatewayresponse
- name: GithubAuthor
  property_count: 2
  slug: discord-githubauthor
- name: GithubCheckApp
  property_count: 1
  slug: discord-githubcheckapp
- name: GithubCheckPullRequest
  property_count: 1
  slug: discord-githubcheckpullrequest
- name: GithubCheckRun
  property_count: 7
  slug: discord-githubcheckrun
- name: GithubCheckRunOutput
  property_count: 2
  slug: discord-githubcheckrunoutput
- name: GithubCheckSuite
  property_count: 5
  slug: discord-githubchecksuite
- name: GithubComment
  property_count: 5
  slug: discord-githubcomment
- name: GithubCommit
  property_count: 4
  slug: discord-githubcommit
- name: GithubDiscussion
  property_count: 6
  slug: discord-githubdiscussion
- name: GithubIssue
  property_count: 7
  slug: discord-githubissue
- name: GithubRelease
  property_count: 4
  slug: discord-githubrelease
- name: GithubRepository
  property_count: 4
  slug: discord-githubrepository
- name: GithubReview
  property_count: 4
  slug: discord-githubreview
- name: GithubUser
  property_count: 4
  slug: discord-githubuser
- name: GithubWebhook
  property_count: 20
  slug: discord-githubwebhook
- name: GroupDMInviteResponse
  property_count: 8
  slug: discord-groupdminviteresponse
- name: Discord Guild
  property_count: 39
  slug: discord-guild
- name: GuildApplicationCommandPermissions
  property_count: 4
  slug: discord-guildapplicationcommandpermissions
- name: GuildAuditLogResponse
  property_count: 8
  slug: discord-guildauditlogresponse
- name: GuildBanResponse
  property_count: 2
  slug: discord-guildbanresponse
- name: GuildChannelResponse
  property_count: 24
  slug: discord-guildchannelresponse
- name: GuildCreateRequest
  property_count: 14
  slug: discord-guildcreaterequest
- name: GuildExplicitContentFilterTypes
  property_count: 0
  slug: discord-guildexplicitcontentfiltertypes
- name: GuildFeatures
  property_count: 0
  slug: discord-guildfeatures
- name: GuildHomeSettingsResponse
  property_count: 5
  slug: discord-guildhomesettingsresponse
- name: GuildIncomingWebhookResponse
  property_count: 10
  slug: discord-guildincomingwebhookresponse
- name: GuildInviteResponse
  property_count: 21
  slug: discord-guildinviteresponse
- name: GuildMember
  property_count: 11
  slug: discord-guildmember
- name: GuildMemberResponse
  property_count: 12
  slug: discord-guildmemberresponse
- name: GuildMFALevel
  property_count: 0
  slug: discord-guildmfalevel
- name: GuildMFALevelResponse
  property_count: 1
  slug: discord-guildmfalevelresponse
- name: GuildNSFWContentLevel
  property_count: 0
  slug: discord-guildnsfwcontentlevel
- name: GuildOnboardingMode
  property_count: 0
  slug: discord-guildonboardingmode
- name: GuildOnboardingResponse
  property_count: 4
  slug: discord-guildonboardingresponse
- name: GuildPatchRequestPartial
  property_count: 22
  slug: discord-guildpatchrequestpartial
- name: GuildPreview
  property_count: 11
  slug: discord-guildpreview
- name: GuildPreviewResponse
  property_count: 12
  slug: discord-guildpreviewresponse
- name: GuildProductPurchaseResponse
  property_count: 2
  slug: discord-guildproductpurchaseresponse
- name: GuildPruneResponse
  property_count: 1
  slug: discord-guildpruneresponse
- name: GuildResponse
  property_count: 39
  slug: discord-guildresponse
- name: GuildRoleResponse
  property_count: 12
  slug: discord-guildroleresponse
- name: GuildRoleTagsResponse
  property_count: 6
  slug: discord-guildroletagsresponse
- name: GuildScheduledEvent
  property_count: 16
  slug: discord-guildscheduledevent
- name: GuildScheduledEventEntityTypes
  property_count: 0
  slug: discord-guildscheduledevententitytypes
- name: GuildScheduledEventPrivacyLevels
  property_count: 0
  slug: discord-guildscheduledeventprivacylevels
- name: GuildScheduledEventStatuses
  property_count: 0
  slug: discord-guildscheduledeventstatuses
- name: GuildStickerResponse
  property_count: 9
  slug: discord-guildstickerresponse
- name: GuildSubscriptionIntegrationResponse
  property_count: 5
  slug: discord-guildsubscriptionintegrationresponse
- name: GuildTemplateChannelResponse
  property_count: 20
  slug: discord-guildtemplatechannelresponse
- name: GuildTemplateChannelTags
  property_count: 4
  slug: discord-guildtemplatechanneltags
- name: GuildTemplateResponse
  property_count: 11
  slug: discord-guildtemplateresponse
- name: GuildTemplateRoleResponse
  property_count: 8
  slug: discord-guildtemplateroleresponse
- name: GuildTemplateSnapshotResponse
  property_count: 13
  slug: discord-guildtemplatesnapshotresponse
- name: GuildWelcomeChannel
  property_count: 4
  slug: discord-guildwelcomechannel
- name: GuildWelcomeScreenChannelResponse
  property_count: 4
  slug: discord-guildwelcomescreenchannelresponse
- name: GuildWelcomeScreenResponse
  property_count: 2
  slug: discord-guildwelcomescreenresponse
- name: GuildWithCountsResponse
  property_count: 41
  slug: discord-guildwithcountsresponse
- name: IconEmojiResponse
  property_count: 0
  slug: discord-iconemojiresponse
- name: IncomingWebhookInteractionRequest
  property_count: 7
  slug: discord-incomingwebhookinteractionrequest
- name: IncomingWebhookRequestPartial
  property_count: 11
  slug: discord-incomingwebhookrequestpartial
- name: IncomingWebhookUpdateForInteractionCallbackRequestPartial
  property_count: 6
  slug: discord-incomingwebhookupdateforinteractioncallbackrequestpartial
- name: IncomingWebhookUpdateRequestPartial
  property_count: 6
  slug: discord-incomingwebhookupdaterequestpartial
- name: InnerErrors
  property_count: 1
  slug: discord-innererrors
- name: InputText
  property_count: 9
  slug: discord-inputtext
- name: Int53Type
  property_count: 0
  slug: discord-int53type
- name: IntegrationApplicationResponse
  property_count: 8
  slug: discord-integrationapplicationresponse
- name: IntegrationExpireBehaviorTypes
  property_count: 0
  slug: discord-integrationexpirebehaviortypes
- name: IntegrationExpireGracePeriodTypes
  property_count: 0
  slug: discord-integrationexpiregraceperiodtypes
- name: IntegrationTypes
  property_count: 0
  slug: discord-integrationtypes
- name: InteractionApplicationCommandAutocompleteCallbackIntegerData
  property_count: 1
  slug: discord-interactionapplicationcommandautocompletecallbackintegerdata
- name: InteractionApplicationCommandAutocompleteCallbackNumberData
  property_count: 1
  slug: discord-interactionapplicationcommandautocompletecallbacknumberdata
- name: InteractionApplicationCommandAutocompleteCallbackStringData
  property_count: 1
  slug: discord-interactionapplicationcommandautocompletecallbackstringdata
- name: InteractionCallbackData
  property_count: 9
  slug: discord-interactioncallbackdata
- name: InteractionCallbackResponse
  property_count: 2
  slug: discord-interactioncallbackresponse
- name: InteractionCallbackTypes
  property_count: 0
  slug: discord-interactioncallbacktypes
- name: InteractionResponse
  property_count: 2
  slug: discord-interactionresponse
- name: InteractionTypes
  property_count: 0
  slug: discord-interactiontypes
- name: Invite
  property_count: 14
  slug: discord-invite
- name: InviteApplicationResponse
  property_count: 21
  slug: discord-inviteapplicationresponse
- name: InviteChannelRecipientResponse
  property_count: 1
  slug: discord-invitechannelrecipientresponse
- name: InviteChannelResponse
  property_count: 5
  slug: discord-invitechannelresponse
- name: InviteGuildResponse
  property_count: 12
  slug: discord-inviteguildresponse
- name: InviteStageInstanceResponse
  property_count: 4
  slug: discord-invitestageinstanceresponse
- name: InviteTargetTypes
  property_count: 0
  slug: discord-invitetargettypes
- name: InviteTypes
  property_count: 0
  slug: discord-invitetypes
- name: KeywordRuleResponse
  property_count: 11
  slug: discord-keywordruleresponse
- name: KeywordTriggerMetadata
  property_count: 3
  slug: discord-keywordtriggermetadata
- name: KeywordTriggerMetadataResponse
  property_count: 3
  slug: discord-keywordtriggermetadataresponse
- name: KeywordUpsertRequest
  property_count: 8
  slug: discord-keywordupsertrequest
- name: KeywordUpsertRequestPartial
  property_count: 8
  slug: discord-keywordupsertrequestpartial
- name: MentionableSelect
  property_count: 7
  slug: discord-mentionableselect
- name: MentionSpamRuleResponse
  property_count: 11
  slug: discord-mentionspamruleresponse
- name: MentionSpamTriggerMetadata
  property_count: 2
  slug: discord-mentionspamtriggermetadata
- name: MentionSpamTriggerMetadataResponse
  property_count: 1
  slug: discord-mentionspamtriggermetadataresponse
- name: MentionSpamUpsertRequest
  property_count: 8
  slug: discord-mentionspamupsertrequest
- name: MentionSpamUpsertRequestPartial
  property_count: 8
  slug: discord-mentionspamupsertrequestpartial
- name: Discord Message
  property_count: 24
  slug: discord-message
- name: MessageActivityResponse
  property_count: 0
  slug: discord-messageactivityresponse
- name: MessageAllowedMentionsRequest
  property_count: 4
  slug: discord-messageallowedmentionsrequest
- name: MessageAttachmentRequest
  property_count: 4
  slug: discord-messageattachmentrequest
- name: MessageAttachmentResponse
  property_count: 16
  slug: discord-messageattachmentresponse
- name: MessageCallResponse
  property_count: 2
  slug: discord-messagecallresponse
- name: MessageComponentActionRowResponse
  property_count: 3
  slug: discord-messagecomponentactionrowresponse
- name: MessageComponentButtonResponse
  property_count: 8
  slug: discord-messagecomponentbuttonresponse
- name: MessageComponentChannelSelectResponse
  property_count: 8
  slug: discord-messagecomponentchannelselectresponse
- name: MessageComponentEmojiResponse
  property_count: 3
  slug: discord-messagecomponentemojiresponse
- name: MessageComponentInputTextResponse
  property_count: 10
  slug: discord-messagecomponentinputtextresponse
- name: MessageComponentMentionableSelectResponse
  property_count: 7
  slug: discord-messagecomponentmentionableselectresponse
- name: MessageComponentRoleSelectResponse
  property_count: 7
  slug: discord-messagecomponentroleselectresponse
- name: MessageComponentStringSelectResponse
  property_count: 8
  slug: discord-messagecomponentstringselectresponse
- name: MessageComponentTypes
  property_count: 0
  slug: discord-messagecomponenttypes
- name: MessageComponentUserSelectResponse
  property_count: 7
  slug: discord-messagecomponentuserselectresponse
- name: MessageCreateRequest
  property_count: 10
  slug: discord-messagecreaterequest
- name: MessageEditRequestPartial
  property_count: 7
  slug: discord-messageeditrequestpartial
- name: MessageEmbedAuthorResponse
  property_count: 4
  slug: discord-messageembedauthorresponse
- name: MessageEmbedFieldResponse
  property_count: 3
  slug: discord-messageembedfieldresponse
- name: MessageEmbedFooterResponse
  property_count: 3
  slug: discord-messageembedfooterresponse
- name: MessageEmbedImageResponse
  property_count: 6
  slug: discord-messageembedimageresponse
- name: MessageEmbedProviderResponse
  property_count: 2
  slug: discord-messageembedproviderresponse
- name: MessageEmbedResponse
  property_count: 13
  slug: discord-messageembedresponse
- name: MessageEmbedVideoResponse
  property_count: 6
  slug: discord-messageembedvideoresponse
- name: MessageInteractionResponse
  property_count: 5
  slug: discord-messageinteractionresponse
- name: MessageMentionChannelResponse
  property_count: 4
  slug: discord-messagementionchannelresponse
- name: MessageReactionCountDetailsResponse
  property_count: 2
  slug: discord-messagereactioncountdetailsresponse
- name: MessageReactionEmojiResponse
  property_count: 3
  slug: discord-messagereactionemojiresponse
- name: MessageReactionResponse
  property_count: 6
  slug: discord-messagereactionresponse
- name: MessageReferenceRequest
  property_count: 5
  slug: discord-messagereferencerequest
- name: MessageReferenceResponse
  property_count: 4
  slug: discord-messagereferenceresponse
- name: MessageReferenceType
  property_count: 0
  slug: discord-messagereferencetype
- name: MessageResponse
  property_count: 34
  slug: discord-messageresponse
- name: MessageRoleSubscriptionDataResponse
  property_count: 4
  slug: discord-messagerolesubscriptiondataresponse
- name: MessageStickerItemResponse
  property_count: 3
  slug: discord-messagestickeritemresponse
- name: MessageType
  property_count: 0
  slug: discord-messagetype
- name: MetadataItemTypes
  property_count: 0
  slug: discord-metadataitemtypes
- name: MLSpamRuleResponse
  property_count: 11
  slug: discord-mlspamruleresponse
- name: MLSpamTriggerMetadata
  property_count: 0
  slug: discord-mlspamtriggermetadata
- name: MLSpamTriggerMetadataResponse
  property_count: 0
  slug: discord-mlspamtriggermetadataresponse
- name: MLSpamUpsertRequest
  property_count: 8
  slug: discord-mlspamupsertrequest
- name: MLSpamUpsertRequestPartial
  property_count: 8
  slug: discord-mlspamupsertrequestpartial
- name: ModalInteractionCallbackData
  property_count: 3
  slug: discord-modalinteractioncallbackdata
- name: ModalInteractionCallbackRequest
  property_count: 2
  slug: discord-modalinteractioncallbackrequest
- name: ModifyChannelRequest
  property_count: 13
  slug: discord-modifychannelrequest
- name: ModifyGuildRequest
  property_count: 19
  slug: discord-modifyguildrequest
- name: MyGuildResponse
  property_count: 8
  slug: discord-myguildresponse
- name: NewMemberActionResponse
  property_count: 6
  slug: discord-newmemberactionresponse
- name: NewMemberActionType
  property_count: 0
  slug: discord-newmemberactiontype
- name: OAuth2GetAuthorizationResponse
  property_count: 4
  slug: discord-oauth2getauthorizationresponse
- name: OAuth2GetKeys
  property_count: 1
  slug: discord-oauth2getkeys
- name: OAuth2Key
  property_count: 6
  slug: discord-oauth2key
- name: OAuth2Scopes
  property_count: 0
  slug: discord-oauth2scopes
- name: OnboardingPromptOptionRequest
  property_count: 8
  slug: discord-onboardingpromptoptionrequest
- name: OnboardingPromptOptionResponse
  property_count: 6
  slug: discord-onboardingpromptoptionresponse
- name: OnboardingPromptResponse
  property_count: 7
  slug: discord-onboardingpromptresponse
- name: OnboardingPromptType
  property_count: 0
  slug: discord-onboardingprompttype
- name: Overwrite
  property_count: 4
  slug: discord-overwrite
- name: PartialDiscordIntegrationResponse
  property_count: 5
  slug: discord-partialdiscordintegrationresponse
- name: PartialExternalConnectionIntegrationResponse
  property_count: 4
  slug: discord-partialexternalconnectionintegrationresponse
- name: PartialGuild
  property_count: 6
  slug: discord-partialguild
- name: PartialGuildSubscriptionIntegrationResponse
  property_count: 4
  slug: discord-partialguildsubscriptionintegrationresponse
- name: PongInteractionCallbackRequest
  property_count: 1
  slug: discord-ponginteractioncallbackrequest
- name: PremiumGuildTiers
  property_count: 0
  slug: discord-premiumguildtiers
- name: PremiumTypes
  property_count: 0
  slug: discord-premiumtypes
- name: PrivateApplicationResponse
  property_count: 27
  slug: discord-privateapplicationresponse
- name: PrivateChannelRequestPartial
  property_count: 2
  slug: discord-privatechannelrequestpartial
- name: PrivateChannelResponse
  property_count: 6
  slug: discord-privatechannelresponse
- name: PrivateGroupChannelResponse
  property_count: 11
  slug: discord-privategroupchannelresponse
- name: PrivateGuildMemberResponse
  property_count: 13
  slug: discord-privateguildmemberresponse
- name: PurchaseNotificationResponse
  property_count: 2
  slug: discord-purchasenotificationresponse
- name: PurchaseType
  property_count: 0
  slug: discord-purchasetype
- name: QuarantineUserAction
  property_count: 2
  slug: discord-quarantineuseraction
- name: QuarantineUserActionMetadata
  property_count: 0
  slug: discord-quarantineuseractionmetadata
- name: QuarantineUserActionMetadataResponse
  property_count: 0
  slug: discord-quarantineuseractionmetadataresponse
- name: QuarantineUserActionResponse
  property_count: 2
  slug: discord-quarantineuseractionresponse
- name: QuestUserEnrollmentData
  property_count: 3
  slug: discord-questuserenrollmentdata
- name: Reaction
  property_count: 5
  slug: discord-reaction
- name: ResolvedObjectsResponse
  property_count: 4
  slug: discord-resolvedobjectsresponse
- name: ResourceChannelResponse
  property_count: 5
  slug: discord-resourcechannelresponse
- name: RichEmbed
  property_count: 13
  slug: discord-richembed
- name: RichEmbedAuthor
  property_count: 3
  slug: discord-richembedauthor
- name: RichEmbedField
  property_count: 3
  slug: discord-richembedfield
- name: RichEmbedFooter
  property_count: 2
  slug: discord-richembedfooter
- name: RichEmbedImage
  property_count: 5
  slug: discord-richembedimage
- name: RichEmbedProvider
  property_count: 2
  slug: discord-richembedprovider
- name: RichEmbedThumbnail
  property_count: 5
  slug: discord-richembedthumbnail
- name: RichEmbedVideo
  property_count: 5
  slug: discord-richembedvideo
- name: Discord Role
  property_count: 12
  slug: discord-role
- name: RoleSelect
  property_count: 7
  slug: discord-roleselect
- name: RoleSelectDefaultValue
  property_count: 2
  slug: discord-roleselectdefaultvalue
- name: RoleTags
  property_count: 6
  slug: discord-roletags
- name: ScheduledEventResponse
  property_count: 16
  slug: discord-scheduledeventresponse
- name: ScheduledEventUserResponse
  property_count: 4
  slug: discord-scheduledeventuserresponse
- name: SelectOption
  property_count: 5
  slug: discord-selectoption
- name: SelectOptionResponse
  property_count: 5
  slug: discord-selectoptionresponse
- name: SettingsEmojiResponse
  property_count: 3
  slug: discord-settingsemojiresponse
- name: SlackWebhook
  property_count: 4
  slug: discord-slackwebhook
- name: Snowflake
  property_count: 0
  slug: discord-snowflake
- name: SnowflakeSelectDefaultValueTypes
  property_count: 0
  slug: discord-snowflakeselectdefaultvaluetypes
- name: SnowflakeType
  property_count: 0
  slug: discord-snowflaketype
- name: SpamLinkRuleResponse
  property_count: 11
  slug: discord-spamlinkruleresponse
- name: SpamLinkTriggerMetadataResponse
  property_count: 0
  slug: discord-spamlinktriggermetadataresponse
- name: StageInstance
  property_count: 7
  slug: discord-stageinstance
- name: StageInstanceResponse
  property_count: 7
  slug: discord-stageinstanceresponse
- name: StageInstancesPrivacyLevels
  property_count: 0
  slug: discord-stageinstancesprivacylevels
- name: StageScheduledEventCreateRequest
  property_count: 9
  slug: discord-stagescheduledeventcreaterequest
- name: StageScheduledEventPatchRequestPartial
  property_count: 10
  slug: discord-stagescheduledeventpatchrequestpartial
- name: StageScheduledEventResponse
  property_count: 17
  slug: discord-stagescheduledeventresponse
- name: StandardStickerResponse
  property_count: 8
  slug: discord-standardstickerresponse
- name: StartThreadRequest
  property_count: 5
  slug: discord-startthreadrequest
- name: Sticker
  property_count: 11
  slug: discord-sticker
- name: StickerFormatTypes
  property_count: 0
  slug: discord-stickerformattypes
- name: StickerPack
  property_count: 7
  slug: discord-stickerpack
- name: StickerPackCollectionResponse
  property_count: 1
  slug: discord-stickerpackcollectionresponse
- name: StickerPackResponse
  property_count: 7
  slug: discord-stickerpackresponse
- name: StickerTypes
  property_count: 0
  slug: discord-stickertypes
- name: StringSelect
  property_count: 7
  slug: discord-stringselect
- name: TeamMemberResponse
  property_count: 3
  slug: discord-teammemberresponse
- name: TeamMembershipStates
  property_count: 0
  slug: discord-teammembershipstates
- name: TeamResponse
  property_count: 5
  slug: discord-teamresponse
- name: TextStyleTypes
  property_count: 0
  slug: discord-textstyletypes
- name: ThreadAutoArchiveDuration
  property_count: 0
  slug: discord-threadautoarchiveduration
- name: ThreadMemberResponse
  property_count: 5
  slug: discord-threadmemberresponse
- name: ThreadMetadata
  property_count: 6
  slug: discord-threadmetadata
- name: ThreadMetadataResponse
  property_count: 6
  slug: discord-threadmetadataresponse
- name: ThreadResponse
  property_count: 21
  slug: discord-threadresponse
- name: ThreadSortOrder
  property_count: 0
  slug: discord-threadsortorder
- name: ThreadsResponse
  property_count: 3
  slug: discord-threadsresponse
- name: TypingIndicatorResponse
  property_count: 0
  slug: discord-typingindicatorresponse
- name: UInt32Type
  property_count: 0
  slug: discord-uint32type
- name: UpdateApplicationRoleConnectionRequest
  property_count: 3
  slug: discord-updateapplicationroleconnectionrequest
- name: UpdateDefaultReactionEmojiRequest
  property_count: 2
  slug: discord-updatedefaultreactionemojirequest
- name: UpdateGuildChannelRequestPartial
  property_count: 19
  slug: discord-updateguildchannelrequestpartial
- name: UpdateGuildOnboardingRequest
  property_count: 4
  slug: discord-updateguildonboardingrequest
- name: UpdateMessageInteractionCallbackRequest
  property_count: 2
  slug: discord-updatemessageinteractioncallbackrequest
- name: UpdateOnboardingPromptRequest
  property_count: 7
  slug: discord-updateonboardingpromptrequest
- name: UpdateThreadRequestPartial
  property_count: 12
  slug: discord-updatethreadrequestpartial
- name: UpdateThreadTagRequest
  property_count: 5
  slug: discord-updatethreadtagrequest
- name: Discord User
  property_count: 17
  slug: discord-user
- name: UserAvatarDecorationResponse
  property_count: 0
  slug: discord-useravatardecorationresponse
- name: UserCommunicationDisabledAction
  property_count: 2
  slug: discord-usercommunicationdisabledaction
- name: UserCommunicationDisabledActionMetadata
  property_count: 1
  slug: discord-usercommunicationdisabledactionmetadata
- name: UserCommunicationDisabledActionMetadataResponse
  property_count: 1
  slug: discord-usercommunicationdisabledactionmetadataresponse
- name: UserCommunicationDisabledActionResponse
  property_count: 2
  slug: discord-usercommunicationdisabledactionresponse
- name: UserGuildOnboardingResponse
  property_count: 4
  slug: discord-userguildonboardingresponse
- name: UserNotificationSettings
  property_count: 0
  slug: discord-usernotificationsettings
- name: UserPIIResponse
  property_count: 16
  slug: discord-userpiiresponse
- name: UserResponse
  property_count: 11
  slug: discord-userresponse
- name: UserSelect
  property_count: 7
  slug: discord-userselect
- name: UserSelectDefaultValue
  property_count: 2
  slug: discord-userselectdefaultvalue
- name: VanityURLErrorResponse
  property_count: 2
  slug: discord-vanityurlerrorresponse
- name: VanityURLResponse
  property_count: 3
  slug: discord-vanityurlresponse
- name: VerificationLevels
  property_count: 0
  slug: discord-verificationlevels
- name: VideoQualityModes
  property_count: 0
  slug: discord-videoqualitymodes
- name: VoiceRegion
  property_count: 5
  slug: discord-voiceregion
- name: VoiceRegionResponse
  property_count: 5
  slug: discord-voiceregionresponse
- name: VoiceScheduledEventCreateRequest
  property_count: 9
  slug: discord-voicescheduledeventcreaterequest
- name: VoiceScheduledEventPatchRequestPartial
  property_count: 10
  slug: discord-voicescheduledeventpatchrequestpartial
- name: VoiceScheduledEventResponse
  property_count: 17
  slug: discord-voicescheduledeventresponse
- name: Discord Webhook
  property_count: 12
  slug: discord-webhook
- name: WebhookEvent
  property_count: 4
  slug: discord-webhookevent
- name: WebhookEventBody
  property_count: 3
  slug: discord-webhookeventbody
- name: WebhookSlackEmbed
  property_count: 14
  slug: discord-webhookslackembed
- name: WebhookSlackEmbedField
  property_count: 3
  slug: discord-webhookslackembedfield
- name: WebhookSourceChannelResponse
  property_count: 2
  slug: discord-webhooksourcechannelresponse
- name: WebhookSourceGuildResponse
  property_count: 3
  slug: discord-webhooksourceguildresponse
- name: WebhookTypes
  property_count: 0
  slug: discord-webhooktypes
- name: WelcomeMessageResponse
  property_count: 2
  slug: discord-welcomemessageresponse
- name: WelcomeScreenPatchRequestPartial
  property_count: 3
  slug: discord-welcomescreenpatchrequestpartial
- name: WidgetActivity
  property_count: 1
  slug: discord-widgetactivity
- name: WidgetChannel
  property_count: 3
  slug: discord-widgetchannel
- name: WidgetImageStyles
  property_count: 0
  slug: discord-widgetimagestyles
- name: WidgetMember
  property_count: 13
  slug: discord-widgetmember
- name: WidgetResponse
  property_count: 6
  slug: discord-widgetresponse
- name: WidgetSettingsResponse
  property_count: 2
  slug: discord-widgetsettingsresponse
- name: WidgetUserDiscriminator
  property_count: 0
  slug: discord-widgetuserdiscriminator
json_structures:
- name: Discord Structure
  property_count: 0
  slug: discord-structure
jsonld:
- class_count: 0
  name: Discord Context
  property_count: 12
  slug: discord-context
layout: provider
modified: '2026-05-19'
name: Discord
nav: Providers
network: true
overview: 'Discord publishes 27 APIs on the [APIs.io](https://apis.io/) network, including Gateway API, Interactions API, OAuth2 API, and 24 more. Tagged areas include Chat, Communications, Gaming, Messaging, and Social.


  The Discord catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Discord''s developer surface includes authentication, developer portal, engineering blog, documentation, getting-started guide, changelog, support, and 48 more developer resources.'
plans:
- name: Discord Plans Pricing
  plan_count: 3
  slug: discord-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Discord Rate Limits
  slug: discord-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Discord API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: discord-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Discord API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: discord-jsonschema-spectral-rules
scopes:
- name: Discord Scopes
  scope_count: 33
  slug: discord-scopes
  summary_line: 33 scopes · implicit/clientCredentials/authorizationCode
score:
  band: developing
  composite: 49.8
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 13.6
    contract_quality: 74.0
    developer_ergonomics: 54.8
    discoverability: 55.6
    governance: 13.6
    operational_transparency: 44.7
  previous_composite: 49.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/discord/refs/heads/main/screenshots/discord-2026-06-20T180039.png
security:
- kind: authentication
  name: Discord Authentication
  slug: discord-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Discord Domain Security
  slug: discord-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Discord Vulnerability Disclosure
  slug: discord-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: discord
tags:
- Chat
- Communications
- Gaming
- Messaging
- Social
- Video
- Voice
website: https://discord.com/developers/applications
---
