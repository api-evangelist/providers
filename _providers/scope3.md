---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 65.8
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 261
  human_in_the_loop: 5
  name: Scope3 Agentic Access
  operation_count: 466
  slug: scope3-agentic-access
  summary_line: 466 operations · 261 acting · 5 human-in-the-loop
api_count: 4
apis:
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The AI Impact Measurement API from Scope3 — 1 operation(s) for ai impact measurement.
  name: Scope3 AI Impact Measurement API
  phrasing_intents:
  - id: calculateImpactBigQuery
    intent: Calculate AI model impact from BigQuery calls
    question: Can I compute AI model energy and emissions impact straight from a BigQuery query?
  phrasing_ops: 1
  slug: scope3-ai-impact-measurement-api
- baseURL: https://api.scope3.com/v2
  baseurl_source: declared
  description: The Benchmarks API from Scope3 — 1 operation(s) for benchmarks.
  name: Scope3 Benchmarks API
  phrasing_intents:
  - id: benchmarks
    intent: Get emissions benchmarks for a country and channel
    question: What are typical advertising emissions percentiles for a country and channel?
  phrasing_ops: 1
  slug: scope3-benchmarks-api
- baseURL: https://api.scope3.com/v2
  baseurl_source: declared
  description: The Creative API from Scope3 — 1 operation(s) for creative.
  name: Scope3 Creative API
  phrasing_intents:
  - id: creative
    intent: Calculate the carbon footprint of a creative
    question: How much carbon does running a particular ad creative produce?
  phrasing_ops: 1
  slug: scope3-creative-api
- baseURL: https://api.scope3.com/v2
  baseurl_source: declared
  description: The Data API from Scope3 — 2 operation(s) for data.
  name: Scope3 Data API
  phrasing_intents:
  - id: postDataUpload
    intent: Upload a data file
    question: Can I upload my own data file and map its columns to the expected fields?
  - id: getDataUploadId
    intent: Check the status of a data file upload
    question: Has the data file I uploaded finished processing?
  phrasing_ops: 2
  slug: scope3-data-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Gpu API from Scope3 — 2 operation(s) for gpu.
  name: Scope3 Gpu API
  phrasing_intents:
  - id: listGPUs
    intent: List GPUs
    question: Which GPUs are available for AI impact calculations?
  - id: createGPU
    intent: Register a custom GPU
    question: How do I add a GPU that isn't in the catalog?
  - id: getGPU
    intent: Get a GPU's specs
    question: What max power and embodied emissions are recorded for a GPU?
  - id: updateGPU
    intent: Update a GPU
    question: Can I correct a GPU's max power figure?
  - id: deleteGPU
    intent: Delete a GPU
    question: Can I remove a custom GPU I added?
  phrasing_ops: 5
  slug: scope3-gpu-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Impact API from Scope3 — 1 operation(s) for impact.
  name: Scope3 Impact API
  phrasing_intents:
  - id: getImpact
    intent: Calculate AI task impact metrics
    question: What is the energy and emissions footprint of my AI inference tasks?
  phrasing_ops: 1
  slug: scope3-impact-api
- baseURL: https://api.scope3.com/v2
  baseurl_source: declared
  description: The Measure API from Scope3 — 1 operation(s) for measure.
  name: Scope3 Measure API
  phrasing_intents:
  - id: measure
    intent: Measure the carbon footprint of ad media delivery
    question: What is the carbon footprint of my media delivery by domain or app?
  phrasing_ops: 1
  slug: scope3-measure-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Model API from Scope3 — 4 operation(s) for model.
  name: Scope3 Model API
  phrasing_intents:
  - id: listModels
    intent: List AI models
    question: Which AI models are available for impact measurement?
  - id: createModel
    intent: Register a custom AI model
    question: How do I add my own fine-tuned model so its footprint can be estimated?
  - id: getModel
    intent: Get an AI model's details
    question: What parameters and training footprint are recorded for a model?
  - id: updateModel
    intent: Update an AI model
    question: Can I correct the parameter count or training energy on a model?
  - id: deleteModel
    intent: Delete an AI model
    question: Can I remove a custom model I registered?
  - id: addModelAlias
    intent: Add an alias to a model
    question: Can a model be known by more than one name?
  - id: removeModelAlias
    intent: Remove an alias from a model
    question: Can I drop an old alias from a model?
  phrasing_ops: 7
  slug: scope3-model-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Node API from Scope3 — 2 operation(s) for node.
  name: Scope3 Node API
  phrasing_intents:
  - id: listNodes
    intent: List compute nodes for AI impact modeling
    question: Which compute nodes are available for AI emissions modeling?
  - id: createNode
    intent: Create a custom compute node
    question: Can I define my own hardware node with a specific GPU and CPU count?
  - id: getNode
    intent: View one compute node
    question: What GPU, CPU and embodied emissions values does a given node use?
  - id: updateNode
    intent: Update a custom compute node
    question: Can I change the utilization rate on a node I defined?
  - id: deleteNode
    intent: Delete a custom compute node
    question: How do I remove a custom node I no longer need?
  phrasing_ops: 5
  slug: scope3-node-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Reload API from Scope3 — 1 operation(s) for reload.
  name: Scope3 Reload API
  phrasing_intents:
  - id: reload
    intent: Reload the AI impact measurement service
    question: Is there a reload endpoint for the AI impact measurement service?
  phrasing_ops: 1
  slug: scope3-reload-api
