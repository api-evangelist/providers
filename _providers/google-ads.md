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
  - scopes
  - rate-limits
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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 168
  human_in_the_loop: 0
  name: Google Ads Agentic Access
  operation_count: 184
  slug: google-ads-agentic-access
  summary_line: 184 operations · 168 acting
api_count: 2
apis:
- description: JavaScript-based scripting interface for programmatically managing and querying Google Ads data directly in a browser-based IDE. Scripts enable automated changes to campaigns, ad groups, and reporting
  name: Google Ads Scripts
  slug: google-ads-scripts
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: Manage ad groups within campaigns
  name: Google Ads Ad Groups API
  phrasing_intents:
  - id: mutateAdGroups
    intent: Create, update or remove ad groups (v18)
    question: How do I add a new ad group to a campaign?
  phrasing_ops: 1
  slug: google-ads-ad-groups-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: Create and manage individual ads within ad groups
  name: Google Ads API
  phrasing_intents:
  - id: mutateAdGroupAds
    intent: Create, update or remove ads (v18)
    question: How do I publish a responsive search ad in an ad group?
  phrasing_ops: 1
  slug: google-ads-ads-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: Manage bidding strategies for campaigns
  name: Google Ads Bidding Strategies API
  phrasing_intents:
  - id: mutateBiddingStrategies
    intent: Create, update or remove bid strategies (v18)
    question: How do I set up a Target CPA portfolio bid strategy?
  phrasing_ops: 1
  slug: google-ads-bidding-strategies-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: Create, read, update, and remove advertising campaigns
  name: Google Ads Campaigns API
  phrasing_intents:
  - id: mutateCampaigns
    intent: Create, update or remove campaigns (v18)
    question: How do I create a new campaign through the v18 API?
  - id: mutateCampaignBudgets
    intent: Create, update or remove campaign budgets (v18)
    question: How do I set a daily spending limit shared by my campaigns?
  phrasing_ops: 2
  slug: google-ads-campaigns-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: Access and manage Google Ads customer account information
  name: Google Ads Customers API
  phrasing_intents:
  - id: getCustomer
    intent: Get a Google Ads account's details
    question: What details can I pull back about a single Google Ads account through the v18 API?
  - id: listAccessibleCustomers
    intent: List accounts my login can access (v18)
    question: Which Google Ads accounts can my OAuth login reach directly on the v18 API?
  - id: googleads_customers_generateShareablePreviews
    intent: Generate shareable ad previews
    question: Can I produce a preview link of my ads to share with a client who has no account access?
  - id: googleads_customers_listAccessibleCustomers
    intent: List accounts my login can access (v25)
    question: Which customer accounts does my authenticated user reach directly on the current v25 API?
  - id: googleads_customers_generateKeywordHistoricalMetrics
    intent: Get historical metrics for keywords
    question: How many monthly searches did a set of keywords get historically?
  - id: googleads_customers_suggestKeywordThemes
    intent: Suggest keyword themes for a Smart campaign
    question: What keyword themes would suit my business for a Smart campaign?
  - id: googleads_customers_generateAudienceDefinition
    intent: Turn a text description into an audience
    question: Can I describe my ideal audience in plain words and get targetable attributes back?
  - id: googleads_customers_generateTrendingInsights
    intent: Get trending YouTube content insights
    question: What content is trending on YouTube for my audience in a given country?
  phrasing_ops: 33
  slug: google-ads-customers-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: Manage keyword targeting criteria for ad groups
  name: Google Ads Keywords API
  phrasing_intents:
  - id: mutateAdGroupCriteria
    intent: Add, change or remove keywords (v18)
    question: How do I add phrase or exact match keywords to an ad group?
  phrasing_ops: 1
  slug: google-ads-keywords-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: Query performance data using Google Ads Query Language (GAQL)
  name: Google Ads Reporting API
  phrasing_intents:
  - id: searchGoogleAds
    intent: Query reports with GAQL, page by page
    question: How do I pull clicks and cost by campaign using a Google Ads Query Language query?
  - id: searchStreamGoogleAds
    intent: Stream a large GAQL report
    question: What's the most efficient way to export a very large report?
  phrasing_ops: 2
  slug: google-ads-reporting-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.accountBudgetProposals API from Google Ads — 1 operation(s) for customers.accountbudgetproposals.
  name: Google Ads Customers.account Budget Proposals API
  phrasing_intents:
  - id: googleads_customers_accountBudgetProposals_mutate
    intent: Propose an account-level budget change
    question: How do I propose a new account budget or change its spending limit?
  phrasing_ops: 1
  slug: google-ads-customers-accountbudgetproposals-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.accountLinks API from Google Ads — 2 operation(s) for customers.accountlinks.
  name: Google Ads Customers.account Links API
  phrasing_intents:
  - id: googleads_customers_accountLinks_create
    intent: Create an account link
    question: How do I link a third-party app analytics account to my ads account?
  - id: googleads_customers_accountLinks_mutate
    intent: Update or remove an account link
    question: Can I remove an existing account link?
  phrasing_ops: 2
  slug: google-ads-customers-accountlinks-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.adGroupAdLabels API from Google Ads — 1 operation(s) for customers.adgroupadlabels.
  name: Google Ads Customers.ad Group Ad Labels API
  phrasing_intents:
  - id: googleads_customers_adGroupAdLabels_mutate
    intent: Label or unlabel ads
    question: Can I tag individual ads with a label to organize them?
  phrasing_ops: 1
  slug: google-ads-customers-adgroupadlabels-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.adGroupAds API from Google Ads — 2 operation(s) for customers.adgroupads.
  name: Google Ads Customers.ad Group Ads API
  phrasing_intents:
  - id: googleads_customers_adGroupAds_removeAutomaticallyCreatedAssets
    intent: Remove auto-created assets from an ad
    question: Can I remove assets Google generated automatically for a specific ad?
  - id: googleads_customers_adGroupAds_mutate
    intent: Create, update or remove ads in ad groups
    question: How do I add a new responsive search ad to an ad group?
  phrasing_ops: 2
  slug: google-ads-customers-adgroupads-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.adGroupAssets API from Google Ads — 1 operation(s) for customers.adgroupassets.
  name: Google Ads Customers.ad Group Assets API
  phrasing_intents:
  - id: googleads_customers_adGroupAssets_mutate
    intent: Link assets to ad groups
    question: Can I add a sitelink or callout asset to just one ad group?
  phrasing_ops: 1
  slug: google-ads-customers-adgroupassets-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.adGroupAssetSets API from Google Ads — 1 operation(s) for customers.adgroupassetsets.
  name: Google Ads Customers.ad Group Asset Sets API
  phrasing_intents:
  - id: googleads_customers_adGroupAssetSets_mutate
    intent: Link asset sets to ad groups
    question: Can I attach an asset set to a specific ad group?
  phrasing_ops: 1
  slug: google-ads-customers-adgroupassetsets-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.adGroupBidModifiers API from Google Ads — 1 operation(s) for customers.adgroupbidmodifiers.
  name: Google Ads Customers.ad Group Bid Modifiers API
  phrasing_intents:
  - id: googleads_customers_adGroupBidModifiers_mutate
    intent: Set bid adjustments on ad groups
    question: Can I raise bids for mobile devices in a single ad group?
  phrasing_ops: 1
  slug: google-ads-customers-adgroupbidmodifiers-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.adGroupCriteria API from Google Ads — 1 operation(s) for customers.adgroupcriteria.
  name: Google Ads Customers.ad Group Criteria API
  phrasing_intents:
  - id: googleads_customers_adGroupCriteria_mutate
    intent: Manage keywords and targeting in ad groups
    question: How do I add keywords or audiences to an ad group?
  phrasing_ops: 1
  slug: google-ads-customers-adgroupcriteria-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.AdGroupCriterionCustomizers API from Google Ads — 1 operation(s) for customers.adgroupcriterioncustomizers.
  name: Google Ads Customers.Ad Group Criterion Customizers API
  phrasing_intents:
  - id: googleads_customers_AdGroupCriterionCustomizers_mutate
    intent: Set customizer values on keywords
    question: Can I give a specific keyword its own ad customizer value?
  phrasing_ops: 1
  slug: google-ads-customers-adgroupcriterioncustomizers-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.adGroupCriterionLabels API from Google Ads — 1 operation(s) for customers.adgroupcriterionlabels.
  name: Google Ads Customers.ad Group Criterion Labels API
  phrasing_intents:
  - id: googleads_customers_adGroupCriterionLabels_mutate
    intent: Label or unlabel keywords
    question: Can I put a label on keywords to group them for reporting?
  phrasing_ops: 1
  slug: google-ads-customers-adgroupcriterionlabels-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.adGroupCustomizers API from Google Ads — 1 operation(s) for customers.adgroupcustomizers.
  name: Google Ads Customers.ad Group Customizers API
  phrasing_intents:
  - id: googleads_customers_adGroupCustomizers_mutate
    intent: Set customizer values on ad groups
    question: Can I give each ad group its own value for an ad customizer attribute?
  phrasing_ops: 1
  slug: google-ads-customers-adgroupcustomizers-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.adGroupLabels API from Google Ads — 1 operation(s) for customers.adgrouplabels.
  name: Google Ads Customers.ad Group Labels API
  phrasing_intents:
  - id: googleads_customers_adGroupLabels_mutate
    intent: Label or unlabel ad groups
    question: Can I tag ad groups with labels to filter them later?
  phrasing_ops: 1
  slug: google-ads-customers-adgrouplabels-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.adGroups API from Google Ads — 1 operation(s) for customers.adgroups.
  name: Google Ads Customers.ad Groups API
  phrasing_intents:
  - id: googleads_customers_adGroups_mutate
    intent: Create, update or remove ad groups
    question: How do I create ad groups in an existing campaign?
  phrasing_ops: 1
  slug: google-ads-customers-adgroups-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.adParameters API from Google Ads — 1 operation(s) for customers.adparameters.
  name: Google Ads Customers.ad Parameters API
  phrasing_intents:
  - id: googleads_customers_adParameters_mutate
    intent: Set ad parameter values on keywords
    question: Can I insert dynamic numbers like prices into ads through ad parameters?
  phrasing_ops: 1
  slug: google-ads-customers-adparameters-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.ads API from Google Ads — 1 operation(s) for customers.ads.
  name: Google Ads Customers.ads API
  phrasing_intents:
  - id: googleads_customers_ads_mutate
    intent: Update existing ads
    question: Can I edit the text or URLs of an ad that already exists?
  phrasing_ops: 1
  slug: google-ads-customers-ads-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.assetGenerations API from Google Ads — 2 operation(s) for customers.assetgenerations.
  name: Google Ads Customers.asset Generations API
  phrasing_intents:
  - id: googleads_customers_assetGenerations_generateText
    intent: Generate ad text with AI
    question: Can AI write headlines and descriptions for my campaign from my landing page?
  - id: googleads_customers_assetGenerations_generateImages
    intent: Generate ad images with AI
    question: Can AI create image assets for my campaign?
  phrasing_ops: 2
  slug: google-ads-customers-assetgenerations-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.assetGroupAssets API from Google Ads — 1 operation(s) for customers.assetgroupassets.
  name: Google Ads Customers.asset Group Assets API
  phrasing_intents:
  - id: googleads_customers_assetGroupAssets_mutate
    intent: Link assets to Performance Max asset groups
    question: How do I add headlines or images to a Performance Max asset group?
  phrasing_ops: 1
  slug: google-ads-customers-assetgroupassets-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.assetGroupListingGroupFilters API from Google Ads — 1 operation(s) for customers.assetgrouplistinggroupfilters.
  name: Google Ads Customers.asset Group Listing Group Filters API
  phrasing_intents:
  - id: googleads_customers_assetGroupListingGroupFilters_mutate
    intent: Manage product listing filters on asset groups
    question: How do I choose which products a Performance Max asset group advertises?
  phrasing_ops: 1
  slug: google-ads-customers-assetgrouplistinggroupfilters-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.assetGroups API from Google Ads — 1 operation(s) for customers.assetgroups.
  name: Google Ads Customers.asset Groups API
  phrasing_intents:
  - id: googleads_customers_assetGroups_mutate
    intent: Create, update or remove asset groups
    question: How do I create a new asset group in a Performance Max campaign?
  phrasing_ops: 1
  slug: google-ads-customers-assetgroups-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.assetGroupSignals API from Google Ads — 1 operation(s) for customers.assetgroupsignals.
  name: Google Ads Customers.asset Group Signals API
  phrasing_intents:
  - id: googleads_customers_assetGroupSignals_mutate
    intent: Add or remove asset group signals
    question: Can I give a Performance Max asset group an audience signal?
  phrasing_ops: 1
  slug: google-ads-customers-assetgroupsignals-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.assets API from Google Ads — 1 operation(s) for customers.assets.
  name: Google Ads Customers.assets API
  phrasing_intents:
  - id: googleads_customers_assets_mutate
    intent: Create assets
    question: How do I upload an image or create a sitelink asset?
  phrasing_ops: 1
  slug: google-ads-customers-assets-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.assetSetAssets API from Google Ads — 1 operation(s) for customers.assetsetassets.
  name: Google Ads Customers.asset Set Assets API
  phrasing_intents:
  - id: googleads_customers_assetSetAssets_mutate
    intent: Add or remove assets in an asset set
    question: How do I put assets into an asset set?
  phrasing_ops: 1
  slug: google-ads-customers-assetsetassets-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.assetSets API from Google Ads — 1 operation(s) for customers.assetsets.
  name: Google Ads Customers.asset Sets API
  phrasing_intents:
  - id: googleads_customers_assetSets_mutate
    intent: Create, update or remove asset sets
    question: How do I create a new asset set, such as a location set?
  phrasing_ops: 1
  slug: google-ads-customers-assetsets-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.audiences API from Google Ads — 1 operation(s) for customers.audiences.
  name: Google Ads Customers.audiences API
  phrasing_intents:
  - id: googleads_customers_audiences_mutate
    intent: Create audiences
    question: How do I build a reusable audience for targeting?
  phrasing_ops: 1
  slug: google-ads-customers-audiences-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.batchJobs API from Google Ads — 4 operation(s) for customers.batchjobs.
  name: Google Ads Customers.batch Jobs API
  phrasing_intents:
  - id: googleads_customers_batchJobs_run
    intent: Run a batch job
    question: How do I start processing a batch job once I've added operations?
  - id: googleads_customers_batchJobs_addOperations
    intent: Add operations to a batch job
    question: Can I keep appending changes to a batch job before running it?
  - id: googleads_customers_batchJobs_mutate
    intent: Create a batch job
    question: How do I create a new batch job for bulk changes?
  - id: googleads_customers_batchJobs_listResults
    intent: Get the results of a finished batch job
    question: Which operations in my batch job succeeded or failed?
  phrasing_ops: 4
  slug: google-ads-customers-batchjobs-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.biddingDataExclusions API from Google Ads — 1 operation(s) for customers.biddingdataexclusions.
  name: Google Ads Customers.bidding Data Exclusions API
  phrasing_intents:
  - id: googleads_customers_biddingDataExclusions_mutate
    intent: Exclude bad data from Smart Bidding
    question: How do I tell Smart Bidding to ignore days when conversion tracking was broken?
  phrasing_ops: 1
  slug: google-ads-customers-biddingdataexclusions-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.biddingSeasonalityAdjustments API from Google Ads — 1 operation(s) for customers.biddingseasonalityadjustments.
  name: Google Ads Customers.bidding Seasonality Adjustments API
  phrasing_intents:
  - id: googleads_customers_biddingSeasonalityAdjustments_mutate
    intent: Set seasonality adjustments for bidding
    question: How do I prepare Smart Bidding for a flash sale with a conversion rate spike?
  phrasing_ops: 1
  slug: google-ads-customers-biddingseasonalityadjustments-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.biddingStrategies API from Google Ads — 1 operation(s) for customers.biddingstrategies.
  name: Google Ads Customers.bidding Strategies API
  phrasing_intents:
  - id: googleads_customers_biddingStrategies_mutate
    intent: Create, update or remove bid strategies
    question: How do I create a shared portfolio bid strategy?
  phrasing_ops: 1
  slug: google-ads-customers-biddingstrategies-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.billingSetups API from Google Ads — 1 operation(s) for customers.billingsetups.
  name: Google Ads Customers.billing Setups API
  phrasing_intents:
  - id: googleads_customers_billingSetups_mutate
    intent: Create or cancel a billing setup
    question: How do I connect a payments account to an ads account with a billing setup?
  phrasing_ops: 1
  slug: google-ads-customers-billingsetups-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.campaignAssets API from Google Ads — 1 operation(s) for customers.campaignassets.
  name: Google Ads Customers.campaign Assets API
  phrasing_intents:
  - id: googleads_customers_campaignAssets_mutate
    intent: Link assets to campaigns
    question: How do I add a callout or sitelink asset to a campaign?
  phrasing_ops: 1
  slug: google-ads-customers-campaignassets-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.campaignAssetSets API from Google Ads — 1 operation(s) for customers.campaignassetsets.
  name: Google Ads Customers.campaign Asset Sets API
  phrasing_intents:
  - id: googleads_customers_campaignAssetSets_mutate
    intent: Link asset sets to campaigns
    question: How do I attach an asset set to a campaign?
  phrasing_ops: 1
  slug: google-ads-customers-campaignassetsets-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.campaignBidModifiers API from Google Ads — 1 operation(s) for customers.campaignbidmodifiers.
  name: Google Ads Customers.campaign Bid Modifiers API
  phrasing_intents:
  - id: googleads_customers_campaignBidModifiers_mutate
    intent: Set bid adjustments on campaigns
    question: Can I adjust bids for an entire campaign by criterion?
  phrasing_ops: 1
  slug: google-ads-customers-campaignbidmodifiers-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.campaignBudgets API from Google Ads — 1 operation(s) for customers.campaignbudgets.
  name: Google Ads Customers.campaign Budgets API
  phrasing_intents:
  - id: googleads_customers_campaignBudgets_mutate
    intent: Create, update or remove campaign budgets
    question: How do I raise a campaign's daily budget?
  phrasing_ops: 1
  slug: google-ads-customers-campaignbudgets-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.campaignConversionGoals API from Google Ads — 1 operation(s) for customers.campaignconversiongoals.
  name: Google Ads Customers.campaign Conversion Goals API
  phrasing_intents:
  - id: googleads_customers_campaignConversionGoals_mutate
    intent: Set which conversion goals a campaign uses
    question: Can I make a campaign optimize toward specific conversion goals?
  phrasing_ops: 1
  slug: google-ads-customers-campaignconversiongoals-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.campaignCriteria API from Google Ads — 1 operation(s) for customers.campaigncriteria.
  name: Google Ads Customers.campaign Criteria API
  phrasing_intents:
  - id: googleads_customers_campaignCriteria_mutate
    intent: Manage campaign targeting criteria
    question: How do I target locations or languages for a whole campaign?
  phrasing_ops: 1
  slug: google-ads-customers-campaigncriteria-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.campaignCustomizers API from Google Ads — 1 operation(s) for customers.campaigncustomizers.
  name: Google Ads Customers.campaign Customizers API
  phrasing_intents:
  - id: googleads_customers_campaignCustomizers_mutate
    intent: Set customizer values on campaigns
    question: Can I give a campaign its own value for an ad customizer attribute?
  phrasing_ops: 1
  slug: google-ads-customers-campaigncustomizers-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.campaignDrafts API from Google Ads — 3 operation(s) for customers.campaigndrafts.
  name: Google Ads Customers.campaign Drafts API
  phrasing_intents:
  - id: googleads_customers_campaignDrafts_promote
    intent: Promote a campaign draft to its base
    question: How do I push the changes in a campaign draft back to the live campaign?
  - id: googleads_customers_campaignDrafts_listAsyncErrors
    intent: List errors from promoting a draft
    question: Why did my campaign draft promotion fail?
  - id: googleads_customers_campaignDrafts_mutate
    intent: Create, update or remove campaign drafts
    question: Can I make a draft copy of a campaign to test changes safely?
  phrasing_ops: 3
  slug: google-ads-customers-campaigndrafts-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.CampaignGoalConfigs API from Google Ads — 1 operation(s) for customers.campaigngoalconfigs.
  name: Google Ads Customers.Campaign Goal Configs API
  phrasing_intents:
  - id: googleads_customers_CampaignGoalConfigs_mutate
    intent: Create or update campaign goal configs
    question: Can I attach a goal configuration to a campaign?
  phrasing_ops: 1
  slug: google-ads-customers-campaigngoalconfigs-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.campaignGroups API from Google Ads — 1 operation(s) for customers.campaigngroups.
  name: Google Ads Customers.campaign Groups API
  phrasing_intents:
  - id: googleads_customers_campaignGroups_mutate
    intent: Create, update or remove campaign groups
    question: Can I group campaigns together for organization?
  phrasing_ops: 1
  slug: google-ads-customers-campaigngroups-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.campaignLabels API from Google Ads — 1 operation(s) for customers.campaignlabels.
  name: Google Ads Customers.campaign Labels API
  phrasing_intents:
  - id: googleads_customers_campaignLabels_mutate
    intent: Label or unlabel campaigns
    question: Can I tag campaigns with a label like 'holiday'?
  phrasing_ops: 1
  slug: google-ads-customers-campaignlabels-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.campaigns API from Google Ads — 2 operation(s) for customers.campaigns.
  name: Google Ads Customers.campaigns API
  phrasing_intents:
  - id: googleads_customers_campaigns_enablePMaxBrandGuidelines
    intent: Enable Brand Guidelines on Performance Max
    question: How do I turn on Brand Guidelines for my Performance Max campaigns?
  - id: googleads_customers_campaigns_mutate
    intent: Create, update or remove campaigns
    question: Can I launch, edit or remove campaigns through the v25 API?
  phrasing_ops: 2
  slug: google-ads-customers-campaigns-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.campaignSharedSets API from Google Ads — 1 operation(s) for customers.campaignsharedsets.
  name: Google Ads Customers.campaign Shared Sets API
  phrasing_intents:
  - id: googleads_customers_campaignSharedSets_mutate
    intent: Attach shared sets to campaigns
    question: How do I apply a shared negative keyword list to a campaign?
  phrasing_ops: 1
  slug: google-ads-customers-campaignsharedsets-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.conversionActions API from Google Ads — 1 operation(s) for customers.conversionactions.
  name: Google Ads Customers.conversion Actions API
  phrasing_intents:
  - id: googleads_customers_conversionActions_mutate
    intent: Create, update or remove conversion actions
    question: How do I set up a new conversion action to track purchases?
  phrasing_ops: 1
  slug: google-ads-customers-conversionactions-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.conversionCustomVariables API from Google Ads — 1 operation(s) for customers.conversioncustomvariables.
  name: Google Ads Customers.conversion Custom Variables API
  phrasing_intents:
  - id: googleads_customers_conversionCustomVariables_mutate
    intent: Create or update conversion custom variables
    question: Can I attach extra custom data to conversions for segmentation?
  phrasing_ops: 1
  slug: google-ads-customers-conversioncustomvariables-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.conversionGoalCampaignConfigs API from Google Ads — 1 operation(s) for customers.conversiongoalcampaignconfigs.
  name: Google Ads Customers.conversion Goal Campaign Configs API
  phrasing_intents:
  - id: googleads_customers_conversionGoalCampaignConfigs_mutate
    intent: Set a campaign's conversion goal config
    question: Can I tell a campaign to use a custom conversion goal instead of account defaults?
  phrasing_ops: 1
  slug: google-ads-customers-conversiongoalcampaignconfigs-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.conversionValueRules API from Google Ads — 1 operation(s) for customers.conversionvaluerules.
  name: Google Ads Customers.conversion Value Rules API
  phrasing_intents:
  - id: googleads_customers_conversionValueRules_mutate
    intent: Create, update or remove conversion value rules
    question: Can I boost conversion values for customers in a certain location or device?
  phrasing_ops: 1
  slug: google-ads-customers-conversionvaluerules-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.conversionValueRuleSets API from Google Ads — 1 operation(s) for customers.conversionvaluerulesets.
  name: Google Ads Customers.conversion Value Rule Sets API
  phrasing_intents:
  - id: googleads_customers_conversionValueRuleSets_mutate
    intent: Manage conversion value rule sets
    question: How do I group conversion value rules into a set and apply it?
  phrasing_ops: 1
  slug: google-ads-customers-conversionvaluerulesets-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.customAudiences API from Google Ads — 1 operation(s) for customers.customaudiences.
  name: Google Ads Customers.custom Audiences API
  phrasing_intents:
  - id: googleads_customers_customAudiences_mutate
    intent: Create or update custom audiences
    question: How do I build a custom audience from keywords or URLs people search?
  phrasing_ops: 1
  slug: google-ads-customers-customaudiences-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.customConversionGoals API from Google Ads — 1 operation(s) for customers.customconversiongoals.
  name: Google Ads Customers.custom Conversion Goals API
  phrasing_intents:
  - id: googleads_customers_customConversionGoals_mutate
    intent: Manage custom conversion goals
    question: Can I bundle specific conversion actions into a custom goal?
  phrasing_ops: 1
  slug: google-ads-customers-customconversiongoals-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.customerAssets API from Google Ads — 1 operation(s) for customers.customerassets.
  name: Google Ads Customers.customer Assets API
  phrasing_intents:
  - id: googleads_customers_customerAssets_mutate
    intent: Link assets at the account level
    question: Can I add a callout asset that applies to every campaign in the account?
  phrasing_ops: 1
  slug: google-ads-customers-customerassets-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.customerAssetSets API from Google Ads — 1 operation(s) for customers.customerassetsets.
  name: Google Ads Customers.customer Asset Sets API
  phrasing_intents:
  - id: googleads_customers_customerAssetSets_mutate
    intent: Link asset sets at the account level
    question: Can I attach an asset set to the whole account?
  phrasing_ops: 1
  slug: google-ads-customers-customerassetsets-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.customerClientLinks API from Google Ads — 1 operation(s) for customers.customerclientlinks.
  name: Google Ads Customers.customer Client Links API
  phrasing_intents:
  - id: googleads_customers_customerClientLinks_mutate
    intent: Link a client account to a manager
    question: How does a manager account invite a client account to link?
  phrasing_ops: 1
  slug: google-ads-customers-customerclientlinks-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.customerConversionGoals API from Google Ads — 1 operation(s) for customers.customerconversiongoals.
  name: Google Ads Customers.customer Conversion Goals API
  phrasing_intents:
  - id: googleads_customers_customerConversionGoals_mutate
    intent: Set account-wide conversion goals
    question: Can I change which conversion goals are biddable across the account?
  phrasing_ops: 1
  slug: google-ads-customers-customerconversiongoals-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.CustomerCustomizers API from Google Ads — 1 operation(s) for customers.customercustomizers.
  name: Google Ads Customers.Customer Customizers API
  phrasing_intents:
  - id: googleads_customers_CustomerCustomizers_mutate
    intent: Set account-level customizer values
    question: Can I set a default ad customizer value for the whole account?
  phrasing_ops: 1
  slug: google-ads-customers-customercustomizers-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.customerLabels API from Google Ads — 1 operation(s) for customers.customerlabels.
  name: Google Ads Customers.customer Labels API
  phrasing_intents:
  - id: googleads_customers_customerLabels_mutate
    intent: Label or unlabel client accounts
    question: Can a manager label client accounts to organize them?
  phrasing_ops: 1
  slug: google-ads-customers-customerlabels-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.customerManagerLinks API from Google Ads — 2 operation(s) for customers.customermanagerlinks.
  name: Google Ads Customers.customer Manager Links API
  phrasing_intents:
  - id: googleads_customers_customerManagerLinks_moveManagerLink
    intent: Move a client to a new manager
    question: How do I move a client account from one manager account to another?
  - id: googleads_customers_customerManagerLinks_mutate
    intent: Update a client's manager links
    question: Can I accept or deactivate a manager's link to my account?
  phrasing_ops: 2
  slug: google-ads-customers-customermanagerlinks-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.customerNegativeCriteria API from Google Ads — 1 operation(s) for customers.customernegativecriteria.
  name: Google Ads Customers.customer Negative Criteria API
  phrasing_intents:
  - id: googleads_customers_customerNegativeCriteria_mutate
    intent: Manage account-level exclusions
    question: How do I exclude placements or content types across my whole account?
  phrasing_ops: 1
  slug: google-ads-customers-customernegativecriteria-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.customerSkAdNetworkConversionValueSchemas API from Google Ads — 1 operation(s) for customers.customerskadnetworkconversionvalueschemas.
  name: Google Ads Customers.customer Sk Ad Network Conversion Value Schemas API
  phrasing_intents:
  - id: googleads_customers_customerSkAdNetworkConversionValueSchemas_mutate
    intent: Set the SKAdNetwork conversion value schema
    question: How do I map iOS SKAdNetwork conversion values to events?
  phrasing_ops: 1
  slug: google-ads-customers-customerskadnetworkconversionvalueschemas-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.customerUserAccesses API from Google Ads — 1 operation(s) for customers.customeruseraccesses.
  name: Google Ads Customers.customer User Accesses API
  phrasing_intents:
  - id: googleads_customers_customerUserAccesses_mutate
    intent: Change or revoke a user's account access
    question: How do I change a user's access role on an account?
  phrasing_ops: 1
  slug: google-ads-customers-customeruseraccesses-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.customerUserAccessInvitations API from Google Ads — 1 operation(s) for customers.customeruseraccessinvitations.
  name: Google Ads Customers.customer User Access Invitations API
  phrasing_intents:
  - id: googleads_customers_customerUserAccessInvitations_mutate
    intent: Invite or uninvite a user to an account
    question: How do I invite a colleague by email to access an ads account?
  phrasing_ops: 1
  slug: google-ads-customers-customeruseraccessinvitations-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.customInterests API from Google Ads — 1 operation(s) for customers.custominterests.
  name: Google Ads Customers.custom Interests API
  phrasing_intents:
  - id: googleads_customers_customInterests_mutate
    intent: Create or update custom interests
    question: Can I define a custom interest audience from keywords and URLs?
  phrasing_ops: 1
  slug: google-ads-customers-custominterests-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.customizerAttributes API from Google Ads — 1 operation(s) for customers.customizerattributes.
  name: Google Ads Customers.customizer Attributes API
  phrasing_intents:
  - id: googleads_customers_customizerAttributes_mutate
    intent: Manage ad customizer attributes
    question: How do I define a new customizer attribute such as price or stock count?
  phrasing_ops: 1
  slug: google-ads-customers-customizerattributes-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.dataLinks API from Google Ads — 3 operation(s) for customers.datalinks.
  name: Google Ads Customers.data Links API
  phrasing_intents:
  - id: googleads_customers_dataLinks_update
    intent: Change the status of a data link
    question: Can I change the status of an existing data link, such as a YouTube video link?
  - id: googleads_customers_dataLinks_create
    intent: Create a data link with a third party
    question: How do I link my account to a YouTube creator's videos?
  - id: googleads_customers_dataLinks_remove
    intent: Remove a data link
    question: Can I disconnect a data link I set up earlier?
  phrasing_ops: 3
  slug: google-ads-customers-datalinks-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.experimentArms API from Google Ads — 1 operation(s) for customers.experimentarms.
  name: Google Ads Customers.experiment Arms API
  phrasing_intents:
  - id: googleads_customers_experimentArms_mutate
    intent: Create, update or remove experiment arms
    question: How do I define the control and treatment arms of an experiment?
  phrasing_ops: 1
  slug: google-ads-customers-experimentarms-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.experiments API from Google Ads — 6 operation(s) for customers.experiments.
  name: Google Ads Customers.experiments API
  phrasing_intents:
  - id: googleads_customers_experiments_scheduleExperiment
    intent: Schedule an experiment to start
    question: How do I start running a campaign experiment I've designed?
  - id: googleads_customers_experiments_graduateExperiment
    intent: Graduate an experiment to a full campaign
    question: Can I turn a winning experiment campaign into its own standalone campaign?
  - id: googleads_customers_experiments_promoteExperiment
    intent: Apply an experiment's changes to the base
    question: How do I copy the changes from my trial campaign back onto the original campaign?
  - id: googleads_customers_experiments_mutate
    intent: Create, update or remove experiments
    question: Can I set up a new campaign experiment in an account?
  - id: googleads_customers_experiments_endExperiment
    intent: End an experiment immediately
    question: Can I stop an experiment right now instead of waiting for its end date?
  - id: googleads_customers_experiments_listExperimentAsyncErrors
    intent: List errors from an experiment update
    question: Why did scheduling or promoting my experiment fail?
  phrasing_ops: 6
  slug: google-ads-customers-experiments-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.Goals API from Google Ads — 1 operation(s) for customers.goals.
  name: Google Ads Customers.Goals API
  phrasing_intents:
  - id: googleads_customers_Goals_mutate
    intent: Create or update goals
    question: Can I create an account goal through the API?
  phrasing_ops: 1
  slug: google-ads-customers-goals-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.googleAds API from Google Ads — 3 operation(s) for customers.googleads.
  name: Google Ads Customers.google Ads API
  phrasing_intents:
  - id: googleads_customers_googleAds_mutate
    intent: Apply many changes across resource types atomically
    question: Can I create a campaign and its budget in a single atomic request?
  - id: googleads_customers_googleAds_search
    intent: Run a paged GAQL report query
    question: How do I pull campaign performance with a Google Ads Query Language query?
  - id: googleads_customers_googleAds_searchStream
    intent: Stream all rows of a GAQL query
    question: What's the best way to pull a very large report in one streamed response?
  phrasing_ops: 3
  slug: google-ads-customers-googleads-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.incentives API from Google Ads — 1 operation(s) for customers.incentives.
  name: Google Ads Customers.incentives API
  phrasing_intents:
  - id: googleads_customers_incentives_applyIncentive
    intent: Apply a promotional incentive to an account
    question: How do I redeem an ad credit incentive on my account?
  phrasing_ops: 1
  slug: google-ads-customers-incentives-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.invoices API from Google Ads — 1 operation(s) for customers.invoices.
  name: Google Ads Customers.invoices API
  phrasing_intents:
  - id: googleads_customers_invoices_list
    intent: List a month's invoices for a billing setup
    question: Where can I download invoices for a particular month?
  phrasing_ops: 1
  slug: google-ads-customers-invoices-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.keywordPlanAdGroupKeywords API from Google Ads — 1 operation(s) for customers.keywordplanadgroupkeywords.
  name: Google Ads Customers.keyword Plan Ad Group Keywords API
  phrasing_intents:
  - id: googleads_customers_keywordPlanAdGroupKeywords_mutate
    intent: Manage keywords in a keyword plan ad group
    question: How do I add keywords to an ad group inside a keyword plan?
  phrasing_ops: 1
  slug: google-ads-customers-keywordplanadgroupkeywords-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.keywordPlanAdGroups API from Google Ads — 1 operation(s) for customers.keywordplanadgroups.
  name: Google Ads Customers.keyword Plan Ad Groups API
  phrasing_intents:
  - id: googleads_customers_keywordPlanAdGroups_mutate
    intent: Manage ad groups in a keyword plan
    question: Can I add ad groups to a keyword plan for forecasting?
  phrasing_ops: 1
  slug: google-ads-customers-keywordplanadgroups-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.keywordPlanCampaignKeywords API from Google Ads — 1 operation(s) for customers.keywordplancampaignkeywords.
  name: Google Ads Customers.keyword Plan Campaign Keywords API
  phrasing_intents:
  - id: googleads_customers_keywordPlanCampaignKeywords_mutate
    intent: Manage campaign keywords in a keyword plan
    question: Can I add negative keywords at the campaign level of a keyword plan?
  phrasing_ops: 1
  slug: google-ads-customers-keywordplancampaignkeywords-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.keywordPlanCampaigns API from Google Ads — 1 operation(s) for customers.keywordplancampaigns.
  name: Google Ads Customers.keyword Plan Campaigns API
  phrasing_intents:
  - id: googleads_customers_keywordPlanCampaigns_mutate
    intent: Manage campaigns in a keyword plan
    question: How do I set up a campaign inside a keyword plan with targeting and bids?
  phrasing_ops: 1
  slug: google-ads-customers-keywordplancampaigns-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.keywordPlans API from Google Ads — 1 operation(s) for customers.keywordplans.
  name: Google Ads Customers.keyword Plans API
  phrasing_intents:
  - id: googleads_customers_keywordPlans_mutate
    intent: Create, update or remove keyword plans
    question: How do I create a keyword plan to forecast traffic?
  phrasing_ops: 1
  slug: google-ads-customers-keywordplans-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.labels API from Google Ads — 1 operation(s) for customers.labels.
  name: Google Ads Customers.labels API
  phrasing_intents:
  - id: googleads_customers_labels_mutate
    intent: Create, update or remove labels
    question: How do I create a new label with a name and color?
  phrasing_ops: 1
  slug: google-ads-customers-labels-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.localServices API from Google Ads — 1 operation(s) for customers.localservices.
  name: Google Ads Customers.local Services API
  phrasing_intents:
  - id: googleads_customers_localServices_appendLeadConversation
    intent: Add messages to Local Services leads
    question: Can I append a conversation, like a message, to a Local Services lead?
  phrasing_ops: 1
  slug: google-ads-customers-localservices-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.localServicesLeads API from Google Ads — 1 operation(s) for customers.localservicesleads.
  name: Google Ads Customers.local Services Leads API
  phrasing_intents:
  - id: googleads_customers_localServicesLeads_provideLeadFeedback
    intent: Rate a Local Services lead
    question: Can I tell Google whether a Local Services lead was good or bad?
  phrasing_ops: 1
  slug: google-ads-customers-localservicesleads-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.multiPartyAuthReview API from Google Ads — 1 operation(s) for customers.multipartyauthreview.
  name: Google Ads Customers.multi Party Auth Review API
  phrasing_intents:
  - id: googleads_customers_multiPartyAuthReview_resolve
    intent: Approve or deny a multi-party auth review
    question: How do I approve a pending multi-party authorization request?
  phrasing_ops: 1
  slug: google-ads-customers-multipartyauthreview-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.offlineUserDataJobs API from Google Ads — 3 operation(s) for customers.offlineuserdatajobs.
  name: Google Ads Customers.offline User Data Jobs API
  phrasing_intents:
  - id: googleads_customers_offlineUserDataJobs_create
    intent: Create an offline user data job
    question: How do I start a job to upload store sales or Customer Match data?
  - id: googleads_customers_offlineUserDataJobs_addOperations
    intent: Add user data to an offline job
    question: Can I add user records to an offline data job in several batches?
  - id: googleads_customers_offlineUserDataJobs_run
    intent: Run an offline user data job
    question: How do I kick off processing of an offline user data job?
  phrasing_ops: 3
  slug: google-ads-customers-offlineuserdatajobs-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.operations API from Google Ads — 4 operation(s) for customers.operations.
  name: Google Ads Customers.operations API
  phrasing_intents:
  - id: googleads_customers_operations_get
    intent: Check a long-running operation's state
    question: Is my long-running operation done yet?
  - id: googleads_customers_operations_delete
    intent: Delete a long-running operation record
    question: Can I discard an operation I no longer care about?
  - id: googleads_customers_operations_list
    intent: List long-running operations
    question: Which long-running operations exist for my account?
  - id: googleads_customers_operations_cancel
    intent: Cancel a long-running operation
    question: How do I cancel a long-running operation that's still in progress?
  - id: googleads_customers_operations_wait
    intent: Wait for a long-running operation to finish
    question: Can I block until an operation completes instead of polling it?
  phrasing_ops: 5
  slug: google-ads-customers-operations-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.paymentsAccounts API from Google Ads — 1 operation(s) for customers.paymentsaccounts.
  name: Google Ads Customers.payments Accounts API
  phrasing_intents:
  - id: googleads_customers_paymentsAccounts_list
    intent: List payments accounts for an account
    question: Which payments accounts can pay for this ads account?
  phrasing_ops: 1
  slug: google-ads-customers-paymentsaccounts-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.productLinkInvitations API from Google Ads — 3 operation(s) for customers.productlinkinvitations.
  name: Google Ads Customers.product Link Invitations API
  phrasing_intents:
  - id: googleads_customers_productLinkInvitations_remove
    intent: Remove a product link invitation
    question: Can I withdraw a product link invitation I sent?
  - id: googleads_customers_productLinkInvitations_update
    intent: Accept or reject a product link invitation
    question: How do I accept an invitation to link a product to my account?
  - id: googleads_customers_productLinkInvitations_create
    intent: Invite a product to link with an account
    question: Can I send an invitation to link another product to my ads account?
  phrasing_ops: 3
  slug: google-ads-customers-productlinkinvitations-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.productLinks API from Google Ads — 2 operation(s) for customers.productlinks.
  name: Google Ads Customers.product Links API
  phrasing_intents:
  - id: googleads_customers_productLinks_create
    intent: Link a product to an ads account
    question: Can I link a product like a Merchant Center account to my ads account?
  - id: googleads_customers_productLinks_remove
    intent: Remove a product link
    question: How do I unlink a product from my ads account?
  phrasing_ops: 2
  slug: google-ads-customers-productlinks-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.recommendations API from Google Ads — 3 operation(s) for customers.recommendations.
  name: Google Ads Customers.recommendations API
  phrasing_intents:
  - id: googleads_customers_recommendations_apply
    intent: Apply recommendations
    question: How do I accept the optimization recommendations for my account?
  - id: googleads_customers_recommendations_generate
    intent: Generate recommendations for a campaign setup
    question: What recommendations would I get for a campaign I haven't launched yet?
  - id: googleads_customers_recommendations_dismiss
    intent: Dismiss recommendations
    question: Can I hide recommendations I don't want to act on?
  phrasing_ops: 3
  slug: google-ads-customers-recommendations-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.recommendationSubscriptions API from Google Ads — 1 operation(s) for customers.recommendationsubscriptions.
  name: Google Ads Customers.recommendation Subscriptions API
  phrasing_intents:
  - id: googleads_customers_recommendationSubscriptions_mutateRecommendationSubscription
    intent: Subscribe to auto-applied recommendations
    question: Can I have certain recommendation types applied automatically?
  phrasing_ops: 1
  slug: google-ads-customers-recommendationsubscriptions-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.remarketingActions API from Google Ads — 1 operation(s) for customers.remarketingactions.
  name: Google Ads Customers.remarketing Actions API
  phrasing_intents:
  - id: googleads_customers_remarketingActions_mutate
    intent: Create or update remarketing actions
    question: How do I set up a remarketing tag action for website visitors?
  phrasing_ops: 1
  slug: google-ads-customers-remarketingactions-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.reservations API from Google Ads — 2 operation(s) for customers.reservations.
  name: Google Ads Customers.reservations API
  phrasing_intents:
  - id: googleads_customers_reservations_quoteCampaigns
    intent: Get a quote for reserved campaigns
    question: How much would it cost to book a reservation campaign?
  - id: googleads_customers_reservations_bookCampaigns
    intent: Book reservation campaigns
    question: How do I book a reserved campaign after getting a quote?
  phrasing_ops: 2
  slug: google-ads-customers-reservations-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.sharedCriteria API from Google Ads — 1 operation(s) for customers.sharedcriteria.
  name: Google Ads Customers.shared Criteria API
  phrasing_intents:
  - id: googleads_customers_sharedCriteria_mutate
    intent: Add or remove criteria in a shared set
    question: How do I add keywords to a shared negative keyword list?
  phrasing_ops: 1
  slug: google-ads-customers-sharedcriteria-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.sharedSets API from Google Ads — 1 operation(s) for customers.sharedsets.
  name: Google Ads Customers.shared Sets API
  phrasing_intents:
  - id: googleads_customers_sharedSets_mutate
    intent: Create, update or remove shared sets
    question: How do I create a shared negative keyword list?
  phrasing_ops: 1
  slug: google-ads-customers-sharedsets-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.smartCampaignSettings API from Google Ads — 2 operation(s) for customers.smartcampaignsettings.
  name: Google Ads Customers.smart Campaign Settings API
  phrasing_intents:
  - id: googleads_customers_smartCampaignSettings_getSmartCampaignStatus
    intent: Check a Smart campaign's status
    question: Is my Smart campaign serving, or why isn't it?
  - id: googleads_customers_smartCampaignSettings_mutate
    intent: Update Smart campaign settings
    question: Can I change the phone number or landing page settings of a Smart campaign?
  phrasing_ops: 2
  slug: google-ads-customers-smartcampaignsettings-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.thirdPartyAppAnalyticsLinks API from Google Ads — 1 operation(s) for customers.thirdpartyappanalyticslinks.
  name: Google Ads Customers.third Party App Analytics Links API
  phrasing_intents:
  - id: googleads_customers_thirdPartyAppAnalyticsLinks_regenerateShareableLinkId
    intent: Regenerate an app analytics shareable link ID
    question: How do I get a new shareable link ID for a third-party app analytics provider?
  phrasing_ops: 1
  slug: google-ads-customers-thirdpartyappanalyticslinks-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.userListCustomerTypes API from Google Ads — 1 operation(s) for customers.userlistcustomertypes.
  name: Google Ads Customers.user List Customer Types API
  phrasing_intents:
  - id: googleads_customers_userListCustomerTypes_mutate
    intent: Attach or remove user list customer types
    question: Can I label a user list as purchasers or high-value customers?
  phrasing_ops: 1
  slug: google-ads-customers-userlistcustomertypes-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.userLists API from Google Ads — 1 operation(s) for customers.userlists.
  name: Google Ads Customers.user Lists API
  phrasing_intents:
  - id: googleads_customers_userLists_mutate
    intent: Create or update user lists
    question: How do I create a remarketing or Customer Match user list?
  phrasing_ops: 1
  slug: google-ads-customers-userlists-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The customers.youTubeVideoUploads API from Google Ads — 2 operation(s) for customers.youtubevideouploads.
  name: Google Ads Customers.you Tube Video Uploads API
  phrasing_intents:
  - id: googleads_customers_youTubeVideoUploads_update
    intent: Update metadata of an API-uploaded video
    question: Can I change the title or description of a YouTube video I uploaded through the API?
  - id: googleads_customers_youTubeVideoUploads_remove
    intent: Remove API-uploaded YouTube videos
    question: How do I delete YouTube videos that I uploaded through the ads API?
  phrasing_ops: 2
  slug: google-ads-customers-youtubevideouploads-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The geoTargetConstants API from Google Ads — 1 operation(s) for geotargetconstants.
  name: Google Ads Geo Target Constants API
  phrasing_intents:
  - id: googleads_geoTargetConstants_suggest
    intent: Find location targets by name
    question: What's the geo target ID for a city I want to target?
  phrasing_ops: 1
  slug: google-ads-geotargetconstants-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The googleAdsFields API from Google Ads — 2 operation(s) for googleadsfields.
  name: Google Ads Google Ads Fields API
  phrasing_intents:
  - id: googleads_googleAdsFields_get
    intent: Look up one queryable report field
    question: What does a particular report field mean and can I filter or sort by it?
  - id: googleads_googleAdsFields_search
    intent: Search queryable report fields
    question: Which fields and metrics are available to query on a resource?
  phrasing_ops: 2
  slug: google-ads-googleadsfields-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The incentives API from Google Ads — 1 operation(s) for incentives.
  name: Google Ads Incentives API
  phrasing_intents:
  - id: googleads_incentives_fetchIncentive
    intent: Fetch incentives available to a user
    question: Are there any ad credit incentives I'm eligible for?
  phrasing_ops: 1
  slug: google-ads-incentives-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The keywordThemeConstants API from Google Ads — 1 operation(s) for keywordthemeconstants.
  name: Google Ads Keyword Theme Constants API
  phrasing_intents:
  - id: googleads_keywordThemeConstants_suggest
    intent: Suggest keyword theme constants
    question: Which predefined keyword themes match what my business does?
  phrasing_ops: 1
  slug: google-ads-keywordthemeconstants-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The media API from Google Ads — 1 operation(s) for media.
  name: Google Ads Media API
  phrasing_intents:
  - id: googleads_media_upload
    intent: Upload a video to YouTube for ads
    question: Can I upload a video ad to a YouTube channel through the ads API?
  phrasing_ops: 1
  slug: google-ads-media-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The V25:generateConversionRates API from Google Ads — 1 operation(s) for v25:generateconversionrates.
  name: Google Ads V25:generate Conversion Rates API
  phrasing_intents:
  - id: googleads_generateConversionRates
    intent: Suggest conversion rates for planned products
    question: What conversion rates should I assume for plannable YouTube products?
  phrasing_ops: 1
  slug: google-ads-v25-generateconversionrates-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The V25:listBenchmarksAvailableDates API from Google Ads — 1 operation(s) for v25:listbenchmarksavailabledates.
  name: Google Ads V25:list Benchmarks Available Dates API
  phrasing_intents:
  - id: googleads_listBenchmarksAvailableDates
    intent: Get the date range benchmarks cover
    question: Which dates can I request industry benchmarks for?
  phrasing_ops: 1
  slug: google-ads-v25-listbenchmarksavailabledates-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The V25:listBenchmarksLocations API from Google Ads — 1 operation(s) for v25:listbenchmarkslocations.
  name: Google Ads V25:list Benchmarks Locations API
  phrasing_intents:
  - id: googleads_listBenchmarksLocations
    intent: List locations that support benchmarks
    question: Which countries have industry benchmark data?
  phrasing_ops: 1
  slug: google-ads-v25-listbenchmarkslocations-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The V25:listBenchmarksProducts API from Google Ads — 1 operation(s) for v25:listbenchmarksproducts.
  name: Google Ads V25:list Benchmarks Products API
  phrasing_intents:
  - id: googleads_listBenchmarksProducts
    intent: List products that support benchmarks
    question: Which ad products can I compare against industry benchmarks?
  phrasing_ops: 1
  slug: google-ads-v25-listbenchmarksproducts-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The V25:listBenchmarksSources API from Google Ads — 1 operation(s) for v25:listbenchmarkssources.
  name: Google Ads V25:list Benchmarks Sources API
  phrasing_intents:
  - id: googleads_listBenchmarksSources
    intent: List benchmark sources like industry verticals
    question: Which industry verticals can I benchmark against?
  phrasing_ops: 1
  slug: google-ads-v25-listbenchmarkssources-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The V25:listPlannableLocations API from Google Ads — 1 operation(s) for v25:listplannablelocations.
  name: Google Ads V25:list Plannable Locations API
  phrasing_intents:
  - id: googleads_listPlannableLocations
    intent: List locations available for reach planning
    question: Which countries can I use in a reach forecast?
  phrasing_ops: 1
  slug: google-ads-v25-listplannablelocations-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The V25:listPlannableProducts API from Google Ads — 1 operation(s) for v25:listplannableproducts.
  name: Google Ads V25:list Plannable Products API
  phrasing_intents:
  - id: googleads_listPlannableProducts
    intent: List plannable YouTube ad formats for a location
    question: Which YouTube ad formats can I plan in a given location?
  phrasing_ops: 1
  slug: google-ads-v25-listplannableproducts-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The V25:listPlannableUserInterests API from Google Ads — 1 operation(s) for v25:listplannableuserinterests.
  name: Google Ads V25:list Plannable User Interests API
  phrasing_intents:
  - id: googleads_listPlannableUserInterests
    intent: List user interests usable in reach forecasts
    question: Which interests can I target in a reach forecast?
  phrasing_ops: 1
  slug: google-ads-v25-listplannableuserinterests-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The V25:listPlannableUserLists API from Google Ads — 1 operation(s) for v25:listplannableuserlists.
  name: Google Ads V25:list Plannable User Lists API
  phrasing_intents:
  - id: googleads_listPlannableUserLists
    intent: List user lists usable in reach planning
    question: Which of my user lists can I plan against?
  phrasing_ops: 1
  slug: google-ads-v25-listplannableuserlists-api
