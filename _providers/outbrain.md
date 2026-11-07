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
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 33
  human_in_the_loop: 1
  name: Outbrain Agentic Access
  operation_count: 103
  slug: outbrain-agentic-access
  summary_line: 103 operations · 33 acting · 1 human-in-the-loop
api_count: 6
apis:
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: Token-based authentication
  name: Outbrain Authentication API
  phrasing_intents:
  - id: login
    intent: Get an API token with username and password
    question: How do I get an OB-TOKEN-V1 token for the Outbrain Amplify API?
  phrasing_ops: 1
  slug: outbrain-authentication-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: Budget management
  name: Outbrain Budgets API
  phrasing_intents:
  - id: getBudgetsId
    intent: Retrieve a budget with remaining spend details
    question: How much is left unspent on one of my Outbrain budgets?
  - id: updateBudgetsId
    intent: Change a budget's amount or dates
    question: How do I raise the amount on an existing budget?
  - id: deleteBudgetsId
    intent: Delete an unused, detached budget
    question: Can I delete a budget that is still attached to a campaign?
  - id: getMarketersIdBudgets
    intent: List a marketer's budgets, optionally detached only
    question: Which budgets aren't attached to any campaign yet?
  - id: createMarketersIdBudgets
    intent: Create a budget that can run forever or end
    question: Can I create a budget with no end date so it runs forever?
  - id: listBudgets
    intent: List all budgets belonging to a marketer
    question: What budgets belong to my marketer account?
  - id: createBudget
    intent: Create a shared budget with a currency
    question: How do I create a shared budget that several campaigns can draw from?
  - id: getBudget
    intent: Look up a budget by its budget ID
    question: How do I fetch a budget when I only have its budgetId?
  phrasing_ops: 8
  slug: outbrain-budgets-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: Campaign management
  name: Outbrain Campaigns API
  phrasing_intents:
  - id: getCampaignsId
    intent: Retrieve a campaign with extra fields
    question: How do I see a campaign's CPC, targeting and budget in one call?
  - id: updateCampaignsId
    intent: Update a campaign's CPC, name or targeting
    question: How do I raise the CPC on a running campaign?
  - id: createCampaigns
    intent: Create a campaign with budget and targeting
    question: What do I need to launch a new campaign, like budget and CPC?
  - id: updateCampaigns
    intent: Update up to 25 campaigns at once
    question: Can I change several campaigns in a single request?
  - id: getCampaignsCampaignIdsMultiple
    intent: Retrieve up to 50 campaigns by ID
    question: Can I fetch several specific campaigns in one call?
  - id: getBudgetsIdCampaigns
    intent: List campaigns drawing from a budget
    question: Which campaigns are spending from a particular budget?
  - id: getMarketersIdCampaigns
    intent: Filter and page a marketer's campaigns
    question: How do I list a marketer's campaigns including archived ones?
  - id: getCampaignsCampaignIdLocations
    intent: Get a campaign's targeted and excluded locations
    question: Which countries and regions is my campaign geotargeting?
  phrasing_ops: 12
  slug: outbrain-campaigns-api
- baseURL: https://r.teads.tv
  baseurl_source: declared
  description: Server-side conversion events
  name: Outbrain Conversions API
  phrasing_intents:
  - id: sendConversionEvent
    intent: Send a server-side conversion event
    question: How do I send a purchase conversion from my backend without a browser pixel?
  - id: sendConversionEventBatch
    intent: Send a batch of conversion events
    question: Can I upload many conversions from my server in one request?
  phrasing_ops: 2
  slug: outbrain-conversions-api