- baseURL: https://api.scope3.com/v2
  baseurl_source: declared
  description: The Saved Lists API from Scope3 — 1 operation(s) for saved lists.
  name: Scope3 Saved Lists API
  phrasing_intents:
  - id: getSavedLists
    intent: List my saved property lists
    question: Which saved property lists do I have, and how many domains are in each?
  phrasing_ops: 1
  slug: scope3-saved-lists-api
- baseURL: https://api.scope3.com/v2
  baseurl_source: declared
  description: The Segment API from Scope3 — 2 operation(s) for segment.
  name: Scope3 Segment API
  phrasing_intents:
  - id: getOrganizationSegmentList
    intent: List my organization's segments
    question: Which audience segments does my organization have?
  - id: getOrganizationSegmentDataBySegmentId
    intent: Get the data behind one segment
    question: What data is stored in a particular segment of mine?
  phrasing_ops: 2
  slug: scope3-segment-api
- baseURL: https://api.scope3.com/v2
  baseurl_source: declared
  description: The Signals API from Scope3 — 1 operation(s) for signals.
  name: Scope3 Signals API
  phrasing_intents:
  - id: getSignalsBySavedList
    intent: Get media quality signals for a saved domain list
    question: What are the media quality scores for every domain in one of my saved lists?
  - id: createSignal
    intent: Register a new signal
    question: What do I need to register a new targeting signal?
  - id: listSignals
    intent: List my registered signals
    question: Which targeting signals have I registered, and which are live?
  - id: getSignal
    intent: View one registered signal and its access
    question: Who has access to a particular signal I registered?
  - id: updateSignal
    intent: Update a registered signal
    question: Can I change a signal's key type or regions after I create it?
  - id: deleteSignal
    intent: Archive a registered signal
    question: What happens to a signal's access records when I delete it?
  - id: discoverSignals
    intent: Discover available signals from signal agents
    question: What audience signals are available from signal agents for my targeting?
  phrasing_ops: 7
  slug: scope3-signals-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Status API from Scope3 — 1 operation(s) for status.
  name: Scope3 Status API
  phrasing_intents:
  - id: status
    intent: Check that the service is up
    question: Is the Scope3 service up right now?
  phrasing_ops: 1
  slug: scope3-status-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: Account management, service tokens, and preferences
  name: Scope3 Account API
  phrasing_intents:
  - id: getCurrentAccount
    intent: Get my current account
    question: Which customer account am I currently working in?
  - id: listCustomerAccounts
    intent: List accounts I belong to
    question: Which customer accounts do I have membership on?
  - id: createChildAccount
    intent: Create a child account
    question: How do I create a child account under my organization?
  - id: updateCustomerDomain
    intent: Update an organization's domain
    question: Can I change the registered organization domain for a customer?
  - id: deleteChildAccount
    intent: Delete a child account
    question: Can I permanently delete a child customer account?
  - id: getMembershipSettings
    intent: Get an org's membership settings
    question: Is domain auto-join turned on for my organization?
  - id: updateMembershipSettings
    intent: Turn domain auto-join on or off
    question: How do I let people with my company email join automatically?
  - id: listBrowserOrigins
    intent: List allowed browser origins
    question: Which browser origins can call the MCP and OAuth endpoints for my account?
  phrasing_ops: 18
  slug: scope3-account-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Activity API from Scope3 — 2 operation(s) for activity.
  name: Scope3 Activity API
  phrasing_intents:
  - id: listActivityCalls
    intent: List my API call activity
    question: Which API calls did my integration make and which ones failed?
  - id: getActivityCall
    intent: Get one API call's detail
    question: What timing and diagnostics were captured for a specific API call?
  phrasing_ops: 2
  slug: scope3-activity-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: Manage advertisers
  name: Scope3 Advertisers API
  phrasing_intents:
  - id: listAdvertisers
    intent: List advertisers
    question: Which advertisers do I have set up in Scope3?
  - id: createAdvertiser
    intent: Create an advertiser
    question: How do I set up a new advertiser before creating campaigns?
  - id: listAllAdvertisersHome
    intent: Get the all-advertisers landing overview
    question: Can I get a portfolio summary across all my advertisers with campaign counts?
  - id: getAdvertiser
    intent: Get an advertiser's details
    question: What brand details and ADCP manifest are stored for one of my advertisers?
  - id: updateAdvertiser
    intent: Update an advertiser
    question: Can I change an existing advertiser's frequency caps or UTM settings?
  - id: deleteAdvertiser
    intent: Archive an advertiser
    question: What happens when I delete an advertiser, is it archived?
  - id: restoreAdvertiser
    intent: Restore an archived advertiser
    question: Can I bring back an advertiser I archived by mistake?
  - id: revalidateDataDeliveryCredential
    intent: Revalidate a data delivery credential
    question: After fixing bucket access, how do I re-test my data delivery destination?
  phrasing_ops: 22
  slug: scope3-advertisers-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: Storefront AI token usage visibility by model
  name: Scope3 AI Usage API
  phrasing_intents:
  - id: getStorefrontAiUsageByModel
    intent: Get daily AI token usage by model
    question: How has my storefront's AI token usage trended day by day?
  - id: getStorefrontAiUsageSummary
    intent: Summarize AI token usage by model
    question: What is my total storefront AI token usage per model?
  phrasing_ops: 2
  slug: scope3-ai-usage-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: What you are waiting on Scope3 for — support, product, and supply asks in one list
  name: Scope3 Asks API
  phrasing_intents:
  - id: listAsks
    intent: List everything I am waiting on Scope3 for
    question: What am I still waiting on Scope3 to deliver for my account?
  phrasing_ops: 1
  slug: scope3-asks-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Audit Logs API from Scope3 — 1 operation(s) for audit logs.
  name: Scope3 Audit Logs API
  phrasing_intents:
  - id: listBuyerAuditLogs
    intent: List buyer audit log entries
    question: Who changed my campaign and when?
  phrasing_ops: 1
  slug: scope3-audit-logs-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Brands API from Scope3 — 1 operation(s) for brands.
  name: Scope3 Brands API
  phrasing_intents:
  - id: resolveBuyerBrand
    intent: Resolve a domain to a brand profile
    question: What brand profile does the platform see for my company's domain?
  phrasing_ops: 1
  slug: scope3-brands-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: Consolidated invoicing for buyers — invoices and pending invoice items issued by Scope3 across the buyer customer.
  name: Scope3 Buyer Billing API
  phrasing_intents:
  - id: getBillingInfo
    intent: View invoice billing details
    question: Which contact, address and tax ID do my invoices go to?
  - id: updateBillingInfo
    intent: Update invoice billing details
    question: What's the minimum billing information needed before an invoice can be issued?
  - id: getBillingAccount
    intent: View my organization's commercial account summary
    question: What plan, pricing and credit balance is my organization on?
  - id: getIuRateCardOffer
    intent: View the IU rate card offer
    question: What IU plan is my organization being offered and has it been accepted?
  - id: getIuRateCardOfferV2
    intent: View the versioned enterprise IU offer document
    question: Where do I find the full enterprise IU proposal with payment options and support terms?
  - id: downloadIuRateCardCommercialOfferDocument
    intent: Download the Commercial Offer PDF
    question: Can I download our Commercial Offer proposal as a PDF?
  - id: acceptIuRateCardOffer
    intent: Accept an IU rate card plan
    question: How does an org admin accept the IU plan we were offered?
  - id: setupPaymentMethod
    intent: Start adding a payment card
    question: How do I add a credit card for my organization to pay with?
  phrasing_ops: 15
  slug: scope3-buyer-billing-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: Manage advertising campaigns
  name: Scope3 Campaigns API
  phrasing_intents:
  - id: listCampaigns
    intent: List campaigns
    question: Which campaigns are running for a particular advertiser?
  - id: createCampaign
    intent: Create a campaign
    question: How do I start a new ad campaign?
  - id: updateCampaign
    intent: Update a campaign
    question: Can I edit a campaign's name or brief after creating it?
  - id: getCampaign
    intent: Get a campaign's details
    question: Can I see the full detail of one campaign including its property lists?
  - id: deleteCampaign
    intent: Delete a campaign
    question: Can I delete a campaign I no longer need?
  - id: getDirectedCampaignDelivery
    intent: Get live campaign delivery
    question: How is my tracked campaign actually delivering right now?
  - id: executeCampaign
    intent: Launch a campaign
    question: How do I launch a campaign so it starts delivering ads?
  - id: pauseCampaign
    intent: Pause a campaign
    question: Does pausing a campaign also pause all of its media buys?
  phrasing_ops: 21
  slug: scope3-campaigns-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: Build, manage, and sync campaign creatives via AdCP Creative Protocol
  name: Scope3 Creatives API
  phrasing_intents:
  - id: listCreativeModelCredentials
    intent: List generation-provider keys for an advertiser
    question: Which of my own AI generation keys can be used for a given advertiser?
  - id: connectCreativeModelCredential
    intent: Connect my own generation-provider key
    question: Can creative generation run on my own model provider account?
  - id: updateCreativeModelCredential
    intent: Rotate or edit a generation-provider key
    question: How do I rotate a generation key without losing its label and assignments?
  - id: getCreativeDashboardUrl
    intent: Get a link to the creative dashboard
    question: Can I get a direct link into the creative dashboard for a campaign?
  - id: createCreativeManifest
    intent: Create a creative in a campaign
    question: How do I upload a new creative with its files to a campaign?
  - id: listCreativeTemplates
    intent: List creative templates and required formats
    question: What creative templates and formats do my campaign's products require?
  - id: listCreativeManifests
    intent: Filter a campaign's creatives by role, source or format
    question: Can I filter a campaign's creatives by format kind, asset type or dimensions?
  - id: listCreatives
    intent: List a campaign's creatives
    question: What creatives are in my campaign right now?
  phrasing_ops: 39
  slug: scope3-creatives-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: Manage event source configurations and log conversion/marketing events for attribution
  name: Scope3 Event Sources API
  phrasing_intents:
  - id: listEventSources
    intent: List an advertiser's conversion event sources
    question: Which conversion data pipelines are set up for an advertiser?
  - id: syncEventSources
    intent: Sync event source configurations to an advertiser
    question: How do I push my event source configuration to an advertiser?
  - id: logEvent
    intent: Log conversion events for an advertiser
    question: How many conversion events can I send in a single call?
  phrasing_ops: 3
  slug: scope3-event-sources-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: Model Context Protocol endpoints for AI agents
  name: Scope3 MCP API
  phrasing_intents:
  - id: mcpInitialize
    intent: Start an MCP session with the buyer API
    question: What has to happen before an agent can use the Scope3 buyer MCP tools?
  - id: mcpApiCall
    intent: Call a buyer REST endpoint through MCP
    question: Can an agent reach any buyer REST endpoint through the MCP api_call tool?
  - id: mcpAskAboutCapability
    intent: Ask a plain-language question about API features
    question: Can I ask the buyer API in plain English what it is able to do?
  phrasing_ops: 3
  slug: scope3-mcp-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: Measurement sources, records, context, and freshness
  name: Scope3 Measurement API
  phrasing_intents:
  - id: syncMeasurementData
    intent: Sync performance measurement data
    question: Can I send campaign performance data directly instead of using a conversions API?
  - id: listTestCohorts
    intent: List an advertiser's test cohorts
    question: Which test cohorts exist for my advertiser?
  - id: createTestCohort
    intent: Create a measurement test cohort
    question: How do I set up a test cohort for incrementality measurement?
  - id: getTestCohort
    intent: Get a test cohort
    question: Can I see the definition of one test cohort?
  - id: updateTestCohort
    intent: Update a test cohort
    question: Can I change a test cohort's definition after creating it?
  - id: deleteTestCohort
    intent: Delete a test cohort
    question: Can I remove a test cohort I no longer use?
  - id: getMeasurementConfig
    intent: Get an advertiser's measurement settings
    question: Is media mix modeling or brand lift enabled for my advertiser?
  - id: updateMeasurementConfig
    intent: Update an advertiser's measurement settings
    question: How do I turn on brand lift measurement for an advertiser?
  phrasing_ops: 16
  slug: scope3-measurement-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Media Billing API from Scope3 — 5 operation(s) for media billing.
  name: Scope3 Media Billing API
  phrasing_intents:
  - id: listMediaBillingEntities
    intent: List media billing entities
    question: Which legal entities does Scope3 invoice for our media spend?
  - id: createMediaBillingEntity
    intent: Create a media billing entity
    question: How do I add a new legal entity to be invoiced for media?
  - id: updateMediaBillingEntity
    intent: Update a media billing entity
    question: Can I change the billing emails or address on an existing entity?
  - id: deleteMediaBillingEntity
    intent: Delete a media billing entity
    question: Why can't I delete a billing entity that still has attachments?
  - id: listMediaBillingAttachments
    intent: List media billing attachments
    question: Which advertisers and accounts are attached to which billing entity?
  - id: createMediaBillingAttachment
    intent: Attach a billing entity to an advertiser or account
    question: How do I bill one advertiser to a different legal entity?
  - id: deleteMediaBillingAttachment
    intent: Remove a media billing attachment
    question: Can I detach an advertiser from its billing entity?
  - id: resolveMediaBillingEntity
    intent: Find who gets invoiced for an advertiser
    question: Which legal entity will be invoiced for this advertiser's media?
  phrasing_ops: 8
  slug: scope3-media-billing-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Moderation API from Scope3 — 1 operation(s) for moderation.
  name: Scope3 Moderation API
  phrasing_intents:
  - id: checkModeration
    intent: Pre-check text against moderation policy
    question: Will my campaign brief pass content moderation before I submit it?
  phrasing_ops: 1
  slug: scope3-moderation-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Notifications API from Scope3 — 4 operation(s) for notifications.
  name: Scope3 Notifications API
  phrasing_intents:
  - id: listNotifications
    intent: List my notifications
    question: Do I have any unread notifications about my campaigns?
  - id: readAllNotifications
    intent: Mark all notifications as read
    question: Can I clear all my unread notifications at once?
  - id: readNotification
    intent: Mark one notification as read
    question: How do I mark a single notification as read?
  - id: acknowledgeNotification
    intent: Acknowledge and dismiss a notification
    question: What's the difference between reading and acknowledging a notification?
  phrasing_ops: 4
  slug: scope3-notifications-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Optimization Suggestions API from Scope3 — 4 operation(s) for optimization suggestions.
  name: Scope3 Optimization Suggestions API
  phrasing_intents:
  - id: listOptimizationSuggestions
    intent: List optimization suggestions
    question: What optimization suggestions are waiting for my review?
  - id: getOptimizationSuggestion
    intent: View one optimization suggestion
    question: What exactly would a given optimization suggestion change?
  - id: approveOptimizationSuggestion
    intent: Approve an optimization suggestion
    question: How do I accept a recommended optimization so it gets applied?
  - id: rejectOptimizationSuggestion
    intent: Reject an optimization suggestion
    question: Can I decline a recommended optimization and say why?
  phrasing_ops: 4
  slug: scope3-optimization-suggestions-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: Discover and select products
  name: Scope3 Product Discovery API
  phrasing_intents:
  - id: getMarketplaceProducts
    intent: Query products across connected storefronts
    question: Can I send one product request to all my connected storefronts at once?
  - id: createMediaBuysBatch
    intent: Stage products from a multi-storefront query on a campaign
    question: After querying several storefronts, how do I put the chosen products into a draft campaign cart?
  - id: discoverProducts
    intent: Start a product discovery session for an advertiser
    question: How do I find ad products that fit my campaign brief and budget?
  - id: browseProducts
    intent: Browse products in an existing discovery session
    question: Can I page through more publishers in a discovery session I already started?
  - id: getProductDetails
    intent: View full details of a discovered product
    question: What pricing, delivery windows and creative formats does a discovered product require?
  - id: getProducts
    intent: List products selected in a discovery session
    question: Which products have I picked so far in a discovery session?
  - id: addProducts
    intent: Add discovered products to my selection
    question: How do I add a discovered product to my selection?
  - id: removeProducts
    intent: Remove products from my selection
    question: Can I drop a product I selected by mistake in a discovery session?
  phrasing_ops: 9
  slug: scope3-product-discovery-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Products API from Scope3 — 1 operation(s) for products.
  name: Scope3 Products API
  phrasing_intents:
  - id: listStorefrontOwnProducts
    intent: List my storefront products eligible for media buys
    question: Which of my storefront's products can a pending media buy be approved against?
  phrasing_ops: 1
  slug: scope3-products-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: Validate property lists against AAO registry
  name: Scope3 Property Lists API
  phrasing_intents:
  - id: listPropertyLists
    intent: List an advertiser's property lists
    question: Which include and exclude domain lists does my advertiser have?
  - id: createPropertyList
    intent: Create an include or exclude domain list
    question: How do I build a blocklist of publisher domains for an advertiser?
  - id: getPropertyList
    intent: Get a property list
    question: Which domains are on one of my property lists?
  - id: updatePropertyList
    intent: Rename or replace domains on a property list
    question: Can I replace all the domains on an existing property list?
  - id: deletePropertyList
    intent: Archive a property list
    question: Does deleting a property list unlink it from targeting?
  - id: getCampaignPropertyLists
    intent: See which property lists apply to a campaign
    question: Which domain lists constrain where my campaign can deliver?
  - id: attachPropertyListToCampaign
    intent: Push an include list to a running campaign
    question: Can I apply a new include list to media buys that are already running?
  - id: checkPropertyList
    intent: Check domains against the community registry
    question: Which of my domains should be removed or reviewed according to the registry?
  phrasing_ops: 9
  slug: scope3-property-lists-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Release Updates API from Scope3 — 2 operation(s) for release updates.
  name: Scope3 Release Updates API
  phrasing_intents:
  - id: listReleaseUpdates
    intent: List release updates for me
    question: What's new in the platform that affects my account?
  - id: markReleaseUpdatesSeen
    intent: Mark release updates as seen
    question: Can I mark all the release notes I've read as seen?
  phrasing_ops: 2
  slug: scope3-release-updates-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: Access performance metrics
  name: Scope3 Reporting API
  phrasing_intents:
  - id: getEventSummary
    intent: Get hourly event counts for an advertiser
    question: How many events of each type did my advertiser record per hour?
  - id: getReportingMetrics
    intent: Get campaign reporting metrics
    question: What did my campaigns spend and deliver over the last 30 days?
  - id: getStorefrontMarginReporting
    intent: Get storefront resale margin P&L
    question: What margin am I making reselling inventory through my storefront?
  phrasing_ops: 3
  slug: scope3-reporting-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: Request reviewed access to Interchange
  name: Scope3 Signup API
  phrasing_intents:
  - id: submitBuyerSignupIntake
    intent: Request buyer access
    question: Can I apply for buyer access to the platform?
  phrasing_ops: 1
  slug: scope3-signup-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: Audit log of configuration and inventory changes on the storefront
  name: Scope3 Storefront Activity API
  phrasing_intents:
  - id: listStorefrontAuditLogs
    intent: List storefront configuration changes
    question: What changed on my storefront recently and who changed it?
  phrasing_ops: 1
  slug: scope3-storefront-activity-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Storefront Ad Server Buyer Routing API from Scope3 — 12 operation(s) for storefront ad server buyer routing.
  name: Scope3 Storefront Ad Server Buyer Routing API
  phrasing_intents:
  - id: getEsaSandboxAccountStatus
    intent: Check ad server sandbox account readiness
    question: Is the sandbox advertiser account ready for no-spend tests on my ad server source?
  - id: ensureEsaSandboxAccount
    intent: Create or repair the ad server sandbox account
    question: How do I make sure a sandbox advertiser account exists for no-spend testing?
  - id: listEsaAdapterAdvertisers
    intent: List ad server advertisers for any adapter
    question: Which advertisers exist in my connected ad server, whatever platform it is?
  - id: listEsaGamAdvertisers
    intent: List cached Google Ad Manager advertisers
    question: Which Google Ad Manager advertisers are cached for my source?
  - id: ensureEsaGamAdvertiser
    intent: Find or create a GAM advertiser by name
    question: How do I create a Google Ad Manager advertiser to route buyers to?
  - id: setEsaDefaultAdvertiser
    intent: Set the catch-all advertiser for any ad server
    question: Where do unmatched buyers get routed in my ad server?
  - id: setEsaDefaultGamAdvertiser
    intent: Set the default GAM advertiser
    question: Can I set the Google Ad Manager-specific default advertiser for buyer routing?
  - id: ensureEsaGamCustomTargetingKeys
    intent: Create GAM custom-targeting keys
    question: How do I add custom-targeting keys in Google Ad Manager through my source?
  phrasing_ops: 14
  slug: scope3-storefront-ad-server-buyer-routing-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Storefront Ad Server Catalog API from Scope3 — 11 operation(s) for storefront ad server catalog.
  name: Scope3 Storefront Ad Server Catalog API
  phrasing_intents:
  - id: createEsaProduct
    intent: Create a wholesale product on an ad server source
    question: How do I add a new wholesale product to my ad server?
  - id: listEsaProducts
    intent: List wholesale products on an ad server source
    question: Which wholesale products are defined on my ad server source?
  - id: validateEsaProduct
    intent: Validate a product draft without saving it
    question: Can I check a product definition for errors before creating it on the ad server?
  - id: getEsaProduct
    intent: View one wholesale product on an ad server source
    question: What's configured on a specific wholesale product in my ad server?
  - id: updateEsaProduct
    intent: Replace a wholesale product's full definition
    question: Does editing a product on the ad server require sending the complete definition?
  - id: patchEsaProduct
    intent: Change only some fields of a wholesale product
    question: Can I change just a product's name or status without resending everything?
  - id: deleteEsaProduct
    intent: Delete a wholesale product from an ad server source
    question: How do I remove a wholesale product from my ad server?
  - id: listEsaSignals
    intent: List targeting signals on an ad server source
    question: Which named targeting definitions have I authored for an ad server source?
  phrasing_ops: 18
  slug: scope3-storefront-ad-server-catalog-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Storefront Ad Server Diagnostics API from Scope3 — 2 operation(s) for storefront ad server diagnostics.
  name: Scope3 Storefront Ad Server Diagnostics API
  phrasing_intents:
  - id: listEsaMediaBuys
    intent: List upstream media buys on an ad server source
    question: Which media buys has my ad server source actually received?
  - id: getEsaMediaBuy
    intent: Get an upstream media buy on an ad server source
    question: What status history and delivery snapshot does an upstream media buy have?
  phrasing_ops: 2
  slug: scope3-storefront-ad-server-diagnostics-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: List and manage registered sales, signals, and outcomes agents
  name: Scope3 Storefront Agents API
  phrasing_intents:
  - id: listStorefrontAgents
    intent: List agents registered to my storefront
    question: Which sales, signals and outcomes agents are registered to my storefront?
  - id: getStorefrontAgent
    intent: Get a registered agent's details
    question: What capabilities and account counts does a registered agent have?
  - id: startAgentOAuth
    intent: Start agent-level OAuth setup
    question: How do I authorize the platform to call an agent with OAuth?
  - id: startAgentAccountOAuth
    intent: Start per-account agent OAuth
    question: Can I authorize an agent separately for each buyer account?
  - id: refreshStorefrontAgentCapabilities
    intent: Refresh an agent's capabilities
    question: How do I pick up new tools or formats an agent added?
  phrasing_ops: 5
  slug: scope3-storefront-agents-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: Manage storefront and inventory sources
  name: Scope3 Storefront API
  phrasing_intents:
  - id: getSellerAccountMappingSummary
    intent: Summarize seller account mapping coverage
    question: How many buyer relationships do I have mapped across my active inventory sources?
  - id: listSellerAccountRelationships
    intent: List seller account relationships
    question: Which operator and brand relationships does my storefront own?
  - id: exportSellerAccountMappings
    intent: Export seller account mappings as CSV
    question: Can I download my current account mappings and the mapping template as CSV?
  - id: listSellerAccountGrantReviews
    intent: List pending buyer account requests
    question: Which buyer account requests are waiting for me to approve or reject?
  - id: decideSellerAccountGrantReview
    intent: Approve or reject a buyer account request
    question: Can I reject a buyer's account request, and do I have to give a reason?
  - id: refreshSellerAccountSourceAccounts
    intent: Refresh advertiser choices for an ad-server source
    question: Can I reload the advertiser list from my Google Ad Manager or FreeWheel source for account mapping?
  - id: prepareSellerAccountBindingFeed
    intent: Prepare an account mapping feed upload
    question: How do I get a signed upload URL for my source_account_bindings.csv file?
  - id: previewSellerAccountBindingFeed
    intent: Validate and preview an account mapping feed
    question: Can I see which rows of my uploaded account mapping file are invalid before applying it?
  phrasing_ops: 159
  slug: scope3-storefront-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: Payout bank details and billing configuration for storefronts
  name: Scope3 Storefront Billing API
  phrasing_intents:
  - id: getStorefrontRateCardOffer
    intent: View the storefront rate card offer
    question: What paid storefront plans am I being offered and at what net price?
  - id: acceptStorefrontRateCardOffer
    intent: Accept a storefront rate card plan
    question: How do I accept a paid storefront plan from the rate card?
  - id: getPayoutActivity
    intent: View storefront payout activity
    question: Have any payouts been paid to my storefront yet?
  - id: getStorefrontBilling
    intent: View storefront billing configuration
    question: What platform fee and payment terms apply to my storefront?
  - id: updateStorefrontBilling
    intent: Change storefront fees, currency or net days
    question: Can I change the platform fee percentage on my storefront?
  - id: setPayoutDetails
    intent: Set the default payout bank account
    question: Where do I enter the bank account my storefront gets paid out to?
  - id: listPayoutPayees
    intent: List payout payees by legal entity
    question: Which legal entities have payout bank accounts on file?
  - id: setPayoutPayee
    intent: Add or update a payee for one legal entity
    question: Can I pay out different legal entities to different bank accounts?
  phrasing_ops: 9
  slug: scope3-storefront-billing-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Storefront Proposals API from Scope3 — 3 operation(s) for storefront proposals.
  name: Scope3 Storefront Proposals API
  phrasing_intents:
  - id: createStorefrontProposal
    intent: Create a shareable proposal code for a buyer
    question: Can I package discovered products into a code a buyer can redeem?
  - id: listStorefrontProposals
    intent: List my storefront proposals
    question: Which proposals has my storefront shared with buyers?
  - id: getStorefrontProposal
    intent: View a storefront proposal
    question: What products did I include in a proposal I sent a buyer?
  - id: updateStorefrontProposal
    intent: Change a proposal's label, notes or expiry
    question: Can I extend the expiry date on a proposal I already shared?
  - id: revokeStorefrontProposal
    intent: Revoke a storefront proposal
    question: How do I stop a buyer from redeeming a proposal code?
  phrasing_ops: 5
  slug: scope3-storefront-proposals-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Storefronts API from Scope3 — 18 operation(s) for storefronts.
  name: Scope3 Storefronts API
  phrasing_intents:
  - id: listStorefronts
    intent: List storefronts I can buy from
    question: Which storefronts are available for me to buy media from?
  - id: getStorefront
    intent: View a storefront and my connection status
    question: Am I connected to a particular storefront?
  - id: getStorefrontCapabilities
    intent: Diagnose a storefront's source capabilities
    question: What can each inventory source in a storefront actually do?
  - id: listStorefrontConnections
    intent: List my storefront connections and sharing settings
    question: Which storefronts have I connected and are buying, events and feeds turned on?
  - id: listStorefrontConnectionAccountMappings
    intent: List external accounts and their advertiser mappings
    question: Which external ad accounts are mapped to which of my advertisers across integrations?
  - id: listStorefrontConnectionAccounts
    intent: List external accounts found on one connection
    question: What external accounts were discovered on a specific integration connection?
  - id: removeStorefrontConnection
    intent: Disconnect from an adapter storefront
    question: How do I disconnect an integration to an adapter storefront?
  - id: selectStorefrontConnectionAccount
    intent: Choose which external account a connection uses
    question: My connection found several ad accounts — how do I pick the one to use?
  phrasing_ops: 19
  slug: scope3-storefronts-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Supply Requests API from Scope3 — 3 operation(s) for supply requests.
  name: Scope3 Supply Requests API
  phrasing_intents:
  - id: suggestSupplyRequests
    intent: Search publisher domains to request as supply
    question: Which seller or publisher domains match a name I want to request?
  - id: listSupplyRequests
    intent: List my requested supply
    question: Which publishers have we already asked to be added as supply?
  - id: requestSupply
    intent: Request a new supply source
    question: How do I ask for a publisher I want to buy from to be added?
  - id: removeSupplyRequest
    intent: Withdraw a supply request
    question: Can I take back a supply request I filed?
  phrasing_ops: 4
  slug: scope3-supply-requests-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: Syndicate resources to ADCP agents
  name: Scope3 Syndication API
  phrasing_intents:
  - id: syndicate
    intent: Turn syndication on or off for an audience or catalog
    question: Can I share an audience, event source or catalog with a specific AdCP agent?
  - id: getSyndicationStatus
    intent: See what an advertiser is syndicating
    question: Which of my audiences and catalogs are currently syndicated to agents?
  phrasing_ops: 2
  slug: scope3-syndication-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: Track async operation status
  name: Scope3 Tasks API
  phrasing_intents:
  - id: getTask
    intent: Check the status of an async task
    question: How can I tell whether a long-running buyer task has finished?
  phrasing_ops: 1
  slug: scope3-tasks-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Update Proposals API from Scope3 — 1 operation(s) for update proposals.
  name: Scope3 Update Proposals API
  phrasing_intents:
  - id: getUpdateProposal
    intent: Check a media buy update proposal
    question: Has the seller approved or rejected my media buy change yet?
  - id: cancelUpdateProposal
    intent: Cancel a pending update proposal
    question: Can I withdraw a media buy change that's still pending?
  phrasing_ops: 2
  slug: scope3-update-proposals-api
