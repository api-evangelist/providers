---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.0
  scored_at: '2026-10-04'
api_count: 18
apis:
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: This endpoint collects and aggregates all activities, provided by all modules
  name: Antavo Activities API
  phrasing_intents:
  - id: getCustomersByCustomerIdActivitiesEarn
    intent: List ways a customer can earn
    question: Which ways can this member earn points right now?
  - id: getCustomersByCustomerIdActivitiesSpend
    intent: List ways a customer can spend
    question: What can a member spend their points on?
  - id: getCustomersByCustomerIdActivities
    intent: List all earn and spend activities
    question: Can I get both earn and spend activities for a customer in one call?
  phrasing_ops: 3
  slug: antavo-activities-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: The Async Events API from Antavo — 2 operation(s) for async events.
  name: Antavo Async Events API
  phrasing_intents:
  - id: getV1AsyncEventsByCorrelationId
    intent: Check an async event's processing status
    question: Has my asynchronously submitted event been processed yet?
  - id: postV1AsyncEvents
    intent: Submit an event for background processing
    question: Can I send a loyalty event without waiting for it to be processed?
  phrasing_ops: 2
  slug: antavo-async-events-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: The Authentication API API from Antavo — 1 operation(s) for authentication api.
  name: Antavo Authentication API
  phrasing_intents:
  - id: postV1AuthToken
    intent: Generate an API access token
    question: How do I get an access token for the Antavo API?
  phrasing_ops: 1
  slug: antavo-authentication-api-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: Cart endpoints collection
  name: Antavo Cart API
  phrasing_intents:
  - id: postV1CartFinalize
    intent: Finalize a checkout with promotions
    question: How do I complete a checkout with the final promotions applied?
  - id: postV1Cart
    intent: Preview promotions for a cart
    question: Which promotions would apply to this cart before checkout?
  phrasing_ops: 2
  slug: antavo-cart-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: Endpoints provided by the _Challenges_ module
  name: Antavo Challenges API
  phrasing_intents:
  - id: getCustomersByCustomerIdActivitiesChallenges
    intent: List open challenges for a customer
    question: Which challenges can a member still complete?
  - id: getCustomersByCustomerIdChallenges
    intent: List a customer's completed challenges
    question: Which challenges has a member already completed?
  - id: getV2CustomersByCustomerIdActivitiesChallenges
    intent: Filter available challenges for a customer
    question: Can I filter a customer's available challenges by tag or points?
  - id: getV2CustomersByCustomerIdChallenges
    intent: Filter a customer's completed challenges by date
    question: Can I see challenges a member completed within a date range?
  phrasing_ops: 4
  slug: antavo-challenges-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: The Clubs API from Antavo — 21 operation(s) for clubs.
  name: Antavo Clubs API
  phrasing_intents:
  - id: getV1ClubsByClubIdHistory
    intent: Show a club's action history
    question: What actions have happened in a club over time?
  - id: getV1ClubsByClubIdMembersByCustomerId
    intent: Get one club member's details
    question: What role, balance and spending limit does a specific club member have?
  - id: getV1ClubsByClubIdMembers
    intent: List a club's members
    question: Who belongs to a given club?
  - id: getV1ClubsByClubIdPointExpiry
    intent: List a club's expiring points by date
    question: Which club points will expire within a date range?
  - id: getV1ClubsByClubId
    intent: Get a club's details
    question: What are the details of one particular club?
  - id: getV1ClubsTemplates
    intent: List club templates
    question: Which club templates are configured?
  - id: getV1Clubs
    intent: List clubs
    question: Which clubs exist in my loyalty program?
  - id: postV1Clubs
    intent: Create a club
    question: Can I create a new club for members to join?
  phrasing_ops: 22
  slug: antavo-clubs-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: The Content consumption API from Antavo — 1 operation(s) for content consumption.
  name: Antavo Content consumption API
  phrasing_intents:
  - id: getCustomersByCustomerIdActivitiesContentConsumption
    intent: List content consumption activities
    question: Which content consumption activities can a member complete?
  phrasing_ops: 1
  slug: antavo-content-consumption-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: Endpoints provided by the _Contests Lite_ module
  name: Antavo Contests API
  phrasing_intents:
  - id: getCustomersByCustomerIdActivitiesContests
    intent: List contests open to a customer
    question: Which contests can a member enter right now?
  - id: postCustomersByCustomerIdActivitiesContestsByContestIdEnter
    intent: Enter a customer into a contest
    question: Can a customer submit more than one entry into a contest?
  phrasing_ops: 2
  slug: antavo-contests-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: The Coupon pools API from Antavo — 2 operation(s) for coupon pools.
  name: Antavo Coupon pools API
  phrasing_intents:
  - id: postV1CouponPoolsByCouponPoolIdUpdate
    intent: Update a coupon pool
    question: Can I change the value or expiration of an existing coupon pool?
  - id: postV1CouponPools
    intent: Create a coupon pool
    question: Can I set up a new pool of coupons with a fixed discount value?
  phrasing_ops: 2
  slug: antavo-coupon-pools-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: Bulk Coupons API endpoints
  name: Antavo Coupons API
  phrasing_intents:
  - id: getV1BulkOperationCouponsByBatchIdStatusError
    intent: List errors from a coupon import
    question: Which coupon codes failed during my coupon import?
  - id: getV1BulkOperationCouponsByBatchIdStatus
    intent: Check the status of a coupon import
    question: Is my coupon batch import queued, processing or done?
  - id: postV1BulkOperationCouponsByCouponPoolIdByAction
    intent: Upload or assign coupons in a pool in bulk
    question: Can I upload a batch of coupon codes into a coupon pool?
  - id: Coupons
    intent: Search coupons across all customers
    question: How do I look up a coupon by its code without knowing which customer has it?
  - id: getCustomersByCustomerIdCoupons
    intent: Filter coupons assigned to a customer
    question: Does a member hold a coupon with a particular code?
  - id: listCustomerCoupons
    intent: List a customer's coupons
    question: What coupons does a specific loyalty member hold?
  phrasing_ops: 6
  slug: antavo-coupons-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: Bulk Customer List API endpoints
  name: Antavo Customer lists API
  phrasing_intents:
  - id: getV1BulkOperationCustomerListByBatchIdStatusErrors
    intent: List errors from a customer list operation
    question: Which customers failed to be added to or removed from a list?
  - id: getV1BulkOperationCustomerListByBatchIdStatus
    intent: Check a customer list operation's status
    question: Has my customer list update finished processing?
  - id: postV1BulkOperationCustomerListAddByCustomerListId
    intent: Add customers to a list in bulk
    question: Can I add many customers to a customer list at once?
  - id: postV1BulkOperationCustomerListRemoveByCustomerListId
    intent: Remove customers from a list in bulk
    question: Can I remove a batch of customers from a list?
  - id: deleteEntitiesCoreCustomerListByEntityId
    intent: Archive a customer list
    question: Can I archive a customer list I no longer use?
  - id: getEntitiesCoreCustomerListByEntityId
    intent: Get a customer list
    question: What are the details of a specific customer list?
  - id: postEntitiesCoreCustomerListByEntityId
    intent: Update a customer list
    question: Can I rename a customer list or change its status?
  - id: getEntitiesCoreCustomerList
    intent: List all customer lists
    question: Which customer lists exist in my program?
  phrasing_ops: 9
  slug: antavo-customer-lists-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: The Customers API from Antavo — 11 operation(s) for customers.
  name: Antavo Customers API
  phrasing_intents:
  - id: getCustomersCount
    intent: Count active customers
    question: How many active members are in my loyalty program?
  - id: getCustomersByCustomerId
    intent: Fetch a customer with selected fields
    question: Can I limit which profile fields come back when fetching one customer?
  - id: getCustomers
    intent: Search customers to find their Antavo ID
    question: Can I find a customer's Antavo ID by searching on their email?
  - id: postCustomersByCustomerIdMerge
    intent: Merge a customer into another account
    question: Can I merge a duplicate loyalty account into another one?
  - id: getCustomersVerify
    intent: Verify a customer's registration
    question: What activates a new member's account after they register?
  - id: postCustomersByCustomerIdOptIn
    intent: Register a customer with login credentials
    question: Can a customer self-register with a password for the loyalty program?
  - id: postCustomersLogin
    intent: Log a customer in
    question: Can I authenticate a loyalty member with a username and password?
  - id: postCustomersPasswordRequest
    intent: Send a password reset request
    question: What lets a member who forgot their password get a reset link?
  phrasing_ops: 11
  slug: antavo-customers-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: Endpoints for probing data extensions
  name: Antavo Data extensions API
  phrasing_intents:
  - id: getCustomersByCustomerIdDataByDataExtension
    intent: Read a customer's data extension
    question: Can I read the custom data stored for a customer in a data extension?
  phrasing_ops: 1
  slug: antavo-data-extensions-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: The Events API from Antavo — 3 operation(s) for events.
  name: Antavo Events API
  phrasing_intents:
  - id: bulk
    intent: Submit many loyalty events in one request
    question: How do I send a batch of customer events in a single call instead of one at a time?
  - id: events
    intent: Submit a single loyalty event for a customer
    question: How do I record one checkout or point_add event for a customer?
  - id: listCustomerEvents
    intent: List a customer's event history
    question: What events are in a customer's loyalty history?
  phrasing_ops: 3
  slug: antavo-events-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: The FAQ API from Antavo — 1 operation(s) for faq.
  name: Antavo FAQ API
  phrasing_intents:
  - id: getFaq
    intent: List FAQ entries
    question: Can I pull the FAQ questions and answers configured for the loyalty program?
  phrasing_ops: 1
  slug: antavo-faq-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: A general method for creating, accessing and modifying an Antavo entity.
  name: Antavo Generic API
  phrasing_intents:
  - id: Entitydelete
    intent: Archive a deactivated entity item
    question: Can I archive an inactive item from any entity module so it disappears from the Management UI?
  - id: entityget
    intent: Retrieve any entity item by its ID
    question: How do I fetch a single item from any Antavo entity module, including custom entities?
  - id: entityupdate
    intent: Update attributes on an existing entity item
    question: How do I change an attribute on an existing item in a generic or custom entity module?
  - id: Genericspeccreate
    intent: Create an entity item with an ID you choose
    question: Can I create a generic entity item and assign my own ID to it instead of letting the system pick one?
  - id: getEntitiesByModuleByEntity
    intent: List all items of an entity type
    question: Can I list every item in a custom entity module?
  - id: Genericcreate
    intent: Create an entity item with a system-assigned ID
    question: How do I add a new item to an entity module without specifying an ID myself?
  - id: postEntities
    intent: Submit entity changes in bulk
    question: Can I send many entity calls in a single request?
  phrasing_ops: 7
  slug: antavo-generic-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: Endpoints providing information regarding the customers interactions with the loyalty cloud
  name: Antavo History API
  phrasing_intents:
  - id: getCustomersByCustomerIdEvents
    intent: List one customer's event history
    question: What has a specific member done in the loyalty program?
  - id: getCustomersEvents
    intent: List events for all customers by time
    question: Can I pull every event across all customers in a time window?
  phrasing_ops: 2
  slug: antavo-history-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: The Leaderboard API from Antavo — 1 operation(s) for leaderboard.
  name: Antavo Leaderboard API
  phrasing_intents:
  - id: getCustomersLeaderboard
    intent: Show the customer leaderboard
    question: Who are the top-performing members in my loyalty program?
  phrasing_ops: 1
  slug: antavo-leaderboard-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: Endpoints provided by the _Offers_ module
  name: Antavo Offers API
  phrasing_intents:
  - id: getCustomersByCustomerIdActivitiesOffers
    intent: List offers available to a customer
    question: Which offers are available to a specific member?
  - id: postCustomersByCustomerIdActivitiesOffersByOfferIdClaim
    intent: Claim an offer for a customer
    question: Can I claim an offer on a customer's behalf?
  - id: postOffers
    intent: Get offers for a cart's products
    question: Which product offers apply to what's in a customer's cart?
  phrasing_ops: 3
  slug: antavo-offers-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: The Points Preview API API from Antavo — 1 operation(s) for points preview api.
  name: Antavo Points Preview API
  phrasing_intents:
  - id: postExtensionsAutomationCampaignBonus
    intent: Preview points for a purchase
    question: How many bonus points would a purchase earn before checkout?
  phrasing_ops: 1
  slug: antavo-points-preview-api-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: The Prize wheels API from Antavo — 2 operation(s) for prize wheels.
  name: Antavo Prize wheels API
  phrasing_intents:
  - id: getCustomersByCustomerIdPrizeWheelsByPwId
    intent: Show a prize wheel's slices
    question: What prizes are on each slice of a prize wheel?
  - id: postCustomersByCustomerIdPrizeWheelsByPwId
    intent: Spin a prize wheel for a customer
    question: Can a member spin a prize wheel through the API?
  - id: getCustomersByCustomerIdPrizeWheels
    intent: List prize wheels for a customer
    question: Which prize wheels can a customer play?
  phrasing_ops: 3
  slug: antavo-prize-wheels-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: Endpoints provided by the _Gamified Profiling_ module
  name: Antavo Profiling API
  phrasing_intents:
  - id: getCustomersByCustomerIdActivitiesProfilingByFlowIdNext
    intent: Get the next profiling question
    question: What's the next profiling question a member should answer?
  - id: getCustomersByCustomerIdActivitiesProfiling
    intent: List profiling flows for a customer
    question: Which profiling flows can a customer complete?
  - id: postCustomersByCustomerIdActivitiesProfilingByFlowIdQuestionsByQuestionId
    intent: Answer a profiling question
    question: Can I submit a customer's answer to a profiling question?
  phrasing_ops: 3
  slug: antavo-profiling-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: Promotion endpoints collection
  name: Antavo Promotion API
  phrasing_intents:
  - id: getV1PromotionByPromotionId
    intent: Get a promotion
    question: What are the settings of one promotion?
  - id: getV1Promotions
    intent: List promotions
    question: Which promotions are configured in my workspace?
  - id: postV1PromotionByPromotionIdStatus
    intent: Change a promotion's status
    question: Can I activate a draft promotion or send it back to draft?
  phrasing_ops: 3
  slug: antavo-promotion-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: Endpoints provided by the _Quizzes_ module
  name: Antavo Quizzes API
  phrasing_intents:
  - id: getCustomersByCustomerIdActivitiesQuizzesByQuizId
    intent: Get a quiz's details
    question: What are the questions and settings of a specific quiz?
  - id: getCustomersByCustomerIdActivitiesQuizzes
    intent: List quizzes for a customer
    question: Which quizzes can a member answer?
  - id: postCustomersByCustomerIdActivitiesQuizzesByQuizIdEarn
    intent: Submit a quiz answer
    question: How do I submit a member's quiz answer?
  phrasing_ops: 3
  slug: antavo-quizzes-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: Bulk Reward Claim API endpoints
  name: Antavo Rewards API
  phrasing_intents:
  - id: getV1BulkOperationRewardClaimByBatchIdStatusError
    intent: List errors from a bulk reward claim
    question: Which customers failed to get the reward in my bulk claim batch?
  - id: getV1BulkOperationRewardClaimByBatchIdStatus
    intent: Check the status of a bulk reward claim
    question: Is my bulk reward claim batch still processing or already done?
  - id: postV1BulkOperationRewardClaimByRewardId
    intent: Claim one reward for many customers
    question: Can I give one reward to thousands of customers at once?
  - id: getCustomersByCustomerIdActivitiesRewardsByRewardId
    intent: Show one reward available to a customer
    question: Can I see the details of a specific reward as a particular member would see it?
  - id: getCustomersByCustomerIdActivitiesRewards
    intent: List rewards a customer can claim
    question: Which rewards can this loyalty member redeem right now?
  - id: getCustomersByCustomerIdRewards
    intent: List a customer's claimed rewards
    question: What rewards has this member already claimed?
  - id: postCustomersByCustomerIdActivitiesRewardsByRewardIdBid
    intent: Bid on an auction reward for a customer
    question: Can a member place a bid on an auction-style reward?
  - id: postCustomersByCustomerIdActivitiesRewardsByRewardIdClaim
    intent: Claim a reward for a customer
    question: How do I redeem a reward on behalf of a loyalty member?
  phrasing_ops: 17
  slug: antavo-rewards-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: The Social Share Campaigns API from Antavo — 1 operation(s) for social share campaigns.
  name: Antavo Social Share Campaigns API
  phrasing_intents:
  - id: postV1SocialShareCampaignsShareIntent
    intent: Register a social share intent
    question: Can I record that a member intends to share a campaign link on social media?
  phrasing_ops: 1
  slug: antavo-social-share-campaigns-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: Endpoints providing customer information regarding specified transaction ids.
  name: Antavo Transactions API
  phrasing_intents:
  - id: getCustomersByCustomerIdTransactionsSearch
    intent: Search a customer's transactions by status
    question: Can I find a member's transactions that are in a particular status?
  - id: postCustomersByCustomerIdTransactionsSearch
    intent: Bulk-search a customer's transactions
    question: Can I search a customer's transactions for many IDs at once in a request body?
  - id: getCustomersByCustomerIdTransactionsByTransactionIdEvents
    intent: List the events of one transaction
    question: Which checkout and update events make up a single transaction?
  - id: getCustomersByCustomerIdTransactionsByTransactionId
    intent: Retrieve one customer transaction
    question: Can I get the full breakdown of one specific purchase for a member?
  - id: getCustomersByCustomerIdTransactions
    intent: Get a customer's transaction history (legacy)
    question: Where do I find the event ID that created a given transaction?
  - id: listCustomerTransactions
    intent: List a customer's purchase transactions
    question: How do I see a member's transactions with their items and points earned?
  phrasing_ops: 6
  slug: antavo-transactions-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: The Treasure hunt API from Antavo — 1 operation(s) for treasure hunt.
  name: Antavo Treasure hunt API
  phrasing_intents:
  - id: getCustomersByCustomerIdActivitiesTreasureHunt
    intent: List treasure hunts for a customer
    question: Which online treasure hunts can a member join?
  phrasing_ops: 1
  slug: antavo-treasure-hunt-api
