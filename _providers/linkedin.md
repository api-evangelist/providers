---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 69
  human_in_the_loop: 2
  name: Linkedin Agentic Access
  operation_count: 163
  slug: linkedin-agentic-access
  summary_line: 163 operations · 69 acting · 2 human-in-the-loop
api_count: 17
apis:
- description: The LinkedIn Consumer Solutions Platform enables sites and applications the power to enhance their sign-in experience using the world's largest professional network. The Consumer Solutions Platform co
  name: LinkedIn Consumer API
  slug: linkedin-consumer-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Manage entity ACLs and assignees
  name: LinkedIn Access Control API
  phrasing_intents:
  - id: upsertEntityAcl
    intent: Create or update ATS entity access controls
    question: Can I control which recruiters see a synced requisition?
  - id: getEntityAcl
    intent: Retrieve synced ATS entity access controls
    question: Who can see a synced ATS job or candidate inside LinkedIn Recruiter?
  - id: deleteEntityAcl
    intent: Delete synced ATS entity access controls
    question: Can I remove an access control entry I previously synced?
  phrasing_ops: 3
  slug: linkedin-access-control-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs to create and manage ad accounts
  name: LinkedIn Account Management API
  phrasing_intents:
  - id: createAdAccount
    intent: Create a test or live ad account
    question: Can I create a test ad account for development?
  - id: searchAdAccounts
    intent: Search ad accounts by type or status
    question: Can I find ad accounts by name, reference or type?
  - id: getAdAccountById
    intent: Fetch an ad account by sponsored account ID
    question: What currency and status does one ad account have?
  - id: updateAdAccount
    intent: Rename or patch an ad account
    question: Can I rename an existing ad account?
  phrasing_ops: 4
  slug: linkedin-account-management-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs to retrieve and manage ad accounts
  name: LinkedIn Ad Accounts API
  phrasing_intents:
  - id: getAdAccounts
    intent: Retrieve the user's ad accounts with filters
    question: Which ad accounts does my authenticated user have on LinkedIn?
  - id: adAccounts_search
    intent: Search ad accounts with page tokens
    question: Can I page through ad account search results with a page token?
  - id: adAccounts_create
    intent: Create one or more ad accounts
    question: Can I create several ad accounts in one batch request?
  - id: adAccounts_get
    intent: Fetch one ad account by ID
    question: What are the settings of a specific ad account?
  - id: adAccounts_update
    intent: Partially update an ad account
    question: Can I change just one field on an existing ad account?
  - id: adAccounts_delete
    intent: Delete a draft ad account
    question: Can I delete an ad account that is still in draft?
  phrasing_ops: 6
  slug: linkedin-ad-accounts-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs to discover and retrieve ad targeting facets and entities
  name: LinkedIn Ad Targeting Entities API
  phrasing_intents:
  - id: getAdTargetingFacets
    intent: List available ad targeting facets
    question: Which targeting categories can I use for LinkedIn ad campaigns?
  - id: searchAdTargetingEntities
    intent: Typeahead search for targeting entities
    question: Can I find the targeting value for a job title as I type it?
  phrasing_ops: 2
  slug: linkedin-ad-targeting-entities-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Operations for retrieving advertiser transparency data for sponsored accounts
  name: LinkedIn Advertiser Transparency API
  phrasing_intents:
  - id: getAdvertiserTransparencyData
    intent: Get advertiser transparency data
    question: What spend and impressions are reported for an advertiser's account?
  phrasing_ops: 1
  slug: linkedin-advertiser-transparency-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs for retrieving child application details
  name: LinkedIn Application Retrieval API
  phrasing_intents:
  - id: getChildApplication
    intent: Get a customer's child application
    question: What credentials were provisioned for a mutual customer's child app?
  phrasing_ops: 1
  slug: linkedin-application-retrieval-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Sync job applications and related data
  name: LinkedIn Application Synchronization API
  phrasing_intents:
  - id: syncApplications
    intent: Sync job applications from an ATS
    question: Can I push job application records from my ATS into LinkedIn?
  - id: createResumeUploadUrl
    intent: Create a signed URL for a resume upload
    question: Where do I upload a candidate's resume file for an application?
  phrasing_ops: 2
  slug: linkedin-application-synchronization-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs for updating child application configurations
  name: LinkedIn Application Updates API
  phrasing_intents:
  - id: updateChildApplicationCallbackUrls
    intent: Update a child application's OAuth callback URLs
    question: Can I change the redirect URLs on a customer's child application?
  phrasing_ops: 1
  slug: linkedin-application-updates-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs for creating and managing Apply Connect enabled job postings
  name: LinkedIn Apply Connect Jobs API
  phrasing_intents:
  - id: createOrUpdateJobPosting
    intent: Create, update or close Apply Connect jobs
    question: Can I post a job that candidates apply to without leaving LinkedIn?
  phrasing_ops: 1
  slug: linkedin-apply-connect-jobs-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs to retrieve audience counts based on targeting criteria
  name: LinkedIn Audience Counts API
  phrasing_intents:
  - id: getAudienceCount
    intent: Count members matching targeting criteria
    question: How many members would my targeting reach?
  phrasing_ops: 1
  slug: linkedin-audience-counts-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs to fetch audience insights based on targeting criteria
  name: LinkedIn Audience Insights API
  phrasing_intents:
  - id: getAudienceInsights
    intent: Get demographic insights for a target audience
    question: What job functions and industries make up my target audience?
  phrasing_ops: 1
  slug: linkedin-audience-insights-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: OAuth 2.0 token management for customer applications
  name: LinkedIn Authentication API
  phrasing_intents:
  - id: getAccessToken
    intent: Get a client credentials access token
    question: Can a customer application get an access token without a user login?
  phrasing_ops: 1
  slug: linkedin-authentication-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Business manager account relationships
  name: LinkedIn Business Manager API
  phrasing_intents:
  - id: getBusinessManagerRelationships
    intent: Get Business Manager account relationships
    question: Which organizations are linked to a Business Manager account?
  phrasing_ops: 1
  slug: linkedin-business-manager-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs to create and manage campaign groups
  name: LinkedIn Campaign Group Management API
  phrasing_intents:
  - id: searchCampaignGroups
    intent: Search campaign groups in an ad account
    question: Which campaign groups exist in my ad account?
  - id: deleteCampaignGroups
    intent: Delete several draft campaign groups
    question: Can I delete multiple draft campaign groups in one call?
  - id: getCampaignGroupById
    intent: Fetch a campaign group by ID
    question: What budget and schedule does one campaign group have?
  - id: updateCampaignGroup
    intent: Partially update a campaign group
    question: Can I change a campaign group's name or status without resending everything?
  - id: deleteCampaignGroup
    intent: Delete a single draft campaign group
    question: Can I delete one campaign group that was never launched?
  phrasing_ops: 5
  slug: linkedin-campaign-group-management-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs to create and manage campaigns
  name: LinkedIn Campaign Management API
  phrasing_intents:
  - id: searchCampaigns
    intent: Search campaigns, optionally by campaign group
    question: Which campaigns belong to a specific campaign group?
  - id: getCampaignById
    intent: Fetch a campaign by ID
    question: What are the settings of one campaign in my account?
  - id: archiveCampaign
    intent: Archive a campaign
    question: Can I archive a campaign I no longer run?
  phrasing_ops: 3
  slug: linkedin-campaign-management-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Sync candidate data from ATS to LinkedIn
  name: LinkedIn Candidate Synchronization API
  phrasing_intents:
  - id: syncCandidates
    intent: Sync candidates from an ATS
    question: Can I push candidate records from my ATS into LinkedIn?
  - id: getCandidateMatches
    intent: Retrieve candidate matches with members
    question: Which LinkedIn members has a synced ATS candidate been matched to?
  phrasing_ops: 2
  slug: linkedin-candidate-synchronization-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs for provisioning and managing customer (child) applications
  name: LinkedIn Child Application Provisioning API
  phrasing_intents:
  - id: provisionChildApplication
    intent: Provision a child application for a customer
    question: Can I create a LinkedIn developer app for one of my customers?
  phrasing_ops: 1
  slug: linkedin-child-application-provisioning-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs to stream company data for account targeting
  name: LinkedIn Company Streaming API
  phrasing_intents:
  - id: streamCompaniesToSegment
    intent: Add or remove companies in a DMP segment
    question: Can I stream a list of target companies into an audience segment?
  phrasing_ops: 1
  slug: linkedin-company-streaming-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs to opt-in and opt-out members for compliance monitoring on LinkedIn
  name: LinkedIn Compliance Authorization API
  phrasing_intents:
  - id: optInMemberForCompliance
    intent: Opt a member in to compliance monitoring
    question: Can I start archiving a regulated member's LinkedIn activity?
  - id: checkMemberRegulationStatus
    intent: Check if a member is opted in to compliance
    question: Is this member currently under compliance monitoring?
  - id: optOutMemberFromCompliance
    intent: Opt a member out of compliance monitoring
    question: Can I stop monitoring a member's activity for compliance?
  phrasing_ops: 3
  slug: linkedin-compliance-authorization-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs to retrieve compliance events for regulated members
  name: LinkedIn Compliance Events API
  phrasing_intents:
  - id: getComplianceEvents
    intent: Retrieve compliance events for a regulated member
    question: What activity has a regulated member posted that I need to archive?
  phrasing_ops: 1
  slug: linkedin-compliance-events-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: 1. Obtain user authorization with consent to create and manage conversions using `rw_conversions`, `r_ads` permissions in the scope. 2. Retrieve authenticated user's sponsored Ad Accounts where user h
  name: LinkedIn Conversion Events Streaming Workflow API
  phrasing_intents:
  - id: getRetrieveAuthenticatedUsersSponsored
    intent: List ad accounts the user can stream conversions to
    question: Which sponsored ad accounts can the signed-in user send conversions for?
  - id: getFetchExistingConversionRules
    intent: List conversion rules in an ad account
    question: Which conversion rules already exist in my ad account?
  - id: postCreateANewConversion
    intent: Create a conversion rule for API streaming
    question: Can I create a new conversion rule that accepts server-side events?
  - id: getFetchActiveCampaigns
    intent: List active campaigns in a sponsored account
    question: Which campaigns are active in my ad account so I can attach a conversion?
  - id: putAssociateCampaignsToConversion
    intent: Associate a campaign with a conversion rule
    question: How can I make a campaign track a specific conversion rule?
  - id: postStreamMultipleConversionEvents
    intent: Stream conversion events to a rule
    question: Can I send several conversion events to a rule in one request?
  phrasing_ops: 6
  slug: linkedin-conversion-events-streaming-workflow-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs to create and manage ad creatives
  name: LinkedIn Creative Management API
  phrasing_intents:
  - id: createCreative
    intent: Create an ad creative for a campaign
    question: Can I add a new creative to a specific campaign?
  phrasing_ops: 1
  slug: linkedin-creative-management-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Create and manage CRM data validation export jobs
  name: LinkedIn CRM Data Validation API
  phrasing_intents:
  - id: createCrmDataValidationExportJob
    intent: Start a CRM data validation export
    question: Can I check my CRM records against LinkedIn for outdated contacts?
  - id: getCrmDataValidationExportJob
    intent: Check a CRM data validation export job
    question: Has my CRM data validation export finished?
  phrasing_ops: 2
  slug: linkedin-crm-data-validation-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs for managing customer ATS integrations for premium job posting
  name: LinkedIn Customer Integrations API
  phrasing_intents:
  - id: updateCustomerIntegrations
    intent: Update a customer's ATS integration
    question: Can I rename a customer's premium job posting integration?
  - id: getCustomerIntegrations
    intent: Get a customer's ATS integration details
    question: Is a customer's ATS integration for premium job posting configured correctly?
  phrasing_ops: 2
  slug: linkedin-customer-integrations-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Delete synced data from LinkedIn
  name: LinkedIn Data Deletion API
  phrasing_intents:
  - id: deleteCandidates
    intent: Delete synced candidates
    question: Can I remove candidate records I previously synced to LinkedIn?
  - id: deleteApplications
    intent: Delete synced job applications
    question: Can I remove job applications I previously synced?
  phrasing_ops: 2
  slug: linkedin-data-deletion-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Retrieve exported candidates and recruiter interactions
  name: LinkedIn Data Retrieval API
  phrasing_intents:
  - id: getExportedCandidates
    intent: Get candidates exported with One-Click Export
    question: Which candidate profiles came through a One-Click Export request?
  - id: getRecruiterSeatholders
    intent: List Recruiter seat holders on a contract
    question: Who holds Recruiter seats on our contract?
  phrasing_ops: 2
  slug: linkedin-data-retrieval-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs to create and manage DMP segments for audience targeting
  name: LinkedIn DMP Segments API
  phrasing_intents:
  - id: getDmpSegments
    intent: Monitor DMP segments for an ad account
    question: What's the match rate and audience size of my uploaded segments?
  - id: createDmpSegment
    intent: Create a DMP segment
    question: Can I create a matched audience segment for list uploads or streaming?
  phrasing_ops: 2
  slug: linkedin-dmp-segments-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Events and live video data
  name: LinkedIn Events API
  phrasing_intents:
  - id: getEvents
    intent: Get events hosted by an organizer
    question: Which events has an organization hosted?
  phrasing_ops: 1
  slug: linkedin-events-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Posts, reactions, comments, and social metadata
  name: LinkedIn Feed Content API
  phrasing_intents:
  - id: getPosts
    intent: Get an organization's posts for data portability
    question: Can I export all posts published by an organization?
  - id: getReactions
    intent: Get reactions on a piece of content
    question: Who reacted to a post, and with which reaction type?
  - id: getComments
    intent: Get comments on a piece of content
    question: Can I export the comments left on a post?
  phrasing_ops: 3
  slug: linkedin-feed-content-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Media Planning API can help Media Planners understand the reach and ROI that LinkedIn can offer to their client. It allows them to make budget allocation recommendations with confidence and know how t
  name: LinkedIn Fetch Media Plan API
  phrasing_intents:
  - id: postForecastAvgLifetimeFrequency
    intent: Forecast average lifetime ad frequency
    question: How often would each member see my ads over a campaign's life?
  phrasing_ops: 1
  slug: linkedin-fetch-media-plan-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Configure and manage customer ATS integrations
  name: LinkedIn Integration Configuration API
  phrasing_intents:
  - id: updateAtsIntegration
    intent: Update a Recruiter System Connect integration
    question: Can I turn on One-Click Export or the profile plugin for a customer?
  - id: getIntegrationNotification
    intent: Get an integration status change notification
    question: What changed when a customer enabled or modified their integration?
  phrasing_ops: 2
  slug: linkedin-integration-configuration-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs for managing the lifecycle of job postings
  name: LinkedIn Job Lifecycle Management API
  phrasing_intents:
  - id: getJobPostingTaskStatus
    intent: Check the status of a job posting task
    question: Did my job posting get created, updated or closed successfully?
  phrasing_ops: 1
  slug: linkedin-job-lifecycle-management-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Lead generation forms and responses
  name: LinkedIn Lead Generation API
  phrasing_intents:
  - id: getLeadGenResponses
    intent: Export lead gen form responses
    question: Can I export every lead form submission for data portability?
  phrasing_ops: 1
  slug: linkedin-lead-generation-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs to retrieve learning activity reports including completions, views, and logins
  name: LinkedIn Learning Activity Reports API
  phrasing_intents:
  - id: getLearningActivityReports
    intent: Get LinkedIn Learning activity reports
    question: How many courses did our learners complete last month?
  phrasing_ops: 1
  slug: linkedin-learning-activity-reports-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs to upload and attach CSV lists to DMP segments
  name: LinkedIn List Uploads API
  phrasing_intents:
  - id: attachListToSegment
    intent: Attach an uploaded list to a DMP segment
    question: Can I attach a CSV of contacts I uploaded to an audience segment?
  phrasing_ops: 1
  slug: linkedin-list-uploads-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Organization ACLs and authorization data
  name: LinkedIn Organization Access Control API
  phrasing_intents:
  - id: getOrganizationAcls
    intent: Export organization role assignments
    question: Who are the administrators and content managers of our organization?
  phrasing_ops: 1
  slug: linkedin-organization-access-control-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Organization profile data retrieval
  name: LinkedIn Organizations API
  phrasing_intents:
  - id: batchGetOrganizations
    intent: Batch get organization profiles
    question: Can I export several company profiles in one request for data portability?
  - id: getOrganization
    intent: Get one organization profile
    question: What profile and settings data does one organization have?
  phrasing_ops: 2
  slug: linkedin-organizations-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Organizational page content and edge analytics
  name: LinkedIn Page Analytics API
  phrasing_intents:
  - id: getPageContentAnalytics
    intent: Get content analytics for an organization page
    question: What impressions and clicks did our company page content get?
  phrasing_ops: 1
  slug: linkedin-page-analytics-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Fetch Sales Navigator profile associations from CRM records
  name: LinkedIn Profile Associations API
  phrasing_intents:
  - id: getProfileAssociation
    intent: Fetch the profile matched to a CRM record
    question: Which Sales Navigator profile is matched to one of my CRM records?
  - id: batchGetProfileAssociations
    intent: Batch fetch profile matches for CRM records
    question: Can I get profile matches for many CRM records at once?
  phrasing_ops: 2
  slug: linkedin-profile-associations-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Retrieve sales access tokens for authenticated iframe sessions
  name: LinkedIn Sales Access Tokens API
  phrasing_intents:
  - id: getSalesAccessToken
    intent: Get a short-lived token for Sales iframe sessions
    question: Can I get a limited-scope token to embed Sales Navigator in an iframe?
  phrasing_ops: 1
  slug: linkedin-sales-access-tokens-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Create and manage sales analytics export jobs
  name: LinkedIn Sales Analytics Export API
  phrasing_intents:
  - id: getSalesAnalyticsExportJob
    intent: Check a sales analytics export job
    question: Is my Sales Navigator analytics export ready to download?
  - id: createSalesAnalyticsExportJob
    intent: Start a sales analytics export job
    question: Can I export seat activity data for a date range?
  phrasing_ops: 2
  slug: linkedin-sales-analytics-export-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Manage and retrieve Sales Navigator contracts
  name: LinkedIn Sales Contracts API
  phrasing_intents:
  - id: getContractsByMember
    intent: Find contracts where the user holds a seat
    question: Which Sales Navigator contracts is the signed-in user seated on?
  phrasing_ops: 1
  slug: linkedin-sales-contracts-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: This template provides detailed conversion analyses, ideal for in-flight optimization, check-ins, QBRs
  name: LinkedIn Use Cases > B2B Templates > Conversions Deep Dive API
  phrasing_intents:
  - id: getConversionsByMemberCompany
    intent: Report conversions by member company size
    question: Which company sizes drive the most conversions for my ads?
  phrasing_ops: 1
  slug: linkedin-use-cases-b2b-templates-conversions-deep-dive-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Linkedin is introducing its next generation of APIs to create and manage Conversation Ads, enabling advertisers to better deliver automated messages to a targeted LinkedIn member's inbox. This API rep
  name: LinkedIn Use Cases > Conversation Ad > Sponsored Conversations API
  phrasing_intents:
  - id: postCreateASponsoredConversation
    intent: Create a sponsored conversation
    question: Can I create a new conversation ad shell before adding messages?
  - id: getGetMultipleSponsoredConversations
    intent: Batch get sponsored conversations
    question: Can I look up several sponsored conversations at once?
  - id: getGetASponsoredConversation
    intent: Get one sponsored conversation
    question: Which ad account owns a particular conversation ad?
  - id: postUpdateASponsoredConversation
    intent: Update a sponsored conversation
    question: Can I change which message opens my conversation ad?
  phrasing_ops: 4
  slug: linkedin-use-cases-conversation-ad-sponsored-conversations-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Within our API, Conversation Ads are represented by the Sponsored Conversation entity. Sponsored Conversations are composed of Sponsored Message Content.
  name: LinkedIn Use Cases > Conversation Ad > Sponsored Message Contents API
  phrasing_intents:
  - id: postBatchCreateSponsoredMessage
    intent: Batch create messages for a conversation ad
    question: Can I add several messages to a conversation ad at once?
  - id: getGetSponsoredMessageContent
    intent: Get one message from a conversation ad
    question: Can I read the text of a single message in a conversation ad?
  - id: postUpdateSponsoredMessageContent
    intent: Update one message in a conversation ad
    question: Can I edit the wording of one message in my conversation ad?
  - id: getBatchGetSponsoredMessage
    intent: Batch get messages in a conversation ad
    question: Can I fetch several messages from a conversation ad in one call?
  - id: postBatchUpdateSponsoredMessage
    intent: Batch update messages in a conversation ad
    question: Can I update many conversation ad messages in one request?
  - id: deleteBatchDeleteSponsoredMessage
    intent: Batch delete messages from a conversation ad
    question: Can I remove several messages from a conversation ad at once?
  phrasing_ops: 6
  slug: linkedin-use-cases-conversation-ad-sponsored-message-contents-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: 'The Creatives API contains all the data and information for visually rendering an ad. There are several types of Ad Creatives that you can associate with campaigns including:'
  name: LinkedIn Use Cases > Creatives API
  phrasing_intents:
  - id: getSearchForCreative
    intent: Search ad creatives by campaign or account
    question: Which creatives are running in a given campaign?
  - id: getGetASponsoredCreative
    intent: Get a sponsored creative
    question: What status and content does one creative have?
  - id: postUpdateACreative
    intent: Update a creative's status or call to action
    question: Can I pause a creative by changing its intended status?
  - id: deleteDeleteACreative
    intent: Delete a creative
    question: Can I delete a creative that has never served?
  phrasing_ops: 4
  slug: linkedin-use-cases-creatives-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: The Use Cases > Document Ad API from LinkedIn — 5 operation(s) for use cases > document ad.
  name: LinkedIn Use Cases > Document Ad API
  phrasing_intents:
  - id: putUploadTheDocumentFile
    intent: Upload a document file to the upload URL
    question: After initializing, how do I send the actual document file bytes?
  - id: getGetMultipleDocuments
    intent: Get several uploaded documents at once
    question: Can I check the status of several uploaded documents together?
  - id: postCreateDocumentContent
    intent: Create a document ad post
    question: Once my document is uploaded, can I turn it into a sponsored post?
  - id: getFetchMultipleDocumentContent
    intent: Fetch several document ad posts
    question: Can I retrieve the posts behind several document ads together?
  - id: postInitializeDocumentUpload
    intent: Initialize a document upload
    question: Can I get an upload URL before sending a document for an ad?
  - id: getGetASingleDocument
    intent: Get one uploaded document
    question: Is my uploaded document ready to use in an ad?
  phrasing_ops: 6
  slug: linkedin-use-cases-document-ad-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: 'Image ads help you engage business decision-makers on LinkedIn''s mobile and desktop news feed. You can create image ads in two ways: \* Post images to your Company Page and sponsor the post to reach m'
  name: LinkedIn Use Cases > Image Ad API
  phrasing_intents:
  - id: postInitializeImageUpload
    intent: Initialize an image upload
    question: Can I get an upload URL before sending an image for an ad?
  - id: getGetASingleImage
    intent: Get one uploaded image
    question: Is my uploaded image ready to use in an ad?
  - id: getFetchMultipleImageContent
    intent: Fetch several image ad posts
    question: Can I retrieve several image ad posts in one call?
  - id: getGetImageContent
    intent: Get the post behind one image ad
    question: Which post content is attached to a specific image ad?
  phrasing_ops: 4
  slug: linkedin-use-cases-image-ad-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: You can set up the message contents sent to targeted LinkedIn members' inbox, either as a Message Ad or a Conversation Ad.
  name: LinkedIn Use Cases > InMail Content API
  phrasing_intents:
  - id: postCreateInmailContent
    intent: Create InMail ad content
    question: Can I create the message content for a sponsored InMail?
  - id: getGetInmailContent
    intent: Get one InMail content item
    question: What does a specific InMail content item contain?
  - id: postUpdateInmailContent
    intent: Update an InMail content item
    question: Can I edit an InMail's content after creating it?
  - id: getBatchGetInmailContent
    intent: Batch get InMail content items
    question: Can I fetch several InMail contents in one request?
  - id: postSendTestInmail
    intent: Send a test InMail
    question: Can I send myself a test copy of an InMail before launch?
  phrasing_ops: 5
  slug: linkedin-use-cases-inmail-content-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: The Use Cases > Organization Access Controls API from LinkedIn — 1 operation(s) for use cases > organization access controls.
  name: LinkedIn Use Cases > Organization Access Controls API
  phrasing_intents:
  - id: getFindOrganizationAccessControl
    intent: Find who has roles on an organization
    question: Which members administer a given company page?
  phrasing_ops: 1
  slug: linkedin-use-cases-organization-access-controls-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: The Use Cases > Organization Followers API from LinkedIn — 2 operation(s) for use cases > organization followers.
  name: LinkedIn Use Cases > Organization Followers API
  phrasing_intents:
  - id: getSearchByKeyword
    intent: Search an organization's followers by keyword
    question: Can I find a follower of my company page by name?
  - id: getSearchByVanityUrl
    intent: Find a follower by vanity URL
    question: Does the member with this profile URL follow my company page?
  phrasing_ops: 2
  slug: linkedin-use-cases-organization-followers-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: The Use Cases > Organization Lookup > Organization Brands API from LinkedIn — 4 operation(s) for use cases > organization lookup > organization brands.
  name: LinkedIn Use Cases > Organization Lookup > Organization Brands API
  phrasing_intents:
  - id: getFindAdministeredOrganizationBrands
    intent: Find brands under a parent organization
    question: Which brand pages belong to a parent company I administer?
  - id: getBatchGetOnAdministered
    intent: Batch get brands I administer
    question: Can I fetch several organization brands I manage at once?
  - id: getRetrieveAnAdministeredOrganization
    intent: Retrieve one brand I administer
    question: What does one of my administered brand pages look like?
  - id: getBatchGetOnNonadministered
    intent: Look up brands I don't administer
    question: Can I look up public details of brands I don't manage?
  phrasing_ops: 4
  slug: linkedin-use-cases-organization-lookup-organization-brands-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: The Use Cases > Organization Lookup > Organizations API from LinkedIn — 3 operation(s) for use cases > organization lookup > organizations.
  name: LinkedIn Use Cases > Organization Lookup > Organizations API
  phrasing_intents:
  - id: getLookupByOrganizationPrimary
    intent: Look up an organization by ID
    question: What details does a company page have, given its organization ID?
  - id: getFindNonadministeredOrganization
    intent: Find organizations I don't administer
    question: Can I look up public details of companies I don't manage?
  - id: getRetrieveOrganizationFollowerCount
    intent: Get an organization's follower count
    question: How many followers does a company page have?
  phrasing_ops: 3
  slug: linkedin-use-cases-organization-lookup-organizations-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: The Posts API facilities the creation and retrieval of organic and sponsored posts.
  name: LinkedIn Use Cases > Posts API
  phrasing_intents:
  - id: getGetPostsByUrn
    intent: Get a post by URN
    question: Can I retrieve a post using its share or UGC post URN?
  - id: deleteDeleteAPost
    intent: Delete a post
    question: Can I delete a post I published?
  - id: postUpdateAPost
    intent: Update a post's commentary or ad details
    question: Can I edit a post's commentary after publishing?
  phrasing_ops: 3
  slug: linkedin-use-cases-posts-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Notifications for the authenticated member’s organizations can be queried using a criteria finder. Notifications are retained and available to pull for 60 days.
  name: LinkedIn Use Cases > Social Actions Notifications > Organization Social Actions Notifications - Pull Workflow API
  phrasing_intents:
  - id: postCreateAShareWith
    intent: Create a share that mentions a company
    question: Can I publish a share that tags a company page?
  - id: getRetrieveNotificationsForThe
    intent: Pull social action notifications for my organization
    question: Which likes, comments and mentions has my company page received?
  phrasing_ops: 2
  slug: linkedin-use-cases-social-actions-notifications-organization-social-actions-notifications-pull-workflow-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Registered webhook URLs will receive notifications from LinkedIn for subscribed events.
  name: LinkedIn Use Cases > Social Actions Notifications > Organization Social Actions Notifications - Push Workflow API
  phrasing_intents:
  - id: putCreateASubscriptionRequest
    intent: Subscribe to organization social action webhooks
    question: Can I get webhook pushes when people like or comment on my company page posts?
  - id: getRetrieveSubscriptionByKey
    intent: Retrieve an organization notification subscription
    question: What webhook URL and expiration does my notification subscription have?
  - id: deleteRemoveASubscription
    intent: Remove an organization notification subscription
    question: Can I stop receiving social action webhooks for a company page?
  phrasing_ops: 3
  slug: linkedin-use-cases-social-actions-notifications-organization-social-actions-notifications-push-workflow-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: 'In order to support collecting leads for sponsored use cases, a partner app needs to build a UX where a user is able to select the sponsored accounts and forms to collect leads for. ###### Step 1: Obt'
  name: LinkedIn Use Cases > Sponsored API
  phrasing_intents:
  - id: getValidateTheUsersOrganization
    intent: Check a user's roles on organization pages
    question: Which company pages does the signed-in member hold an admin role on?
  - id: getGetFormsForThe
    intent: List lead gen forms for a sponsored account
    question: Which lead gen forms exist on the ad account I picked for lead sync?
  - id: getSchedulePeriodicFormResponse
    intent: Pull lead form responses on a schedule
    question: How can I pull all new leads for a sponsored account on a recurring schedule?
  - id: postSubscribeForLeadNotification
    intent: Register a webhook for new lead notifications
    question: Can I get a webhook call whenever a new lead form is submitted?
  - id: getFetchFullLeadData
    intent: Fetch one lead's full form response
    question: After a lead webhook fires, how do I get the full answers for that lead?
  - id: deletePushDeleteARegistered
    intent: Delete a registered lead notification webhook
    question: Can I remove a lead notification webhook I registered earlier?
  - id: getGetTheUsersSponsored
    intent: Search the user's sponsored ad accounts
    question: Which sponsored ad accounts can the signed-in user choose from for lead sync?
  phrasing_ops: 7
  slug: linkedin-use-cases-sponsored-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Spotlight Ads allow you to showcase your product, service, event, content, and more. Upon clicking your Ad, you navigate to the website or landing page of your choice. Learn more about [Spotlight Ads]
  name: LinkedIn Use Cases > Spotlight Ad API
  phrasing_intents:
  - id: postCreateADynamicSpotlight
    intent: Create a dynamic spotlight ad
    question: Can I create a spotlight ad that personalizes with the viewer's photo?
  - id: getGetADynamicSpotlight
    intent: Get a dynamic spotlight ad
    question: Why is my spotlight ad on serving hold?
  - id: postUpdateADynamicSpotlight
    intent: Update a dynamic spotlight ad
    question: Can I change the status of a spotlight ad?
  - id: deleteDeleteADynamicSpotlight
    intent: Delete a dynamic spotlight ad
    question: Can I delete a spotlight ad creative?
  phrasing_ops: 4
  slug: linkedin-use-cases-spotlight-ad-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: This API describes usage of Organization Follower Statistics. Fore more details, check [here](https://docs.microsoft.com/en-us/linkedin/marketing/integrations/community-management/organizations/follow
  name: LinkedIn Use Cases > Statistics APIs > Organization Follower Statistics API
  phrasing_intents:
  - id: getTimeboundFollowerStatistics
    intent: Get follower gains over a time range
    question: How many followers did our page gain each day last month?
  phrasing_ops: 1
  slug: linkedin-use-cases-statistics-apis-organization-follower-statistics-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: This API describes usage of Organization Page Statistics. Fore more details, check [here](https://docs.microsoft.com/en-us/linkedin/marketing/integrations/community-management/organizations/page-stati
  name: LinkedIn Use Cases > Statistics APIs > Organization Page Statistics API
  phrasing_intents:
  - id: getLifetimePageStatistics
    intent: Get lifetime page view statistics
    question: How many page views has our company page had overall?
  phrasing_ops: 1
  slug: linkedin-use-cases-statistics-apis-organization-page-statistics-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: This API describes usage of Organization Share Statistics. Fore more details, check [here](https://docs.microsoft.com/en-us/linkedin/marketing/integrations/community-management/organizations/share-sta
  name: LinkedIn Use Cases > Statistics APIs > Organization Share Statistics API
  phrasing_intents:
  - id: getTimeBoundShareStatistics
    intent: Get post engagement over a time range
    question: What impressions and clicks did our page's posts get last week?
  phrasing_ops: 1
  slug: linkedin-use-cases-statistics-apis-organization-share-statistics-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: The Videos API is a new offering from LinkedIn that features the ability to upload a captions file as well as thumbnail video functionality.
  name: LinkedIn Use Cases > Video Ad API
  phrasing_intents:
  - id: getGetMultipleVideos
    intent: Get several uploaded videos
    question: Can I check the status of several videos together?
  - id: postInitializeVideoUpload
    intent: Initialize a video upload
    question: Can I get upload instructions before sending a video for an ad?
  - id: getGetASingleVideo
    intent: Get one uploaded video
    question: Is a specific uploaded video ready to use?
  phrasing_ops: 3
  slug: linkedin-use-cases-video-ad-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs to manage ad account user access and roles
  name: LinkedIn User Access API
  phrasing_intents:
  - id: createAdAccountUser
    intent: Grant a member access to an ad account
    question: Can I give a colleague access to my ad account with a chosen role?
  - id: getAdAccountUser
    intent: Fetch a member's access on an ad account
    question: What role does a specific person have on one ad account?
  - id: updateAdAccountUser
    intent: Change a member's role on an ad account
    question: Can I change someone's existing role on an ad account?
  - id: deleteAdAccountUser
    intent: Remove a member from an ad account
    question: Can I revoke a person's access to my ad account?
  - id: getAuthenticatedUserAdAccounts
    intent: List ad accounts the current user can access
    question: Which ad accounts do I personally have access to?
  - id: getOrganizationAcls
    intent: List the current user's organization roles
    question: Which company pages am I an administrator of?
  phrasing_ops: 6
  slug: linkedin-user-access-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: APIs to stream user data for contact targeting
  name: LinkedIn User Streaming API
  phrasing_intents:
  - id: streamUsersToSegment
    intent: Add or remove users in a DMP segment
    question: Can I stream contacts into a matched audience segment in real time?
  phrasing_ops: 1
  slug: linkedin-user-streaming-api
- description: The LinkedIn Marketing API enables programmatic management of LinkedIn advertising campaigns, audience targeting, creative assets, and performance reporting. Developers can create sponsored content, m
  name: LinkedIn Marketing API
  slug: marketing-api
- description: The LinkedIn Talent Solutions API provides access to recruiting and talent management capabilities. It enables integration with applicant tracking systems, job posting management, candidate search, an
  name: LinkedIn Talent Solutions API
  slug: talent-solutions-api
- baseURL: https://api.linkedin.com/v2/
  baseurl_source: declared
  description: Manage ad account user permissions
  name: Microsoft LinkedIn AdAccountUsers API
  phrasing_intents:
  - id: adAccountUsers_find
    intent: Find users on ad accounts
    question: Who has access to a given ad account?
  phrasing_ops: 1
  slug: microsoft-linkedin-adaccountusers-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Manage campaign groups
  name: LinkedIn Ad Campaign Groups API
  phrasing_intents:
  - id: adCampaignGroups_search
    intent: Search campaign groups in an ad account
    question: Which campaign groups sit under my ad account?
  - id: adCampaignGroups_create
    intent: Create a campaign group
    question: Can I create a new campaign group to organize campaigns?
  - id: adCampaignGroups_get
    intent: Get a campaign group
    question: What are the settings of one campaign group?
  - id: adCampaignGroups_update
    intent: Partially update a campaign group
    question: Can I change one field on a campaign group?
  phrasing_ops: 4
  slug: linkedin-ad-campaign-groups-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Manage campaigns
  name: LinkedIn Ad Campaigns API
  phrasing_intents:
  - id: adCampaigns_search
    intent: Search campaigns in an ad account
    question: Which campaigns are running in my ad account?
  - id: adCampaigns_create
    intent: Create an ad campaign
    question: Can I create a campaign with a daily budget and targeting?
  - id: adCampaigns_get
    intent: Get a campaign
    question: What budget and targeting does one campaign use?
  - id: adCampaigns_update
    intent: Partially update a campaign
    question: Can I change a campaign's budget without recreating it?
  phrasing_ops: 4
  slug: linkedin-ad-campaigns-api
- baseURL: https://api.linkedin.com
  baseurl_source: declared
  description: Manage creatives
  name: LinkedIn Ad Creatives API
  phrasing_intents:
  - id: adCreatives_search
    intent: Search creatives in an ad account
    question: Which creatives belong to my ad account?
  - id: adCreatives_create
    intent: Create a creative in an ad account
    question: Can I add a new creative to a campaign in my ad account?
  - id: adCreatives_get
    intent: Get a creative
    question: What content and status does one creative have?
  phrasing_ops: 3
  slug: linkedin-ad-creatives-api
arazzos:
- description: Confirm an organization exists and then publish a text share authored by it.
  name: LinkedIn Create an Organization Share
  slug: linkedin-create-organization-share-workflow
- description: Read a post by URN, and when it exists delete it idempotently.
  name: LinkedIn Delete an Organization Post
  slug: linkedin-delete-organization-post-workflow
- description: Pull an organization's posts, then export the reactions and comments on a chosen activity.
  name: LinkedIn Export Post Engagement
  slug: linkedin-export-post-engagement-workflow
- description: Resolve an organization by its vanity URL, then typeahead-search its followers by keyword.
  name: LinkedIn Find Organization and People
  slug: linkedin-find-org-and-people-workflow
- description: Confirm organization access, then list the administered brands under that parent organization.
  name: LinkedIn Organization Access and Brands
  slug: linkedin-org-access-and-brands-workflow
- description: Resolve an organization, then pull time-bound follower statistics for a date range.
  name: LinkedIn Organization Follower Analytics
  slug: linkedin-organization-follower-analytics-workflow
- description: Resolve an organization, then gather its follower count and lifetime page statistics.
  name: LinkedIn Organization Profile Overview
  slug: linkedin-organization-profile-overview-workflow
- description: Resolve an organization, then pull time-bound share statistics for a date range.
  name: LinkedIn Organization Share Analytics
  slug: linkedin-organization-share-analytics-workflow
- description: Create an organization post, then read it back by URN to confirm it published.
  name: LinkedIn Publish and Verify a Post
  slug: linkedin-publish-and-verify-post-workflow
- description: Confirm organization access, then pull pending social action notifications.
  name: LinkedIn Pull Social Action Notifications
  slug: linkedin-pull-social-action-notifications-workflow
- description: Register a webhook subscription for organization social actions, then read it back.
  name: LinkedIn Subscribe to Social Action Notifications
  slug: linkedin-subscribe-social-action-notifications-workflow
- description: Read a post by URN, and when it exists patch its commentary and call to action.
  name: LinkedIn Update an Organization Post
  slug: linkedin-update-organization-post-workflow
- description: Register a document upload, push the file bytes, then publish a document post.
  name: LinkedIn Upload a Document and Create a Post
  slug: linkedin-upload-document-and-create-post-workflow
- description: Register an image upload, confirm the image asset, then publish a post that references it.
  name: LinkedIn Upload an Image and Create a Post
  slug: linkedin-upload-image-and-create-post-workflow
- description: Register a video upload for an owner, then confirm the resulting video asset resolves.
  name: LinkedIn Upload a Video and Verify the Asset
  slug: linkedin-upload-video-and-verify-workflow
artifact_total: 988
asyncapis:
- description: ''
  name: Linkedin Webhooks
  slug: linkedin-webhooks
collections:
- collection_type: postman
  name: LinkedIn Compliance Events API
  slug: postman-linkedin-compliance-events
- collection_type: postman
  name: LinkedIn Learning Activity Reports API
  slug: postman-linkedin-learning-activity-reports
- collection_type: postman
  name: LinkedIn Marketing Audience Insights API
  slug: postman-linkedin-marketing-audience-insights
- collection_type: postman
  name: LinkedIn Marketing Audiences API
  slug: postman-linkedin-marketing-audience
- collection_type: postman
  name: LinkedIn Marketing Campaign Management API
  slug: postman-linkedin-marketing-campaigns
- collection_type: postman
  name: Community Management
  slug: postman-linkedin-marketing-community
- collection_type: postman
  name: Content APIs
  slug: postman-linkedin-marketing-content
- collection_type: postman
  name: Conversions API
  slug: postman-linkedin-marketing-conversions
- collection_type: postman
  name: Lead Sync
  slug: postman-linkedin-marketing-leads
- collection_type: postman
  name: Media Planning
  slug: postman-linkedin-marketing-media-planning
- collection_type: postman
  name: Reporting & ROI
  slug: postman-linkedin-marketing-reporting-roi
- collection_type: postman
  name: LinkedIn Pages Data Portability API
  slug: postman-linkedin-regulations-data-portability
- collection_type: postman
  name: LinkedIn Ads Transparency API
  slug: postman-linkedin-regulatory-ads-transparency
- collection_type: postman
  name: LinkedIn Sales Navigator API
  slug: postman-linkedin-sales-navigator
- collection_type: postman
  name: LinkedIn Job Posting API
  slug: postman-linkedin-talent-job-posting
- collection_type: postman
  name: LinkedIn Parent Application Management API
  slug: postman-linkedin-talent-learning-parent-application
- collection_type: postman
  name: LinkedIn Recruiter System Connect API
  slug: postman-linkedin-talent-recruiter-system-connect
- collection_type: open
  name: LinkedIn Compliance Events Access Control API
  slug: open-linkedin-access-control-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Account Management API
  slug: open-linkedin-account-management-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Ad Accounts API
  slug: open-linkedin-ad-accounts-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Ad Targeting Entities API
  slug: open-linkedin-ad-targeting-entities-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Advertiser Transparency API
  slug: open-linkedin-advertiser-transparency-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Application Retrieval API
  slug: open-linkedin-application-retrieval-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Application Synchronization API
  slug: open-linkedin-application-synchronization-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Application Updates API
  slug: open-linkedin-application-updates-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Apply Connect Jobs API
  slug: open-linkedin-apply-connect-jobs-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Audience Counts API
  slug: open-linkedin-audience-counts-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Audience Insights API
  slug: open-linkedin-audience-insights-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Authentication API
  slug: open-linkedin-authentication-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Business Manager API
  slug: open-linkedin-business-manager-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Campaign Group Management API
  slug: open-linkedin-campaign-group-management-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Campaign Management API
  slug: open-linkedin-campaign-management-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Candidate Synchronization API
  slug: open-linkedin-candidate-synchronization-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Child Application Provisioning API
  slug: open-linkedin-child-application-provisioning-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Company Streaming API
  slug: open-linkedin-company-streaming-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Compliance Authorization API
  slug: open-linkedin-compliance-authorization-api
- collection_type: open
  name: LinkedIn Access Control Compliance Events API
  slug: open-linkedin-compliance-events-api
- collection_type: open
  name: LinkedIn Compliance Events API
  slug: open-linkedin-compliance-events
- collection_type: open
  name: LinkedIn Compliance Events Access Control Conversion Events Streaming Workflow API
  slug: open-linkedin-conversion-events-streaming-workflow-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Creative Management API
  slug: open-linkedin-creative-management-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control CRM Data Validation API
  slug: open-linkedin-crm-data-validation-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Customer Integrations API
  slug: open-linkedin-customer-integrations-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Data Deletion API
  slug: open-linkedin-data-deletion-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Data Retrieval API
  slug: open-linkedin-data-retrieval-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control DMP Segments API
  slug: open-linkedin-dmp-segments-api
- collection_type: open
  name: LinkedIn Compliance Access Control Events API
  slug: open-linkedin-events-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Feed Content API
  slug: open-linkedin-feed-content-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Fetch Media Plan API
  slug: open-linkedin-fetch-media-plan-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Integration Configuration API
  slug: open-linkedin-integration-configuration-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Job Lifecycle Management API
  slug: open-linkedin-job-lifecycle-management-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Lead Generation API
  slug: open-linkedin-lead-generation-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Learning Activity Reports API
  slug: open-linkedin-learning-activity-reports-api
- collection_type: open
  name: LinkedIn Learning Activity Reports API
  slug: open-linkedin-learning-activity-reports
- collection_type: open
  name: LinkedIn Compliance Events Access Control List Uploads API
  slug: open-linkedin-list-uploads-api
- collection_type: open
  name: LinkedIn Marketing Audience Insights API
  slug: open-linkedin-marketing-audience-insights
- collection_type: open
  name: LinkedIn Marketing Audiences API
  slug: open-linkedin-marketing-audience
- collection_type: open
  name: LinkedIn Marketing Campaign Management API
  slug: open-linkedin-marketing-campaigns
- collection_type: open
  name: Community Management
  slug: open-linkedin-marketing-community
- collection_type: open
  name: Content APIs
  slug: open-linkedin-marketing-content
- collection_type: open
  name: Conversions API
  slug: open-linkedin-marketing-conversions
- collection_type: open
  name: Lead Sync
  slug: open-linkedin-marketing-leads
- collection_type: open
  name: Media Planning
  slug: open-linkedin-marketing-media-planning
- collection_type: open
  name: Reporting & ROI
  slug: open-linkedin-marketing-reporting-roi
- collection_type: open
  name: LinkedIn Compliance Events Access Control Organization Access Control API
  slug: open-linkedin-organization-access-control-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Organizations API
  slug: open-linkedin-organizations-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Page Analytics API
  slug: open-linkedin-page-analytics-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Profile Associations API
  slug: open-linkedin-profile-associations-api
- collection_type: open
  name: LinkedIn Pages Data Portability API
  slug: open-linkedin-regulations-data-portability
- collection_type: open
  name: LinkedIn Ads Transparency API
  slug: open-linkedin-regulatory-ads-transparency
- collection_type: open
  name: LinkedIn Compliance Events Access Control Sales Access Tokens API
  slug: open-linkedin-sales-access-tokens-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Sales Analytics Export API
  slug: open-linkedin-sales-analytics-export-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Sales Contracts API
  slug: open-linkedin-sales-contracts-api
- collection_type: open
  name: LinkedIn Sales Navigator API
  slug: open-linkedin-sales-navigator
- collection_type: open
  name: LinkedIn Job Posting API
  slug: open-linkedin-talent-job-posting
- collection_type: open
  name: LinkedIn Parent Application Management API
  slug: open-linkedin-talent-learning-parent-application
- collection_type: open
  name: LinkedIn Recruiter System Connect API
  slug: open-linkedin-talent-recruiter-system-connect
- collection_type: open
  name: LinkedIn Compliance Events Access Control Use Cases > B2B Templates > Conversions Deep Dive API
  slug: open-linkedin-use-cases-b2b-templates-conversions-deep-dive-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Use Cases > Conversation Ad > Sponsored Conversations API
  slug: open-linkedin-use-cases-conversation-ad-sponsored-conversations-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Use Cases > Conversation Ad > Sponsored Message Contents API
  slug: open-linkedin-use-cases-conversation-ad-sponsored-message-contents-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Use Cases > Creatives API
  slug: open-linkedin-use-cases-creatives-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Use Cases > Document Ad API
  slug: open-linkedin-use-cases-document-ad-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Use Cases > Image Ad API
  slug: open-linkedin-use-cases-image-ad-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Use Cases > InMail Content API
  slug: open-linkedin-use-cases-inmail-content-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Use Cases > Organization Access Controls API
  slug: open-linkedin-use-cases-organization-access-controls-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Use Cases > Organization Followers API
  slug: open-linkedin-use-cases-organization-followers-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Use Cases > Organization Lookup > Organization Brands API
  slug: open-linkedin-use-cases-organization-lookup-organization-brands-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Use Cases > Organization Lookup > Organizations API
  slug: open-linkedin-use-cases-organization-lookup-organizations-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Use Cases > Posts API
  slug: open-linkedin-use-cases-posts-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Use Cases > Social Actions Notifications > Organization Social Actions Notifications - Pull Workflow API
  slug: open-linkedin-use-cases-social-actions-notifications-organization-social-actions-notifications-pull-workflow-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Use Cases > Social Actions Notifications > Organization Social Actions Notifications - Push Workflow API
  slug: open-linkedin-use-cases-social-actions-notifications-organization-social-actions-notifications-push-workflow-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Use Cases > Sponsored API
  slug: open-linkedin-use-cases-sponsored-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Use Cases > Spotlight Ad API
  slug: open-linkedin-use-cases-spotlight-ad-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Use Cases > Statistics APIs > Organization Follower Statistics API
  slug: open-linkedin-use-cases-statistics-apis-organization-follower-statistics-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Use Cases > Statistics APIs > Organization Page Statistics API
  slug: open-linkedin-use-cases-statistics-apis-organization-page-statistics-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Use Cases > Statistics APIs > Organization Share Statistics API
  slug: open-linkedin-use-cases-statistics-apis-organization-share-statistics-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control Use Cases > Video Ad API
  slug: open-linkedin-use-cases-video-ad-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control User Access API
  slug: open-linkedin-user-access-api
- collection_type: open
  name: LinkedIn Compliance Events Access Control User Streaming API
  slug: open-linkedin-user-streaming-api
common:
- group: design
  href: https://artifacts.apis.io/linkedin/conventions/linkedin-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/linkedin-conventions.yml
- group: agent
  href: https://artifacts.apis.io/linkedin/llms/linkedin-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/linkedin-llms.txt
- group: operate
  href: https://artifacts.apis.io/linkedin/rate-limits/linkedin-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/linkedin-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/linkedin/rules/linkedin-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/linkedin-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/linkedin/rules/linkedin-rules.yml
  title: ''
  type: Spectral
  url: rules/linkedin-rules.yml
- group: design
  href: https://artifacts.apis.io/linkedin/rules/linkedin-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/linkedin-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/linkedin/json-ld/linkedin-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/linkedin-context.jsonld
- group: design
  href: https://artifacts.apis.io/linkedin/json-ld/linkedin-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/linkedin-api-context.jsonld
- group: other
  href: https://artifacts.apis.io/linkedin/hosts/linkedin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/linkedin-hosts.yml
- group: build
  href: https://artifacts.apis.io/linkedin/integrations/linkedin-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/linkedin-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/linkedin/vendors/linkedin-vendors.yml
  title: ''
  type: Vendors
  url: vendors/linkedin-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: other
  href: https://artifacts.apis.io/linkedin/overlays/linkedin-adaccounts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-adaccounts-overlay.yaml
- group: other
  href: https://artifacts.apis.io/linkedin/overlays/linkedin-adcampaigngroups-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-adcampaigngroups-overlay.yaml
- group: other
  href: https://artifacts.apis.io/linkedin/overlays/linkedin-adcampaigns-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-adcampaigns-overlay.yaml
- group: other
  href: https://artifacts.apis.io/linkedin/overlays/linkedin-adcreatives-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-adcreatives-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.linkedin.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.linkedin.com/developers/apps/new
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/linkedin-developer-apis/workspace/linkedin-marketing-solutions-versioned-apis/overview
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: other
  href: https://artifacts.apis.io/linkedin/capabilities/linkedin-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/linkedin-capability-edges.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/linkedin/marketing/quick-start
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/linkedin/shared/breaking-change-policy
- group: auth
  title: ''
  type: Security
  url: https://security.linkedin.com/vulnerability-disclosure
- group: auth
  title: ''
  type: Compliance
  url: https://security.linkedin.com/trust-and-compliance
- group: auth
  href: https://artifacts.apis.io/linkedin/security/linkedin-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/linkedin-trust-center.yml
- group: design
  href: https://artifacts.apis.io/linkedin/asyncapi/linkedin-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/linkedin-webhooks.yml
- group: start
  href: https://artifacts.apis.io/linkedin/sandbox/linkedin-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/linkedin-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/linkedin/skills/_index.yml
  title: ''
  type: AgentSkills
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/linkedin/skills/linkedin-authenticate.md
  title: ''
  type: AgentSkill
  url: skills/linkedin-authenticate.md
- group: agent
  href: https://artifacts.apis.io/linkedin/skills/linkedin-publish-organization-post.md
  title: ''
  type: AgentSkill
  url: skills/linkedin-publish-organization-post.md
- group: agent
  href: https://artifacts.apis.io/linkedin/skills/linkedin-upload-media-and-post.md
  title: ''
  type: AgentSkill
  url: skills/linkedin-upload-media-and-post.md
- group: agent
  href: https://artifacts.apis.io/linkedin/skills/linkedin-organization-analytics.md
  title: ''
  type: AgentSkill
  url: skills/linkedin-organization-analytics.md
- group: agent
  href: https://artifacts.apis.io/linkedin/skills/linkedin-subscribe-social-action-webhooks.md
  title: ''
  type: AgentSkill
  url: skills/linkedin-subscribe-social-action-webhooks.md
- group: agent
  href: https://artifacts.apis.io/linkedin/skills/linkedin-manage-ad-campaigns.md
  title: ''
  type: AgentSkill
  url: skills/linkedin-manage-ad-campaigns.md
- group: agent
  href: https://artifacts.apis.io/linkedin/skills/linkedin-lead-sync.md
  title: ''
  type: AgentSkill
  url: skills/linkedin-lead-sync.md
- group: commercial
  href: https://artifacts.apis.io/linkedin/plans/linkedin-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/linkedin-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/linkedin/vocabulary/linkedin-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/linkedin-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/linkedin/rules/linkedin-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/linkedin-spectral-rules.yml
- group: commercial
  href: https://artifacts.apis.io/linkedin/finops/linkedin-finops.yml
  title: ''
  type: FinOps
  url: finops/linkedin-finops.yml
- group: build
  href: https://artifacts.apis.io/linkedin/examples/linkedin-attachlisttosegment-example.json
  title: ''
  type: Examples
  url: examples/linkedin-attachlisttosegment-example.json
- group: build
  href: https://artifacts.apis.io/linkedin/examples/linkedin-batchgetprofileassociations-example.json
  title: ''
  type: Examples
  url: examples/linkedin-batchgetprofileassociations-example.json
- group: build
  href: https://artifacts.apis.io/linkedin/examples/linkedin-compliance-events-compliance-authorization-example.json
  title: ''
  type: Examples
  url: examples/linkedin-compliance-events-compliance-authorization-example.json
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/linkedin-developer-apis
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/linkedin/overview
- group: agent
  href: https://artifacts.apis.io/linkedin/agentic-access/linkedin-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/linkedin-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/linkedin/packages/linkedin-packages.yml
  title: ''
  type: Packages
  url: packages/linkedin-packages.yml
- group: agent
  href: https://artifacts.apis.io/linkedin/well-known/linkedin-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/linkedin-well-known.yml
- group: auth
  href: https://artifacts.apis.io/linkedin/well-known/linkedin-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/linkedin-security.txt
- group: agent
  href: https://artifacts.apis.io/linkedin/mcp/linkedin-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/linkedin-mcp.yml
- group: design
  href: https://artifacts.apis.io/linkedin/conformance/linkedin-conformance.yml
  title: ''
  type: Conformance
  url: conformance/linkedin-conformance.yml
- group: design
  href: https://artifacts.apis.io/linkedin/errors/linkedin-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/linkedin-problem-types.yml
- group: design
  href: https://artifacts.apis.io/linkedin/lifecycle/linkedin-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/linkedin-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/linkedin/conventions/linkedin-conventions.yml
  title: ''
  type: Conventions
  url: conventions/linkedin-conventions.yml
- group: operate
  href: https://artifacts.apis.io/linkedin/changelog/linkedin-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/linkedin-changelog.yml
- group: design
  href: https://artifacts.apis.io/linkedin/components/linkedin-components.yml
  title: ''
  type: Components
  url: components/linkedin-components.yml
- group: design
  href: https://artifacts.apis.io/linkedin/data-model/linkedin-data-model.yml
  title: ''
  type: DataModel
  url: data-model/linkedin-data-model.yml
- group: other
  href: https://artifacts.apis.io/linkedin/overlays/linkedin-compliance-events-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-compliance-events-overlay.yaml
- group: other
  href: https://artifacts.apis.io/linkedin/overlays/linkedin-learning-activity-reports-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-learning-activity-reports-overlay.yaml
- group: other
  href: https://artifacts.apis.io/linkedin/overlays/linkedin-marketing-audience-insights-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-marketing-audience-insights-overlay.yaml
- group: other
  href: https://artifacts.apis.io/linkedin/overlays/linkedin-marketing-audience-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-marketing-audience-overlay.yaml
- group: other
  href: https://artifacts.apis.io/linkedin/overlays/linkedin-marketing-campaigns-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-marketing-campaigns-overlay.yaml
- group: other
  href: https://artifacts.apis.io/linkedin/overlays/linkedin-marketing-community-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-marketing-community-overlay.yaml
- group: other
  href: https://artifacts.apis.io/linkedin/overlays/linkedin-marketing-content-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-marketing-content-overlay.yaml
- group: other
  href: https://artifacts.apis.io/linkedin/overlays/linkedin-marketing-conversions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-marketing-conversions-overlay.yaml
- group: other
  href: https://artifacts.apis.io/linkedin/overlays/linkedin-marketing-leads-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-marketing-leads-overlay.yaml
- group: other
  href: https://artifacts.apis.io/linkedin/overlays/linkedin-marketing-media-planning-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-marketing-media-planning-overlay.yaml
- group: other
  href: https://artifacts.apis.io/linkedin/overlays/linkedin-marketing-reporting-roi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-marketing-reporting-roi-overlay.yaml
- group: other
  href: https://artifacts.apis.io/linkedin/overlays/linkedin-regulations-data-portability-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-regulations-data-portability-overlay.yaml
- group: other
  href: https://artifacts.apis.io/linkedin/overlays/linkedin-regulatory-ads-transparency-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-regulatory-ads-transparency-overlay.yaml
- group: other
  href: https://artifacts.apis.io/linkedin/overlays/linkedin-sales-navigator-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-sales-navigator-overlay.yaml
- group: other
  href: https://artifacts.apis.io/linkedin/overlays/linkedin-talent-job-posting-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-talent-job-posting-overlay.yaml
- group: other
  href: https://artifacts.apis.io/linkedin/overlays/linkedin-talent-learning-parent-application-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-talent-learning-parent-application-overlay.yaml
- group: other
  href: https://artifacts.apis.io/linkedin/overlays/linkedin-talent-recruiter-system-connect-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/linkedin-talent-recruiter-system-connect-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/linkedin/security/linkedin-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/linkedin-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/linkedin/security/linkedin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/linkedin-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/linkedin/authentication/linkedin-authentication.yml
  title: ''
  type: Authentication
  url: authentication/linkedin-authentication.yml
- group: auth
  href: https://artifacts.apis.io/linkedin/scopes/linkedin-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/linkedin-scopes.yml
- group: design
  href: https://artifacts.apis.io/linkedin/arazzo/linkedin-create-organization-share-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/linkedin-create-organization-share-workflow.yml
- group: design
  href: https://artifacts.apis.io/linkedin/arazzo/linkedin-delete-organization-post-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/linkedin-delete-organization-post-workflow.yml
- group: design
  href: https://artifacts.apis.io/linkedin/arazzo/linkedin-export-post-engagement-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/linkedin-export-post-engagement-workflow.yml
- group: design
  href: https://artifacts.apis.io/linkedin/arazzo/linkedin-find-org-and-people-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/linkedin-find-org-and-people-workflow.yml
- group: design
  href: https://artifacts.apis.io/linkedin/arazzo/linkedin-org-access-and-brands-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/linkedin-org-access-and-brands-workflow.yml
- group: design
  href: https://artifacts.apis.io/linkedin/arazzo/linkedin-organization-follower-analytics-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/linkedin-organization-follower-analytics-workflow.yml
- group: design
  href: https://artifacts.apis.io/linkedin/arazzo/linkedin-organization-profile-overview-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/linkedin-organization-profile-overview-workflow.yml
- group: design
  href: https://artifacts.apis.io/linkedin/arazzo/linkedin-organization-share-analytics-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/linkedin-organization-share-analytics-workflow.yml
- group: design
  href: https://artifacts.apis.io/linkedin/arazzo/linkedin-publish-and-verify-post-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/linkedin-publish-and-verify-post-workflow.yml
- group: design
  href: https://artifacts.apis.io/linkedin/arazzo/linkedin-pull-social-action-notifications-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/linkedin-pull-social-action-notifications-workflow.yml
- group: design
  href: https://artifacts.apis.io/linkedin/arazzo/linkedin-subscribe-social-action-notifications-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/linkedin-subscribe-social-action-notifications-workflow.yml
- group: design
  href: https://artifacts.apis.io/linkedin/arazzo/linkedin-update-organization-post-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/linkedin-update-organization-post-workflow.yml
- group: design
  href: https://artifacts.apis.io/linkedin/arazzo/linkedin-upload-document-and-create-post-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/linkedin-upload-document-and-create-post-workflow.yml
- group: design
  href: https://artifacts.apis.io/linkedin/arazzo/linkedin-upload-image-and-create-post-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/linkedin-upload-image-and-create-post-workflow.yml
- group: design
  href: https://artifacts.apis.io/linkedin/arazzo/linkedin-upload-video-and-verify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/linkedin-upload-video-and-verify-workflow.yml
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authentication
- group: docs
  title: ''
  type: Documentation
  url: https://www.linkedin.com/oauth/.well-known/openid-configuration
- group: build
  title: ''
  type: CodeExamples
  url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/sample-applications
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/shared/breaking-change-policy
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/marketing/versioning
- group: other
  title: ''
  type: BestPractices
  url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/best-practices/overview
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts?context=linkedin/consumer/context
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/error-handling?context=linkedin/consumer/context
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.microsoft.com/en-us/linkedin/shared/api-guide/concepts/rate-limits
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/plugins?context=linkedin/consumer/context
- group: start
  title: ''
  type: Portal
  url: https://www.linkedin.com/developers/
- group: start
  title: ''
  type: Signup
  url: https://www.linkedin.com/developers/apps
- group: build
  title: ''
  type: Tools
  url: https://www.linkedin.com/developers/tools/oauth
- group: operate
  title: ''
  type: StatusPage
  url: https://www.linkedin-apistatus.com/
- group: company
  title: ''
  type: Blog
  url: https://www.linkedin.com/content/developers/news
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/authorization-code-flow
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/client-credentials-flow
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/programmatic-refresh-tokens
- group: build
  title: ''
  type: Tools
  url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/developer-portal-tools
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/shared/authentication/postman-getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/concepts/pagination
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/webhook-validation
- group: other
  title: ''
  type: BestPractices
  url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/best-practices/application-development
- group: other
  title: ''
  type: BestPractices
  url: https://learn.microsoft.com/en-us/linkedin/shared/api-guide/best-practices/secure-applications
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/linkedin/shared/development-resources/api-clients
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/linkedin/shared/integrations/people/profile-api
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/linkedin-developers
- group: build
  title: ''
  type: SDKs
  url: https://github.com/linkedin-developers/linkedin-api-js-client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/linkedin-developers/linkedin-api-python-client
- group: operate
  title: ''
  type: Support
  url: https://developer.linkedin.com/support
- group: build
  title: ''
  type: Tools
  url: https://github.com/linkedin-developers/linkedin-capi-tag-template
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/linkedin-developers/java-sample-application
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.linkedin.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.linkedin.com/legal/l/api-terms-of-use
created: '2024-04-14'
description: LinkedIn is a professional networking platform providing APIs for consumer integrations (Sign In, Share, Verified on LinkedIn), marketing solutions (ad campaigns, audiences, conversions, analytics), talent solutions (job posting, recruiter system connect), learning solutions (activity reports, content), sales navigator (CRM sync, display, analytics), compliance (message archiving), and regulatory data portability.
examples:
- key_count: 6
  name: Linkedin Attachlisttosegment Example
  slug: linkedin-attachlisttosegment-example
- key_count: 6
  name: Linkedin Batchgetprofileassociations Example
  slug: linkedin-batchgetprofileassociations-example
- key_count: 4
  name: Linkedin Compliance Events Compliance Authorization Example
  slug: linkedin-compliance-events-compliance-authorization-example
- key_count: 1
  name: Linkedin Compliance Events Compliance Authorization Request Example
  slug: linkedin-compliance-events-compliance-authorization-request-example
- key_count: 2
  name: Linkedin Compliance Events Compliance Authorization Response Example
  slug: linkedin-compliance-events-compliance-authorization-response-example
- key_count: 10
  name: Linkedin Compliance Events Compliance Event Example
  slug: linkedin-compliance-events-compliance-event-example
- key_count: 2
  name: Linkedin Compliance Events Compliance Events Response Example
  slug: linkedin-compliance-events-compliance-events-response-example
- key_count: 3
  name: Linkedin Compliance Events Error Response Example
  slug: linkedin-compliance-events-error-response-example
- key_count: 3
  name: Linkedin Compliance Events Member Profile Example
  slug: linkedin-compliance-events-member-profile-example
- key_count: 4
  name: Linkedin Compliance Events Paging Example
  slug: linkedin-compliance-events-paging-example
- key_count: 3
  name: Linkedin Compliance Events Paging Link Example
  slug: linkedin-compliance-events-paging-link-example
- key_count: 6
  name: Linkedin Createadaccount Example
  slug: linkedin-createadaccount-example
- key_count: 6
  name: Linkedin Createadaccountuser Example
  slug: linkedin-createadaccountuser-example
- key_count: 6
  name: Linkedin Createcreative Example
  slug: linkedin-createcreative-example
- key_count: 6
  name: Linkedin Createcrmdatavalidationexportjob Example
  slug: linkedin-createcrmdatavalidationexportjob-example
- key_count: 6
  name: Linkedin Createdmpsegment Example
  slug: linkedin-createdmpsegment-example
- key_count: 6
  name: Linkedin Createsalesanalyticsexportjob Example
  slug: linkedin-createsalesanalyticsexportjob-example
- key_count: 6
  name: Linkedin Getadaccountbyid Example
  slug: linkedin-getadaccountbyid-example
- key_count: 6
  name: Linkedin Getadaccountuser Example
  slug: linkedin-getadaccountuser-example
- key_count: 6
  name: Linkedin Getaudiencecount Example
  slug: linkedin-getaudiencecount-example
- key_count: 6
  name: Linkedin Getauthenticateduseradaccounts Example
  slug: linkedin-getauthenticateduseradaccounts-example
- key_count: 6
  name: Linkedin Getcampaignbyid Example
  slug: linkedin-getcampaignbyid-example
- key_count: 6
  name: Linkedin Getcampaigngroupbyid Example
  slug: linkedin-getcampaigngroupbyid-example
- key_count: 6
  name: Linkedin Getdmpsegments Example
  slug: linkedin-getdmpsegments-example
- key_count: 6
  name: Linkedin Getlearningactivityreports Example
  slug: linkedin-getlearningactivityreports-example
- key_count: 6
  name: Linkedin Getorganizationacls Example
  slug: linkedin-getorganizationacls-example
- key_count: 3
  name: Linkedin Learning Activity Reports Error Response Example
  slug: linkedin-learning-activity-reports-error-response-example
- key_count: 1
  name: Linkedin Learning Activity Reports Learner Details Example
  slug: linkedin-learning-activity-reports-learner-details-example
- key_count: 4
  name: Linkedin Learning Activity Reports Learner Entity Example
  slug: linkedin-learning-activity-reports-learner-entity-example
- key_count: 6
  name: Linkedin Learning Activity Reports Learning Activity Example
  slug: linkedin-learning-activity-reports-learning-activity-example
- key_count: 3
  name: Linkedin Learning Activity Reports Learning Activity Report Example
  slug: linkedin-learning-activity-reports-learning-activity-report-example
- key_count: 2
  name: Linkedin Learning Activity Reports Learning Activity Report Response Example
  slug: linkedin-learning-activity-reports-learning-activity-report-response-example
- key_count: 4
  name: Linkedin Learning Activity Reports Paging Example
  slug: linkedin-learning-activity-reports-paging-example
- key_count: 3
  name: Linkedin Learning Activity Reports Paging Link Example
  slug: linkedin-learning-activity-reports-paging-link-example
- key_count: 4
  name: Linkedin Marketing Audience Ad Account Example
  slug: linkedin-marketing-audience-ad-account-example
- key_count: 2
  name: Linkedin Marketing Audience Ad Accounts Response Example
  slug: linkedin-marketing-audience-ad-accounts-response-example
- key_count: 4
  name: Linkedin Marketing Audience Company Stream Element Example
  slug: linkedin-marketing-audience-company-stream-element-example
- key_count: 1
  name: Linkedin Marketing Audience Company Stream Request Example
  slug: linkedin-marketing-audience-company-stream-request-example
- key_count: 6
  name: Linkedin Marketing Audience Dmp Segment Create Request Example
  slug: linkedin-marketing-audience-dmp-segment-create-request-example
- key_count: 10
  name: Linkedin Marketing Audience Dmp Segment Example
  slug: linkedin-marketing-audience-dmp-segment-example
- key_count: 2
  name: Linkedin Marketing Audience Dmp Segments Response Example
  slug: linkedin-marketing-audience-dmp-segments-response-example
- key_count: 2
  name: Linkedin Marketing Audience Insights Ad Targeting Entities Response Example
  slug: linkedin-marketing-audience-insights-ad-targeting-entities-response-example
- key_count: 3
  name: Linkedin Marketing Audience Insights Ad Targeting Entity Example
  slug: linkedin-marketing-audience-insights-ad-targeting-entity-example
- key_count: 4
  name: Linkedin Marketing Audience Insights Ad Targeting Facet Example
  slug: linkedin-marketing-audience-insights-ad-targeting-facet-example
- key_count: 2
  name: Linkedin Marketing Audience Insights Ad Targeting Facets Response Example
  slug: linkedin-marketing-audience-insights-ad-targeting-facets-response-example
- key_count: 2
  name: Linkedin Marketing Audience Insights Audience Insight Example
  slug: linkedin-marketing-audience-insights-audience-insight-example
- key_count: 1
  name: Linkedin Marketing Audience Insights Audience Insights Request Example
  slug: linkedin-marketing-audience-insights-audience-insights-request-example
- key_count: 1
  name: Linkedin Marketing Audience Insights Audience Insights Response Example
  slug: linkedin-marketing-audience-insights-audience-insights-response-example
- key_count: 3
  name: Linkedin Marketing Audience Insights Error Response Example
  slug: linkedin-marketing-audience-insights-error-response-example
- key_count: 3
  name: Linkedin Marketing Audience Insights Insight Segmentation Example
  slug: linkedin-marketing-audience-insights-insight-segmentation-example
- key_count: 4
  name: Linkedin Marketing Audience Insights Paging Example
  slug: linkedin-marketing-audience-insights-paging-example
- key_count: 3
  name: Linkedin Marketing Audience Insights Paging Link Example
  slug: linkedin-marketing-audience-insights-paging-link-example
- key_count: 1
  name: Linkedin Marketing Audience Insights Request Meta Data Example
  slug: linkedin-marketing-audience-insights-request-meta-data-example
- key_count: 1
  name: Linkedin Marketing Audience Insights Targeting Criteria Example
  slug: linkedin-marketing-audience-insights-targeting-criteria-example
- key_count: 1
  name: Linkedin Marketing Audience List Upload Request Example
  slug: linkedin-marketing-audience-list-upload-request-example
- key_count: 4
  name: Linkedin Marketing Audience Paging Example
  slug: linkedin-marketing-audience-paging-example
- key_count: 1
  name: Linkedin Marketing Audience Segment Destination Example
  slug: linkedin-marketing-audience-segment-destination-example
- key_count: 1
  name: Linkedin Marketing Audience Stream Response Example
  slug: linkedin-marketing-audience-stream-response-example
- key_count: 1
  name: Linkedin Marketing Audience Stream Result Element Example
  slug: linkedin-marketing-audience-stream-result-element-example
- key_count: 2
  name: Linkedin Marketing Audience User Id Example
  slug: linkedin-marketing-audience-user-id-example
- key_count: 2
  name: Linkedin Marketing Audience User Stream Element Example
  slug: linkedin-marketing-audience-user-stream-element-example
- key_count: 1
  name: Linkedin Marketing Audience User Stream Request Example
  slug: linkedin-marketing-audience-user-stream-request-example
- key_count: 9
  name: Linkedin Marketing Campaigns Ad Account Create Request Example
  slug: linkedin-marketing-campaigns-ad-account-create-request-example
- key_count: 10
  name: Linkedin Marketing Campaigns Ad Account Example
  slug: linkedin-marketing-campaigns-ad-account-example
- key_count: 3
  name: Linkedin Marketing Campaigns Ad Account User Create Request Example
  slug: linkedin-marketing-campaigns-ad-account-user-create-request-example
- key_count: 3
  name: Linkedin Marketing Campaigns Ad Account User Example
  slug: linkedin-marketing-campaigns-ad-account-user-example
- key_count: 1
  name: Linkedin Marketing Campaigns Ad Account User Update Request Example
  slug: linkedin-marketing-campaigns-ad-account-user-update-request-example
- key_count: 2
  name: Linkedin Marketing Campaigns Audience Count Example
  slug: linkedin-marketing-campaigns-audience-count-example
- key_count: 2
  name: Linkedin Marketing Campaigns Budget Example
  slug: linkedin-marketing-campaigns-budget-example
- key_count: 10
  name: Linkedin Marketing Campaigns Campaign Example
  slug: linkedin-marketing-campaigns-campaign-example
- key_count: 6
  name: Linkedin Marketing Campaigns Campaign Group Example
  slug: linkedin-marketing-campaigns-campaign-group-example
- key_count: 1
  name: Linkedin Marketing Campaigns Campaign Update Request Example
  slug: linkedin-marketing-campaigns-campaign-update-request-example
- key_count: 5
  name: Linkedin Marketing Campaigns Creative Create Request Example
  slug: linkedin-marketing-campaigns-creative-create-request-example
- key_count: 5
  name: Linkedin Marketing Campaigns Creative Example
  slug: linkedin-marketing-campaigns-creative-example
- key_count: 3
  name: Linkedin Marketing Campaigns Organization Acl Example
  slug: linkedin-marketing-campaigns-organization-acl-example
- key_count: 4
  name: Linkedin Marketing Campaigns Paging Example
  slug: linkedin-marketing-campaigns-paging-example
- key_count: 2
  name: Linkedin Marketing Campaigns Run Schedule Example
  slug: linkedin-marketing-campaigns-run-schedule-example
- key_count: 3
  name: Linkedin Marketing Community Batch Get On Administered Response200 Example
  slug: linkedin-marketing-community-batch-get-on-administered-response200-example
- key_count: 3
  name: Linkedin Marketing Community Batch Get On Nonadministered Response200 Example
  slug: linkedin-marketing-community-batch-get-on-nonadministered-response200-example
- key_count: 2
  name: Linkedin Marketing Community Find Administered Organization Brands Response200 Example
  slug: linkedin-marketing-community-find-administered-organization-brands-response200-example
- key_count: 3
  name: Linkedin Marketing Community Find Nonadministered Organization Response200 Example
  slug: linkedin-marketing-community-find-nonadministered-organization-response200-example
- key_count: 1
  name: Linkedin Marketing Community Lookup By Organization Primary Response200 Example
  slug: linkedin-marketing-community-lookup-by-organization-primary-response200-example
- key_count: 10
  name: Linkedin Marketing Community Retrieve An Administered Organization Response200 Example
  slug: linkedin-marketing-community-retrieve-an-administered-organization-response200-example
- key_count: 1
  name: Linkedin Marketing Community Retrieve Organization Follower Count Response200 Example
  slug: linkedin-marketing-community-retrieve-organization-follower-count-response200-example
- key_count: 10
  name: Linkedin Marketing Conversions Create A New Conversion Response201 Example
  slug: linkedin-marketing-conversions-create-a-new-conversion-response201-example
- key_count: 2
  name: Linkedin Marketing Conversions Fetch Active Campaigns Response200 Example
  slug: linkedin-marketing-conversions-fetch-active-campaigns-response200-example
- key_count: 2
  name: Linkedin Marketing Conversions Fetch Existing Conversion Rules Response200 Example
  slug: linkedin-marketing-conversions-fetch-existing-conversion-rules-response200-example
- key_count: 2
  name: Linkedin Marketing Conversions Retrieve Authenticated Users Sponsored Response200 Example
  slug: linkedin-marketing-conversions-retrieve-authenticated-users-sponsored-response200-example
- key_count: 1
  name: Linkedin Marketing Conversions Stream Multiple Conversion Events Response200 Example
  slug: linkedin-marketing-conversions-stream-multiple-conversion-events-response200-example
- key_count: 10
  name: Linkedin Marketing Leads Fetch Full Lead Data Response200 Example
  slug: linkedin-marketing-leads-fetch-full-lead-data-response200-example
- key_count: 2
  name: Linkedin Marketing Leads Get Forms For The Response200 Example
  slug: linkedin-marketing-leads-get-forms-for-the-response200-example
- key_count: 2
  name: Linkedin Marketing Leads Get The Users Sponsored Response200 Example
  slug: linkedin-marketing-leads-get-the-users-sponsored-response200-example
- key_count: 2
  name: Linkedin Marketing Leads Validate The Users Organization Response200 Example
  slug: linkedin-marketing-leads-validate-the-users-organization-response200-example
- key_count: 2
  name: Linkedin Marketing Media Planning Get A List Of Response200 Example
  slug: linkedin-marketing-media-planning-get-a-list-of-response200-example
- key_count: 2
  name: Linkedin Marketing Media Planning Get Bing Geo Locations Response200 Example
  slug: linkedin-marketing-media-planning-get-bing-geo-locations-response200-example
- key_count: 2
  name: Linkedin Marketing Reporting Roi Conversions By Member Company Response200 Example
  slug: linkedin-marketing-reporting-roi-conversions-by-member-company-response200-example
- key_count: 6
  name: Linkedin Optinmemberforcompliance Example
  slug: linkedin-optinmemberforcompliance-example
- key_count: 5
  name: Linkedin Regulations Data Portability Address Example
  slug: linkedin-regulations-data-portability-address-example
- key_count: 3
  name: Linkedin Regulations Data Portability Batch Organization Response Example
  slug: linkedin-regulations-data-portability-batch-organization-response-example
- key_count: 3
  name: Linkedin Regulations Data Portability Date Info Example
  slug: linkedin-regulations-data-portability-date-info-example
- key_count: 3
  name: Linkedin Regulations Data Portability Image Asset Example
  slug: linkedin-regulations-data-portability-image-asset-example
- key_count: 3
  name: Linkedin Regulations Data Portability Image Reference Example
  slug: linkedin-regulations-data-portability-image-reference-example
- key_count: 2
  name: Linkedin Regulations Data Portability Locale Example
  slug: linkedin-regulations-data-portability-locale-example
- key_count: 2
  name: Linkedin Regulations Data Portability Localized String Example
  slug: linkedin-regulations-data-portability-localized-string-example
- key_count: 5
  name: Linkedin Regulations Data Portability Organization Acl Example
  slug: linkedin-regulations-data-portability-organization-acl-example
- key_count: 2
  name: Linkedin Regulations Data Portability Organization Acl Response Example
  slug: linkedin-regulations-data-portability-organization-acl-response-example
- key_count: 5
  name: Linkedin Regulations Data Portability Organization Location Example
  slug: linkedin-regulations-data-portability-organization-location-example
- key_count: 10
  name: Linkedin Regulations Data Portability Organization Response Example
  slug: linkedin-regulations-data-portability-organization-response-example
- key_count: 7
  name: Linkedin Regulations Data Portability Post Example
  slug: linkedin-regulations-data-portability-post-example
- key_count: 2
  name: Linkedin Regulations Data Portability Post Response Example
  slug: linkedin-regulations-data-portability-post-response-example
- key_count: 2
  name: Linkedin Regulations Data Portability Reaction Response Example
  slug: linkedin-regulations-data-portability-reaction-response-example
- key_count: 1
  name: Linkedin Regulations Data Portability Timestamp Example
  slug: linkedin-regulations-data-portability-timestamp-example
- key_count: 2
  name: Linkedin Regulatory Ads Transparency Advertiser Transparency Request Example
  slug: linkedin-regulatory-ads-transparency-advertiser-transparency-request-example
- key_count: 7
  name: Linkedin Regulatory Ads Transparency Advertiser Transparency Response Example
  slug: linkedin-regulatory-ads-transparency-advertiser-transparency-response-example
- key_count: 3
  name: Linkedin Regulatory Ads Transparency Error Response Example
  slug: linkedin-regulatory-ads-transparency-error-response-example
- key_count: 3
  name: Linkedin Sales Navigator Batch Profile Association Response Example
  slug: linkedin-sales-navigator-batch-profile-association-response-example
- key_count: 4
  name: Linkedin Sales Navigator Contract Example
  slug: linkedin-sales-navigator-contract-example
- key_count: 2
  name: Linkedin Sales Navigator Contracts Response Example
  slug: linkedin-sales-navigator-contracts-response-example
- key_count: 7
  name: Linkedin Sales Navigator Crm Data Validation Export Job Example
  slug: linkedin-sales-navigator-crm-data-validation-export-job-example
- key_count: 1
  name: Linkedin Sales Navigator Crm Data Validation Export Job Request Example
  slug: linkedin-sales-navigator-crm-data-validation-export-job-request-example
- key_count: 3
  name: Linkedin Sales Navigator Error Response Example
  slug: linkedin-sales-navigator-error-response-example
- key_count: 3
  name: Linkedin Sales Navigator Paging Example
  slug: linkedin-sales-navigator-paging-example
- key_count: 2
  name: Linkedin Sales Navigator Sales Access Token Example
  slug: linkedin-sales-navigator-sales-access-token-example
- key_count: 2
  name: Linkedin Sales Navigator Sales Access Token Response Example
  slug: linkedin-sales-navigator-sales-access-token-response-example
- key_count: 5
  name: Linkedin Sales Navigator Sales Analytics Export Job Example
  slug: linkedin-sales-navigator-sales-analytics-export-job-example
- key_count: 3
  name: Linkedin Sales Navigator Sales Analytics Export Job Request Example
  slug: linkedin-sales-navigator-sales-analytics-export-job-request-example
- key_count: 1
  name: Linkedin Sales Navigator Sales Analytics Export Job Response Example
  slug: linkedin-sales-navigator-sales-analytics-export-job-response-example
- key_count: 3
  name: Linkedin Sales Navigator Sales Navigator Profile Association Example
  slug: linkedin-sales-navigator-sales-navigator-profile-association-example
- key_count: 3
  name: Linkedin Sales Navigator Sales Navigator Profile Association Key Example
  slug: linkedin-sales-navigator-sales-navigator-profile-association-key-example
- key_count: 6
  name: Linkedin Searchadaccounts Example
  slug: linkedin-searchadaccounts-example
- key_count: 6
  name: Linkedin Searchcampaigngroups Example
  slug: linkedin-searchcampaigngroups-example
- key_count: 6
  name: Linkedin Searchcampaigns Example
  slug: linkedin-searchcampaigns-example
- key_count: 6
  name: Linkedin Streamcompaniestosegment Example
  slug: linkedin-streamcompaniestosegment-example
- key_count: 1
  name: Linkedin Talent Job Posting Additional Questions Example
  slug: linkedin-talent-job-posting-additional-questions-example
- key_count: 6
  name: Linkedin Talent Job Posting Application Questions Example
  slug: linkedin-talent-job-posting-application-questions-example
- key_count: 1
  name: Linkedin Talent Job Posting Cover Letter Questions Example
  slug: linkedin-talent-job-posting-cover-letter-questions-example
- key_count: 4
  name: Linkedin Talent Job Posting Custom Question Example
  slug: linkedin-talent-job-posting-custom-question-example
- key_count: 2
  name: Linkedin Talent Job Posting Custom Question Set Example
  slug: linkedin-talent-job-posting-custom-question-set-example
- key_count: 1
  name: Linkedin Talent Job Posting Education Questions Example
  slug: linkedin-talent-job-posting-education-questions-example
- key_count: 10
  name: Linkedin Talent Job Posting Job Posting Element Example
  slug: linkedin-talent-job-posting-job-posting-element-example
- key_count: 1
  name: Linkedin Talent Job Posting Job Posting Response Example
  slug: linkedin-talent-job-posting-job-posting-response-example
- key_count: 3
  name: Linkedin Talent Job Posting Multiple Choice Question Details Example
  slug: linkedin-talent-job-posting-multiple-choice-question-details-example
- key_count: 2
  name: Linkedin Talent Job Posting Onsite Apply Configuration Example
  slug: linkedin-talent-job-posting-onsite-apply-configuration-example
- key_count: 2
  name: Linkedin Talent Job Posting Question Choice Example
  slug: linkedin-talent-job-posting-question-choice-example
- key_count: 1
  name: Linkedin Talent Job Posting Question Details Example
  slug: linkedin-talent-job-posting-question-details-example
- key_count: 1
  name: Linkedin Talent Job Posting Resume Questions Example
  slug: linkedin-talent-job-posting-resume-questions-example
- key_count: 1
  name: Linkedin Talent Job Posting Simple Job Posting Request Example
  slug: linkedin-talent-job-posting-simple-job-posting-request-example
- key_count: 1
  name: Linkedin Talent Job Posting Work Questions Example
  slug: linkedin-talent-job-posting-work-questions-example
- key_count: 4
  name: Linkedin Talent Learning Parent Application Application Credentials Example
  slug: linkedin-talent-learning-parent-application-application-credentials-example
- key_count: 3
  name: Linkedin Talent Learning Parent Application Error Response Example
  slug: linkedin-talent-learning-parent-application-error-response-example
- key_count: 1
  name: Linkedin Talent Learning Parent Application Get Application Response Example
  slug: linkedin-talent-learning-parent-application-get-application-response-example
- key_count: 5
  name: Linkedin Talent Learning Parent Application Provision Application Request Example
  slug: linkedin-talent-learning-parent-application-provision-application-request-example
- key_count: 8
  name: Linkedin Talent Learning Parent Application Provision Application Response Example
  slug: linkedin-talent-learning-parent-application-provision-application-response-example
- key_count: 1
  name: Linkedin Talent Learning Parent Application Update Callback Url Request Example
  slug: linkedin-talent-learning-parent-application-update-callback-url-request-example
- key_count: 3
  name: Linkedin Talent Recruiter System Connect Access Token Request Example
  slug: linkedin-talent-recruiter-system-connect-access-token-request-example
- key_count: 3
  name: Linkedin Talent Recruiter System Connect Access Token Response Example
  slug: linkedin-talent-recruiter-system-connect-access-token-response-example
- key_count: 6
  name: Linkedin Talent Recruiter System Connect Address Example
  slug: linkedin-talent-recruiter-system-connect-address-example
- key_count: 10
  name: Linkedin Talent Recruiter System Connect Application Data Example
  slug: linkedin-talent-recruiter-system-connect-application-data-example
- key_count: 1
  name: Linkedin Talent Recruiter System Connect Application Request Example
  slug: linkedin-talent-recruiter-system-connect-application-request-example
- key_count: 1
  name: Linkedin Talent Recruiter System Connect Ats Integration Update Request Example
  slug: linkedin-talent-recruiter-system-connect-ats-integration-update-request-example
- key_count: 10
  name: Linkedin Talent Recruiter System Connect Candidate Data Example
  slug: linkedin-talent-recruiter-system-connect-candidate-data-example
- key_count: 1
  name: Linkedin Talent Recruiter System Connect Candidate Request Example
  slug: linkedin-talent-recruiter-system-connect-candidate-request-example
- key_count: 1
  name: Linkedin Talent Recruiter System Connect Configuration Value Example
  slug: linkedin-talent-recruiter-system-connect-configuration-value-example
- key_count: 1
  name: Linkedin Talent Recruiter System Connect Integration Configuration Request Example
  slug: linkedin-talent-recruiter-system-connect-integration-configuration-request-example
- key_count: 1
  name: Linkedin Talent Recruiter System Connect Integration Patch Example
  slug: linkedin-talent-recruiter-system-connect-integration-patch-example
- key_count: 3
  name: Linkedin Talent Recruiter System Connect Note Data Example
  slug: linkedin-talent-recruiter-system-connect-note-data-example
- key_count: 1
  name: Linkedin Talent Recruiter System Connect Note Request Example
  slug: linkedin-talent-recruiter-system-connect-note-request-example
- key_count: 2
  name: Linkedin Talent Recruiter System Connect Person Name Example
  slug: linkedin-talent-recruiter-system-connect-person-name-example
- key_count: 2
  name: Linkedin Talent Recruiter System Connect Phone Number Example
  slug: linkedin-talent-recruiter-system-connect-phone-number-example
- key_count: 6
  name: Linkedin Updateadaccount Example
  slug: linkedin-updateadaccount-example
features:
- description: OpenID Connect-based authentication enabling users to sign in to third-party applications with their LinkedIn credentials.
  name: Sign In with LinkedIn
- description: Enable users to share content from your application directly to their LinkedIn feed.
  name: Share on LinkedIn
- description: Display verified professional credentials and certifications from LinkedIn on third-party platforms.
  name: Verified on LinkedIn
- description: Programmatically create, manage, and optimize B2B advertising campaigns with targeting and budget controls.
  name: Campaign Management
- description: Access aggregated audience demographics and firmographic data for ad targeting and market research.
  name: Audience Insights
- description: Send online and offline conversion events for attribution and campaign optimization.
  name: Conversions API
- description: Collect leads directly from LinkedIn ads with pre-filled forms using member profile data.
  name: Lead Gen Forms
- description: Programmatically publish and manage job listings on LinkedIn through the Talent Solutions API.
  name: Job Posting
- description: Integrate applicant tracking systems with LinkedIn Recruiter for seamless candidate management.
  name: Recruiter System Connect
- description: Retrieve learner engagement, completions, and activity data from LinkedIn Learning.
  name: Learning Activity Reports
- description: Archive and monitor LinkedIn messages and activities for regulatory compliance in regulated industries.
  name: Compliance Archiving
- description: Access member and organization data portability endpoints for Digital Markets Act compliance.
  name: Data Portability
finops:
- has_sources: true
  method: generated
  name: Linkedin Finops
  primary_unit: ''
  service_category: Marketing / Recruiting / Professional Networking
  slug: linkedin-finops
  template: false
image: https://content.linkedin.com/content/dam/me/business/en-us/amp/brand-site/v2/bg/LI-Bug.svg.original.svg
integrations:
- description: LinkedIn Sales Navigator integration with Salesforce CRM for lead and account synchronization.
  name: Salesforce
- description: Native integration with Microsoft Dynamics 365 for sales intelligence and lead management.
  name: Microsoft Dynamics
- description: LinkedIn Ads integration with HubSpot for campaign management and lead synchronization.
  name: HubSpot
- description: Official Postman workspaces for all LinkedIn API business lines with pre-built collections.
  name: Postman
- description: Standards-based authentication using OpenID Connect for Sign In with LinkedIn.
  name: OpenID Connect
json_schemas:
- name: AccessTokenRequest
  property_count: 3
  slug: linkedin-access-token-request
- name: AccessTokenResponse
  property_count: 3
  slug: linkedin-access-token-response
- name: AccessTokenRequest
  property_count: 3
  slug: linkedin-accesstokenrequest
- name: AccessTokenResponse
  property_count: 3
  slug: linkedin-accesstokenresponse
- name: AdAccountCreateRequest
  property_count: 9
  slug: linkedin-ad-account-create-request
- name: AdAccount
  property_count: 11
  slug: linkedin-ad-account
- name: AdAccountSearchResponse
  property_count: 2
  slug: linkedin-ad-account-search-response
- name: AdAccountUserCreateRequest
  property_count: 3
  slug: linkedin-ad-account-user-create-request
- name: AdAccountUser
  property_count: 3
  slug: linkedin-ad-account-user
- name: AdAccountUserUpdateRequest
  property_count: 1
  slug: linkedin-ad-account-user-update-request
- name: AdAccountsResponse
  property_count: 2
  slug: linkedin-ad-accounts-response
- name: AdCampaign
  property_count: 12
  slug: linkedin-ad-campaign
- name: AdTargetingEntitiesResponse
  property_count: 2
  slug: linkedin-ad-targeting-entities-response
- name: AdTargetingFacetsResponse
  property_count: 2
  slug: linkedin-ad-targeting-facets-response
- name: AdAccount
  property_count: 4
  slug: linkedin-adaccount
- name: AdAccountCreateRequest
  property_count: 9
  slug: linkedin-adaccountcreaterequest
- name: AdAccountsResponse
  property_count: 2
  slug: linkedin-adaccountsresponse
- name: AdAccountUser
  property_count: 3
  slug: linkedin-adaccountuser
- name: AdAccountUserCreateRequest
  property_count: 3
  slug: linkedin-adaccountusercreaterequest
- name: AdAccountUserUpdateRequest
  property_count: 1
  slug: linkedin-adaccountuserupdaterequest
- name: AdditionalQuestions
  property_count: 1
  slug: linkedin-additionalquestions
- name: Address
  property_count: 5
  slug: linkedin-address
- name: AdTargetingEntitiesResponse
  property_count: 2
  slug: linkedin-adtargetingentitiesresponse
- name: AdTargetingEntity
  property_count: 3
  slug: linkedin-adtargetingentity
- name: AdTargetingFacet
  property_count: 4
  slug: linkedin-adtargetingfacet
- name: AdTargetingFacetsResponse
  property_count: 2
  slug: linkedin-adtargetingfacetsresponse
- name: AdvertiserTransparencyResponse
  property_count: 7
  slug: linkedin-advertiser-transparency-response
- name: AdvertiserTransparencyRequest
  property_count: 2
  slug: linkedin-advertisertransparencyrequest
- name: AdvertiserTransparencyResponse
  property_count: 7
  slug: linkedin-advertisertransparencyresponse
- name: AnalyticsResponse
  property_count: 2
  slug: linkedin-analytics-response
- name: AnalyticsRecord
  property_count: 7
  slug: linkedin-analyticsrecord
- name: AnalyticsResponse
  property_count: 2
  slug: linkedin-analyticsresponse
- name: ApplicationRequest
  property_count: 1
  slug: linkedin-application-request
- name: ApplicationCredentials
  property_count: 4
  slug: linkedin-applicationcredentials
- name: ApplicationData
  property_count: 10
  slug: linkedin-applicationdata
- name: ApplicationQuestions
  property_count: 6
  slug: linkedin-applicationquestions
- name: ApplicationRequest
  property_count: 1
  slug: linkedin-applicationrequest
- name: AssociateCampaignsToConversionRequest
  property_count: 0
  slug: linkedin-associatecampaignstoconversionrequest
- name: AssociateCampaignsToConversionResponse204
  property_count: 0
  slug: linkedin-associatecampaignstoconversionresponse204
- name: AtsIntegrationResponse
  property_count: 1
  slug: linkedin-ats-integration-response
- name: AtsIntegrationUpdateRequest
  property_count: 1
  slug: linkedin-ats-integration-update-request
- name: AtsIntegrationDetail
  property_count: 4
  slug: linkedin-atsintegrationdetail
- name: AtsIntegrationPatch
  property_count: 1
  slug: linkedin-atsintegrationpatch
- name: AtsIntegrationResponse
  property_count: 1
  slug: linkedin-atsintegrationresponse
- name: AtsIntegrationUpdateRequest
  property_count: 1
  slug: linkedin-atsintegrationupdaterequest
- name: AudienceCount
  property_count: 2
  slug: linkedin-audience-count
- name: AudienceInsightsRequest
  property_count: 1
  slug: linkedin-audience-insights-request
- name: AudienceInsightsResponse
  property_count: 1
  slug: linkedin-audience-insights-response
- name: AudienceCount
  property_count: 2
  slug: linkedin-audiencecount
- name: AudienceInsight
  property_count: 2
  slug: linkedin-audienceinsight
- name: AudienceInsightsRequest
  property_count: 1
  slug: linkedin-audienceinsightsrequest
- name: AudienceInsightsResponse
  property_count: 1
  slug: linkedin-audienceinsightsresponse
- name: BatchCreateSponsoredMessageRequest
  property_count: 0
  slug: linkedin-batch-create-sponsored-message-request
- name: BatchGetOnAdministeredResponse200
  property_count: 3
  slug: linkedin-batch-get-on-administered-response200
- name: BatchGetOnNonadministeredResponse200
  property_count: 3
  slug: linkedin-batch-get-on-nonadministered-response200
- name: BatchOrganizationResponse
  property_count: 3
  slug: linkedin-batch-organization-response
- name: BatchProfileAssociationResponse
  property_count: 3
  slug: linkedin-batch-profile-association-response
- name: BatchUpdateSponsoredMessageRequest
  property_count: 0
  slug: linkedin-batch-update-sponsored-message-request
- name: BatchCreateSponsoredMessageRequest
  property_count: 0
  slug: linkedin-batchcreatesponsoredmessagerequest
- name: BatchGetOnAdministeredResponse200
  property_count: 3
  slug: linkedin-batchgetonadministeredresponse200
- name: BatchGetOnNonadministeredResponse200
  property_count: 3
  slug: linkedin-batchgetonnonadministeredresponse200
- name: BatchOrganizationResponse
  property_count: 3
  slug: linkedin-batchorganizationresponse
- name: BatchProfileAssociationResponse
  property_count: 3
  slug: linkedin-batchprofileassociationresponse
- name: BatchUpdateSponsoredMessageRequest
  property_count: 0
  slug: linkedin-batchupdatesponsoredmessagerequest
- name: Budget
  property_count: 2
  slug: linkedin-budget
- name: CampaignGroup
  property_count: 6
  slug: linkedin-campaign-group
- name: Campaign
  property_count: 10
  slug: linkedin-campaign
- name: CampaignUpdateRequest
  property_count: 1
  slug: linkedin-campaign-update-request
- name: CampaignGroup
  property_count: 6
  slug: linkedin-campaigngroup
- name: CampaignUpdateRequest
  property_count: 1
  slug: linkedin-campaignupdaterequest
- name: CandidateData
  property_count: 13
  slug: linkedin-candidate-data
- name: CandidateRequest
  property_count: 1
  slug: linkedin-candidate-request
- name: CandidateData
  property_count: 13
  slug: linkedin-candidatedata
- name: CandidateRequest
  property_count: 1
  slug: linkedin-candidaterequest
- name: CommentResponse
  property_count: 2
  slug: linkedin-comment-response
- name: Comment
  property_count: 5
  slug: linkedin-comment
- name: CommentResponse
  property_count: 2
  slug: linkedin-commentresponse
- name: CompanyStreamRequest
  property_count: 1
  slug: linkedin-company-stream-request
- name: CompanyStreamElement
  property_count: 4
  slug: linkedin-companystreamelement
- name: CompanyStreamRequest
  property_count: 1
  slug: linkedin-companystreamrequest
- name: ComplianceAuthorizationRequest
  property_count: 1
  slug: linkedin-compliance-authorization-request
- name: ComplianceAuthorizationResponse
  property_count: 2
  slug: linkedin-compliance-authorization-response
- name: ComplianceAuthorization
  property_count: 4
  slug: linkedin-compliance-authorization
- name: ComplianceAuthorizationRequest
  property_count: 1
  slug: linkedin-compliance-events-compliance-authorization-request
- name: ComplianceAuthorizationResponse
  property_count: 2
  slug: linkedin-compliance-events-compliance-authorization-response
- name: ComplianceAuthorization
  property_count: 4
  slug: linkedin-compliance-events-compliance-authorization
- name: ComplianceEvent
  property_count: 15
  slug: linkedin-compliance-events-compliance-event
- name: ComplianceEventsResponse
  property_count: 2
  slug: linkedin-compliance-events-compliance-events-response
- name: ErrorResponse
  property_count: 3
  slug: linkedin-compliance-events-error-response
- name: MemberProfile
  property_count: 3
  slug: linkedin-compliance-events-member-profile
- name: PagingLink
  property_count: 3
  slug: linkedin-compliance-events-paging-link
- name: Paging
  property_count: 4
  slug: linkedin-compliance-events-paging
- name: ComplianceEventsResponse
  property_count: 2
  slug: linkedin-compliance-events-response
- name: ComplianceAuthorization
  property_count: 4
  slug: linkedin-complianceauthorization
- name: ComplianceAuthorizationRequest
  property_count: 1
  slug: linkedin-complianceauthorizationrequest
- name: ComplianceAuthorizationResponse
  property_count: 2
  slug: linkedin-complianceauthorizationresponse
- name: ComplianceEvent
  property_count: 15
  slug: linkedin-complianceevent
- name: ComplianceEventsResponse
  property_count: 2
  slug: linkedin-complianceeventsresponse
- name: ConfigurationValue
  property_count: 1
  slug: linkedin-configurationvalue
- name: Contract
  property_count: 4
  slug: linkedin-contract
- name: ContractsResponse
  property_count: 2
  slug: linkedin-contracts-response
- name: ContractsResponse
  property_count: 2
  slug: linkedin-contractsresponse
- name: ConversionsByMemberCompanyResponse200
  property_count: 2
  slug: linkedin-conversions-by-member-company-response200
- name: ConversionsByMemberCompanyResponse200
  property_count: 2
  slug: linkedin-conversionsbymembercompanyresponse200
- name: CoverLetterQuestions
  property_count: 1
  slug: linkedin-coverletterquestions
- name: CreateADynamicSpotlightRequest
  property_count: 0
  slug: linkedin-create-adynamic-spotlight-request
- name: CreateANewConversionRequest
  property_count: 0
  slug: linkedin-create-anew-conversion-request
- name: CreateANewConversionResponse201
  property_count: 14
  slug: linkedin-create-anew-conversion-response201
- name: CreateAShareWithRequest
  property_count: 0
  slug: linkedin-create-ashare-with-request
- name: CreateASubscriptionRequestRequest
  property_count: 0
  slug: linkedin-create-asubscription-request-request
- name: CreateDocumentContentRequest
  property_count: 0
  slug: linkedin-create-document-content-request
- name: CreateInmailContentRequest
  property_count: 0
  slug: linkedin-create-inmail-content-request
- name: CreateADynamicSpotlightRequest
  property_count: 0
  slug: linkedin-createadynamicspotlightrequest
- name: CreateANewConversionRequest
  property_count: 0
  slug: linkedin-createanewconversionrequest
- name: CreateANewConversionResponse201
  property_count: 14
  slug: linkedin-createanewconversionresponse201
- name: CreateAShareWithRequest
  property_count: 0
  slug: linkedin-createasharewithrequest
- name: CreateASubscriptionRequestRequest
  property_count: 0
  slug: linkedin-createasubscriptionrequestrequest
- name: CreateDocumentContentRequest
  property_count: 0
  slug: linkedin-createdocumentcontentrequest
- name: CreateInmailContentRequest
  property_count: 0
  slug: linkedin-createinmailcontentrequest
- name: CreativeCreateRequest
  property_count: 5
  slug: linkedin-creative-create-request
- name: Creative
  property_count: 5
  slug: linkedin-creative
- name: CreativeCreateRequest
  property_count: 5
  slug: linkedin-creativecreaterequest
- name: CrmDataValidationExportJobRequest
  property_count: 1
  slug: linkedin-crm-data-validation-export-job-request
- name: CrmDataValidationExportJob
  property_count: 7
  slug: linkedin-crm-data-validation-export-job
- name: CrmDataValidationExportJob
  property_count: 7
  slug: linkedin-crmdatavalidationexportjob
- name: CrmDataValidationExportJobRequest
  property_count: 1
  slug: linkedin-crmdatavalidationexportjobrequest
- name: CustomQuestion
  property_count: 4
  slug: linkedin-customquestion
- name: CustomQuestionSet
  property_count: 2
  slug: linkedin-customquestionset
- name: DateInfo
  property_count: 3
  slug: linkedin-dateinfo
- name: DmpSegmentCreateRequest
  property_count: 6
  slug: linkedin-dmp-segment-create-request
- name: DmpSegment
  property_count: 11
  slug: linkedin-dmp-segment
- name: DmpSegmentsResponse
  property_count: 2
  slug: linkedin-dmp-segments-response
- name: DmpSegment
  property_count: 11
  slug: linkedin-dmpsegment
- name: DmpSegmentCreateRequest
  property_count: 6
  slug: linkedin-dmpsegmentcreaterequest
- name: DmpSegmentsResponse
  property_count: 2
  slug: linkedin-dmpsegmentsresponse
- name: EducationQuestions
  property_count: 1
  slug: linkedin-educationquestions
- name: EntityAclRequest
  property_count: 1
  slug: linkedin-entity-acl-request
- name: EntityAclRequest
  property_count: 1
  slug: linkedin-entityaclrequest
- name: ErrorDetail
  property_count: 3
  slug: linkedin-errordetail
- name: ErrorResponse
  property_count: 3
  slug: linkedin-errorresponse
- name: Evaluation
  property_count: 2
  slug: linkedin-evaluation
- name: EventResponse
  property_count: 2
  slug: linkedin-event-response
- name: Event
  property_count: 8
  slug: linkedin-event
- name: EventResponse
  property_count: 2
  slug: linkedin-eventresponse
- name: ExportedCandidateResponse
  property_count: 1
  slug: linkedin-exported-candidate-response
- name: ExportedCandidate
  property_count: 5
  slug: linkedin-exportedcandidate
- name: ExportedCandidateResponse
  property_count: 1
  slug: linkedin-exportedcandidateresponse
- name: FetchActiveCampaignsResponse200
  property_count: 2
  slug: linkedin-fetch-active-campaigns-response200
- name: FetchExistingConversionRulesResponse200
  property_count: 2
  slug: linkedin-fetch-existing-conversion-rules-response200
- name: FetchFullLeadDataResponse200
  property_count: 10
  slug: linkedin-fetch-full-lead-data-response200
- name: FetchActiveCampaignsResponse200
  property_count: 2
  slug: linkedin-fetchactivecampaignsresponse200
- name: FetchExistingConversionRulesResponse200
  property_count: 2
  slug: linkedin-fetchexistingconversionrulesresponse200
- name: FetchFullLeadDataResponse200
  property_count: 10
  slug: linkedin-fetchfullleaddataresponse200
- name: FindAdministeredOrganizationBrandsResponse200
  property_count: 2
  slug: linkedin-find-administered-organization-brands-response200
- name: FindNonadministeredOrganizationResponse200
  property_count: 3
  slug: linkedin-find-nonadministered-organization-response200
- name: FindAdministeredOrganizationBrandsResponse200
  property_count: 2
  slug: linkedin-findadministeredorganizationbrandsresponse200
- name: FindNonadministeredOrganizationResponse200
  property_count: 3
  slug: linkedin-findnonadministeredorganizationresponse200
- name: ForecastAvgLifetimeFrequencyRequest
  property_count: 0
  slug: linkedin-forecast-avg-lifetime-frequency-request
- name: ForecastAvgLifetimeFrequencyRequest
  property_count: 0
  slug: linkedin-forecastavglifetimefrequencyrequest
- name: ForecastAvgLifetimeFrequencyResponseundefined
  property_count: 0
  slug: linkedin-forecastavglifetimefrequencyresponseundefined
- name: GetApplicationResponse
  property_count: 1
  slug: linkedin-get-application-response
- name: GetFormsForTheResponse200
  property_count: 2
  slug: linkedin-get-forms-for-the-response200
- name: GetTheUsersSponsoredResponse200
  property_count: 2
  slug: linkedin-get-the-users-sponsored-response200
- name: GetAListOfResponse200
  property_count: 2
  slug: linkedin-getalistofresponse200
- name: GetApplicationResponse
  property_count: 1
  slug: linkedin-getapplicationresponse
- name: GetBingGeoLocationsResponse200
  property_count: 2
  slug: linkedin-getbinggeolocationsresponse200
- name: GetFormsForTheResponse200
  property_count: 2
  slug: linkedin-getformsfortheresponse200
- name: GetTheUsersSponsoredResponse200
  property_count: 2
  slug: linkedin-gettheuserssponsoredresponse200
- name: ImageAsset
  property_count: 3
  slug: linkedin-imageasset
- name: ImageReference
  property_count: 3
  slug: linkedin-imagereference
- name: InitializeImageUploadRequest
  property_count: 0
  slug: linkedin-initialize-image-upload-request
- name: InitializeVideoUploadRequest
  property_count: 0
  slug: linkedin-initialize-video-upload-request
- name: InitializeImageUploadRequest
  property_count: 0
  slug: linkedin-initializeimageuploadrequest
- name: InitializeVideoUploadRequest
  property_count: 0
  slug: linkedin-initializevideouploadrequest
- name: InsightSegmentation
  property_count: 3
  slug: linkedin-insightsegmentation
- name: IntegrationConfigurationRequest
  property_count: 1
  slug: linkedin-integrationconfigurationrequest
- name: IntegrationPatch
  property_count: 1
  slug: linkedin-integrationpatch
- name: InterviewFeedbackData
  property_count: 4
  slug: linkedin-interviewfeedbackdata
- name: InterviewFeedbackRequest
  property_count: 1
  slug: linkedin-interviewfeedbackrequest
- name: JobPostingResponse
  property_count: 1
  slug: linkedin-job-posting-response
- name: JobPostingTaskResponse
  property_count: 1
  slug: linkedin-job-posting-task-response
- name: JobPostingElement
  property_count: 10
  slug: linkedin-jobpostingelement
- name: JobPostingResponse
  property_count: 1
  slug: linkedin-jobpostingresponse
- name: JobPostingResult
  property_count: 2
  slug: linkedin-jobpostingresult
- name: JobPostingTaskResponse
  property_count: 1
  slug: linkedin-jobpostingtaskresponse
- name: JobPostingTaskResult
  property_count: 3
  slug: linkedin-jobpostingtaskresult
- name: LeadGenResponse
  property_count: 2
  slug: linkedin-lead-gen-response
- name: LeadGenAnswer
  property_count: 2
  slug: linkedin-leadgenanswer
- name: LeadGenRecord
  property_count: 4
  slug: linkedin-leadgenrecord
- name: LeadGenResponse
  property_count: 2
  slug: linkedin-leadgenresponse
- name: LearnerDetails
  property_count: 1
  slug: linkedin-learnerdetails
- name: LearnerEntity
  property_count: 4
  slug: linkedin-learnerentity
- name: LearningActivityReportResponse
  property_count: 2
  slug: linkedin-learning-activity-report-response
- name: ErrorResponse
  property_count: 3
  slug: linkedin-learning-activity-reports-error-response
- name: LearnerDetails
  property_count: 1
  slug: linkedin-learning-activity-reports-learner-details
- name: LearnerEntity
  property_count: 4
  slug: linkedin-learning-activity-reports-learner-entity
- name: LearningActivityReportResponse
  property_count: 2
  slug: linkedin-learning-activity-reports-learning-activity-report-response
- name: LearningActivityReport
  property_count: 3
  slug: linkedin-learning-activity-reports-learning-activity-report
- name: LearningActivity
  property_count: 6
  slug: linkedin-learning-activity-reports-learning-activity
- name: PagingLink
  property_count: 3
  slug: linkedin-learning-activity-reports-paging-link
- name: Paging
  property_count: 4
  slug: linkedin-learning-activity-reports-paging
- name: LearningActivity
  property_count: 6
  slug: linkedin-learningactivity
- name: LearningActivityReport
  property_count: 3
  slug: linkedin-learningactivityreport
- name: LearningActivityReportResponse
  property_count: 2
  slug: linkedin-learningactivityreportresponse
- name: ListUploadRequest
  property_count: 1
  slug: linkedin-list-upload-request
- name: ListUploadRequest
  property_count: 1
  slug: linkedin-listuploadrequest
- name: Locale
  property_count: 2
  slug: linkedin-locale
- name: LocalizedString
  property_count: 2
  slug: linkedin-localizedstring
- name: LookupByOrganizationPrimaryResponse200
  property_count: 1
  slug: linkedin-lookup-by-organization-primary-response200
- name: LookupByOrganizationPrimaryResponse200
  property_count: 1
  slug: linkedin-lookupbyorganizationprimaryresponse200
- name: AdAccount
  property_count: 4
  slug: linkedin-marketing-audience-ad-account
- name: AdAccountsResponse
  property_count: 2
  slug: linkedin-marketing-audience-ad-accounts-response
- name: CompanyStreamElement
  property_count: 4
  slug: linkedin-marketing-audience-company-stream-element
- name: CompanyStreamRequest
  property_count: 1
  slug: linkedin-marketing-audience-company-stream-request
- name: DmpSegmentCreateRequest
  property_count: 6
  slug: linkedin-marketing-audience-dmp-segment-create-request
- name: DmpSegment
  property_count: 11
  slug: linkedin-marketing-audience-dmp-segment
- name: DmpSegmentsResponse
  property_count: 2
  slug: linkedin-marketing-audience-dmp-segments-response
- name: AdTargetingEntitiesResponse
  property_count: 2
  slug: linkedin-marketing-audience-insights-ad-targeting-entities-response
- name: AdTargetingEntity
  property_count: 3
  slug: linkedin-marketing-audience-insights-ad-targeting-entity
- name: AdTargetingFacet
  property_count: 4
  slug: linkedin-marketing-audience-insights-ad-targeting-facet
- name: AdTargetingFacetsResponse
  property_count: 2
  slug: linkedin-marketing-audience-insights-ad-targeting-facets-response
- name: AudienceInsight
  property_count: 2
  slug: linkedin-marketing-audience-insights-audience-insight
- name: AudienceInsightsRequest
  property_count: 1
  slug: linkedin-marketing-audience-insights-audience-insights-request
- name: AudienceInsightsResponse
  property_count: 1
  slug: linkedin-marketing-audience-insights-audience-insights-response
- name: ErrorResponse
  property_count: 3
  slug: linkedin-marketing-audience-insights-error-response
- name: InsightSegmentation
  property_count: 3
  slug: linkedin-marketing-audience-insights-insight-segmentation
- name: PagingLink
  property_count: 3
  slug: linkedin-marketing-audience-insights-paging-link
- name: Paging
  property_count: 4
  slug: linkedin-marketing-audience-insights-paging
- name: RequestMetaData
  property_count: 1
  slug: linkedin-marketing-audience-insights-request-meta-data
- name: TargetingCriteria
  property_count: 1
  slug: linkedin-marketing-audience-insights-targeting-criteria
- name: ListUploadRequest
  property_count: 1
  slug: linkedin-marketing-audience-list-upload-request
- name: Paging
  property_count: 4
  slug: linkedin-marketing-audience-paging
- name: SegmentDestination
  property_count: 1
  slug: linkedin-marketing-audience-segment-destination
- name: StreamResponse
  property_count: 1
  slug: linkedin-marketing-audience-stream-response
- name: StreamResultElement
  property_count: 1
  slug: linkedin-marketing-audience-stream-result-element
- name: UserId
  property_count: 2
  slug: linkedin-marketing-audience-user-id
- name: UserStreamElement
  property_count: 2
  slug: linkedin-marketing-audience-user-stream-element
- name: UserStreamRequest
  property_count: 1
  slug: linkedin-marketing-audience-user-stream-request
- name: AdAccountCreateRequest
  property_count: 9
  slug: linkedin-marketing-campaigns-ad-account-create-request
- name: AdAccount
  property_count: 11
  slug: linkedin-marketing-campaigns-ad-account
- name: AdAccountUserCreateRequest
  property_count: 3
  slug: linkedin-marketing-campaigns-ad-account-user-create-request
- name: AdAccountUser
  property_count: 3
  slug: linkedin-marketing-campaigns-ad-account-user
- name: AdAccountUserUpdateRequest
  property_count: 1
  slug: linkedin-marketing-campaigns-ad-account-user-update-request
- name: AudienceCount
  property_count: 2
  slug: linkedin-marketing-campaigns-audience-count
- name: Budget
  property_count: 2
  slug: linkedin-marketing-campaigns-budget
- name: CampaignGroup
  property_count: 6
  slug: linkedin-marketing-campaigns-campaign-group
- name: Campaign
  property_count: 10
  slug: linkedin-marketing-campaigns-campaign
- name: CampaignUpdateRequest
  property_count: 1
  slug: linkedin-marketing-campaigns-campaign-update-request
- name: CreativeCreateRequest
  property_count: 5
  slug: linkedin-marketing-campaigns-creative-create-request
- name: Creative
  property_count: 5
  slug: linkedin-marketing-campaigns-creative
- name: OrganizationAcl
  property_count: 3
  slug: linkedin-marketing-campaigns-organization-acl
- name: Paging
  property_count: 4
  slug: linkedin-marketing-campaigns-paging
- name: RunSchedule
  property_count: 2
  slug: linkedin-marketing-campaigns-run-schedule
- name: BatchGetOnAdministeredResponse200
  property_count: 3
  slug: linkedin-marketing-community-batch-get-on-administered-response200
- name: BatchGetOnNonadministeredResponse200
  property_count: 3
  slug: linkedin-marketing-community-batch-get-on-nonadministered-response200
- name: FindAdministeredOrganizationBrandsResponse200
  property_count: 2
  slug: linkedin-marketing-community-find-administered-organization-brands-response200
- name: FindNonadministeredOrganizationResponse200
  property_count: 3
  slug: linkedin-marketing-community-find-nonadministered-organization-response200
- name: LookupByOrganizationPrimaryResponse200
  property_count: 1
  slug: linkedin-marketing-community-lookup-by-organization-primary-response200
- name: RetrieveAnAdministeredOrganizationResponse200
  property_count: 16
  slug: linkedin-marketing-community-retrieve-an-administered-organization-response200
- name: RetrieveOrganizationFollowerCountResponse200
  property_count: 1
  slug: linkedin-marketing-community-retrieve-organization-follower-count-response200
- name: CreateANewConversionResponse201
  property_count: 14
  slug: linkedin-marketing-conversions-create-a-new-conversion-response201
- name: FetchActiveCampaignsResponse200
  property_count: 2
  slug: linkedin-marketing-conversions-fetch-active-campaigns-response200
- name: FetchExistingConversionRulesResponse200
  property_count: 2
  slug: linkedin-marketing-conversions-fetch-existing-conversion-rules-response200
- name: RetrieveAuthenticatedUsersSponsoredResponse200
  property_count: 2
  slug: linkedin-marketing-conversions-retrieve-authenticated-users-sponsored-response200
- name: StreamMultipleConversionEventsResponse200
  property_count: 1
  slug: linkedin-marketing-conversions-stream-multiple-conversion-events-response200
- name: FetchFullLeadDataResponse200
  property_count: 10
  slug: linkedin-marketing-leads-fetch-full-lead-data-response200
- name: GetFormsForTheResponse200
  property_count: 2
  slug: linkedin-marketing-leads-get-forms-for-the-response200
- name: GetTheUsersSponsoredResponse200
  property_count: 2
  slug: linkedin-marketing-leads-get-the-users-sponsored-response200
- name: ValidateTheUsersOrganizationResponse200
  property_count: 2
  slug: linkedin-marketing-leads-validate-the-users-organization-response200
- name: GetAListOfResponse200
  property_count: 2
  slug: linkedin-marketing-media-planning-get-a-list-of-response200
- name: GetBingGeoLocationsResponse200
  property_count: 2
  slug: linkedin-marketing-media-planning-get-bing-geo-locations-response200
- name: ConversionsByMemberCompanyResponse200
  property_count: 2
  slug: linkedin-marketing-reporting-roi-conversions-by-member-company-response200
- name: MemberProfile
  property_count: 3
  slug: linkedin-memberprofile
- name: MultipleChoiceQuestionDetails
  property_count: 3
  slug: linkedin-multiplechoicequestiondetails
- name: NoteData
  property_count: 3
  slug: linkedin-notedata
- name: NoteRequest
  property_count: 1
  slug: linkedin-noterequest
- name: OnsiteApplyConfiguration
  property_count: 2
  slug: linkedin-onsiteapplyconfiguration
- name: OrganizationAclResponse
  property_count: 2
  slug: linkedin-organization-acl-response
- name: OrganizationAcl
  property_count: 3
  slug: linkedin-organization-acl
- name: OrganizationResponse
  property_count: 18
  slug: linkedin-organization-response
- name: OrganizationAcl
  property_count: 3
  slug: linkedin-organizationacl
- name: OrganizationAclResponse
  property_count: 2
  slug: linkedin-organizationaclresponse
- name: OrganizationLocation
  property_count: 5
  slug: linkedin-organizationlocation
- name: OrganizationResponse
  property_count: 18
  slug: linkedin-organizationresponse
- name: Paging
  property_count: 4
  slug: linkedin-paging
- name: PagingLink
  property_count: 3
  slug: linkedin-paginglink
- name: PersonName
  property_count: 2
  slug: linkedin-personname
- name: PhoneNumber
  property_count: 2
  slug: linkedin-phonenumber
- name: PostResponse
  property_count: 2
  slug: linkedin-post-response
- name: Post
  property_count: 7
  slug: linkedin-post
- name: PostResponse
  property_count: 2
  slug: linkedin-postresponse
- name: ProvisionApplicationRequest
  property_count: 5
  slug: linkedin-provision-application-request
- name: ProvisionApplicationResponse
  property_count: 8
  slug: linkedin-provision-application-response
- name: ProvisionApplicationRequest
  property_count: 5
  slug: linkedin-provisionapplicationrequest
- name: ProvisionApplicationResponse
  property_count: 8
  slug: linkedin-provisionapplicationresponse
- name: QuestionChoice
  property_count: 2
  slug: linkedin-questionchoice
- name: QuestionDetails
  property_count: 1
  slug: linkedin-questiondetails
- name: ReactionResponse
  property_count: 2
  slug: linkedin-reaction-response
- name: Reaction
  property_count: 3
  slug: linkedin-reaction
- name: ReactionResponse
  property_count: 2
  slug: linkedin-reactionresponse
- name: Address
  property_count: 5
  slug: linkedin-regulations-data-portability-address
- name: BatchOrganizationResponse
  property_count: 3
  slug: linkedin-regulations-data-portability-batch-organization-response
- name: DateInfo
  property_count: 3
  slug: linkedin-regulations-data-portability-date-info
- name: ImageAsset
  property_count: 3
  slug: linkedin-regulations-data-portability-image-asset
- name: ImageReference
  property_count: 3
  slug: linkedin-regulations-data-portability-image-reference
- name: Locale
  property_count: 2
  slug: linkedin-regulations-data-portability-locale
- name: LocalizedString
  property_count: 2
  slug: linkedin-regulations-data-portability-localized-string
- name: OrganizationAclResponse
  property_count: 2
  slug: linkedin-regulations-data-portability-organization-acl-response
- name: OrganizationAcl
  property_count: 5
  slug: linkedin-regulations-data-portability-organization-acl
- name: OrganizationLocation
  property_count: 5
  slug: linkedin-regulations-data-portability-organization-location
- name: OrganizationResponse
  property_count: 18
  slug: linkedin-regulations-data-portability-organization-response
- name: PostResponse
  property_count: 2
  slug: linkedin-regulations-data-portability-post-response
- name: Post
  property_count: 7
  slug: linkedin-regulations-data-portability-post
- name: ReactionResponse
  property_count: 2
  slug: linkedin-regulations-data-portability-reaction-response
- name: Timestamp
  property_count: 1
  slug: linkedin-regulations-data-portability-timestamp
- name: AdvertiserTransparencyRequest
  property_count: 2
  slug: linkedin-regulatory-ads-transparency-advertiser-transparency-request
- name: AdvertiserTransparencyResponse
  property_count: 7
  slug: linkedin-regulatory-ads-transparency-advertiser-transparency-response
- name: ErrorResponse
  property_count: 3
  slug: linkedin-regulatory-ads-transparency-error-response
- name: RequestMetaData
  property_count: 1
  slug: linkedin-requestmetadata
- name: ResumeUploadRequest
  property_count: 5
  slug: linkedin-resume-upload-request
- name: ResumeUploadResponse
  property_count: 2
  slug: linkedin-resume-upload-response
- name: ResumeQuestions
  property_count: 1
  slug: linkedin-resumequestions
- name: ResumeUploadRequest
  property_count: 5
  slug: linkedin-resumeuploadrequest
- name: ResumeUploadResponse
  property_count: 2
  slug: linkedin-resumeuploadresponse
- name: RetrieveAnAdministeredOrganizationResponse200
  property_count: 16
  slug: linkedin-retrieve-an-administered-organization-response200
- name: RetrieveAuthenticatedUsersSponsoredResponse200
  property_count: 2
  slug: linkedin-retrieve-authenticated-users-sponsored-response200
- name: RetrieveOrganizationFollowerCountResponse200
  property_count: 1
  slug: linkedin-retrieve-organization-follower-count-response200
- name: RetrieveAnAdministeredOrganizationResponse200
  property_count: 16
  slug: linkedin-retrieveanadministeredorganizationresponse200
- name: RetrieveAuthenticatedUsersSponsoredResponse200
  property_count: 2
  slug: linkedin-retrieveauthenticateduserssponsoredresponse200
- name: RetrieveOrganizationFollowerCountResponse200
  property_count: 1
  slug: linkedin-retrieveorganizationfollowercountresponse200
- name: RunSchedule
  property_count: 2
  slug: linkedin-runschedule
- name: SalesAccessTokenResponse
  property_count: 2
  slug: linkedin-sales-access-token-response
- name: SalesAnalyticsExportJobRequest
  property_count: 3
  slug: linkedin-sales-analytics-export-job-request
- name: SalesAnalyticsExportJobResponse
  property_count: 1
  slug: linkedin-sales-analytics-export-job-response
- name: SalesAnalyticsExportJob
  property_count: 5
  slug: linkedin-sales-analytics-export-job
- name: BatchProfileAssociationResponse
  property_count: 3
  slug: linkedin-sales-navigator-batch-profile-association-response
- name: Contract
  property_count: 4
  slug: linkedin-sales-navigator-contract
- name: ContractsResponse
  property_count: 2
  slug: linkedin-sales-navigator-contracts-response
- name: CrmDataValidationExportJobRequest
  property_count: 1
  slug: linkedin-sales-navigator-crm-data-validation-export-job-request
- name: CrmDataValidationExportJob
  property_count: 7
  slug: linkedin-sales-navigator-crm-data-validation-export-job
- name: ErrorResponse
  property_count: 3
  slug: linkedin-sales-navigator-error-response
- name: Paging
  property_count: 3
  slug: linkedin-sales-navigator-paging
- name: SalesNavigatorProfileAssociation
  property_count: 3
  slug: linkedin-sales-navigator-profile-association
- name: SalesAccessTokenResponse
  property_count: 2
  slug: linkedin-sales-navigator-sales-access-token-response
- name: SalesAccessToken
  property_count: 2
  slug: linkedin-sales-navigator-sales-access-token
- name: SalesAnalyticsExportJobRequest
  property_count: 3
  slug: linkedin-sales-navigator-sales-analytics-export-job-request
- name: SalesAnalyticsExportJobResponse
  property_count: 1
  slug: linkedin-sales-navigator-sales-analytics-export-job-response
- name: SalesAnalyticsExportJob
  property_count: 5
  slug: linkedin-sales-navigator-sales-analytics-export-job
- name: SalesNavigatorProfileAssociationKey
  property_count: 3
  slug: linkedin-sales-navigator-sales-navigator-profile-association-key
- name: SalesNavigatorProfileAssociation
  property_count: 3
  slug: linkedin-sales-navigator-sales-navigator-profile-association
- name: SalesAccessToken
  property_count: 2
  slug: linkedin-salesaccesstoken
- name: SalesAccessTokenResponse
  property_count: 2
  slug: linkedin-salesaccesstokenresponse
- name: SalesAnalyticsExportJob
  property_count: 5
  slug: linkedin-salesanalyticsexportjob
- name: SalesAnalyticsExportJobRequest
  property_count: 3
  slug: linkedin-salesanalyticsexportjobrequest
- name: SalesAnalyticsExportJobResponse
  property_count: 1
  slug: linkedin-salesanalyticsexportjobresponse
- name: SalesNavigatorProfileAssociation
  property_count: 3
  slug: linkedin-salesnavigatorprofileassociation
- name: SalesNavigatorProfileAssociationKey
  property_count: 3
  slug: linkedin-salesnavigatorprofileassociationkey
- name: Seatholder
  property_count: 5
  slug: linkedin-seatholder
- name: SeatholdersResponse
  property_count: 2
  slug: linkedin-seatholders-response
- name: SeatholdersResponse
  property_count: 2
  slug: linkedin-seatholdersresponse
- name: SegmentDestination
  property_count: 1
  slug: linkedin-segmentdestination
- name: SimpleJobPostingRequest
  property_count: 1
  slug: linkedin-simple-job-posting-request
- name: SimpleJobPostingRequest
  property_count: 1
  slug: linkedin-simplejobpostingrequest
- name: StageData
  property_count: 2
  slug: linkedin-stagedata
- name: StageRequest
  property_count: 1
  slug: linkedin-stagerequest
- name: StreamMultipleConversionEventsRequest
  property_count: 0
  slug: linkedin-stream-multiple-conversion-events-request
- name: StreamResponse
  property_count: 1
  slug: linkedin-stream-response
- name: StreamMultipleConversionEventsRequest
  property_count: 0
  slug: linkedin-streammultipleconversioneventsrequest
- name: StreamMultipleConversionEventsResponse200
  property_count: 1
  slug: linkedin-streammultipleconversioneventsresponse200
- name: StreamResponse
  property_count: 1
  slug: linkedin-streamresponse
- name: StreamResultElement
  property_count: 1
  slug: linkedin-streamresultelement
- name: SubscribeForLeadNotificationRequest
  property_count: 0
  slug: linkedin-subscribe-for-lead-notification-request
- name: SubscribeForLeadNotificationRequest
  property_count: 0
  slug: linkedin-subscribeforleadnotificationrequest
- name: SuccessResponse
  property_count: 1
  slug: linkedin-success-response
- name: SuccessResponse
  property_count: 1
  slug: linkedin-successresponse
- name: AdditionalQuestions
  property_count: 1
  slug: linkedin-talent-job-posting-additional-questions
- name: ApplicationQuestions
  property_count: 6
  slug: linkedin-talent-job-posting-application-questions
- name: CoverLetterQuestions
  property_count: 1
  slug: linkedin-talent-job-posting-cover-letter-questions
- name: CustomQuestion
  property_count: 4
  slug: linkedin-talent-job-posting-custom-question
- name: CustomQuestionSet
  property_count: 2
  slug: linkedin-talent-job-posting-custom-question-set
- name: EducationQuestions
  property_count: 1
  slug: linkedin-talent-job-posting-education-questions
- name: JobPostingElement
  property_count: 10
  slug: linkedin-talent-job-posting-job-posting-element
- name: JobPostingResponse
  property_count: 1
  slug: linkedin-talent-job-posting-job-posting-response
- name: MultipleChoiceQuestionDetails
  property_count: 3
  slug: linkedin-talent-job-posting-multiple-choice-question-details
- name: OnsiteApplyConfiguration
  property_count: 2
  slug: linkedin-talent-job-posting-onsite-apply-configuration
- name: QuestionChoice
  property_count: 2
  slug: linkedin-talent-job-posting-question-choice
- name: QuestionDetails
  property_count: 1
  slug: linkedin-talent-job-posting-question-details
- name: ResumeQuestions
  property_count: 1
  slug: linkedin-talent-job-posting-resume-questions
- name: SimpleJobPostingRequest
  property_count: 1
  slug: linkedin-talent-job-posting-simple-job-posting-request
- name: WorkQuestions
  property_count: 1
  slug: linkedin-talent-job-posting-work-questions
- name: ApplicationCredentials
  property_count: 4
  slug: linkedin-talent-learning-parent-application-application-credentials
- name: ErrorResponse
  property_count: 3
  slug: linkedin-talent-learning-parent-application-error-response
- name: GetApplicationResponse
  property_count: 1
  slug: linkedin-talent-learning-parent-application-get-application-response
- name: ProvisionApplicationRequest
  property_count: 5
  slug: linkedin-talent-learning-parent-application-provision-application-request
- name: ProvisionApplicationResponse
  property_count: 8
  slug: linkedin-talent-learning-parent-application-provision-application-response
- name: UpdateCallbackUrlRequest
  property_count: 1
  slug: linkedin-talent-learning-parent-application-update-callback-url-request
- name: AccessTokenRequest
  property_count: 3
  slug: linkedin-talent-recruiter-system-connect-access-token-request
- name: AccessTokenResponse
  property_count: 3
  slug: linkedin-talent-recruiter-system-connect-access-token-response
- name: Address
  property_count: 6
  slug: linkedin-talent-recruiter-system-connect-address
- name: ApplicationData
  property_count: 10
  slug: linkedin-talent-recruiter-system-connect-application-data
- name: ApplicationRequest
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-application-request
- name: AtsIntegrationUpdateRequest
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-ats-integration-update-request
- name: CandidateData
  property_count: 13
  slug: linkedin-talent-recruiter-system-connect-candidate-data
- name: CandidateRequest
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-candidate-request
- name: ConfigurationValue
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-configuration-value
- name: IntegrationConfigurationRequest
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-integration-configuration-request
- name: IntegrationPatch
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-integration-patch
- name: NoteData
  property_count: 3
  slug: linkedin-talent-recruiter-system-connect-note-data
- name: NoteRequest
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-note-request
- name: PersonName
  property_count: 2
  slug: linkedin-talent-recruiter-system-connect-person-name
- name: PhoneNumber
  property_count: 2
  slug: linkedin-talent-recruiter-system-connect-phone-number
- name: TargetingCriteria
  property_count: 1
  slug: linkedin-targetingcriteria
- name: Timestamp
  property_count: 1
  slug: linkedin-timestamp
- name: UpdateADynamicSpotlightRequest
  property_count: 0
  slug: linkedin-update-adynamic-spotlight-request
- name: UpdateAPostRequest
  property_count: 0
  slug: linkedin-update-apost-request
- name: UpdateASponsoredConversationRequest
  property_count: 0
  slug: linkedin-update-asponsored-conversation-request
- name: UpdateCallbackUrlRequest
  property_count: 1
  slug: linkedin-update-callback-url-request
- name: UpdateInmailContentRequest
  property_count: 0
  slug: linkedin-update-inmail-content-request
- name: UpdateSponsoredMessageContentRequest
  property_count: 0
  slug: linkedin-update-sponsored-message-content-request
- name: UpdateADynamicSpotlightRequest
  property_count: 0
  slug: linkedin-updateadynamicspotlightrequest
- name: UpdateAPostRequest
  property_count: 0
  slug: linkedin-updateapostrequest
- name: UpdateASponsoredConversationRequest
  property_count: 0
  slug: linkedin-updateasponsoredconversationrequest
- name: UpdateCallbackUrlRequest
  property_count: 1
  slug: linkedin-updatecallbackurlrequest
- name: UpdateInmailContentRequest
  property_count: 0
  slug: linkedin-updateinmailcontentrequest
- name: UpdateSponsoredMessageContentRequest
  property_count: 0
  slug: linkedin-updatesponsoredmessagecontentrequest
- name: UserStreamRequest
  property_count: 1
  slug: linkedin-user-stream-request
- name: UserId
  property_count: 2
  slug: linkedin-userid
- name: UserStreamElement
  property_count: 2
  slug: linkedin-userstreamelement
- name: UserStreamRequest
  property_count: 1
  slug: linkedin-userstreamrequest
- name: ValidateTheUsersOrganizationResponse200
  property_count: 2
  slug: linkedin-validate-the-users-organization-response200
- name: ValidateTheUsersOrganizationResponse200
  property_count: 2
  slug: linkedin-validatetheusersorganizationresponse200
- name: WorkQuestions
  property_count: 1
  slug: linkedin-workquestions
json_structures:
- name: Linkedin Compliance Events Compliance Authorization Request Structure
  property_count: 1
  slug: linkedin-compliance-events-compliance-authorization-request-structure
- name: Linkedin Compliance Events Compliance Authorization Response Structure
  property_count: 2
  slug: linkedin-compliance-events-compliance-authorization-response-structure
- name: Linkedin Compliance Events Compliance Authorization Structure
  property_count: 4
  slug: linkedin-compliance-events-compliance-authorization-structure
- name: Linkedin Compliance Events Compliance Event Structure
  property_count: 15
  slug: linkedin-compliance-events-compliance-event-structure
- name: Linkedin Compliance Events Compliance Events Response Structure
  property_count: 2
  slug: linkedin-compliance-events-compliance-events-response-structure
- name: Linkedin Compliance Events Error Response Structure
  property_count: 3
  slug: linkedin-compliance-events-error-response-structure
- name: Linkedin Compliance Events Member Profile Structure
  property_count: 3
  slug: linkedin-compliance-events-member-profile-structure
- name: Linkedin Compliance Events Paging Link Structure
  property_count: 3
  slug: linkedin-compliance-events-paging-link-structure
- name: Linkedin Compliance Events Paging Structure
  property_count: 4
  slug: linkedin-compliance-events-paging-structure
- name: Linkedin Learning Activity Reports Error Response Structure
  property_count: 3
  slug: linkedin-learning-activity-reports-error-response-structure
- name: Linkedin Learning Activity Reports Learner Details Structure
  property_count: 1
  slug: linkedin-learning-activity-reports-learner-details-structure
- name: Linkedin Learning Activity Reports Learner Entity Structure
  property_count: 4
  slug: linkedin-learning-activity-reports-learner-entity-structure
- name: Linkedin Learning Activity Reports Learning Activity Report Response Structure
  property_count: 2
  slug: linkedin-learning-activity-reports-learning-activity-report-response-structure
- name: Linkedin Learning Activity Reports Learning Activity Report Structure
  property_count: 3
  slug: linkedin-learning-activity-reports-learning-activity-report-structure
- name: Linkedin Learning Activity Reports Learning Activity Structure
  property_count: 6
  slug: linkedin-learning-activity-reports-learning-activity-structure
- name: Linkedin Learning Activity Reports Paging Link Structure
  property_count: 3
  slug: linkedin-learning-activity-reports-paging-link-structure
- name: Linkedin Learning Activity Reports Paging Structure
  property_count: 4
  slug: linkedin-learning-activity-reports-paging-structure
- name: Linkedin Marketing Audience Ad Account Structure
  property_count: 4
  slug: linkedin-marketing-audience-ad-account-structure
- name: Linkedin Marketing Audience Ad Accounts Response Structure
  property_count: 2
  slug: linkedin-marketing-audience-ad-accounts-response-structure
- name: Linkedin Marketing Audience Company Stream Element Structure
  property_count: 4
  slug: linkedin-marketing-audience-company-stream-element-structure
- name: Linkedin Marketing Audience Company Stream Request Structure
  property_count: 1
  slug: linkedin-marketing-audience-company-stream-request-structure
- name: Linkedin Marketing Audience Dmp Segment Create Request Structure
  property_count: 6
  slug: linkedin-marketing-audience-dmp-segment-create-request-structure
- name: Linkedin Marketing Audience Dmp Segment Structure
  property_count: 11
  slug: linkedin-marketing-audience-dmp-segment-structure
- name: Linkedin Marketing Audience Dmp Segments Response Structure
  property_count: 2
  slug: linkedin-marketing-audience-dmp-segments-response-structure
- name: Linkedin Marketing Audience Insights Ad Targeting Entities Response Structure
  property_count: 2
  slug: linkedin-marketing-audience-insights-ad-targeting-entities-response-structure
- name: Linkedin Marketing Audience Insights Ad Targeting Entity Structure
  property_count: 3
  slug: linkedin-marketing-audience-insights-ad-targeting-entity-structure
- name: Linkedin Marketing Audience Insights Ad Targeting Facet Structure
  property_count: 4
  slug: linkedin-marketing-audience-insights-ad-targeting-facet-structure
- name: Linkedin Marketing Audience Insights Ad Targeting Facets Response Structure
  property_count: 2
  slug: linkedin-marketing-audience-insights-ad-targeting-facets-response-structure
- name: Linkedin Marketing Audience Insights Audience Insight Structure
  property_count: 2
  slug: linkedin-marketing-audience-insights-audience-insight-structure
- name: Linkedin Marketing Audience Insights Audience Insights Request Structure
  property_count: 1
  slug: linkedin-marketing-audience-insights-audience-insights-request-structure
- name: Linkedin Marketing Audience Insights Audience Insights Response Structure
  property_count: 1
  slug: linkedin-marketing-audience-insights-audience-insights-response-structure
- name: Linkedin Marketing Audience Insights Error Response Structure
  property_count: 3
  slug: linkedin-marketing-audience-insights-error-response-structure
- name: Linkedin Marketing Audience Insights Insight Segmentation Structure
  property_count: 3
  slug: linkedin-marketing-audience-insights-insight-segmentation-structure
- name: Linkedin Marketing Audience Insights Paging Link Structure
  property_count: 3
  slug: linkedin-marketing-audience-insights-paging-link-structure
- name: Linkedin Marketing Audience Insights Paging Structure
  property_count: 4
  slug: linkedin-marketing-audience-insights-paging-structure
- name: Linkedin Marketing Audience Insights Request Meta Data Structure
  property_count: 1
  slug: linkedin-marketing-audience-insights-request-meta-data-structure
- name: Linkedin Marketing Audience Insights Targeting Criteria Structure
  property_count: 1
  slug: linkedin-marketing-audience-insights-targeting-criteria-structure
- name: Linkedin Marketing Audience List Upload Request Structure
  property_count: 1
  slug: linkedin-marketing-audience-list-upload-request-structure
- name: Linkedin Marketing Audience Paging Structure
  property_count: 4
  slug: linkedin-marketing-audience-paging-structure
- name: Linkedin Marketing Audience Segment Destination Structure
  property_count: 1
  slug: linkedin-marketing-audience-segment-destination-structure
- name: Linkedin Marketing Audience Stream Response Structure
  property_count: 1
  slug: linkedin-marketing-audience-stream-response-structure
- name: Linkedin Marketing Audience Stream Result Element Structure
  property_count: 1
  slug: linkedin-marketing-audience-stream-result-element-structure
- name: Linkedin Marketing Audience User Id Structure
  property_count: 2
  slug: linkedin-marketing-audience-user-id-structure
- name: Linkedin Marketing Audience User Stream Element Structure
  property_count: 2
  slug: linkedin-marketing-audience-user-stream-element-structure
- name: Linkedin Marketing Audience User Stream Request Structure
  property_count: 1
  slug: linkedin-marketing-audience-user-stream-request-structure
- name: Linkedin Marketing Campaigns Ad Account Create Request Structure
  property_count: 9
  slug: linkedin-marketing-campaigns-ad-account-create-request-structure
- name: Linkedin Marketing Campaigns Ad Account Structure
  property_count: 11
  slug: linkedin-marketing-campaigns-ad-account-structure
- name: Linkedin Marketing Campaigns Ad Account User Create Request Structure
  property_count: 3
  slug: linkedin-marketing-campaigns-ad-account-user-create-request-structure
- name: Linkedin Marketing Campaigns Ad Account User Structure
  property_count: 3
  slug: linkedin-marketing-campaigns-ad-account-user-structure
- name: Linkedin Marketing Campaigns Ad Account User Update Request Structure
  property_count: 1
  slug: linkedin-marketing-campaigns-ad-account-user-update-request-structure
- name: Linkedin Marketing Campaigns Audience Count Structure
  property_count: 2
  slug: linkedin-marketing-campaigns-audience-count-structure
- name: Linkedin Marketing Campaigns Budget Structure
  property_count: 2
  slug: linkedin-marketing-campaigns-budget-structure
- name: Linkedin Marketing Campaigns Campaign Group Structure
  property_count: 6
  slug: linkedin-marketing-campaigns-campaign-group-structure
- name: Linkedin Marketing Campaigns Campaign Structure
  property_count: 10
  slug: linkedin-marketing-campaigns-campaign-structure
- name: Linkedin Marketing Campaigns Campaign Update Request Structure
  property_count: 1
  slug: linkedin-marketing-campaigns-campaign-update-request-structure
- name: Linkedin Marketing Campaigns Creative Create Request Structure
  property_count: 5
  slug: linkedin-marketing-campaigns-creative-create-request-structure
- name: Linkedin Marketing Campaigns Creative Structure
  property_count: 5
  slug: linkedin-marketing-campaigns-creative-structure
- name: Linkedin Marketing Campaigns Organization Acl Structure
  property_count: 3
  slug: linkedin-marketing-campaigns-organization-acl-structure
- name: Linkedin Marketing Campaigns Paging Structure
  property_count: 4
  slug: linkedin-marketing-campaigns-paging-structure
- name: Linkedin Marketing Campaigns Run Schedule Structure
  property_count: 2
  slug: linkedin-marketing-campaigns-run-schedule-structure
- name: Linkedin Marketing Community Batch Get On Administered Response200 Structure
  property_count: 3
  slug: linkedin-marketing-community-batch-get-on-administered-response200-structure
- name: Linkedin Marketing Community Batch Get On Nonadministered Response200 Structure
  property_count: 3
  slug: linkedin-marketing-community-batch-get-on-nonadministered-response200-structure
- name: Linkedin Marketing Community Find Administered Organization Brands Response200 Structure
  property_count: 2
  slug: linkedin-marketing-community-find-administered-organization-brands-response200-structure
- name: Linkedin Marketing Community Find Nonadministered Organization Response200 Structure
  property_count: 3
  slug: linkedin-marketing-community-find-nonadministered-organization-response200-structure
- name: Linkedin Marketing Community Lookup By Organization Primary Response200 Structure
  property_count: 1
  slug: linkedin-marketing-community-lookup-by-organization-primary-response200-structure
- name: Linkedin Marketing Community Retrieve An Administered Organization Response200 Structure
  property_count: 16
  slug: linkedin-marketing-community-retrieve-an-administered-organization-response200-structure
- name: Linkedin Marketing Community Retrieve Organization Follower Count Response200 Structure
  property_count: 1
  slug: linkedin-marketing-community-retrieve-organization-follower-count-response200-structure
- name: Linkedin Marketing Conversions Create A New Conversion Response201 Structure
  property_count: 14
  slug: linkedin-marketing-conversions-create-a-new-conversion-response201-structure
- name: Linkedin Marketing Conversions Fetch Active Campaigns Response200 Structure
  property_count: 2
  slug: linkedin-marketing-conversions-fetch-active-campaigns-response200-structure
- name: Linkedin Marketing Conversions Fetch Existing Conversion Rules Response200 Structure
  property_count: 2
  slug: linkedin-marketing-conversions-fetch-existing-conversion-rules-response200-structure
- name: Linkedin Marketing Conversions Retrieve Authenticated Users Sponsored Response200 Structure
  property_count: 2
  slug: linkedin-marketing-conversions-retrieve-authenticated-users-sponsored-response200-structure
- name: Linkedin Marketing Conversions Stream Multiple Conversion Events Response200 Structure
  property_count: 1
  slug: linkedin-marketing-conversions-stream-multiple-conversion-events-response200-structure
- name: Linkedin Marketing Leads Fetch Full Lead Data Response200 Structure
  property_count: 10
  slug: linkedin-marketing-leads-fetch-full-lead-data-response200-structure
- name: Linkedin Marketing Leads Get Forms For The Response200 Structure
  property_count: 2
  slug: linkedin-marketing-leads-get-forms-for-the-response200-structure
- name: Linkedin Marketing Leads Get The Users Sponsored Response200 Structure
  property_count: 2
  slug: linkedin-marketing-leads-get-the-users-sponsored-response200-structure
- name: Linkedin Marketing Leads Validate The Users Organization Response200 Structure
  property_count: 2
  slug: linkedin-marketing-leads-validate-the-users-organization-response200-structure
- name: Linkedin Marketing Media Planning Get A List Of Response200 Structure
  property_count: 2
  slug: linkedin-marketing-media-planning-get-a-list-of-response200-structure
- name: Linkedin Marketing Media Planning Get Bing Geo Locations Response200 Structure
  property_count: 2
  slug: linkedin-marketing-media-planning-get-bing-geo-locations-response200-structure
- name: Linkedin Marketing Reporting Roi Conversions By Member Company Response200 Structure
  property_count: 2
  slug: linkedin-marketing-reporting-roi-conversions-by-member-company-response200-structure
- name: Linkedin Regulations Data Portability Address Structure
  property_count: 5
  slug: linkedin-regulations-data-portability-address-structure
- name: Linkedin Regulations Data Portability Batch Organization Response Structure
  property_count: 3
  slug: linkedin-regulations-data-portability-batch-organization-response-structure
- name: Linkedin Regulations Data Portability Date Info Structure
  property_count: 3
  slug: linkedin-regulations-data-portability-date-info-structure
- name: Linkedin Regulations Data Portability Image Asset Structure
  property_count: 3
  slug: linkedin-regulations-data-portability-image-asset-structure
- name: Linkedin Regulations Data Portability Image Reference Structure
  property_count: 3
  slug: linkedin-regulations-data-portability-image-reference-structure
- name: Linkedin Regulations Data Portability Locale Structure
  property_count: 2
  slug: linkedin-regulations-data-portability-locale-structure
- name: Linkedin Regulations Data Portability Localized String Structure
  property_count: 2
  slug: linkedin-regulations-data-portability-localized-string-structure
- name: Linkedin Regulations Data Portability Organization Acl Response Structure
  property_count: 2
  slug: linkedin-regulations-data-portability-organization-acl-response-structure
- name: Linkedin Regulations Data Portability Organization Acl Structure
  property_count: 5
  slug: linkedin-regulations-data-portability-organization-acl-structure
- name: Linkedin Regulations Data Portability Organization Location Structure
  property_count: 5
  slug: linkedin-regulations-data-portability-organization-location-structure
- name: Linkedin Regulations Data Portability Organization Response Structure
  property_count: 18
  slug: linkedin-regulations-data-portability-organization-response-structure
- name: Linkedin Regulations Data Portability Post Response Structure
  property_count: 2
  slug: linkedin-regulations-data-portability-post-response-structure
- name: Linkedin Regulations Data Portability Post Structure
  property_count: 7
  slug: linkedin-regulations-data-portability-post-structure
- name: Linkedin Regulations Data Portability Reaction Response Structure
  property_count: 2
  slug: linkedin-regulations-data-portability-reaction-response-structure
- name: Linkedin Regulations Data Portability Timestamp Structure
  property_count: 1
  slug: linkedin-regulations-data-portability-timestamp-structure
- name: Linkedin Regulatory Ads Transparency Advertiser Transparency Request Structure
  property_count: 2
  slug: linkedin-regulatory-ads-transparency-advertiser-transparency-request-structure
- name: Linkedin Regulatory Ads Transparency Advertiser Transparency Response Structure
  property_count: 7
  slug: linkedin-regulatory-ads-transparency-advertiser-transparency-response-structure
- name: Linkedin Regulatory Ads Transparency Error Response Structure
  property_count: 3
  slug: linkedin-regulatory-ads-transparency-error-response-structure
- name: Linkedin Sales Navigator Batch Profile Association Response Structure
  property_count: 3
  slug: linkedin-sales-navigator-batch-profile-association-response-structure
- name: Linkedin Sales Navigator Contract Structure
  property_count: 4
  slug: linkedin-sales-navigator-contract-structure
- name: Linkedin Sales Navigator Contracts Response Structure
  property_count: 2
  slug: linkedin-sales-navigator-contracts-response-structure
- name: Linkedin Sales Navigator Crm Data Validation Export Job Request Structure
  property_count: 1
  slug: linkedin-sales-navigator-crm-data-validation-export-job-request-structure
- name: Linkedin Sales Navigator Crm Data Validation Export Job Structure
  property_count: 7
  slug: linkedin-sales-navigator-crm-data-validation-export-job-structure
- name: Linkedin Sales Navigator Error Response Structure
  property_count: 3
  slug: linkedin-sales-navigator-error-response-structure
- name: Linkedin Sales Navigator Paging Structure
  property_count: 3
  slug: linkedin-sales-navigator-paging-structure
- name: Linkedin Sales Navigator Sales Access Token Response Structure
  property_count: 2
  slug: linkedin-sales-navigator-sales-access-token-response-structure
- name: Linkedin Sales Navigator Sales Access Token Structure
  property_count: 2
  slug: linkedin-sales-navigator-sales-access-token-structure
- name: Linkedin Sales Navigator Sales Analytics Export Job Request Structure
  property_count: 3
  slug: linkedin-sales-navigator-sales-analytics-export-job-request-structure
- name: Linkedin Sales Navigator Sales Analytics Export Job Response Structure
  property_count: 1
  slug: linkedin-sales-navigator-sales-analytics-export-job-response-structure
- name: Linkedin Sales Navigator Sales Analytics Export Job Structure
  property_count: 5
  slug: linkedin-sales-navigator-sales-analytics-export-job-structure
- name: Linkedin Sales Navigator Sales Navigator Profile Association Key Structure
  property_count: 3
  slug: linkedin-sales-navigator-sales-navigator-profile-association-key-structure
- name: Linkedin Sales Navigator Sales Navigator Profile Association Structure
  property_count: 3
  slug: linkedin-sales-navigator-sales-navigator-profile-association-structure
- name: Linkedin Structure
  property_count: 0
  slug: linkedin-structure
- name: Linkedin Talent Job Posting Additional Questions Structure
  property_count: 1
  slug: linkedin-talent-job-posting-additional-questions-structure
- name: Linkedin Talent Job Posting Application Questions Structure
  property_count: 6
  slug: linkedin-talent-job-posting-application-questions-structure
- name: Linkedin Talent Job Posting Cover Letter Questions Structure
  property_count: 1
  slug: linkedin-talent-job-posting-cover-letter-questions-structure
- name: Linkedin Talent Job Posting Custom Question Set Structure
  property_count: 2
  slug: linkedin-talent-job-posting-custom-question-set-structure
- name: Linkedin Talent Job Posting Custom Question Structure
  property_count: 4
  slug: linkedin-talent-job-posting-custom-question-structure
- name: Linkedin Talent Job Posting Education Questions Structure
  property_count: 1
  slug: linkedin-talent-job-posting-education-questions-structure
- name: Linkedin Talent Job Posting Job Posting Element Structure
  property_count: 10
  slug: linkedin-talent-job-posting-job-posting-element-structure
- name: Linkedin Talent Job Posting Job Posting Response Structure
  property_count: 1
  slug: linkedin-talent-job-posting-job-posting-response-structure
- name: Linkedin Talent Job Posting Multiple Choice Question Details Structure
  property_count: 3
  slug: linkedin-talent-job-posting-multiple-choice-question-details-structure
- name: Linkedin Talent Job Posting Onsite Apply Configuration Structure
  property_count: 2
  slug: linkedin-talent-job-posting-onsite-apply-configuration-structure
- name: Linkedin Talent Job Posting Question Choice Structure
  property_count: 2
  slug: linkedin-talent-job-posting-question-choice-structure
- name: Linkedin Talent Job Posting Question Details Structure
  property_count: 1
  slug: linkedin-talent-job-posting-question-details-structure
- name: Linkedin Talent Job Posting Resume Questions Structure
  property_count: 1
  slug: linkedin-talent-job-posting-resume-questions-structure
- name: Linkedin Talent Job Posting Simple Job Posting Request Structure
  property_count: 1
  slug: linkedin-talent-job-posting-simple-job-posting-request-structure
- name: Linkedin Talent Job Posting Work Questions Structure
  property_count: 1
  slug: linkedin-talent-job-posting-work-questions-structure
- name: Linkedin Talent Learning Parent Application Application Credentials Structure
  property_count: 4
  slug: linkedin-talent-learning-parent-application-application-credentials-structure
- name: Linkedin Talent Learning Parent Application Error Response Structure
  property_count: 3
  slug: linkedin-talent-learning-parent-application-error-response-structure
- name: Linkedin Talent Learning Parent Application Get Application Response Structure
  property_count: 1
  slug: linkedin-talent-learning-parent-application-get-application-response-structure
- name: Linkedin Talent Learning Parent Application Provision Application Request Structure
  property_count: 5
  slug: linkedin-talent-learning-parent-application-provision-application-request-structure
- name: Linkedin Talent Learning Parent Application Provision Application Response Structure
  property_count: 8
  slug: linkedin-talent-learning-parent-application-provision-application-response-structure
- name: Linkedin Talent Learning Parent Application Update Callback Url Request Structure
  property_count: 1
  slug: linkedin-talent-learning-parent-application-update-callback-url-request-structure
- name: Linkedin Talent Recruiter System Connect Access Token Request Structure
  property_count: 3
  slug: linkedin-talent-recruiter-system-connect-access-token-request-structure
- name: Linkedin Talent Recruiter System Connect Access Token Response Structure
  property_count: 3
  slug: linkedin-talent-recruiter-system-connect-access-token-response-structure
- name: Linkedin Talent Recruiter System Connect Address Structure
  property_count: 6
  slug: linkedin-talent-recruiter-system-connect-address-structure
- name: Linkedin Talent Recruiter System Connect Application Data Structure
  property_count: 10
  slug: linkedin-talent-recruiter-system-connect-application-data-structure
- name: Linkedin Talent Recruiter System Connect Application Request Structure
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-application-request-structure
- name: Linkedin Talent Recruiter System Connect Ats Integration Update Request Structure
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-ats-integration-update-request-structure
- name: Linkedin Talent Recruiter System Connect Candidate Data Structure
  property_count: 13
  slug: linkedin-talent-recruiter-system-connect-candidate-data-structure
- name: Linkedin Talent Recruiter System Connect Candidate Request Structure
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-candidate-request-structure
- name: Linkedin Talent Recruiter System Connect Configuration Value Structure
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-configuration-value-structure
- name: Linkedin Talent Recruiter System Connect Integration Configuration Request Structure
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-integration-configuration-request-structure
- name: Linkedin Talent Recruiter System Connect Integration Patch Structure
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-integration-patch-structure
- name: Linkedin Talent Recruiter System Connect Note Data Structure
  property_count: 3
  slug: linkedin-talent-recruiter-system-connect-note-data-structure
- name: Linkedin Talent Recruiter System Connect Note Request Structure
  property_count: 1
  slug: linkedin-talent-recruiter-system-connect-note-request-structure
- name: Linkedin Talent Recruiter System Connect Person Name Structure
  property_count: 2
  slug: linkedin-talent-recruiter-system-connect-person-name-structure
- name: Linkedin Talent Recruiter System Connect Phone Number Structure
  property_count: 2
  slug: linkedin-talent-recruiter-system-connect-phone-number-structure
jsonld:
- class_count: 132
  name: Linkedin Api Context
  property_count: 265
  slug: linkedin-api-context
- class_count: 120
  name: Linkedin Context
  property_count: 254
  slug: linkedin-context
layout: provider
modified: '2026-08-13'
name: LinkedIn
nav: Providers
network: true
overview: 'LinkedIn publishes 71 API contracts indexed on the [APIs.io](https://apis.io/) network, including Consumer API, Access Control API, Account Management API, and 68 more. Tagged areas include LinkedIn, Business, Careers, Marketing, and Professional Networking.


  The LinkedIn catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 3 Spectral governance rulesets.


  LinkedIn''s developer surface includes signup flow, getting-started guide, sandbox, code examples, changelog, authentication, documentation, and 121 more developer resources.'
plans:
- name: Linkedin Plans Pricing
  plan_count: 8
  slug: linkedin-plans-pricing
press:
- date: ''
  title: LinkedIn Pressroom | LinkedIn
  url: https://news.linkedin.com/
- date: ''
  title: Why using AI to write your press release could be hurting ...
  url: https://www.linkedin.com/pulse/why-using-ai-write-your-press-release-could-hurting-brand-dybac-brpac
- date: ''
  title: (PDF) The Rise of AI-Generated Content on LinkedIn
  url: https://www.researchgate.net/publication/391873822_The_Rise_of_AI-Generated_Content_on_LinkedIn_Implications_for_Engagement_Trust_and_Thought_Leadership
- date: ''
  title: Artificial Intelligence News
  url: https://www.linkedin.com/showcase/artificial-intelligence-news/
- date: ''
  title: AI's Impact on Local News Production
  url: https://www.linkedin.com/top-content/artificial-intelligence/ai-in-journalism/ai-s-impact-on-local-news-production/
random_paper: 6
rate_limits:
- limit_count: 3
  name: Linkedin Rate Limits
  slug: linkedin-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: LinkedIn — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: linkedin-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: LinkedIn API Rules
  rule_count: 66
  severity_counts:
    error: 42
    hint: 0
    info: 4
    warn: 20
  slug: linkedin-rules
- authorship: generated
  effective_rule_count: 68
  extends:
  - spectral:oas
  name: LinkedIn API Rules
  rule_count: 27
  severity_counts:
    error: 14
    hint: 0
    info: 3
    warn: 10
  slug: linkedin-spectral-rules
scopes:
- name: Linkedin Scopes
  scope_count: 7
  slug: linkedin-scopes
  summary_line: 7 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 76.4
  coverage:
    artifact_dirs: 44
    catalog_earned: 75.0
    catalog_earned_first_party: 0.0
    catalog_gap: 40.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 57.9
    contract_governance: 45.5
    contract_quality: 76.3
    developer_ergonomics: 85.1
    discoverability: 80.4
    operational_transparency: 71.1
  previous_composite: 74.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 68
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
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/linkedin/linkedin-2026-06-20T184544.png
security:
- kind: authentication
  name: Linkedin Authentication
  slug: linkedin-authentication
  summary_line: http/oauth2 · 4 schemes
- kind: domain-security
  name: Linkedin Domain Security
  slug: linkedin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Linkedin Vulnerability Disclosure
  slug: linkedin-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Linkedin Trust Center
  slug: linkedin-trust-center
  summary_line: GDPR
skill_count: 7
skills:
- name: linkedin-authenticate
  slug: linkedin-authenticate
- name: linkedin-lead-sync
  slug: linkedin-lead-sync
- name: linkedin-manage-ad-campaigns
  slug: linkedin-manage-ad-campaigns
- name: linkedin-organization-analytics
  slug: linkedin-organization-analytics
- name: linkedin-publish-organization-post
  slug: linkedin-publish-organization-post
- name: linkedin-subscribe-social-action-webhooks
  slug: linkedin-subscribe-social-action-webhooks
- name: linkedin-upload-media-and-post
  slug: linkedin-upload-media-and-post
slug: linkedin
solutions:
- description: Sign In with LinkedIn, Share on LinkedIn, and Verified on LinkedIn for consumer-facing integrations.
  name: Consumer Solutions
- description: B2B advertising platform with campaign management, audience targeting, lead generation, and analytics.
  name: Marketing Solutions
- description: Job posting, recruiter system connect, and apply with LinkedIn for talent acquisition and ATS integration.
  name: Talent Solutions
- description: LinkedIn Learning integration for employee development tracking, content access, and activity reporting.
  name: Learning Solutions
- description: LinkedIn Sales Navigator API for CRM sync, display services, and sales analytics.
  name: Sales Solutions
- description: Message archiving and activity monitoring for regulated industries requiring communications governance.
  name: Compliance Solutions
- description: Data portability and advertiser transparency APIs for Digital Markets Act and regulatory compliance.
  name: Regulatory Solutions
tags:
- LinkedIn
- Business
- Careers
- Marketing
- Professional Networking
- Recruiting
- Social Media
- Fortune 1000
- Social
use_cases:
- description: Implement Sign In with LinkedIn for professional identity verification and streamlined authentication.
  name: Social Login
- description: Create and manage targeted advertising campaigns reaching professional audiences by industry, job title, and company.
  name: B2B Advertising
- description: Retrieve campaign performance metrics, audience insights, and conversion attribution for marketing optimization.
  name: Marketing Analytics
- description: Post jobs, manage candidates, and integrate ATS systems with LinkedIn Recruiter for streamlined hiring.
  name: Talent Acquisition
- description: Integrate CRM systems with LinkedIn Sales Navigator for lead enrichment and relationship insights.
  name: Sales Intelligence
- description: Track and report on LinkedIn Learning usage, completions, and skill development across organizations.
  name: Employee Learning
- description: Archive communications and activities on LinkedIn for compliance with financial industry regulations.
  name: Regulatory Compliance
- description: Automate sharing of articles, updates, and media content to LinkedIn feeds and company pages.
  name: Content Distribution
website: https://www.microsoft.com/
---
