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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 63.3
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 127
  human_in_the_loop: 0
  name: Birdeye Agentic Access
  operation_count: 162
  slug: birdeye-agentic-access
  summary_line: 162 operations · 127 acting
api_count: 2
apis:
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Access your public data from 150+ review sites.
  name: Birdeye Aggregation API
  phrasing_intents:
  - id: get-all-aggregation-source
    intent: List a business's review aggregation sources
    question: Which review site URLs is Birdeye aggregating reviews from for my location?
  - id: getV1SurveyReviewsitesAlias
    intent: List review site aliases for a business
    question: What source alias names can I use when adding a review site URL?
  - id: add-aggregation-url
    intent: Add a review site URL to aggregate
    question: Can I add a review site page URL so its reviews get aggregated for my business?
  - id: delete-aggregation-url
    intent: Remove a review aggregation URL
    question: Can I stop aggregating reviews from a site I added by mistake?
  phrasing_ops: 4
  slug: birdeye-aggregation-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Create and maintain your business on Birdeye.
  name: Birdeye Business API
  phrasing_intents:
  - id: create-a-business
    intent: Create a business under a reseller
    question: Can a reseller create a new sub-account business through the API?
  - id: search-business
    intent: Search businesses under an account
    question: How do I search the businesses under my account by name?
  - id: get-business
    intent: Get a business profile
    question: What profile details does Birdeye hold for one of my businesses?
  - id: update-business
    intent: Update a business profile
    question: Can I change a location's hours of operation and website through the API?
  - id: delete-business
    intent: Delete a business
    question: Can I permanently delete a business from my account?
  - id: update-the-status
    intent: Set a business active or inactive
    question: Can I mark a business inactive without deleting it?
  - id: get-child-businesses
    intent: List child businesses of a parent account
    question: Which child businesses sit under my reseller or enterprise account?
  - id: update-public-profile-of-businesses
    intent: Choose the tabs on a public profile
    question: Can I choose which tabs appear on a business's public profile page?
  phrasing_ops: 15
  slug: birdeye-business-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: 'Add, delete and manage business media. Supported Media Size Photo: JPG or PNG. 720 x 720px. 10KB min. Video: 30 sec long. 720p or more upto 75MB. Note Uploaded media will be pushed to your google busi'
  name: Birdeye Business Media API
  phrasing_intents:
  - id: add-media
    intent: Upload media to a location
    question: Can I upload photos to a location's business profile media?
  - id: get-media
    intent: List a location's media
    question: Which photos and media are currently attached to my location?
  - id: update-media
    intent: Change a media item's category
    question: Can I recategorize a media item already uploaded to a location?
  - id: delete-media
    intent: Delete media from a location
    question: Can I delete media from a location's profile?
  phrasing_ops: 4
  slug: birdeye-business-media-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Create a short link for review requests and set review sources in the template.
  name: Birdeye Campaign API
  phrasing_intents:
  - id: fetch-request-url
    intent: Get a review request link for a customer
    question: Can I generate a review request link for a specific customer?
  - id: set-defaullt-review-sources
    intent: Apply default review sources to a customer
    question: Can I set the default review sources a customer is asked to review on?
  phrasing_ops: 2
  slug: birdeye-campaign-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Competitive intelligence, simplified by AI.
  name: Birdeye Competitor AI API
  phrasing_intents:
  - id: retrieve-competitor-reviews
    intent: Retrieve competitors' reviews
    question: Can I pull the actual reviews my competitors received over a date range?
  - id: retrieve-competitor-review-metrics
    intent: Get competitor review metrics
    question: What are my competitors' review counts and average ratings?
  phrasing_ops: 2
  slug: birdeye-competitor-ai-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Make competitive insights your unfair advantage.
  name: Birdeye Competitor API
  phrasing_intents:
  - id: get-competitor-business
    intent: List an enterprise's competitor businesses
    question: Which competitor businesses are tracked for my enterprise?
  - id: get-competitor-child-business
    intent: List a competitor enterprise's locations
    question: Can I list the child locations under a competitor enterprise?
  - id: get-business-competitors
    intent: List competitors for one location
    question: Who are the competitors configured for a single location?
  - id: create-new-competitor-enterprise
    intent: Add a competitor to track
    question: Can I add a new competitor to track for my account?
  - id: create-new-child-business-in-competitor-enterprise
    intent: Add a location to a competitor enterprise
    question: Can I add another location to a competitor I already track?
  - id: add-new-competitor-aggregation-url
    intent: Add a review source URL for a competitor
    question: Can I point Birdeye at a competitor's review site page to collect their reviews?
  - id: get-competitor-reviews
    intent: Get a competitor enterprise's reviews
    question: Can I read a competitor enterprise's reviews filtered by rating and source?
  - id: get-score
    intent: Get competitive category scores
    question: What is my competitive insight score by category compared with competitors?
  phrasing_ops: 10
  slug: birdeye-competitor-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Manage contacts across locations effortlessly with a robust Contact Management System.
  name: Birdeye Contact API
  phrasing_intents:
  - id: create-or-update-contact
    intent: Create or update a contact
    question: Can I add a new contact or update an existing one in a single call?
  - id: get-contact
    intent: Look up a contact
    question: Can I look up a contact by email or phone number?
  - id: delete-contact
    intent: Delete a contact from locations
    question: Can I delete a contact from one or more locations?
  - id: customer-checkin
    intent: Record a customer check-in
    question: Can I record a customer check-in at a location with their name and phone?
  - id: customer-activity-log
    intent: Get a customer's activity history
    question: Can I see a customer's activity history for a date range?
  - id: customer-delete
    intent: Delete an enterprise customer by ID
    question: Can I delete an enterprise customer record by its customer ID?
  - id: subscribe-unsubscribe-customer
    intent: Subscribe or unsubscribe a customer
    question: Can I unsubscribe a customer from messages by email or phone?
  - id: contact
    intent: List a business's contacts
    question: Can I page through all contacts of a business sorted my way?
  phrasing_ops: 11
  slug: birdeye-contact-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Easily manage contacts across multiple locations using enhanced Contact APIs, featuring built-in support for communication preference flags.
  name: Birdeye Contact V2 API
  phrasing_intents:
  - id: upsert-contact
    intent: Upsert a contact with preferences
    question: Can I save a contact along with their per-channel email and SMS preferences?
  - id: retrieve-contact
    intent: Retrieve a contact with preferences
    question: Can I fetch a contact and their communication preferences by phone?
  - id: customer-checkin
    intent: Check in a customer with preferences
    question: Can I check in a visitor and set their email and SMS preferences at the same time?
  - id: update-communication-preferences
    intent: Update a contact's messaging preferences
    question: Can I change which email and SMS messages a contact receives?
  - id: retrieve-opted-out-contacts
    intent: List contacts who opted out
    question: Which contacts opted out of messages between two dates?
  phrasing_ops: 5
  slug: birdeye-contact-v2-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Connect with customers across a range of digital channels from one unified inbox.
  name: Birdeye Conversation API
  phrasing_intents:
  - id: list-conversations
    intent: Export messenger conversations
    question: Can I export messenger conversations for a location over a date range?
  phrasing_ops: 1
  slug: birdeye-conversation-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Create, delete , update , associate and get custom fields easily.
  name: Birdeye Custom Fields API
  phrasing_intents:
  - id: create
    intent: Create a custom field
    question: Can I define a new custom field such as a dropdown for my locations?
  - id: update
    intent: Update a custom field definition
    question: Can I change the dropdown options or default value of an existing custom field?
  - id: get
    intent: Get one custom field for a location
    question: What's the definition and value of one custom field for a location?
  - id: post
    intent: List custom fields for a location
    question: Which custom fields exist for a location?
  - id: delete
    intent: Delete a custom field
    question: Can I delete a custom field I no longer use?
  - id: associate
    intent: Set a custom field value on a location
    question: Can I set a custom field's value on a specific location?
  - id: create-custom-card
    intent: Create a profile custom card
    question: Can I add a new custom card with an image and link to a business profile?
  phrasing_ops: 7
  slug: birdeye-custom-fields-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: The Employee API from Birdeye — 1 operation(s) for employee.
  name: Birdeye Employee API
  phrasing_intents:
  - id: get-details-of-employees
    intent: List a business's employees
    question: Which employees are set up for a business?
  phrasing_ops: 1
  slug: birdeye-employee-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: To retrieve all Question and Answer (QnA) entries across locations using FAQ APIs, enabling smart support and knowledge features for businesses.
  name: Birdeye FAQ API
  phrasing_intents:
  - id: get-all-qna
    intent: List FAQ questions and answers
    question: Can I pull all FAQ questions and answers across my locations?
  phrasing_ops: 1
  slug: birdeye-faq-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: To manage products, locations, and business details through Listing GMB platform
  name: Birdeye GMB Products API
  phrasing_intents:
  - id: onboard-google-merchant-account
    intent: Connect a Google Merchant Center account
    question: Can I connect my Google Merchant Center account to manage product listings?
  - id: create-product-listing
    intent: Create a product listing
    question: Can I create a product listing with a price and image for my Google profile?
  - id: update-product-listing
    intent: Update a product listing
    question: Can I change the price or sale price of an existing product listing?
  - id: get-product-listing
    intent: Get one product listing
    question: Can I fetch one product listing by its identifier?
  - id: delete-product-listings
    intent: Delete product listings
    question: Can I delete several product listings at once?
  - id: get-list-product-listing
    intent: List product listings
    question: Which products are listed for my locations?
  - id: add-products-on-a-location
    intent: Add existing products to a location
    question: Can I publish existing products to a location?
  - id: remove-products-on-a-location
    intent: Remove products from a location
    question: Can I take products off a location without deleting them from the catalog?
  phrasing_ops: 8
  slug: birdeye-gmb-products-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Note Applicable to be used only by paid listings clients, for their active locations, for the Google Q&A section, in the Google listing
  name: Birdeye Google Q&A API
  phrasing_intents:
  - id: create-question
    intent: Post a question and answer
    question: Can I post a question and its answer to my Google profile Q&A?
  - id: create-answer
    intent: Answer an existing question
    question: Can I answer a question someone already asked on my Google profile?
  - id: update-question
    intent: Edit a posted question
    question: Can I edit the wording of a question I posted?
  - id: update-answer
    intent: Edit a posted answer
    question: Can I edit an answer already posted to a question?
  - id: delete-question
    intent: Delete a question
    question: Can I delete a single question from my Google Q&A?
  - id: delete-answer
    intent: Delete an answer
    question: Can I delete one answer but keep the question?
  - id: delete-all-questions-and-answers
    intent: Delete all Q&A for a business
    question: Can I wipe every question and answer from a location at once?
  - id: get-all-questions-and-answers
    intent: List all questions and answers
    question: Can I list all Q&A on my Google profile?
  phrasing_ops: 9
  slug: birdeye-google-q-a-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Note Applicable to be used only by paid listings clients, for their active locations, for the Google Services section, in the Google listing. No two services should have the same service name. It is r
  name: Birdeye Google Services API
  phrasing_intents:
  - id: create-service
    intent: Create a service offering
    question: Can I add a service with a price and duration to my Google profile?
  - id: get-all-services
    intent: List service offerings
    question: Which services are listed on my Google profile?
  - id: update-service
    intent: Update a service offering
    question: Can I change the price or description of an existing service?
  - id: delete-services
    intent: Delete service offerings
    question: Can I delete several services at once?
  - id: get-location-mapping
    intent: Get service-to-category location mapping
    question: Which services are mapped to which categories across my locations?
  - id: update-location-mapping
    intent: Map a service to a category
    question: Can I map a service to a category across all locations?
  phrasing_ops: 6
  slug: birdeye-google-services-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Insight intelligence, simplified by AI.
  name: Birdeye Insight AI API
  phrasing_intents:
  - id: get-insight-experience-score-benchmark
    intent: Benchmark experience scores
    question: What is my experience score benchmark for a set of locations?
  - id: get-insight-experience-location-info
    intent: Get experience insights per location
    question: Can I see experience insights broken down per location?
  - id: getInsightExperienceOverTime
    intent: Trend experience scores over time
    question: How has my experience score trended week over week?
  phrasing_ops: 3
  slug: birdeye-insight-ai-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Birdeye integrates with various software or tools you use.
  name: Birdeye Integration API
  phrasing_intents:
  - id: add-locations
    intent: Map locations to an integration
    question: Can I map locations to an integration group?
  phrasing_ops: 1
  slug: birdeye-integration-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Keep your business information accurate and consistent across 50+ websites.
  name: Birdeye Listing API
  phrasing_intents:
  - id: fix-listing
    intent: Trigger a listing fix for a business
    question: Can I trigger a fix for a location's inaccurate listings?
  - id: get-location-status-report
    intent: Get a location's listing status report
    question: What is the listing status on each site for my location?
  - id: listings-insights
    intent: Get listing insights
    question: Can I get listing insights for my locations over a date range?
  - id: listings-insights-datapoints
    intent: Get datapoints for a listing report type
    question: Can I get datapoints for one listing report type, like search views or customer actions?
  - id: get-gmb-attributes
    intent: List Google Business Profile attributes
    question: Which Google Business Profile attributes apply to my category?
  - id: get-apple-attributes
    intent: List Apple location attributes
    question: Which Apple location attributes can I set on my listing?
  - id: get-apple-action-links
    intent: List Apple action links
    question: What Apple action links can be added to my location?
  - id: get-category-list
    intent: List business categories for a listing source
    question: Which business categories can I choose on a given listing site?
  phrasing_ops: 16
  slug: birdeye-listing-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Various reporting data points across Birdeye modules like reviews, insights and competitors etc for all your data visualisation
  name: Birdeye Report API
  phrasing_intents:
  - id: get-dashboard-data
    intent: Get small-business dashboard data
    question: Can I get the summary dashboard numbers for a small business?
  - id: get-review-conversion-report
    intent: Get the review request conversion report
    question: What is my review request conversion rate for recent days or months?
  - id: review-and-rating-over-time-report
    intent: Trend review count and rating over time
    question: How have my review count and average rating changed over time?
  - id: reviews-rating-by-location-report
    intent: Compare reviews and rating by location
    question: Which locations have the most reviews and highest ratings?
  - id: review-count-rating
    intent: Count reviews by star rating
    question: How many reviews did I get at each star rating?
  - id: review-count-rating-by-employee
    intent: Count reviews and ratings by employee
    question: How many reviews and what ratings does each employee have?
  - id: insights-category-report-by-location-report
    intent: Get review insight categories by location
    question: How do my locations compare on insight categories from review content?
  - id: competitive-ranking-report
    intent: Get the competitive ranking report
    question: Where do I rank against competitors on reviews?
  phrasing_ops: 17
  slug: birdeye-report-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Consistently generate more reviews and higher ratings.
  name: Birdeye Reviews API
  phrasing_intents:
  - id: get-reviews
    intent: Get reviews for a business
    question: Can I pull reviews for a business filtered by date, rating and source?
  - id: archived-get-reviews
    intent: Get archived reviews
    question: Can I retrieve reviews that were archived or deleted?
  - id: get-reviews-summary
    intent: Get a business's review summary
    question: What does my overall review summary look like for a business?
  - id: post-review-reply
    intent: Reply to a review
    question: Can I reply to a customer review through the API?
  - id: create-tags
    intent: Create review tags
    question: Can I create review tags for a business?
  - id: delete-a-tag
    intent: Delete a review tag
    question: Can I delete a review tag I no longer need?
  - id: get-all-tags
    intent: List review tags
    question: Which review tags exist for my business?
  - id: assign-tags-to-filtered-reviews
    intent: Tag a filtered set of reviews
    question: Can I tag a filtered set of reviews in bulk?
  phrasing_ops: 10
  slug: birdeye-reviews-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Search AI provides a comprehensive view of your business performance across AI-powered search platforms, including data accuracy, sentiment analysis, citations, brand ranking, and overall visibility.
  name: Birdeye Search AI API
  phrasing_intents:
  - id: get-search-ai-configuration
    intent: Get my account's Search AI setup
    question: What is the Search AI setup on the account I'm signed into?
  - id: get-search-ai-available-runs
    intent: Get my account's remaining Search AI runs
    question: How many Search AI runs do I have left on my account?
  - id: get-search-ai-citations
    intent: Get sources AI models cite for my business
    question: Which sources do AI models cite when answering about my business?
  - id: get-search-ai-businesses
    intent: Get businesses surfaced in AI search
    question: Which businesses appear in AI search answers for my themes?
  - id: get-accuracy-report
    intent: Get the AI answer accuracy report
    question: How accurate is the information AI models give about my locations?
  - id: get-sentiment-report
    intent: Get the AI search sentiment report
    question: What sentiment do AI models express about my business?
  - id: getSearchAiConfiguration
    intent: Get a business's Search AI setup as a partner
    question: Can a partner fetch the Search AI configuration for a specific business number?
  - id: getSearchAiAvailableRuns
    intent: Get a business's Search AI runs as a partner
    question: Can a partner check available Search AI runs for a given business number?
  phrasing_ops: 8
  slug: birdeye-search-ai-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Create and track Social posting for all channels.
  name: Birdeye Social API
  phrasing_intents:
  - id: schedule-social-post
    intent: Schedule a social media post
    question: Can I schedule a social media post for a future time?
  - id: edit-scheduled-social-post
    intent: Edit a scheduled social post
    question: Can I change a post that's scheduled but not yet published?
  - id: edit-published-social-post
    intent: Edit a published social post
    question: Can I edit a social post after it has already been published?
  - id: delete-public-social-post
    intent: Delete a social post
    question: Can I delete a social post from specific locations?
  - id: track-social-post
    intent: Track a social post's status
    question: Did my social post publish successfully?
  - id: social-open-url-performance-report
    intent: Get the social open URL performance report
    question: Can I get the social open URL performance report for a date range?
  - id: uploadSocialMedia
    intent: Upload images or videos to the media library
    question: Can I upload images or videos from URLs into the social media library?
  - id: trackSocialMediaUpload
    intent: Check a media upload batch's status
    question: Has my media upload batch finished processing?
  phrasing_ops: 8
  slug: birdeye-social-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Subscribe or Unsubscribe multiple webhooks with different URLs or Events for a subscription and deliver real-time notifications.
  name: Birdeye Subscription API
  phrasing_intents:
  - id: create-subscription
    intent: Subscribe to account events
    question: Can I subscribe a webhook URL to Birdeye events for my account?
  - id: unsubscribe-subscription
    intent: Cancel an event subscription
    question: Can I cancel an event subscription I created?
  phrasing_ops: 2
  slug: birdeye-subscription-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Engage each customer at the right time with NPS or CSAT surveys to improve your service.
  name: Birdeye Survey API
  phrasing_intents:
  - id: get-survey
    intent: Get a survey
    question: Can I fetch a survey's content in a particular language?
  - id: post-a-survey-response
    intent: Submit a survey response
    question: Can I submit a survey response through the API?
  - id: list-responses-for-a-survey
    intent: List responses to a survey
    question: Can I list all responses to a survey for a date range?
  - id: get-all-surveys
    intent: List a business's surveys
    question: Which surveys does my business have?
  - id: create-survey
    intent: Create a survey
    question: Can I create a new survey for a business?
  - id: update-survey-settings
    intent: Update a survey's settings
    question: Can I change a survey's settings or who can access it?
  phrasing_ops: 6
  slug: birdeye-survey-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Create standout customer support with ticketing across reviews, untagged, and survey responses.
  name: Birdeye Ticketing API
  phrasing_intents:
  - id: create-ticket
    intent: Create a ticket
    question: Can I open a ticket for a customer issue and assign it to someone?
  - id: add-ticket-comments
    intent: Comment on a ticket
    question: Can I add a comment to an existing ticket?
  - id: update-ticket
    intent: Update tickets at a location
    question: Can I update existing tickets at a location?
  - id: get-all-ticket-data
    intent: List tickets or ticket counts
    question: Can I list tickets filtered by status, type, or assignee?
  phrasing_ops: 4
  slug: birdeye-ticketing-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Delete and manage user profiles and permissions easily.
  name: Birdeye User API
  phrasing_intents:
  - id: create-user
    intent: Create a user
    question: Can I add a new user with a role and send them an invite?
  - id: update-user
    intent: Update a user's role and access
    question: Can I change a user's role or which locations they can access?
  - id: delete-a-user
    intent: Revoke a user's access to a business
    question: Can I revoke a user's access to a business?
  - id: forgot-password
    intent: Start a password reset
    question: Can I trigger a password reset for a user?
  - id: get-details-of-a-user
    intent: Get a user's details
    question: What role and access does a given user have?
  phrasing_ops: 5
  slug: birdeye-user-api
