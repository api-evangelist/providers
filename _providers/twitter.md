---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 67
  human_in_the_loop: 3
  name: Twitter Agentic Access
  operation_count: 163
  slug: twitter-agentic-access
  summary_line: 163 operations · 67 acting · 3 human-in-the-loop
api_count: 23
apis:
- description: 'The X Ads API enables programmatic management of advertising campaigns on the X platform including campaign creation and scheduling, custom audience building, creative management (draft posts, cards, '
  name: X Ads API
  slug: x-ads-api
- description: The X Activity API provides real-time activity event subscriptions with sub-second delivery via streaming or webhooks. Subscribe to profile updates, follows, likes, reposts, and other user activity ev
  name: X Activity API
  slug: x-activity-api
- description: Endpoints relating to retrieving, managing AAA subscriptions
  name: X (Twitter) Account Activity API
  slug: twitter-account-activity-api
- description: The Activity API from X (Twitter) — 3 operation(s) for activity.
  name: X (Twitter) Activity API
  slug: twitter-activity-api
- description: Endpoints related to retrieving, managing bookmarks of a user
  name: X (Twitter) Bookmarks API
  slug: twitter-bookmarks-api
- description: The Chat API from X (Twitter) — 15 operation(s) for chat.
  name: X (Twitter) Chat API
  slug: twitter-chat-api
- description: The Communities API from X (Twitter) — 2 operation(s) for communities.
  name: X (Twitter) Communities API
  slug: twitter-communities-api
- description: The Community Notes API from X (Twitter) — 5 operation(s) for community notes.
  name: X (Twitter) Community Notes API
  slug: twitter-community-notes-api
- description: Endpoints related to keeping X data in your systems compliant
  name: X (Twitter) Compliance API
  slug: twitter-compliance-api
- description: Endpoints related to streaming connections
  name: X (Twitter) Connections API
  slug: twitter-connections-api
- description: Endpoints related to retrieving, managing Direct Messages
  name: X (Twitter) Direct Messages API
  slug: twitter-direct-messages-api
- description: Miscellaneous endpoints for general API functionality
  name: X (Twitter) General API
  slug: twitter-general-api
- description: The Likes API from X (Twitter) — 2 operation(s) for likes.
  name: X (Twitter) Likes API
  slug: twitter-likes-api
- description: Endpoints related to retrieving, managing Lists
  name: X (Twitter) Lists API
  slug: twitter-lists-api
- description: Endpoints related to Media
  name: X (Twitter) Media API
  slug: twitter-media-api
- description: Endpoint for retrieving news stories
  name: X (Twitter) News API
  slug: twitter-news-api
- description: Endpoints related to retrieving, managing Spaces
  name: X (Twitter) Spaces API
  slug: twitter-spaces-api
- description: Endpoints related to streaming
  name: X (Twitter) Stream API
  slug: twitter-stream-api
- description: The Trends API from X (Twitter) — 2 operation(s) for trends.
  name: X (Twitter) Trends API
  slug: twitter-trends-api
- description: Endpoints related to retrieving, searching, and modifying Tweets
  name: X (Twitter) Tweets API
  slug: twitter-tweets-api
- description: The Usage API from X (Twitter) — 1 operation(s) for usage.
  name: X (Twitter) Usage API
  slug: twitter-usage-api
- description: Endpoints related to retrieving, managing relationships of Users
  name: X (Twitter) Users API
  slug: twitter-users-api
- description: The Webhooks API from X (Twitter) — 5 operation(s) for webhooks.
  name: X (Twitter) Webhooks API
  slug: twitter-webhooks-api
arazzos:
- description: Find a post by search, bookmark it, then delete that bookmark.
  name: X Search, Bookmark a Post, Then Remove the Bookmark
  slug: twitter-bookmark-and-remove-workflow
- description: Create a new List, resolve a member handle, and add them to the List.
  name: X Create a List and Add a Member by Username
  slug: twitter-create-list-add-member-workflow
