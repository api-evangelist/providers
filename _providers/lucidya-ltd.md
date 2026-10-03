---
access_model:
  confidence: high
  label: Docs public, key requires CSM approval
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
  scored_at: '2026-10-03'
api_count: 10
apis:
- description: Receive real-time push notifications when specific events or conditions are met across your monitors.
  name: Lucidya Webhooks
  slug: lucidya-webhooks
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: The aggregated pages > Analytics API from Lucidya Ltd — 1 operation(s) for aggregated pages > analytics.
  name: Lucidya Ltd aggregated pages > Analytics API
  phrasing_intents:
  - id: createAnalyticsWidgetData
    intent: Request analytics page widget data for a date range
    question: How do I start a job that builds analytics page widgets across my monitors?
  - id: getAnalyticsInteractionsWidgetData
    intent: Fetch finished analytics or interactions widget results
    question: Where do I pick up the analytics page widget results once my job is done?
  phrasing_ops: 2
  slug: lucidya-ltd-aggregated-pages-analytics-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: The aggregated pages > Interactions API from Lucidya Ltd — 1 operation(s) for aggregated pages > interactions.
  name: Lucidya Ltd aggregated pages > Interactions API
  phrasing_intents:
  - id: createInteractionsWidgetData
    intent: Request interactions page widget data for a date range
    question: How do I kick off a job that builds the INTERACTIONS page widgets?
  phrasing_ops: 1
  slug: lucidya-ltd-aggregated-pages-interactions-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: Endpoints for creating and retrieving analytics jobs
  name: Lucidya Ltd Analytics Jobs API
  phrasing_intents:
  - id: createAnalyticsJob
    intent: Create an analytics job for an analytics page
    question: How do I generate analytics for the inbox or SLAs page and get back a job_id?
  - id: getAnalyticsByPageNameIndex
    intent: Get the results of an analytics page job
    question: Where do I retrieve the widget data from an analytics job I already started?
  phrasing_ops: 2
  slug: lucidya-ltd-analytics-jobs-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: Endpoints for discovering and managing analytics pages, widgets, and filters
  name: Lucidya Ltd Analytics Pages API
  phrasing_intents:
  - id: getAnalyticsPages
    intent: List analytics pages available to my company
    question: Which analytics pages does my company have access to?
  - id: getPageWidgets
    intent: List widgets available on an analytics page
    question: What widgets can I request on the agents analytics page?
  - id: getPageFilters
    intent: Get filter definitions for an analytics page
    question: Which filters can I apply on the SLAs analytics page?
  phrasing_ops: 3
  slug: lucidya-ltd-analytics-pages-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: The Audio Transcription API from Lucidya Ltd — 3 operation(s) for audio transcription.
  name: Lucidya Ltd Audio Transcription API
  phrasing_intents:
  - id: post_audio_transcription_transcribe_offline
    intent: Submit an audio file for transcription and analysis
    question: How do I upload a call recording to get it transcribed and analyzed?
  - id: checkAudioAnalysisStatus
    intent: Check the status of an audio transcription job
    question: Is my audio transcription job finished yet?
  - id: getAudioAnalysisResult
    intent: Get the transcript and analysis of an audio job
    question: Where can I get the transcript with speaker diarization for a completed recording?
  phrasing_ops: 3
  slug: lucidya-ltd-audio-transcription-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: Operations related to Genesys channel.
  name: Lucidya Ltd Calls > Genesys API
  phrasing_intents:
  - id: createGenesysWidgetData
    intent: Request Genesys call widget data for a period
    question: How do I start a job to analyze my Genesys call channel widgets?
  - id: getGenesysWidgetData
    intent: Get Genesys call widget results for a job
    question: Where do I read the Genesys call analytics once the widget job is ready?
  phrasing_ops: 2
  slug: lucidya-ltd-calls-genesys-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: The Chats > chats API from Lucidya Ltd — 1 operation(s) for chats > chats.
  name: Lucidya Ltd Chats > chats API
  phrasing_intents:
  - id: createChatsWidgetData
    intent: Request widget data across all chat channels
    question: How do I request one analytics job covering every connected chat channel?
  - id: getChatsWidgetData
    intent: Get the all-chats overview widget results
    question: Where do I get an overview across all my connected chat channels?
  phrasing_ops: 2
  slug: lucidya-ltd-chats-chats-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: Operations related to Intercom channel.
  name: Lucidya Ltd Chats > Intercom API
  phrasing_intents:
  - id: createIntercomWidgetData
    intent: Request Intercom chat widget data for a period
    question: How do I start an analytics job for my Intercom chat channel?
  - id: getIntercomWidgetData
    intent: Get Intercom chat widget results for a job
    question: Where do I read Intercom conversation analytics after the job finishes?
  phrasing_ops: 2
  slug: lucidya-ltd-chats-intercom-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: The Chats > Whatsapp API from Lucidya Ltd — 1 operation(s) for chats > whatsapp.
  name: Lucidya Ltd Chats > Whatsapp API
  phrasing_intents:
  - id: createWhatsappWidgetData
    intent: Request WhatsApp chat widget data for a period
    question: How do I start an analytics job for my WhatsApp channel?
  - id: getWhatsappWidgetData
    intent: Get WhatsApp chat widget results for a job
    question: Where do I read WhatsApp conversation analytics once the job completes?
  phrasing_ops: 2
  slug: lucidya-ltd-chats-whatsapp-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: Endpoints for CSAT (Customer Satisfaction) survey analytics
  name: Lucidya Ltd CSAT Analytics API
  phrasing_intents:
  - id: getCsatQuestions
    intent: List CSAT survey questions for a data source
    question: Which CSAT questions are set up for my facebook data source?
  - id: getAnalyticsInChatSurveyFilters
    intent: List filters available on the in-chat survey page
    question: Which filters can I apply to in-chat survey analytics?
  - id: getAnalyticsInChatSurveyIndex
    intent: Get the results of a CSAT analytics job
    question: Where do I collect the output of a CSAT job I already created?
  - id: csatResponseCounts
    intent: Start a CSAT response counts job
    question: How many CSAT responses did each question get over a date range?
  - id: csatQuestionResponses
    intent: Start a job for one CSAT question's responses
    question: What did customers actually answer to one specific CSAT question?
  - id: csatUserResponses
    intent: Start a CSAT responses-by-user job
    question: Which users submitted CSAT surveys during a period and what did they say?
  phrasing_ops: 6
  slug: lucidya-ltd-csat-analytics-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: Endpoints for retrieving per-engagement applied custom-field values (job-based)
  name: Lucidya Ltd Custom Fields API
  phrasing_intents:
  - id: createCustomFieldsJob
    intent: Start a job for engagements' custom-field values
    question: How do I export the custom-field values tagged on engagements for a period?
  - id: getCustomFieldsResults
    intent: Get results of a custom fields job
    question: Are my custom field results ready to read yet?
  phrasing_ops: 2
  slug: lucidya-ltd-custom-fields-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: Operations related to default and main endpoints on OmniChannel.
  name: Lucidya Ltd Default API
  phrasing_intents:
  - id: getChannelList
    intent: List connected OmniChannel channels
    question: Which channels are connected to my OmniChannel product?
  - id: getCategories
    intent: List OmniChannel categories and their data sources
    question: What categories like social media, reviews and calls does OmniChannel group sources into?
  - id: getWidgetNames
    intent: List widget names for a channel and category
    question: What widget names can I request for the TWITTER_PUBLIC channel?
  phrasing_ops: 3
  slug: lucidya-ltd-default-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: The Dialects API from Lucidya Ltd — 1 operation(s) for dialects.
  name: Lucidya Ltd Dialects API
  phrasing_intents:
  - id: predict_dialects_batch_ai_dialects_predict_batch_post
    intent: Detect Arabic dialects in a batch of texts
    question: Can I detect which Arabic dialect and sub-dialect a set of posts is written in?
  phrasing_ops: 1
  slug: lucidya-ltd-dialects-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: The Domains API from Lucidya Ltd — 1 operation(s) for domains.
  name: Lucidya Ltd Domains API
  phrasing_intents:
  - id: predict_domains_batch_ai_domains_predict_batch_post
    intent: Classify texts by topic domain in batch
    question: Can I tag a batch of texts with domains like technology or shopping and fashion?
  phrasing_ops: 1
  slug: lucidya-ltd-domains-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: Operations related to Gmail channel.
  name: Lucidya Ltd Email > Gmail API
  phrasing_intents:
  - id: createGmailWidgetData
    intent: Request Gmail email widget data for a period
    question: How do I start an analytics job for my connected Gmail inbox?
  - id: getGmailWidgetData
    intent: Get Gmail email widget results for a job
    question: Where do I read email analytics for my Gmail channel after the job runs?
  phrasing_ops: 2
  slug: lucidya-ltd-email-gmail-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: The Filters API from Lucidya Ltd — 1 operation(s) for filters.
  name: Lucidya Ltd Filters API
  phrasing_intents:
  - id: getFilters
    intent: List filters available in my CDP account
    question: Which segment and data source filters can I use on customer profiles?
  phrasing_ops: 1
  slug: lucidya-ltd-filters-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: The Profile Interactions API from Lucidya Ltd — 2 operation(s) for profile interactions.
  name: Lucidya Ltd Profile Interactions API
  phrasing_intents:
  - id: createInteractionProfile
    intent: Start a job collecting a customer's interactions
    question: How do I gather every interaction a customer had with us over a period?
  - id: getInteractionProfileById
    intent: Get a customer's public and private interactions
    question: Can I see all public and private social interactions for one customer?
  phrasing_ops: 2
  slug: lucidya-ltd-profile-interactions-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: The Profiles API from Lucidya Ltd — 2 operation(s) for profiles.
  name: Lucidya Ltd Profiles API
  phrasing_intents:
  - id: getProfileList
    intent: List customer profiles in a date range
    question: Which customer profile IDs exist in my CDP for a given period?
  - id: createProfile
    intent: Create a new customer profile
    question: How do I add a brand-new customer profile to the CDP?
  - id: updateProfile
    intent: Update a customer profile's contact details
    question: Can I change the email or phone on an existing CDP profile?
  - id: getProfileById
    intent: Get full details for one customer profile
    question: What has Lucidya analysed about a specific customer?
  phrasing_ops: 4
  slug: lucidya-ltd-profiles-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: The Public API - Monitors List API from Lucidya Ltd — 1 operation(s) for public api - monitors list.
  name: Lucidya Ltd Public API - Monitors List API
  phrasing_intents:
  - id: monitors_list
    intent: List social listening monitors in my account
    question: Which social listening monitors do I have set up?
  phrasing_ops: 1
  slug: lucidya-ltd-public-api-monitors-list-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: The Public APIs - Social Listening - Base APIs API from Lucidya Ltd — 3 operation(s) for public apis - social listening - base apis.
  name: Lucidya Ltd Public APIs - Social Listening - Base APIs API
  phrasing_intents:
  - id: Widgets
    intent: List widgets for a social listening monitor
    question: What widgets are available on my social listening monitor?
  - id: filters
    intent: Get filters for a social listening monitor
    question: Which filters can I apply to my monitor's data?
  - id: pages
    intent: List pages for a social listening monitor
    question: Which pages does my social listening monitor have for a data source?
  phrasing_ops: 3
  slug: lucidya-ltd-public-apis-social-listening-base-apis-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: The Public APIs - Social Listening - Facebook widget_data APIs API from Lucidya Ltd — 1 operation(s) for public apis - social listening - facebook widget_data apis.
  name: Lucidya Ltd Public APIs - Social Listening - Facebook widget_data APIs API
  phrasing_intents:
  - id: post-facebook-widget-data
    intent: Request Facebook listening widget data for a monitor
    question: How do I get a job_id for Facebook widgets on my social listening monitor?
  phrasing_ops: 1
  slug: lucidya-ltd-public-apis-social-listening-facebook-widget-data-apis-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: The Public APIs - Social Listening - instagram widget_data APIs API from Lucidya Ltd — 1 operation(s) for public apis - social listening - instagram widget_data apis.
  name: Lucidya Ltd Public APIs - Social Listening - instagram widget_data APIs API
  phrasing_intents:
  - id: post-instagram-widget-data
    intent: Request Instagram listening widget data for a monitor
    question: How do I get a job_id for Instagram widgets on my listening monitor?
  phrasing_ops: 1
  slug: lucidya-ltd-public-apis-social-listening-instagram-widget-data-apis-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: The Public APIs - Social Listening - nb widget_data APIs API from Lucidya Ltd — 1 operation(s) for public apis - social listening - nb widget_data apis.
  name: Lucidya Ltd Public APIs - Social Listening - nb widget_data APIs API
  phrasing_intents:
  - id: post-new-blogs-widget-data
    intent: Request News & Blogs widget data for a monitor
    question: How do I pull news and blog coverage widgets for my listening monitor?
  phrasing_ops: 1
  slug: lucidya-ltd-public-apis-social-listening-nb-widget-data-apis-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: The Public APIs - Social Listening - twitter widget_data APIs API from Lucidya Ltd — 1 operation(s) for public apis - social listening - twitter widget_data apis.
  name: Lucidya Ltd Public APIs - Social Listening - twitter widget_data APIs API
  phrasing_intents:
  - id: post-twitter-widget-data
    intent: Request Twitter listening widget data for a monitor
    question: How do I get a job_id for Twitter widgets on my social listening monitor?
  phrasing_ops: 1
  slug: lucidya-ltd-public-apis-social-listening-twitter-widget-data-apis-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: Operations related to Google My Business channel.
  name: Lucidya Ltd Rating > Google My Business API
  phrasing_intents:
  - id: createGoogleMyBusinessWidgetData
    intent: Request Google My Business review widget data
    question: How do I start an analytics job on my Google My Business reviews?
  - id: getGoogleMyBusinessWidgetData
    intent: Get Google My Business review widget results
    question: Where do I read my Google My Business review analytics once the job is ready?
  phrasing_ops: 2
  slug: lucidya-ltd-rating-google-my-business-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: Endpoints for fetching reference data (agents, teams, data sources)
  name: Lucidya Ltd Reference Data API
  phrasing_intents:
  - id: getAgents
    intent: List my company's agents
    question: Who are the active agents in my company account?
  - id: getTeams
    intent: List my company's teams
    question: Which teams are set up in my company?
  - id: getDataSources
    intent: List data sources available to my company
    question: Which data sources are available for my company?
  - id: getRoutings
    intent: List inbound routings
    question: Which inbound routing rules does my company have?
  - id: getSlas
    intent: List SLAs and their time thresholds
    question: What SLA policies do we have and what are their time thresholds?
  phrasing_ops: 5
  slug: lucidya-ltd-reference-data-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: The Segments API from Lucidya Ltd — 3 operation(s) for segments.
  name: Lucidya Ltd Segments API
  phrasing_intents:
  - id: getSegmentList
    intent: List customer segments
    question: Which customer segments exist in my account?
  - id: appendProfilleToSegment
    intent: Add profiles to a segment
    question: How do I add several customer profiles to an existing segment?
  - id: deleteProfilleFromSegment
    intent: Remove profiles from a segment
    question: How do I take customers out of a segment?
  phrasing_ops: 3
  slug: lucidya-ltd-segments-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: The Sentiment API from Lucidya Ltd — 1 operation(s) for sentiment.
  name: Lucidya Ltd Sentiment API
  phrasing_intents:
  - id: predict_sentiment_batch_ai_sentiment_predict_batch_post
    intent: Predict sentiment for a batch of texts
    question: Can I score the sentiment of many posts in one call?
  phrasing_ops: 1
  slug: lucidya-ltd-sentiment-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: Operations related to Facebook "Public and Private" channel.
  name: Lucidya Ltd Social Media > Facebook API
  phrasing_intents:
  - id: createFacebookWidgetData
    intent: Request Facebook public or private widget data
    question: How do I start an analytics job for public or private Facebook data?
  - id: getFacebookWidgetData
    intent: Get Facebook public or private widget results
    question: Where do I read Facebook page analytics once my widget job is done?
  phrasing_ops: 2
  slug: lucidya-ltd-social-media-facebook-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: Operations related to Instagram "Public and Private" channel.
  name: Lucidya Ltd Social Media > Instagram API
  phrasing_intents:
  - id: createInstagramWidgetData
    intent: Request Instagram public or private widget data
    question: How do I start an analytics job for my Instagram channel?
  - id: getInstagramWidgetData
    intent: Get Instagram public or private widget results
    question: Where do I read Instagram account analytics after my widget job finishes?
  phrasing_ops: 2
  slug: lucidya-ltd-social-media-instagram-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: Operations related to Linkedin channel.
  name: Lucidya Ltd Social Media > Linkedin API
  phrasing_intents:
  - id: createLinkedInWidgetData
    intent: Request LinkedIn public widget data for a period
    question: How do I start an analytics job for my LinkedIn public page?
  - id: getLinkedInWidgetData
    intent: Get LinkedIn public widget results for a job
    question: Where do I read LinkedIn page analytics once the widget job completes?
  phrasing_ops: 2
  slug: lucidya-ltd-social-media-linkedin-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: Operations related to all social cannels.
  name: Lucidya Ltd Social Media > Social API
  phrasing_intents:
  - id: createSocialWidgetData
    intent: Request widget data across all social channels
    question: How do I request a single job that covers every connected social channel?
  - id: getSocialWidgetData
    intent: Get the all-social-channels overview widget results
    question: Where do I get one overview across all my connected social media channels?
  phrasing_ops: 2
  slug: lucidya-ltd-social-media-social-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: Operations related to TikTok channel.
  name: Lucidya Ltd Social Media > TikTok API
  phrasing_intents:
  - id: createTikTokWidgetData
    intent: Request TikTok public widget data for a period
    question: How do I start an analytics job for my TikTok channel?
  - id: get-omnichannel-tiktok-widget_data
    intent: Get TikTok public widget results for a job
    question: Where do I read TikTok account analytics once the widget job is ready?
  phrasing_ops: 2
  slug: lucidya-ltd-social-media-tiktok-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: Operations related to X (Twitter) "Public and Private" channel.
  name: Lucidya Ltd Social Media > X (Twitter) API
  phrasing_intents:
  - id: createTwitterWidgetData
    intent: Request X (Twitter) widget data for a period
    question: How do I start an omnichannel analytics job for my X account?
  phrasing_ops: 1
  slug: lucidya-ltd-social-media-x-twitter-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: The Surveys API from Lucidya Ltd — 1 operation(s) for surveys.
  name: Lucidya Ltd Surveys API
  phrasing_intents:
  - id: getSurveyByProfileId
    intent: Get survey responses for a customer profile
    question: What surveys has a specific customer answered?
  phrasing_ops: 1
  slug: lucidya-ltd-surveys-api