- baseURL: https://odb.outbrain.com
  baseurl_source: declared
  description: Impression and click events
  name: Outbrain Events API
  phrasing_intents:
  - id: reportImpression
    intent: Report a widget impression
    question: How do I tell Outbrain that my widget displayed a set of recommendations?
  - id: reportClick
    intent: Report a click on a recommendation
    question: How do I record that a reader clicked one of the recommended links?
  phrasing_ops: 2
  slug: outbrain-events-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: Marketer (customer account) resources
  name: Outbrain Marketers API
  phrasing_intents:
  - id: getMarketersId
    intent: Retrieve a marketer with optional extra fields
    question: Is my marketer account enabled, and when was it last modified?
  - id: updateMarketersId
    intent: Update a marketer account's settings
    question: How do I change settings on my Outbrain marketer account?
  - id: getMarketers
    intent: List marketers my user can access
    question: Which marketer accounts can my API token access?
  - id: getMarketer
    intent: Look up a marketer by its marketer ID
    question: How do I fetch one marketer when I only have the marketerId?
  phrasing_ops: 4
  slug: outbrain-marketers-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: Promoted link (ad creative) management
  name: Outbrain PromotedLinks API
  phrasing_intents:
  - id: getPromotedLinksId
    intent: Retrieve a promoted link with image sizing
    question: How do I see the headline, image and approval status of one ad?
  - id: updatePromotedLinksIds
    intent: Enable or pause promoted links by ID
    question: How do I pause several ads at once using their IDs?
  - id: updateCampaignsCampaignIdPromotedLinks
    intent: Set CPC or status on a campaign's promoted links
    question: Can I set a different CPC on individual ads within a campaign?
  - id: createCampaignsCampaignIdPromotedLinks
    intent: Create one promoted link in a campaign
    question: How do I add a single new ad with my own headline and image to a campaign?
  - id: listPromotedLinks
    intent: List all ad creatives in a campaign
    question: What ad creatives are running in my campaign?
  - id: createCampaignsCampaignIdMultiplePromotedLinks
    intent: Create several promoted links in one request
    question: Can I upload a batch of new ads to a campaign in one call?
  - id: updateCampaignsCampaignIdPromotedLinks2
    intent: Bulk-edit up to 500 promoted links
    question: Can I change titles and descriptions on hundreds of ads at once?
  - id: getCampaignsIdPromotedLinks
    intent: Filter and page a campaign's promoted links
    question: How do I list only the enabled ads in a campaign?
  phrasing_ops: 10
  slug: outbrain-promotedlinks-api
- baseURL: https://odb.outbrain.com
  baseurl_source: declared
  description: Retrieve content recommendations
  name: Outbrain Recommendations API
  phrasing_intents:
  - id: getRecommendations
    intent: Fetch recommendations for a publisher widget
    question: How do I get the recommended articles and sponsored links for a widget on my page?
  phrasing_ops: 1
  slug: outbrain-recommendations-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: Performance reporting
  name: Outbrain Reporting API
  phrasing_intents:
  - id: reportPerformanceByCampaign
    intent: Report performance by campaign for a date range
    question: How much did each campaign spend and convert last month?
  - id: reportPerformanceByPeriodicContent
    intent: Report promoted link performance over a period
    question: Which ads performed best over the past two weeks?
  - id: reportPerformanceRealtime
    intent: Get real-time performance for a marketer
    question: How are my campaigns doing right now?
  - id: createReport
    intent: Start an asynchronous custom report
    question: How do I request a large custom report that runs in the background?
  - id: getReportStatus
    intent: Check a custom report's processing status
    question: Is my custom report still queued or has it finished?
  - id: listProcessingReports
    intent: List reports currently processing
    question: Which custom reports are running right now?
  - id: cancelReport
    intent: Cancel a report that is processing
    question: How do I stop a custom report I no longer need?
  phrasing_ops: 7
  slug: outbrain-reporting-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: Audience and contextual targeting
  name: Outbrain Targeting API
  phrasing_intents:
  - id: getAudienceTargeting
    intent: Get a campaign's audience targeting
    question: Which segments, locations, devices and browsers is my campaign targeting?
  - id: updateAudienceTargeting
    intent: Change a campaign's audience targeting
    question: How do I change the geo and platform targeting on a campaign?
  phrasing_ops: 2
  slug: outbrain-targeting-api