- baseURL: https://api.antavo.com
  baseurl_source: declared
  description: Endpoints provided by the _Wallet_ module
  name: Antavo Wallet API
  phrasing_intents:
  - id: getCustomersByCustomerIdWallet
    intent: Get a customer's wallet pass links
    question: Can I get download links for a member's wallet passes?
  phrasing_ops: 1
  slug: antavo-wallet-api
artifact_total: 55
asyncapis:
- description: ''
  name: Antavo Webhooks
  slug: antavo-webhooks
collections:
- collection_type: open
  name: Antavo Async Events API
  slug: open-antavo-async-events
- collection_type: open
  name: Antavo Authentication API
  slug: open-antavo-authentication
- collection_type: open
  name: Antavo Bulk Operations API
  slug: open-antavo-bulk-operations
- collection_type: open
  name: Antavo Clubs API
  slug: open-antavo-clubs
- collection_type: open
  name: Antavo Coupon Pools API
  slug: open-antavo-coupon-pools
- collection_type: open
  name: Antavo Coupons API
  slug: open-antavo-coupons
- collection_type: open
  name: Antavo Customers API
  slug: open-antavo-customer
- collection_type: open
  name: Antavo Display API
  slug: open-antavo-display
- collection_type: open
  name: Antavo Entities API
  slug: open-antavo-entities
