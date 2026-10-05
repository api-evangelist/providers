---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: true
    agentic_commerce: false
    auth_clarity: served
    consent_identity: true
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 91.4
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 56
  human_in_the_loop: 56
  name: Xquik Agentic Access
  operation_count: 127
  slug: xquik-agentic-access
  summary_line: 127 operations · 56 acting · 56 human-in-the-loop
api_count: 2
apis:
- description: Hosted MCP server for the Xquik API with OAuth 2.1 and API-key access.
  name: Xquik API MCP Server
  slug: xquik-api-mcp-server
- description: Read-only hosted MCP server for searching Xquik documentation.
  name: Xquik Docs MCP Server
  slug: xquik-docs-mcp-server
- baseURL: https://xquik.com/api/v1
  baseurl_source: declared
  description: Account info and settings
  name: Xquik Account API
  phrasing_intents:
  - id: getAccount
    intent: View my account info
    question: Can I pull up my own account info through the API?
  - id: updateAccount
    intent: Change my account locale
    question: Can I change the language locale on my account?
  - id: setXIdentity
    intent: Link an X username to my account
    question: Can I link my X username to my account?
  phrasing_ops: 3
  slug: xquik-api-account-api
- baseURL: https://xquik.com/api/v1
  baseurl_source: declared
  description: API key management (session auth only)
  name: Xquik API Keys API
  phrasing_intents:
  - id: listApiKeys
    intent: List my API keys
    question: Which API keys exist on my account?
  - id: createApiKey
    intent: Create a new API key
    question: How do I generate a new API key?
  - id: revokeApiKey
    intent: Revoke an API key
    question: Can I revoke an API key that leaked?
  phrasing_ops: 3
  slug: xquik-api-api-keys-api
- baseURL: https://xquik.com/api/v1
  baseurl_source: declared
  description: Long-form X Article extraction
  name: Xquik Articles API
  phrasing_intents:
  - id: getArticle
    intent: Read the full content of an X Article
    question: Can I get the full text of an X Article from its tweet ID?
  phrasing_ops: 1
  slug: xquik-api-articles-api
- baseURL: https://xquik.com/api/v1
  baseurl_source: declared
  description: X Community info, members, and tweets
  name: Xquik Communities API
  phrasing_intents:
  - id: getCommunityInfo
    intent: Get an X Community's profile
    question: How many members does an X Community have?
  - id: getCommunityMembers
    intent: List members of an X Community
    question: Who are the members of an X Community?
  - id: getCommunityModerators
    intent: List moderators of an X Community
    question: Who moderates an X Community?
  - id: getCommunityTweets
    intent: Read the tweet feed of an X Community
    question: What has been posted recently in an X Community?
  - id: searchCommunities
    intent: Keyword-search tweets in a community
    question: Can I keyword-search the posts inside one X Community using the community search endpoint?
  - id: getAllCommunityTweets
    intent: Query all community tweets matching a keyword
    question: Can I query every tweet in a community that matches a keyword via the community tweets endpoint?
  phrasing_ops: 6
  slug: xquik-api-communities-api
- baseURL: https://xquik.com/api/v1
  baseurl_source: declared
  description: AI tweet composition, drafts, writing styles, and radar
  name: Xquik Composition API
  phrasing_intents:
  - id: compose
    intent: Build, refine or score a post draft
    question: Can Xquik help me build and refine a tweet draft step by step?
  - id: listDrafts
    intent: List my saved tweet drafts
    question: Where can I see all my saved tweet drafts?
  - id: createDraft
    intent: Save a tweet draft
    question: Can I save a tweet draft to finish later?
  - id: getDraft
    intent: Open a saved draft
    question: Can I open a single saved draft by its ID?
  - id: deleteDraft
    intent: Delete a saved draft
    question: How do I delete a draft I no longer need?
  - id: listStyles
    intent: List my cached style profiles
    question: Which writing style profiles have I already analyzed?
  - id: analyzeStyle
    intent: Analyze an account's writing style
    question: Can I analyze someone's writing style from their recent tweets?
  - id: compareStyles
    intent: Compare two writing style profiles
    question: How does one account's tweeting style differ from another's?
  phrasing_ops: 13
  slug: xquik-api-composition-api