- baseURL: https://api.birdeye.com
  baseurl_source: declared
  description: Configure multiple webhooks with different URLs for a subscription and deliver real-time notifications.
  name: Birdeye Webhook API
  phrasing_intents:
  - id: get-events
    intent: List messenger webhook events
    question: Which messenger webhook events can I subscribe to?
  - id: create-webhook-subscription
    intent: Subscribe an endpoint to messenger events
    question: Can I send messenger events to my own endpoint?
  phrasing_ops: 2
  slug: birdeye-webhook-api
artifact_total: 244
asyncapis:
- description: ''
  name: Birdeye Webhooks
  slug: birdeye-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Birdeye Aggregation API
  slug: open-birdeye-aggregation-api
- collection_type: open
  name: Birdeye Aggregation Business API
  slug: open-birdeye-business-api
- collection_type: open
  name: Birdeye Aggregation Business Media API
  slug: open-birdeye-business-media-api
- collection_type: open
  name: Birdeye Aggregation Campaign API
  slug: open-birdeye-campaign-api
- collection_type: open
  name: Birdeye Aggregation Competitor AI API
  slug: open-birdeye-competitor-ai-api
- collection_type: open
  name: Birdeye Aggregation Competitor API
  slug: open-birdeye-competitor-api
- collection_type: open
  name: Birdeye Aggregation Contact API
  slug: open-birdeye-contact-api