- description: Read a List by id to confirm it exists, then follow that List.
  name: X Confirm a List and Follow It
  slug: twitter-follow-list-by-id-workflow
- description: Resolve a target handle to an id, then follow that user.
  name: X Follow a User by Their Username
  slug: twitter-follow-user-by-username-workflow
- description: Resolve a username to an id, then page that user's followers.
  name: X List the Followers of a Handle
  slug: twitter-followers-of-handle-workflow
- description: Resolve a username to an id, then fetch that user's liked posts.
  name: X List the Posts a Handle Has Liked
  slug: twitter-liked-posts-of-handle-workflow
- description: Read a List by id, then page the members of that List.
  name: X Fetch a List's Details and Its Members
  slug: twitter-list-detail-and-members-workflow
- description: Resolve a username to an id, then fetch posts that mention that user.
  name: X List the Posts Mentioning a Handle
  slug: twitter-mentions-of-handle-workflow
- description: Resolve a target handle to an id, then mute that user.
  name: X Mute a User by Their Username
  slug: twitter-mute-user-by-username-workflow
- description: List the owned Lists, then pin the first one to the user's profile.
  name: X Pin the Authenticated User's First Owned List
  slug: twitter-pin-owned-list-workflow
- description: Resolve a handle, get their latest post, then list who liked it.
  name: X Audit Engagement on a User's Latest Post
  slug: twitter-post-engagement-audit-workflow
- description: Publish a post, like it from the authenticated account, then remove it.
  name: X Create a Post, Like It, Then Delete It
  slug: twitter-post-like-cleanup-workflow
- description: Search recent posts, then publish a quote post of the top match.
  name: X Quote a Post Found by Search
  slug: twitter-quote-post-from-search-workflow
- description: Resolve a handle, fetch their latest post, then reply to it.
  name: X Reply to a User's Latest Post
  slug: twitter-reply-to-latest-post-workflow
- description: Search for a post, repost the top match, then remove the repost.
  name: X Find a Post, Repost It, Then Undo the Repost
  slug: twitter-repost-then-undo-workflow
- description: Resolve a handle, get their latest post, then list who reposted it.
  name: X List Who Reposted a Handle's Latest Post
  slug: twitter-reposters-of-latest-post-workflow
- description: Run a recent search, then fetch full details for the first matching post.
  name: X Search Recent Posts and Hydrate the Top Match
  slug: twitter-search-recent-get-details-workflow
- description: Resolve a target handle to an id, then unfollow that user.
  name: X Unfollow a User by Their Username
  slug: twitter-unfollow-user-by-username-workflow
- description: Look up a user by username, then pull their most recent posts.
  name: X Resolve User and List Their Recent Posts
  slug: twitter-user-lookup-recent-posts-workflow
artifact_total: 175
collections:
- collection_type: postman
  name: X API v2
  slug: postman-x-api-openapi
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: X API v2 Account Activity API
  slug: open-twitter-account-activity-api
- collection_type: open
  name: X API v2 Account Activity API
  slug: open-twitter-activity-api
- collection_type: open
  name: X API v2 Account Activity Bookmarks API
  slug: open-twitter-bookmarks-api
- collection_type: open
  name: X API v2 Account Activity Chat API
  slug: open-twitter-chat-api
- collection_type: open
  name: X API v2 Account Activity Communities API
  slug: open-twitter-communities-api
- collection_type: open
  name: X API v2 Account Activity Community Notes API
  slug: open-twitter-community-notes-api
- collection_type: open
  name: X API v2 Account Activity Compliance API
  slug: open-twitter-compliance-api
- collection_type: open
  name: X API v2 Account Activity Connections API
  slug: open-twitter-connections-api
- collection_type: open
  name: X API v2 Account Activity Direct Messages API
  slug: open-twitter-direct-messages-api
- collection_type: open
  name: X API v2 Account Activity General API
  slug: open-twitter-general-api
- collection_type: open
  name: X API v2 Account Activity Likes API
  slug: open-twitter-likes-api