- baseURL: https://xquik.com/api/v1
  baseurl_source: declared
  description: Giveaway draws from tweet replies
  name: Xquik Draws API
  phrasing_intents:
  - id: listDraws
    intent: List my giveaway draws
    question: Can I see all the giveaway draws I've run?
  - id: createDraw
    intent: Run a giveaway draw on a tweet
    question: How do I pick random giveaway winners from replies to a tweet?
  - id: getDraw
    intent: Get a giveaway draw's details
    question: Who won a giveaway draw I ran?
  - id: exportDraw
    intent: Export a giveaway draw's data
    question: Can I export a draw's data as a file?
  phrasing_ops: 4
  slug: xquik-api-draws-api
- baseURL: https://xquik.com/api/v1
  baseurl_source: declared
  description: Activity events from monitored accounts
  name: Xquik Events API
  phrasing_intents:
  - id: listEvents
    intent: List events captured by my monitors
    question: What events have my monitors picked up lately?
  - id: getEvent
    intent: Get one monitor event
    question: Can I look up one specific monitor event by ID?
  phrasing_ops: 2
  slug: xquik-api-events-api
- baseURL: https://xquik.com/api/v1
  baseurl_source: declared
  description: Bulk data extraction (23 tool types)
  name: Xquik Extractions API
  phrasing_intents:
  - id: listExtractions
    intent: List my extraction jobs
    question: Which extraction jobs have I run?
  - id: createExtraction
    intent: Run a bulk data extraction job
    question: Can I run a bulk extraction job on a tweet, user, community or list?
  - id: estimateExtraction
    intent: Estimate an extraction's credit cost
    question: How much will an extraction job cost before I run it?
  - id: getExtraction
    intent: Read an extraction job's results
    question: Can I read the results of a finished extraction?
  - id: exportExtraction
    intent: Export extraction results to a file
    question: Can I export extraction results to a file?
  phrasing_ops: 5
  slug: xquik-api-extractions-api
- baseURL: https://xquik.com/api/v1
  baseurl_source: declared
  description: Accountless prepaid access for paid read endpoints
  name: Xquik Guest Wallets API
  phrasing_intents:
  - id: createGuestWallet
    intent: Start a prepaid guest wallet checkout
    question: Can I buy API reads without creating an Xquik account?
  - id: topUpGuestWallet
    intent: Top up an existing guest wallet
    question: How do I add more funds to my existing guest key?
  - id: getGuestWalletStatus
    intent: Check guest wallet payment status
    question: Has my guest wallet payment gone through yet?
  phrasing_ops: 3
  slug: xquik-api-guest-wallets-api
- baseURL: https://xquik.com/api/v1
  baseurl_source: declared
  description: X List followers, members, and tweets
  name: Xquik Lists API
  phrasing_intents:
  - id: getListFollowers
    intent: List followers of an X List
    question: Who follows a particular X List?
  - id: getListMembers
    intent: List members of an X List
    question: Which accounts are members of an X List?
  - id: getListTweets
    intent: Read tweets from an X List
    question: What are the latest tweets from accounts on an X List?
  phrasing_ops: 3
  slug: xquik-api-lists-api
- baseURL: https://xquik.com/api/v1
  baseurl_source: declared
  description: Media upload and download
  name: Xquik Media API
  phrasing_intents:
  - id: downloadMedia
    intent: Download images and videos from tweets
    question: Can I download the images and videos from a tweet?
  phrasing_ops: 1
  slug: xquik-api-media-api
- baseURL: https://xquik.com/api/v1
  baseurl_source: declared
  description: X account monitoring with 1-second checks
  name: Xquik Monitors API
  phrasing_intents:
  - id: listMonitors
    intent: List my account monitors
    question: Which X accounts am I currently monitoring?
  - id: createMonitor
    intent: Monitor an X account for activity
    question: How do I get alerted when a specific X account posts?
  - id: listKeywordMonitors
    intent: List my keyword monitors
    question: Which keyword monitors do I have running?
  - id: createKeywordMonitor
    intent: Monitor X for a keyword
    question: Can I get notified whenever a keyword is tweeted?
  - id: getKeywordMonitor
    intent: Get a keyword monitor
    question: Can I look up the settings of one keyword monitor?
  - id: updateKeywordMonitor
    intent: Pause or change a keyword monitor
    question: Can I pause a keyword monitor without deleting it?
  - id: deleteKeywordMonitor
    intent: Delete a keyword monitor
    question: What's the way to delete a keyword monitor I no longer need?
  - id: getMonitor
    intent: Get an account monitor
    question: Can I check the settings of one account monitor?
  phrasing_ops: 10
  slug: xquik-api-monitors-api