- collection_type: open
  name: Birdeye Aggregation Contact V2 API
  slug: open-birdeye-contact-v2-api
- collection_type: open
  name: Birdeye Aggregation Conversation API
  slug: open-birdeye-conversation-api
- collection_type: open
  name: Birdeye Aggregation Custom Fields API
  slug: open-birdeye-custom-fields-api
- collection_type: open
  name: Birdeye Aggregation Employee API
  slug: open-birdeye-employee-api
- collection_type: open
  name: Birdeye Aggregation FAQ API
  slug: open-birdeye-faq-api
- collection_type: open
  name: Birdeye Aggregation GMB Products API
  slug: open-birdeye-gmb-products-api
- collection_type: open
  name: Birdeye Aggregation Google Q&A API
  slug: open-birdeye-google-q-a-api
- collection_type: open
  name: Birdeye Aggregation Google Services API
  slug: open-birdeye-google-services-api
- collection_type: open
  name: Birdeye Aggregation Insight AI API
  slug: open-birdeye-insight-ai-api
- collection_type: open
  name: Birdeye Aggregation Integration API
  slug: open-birdeye-integration-api
- collection_type: open
  name: Birdeye Aggregation Listing API
  slug: open-birdeye-listing-api
- collection_type: open
  name: Birdeye Aggregation Report API
  slug: open-birdeye-report-api