- baseURL: https://aiapi.scope3.com
  baseurl_source: declared
  description: The Webhook Subscriptions API from Scope3 — 2 operation(s) for webhook subscriptions.
  name: Scope3 Webhook Subscriptions API
  phrasing_intents:
  - id: createWebhookSubscription
    intent: Register a webhook for push events
    question: Can I get progressive discovery updates pushed to my server instead of polling?
  - id: listWebhookSubscriptions
    intent: List my webhook subscriptions
    question: Which webhook endpoints have I registered for push events?
  - id: deleteWebhookSubscription
    intent: Delete a webhook subscription
    question: How do I stop webhook deliveries to an endpoint I no longer use?
  phrasing_ops: 3
  slug: scope3-webhook-subscriptions-api
artifact_total: 74
asyncapis:
- description: ''
  name: Scope3 Webhooks
  slug: scope3-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AI Impact Measurement API
  slug: open-scope3-ai-impact-measurement-api
- collection_type: open
  name: AI Impact Measurement Benchmarks API
  slug: open-scope3-benchmarks-api
- collection_type: open
  name: AI Impact Measurement Creative API
  slug: open-scope3-creative-api
- collection_type: open
  name: AI Impact Measurement Data API
  slug: open-scope3-data-api
- collection_type: open
  name: AI Impact Measurement Gpu API
  slug: open-scope3-gpu-api