- baseURL: https://xquik.com/api/v1
  baseurl_source: declared
  description: Subscription, billing, and credits
  name: Xquik Subscribe API
  phrasing_intents:
  - id: subscribe
    intent: Start a subscription checkout
    question: How do I start a paid subscription?
  - id: getCredits
    intent: Check my credit balance
    question: How many credits do I have left?
  - id: topUpCredits
    intent: Buy credits through a hosted checkout
    question: Can I buy more credits through a hosted checkout?
  - id: getCreditTopupStatus
    intent: Check a credit top-up's billing status
    question: Did my credit top-up payment succeed?
  - id: quickTopUpCredits
    intent: Charge my saved card for credits
    question: Can I buy credits instantly with my saved card?
  phrasing_ops: 5
  slug: xquik-api-subscribe-api
- baseURL: https://xquik.com/api/v1
  baseurl_source: declared
  description: Support ticket management
  name: Xquik Support API
  phrasing_intents:
  - id: downloadSupportAttachment
    intent: Download a support ticket attachment
    question: Can I download an image or video attached to my support ticket?
  - id: createTicket
    intent: Open a support ticket
    question: How do I contact support about a problem?
  - id: listTickets
    intent: List my support tickets
    question: What support tickets have I opened?
  - id: getTicket
    intent: Read a support ticket and its messages
    question: Can I read the full conversation on a support ticket?
  - id: updateTicketStatus
    intent: Change a support ticket's status
    question: Can I close a support ticket once my issue is fixed?
  - id: addTicketMessage
    intent: Reply to a support ticket
    question: How do I reply to support on an existing ticket?
  phrasing_ops: 6
  slug: xquik-api-support-api
- baseURL: https://xquik.com/api/v1
  baseurl_source: declared
  description: Trending topics and hashtags by region
  name: Xquik Trends API
  phrasing_intents:
  - id: getXTrends
    intent: Get trending X topics by region
    question: What is trending on X right now in a given region?
  - id: getTrends
    intent: Get regional trends via the alias endpoint
    question: Is there a shorter alias endpoint for regional trending topics?
  phrasing_ops: 2
  slug: xquik-api-trends-api
- baseURL: https://xquik.com/api/v1
  baseurl_source: declared
  description: Look up, search, and analyze individual tweets
  name: Xquik Tweets API
  phrasing_intents:
  - id: getBatchTweets
    intent: Look up several tweets by ID
    question: Can I fetch several tweets at once by their IDs?
  - id: searchTweets
    intent: Search tweets
    question: How do I search tweets for a keyword?
  - id: lookupTweet
    intent: Get a single tweet
    question: Can I get a single tweet's full text, author and metrics?
  - id: getTweetFavoriters
    intent: List users who liked a tweet
    question: Who liked a specific tweet?
  - id: getBookmarks
    intent: Read my bookmarked tweets
    question: Can I read my bookmarked tweets?
  - id: getBookmarkFolders
    intent: List my bookmark folders
    question: What bookmark folders do I have?
  - id: getTimeline
    intent: Read my home timeline
    question: Can I read my home timeline through the API?
  - id: getTweetQuotes
    intent: List quote tweets of a post
    question: Who has quote-tweeted a post?
  phrasing_ops: 11
  slug: xquik-api-tweets-api