- description: Contextual sponsored-recommendation API for chatbot and LLM publishers, backing the Teads Conversational AI Ads SDK (public beta since 2025-11-12). Takes a partner key plus one of contentUrl / bundleU
  name: Teads In-Chat API
  slug: outbrain-teads-in-chat-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: Token Obtaining a token should be your 1st step toward using Amplify API. You need to include it in all further requests using the HTTP Header OB-TOKEN-V1. In order to protect your privacy, the tokens
  name: Outbrain Authentications API
  phrasing_intents:
  - id: getLogin
    intent: Obtain a new Amplify API token before expiry
    question: Can I renew my Amplify token through the API before it expires?
  phrasing_ops: 1
  slug: outbrain-authentications-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: Metadata about the available currencies
  name: Outbrain Currencies API
  phrasing_intents:
  - id: getCurrencies
    intent: List supported currencies and minimum CPC
    question: Which currencies can I use for my Outbrain campaigns?
  phrasing_ops: 1
  slug: outbrain-currencies-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: GeoLocations are representatives of Outbrain Geographic Locations. GeoLocations are being used for campaigns to be targeted (or excluded) by geography. The GeoLocation object has the following attribu
  name: Outbrain Geo Locations API
  phrasing_intents:
  - id: getLocationsSearch
    intent: Search for a geo location to target
    question: How do I find the location ID for a city I want to geotarget?
  - id: createLocationsSearchMultiple
    intent: Search several geo location terms at once
    question: Can I look up several cities and regions in a single location search?
  - id: getMetadataSupportedLanguages
    intent: List supported languages
    question: Which languages does Outbrain support for targeting and location names?
  phrasing_ops: 3
  slug: outbrain-geo-locations-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: 'IAB category Targeting gives you the abillity to select your preferred IAB categories in your campaign setup. The IAB category Targeting object has the following attributes: Property Type Semantic Exa'
  name: Outbrain IAB category Targeting API
  phrasing_intents:
  - id: getIabcategoriesAll
    intent: List all IAB categories
    question: Which IAB content categories can I target or exclude in Outbrain?
  phrasing_ops: 1
  slug: outbrain-iab-category-targeting-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: Interest Targeting gives you the abillity to select your preferred interests categories in your campaign setup. Then, using our powerful interest insights and predictive technology, we’ll match you wi
  name: Outbrain Interest Targeting API
  phrasing_intents:
  - id: getInterestsSearch
    intent: Search audience interests by keyword
    question: How do I find interest segments matching a keyword like travel?
  - id: getInterestsAll
    intent: List all targetable interests
    question: What is the complete list of interests available for targeting on Outbrain?
  phrasing_ops: 2
  slug: outbrain-interest-targeting-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: 'Multiple Conversions gives the ability to track any of the actions a user takes after clicking through to your content. You can track everything from top of funnel (page landings and time on site) to '
  name: Outbrain Multiple Conversions API
  phrasing_intents:
  - id: getConversionEventsId
    intent: Retrieve a conversion event definition
    question: How is one of my conversion events configured?
  - id: updateConversionEventsId
    intent: Update a conversion event definition
    question: How do I rename or reconfigure an existing conversion event?
  - id: createMarketersMarketerIdConversionEvents
    intent: Create a conversion event for a marketer
    question: How do I define a new conversion event to track sign-ups?
  - id: getMarketersIdConversionEvents
    intent: List a marketer's conversion events
    question: Which conversion events are defined on my marketer?
  - id: getMarketersIdEngagementMetrics
    intent: List engagement metrics for bid optimization
    question: Which Google Analytics engagement metrics can I optimize bids toward?
  phrasing_ops: 5
  slug: outbrain-multiple-conversions-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: 'There are a multitude of reporting endpoints that allow you to retrieve metrics at various levels of granularity. Note: All performance reports have a 10-30 minutes delay, therefore performance metric'
  name: Outbrain Performance Reporting API
  phrasing_intents:
  - id: getReportsFullDay
    intent: Find the last day with complete report data
    question: Up to which date is performance data complete and final?
  - id: getReportsDataFreshness
    intent: Check how fresh performance report data is
    question: How far behind real time is the performance reporting data?
  - id: getReportsAccountsPrimaryAccountIdMarketers
    intent: Report performance for marketers under an account
    question: How are all the marketers in my agency's primary account performing?
  - id: getReportsMarketersIdCampaigns
    intent: Report campaign performance totals for a marketer
    question: What were the clicks, spend and conversions per campaign for my marketer this month?
  - id: getReportsMarketersIdPromotedContent
    intent: Report performance by promoted link for a marketer
    question: Which individual ads, including carousels and app installs, drove the most clicks?
  - id: getReportsMarketersIdPeriodic
    intent: Report a marketer's performance over time
    question: How did my overall spend trend day by day or week by week?
  - id: getReportsMarketersIdCampaignsPeriodic
    intent: Report each campaign's performance over time
    question: How did each campaign perform per day of the week or hour of day?
  - id: getReportsMarketersIdCampaignsPeriodicHourly
    intent: Report recent hourly performance per campaign
    question: How has each campaign performed hour by hour over the last day?
  phrasing_ops: 23
  slug: outbrain-performance-reporting-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: 'Sequences comes in 2 formats: - Carousel - multi-promotedLink format that features CTA buttons, brand logo, and more. You can use Carousel to tell your brand story, showcase multiple products, and bui'
  name: Outbrain Promoted Links Sequences API
  phrasing_intents:
  - id: getPromotedLinksSequencesId
    intent: Retrieve a promoted links sequence
    question: How do I view one carousel or app install sequence by its ID?
  - id: createCampaignsCampaignIdPromotedLinksSequences
    intent: Create a carousel or promoted links sequence
    question: How do I create a carousel ad with several promoted links?
  - id: getCampaignsCampaignIdPromotedLinksSequences
    intent: List a campaign's promoted links sequences
    question: Which carousels does my campaign have?
  - id: updatePromotedLinksSequencesPromotedLinksSequenceId
    intent: Update a promoted links sequence
    question: Can I change the title or sponsor on an existing carousel?
  phrasing_ops: 4
  slug: outbrain-promotedlinkssequences-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: A Section is a specific content within the publisher's site such as sports, business etc.
  name: Outbrain Sections API
  phrasing_intents:
  - id: createSections
    intent: Look up metadata for section IDs
    question: How do I get the names and details of publisher sections from their IDs?
  phrasing_ops: 1
  slug: outbrain-sections-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: 'Segments give the ability to segment customers based on their actions, and retarget them with new or existing campaigns. This translates into your campaigns reaching a highly engaged audience that is '
  name: Outbrain Segments API
  phrasing_intents:
  - id: getSegmentsId
    intent: Retrieve an audience segment
    question: What rules define membership in one of my audience segments?
  - id: updateSegmentsId
    intent: Update an audience segment
    question: How do I rename or disable an existing audience segment?
  - id: getMarketersMarketerIdSegments
    intent: List a marketer's audience segments
    question: Which audience segments does my marketer have?
  - id: createMarketersMarketerIdSegments
    intent: Create a new audience segment
    question: How do I build a retargeting segment from people who clicked my campaigns?
  - id: getAudienceIntelSegmentsAll
    intent: List global audience intelligence segments
    question: What prebuilt global audience segments are available to target?
  - id: createSegmentsTargetingCampaigns
    intent: Find campaigns targeting given segments
    question: Which campaigns are currently targeting a particular segment?
  phrasing_ops: 6
  slug: outbrain-segments-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: User represents a single person's access to Outbrain services and to the site my.outbrain.com. A User is permitted to one or more Marketer accounts, each marketer with a role that specifies the user p
  name: Outbrain Users API
  phrasing_intents:
  - id: getMarketersMarketerIdUsers
    intent: List users with access to a marketer
    question: Who has access to my marketer account and what role does each person have?
  - id: updateMarketersMarketerIdUsers
    intent: Enable, disable or change a user's role
    question: How do I disable a user on a marketer without removing them?
  - id: deleteMarketersMarketerIdUsers
    intent: Revoke a user's access to a marketer
    question: How do I remove someone's access to a marketer account entirely?
  - id: createInvitationsMultiple
    intent: Invite new users to a marketer
    question: How do I invite several new colleagues to a marketer account at once?
  - id: updateInvitations
    intent: Revoke pending user invitations
    question: How do I cancel an invitation that hasn't been accepted yet?
  phrasing_ops: 5
  slug: outbrain-users-api