- collection_type: open
  name: X API v2 Account Activity Lists API
  slug: open-twitter-lists-api
- collection_type: open
  name: X API v2 Account Activity Media API
  slug: open-twitter-media-api
- collection_type: open
  name: X API v2 Account Activity News API
  slug: open-twitter-news-api
- collection_type: open
  name: X API v2 Account Activity Spaces API
  slug: open-twitter-spaces-api
- collection_type: open
  name: X API v2 Account Activity Stream API
  slug: open-twitter-stream-api
- collection_type: open
  name: X API v2 Account Activity Trends API
  slug: open-twitter-trends-api
- collection_type: open
  name: X API v2 Account Activity Tweets API
  slug: open-twitter-tweets-api
- collection_type: open
  name: X API v2 Account Activity Usage API
  slug: open-twitter-usage-api
- collection_type: open
  name: X API v2 Account Activity Users API
  slug: open-twitter-users-api
- collection_type: open
  name: X API v2 Account Activity Webhooks API
  slug: open-twitter-webhooks-api
- collection_type: open
  name: X API v2
  slug: open-x-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/twitter-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/twitter-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/twitter-scopes.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/twitter-bookmark-and-remove-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/twitter-create-list-add-member-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/twitter-follow-list-by-id-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/twitter-follow-user-by-username-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/twitter-followers-of-handle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/twitter-liked-posts-of-handle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/twitter-list-detail-and-members-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/twitter-mentions-of-handle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/twitter-mute-user-by-username-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/twitter-pin-owned-list-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/twitter-post-engagement-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/twitter-post-like-cleanup-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/twitter-quote-post-from-search-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/twitter-reply-to-latest-post-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/twitter-repost-then-undo-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/twitter-reposters-of-latest-post-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/twitter-search-recent-get-details-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/twitter-unfollow-user-by-username-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/twitter-user-lookup-recent-posts-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/x-corp
- group: start
  title: ''
  type: Portal
  url: https://developer.x.com/en/portal/dashboard
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.x.com/x-api/getting-started/make-your-first-request
- group: start
  title: ''
  type: Console
  url: https://developer.x.com/en/portal/dashboard
- group: start
  title: ''
  type: Signup
  url: https://developer.x.com/en/portal/petition/essential/basic-info
- group: auth
  title: ''
  type: Authentication
  url: https://docs.x.com/resources/fundamentals/authentication
- group: build
  title: Python XDK
  type: SDKs
  url: https://docs.x.com/sdks-and-tools/python-xdk
- group: build
  title: TypeScript XDK
  type: SDKs
  url: https://docs.x.com/sdks-and-tools/typescript-xdk
- group: build
  title: xurl
  type: CLI
  url: https://docs.x.com/sdks-and-tools/xurl
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.x.com/en/portal/petition/essential/basic-info
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
  url: https://api.twitterstat.us/
- group: operate
  title: ''
  type: Support
  url: https://devcommunity.x.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.x.com/developer
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.x.com/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xdevplatform
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/xdevplatform/xdk-python
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/xdevplatform/xdk-typescript
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/xdevplatform/xurl
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/xdevplatform/xdk
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/xdevplatform/twitter-api-java-sdk
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/xdevplatform/twitter-ruby-ads-sdk
- group: build
  title: ''
  type: Tools
  url: https://github.com/xdevplatform/xmcp
- group: start
  title: ''
  type: Sandbox
  url: https://github.com/xdevplatform/playground
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/xdevplatform/samples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/xdevplatform/xchat-bot-python
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://docs.x.com/sdks-and-tools/postman
- group: other
  title: ''
  type: X
  url: https://x.com/XDevelopers
created: '2025-07-29'
description: X (formerly Twitter) is a social media platform providing APIs for accessing and integrating with posts, users, spaces, direct messages, lists, media, trends, and real-time streaming data. The X API enables developers to build applications that read and write X data, manage advertising campaigns, and subscribe to real-time activity events. Available through pay-per-use credit-based pricing with enterprise options for high-volume access.
examples:
- key_count: 2
  name: X Api Activity Streaming Response Example
  slug: x-api-activity-streaming-response-example