- collection_type: open
  name: AI Measurement Impact API
  slug: open-scope3-impact-api
- collection_type: open
  name: AI Impact Measurement Measure API
  slug: open-scope3-measure-api
- collection_type: open
  name: AI Impact Measurement Model API
  slug: open-scope3-model-api
- collection_type: open
  name: AI Impact Measurement Node API
  slug: open-scope3-node-api
- collection_type: open
  name: AI Impact Measurement Reload API
  slug: open-scope3-reload-api
- collection_type: open
  name: AI Impact Measurement Saved Lists API
  slug: open-scope3-saved-lists-api
- collection_type: open
  name: AI Impact Measurement Segment API
  slug: open-scope3-segment-api
- collection_type: open
  name: AI Impact Measurement Signals API
  slug: open-scope3-signals-api
- collection_type: open
  name: AI Impact Measurement Status API
  slug: open-scope3-status-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/capabilities/scope3-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/scope3-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/overlays/scope3-buyer-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/scope3-buyer-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/skills/scope3-agentic-buyer.md
  title: ''
  type: AgentSkill
  url: skills/scope3-agentic-buyer.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/overlays/scope3-storefront-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/scope3-storefront-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/skills/scope3-agentic-storefront.md
  title: ''
  type: AgentSkill
  url: skills/scope3-agentic-storefront.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/overlays/scope3-ai-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/scope3-ai-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/a2a/scope3-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/scope3-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/well-known/scope3-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/scope3-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/mcp/scope3-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/scope3-tool-crosswalk.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/conventions/scope3-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/scope3-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/scopes/scope3-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/scope3-scopes.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/plans/scope3-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/scope3-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/rate-limits/scope3-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/scope3-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/agentic-access/scope3-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/scope3-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/security/scope3-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scope3-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/authentication/scope3-authentication.yml
  title: ''
  type: Authentication
  url: authentication/scope3-authentication.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/packages/scope3-packages.yml
  title: ''
  type: Packages
  url: packages/scope3-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/packages/scope3-packages.yml
  title: ''
  type: SDKs
  url: packages/scope3-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/cli/scope3-cli.yml
  title: ''
  type: CLI
  url: cli/scope3-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/mcp/scope3-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/scope3-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/llms/scope3-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scope3-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/errors/scope3-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/scope3-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/conventions/scope3-conventions.yml
  title: ''
  type: Conventions
  url: conventions/scope3-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/lifecycle/scope3-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/scope3-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/lifecycle/scope3-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/scope3-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/changelog/scope3-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/scope3-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/conformance/scope3-conformance.yml
  title: ''
  type: Conformance
  url: conformance/scope3-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/data-model/scope3-data-model.yml
  title: ''
  type: DataModel
  url: data-model/scope3-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/sandbox/scope3-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/scope3-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/asyncapi/scope3-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/scope3-webhooks.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.scope3.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.scope3.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://docs.scope3.com/reference/measure-1
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.scope3.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://scope3.com/support
- group: company
  title: ''
  type: Blog
  url: https://scope3.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scope3data
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.interchange.io/v2/buyer/billing/how-iu-billing-works
- group: start
  title: ''
  type: SignUp
  url: https://interchange.io/signup