- baseURL: https://api.outbrain.com/amplify/v0.1
  baseurl_source: declared
  description: The Meta Data section represents the various values (Enumarations) that can be provided as part of the different API end-points
  name: Outbrain Metadata API
  phrasing_intents:
  - id: getMetadataBrowsers
    intent: List browsers available for targeting
    question: Which web browsers can I target in Outbrain campaigns?
  - id: getMetadataOperatingSystems
    intent: List operating systems available for targeting
    question: Which operating systems can I target, like iOS or Android?
  phrasing_ops: 2
  slug: outbrain-metadata-api
artifact_total: 88
collections:
- collection_type: postman
  name: Outbrain Amplify Authentication API
  slug: postman-outbrain-authentication-api
- collection_type: postman
  name: Outbrain Amplify Authentication Budgets API
  slug: postman-outbrain-budgets-api
- collection_type: postman
  name: Outbrain Amplify Authentication Campaigns API
  slug: postman-outbrain-campaigns-api
- collection_type: postman
  name: Outbrain Amplify Authentication Conversions API
  slug: postman-outbrain-conversions-api
- collection_type: postman
  name: Outbrain Amplify Authentication Events API
  slug: postman-outbrain-events-api
- collection_type: postman
  name: Outbrain Amplify Authentication Marketers API
  slug: postman-outbrain-marketers-api