- collection_type: open
  name: Birdeye Aggregation Search AI API
  slug: open-birdeye-search-ai-api
- collection_type: open
  name: Birdeye Aggregation Social API
  slug: open-birdeye-social-api
- collection_type: open
  name: Birdeye Aggregation Subscription API
  slug: open-birdeye-subscription-api
- collection_type: open
  name: Birdeye Aggregation Survey API
  slug: open-birdeye-survey-api
- collection_type: open
  name: Birdeye Aggregation Ticketing API
  slug: open-birdeye-ticketing-api
- collection_type: open
  name: Birdeye Aggregation User API
  slug: open-birdeye-user-api
- collection_type: open
  name: Birdeye Aggregation Webhook API
  slug: open-birdeye-webhook-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/capabilities/birdeye-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/birdeye-capability-edges.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/openapi/_original/birdeye-openapi-original.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/birdeye-openapi-original.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/a2a/birdeye-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/birdeye-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/mcp/birdeye-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/birdeye-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/mcp/birdeye-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/birdeye-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/llms/birdeye-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/birdeye-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/well-known/birdeye-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/birdeye-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/conventions/birdeye-conventions.yml
  title: ''
  type: Conventions
  url: conventions/birdeye-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/errors/birdeye-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/birdeye-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/data-model/birdeye-data-model.yml
  title: ''
  type: DataModel
  url: data-model/birdeye-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/overlays/birdeye-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/birdeye-openapi-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/conformance/birdeye-conformance.yml
  title: ''
  type: Conformance
  url: conformance/birdeye-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://birdeye.com/security/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/security/birdeye-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/birdeye-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/security/birdeye-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/birdeye-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://birdeye.com/security/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/scopes/birdeye-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/birdeye-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/lifecycle/birdeye-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/birdeye-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/changelog/birdeye-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/birdeye-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/asyncapi/birdeye-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/birdeye-webhooks.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.birdeye.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.birdeye.com/api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.birdeye.com/mcp/quickstart