- baseURL: https://xquik.com/api/v1
  baseurl_source: declared
  description: Look up, search, and explore user profiles and relationships
  name: Xquik Users API
  phrasing_intents:
  - id: getBatchUsers
    intent: Look up several users by ID
    question: Can I look up several X users by ID in one call?
  - id: searchUsers
    intent: Search users by name or handle
    question: Can I find X accounts by name or handle?
  - id: getUser
    intent: Get a user's profile
    question: How many followers does a given X user have?
  - id: checkFollow
    intent: Check whether one user follows another
    question: Does one X account follow another?
  - id: getUserTweets
    intent: List a user's recent tweets
    question: What has an account tweeted recently?
  - id: getUserReplies
    intent: Read a user's With Replies timeline
    question: Can I see a user's With Replies timeline?
  - id: getUserLikes
    intent: List tweets a user liked
    question: Which tweets has a user liked?
  - id: getUserMedia
    intent: List a user's media tweets
    question: Can I list only the photo and video tweets from an account?
  phrasing_ops: 15
  slug: xquik-api-users-api
- baseURL: https://xquik.com/api/v1
  baseurl_source: declared
  description: Webhook endpoint management and delivery
  name: Xquik Webhooks API
  phrasing_intents:
  - id: listWebhooks
    intent: List my webhooks
    question: Which webhook endpoints have I registered?
  - id: createWebhook
    intent: Register a webhook for monitor events
    question: How do I receive monitor events at my own URL?
  - id: updateWebhook
    intent: Change a webhook's URL or events
    question: Can I change the URL a webhook posts to?
  - id: deleteWebhook
    intent: Deactivate a webhook
    question: What's the way to deactivate a webhook?
  - id: listWebhookDeliveries
    intent: List a webhook's deliveries
    question: Did my webhook deliveries succeed?
  - id: testWebhook
    intent: Send a test event to a webhook
    question: Can I send a test event to my webhook endpoint?
  - id: resumeWebhook
    intent: Test and resume a webhook
    question: Can I test and reactivate a webhook in one step?
  phrasing_ops: 7
  slug: xquik-api-webhooks-api
- baseURL: https://xquik.com/api/v1
  baseurl_source: declared
  description: Connected X account management
  name: Xquik X Accounts API
  phrasing_intents:
  - id: listXAccounts
    intent: List my connected X accounts
    question: Which X accounts have I connected?
  - id: connectXAccount
    intent: Connect an X account
    question: How do I connect my X account so the API can post for me?
  - id: getXAccountConnectionAttempt
    intent: Check an X account connection attempt
    question: Did my X account connection attempt succeed?
  - id: submitXAccountConnectionChallenge
    intent: Submit an X email verification code
    question: X asked for an email verification code while connecting; how do I submit it?
  - id: getXAccount
    intent: Get a connected X account
    question: Can I see the details of one connected X account?
  - id: disconnectXAccount
    intent: Disconnect an X account
    question: What's the way to disconnect an X account?
  - id: reauthXAccount
    intent: Re-authenticate a connected X account
    question: What do I do when a connected X account needs to log in again?
  - id: bulkRetryXAccounts
    intent: Retry all temporarily failed X accounts
    question: Can I retry all X accounts that failed to log in temporarily?
  phrasing_ops: 8
  slug: xquik-api-x-accounts-api
- baseURL: https://xquik.com/api/v1
  baseurl_source: declared
  description: X write actions (tweets, likes, follows, DMs)
  name: Xquik X Write API
  phrasing_intents:
  - id: createTweet
    intent: Post a tweet
    question: How do I post a tweet through the API?
  - id: getWriteActionStatus
    intent: Check a write action's status
    question: Did my queued tweet or like actually go through?
  - id: deleteTweet
    intent: Delete a tweet
    question: Can I delete a tweet I posted?
  - id: likeTweet
    intent: Like a tweet
    question: Can I like a tweet from a connected account?
  - id: unlikeTweet
    intent: Remove a like from a tweet
    question: How do I remove a like from a tweet?
  - id: retweet
    intent: Retweet a post
    question: Can I retweet a post from my connected account?
  - id: unretweet
    intent: Undo a retweet
    question: How do I undo a retweet?
  - id: followUser
    intent: Follow a user
    question: Can I follow an X user from a connected account?
  phrasing_ops: 19
  slug: xquik-api-x-write-api
artifact_total: 39
asyncapis:
- description: ''
  name: Xquik Asyncapi Provenance
  slug: xquik-asyncapi-provenance