- baseURL: https://api.lucidya.com
  baseurl_source: declared
  description: The Themes API from Lucidya Ltd — 1 operation(s) for themes.
  name: Lucidya Ltd Themes API
  phrasing_intents:
  - id: predict_themes_batch_ai_themes_predict_batch_post
    intent: Predict themes and sub-themes for texts
    question: Can I tell whether each message is a question, complaint or something else?
  phrasing_ops: 1
  slug: lucidya-ltd-themes-api
artifact_total: 49
asyncapis:
- description: ''
  name: Lucidya Ltd Webhooks
  slug: lucidya-ltd-webhooks
collections:
- collection_type: open
  name: Lucidya Public AI API
  slug: open-lucidya-ltd-ai-api
- collection_type: open
  name: CDP (Customer Data Platform) API
  slug: open-lucidya-ltd-cdp-api
- collection_type: open
  name: OmniChannel API
  slug: open-lucidya-ltd-omnichannel-api
- collection_type: open
  name: OmniServe Analytics API
  slug: open-lucidya-ltd-omniserve-analytics-api
- collection_type: open
  name: Lucidya Social Listening Public API
  slug: open-lucidya-ltd-social-listening-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/capabilities/lucidya-ltd-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lucidya-ltd-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/skills/lucidya-ltd-pull-social-listening-widget-data.md
  title: ''
  type: AgentSkill
  url: skills/lucidya-ltd-pull-social-listening-widget-data.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/overlays/lucidya-ltd-ai-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lucidya-ltd-ai-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/skills/lucidya-ltd-analyze-arabic-text.md
  title: ''
  type: AgentSkill
  url: skills/lucidya-ltd-analyze-arabic-text.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/skills/lucidya-ltd-transcribe-audio.md
  title: ''
  type: AgentSkill
  url: skills/lucidya-ltd-transcribe-audio.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/overlays/lucidya-ltd-cdp-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lucidya-ltd-cdp-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/skills/lucidya-ltd-manage-cdp-profiles-and-segments.md
  title: ''
  type: AgentSkill
  url: skills/lucidya-ltd-manage-cdp-profiles-and-segments.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/overlays/lucidya-ltd-omnichannel-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lucidya-ltd-omnichannel-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/overlays/lucidya-ltd-omniserve-analytics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lucidya-ltd-omniserve-analytics-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/skills/lucidya-ltd-run-omniserve-analytics-job.md
  title: ''
  type: AgentSkill
  url: skills/lucidya-ltd-run-omniserve-analytics-job.md
