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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 127
  human_in_the_loop: 0
  name: Birdeye Agentic Access
  operation_count: 162
  slug: birdeye-agentic-access
  summary_line: 162 operations · 127 acting
api_count: 27
apis:
- description: Access your public data from 150+ review sites.
  name: Birdeye Aggregation API
  slug: birdeye-aggregation-api
- description: Create and maintain your business on Birdeye.
  name: Birdeye Business API
  slug: birdeye-business-api
- description: 'Add, delete and manage business media. Supported Media Size Photo: JPG or PNG. 720 x 720px. 10KB min. Video: 30 sec long. 720p or more upto 75MB. Note Uploaded media will be pushed to your google busi'
  name: Birdeye Business Media API
  slug: birdeye-business-media-api
- description: Create a short link for review requests and set review sources in the template.
  name: Birdeye Campaign API
  slug: birdeye-campaign-api
- description: Competitive intelligence, simplified by AI.
  name: Birdeye Competitor AI API
  slug: birdeye-competitor-ai-api
- description: Make competitive insights your unfair advantage.
  name: Birdeye Competitor API
  slug: birdeye-competitor-api
- description: Manage contacts across locations effortlessly with a robust Contact Management System.
  name: Birdeye Contact API
  slug: birdeye-contact-api
- description: Easily manage contacts across multiple locations using enhanced Contact APIs, featuring built-in support for communication preference flags.
  name: Birdeye Contact V2 API
  slug: birdeye-contact-v2-api
- description: Connect with customers across a range of digital channels from one unified inbox.
  name: Birdeye Conversation API
  slug: birdeye-conversation-api
- description: Create, delete , update , associate and get custom fields easily.
  name: Birdeye Custom Fields API
  slug: birdeye-custom-fields-api
- description: The Employee API from Birdeye — 1 operation(s) for employee.
  name: Birdeye Employee API
  slug: birdeye-employee-api
- description: To retrieve all Question and Answer (QnA) entries across locations using FAQ APIs, enabling smart support and knowledge features for businesses.
  name: Birdeye FAQ API
  slug: birdeye-faq-api
- description: To manage products, locations, and business details through Listing GMB platform
  name: Birdeye GMB Products API
  slug: birdeye-gmb-products-api
- description: Note Applicable to be used only by paid listings clients, for their active locations, for the Google Q&amp;A section, in the Google listing
  name: Birdeye Google Q&A API
  slug: birdeye-google-q-a-api
- description: Note Applicable to be used only by paid listings clients, for their active locations, for the Google Services section, in the Google listing. No two services should have the same service name. It is r
  name: Birdeye Google Services API
  slug: birdeye-google-services-api
- description: Insight intelligence, simplified by AI.
  name: Birdeye Insight AI API
  slug: birdeye-insight-ai-api
- description: Birdeye integrates with various software or tools you use.
  name: Birdeye Integration API
  slug: birdeye-integration-api
- description: Keep your business information accurate and consistent across 50+ websites.
  name: Birdeye Listing API
  slug: birdeye-listing-api
- description: Various reporting data points across Birdeye modules like reviews, insights and competitors etc for all your data visualisation
  name: Birdeye Report API
  slug: birdeye-report-api
- description: Consistently generate more reviews and higher ratings.
  name: Birdeye Reviews API
  slug: birdeye-reviews-api
- description: Search AI provides a comprehensive view of your business performance across AI-powered search platforms, including data accuracy, sentiment analysis, citations, brand ranking, and overall visibility.
  name: Birdeye Search AI API
  slug: birdeye-search-ai-api
- description: Create and track Social posting for all channels.
  name: Birdeye Social API
  slug: birdeye-social-api
- description: Subscribe or Unsubscribe multiple webhooks with different URLs or Events for a subscription and deliver real-time notifications.
  name: Birdeye Subscription API
  slug: birdeye-subscription-api
- description: Engage each customer at the right time with NPS or CSAT surveys to improve your service.
  name: Birdeye Survey API
  slug: birdeye-survey-api
- description: Create standout customer support with ticketing across reviews, untagged, and survey responses.
  name: Birdeye Ticketing API
  slug: birdeye-ticketing-api
- description: Delete and manage user profiles and permissions easily.
  name: Birdeye User API
  slug: birdeye-user-api
- description: Configure multiple webhooks with different URLs for a subscription and deliver real-time notifications.
  name: Birdeye Webhook API
  slug: birdeye-webhook-api
artifact_total: 212
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/birdeye-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/birdeye-domain-security.yml
- group: auth
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
  url: https://developers.birdeye.com/
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
  title: ''
  type: Plans
  url: plans/birdeye-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/birdeye-rate-limits.yml
- group: commercial
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
modified: 2026-06-13
name: Birdeye
nav: Providers
network: true
overview: 'Birdeye publishes 27 APIs on the [APIs.io](https://apis.io/) network, including Aggregation API, Business API, Business Media API, and 24 more. Tagged areas include Reputation Management, Reviews, Customer Experience, Surveys, and Messaging.


  The Birdeye catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Birdeye''s developer surface includes authentication, documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Birdeye Plans Pricing
  plan_count: 4
  slug: birdeye-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 1
  name: Birdeye Rate Limits
  slug: birdeye-rate-limits
rules:
- name: Birdeye API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: birdeye-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.6
  delta: 2.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 68.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 44.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/birdeye/refs/heads/main/screenshots/birdeye-2026-06-20T173257.png
security:
- kind: authentication
  name: Birdeye Authentication
  slug: birdeye-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Birdeye Domain Security
  slug: birdeye-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: birdeye
tags:
- Reputation Management
- Reviews
- Customer Experience
- Surveys
- Messaging
- Multi-Location
- AI
website: https://birdeye.com/
---