- collection_type: open
  name: Antavo Events API
  slug: open-antavo-events
- collection_type: open
  name: Antavo FAQ API
  slug: open-antavo-faq
- collection_type: open
  name: Antavo Leaderboard API
  slug: open-antavo-leaderboard
- collection_type: open
  name: Antavo Loyalty Read API
  slug: open-antavo-loyalty-read
- collection_type: open
  name: Antavo Offers API
  slug: open-antavo-offers
- collection_type: open
  name: Antavo Promotion Engine API
  slug: open-antavo-promotion-engine
- collection_type: open
  name: Antavo Rewards API
  slug: open-antavo-rewards
- collection_type: open
  name: Antavo Socal Share Campaigns API
  slug: open-antavo-social-share-campaigns
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/capabilities/antavo-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/antavo-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/overlays/antavo-events-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/antavo-events-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/overlays/antavo-async-events-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/antavo-async-events-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/overlays/antavo-customer-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/antavo-customer-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/overlays/antavo-display-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/antavo-display-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/overlays/antavo-entities-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/antavo-entities-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/overlays/antavo-rewards-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/antavo-rewards-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/overlays/antavo-coupons-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/antavo-coupons-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/overlays/antavo-coupon-pools-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/antavo-coupon-pools-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/overlays/antavo-offers-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/antavo-offers-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/overlays/antavo-points-preview-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/antavo-points-preview-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/overlays/antavo-leaderboard-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/antavo-leaderboard-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/overlays/antavo-bulk-operations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/antavo-bulk-operations-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/overlays/antavo-clubs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/antavo-clubs-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/overlays/antavo-promotion-engine-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/antavo-promotion-engine-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/overlays/antavo-authentication-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/antavo-authentication-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/overlays/antavo-faq-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/antavo-faq-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/overlays/antavo-loyalty-read-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/antavo-loyalty-read-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/overlays/antavo-social-share-campaigns-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/antavo-social-share-campaigns-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/authentication/antavo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/antavo-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/security/antavo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/antavo-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/antavo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/antavo
- group: company
  title: ''
  type: Website
  url: https://antavo.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.antavo.com/docs/antavo-apis
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/plans/antavo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/antavo-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/rate-limits/antavo-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/antavo-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/finops/antavo-finops.yml
  title: ''
  type: FinOps
  url: finops/antavo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://antavo.com/blog/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.antavo.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.antavo.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.antavo.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://antavo.atlassian.net/servicedesk/customer/portals
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.antavo.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://antavo.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://antavo.com/legals/privacy/
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/31303107/2sAYdmkTFm
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/llms/antavo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/antavo-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/packages/antavo-packages.yml
  title: ''
  type: Packages
  url: packages/antavo-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/packages/antavo-packages.yml
  title: ''
  type: SDKs
  url: packages/antavo-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/conventions/antavo-conventions.yml
  title: ''
  type: Conventions
  url: conventions/antavo-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/lifecycle/antavo-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/antavo-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://antavo.com/status/
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.antavo.com/changelog
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/changelog/antavo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/antavo-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/scopes/antavo-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/antavo-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/conformance/antavo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/antavo-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://antavo.com/product/loyalty-engine/technology/security/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/security/antavo-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/antavo-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/security/antavo-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/antavo-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/errors/antavo-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/antavo-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/data-model/antavo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/antavo-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/sandbox/antavo-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/antavo-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/asyncapi/antavo-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/antavo-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/skills/antavo-submit-loyalty-event.md
  title: ''
  type: AgentSkill
  url: skills/antavo-submit-loyalty-event.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/skills/antavo-async-event-ingestion.md
  title: ''
  type: AgentSkill
  url: skills/antavo-async-event-ingestion.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/skills/antavo-member-experience-and-reward-claim.md
  title: ''
  type: AgentSkill
  url: skills/antavo-member-experience-and-reward-claim.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/skills/antavo-cart-promotions-and-points-preview.md
  title: ''
  type: AgentSkill
  url: skills/antavo-cart-promotions-and-points-preview.md