- group: operate
  title: ''
  type: Support
  url: https://support.birdeye.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://birdeye.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://birdeye.com/privacy/
- group: start
  title: ''
  type: Login
  url: https://birdeye.com/login/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/birdeyeinc
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/agentic-access/birdeye-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/birdeye-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/security/birdeye-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/birdeye-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/authentication/birdeye-authentication.yml
  title: ''
  type: Authentication
  url: authentication/birdeye-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://birdeye.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.birdeye.com/api/introduction
- group: company
  title: ''
  type: Blog
  url: https://birdeye.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://birdeye.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.birdeye.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/birdeye
- group: other
  title: ''
  type: X
  url: https://x.com/Birdeye_
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/plans/birdeye-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/birdeye-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/rate-limits/birdeye-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/birdeye-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/finops/birdeye-finops.yml
  title: ''
  type: FinOps
  url: finops/birdeye-finops.yml
created: 2026-06-13
description: Birdeye is an AI-powered customer experience and reputation management platform for multi-location brands. Its REST API enables developers to manage online reviews across 200+ sites, send surveys, respond to messages, automate review requests, and track reputation metrics including ratings, sentiment trends, and NPS scores. Integrations cover listings, webchat, appointments, payments, social posting, and customer insights.
examples:
- key_count: 5
  name: Add Aggregation Url
  slug: add-aggregation-url
- key_count: 5
  name: Add Media
  slug: add-media