- key_count: 7
  name: X Api Activity Subscription Example
  slug: x-api-activity-subscription-example
- key_count: 9
  name: X Api Compliance Job Example
  slug: x-api-compliance-job-example
- key_count: 3
  name: X Api Create Dm Conversation Request Example
  slug: x-api-create-dm-conversation-request-example
- key_count: 10
  name: X Api Dm Event Example
  slug: x-api-dm-event-example
- key_count: 2
  name: X Api Error Example
  slug: x-api-error-example
- key_count: 6
  name: X Api Expansions Example
  slug: x-api-expansions-example
- key_count: 4
  name: X Api Filtered Streaming Tweet Response Example
  slug: x-api-filtered-streaming-tweet-response-example
- key_count: 4
  name: X Api Get2 Tweets Search Recent Response Example
  slug: x-api-get2-tweets-search-recent-response-example
- key_count: 3
  name: X Api Get2 Users Id Response Example
  slug: x-api-get2-users-id-response-example
- key_count: 3
  name: X Api List Create Request Example
  slug: x-api-list-create-request-example
- key_count: 8
  name: X Api List Example
  slug: x-api-list-example
- key_count: 4
  name: X Api Media Example
  slug: x-api-media-example
- key_count: 8
  name: X Api Place Example
  slug: x-api-place-example
- key_count: 5
  name: X Api Poll Example
  slug: x-api-poll-example
- key_count: 4
  name: X Api Problem Example
  slug: x-api-problem-example
- key_count: 10
  name: X Api Space Example
  slug: x-api-space-example
- key_count: 10
  name: X Api Tweet Create Request Example
  slug: x-api-tweet-create-request-example
- key_count: 2
  name: X Api Tweet Create Response Example
  slug: x-api-tweet-create-response-example
- key_count: 2
  name: X Api Tweet Delete Response Example
  slug: x-api-tweet-delete-response-example
- key_count: 10
  name: X Api Tweet Example
  slug: x-api-tweet-example
- key_count: 10
  name: X Api User Example
  slug: x-api-user-example
- key_count: 1
  name: X Api Users Following Create Request Example
  slug: x-api-users-following-create-request-example
features:
- description: Create, delete, edit, repost, quote, like, and bookmark posts programmatically.
  name: Post Management
- description: Access filtered streams, sampled streams, firehose, and language-specific streams for real-time post data.
  name: Real-Time Streaming
- description: Search the complete archive of public posts with advanced query operators and date filtering.
  name: Full-Archive Search
- description: Look up users by ID or username, manage follows, blocks, mutes, and retrieve user metrics.
  name: User Lookup and Management
- description: Discover and look up live audio Spaces with host, speaker, and listener data.
  name: Spaces
- description: Send and receive direct messages, create conversations, and manage participants.
  name: Direct Messages
- description: Create, manage, and query lists including membership, followers, and pinned lists.
  name: Lists
- description: Access personalized and geographic trending topics.
  name: Trends
- description: Upload images, videos, and large files using chunked upload with metadata and subtitle support.
  name: Media Upload
- description: Access compliance streams and batch jobs for data deletion and user protection events.
  name: Compliance
- description: Access community data and community notes for collaborative fact-checking.
  name: Communities and Community Notes
- description: Programmatically create, schedule, and manage advertising campaigns with targeting and budget controls.
  name: Ad Campaign Management
finops:
- name: Twitter Finops
  service_category: Social Media Developer API
  slug: twitter-finops
graphqls:
- description: This conceptual GraphQL schema models the Twitter (X) API v2 data model. The X API v2 is a REST API available at `https://api.x.com/2`, but the types defined here represent the full surface of objects
  name: Twitter (X) GraphQL Schema
  slug: twitter-graphql
image: https://abs.twimg.com/favicons/twitter.ico
integrations:
- description: Official Postman collections for exploring and testing X API endpoints interactively.
  name: Postman
