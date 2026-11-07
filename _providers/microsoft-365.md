---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Microsoft 365 Agentic Access
  operation_count: 18
  slug: microsoft-365-agentic-access
  summary_line: 18 operations · 5 acting
api_count: 7
apis:
- description: Unified REST API providing a single endpoint to access data and intelligence across Microsoft 365, Microsoft Entra ID, Windows, and Enterprise Mobility + Security. Supports OAuth 2.0 authentication an
  name: Microsoft Graph API
  slug: graph-api
- description: Beta endpoint of the Microsoft Graph API offering preview features and resources before they are promoted to v1.0, including additional insights, reporting, and management capabilities.
  name: Microsoft Graph Beta API
  slug: graph-beta-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Microsoft Graph v1.0 Calendar workload, from the first-party OpenAPI module Microsoft publishes in microsoftgraph/msgraph-sdk-powershell (servers https://graph.microsoft.com/v1.0).
  name: Microsoft 365 Calendar API
  slug: microsoft-365-calendar-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Microsoft Graph v1.0 Files workload, from the first-party OpenAPI module Microsoft publishes in microsoftgraph/msgraph-sdk-powershell (servers https://graph.microsoft.com/v1.0).
  name: Microsoft 365 Files API
  slug: microsoft-365-files-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Microsoft Graph v1.0 Groups workload, from the first-party OpenAPI module Microsoft publishes in microsoftgraph/msgraph-sdk-powershell (servers https://graph.microsoft.com/v1.0).
  name: Microsoft 365 Groups API
  slug: microsoft-365-groups-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Microsoft Graph v1.0 Mail workload, from the first-party OpenAPI module Microsoft publishes in microsoftgraph/msgraph-sdk-powershell (servers https://graph.microsoft.com/v1.0).
  name: Microsoft 365 Mail API
  slug: microsoft-365-mail-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: The Me API from Microsoft 365 — 3 operation(s) for me.
  name: Microsoft 365 Me API
  slug: microsoft-365-me-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Microsoft Graph v1.0 Teams workload, from the first-party OpenAPI module Microsoft publishes in microsoftgraph/msgraph-sdk-powershell (servers https://graph.microsoft.com/v1.0).
  name: Microsoft 365 Teams API
  slug: microsoft-365-teams-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Microsoft Graph v1.0 Users workload, from the first-party OpenAPI module Microsoft publishes in microsoftgraph/msgraph-sdk-powershell (servers https://graph.microsoft.com/v1.0).
  name: Microsoft 365 Users API
  slug: microsoft-365-users-api
- description: 'Remote Model Context Protocol server (public preview) that lets AI agents query Microsoft Entra tenant data with natural language, translated into read-only Microsoft Graph calls; OAuth via Microsoft '
  name: Microsoft MCP Server for Enterprise
  slug: mcp-server-enterprise
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The appCatalogs.teamsApp API from Microsoft 365 — 7 operation(s) for appcatalogs.teamsapp.
  name: Microsoft 365 App Catalogs.teams App API
  slug: microsoft-365-appcatalogs-teamsapp-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The chats.chat.Actions API from Microsoft 365 — 8 operation(s) for chats.chat.actions.
  name: Microsoft 365 Chats.chat.Actions API
  slug: microsoft-365-chats-chat-actions-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The chats.chat API from Microsoft 365 — 3 operation(s) for chats.chat.
  name: Microsoft 365 Chats.chat API
  slug: microsoft-365-chats-chat-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The chats.chat.Functions API from Microsoft 365 — 2 operation(s) for chats.chat.functions.
  name: Microsoft 365 Chats.chat.Functions API
  slug: microsoft-365-chats-chat-functions-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The chats.chatMessage API from Microsoft 365 — 26 operation(s) for chats.chatmessage.
  name: Microsoft 365 Chats.chat Message API
  slug: microsoft-365-chats-chatmessage-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The chats.chatMessageInfo API from Microsoft 365 — 1 operation(s) for chats.chatmessageinfo.
  name: Microsoft 365 Chats.chat Message Info API
  slug: microsoft-365-chats-chatmessageinfo-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The chats.conversationMember API from Microsoft 365 — 5 operation(s) for chats.conversationmember.
  name: Microsoft 365 Chats.conversation Member API
  slug: microsoft-365-chats-conversationmember-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The chats.pinnedChatMessageInfo API from Microsoft 365 — 4 operation(s) for chats.pinnedchatmessageinfo.
  name: Microsoft 365 Chats.pinned Chat Message Info API
  slug: microsoft-365-chats-pinnedchatmessageinfo-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The chats.resourceSpecificPermissionGrant API from Microsoft 365 — 3 operation(s) for chats.resourcespecificpermissiongrant.
  name: Microsoft 365 Chats.resource Specific Permission Grant API
  slug: microsoft-365-chats-resourcespecificpermissiongrant-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The chats.targetedChatMessage API from Microsoft 365 — 20 operation(s) for chats.targetedchatmessage.
  name: Microsoft 365 Chats.targeted Chat Message API
  slug: microsoft-365-chats-targetedchatmessage-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The chats.teamsAppInstallation API from Microsoft 365 — 6 operation(s) for chats.teamsappinstallation.
  name: Microsoft 365 Chats.teams App Installation API
  slug: microsoft-365-chats-teamsappinstallation-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The chats.teamsTab API from Microsoft 365 — 4 operation(s) for chats.teamstab.
  name: Microsoft 365 Chats.teams Tab API
  slug: microsoft-365-chats-teamstab-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The drives.drive API from Microsoft 365 — 2 operation(s) for drives.drive.
  name: Microsoft 365 Drives.drive API
  slug: microsoft-365-drives-drive-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The drives.drive.Functions API from Microsoft 365 — 3 operation(s) for drives.drive.functions.
  name: Microsoft 365 Drives.drive.Functions API
  slug: microsoft-365-drives-drive-functions-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The drives.driveItem API from Microsoft 365 — 198 operation(s) for drives.driveitem.
  name: Microsoft 365 Drives.drive Item API
  slug: microsoft-365-drives-driveitem-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The drives.list API from Microsoft 365 — 84 operation(s) for drives.list.
  name: Microsoft 365 Drives.list API
  slug: microsoft-365-drives-list-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The drives.user API from Microsoft 365 — 8 operation(s) for drives.user.
  name: Microsoft 365 Drives.user API
  slug: microsoft-365-drives-user-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groupLifecyclePolicies.groupLifecyclePolicy.Actions API from Microsoft 365 — 2 operation(s) for grouplifecyclepolicies.grouplifecyclepolicy.actions.
  name: Microsoft 365 Group Lifecycle Policies.group Lifecycle Policy.Actions API
  slug: microsoft-365-grouplifecyclepolicies-grouplifecyclepolicy-actions-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groupLifecyclePolicies.groupLifecyclePolicy API from Microsoft 365 — 3 operation(s) for grouplifecyclepolicies.grouplifecyclepolicy.
  name: Microsoft 365 Group Lifecycle Policies.group Lifecycle Policy API
  slug: microsoft-365-grouplifecyclepolicies-grouplifecyclepolicy-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groups.calendar API from Microsoft 365 — 31 operation(s) for groups.calendar.
  name: Microsoft 365 Groups.calendar API
  slug: microsoft-365-groups-calendar-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groups.conversation API from Microsoft 365 — 29 operation(s) for groups.conversation.
  name: Microsoft 365 Groups.conversation API
  slug: microsoft-365-groups-conversation-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groups.conversationThread API from Microsoft 365 — 26 operation(s) for groups.conversationthread.
  name: Microsoft 365 Groups.conversation Thread API
  slug: microsoft-365-groups-conversationthread-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groups.directoryObject API from Microsoft 365 — 113 operation(s) for groups.directoryobject.
  name: Microsoft 365 Groups.directory Object API
  slug: microsoft-365-groups-directoryobject-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groups.drive API from Microsoft 365 — 296 operation(s) for groups.drive.
  name: Microsoft 365 Groups.drive API
  slug: microsoft-365-groups-drive-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groups.event API from Microsoft 365 — 24 operation(s) for groups.event.
  name: Microsoft 365 Groups.event API
  slug: microsoft-365-groups-event-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groups.extension API from Microsoft 365 — 3 operation(s) for groups.extension.
  name: Microsoft 365 Groups.extension API
  slug: microsoft-365-groups-extension-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groups.group.Actions API from Microsoft 365 — 18 operation(s) for groups.group.actions.
  name: Microsoft 365 Groups.group.Actions API
  slug: microsoft-365-groups-group-actions-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groups.group API from Microsoft 365 — 4 operation(s) for groups.group.
  name: Microsoft 365 Groups.group API
  slug: microsoft-365-groups-group-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groups.group.Functions API from Microsoft 365 — 4 operation(s) for groups.group.functions.
  name: Microsoft 365 Groups.group.Functions API
  slug: microsoft-365-groups-group-functions-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groups.groupLifecyclePolicy API from Microsoft 365 — 5 operation(s) for groups.grouplifecyclepolicy.
  name: Microsoft 365 Groups.group Lifecycle Policy API
  slug: microsoft-365-groups-grouplifecyclepolicy-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groups.groupSetting API from Microsoft 365 — 3 operation(s) for groups.groupsetting.
  name: Microsoft 365 Groups.group Setting API
  slug: microsoft-365-groups-groupsetting-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groups.onPremisesSyncBehavior API from Microsoft 365 — 1 operation(s) for groups.onpremisessyncbehavior.
  name: Microsoft 365 Groups.on Premises Sync Behavior API
  slug: microsoft-365-groups-onpremisessyncbehavior-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groups.profilePhoto API from Microsoft 365 — 5 operation(s) for groups.profilephoto.
  name: Microsoft 365 Groups.profile Photo API
  slug: microsoft-365-groups-profilephoto-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groups.resourceSpecificPermissionGrant API from Microsoft 365 — 3 operation(s) for groups.resourcespecificpermissiongrant.
  name: Microsoft 365 Groups.resource Specific Permission Grant API
  slug: microsoft-365-groups-resourcespecificpermissiongrant-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groups.team API from Microsoft 365 — 205 operation(s) for groups.team.
  name: Microsoft 365 Groups.team API
  slug: microsoft-365-groups-team-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groupSettings.groupSetting API from Microsoft 365 — 3 operation(s) for groupsettings.groupsetting.
  name: Microsoft 365 Group Settings.group Setting API
  slug: microsoft-365-groupsettings-groupsetting-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groupSettingTemplates.groupSettingTemplate.Actions API from Microsoft 365 — 8 operation(s) for groupsettingtemplates.groupsettingtemplate.actions.
  name: Microsoft 365 Group Setting Templates.group Setting Template.Actions API
  slug: microsoft-365-groupsettingtemplates-groupsettingtemplate-actions-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groupSettingTemplates.groupSettingTemplate API from Microsoft 365 — 3 operation(s) for groupsettingtemplates.groupsettingtemplate.
  name: Microsoft 365 Group Setting Templates.group Setting Template API
  slug: microsoft-365-groupsettingtemplates-groupsettingtemplate-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The groupSettingTemplates.groupSettingTemplate.Functions API from Microsoft 365 — 1 operation(s) for groupsettingtemplates.groupsettingtemplate.functions.
  name: Microsoft 365 Group Setting Templates.group Setting Template.Functions API
  slug: microsoft-365-groupsettingtemplates-groupsettingtemplate-functions-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The places.buildingMap API from Microsoft 365 — 16 operation(s) for places.buildingmap.
  name: Microsoft 365 Places.building Map API
  slug: microsoft-365-places-buildingmap-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The places.checkInClaim API from Microsoft 365 — 24 operation(s) for places.checkinclaim.
  name: Microsoft 365 Places.check In Claim API
  slug: microsoft-365-places-checkinclaim-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The places.place API from Microsoft 365 — 24 operation(s) for places.place.
  name: Microsoft 365 Places.place API
  slug: microsoft-365-places-place-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The places.place.Functions API from Microsoft 365 — 1 operation(s) for places.place.functions.
  name: Microsoft 365 Places.place.Functions API
  slug: microsoft-365-places-place-functions-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The places.room API from Microsoft 365 — 6 operation(s) for places.room.
  name: Microsoft 365 Places.room API
  slug: microsoft-365-places-room-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The places.workspace API from Microsoft 365 — 6 operation(s) for places.workspace.
  name: Microsoft 365 Places.workspace API
  slug: microsoft-365-places-workspace-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The shares.driveItem API from Microsoft 365 — 8 operation(s) for shares.driveitem.
  name: Microsoft 365 Shares.drive Item API
  slug: microsoft-365-shares-driveitem-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The shares.list API from Microsoft 365 — 83 operation(s) for shares.list.
  name: Microsoft 365 Shares.list API
  slug: microsoft-365-shares-list-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The shares.listItem API from Microsoft 365 — 30 operation(s) for shares.listitem.
  name: Microsoft 365 Shares.list Item API
  slug: microsoft-365-shares-listitem-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The shares.permission API from Microsoft 365 — 2 operation(s) for shares.permission.
  name: Microsoft 365 Shares.permission API
  slug: microsoft-365-shares-permission-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The shares.sharedDriveItem API from Microsoft 365 — 3 operation(s) for shares.shareddriveitem.
  name: Microsoft 365 Shares.shared Drive Item API
  slug: microsoft-365-shares-shareddriveitem-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The shares.site API from Microsoft 365 — 1 operation(s) for shares.site.
  name: Microsoft 365 Shares.site API
  slug: microsoft-365-shares-site-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The shares.user API from Microsoft 365 — 8 operation(s) for shares.user.
  name: Microsoft 365 Shares.user API
  slug: microsoft-365-shares-user-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The teams.channel API from Microsoft 365 — 130 operation(s) for teams.channel.
  name: Microsoft 365 Teams.channel API
  slug: microsoft-365-teams-channel-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The teams.conversationMember API from Microsoft 365 — 5 operation(s) for teams.conversationmember.
  name: Microsoft 365 Teams.conversation Member API
  slug: microsoft-365-teams-conversationmember-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The teams.group API from Microsoft 365 — 3 operation(s) for teams.group.
  name: Microsoft 365 Teams.group API
  slug: microsoft-365-teams-group-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The teams.profilePhoto API from Microsoft 365 — 2 operation(s) for teams.profilephoto.
  name: Microsoft 365 Teams.profile Photo API
  slug: microsoft-365-teams-profilephoto-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The teams.resourceSpecificPermissionGrant API from Microsoft 365 — 3 operation(s) for teams.resourcespecificpermissiongrant.
  name: Microsoft 365 Teams.resource Specific Permission Grant API
  slug: microsoft-365-teams-resourcespecificpermissiongrant-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The teams.schedule API from Microsoft 365 — 40 operation(s) for teams.schedule.
  name: Microsoft 365 Teams.schedule API
  slug: microsoft-365-teams-schedule-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The teams.team.Actions API from Microsoft 365 — 5 operation(s) for teams.team.actions.
  name: Microsoft 365 Teams.team.Actions API
  slug: microsoft-365-teams-team-actions-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The teams.team API from Microsoft 365 — 3 operation(s) for teams.team.
  name: Microsoft 365 Teams.team API
  slug: microsoft-365-teams-team-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The teams.team.Functions API from Microsoft 365 — 1 operation(s) for teams.team.functions.
  name: Microsoft 365 Teams.team.Functions API
  slug: microsoft-365-teams-team-functions-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The teams.teamsAppInstallation API from Microsoft 365 — 6 operation(s) for teams.teamsappinstallation.
  name: Microsoft 365 Teams.teams App Installation API
  slug: microsoft-365-teams-teamsappinstallation-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The teams.teamsAsyncOperation API from Microsoft 365 — 3 operation(s) for teams.teamsasyncoperation.
  name: Microsoft 365 Teams.teams Async Operation API
  slug: microsoft-365-teams-teamsasyncoperation-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The teams.teamsTemplate API from Microsoft 365 — 1 operation(s) for teams.teamstemplate.
  name: Microsoft 365 Teams.teams Template API
  slug: microsoft-365-teams-teamstemplate-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The teams.teamworkTag API from Microsoft 365 — 6 operation(s) for teams.teamworktag.
  name: Microsoft 365 Teams.teamwork Tag API
  slug: microsoft-365-teams-teamworktag-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The teamwork.deletedChat API from Microsoft 365 — 4 operation(s) for teamwork.deletedchat.
  name: Microsoft 365 Teamwork.deleted Chat API
  slug: microsoft-365-teamwork-deletedchat-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The teamwork.deletedTeam API from Microsoft 365 — 68 operation(s) for teamwork.deletedteam.
  name: Microsoft 365 Teamwork.deleted Team API
  slug: microsoft-365-teamwork-deletedteam-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The teamwork.teamsAppSettings API from Microsoft 365 — 1 operation(s) for teamwork.teamsappsettings.
  name: Microsoft 365 Teamwork.teams App Settings API
  slug: microsoft-365-teamwork-teamsappsettings-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The teamwork.teamwork.Actions API from Microsoft 365 — 1 operation(s) for teamwork.teamwork.actions.
  name: Microsoft 365 Teamwork.teamwork.Actions API
  slug: microsoft-365-teamwork-teamwork-actions-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The teamwork.teamwork API from Microsoft 365 — 1 operation(s) for teamwork.teamwork.
  name: Microsoft 365 Teamwork.teamwork API
  slug: microsoft-365-teamwork-teamwork-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The teamwork.workforceIntegration API from Microsoft 365 — 3 operation(s) for teamwork.workforceintegration.
  name: Microsoft 365 Teamwork.workforce Integration API
  slug: microsoft-365-teamwork-workforceintegration-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.calendar API from Microsoft 365 — 64 operation(s) for users.calendar.
  name: Microsoft 365 Users.calendar API
  slug: microsoft-365-users-calendar-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.calendarGroup API from Microsoft 365 — 36 operation(s) for users.calendargroup.
  name: Microsoft 365 Users.calendar Group API
  slug: microsoft-365-users-calendargroup-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.chat API from Microsoft 365 — 82 operation(s) for users.chat.
  name: Microsoft 365 Users.chat API
  slug: microsoft-365-users-chat-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.directoryObject API from Microsoft 365 — 84 operation(s) for users.directoryobject.
  name: Microsoft 365 Users.directory Object API
  slug: microsoft-365-users-directoryobject-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.drive API from Microsoft 365 — 296 operation(s) for users.drive.
  name: Microsoft 365 Users.drive API
  slug: microsoft-365-users-drive-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.event API from Microsoft 365 — 24 operation(s) for users.event.
  name: Microsoft 365 Users.event API
  slug: microsoft-365-users-event-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.extension API from Microsoft 365 — 3 operation(s) for users.extension.
  name: Microsoft 365 Users.extension API
  slug: microsoft-365-users-extension-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.inferenceClassification API from Microsoft 365 — 4 operation(s) for users.inferenceclassification.
  name: Microsoft 365 Users.inference Classification API
  slug: microsoft-365-users-inferenceclassification-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.itemInsights API from Microsoft 365 — 14 operation(s) for users.iteminsights.
  name: Microsoft 365 Users.item Insights API
  slug: microsoft-365-users-iteminsights-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.licenseDetails API from Microsoft 365 — 4 operation(s) for users.licensedetails.
  name: Microsoft 365 Users.license Details API
  slug: microsoft-365-users-licensedetails-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.mailboxSettings API from Microsoft 365 — 1 operation(s) for users.mailboxsettings.
  name: Microsoft 365 Users.mailbox Settings API
  slug: microsoft-365-users-mailboxsettings-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.mailFolder API from Microsoft 365 — 64 operation(s) for users.mailfolder.
  name: Microsoft 365 Users.mail Folder API
  slug: microsoft-365-users-mailfolder-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.message API from Microsoft 365 — 22 operation(s) for users.message.
  name: Microsoft 365 Users.message API
  slug: microsoft-365-users-message-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.oAuth2PermissionGrant API from Microsoft 365 — 3 operation(s) for users.oauth2permissiongrant.
  name: Microsoft 365 Users.o Auth2 Permission Grant API
  slug: microsoft-365-users-oauth2permissiongrant-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.onPremisesSyncBehavior API from Microsoft 365 — 1 operation(s) for users.onpremisessyncbehavior.
  name: Microsoft 365 Users.on Premises Sync Behavior API
  slug: microsoft-365-users-onpremisessyncbehavior-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.outlookUser API from Microsoft 365 — 7 operation(s) for users.outlookuser.
  name: Microsoft 365 Users.outlook User API
  slug: microsoft-365-users-outlookuser-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.profilePhoto API from Microsoft 365 — 5 operation(s) for users.profilephoto.
  name: Microsoft 365 Users.profile Photo API
  slug: microsoft-365-users-profilephoto-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.team API from Microsoft 365 — 208 operation(s) for users.team.
  name: Microsoft 365 Users.team API
  slug: microsoft-365-users-team-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.todo API from Microsoft 365 — 30 operation(s) for users.todo.
  name: Microsoft 365 Users.todo API
  slug: microsoft-365-users-todo-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.user API from Microsoft 365 — 4 operation(s) for users.user.
  name: Microsoft 365 Users.user API
  slug: microsoft-365-users-user-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.userSettings API from Microsoft 365 — 24 operation(s) for users.usersettings.
  name: Microsoft 365 Users.user Settings API
  slug: microsoft-365-users-usersettings-api
- baseURL: https://graph.microsoft.com/v1.0/
  baseurl_source: declared
  description: The users.userTeamwork API from Microsoft 365 — 15 operation(s) for users.userteamwork.
  name: Microsoft 365 Users.user Teamwork API
  slug: microsoft-365-users-userteamwork-api
artifact_total: 151
collections:
- collection_type: open
  name: Microsoft 365 (Microsoft Graph API) Calendar API
  slug: open-microsoft-365-calendar-api
- collection_type: open
  name: Microsoft 365 (Microsoft Graph API) Calendar Files API
  slug: open-microsoft-365-files-api
- collection_type: open
  name: Microsoft 365 (Microsoft Graph API) Calendar Groups API
  slug: open-microsoft-365-groups-api
- collection_type: open
  name: Microsoft 365 (Microsoft Graph API) Calendar Mail API
  slug: open-microsoft-365-mail-api
- collection_type: open
  name: Microsoft 365 (Microsoft Graph API) Calendar Me API
  slug: open-microsoft-365-me-api
- collection_type: open
  name: Microsoft 365 (Microsoft Graph API) Calendar Teams API
  slug: open-microsoft-365-teams-api
- collection_type: open
  name: Microsoft 365 (Microsoft Graph API) Calendar Users API
  slug: open-microsoft-365-users-api
- collection_type: open
  name: Microsoft 365 (Microsoft Graph API)
  slug: open-microsoft-365
common:
- group: operate
  href: https://artifacts.apis.io/microsoft-365/rate-limits/microsoft-365-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-365-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/microsoft-365/rules/microsoft-365-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-365-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-365/json-ld/microsoft-365-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-365-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-365/vocabulary/microsoft-365-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-365-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-365/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/microsoft-365/data-model/microsoft-365-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-365-data-model.yml
- group: design
  href: https://artifacts.apis.io/microsoft-365/conventions/microsoft-365-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-365-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/graph/versioning-and-support
- group: design
  href: https://artifacts.apis.io/microsoft-365/lifecycle/microsoft-365-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-365-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-365/errors/microsoft-365-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-365-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-365/conformance/microsoft-365-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-365-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-365/llms/microsoft-365-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-365-llms.txt
- group: build
  href: https://artifacts.apis.io/microsoft-365/mcp/microsoft-365-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-365-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-365/well-known/microsoft-365-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-365-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-365/well-known/microsoft-365-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-365-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-365/hosts/microsoft-365-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-365-hosts.yml
- group: build
  href: https://artifacts.apis.io/microsoft-365/integrations/microsoft-365-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/microsoft-365-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-365/vendors/microsoft-365-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-365-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-365/packages/microsoft-365-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-365-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/category/azure/blog/analyticsonazure
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/adaptive-cards/sdk/rendering-cards/android/getting-started
- group: commercial
  href: https://artifacts.apis.io/microsoft-365/plans/microsoft-365-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-365-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/microsoft-365/capabilities/microsoft-365-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-365-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-365/agentic-access/microsoft-365-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-365-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-365/security/microsoft-365-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-365-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-365/security/microsoft-365-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-365-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-365/security/microsoft-365-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-365-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-365/authentication/microsoft-365-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-365-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-365/scopes/microsoft-365-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-365-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-365
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/microsoft-365
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/microsoft-365
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/graph
- group: start
  title: ''
  type: Signup
  url: https://www.microsoft.com/microsoft-365/business/compare-all-plans
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/microsoft-365/business/compare-all-plans
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoftgraph
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/auth-concepts
- group: operate
  title: ''
  type: StatusPage
  url: https://admin.microsoft.com/servicestatus
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/graph/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/graph/api/overview
- group: operate
  title: ''
  type: Roadmap
  url: https://www.microsoft.com/en-us/microsoft-365/roadmap
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
created: '2026-05-11'
description: Microsoft 365 is Microsoft's productivity and collaboration suite, including Word, Excel, PowerPoint, Outlook, Teams, OneDrive, SharePoint, and OneNote, along with identity, security, and device management services. Developers access Microsoft 365 data and intelligence programmatically through Microsoft Graph, a unified REST API that exposes users, mail, calendar, files, Teams messages, sites, devices, and more across the Microsoft cloud.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-365.png
json_schemas:
- name: microsoft.graph.application
  property_count: 53
  slug: microsoft-365-microsoft-graph-application
- name: attachmentItem
  property_count: 6
  slug: microsoft-365-microsoft-graph-attachment-item
- name: microsoft.graph.attachment
  property_count: 6
  slug: microsoft-365-microsoft-graph-attachment
- name: microsoft.graph.calendarPermission
  property_count: 6
  slug: microsoft-365-microsoft-graph-calendar-permission
- name: microsoft.graph.calendar
  property_count: 19
  slug: microsoft-365-microsoft-graph-calendar
- name: microsoft.graph.channel
  property_count: 21
  slug: microsoft-365-microsoft-graph-channel
- name: microsoft.graph.chatMessage
  property_count: 25
  slug: microsoft-365-microsoft-graph-chat-message
- name: microsoft.graph.chat
  property_count: 20
  slug: microsoft-365-microsoft-graph-chat
- name: microsoft.graph.columnDefinition
  property_count: 33
  slug: microsoft-365-microsoft-graph-column-definition
- name: microsoft.graph.contentType
  property_count: 20
  slug: microsoft-365-microsoft-graph-content-type
- name: microsoft.graph.device
  property_count: 37
  slug: microsoft-365-microsoft-graph-device
- name: microsoft.graph.driveItem
  property_count: 45
  slug: microsoft-365-microsoft-graph-drive-item
- name: microsoft.graph.event
  property_count: 49
  slug: microsoft-365-microsoft-graph-event
- name: microsoft.graph.group
  property_count: 81
  slug: microsoft-365-microsoft-graph-group
- name: microsoft.graph.mailFolder
  property_count: 12
  slug: microsoft-365-microsoft-graph-mail-folder
- name: microsoft.graph.messageRule
  property_count: 9
  slug: microsoft-365-microsoft-graph-message-rule
- name: microsoft.graph.message
  property_count: 35
  slug: microsoft-365-microsoft-graph-message
- name: microsoft.graph.orgContact
  property_count: 22
  slug: microsoft-365-microsoft-graph-org-contact
- name: microsoft.graph.place
  property_count: 11
  slug: microsoft-365-microsoft-graph-place
- name: microsoft.graph.room
  property_count: 22
  slug: microsoft-365-microsoft-graph-room
- name: microsoft.graph.schedule
  property_count: 25
  slug: microsoft-365-microsoft-graph-schedule
- name: microsoft.graph.servicePrincipal
  property_count: 56
  slug: microsoft-365-microsoft-graph-service-principal
- name: microsoft.graph.site
  property_count: 33
  slug: microsoft-365-microsoft-graph-site
- name: microsoft.graph.subscription
  property_count: 15
  slug: microsoft-365-microsoft-graph-subscription
- name: microsoft.graph.team
  property_count: 30
  slug: microsoft-365-microsoft-graph-team
- name: uploadSession
  property_count: 3
  slug: microsoft-365-microsoft-graph-upload-session
- name: microsoft.graph.user
  property_count: 138
  slug: microsoft-365-microsoft-graph-user
- name: User
  property_count: 7
  slug: microsoft-365-user
jsonld:
- class_count: 120
  name: Microsoft 365 Context
  property_count: 236
  slug: microsoft-365-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.svc.cloud.microsoft requiring OAuth; 3 tools listed.
  name: Microsoft MCP Server for Enterprise
  slug: microsoft-mcp-server-for-enterprise
modified: '2026-11-04'
name: Microsoft 365
nav: Providers
network: true
overview: 'Microsoft 365 publishes 103 API contracts indexed on the [APIs.io](https://apis.io/) network, including Calendar API, Files API, Groups API, and 100 more. Tagged areas include Productivity, Collaboration, Email, Calendar, and File.


  The Microsoft 365 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft 365''s developer surface includes engineering blog, getting-started guide, authentication, documentation, signup flow, pricing, changelog, and 40 more developer resources.'
plans:
- name: Microsoft 365 Plans Pricing
  plan_count: 0
  slug: microsoft-365-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Microsoft 365 Rate Limits
  slug: microsoft-365-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Microsoft 365 API Rules
  rule_count: 56
  severity_counts:
    error: 45
    hint: 0
    info: 3
    warn: 8
  slug: microsoft-365-rules
scopes:
- name: Microsoft 365 Scopes
  scope_count: 8
  slug: microsoft-365-scopes
  summary_line: 8 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 64.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 73.8
    catalog_earned_first_party: 8.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 23.3
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 62.2
    developer_ergonomics: 66.1
    discoverability: 78.3
    operational_transparency: 78.9
  previous_composite: 41.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 100
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/microsoft-365/microsoft-365-2026-06-20T185401.png
security:
- kind: authentication
  name: Microsoft 365 Authentication
  slug: microsoft-365-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Microsoft 365 Domain Security
  slug: microsoft-365-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft 365 Vulnerability Disclosure
  slug: microsoft-365-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft 365 Trust Center
  slug: microsoft-365-trust-center
  summary_line: GDPR
skill_count: 1
skills:
- name: read-mailbox
  slug: microsoft-365-read-mailbox
slug: microsoft-365
tags:
- Productivity
- Collaboration
- Email
- Calendar
- File
- Identity
- Microsoft
- Microsoft Graph
website: https://www.microsoft.com/microsoft-365
---