- key_count: 5
  name: Add New Competitor Aggregation Url
  slug: add-new-competitor-aggregation-url
- key_count: 5
  name: Add Products On A Location
  slug: add-products-on-a-location
- key_count: 5
  name: Add Ticket Comments
  slug: add-ticket-comments
- key_count: 5
  name: Archived Get Reviews
  slug: archived-get-reviews
- key_count: 5
  name: Assign Tags To Filtered Reviews
  slug: assign-tags-to-filtered-reviews
- key_count: 5
  name: Associate
  slug: associate
- key_count: 5
  name: Average Response Time By Location
  slug: average-response-time-by-location
- key_count: 5
  name: Average Response Time Over Time
  slug: average-response-time-over-time
- key_count: 5
  name: Competitive Ranking Report
  slug: competitive-ranking-report
- key_count: 5
  name: Contact Us Request
  slug: contact-us-request
- key_count: 5
  name: Contact
  slug: contact
- key_count: 5
  name: Create A Business
  slug: create-a-business
- key_count: 5
  name: Create Answer
  slug: create-answer
- key_count: 5
  name: Create Custom Card
  slug: create-custom-card
- key_count: 5
  name: Create Listing
  slug: create-listing
- key_count: 5
  name: Create New Child Business In Competitor Enterprise
  slug: create-new-child-business-in-competitor-enterprise
- key_count: 5
  name: Create New Competitor Enterprise
  slug: create-new-competitor-enterprise
- key_count: 5
  name: Create Or Update Contact
  slug: create-or-update-contact
- key_count: 5
  name: Create Product Listing
  slug: create-product-listing
- key_count: 5
  name: Create Question
  slug: create-question
- key_count: 5
  name: Create Service
  slug: create-service
- key_count: 5
  name: Create Subscription
  slug: create-subscription
- key_count: 5
  name: Create Survey
  slug: create-survey
- key_count: 5
  name: Create Tags
  slug: create-tags
- key_count: 5
  name: Create Ticket
  slug: create-ticket
- key_count: 5
  name: Create User
  slug: create-user
- key_count: 5
  name: Create Webhook Subscription
  slug: create-webhook-subscription
- key_count: 5
  name: Create
  slug: create
- key_count: 5
  name: Customer Activity Log
  slug: customer-activity-log
- key_count: 5
  name: Customer Checkin
  slug: customer-checkin
- key_count: 5
  name: Customer Delete
  slug: customer-delete
- key_count: 5
  name: Customer Or Lead List
  slug: customer-or-lead-list
- key_count: 5
  name: Deactivate Listing
  slug: deactivate-listing
- key_count: 5
  name: Delete A Tag
  slug: delete-a-tag
- key_count: 5
  name: Delete A User
  slug: delete-a-user
- key_count: 5
  name: Delete Aggregation Url
  slug: delete-aggregation-url
- key_count: 5
  name: Delete All Questions And Answers
  slug: delete-all-questions-and-answers
- key_count: 5
  name: Delete Answer
  slug: delete-answer
- key_count: 5
  name: Delete Business
  slug: delete-business
- key_count: 5
  name: Delete Contact
  slug: delete-contact
- key_count: 5
  name: Delete Custom Card
  slug: delete-custom-card
- key_count: 5
  name: Delete Media
  slug: delete-media
- key_count: 5
  name: Delete Product Listings
  slug: delete-product-listings
- key_count: 5
  name: Delete Public Social Post
  slug: delete-public-social-post
- key_count: 5
  name: Delete Question
  slug: delete-question
- key_count: 5
  name: Delete Services
  slug: delete-services
- key_count: 5
  name: Delete
  slug: delete
- key_count: 5
  name: Edit Published Social Post
  slug: edit-published-social-post
- key_count: 5
  name: Edit Scheduled Social Post
  slug: edit-scheduled-social-post
- key_count: 5
  name: Fetch Request Url
  slug: fetch-request-url
- key_count: 5
  name: Fix Listing
  slug: fix-listing
- key_count: 5
  name: Forgot Password
  slug: forgot-password
- key_count: 5
  name: Get Accuracy Report
  slug: get-accuracy-report
- key_count: 5
  name: Get All Aggregation Source
  slug: get-all-aggregation-source
- key_count: 5
  name: Get All Qna
  slug: get-all-qna
- key_count: 5
  name: Get All Questions And Answers
  slug: get-all-questions-and-answers
- key_count: 5
  name: Get All Services
  slug: get-all-services
- key_count: 5
  name: Get All Surveys
  slug: get-all-surveys
- key_count: 5
  name: Get All Tags
  slug: get-all-tags
- key_count: 5
  name: Get All Ticket Data
  slug: get-all-ticket-data
- key_count: 5
  name: Get All Unanswered Questions And Answers
  slug: get-all-unanswered-questions-and-answers
- key_count: 5
  name: Get Apple Action Links
  slug: get-apple-action-links
- key_count: 5
  name: Get Apple Attributes
  slug: get-apple-attributes
- key_count: 5
  name: Get Birdeye Impressions
  slug: get-birdeye-impressions
- key_count: 5
  name: Get Business Competitors
  slug: get-business-competitors
- key_count: 5
  name: Get Business
  slug: get-business
- key_count: 5
  name: Get Category List
  slug: get-category-list
- key_count: 5
  name: Get Competitor Business
  slug: get-competitor-business
- key_count: 5
  name: Get Competitor Child Business
  slug: get-competitor-child-business
- key_count: 5
  name: Get Competitor Reviews
  slug: get-competitor-reviews