- description: Integration with AI tools and agents through Model Context Protocol servers.
  name: MCP Servers
- description: Real-time event delivery via webhooks for the Activity API.
  name: Webhook Delivery
json_schemas:
- name: ActivityStreamingResponse
  property_count: 2
  slug: x-api-activity-streaming-response
- name: ActivitySubscription
  property_count: 7
  slug: x-api-activity-subscription
- name: AddOrDeleteRulesRequest
  property_count: 0
  slug: x-api-add-or-delete-rules-request
- name: ComplianceJob
  property_count: 9
  slug: x-api-compliance-job
- name: ComplianceJobStatus
  property_count: 0
  slug: x-api-compliance-job-status
- name: CreateDmConversationRequest
  property_count: 3
  slug: x-api-create-dm-conversation-request
- name: DmEvent
  property_count: 13
  slug: x-api-dm-event
- name: Error
  property_count: 2
  slug: x-api-error
- name: Expansions
  property_count: 6
  slug: x-api-expansions
- name: FilteredStreamingTweetResponse
  property_count: 4
  slug: x-api-filtered-streaming-tweet-response
- name: Get2TweetsSearchRecentResponse
  property_count: 4
  slug: x-api-get2-tweets-search-recent-response
- name: Get2UsersIdResponse
  property_count: 3
  slug: x-api-get2-users-id-response
- name: ListCreateRequest
  property_count: 3
  slug: x-api-list-create-request
- name: List
  property_count: 8
  slug: x-api-list
- name: Media
  property_count: 4
  slug: x-api-media
- name: Place
  property_count: 8
  slug: x-api-place
- name: Poll
  property_count: 5
  slug: x-api-poll
- name: Problem
  property_count: 4
  slug: x-api-problem
- name: Space
  property_count: 17
  slug: x-api-space
- name: TweetCreateRequest
  property_count: 16
  slug: x-api-tweet-create-request
- name: TweetCreateResponse
  property_count: 2
  slug: x-api-tweet-create-response
- name: TweetDeleteResponse
  property_count: 2
  slug: x-api-tweet-delete-response
- name: Tweet
  property_count: 29
  slug: x-api-tweet
- name: User
  property_count: 21
  slug: x-api-user
- name: UsersFollowingCreateRequest
  property_count: 1
  slug: x-api-users-following-create-request
json_structures:
- name: X Api Activity Streaming Response Structure
  property_count: 2
  slug: x-api-activity-streaming-response-structure
- name: X Api Activity Subscription Structure
  property_count: 7
  slug: x-api-activity-subscription-structure
- name: X Api Add Or Delete Rules Request Structure
  property_count: 0
  slug: x-api-add-or-delete-rules-request-structure
- name: X Api Compliance Job Status Structure
  property_count: 0
  slug: x-api-compliance-job-status-structure
- name: X Api Compliance Job Structure
  property_count: 9
  slug: x-api-compliance-job-structure
- name: X Api Create Dm Conversation Request Structure
  property_count: 3
  slug: x-api-create-dm-conversation-request-structure
- name: X Api Dm Event Structure
  property_count: 13
  slug: x-api-dm-event-structure
- name: X Api Error Structure
  property_count: 2
  slug: x-api-error-structure
- name: X Api Expansions Structure
  property_count: 6
  slug: x-api-expansions-structure
- name: X Api Filtered Streaming Tweet Response Structure
  property_count: 4
  slug: x-api-filtered-streaming-tweet-response-structure
- name: X Api Get2 Tweets Search Recent Response Structure
  property_count: 4
  slug: x-api-get2-tweets-search-recent-response-structure
- name: X Api Get2 Users Id Response Structure
  property_count: 3
  slug: x-api-get2-users-id-response-structure
- name: X Api List Create Request Structure
  property_count: 3
  slug: x-api-list-create-request-structure
- name: X Api List Structure
  property_count: 8
  slug: x-api-list-structure
- name: X Api Media Structure
  property_count: 4
  slug: x-api-media-structure
- name: X Api Place Structure
  property_count: 8
  slug: x-api-place-structure