- collection_type: postman
  name: Outbrain Amplify Authentication PromotedLinks API
  slug: postman-outbrain-promotedlinks-api
- collection_type: postman
  name: Outbrain Amplify Authentication Recommendations API
  slug: postman-outbrain-recommendations-api
- collection_type: postman
  name: Outbrain Amplify Authentication Reporting API
  slug: postman-outbrain-reporting-api
- collection_type: postman
  name: Outbrain Amplify Authentication Targeting API
  slug: postman-outbrain-targeting-api
- collection_type: open
  name: Outbrain Amplify API
  slug: open-outbrain-amplify-api-full
- collection_type: open
  name: Outbrain Amplify API
  slug: open-outbrain-amplify-api
- collection_type: open
  name: Outbrain Amplify Authentication API
  slug: open-outbrain-authentication-api
- collection_type: open
  name: Outbrain Amplify Authentication Budgets API
  slug: open-outbrain-budgets-api
- collection_type: open
  name: Outbrain Amplify Authentication Campaigns API
  slug: open-outbrain-campaigns-api
- collection_type: open
  name: Outbrain Amplify Authentication Conversions API
  slug: open-outbrain-conversions-api
- collection_type: open
  name: Outbrain Engage API
  slug: open-outbrain-engage-api
- collection_type: open
  name: Outbrain Amplify Authentication Events API
  slug: open-outbrain-events-api
- collection_type: open
  name: Outbrain Amplify Authentication Marketers API
  slug: open-outbrain-marketers-api
- collection_type: open
  name: Outbrain Amplify Authentication PromotedLinks API
  slug: open-outbrain-promotedlinks-api
- collection_type: open
  name: Outbrain Amplify Authentication Recommendations API
  slug: open-outbrain-recommendations-api
- collection_type: open
  name: Outbrain Amplify Authentication Reporting API
  slug: open-outbrain-reporting-api
- collection_type: open
  name: Outbrain Amplify Authentication Targeting API
  slug: open-outbrain-targeting-api
- collection_type: open
  name: Teads Advertiser Conversion API
  slug: open-outbrain-teads-conversion-api
- collection_type: open
  name: Teads Report API
  slug: open-outbrain-teads-report-api
