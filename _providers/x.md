---
access_model:
  confidence: high
  label: Pay-per-usage credits · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 61.8
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 86
  human_in_the_loop: 4
  name: X Agentic Access
  operation_count: 190
  slug: x-agentic-access
  summary_line: 190 operations · 86 acting · 4 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Endpoints relating to retrieving, managing Account Activity subscriptions — 5 operation(s) in the X-published contract.
  name: X Account Activity API
  phrasing_intents:
  - id: getAccountActivitySubscriptionCount
    intent: Count Account Activity subscriptions
    question: How many Account Activity subscriptions does my app currently have?
  - id: validateAccountActivitySubscription
    intent: Check a user's Account Activity subscription
    question: How can I confirm the authenticated user is subscribed to a given Account Activity webhook?
  - id: createAccountActivitySubscription
    intent: Subscribe a user to Account Activity events
    question: How do I start receiving Account Activity events for a user on my webhook?
  - id: getAccountActivitySubscriptions
    intent: List subscriptions on an Account Activity webhook
    question: Which users are subscribed to my Account Activity webhook?
  - id: deleteAccountActivitySubscription
    intent: Remove a user's Account Activity subscription
    question: How do I stop sending a user's Account Activity events to my webhook?
  phrasing_ops: 5
  slug: x-account-activity-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Endpoints for managing the authenticated user's X Developer Platform account — 2 operation(s) in the X-published contract.
  name: X Account API
  phrasing_intents:
  - id: getDeveloperAccount
    intent: Get my X Developer Platform account
    question: Do I already have an X Developer Platform account?
  - id: ensureAccount
    intent: Create a developer account if missing
    question: How do I provision a developer account for the signed-in user only when they don't have one?
  phrasing_ops: 2
  slug: x-account-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Endpoints relating to retrieving, managing activity subscriptions — 5 operation(s) in the X-published contract.
  name: X Activity API
  phrasing_intents:
  - id: deleteActivitySubscriptionsByIds
    intent: Delete several activity subscriptions at once
    question: Can I remove multiple X activity subscriptions in one call?
  - id: getActivitySubscriptions
    intent: List X activity subscriptions
    question: Which X activity event subscriptions are active for my app?
  - id: createActivitySubscription
    intent: Subscribe to an X activity event
    question: How do I subscribe to like or follow events for a user and send them to my webhook?
  - id: deleteActivitySubscription
    intent: Delete one activity subscription
    question: How do I cancel a single X activity subscription?
  - id: updateActivitySubscription
    intent: Change an activity subscription's webhook or tag
    question: How do I point an existing activity subscription at a different webhook?
  phrasing_ops: 5
  slug: x-activity-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Endpoints related to retrieving, creating & modifying Articles — 2 operation(s) in the X-published contract.
  name: X Articles API
  phrasing_intents:
  - id: articleCreateDraft
    intent: Create a draft Article
    question: Can I start a long-form Article on X as a draft first?
  - id: articlePublish
    intent: Publish a draft Article
    question: How do I make a drafted Article publicly visible?
  phrasing_ops: 2
  slug: x-articles-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: The Bots surface of the X API v2. — 6 operation(s) in the X-published contract.
  name: X Bots API
  phrasing_intents:
  - id: getBots
    intent: List bots in my project
    question: Which bot accounts exist in my app's project?
  - id: createBot
    intent: Create a bot account
    question: How do I create a bot account and get its bearer token?
  - id: deleteBot
    intent: Delete a bot account
    question: What's needed to permanently remove a bot from my project?
  - id: updateBot
    intent: Update a bot's handle, name or DM permission
    question: Can I rename an existing bot or change its handle?
  - id: revokeBotToken
    intent: Revoke a bot's bearer token
    question: How do I kill a leaked bot token without deleting the bot?
  - id: rotateBotToken
    intent: Rotate a bot's bearer token
    question: How do I issue a fresh bearer token for my bot?
  phrasing_ops: 6
  slug: x-bots-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Endpoints related to live broadcasts and their chat — 13 operation(s) in the X-published contract.
  name: X Broadcasts API
  phrasing_intents:
  - id: listBroadcasts
    intent: List my live-video broadcasts
    question: How can I see all the live-video broadcasts I've run on X?
  - id: listScheduledBroadcasts
    intent: List my scheduled broadcasts
    question: Which upcoming broadcasts do I have scheduled?
  - id: createScheduledBroadcast
    intent: Schedule a live broadcast
    question: How do I schedule a live-video broadcast ahead of time?
  - id: deleteScheduledBroadcast
    intent: Delete a scheduled broadcast
    question: Can I cancel a broadcast I scheduled earlier?
  - id: getScheduledBroadcast
    intent: Get one scheduled broadcast
    question: How do I look up the details of a single scheduled broadcast?
  - id: updateScheduledBroadcast
    intent: Reschedule a scheduled broadcast
    question: How do I move a scheduled broadcast to a new time?
  - id: goLiveScheduledBroadcast
    intent: Go live on a manually published broadcast
    question: How do I start a scheduled broadcast that was set to manual publish?
  - id: getBroadcast
    intent: Get one of my broadcasts
    question: How can I retrieve the details of a single live-video broadcast I own?
  phrasing_ops: 13
  slug: x-broadcasts-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Endpoints related to Chat encrypted messaging — 16 operation(s) in the X-published contract.
  name: X Chat API
  phrasing_intents:
  - id: getChatConversations
    intent: List my Chat inbox conversations
    question: Which encrypted Chat conversations are in my inbox?
  - id: createChatConversation
    intent: Create an encrypted Chat group
    question: How do I finish creating an encrypted Chat group after initializing it?
  - id: initializeChatGroup
    intent: Reserve an ID for a new Chat group
    question: What's the first step to create a new Chat group conversation?
  - id: getChatConversation
    intent: Get a Chat conversation's details
    question: How can I see whether a Chat conversation is muted and who its admins are?
  - id: getChatConversationEvents
    intent: Read messages in a Chat conversation
    question: Where can I get the message history of a Chat conversation?
  - id: addConversationKeys
    intent: Initialize or rotate a Chat conversation key
    question: What do I need to call before sending the first message in a new 1:1 encrypted chat?
  - id: addChatGroupMembers
    intent: Add members to a Chat group
    question: Can I invite more people into an existing encrypted group chat?
  - id: sendChatMessage
    intent: Send an encrypted Chat message
    question: How do I send an encrypted message into an XChat conversation?
  phrasing_ops: 16
  slug: x-chat-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Endpoints related to retrieving and managing Communities — 2 operation(s) in the X-published contract.
  name: X Communities API
  phrasing_intents:
  - id: searchCommunities
    intent: Search Communities by keyword
    question: Which X Communities exist about a given topic?
  - id: getCommunitiesById
    intent: Get a Community by ID
    question: How can I look up a single Community's details from its ID?
  phrasing_ops: 2
  slug: x-communities-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Endpoints related to retrieving, searching, and modifying Community Notes — 5 operation(s) in the X-published contract.
  name: X Community Notes API
  phrasing_intents:
  - id: createCommunityNotes
    intent: Write a Community Note on a post
    question: How can an AI note writer submit a Community Note on a post?
  - id: evaluateCommunityNotes
    intent: Evaluate a draft Community Note
    question: Can I get feedback on a Community Note's text before submitting it?
  - id: searchCommunityNotesWritten
    intent: List Community Notes I've written
    question: Which Community Notes have I already written?
  - id: searchEligiblePosts
    intent: Find posts eligible for Community Notes
    question: Which posts are currently eligible to receive a Community Note?
  - id: deleteCommunityNotes
    intent: Delete a Community Note
    question: Is there a way to delete a Community Note I wrote?
  phrasing_ops: 5
  slug: x-community-notes-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Endpoints related to keeping X data in your systems compliant — 6 operation(s) in the X-published contract.
  name: X Compliance API
  phrasing_intents:
  - id: getComplianceJobs
    intent: List compliance jobs by type
    question: Which batch compliance jobs have I created for posts or users?
  - id: createComplianceJobs
    intent: Create a batch compliance job
    question: How do I check a stored dataset of post or user IDs for deletions and suspensions?
  - id: deleteComplianceJobsById
    intent: Cancel an unfinished compliance job
    question: Can I cancel a compliance job that's still processing so I can start another of the same type?
  - id: getComplianceJobsById
    intent: Check a compliance job's status
    question: Has my compliance job finished processing yet?
  - id: downloadComplianceJobResults
    intent: Download a compliance job's results
    question: Where do I get the results file once a compliance job completes?
  - id: uploadComplianceJobSubmission
    intent: Upload IDs to a compliance job
    question: How do I upload my newline-delimited ID file to a compliance job?
  phrasing_ops: 6
  slug: x-compliance-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Endpoints related to streaming connections — 4 operation(s) in the X-published contract.
  name: X Connections API
  phrasing_intents:
  - id: deleteConnectionsByUuids
    intent: Terminate specific streaming connections
    question: How do I close particular streaming connections by their UUIDs?
  - id: getConnectionHistory
    intent: View streaming connection history
    question: Why did my streaming connection disconnect?
  - id: deleteAllConnections
    intent: Terminate all streaming connections
    question: Is there a way to kill every active streaming connection my app has?
  - id: deleteConnectionsByEndpoint
    intent: Terminate streams on one endpoint
    question: Can I close all connections to just one streaming endpoint?
  phrasing_ops: 4
  slug: x-connections-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Endpoints related to retrieving, managing Direct Messages — 9 operation(s) in the X-published contract.
  name: X Direct Messages API
  phrasing_intents:
  - id: createDirectMessagesConversation
    intent: Start a group DM conversation
    question: How do I start a new group Direct Message with several people?
  - id: dmConversationsMediaDownload
    intent: Download media from a legacy DM
    question: Can I download a photo or video attached to an older Direct Message?
  - id: getDirectMessagesEventsByParticipantId
    intent: Get my DM history with one person
    question: What have I and a specific user said to each other in DMs?
  - id: createDirectMessagesByParticipantId
    intent: Send a DM to a user
    question: How do I send a Direct Message to someone by their user ID?
  - id: createDirectMessagesByConversationId
    intent: Send a message into an existing DM conversation
    question: Can I post a message into a group DM conversation I'm already part of?
  - id: getDirectMessagesEventsByConversationId
    intent: Read the events in a DM conversation
    question: Which messages are in a particular group DM conversation?
  - id: getDirectMessagesEvents
    intent: List my recent DM events across conversations
    question: What are my most recent Direct Messages across all conversations?
  - id: deleteDirectMessagesEvents
    intent: Delete a DM I sent
    question: Can I delete a Direct Message I sent?
  phrasing_ops: 9
  slug: x-direct-messages-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Miscellaneous endpoints for general API functionality — 1 operation(s) in the X-published contract.
  name: X General API
  phrasing_intents:
  - id: getOpenApiSpec
    intent: Download the API's OpenAPI specification
    question: Where can I get the machine-readable OpenAPI spec for the X API?
  phrasing_ops: 1
  slug: x-general-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Endpoints related to retrieving, managing Lists — 9 operation(s) in the X-published contract.
  name: X Lists API
  phrasing_intents:
  - id: createLists
    intent: Create a List
    question: Can I create a new List on X via the API?
  - id: deleteLists
    intent: Delete a List I own
    question: What's the call to delete one of my Lists?
  - id: getListsById
    intent: Get a List's details
    question: What are the name, owner and description of a given List?
  - id: updateLists
    intent: Rename or edit a List I own
    question: Can I rename an existing List or change its description?
  - id: getListsFollowers
    intent: List a List's followers
    question: Who follows a particular List?
  - id: getListsMembers
    intent: List the members of a List
    question: Which accounts are members of a given List?
  - id: addListsMember
    intent: Add a user to a List
    question: Can I add an account to one of my Lists?
  - id: removeListsMemberByUserId
    intent: Remove a user from a List
    question: What removes someone from one of my Lists?
  phrasing_ops: 9
  slug: x-lists-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Endpoints related to retrieving and uploading Media — 11 operation(s) in the X-published contract.
  name: X Media API
  phrasing_intents:
  - id: getMediaByMediaKeys
    intent: Look up several media items by key
    question: Can I get details for a batch of media keys in one call?
  - id: getMediaAnalytics
    intent: Get analytics for media items
    question: How are my uploaded videos performing over a date range?
  - id: createMediaMetadata
    intent: Add metadata to uploaded media
    question: Can I attach extra metadata to an image after uploading it?
  - id: deleteMediaSubtitles
    intent: Remove subtitles from a video
    question: How do I delete a subtitle track in a particular language from a video?
  - id: createMediaSubtitles
    intent: Add subtitles to a video
    question: Can I attach subtitle files to a video I uploaded?
  - id: getMediaUploadStatus
    intent: Check a media upload's processing status
    question: Is my uploaded video still processing or ready to post?
  - id: mediaUpload
    intent: Upload a media file in one request
    question: What's the simplest way to upload an image for a post in a single request?
  - id: initializeMediaUpload
    intent: Start a chunked media upload
    question: Where does a chunked upload for a large video begin?
  phrasing_ops: 11
  slug: x-media-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Endpoint for retrieving news stories — 2 operation(s) in the X-published contract.
  name: X News API
  phrasing_intents:
  - id: searchNews
    intent: Search news stories
    question: What news stories on X are about a given topic?
  - id: getNews
    intent: Get a news story by ID
    question: How do I fetch one news story when I already have its ID?
  phrasing_ops: 2
  slug: x-news-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Endpoints related to retrieving, searching, and modifying Posts — 14 operation(s) in the X-published contract.
  name: X Posts API
  phrasing_intents:
  - id: getPostsByIds
    intent: Look up several posts by ID
    question: Can I fetch a batch of posts in a single request?
  - id: createPosts
    intent: Publish a post
    question: What's the v2 call to publish a post?
  - id: getPostsAnalytics
    intent: Get engagement analytics for posts
    question: How did my posts perform over a given time window?
  - id: getPostsCountsAll
    intent: Count matching posts across the full archive
    question: How many posts mentioned a keyword across all of X's history?
  - id: getPostsCountsRecent
    intent: Count matching posts from the last 7 days
    question: How many posts matched my query recently?
  - id: searchPostsAll
    intent: Search the full post archive (v2)
    question: Where can I search posts going back to the beginning of X on the v2 API?
  - id: searchPostsRecent
    intent: Search posts from the last 7 days
    question: What have people posted about a topic recently?
  - id: deletePosts
    intent: Delete a post
    question: How can I delete one of my posts?
  phrasing_ops: 19
  slug: x-posts-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Endpoints related to retrieving, managing Spaces — 6 operation(s) in the X-published contract.
  name: X Spaces API
  phrasing_intents:
  - id: getSpacesByIds
    intent: Look up several Spaces by ID
    question: Can I fetch details for multiple Spaces in one request?
  - id: getSpacesByCreatorIds
    intent: Find Spaces hosted by given users
    question: Which Spaces are certain users hosting?
  - id: searchSpaces
    intent: Search Spaces by keyword
    question: Are there any live Spaces about a topic right now?
  - id: getSpacesById
    intent: Get one Space by ID
    question: What details does a single Space expose?
  - id: getSpacesBuyers
    intent: List ticket buyers for a Space
    question: Who bought tickets to my ticketed Space?
  - id: getSpacesPosts
    intent: Get posts shared in a Space
    question: Which posts were shared during a Space?
  phrasing_ops: 6
  slug: x-spaces-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Endpoints related to streaming — 18 operation(s) in the X-published contract.
  name: X Stream API
  phrasing_intents:
  - id: activityStream
    intent: Stream X activity events
    question: Can I open a live stream of the activity events I've subscribed to?
  - id: streamLikesCompliance
    intent: Stream Likes compliance events
    question: Where do I get compliance events about Likes I've stored?
  - id: streamLikesFirehose
    intent: Stream every public Like
    question: Is there a firehose of all public Likes in real time?
  - id: streamLikesSample10
    intent: Stream a 10% sample of Likes
    question: Can I get a 10 percent sample of public Likes instead of the whole firehose?
  - id: streamPostsCompliance
    intent: Stream Posts compliance events
    question: Where do I receive compliance events for Posts I've stored?
  - id: streamPostsFirehose
    intent: Stream every public Post in all languages
    question: Is there a full firehose of every public Post in real time?
  - id: streamPostsFirehoseEn
    intent: Stream all English-language Posts
    question: Can I get a firehose of only English-language Posts?
  - id: streamPostsFirehoseJa
    intent: Stream all Japanese-language Posts
    question: Can I get a firehose of only Japanese-language Posts?
  phrasing_ops: 18
  slug: x-stream-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Endpoint for retrieving trends — 2 operation(s) in the X-published contract.
  name: X Trends API
  phrasing_intents:
  - id: getTrendsByWoeid
    intent: Get trends for a location (v2)
    question: What's trending right now in a specific city or country on the v2 endpoint?
  - id: getTrendsPersonalizedTrends
    intent: Get my personalized trends
    question: What topics are trending for me personally?
  - id: getTrendsByWoeidByWoeid
    intent: Get location trends (unversioned endpoint)
    question: Is there an older unversioned path for trending topics by Where On Earth ID?
  phrasing_ops: 3
  slug: x-trends-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Endpoints related to retrieving usage — 2 operation(s) in the X-published contract.
  name: X Usage API
  phrasing_intents:
  - id: getUsageCredits
    intent: Check my developer credit balance
    question: How much developer-platform credit do I have left in USD?
  - id: getUsage
    intent: Get post consumption usage
    question: How many posts has my app consumed recently?
  phrasing_ops: 2
  slug: x-usage-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Endpoints related to retrieving, managing relationships of Users — 42 operation(s) in the X-published contract.
  name: X Users API
  phrasing_intents:
  - id: getUsersByIds
    intent: Look up several users by ID
    question: Can I fetch profiles for a batch of user IDs at once?
  - id: getUsersByUsernames
    intent: Look up several users by username
    question: How do I turn a list of @handles into user profiles in one call?
  - id: getUsersByUsername
    intent: Look up one user by username (v2)
    question: What's the v2 way to get a single profile from an @handle?
  - id: getUsersMe
    intent: Get the authenticated user's profile
    question: Which account is my access token acting as?
  - id: getUsersPublicKeys
    intent: Get Chat public keys for several users
    question: Can I fetch the X Chat encryption public keys for a batch of users?
  - id: getUsersRepostsOfMe
    intent: See reposts of my posts
    question: Which of my posts have other people reposted?
  - id: searchUsers
    intent: Search for users by keyword
    question: What accounts match a name or keyword?
  - id: getUsersById
    intent: Look up one user by ID (v2)
    question: What's the v2 call for a single user profile by numeric ID?
  phrasing_ops: 44
  slug: x-users-api