- name: X Api Poll Structure
  property_count: 5
  slug: x-api-poll-structure
- name: X Api Problem Structure
  property_count: 4
  slug: x-api-problem-structure
- name: X Api Space Structure
  property_count: 17
  slug: x-api-space-structure
- name: X Api Tweet Create Request Structure
  property_count: 16
  slug: x-api-tweet-create-request-structure
- name: X Api Tweet Create Response Structure
  property_count: 2
  slug: x-api-tweet-create-response-structure
- name: X Api Tweet Delete Response Structure
  property_count: 2
  slug: x-api-tweet-delete-response-structure
- name: X Api Tweet Structure
  property_count: 29
  slug: x-api-tweet-structure
- name: X Api User Structure
  property_count: 21
  slug: x-api-user-structure
- name: X Api Users Following Create Request Structure
  property_count: 1
  slug: x-api-users-following-create-request-structure
jsonld:
- class_count: 23
  name: X Api Context
  property_count: 118
  slug: x-api-context
layout: provider
modified: '2026-05-19'
name: X (Twitter)
nav: Providers
network: true
overview: 'X (Twitter) publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Account Activity API, Activity API, Bookmarks API, and 18 more. Tagged areas include Social-Media, Microblogging, Real-Time Data, Streaming, and Advertising.


  The X (Twitter) catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  X (Twitter)''s developer surface includes authentication, developer portal, getting-started guide, developer console, signup flow, CLI, pricing, and 44 more developer resources.'
plans:
- name: Twitter Plans Pricing
  plan_count: 1
  slug: twitter-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 13
  name: Twitter Rate Limits
  slug: twitter-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: X (Twitter) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: twitter-jsonschema-spectral-rules
- effective_rule_count: 94
  extends:
  - spectral:oas
  name: X (Twitter) API Rules
  rule_count: 53
  severity_counts:
    error: 16
    hint: 0
    info: 18
    warn: 19
  slug: twitter-spectral-rules
scopes:
- name: Twitter Scopes
  scope_count: 21
  slug: twitter-scopes
  summary_line: 21 scopes · authorizationCode
score:
  band: strong
  composite: 58.3
  delta: 3.4
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 13.6
    contract_quality: 67.8
    developer_ergonomics: 76.2
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 42.1
  previous_composite: 54.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/twitter/refs/heads/main/screenshots/twitter-2026-08-17T130216.png
security:
- kind: authentication
  name: Twitter Authentication
  slug: twitter-authentication
  summary_line: http/oauth2 · 3 schemes
slug: twitter
solutions:
- description: Credit-based pricing with no commitments. Pay only for what you use with access to core X API endpoints.
  name: X API Pay-Per-Use
- description: High-volume access with custom rate limits, dedicated account management, full firehose, and premium support.
  name: X API Enterprise
- description: Advertising platform API for campaign management, audience targeting, creative management, and analytics.
  name: X Ads API
tags:
- Social-Media
- Microblogging
- Real-Time Data
- Streaming
- Advertising
- Content
use_cases:
- description: Monitor brand mentions, sentiment, and conversations in real-time using filtered streams and search endpoints.
  name: Social Listening
- description: Automate post creation, scheduling, and thread publishing for social media management platforms.
  name: Content Publishing
- description: Retrieve post metrics, user engagement data, and campaign performance for business intelligence.
  name: Analytics and Reporting
- description: Build automated accounts that respond to mentions, post updates, or provide customer service.
  name: Bot Development
- description: Access full-archive search and streaming data for social media research and trend analysis.
  name: Research and Academic Analysis
- description: Programmatically manage ad campaigns, audiences, creatives, and bidding strategies at scale.
  name: Advertising Automation
- description: Track live events, breaking news, and trending topics with streaming APIs and trend endpoints.
  name: Real-Time Event Monitoring
- description: Manage followers, lists, and direct messages for community engagement and moderation.
  name: Community Management
website: https://developer.x.com/en/portal/dashboard
---