- baseURL: https://googleads.googleapis.com
  baseurl_source: declared
  description: The Audience Insights API from Google Ads — 1 operation(s) for audience insights.
  name: Google Ads Audience Insights API
  phrasing_intents:
  - id: googleads_audienceInsights_listInsightsEligibleDates
    intent: List dates available for audience insights
    question: Which date ranges can I request audience insights data for?
  phrasing_ops: 1
  slug: google-ads-audience-insights-api
artifact_total: 431
collections:
- collection_type: postman
  name: Google Ads Ad Groups API
  slug: postman-google-ads-ad-groups-api
- collection_type: postman
  name: Google Ad Groups Ads API
  slug: postman-google-ads-ads-api
- collection_type: postman
  name: Google Ads Ad Groups Bidding Strategies API
  slug: postman-google-ads-bidding-strategies-api
- collection_type: postman
  name: Google Ads Ad Groups Campaigns API
  slug: postman-google-ads-campaigns-api
- collection_type: postman
  name: Google Ads Ad Groups Customers API
  slug: postman-google-ads-customers-api
- collection_type: postman
  name: Google Ads Ad Groups Keywords API
  slug: postman-google-ads-keywords-api
- collection_type: postman
  name: Google Ads Ad Groups Reporting API
  slug: postman-google-ads-reporting-api