- baseURL: https://api.x.com
  baseurl_source: declared
  description: Endpoints relating to retrieving, managing webhooks and webhook configs — 8 operation(s) in the X-published contract.
  name: X Webhooks API
  phrasing_intents:
  - id: getWebhooksStreamLinks
    intent: List filtered-stream webhook links
    question: Which webhooks are currently receiving my filtered stream events?
  - id: deleteWebhooksStreamLink
    intent: Stop filtered stream delivery to a webhook
    question: Can I stop filtered stream events going to a webhook?
  - id: createWebhooksStreamLink
    intent: Deliver filtered stream events to a webhook
    question: How do I get filtered stream matches pushed to a webhook instead of holding a connection open?
  - id: getWebhooks
    intent: List my app's webhook configs
    question: Which webhook URLs are registered for my app?
  - id: createWebhooks
    intent: Register a webhook URL
    question: How do I register a new webhook URL with X?
  - id: createWebhookReplayJob
    intent: Replay missed webhook events
    question: Can I get events my webhook missed during an outage re-delivered?
  - id: deleteWebhooks
    intent: Delete a webhook config
    question: Can I remove a webhook URL I no longer use?
  - id: validateWebhooks
    intent: Trigger a CRC check on a webhook
    question: Can I re-validate my webhook with a fresh CRC challenge?
  phrasing_ops: 8
  slug: x-webhooks-api