- key_count: 5
  name: Get Contact
  slug: get-contact
- key_count: 5
  name: Get Custom Card Details
  slug: get-custom-card-details
- key_count: 5
  name: Get Dashboard Data
  slug: get-dashboard-data
- key_count: 5
  name: Get Details Of A User
  slug: get-details-of-a-user
- key_count: 5
  name: Get Details Of Employees
  slug: get-details-of-employees
- key_count: 5
  name: Get Gmb Attributes
  slug: get-gmb-attributes
- key_count: 5
  name: Get Google Keywords Count
  slug: get-google-keywords-count
- key_count: 5
  name: Get Hierarchy For An Enterprise
  slug: get-hierarchy-for-an-enterprise
- key_count: 5
  name: Get Insight Experience Location Info
  slug: get-insight-experience-location-info
- key_count: 5
  name: Get Insight Experience Score Benchmark
  slug: get-insight-experience-score-benchmark
- key_count: 5
  name: Get Keyword Statistics
  slug: get-keyword-statistics
- key_count: 5
  name: Get List Product Listing
  slug: get-list-product-listing
- key_count: 5
  name: Get Listing
  slug: get-listing
- key_count: 5
  name: Get Location Mapping
  slug: get-location-mapping
- key_count: 5
  name: Get Location Status Report
  slug: get-location-status-report
- key_count: 5
  name: Get Media
  slug: get-media
- key_count: 5
  name: Get More Hours Type
  slug: get-more-hours-type
- key_count: 5
  name: Get Opt Out Contact Data
  slug: get-opt-out-contact-data
- key_count: 5
  name: Get Product Listing
  slug: get-product-listing
- key_count: 5
  name: Get Review Conversion Report
  slug: get-review-conversion-report
- key_count: 5
  name: Get Reviews Summary
  slug: get-reviews-summary
- key_count: 5
  name: Get Reviews
  slug: get-reviews
- key_count: 5
  name: Get Score
  slug: get-score
- key_count: 5
  name: Get Search Ai Available Runs
  slug: get-search-ai-available-runs
- key_count: 5
  name: Get Search Ai Businesses
  slug: get-search-ai-businesses
- key_count: 5
  name: Get Search Ai Citations
  slug: get-search-ai-citations
- key_count: 5
  name: Get Search Ai Configuration
  slug: get-search-ai-configuration
- key_count: 5
  name: Get Sentiment Report
  slug: get-sentiment-report
- key_count: 5
  name: Get Survey
  slug: get-survey
- key_count: 5
  name: Get Theme Statistics
  slug: get-theme-statistics
- key_count: 5
  name: Get Timezone List
  slug: get-timezone-list
- key_count: 5
  name: Get
  slug: get
- key_count: 5
  name: Insights Category Report By Location Report
  slug: insights-category-report-by-location-report
- key_count: 5
  name: List Conversations
  slug: list-conversations
- key_count: 5
  name: List Responses For A Survey
  slug: list-responses-for-a-survey
- key_count: 5
  name: Listings Insights Datapoints
  slug: listings-insights-datapoints
- key_count: 5
  name: Listings Insights
  slug: listings-insights
- key_count: 5
  name: Nps By Location Report
  slug: nps-by-location-report
- key_count: 5
  name: Nps Over Time Report
  slug: nps-over-time-report
- key_count: 5
  name: Onboard Google Merchant Account
  slug: onboard-google-merchant-account
- key_count: 5
  name: Post A Survey Response
  slug: post-a-survey-response
- key_count: 5
  name: Post Review Reply
  slug: post-review-reply
- key_count: 5
  name: Post
  slug: post
- key_count: 5
  name: Remove Particular Tags From All Reviews
  slug: remove-particular-tags-from-all-reviews
- key_count: 5
  name: Remove Products On A Location
  slug: remove-products-on-a-location
- key_count: 5
  name: Remove Tags From Filtered Reviews
  slug: remove-tags-from-filtered-reviews
- key_count: 5
  name: Retrieve Competitor Review Metrics
  slug: retrieve-competitor-review-metrics
- key_count: 5
  name: Retrieve Competitor Reviews
  slug: retrieve-competitor-reviews
- key_count: 5
  name: Retrieve Contact
  slug: retrieve-contact
- key_count: 5
  name: Retrieve Menu Details
  slug: retrieve-menu-details
- key_count: 5
  name: Retrieve Opted Out Contacts
  slug: retrieve-opted-out-contacts
- key_count: 5
  name: Review And Rating Over Time Report
  slug: review-and-rating-over-time-report
- key_count: 5
  name: Review By Source Report
  slug: review-by-source-report
- key_count: 5
  name: Review Count Rating By Employee
  slug: review-count-rating-by-employee
- key_count: 5
  name: Review Count Rating
  slug: review-count-rating
- key_count: 5
  name: Review Response Rate By Location Overview
  slug: review-response-rate-by-location-overview
- key_count: 5
  name: Review Response Rate Over Time
  slug: review-response-rate-over-time
- key_count: 5
  name: Reviews Rating By Location Report
  slug: reviews-rating-by-location-report
- key_count: 5
  name: Schedule Social Post
  slug: schedule-social-post
- key_count: 5
  name: Search Business
  slug: search-business
- key_count: 5
  name: Set Defaullt Review Sources
  slug: set-defaullt-review-sources
- key_count: 5
  name: Social Open Url Performance Report
  slug: social-open-url-performance-report