- collection_type: open
  name: Google Ads Ad Groups API
  slug: open-google-ads-ad-groups-api
- collection_type: open
  name: Google Ad Groups Ads API
  slug: open-google-ads-ads-api
- collection_type: open
  name: Google Ads API
  slug: open-google-ads-api-v25
- collection_type: open
  name: Google Ads API
  slug: open-google-ads-api
- collection_type: open
  name: Google Ads Ad Groups Bidding Strategies API
  slug: open-google-ads-bidding-strategies-api
- collection_type: open
  name: Google Ads Ad Groups Campaigns API
  slug: open-google-ads-campaigns-api
- collection_type: open
  name: Google Ads Ad Groups Customers API
  slug: open-google-ads-customers-api
- collection_type: open
  name: Google Ads Ad Groups Keywords API
  slug: open-google-ads-keywords-api
- collection_type: open
  name: Google Ads Ad Groups Reporting API
  slug: open-google-ads-reporting-api
common:
- group: design
  href: https://artifacts.apis.io/google-ads/rules/google-ads-rules.yml
  title: ''
  type: Spectral
  url: rules/google-ads-rules.yml
- group: design
  href: https://artifacts.apis.io/google-ads/rules/google-ads-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/google-ads-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/google-ads/vocabulary/google-ads-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/google-ads-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/google-ads/grpc/google-ads-google-ads-field-service.proto
  title: ''
  type: Protobuf
  url: grpc/google-ads-google-ads-field-service.proto