- description: 'The X Ads API enables programmatic management of advertising campaigns on the X platform including campaign creation and scheduling, custom audience building, creative management (draft posts, cards, '
  name: X Ads API
  slug: x-ads-api
artifact_total: 39
asyncapis:
- description: ''
  name: X Webhooks
  slug: x-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: X API v2 Posts API
  slug: open-x-posts-api
- collection_type: open
  name: X API v2 Posts Trends API
  slug: open-x-trends-api
- collection_type: open
  name: X API v2 Posts Users API
  slug: open-x-users-api
- collection_type: open
  name: X API v2
  slug: open-x
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/capabilities/x-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/x-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/skills/x-x-skill.md
  title: ''
  type: AgentSkill
  url: skills/x-x-skill.md
- group: company
  title: ''
  type: Website
  url: https://x.com/
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/openapi/_original/x-api-v2-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/x-api-v2-openapi.json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/authentication/x-authentication.yml
  title: ''
  type: Authentication
  url: authentication/x-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/scopes/x-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/x-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/agentic-access/x-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/x-agentic-access.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/packages/x-packages.yml
  title: ''
  type: Packages
  url: packages/x-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/packages/x-packages.yml
  title: ''
  type: SDKs
  url: packages/x-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/cli/x-cli.yml
  title: ''
  type: CLI
  url: cli/x-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/components/x-components.yml
  title: ''
  type: Components
  url: components/x-components.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/sandbox/x-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/x-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/mcp/x-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/x-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/mcp/x-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/x-tool-crosswalk.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/a2a/x-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/x-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/llms/x-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/x-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/well-known/x-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/x-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/well-known/x-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/x-security.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/conformance/x-conformance.yml
  title: ''
  type: Conformance
  url: conformance/x-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/errors/x-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/x-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/conventions/x-conventions.yml
  title: ''
  type: Conventions
  url: conventions/x-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/conventions/x-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/x-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/data-model/x-data-model.yml
  title: ''
  type: DataModel
  url: data-model/x-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/asyncapi/x-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/x-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/lifecycle/x-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/x-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/changelog/x-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/x-changelog.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/overlays/x-api-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/x-api-v2-overlay.yaml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/plans/x-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/x-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/rate-limits/x-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/x-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/finops/x-finops.yml
  title: ''
  type: FinOps
  url: finops/x-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/security/x-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/x-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/security/x-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/x-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/security/x-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/x-vulnerability-disclosure.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.x.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.x.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.x.com/x-api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.x.com/x-api/getting-started/make-your-first-request