- description: Xquik sends signed monitor events to customer-managed HTTPS webhook endpoints. Xquik is not affiliated with or endorsed by X Corp.
  name: Xquik Monitor Webhooks
  slug: xquik-asyncapi
collections:
- collection_type: open
  name: Xquik API
  slug: open-xquik-rest-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/capabilities/xquik-api-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/xquik-api-capability-edges.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/security/xquik-api-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/xquik-api-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/security/xquik-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xquik-api-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/authentication/xquik-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/xquik-api-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://xquik.com/en
- group: other
  title: ''
  type: APIsJSON
  url: https://xquik.com/apis.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.xquik.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.xquik.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.xquik.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.xquik.com/x-api-quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://docs.xquik.com/api-reference/authentication
- group: design
  title: ''
  type: Idempotency
  url: https://docs.xquik.com/api-reference/x-write/create-tweet
- group: build
  title: ''
  type: SDK
  url: https://github.com/Xquik-dev/x-twitter-scraper-typescript
- group: build
  title: ''
  type: SDK
  url: https://github.com/Xquik-dev/x-twitter-scraper-python
- group: build
  title: ''
  type: SDK
  url: https://github.com/Xquik-dev/x-twitter-scraper-go
- group: build
  title: ''
  type: SDK
  url: https://github.com/Xquik-dev/x-twitter-scraper-ruby
- group: build
  title: ''
  type: SDK
  url: https://github.com/Xquik-dev/x-twitter-scraper-java
- group: build
  title: ''
  type: SDK
  url: https://github.com/Xquik-dev/x-twitter-scraper-kotlin
- group: build
  title: ''
  type: SDK
  url: https://github.com/Xquik-dev/x-twitter-scraper-csharp
- group: build
  title: ''
  type: SDK
  url: https://github.com/Xquik-dev/x-twitter-scraper-php
- group: build
  title: ''
  type: CLI
  url: https://github.com/Xquik-dev/x-twitter-scraper-cli
- group: start
  title: ''
  type: Sandbox
  url: https://docs.xquik.com/mcp/tools
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/collections/xquik.postman_collection.json
  title: ''
  type: Postman
  url: collections/xquik.postman_collection.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/mcp/xquik-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/xquik-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: mailto:support@xquik.com
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/plans/xquik-plans.yml
  title: ''
  type: Plans
  url: plans/xquik-plans.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://xquik.com/en#pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.xquik.com/en/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.xquik.com/en/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://xquik.com/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://xquik.com/en/privacy
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/finops/xquik-finops.yml
  title: ''
  type: FinOps
  url: finops/xquik-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/security/xquik-compliance.md
  title: ''
  type: Compliance
  url: security/xquik-compliance.md
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/security/xquik-trust-center.md
  title: ''
  type: TrustCenter
  url: security/xquik-trust-center.md
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.xquik.com/changelog
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/rate-limits/xquik-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/xquik-rate-limits.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/lifecycle/xquik-deprecation-policy.md
  title: ''
  type: Deprecation
  url: lifecycle/xquik-deprecation-policy.md
- group: auth
  title: ''
  type: Security
  url: https://docs.xquik.com/security
- group: design
  title: ''
  type: Webhooks
  url: https://docs.xquik.com/webhooks/overview
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Xquik-dev
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/roadmap/xquik-roadmap.md
  title: ''
  type: RoadMap
  url: roadmap/xquik-roadmap.md