- group: start
  title: ''
  type: Login
  url: https://interchange.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://scope3.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://scope3.com/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://scope3.com
- group: other
  title: ''
  type: Interchange
  url: https://interchange.io
created: '2026-07-17'
description: 'Scope3 is the source of truth for greenhouse-gas emissions data in media and advertising, and operates Scope3 Interchange, an agentic advertising platform where buyer agents and seller storefronts transact on the open Ad Context Protocol (AdCP). Its APIs let buyers, publishers and platforms measure the carbon footprint of every ad impression and creative across channels, benchmark against country/channel percentiles, and run AI-driven programmatic advertising end to end. Scope3 publishes four OpenAPI documents across three surfaces: the Carbon Calculator (Measurement) API at api.scope3.com/v2, the AI Impact Measurement API at aiapi.scope3.com (energy, gCO2e and water per inference), and the Interchange Buyer and Storefront v2 APIs at api.interchange.io with 481 operations between them. Interchange is built for AI agents as primary callers: hosted remote MCP endpoints with OAuth (RFC 8414 metadata, dynamic client registration, PKCE), an A2A agent card, three published Agent
  Skills, a documented error envelope, IETF draft-7 rate-limit headers and a published IU pricing model. Backed by GV.'
image: https://scope3.com/og-default.png
layout: provider
mcp_servers:
- description: ''
  name: Scope3 MCP Server
  slug: scope3-mcp-server