- group: operate
  title: ''
  type: Support
  url: https://devcommunity.x.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xdevplatform
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.x.com/x-api/getting-started/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.x.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.x.com/en/developer-terms/agreement-and-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://x.com/en/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.x.com/status
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.x.com/x-api/fundamentals/versioning
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/xapidevelopers/x-api-public-workspace/collection/34902927-2efc5689-99c6-4ab6-8091-996f35c2fd80
created: '2025-08-14'
description: X (formerly Twitter) operates the X Developer Platform, the programmable interface to the public conversation on X. The X API v2 is a 190-operation REST surface covering Posts, Users, Direct Messages, the encrypted Chat API, Lists, Spaces, Media, Communities, Community Notes, Broadcasts, News, Trends, Articles and Bots, plus a substantial real-time layer — filtered stream, firehose and sample volume streams, compliance streams, Account Activity webhooks and the X Activity API. X publishes a machine-readable OpenAPI at api.x.com/2/openapi.json, an llms.txt family, an AGENTS.md, an agentskills.io skill, an A2A agent card and two hosted MCP servers. Access is sold pay-per-usage in prepaid credits rather than by subscription tier, with an Enterprise agreement for volume above the published cap.
finops:
- name: X Finops
  service_category: API
  slug: x-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/x.png
layout: provider
mcp_servers:
- description: 'X ships TWO hosted MCP servers: an API server at https://api.x.com/mcp that calls X API v2 endpoints, and a documentation-search server at https://docs.x.com/mcp. Both are Streamable HTTP remote endpo'
  name: X MCP Server
  slug: x-mcp-yml