- group: other
  href: https://artifacts.apis.io/google-ads/grpc/google-ads-errors.proto
  title: ''
  type: Protobuf
  url: grpc/google-ads-errors.proto
- group: other
  href: https://artifacts.apis.io/google-ads/grpc/google-ads-customer-service.proto
  title: ''
  type: Protobuf
  url: grpc/google-ads-customer-service.proto
- group: other
  href: https://artifacts.apis.io/google-ads/grpc/google-ads-campaign-service.proto
  title: ''
  type: Protobuf
  url: grpc/google-ads-campaign-service.proto
- group: other
  href: https://artifacts.apis.io/google-ads/grpc/google-ads-ad-group-service.proto
  title: ''
  type: Protobuf
  url: grpc/google-ads-ad-group-service.proto
- group: other
  href: https://artifacts.apis.io/google-ads/hosts/google-ads-hosts.yml
  title: ''
  type: Hosts
  url: hosts/google-ads-hosts.yml
- group: build
  href: https://artifacts.apis.io/google-ads/integrations/google-ads-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/google-ads-integration-edges.yml
- group: start
  title: ''
  type: Login
  url: https://accounts.google.com/v3/signin/identifier?continue=https://docs.google.com/&emr=1&followup=https://docs.google.com/&osid=1&passive=1209600&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1242415125:1793808266951534