- key_count: 5
  name: Subscribe Unsubscribe Customer
  slug: subscribe-unsubscribe-customer
- key_count: 5
  name: Track Social Post
  slug: track-social-post
- key_count: 5
  name: Unsubscribe Subscription
  slug: unsubscribe-subscription
- key_count: 5
  name: Update Answer
  slug: update-answer
- key_count: 5
  name: Update Business
  slug: update-business
- key_count: 5
  name: Update Communication Preferences
  slug: update-communication-preferences
- key_count: 5
  name: Update Custom Card
  slug: update-custom-card
- key_count: 5
  name: Update Hierarchy
  slug: update-hierarchy
- key_count: 5
  name: Update Listing
  slug: update-listing
- key_count: 5
  name: Update Location Mapping
  slug: update-location-mapping
- key_count: 5
  name: Update Media
  slug: update-media
- key_count: 5
  name: Update Product Listing
  slug: update-product-listing
- key_count: 5
  name: Update Public Profile Of Businesses
  slug: update-public-profile-of-businesses
- key_count: 5
  name: Update Question
  slug: update-question
- key_count: 5
  name: Update Service
  slug: update-service
- key_count: 5
  name: Update Survey Settings
  slug: update-survey-settings
- key_count: 5
  name: Update The Status
  slug: update-the-status
- key_count: 5
  name: Update Ticket
  slug: update-ticket
- key_count: 5
  name: Update User
  slug: update-user
- key_count: 5
  name: Update
  slug: update
- key_count: 5
  name: Upsert Contact
  slug: upsert-contact
- key_count: 5
  name: Usage Report
  slug: usage-report
- key_count: 5
  name: Visitor Report
  slug: visitor-report
finops:
- name: Birdeye Finops
  service_category: ''
  slug: birdeye-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/birdeye.png
json_schemas:
- name: Archived Get Reviews Request
  property_count: 9
  slug: archived-get-reviews-request
- name: Associate Request
  property_count: 3
  slug: associate-request
- name: Create A Business Request
  property_count: 7
  slug: create-a-business-request
- name: Create Custom Card Request
  property_count: 7
  slug: create-custom-card-request
- name: Create Or Update Contact Request
  property_count: 13
  slug: create-or-update-contact-request
- name: Create Request
  property_count: 6
  slug: create-request
- name: Create Tags Request
  property_count: 1
  slug: create-tags-request
- name: Create User Request
  property_count: 6
  slug: create-user-request
- name: Get Birdeye Impressions Request
  property_count: 7
  slug: get-birdeye-impressions-request
- name: Get Reviews Request
  property_count: 16
  slug: get-reviews-request
- name: Post Request
  property_count: 5
  slug: post-request
- name: Post Review Reply Request
  property_count: 2
  slug: post-review-reply-request
- name: Remove Particular Tags From All Reviews Request
  property_count: 1
  slug: remove-particular-tags-from-all-reviews-request
- name: Search Business Request
  property_count: 5
  slug: search-business-request
- name: Update Business Request
  property_count: 50
  slug: update-business-request
- name: Update Custom Card Request
  property_count: 10
  slug: update-custom-card-request
- name: Update Hierarchy Request
  property_count: 1
  slug: update-hierarchy-request
- name: Update Public Profile Of Businesses Request
  property_count: 1
  slug: update-public-profile-of-businesses-request
- name: Update Request
  property_count: 5
  slug: update-request
- name: Update User Request
  property_count: 4
  slug: update-user-request
jsonld:
- class_count: 279
  name: Birdeye Context
  property_count: 18
  slug: birdeye-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.birdeye.com over streamable HTTP requiring OAuth; 25 tools listed.
  name: Birdeye
  slug: birdeye
modified: 2026-08-13
name: Birdeye
nav: Providers
network: true
overview: 'Birdeye publishes 27 APIs on the [APIs.io](https://apis.io/) network, including Aggregation API, Business API, Business Media API, and 24 more. Tagged areas include Reputation Management, Reviews, Customer Experience, Surveys, and Messaging.


  The Birdeye catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Birdeye''s developer surface includes changelog, API reference, getting-started guide, support, authentication, documentation, engineering blog, and 35 more developer resources.'
plans:
- name: Birdeye Plans Pricing
  plan_count: 4
  slug: birdeye-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Birdeye Rate Limits
  slug: birdeye-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Birdeye API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: birdeye-jsonschema-spectral-rules
scopes:
- name: Birdeye Scopes
  scope_count: 3
  slug: birdeye-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: exemplar
  composite: 77.3
  coverage:
    artifact_dirs: 32
    catalog_earned: 78.8
    catalog_earned_first_party: 20.0
    catalog_gap: 36.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 93.4
    contract_governance: 41.7
    contract_quality: 62.0
    developer_ergonomics: 64.3
    discoverability: 75.0
    operational_transparency: 73.7
  previous_composite: 77.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/screenshots/birdeye-2026-06-20T173257.png
security:
- kind: authentication
  name: Birdeye Authentication
  slug: birdeye-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Birdeye Domain Security
  slug: birdeye-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Birdeye Vulnerability Disclosure
  slug: birdeye-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Birdeye Trust Center
  slug: birdeye-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001, HIPAA, GDPR, CCPA / CPRA
slug: birdeye
tags:
- Reputation Management
- Reviews
- Customer Experience
- Surveys
- Messaging
- Multi-Location
- Artificial Intelligence
- A2A
website: https://birdeye.com/
---
