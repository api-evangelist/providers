---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 350
  human_in_the_loop: 8
  name: Peertube Agentic Access
  operation_count: 580
  slug: peertube-agentic-access
  summary_line: 580 operations · 350 acting · 8 human-in-the-loop
api_count: 54
apis:
- description: Abuses deal with reports of local or remote videos/comments/accounts alike.
  name: PeerTube Abuses API
  slug: peertube-abuses-api
- description: The Account Blocklist API from PeerTube — 5 operation(s) for account blocklist.
  name: PeerTube Account Blocklist API
  slug: peertube-account-blocklist-api
- description: 'Accounts encompass remote accounts discovered across the federation, and correspond to the main Actor, along with video channels a user can create, which are also Actors. When a comment is posted, it '
  name: PeerTube Accounts API
  slug: peertube-accounts-api
- description: Automatic tags set on objects (like comments or videos) by specific rules (external link, watched words, etc.)
  name: PeerTube Automatic Tags API
  slug: peertube-automatic-tags-api
- description: Operations dealing with synchronizing PeerTube user's channel with channels of other platforms
  name: PeerTube Channels Sync API
  slug: peertube-channels-sync-api
- description: Configuration of the web client.
  name: PeerTube Client Config API
  slug: peertube-client-config-api
- description: Each server exposes public information regarding supported videos and options.
  name: PeerTube Config API
  slug: peertube-config-api
- description: Send a message to the instance administrators.
  name: PeerTube Contact API
  slug: peertube-contact-api
- description: Administrative debug endpoints.
  name: PeerTube Debug API
  slug: peertube-debug-api
- description: Get and update the custom homepage
  name: PeerTube Homepage API
  slug: peertube-homepage-api
- description: Managing servers which the instance interacts with is crucial to the concept of federation in PeerTube and external video indexation. The PeerTube server then deals with inter-server ActivityPub opera
  name: PeerTube Instance Follows API
  slug: peertube-instance-follows-api
- description: Redundancy is part of the inter-server solidarity that PeerTube fosters. Manage the list of instances you wish to help by seeding their videos according to the policy of video selection of your choice
  name: PeerTube Instance Redundancy API
  slug: peertube-instance-redundancy-api
- description: Jobs are long-running tasks enqueued and processed by the instance itself. No additional worker registration is currently available.
  name: PeerTube Job API
  slug: peertube-job-api
- description: The Live Videos API from PeerTube — 4 operation(s) for live videos.
  name: PeerTube Live Videos API
  slug: peertube-live-videos-api
- description: Operations dealing with client, server and audit logs.
  name: PeerTube Logs API
  slug: peertube-logs-api
- description: Operations related to your watch history.
  name: PeerTube My History API
  slug: peertube-my-history-api
- description: Notifications following new videos, follows or reports. They allow you to keep track of the interactions and overall important information that concerns you. You MAY set per-notification type delivery
  name: PeerTube My Notifications API
  slug: peertube-my-notifications-api
- description: Operations related to your subscriptions to video channels, their new videos, and how to keep up to date with their latest publications!
  name: PeerTube My Subscriptions API
  slug: peertube-my-subscriptions-api
- description: Operations related to your own User, when logged-in.
  name: PeerTube My User API
  slug: peertube-my-user-api
- description: The Ownership Change API from PeerTube — 12 operation(s) for ownership change.
  name: PeerTube Ownership Change API
  slug: peertube-ownership-change-api
- description: Operations dealing with video player settings for videos and channels.
  name: PeerTube Player Settings API
  slug: peertube-player-settings-api
- description: Managing plugins installed from a local path or from NPM, or search for new ones.
  name: PeerTube Plugins API
  slug: peertube-plugins-api