- group: company
  title: ''
  type: Website
  url: https://ads.google.com/
- group: other
  href: https://artifacts.apis.io/google-ads/capabilities/google-ads-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/google-ads-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/google-ads/overlays/google-ads-api-v25-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/google-ads-api-v25-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-ads/overview
- group: agent
  href: https://artifacts.apis.io/google-ads/agentic-access/google-ads-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/google-ads-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/google-ads/security/google-ads-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-ads-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/google-ads/security/google-ads-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/google-ads-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/google-ads/authentication/google-ads-authentication.yml
  title: ''
  type: Authentication
  url: authentication/google-ads-authentication.yml
- group: auth
  href: https://artifacts.apis.io/google-ads/scopes/google-ads-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/google-ads-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/google-ads-
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/google-ads/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/google-ads/api/docs/first-call/overview
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/google-ads/api/docs/oauth/overview
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: company
  title: ''
  type: Blog
  url: https://ads-developers.googleblog.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/google-ads/api/support
- group: build
  title: ''
  type: SDKs
  url: https://developers.google.com/google-ads/api/docs/client-libs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleads
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/google-ads-api
- group: operate
  title: ''
  type: Community
  url: https://groups.google.com/g/adwords-api
- group: start
  title: ''
  type: Console
  url: https://ads.google.com/
- group: start
  title: ''
  type: Signup
  url: https://ads.google.com/signup
- group: build
  title: ''
  type: Developer Tools
  url: https://developers.google.com/google-ads/api/docs/developer-toolkit/ai-assistant
- group: docs
  href: https://artifacts.apis.io/google-ads/json-schema/google-ads-campaign-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/google-ads-campaign-schema.json
- group: design
  href: https://artifacts.apis.io/google-ads/json-ld/google-ads-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/google-ads-context.jsonld
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/googleads/google-ads-mcp
- group: agent
  href: https://artifacts.apis.io/google-ads/mcp/google-ads-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/google-ads-mcp.yml
- group: build
  href: https://artifacts.apis.io/google-ads/mcp/google-ads-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/google-ads-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/google-ads/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/google-ads/llms/google-ads-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/google-ads-llms.txt
- group: build
  href: https://artifacts.apis.io/google-ads/packages/google-ads-packages.yml
  title: ''
  type: Packages
  url: packages/google-ads-packages.yml
- group: build
  href: https://artifacts.apis.io/google-ads/packages/google-ads-packages.yml
  title: ''
  type: SDKs
  url: packages/google-ads-packages.yml
- group: build
  href: https://artifacts.apis.io/google-ads/cli/google-ads-cli.yml
  title: ''
  type: CLI
  url: cli/google-ads-cli.yml
- group: design
  href: https://artifacts.apis.io/google-ads/conventions/google-ads-conventions.yml
  title: ''
  type: Conventions
  url: conventions/google-ads-conventions.yml
- group: design
  href: https://artifacts.apis.io/google-ads/errors/google-ads-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/google-ads-problem-types.yml
- group: design
  href: https://artifacts.apis.io/google-ads/lifecycle/google-ads-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/google-ads-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/google-ads/lifecycle/google-ads-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/google-ads-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/google-ads/changelog/google-ads-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/google-ads-changelog.yml
- group: design
  href: https://artifacts.apis.io/google-ads/conformance/google-ads-conformance.yml
  title: ''
  type: Conformance
  url: conformance/google-ads-conformance.yml
- group: design
  href: https://artifacts.apis.io/google-ads/data-model/google-ads-data-model.yml
  title: ''
  type: DataModel
  url: data-model/google-ads-data-model.yml
- group: start
  href: https://artifacts.apis.io/google-ads/sandbox/google-ads-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/google-ads-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/google-ads/plans/google-ads-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/google-ads-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/google-ads/rate-limits/google-ads-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/google-ads-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/google-ads/well-known/google-ads-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/google-ads-well-known.yml