modified: '2026-08-28'
name: X
nav: Providers
network: true
overview: 'X publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Account Activity API, Account API, Activity API, and 21 more. Tagged areas include Spaces, Conversations, X, Social, and Social Media.


  The X catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  X''s developer surface includes authentication, CLI, sandbox, changelog, documentation, API reference, getting-started guide, and 40 more developer resources.'
plans:
- name: X Plans Pricing
  plan_count: 2
  slug: x-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 17
  name: X Rate Limits
  slug: x-rate-limits
scopes:
- name: X Scopes
  scope_count: 29
  slug: x-scopes
  summary_line: 29 scopes · authorizationCode
score:
  band: exemplar
  composite: 70.9
  coverage:
    artifact_dirs: 29
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.4
  facets:
    access_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 57.6
    developer_ergonomics: 76.2
    discoverability: 75.0
    operational_transparency: 76.3
  previous_composite: 68.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/screenshots/x-2026-06-20T201653.png
security:
- kind: authentication
  name: X Authentication
  slug: x-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: X Domain Security
  slug: x-domain-security
  summary_line: HSTS
- kind: vulnerability-disclosure
  name: X Vulnerability Disclosure
  slug: x-vulnerability-disclosure
  summary_line: Hackerone
slug: x
tags:
- Spaces
- Conversations
- X
- Social
- Social Media
- Posts
- User
- Direct Messages
- Streaming
- Webhook
- Real-Time
- Trends
- Media
- Content
- Agents
- MCP
- A2A
website: https://x.com/
---