- group: company
  title: ''
  type: Website
  url: https://lucidya.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lucidya.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lucidya.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lucidya.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lucidya.com/docs/Social-Listening-api/rqwky70duwx76-get-started
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/authentication/lucidya-ltd-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lucidya-ltd-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/conventions/lucidya-ltd-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lucidya-ltd-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/asyncapi/lucidya-ltd-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/lucidya-ltd-webhooks.yml
- group: operate
  title: ''
  type: Support
  url: https://help.lucidya.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.lucidya.com/
- group: company
  title: ''
  type: Blog
  url: https://lucidya.com/blog
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/changelog/lucidya-ltd-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/lucidya-ltd-changelog.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.lucidya.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/lifecycle/lucidya-ltd-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lucidya-ltd-lifecycle.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lucidya.com/pricing/omniserve
- group: start
  title: ''
  type: SignUp
  url: https://cxm.lucidya.com/register
- group: start
  title: ''
  type: Login
  url: https://cxm.lucidya.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lucidya.com/service-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lucidya.com/privacy-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/security/lucidya-ltd-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/lucidya-ltd-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/security/lucidya-ltd-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/lucidya-ltd-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.lucidya.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/conformance/lucidya-ltd-conformance.yml
  title: ''
  type: Compliance
  url: conformance/lucidya-ltd-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/conformance/lucidya-ltd-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lucidya-ltd-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/security/lucidya-ltd-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lucidya-ltd-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lucidya
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/llms/lucidya-ltd-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lucidya-ltd-llms.txt
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/openapi/_original/lucidya-ltd-social-listening-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/lucidya-ltd-social-listening-api-openapi.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/overlays/lucidya-ltd-social-listening-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lucidya-ltd-social-listening-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/errors/lucidya-ltd-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/lucidya-ltd-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/rate-limits/lucidya-ltd-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lucidya-ltd-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/plans/lucidya-ltd-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lucidya-ltd-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/data-model/lucidya-ltd-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lucidya-ltd-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/sandbox/lucidya-ltd-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/lucidya-ltd-sandbox.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/packages/lucidya-ltd-packages.yml
  title: ''
  type: Packages
  url: packages/lucidya-ltd-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/mcp/lucidya-ltd-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/lucidya-ltd-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Lucidya is an AI-native customer experience management (CXM) platform for social listening, unified customer data, omnichannel engagement, surveys, and AI-powered text analysis, with deep Arabic-language and MENA-market capabilities. Its public developer platform (docs.lucidya.com) exposes a suite of RESTful APIs across six products — Social Listening, AI, CDP, OmniChannel, OmniServe Analytics, and Webhooks — for programmatic access to social data, customer profiles, analytics, AI text/audio models, and real-time event notifications. Lucidya is a 500 Global portfolio company headquartered in Saudi Arabia and is certified for SOC 2 Type 2 and ISO 27001.