created: '2026-07-10'
description: Antavo is an enterprise loyalty management platform - the Antavo AI Loyalty Cloud - that lets brands build and run omnichannel, multi-brand, multi-country loyalty programs. Its API-first, headless Loyalty Engine exposes a comprehensive REST API covering customer events, customer profiles, the headless Display surface for loyalty experiences, configurable entities (rewards, challenges, stores, products, transactions), coupons, offers, leaderboards, clubs, promotions, and bulk operations. Requests use standard HTTP verbs with JSON, secured by API key/secret with optional request signing, IP filtering, and token-based auth. API access is provisioned per Antavo environment for enterprise customers, while the developer documentation is fully public.
finops:
- name: Antavo Finops
  service_category: Marketing and Customer Loyalty
  slug: antavo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/antavo.png
layout: provider
modified: '2026-08-13'
name: Antavo
nav: Providers
network: true
overview: 'Antavo publishes 29 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Async Events API, Authentication API, and 26 more. Tagged areas include Loyalty, Customer Loyalty, Rewards, Enterprise, and Headless.


  The Antavo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Antavo''s developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, support, pricing, and 52 more developer resources.'
plans:
- name: Antavo Plans Pricing
  plan_count: 2
  slug: antavo-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Antavo Rate Limits
  slug: antavo-rate-limits
scopes:
- name: Antavo Scopes
  scope_count: 1
  slug: antavo-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: exemplar
  composite: 66.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 63.0
    catalog_earned_first_party: 20.0
    catalog_gap: 52.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 57.0
    developer_ergonomics: 67.3
    discoverability: 78.6
    operational_transparency: 77.6
  previous_composite: 66.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 29
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/screenshots/antavo-2026-07-25T200404.png
security:
- kind: authentication
  name: Antavo Authentication
  slug: antavo-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Antavo Domain Security
  slug: antavo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Antavo Vulnerability Disclosure
  slug: antavo-vulnerability-disclosure
  summary_line: security.txt
- kind: trust-center
  name: Antavo Trust Center
  slug: antavo-trust-center
  summary_line: ISO 27001, ISO 27017, ISO 27018, GDPR / UK GDPR
slug: antavo
tags:
- Loyalty
- Customer Loyalty
- Rewards
- Enterprise
- Headless
- Retail
- Marketing
- Engagement
- Promotions
- Gamification
- Event
- E-Commerce
- Coupons
- Points
- Membership
- Loyalty & Incentives
website: https://antavo.com
---