common:
- group: other
  href: https://artifacts.apis.io/outbrain/capabilities/outbrain-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/outbrain-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://outbrain.com
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/outbrain/overview
- group: agent
  href: https://artifacts.apis.io/outbrain/agentic-access/outbrain-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/outbrain-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/outbrain/security/outbrain-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/outbrain-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/outbrain/security/outbrain-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/outbrain-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/outbrain/security/outbrain-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/outbrain-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/outbrain/authentication/outbrain-authentication.yml
  title: ''
  type: Authentication
  url: authentication/outbrain-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://www.outbrain.com
- group: start
  title: ''
  type: Portal
  url: https://www.teads.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.outbrain.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.outbrain.com/apis/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.outbrain.com/home-page/amplify-api/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.outbrain.com/home-page/amplify-api/documentation/
- group: docs
  title: ''
  type: Documentation
  url: https://amplifyv01.docs.apiary.io/
- group: docs
  title: ''
  type: Documentation
  url: https://teadsapi.docs.apiary.io/
- group: start
  title: ''
  type: Signup
  url: https://www.outbrain.com/partner-api/
- group: start
  title: ''
  type: Signup
  url: https://developer.outbrain.com/home-page/amplify-api/apply/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.outbrain.com/outbrain-javascript-implementation-guide/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.outbrain.com/apis/outbrain-js-api-guide/
- group: build
  title: ''
  type: SDKs
  url: https://sdk.outbrain.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.outbrain.com/help/advertisers/amplify-api/
- group: learn
  title: ''
  type: Training
  url: https://academy.teads.com
- group: company
  title: ''
  type: Blog
  url: https://engineering.teads.com
- group: company
  title: ''
  type: Blog
  url: https://blog.outbrain.com
- group: company
  title: ''
  type: Blog
  url: https://www.outbrain.com/blog/
- group: company
  title: ''
  type: Blog
  url: https://www.teads.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://investors.teads.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.outbrain.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.outbrain.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://www.outbrain.com/help/
- group: operate
  title: ''
  type: Forums
  url: https://groups.google.com/g/outbrain-amplifyapi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/outbrain
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teads
- group: build
  title: ''
  type: SDKs
  url: https://github.com/teads/TeadsSDK-iOS
- group: build
  title: ''
  type: SDKs
  url: https://github.com/teads/TeadsSDK-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/teads/TeadsSDK-ReactNative
- group: build
  title: ''
  type: Tools
  url: https://github.com/teads/teads-gtm-template
- group: build
  title: ''
  type: Tools
  url: https://github.com/teads/teads-advertiser-conversion-api-gtm-template
- group: build
  title: ''
  type: Tools
  url: https://github.com/teads/prebid-server-fork
- group: build
  title: ''
  type: Tools
  url: https://github.com/outbrain/go-secretcrypt
- group: build
  title: ''
  type: Tools
  url: https://github.com/outbrain/gracefulshutdown
- group: build
  title: ''
  type: Tools
  url: https://github.com/outbrain/elasticsearch_exporter
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/teads
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/outbrain
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/outbrain
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/teads
- group: commercial
  href: https://artifacts.apis.io/outbrain/plans/outbrain-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/outbrain-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/outbrain/rate-limits/outbrain-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/outbrain-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/outbrain/finops/outbrain-finops.yml
  title: ''
  type: FinOps
  url: finops/outbrain-finops.yml
- group: design
  href: https://artifacts.apis.io/outbrain/vocabulary/outbrain-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/outbrain-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/outbrain/rules/outbrain-rules.yml
  title: ''
  type: SpectralRules
  url: rules/outbrain-rules.yml
- group: build
  href: https://artifacts.apis.io/outbrain/packages/outbrain-packages.yml
  title: ''
  type: Packages
  url: packages/outbrain-packages.yml
- group: build
  href: https://artifacts.apis.io/outbrain/packages/outbrain-packages.yml
  title: ''
  type: SDKs
  url: packages/outbrain-packages.yml
- group: agent
  href: https://artifacts.apis.io/outbrain/well-known/outbrain-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/outbrain-well-known.yml
- group: auth
  href: https://artifacts.apis.io/outbrain/well-known/outbrain-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/outbrain-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.outbrain.com/security/bug-bounty/
- group: auth
  title: ''
  type: Compliance
  url: https://www.outbrain.com/security/