- group: auth
  href: https://artifacts.apis.io/google-ads/well-known/google-ads-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/google-ads-security.txt
- group: auth
  href: https://artifacts.apis.io/google-ads/security/google-ads-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/google-ads-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/google-ads/grpc/google-ads-google-ads-service.proto
  title: ''
  type: Protobuf
  url: grpc/google-ads-google-ads-service.proto
- group: other
  href: https://artifacts.apis.io/google-ads/discovery/google-ads-api-v25-discovery.json
  title: ''
  type: Discovery
  url: discovery/google-ads-api-v25-discovery.json
- group: commercial
  href: https://artifacts.apis.io/google-ads/finops/google-ads-finops.yml
  title: ''
  type: FinOps
  url: finops/google-ads-finops.yml
- group: design
  href: https://artifacts.apis.io/google-ads/rules/google-ads-jsonschema-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/google-ads-jsonschema-spectral-rules.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developers.google.com/google-ads/api/reference/rpc/latest/overview
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/google-ads/api/docs/start
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.google.com/google-ads/api/docs/sunset-dates
created: '2024-01-01'
description: The Google Ads API is the modern programmatic interface to Google Ads and the next generation of the AdWords API. It enables developers to interact directly with the Google Ads platform, vastly increasing the efficiency of managing large or complex Google Ads accounts and campaigns.
finops:
- has_sources: true
  method: derived
  name: Google Ads Finops
  primary_unit: ''
  service_category: ''
  slug: google-ads-finops
  template: true
image: https://www.gstatic.com/images/branding/product/1x/google_ads_64dp.png
json_schemas:
- name: Google Ads Campaign
  property_count: 29
  slug: google-ads-campaign
- name: GoogleAdsGoogleadsV25Resources__GoogleAdsField
  property_count: 14
  slug: google-ads-google-ads-googleads-v25-resources-google-ads-field
- name: GoogleAdsGoogleadsV25Services__AddBatchJobOperationsRequest
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-add-batch-job-operations-request
- name: GoogleAdsGoogleadsV25Services__AddBatchJobOperationsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-add-batch-job-operations-response
- name: GoogleAdsGoogleadsV25Services__AddOfflineUserDataJobOperationsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-add-offline-user-data-job-operations-request
- name: GoogleAdsGoogleadsV25Services__AddOfflineUserDataJobOperationsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-add-offline-user-data-job-operations-response
- name: GoogleAdsGoogleadsV25Services__AppendLeadConversationRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-append-lead-conversation-request
- name: GoogleAdsGoogleadsV25Services__AppendLeadConversationResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-append-lead-conversation-response
- name: GoogleAdsGoogleadsV25Services__ApplyIncentiveRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-apply-incentive-request
- name: GoogleAdsGoogleadsV25Services__ApplyIncentiveResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-apply-incentive-response
- name: GoogleAdsGoogleadsV25Services__ApplyRecommendationRequest
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-apply-recommendation-request
- name: GoogleAdsGoogleadsV25Services__ApplyRecommendationResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-apply-recommendation-response
- name: GoogleAdsGoogleadsV25Services__BookCampaignsRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-book-campaigns-request
- name: GoogleAdsGoogleadsV25Services__BookCampaignsResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-book-campaigns-response
- name: GoogleAdsGoogleadsV25Services__CreateAccountLinkRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-create-account-link-request
- name: GoogleAdsGoogleadsV25Services__CreateAccountLinkResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-create-account-link-response
- name: GoogleAdsGoogleadsV25Services__CreateDataLinkRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-create-data-link-request
- name: GoogleAdsGoogleadsV25Services__CreateDataLinkResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-create-data-link-response
- name: GoogleAdsGoogleadsV25Services__CreateOfflineUserDataJobRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-create-offline-user-data-job-request
- name: GoogleAdsGoogleadsV25Services__CreateOfflineUserDataJobResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-create-offline-user-data-job-response
- name: GoogleAdsGoogleadsV25Services__CreateProductLinkInvitationRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-create-product-link-invitation-request
- name: GoogleAdsGoogleadsV25Services__CreateProductLinkInvitationResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-create-product-link-invitation-response
- name: GoogleAdsGoogleadsV25Services__CreateProductLinkRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-create-product-link-request
- name: GoogleAdsGoogleadsV25Services__CreateProductLinkResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-create-product-link-response
- name: GoogleAdsGoogleadsV25Services__CreateYouTubeVideoUploadRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-create-you-tube-video-upload-request
- name: GoogleAdsGoogleadsV25Services__CreateYouTubeVideoUploadResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-create-you-tube-video-upload-response
- name: GoogleAdsGoogleadsV25Services__DismissRecommendationRequest
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-dismiss-recommendation-request
- name: GoogleAdsGoogleadsV25Services__DismissRecommendationResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-dismiss-recommendation-response
- name: GoogleAdsGoogleadsV25Services__EnablePMaxBrandGuidelinesRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-enable-pmax-brand-guidelines-request
- name: GoogleAdsGoogleadsV25Services__EnablePMaxBrandGuidelinesResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-enable-pmax-brand-guidelines-response
- name: GoogleAdsGoogleadsV25Services__FetchIncentiveResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-fetch-incentive-response
- name: GoogleAdsGoogleadsV25Services__GenerateAudienceCompositionInsightsRequest
  property_count: 6
  slug: google-ads-google-ads-googleads-v25-services-generate-audience-composition-insights-request
- name: GoogleAdsGoogleadsV25Services__GenerateConversionRatesRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-generate-conversion-rates-request
- name: GoogleAdsGoogleadsV25Services__GenerateConversionRatesResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-generate-conversion-rates-response
- name: GoogleAdsGoogleadsV25Services__GenerateCreatorInsightsRequest
  property_count: 8
  slug: google-ads-google-ads-googleads-v25-services-generate-creator-insights-request
- name: GoogleAdsGoogleadsV25Services__GenerateImagesRequest
  property_count: 5
  slug: google-ads-google-ads-googleads-v25-services-generate-images-request
- name: GoogleAdsGoogleadsV25Services__GenerateImagesResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-generate-images-response
- name: GoogleAdsGoogleadsV25Services__GenerateKeywordIdeasRequest
  property_count: 13
  slug: google-ads-google-ads-googleads-v25-services-generate-keyword-ideas-request
- name: GoogleAdsGoogleadsV25Services__GenerateReachForecastRequest
  property_count: 10
  slug: google-ads-google-ads-googleads-v25-services-generate-reach-forecast-request
- name: GoogleAdsGoogleadsV25Services__GenerateRecommendationsRequest
  property_count: 19
  slug: google-ads-google-ads-googleads-v25-services-generate-recommendations-request
- name: GoogleAdsGoogleadsV25Services__GenerateRecommendationsResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-generate-recommendations-response
- name: GoogleAdsGoogleadsV25Services__GenerateTextRequest
  property_count: 6
  slug: google-ads-google-ads-googleads-v25-services-generate-text-request
- name: GoogleAdsGoogleadsV25Services__GenerateTextResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-generate-text-response
- name: GoogleAdsGoogleadsV25Services__GenerateTrendingInsightsRequest
  property_count: 7
  slug: google-ads-google-ads-googleads-v25-services-generate-trending-insights-request
- name: GoogleAdsGoogleadsV25Services__GetSmartCampaignStatusResponse
  property_count: 6
  slug: google-ads-google-ads-googleads-v25-services-get-smart-campaign-status-response
- name: GoogleAdsGoogleadsV25Services__GraduateExperimentRequest
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-graduate-experiment-request
- name: GoogleAdsGoogleadsV25Services__ListAudienceInsightsAttributesRequest
  property_count: 7
  slug: google-ads-google-ads-googleads-v25-services-list-audience-insights-attributes-request
- name: GoogleAdsGoogleadsV25Services__ListBatchJobResultsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-list-batch-job-results-response
- name: GoogleAdsGoogleadsV25Services__ListBenchmarksAvailableDatesRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-list-benchmarks-available-dates-request
- name: GoogleAdsGoogleadsV25Services__ListBenchmarksAvailableDatesResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-list-benchmarks-available-dates-response
- name: GoogleAdsGoogleadsV25Services__ListBenchmarksLocationsRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-list-benchmarks-locations-request
- name: GoogleAdsGoogleadsV25Services__ListBenchmarksLocationsResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-list-benchmarks-locations-response
- name: GoogleAdsGoogleadsV25Services__ListBenchmarksProductsRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-list-benchmarks-products-request
- name: GoogleAdsGoogleadsV25Services__ListBenchmarksProductsResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-list-benchmarks-products-response
- name: GoogleAdsGoogleadsV25Services__ListBenchmarksSourcesRequest
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-list-benchmarks-sources-request
- name: GoogleAdsGoogleadsV25Services__ListBenchmarksSourcesResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-list-benchmarks-sources-response
- name: GoogleAdsGoogleadsV25Services__ListCampaignDraftAsyncErrorsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-list-campaign-draft-async-errors-response
- name: GoogleAdsGoogleadsV25Services__ListExperimentAsyncErrorsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-list-experiment-async-errors-response
- name: GoogleAdsGoogleadsV25Services__ListInsightsEligibleDatesRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-list-insights-eligible-dates-request
- name: GoogleAdsGoogleadsV25Services__ListInsightsEligibleDatesResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-list-insights-eligible-dates-response
- name: GoogleAdsGoogleadsV25Services__ListInvoicesResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-list-invoices-response
- name: GoogleAdsGoogleadsV25Services__ListPaymentsAccountsResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-list-payments-accounts-response
- name: GoogleAdsGoogleadsV25Services__ListPlannableLocationsRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-list-plannable-locations-request
- name: GoogleAdsGoogleadsV25Services__ListPlannableLocationsResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-list-plannable-locations-response
- name: GoogleAdsGoogleadsV25Services__ListPlannableProductsRequest
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-list-plannable-products-request
- name: GoogleAdsGoogleadsV25Services__ListPlannableProductsResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-list-plannable-products-response
- name: GoogleAdsGoogleadsV25Services__ListPlannableUserInterestsRequest
  property_count: 5
  slug: google-ads-google-ads-googleads-v25-services-list-plannable-user-interests-request