image: https://lh3.googleusercontent.com/d/1rlLPfBLpzoGQ2qAS_b9JeAxSnoyaa6RQ
layout: provider
modified: '2026-09-16'
name: Lucidya
nav: Providers
network: true
overview: 'Lucidya publishes 37 APIs on the [APIs.io](https://apis.io/) network, including Ltd aggregated pages > Analytics API, Ltd aggregated pages > Interactions API, Ltd Analytics Jobs API, and 34 more. Tagged areas include Company, Customer Experience, Social Listening, Customer Data Platform, and Analytics.


  The Lucidya catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lucidya''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, changelog, and 40 more developer resources.'
plans:
- name: Lucidya Ltd Plans Pricing
  plan_count: 5
  slug: lucidya-ltd-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 4
  name: Lucidya Ltd Rate Limits
  slug: lucidya-ltd-rate-limits
score:
  band: exemplar
  composite: 68.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 59.4
    developer_ergonomics: 66.1
    discoverability: 78.6
    operational_transparency: 84.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - saudi-arabia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 67.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 36
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
    score: 32.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/lucidya-ltd/refs/heads/main/screenshots/lucidya-ltd-2026-07-25T225641.png
security:
- kind: authentication
  name: Lucidya Ltd Authentication
  slug: lucidya-ltd-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Lucidya Ltd Domain Security
  slug: lucidya-ltd-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Lucidya Ltd Vulnerability Disclosure
  slug: lucidya-ltd-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Lucidya Ltd Trust Center
  slug: lucidya-ltd-trust-center
  summary_line: SOC 2 Type 2, ISO 27001
slug: lucidya-ltd
tags:
- Company
- Customer Experience
- Social Listening
- Customer Data Platform
- Analytics
- Artificial Intelligence
- Omnichannel
- Arabic NLP
- MENA
website: https://lucidya.com
---