- group: agent
  href: https://artifacts.apis.io/outbrain/mcp/outbrain-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/outbrain-mcp.yml
- group: agent
  href: https://artifacts.apis.io/outbrain/llms/outbrain-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/outbrain-llms.txt
- group: design
  href: https://artifacts.apis.io/outbrain/conformance/outbrain-conformance.yml
  title: ''
  type: Conformance
  url: conformance/outbrain-conformance.yml
- group: design
  href: https://artifacts.apis.io/outbrain/errors/outbrain-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/outbrain-problem-types.yml
- group: design
  href: https://artifacts.apis.io/outbrain/errors/outbrain-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/outbrain-error-codes.yml
- group: design
  href: https://artifacts.apis.io/outbrain/lifecycle/outbrain-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/outbrain-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/outbrain/conventions/outbrain-conventions.yml
  title: ''
  type: Conventions
  url: conventions/outbrain-conventions.yml
- group: operate
  href: https://artifacts.apis.io/outbrain/changelog/outbrain-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/outbrain-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://amplifyv01.docs.apiary.io/
- group: start
  href: https://artifacts.apis.io/outbrain/sandbox/outbrain-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/outbrain-sandbox.yml
- group: design
  href: https://artifacts.apis.io/outbrain/components/outbrain-components.yml
  title: ''
  type: Components
  url: components/outbrain-components.yml
- group: design
  href: https://artifacts.apis.io/outbrain/data-model/outbrain-data-model.yml
  title: ''
  type: DataModel
  url: data-model/outbrain-data-model.yml
- group: agent
  href: https://artifacts.apis.io/outbrain/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/outbrain/overlays/outbrain-amplify-api-full-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/outbrain-amplify-api-full-overlay.yaml
- group: other
  href: https://artifacts.apis.io/outbrain/overlays/outbrain-teads-report-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/outbrain-teads-report-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.teads.com
- group: docs
  title: ''
  type: APIReference
  url: https://amplifyv01.docs.apiary.io/
- group: docs
  title: ''
  type: APIReference
  url: https://teadsapi.docs.apiary.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.teads.com/docs/category/start-here
- group: operate
  title: ''
  type: Support
  url: https://support.teads.com
- group: operate
  title: ''
  type: Support
  url: https://groups.google.com/g/outbrain-amplifyapi
- group: start
  title: ''
  type: SignUp
  url: https://www.outbrain.com/partner-api/
- group: start
  title: ''
  type: Login
  url: https://my.outbrain.com/create-token
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.teads.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.teads.com/privacy-policy/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/teads/TeadsSDK-iOS
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/teads/TeadsSDK-android
created: '2026-05-25T00:00:00.000Z'
description: 'Outbrain Inc. (NASDAQ: OB), which closed its acquisition of Teads in early 2025 and now operates publicly as Teads, is one of the largest open-internet advertising platforms — reaching 2 billion+ consumers per month across 50+ markets, with 20,000+ direct advertisers and 10,000+ premium media properties. The combined company spans open-web native (Outbrain Amplify), premium video, display, and Connected TV (Teads), powered by a Predictive AI engine and an omnichannel data graph. Developer surface area centers on the Amplify API (campaign management + reporting), the Engage API (publisher content recommendations and the JS Widget / Mobile SDK), and a server-side Conversion API for cookieless measurement and optimization.'
examples:
- key_count: 2
  name: Outbrain List Campaigns Example
  slug: outbrain-list-campaigns-example
- key_count: 2
  name: Outbrain Realtime Report Example
  slug: outbrain-realtime-report-example