- description: As a visitor, you can use this API to open an account (if registrations are open on that PeerTube instance). As an admin, you should use the dedicated [User creation API](#operation/addUser) instead.
  name: PeerTube Register API
  slug: peertube-register-api
- description: Manage runner jobs and runner-side job execution.
  name: PeerTube Runner Jobs API
  slug: peertube-runner-jobs-api
- description: Manage runner registration tokens.
  name: PeerTube Runner Registration Token API
  slug: peertube-runner-registration-token-api
- description: Register, list and remove remote runners.
  name: PeerTube Runners API
  slug: peertube-runners-api
- description: The search helps to find _videos_ or _channels_ from within the instance and beyond. Videos from other instances federated by the instance (that is, instances followed by the instance) can be found vi
  name: PeerTube Search API
  slug: peertube-search-api
- description: The Server Blocklist API from PeerTube — 5 operation(s) for server blocklist.
  name: PeerTube Server Blocklist API
  slug: peertube-server-blocklist-api
- description: Sessions deal with access tokens over time. Only __one session token can currently be used at a time__.
  name: PeerTube Session API
  slug: peertube-session-api
- description: The Static Video Files API from PeerTube — 4 operation(s) for static video files.
  name: PeerTube Static Video Files API
  slug: peertube-static-video-files-api
- description: Statistics
  name: PeerTube Stats API
  slug: peertube-stats-api
- description: To create an archive of user data.
  name: PeerTube User Exports API
  slug: peertube-user-exports-api
- description: To import an archive of user data.
  name: PeerTube User Imports API
  slug: peertube-user-imports-api
- description: Using some features of PeerTube require authentication, for which User provide different levels of permission as well as associated user information. Each user has a corresponding local Account for fe
  name: PeerTube Users API
  slug: peertube-users-api
- description: Operations dealing with listing, uploading, fetching or modifying videos.
  name: PeerTube Video API
  slug: peertube-video-api
- description: Operations dealing with blocking videos (removing them from view and preventing interactions).
  name: PeerTube Video Blocks API
  slug: peertube-video-blocks-api
- description: Operations dealing with listing, adding and removing closed captions of a video.
  name: PeerTube Video Captions API
  slug: peertube-video-captions-api
- description: Operations dealing with the creation, modification and listing of videos within a channel.
  name: PeerTube Video Channels API
  slug: peertube-video-channels-api
- description: Operations dealing with managing chapters of a video.
  name: PeerTube Video Chapters API
  slug: peertube-video-chapters-api
- description: 'Operations dealing with comments to a video. Comments are organized in threads: adding a comment in response to the video starts a thread, adding a reply to a comment adds it to its root comment threa'
  name: PeerTube Video Comments API
  slug: peertube-video-comments-api
- description: Download video files
  name: PeerTube Video Download API
  slug: peertube-video-download-api
- description: The Video Embed Privacy API from PeerTube — 2 operation(s) for video embed privacy.
  name: PeerTube Video Embed Privacy API
  slug: peertube-video-embed-privacy-api
- description: Server syndication feeds of videos
  name: PeerTube Video Feeds API
  slug: peertube-video-feeds-api
- description: Operations on video files
  name: PeerTube Video Files API
  slug: peertube-video-files-api
- description: Operations dealing with listing, adding and removing video imports.
  name: PeerTube Video Imports API
  slug: peertube-video-imports-api
- description: PeerTube instances can mirror videos from one another, and help distribute some videos. For importing videos as your own, refer to [video imports](#operation/importVideo).
  name: PeerTube Video Mirroring API
  slug: peertube-video-mirroring-api
- description: Operations on video passwords.
  name: PeerTube Video Passwords API
  slug: peertube-video-passwords-api
- description: Operations dealing with playlists of videos. Playlists are bound to users and/or channels.
  name: PeerTube Video Playlists API
  slug: peertube-video-playlists-api
- description: Like/dislike a video.
  name: PeerTube Video Rates API
  slug: peertube-video-rates-api
- description: Video statistics
  name: PeerTube Video Stats API
  slug: peertube-video-stats-api
- description: Video transcoding related operations
  name: PeerTube Video Transcoding API
  slug: peertube-video-transcoding-api
- description: 'Operations dealing with adding video or audio. PeerTube supports two upload modes, and three import modes. ### Upload - [_legacy_](#operation/uploadLegacy), where the video file is sent in a single re'
  name: PeerTube Video Upload API
  slug: peertube-video-upload-api
- description: The Videos API from PeerTube — 4 operation(s) for videos.
  name: PeerTube Videos API
  slug: peertube-videos-api
- description: Manage list of watched words to detect patterns on objects (like comments of videos)
  name: PeerTube Watched Words API
  slug: peertube-watched-words-api
artifact_total: 524
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/peertube-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peertube-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/peertube-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/peertube-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://joinpeertube.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.joinpeertube.org/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Chocobozzz/PeerTube
- group: company
  title: ''
  type: Blog
  url: https://framablog.org/
- group: operate
  title: ''
  type: Forums
  url: https://framacolibri.org/c/peertube
- group: other
  title: ''
  type: MobileApp
  url: https://joinpeertube.org/apps
- group: other
  title: ''
  type: ActivityPub
  url: https://docs.joinpeertube.org/api/activitypub
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://joinpeertube.org/privacy
- group: commercial
  title: ''
  type: License
  url: https://github.com/Chocobozzz/PeerTube/blob/develop/LICENSE
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/Chocobozzz/PeerTube
description: PeerTube is a free, decentralized, and federated video hosting platform developed by Framasoft as an open-source alternative to centralized video services like YouTube. It enables anyone to self-host a video platform that federates with other instances via ActivityPub, forming a global network of over 1,600 platforms hosting more than one million videos. The REST API supports video uploading and management, channel and playlist operations, live streaming, search and discovery across federated nodes, content moderation, plugin management, and distributed transcoding via remote runner jobs.
examples:
- key_count: 9
  name: Acceptregistration
  slug: acceptRegistration
- key_count: 9
  name: Acceptvideochannelcollaborator
  slug: acceptVideoChannelCollaborator
- key_count: 9
  name: Addlive
  slug: addLive
- key_count: 9
  name: Addplaylist
  slug: addPlaylist
- key_count: 9
  name: Addplugin
  slug: addPlugin
- key_count: 9
  name: Adduser
  slug: addUser
- key_count: 9
  name: Addvideoblock
  slug: addVideoBlock
- key_count: 9
  name: Addvideocaption
  slug: addVideoCaption
- key_count: 9
  name: Addvideochannel
  slug: addVideoChannel
- key_count: 9
  name: Addvideochannelsync
  slug: addVideoChannelSync
- key_count: 9
  name: Addvideopassword
  slug: addVideoPassword
- key_count: 9
  name: Addvideoplaylistvideo
  slug: addVideoPlaylistVideo
- key_count: 9
  name: Addview
  slug: addView
- key_count: 9
  name: Blockaccount
  slug: blockAccount
- key_count: 9
  name: Blockserver
  slug: blockServer
- key_count: 9
  name: Confirmtwofactorrequest
  slug: confirmTwoFactorRequest
- key_count: 9
  name: Contactadministrator
  slug: contactAdministrator
- key_count: 9
  name: Createvideotranscoding
  slug: createVideoTranscoding
- key_count: 9
  name: Delcustomconfig
  slug: delCustomConfig
- key_count: 9
  name: Delmirroredvideo
  slug: delMirroredVideo
- key_count: 9
  name: Deluser
  slug: delUser
- key_count: 9
  name: Delvideo
  slug: delVideo
- key_count: 9
  name: Delvideoblock
  slug: delVideoBlock
- key_count: 9
  name: Delvideocaption
  slug: delVideoCaption
- key_count: 9
  name: Delvideochannel
  slug: delVideoChannel
- key_count: 9
  name: Delvideochannelsync
  slug: delVideoChannelSync
- key_count: 9
  name: Delvideohls
  slug: delVideoHLS
- key_count: 9
  name: Delvideoplaylistvideo
  slug: delVideoPlaylistVideo
- key_count: 9
  name: Delvideowebvideos
  slug: delVideoWebVideos
- key_count: 9
  name: Deleteme
  slug: deleteMe
- key_count: 9
  name: Deleteregistration
  slug: deleteRegistration
- key_count: 9
  name: Deleteuserexport
  slug: deleteUserExport
- key_count: 9
  name: Deletevideosourcefile
  slug: deleteVideoSourceFile
- key_count: 9
  name: Delete_Api_V1_Abuses_Abuseid
  slug: delete_api_v1_abuses_abuseId
- key_count: 9
  name: Delete_Api_V1_Abuses_Abuseid_Messages_Abusemessageid
  slug: delete_api_v1_abuses_abuseId_messages_abuseMessageId
- key_count: 9
  name: Delete_Api_V1_Config_Instance Avatar
  slug: delete_api_v1_config_instance-avatar
- key_count: 9
  name: Delete_Api_V1_Config_Instance Banner
  slug: delete_api_v1_config_instance-banner
- key_count: 9
  name: Delete_Api_V1_Config_Instance Logo_Logotype
  slug: delete_api_v1_config_instance-logo_logoType
- key_count: 9
  name: Delete_Api_V1_Runners_Jobs_Jobuuid
  slug: delete_api_v1_runners_jobs_jobUUID
- key_count: 9
  name: Delete_Api_V1_Runners_Registration Tokens_Registrationtokenid
  slug: delete_api_v1_runners_registration-tokens_registrationTokenId
- key_count: 9
  name: Delete_Api_V1_Runners_Runnerid
  slug: delete_api_v1_runners_runnerId
- key_count: 9
  name: Delete_Api_V1_Server_Blocklist_Accounts_Accountname
  slug: delete_api_v1_server_blocklist_accounts_accountName
- key_count: 9
  name: Delete_Api_V1_Server_Blocklist_Servers_Host
  slug: delete_api_v1_server_blocklist_servers_host
- key_count: 9
  name: Delete_Api_V1_Server_Followers_Handle
  slug: delete_api_v1_server_followers_handle
- key_count: 9
  name: Delete_Api_V1_Server_Following_Hostorhandle
  slug: delete_api_v1_server_following_hostOrHandle
- key_count: 9
  name: Delete_Api_V1_Users_Me_Avatar
  slug: delete_api_v1_users_me_avatar
- key_count: 9
  name: Delete_Api_V1_Users_Me_History_Videos_Videoidoruuid
  slug: delete_api_v1_users_me_history_videos_videoIdOrUUID
- key_count: 9
  name: Delete_Api_V1_Users_Me_Subscriptions_Subscriptionhandle
  slug: delete_api_v1_users_me_subscriptions_subscriptionHandle
- key_count: 9
  name: Delete_Api_V1_Video Channels_Channelhandle_Avatar
  slug: delete_api_v1_video-channels_channelHandle_avatar
- key_count: 9
  name: Delete_Api_V1_Video Channels_Channelhandle_Banner
  slug: delete_api_v1_video-channels_channelHandle_banner
- key_count: 9
  name: Delete_Api_V1_Video Channels_Ownership_Id
  slug: delete_api_v1_video-channels_ownership_id
- key_count: 9
  name: Delete_Api_V1_Video Playlists_Playlistid
  slug: delete_api_v1_video-playlists_playlistId
- key_count: 9
  name: Delete_Api_V1_Videos_Id_Comments_Commentid
  slug: delete_api_v1_videos_id_comments_commentId
- key_count: 9
  name: Delete_Api_V1_Videos_Imports_Id
  slug: delete_api_v1_videos_imports_id
- key_count: 9
  name: Delete_Api_V1_Videos_Ownership_Id
  slug: delete_api_v1_videos_ownership_id
- key_count: 9
  name: Delete_Api_V1_Watched Words_Accounts_Accountname_Lists_Listid
  slug: delete_api_v1_watched-words_accounts_accountName_lists_listId
- key_count: 9
  name: Delete_Api_V1_Watched Words_Server_Lists_Listid
  slug: delete_api_v1_watched-words_server_lists_listId
- key_count: 9
  name: Disabletwofactor
  slug: disableTwoFactor
- key_count: 9
  name: Generatevideocaption
  slug: generateVideoCaption
- key_count: 9
  name: Getabout
  slug: getAbout
- key_count: 9
  name: Getabuses
  slug: getAbuses
- key_count: 9
  name: Getaccount
  slug: getAccount
- key_count: 9
  name: Getaccountfollowers
  slug: getAccountFollowers
- key_count: 9
  name: Getaccountvideos
  slug: getAccountVideos
- key_count: 9
  name: Getaccounts
  slug: getAccounts
- key_count: 9
  name: Getavailableplugins
  slug: getAvailablePlugins
- key_count: 9
  name: Getcategories
  slug: getCategories
- key_count: 9
  name: Getchannelplayersettings
  slug: getChannelPlayerSettings
- key_count: 9
  name: Getconfig
  slug: getConfig
- key_count: 9
  name: Getcustomconfig
  slug: getCustomConfig
- key_count: 9
  name: Getdebug
  slug: getDebug
- key_count: 9
  name: Getinstanceauditlogs
  slug: getInstanceAuditLogs
- key_count: 9
  name: Getinstancelogs
  slug: getInstanceLogs
- key_count: 9
  name: Getinstancestats
  slug: getInstanceStats
- key_count: 9
  name: Getjobs
  slug: getJobs
- key_count: 9
  name: Getlanguages
  slug: getLanguages
- key_count: 9
  name: Getlatestuserimport
  slug: getLatestUserImport
- key_count: 9
  name: Getlicences
  slug: getLicences
- key_count: 9
  name: Getliveid
  slug: getLiveId
- key_count: 9
  name: Getmirroredvideos
  slug: getMirroredVideos
- key_count: 9
  name: Getmyabuses
  slug: getMyAbuses
- key_count: 9
  name: Getmyblockedaccounts
  slug: getMyBlockedAccounts
- key_count: 9
  name: Getmyblockedservers
  slug: getMyBlockedServers
- key_count: 9
  name: Getoauthclient
  slug: getOAuthClient
- key_count: 9
  name: Getoauthtoken
  slug: getOAuthToken
- key_count: 9
  name: Getplaylistprivacypolicies
  slug: getPlaylistPrivacyPolicies
- key_count: 9
  name: Getplaylists
  slug: getPlaylists
- key_count: 9
  name: Getplugin
  slug: getPlugin
- key_count: 9
  name: Getplugins
  slug: getPlugins
- key_count: 9
  name: Getsyndicatedcomments
  slug: getSyndicatedComments
- key_count: 9
  name: Getsyndicatedsubscriptionvideos
  slug: getSyndicatedSubscriptionVideos
- key_count: 9
  name: Getsyndicatedvideos
  slug: getSyndicatedVideos
- key_count: 9
  name: Getuser
  slug: getUser
- key_count: 9
  name: Getuserinfo
  slug: getUserInfo
- key_count: 9
  name: Getusers
  slug: getUsers
- key_count: 9
  name: Getvideo
  slug: getVideo
- key_count: 9
  name: Getvideoblocks
  slug: getVideoBlocks
- key_count: 9
  name: Getvideocaptions
  slug: getVideoCaptions
- key_count: 9
  name: Getvideochannel
  slug: getVideoChannel
- key_count: 9
  name: Getvideochannelfollowers
  slug: getVideoChannelFollowers
- key_count: 9
  name: Getvideochannelvideos
  slug: getVideoChannelVideos
- key_count: 9
  name: Getvideochannels
  slug: getVideoChannels
- key_count: 9
  name: Getvideochapters
  slug: getVideoChapters
- key_count: 9
  name: Getvideoembedprivacy
  slug: getVideoEmbedPrivacy
- key_count: 9
  name: Getvideoplayersettings
  slug: getVideoPlayerSettings
- key_count: 9
  name: Getvideoplaylistvideos
  slug: getVideoPlaylistVideos
- key_count: 9
  name: Getvideoprivacypolicies
  slug: getVideoPrivacyPolicies
- key_count: 9
  name: Getvideosource
  slug: getVideoSource
- key_count: 9
  name: Getvideos
  slug: getVideos
- key_count: 9
  name: Getvideospodcastfeed
  slug: getVideosPodcastFeed
- key_count: 9
  name: Get_Api_V1_Abuses_Abuseid_Messages
  slug: get_api_v1_abuses_abuseId_messages
- key_count: 9
  name: Get_Api_V1_Accounts_Name_Ratings
  slug: get_api_v1_accounts_name_ratings
- key_count: 9
  name: Get_Api_V1_Accounts_Name_Video Channel Syncs
  slug: get_api_v1_accounts_name_video-channel-syncs
- key_count: 9
  name: Get_Api_V1_Accounts_Name_Video Channels
  slug: get_api_v1_accounts_name_video-channels
- key_count: 9
  name: Get_Api_V1_Accounts_Name_Video Playlists
  slug: get_api_v1_accounts_name_video-playlists
- key_count: 9
  name: Get_Api_V1_Automatic Tags_Accounts_Accountname_Available
  slug: get_api_v1_automatic-tags_accounts_accountName_available
- key_count: 9
  name: Get_Api_V1_Automatic Tags_Policies_Accounts_Accountname_Comments
  slug: get_api_v1_automatic-tags_policies_accounts_accountName_comments
- key_count: 9
  name: Get_Api_V1_Automatic Tags_Server_Available
  slug: get_api_v1_automatic-tags_server_available
- key_count: 9
  name: Get_Api_V1_Blocklist_Status
  slug: get_api_v1_blocklist_status
- key_count: 9
  name: Get_Api_V1_Custom Pages_Homepage_Instance
  slug: get_api_v1_custom-pages_homepage_instance
- key_count: 9
  name: Get_Api_V1_Plugins_Npmname_Public Settings
  slug: get_api_v1_plugins_npmName_public-settings
- key_count: 9
  name: Get_Api_V1_Plugins_Npmname_Registered Settings
  slug: get_api_v1_plugins_npmName_registered-settings
- key_count: 9
  name: Get_Api_V1_Runners
  slug: get_api_v1_runners
- key_count: 9
  name: Get_Api_V1_Runners_Jobs
  slug: get_api_v1_runners_jobs
- key_count: 9
  name: Get_Api_V1_Runners_Registration Tokens
  slug: get_api_v1_runners_registration-tokens
- key_count: 9
  name: Get_Api_V1_Server_Blocklist_Accounts
  slug: get_api_v1_server_blocklist_accounts
- key_count: 9
  name: Get_Api_V1_Server_Blocklist_Servers
  slug: get_api_v1_server_blocklist_servers
- key_count: 9
  name: Get_Api_V1_Server_Followers
  slug: get_api_v1_server_followers
- key_count: 9
  name: Get_Api_V1_Server_Following
  slug: get_api_v1_server_following
- key_count: 9
  name: Get_Api_V1_Users_Id_Token Sessions
  slug: get_api_v1_users_id_token-sessions
- key_count: 9
  name: Get_Api_V1_Users_Id_Token Sessions_Tokensessionid_Revoke
  slug: get_api_v1_users_id_token-sessions_tokenSessionId_revoke
- key_count: 9
  name: Get_Api_V1_Users_Me_History_Videos
  slug: get_api_v1_users_me_history_videos
- key_count: 9
  name: Get_Api_V1_Users_Me_Notifications
  slug: get_api_v1_users_me_notifications
- key_count: 9
  name: Get_Api_V1_Users_Me_Subscriptions
  slug: get_api_v1_users_me_subscriptions
- key_count: 9
  name: Get_Api_V1_Users_Me_Subscriptions_Exist
  slug: get_api_v1_users_me_subscriptions_exist
- key_count: 9
  name: Get_Api_V1_Users_Me_Subscriptions_Subscriptionhandle
  slug: get_api_v1_users_me_subscriptions_subscriptionHandle
- key_count: 9
  name: Get_Api_V1_Users_Me_Subscriptions_Videos
  slug: get_api_v1_users_me_subscriptions_videos
- key_count: 9
  name: Get_Api_V1_Users_Me_Video Playlists_Videos Exist
  slug: get_api_v1_users_me_video-playlists_videos-exist
- key_count: 9
  name: Get_Api_V1_Users_Me_Video Quota Used
  slug: get_api_v1_users_me_video-quota-used
- key_count: 9
  name: Get_Api_V1_Users_Me_Videos
  slug: get_api_v1_users_me_videos
- key_count: 9
  name: Get_Api_V1_Users_Me_Videos_Comments
  slug: get_api_v1_users_me_videos_comments
- key_count: 9
  name: Get_Api_V1_Users_Me_Videos_Imports
  slug: get_api_v1_users_me_videos_imports
- key_count: 9
  name: Get_Api_V1_Users_Me_Videos_Videoidoruuid_Rating
  slug: get_api_v1_users_me_videos_videoIdOrUUID_rating
- key_count: 9
  name: Get_Api_V1_Video Channels_Channelhandle_Ownership
  slug: get_api_v1_video-channels_channelHandle_ownership
- key_count: 9
  name: Get_Api_V1_Video Channels_Channelhandle_Video Playlists
  slug: get_api_v1_video-channels_channelHandle_video-playlists
- key_count: 9
  name: Get_Api_V1_Video Channels_Ownership
  slug: get_api_v1_video-channels_ownership
- key_count: 9
  name: Get_Api_V1_Video Playlists_Playlistid
  slug: get_api_v1_video-playlists_playlistId
- key_count: 9
  name: Get_Api_V1_Videos_Comments
  slug: get_api_v1_videos_comments
- key_count: 9
  name: Get_Api_V1_Videos_Id_Comment Threads
  slug: get_api_v1_videos_id_comment-threads
- key_count: 9
  name: Get_Api_V1_Videos_Id_Comment Threads_Threadid
  slug: get_api_v1_videos_id_comment-threads_threadId
- key_count: 9
  name: Get_Api_V1_Videos_Id_Live Session
  slug: get_api_v1_videos_id_live-session
- key_count: 9
  name: Get_Api_V1_Videos_Id_Stats_Overall
  slug: get_api_v1_videos_id_stats_overall
- key_count: 9
  name: Get_Api_V1_Videos_Id_Stats_Retention
  slug: get_api_v1_videos_id_stats_retention
- key_count: 9
  name: Get_Api_V1_Videos_Id_Stats_Timeseries_Metric
  slug: get_api_v1_videos_id_stats_timeseries_metric
- key_count: 9
  name: Get_Api_V1_Videos_Id_Stats_User Agent
  slug: get_api_v1_videos_id_stats_user-agent
- key_count: 9
  name: Get_Api_V1_Videos_Live_Id_Sessions
  slug: get_api_v1_videos_live_id_sessions
- key_count: 9
  name: Get_Api_V1_Videos_Ownership
  slug: get_api_v1_videos_ownership
- key_count: 9
  name: Get_Api_V1_Videos_Videoidoruuid_Ownership
  slug: get_api_v1_videos_videoIdOrUUID_ownership
- key_count: 9
  name: Get_Api_V1_Watched Words_Accounts_Accountname_Lists
  slug: get_api_v1_watched-words_accounts_accountName_lists
- key_count: 9
  name: Get_Api_V1_Watched Words_Server_Lists
  slug: get_api_v1_watched-words_server_lists
- key_count: 9
  name: Get_Download_Videos_Generate_Videoidoruuid
  slug: get_download_videos_generate_videoIdOrUUID
- key_count: 9
  name: Get_Static_Streaming Playlists_Hls_Filename
  slug: get_static_streaming-playlists_hls_filename
- key_count: 9
  name: Get_Static_Streaming Playlists_Hls_Private_Filename
  slug: get_static_streaming-playlists_hls_private_filename
- key_count: 9
  name: Get_Static_Web Videos_Filename
  slug: get_static_web-videos_filename
- key_count: 9
  name: Get_Static_Web Videos_Private_Filename
  slug: get_static_web-videos_private_filename
- key_count: 9
  name: Importvideo
  slug: importVideo
- key_count: 9
  name: Invitevideochannelcollaborator
  slug: inviteVideoChannelCollaborator
- key_count: 9
  name: Isvideoembedondomainallowed
  slug: isVideoEmbedOnDomainAllowed
- key_count: 9
  name: Listregistrations
  slug: listRegistrations
- key_count: 9
  name: Listuserexports
  slug: listUserExports
- key_count: 9
  name: Listvideochannelactivities
  slug: listVideoChannelActivities
- key_count: 9
  name: Listvideochannelcollaborators
  slug: listVideoChannelCollaborators
- key_count: 9
  name: Listvideopasswords
  slug: listVideoPasswords
- key_count: 9
  name: Listvideostoryboards
  slug: listVideoStoryboards
- key_count: 9
  name: Post_Api_V1_Abuses
  slug: post_api_v1_abuses
- key_count: 9
  name: Post_Api_V1_Abuses_Abuseid_Messages
  slug: post_api_v1_abuses_abuseId_messages
- key_count: 9
  name: Post_Api_V1_Config_Instance Avatar_Pick
  slug: post_api_v1_config_instance-avatar_pick
- key_count: 9
  name: Post_Api_V1_Config_Instance Banner_Pick
  slug: post_api_v1_config_instance-banner_pick
- key_count: 9
  name: Post_Api_V1_Config_Instance Logo_Logotype_Pick
  slug: post_api_v1_config_instance-logo_logoType_pick
- key_count: 9
  name: Post_Api_V1_Jobs_Pause
  slug: post_api_v1_jobs_pause
- key_count: 9
  name: Post_Api_V1_Jobs_Resume
  slug: post_api_v1_jobs_resume
- key_count: 9
  name: Post_Api_V1_Metrics_Playback
  slug: post_api_v1_metrics_playback
- key_count: 9
  name: Post_Api_V1_Runners_Jobs_Jobuuid_Abort
  slug: post_api_v1_runners_jobs_jobUUID_abort
- key_count: 9
  name: Post_Api_V1_Runners_Jobs_Jobuuid_Accept
  slug: post_api_v1_runners_jobs_jobUUID_accept
- key_count: 9
  name: Post_Api_V1_Runners_Jobs_Jobuuid_Cancel
  slug: post_api_v1_runners_jobs_jobUUID_cancel
- key_count: 9
  name: Post_Api_V1_Runners_Jobs_Jobuuid_Error
  slug: post_api_v1_runners_jobs_jobUUID_error
- key_count: 9
  name: Post_Api_V1_Runners_Jobs_Jobuuid_Files_Videos_Videoidoruuid_Max Quality
  slug: post_api_v1_runners_jobs_jobUUID_files_videos_videoIdOrUUID_max-quality
- key_count: 9
  name: Post_Api_V1_Runners_Jobs_Jobuuid_Files_Videos_Videoidoruuid_Max Quality_Audio
  slug: post_api_v1_runners_jobs_jobUUID_files_videos_videoIdOrUUID_max-quality_audio
- key_count: 9
  name: Post_Api_V1_Runners_Jobs_Jobuuid_Files_Videos_Videoidoruuid_Previews_Max Quality
  slug: post_api_v1_runners_jobs_jobUUID_files_videos_videoIdOrUUID_previews_max-quality
- key_count: 9
  name: Post_Api_V1_Runners_Jobs_Jobuuid_Files_Videos_Videoidoruuid_Studio_Task Files_Fi
  slug: post_api_v1_runners_jobs_jobUUID_files_videos_videoIdOrUUID_studio_task-files_fi
- key_count: 9
  name: Post_Api_V1_Runners_Jobs_Jobuuid_Files_Videos_Videoidoruuid_Thumbnails_Max Quali
  slug: post_api_v1_runners_jobs_jobUUID_files_videos_videoIdOrUUID_thumbnails_max-quali
- key_count: 9
  name: Post_Api_V1_Runners_Jobs_Jobuuid_Success
  slug: post_api_v1_runners_jobs_jobUUID_success
- key_count: 9
  name: Post_Api_V1_Runners_Jobs_Jobuuid_Update
  slug: post_api_v1_runners_jobs_jobUUID_update
- key_count: 9
  name: Post_Api_V1_Runners_Jobs_Request
  slug: post_api_v1_runners_jobs_request
- key_count: 9
  name: Post_Api_V1_Runners_Register
  slug: post_api_v1_runners_register
- key_count: 9
  name: Post_Api_V1_Runners_Registration Tokens_Generate
  slug: post_api_v1_runners_registration-tokens_generate
- key_count: 9
  name: Post_Api_V1_Runners_Unregister
  slug: post_api_v1_runners_unregister
- key_count: 9
  name: Post_Api_V1_Server_Blocklist_Accounts
  slug: post_api_v1_server_blocklist_accounts
- key_count: 9
  name: Post_Api_V1_Server_Blocklist_Servers
  slug: post_api_v1_server_blocklist_servers
- key_count: 9
  name: Post_Api_V1_Server_Followers_Handle_Accept
  slug: post_api_v1_server_followers_handle_accept
- key_count: 9
  name: Post_Api_V1_Server_Followers_Handle_Reject
  slug: post_api_v1_server_followers_handle_reject
- key_count: 9
  name: Post_Api_V1_Server_Following
  slug: post_api_v1_server_following
- key_count: 9
  name: Post_Api_V1_Users_Ask Reset Password
  slug: post_api_v1_users_ask-reset-password
- key_count: 9
  name: Post_Api_V1_Users_Id_Block
  slug: post_api_v1_users_id_block
- key_count: 9
  name: Post_Api_V1_Users_Id_Reset Password
  slug: post_api_v1_users_id_reset-password
- key_count: 9
  name: Post_Api_V1_Users_Id_Unblock
  slug: post_api_v1_users_id_unblock
- key_count: 9
  name: Post_Api_V1_Users_Me_Avatar_Pick
  slug: post_api_v1_users_me_avatar_pick
- key_count: 9
  name: Post_Api_V1_Users_Me_History_Videos_Remove
  slug: post_api_v1_users_me_history_videos_remove
- key_count: 9
  name: Post_Api_V1_Users_Me_New Feature Info_Read
  slug: post_api_v1_users_me_new-feature-info_read
- key_count: 9
  name: Post_Api_V1_Users_Me_Notifications_Read All
  slug: post_api_v1_users_me_notifications_read-all
- key_count: 9
  name: Post_Api_V1_Users_Me_Notifications_Read
  slug: post_api_v1_users_me_notifications_read
- key_count: 9
  name: Post_Api_V1_Users_Me_Subscriptions
  slug: post_api_v1_users_me_subscriptions
- key_count: 9
  name: Post_Api_V1_Video Channels_Channelhandle_Avatar_Pick
  slug: post_api_v1_video-channels_channelHandle_avatar_pick
- key_count: 9
  name: Post_Api_V1_Video Channels_Channelhandle_Banner_Pick
  slug: post_api_v1_video-channels_channelHandle_banner_pick
- key_count: 9
  name: Post_Api_V1_Video Channels_Channelhandle_Give Ownership
  slug: post_api_v1_video-channels_channelHandle_give-ownership
- key_count: 9
  name: Post_Api_V1_Video Channels_Channelhandle_Import Videos
  slug: post_api_v1_video-channels_channelHandle_import-videos
- key_count: 9
  name: Post_Api_V1_Video Channels_Ownership_Id_Accept
  slug: post_api_v1_video-channels_ownership_id_accept
- key_count: 9
  name: Post_Api_V1_Video Channels_Ownership_Id_Refuse
  slug: post_api_v1_video-channels_ownership_id_refuse
- key_count: 9
  name: Post_Api_V1_Videos_Id_Comment Threads
  slug: post_api_v1_videos_id_comment-threads
- key_count: 9
  name: Post_Api_V1_Videos_Id_Comments_Commentid
  slug: post_api_v1_videos_id_comments_commentId
- key_count: 9
  name: Post_Api_V1_Videos_Id_Comments_Commentid_Approve
  slug: post_api_v1_videos_id_comments_commentId_approve
- key_count: 9
  name: Post_Api_V1_Videos_Id_Studio_Edit
  slug: post_api_v1_videos_id_studio_edit
- key_count: 9
  name: Post_Api_V1_Videos_Imports_Id_Cancel
  slug: post_api_v1_videos_imports_id_cancel
- key_count: 9
  name: Post_Api_V1_Videos_Imports_Id_Retry
  slug: post_api_v1_videos_imports_id_retry
- key_count: 9
  name: Post_Api_V1_Videos_Ownership_Id_Accept
  slug: post_api_v1_videos_ownership_id_accept
- key_count: 9
  name: Post_Api_V1_Videos_Ownership_Id_Refuse
  slug: post_api_v1_videos_ownership_id_refuse
- key_count: 9
  name: Post_Api_V1_Videos_Videoidoruuid_Give Ownership
  slug: post_api_v1_videos_videoIdOrUUID_give-ownership
- key_count: 9
  name: Post_Api_V1_Watched Words_Accounts_Accountname_Lists
  slug: post_api_v1_watched-words_accounts_accountName_lists
- key_count: 9
  name: Post_Api_V1_Watched Words_Server_Lists
  slug: post_api_v1_watched-words_server_lists
- key_count: 9
  name: Putcustomconfig
  slug: putCustomConfig
- key_count: 9
  name: Putmirroredvideo
  slug: putMirroredVideo
- key_count: 9
  name: Putuser
  slug: putUser
- key_count: 9
  name: Putuserinfo
  slug: putUserInfo
- key_count: 9
  name: Putvideo
  slug: putVideo
- key_count: 9
  name: Putvideochannel
  slug: putVideoChannel
- key_count: 9
  name: Putvideoplaylistvideo
  slug: putVideoPlaylistVideo
- key_count: 9
  name: Put_Api_V1_Abuses_Abuseid
  slug: put_api_v1_abuses_abuseId
- key_count: 9
  name: Put_Api_V1_Automatic Tags_Policies_Accounts_Accountname_Comments
  slug: put_api_v1_automatic-tags_policies_accounts_accountName_comments
- key_count: 9
  name: Put_Api_V1_Custom Pages_Homepage_Instance
  slug: put_api_v1_custom-pages_homepage_instance
- key_count: 9
  name: Put_Api_V1_Plugins_Npmname_Settings
  slug: put_api_v1_plugins_npmName_settings
- key_count: 9
  name: Put_Api_V1_Server_Redundancy_Host
  slug: put_api_v1_server_redundancy_host
- key_count: 9
  name: Put_Api_V1_Users_Me_Notification Settings
  slug: put_api_v1_users_me_notification-settings
- key_count: 9
  name: Put_Api_V1_Video Playlists_Playlistid
  slug: put_api_v1_video-playlists_playlistId
- key_count: 9
  name: Put_Api_V1_Videos_Id_Rate
  slug: put_api_v1_videos_id_rate
- key_count: 9
  name: Put_Api_V1_Watched Words_Accounts_Accountname_Lists_Listid
  slug: put_api_v1_watched-words_accounts_accountName_lists_listId
- key_count: 9
  name: Put_Api_V1_Watched Words_Server_Lists_Listid
  slug: put_api_v1_watched-words_server_lists_listId
- key_count: 9
  name: Registeruser
  slug: registerUser
- key_count: 9
  name: Rejectregistration
  slug: rejectRegistration
- key_count: 9
  name: Rejectvideochannelcollaborator
  slug: rejectVideoChannelCollaborator
- key_count: 9
  name: Removevideochannelcollaborator
  slug: removeVideoChannelCollaborator
- key_count: 9
  name: Removevideopassword
  slug: removeVideoPassword
- key_count: 9
  name: Reordervideoplaylist
  slug: reorderVideoPlaylist
- key_count: 9
  name: Reordervideoplaylistsofchannel
  slug: reorderVideoPlaylistsOfChannel
- key_count: 9
  name: Replacevideochapters
  slug: replaceVideoChapters
- key_count: 9
  name: Replacevideosourceresumable
  slug: replaceVideoSourceResumable
- key_count: 9
  name: Replacevideosourceresumablecancel
  slug: replaceVideoSourceResumableCancel
- key_count: 9
  name: Replacevideosourceresumableinit
  slug: replaceVideoSourceResumableInit
- key_count: 9
  name: Requestregistration
  slug: requestRegistration
- key_count: 9
  name: Requesttwofactor
  slug: requestTwoFactor
- key_count: 9
  name: Requestuserexport
  slug: requestUserExport
- key_count: 9
  name: Requestvideotoken
  slug: requestVideoToken
- key_count: 9
  name: Resendemailtoverifyregistration
  slug: resendEmailToVerifyRegistration
- key_count: 9
  name: Resendemailtoverifyuser
  slug: resendEmailToVerifyUser
- key_count: 9
  name: Revokeoauthtoken
  slug: revokeOAuthToken
- key_count: 9
  name: Rundebugcommand
  slug: runDebugCommand
- key_count: 9
  name: Searchchannels
  slug: searchChannels
- key_count: 9
  name: Searchplaylists
  slug: searchPlaylists
- key_count: 9
  name: Searchvideos
  slug: searchVideos
- key_count: 9
  name: Sendclientlog
  slug: sendClientLog
- key_count: 9
  name: Triggervideochannelsync
  slug: triggerVideoChannelSync
- key_count: 9
  name: Unblockaccount
  slug: unblockAccount
- key_count: 9
  name: Unblockserver
  slug: unblockServer
- key_count: 9
  name: Uninstallplugin
  slug: uninstallPlugin
- key_count: 9
  name: Updatechannelplayersettings
  slug: updateChannelPlayerSettings
- key_count: 9
  name: Updateclientinterfacelanguage
  slug: updateClientInterfaceLanguage
- key_count: 9
  name: Updateclientlanguage
  slug: updateClientLanguage
- key_count: 9
  name: Updateliveid
  slug: updateLiveId
- key_count: 9
  name: Updateplugin
  slug: updatePlugin
- key_count: 9
  name: Updatevideoembedprivacy
  slug: updateVideoEmbedPrivacy
- key_count: 9
  name: Updatevideopasswordlist
  slug: updateVideoPasswordList
- key_count: 9
  name: Updatevideoplayersettings
  slug: updateVideoPlayerSettings
- key_count: 9
  name: Uploadlegacy
  slug: uploadLegacy
- key_count: 9
  name: Uploadresumable
  slug: uploadResumable
- key_count: 9
  name: Uploadresumablecancel
  slug: uploadResumableCancel
- key_count: 9
  name: Uploadresumableinit
  slug: uploadResumableInit
- key_count: 9
  name: Userimportresumable
  slug: userImportResumable
- key_count: 9
  name: Userimportresumablecancel
  slug: userImportResumableCancel
- key_count: 9
  name: Userimportresumableinit
  slug: userImportResumableInit
- key_count: 9
  name: Verifyregistrationemail
  slug: verifyRegistrationEmail
- key_count: 9
  name: Verifyuser
  slug: verifyUser
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/peertube.png
json_schemas:
- name: Abuse
  property_count: 8
  slug: Abuse
- name: AbuseMessage
  property_count: 5
  slug: AbuseMessage
- name: AbusePredefinedReasons
  property_count: 0
  slug: AbusePredefinedReasons
- name: AbuseStateConstant
  property_count: 2
  slug: AbuseStateConstant
- name: AbuseStateSet
  property_count: 0
  slug: AbuseStateSet
- name: Account
  property_count: 0
  slug: Account
- name: AccountBlock
  property_count: 3
  slug: AccountBlock
- name: AccountSummary
  property_count: 6
  slug: AccountSummary
- name: Actor
  property_count: 10
  slug: Actor
- name: ActorImage
  property_count: 6
  slug: ActorImage
- name: ActorInfo
  property_count: 5
  slug: ActorInfo
- name: AddUser
  property_count: 8
  slug: AddUser
- name: AddUserResponse
  property_count: 1
  slug: AddUserResponse
- name: AddVideoPasswords
  property_count: 0
  slug: AddVideoPasswords
- name: AutomaticTagAvailable
  property_count: 1
  slug: AutomaticTagAvailable
- name: BlockStatus
  property_count: 2
  slug: BlockStatus
- name: ChangeOwnership
  property_count: 7
  slug: ChangeOwnership
- name: ChangeOwnershipState
  property_count: 0
  slug: ChangeOwnershipState
- name: ChannelActivityListResponse
  property_count: 2
  slug: ChannelActivityListResponse
- name: CommentAutoTagPolicies
  property_count: 1
  slug: CommentAutoTagPolicies
- name: CommentThreadPostResponse
  property_count: 1
  slug: CommentThreadPostResponse
- name: CommentThreadResponse
  property_count: 3
  slug: CommentThreadResponse
- name: CustomHomepage
  property_count: 1
  slug: CustomHomepage
- name: FileRedundancyInformation
  property_count: 7
  slug: FileRedundancyInformation
- name: FileStorage
  property_count: 0
  slug: FileStorage
- name: Follow
  property_count: 7
  slug: Follow
- name: GetMeVideoRating
  property_count: 2
  slug: GetMeVideoRating
- name: ImportVideosInChannelCreate
  property_count: 2
  slug: ImportVideosInChannelCreate
- name: Job
  property_count: 8
  slug: Job
- name: LiveSchedule
  property_count: 1
  slug: LiveSchedule
- name: LiveVideoLatencyMode
  property_count: 0
  slug: LiveVideoLatencyMode
- name: LiveVideoReplaySettings
  property_count: 1
  slug: LiveVideoReplaySettings
- name: LiveVideoResponse
  property_count: 8
  slug: LiveVideoResponse
- name: LiveVideoSessionResponse
  property_count: 5
  slug: LiveVideoSessionResponse
- name: LiveVideoUpdate
  property_count: 5
  slug: LiveVideoUpdate
- name: MRSSGroupContent
  property_count: 7
  slug: MRSSGroupContent
- name: MRSSPeerLink
  property_count: 2
  slug: MRSSPeerLink
- name: NSFWFlag
  property_count: 0
  slug: NSFWFlag
- name: NSFWPolicy
  property_count: 0
  slug: NSFWPolicy
- name: NewFeatureInfoType
  property_count: 0
  slug: NewFeatureInfoType
- name: Notification
  property_count: 12
  slug: Notification
- name: NotificationListResponse
  property_count: 2
  slug: NotificationListResponse
- name: NotificationSettingValue
  property_count: 0
  slug: NotificationSettingValue
- name: NotificationType
  property_count: 0
  slug: NotificationType
- name: OAuthClient
  property_count: 2
  slug: OAuthClient
- name: OAuthToken-password
  property_count: 0
  slug: OAuthToken-password
- name: OAuthToken-refresh_token
  property_count: 0
  slug: OAuthToken-refresh_token
- name: PlaybackMetricCreate
  property_count: 12
  slug: PlaybackMetricCreate
- name: PlayerChannelSettings
  property_count: 1
  slug: PlayerChannelSettings
- name: PlayerChannelSettingsUpdate
  property_count: 1
  slug: PlayerChannelSettingsUpdate
- name: PlayerTheme
  property_count: 0
  slug: PlayerTheme
- name: PlayerThemeChannelSetting
  property_count: 0
  slug: PlayerThemeChannelSetting
- name: PlayerThemeVideoSetting
  property_count: 0
  slug: PlayerThemeVideoSetting
- name: PlayerVideoSettings
  property_count: 1
  slug: PlayerVideoSettings
- name: PlayerVideoSettingsUpdate
  property_count: 1
  slug: PlayerVideoSettingsUpdate
- name: PlaylistElement
  property_count: 4
  slug: PlaylistElement
- name: Plugin
  property_count: 12
  slug: Plugin
- name: PluginResponse
  property_count: 2
  slug: PluginResponse
- name: PredefinedAbuseReasons
  property_count: 0
  slug: PredefinedAbuseReasons
- name: RegisterUser
  property_count: 5
  slug: RegisterUser
- name: RequestTwoFactorResponse
  property_count: 1
  slug: RequestTwoFactorResponse
- name: Runner
  property_count: 7
  slug: Runner
- name: RunnerJob
  property_count: 14
  slug: RunnerJob
- name: RunnerJobAdmin
  property_count: 0
  slug: RunnerJobAdmin
- name: RunnerJobPayload
  property_count: 0
  slug: RunnerJobPayload
- name: RunnerJobState
  property_count: 0
  slug: RunnerJobState
- name: RunnerJobStateConstant
  property_count: 2
  slug: RunnerJobStateConstant
- name: RunnerJobType
  property_count: 0
  slug: RunnerJobType
- name: RunnerRegistrationToken
  property_count: 5
  slug: RunnerRegistrationToken
- name: SendClientLog
  property_count: 6
  slug: SendClientLog
- name: ServerBlock
  property_count: 3
  slug: ServerBlock
- name: ServerConfig
  property_count: 24
  slug: ServerConfig
- name: ServerConfigAbout
  property_count: 1
  slug: ServerConfigAbout
- name: ServerConfigCustom
  property_count: 14
  slug: ServerConfigCustom
- name: ServerError
  property_count: 4
  slug: ServerError
- name: ServerStats
  property_count: 32
  slug: ServerStats
- name: Storyboard
  property_count: 7
  slug: Storyboard
- name: Thumbnail
  property_count: 4
  slug: Thumbnail
- name: TokenSession
  property_count: 9
  slug: TokenSession
- name: UUIDv4
  property_count: 0
  slug: UUIDv4
- name: UpdateMe
  property_count: 20
  slug: UpdateMe
- name: UpdateUser
  property_count: 8
  slug: UpdateUser
- name: User
  property_count: 35
  slug: User
- name: UserAdminFlags
  property_count: 0
  slug: UserAdminFlags
- name: UserExportState
  property_count: 0
  slug: UserExportState
- name: UserImportResumable
  property_count: 1
  slug: UserImportResumable
- name: UserImportState
  property_count: 0
  slug: UserImportState
- name: UserNotificationSettings
  property_count: 18
  slug: UserNotificationSettings
- name: UserRegistration
  property_count: 13
  slug: UserRegistration
- name: UserRegistrationAcceptOrReject
  property_count: 2
  slug: UserRegistrationAcceptOrReject
- name: UserRegistrationRequest
  property_count: 0
  slug: UserRegistrationRequest
- name: UserRegistrationState
  property_count: 0
  slug: UserRegistrationState
- name: UserRole
  property_count: 0
  slug: UserRole
- name: UserViewingVideo
  property_count: 6
  slug: UserViewingVideo
- name: UserWithStats
  property_count: 0
  slug: UserWithStats
- name: Video
  property_count: 37
  slug: Video
- name: VideoBlacklist
  property_count: 12
  slug: VideoBlacklist
- name: VideoCaption
  property_count: 6
  slug: VideoCaption
- name: VideoCategorySet
  property_count: 0
  slug: VideoCategorySet
- name: VideoChannel
  property_count: 0
  slug: VideoChannel
- name: VideoChannelActivityAction
  property_count: 0
  slug: VideoChannelActivityAction
- name: VideoChannelActivityTarget
  property_count: 0
  slug: VideoChannelActivityTarget
- name: VideoChannelCollaborator
  property_count: 5
  slug: VideoChannelCollaborator
- name: VideoChannelCollaboratorState
  property_count: 0
  slug: VideoChannelCollaboratorState
- name: VideoChannelCreate
  property_count: 0
  slug: VideoChannelCreate
- name: VideoChannelEdit
  property_count: 3
  slug: VideoChannelEdit
- name: VideoChannelList
  property_count: 2
  slug: VideoChannelList
- name: VideoChannelSummary
  property_count: 6
  slug: VideoChannelSummary
- name: VideoChannelSync
  property_count: 6
  slug: VideoChannelSync
- name: VideoChannelSyncCreate
  property_count: 2
  slug: VideoChannelSyncCreate
- name: VideoChannelSyncList
  property_count: 2
  slug: VideoChannelSyncList
- name: VideoChannelUpdate
  property_count: 0
  slug: VideoChannelUpdate
- name: VideoChapters
  property_count: 1
  slug: VideoChapters
- name: VideoComment
  property_count: 14
  slug: VideoComment
- name: VideoCommentForOwnerOrAdmin
  property_count: 11
  slug: VideoCommentForOwnerOrAdmin
- name: VideoCommentThreadTree
  property_count: 2
  slug: VideoCommentThreadTree
- name: VideoCommentsForXML
  property_count: 0
  slug: VideoCommentsForXML
- name: VideoCommentsPolicyConstant
  property_count: 2
  slug: VideoCommentsPolicyConstant
- name: VideoCommentsPolicySet
  property_count: 0
  slug: VideoCommentsPolicySet
- name: VideoConstantNumber-Category
  property_count: 2
  slug: VideoConstantNumber-Category
- name: VideoConstantNumber-Licence
  property_count: 2
  slug: VideoConstantNumber-Licence
- name: VideoConstantString-Language
  property_count: 2
  slug: VideoConstantString-Language
- name: VideoCreateImport
  property_count: 0
  slug: VideoCreateImport
- name: VideoDetails
  property_count: 0
  slug: VideoDetails
- name: VideoEmbedPrivacy
  property_count: 0
  slug: VideoEmbedPrivacy
- name: VideoFile
  property_count: 16
  slug: VideoFile
- name: VideoImport
  property_count: 10
  slug: VideoImport
- name: VideoImportStateConstant
  property_count: 2
  slug: VideoImportStateConstant
- name: VideoImportsList
  property_count: 2
  slug: VideoImportsList
- name: VideoInfo
  property_count: 4
  slug: VideoInfo
- name: VideoLanguageSet
  property_count: 0
  slug: VideoLanguageSet
- name: VideoLicenceSet
  property_count: 0
  slug: VideoLicenceSet
- name: VideoListResponse
  property_count: 2
  slug: VideoListResponse
- name: VideoPassword
  property_count: 3
  slug: VideoPassword
- name: VideoPasswordList
  property_count: 2
  slug: VideoPasswordList
- name: VideoPlaylist
  property_count: 16
  slug: VideoPlaylist
- name: VideoPlaylistPrivacyConstant
  property_count: 2
  slug: VideoPlaylistPrivacyConstant
- name: VideoPlaylistPrivacySet
  property_count: 0
  slug: VideoPlaylistPrivacySet
- name: VideoPlaylistTypeConstant
  property_count: 2
  slug: VideoPlaylistTypeConstant
- name: VideoPlaylistTypeSet
  property_count: 0
  slug: VideoPlaylistTypeSet
- name: VideoPrivacyConstant
  property_count: 2
  slug: VideoPrivacyConstant
- name: VideoPrivacySet
  property_count: 0
  slug: VideoPrivacySet
- name: VideoRating
  property_count: 2
  slug: VideoRating
- name: VideoRedundancy
  property_count: 5
  slug: VideoRedundancy
- name: VideoReplaceSourceRequestResumable
  property_count: 1
  slug: VideoReplaceSourceRequestResumable
- name: VideoResolutionConstant
  property_count: 2
  slug: VideoResolutionConstant
- name: VideoResolutionSet
  property_count: 0
  slug: VideoResolutionSet
- name: VideoScheduledUpdate
  property_count: 2
  slug: VideoScheduledUpdate
- name: VideoSource
  property_count: 8
  slug: VideoSource
- name: VideoStateConstant
  property_count: 2
  slug: VideoStateConstant
- name: VideoStatsOverall
  property_count: 7
  slug: VideoStatsOverall
- name: VideoStatsRetention
  property_count: 1
  slug: VideoStatsRetention
- name: VideoStatsTimeserie
  property_count: 1
  slug: VideoStatsTimeserie
- name: VideoStatsUserAgent
  property_count: 3
  slug: VideoStatsUserAgent
- name: VideoStatsUserAgentDevice
  property_count: 0
  slug: VideoStatsUserAgentDevice
- name: VideoStreamingPlaylists-HLS
  property_count: 4
  slug: VideoStreamingPlaylists-HLS
- name: VideoStreamingPlaylists
  property_count: 0
  slug: VideoStreamingPlaylists
- name: VideoStudioCreateTask
  property_count: 0
  slug: VideoStudioCreateTask
- name: VideoSummary
  property_count: 9
  slug: VideoSummary
- name: VideoTokenResponse
  property_count: 1
  slug: VideoTokenResponse
- name: VideoUploadRequestCommon
  property_count: 21
  slug: VideoUploadRequestCommon
- name: VideoUploadRequestLegacy
  property_count: 0
  slug: VideoUploadRequestLegacy
- name: VideoUploadRequestResumable
  property_count: 0
  slug: VideoUploadRequestResumable
- name: VideoUploadResponse
  property_count: 1
  slug: VideoUploadResponse
- name: VideosForXML
  property_count: 0
  slug: VideosForXML
- name: WatchedWordsLists
  property_count: 5
  slug: WatchedWordsLists
- name: id
  property_count: 0
  slug: id
- name: password
  property_count: 0
  slug: password
- name: shortUUID
  property_count: 0
  slug: shortUUID
- name: username
  property_count: 0
  slug: username
- name: usernameChannel
  property_count: 0
  slug: usernameChannel
jsonld:
- class_count: 0
  name: Peertube Context
  property_count: 0
  slug: peertube
layout: provider
modified: '2026-06-13'
name: PeerTube
nav: Providers
network: true
overview: 'PeerTube publishes 54 APIs on the [APIs.io](https://apis.io/) network, including Abuses API, Account Blocklist API, Accounts API, and 51 more. Tagged areas include Video, Decentralized, Federation, Open Source, and ActivityPub.


  The PeerTube catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PeerTube''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 40
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: PeerTube API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: peertube-jsonschema-spectral-rules
scopes:
- name: Peertube Scopes
  scope_count: 3
  slug: peertube-scopes
  summary_line: 3 scopes · password
score:
  band: thin
  composite: 41.0
  delta: -4.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.8
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 54
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/peertube/refs/heads/main/screenshots/peertube-2026-06-20T191525.png
security:
- kind: authentication
  name: Peertube Authentication
  slug: peertube-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Peertube Domain Security
  slug: peertube-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: peertube
tags:
- Video
- Decentralized
- Federation
- Open Source
- ActivityPub
- Self-Hosted
- Streaming
website: https://joinpeertube.org/
---