- name: GoogleAdsGoogleadsV25Services__ListPlannableUserInterestsResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-list-plannable-user-interests-response
- name: GoogleAdsGoogleadsV25Services__ListPlannableUserListsRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-list-plannable-user-lists-request
- name: GoogleAdsGoogleadsV25Services__ListPlannableUserListsResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-list-plannable-user-lists-response
- name: GoogleAdsGoogleadsV25Services__MoveManagerLinkRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-move-manager-link-request
- name: GoogleAdsGoogleadsV25Services__MoveManagerLinkResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-move-manager-link-response
- name: GoogleAdsGoogleadsV25Services__MutateAccountBudgetProposalRequest
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-account-budget-proposal-request
- name: GoogleAdsGoogleadsV25Services__MutateAccountBudgetProposalResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-mutate-account-budget-proposal-response
- name: GoogleAdsGoogleadsV25Services__MutateAccountLinkRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-account-link-request
- name: GoogleAdsGoogleadsV25Services__MutateAccountLinkResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-account-link-response
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupAdLabelsRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-group-ad-labels-request
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupAdLabelsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-group-ad-labels-response
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupAdsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-group-ads-request
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupAdsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-group-ads-response
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupAssetSetsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-group-asset-sets-request
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupAssetSetsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-group-asset-sets-response
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupAssetsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-group-assets-request
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupAssetsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-group-assets-response
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupBidModifiersRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-group-bid-modifiers-request
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupBidModifiersResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-group-bid-modifiers-response
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupCriteriaRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-group-criteria-request
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupCriteriaResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-group-criteria-response
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupCriterionCustomizersRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-group-criterion-customizers-request
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupCriterionCustomizersResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-group-criterion-customizers-response
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupCriterionLabelsRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-group-criterion-labels-request
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupCriterionLabelsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-group-criterion-labels-response
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupCustomizersRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-group-customizers-request
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupCustomizersResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-group-customizers-response
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupLabelsRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-group-labels-request
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupLabelsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-group-labels-response
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-groups-request
- name: GoogleAdsGoogleadsV25Services__MutateAdGroupsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-groups-response
- name: GoogleAdsGoogleadsV25Services__MutateAdParametersRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-parameters-request
- name: GoogleAdsGoogleadsV25Services__MutateAdParametersResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-ad-parameters-response
- name: GoogleAdsGoogleadsV25Services__MutateAdsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-ads-request
- name: GoogleAdsGoogleadsV25Services__MutateAdsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-ads-response
- name: GoogleAdsGoogleadsV25Services__MutateAssetGroupAssetsRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-asset-group-assets-request
- name: GoogleAdsGoogleadsV25Services__MutateAssetGroupAssetsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-asset-group-assets-response
- name: GoogleAdsGoogleadsV25Services__MutateAssetGroupListingGroupFiltersRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-asset-group-listing-group-filters-request
- name: GoogleAdsGoogleadsV25Services__MutateAssetGroupListingGroupFiltersResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-mutate-asset-group-listing-group-filters-response
- name: GoogleAdsGoogleadsV25Services__MutateAssetGroupSignalsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-asset-group-signals-request
- name: GoogleAdsGoogleadsV25Services__MutateAssetGroupSignalsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-asset-group-signals-response
- name: GoogleAdsGoogleadsV25Services__MutateAssetGroupsRequest
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-asset-groups-request
- name: GoogleAdsGoogleadsV25Services__MutateAssetGroupsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-asset-groups-response
- name: GoogleAdsGoogleadsV25Services__MutateAssetSetAssetsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-asset-set-assets-request
- name: GoogleAdsGoogleadsV25Services__MutateAssetSetAssetsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-asset-set-assets-response
- name: GoogleAdsGoogleadsV25Services__MutateAssetSetsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-asset-sets-request
- name: GoogleAdsGoogleadsV25Services__MutateAssetSetsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-asset-sets-response
- name: GoogleAdsGoogleadsV25Services__MutateAssetsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-assets-request
- name: GoogleAdsGoogleadsV25Services__MutateAssetsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-assets-response
- name: GoogleAdsGoogleadsV25Services__MutateAudiencesRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-audiences-request
- name: GoogleAdsGoogleadsV25Services__MutateAudiencesResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-audiences-response
- name: GoogleAdsGoogleadsV25Services__MutateBatchJobRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-mutate-batch-job-request
- name: GoogleAdsGoogleadsV25Services__MutateBatchJobResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-mutate-batch-job-response
- name: GoogleAdsGoogleadsV25Services__MutateBiddingDataExclusionsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-bidding-data-exclusions-request
- name: GoogleAdsGoogleadsV25Services__MutateBiddingDataExclusionsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-bidding-data-exclusions-response
- name: GoogleAdsGoogleadsV25Services__MutateBiddingSeasonalityAdjustmentsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-bidding-seasonality-adjustments-request
- name: GoogleAdsGoogleadsV25Services__MutateBiddingSeasonalityAdjustmentsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-bidding-seasonality-adjustments-response
- name: GoogleAdsGoogleadsV25Services__MutateBiddingStrategiesRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-bidding-strategies-request
- name: GoogleAdsGoogleadsV25Services__MutateBiddingStrategiesResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-bidding-strategies-response
- name: GoogleAdsGoogleadsV25Services__MutateBillingSetupRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-mutate-billing-setup-request
- name: GoogleAdsGoogleadsV25Services__MutateBillingSetupResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-mutate-billing-setup-response
- name: GoogleAdsGoogleadsV25Services__MutateCampaignAssetSetsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-asset-sets-request
- name: GoogleAdsGoogleadsV25Services__MutateCampaignAssetSetsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-asset-sets-response
- name: GoogleAdsGoogleadsV25Services__MutateCampaignAssetsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-assets-request
- name: GoogleAdsGoogleadsV25Services__MutateCampaignAssetsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-assets-response
- name: GoogleAdsGoogleadsV25Services__MutateCampaignBidModifiersRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-bid-modifiers-request
- name: GoogleAdsGoogleadsV25Services__MutateCampaignBidModifiersResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-bid-modifiers-response
- name: GoogleAdsGoogleadsV25Services__MutateCampaignBudgetsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-budgets-request
- name: GoogleAdsGoogleadsV25Services__MutateCampaignBudgetsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-budgets-response
- name: GoogleAdsGoogleadsV25Services__MutateCampaignConversionGoalsRequest
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-conversion-goals-request
- name: GoogleAdsGoogleadsV25Services__MutateCampaignConversionGoalsResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-conversion-goals-response
- name: GoogleAdsGoogleadsV25Services__MutateCampaignCriteriaRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-criteria-request
- name: GoogleAdsGoogleadsV25Services__MutateCampaignCriteriaResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-criteria-response
- name: GoogleAdsGoogleadsV25Services__MutateCampaignCustomizersRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-customizers-request
- name: GoogleAdsGoogleadsV25Services__MutateCampaignCustomizersResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-customizers-response
- name: GoogleAdsGoogleadsV25Services__MutateCampaignDraftsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-drafts-request
- name: GoogleAdsGoogleadsV25Services__MutateCampaignDraftsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-drafts-response
- name: GoogleAdsGoogleadsV25Services__MutateCampaignGoalConfigsRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-goal-configs-request
- name: GoogleAdsGoogleadsV25Services__MutateCampaignGoalConfigsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-goal-configs-response
- name: GoogleAdsGoogleadsV25Services__MutateCampaignGroupsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-groups-request
- name: GoogleAdsGoogleadsV25Services__MutateCampaignGroupsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-groups-response
- name: GoogleAdsGoogleadsV25Services__MutateCampaignLabelsRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-labels-request
- name: GoogleAdsGoogleadsV25Services__MutateCampaignLabelsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-labels-response
- name: GoogleAdsGoogleadsV25Services__MutateCampaignSharedSetsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-shared-sets-request
- name: GoogleAdsGoogleadsV25Services__MutateCampaignSharedSetsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaign-shared-sets-response
- name: GoogleAdsGoogleadsV25Services__MutateCampaignsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaigns-request
- name: GoogleAdsGoogleadsV25Services__MutateCampaignsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-campaigns-response
- name: GoogleAdsGoogleadsV25Services__MutateConversionActionsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-conversion-actions-request
- name: GoogleAdsGoogleadsV25Services__MutateConversionActionsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-conversion-actions-response
- name: GoogleAdsGoogleadsV25Services__MutateConversionCustomVariablesRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-conversion-custom-variables-request
- name: GoogleAdsGoogleadsV25Services__MutateConversionCustomVariablesResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-conversion-custom-variables-response
- name: GoogleAdsGoogleadsV25Services__MutateConversionGoalCampaignConfigsRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-conversion-goal-campaign-configs-request
- name: GoogleAdsGoogleadsV25Services__MutateConversionGoalCampaignConfigsResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-mutate-conversion-goal-campaign-configs-response
- name: GoogleAdsGoogleadsV25Services__MutateConversionValueRuleSetsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-conversion-value-rule-sets-request
- name: GoogleAdsGoogleadsV25Services__MutateConversionValueRuleSetsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-conversion-value-rule-sets-response
- name: GoogleAdsGoogleadsV25Services__MutateConversionValueRulesRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-conversion-value-rules-request
- name: GoogleAdsGoogleadsV25Services__MutateConversionValueRulesResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-conversion-value-rules-response
- name: GoogleAdsGoogleadsV25Services__MutateCustomAudiencesRequest
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-custom-audiences-request
- name: GoogleAdsGoogleadsV25Services__MutateCustomAudiencesResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-mutate-custom-audiences-response
- name: GoogleAdsGoogleadsV25Services__MutateCustomConversionGoalsRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-custom-conversion-goals-request
- name: GoogleAdsGoogleadsV25Services__MutateCustomConversionGoalsResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-mutate-custom-conversion-goals-response
- name: GoogleAdsGoogleadsV25Services__MutateCustomInterestsRequest
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-custom-interests-request
- name: GoogleAdsGoogleadsV25Services__MutateCustomInterestsResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-mutate-custom-interests-response
- name: GoogleAdsGoogleadsV25Services__MutateCustomerAssetSetsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-asset-sets-request
- name: GoogleAdsGoogleadsV25Services__MutateCustomerAssetSetsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-asset-sets-response
- name: GoogleAdsGoogleadsV25Services__MutateCustomerAssetsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-assets-request
- name: GoogleAdsGoogleadsV25Services__MutateCustomerAssetsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-assets-response
- name: GoogleAdsGoogleadsV25Services__MutateCustomerClientLinkRequest
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-client-link-request
- name: GoogleAdsGoogleadsV25Services__MutateCustomerClientLinkResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-client-link-response
- name: GoogleAdsGoogleadsV25Services__MutateCustomerConversionGoalsRequest
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-conversion-goals-request
- name: GoogleAdsGoogleadsV25Services__MutateCustomerConversionGoalsResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-conversion-goals-response
- name: GoogleAdsGoogleadsV25Services__MutateCustomerCustomizersRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-customizers-request
- name: GoogleAdsGoogleadsV25Services__MutateCustomerCustomizersResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-customizers-response
- name: GoogleAdsGoogleadsV25Services__MutateCustomerLabelsRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-labels-request
- name: GoogleAdsGoogleadsV25Services__MutateCustomerLabelsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-labels-response
- name: GoogleAdsGoogleadsV25Services__MutateCustomerManagerLinkRequest
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-manager-link-request
- name: GoogleAdsGoogleadsV25Services__MutateCustomerManagerLinkResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-manager-link-response
- name: GoogleAdsGoogleadsV25Services__MutateCustomerNegativeCriteriaRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-negative-criteria-request
- name: GoogleAdsGoogleadsV25Services__MutateCustomerNegativeCriteriaResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-negative-criteria-response
- name: GoogleAdsGoogleadsV25Services__MutateCustomerSkAdNetworkConversionValueSchemaRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-sk-ad-network-conversion-value-schema-request
- name: GoogleAdsGoogleadsV25Services__MutateCustomerSkAdNetworkConversionValueSchemaResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-sk-ad-network-conversion-value-schema-response
- name: GoogleAdsGoogleadsV25Services__MutateCustomerUserAccessInvitationRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-user-access-invitation-request
- name: GoogleAdsGoogleadsV25Services__MutateCustomerUserAccessInvitationResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-user-access-invitation-response
- name: GoogleAdsGoogleadsV25Services__MutateCustomerUserAccessRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-user-access-request
- name: GoogleAdsGoogleadsV25Services__MutateCustomerUserAccessResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-mutate-customer-user-access-response
- name: GoogleAdsGoogleadsV25Services__MutateCustomizerAttributesRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-customizer-attributes-request
- name: GoogleAdsGoogleadsV25Services__MutateCustomizerAttributesResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-customizer-attributes-response
- name: GoogleAdsGoogleadsV25Services__MutateExperimentArmsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-experiment-arms-request
- name: GoogleAdsGoogleadsV25Services__MutateExperimentArmsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-experiment-arms-response
- name: GoogleAdsGoogleadsV25Services__MutateExperimentsRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-experiments-request
- name: GoogleAdsGoogleadsV25Services__MutateExperimentsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-experiments-response
- name: GoogleAdsGoogleadsV25Services__MutateGoalsRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-goals-request
- name: GoogleAdsGoogleadsV25Services__MutateGoalsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-goals-response
- name: GoogleAdsGoogleadsV25Services__MutateGoogleAdsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-google-ads-request
- name: GoogleAdsGoogleadsV25Services__MutateKeywordPlanAdGroupKeywordsRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-keyword-plan-ad-group-keywords-request
- name: GoogleAdsGoogleadsV25Services__MutateKeywordPlanAdGroupKeywordsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-keyword-plan-ad-group-keywords-response
- name: GoogleAdsGoogleadsV25Services__MutateKeywordPlanAdGroupsRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-keyword-plan-ad-groups-request
- name: GoogleAdsGoogleadsV25Services__MutateKeywordPlanAdGroupsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-keyword-plan-ad-groups-response
- name: GoogleAdsGoogleadsV25Services__MutateKeywordPlanCampaignKeywordsRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-keyword-plan-campaign-keywords-request
- name: GoogleAdsGoogleadsV25Services__MutateKeywordPlanCampaignKeywordsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-keyword-plan-campaign-keywords-response
- name: GoogleAdsGoogleadsV25Services__MutateKeywordPlanCampaignsRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-keyword-plan-campaigns-request
- name: GoogleAdsGoogleadsV25Services__MutateKeywordPlanCampaignsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-keyword-plan-campaigns-response
- name: GoogleAdsGoogleadsV25Services__MutateKeywordPlansRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-keyword-plans-request
- name: GoogleAdsGoogleadsV25Services__MutateKeywordPlansResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-keyword-plans-response
- name: GoogleAdsGoogleadsV25Services__MutateLabelsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-labels-request
- name: GoogleAdsGoogleadsV25Services__MutateLabelsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-labels-response
- name: GoogleAdsGoogleadsV25Services__MutateRecommendationSubscriptionRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-recommendation-subscription-request
- name: GoogleAdsGoogleadsV25Services__MutateRecommendationSubscriptionResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-recommendation-subscription-response
- name: GoogleAdsGoogleadsV25Services__MutateRemarketingActionsRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-remarketing-actions-request
- name: GoogleAdsGoogleadsV25Services__MutateRemarketingActionsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-remarketing-actions-response
- name: GoogleAdsGoogleadsV25Services__MutateSharedCriteriaRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-shared-criteria-request
- name: GoogleAdsGoogleadsV25Services__MutateSharedCriteriaResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-shared-criteria-response
- name: GoogleAdsGoogleadsV25Services__MutateSharedSetsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-shared-sets-request
- name: GoogleAdsGoogleadsV25Services__MutateSharedSetsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-shared-sets-response
- name: GoogleAdsGoogleadsV25Services__MutateSmartCampaignSettingsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-mutate-smart-campaign-settings-request
- name: GoogleAdsGoogleadsV25Services__MutateSmartCampaignSettingsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-smart-campaign-settings-response
- name: GoogleAdsGoogleadsV25Services__MutateUserListCustomerTypesRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-user-list-customer-types-request
- name: GoogleAdsGoogleadsV25Services__MutateUserListCustomerTypesResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-user-list-customer-types-response
- name: GoogleAdsGoogleadsV25Services__MutateUserListsRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-mutate-user-lists-request
- name: GoogleAdsGoogleadsV25Services__MutateUserListsResponse
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-mutate-user-lists-response
- name: GoogleAdsGoogleadsV25Services__PromoteCampaignDraftRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-promote-campaign-draft-request
- name: GoogleAdsGoogleadsV25Services__ProvideLeadFeedbackRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-provide-lead-feedback-request
- name: GoogleAdsGoogleadsV25Services__ProvideLeadFeedbackResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-provide-lead-feedback-response
- name: GoogleAdsGoogleadsV25Services__QuoteCampaignsRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-quote-campaigns-request
- name: GoogleAdsGoogleadsV25Services__QuoteCampaignsResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-quote-campaigns-response
- name: GoogleAdsGoogleadsV25Services__RegenerateShareableLinkIdRequest
  property_count: 0
  slug: google-ads-google-ads-googleads-v25-services-regenerate-shareable-link-id-request