modified: '2026-08-13'
name: Scope3
nav: Providers
network: true
overview: 'Scope3 publishes 51 APIs on the [APIs.io](https://apis.io/) network, including AI Impact Measurement API, Benchmarks API, Creative API, and 48 more. Tagged areas include Company, Enterprise, Advertising, Carbon Emissions, and Sustainability.


  The Scope3 catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Scope3''s developer surface includes authentication, CLI, changelog, sandbox, documentation, API reference, getting-started guide, and 38 more developer resources.'
plans:
- name: Scope3 Plans Pricing
  plan_count: 3
  slug: scope3-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 4
  name: Scope3 Rate Limits
  slug: scope3-rate-limits
scopes:
- name: Scope3 Scopes
  scope_count: 4
  slug: scope3-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: exemplar
  composite: 66.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 69.7
    contract_governance: 18.2
    contract_quality: 56.4
    developer_ergonomics: 66.7
    discoverability: 78.6
    operational_transparency: 65.8
  previous_composite: 66.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 86.3
      derived: 1
      marker_coverage: 2.0
      total: 51
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://raw.githubusercontent.com/api-evangelist/scope3/refs/heads/main/screenshots/scope3-2026-08-17T080422.png
security:
- kind: authentication
  name: Scope3 Authentication
  slug: scope3-authentication
  summary_line: http/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: Scope3 Domain Security
  slug: scope3-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: scope3
tags:
- Company
- Enterprise
- Advertising
- Carbon Emissions
- Sustainability
- AdTech
- Measurements
- Artificial Intelligence
- AI Agents
- AdCP
- MCP
- Programmatic
- Media Buying
- Publishing
- A2A
website: https://scope3.com
---