features:
- Outbrain Amplify — open-web native advertising platform with self-service and managed offerings
- Teads — premium video, display, and CTV inventory across 10,000+ media environments in 50+ markets
- Combined open-internet platform reaching 2B+ consumers/month with 20,000+ direct advertisers
- Amplify API for programmatic campaign management — Marketer, Campaign, PromotedLink, Budget, Targeting
- Performance and real-time reporting APIs (10 req/min and 50 req/min per marketer)
- OB-TOKEN-V1 bearer authentication acquired via /login HTTP Basic
- Engage API for publisher-side content recommendations (organic + paid)
- JS Widget for web (WordPress, GAM, mediation guides) and Mobile SDK for iOS / Android / React Native / Flutter
- Conversion API (server-to-server) for cookieless conversion measurement and Predictive AI optimization
- Teads Conversion API GTM server-side template (open source)
- Teads SDKs for iOS, Android, and React Native (open source on github.com/teads)
- Prebid Server fork on github.com/teads for OpenRTB / programmatic integrations
- Predictive AI engine — 1B predictions/sec across 500+ microservices, 18B ad opportunities/day, 8M req/sec
- Omnichannel Graph with audience, contextual, conversion, and purchase signals
- High-impact creative formats via Teads Studio (outstream, InRead, CTV)
- Conversion Bid Strategy for goal-based bidding in Amplify
- Direct IO, PMP deals, and open exchange paths for buy-side integrations
- Headquartered in NYC and managed in the US; combined company trades NASDAQ&#58; OB; brand consolidated as Teads
- Engineering hubs in Paris, Netanya, Montpellier, Ljubljana
finops:
- has_sources: true
  method: derived
  name: Outbrain Finops
  primary_unit: ''
  service_category: ''
  slug: outbrain-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/outbrain.png
json_schemas:
- name: Outbrain Amplify Campaign
  property_count: 12
  slug: outbrain-campaign
- name: Outbrain Amplify Promoted Link
  property_count: 9
  slug: outbrain-promoted-link
- name: Outbrain Engage Recommendation
  property_count: 8
  slug: outbrain-recommendation
json_structures:
- name: Outbrain Campaign Structure
  property_count: 1
  slug: outbrain-campaign-structure
jsonld:
- class_count: 14
  name: Outbrain Context
  property_count: 8
  slug: outbrain-context
layout: provider
modified: '2026-09-16'
name: Outbrain
nav: Providers
network: true
overview: 'Outbrain publishes 23 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Budgets API, Campaigns API, and 20 more. Tagged areas include Advertising, Native Advertising, Open Web, CTV, and Connected TV.


  The Outbrain catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Outbrain''s developer surface includes authentication, developer portal, documentation, signup flow, training material, engineering blog, support, and 78 more developer resources.'
plans:
- name: Outbrain Plans Pricing
  plan_count: 4
  slug: outbrain-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 7
  name: Outbrain Rate Limits
  slug: outbrain-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Outbrain — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: outbrain-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 45
  extends:
  - spectral:oas
  name: Outbrain API Rules
  rule_count: 4
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 2
  slug: outbrain-rules
score:
  band: exemplar
  composite: 73.3
  coverage:
    artifact_dirs: 36
    catalog_earned: 90.0
    catalog_earned_first_party: 24.0
    catalog_gap: 25.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    contract_governance: 31.8
    contract_quality: 63.8
    developer_ergonomics: 83.9
    discoverability: 71.4
    operational_transparency: 63.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 73.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/outbrain/outbrain-2026-06-20T191227.png
security:
- kind: authentication
  name: Outbrain Authentication
  slug: outbrain-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Outbrain Domain Security
  slug: outbrain-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Outbrain Vulnerability Disclosure
  slug: outbrain-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Outbrain Trust Center
  slug: outbrain-trust-center
  summary_line: SOC 2, ISO 27001
skill_count: 4
skills:
- name: Authenticate to the Outbrain Amplify API and list marketers
  slug: outbrain-authenticate-and-list-marketers
- name: Fund, launch and creative-load an Outbrain Amplify campaign
  slug: outbrain-create-campaign-and-promoted-links
- name: Pull Outbrain Amplify performance reporting
  slug: outbrain-pull-campaign-performance
- name: Run an asynchronous Teads analytics report
  slug: outbrain-run-teads-report
slug: outbrain
tags:
- Advertising
- Native Advertising
- Open Web
- CTV
- Connected TV
- Video Advertising
- Content Discovery
- Programmatic
- Performance Marketing
- AdTech
- Teads
website: https://outbrain.com
---