- name: GoogleAdsGoogleadsV25Services__RegenerateShareableLinkIdResponse
  property_count: 0
  slug: google-ads-google-ads-googleads-v25-services-regenerate-shareable-link-id-response
- name: GoogleAdsGoogleadsV25Services__RemoveAutomaticallyCreatedAssetsRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-remove-automatically-created-assets-request
- name: GoogleAdsGoogleadsV25Services__RemoveDataLinkRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-remove-data-link-request
- name: GoogleAdsGoogleadsV25Services__RemoveDataLinkResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-remove-data-link-response
- name: GoogleAdsGoogleadsV25Services__RemoveProductLinkInvitationRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-remove-product-link-invitation-request
- name: GoogleAdsGoogleadsV25Services__RemoveProductLinkInvitationResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-remove-product-link-invitation-response
- name: GoogleAdsGoogleadsV25Services__RemoveProductLinkRequest
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-remove-product-link-request
- name: GoogleAdsGoogleadsV25Services__RemoveProductLinkResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-remove-product-link-response
- name: GoogleAdsGoogleadsV25Services__RemoveYouTubeVideoUploadRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-remove-you-tube-video-upload-request
- name: GoogleAdsGoogleadsV25Services__RemoveYouTubeVideoUploadResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-remove-you-tube-video-upload-response
- name: GoogleAdsGoogleadsV25Services__ResolveMultiPartyAuthReviewRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-resolve-multi-party-auth-review-request
- name: GoogleAdsGoogleadsV25Services__ResolveMultiPartyAuthReviewResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-resolve-multi-party-auth-review-response
- name: GoogleAdsGoogleadsV25Services__RunOfflineUserDataJobRequest
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-run-offline-user-data-job-request
- name: GoogleAdsGoogleadsV25Services__SearchGoogleAdsFieldsRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-search-google-ads-fields-request
- name: GoogleAdsGoogleadsV25Services__SearchGoogleAdsFieldsResponse
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-search-google-ads-fields-response
- name: GoogleAdsGoogleadsV25Services__SearchGoogleAdsResponse
  property_count: 7
  slug: google-ads-google-ads-googleads-v25-services-search-google-ads-response
- name: GoogleAdsGoogleadsV25Services__SuggestGeoTargetConstantsRequest
  property_count: 4
  slug: google-ads-google-ads-googleads-v25-services-suggest-geo-target-constants-request
- name: GoogleAdsGoogleadsV25Services__SuggestGeoTargetConstantsResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-suggest-geo-target-constants-response
- name: GoogleAdsGoogleadsV25Services__SuggestKeywordThemeConstantsRequest
  property_count: 3
  slug: google-ads-google-ads-googleads-v25-services-suggest-keyword-theme-constants-request
- name: GoogleAdsGoogleadsV25Services__SuggestKeywordThemeConstantsResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-suggest-keyword-theme-constants-response
- name: GoogleAdsGoogleadsV25Services__UpdateDataLinkRequest
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-update-data-link-request
- name: GoogleAdsGoogleadsV25Services__UpdateDataLinkResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-update-data-link-response
- name: GoogleAdsGoogleadsV25Services__UpdateProductLinkInvitationRequest
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-update-product-link-invitation-request
- name: GoogleAdsGoogleadsV25Services__UpdateProductLinkInvitationResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-update-product-link-invitation-response
- name: GoogleAdsGoogleadsV25Services__UpdateYouTubeVideoUploadRequest
  property_count: 2
  slug: google-ads-google-ads-googleads-v25-services-update-you-tube-video-upload-request
- name: GoogleAdsGoogleadsV25Services__UpdateYouTubeVideoUploadResponse
  property_count: 1
  slug: google-ads-google-ads-googleads-v25-services-update-you-tube-video-upload-response
- name: GoogleLongrunning__CancelOperationRequest
  property_count: 0
  slug: google-ads-google-longrunning-cancel-operation-request
- name: GoogleLongrunning__ListOperationsResponse
  property_count: 3
  slug: google-ads-google-longrunning-list-operations-response
- name: GoogleLongrunning__Operation
  property_count: 5
  slug: google-ads-google-longrunning-operation
- name: GoogleLongrunning__WaitOperationRequest
  property_count: 1
  slug: google-ads-google-longrunning-wait-operation-request
- name: GoogleProtobuf__Empty
  property_count: 0
  slug: google-ads-google-protobuf-empty
- name: MutateAdGroupAdsRequest
  property_count: 3
  slug: google-ads-mutate-ad-group-ads-request
- name: MutateAdGroupAdsResponse
  property_count: 2
  slug: google-ads-mutate-ad-group-ads-response
- name: MutateAdGroupCriteriaRequest
  property_count: 3
  slug: google-ads-mutate-ad-group-criteria-request
- name: MutateAdGroupCriteriaResponse
  property_count: 2
  slug: google-ads-mutate-ad-group-criteria-response
- name: MutateAdGroupsRequest
  property_count: 3
  slug: google-ads-mutate-ad-groups-request
- name: MutateAdGroupsResponse
  property_count: 2
  slug: google-ads-mutate-ad-groups-response
- name: MutateBiddingStrategiesRequest
  property_count: 3
  slug: google-ads-mutate-bidding-strategies-request
- name: MutateBiddingStrategiesResponse
  property_count: 2
  slug: google-ads-mutate-bidding-strategies-response
- name: MutateCampaignBudgetsRequest
  property_count: 3
  slug: google-ads-mutate-campaign-budgets-request
- name: MutateCampaignBudgetsResponse
  property_count: 2
  slug: google-ads-mutate-campaign-budgets-response
- name: MutateCampaignsRequest
  property_count: 3
  slug: google-ads-mutate-campaigns-request
- name: MutateCampaignsResponse
  property_count: 2
  slug: google-ads-mutate-campaigns-response
- name: SearchGoogleAdsRequest
  property_count: 6
  slug: google-ads-search-google-ads-request
- name: SearchGoogleAdsResponse
  property_count: 5
  slug: google-ads-search-google-ads-response
- name: SearchGoogleAdsStreamRequest
  property_count: 2
  slug: google-ads-search-google-ads-stream-request
- name: SearchGoogleAdsStreamResponse
  property_count: 4
  slug: google-ads-search-google-ads-stream-response
jsonld:
- class_count: 70
  name: Google Ads Context
  property_count: 36
  slug: google-ads-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
- description: Google's first-party Model Context Protocol server for the Google Ads API. It is a Python (FastMCP) server that Google publishes as source and installs from git; Google does not operate a hosted endpo
  name: Google Ads MCP Server
  slug: google-ads-mcp-server
modified: '2026-09-16'
name: Google Ads
nav: Providers
network: true
overview: 'Google Ads publishes 117 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ad Groups API, Bidding Strategies API, and 115 more. Tagged areas include Advertising, Campaign Management, Digital Advertising, Google, and Marketing.


  The Google Ads catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Ads'' developer surface includes authentication, developer portal, getting-started guide, engineering blog, support, Stack Overflow tag, developer console, and 59 more developer resources.'
plans:
- name: Google Ads Plans Pricing
  plan_count: 4
  slug: google-ads-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 8
  name: Google Ads Rate Limits
  slug: google-ads-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Google Ads — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-ads-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 113
  extends:
  - spectral:oas
  name: Google Ads API Rules
  rule_count: 72
  severity_counts:
    error: 56
    hint: 0
    info: 1
    warn: 15
  slug: google-ads-rules
scopes:
- name: Google Ads Scopes
  scope_count: 1
  slug: google-ads-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: exemplar
  composite: 73.1
  coverage:
    artifact_dirs: 40
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 59.2
    contract_governance: 22.0
    contract_quality: 64.4
    developer_ergonomics: 81.5
    discoverability: 71.7
    operational_transparency: 84.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 71.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 116
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/google-ads/google-ads-2026-06-20T182011.png
security:
- kind: authentication
  name: Google Ads Authentication
  slug: google-ads-authentication
  summary_line: oauth2 · 4 schemes
- kind: domain-security
  name: Google Ads Domain Security
  slug: google-ads-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Ads Vulnerability Disclosure
  slug: google-ads-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: google-ads-bulk-mutate-batch-jobs
  slug: google-ads-bulk-mutate-batch-jobs
- name: google-ads-launch-search-campaign
  slug: google-ads-launch-search-campaign
- name: google-ads-plan-keywords
  slug: google-ads-plan-keywords
- name: google-ads-report-performance
  slug: google-ads-report-performance
- name: google-ads-upload-offline-conversions
  slug: google-ads-upload-offline-conversions
slug: google-ads
tags:
- Advertising
- Campaign Management
- Digital Advertising
- Google
- Marketing
- PPC
- Google Ads
- AdTech
website: https://ads.google.com/
---