- group: design
  title: ''
  type: ErrorCatalog
  url: https://docs.xquik.com/guides/error-handling
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/well-known/xquik-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/xquik-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: https://xquik.com/.well-known/security.txt
- group: other
  title: ''
  type: HTTPMessageSignatures
  url: https://xquik.com/.well-known/http-message-signatures-directory
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/llms/xquik-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/xquik-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/a2a/xquik-api-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/xquik-api-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/agentic-access/xquik-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/xquik-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/rules/xquik-rules.yml
  title: ''
  type: SpectralRules
  url: rules/xquik-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/vocabulary/xquik-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/xquik-vocabulary.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/overlays/xquik-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/xquik-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/conformance/xquik-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xquik-conformance.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/asyncapi/xquik-asyncapi.yaml
  title: ''
  type: AsyncAPI
  url: asyncapi/xquik-asyncapi.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/json-ld/xquik-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/xquik-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/json-schema/xquik-webhook-event.schema.json
  title: ''
  type: JSONSchema
  url: json-schema/xquik-webhook-event.schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/json-schema/xquik-webhook-endpoint.schema.json
  title: ''
  type: JSONSchema
  url: json-schema/xquik-webhook-endpoint.schema.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/packages/xquik-packages.yml
  title: ''
  type: Packages
  url: packages/xquik-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/packages/xquik-packages.yml
  title: ''
  type: SDKs
  url: packages/xquik-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/conventions/xquik-conventions.yml
  title: ''
  type: Conventions
  url: conventions/xquik-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/conventions/xquik-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/xquik-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/errors/xquik-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/xquik-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/data-model/xquik-data-model.yml
  title: ''
  type: DataModel
  url: data-model/xquik-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/changelog/xquik-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/xquik-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/cli/xquik-cli.yml
  title: ''
  type: CLI
  url: cli/xquik-cli.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/sandbox/xquik-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/xquik-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/scopes/xquik-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/xquik-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/lifecycle/xquik-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/xquik-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/well-known/xquik-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/xquik-security.txt
created: '2026-04-14'
description: Xquik is an independent third-party X data and automation platform. It provides public data reads, connected-account write actions, monitoring, signed webhooks, exports, hosted MCP servers, OAuth 2.1, API keys, 8 SDKs, a CLI, Agent Skills, and an OpenAPI 3.1 contract. Not affiliated with X Corp.
finops:
- name: Xquik Finops
  service_category: Social Media Data
  slug: xquik-finops
image: https://xquik.com/logo-square.png
json_schemas:
- name: Xquik Webhook Endpoint
  property_count: 8
  slug: xquik-webhook-endpoint.schema
- name: Xquik Webhook Event
  property_count: 8
  slug: xquik-webhook-event.schema
jsonld:
- class_count: 18
  name: Xquik Context
  property_count: 4
  slug: xquik-context
layout: provider
mcp_servers:
- description: Xquik operates an official remote MCP server for its REST API. The manifest, the OAuth protected-resource metadata and the endpoint itself were all probed live on 2026-08-13. The endpoint answers, and
  name: Xquik MCP Server
  slug: com-xquik-mcp
- description: ''
  name: Xquik MCP Server
  slug: mcp
modified: '2026-08-13'
name: Xquik
nav: Providers
network: true
overview: 'Xquik publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Account API, API Keys API, Articles API, and 19 more. Tagged areas include social-media-data, X / Twitter, Social Listening, Data Extraction, and Automation.


  The Xquik catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Xquik''s developer surface includes authentication, documentation, API reference, getting-started guide, SDKs, CLI, sandbox, and 62 more developer resources.'
plans:
- name: Xquik Plans
  plan_count: 4
  slug: xquik-plans
random_paper: 19
rate_limits:
- limit_count: 7
  name: Xquik Rate Limits
  slug: xquik-rate-limits
rules:
- effective_rule_count: 20
  extends: []
  name: Xquik API Rules
  rule_count: 20
  severity_counts:
    error: 15
    hint: 0
    info: 2
    warn: 3
  slug: xquik-rules
scopes:
- name: Xquik Scopes
  scope_count: 1
  slug: xquik-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: exemplar
  composite: 88.7
  coverage:
    artifact_dirs: 35
    catalog_earned: 92.7
    catalog_earned_first_party: 24.0
    catalog_gap: 22.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 80.9
    contract_quality: 66.7
    developer_ergonomics: 94.0
    discoverability: 91.7
    operational_transparency: 81.6
  previous_composite: 88.7
  provenance:
    agentic_access: first-party
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 20
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/xquik-api/refs/heads/main/screenshots/xquik-api-2026-08-17T075407.png
security:
- kind: authentication
  name: Xquik Api Authentication
  slug: xquik-api-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Xquik Api Domain Security
  slug: xquik-api-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Xquik Api Vulnerability Disclosure
  slug: xquik-api-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: xquik-api
tags:
- social-media-data
- X / Twitter
- Social Listening
- Data Extraction
- Automation
- Webhook
- MCP
- Developer API
- A2A
website: https://xquik.com/en
---
