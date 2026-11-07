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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 52.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 676
  human_in_the_loop: 7
  name: Hubspot Agentic Access
  operation_count: 1058
  slug: hubspot-agentic-access
  summary_line: 1058 operations · 676 acting · 7 human-in-the-loop
api_count: 107
apis:
- description: 'URL redirects allow you to redirect traffic from a HubSpot-hosted page or blog post to any URL. You can also update URL redirects in bulk and use a flexible pattern redirect to dynamically update the '
  name: HubSpot URL Redirects API
  slug: hubspot-url-redirects-api
- description: Pipelines allow you to track records through defined stages in a process, such as sales deals or support tickets. The pipelines endpoints allow you to create, retrieve, update, and delete pipelines an
  name: HubSpot Pipelines API
  slug: hubspot-pipelines-api
- description: Products represent the goods or services you sell in HubSpot. The products endpoints allow you to manage a product library which can be used to quickly add products to deals, generate quotes, and repo
  name: HubSpot Products API
  slug: hubspot-products-api
- description: Line items are individual instances of products that are attached to a deal or quote. The line items endpoints allow you to create, retrieve, update, and delete line item records, enabling detailed pr
  name: HubSpot Line Items API
  slug: hubspot-line-items-api
- description: Quotes allow you to share pricing information with prospects and customers. The quotes endpoints allow you to create and manage quotes with associated line items, deals, and contacts, and support feat
  name: HubSpot Quotes API
  slug: hubspot-quotes-api
- description: The CRM properties endpoints allow you to manage custom properties and view default property details for any CRM object type. You can create, retrieve, update, and delete properties for contacts, comp
  name: HubSpot CRM Properties API
  slug: hubspot-crm-properties-api
- description: The owners endpoints are used to retrieve the list of available owners for a HubSpot account. HubSpot uses owners to assign CRM object records to specific users, and owner IDs are used when setting re
  name: HubSpot Owners API
  slug: hubspot-owners-api
- description: 'The imports endpoints allow you to import contact, company, deal, and other CRM object data into a HubSpot account in bulk using CSV or Excel files. You can map file columns to HubSpot properties and '
  name: HubSpot CRM Imports API
  slug: hubspot-crm-imports-api
- description: 'Custom objects allow you to define and create CRM object types that represent data unique to your business. The custom objects API allows you to define schemas, create records, manage properties, and '
  name: HubSpot Custom Objects API
  slug: hubspot-custom-objects-api
- description: Marketing events are CRM objects that enable you to track marketing activities such as webinars along with the contacts who registered and attended. The marketing events API supports creating and mana
  name: HubSpot Marketing Events API
  slug: hubspot-marketing-events-api
- description: The forms endpoints allow you to create and manage HubSpot forms used for capturing lead information. Supported form types include HubSpot native forms, captured external forms, flow forms, and blog c
  name: HubSpot Forms API
  slug: hubspot-forms-api
- description: The workflows API allows you to programmatically create, retrieve, update, and delete HubSpot automation workflows. You can manage workflow definitions and automate business processes across CRM objec
  name: HubSpot Workflows API
  slug: hubspot-workflows-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The webhooks API allows you to subscribe to events occurring in a HubSpot account, receiving real-time notifications when CRM objects or conversations are created, updated, or deleted. You can configu
  name: HubSpot Webhooks API
  slug: hubspot-webhooks-api
- description: The user provisioning API allows you to create and manage users in a HubSpot account along with their roles, permissions, and team assignments. You can add, retrieve, update, and remove users programm
  name: HubSpot Settings User Provisioning API
  slug: hubspot-settings-user-provisioning-api
- description: The blog tags API allows you to create, manage, and organize blog post tags in HubSpot CMS. Tags help organize blog content and improve discoverability. You can create, retrieve, update, and delete ta
  name: HubSpot Blog Tags API
  slug: hubspot-blog-tags-api
- description: 'The site search API allows you to search the content of HubSpot-hosted sites, including site pages, blog posts, landing pages, and knowledge articles. You can build custom site search experiences and '
  name: HubSpot CMS Site Search API
  slug: hubspot-cms-site-search-api
- description: The CMS content audit API allows you to query audit logs of CMS changes that occurred within your HubSpot account. You can filter and sort on content object changes by type, time period, or HubSpot us
  name: HubSpot CMS Content Audit API
  slug: hubspot-cms-content-audit-api
- description: The feedback submissions API allows you to retrieve survey response data from HubSpot surveys including NPS, CSAT, CES, and custom surveys. This is a read-only API that provides access to existing sur
  name: HubSpot Feedback Submissions API
  slug: hubspot-feedback-submissions-api
- description: The leads API enables you to manage lead records in HubSpot. Leads are contacts or companies that are potential customers who have shown interest in your products or services. You can create, retrieve
  name: HubSpot Leads API
  slug: hubspot-leads-api
- description: The goals API enables you to sync user-specific sales and service team quotas between HubSpot and external systems. Goals are used to create user-specific quotas based on templates provided by HubSpot
  name: HubSpot Goals API
  slug: hubspot-goals-api
- description: The orders API enables you to create and manage ecommerce order data in HubSpot. You can create orders, manage associations to contacts, line items, payments, and invoices, and track fulfillment progr
  name: HubSpot Orders API
  slug: hubspot-orders-api
- description: The carts API enables you to create and manage ecommerce cart data in HubSpot. You can sync cart information between HubSpot and external ecommerce platforms, manage cart properties like pricing and c
  name: HubSpot Carts API
  slug: hubspot-carts-api
- description: The invoices API allows you to create, manage, retrieve, and delete invoices used for billing customers. Invoices progress through draft, open, paid, and voided statuses, and can be configured with di
  name: HubSpot Invoices API
  slug: hubspot-invoices-api
- description: The taxes API enables you to create and associate tax objects as part of the pricing details for quotes and invoices. Taxes are used in conjunction with discounts and fees when determining pricing tot
  name: HubSpot Taxes API
  slug: hubspot-taxes-api
- description: 'The fees API allows you to create and manage fees that can be included in invoices and legacy quotes. Fees support fixed dollar amounts or percentage-based values and are used alongside discounts and '
  name: HubSpot Fees API
  slug: hubspot-fees-api
- description: The discounts API enables you to create and associate discounts as part of the pricing details for quotes. Discounts work alongside fees and taxes in the quote pricing workflow, being applied first in
  name: HubSpot Discounts API
  slug: hubspot-discounts-api
- description: The communications API allows you to log WhatsApp, LinkedIn, or SMS messages to CRM record timelines. You can create, retrieve, update, and manage message engagement records and associate them with co
  name: HubSpot Engagement Communications API
  slug: hubspot-engagement-communications-api
- description: The postal mail engagement API allows you to log postal mail sent to or received from contacts or companies on their CRM records. You can create, retrieve, update, and delete postal mail engagement re
  name: HubSpot Engagement Postal Mail API
  slug: hubspot-engagement-postal-mail-api
- description: The transactional email API enables sending template-based transactional emails through HubSpot using the Single Send API and managing SMTP tokens. You can send emails for commerce receipts, account u
  name: HubSpot Transactional Email API
  slug: hubspot-transactional-email-api
- description: 'The subscription preferences API allows you to manage email subscription details for contacts in your account. You can retrieve subscription types, check contact preferences, subscribe or unsubscribe '
  name: HubSpot Subscription Preferences API
  slug: hubspot-subscription-preferences-api
- description: The timeline events API enables technology partners to send custom event data from external systems into HubSpot for display on CRM record activity timelines. You can create event templates, define cu
  name: HubSpot Timeline Events API
  slug: hubspot-timeline-events-api
- description: 'The calling extensions SDK enables apps to provide a custom calling option to HubSpot users directly from CRM records. The SDK facilitates bidirectional communication between calling applications and '
  name: HubSpot Calling Extensions API
  slug: hubspot-calling-extensions-api
- description: The video conferencing API enables you to integrate custom video conferencing solutions into HubSpot's meeting creation workflow. You can configure webhook notifications for meeting creation, updates,
  name: HubSpot Video Conferencing API
  slug: hubspot-video-conferencing-api
- description: The account information API provides account configuration and usage data for HubSpot accounts. You can retrieve account details including portal ID, time zone, currency settings, and data center loca
  name: HubSpot Account Information API
  slug: hubspot-account-information-api
- description: 'The business units (brands) API provides information about brands tied to a HubSpot user. You can retrieve brand data including brand name, ID, and logo metadata for brands associated with a specific '
  name: HubSpot Business Units API
  slug: hubspot-business-units-api
- description: The currencies API allows you to manage the currencies used in your HubSpot account. You can set your account's company currency, create additional currencies, update exchange rates, and configure aut
  name: HubSpot Currencies API
  slug: hubspot-currencies-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The A/B tests API from HubSpot — 6 operation(s) for a/b tests.
  name: HubSpot A/B tests API
  phrasing_intents:
  - id: post-/cms/pages/2026-09/landing-pages/ab-test/create-variation_createABTestVariation
    intent: Create an A/B test variant of a landing page
    question: How do I A/B test a HubSpot landing page?
  - id: post-/cms/pages/2026-09/landing-pages/ab-test/end_endActiveABTest
    intent: End a landing page A/B test and pick a winner
    question: When my landing page test is done, how do I declare the winning version?
  - id: post-/cms/pages/2026-09/landing-pages/ab-test/rerun_rerunPreviousABTest
    intent: Rerun a past A/B test on a landing page
    question: Can I restart a landing page A/B test that already ended?
  - id: post-/cms/pages/2026-09/site-pages/ab-test/create-variation_createABTestVariation
    intent: Create an A/B test variant of a website page
    question: Is it possible to A/B test a regular website page, not just a landing page?
  - id: post-/cms/pages/2026-09/site-pages/ab-test/end_endActiveABTest
    intent: End a website page A/B test and pick a winner
    question: How do I close out an A/B test on a website page and keep the better version?
  - id: post-/cms/pages/2026-09/site-pages/ab-test/rerun_rerunPreviousABTest
    intent: Rerun a past A/B test on a website page
    question: Can I run an earlier website page A/B test again?
  phrasing_ops: 6
  slug: hubspot-a-b-tests-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Actors API from HubSpot — 2 operation(s) for actors.
  name: HubSpot Actors API
  phrasing_intents:
  - id: post-/conversations/v3/conversations/actors/batch/read
    intent: Resolve several conversation actors at once
    question: How do I turn a batch of actor IDs from conversation messages into real participants?
  - id: get-/conversations/v3/conversations/actors/{actorId}
    intent: Get one conversation actor
    question: Who is behind a particular actor ID on a conversation message?
  phrasing_ops: 2
  slug: hubspot-actors-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Advanced API from HubSpot — 56 operation(s) for advanced.
  name: HubSpot Advanced API
  phrasing_intents:
  - id: post-/oauth/2026-09/token_/oauth/v3/token
    intent: Exchange an OAuth code or refresh token for tokens
    question: How do I trade an OAuth authorization code for an access token and refresh token?
  - id: post-/oauth/2026-09/token/introspect_/oauth/v3/token/introspect
    intent: Check whether an OAuth token is valid
    question: Is there a way to check if an access token is still valid and what metadata it carries?
  - id: post-/oauth/2026-09/token/revoke_/oauth/v3/token/revoke
    intent: Revoke a refresh token
    question: How can I revoke a refresh token when a user disconnects my app?
  - id: get-/cms/blog-settings/2026-09/settings/{blogId}/revisions
    intent: List the revision history of a blog's settings
    question: Where can I see every past revision of a blog's settings?
  - id: get-/cms/blog-settings/2026-09/settings/{blogId}/revisions/{revisionId}
    intent: Get one revision of a blog's settings
    question: What did a blog's settings look like at one particular revision?
  - id: post-/cms/audit-logs/2026-09/export_/cms/audit-logs/2026-03/export
    intent: Export CMS audit logs to recipients
    question: Can I export the CMS audit log and have it sent to specific users?
  - id: post-/media-bridge/2026-09/events/attention-span
    intent: Record an attention span event for media
    question: How can I track how long someone paid attention to a video or audio file?
  - id: post-/media-bridge/2026-09/events/media-played
    intent: Record that a media item was played
    question: Can I log the moment a contact starts playing a video on my page?
  phrasing_ops: 57
  slug: hubspot-advanced-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Assets API from HubSpot — 2 operation(s) for assets.
  name: HubSpot Assets API
  phrasing_intents:
  - id: get-/marketing/campaigns/2026-03/{campaignGuid}/assets/{assetType}
    intent: List a campaign's assets of one type
    question: Which landing pages or emails are associated with my marketing campaign?
  - id: put-/marketing/campaigns/2026-03/{campaignGuid}/assets/{assetType}/{assetId}
    intent: Associate an asset with a campaign
    question: How do I attach a blog post or form to a marketing campaign?
  - id: delete-/marketing/campaigns/2026-03/{campaignGuid}/assets/{assetType}/{assetId}
    intent: Remove an asset from a campaign
    question: How do I unlink a form or email from a campaign without deleting the asset itself?
  phrasing_ops: 3
  slug: hubspot-assets-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Basic API from HubSpot — 271 operation(s) for basic.
  name: HubSpot Basic API
  phrasing_intents:
  - id: get-/account-info/2026-09/activity/audit-logs
    intent: Review account audit logs of user actions
    question: Who changed what in my HubSpot account last week?
  - id: get-/account-info/2026-09/activity/login
    intent: See user login history for the account
    question: When did each person last log in to our portal?
  - id: get-/account-info/2026-09/activity/security
    intent: Review security activity in the account
    question: What security events have happened in my account recently?
  - id: get-/account-info/2026-09/api-usage/daily/private-apps
    intent: Check daily API usage for private apps
    question: How many API calls have my private apps made today?
  - id: get-/account-info/2026-09/details
    intent: Get account details like time zone and currency
    question: What time zone and currency is my HubSpot account set to?
  - id: get-/automation/email-templates/2026-09_/automation/email-templates/2026-09-beta
    intent: List sequence email templates
    question: Which email templates do I have for automated sequences?
  - id: post-/automation/email-templates/2026-09_/automation/email-templates/2026-09-beta
    intent: Create a sequence email template
    question: Can I create a new email template for sequences through the API?
  - id: get-/automation/email-templates/2026-09/folders_/automation/email-templates/2026-09-beta/folders
    intent: List email template folders
    question: What folders are my sequence email templates organized into?
  phrasing_ops: 483
  slug: hubspot-basic-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Batch API from HubSpot — 223 operation(s) for batch.
  name: HubSpot Batch API
  phrasing_intents:
  - id: post-/cms/blogs/2026-09/authors/batch/archive_archiveBatch
    intent: Delete several blog authors at once
    question: How do I remove a whole list of blog authors from my HubSpot blog in one call?
  - id: post-/cms/blogs/2026-09/authors/batch/create_createBatch
    intent: Create several blog authors at once
    question: Can I add a batch of new blog authors with names and bios in one request?
  - id: post-/cms/blogs/2026-09/authors/batch/read_readBatch
    intent: Look up several blog authors by ID
    question: How can I fetch the details of several blog authors when I already have their IDs?
  - id: post-/cms/blogs/2026-09/authors/batch/update_updateBatch
    intent: Edit several blog authors at once
    question: How do I change the bios or display names of many blog authors together?
  - id: post-/media-bridge/2026-09/{appId}/properties/{objectType}/batch/archive
    intent: Archive app properties for a Media Bridge object type
    question: Can I retire several Media Bridge properties my app defined for one object type?
  - id: post-/media-bridge/2026-09/{appId}/properties/{objectType}/batch/create
    intent: Define new properties for a Media Bridge object type
    question: How can my Media Bridge app set up several custom properties on a media object type at once?
  - id: post-/media-bridge/2026-09/{appId}/properties/{objectType}/batch/read
    intent: Read Media Bridge property definitions in bulk
    question: Which details can I get back for a list of my Media Bridge app's properties by name?
  - id: post-/cms/pages/2026-09/landing-pages/batch/archive_archiveBatch
    intent: Delete several landing pages
    question: How do I permanently delete a set of landing pages by ID?
  phrasing_ops: 223
  slug: hubspot-batch-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Budget API from HubSpot — 3 operation(s) for budget.
  name: HubSpot Budget API
  phrasing_intents:
  - id: post-/marketing/campaigns/2026-03/{campaignGuid}/budget
    intent: Add a budget line item to a campaign
    question: How do I add a new budget line to a marketing campaign?
  - id: get-/marketing/campaigns/2026-03/{campaignGuid}/budget/totals
    intent: See a campaign's total budget, spend and remainder
    question: How much budget is left on my marketing campaign?
  - id: get-/marketing/campaigns/2026-03/{campaignGuid}/budget/{budgetId}
    intent: Get one campaign budget item
    question: How do I look up a single budget line on a campaign by its ID?
  - id: put-/marketing/campaigns/2026-03/{campaignGuid}/budget/{budgetId}
    intent: Update a campaign budget item
    question: How do I change the amount on an existing campaign budget line?
  - id: delete-/marketing/campaigns/2026-03/{campaignGuid}/budget/{budgetId}
    intent: Delete a campaign budget item
    question: How do I remove a budget line from a marketing campaign?
  phrasing_ops: 5
  slug: hubspot-budget-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Callbacks API from HubSpot — 2 operation(s) for callbacks.
  name: HubSpot Callbacks API
  phrasing_intents:
  - id: post-/automation/actions/callbacks/2026-09/complete_completeBatch
    intent: Complete many blocked workflow actions at once
    question: How do I resume a bunch of workflow actions that are waiting on my app?
  - id: post-/automation/actions/callbacks/2026-09/{callbackId}/complete_complete
    intent: Complete one blocked workflow action
    question: How do I tell a workflow that my app finished processing one blocked action?
  phrasing_ops: 2
  slug: hubspot-callbacks-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Central FX rates API from HubSpot — 3 operation(s) for central fx rates.
  name: HubSpot Central FX rates API
  phrasing_intents:
  - id: post-/settings/currencies/2026-09/central-fx-rates/add-currency_/settings/v3/currencies/central-fx-rates/add-currency
    intent: Add a currency that uses central exchange rates
    question: How do I add a new currency to my account with automatically managed exchange rates?
  - id: get-/settings/currencies/2026-09/central-fx-rates/information_/settings/v3/currencies/central-fx-rates/information
    intent: Check whether central exchange rates are enabled
    question: Is the central exchange rates feature turned on for my HubSpot portal?
  - id: get-/settings/currencies/2026-09/central-fx-rates/unsupported-currencies_/settings/v3/currencies/central-fx-rates/unsupported-currencies
    intent: List currencies without central exchange rates
    question: Which currencies aren't covered by central exchange rates?
  phrasing_ops: 3
  slug: hubspot-central-fx-rates-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Channel accounts API from HubSpot — 5 operation(s) for channel accounts.
  name: HubSpot Channel accounts API
  phrasing_intents:
  - id: get-/conversations/v3/conversations/channel-accounts
    intent: List channel accounts across inboxes
    question: Which channel accounts are connected to my conversations inboxes?
  - id: get-/conversations/v3/conversations/channel-accounts/{channelAccountId}
    intent: Get one channel account
    question: How do I look up a single channel account by its ID?
  - id: patch-/conversations/custom-channels/2026-09/{channelId}/channel-account-staging-tokens/{accountToken}
    intent: Update a channel account staging token
    question: Can I set the account name on a staging token before its channel account is created?
  - id: get-/conversations/custom-channels/2026-09/{channelId}/channel-accounts
    intent: List accounts on a custom channel
    question: Can I list every account connected to one of my custom channels?
  - id: post-/conversations/custom-channels/2026-09/{channelId}/channel-accounts
    intent: Create an account on a custom channel
    question: How do I add a new account to a custom channel?
  - id: patch-/conversations/custom-channels/2026-09/{channelId}/channel-accounts/{channelAccountId}
    intent: Rename or disable a custom channel account
    question: Can I disable a custom channel account without deleting it?
  phrasing_ops: 6
  slug: hubspot-channel-accounts-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Channels API from HubSpot — 4 operation(s) for channels.
  name: HubSpot Channels API
  phrasing_intents:
  - id: get-/conversations/v3/conversations/channels
    intent: List conversation channels
    question: What conversation channels are available in my HubSpot inbox setup?
  - id: get-/conversations/v3/conversations/channels/{channelId}
    intent: Get a conversation channel's details
    question: How do I look up a single conversations channel by its ID?
  - id: get-/conversations/custom-channels/2026-09/{channelId}
    intent: Get a custom channel's capabilities and settings
    question: What capabilities does my registered custom messaging channel currently support?
  - id: delete-/conversations/custom-channels/2026-09/{channelId}
    intent: Archive a custom messaging channel
    question: How do I retire a custom channel my app registered?
  - id: patch-/conversations/custom-channels/2026-09/{channelId}
    intent: Update a custom channel's capabilities and URLs
    question: How do I change the webhook URL for my custom messaging channel?
  - id: get-/conversations/custom-channels/2026-09/{channelId}/channel-accounts/{channelAccountId}
    intent: Get a custom channel account's details
    question: Which inbox is a custom channel account connected to?
  phrasing_ops: 6
  slug: hubspot-channels-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Definitions API from HubSpot — 5 operation(s) for definitions.
  name: HubSpot Definitions API
  phrasing_intents:
  - id: get-/automation/actions/2026-09/{appId}_getPage
    intent: List an app's custom workflow actions
    question: Which custom workflow actions has my app defined?
  - id: post-/automation/actions/2026-09/{appId}_create
    intent: Create a custom workflow action
    question: How do I add my own action to HubSpot workflows from my app?
  - id: get-/automation/actions/2026-09/{appId}/{definitionId}_getById
    intent: Get one custom workflow action
    question: How do I view the full configuration of one custom action definition?
  - id: delete-/automation/actions/2026-09/{appId}/{definitionId}_archive
    intent: Delete a custom workflow action
    question: How do I remove a custom workflow action my app no longer supports?
  - id: patch-/automation/actions/2026-09/{appId}/{definitionId}_update
    intent: Update a custom workflow action
    question: Can I change the URL an existing custom action calls?
  - id: get-/automation/actions/2026-09/{appId}/{definitionId}/requires-object_/automation/v4/actions/{appId}/{definitionId}/requires-object
    intent: Check if a custom action requires an object
    question: Does my custom workflow action need an enrolled CRM object to run?
  - id: post-/automation/actions/2026-09/{appId}/{definitionId}/requires-object_/automation/v4/actions/{appId}/{definitionId}/requires-object
    intent: Set whether a custom action requires an object
    question: Can I let a custom action run without an associated CRM object?
  - id: get-/communication-preferences/2026-09/definitions
    intent: List subscription type definitions
    question: What email subscription types are set up in my account?
  phrasing_ops: 9
  slug: hubspot-definitions-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Emails API from HubSpot — 12 operation(s) for emails.
  name: HubSpot Emails API
  phrasing_intents:
  - id: post-/marketing/emails/2026-09/ab-test/create-variation_createAbTestVariation
    intent: Create an A/B test variant of a marketing email
    question: How do I set up an A/B test on a marketing email in HubSpot?
  - id: post-/marketing/emails/2026-09/clone_clone
    intent: Duplicate a marketing email
    question: Can I make a copy of an existing marketing email instead of building it from scratch?
  - id: get-/marketing/emails/2026-09/{emailId}_getById
    intent: Look up a marketing email's details
    question: Where can I see the full settings and content of one marketing email?
  - id: delete-/marketing/emails/2026-09/{emailId}_archive
    intent: Delete a marketing email
    question: How do I get rid of a marketing email I no longer need?
  - id: patch-/marketing/emails/2026-09/{emailId}_update
    intent: Change a marketing email's live properties
    question: How do I change the subject line of a marketing email directly, without going through a draft?
  - id: get-/marketing/emails/2026-09/{emailId}/ab-test/get-variation_getAbTestVariation
    intent: Find the other version of an A/B tested email
    question: Given version A of an A/B test email, how do I find its version B?
  - id: get-/marketing/emails/2026-09/{emailId}/draft_getDraft
    intent: View the unpublished draft of a marketing email
    question: How can I see pending edits to a marketing email before they go live?
  - id: patch-/marketing/emails/2026-09/{emailId}/draft_upsertDraft
    intent: Edit the draft of a marketing email
    question: Can I stage changes to a live marketing email without affecting the published version?
  phrasing_ops: 15
  slug: hubspot-emails-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Event Attendees API from HubSpot — 4 operation(s) for event attendees.
  name: HubSpot Event Attendees API
  phrasing_intents:
  - id: post-/marketing/marketing-events/2026-09/attendance/{externalEventId}/{subscriberState}/create_recordByContactIds
    intent: Record attendance by contact ID for an external event
    question: How do I mark contacts as attending an event I track by my own external event ID, using their contact IDs?
  - id: post-/marketing/marketing-events/2026-09/attendance/{externalEventId}/{subscriberState}/email-create_recordByContactEmails
    intent: Record attendance by email for an external event
    question: Can I register attendees by email address for an event I identify with my own external event ID?
  - id: post-/marketing/marketing-events/2026-09/{objectId}/attendance/{subscriberState}/create_recordByContactId
    intent: Record attendance by contact ID for a HubSpot event
    question: Can I mark contacts as registered, attended or cancelled using the marketing event's HubSpot object ID and their contact IDs?
  - id: post-/marketing/marketing-events/2026-09/{objectId}/attendance/{subscriberState}/email-create_recordByEmail
    intent: Record attendance by email for a HubSpot event
    question: Can I record attendees by email against a marketing event using its HubSpot object ID?
  phrasing_ops: 4
  slug: hubspot-event-attendees-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Event Status API from HubSpot — 2 operation(s) for event status.
  name: HubSpot Event Status API
  phrasing_intents:
  - id: post-/marketing/marketing-events/2026-09/events/{externalEventId}/cancel_cancel
    intent: Cancel a marketing event
    question: How do I mark a webinar synced from my event app as cancelled?
  - id: post-/marketing/marketing-events/2026-09/events/{externalEventId}/complete_complete
    intent: Mark a marketing event as completed
    question: How do I flag a marketing event as finished once it's over?
  phrasing_ops: 2
  slug: hubspot-event-status-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Exchange rates API from HubSpot — 4 operation(s) for exchange rates.
  name: HubSpot Exchange rates API
  phrasing_intents:
  - id: get-/settings/currencies/2026-09/exchange-rates
    intent: List exchange rates
    question: What exchange rate history do I have for euros to dollars?
  - id: post-/settings/currencies/2026-09/exchange-rates
    intent: Add an exchange rate
    question: How do I add a new conversion rate for a currency?
  - id: get-/settings/currencies/2026-09/exchange-rates/current
    intent: Get current exchange rates
    question: What are today's conversion rates for every currency pair in my account?
  - id: post-/settings/currencies/2026-09/exchange-rates/update-visibility
    intent: Show or hide a currency pair
    question: Can I hide a currency pair from users in the multi-currency settings?
  - id: get-/settings/currencies/2026-09/exchange-rates/{exchangeRateId}
    intent: Get one exchange rate
    question: How do I look up a single exchange rate record by its ID?
  - id: patch-/settings/currencies/2026-09/exchange-rates/{exchangeRateId}
    intent: Update an existing conversion rate
    question: Can I correct a conversion rate I already entered?
  phrasing_ops: 6
  slug: hubspot-exchange-rates-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The files API allows you to upload, manage, and organize files in HubSpot's file manager. You can upload files, organize them into folders, control file accessibility and privacy settings, retrieve fi
  name: HubSpot Files API
  phrasing_intents:
  - id: post-/files/2026-03/files_upload
    intent: Upload a file to the file manager
    question: How do I upload an image from my computer into the HubSpot file manager?
  - id: post-/files/2026-03/files/import-from-url/async_importFromUrl
    intent: Import a file from a URL
    question: Can I pull a file into the file manager straight from a web address?
  - id: get-/files/2026-03/files/import-from-url/async/tasks/{taskId}/status_checkImport
    intent: Check a URL import's status
    question: Has my import-from-URL file task finished yet?
  - id: get-/files/2026-03/files/search_doSearch
    intent: Search files in the file manager
    question: How do I find all PDFs in my file manager?
  - id: get-/files/2026-03/files/stat/{path}_getMetadata
    intent: Look up a file by its path
    question: I know where a file lives in my folders; how do I get its details from that path?
  - id: get-/files/2026-03/files/{fileId}_getById
    intent: Retrieve a file by ID
    question: How do I get a file's details when I have its file ID?
  - id: put-/files/2026-03/files/{fileId}_replace
    intent: Replace a file's contents
    question: Can I swap an image's content without breaking every page that links to it?
  - id: delete-/files/2026-03/files/{fileId}_archive
    intent: Delete a file
    question: How do I remove a file I no longer need from the file manager?
  phrasing_ops: 12
  slug: hubspot-files-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Folders API from HubSpot — 11 operation(s) for folders.
  name: HubSpot Folders API
  phrasing_intents:
  - id: get-/cms/pages/2026-09/landing-pages/folders_getFoldersPage
    intent: List landing page folders
    question: How do I list all the folders my landing pages are organized into?
  - id: post-/cms/pages/2026-09/landing-pages/folders_createFolder
    intent: Create a landing page folder
    question: How do I create a new folder to group my landing pages?
  - id: post-/cms/pages/2026-09/landing-pages/folders/batch/read_readFolders
    intent: Fetch several landing page folders at once
    question: Can I look up a batch of landing page folders by their IDs in one call?
  - id: get-/cms/pages/2026-09/landing-pages/folders/{objectId}_getFolderById
    intent: Get one landing page folder
    question: How do I look up a single landing page folder by its ID?
  - id: delete-/cms/pages/2026-09/landing-pages/folders/{objectId}_archiveFolder
    intent: Delete a landing page folder
    question: Can I delete a landing page folder I no longer use?
  - id: patch-/cms/pages/2026-09/landing-pages/folders/{objectId}_updateFolder
    intent: Rename or move a landing page folder
    question: How do I rename an existing landing page folder?
  - id: get-/cms/pages/2026-09/landing-pages/folders/{objectId}/revisions_getFolderPreviousVersions
    intent: List a landing page folder's revision history
    question: Where can I see every earlier version of a landing page folder?
  - id: get-/cms/pages/2026-09/landing-pages/folders/{objectId}/revisions/{revisionId}_getFolderPreviousVersion
    intent: View one past revision of a landing page folder
    question: Can I inspect exactly what a landing page folder looked like at a specific revision?
  phrasing_ops: 17
  slug: hubspot-folders-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Functions API from HubSpot — 3 operation(s) for functions.
  name: HubSpot Functions API
  phrasing_intents:
  - id: get-/automation/actions/2026-09/{appId}/{definitionId}/functions_getPage
    intent: List all functions on a custom workflow action
    question: Which serverless functions are attached to my custom workflow action definition?
  - id: get-/automation/actions/2026-09/{appId}/{definitionId}/functions/{functionType}_getByFunctionType
    intent: Get a custom action's functions of one type
    question: Can I fetch just the pre-action execution function for a custom workflow action?
  - id: put-/automation/actions/2026-09/{appId}/{definitionId}/functions/{functionType}_createOrReplaceByFunctionType
    intent: Add or replace a function by type on an action
    question: How do I attach a new serverless function of a given type to my custom workflow action?
  - id: delete-/automation/actions/2026-09/{appId}/{definitionId}/functions/{functionType}_archiveByFunctionType
    intent: Delete an action's function of a given type
    question: How do I remove the function of a certain type from my custom workflow action?
  - id: get-/automation/actions/2026-09/{appId}/{definitionId}/functions/{functionType}/{functionId}_getById
    intent: Get one function on a custom action by ID
    question: How do I look up a single function on my workflow action when I know its ID?
  - id: put-/automation/actions/2026-09/{appId}/{definitionId}/functions/{functionType}/{functionId}_createOrReplace
    intent: Update a specific function on a custom action
    question: How do I update one particular function on my custom workflow action by its ID?
  - id: delete-/automation/actions/2026-09/{appId}/{definitionId}/functions/{functionType}/{functionId}_archive
    intent: Archive one function on a custom action by ID
    question: How do I archive a single function on my workflow action using its ID?
  phrasing_ops: 7
  slug: hubspot-functions-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Identifiers API from HubSpot — 2 operation(s) for identifiers.
  name: HubSpot Identifiers API
  phrasing_intents:
  - id: get-/marketing/marketing-events/2026-09/events/search_doSearch
    intent: Find my app's marketing events by external ID
    question: How can my app find the marketing events it created that carry a given external event ID?
  - id: get-/marketing/marketing-events/2026-09/{externalEventId}/identifiers_searchPortalEvents
    intent: Find all portal marketing events by external ID
    question: Can I get the HubSpot object IDs of every marketing event in the portal that shares an external event ID?
  phrasing_ops: 2
  slug: hubspot-identifiers-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Inboxes API from HubSpot — 2 operation(s) for inboxes.
  name: HubSpot Inboxes API
  phrasing_intents:
  - id: get-/conversations/v3/conversations/inboxes
    intent: List conversations inboxes
    question: What conversations inboxes does my HubSpot account have?
  - id: get-/conversations/v3/conversations/inboxes/{inboxId}
    intent: Get details of one conversations inbox
    question: How do I see the settings of a single inbox if I have its ID?
  phrasing_ops: 2
  slug: hubspot-inboxes-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Items API from HubSpot — 2 operation(s) for items.
  name: HubSpot Items API
  phrasing_intents:
  - id: get-/commerce/price-books/2026-09/price-books/{priceBookId}/items_/commerce/price-books/2026-09-beta/price-books/{priceBookId}/items
    intent: List the items in a price book
    question: Which products are in a given price book?
  - id: post-/commerce/price-books/2026-09/price-books/{priceBookId}/items_/commerce/price-books/2026-09-beta/price-books/{priceBookId}/items
    intent: Add a product to a price book
    question: How do I add a product to one of my price books?
  - id: get-/commerce/price-books/2026-09/price-books/{priceBookId}/items/{priceBookItemId}_/commerce/price-books/2026-09-beta/price-books/{priceBookId}/items/{priceBookItemId}
    intent: Get one price book item
    question: How do I see the pricing details of one item in a price book?
  - id: delete-/commerce/price-books/2026-09/price-books/{priceBookId}/items/{priceBookItemId}
    intent: Remove an item from a price book
    question: How do I take a product out of a price book?
  - id: patch-/commerce/price-books/2026-09/price-books/{priceBookId}/items/{priceBookItemId}
    intent: Update a price book item
    question: Can I change the price or billing frequency of an item already in a price book?
  phrasing_ops: 5
  slug: hubspot-items-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Labels API from HubSpot — 2 operation(s) for labels.
  name: HubSpot Labels API
  phrasing_intents:
  - id: get-/crm/associations/2026-09/{fromObjectType}/{toObjectType}/labels_getPage
    intent: List association labels between two object types
    question: What association labels exist between contacts and companies in my CRM?
  - id: put-/crm/associations/2026-09/{fromObjectType}/{toObjectType}/labels_update
    intent: Rename an existing association label
    question: How do I change the wording of an association label I already created?
  - id: post-/crm/associations/2026-09/{fromObjectType}/{toObjectType}/labels_create
    intent: Create a new association label
    question: Can I define a custom relationship label, like Manager, between two CRM object types?
  - id: delete-/crm/associations/2026-09/{fromObjectType}/{toObjectType}/labels/{associationTypeId}_remove
    intent: Delete an association label
    question: How do I remove an association label I no longer use?
  phrasing_ops: 4
  slug: hubspot-labels-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Landing pages API from HubSpot — 7 operation(s) for landing pages.
  name: HubSpot Landing pages API
  phrasing_intents:
  - id: get-/cms/pages/2026-09/landing-pages_getPage
    intent: List landing pages
    question: How do I get a list of every landing page in my HubSpot account?
  - id: post-/cms/pages/2026-09/landing-pages_create
    intent: Create a landing page
    question: How do I build a brand-new landing page through the API?
  - id: post-/cms/pages/2026-09/landing-pages/clone_clone
    intent: Clone a landing page
    question: Can I duplicate an existing landing page instead of starting from scratch?
  - id: post-/cms/pages/2026-09/landing-pages/schedule_schedule
    intent: Schedule a landing page to publish
    question: How do I set a landing page to go live at a future date?
  - id: get-/cms/pages/2026-09/landing-pages/{objectId}_getById
    intent: Get a live landing page
    question: How can I pull the details of one specific landing page by its ID?
  - id: delete-/cms/pages/2026-09/landing-pages/{objectId}_archive
    intent: Delete a landing page
    question: Can I delete a landing page I no longer need?
  - id: patch-/cms/pages/2026-09/landing-pages/{objectId}_update
    intent: Update a live landing page
    question: How do I change the title or meta description of a published landing page directly?
  - id: get-/cms/pages/2026-09/landing-pages/{objectId}/draft_getDraftById
    intent: Get a landing page's draft version
    question: Where can I see the unpublished draft edits of a landing page?
  phrasing_ops: 11
  slug: hubspot-landing-pages-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Limits API from HubSpot — 5 operation(s) for limits.
  name: HubSpot Limits API
  phrasing_intents:
  - id: get-/crm/associations/2026-09/definitions/configurations/all_getPage
    intent: List every association limit in the CRM
    question: Where can I see all the association limits configured across my CRM objects?
  - id: get-/crm/associations/2026-09/definitions/configurations/{fromObjectType}/{toObjectType}_getPageBetweenTwoObjectTypes
    intent: Check association limits between two object types
    question: How many companies can a contact be associated with under my current limits?
  - id: post-/crm/associations/2026-09/definitions/configurations/{fromObjectType}/{toObjectType}/batch/create_batchCreate
    intent: Set new association limits between object types
    question: Can I cap how many deals a contact can be associated with?
  - id: post-/crm/associations/2026-09/definitions/configurations/{fromObjectType}/{toObjectType}/batch/purge_batchRemove
    intent: Remove association limits between object types
    question: How do I lift an association limit I set earlier?
  - id: post-/crm/associations/2026-09/definitions/configurations/{fromObjectType}/{toObjectType}/batch/update_batchUpdate
    intent: Change existing association limits
    question: Can I raise an association limit that's already configured?
  phrasing_ops: 5
  slug: hubspot-limits-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The List Associations API from HubSpot — 4 operation(s) for list associations.
  name: HubSpot List Associations API
  phrasing_intents:
  - id: get-/marketing/marketing-events/2026-09/associations/{externalAccountId}/{externalEventId}/lists_getAllByExternalAccountAndEventIds
    intent: List lists tied to an event by its external IDs
    question: Which contact lists are linked to a marketing event from my external event app?
  - id: put-/marketing/marketing-events/2026-09/associations/{externalAccountId}/{externalEventId}/lists/{listId}_associateByExternalAccountAndEventIds
    intent: Link a list to an event by its external IDs
    question: How do I attach a contact list to a marketing event using my external event ID?
  - id: delete-/marketing/marketing-events/2026-09/associations/{externalAccountId}/{externalEventId}/lists/{listId}_disassociateByExternalAccountAndEventIds
    intent: Unlink a list from an event by its external IDs
    question: How do I detach a list from a marketing event I track by external event ID?
  - id: get-/marketing/marketing-events/2026-09/associations/{marketingEventId}/lists_getAllByMarketingEventId
    intent: List lists tied to a marketing event
    question: Which lists are associated with a marketing event when I have its HubSpot marketing event ID?
  - id: put-/marketing/marketing-events/2026-09/associations/{marketingEventId}/lists/{listId}_associateByMarketingEventId
    intent: Link a list to a marketing event
    question: How do I associate a contact list with a marketing event using its HubSpot event ID?
  - id: delete-/marketing/marketing-events/2026-09/associations/{marketingEventId}/lists/{listId}_disassociateByMarketingEventId
    intent: Unlink a list from a marketing event
    question: How do I remove a list's association from a marketing event by its HubSpot event ID?
  phrasing_ops: 6
  slug: hubspot-list-associations-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Messages API from HubSpot — 4 operation(s) for messages.
  name: HubSpot Messages API
  phrasing_intents:
  - id: get-/conversations/v3/conversations/threads/{threadId}/messages/{messageId}
    intent: Get a message from a conversation thread
    question: How do I read one specific message inside an inbox conversation thread?
  - id: get-/conversations/v3/conversations/threads/{threadId}/messages/{messageId}/original-content
    intent: Get a message's full untruncated content
    question: A conversation message looks cut off; how can I get its complete original text?
  - id: post-/conversations/custom-channels/2026-09/{channelId}/messages
    intent: Publish a message over a custom channel
    question: How do I send an incoming or outgoing message into HubSpot through my custom channel?
  - id: get-/conversations/custom-channels/2026-09/{channelId}/messages/{messageId}
    intent: Get a message sent over a custom channel
    question: How can I look up a message that went through my custom channel?
  - id: patch-/conversations/custom-channels/2026-09/{channelId}/messages/{messageId}
    intent: Update a custom channel message's delivery status
    question: How do I mark a custom channel message as sent, failed or read?
  phrasing_ops: 5
  slug: hubspot-messages-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Metrics API from HubSpot — 3 operation(s) for metrics.
  name: HubSpot Metrics API
  phrasing_intents:
  - id: get-/marketing/campaigns/2026-03/{campaignGuid}/reports/contacts/{contactType}
    intent: List contacts a campaign reached
    question: Which contact IDs did my marketing campaign influence?
  - id: get-/marketing/campaigns/2026-03/{campaignGuid}/reports/metrics
    intent: Get a campaign's attribution metrics
    question: How many sessions and new contacts did my campaign drive?
  - id: get-/marketing/campaigns/2026-03/{campaignGuid}/reports/revenue
    intent: Get a campaign's attributed revenue
    question: How much deal revenue is attributed to my campaign?
  phrasing_ops: 3
  slug: hubspot-metrics-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Multi-language API from HubSpot — 29 operation(s) for multi-language.
  name: HubSpot Multi Language API
  phrasing_intents:
  - id: post-/cms/blogs/2026-09/authors/multi-language/attach-to-lang-group_attachToLangGroup
    intent: Add a blog author to a translation group
    question: How do I link a blog author profile to its version in another language?
  - id: post-/cms/blogs/2026-09/authors/multi-language/create-language-variation_createLangVariation
    intent: Clone a blog author into another language
    question: Can I clone a blog author profile to make a translated version?
  - id: post-/cms/blogs/2026-09/authors/multi-language/detach-from-lang-group_detachFromLangGroup
    intent: Remove a blog author from a translation group
    question: How do I unlink a blog author from its other-language versions?
  - id: put-/cms/blogs/2026-09/authors/multi-language/set-new-lang-primary_setLangPrimary
    intent: Make a blog author the primary language version
    question: How do I change which blog author translation is the primary one?
  - id: post-/cms/blogs/2026-09/authors/multi-language/update-languages_updateLangs
    intent: Reassign languages across a blog author group
    question: I tagged my blog author translations with the wrong languages. How do I fix all of them at once?
  - id: post-/cms/blog-settings/2026-09/settings/multi-language/attach-to-lang-group
    intent: Add a blog to a translation group
    question: How do I connect my French blog to the English blog as translations of each other?
  - id: post-/cms/blog-settings/2026-09/settings/multi-language/create-language-variation
    intent: Clone a whole blog into another language
    question: Can I spin up a Spanish version of my entire blog from the existing one?
  - id: post-/cms/blog-settings/2026-09/settings/multi-language/detach-from-lang-group
    intent: Remove a blog from a translation group
    question: How do I stop a blog from being treated as a translation of another blog?
  phrasing_ops: 29
  slug: hubspot-multi-language-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Participant State API from HubSpot — 5 operation(s) for participant state.
  name: HubSpot Participant State API
  phrasing_intents:
  - id: get-/marketing/marketing-events/2026-09/participations/contacts/{contactIdentifier}/breakdown_getParticipationsBreakdownByContactId
    intent: See which marketing events a contact took part in
    question: Which webinars and events has a given contact registered for or attended?
  - id: get-/marketing/marketing-events/2026-09/participations/{externalAccountId}/{externalEventId}_getParticipationsCountersByEventExternalId
    intent: Count attendees for an event by its external ID
    question: How many people registered, attended or cancelled for an event synced from my event app?
  - id: get-/marketing/marketing-events/2026-09/participations/{externalAccountId}/{externalEventId}/breakdown_getParticipationsBreakdownByExternalEventId
    intent: List participants of an event by its external ID
    question: Who attended an event I synced from my external event tool?
  - id: get-/marketing/marketing-events/2026-09/participations/{marketingEventId}_getParticipationsCountersByMarketingEventId
    intent: Count attendees for a HubSpot marketing event
    question: How many contacts registered and attended a marketing event, using its HubSpot ID?
  - id: get-/marketing/marketing-events/2026-09/participations/{marketingEventId}/breakdown_getParticipationsBreakdownByMarketingEventId
    intent: List participants of a HubSpot marketing event
    question: Who registered for a marketing event, looked up by its HubSpot event ID?
  phrasing_ops: 5
  slug: hubspot-participant-state-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Revisions API from HubSpot — 6 operation(s) for revisions.
  name: HubSpot Revisions API
  phrasing_intents:
  - id: get-/automation/actions/2026-09/{appId}/{definitionId}/revisions_getPage
    intent: List versions of a custom workflow action
    question: How do I see the version history of a custom workflow action my app defines?
  - id: get-/automation/actions/2026-09/{appId}/{definitionId}/revisions/{revisionId}_getById
    intent: Get one version of a custom workflow action
    question: What did my custom workflow action look like in a specific earlier revision?
  - id: get-/cms/blogs/2026-09/posts/{objectId}/revisions_getPreviousVersions
    intent: List previous versions of a blog post
    question: Where can I find the edit history of a HubSpot blog post?
  - id: get-/cms/blogs/2026-09/posts/{objectId}/revisions/{revisionId}_getPreviousVersion
    intent: View one previous version of a blog post
    question: How do I read exactly what a blog post said in an older revision?
  - id: post-/cms/blogs/2026-09/posts/{objectId}/revisions/{revisionId}/restore_restorePreviousVersion
    intent: Restore a blog post to an earlier version
    question: How do I roll a blog post back to how it looked before recent edits?
  - id: post-/cms/blogs/2026-09/posts/{objectId}/revisions/{revisionId}/restore-to-draft_restorePreviousVersionToDraft
    intent: Make an old blog post version the new draft
    question: Can I bring back an old version of a blog post as a draft to rework it before publishing?
  phrasing_ops: 6
  slug: hubspot-revisions-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Roles API from HubSpot — 1 operation(s) for roles.
  name: HubSpot Roles API
  phrasing_intents:
  - id: get-/settings/users/2026-03/roles_getAll
    intent: List the user roles on an account
    question: What user roles are defined in my HubSpot account?
  phrasing_ops: 1
  slug: hubspot-roles-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Rows API from HubSpot — 11 operation(s) for rows.
  name: HubSpot Rows API
  phrasing_intents:
  - id: get-/cms/v3/hubdb/2026-09/tables/{tableIdOrName}/rows_getTableRows
    intent: List rows in a published HubDB table
    question: How do I read all the rows of a published HubDB table?
  - id: post-/cms/v3/hubdb/2026-09/tables/{tableIdOrName}/rows_createTableRow
    intent: Add one row to a HubDB table
    question: How do I add a single new row to a HubDB table?
  - id: post-/cms/v3/hubdb/2026-09/tables/{tableIdOrName}/rows/batch/read_readTableRows
    intent: Fetch several published HubDB rows by ID
    question: Can I pull a specific set of live HubDB rows by their IDs in one request?
  - id: post-/cms/v3/hubdb/2026-09/tables/{tableIdOrName}/rows/draft/batch/clone_cloneDraftTableRows
    intent: Clone many HubDB rows at once
    question: How many HubDB rows can I duplicate in a single call?
  - id: post-/cms/v3/hubdb/2026-09/tables/{tableIdOrName}/rows/draft/batch/create_createDraftTableRows
    intent: Bulk add rows to a HubDB table draft
    question: What's the fastest way to load a lot of new rows into HubDB?
  - id: post-/cms/v3/hubdb/2026-09/tables/{tableIdOrName}/rows/draft/batch/purge_purgeDraftTableRows
    intent: Permanently delete many HubDB rows
    question: How do I delete a batch of rows from a HubDB table for good?
  - id: post-/cms/v3/hubdb/2026-09/tables/{tableIdOrName}/rows/draft/batch/read_readDraftTableRows
    intent: Fetch several draft HubDB rows by ID
    question: Can I read a set of unpublished rows from a HubDB table's draft by ID?
  - id: post-/cms/v3/hubdb/2026-09/tables/{tableIdOrName}/rows/draft/batch/replace_replaceDraftTableRows
    intent: Overwrite many HubDB rows at once
    question: Can I fully replace the contents of many HubDB rows in one request?
  phrasing_ops: 15
  slug: hubspot-rows-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Search API from HubSpot — 35 operation(s) for search.
  name: HubSpot Search API
  phrasing_intents:
  - id: post-/crm/objects/2026-03/{objectType}/search_/crm/objects/v3/{objectType}/search
    intent: Search records of any CRM object type
    question: Is there one search endpoint that works for whatever CRM object type I name, such as appointments?
  - id: post-/crm/objects/2026-03/calls/search_doSearch
    intent: Search logged calls
    question: How do I find logged calls in the CRM that match certain property values?
  - id: post-/crm/objects/2026-03/carts/search
    intent: Search shopping carts
    question: Can I look up carts in the CRM by filtering on their properties?
  - id: post-/crm/objects/2026-03/commerce_payments/search
    intent: Search commerce payment records
    question: Is there a way to query payment records collected through HubSpot commerce with filter groups?
  - id: post-/crm/objects/2026-03/communications/search_doSearch
    intent: Search logged communication messages
    question: Can I search the logged communications messages attached to CRM records?
  - id: post-/crm/objects/2026-03/companies/search_doSearch
    intent: Search companies
    question: How do I find companies in my CRM by searching for a name?
  - id: post-/crm/objects/2026-03/contacts/search_doSearch
    intent: Search contacts
    question: What's the way to find contacts whose properties match a filter, like a lifecycle stage?
  - id: post-/crm/objects/2026-03/0-410/search
    intent: Search courses
    question: Can I search course records in the CRM by their properties?
  phrasing_ops: 36
  slug: hubspot-search-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Send transactional email API from HubSpot — 1 operation(s) for send transactional email.
  name: HubSpot Send transactional email API
  phrasing_intents:
  - id: post-/marketing/transactional/2026-09/single-email/send_sendEmail
    intent: Send a transactional email
    question: How do I send a receipt or password reset email built in the email tool?
  phrasing_ops: 1
  slug: hubspot-send-transactional-email-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Settings API from HubSpot — 1 operation(s) for settings.
  name: HubSpot Settings API
  phrasing_intents:
  - id: get-/marketing/marketing-events/2026-09/{appId}/settings_getAll
    intent: Get an app's marketing event settings
    question: What event details URL is my marketing events app configured with?
  - id: post-/marketing/marketing-events/2026-09/{appId}/settings_update
    intent: Set an app's marketing event settings
    question: How do I tell HubSpot where to fetch marketing event details from my app?
  phrasing_ops: 2
  slug: hubspot-settings-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The SMTP Tokens API from HubSpot — 3 operation(s) for smtp tokens.
  name: HubSpot SMTP Tokens API
  phrasing_intents:
  - id: get-/marketing/transactional/2026-09/smtp-tokens_getTokensPage
    intent: Find SMTP API tokens by campaign
    question: How do I find which SMTP API tokens exist for a given email campaign name?
  - id: post-/marketing/transactional/2026-09/smtp-tokens_createToken
    intent: Create an SMTP API token
    question: How do I get credentials to send transactional email through HubSpot's SMTP API?
  - id: get-/marketing/transactional/2026-09/smtp-tokens/{tokenId}_getTokenById
    intent: Look up one SMTP API token
    question: Can I see the details of one SMTP token if I know its token ID?
  - id: delete-/marketing/transactional/2026-09/smtp-tokens/{tokenId}_archiveToken
    intent: Delete an SMTP API token
    question: Is there a way to delete an SMTP token I'm no longer using?
  - id: post-/marketing/transactional/2026-09/smtp-tokens/{tokenId}/password-reset_resetPassword
    intent: Rotate the password of an SMTP token
    question: How do I rotate the password on an SMTP token while keeping the token itself?
  phrasing_ops: 5
  slug: hubspot-smtp-tokens-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Spend API from HubSpot — 2 operation(s) for spend.
  name: HubSpot Spend API
  phrasing_intents:
  - id: post-/marketing/campaigns/2026-03/{campaignGuid}/spend
    intent: Add a spend item to a campaign
    question: How do I record money spent on a marketing campaign?
  - id: get-/marketing/campaigns/2026-03/{campaignGuid}/spend/{spendId}
    intent: Get a campaign spend item
    question: Where can I see the amount recorded for one spend item on a campaign?
  - id: put-/marketing/campaigns/2026-03/{campaignGuid}/spend/{spendId}
    intent: Update a campaign spend item
    question: How do I correct the amount on a spend item I already logged for a campaign?
  - id: delete-/marketing/campaigns/2026-03/{campaignGuid}/spend/{spendId}
    intent: Delete a campaign spend item
    question: Can I remove a spend entry that was logged against the wrong campaign?
  phrasing_ops: 4
  slug: hubspot-spend-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Status API from HubSpot — 3 operation(s) for status.
  name: HubSpot Status API
  phrasing_intents:
  - id: post-/communication-preferences/2026-09/links/generate_/communication-preferences/v4/links/generate
    intent: Generate subscription preference links
    question: How do I get a manage-preferences or unsubscribe link for a specific subscriber?
  - id: get-/communication-preferences/2026-09/statuses/{subscriberIdString}
    intent: Get a contact's subscription preferences
    question: Which email subscriptions is a contact currently opted into?
  - id: post-/communication-preferences/2026-09/statuses/{subscriberIdString}
    intent: Set a contact's status for one subscription
    question: How do I subscribe or unsubscribe a contact from one specific email type?
  - id: get-/communication-preferences/2026-09/statuses/{subscriberIdString}/unsubscribe-all
    intent: Check if a contact opted out of everything
    question: Has this contact unsubscribed from all emails?
  phrasing_ops: 4
  slug: hubspot-status-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Subscriber State Changes API from HubSpot — 2 operation(s) for subscriber state changes.
  name: HubSpot Subscriber State Changes API
  phrasing_intents:
  - id: post-/marketing/marketing-events/2026-09/events/{externalEventId}/{subscriberState}/email-upsert_upsertByContactEmail
    intent: Record event attendance state by contact email
    question: How do I mark a list of contacts as registered or attended for a marketing event using their email addresses?
  - id: post-/marketing/marketing-events/2026-09/events/{externalEventId}/{subscriberState}/upsert_upsertByContactId
    intent: Record event attendance state by contact ID
    question: Can I record that contacts cancelled or attended an event when I only have their HubSpot contact IDs?
  phrasing_ops: 2
  slug: hubspot-subscriber-state-changes-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Tables API from HubSpot — 13 operation(s) for tables.
  name: HubSpot Tables API
  phrasing_intents:
  - id: get-/cms/v3/hubdb/2026-09/tables_getAllTables
    intent: List all published HubDB tables
    question: Which HubDB tables are live on my site right now, with their columns?
  - id: post-/cms/v3/hubdb/2026-09/tables_createTable
    intent: Create a new HubDB table
    question: How do I create a new HubDB table with my own columns?
  - id: get-/cms/v3/hubdb/2026-09/tables/draft_getAllDraftTables
    intent: List all draft HubDB tables
    question: What unpublished draft HubDB tables exist in my account?
  - id: get-/cms/v3/hubdb/2026-09/tables/{tableIdOrName}_getTableDetails
    intent: Get a published HubDB table's details
    question: How many rows does my published HubDB table have and what are its columns?
  - id: delete-/cms/v3/hubdb/2026-09/tables/{tableIdOrName}_archiveTable
    intent: Archive a HubDB table
    question: How do I archive a HubDB table I no longer use?
  - id: get-/cms/v3/hubdb/2026-09/tables/{tableIdOrName}/draft_getDraftTableDetailsById
    intent: Get a draft HubDB table's details
    question: What columns does the draft version of my HubDB table have before I publish?
  - id: patch-/cms/v3/hubdb/2026-09/tables/{tableIdOrName}/draft_updateDraftTable
    intent: Update a draft HubDB table's schema
    question: How do I add or remove columns on an existing HubDB table?
  - id: post-/cms/v3/hubdb/2026-09/tables/{tableIdOrName}/draft/clone_cloneDraftTable
    intent: Clone a HubDB table
    question: Can I duplicate an existing HubDB table under a new name?
  phrasing_ops: 16
  slug: hubspot-tables-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Teams API from HubSpot — 1 operation(s) for teams.
  name: HubSpot Teams API
  phrasing_intents:
  - id: get-/settings/users/2026-03/teams_getAll
    intent: List the account's teams
    question: What teams are set up in my HubSpot account?
  phrasing_ops: 1
  slug: hubspot-teams-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Threads API from HubSpot — 3 operation(s) for threads.
  name: HubSpot Threads API
  phrasing_intents:
  - id: get-/conversations/v3/conversations/threads
    intent: List conversation threads
    question: How do I list the conversation threads in a specific inbox?
  - id: get-/conversations/v3/conversations/threads/{threadId}
    intent: Get one conversation thread
    question: What details can I see about a single conversation thread?
  - id: delete-/conversations/v3/conversations/threads/{threadId}
    intent: Archive a conversation thread
    question: What happens to a conversation thread after I archive it?
  - id: patch-/conversations/v3/conversations/threads/{threadId}
    intent: Close, reopen or restore a thread
    question: How do I mark a conversation thread as closed?
  - id: get-/conversations/v3/conversations/threads/{threadId}/messages
    intent: Get a thread's message history
    question: Where can I read every message exchanged in a conversation thread?
  - id: post-/conversations/v3/conversations/threads/{threadId}/messages
    intent: Send a message on a thread
    question: Can I reply to a customer conversation thread through the API?
  phrasing_ops: 6
  slug: hubspot-threads-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Users API from HubSpot — 1 operation(s) for users.
  name: HubSpot Users API
  phrasing_intents:
  - id: get-/settings/users/2026-03/{userId}_getById
    intent: Look up a user in the account
    question: Which role and teams does a given user in my HubSpot account have?
  - id: put-/settings/users/2026-03/{userId}_update
    intent: Change a user's name, role or teams
    question: How do I change a user's role through the API?
  - id: delete-/settings/users/2026-03/{userId}_archive
    intent: Remove a user from the account
    question: Someone left the company; can I remove their user seat through the API?
  phrasing_ops: 3
  slug: hubspot-users-api
- baseURL: https://api.hubapi.com
  baseurl_source: declared
  description: The Website pages API from HubSpot — 7 operation(s) for website pages.
  name: HubSpot Website pages API
  phrasing_intents:
  - id: put-/cms/pages/2026-09/landing-pages/multi-language/set-new-lang-primary_setLangPrimary
    intent: Make a page the primary language in its group
    question: How do I change which translation is the primary language of a multi-language page group?
  - id: get-/cms/pages/2026-09/site-pages_getPage
    intent: List website pages
    question: How do I get every website page on my HubSpot site?
  - id: post-/cms/pages/2026-09/site-pages_create
    intent: Create a website page
    question: How do I add a new page to my website through the API?
  - id: post-/cms/pages/2026-09/site-pages/clone_clone
    intent: Clone a website page
    question: Can I duplicate an existing website page to use as a starting point?
  - id: post-/cms/pages/2026-09/site-pages/schedule_schedule
    intent: Schedule a website page to publish
    question: How do I schedule a website page to publish at a future time?
  - id: get-/cms/pages/2026-09/site-pages/{objectId}_getById
    intent: Get a live website page
    question: How can I fetch the details of one website page by its ID?
  - id: delete-/cms/pages/2026-09/site-pages/{objectId}_archive
    intent: Delete a website page
    question: Can I delete a page from my website that's no longer needed?
  - id: patch-/cms/pages/2026-09/site-pages/{objectId}_update
    intent: Update a live website page
    question: How do I change a published website page's title directly, not through its draft?
  phrasing_ops: 11
  slug: hubspot-website-pages-api
arazzos:
- description: Create a note engagement and associate it to a CRM record.
  name: HubSpot Add a Note to a Record
  slug: hubspot-add-note-to-record-workflow
- description: Find a deal by name and move it to a new pipeline stage.
  name: HubSpot Advance a Deal Stage
  slug: hubspot-advance-deal-stage-workflow
- description: Create an association between two CRM objects, then list it back to verify.
  name: HubSpot Associate Two CRM Records
  slug: hubspot-associate-records-workflow
- description: Batch-create a set of contacts then batch-read them back to verify.
  name: HubSpot Batch Import Contacts
  slug: hubspot-batch-import-contacts-workflow
- description: Discover available analytics event types, then query event instances for a CRM object.
  name: HubSpot Query Behavioral Analytics Events
  slug: hubspot-capture-analytics-event-workflow
- description: Create a CMS site page in draft, then publish its draft live.
  name: HubSpot Create and Publish a CMS Page
  slug: hubspot-create-cms-page-workflow
- description: Create a contact, create a company, and associate the two records.
  name: HubSpot Create a Contact With a Company
  slug: hubspot-create-contact-with-company-workflow
- description: Create a deal and associate it to an existing contact and company.
  name: HubSpot Create a Deal With Associations
  slug: hubspot-create-deal-with-associations-workflow
- description: Create a task engagement with a due date and associate it to a record.
  name: HubSpot Create a Follow-up Task
  slug: hubspot-create-followup-task-workflow
- description: Find a contact by email, create a support ticket, and associate them.
  name: HubSpot Create a Ticket For a Contact
  slug: hubspot-create-ticket-for-contact-workflow
- description: List commerce payments, then retrieve the full record for the first payment.
  name: HubSpot List and Read Commerce Payments
  slug: hubspot-list-payments-workflow
- description: Create a call engagement and associate it to a contact in a single flow.
  name: HubSpot Log a Call on a Contact
  slug: hubspot-log-call-on-contact-workflow
- description: Create an email engagement and associate it to a contact.
  name: HubSpot Log an Email Engagement
  slug: hubspot-log-email-engagement-workflow
- description: Create a meeting engagement and associate it to a deal.
  name: HubSpot Log a Meeting on a Deal
  slug: hubspot-log-meeting-on-deal-workflow
- description: Create a HubDB table, add a row to its draft, then publish the table.
  name: HubSpot Manage a HubDB Table
  slug: hubspot-manage-hubdb-table-workflow
- description: Retrieve a commerce subscription, then update its properties or archive it.
  name: HubSpot Manage a Commerce Subscription
  slug: hubspot-manage-subscription-workflow
- description: Exchange an authorization code for tokens, refresh the access token, then read its metadata.
  name: HubSpot OAuth Token Lifecycle
  slug: hubspot-oauth-token-lifecycle-workflow
- description: Resolve or create a blog author, create a blog post, then publish or schedule it.
  name: HubSpot Publish a Blog Post
  slug: hubspot-publish-blog-post-workflow
- description: List conversation threads, retrieve one, then send a reply message.
  name: HubSpot Respond to a Conversation
  slug: hubspot-respond-to-conversation-workflow
- description: Search CRM objects with a filter, then add the matches to a static list.
  name: HubSpot Search and Add to a List
  slug: hubspot-search-and-add-to-list-workflow
- description: Create an SMTP token for a campaign, read it back, then send a transactional email.
  name: HubSpot Send a Transactional Marketing Email
  slug: hubspot-send-marketing-email-workflow
- description: List tasks then update a task's status and priority.
  name: HubSpot Triage Tasks
  slug: hubspot-triage-tasks-workflow
- description: Find a contact by email and update it if it exists, otherwise create it.
  name: HubSpot Upsert a Contact
  slug: hubspot-upsert-contact-workflow
artifact_total: 2538
asyncapis:
- description: 'The HubSpot Webhooks API enables real-time event notifications for changes to CRM objects and conversations in a HubSpot portal. When subscribed events occur, HubSpot delivers HTTP POST requests to a '
  name: HubSpot Webhooks API
  slug: hubspot-webhooks-asyncapi
collections:
- collection_type: postman
  name: HubSpot Analytics Events API
  slug: postman-hubspot-analytics-events-api
- collection_type: postman
  name: HubSpot Blog Authors API
  slug: postman-hubspot-authors-api
- collection_type: postman
  name: HubSpot Blog Posts API
  slug: postman-hubspot-blog-posts-api
- collection_type: postman
  name: HubSpot CMS HubDB API
  slug: postman-hubspot-cms-hubdb-api
- collection_type: postman
  name: HubSpot CMS Pages API
  slug: postman-hubspot-cms-pages-api
- collection_type: postman
  name: HubSpot Commerce Payments API
  slug: postman-hubspot-commerce-payments-api
- collection_type: postman
  name: HubSpot Commerce Subscriptions API
  slug: postman-hubspot-commerce-subscriptions-api
- collection_type: postman
  name: HubSpot Conversations API
  slug: postman-hubspot-conversations-api
- collection_type: postman
  name: HubSpot CRM Associations API
  slug: postman-hubspot-crm-associations-api
- collection_type: postman
  name: HubSpot CRM Companies API
  slug: postman-hubspot-crm-companies-api
- collection_type: postman
  name: HubSpot CRM Contacts API
  slug: postman-hubspot-crm-contacts-api
- collection_type: postman
  name: HubSpot CRM Deals API
  slug: postman-hubspot-crm-deals-api
- collection_type: postman
  name: HubSpot CRM Feature Flags API
  slug: postman-hubspot-crm-feature-flags-api
- collection_type: postman
  name: HubSpot CRM Lists API
  slug: postman-hubspot-crm-lists-api
- collection_type: postman
  name: HubSpot CRM Search API
  slug: postman-hubspot-crm-search-api
- collection_type: postman
  name: HubSpot CRM Tickets API
  slug: postman-hubspot-crm-tickets-api
- collection_type: postman
  name: HubSpot Custom Workflow Actions API
  slug: postman-hubspot-custom-workflow-actions-api
- collection_type: postman
  name: HubSpot CMS Domains API
  slug: postman-hubspot-domains-api
- collection_type: postman
  name: HubSpot CRM Engagement Calls API
  slug: postman-hubspot-engagement-calls-api
- collection_type: postman
  name: HubSpot Engagement Emails API
  slug: postman-hubspot-engagement-emails-api
- collection_type: postman
  name: HubSpot Engagement Meetings API
  slug: postman-hubspot-engagement-meetings-api
- collection_type: postman
  name: HubSpot CRM Engagement Notes API
  slug: postman-hubspot-engagement-notes
- collection_type: postman
  name: HubSpot Engagement Tasks API
  slug: postman-hubspot-engagement-tasks-api
- collection_type: postman
  name: HubSpot Marketing Transactional Email API
  slug: postman-hubspot-marketing-emal-api
- collection_type: postman
  name: HubSpot OAuth API
  slug: postman-hubspot-oauth-api
- collection_type: postman
  name: HubSpot CMS Source Code API
  slug: postman-hubspot-source-code-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens API
  slug: open-hubspot-access-tokens-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Action Definitions API
  slug: open-hubspot-action-definitions-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Action Functions API
  slug: open-hubspot-action-functions-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Actors API
  slug: open-hubspot-actors-api
- collection_type: open
  name: HubSpot Analytics Events API
  slug: open-hubspot-analytics-events-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Application Feature Flags API
  slug: open-hubspot-application-feature-flags-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Association Label Management API
  slug: open-hubspot-association-label-management-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Association Type Definitions API
  slug: open-hubspot-association-type-definitions-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Associations API
  slug: open-hubspot-associations-api
- collection_type: open
  name: HubSpot Blog Authors API
  slug: open-hubspot-authors-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Basic Operations API
  slug: open-hubspot-basic-operations-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Batch API
  slug: open-hubspot-batch-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Batch Association Operations API
  slug: open-hubspot-batch-association-operations-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Batch Operations API
  slug: open-hubspot-batch-operations-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Batch Portal Operations API
  slug: open-hubspot-batch-portal-operations-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Blog Authors API
  slug: open-hubspot-blog-authors-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Blog Posts API
  slug: open-hubspot-blog-posts-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Channels API
  slug: open-hubspot-channels-api
- collection_type: open
  name: HubSpot CMS HubDB API
  slug: open-hubspot-cms-hubdb-api
- collection_type: open
  name: HubSpot CMS Pages API
  slug: open-hubspot-cms-pages-api
- collection_type: open
  name: HubSpot Commerce Payments API
  slug: open-hubspot-commerce-payments-api
- collection_type: open
  name: HubSpot Commerce Subscriptions API
  slug: open-hubspot-commerce-subscriptions-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Companies API
  slug: open-hubspot-companies-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Contacts API
  slug: open-hubspot-contacts-api
- collection_type: open
  name: HubSpot Conversations API
  slug: open-hubspot-conversations-api
- collection_type: open
  name: HubSpot CRM Associations API
  slug: open-hubspot-crm-associations-api
- collection_type: open
  name: HubSpot CRM Companies API
  slug: open-hubspot-crm-companies-api
- collection_type: open
  name: HubSpot CRM Contacts API
  slug: open-hubspot-crm-contacts-api
- collection_type: open
  name: HubSpot CRM Deals API
  slug: open-hubspot-crm-deals-api
- collection_type: open
  name: HubSpot CRM Feature Flags API
  slug: open-hubspot-crm-feature-flags-api
- collection_type: open
  name: HubSpot CRM Lists API
  slug: open-hubspot-crm-lists-api
- collection_type: open
  name: HubSpot CRM Search API
  slug: open-hubspot-crm-search-api
- collection_type: open
  name: HubSpot CRM Tickets API
  slug: open-hubspot-crm-tickets-api
- collection_type: open
  name: HubSpot Custom Workflow Actions API
  slug: open-hubspot-custom-workflow-actions-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Deals API
  slug: open-hubspot-deals-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Definition Revisions API
  slug: open-hubspot-definition-revisions-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Domain Management API
  slug: open-hubspot-domain-management-api
- collection_type: open
  name: HubSpot CMS Domains API
  slug: open-hubspot-domains-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Drafts and Revisions API
  slug: open-hubspot-drafts-and-revisions-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Emails API
  slug: open-hubspot-emails-api
- collection_type: open
  name: HubSpot CRM Engagement Calls API
  slug: open-hubspot-engagement-calls-api
- collection_type: open
  name: HubSpot Engagement Emails API
  slug: open-hubspot-engagement-emails-api
- collection_type: open
  name: HubSpot Engagement Meetings API
  slug: open-hubspot-engagement-meetings-api
- collection_type: open
  name: HubSpot CRM Engagement Notes API
  slug: open-hubspot-engagement-notes
- collection_type: open
  name: HubSpot Engagement Tasks API
  slug: open-hubspot-engagement-tasks-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Event Instances API
  slug: open-hubspot-event-instances-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Event Types API
  slug: open-hubspot-event-types-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens File Content API
  slug: open-hubspot-file-content-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens File Extraction API
  slug: open-hubspot-file-extraction-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens File Metadata API
  slug: open-hubspot-file-metadata-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens File Validation API
  slug: open-hubspot-file-validation-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens GDPR Compliance API
  slug: open-hubspot-gdpr-compliance-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Inboxes API
  slug: open-hubspot-inboxes-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Landing Pages API
  slug: open-hubspot-landing-pages-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Lists API
  slug: open-hubspot-lists-api
- collection_type: open
  name: HubSpot Marketing Transactional Email API
  slug: open-hubspot-marketing-emal-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Meetings API
  slug: open-hubspot-meetings-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Memberships API
  slug: open-hubspot-memberships-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Messages API
  slug: open-hubspot-messages-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Multi-Language Management API
  slug: open-hubspot-multi-language-management-api
- collection_type: open
  name: HubSpot OAuth API
  slug: open-hubspot-oauth-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Object Associations API
  slug: open-hubspot-object-associations-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Payment Search API
  slug: open-hubspot-payment-search-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Portal Flag States API
  slug: open-hubspot-portal-flag-states-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Post Cloning API
  slug: open-hubspot-post-cloning-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Publishing and Scheduling API
  slug: open-hubspot-publishing-and-scheduling-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Refresh Tokens API
  slug: open-hubspot-refresh-tokens-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Rows API
  slug: open-hubspot-rows-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Search API
  slug: open-hubspot-search-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Single Payment Operations API
  slug: open-hubspot-single-payment-operations-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Single Send API
  slug: open-hubspot-single-send-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Site Pages API
  slug: open-hubspot-site-pages-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens SMTP Token Management API
  slug: open-hubspot-smtp-token-management-api
- collection_type: open
  name: HubSpot CMS Source Code API
  slug: open-hubspot-source-code-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Subscriptions API
  slug: open-hubspot-subscriptions-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Tables API
  slug: open-hubspot-tables-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Tasks API
  slug: open-hubspot-tasks-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Threads API
  slug: open-hubspot-threads-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Tickets API
  slug: open-hubspot-tickets-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Token Management API
  slug: open-hubspot-token-management-api
- collection_type: open
  name: HubSpot Analytics Events Access Tokens Workflow Callbacks API
  slug: open-hubspot-workflow-callbacks-api
common:
- group: design
  href: https://artifacts.apis.io/hubspot/conventions/hubspot-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/hubspot-conventions.yml
- group: design
  href: https://artifacts.apis.io/hubspot/rules/hubspot-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/hubspot-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/hubspot/rules/hubspot-rules.yml
  title: ''
  type: Spectral
  url: rules/hubspot-rules.yml
- group: design
  href: https://artifacts.apis.io/hubspot/rules/hubspot-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/hubspot-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/hubspot/rules/hubspot-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/hubspot-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-source-code-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-source-code-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-oauth-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-oauth-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-marketing-emal-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-marketing-emal-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-engagement-tasks-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-tasks-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-engagement-notes-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-engagement-meetings-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-meetings-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-engagement-emails-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-emails-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-engagement-calls-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-calls-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-domains-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-domains-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-custom-workflow-actions-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-custom-workflow-actions-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-crm-tickets-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-tickets-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-crm-search-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-search-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-crm-lists-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-lists-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-crm-feature-flags-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-feature-flags-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-crm-deals-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-deals-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-crm-contacts-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-contacts-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-crm-companies-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-companies-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-crm-associations-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-associations-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-conversations-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-conversations-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-commerce-subscriptions-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-commerce-subscriptions-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-commerce-payments-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-commerce-payments-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-cms-pages-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-cms-pages-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-cms-hubdb-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-cms-hubdb-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-blog-posts-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-blog-posts-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-authors-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-authors-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-analytics-events-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-analytics-events-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/vocabulary/hubspot-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hubspot-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/hubspot/hosts/hubspot-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hubspot-hosts.yml
- group: build
  href: https://artifacts.apis.io/hubspot/integrations/hubspot-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/hubspot-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/hubspot/vendors/hubspot-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hubspot-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.hubspot.com/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.hubspot.com/company/management
- group: commercial
  href: https://artifacts.apis.io/hubspot/finops/hubspot-finops.yml
  title: ''
  type: FinOps
  url: finops/hubspot-finops.yml
- group: other
  href: https://artifacts.apis.io/hubspot/vendor-facets/hubspot-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/hubspot-vendor-facets.yml
- group: company
  title: ''
  type: Website
  url: https://www.hubspot.com/
- group: other
  href: https://artifacts.apis.io/hubspot/capabilities/hubspot-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/hubspot-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/HubSpot/mcp-server/issues
- group: agent
  href: https://artifacts.apis.io/hubspot/agentic-access/hubspot-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hubspot-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/hubspot/security/hubspot-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/hubspot-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/hubspot/security/hubspot-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/hubspot-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/hubspot/security/hubspot-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hubspot-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/hubspot/authentication/hubspot-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hubspot-authentication.yml
- group: auth
  href: https://artifacts.apis.io/hubspot/scopes/hubspot-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/hubspot-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/hubspot/overview
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-add-note-to-record-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-add-note-to-record-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-advance-deal-stage-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-advance-deal-stage-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-associate-records-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-associate-records-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-batch-import-contacts-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-batch-import-contacts-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-capture-analytics-event-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-capture-analytics-event-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-create-cms-page-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-create-cms-page-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-create-contact-with-company-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-create-contact-with-company-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-create-deal-with-associations-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-create-deal-with-associations-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-create-followup-task-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-create-followup-task-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-create-ticket-for-contact-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-create-ticket-for-contact-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-list-payments-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-list-payments-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-log-call-on-contact-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-log-call-on-contact-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-log-email-engagement-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-log-email-engagement-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-log-meeting-on-deal-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-log-meeting-on-deal-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-manage-hubdb-table-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-manage-hubdb-table-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-manage-subscription-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-manage-subscription-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-oauth-token-lifecycle-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-oauth-token-lifecycle-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-publish-blog-post-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-publish-blog-post-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-respond-to-conversation-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-respond-to-conversation-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-search-and-add-to-list-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-search-and-add-to-list-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-send-marketing-email-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-send-marketing-email-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-triage-tasks-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-triage-tasks-workflow.yml
- group: design
  href: https://artifacts.apis.io/hubspot/arazzo/hubspot-upsert-contact-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/hubspot-upsert-contact-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hubspot
- group: docs
  title: ''
  type: APIReference
  url: https://developers.hubspot.com/docs/api-reference/overview
- group: start
  title: ''
  type: Portal
  url: https://developers.hubspot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.hubspot.com/docs/api/overview
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.hubspot.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://community.hubspot.com/t5/HubSpot-Developers/ct-p/developers
- group: operate
  title: ''
  type: Support
  url: https://developers.hubspot.com/slack
- group: company
  title: ''
  type: Blog
  url: https://developers.hubspot.com/blog
- group: company
  title: ''
  type: Newsletter
  url: https://offers.hubspot.com/developer-newsletter-signup
- group: other
  title: ''
  type: Events
  url: https://www.hubspot.com/developer-community-events
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.hubspot.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.hubspot.com/terms-of-service
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.hubspot.com/docs/getting-started/developer-overview
- group: docs
  title: ''
  type: Documentation
  url: https://developers.hubspot.com/docs/guides/api
- group: docs
  title: ''
  type: Documentation
  url: https://developers.hubspot.com/docs/reference/api/overview
- group: start
  title: ''
  type: Login
  url: https://app.hubspot.com/login
- group: operate
  title: ''
  type: Contact
  url: https://offers.hubspot.com/crm-platform-demo
- group: docs
  title: ''
  type: Documentation
  url: https://www.hubspot.com/our-story
- group: company
  title: ''
  type: Blog
  url: https://blog.hubspot.com/
- group: auth
  title: ''
  type: Security
  url: https://legal.hubspot.com/security
- group: company
  title: ''
  type: Partners
  url: https://www.hubspot.com/partners/affiliates
- group: company
  title: ''
  type: Partners
  url: https://www.hubspot.com/partners
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hubspot.com/pricing/marketing/enterprise
- group: other
  title: ''
  type: Showcase
  url: https://www.hubspot.com/case-studies
- group: start
  title: ''
  type: Signup
  url: https://app.hubspot.com/signup/developers
- group: auth
  title: ''
  type: Authentication
  url: https://developers.hubspot.com/docs/api/intro-to-auth
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.hubspot.com/docs/developer-tooling/platform/usage-guidelines
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hubspot.com
- group: operate
  title: ''
  type: Support
  url: https://community.hubspot.com/t5/APIs-Integrations/bd-p/integrations
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HubSpot
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/HubSpot/HubSpot-public-api-spec-collection
- group: build
  title: ''
  type: SDKs
  url: https://developers.hubspot.com/docs/developer-tooling/sdks/node
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/hubspot
- group: other
  title: ''
  type: Resources
  url: https://www.postman.com/hubspot/hubspot-public-api-workspace/overview
- group: other
  title: ''
  type: Resources
  url: https://developers.hubspot.com/developer-tools
- group: docs
  title: ''
  type: APIReference
  url: https://developers.hubspot.com/apisbytier
- group: docs
  href: https://artifacts.apis.io/hubspot/json-schema/hubspot-crm-object-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/hubspot-crm-object-schema.json
- group: docs
  href: https://artifacts.apis.io/hubspot/json-schema/hubspot-crm-search-request-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/hubspot-crm-search-request-schema.json
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-context.jsonld
- group: build
  title: Python SDK
  type: SDKs
  url: https://pypi.org/project/hubspot-api-client/
- group: build
  title: Node.js SDK
  type: SDKs
  url: https://www.npmjs.com/package/@hubspot/api-client
- group: build
  title: Ruby SDK
  type: SDKs
  url: https://rubygems.org/gems/hubspot-api-client
- group: build
  title: PHP SDK
  type: SDKs
  url: https://packagist.org/packages/hubspot/api-client
- group: build
  title: HubSpot CLI
  type: CLI
  url: https://www.npmjs.com/package/@hubspot/cli
- group: build
  title: HubSpot MCP Server
  type: GitHubRepository
  url: https://github.com/HubSpot/mcp-server
- group: build
  title: Calling Extensions SDK
  type: SDKs
  url: https://github.com/HubSpot/calling-extensions-sdk
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-analytics-events-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-analytics-events-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-authors-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-authors-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-blog-posts-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-blog-posts-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-cms-hubdb-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-cms-hubdb-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-cms-pages-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-cms-pages-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-commerce-payments-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-commerce-payments-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-commerce-subscriptions-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-commerce-subscriptions-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-conversations-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-conversations-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-crm-associations-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-associations-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-crm-companies-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-companies-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-crm-contacts-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-contacts-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-crm-deals-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-deals-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-crm-feature-flags-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-feature-flags-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-crm-lists-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-lists-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-crm-search-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-search-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-crm-tickets-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-crm-tickets-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-custom-workflow-actions-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-custom-workflow-actions-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-domains-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-domains-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-engagement-calls-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-calls-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-engagement-emails-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-emails-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-engagement-meetings-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-meetings-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-engagement-notes-association-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-association-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-engagement-notes-batch-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-batch-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-engagement-notes-filter-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-filter-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-engagement-notes-gdpr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-gdpr-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-engagement-notes-next-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-next-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-engagement-notes-note-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-note-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-engagement-notes-paging-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-paging-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-engagement-notes-property-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-property-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-engagement-notes-sort-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-notes-sort-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-engagement-tasks-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-engagement-tasks-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-marketing-emal-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-marketing-emal-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-oauth-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-oauth-api-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubspot/json-ld/hubspot-source-code-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubspot-source-code-api-context.jsonld
- group: docs
  href: https://artifacts.apis.io/hubspot/rules/hubspot-spectral-rules.yml
  title: Spectral Rules
  type: Documentation
  url: rules/hubspot-spectral-rules.yml
- group: docs
  href: https://artifacts.apis.io/hubspot/vocabulary/hubspot-vocabulary.yaml
  title: Vocabulary
  type: Documentation
  url: vocabulary/hubspot-vocabulary.yaml
- group: agent
  href: https://artifacts.apis.io/hubspot/mcp/hubspot-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hubspot-mcp.yml
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/HubSpot/noc-skills
- group: build
  href: https://artifacts.apis.io/hubspot/packages/hubspot-packages.yml
  title: ''
  type: Packages
  url: packages/hubspot-packages.yml
- group: build
  href: https://artifacts.apis.io/hubspot/packages/hubspot-packages.yml
  title: ''
  type: SDKs
  url: packages/hubspot-packages.yml
- group: agent
  href: https://artifacts.apis.io/hubspot/well-known/hubspot-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hubspot-well-known.yml
- group: auth
  href: https://artifacts.apis.io/hubspot/well-known/hubspot-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/hubspot-security.txt
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/hubspot
- group: auth
  title: ''
  type: Compliance
  url: https://trust.hubspot.com/
- group: build
  href: https://artifacts.apis.io/hubspot/mcp/hubspot-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/hubspot-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/hubspot/llms/hubspot-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hubspot-llms.txt
- group: other
  href: https://artifacts.apis.io/hubspot/overlays/_index.yml
  title: ''
  type: Overlay
  url: overlays/_index.yml
- group: design
  href: https://artifacts.apis.io/hubspot/conformance/hubspot-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hubspot-conformance.yml
- group: design
  href: https://artifacts.apis.io/hubspot/errors/hubspot-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/hubspot-problem-types.yml
- group: design
  href: https://artifacts.apis.io/hubspot/lifecycle/hubspot-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hubspot-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hubspot.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.hubspot.com/changelog
- group: design
  href: https://artifacts.apis.io/hubspot/conventions/hubspot-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hubspot-conventions.yml
- group: operate
  href: https://artifacts.apis.io/hubspot/changelog/hubspot-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hubspot-changelog.yml
- group: build
  href: https://artifacts.apis.io/hubspot/cli/hubspot-cli.yml
  title: ''
  type: CLI
  url: cli/hubspot-cli.yml
- group: design
  href: https://artifacts.apis.io/hubspot/components/hubspot-components.yml
  title: ''
  type: Components
  url: components/hubspot-components.yml
- group: start
  href: https://artifacts.apis.io/hubspot/sandbox/hubspot-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/hubspot-sandbox.yml
- group: design
  href: https://artifacts.apis.io/hubspot/data-model/hubspot-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hubspot-data-model.yml
- group: docs
  href: https://artifacts.apis.io/hubspot/asyncapi/hubspot-webhooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/hubspot-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/hubspot/asyncapi/hubspot-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/hubspot-webhooks-asyncapi.yml
- group: agent
  href: https://artifacts.apis.io/hubspot/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/hubspot/plans/hubspot-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hubspot-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/hubspot/rate-limits/hubspot-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hubspot-rate-limits.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.hubspot.com/
- group: start
  title: ''
  type: SignUp
  url: https://app.hubspot.com/signup/developers
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/hubspot/hubspot-public-api-workspace/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developers.hubspot.com/docs/reference/api/other-resources/error-handling
created: 2023/11/14
description: HubSpot is an AI-native customer platform built around the Smart CRM, unifying marketing, sales, customer service, content, commerce and operations on a single shared customer record. Its developer platform exposes that record through a broad REST surface at api.hubapi.com covering CRM objects and associations, engagements, lists and segments, marketing and transactional email, CMS pages, blogs and HubDB, conversations, commerce payments and subscriptions, custom workflow actions, webhooks and analytics events. HubSpot ships first-party Node, Python, Ruby and PHP clients, a CLI, OAuth 2.0 with a granular scope model, a public developer changelog, date-based API versioning and a hosted MCP server for agents.
examples:
- key_count: 2
  name: Analytics Events Api Event Instance Collection Example
  slug: analytics-events-api-event-instance-collection-example
- key_count: 6
  name: Analytics Events Api Event Instance Example
  slug: analytics-events-api-event-instance-example
- key_count: 1
  name: Analytics Events Api Event Type Collection Example
  slug: analytics-events-api-event-type-collection-example
- key_count: 2
  name: Analytics Events Api Paging Example
  slug: analytics-events-api-paging-example
- key_count: 2
  name: Analytics Events Api Paging Next Example
  slug: analytics-events-api-paging-next-example
- key_count: 2
  name: Analytics Events Api Paging Previous Example
  slug: analytics-events-api-paging-previous-example
- key_count: 4
  name: Authors Api Attach To Language Group Request Example
  slug: authors-api-attach-to-language-group-request-example
- key_count: 1
  name: Authors Api Batch Archive Input Example
  slug: authors-api-batch-archive-input-example
- key_count: 1
  name: Authors Api Batch Create Input Example
  slug: authors-api-batch-create-input-example
- key_count: 1
  name: Authors Api Batch Input Example
  slug: authors-api-batch-input-example
- key_count: 2
  name: Authors Api Batch Input Item Example
  slug: authors-api-batch-input-item-example
- key_count: 1
  name: Authors Api Batch Read Input Example
  slug: authors-api-batch-read-input-example
- key_count: 6
  name: Authors Api Batch Response Example
  slug: authors-api-batch-response-example
- key_count: 3
  name: Authors Api Blog Author Collection Example
  slug: authors-api-blog-author-collection-example
- key_count: 15
  name: Authors Api Blog Author Example
  slug: authors-api-blog-author-example
- key_count: 9
  name: Authors Api Blog Author Input Example
  slug: authors-api-blog-author-input-example
- key_count: 2
  name: Authors Api Create Language Variation Request Example
  slug: authors-api-create-language-variation-request-example
- key_count: 1
  name: Authors Api Detach From Language Group Request Example
  slug: authors-api-detach-from-language-group-request-example
- key_count: 1
  name: Authors Api Paging Example
  slug: authors-api-paging-example
- key_count: 2
  name: Authors Api Paging Next Example
  slug: authors-api-paging-next-example
- key_count: 1
  name: Authors Api Set Language Primary Request Example
  slug: authors-api-set-language-primary-request-example
- key_count: 4
  name: Blog Posts Api Attach To Language Group Request Example
  slug: blog-posts-api-attach-to-language-group-request-example
- key_count: 1
  name: Blog Posts Api Batch Input Example
  slug: blog-posts-api-batch-input-example
- key_count: 1
  name: Blog Posts Api Batch Input Item Example
  slug: blog-posts-api-batch-input-item-example
- key_count: 6
  name: Blog Posts Api Batch Response Example
  slug: blog-posts-api-batch-response-example
- key_count: 3
  name: Blog Posts Api Blog Post Collection Example
  slug: blog-posts-api-blog-post-collection-example
- key_count: 32
  name: Blog Posts Api Blog Post Example
  slug: blog-posts-api-blog-post-example
- key_count: 15
  name: Blog Posts Api Blog Post Input Example
  slug: blog-posts-api-blog-post-input-example
- key_count: 1
  name: Blog Posts Api Clone Request Example
  slug: blog-posts-api-clone-request-example
- key_count: 2
  name: Blog Posts Api Create Language Variation Request Example
  slug: blog-posts-api-create-language-variation-request-example
- key_count: 1
  name: Blog Posts Api Detach From Language Group Request Example
  slug: blog-posts-api-detach-from-language-group-request-example
- key_count: 2
  name: Blog Posts Api Paging Example
  slug: blog-posts-api-paging-example
- key_count: 2
  name: Blog Posts Api Paging Next Example
  slug: blog-posts-api-paging-next-example
- key_count: 2
  name: Blog Posts Api Paging Previous Example
  slug: blog-posts-api-paging-previous-example
- key_count: 1
  name: Blog Posts Api Push Live Request Example
  slug: blog-posts-api-push-live-request-example
- key_count: 1
  name: Blog Posts Api Reset Draft Request Example
  slug: blog-posts-api-reset-draft-request-example
- key_count: 2
  name: Blog Posts Api Restore Previous Version Request Example
  slug: blog-posts-api-restore-previous-version-request-example
- key_count: 2
  name: Blog Posts Api Schedule Request Example
  slug: blog-posts-api-schedule-request-example
- key_count: 1
  name: Blog Posts Api Set Language Primary Request Example
  slug: blog-posts-api-set-language-primary-request-example
- key_count: 4
  name: Blog Posts Api Version History Example
  slug: blog-posts-api-version-history-example
- key_count: 2
  name: Cms Hubdb Api Collection Response Hub Dbrow Example
  slug: cms-hubdb-api-collection-response-hub-dbrow-example
- key_count: 2
  name: Cms Hubdb Api Collection Response Hub Dbtable Example
  slug: cms-hubdb-api-collection-response-hub-dbtable-example
- key_count: 5
  name: Cms Hubdb Api Hub Dbcolumn Example
  slug: cms-hubdb-api-hub-dbcolumn-example
- key_count: 1
  name: Cms Hubdb Api Hub Dbrow Create Request Example
  slug: cms-hubdb-api-hub-dbrow-create-request-example
- key_count: 4
  name: Cms Hubdb Api Hub Dbrow Example
  slug: cms-hubdb-api-hub-dbrow-example
- key_count: 3
  name: Cms Hubdb Api Hub Dbtable Create Request Example
  slug: cms-hubdb-api-hub-dbtable-create-request-example
- key_count: 9
  name: Cms Hubdb Api Hub Dbtable Example
  slug: cms-hubdb-api-hub-dbtable-example
- key_count: 1
  name: Cms Hubdb Api Paging Example
  slug: cms-hubdb-api-paging-example
- key_count: 2
  name: Cms Pages Api Collection Response Page Example
  slug: cms-pages-api-collection-response-page-example
- key_count: 8
  name: Cms Pages Api Page Create Request Example
  slug: cms-pages-api-page-create-request-example
- key_count: 16
  name: Cms Pages Api Page Example
  slug: cms-pages-api-page-example
- key_count: 5
  name: Cms Pages Api Page Update Request Example
  slug: cms-pages-api-page-update-request-example
- key_count: 1
  name: Cms Pages Api Paging Example
  slug: cms-pages-api-paging-example
- key_count: 2
  name: Commerce Payments Api Association Input Example
  slug: commerce-payments-api-association-input-example
- key_count: 2
  name: Commerce Payments Api Association Result Example
  slug: commerce-payments-api-association-result-example
- key_count: 2
  name: Commerce Payments Api Association Type Example
  slug: commerce-payments-api-association-type-example
- key_count: 1
  name: Commerce Payments Api Batch Archive Request Example
  slug: commerce-payments-api-batch-archive-request-example
- key_count: 1
  name: Commerce Payments Api Batch Create Request Example
  slug: commerce-payments-api-batch-create-request-example
- key_count: 8
  name: Commerce Payments Api Batch Create Response Example
  slug: commerce-payments-api-batch-create-response-example
- key_count: 8
  name: Commerce Payments Api Batch Error Example
  slug: commerce-payments-api-batch-error-example
- key_count: 1
  name: Commerce Payments Api Batch Read Input Item Example
  slug: commerce-payments-api-batch-read-input-item-example
- key_count: 4
  name: Commerce Payments Api Batch Read Request Example
  slug: commerce-payments-api-batch-read-request-example
- key_count: 8
  name: Commerce Payments Api Batch Read Response Example
  slug: commerce-payments-api-batch-read-response-example
- key_count: 3
  name: Commerce Payments Api Batch Update Input Item Example
  slug: commerce-payments-api-batch-update-input-item-example
- key_count: 1
  name: Commerce Payments Api Batch Update Request Example
  slug: commerce-payments-api-batch-update-request-example
- key_count: 8
  name: Commerce Payments Api Batch Update Response Example
  slug: commerce-payments-api-batch-update-response-example
- key_count: 2
  name: Commerce Payments Api Commerce Payment Collection Example
  slug: commerce-payments-api-commerce-payment-collection-example
- key_count: 8
  name: Commerce Payments Api Commerce Payment Example
  slug: commerce-payments-api-commerce-payment-example
- key_count: 2
  name: Commerce Payments Api Commerce Payment Input Example
  slug: commerce-payments-api-commerce-payment-input-example
- key_count: 1
  name: Commerce Payments Api Commerce Payment Patch Example
  slug: commerce-payments-api-commerce-payment-patch-example
- key_count: 5
  name: Commerce Payments Api Filter Example
  slug: commerce-payments-api-filter-example
- key_count: 1
  name: Commerce Payments Api Filter Group Example
  slug: commerce-payments-api-filter-group-example
- key_count: 2
  name: Commerce Payments Api Paging Example
  slug: commerce-payments-api-paging-example
- key_count: 6
  name: Commerce Payments Api Property History Example
  slug: commerce-payments-api-property-history-example
- key_count: 6
  name: Commerce Payments Api Search Request Example
  slug: commerce-payments-api-search-request-example
- key_count: 3
  name: Commerce Payments Api Search Response Example
  slug: commerce-payments-api-search-response-example
- key_count: 2
  name: Commerce Payments Api Sort Option Example
  slug: commerce-payments-api-sort-option-example
- key_count: 2
  name: Commerce Subscriptions Api Association Example
  slug: commerce-subscriptions-api-association-example
- key_count: 1
  name: Commerce Subscriptions Api Batch Create Input Example
  slug: commerce-subscriptions-api-batch-create-input-example
- key_count: 2
  name: Commerce Subscriptions Api Batch Read Input Example
  slug: commerce-subscriptions-api-batch-read-input-example
- key_count: 3
  name: Commerce Subscriptions Api Batch Response Subscription Example
  slug: commerce-subscriptions-api-batch-response-subscription-example
- key_count: 1
  name: Commerce Subscriptions Api Batch Update Input Example
  slug: commerce-subscriptions-api-batch-update-input-example
- key_count: 2
  name: Commerce Subscriptions Api Collection Response Association Example
  slug: commerce-subscriptions-api-collection-response-association-example
- key_count: 2
  name: Commerce Subscriptions Api Collection Response Subscription Example
  slug: commerce-subscriptions-api-collection-response-subscription-example
- key_count: 3
  name: Commerce Subscriptions Api Filter Example
  slug: commerce-subscriptions-api-filter-example
- key_count: 1
  name: Commerce Subscriptions Api Filter Group Example
  slug: commerce-subscriptions-api-filter-group-example
- key_count: 1
  name: Commerce Subscriptions Api Paging Example
  slug: commerce-subscriptions-api-paging-example
- key_count: 6
  name: Commerce Subscriptions Api Search Request Example
  slug: commerce-subscriptions-api-search-request-example
- key_count: 1
  name: Commerce Subscriptions Api Simple Public Object Input Example
  slug: commerce-subscriptions-api-simple-public-object-input-example
- key_count: 6
  name: Commerce Subscriptions Api Subscription Example
  slug: commerce-subscriptions-api-subscription-example
- key_count: 2
  name: Conversations Api Actor Collection Example
  slug: conversations-api-actor-collection-example
- key_count: 5
  name: Conversations Api Actor Example
  slug: conversations-api-actor-example
- key_count: 5
  name: Conversations Api Attachment Example
  slug: conversations-api-attachment-example
- key_count: 2
  name: Conversations Api Channel Collection Example
  slug: conversations-api-channel-collection-example
- key_count: 5
  name: Conversations Api Channel Example
  slug: conversations-api-channel-example
- key_count: 3
  name: Conversations Api Inbox Collection Example
  slug: conversations-api-inbox-collection-example
- key_count: 6
  name: Conversations Api Inbox Example
  slug: conversations-api-inbox-example
- key_count: 2
  name: Conversations Api Message Collection Example
  slug: conversations-api-message-collection-example
- key_count: 13
  name: Conversations Api Message Example
  slug: conversations-api-message-example
- key_count: 1
  name: Conversations Api Message Recipient Example
  slug: conversations-api-message-recipient-example
- key_count: 1
  name: Conversations Api Message Status Example
  slug: conversations-api-message-status-example
- key_count: 1
  name: Conversations Api Paging Example
  slug: conversations-api-paging-example
- key_count: 2
  name: Conversations Api Paging Next Example
  slug: conversations-api-paging-next-example
- key_count: 7
  name: Conversations Api Send Message Request Example
  slug: conversations-api-send-message-request-example
- key_count: 2
  name: Conversations Api Thread Collection Example
  slug: conversations-api-thread-collection-example
- key_count: 14
  name: Conversations Api Thread Example
  slug: conversations-api-thread-example
- key_count: 2
  name: Conversations Api Update Thread Request Example
  slug: conversations-api-update-thread-request-example
- key_count: 2
  name: Crm Associations Api Association Definition Collection Example
  slug: crm-associations-api-association-definition-collection-example
- key_count: 7
  name: Crm Associations Api Association Definition Example
  slug: crm-associations-api-association-definition-example
- key_count: 2
  name: Crm Associations Api Association Example
  slug: crm-associations-api-association-example
- key_count: 2
  name: Crm Associations Api Association Label Collection Example
  slug: crm-associations-api-association-label-collection-example
- key_count: 3
  name: Crm Associations Api Association Label Example
  slug: crm-associations-api-association-label-example
- key_count: 3
  name: Crm Associations Api Association Result Example
  slug: crm-associations-api-association-result-example
- key_count: 3
  name: Crm Associations Api Association Type Example
  slug: crm-associations-api-association-type-example
- key_count: 2
  name: Crm Associations Api Association Type Input Example
  slug: crm-associations-api-association-type-input-example
- key_count: 1
  name: Crm Associations Api Batch Association Archive Input Example
  slug: crm-associations-api-batch-association-archive-input-example
- key_count: 3
  name: Crm Associations Api Batch Association Archive Item Example
  slug: crm-associations-api-batch-association-archive-item-example
- key_count: 1
  name: Crm Associations Api Batch Association Create Input Example
  slug: crm-associations-api-batch-association-create-input-example
- key_count: 3
  name: Crm Associations Api Batch Association Create Item Example
  slug: crm-associations-api-batch-association-create-item-example
- key_count: 1
  name: Crm Associations Api Batch Association Read Input Example
  slug: crm-associations-api-batch-association-read-input-example
- key_count: 8
  name: Crm Associations Api Batch Association Response Example
  slug: crm-associations-api-batch-association-response-example
- key_count: 2
  name: Crm Associations Api Create Association Input Example
  slug: crm-associations-api-create-association-input-example
- key_count: 3
  name: Crm Associations Api Create Label Input Example
  slug: crm-associations-api-create-label-input-example
- key_count: 1
  name: Crm Associations Api Object Reference Example
  slug: crm-associations-api-object-reference-example
- key_count: 1
  name: Crm Associations Api Paging Example
  slug: crm-associations-api-paging-example
- key_count: 2
  name: Crm Associations Api Paging Next Example
  slug: crm-associations-api-paging-next-example
- key_count: 2
  name: Crm Companies Api Association Example
  slug: crm-companies-api-association-example
- key_count: 1
  name: Crm Companies Api Batch Archive Input Example
  slug: crm-companies-api-batch-archive-input-example
- key_count: 1
  name: Crm Companies Api Batch Create Input Example
  slug: crm-companies-api-batch-create-input-example
- key_count: 2
  name: Crm Companies Api Batch Read Input Example
  slug: crm-companies-api-batch-read-input-example
- key_count: 3
  name: Crm Companies Api Batch Response Company Example
  slug: crm-companies-api-batch-response-company-example
- key_count: 1
  name: Crm Companies Api Batch Update Input Example
  slug: crm-companies-api-batch-update-input-example
- key_count: 2
  name: Crm Companies Api Collection Response Association Example
  slug: crm-companies-api-collection-response-association-example
- key_count: 2
  name: Crm Companies Api Collection Response Company Example
  slug: crm-companies-api-collection-response-company-example
- key_count: 6
  name: Crm Companies Api Company Example
  slug: crm-companies-api-company-example
- key_count: 3
  name: Crm Companies Api Filter Example
  slug: crm-companies-api-filter-example
- key_count: 1
  name: Crm Companies Api Filter Group Example
  slug: crm-companies-api-filter-group-example
- key_count: 1
  name: Crm Companies Api Paging Example
  slug: crm-companies-api-paging-example
- key_count: 6
  name: Crm Companies Api Search Request Example
  slug: crm-companies-api-search-request-example
- key_count: 1
  name: Crm Companies Api Simple Public Object Input Example
  slug: crm-companies-api-simple-public-object-input-example
- key_count: 2
  name: Crm Contacts Api Association Example
  slug: crm-contacts-api-association-example
- key_count: 1
  name: Crm Contacts Api Batch Archive Input Example
  slug: crm-contacts-api-batch-archive-input-example
- key_count: 1
  name: Crm Contacts Api Batch Create Input Example
  slug: crm-contacts-api-batch-create-input-example
- key_count: 2
  name: Crm Contacts Api Batch Read Input Example
  slug: crm-contacts-api-batch-read-input-example
- key_count: 3
  name: Crm Contacts Api Batch Response Contact Example
  slug: crm-contacts-api-batch-response-contact-example
- key_count: 1
  name: Crm Contacts Api Batch Update Input Example
  slug: crm-contacts-api-batch-update-input-example
- key_count: 2
  name: Crm Contacts Api Collection Response Association Example
  slug: crm-contacts-api-collection-response-association-example
- key_count: 2
  name: Crm Contacts Api Collection Response Contact Example
  slug: crm-contacts-api-collection-response-contact-example
- key_count: 6
  name: Crm Contacts Api Contact Example
  slug: crm-contacts-api-contact-example
- key_count: 3
  name: Crm Contacts Api Filter Example
  slug: crm-contacts-api-filter-example
- key_count: 1
  name: Crm Contacts Api Filter Group Example
  slug: crm-contacts-api-filter-group-example
- key_count: 1
  name: Crm Contacts Api Paging Example
  slug: crm-contacts-api-paging-example
- key_count: 6
  name: Crm Contacts Api Search Request Example
  slug: crm-contacts-api-search-request-example
- key_count: 1
  name: Crm Contacts Api Simple Public Object Input Example
  slug: crm-contacts-api-simple-public-object-input-example
- key_count: 2
  name: Crm Deals Api Association Example
  slug: crm-deals-api-association-example
- key_count: 1
  name: Crm Deals Api Batch Archive Input Example
  slug: crm-deals-api-batch-archive-input-example
- key_count: 1
  name: Crm Deals Api Batch Create Input Example
  slug: crm-deals-api-batch-create-input-example
- key_count: 2
  name: Crm Deals Api Batch Read Input Example
  slug: crm-deals-api-batch-read-input-example
- key_count: 3
  name: Crm Deals Api Batch Response Deal Example
  slug: crm-deals-api-batch-response-deal-example
- key_count: 1
  name: Crm Deals Api Batch Update Input Example
  slug: crm-deals-api-batch-update-input-example
- key_count: 2
  name: Crm Deals Api Collection Response Association Example
  slug: crm-deals-api-collection-response-association-example
- key_count: 2
  name: Crm Deals Api Collection Response Deal Example
  slug: crm-deals-api-collection-response-deal-example
- key_count: 6
  name: Crm Deals Api Deal Example
  slug: crm-deals-api-deal-example
- key_count: 3
  name: Crm Deals Api Filter Example
  slug: crm-deals-api-filter-example
- key_count: 1
  name: Crm Deals Api Filter Group Example
  slug: crm-deals-api-filter-group-example
- key_count: 1
  name: Crm Deals Api Paging Example
  slug: crm-deals-api-paging-example
- key_count: 6
  name: Crm Deals Api Search Request Example
  slug: crm-deals-api-search-request-example
- key_count: 1
  name: Crm Deals Api Simple Public Object Input Example
  slug: crm-deals-api-simple-public-object-input-example
- key_count: 1
  name: Crm Feature Flags Api Batch Delete Input Example
  slug: crm-feature-flags-api-batch-delete-input-example
- key_count: 1
  name: Crm Feature Flags Api Batch Delete Input Item Example
  slug: crm-feature-flags-api-batch-delete-input-item-example
- key_count: 4
  name: Crm Feature Flags Api Batch Error Example
  slug: crm-feature-flags-api-batch-error-example
- key_count: 1
  name: Crm Feature Flags Api Batch Portal Flag State Input Example
  slug: crm-feature-flags-api-batch-portal-flag-state-input-example
- key_count: 2
  name: Crm Feature Flags Api Batch Portal Flag State Input Item Example
  slug: crm-feature-flags-api-batch-portal-flag-state-input-item-example
- key_count: 4
  name: Crm Feature Flags Api Batch Portal Flag State Response Example
  slug: crm-feature-flags-api-batch-portal-flag-state-response-example
- key_count: 5
  name: Crm Feature Flags Api Batch Portal Flag State Response With Errors Example
  slug: crm-feature-flags-api-batch-portal-flag-state-response-with-errors-example
- key_count: 4
  name: Crm Feature Flags Api Feature Flag Example
  slug: crm-feature-flags-api-feature-flag-example
- key_count: 1
  name: Crm Feature Flags Api Feature Flag Input Example
  slug: crm-feature-flags-api-feature-flag-input-example
- key_count: 1
  name: Crm Feature Flags Api Paging Example
  slug: crm-feature-flags-api-paging-example
- key_count: 2
  name: Crm Feature Flags Api Paging Next Example
  slug: crm-feature-flags-api-paging-next-example
- key_count: 2
  name: Crm Feature Flags Api Portal Flag State Collection Example
  slug: crm-feature-flags-api-portal-flag-state-collection-example
- key_count: 4
  name: Crm Feature Flags Api Portal Flag State Example
  slug: crm-feature-flags-api-portal-flag-state-example
- key_count: 1
  name: Crm Feature Flags Api Portal Flag State Input Example
  slug: crm-feature-flags-api-portal-flag-state-input-example
- key_count: 2
  name: Crm Lists Api Collection Response List Example
  slug: crm-lists-api-collection-response-list-example
- key_count: 2
  name: Crm Lists Api Collection Response Membership Example
  slug: crm-lists-api-collection-response-membership-example
- key_count: 4
  name: Crm Lists Api List Create Request Example
  slug: crm-lists-api-list-create-request-example
- key_count: 9
  name: Crm Lists Api List Example
  slug: crm-lists-api-list-example
- key_count: 2
  name: Crm Lists Api Membership Change Request Example
  slug: crm-lists-api-membership-change-request-example
- key_count: 4
  name: Crm Lists Api Membership Change Response Example
  slug: crm-lists-api-membership-change-response-example
- key_count: 2
  name: Crm Lists Api Membership Example
  slug: crm-lists-api-membership-example
- key_count: 1
  name: Crm Lists Api Paging Example
  slug: crm-lists-api-paging-example
- key_count: 5
  name: Crm Search Api Crmobject Example
  slug: crm-search-api-crmobject-example
- key_count: 5
  name: Crm Search Api Filter Example
  slug: crm-search-api-filter-example
- key_count: 1
  name: Crm Search Api Filter Group Example
  slug: crm-search-api-filter-group-example
- key_count: 1
  name: Crm Search Api Paging Example
  slug: crm-search-api-paging-example
- key_count: 6
  name: Crm Search Api Search Request Example
  slug: crm-search-api-search-request-example
- key_count: 3
  name: Crm Search Api Search Response Example
  slug: crm-search-api-search-response-example
- key_count: 2
  name: Crm Search Api Sort Example
  slug: crm-search-api-sort-example
- key_count: 2
  name: Crm Tickets Api Association Example
  slug: crm-tickets-api-association-example
- key_count: 1
  name: Crm Tickets Api Batch Archive Input Example
  slug: crm-tickets-api-batch-archive-input-example
- key_count: 1
  name: Crm Tickets Api Batch Create Input Example
  slug: crm-tickets-api-batch-create-input-example
- key_count: 2
  name: Crm Tickets Api Batch Read Input Example
  slug: crm-tickets-api-batch-read-input-example
- key_count: 3
  name: Crm Tickets Api Batch Response Ticket Example
  slug: crm-tickets-api-batch-response-ticket-example
- key_count: 1
  name: Crm Tickets Api Batch Update Input Example
  slug: crm-tickets-api-batch-update-input-example
- key_count: 2
  name: Crm Tickets Api Collection Response Association Example
  slug: crm-tickets-api-collection-response-association-example
- key_count: 2
  name: Crm Tickets Api Collection Response Ticket Example
  slug: crm-tickets-api-collection-response-ticket-example
- key_count: 3
  name: Crm Tickets Api Filter Example
  slug: crm-tickets-api-filter-example
- key_count: 1
  name: Crm Tickets Api Filter Group Example
  slug: crm-tickets-api-filter-group-example
- key_count: 1
  name: Crm Tickets Api Paging Example
  slug: crm-tickets-api-paging-example
- key_count: 6
  name: Crm Tickets Api Search Request Example
  slug: crm-tickets-api-search-request-example
- key_count: 1
  name: Crm Tickets Api Simple Public Object Input Example
  slug: crm-tickets-api-simple-public-object-input-example
- key_count: 6
  name: Crm Tickets Api Ticket Example
  slug: crm-tickets-api-ticket-example
- key_count: 2
  name: Custom Workflow Actions Api Action Definition Collection Example
  slug: custom-workflow-actions-api-action-definition-collection-example
- key_count: 10
  name: Custom Workflow Actions Api Action Definition Example
  slug: custom-workflow-actions-api-action-definition-example
- key_count: 7
  name: Custom Workflow Actions Api Action Definition Input Example
  slug: custom-workflow-actions-api-action-definition-input-example
- key_count: 7
  name: Custom Workflow Actions Api Action Definition Patch Example
  slug: custom-workflow-actions-api-action-definition-patch-example
- key_count: 2
  name: Custom Workflow Actions Api Action Definition Revision Collection Example
  slug: custom-workflow-actions-api-action-definition-revision-collection-example
- key_count: 3
  name: Custom Workflow Actions Api Action Definition Revision Example
  slug: custom-workflow-actions-api-action-definition-revision-example
- key_count: 1
  name: Custom Workflow Actions Api Action Function Collection Example
  slug: custom-workflow-actions-api-action-function-collection-example
- key_count: 3
  name: Custom Workflow Actions Api Action Function Example
  slug: custom-workflow-actions-api-action-function-example
- key_count: 1
  name: Custom Workflow Actions Api Action Function Input Example
  slug: custom-workflow-actions-api-action-function-input-example
- key_count: 2
  name: Custom Workflow Actions Api Action Function Reference Example
  slug: custom-workflow-actions-api-action-function-reference-example
- key_count: 4
  name: Custom Workflow Actions Api Action Labels Example
  slug: custom-workflow-actions-api-action-labels-example
- key_count: 1
  name: Custom Workflow Actions Api Batch Callback Completion Request Example
  slug: custom-workflow-actions-api-batch-callback-completion-request-example
- key_count: 3
  name: Custom Workflow Actions Api Batch Callback Error Example
  slug: custom-workflow-actions-api-batch-callback-error-example
- key_count: 2
  name: Custom Workflow Actions Api Batch Callback Input Example
  slug: custom-workflow-actions-api-batch-callback-input-example
- key_count: 2
  name: Custom Workflow Actions Api Batch Callback Response Example
  slug: custom-workflow-actions-api-batch-callback-response-example
- key_count: 1
  name: Custom Workflow Actions Api Callback Completion Request Example
  slug: custom-workflow-actions-api-callback-completion-request-example
- key_count: 3
  name: Custom Workflow Actions Api Field Option Example
  slug: custom-workflow-actions-api-field-option-example
- key_count: 6
  name: Custom Workflow Actions Api Field Type Definition Example
  slug: custom-workflow-actions-api-field-type-definition-example
- key_count: 3
  name: Custom Workflow Actions Api Input Field Example
  slug: custom-workflow-actions-api-input-field-example
- key_count: 1
  name: Custom Workflow Actions Api Object Request Options Example
  slug: custom-workflow-actions-api-object-request-options-example
- key_count: 1
  name: Custom Workflow Actions Api Output Field Example
  slug: custom-workflow-actions-api-output-field-example
- key_count: 1
  name: Custom Workflow Actions Api Paging Example
  slug: custom-workflow-actions-api-paging-example
- key_count: 3
  name: Domains Api Domain Collection Response Example
  slug: domains-api-domain-collection-response-example
- key_count: 21
  name: Domains Api Domain Example
  slug: domains-api-domain-example
- key_count: 1
  name: Domains Api Forward Paging Example
  slug: domains-api-forward-paging-example
- key_count: 2
  name: Domains Api Next Page Example
  slug: domains-api-next-page-example
- key_count: 2
  name: Engagement Calls Api Association Input Example
  slug: engagement-calls-api-association-input-example
- key_count: 2
  name: Engagement Calls Api Association Type Example
  slug: engagement-calls-api-association-type-example
- key_count: 1
  name: Engagement Calls Api Batch Archive Calls Request Example
  slug: engagement-calls-api-batch-archive-calls-request-example
- key_count: 7
  name: Engagement Calls Api Batch Calls Response Example
  slug: engagement-calls-api-batch-calls-response-example
- key_count: 1
  name: Engagement Calls Api Batch Create Calls Request Example
  slug: engagement-calls-api-batch-create-calls-request-example
- key_count: 5
  name: Engagement Calls Api Batch Error Example
  slug: engagement-calls-api-batch-error-example
- key_count: 4
  name: Engagement Calls Api Batch Read Calls Request Example
  slug: engagement-calls-api-batch-read-calls-request-example
- key_count: 1
  name: Engagement Calls Api Batch Read Input Example
  slug: engagement-calls-api-batch-read-input-example
- key_count: 1
  name: Engagement Calls Api Batch Update Calls Request Example
  slug: engagement-calls-api-batch-update-calls-request-example
- key_count: 2
  name: Engagement Calls Api Batch Update Input Example
  slug: engagement-calls-api-batch-update-input-example
- key_count: 2
  name: Engagement Calls Api Call Collection Response Example
  slug: engagement-calls-api-call-collection-response-example
- key_count: 2
  name: Engagement Calls Api Call Create Request Example
  slug: engagement-calls-api-call-create-request-example
- key_count: 7
  name: Engagement Calls Api Call Example
  slug: engagement-calls-api-call-example
- key_count: 6
  name: Engagement Calls Api Call Search Request Example
  slug: engagement-calls-api-call-search-request-example
- key_count: 3
  name: Engagement Calls Api Call Search Response Example
  slug: engagement-calls-api-call-search-response-example
- key_count: 1
  name: Engagement Calls Api Call Update Request Example
  slug: engagement-calls-api-call-update-request-example
- key_count: 5
  name: Engagement Calls Api Filter Example
  slug: engagement-calls-api-filter-example
- key_count: 1
  name: Engagement Calls Api Filter Group Example
  slug: engagement-calls-api-filter-group-example
- key_count: 2
  name: Engagement Calls Api Gdpr Delete Request Example
  slug: engagement-calls-api-gdpr-delete-request-example
- key_count: 2
  name: Engagement Calls Api Next Page Example
  slug: engagement-calls-api-next-page-example
- key_count: 1
  name: Engagement Calls Api Paging Example
  slug: engagement-calls-api-paging-example
- key_count: 6
  name: Engagement Calls Api Property History Example
  slug: engagement-calls-api-property-history-example
- key_count: 2
  name: Engagement Calls Api Sort Option Example
  slug: engagement-calls-api-sort-option-example
- key_count: 2
  name: Engagement Emails Api Association Example
  slug: engagement-emails-api-association-example
- key_count: 1
  name: Engagement Emails Api Batch Create Input Example
  slug: engagement-emails-api-batch-create-input-example
- key_count: 2
  name: Engagement Emails Api Batch Read Input Example
  slug: engagement-emails-api-batch-read-input-example
- key_count: 3
  name: Engagement Emails Api Batch Response Email Engagement Example
  slug: engagement-emails-api-batch-response-email-engagement-example
- key_count: 1
  name: Engagement Emails Api Batch Update Input Example
  slug: engagement-emails-api-batch-update-input-example
- key_count: 2
  name: Engagement Emails Api Collection Response Association Example
  slug: engagement-emails-api-collection-response-association-example
- key_count: 2
  name: Engagement Emails Api Collection Response Email Engagement Example
  slug: engagement-emails-api-collection-response-email-engagement-example
- key_count: 6
  name: Engagement Emails Api Email Engagement Example
  slug: engagement-emails-api-email-engagement-example
- key_count: 3
  name: Engagement Emails Api Filter Example
  slug: engagement-emails-api-filter-example
- key_count: 1
  name: Engagement Emails Api Filter Group Example
  slug: engagement-emails-api-filter-group-example
- key_count: 1
  name: Engagement Emails Api Paging Example
  slug: engagement-emails-api-paging-example
- key_count: 6
  name: Engagement Emails Api Search Request Example
  slug: engagement-emails-api-search-request-example
- key_count: 1
  name: Engagement Emails Api Simple Public Object Input Example
  slug: engagement-emails-api-simple-public-object-input-example
- key_count: 2
  name: Engagement Meetings Api Association Example
  slug: engagement-meetings-api-association-example
- key_count: 1
  name: Engagement Meetings Api Batch Create Input Example
  slug: engagement-meetings-api-batch-create-input-example
- key_count: 2
  name: Engagement Meetings Api Batch Read Input Example
  slug: engagement-meetings-api-batch-read-input-example
- key_count: 3
  name: Engagement Meetings Api Batch Response Meeting Example
  slug: engagement-meetings-api-batch-response-meeting-example
- key_count: 1
  name: Engagement Meetings Api Batch Update Input Example
  slug: engagement-meetings-api-batch-update-input-example
- key_count: 2
  name: Engagement Meetings Api Collection Response Association Example
  slug: engagement-meetings-api-collection-response-association-example
- key_count: 2
  name: Engagement Meetings Api Collection Response Meeting Example
  slug: engagement-meetings-api-collection-response-meeting-example
- key_count: 3
  name: Engagement Meetings Api Filter Example
  slug: engagement-meetings-api-filter-example
- key_count: 1
  name: Engagement Meetings Api Filter Group Example
  slug: engagement-meetings-api-filter-group-example
- key_count: 6
  name: Engagement Meetings Api Meeting Example
  slug: engagement-meetings-api-meeting-example
- key_count: 1
  name: Engagement Meetings Api Paging Example
  slug: engagement-meetings-api-paging-example
- key_count: 6
  name: Engagement Meetings Api Search Request Example
  slug: engagement-meetings-api-search-request-example
- key_count: 1
  name: Engagement Meetings Api Simple Public Object Input Example
  slug: engagement-meetings-api-simple-public-object-input-example
- key_count: 2
  name: Engagement Notes Association Input Example
  slug: engagement-notes-association-input-example
- key_count: 2
  name: Engagement Notes Association Type Example
  slug: engagement-notes-association-type-example
- key_count: 1
  name: Engagement Notes Batch Archive Notes Request Example
  slug: engagement-notes-batch-archive-notes-request-example
- key_count: 1
  name: Engagement Notes Batch Create Notes Request Example
  slug: engagement-notes-batch-create-notes-request-example
- key_count: 5
  name: Engagement Notes Batch Error Example
  slug: engagement-notes-batch-error-example
- key_count: 7
  name: Engagement Notes Batch Notes Response Example
  slug: engagement-notes-batch-notes-response-example
- key_count: 1
  name: Engagement Notes Batch Read Input Example
  slug: engagement-notes-batch-read-input-example
- key_count: 4
  name: Engagement Notes Batch Read Notes Request Example
  slug: engagement-notes-batch-read-notes-request-example
- key_count: 2
  name: Engagement Notes Batch Update Input Example
  slug: engagement-notes-batch-update-input-example
- key_count: 1
  name: Engagement Notes Batch Update Notes Request Example
  slug: engagement-notes-batch-update-notes-request-example
- key_count: 5
  name: Engagement Notes Filter Example
  slug: engagement-notes-filter-example
- key_count: 1
  name: Engagement Notes Filter Group Example
  slug: engagement-notes-filter-group-example
- key_count: 2
  name: Engagement Notes Gdpr Delete Request Example
  slug: engagement-notes-gdpr-delete-request-example
- key_count: 2
  name: Engagement Notes Next Page Example
  slug: engagement-notes-next-page-example
- key_count: 2
  name: Engagement Notes Note Collection Response Example
  slug: engagement-notes-note-collection-response-example
- key_count: 2
  name: Engagement Notes Note Create Request Example
  slug: engagement-notes-note-create-request-example
- key_count: 7
  name: Engagement Notes Note Example
  slug: engagement-notes-note-example
- key_count: 6
  name: Engagement Notes Note Search Request Example
  slug: engagement-notes-note-search-request-example
- key_count: 3
  name: Engagement Notes Note Search Response Example
  slug: engagement-notes-note-search-response-example
- key_count: 1
  name: Engagement Notes Note Update Request Example
  slug: engagement-notes-note-update-request-example
- key_count: 1
  name: Engagement Notes Paging Example
  slug: engagement-notes-paging-example
- key_count: 6
  name: Engagement Notes Property History Example
  slug: engagement-notes-property-history-example
- key_count: 2
  name: Engagement Notes Sort Option Example
  slug: engagement-notes-sort-option-example
- key_count: 2
  name: Engagement Tasks Api Association Example
  slug: engagement-tasks-api-association-example
- key_count: 1
  name: Engagement Tasks Api Batch Create Input Example
  slug: engagement-tasks-api-batch-create-input-example
- key_count: 2
  name: Engagement Tasks Api Batch Read Input Example
  slug: engagement-tasks-api-batch-read-input-example
- key_count: 3
  name: Engagement Tasks Api Batch Response Task Example
  slug: engagement-tasks-api-batch-response-task-example
- key_count: 1
  name: Engagement Tasks Api Batch Update Input Example
  slug: engagement-tasks-api-batch-update-input-example
- key_count: 2
  name: Engagement Tasks Api Collection Response Association Example
  slug: engagement-tasks-api-collection-response-association-example
- key_count: 2
  name: Engagement Tasks Api Collection Response Task Example
  slug: engagement-tasks-api-collection-response-task-example
- key_count: 3
  name: Engagement Tasks Api Filter Example
  slug: engagement-tasks-api-filter-example
- key_count: 1
  name: Engagement Tasks Api Filter Group Example
  slug: engagement-tasks-api-filter-group-example
- key_count: 1
  name: Engagement Tasks Api Paging Example
  slug: engagement-tasks-api-paging-example
- key_count: 6
  name: Engagement Tasks Api Search Request Example
  slug: engagement-tasks-api-search-request-example
- key_count: 1
  name: Engagement Tasks Api Simple Public Object Input Example
  slug: engagement-tasks-api-simple-public-object-input-example
- key_count: 6
  name: Engagement Tasks Api Task Example
  slug: engagement-tasks-api-task-example
- key_count: 5
  name: Hubspot Analytics Events Error Detail Example
  slug: hubspot-analytics-events-error-detail-example
- key_count: 7
  name: Hubspot Analytics Events Error Example
  slug: hubspot-analytics-events-error-example
- key_count: 2
  name: Hubspot Analytics Events Event Instance Collection Example
  slug: hubspot-analytics-events-event-instance-collection-example
- key_count: 6
  name: Hubspot Analytics Events Event Instance Example
  slug: hubspot-analytics-events-event-instance-example
- key_count: 1
  name: Hubspot Analytics Events Event Type Collection Example
  slug: hubspot-analytics-events-event-type-collection-example
- key_count: 2
  name: Hubspot Analytics Events Paging Example
  slug: hubspot-analytics-events-paging-example
- key_count: 2
  name: Hubspot Analytics Events Paging Next Example
  slug: hubspot-analytics-events-paging-next-example
- key_count: 2
  name: Hubspot Analytics Events Paging Previous Example
  slug: hubspot-analytics-events-paging-previous-example
- key_count: 4
  name: Hubspot Authors Attach To Language Group Request Example
  slug: hubspot-authors-attach-to-language-group-request-example
- key_count: 1
  name: Hubspot Authors Batch Archive Input Example
  slug: hubspot-authors-batch-archive-input-example
- key_count: 1
  name: Hubspot Authors Batch Create Input Example
  slug: hubspot-authors-batch-create-input-example
- key_count: 1
  name: Hubspot Authors Batch Input Example
  slug: hubspot-authors-batch-input-example
- key_count: 2
  name: Hubspot Authors Batch Input Item Example
  slug: hubspot-authors-batch-input-item-example
- key_count: 1
  name: Hubspot Authors Batch Read Input Example
  slug: hubspot-authors-batch-read-input-example
- key_count: 6
  name: Hubspot Authors Batch Response Example
  slug: hubspot-authors-batch-response-example
- key_count: 0
  name: Hubspot Authors Batch Response With Errors Example
  slug: hubspot-authors-batch-response-with-errors-example
- key_count: 3
  name: Hubspot Authors Blog Author Collection Example
  slug: hubspot-authors-blog-author-collection-example
- key_count: 15
  name: Hubspot Authors Blog Author Example
  slug: hubspot-authors-blog-author-example
- key_count: 9
  name: Hubspot Authors Blog Author Input Example
  slug: hubspot-authors-blog-author-input-example
- key_count: 2
  name: Hubspot Authors Create Language Variation Request Example
  slug: hubspot-authors-create-language-variation-request-example
- key_count: 1
  name: Hubspot Authors Detach From Language Group Request Example
  slug: hubspot-authors-detach-from-language-group-request-example
- key_count: 5
  name: Hubspot Authors Error Detail Example
  slug: hubspot-authors-error-detail-example
- key_count: 7
  name: Hubspot Authors Error Example
  slug: hubspot-authors-error-example
- key_count: 1
  name: Hubspot Authors Paging Example
  slug: hubspot-authors-paging-example
- key_count: 2
  name: Hubspot Authors Paging Next Example
  slug: hubspot-authors-paging-next-example
- key_count: 1
  name: Hubspot Authors Set Language Primary Request Example
  slug: hubspot-authors-set-language-primary-request-example
- key_count: 7
  name: Hubspot Authors Standard Error Example
  slug: hubspot-authors-standard-error-example
- key_count: 4
  name: Hubspot Blog Posts Attach To Language Group Request Example
  slug: hubspot-blog-posts-attach-to-language-group-request-example
- key_count: 1
  name: Hubspot Blog Posts Batch Input Example
  slug: hubspot-blog-posts-batch-input-example
- key_count: 1
  name: Hubspot Blog Posts Batch Input Item Example
  slug: hubspot-blog-posts-batch-input-item-example
- key_count: 6
  name: Hubspot Blog Posts Batch Response Example
  slug: hubspot-blog-posts-batch-response-example
- key_count: 0
  name: Hubspot Blog Posts Batch Response With Errors Example
  slug: hubspot-blog-posts-batch-response-with-errors-example
- key_count: 3
  name: Hubspot Blog Posts Blog Post Collection Example
  slug: hubspot-blog-posts-blog-post-collection-example
- key_count: 32
  name: Hubspot Blog Posts Blog Post Example
  slug: hubspot-blog-posts-blog-post-example
- key_count: 15
  name: Hubspot Blog Posts Blog Post Input Example
  slug: hubspot-blog-posts-blog-post-input-example
- key_count: 1
  name: Hubspot Blog Posts Clone Request Example
  slug: hubspot-blog-posts-clone-request-example
- key_count: 2
  name: Hubspot Blog Posts Create Language Variation Request Example
  slug: hubspot-blog-posts-create-language-variation-request-example
- key_count: 1
  name: Hubspot Blog Posts Detach From Language Group Request Example
  slug: hubspot-blog-posts-detach-from-language-group-request-example
- key_count: 5
  name: Hubspot Blog Posts Error Detail Example
  slug: hubspot-blog-posts-error-detail-example
- key_count: 7
  name: Hubspot Blog Posts Error Example
  slug: hubspot-blog-posts-error-example
- key_count: 2
  name: Hubspot Blog Posts Paging Example
  slug: hubspot-blog-posts-paging-example
- key_count: 2
  name: Hubspot Blog Posts Paging Next Example
  slug: hubspot-blog-posts-paging-next-example
- key_count: 2
  name: Hubspot Blog Posts Paging Previous Example
  slug: hubspot-blog-posts-paging-previous-example
- key_count: 1
  name: Hubspot Blog Posts Push Live Request Example
  slug: hubspot-blog-posts-push-live-request-example
- key_count: 1
  name: Hubspot Blog Posts Reset Draft Request Example
  slug: hubspot-blog-posts-reset-draft-request-example
- key_count: 2
  name: Hubspot Blog Posts Restore Previous Version Request Example
  slug: hubspot-blog-posts-restore-previous-version-request-example
- key_count: 2
  name: Hubspot Blog Posts Schedule Request Example
  slug: hubspot-blog-posts-schedule-request-example
- key_count: 1
  name: Hubspot Blog Posts Set Language Primary Request Example
  slug: hubspot-blog-posts-set-language-primary-request-example
- key_count: 7
  name: Hubspot Blog Posts Standard Error Example
  slug: hubspot-blog-posts-standard-error-example
- key_count: 4
  name: Hubspot Blog Posts Version History Example
  slug: hubspot-blog-posts-version-history-example
- key_count: 2
  name: Hubspot Cms Hubdb Collection Response Hub Db Row Example
  slug: hubspot-cms-hubdb-collection-response-hub-db-row-example
- key_count: 2
  name: Hubspot Cms Hubdb Collection Response Hub Db Table Example
  slug: hubspot-cms-hubdb-collection-response-hub-db-table-example
- key_count: 4
  name: Hubspot Cms Hubdb Error Example
  slug: hubspot-cms-hubdb-error-example
- key_count: 5
  name: Hubspot Cms Hubdb Hub Db Column Example
  slug: hubspot-cms-hubdb-hub-db-column-example
- key_count: 1
  name: Hubspot Cms Hubdb Hub Db Row Create Request Example
  slug: hubspot-cms-hubdb-hub-db-row-create-request-example
- key_count: 4
  name: Hubspot Cms Hubdb Hub Db Row Example
  slug: hubspot-cms-hubdb-hub-db-row-example
- key_count: 3
  name: Hubspot Cms Hubdb Hub Db Table Create Request Example
  slug: hubspot-cms-hubdb-hub-db-table-create-request-example
- key_count: 9
  name: Hubspot Cms Hubdb Hub Db Table Example
  slug: hubspot-cms-hubdb-hub-db-table-example
- key_count: 1
  name: Hubspot Cms Hubdb Paging Example
  slug: hubspot-cms-hubdb-paging-example
- key_count: 2
  name: Hubspot Cms Pages Collection Response Page Example
  slug: hubspot-cms-pages-collection-response-page-example
- key_count: 4
  name: Hubspot Cms Pages Error Example
  slug: hubspot-cms-pages-error-example
- key_count: 8
  name: Hubspot Cms Pages Page Create Request Example
  slug: hubspot-cms-pages-page-create-request-example
- key_count: 16
  name: Hubspot Cms Pages Page Example
  slug: hubspot-cms-pages-page-example
- key_count: 5
  name: Hubspot Cms Pages Page Update Request Example
  slug: hubspot-cms-pages-page-update-request-example
- key_count: 1
  name: Hubspot Cms Pages Paging Example
  slug: hubspot-cms-pages-paging-example
- key_count: 2
  name: Hubspot Commerce Payments Association Input Example
  slug: hubspot-commerce-payments-association-input-example
- key_count: 2
  name: Hubspot Commerce Payments Association Result Example
  slug: hubspot-commerce-payments-association-result-example
- key_count: 2
  name: Hubspot Commerce Payments Association Type Example
  slug: hubspot-commerce-payments-association-type-example
- key_count: 1
  name: Hubspot Commerce Payments Batch Archive Request Example
  slug: hubspot-commerce-payments-batch-archive-request-example
- key_count: 1
  name: Hubspot Commerce Payments Batch Create Request Example
  slug: hubspot-commerce-payments-batch-create-request-example
- key_count: 8
  name: Hubspot Commerce Payments Batch Create Response Example
  slug: hubspot-commerce-payments-batch-create-response-example
- key_count: 8
  name: Hubspot Commerce Payments Batch Error Example
  slug: hubspot-commerce-payments-batch-error-example
- key_count: 1
  name: Hubspot Commerce Payments Batch Read Input Item Example
  slug: hubspot-commerce-payments-batch-read-input-item-example
- key_count: 4
  name: Hubspot Commerce Payments Batch Read Request Example
  slug: hubspot-commerce-payments-batch-read-request-example
- key_count: 8
  name: Hubspot Commerce Payments Batch Read Response Example
  slug: hubspot-commerce-payments-batch-read-response-example
- key_count: 3
  name: Hubspot Commerce Payments Batch Update Input Item Example
  slug: hubspot-commerce-payments-batch-update-input-item-example
- key_count: 1
  name: Hubspot Commerce Payments Batch Update Request Example
  slug: hubspot-commerce-payments-batch-update-request-example
- key_count: 8
  name: Hubspot Commerce Payments Batch Update Response Example
  slug: hubspot-commerce-payments-batch-update-response-example
- key_count: 2
  name: Hubspot Commerce Payments Commerce Payment Collection Example
  slug: hubspot-commerce-payments-commerce-payment-collection-example
- key_count: 8
  name: Hubspot Commerce Payments Commerce Payment Example
  slug: hubspot-commerce-payments-commerce-payment-example
- key_count: 2
  name: Hubspot Commerce Payments Commerce Payment Input Example
  slug: hubspot-commerce-payments-commerce-payment-input-example
- key_count: 1
  name: Hubspot Commerce Payments Commerce Payment Patch Example
  slug: hubspot-commerce-payments-commerce-payment-patch-example
- key_count: 5
  name: Hubspot Commerce Payments Error Detail Example
  slug: hubspot-commerce-payments-error-detail-example
- key_count: 7
  name: Hubspot Commerce Payments Error Example
  slug: hubspot-commerce-payments-error-example
- key_count: 5
  name: Hubspot Commerce Payments Filter Example
  slug: hubspot-commerce-payments-filter-example
- key_count: 1
  name: Hubspot Commerce Payments Filter Group Example
  slug: hubspot-commerce-payments-filter-group-example
- key_count: 2
  name: Hubspot Commerce Payments Paging Example
  slug: hubspot-commerce-payments-paging-example
- key_count: 6
  name: Hubspot Commerce Payments Property History Example
  slug: hubspot-commerce-payments-property-history-example
- key_count: 6
  name: Hubspot Commerce Payments Search Request Example
  slug: hubspot-commerce-payments-search-request-example
- key_count: 3
  name: Hubspot Commerce Payments Search Response Example
  slug: hubspot-commerce-payments-search-response-example
- key_count: 2
  name: Hubspot Commerce Payments Sort Option Example
  slug: hubspot-commerce-payments-sort-option-example
- key_count: 2
  name: Hubspot Commerce Subscriptions Association Example
  slug: hubspot-commerce-subscriptions-association-example
- key_count: 1
  name: Hubspot Commerce Subscriptions Batch Create Input Example
  slug: hubspot-commerce-subscriptions-batch-create-input-example
- key_count: 2
  name: Hubspot Commerce Subscriptions Batch Read Input Example
  slug: hubspot-commerce-subscriptions-batch-read-input-example
- key_count: 3
  name: Hubspot Commerce Subscriptions Batch Response Subscription Example
  slug: hubspot-commerce-subscriptions-batch-response-subscription-example
- key_count: 1
  name: Hubspot Commerce Subscriptions Batch Update Input Example
  slug: hubspot-commerce-subscriptions-batch-update-input-example
- key_count: 2
  name: Hubspot Commerce Subscriptions Collection Response Association Example
  slug: hubspot-commerce-subscriptions-collection-response-association-example
- key_count: 2
  name: Hubspot Commerce Subscriptions Collection Response Subscription Example
  slug: hubspot-commerce-subscriptions-collection-response-subscription-example
- key_count: 4
  name: Hubspot Commerce Subscriptions Error Example
  slug: hubspot-commerce-subscriptions-error-example
- key_count: 3
  name: Hubspot Commerce Subscriptions Filter Example
  slug: hubspot-commerce-subscriptions-filter-example
- key_count: 1
  name: Hubspot Commerce Subscriptions Filter Group Example
  slug: hubspot-commerce-subscriptions-filter-group-example
- key_count: 1
  name: Hubspot Commerce Subscriptions Paging Example
  slug: hubspot-commerce-subscriptions-paging-example
- key_count: 6
  name: Hubspot Commerce Subscriptions Search Request Example
  slug: hubspot-commerce-subscriptions-search-request-example
- key_count: 1
  name: Hubspot Commerce Subscriptions Simple Public Object Input Example
  slug: hubspot-commerce-subscriptions-simple-public-object-input-example
- key_count: 6
  name: Hubspot Commerce Subscriptions Subscription Example
  slug: hubspot-commerce-subscriptions-subscription-example
- key_count: 2
  name: Hubspot Conversations Actor Collection Example
  slug: hubspot-conversations-actor-collection-example
- key_count: 5
  name: Hubspot Conversations Actor Example
  slug: hubspot-conversations-actor-example
- key_count: 5
  name: Hubspot Conversations Attachment Example
  slug: hubspot-conversations-attachment-example
- key_count: 2
  name: Hubspot Conversations Channel Collection Example
  slug: hubspot-conversations-channel-collection-example
- key_count: 5
  name: Hubspot Conversations Channel Example
  slug: hubspot-conversations-channel-example
- key_count: 5
  name: Hubspot Conversations Error Detail Example
  slug: hubspot-conversations-error-detail-example
- key_count: 7
  name: Hubspot Conversations Error Example
  slug: hubspot-conversations-error-example
- key_count: 3
  name: Hubspot Conversations Inbox Collection Example
  slug: hubspot-conversations-inbox-collection-example
- key_count: 6
  name: Hubspot Conversations Inbox Example
  slug: hubspot-conversations-inbox-example
- key_count: 2
  name: Hubspot Conversations Message Collection Example
  slug: hubspot-conversations-message-collection-example
- key_count: 13
  name: Hubspot Conversations Message Example
  slug: hubspot-conversations-message-example
- key_count: 1
  name: Hubspot Conversations Message Recipient Example
  slug: hubspot-conversations-message-recipient-example
- key_count: 1
  name: Hubspot Conversations Message Status Example
  slug: hubspot-conversations-message-status-example
- key_count: 1
  name: Hubspot Conversations Paging Example
  slug: hubspot-conversations-paging-example
- key_count: 2
  name: Hubspot Conversations Paging Next Example
  slug: hubspot-conversations-paging-next-example
- key_count: 7
  name: Hubspot Conversations Send Message Request Example
  slug: hubspot-conversations-send-message-request-example
- key_count: 2
  name: Hubspot Conversations Thread Collection Example
  slug: hubspot-conversations-thread-collection-example
- key_count: 14
  name: Hubspot Conversations Thread Example
  slug: hubspot-conversations-thread-example
- key_count: 2
  name: Hubspot Conversations Update Thread Request Example
  slug: hubspot-conversations-update-thread-request-example
- key_count: 2
  name: Hubspot Crm Associations Association Definition Collection Example
  slug: hubspot-crm-associations-association-definition-collection-example
- key_count: 7
  name: Hubspot Crm Associations Association Definition Example
  slug: hubspot-crm-associations-association-definition-example
- key_count: 2
  name: Hubspot Crm Associations Association Example
  slug: hubspot-crm-associations-association-example
- key_count: 2
  name: Hubspot Crm Associations Association Label Collection Example
  slug: hubspot-crm-associations-association-label-collection-example
- key_count: 3
  name: Hubspot Crm Associations Association Label Example
  slug: hubspot-crm-associations-association-label-example
- key_count: 3
  name: Hubspot Crm Associations Association Result Example
  slug: hubspot-crm-associations-association-result-example
- key_count: 3
  name: Hubspot Crm Associations Association Type Example
  slug: hubspot-crm-associations-association-type-example
- key_count: 2
  name: Hubspot Crm Associations Association Type Input Example
  slug: hubspot-crm-associations-association-type-input-example
- key_count: 1
  name: Hubspot Crm Associations Batch Association Archive Input Example
  slug: hubspot-crm-associations-batch-association-archive-input-example
- key_count: 3
  name: Hubspot Crm Associations Batch Association Archive Item Example
  slug: hubspot-crm-associations-batch-association-archive-item-example
- key_count: 1
  name: Hubspot Crm Associations Batch Association Create Input Example
  slug: hubspot-crm-associations-batch-association-create-input-example
- key_count: 3
  name: Hubspot Crm Associations Batch Association Create Item Example
  slug: hubspot-crm-associations-batch-association-create-item-example
- key_count: 1
  name: Hubspot Crm Associations Batch Association Read Input Example
  slug: hubspot-crm-associations-batch-association-read-input-example
- key_count: 8
  name: Hubspot Crm Associations Batch Association Response Example
  slug: hubspot-crm-associations-batch-association-response-example
- key_count: 2
  name: Hubspot Crm Associations Create Association Input Example
  slug: hubspot-crm-associations-create-association-input-example
- key_count: 3
  name: Hubspot Crm Associations Create Label Input Example
  slug: hubspot-crm-associations-create-label-input-example
- key_count: 5
  name: Hubspot Crm Associations Error Detail Example
  slug: hubspot-crm-associations-error-detail-example
- key_count: 7
  name: Hubspot Crm Associations Error Example
  slug: hubspot-crm-associations-error-example
- key_count: 1
  name: Hubspot Crm Associations Object Reference Example
  slug: hubspot-crm-associations-object-reference-example
- key_count: 1
  name: Hubspot Crm Associations Paging Example
  slug: hubspot-crm-associations-paging-example
- key_count: 2
  name: Hubspot Crm Associations Paging Next Example
  slug: hubspot-crm-associations-paging-next-example
- key_count: 7
  name: Hubspot Crm Associations Standard Error Example
  slug: hubspot-crm-associations-standard-error-example
- key_count: 2
  name: Hubspot Crm Companies Association Example
  slug: hubspot-crm-companies-association-example
- key_count: 1
  name: Hubspot Crm Companies Batch Archive Input Example
  slug: hubspot-crm-companies-batch-archive-input-example
- key_count: 1
  name: Hubspot Crm Companies Batch Create Input Example
  slug: hubspot-crm-companies-batch-create-input-example
- key_count: 2
  name: Hubspot Crm Companies Batch Read Input Example
  slug: hubspot-crm-companies-batch-read-input-example
- key_count: 3
  name: Hubspot Crm Companies Batch Response Company Example
  slug: hubspot-crm-companies-batch-response-company-example
- key_count: 1
  name: Hubspot Crm Companies Batch Update Input Example
  slug: hubspot-crm-companies-batch-update-input-example
- key_count: 2
  name: Hubspot Crm Companies Collection Response Association Example
  slug: hubspot-crm-companies-collection-response-association-example
- key_count: 2
  name: Hubspot Crm Companies Collection Response Company Example
  slug: hubspot-crm-companies-collection-response-company-example
- key_count: 6
  name: Hubspot Crm Companies Company Example
  slug: hubspot-crm-companies-company-example
- key_count: 4
  name: Hubspot Crm Companies Error Example
  slug: hubspot-crm-companies-error-example
- key_count: 3
  name: Hubspot Crm Companies Filter Example
  slug: hubspot-crm-companies-filter-example
- key_count: 1
  name: Hubspot Crm Companies Filter Group Example
  slug: hubspot-crm-companies-filter-group-example
- key_count: 1
  name: Hubspot Crm Companies Paging Example
  slug: hubspot-crm-companies-paging-example
- key_count: 6
  name: Hubspot Crm Companies Search Request Example
  slug: hubspot-crm-companies-search-request-example
- key_count: 1
  name: Hubspot Crm Companies Simple Public Object Input Example
  slug: hubspot-crm-companies-simple-public-object-input-example
- key_count: 2
  name: Hubspot Crm Contacts Association Example
  slug: hubspot-crm-contacts-association-example
- key_count: 1
  name: Hubspot Crm Contacts Batch Archive Input Example
  slug: hubspot-crm-contacts-batch-archive-input-example
- key_count: 1
  name: Hubspot Crm Contacts Batch Create Input Example
  slug: hubspot-crm-contacts-batch-create-input-example
- key_count: 2
  name: Hubspot Crm Contacts Batch Read Input Example
  slug: hubspot-crm-contacts-batch-read-input-example
- key_count: 3
  name: Hubspot Crm Contacts Batch Response Contact Example
  slug: hubspot-crm-contacts-batch-response-contact-example
- key_count: 1
  name: Hubspot Crm Contacts Batch Update Input Example
  slug: hubspot-crm-contacts-batch-update-input-example
- key_count: 2
  name: Hubspot Crm Contacts Collection Response Association Example
  slug: hubspot-crm-contacts-collection-response-association-example
- key_count: 2
  name: Hubspot Crm Contacts Collection Response Contact Example
  slug: hubspot-crm-contacts-collection-response-contact-example
- key_count: 6
  name: Hubspot Crm Contacts Contact Example
  slug: hubspot-crm-contacts-contact-example
- key_count: 4
  name: Hubspot Crm Contacts Error Example
  slug: hubspot-crm-contacts-error-example
- key_count: 3
  name: Hubspot Crm Contacts Filter Example
  slug: hubspot-crm-contacts-filter-example
- key_count: 1
  name: Hubspot Crm Contacts Filter Group Example
  slug: hubspot-crm-contacts-filter-group-example
- key_count: 1
  name: Hubspot Crm Contacts Paging Example
  slug: hubspot-crm-contacts-paging-example
- key_count: 6
  name: Hubspot Crm Contacts Search Request Example
  slug: hubspot-crm-contacts-search-request-example
- key_count: 1
  name: Hubspot Crm Contacts Simple Public Object Input Example
  slug: hubspot-crm-contacts-simple-public-object-input-example
- key_count: 2
  name: Hubspot Crm Deals Association Example
  slug: hubspot-crm-deals-association-example
- key_count: 1
  name: Hubspot Crm Deals Batch Archive Input Example
  slug: hubspot-crm-deals-batch-archive-input-example
- key_count: 1
  name: Hubspot Crm Deals Batch Create Input Example
  slug: hubspot-crm-deals-batch-create-input-example
- key_count: 2
  name: Hubspot Crm Deals Batch Read Input Example
  slug: hubspot-crm-deals-batch-read-input-example
- key_count: 3
  name: Hubspot Crm Deals Batch Response Deal Example
  slug: hubspot-crm-deals-batch-response-deal-example
- key_count: 1
  name: Hubspot Crm Deals Batch Update Input Example
  slug: hubspot-crm-deals-batch-update-input-example
- key_count: 2
  name: Hubspot Crm Deals Collection Response Association Example
  slug: hubspot-crm-deals-collection-response-association-example
- key_count: 2
  name: Hubspot Crm Deals Collection Response Deal Example
  slug: hubspot-crm-deals-collection-response-deal-example
- key_count: 6
  name: Hubspot Crm Deals Deal Example
  slug: hubspot-crm-deals-deal-example
- key_count: 4
  name: Hubspot Crm Deals Error Example
  slug: hubspot-crm-deals-error-example
- key_count: 3
  name: Hubspot Crm Deals Filter Example
  slug: hubspot-crm-deals-filter-example
- key_count: 1
  name: Hubspot Crm Deals Filter Group Example
  slug: hubspot-crm-deals-filter-group-example
- key_count: 1
  name: Hubspot Crm Deals Paging Example
  slug: hubspot-crm-deals-paging-example
- key_count: 6
  name: Hubspot Crm Deals Search Request Example
  slug: hubspot-crm-deals-search-request-example
- key_count: 1
  name: Hubspot Crm Deals Simple Public Object Input Example
  slug: hubspot-crm-deals-simple-public-object-input-example
- key_count: 1
  name: Hubspot Crm Feature Flags Batch Delete Input Example
  slug: hubspot-crm-feature-flags-batch-delete-input-example
- key_count: 1
  name: Hubspot Crm Feature Flags Batch Delete Input Item Example
  slug: hubspot-crm-feature-flags-batch-delete-input-item-example
- key_count: 4
  name: Hubspot Crm Feature Flags Batch Error Example
  slug: hubspot-crm-feature-flags-batch-error-example
- key_count: 1
  name: Hubspot Crm Feature Flags Batch Portal Flag State Input Example
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-input-example
- key_count: 2
  name: Hubspot Crm Feature Flags Batch Portal Flag State Input Item Example
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-input-item-example
- key_count: 4
  name: Hubspot Crm Feature Flags Batch Portal Flag State Response Example
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-response-example
- key_count: 5
  name: Hubspot Crm Feature Flags Batch Portal Flag State Response With Errors Example
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-response-with-errors-example
- key_count: 5
  name: Hubspot Crm Feature Flags Error Detail Example
  slug: hubspot-crm-feature-flags-error-detail-example
- key_count: 7
  name: Hubspot Crm Feature Flags Error Example
  slug: hubspot-crm-feature-flags-error-example
- key_count: 4
  name: Hubspot Crm Feature Flags Feature Flag Example
  slug: hubspot-crm-feature-flags-feature-flag-example
- key_count: 1
  name: Hubspot Crm Feature Flags Feature Flag Input Example
  slug: hubspot-crm-feature-flags-feature-flag-input-example
- key_count: 1
  name: Hubspot Crm Feature Flags Paging Example
  slug: hubspot-crm-feature-flags-paging-example
- key_count: 2
  name: Hubspot Crm Feature Flags Paging Next Example
  slug: hubspot-crm-feature-flags-paging-next-example
- key_count: 2
  name: Hubspot Crm Feature Flags Portal Flag State Collection Example
  slug: hubspot-crm-feature-flags-portal-flag-state-collection-example
- key_count: 4
  name: Hubspot Crm Feature Flags Portal Flag State Example
  slug: hubspot-crm-feature-flags-portal-flag-state-example
- key_count: 1
  name: Hubspot Crm Feature Flags Portal Flag State Input Example
  slug: hubspot-crm-feature-flags-portal-flag-state-input-example
- key_count: 2
  name: Hubspot Crm Lists Collection Response List Example
  slug: hubspot-crm-lists-collection-response-list-example
- key_count: 2
  name: Hubspot Crm Lists Collection Response Membership Example
  slug: hubspot-crm-lists-collection-response-membership-example
- key_count: 4
  name: Hubspot Crm Lists Error Example
  slug: hubspot-crm-lists-error-example
- key_count: 4
  name: Hubspot Crm Lists List Create Request Example
  slug: hubspot-crm-lists-list-create-request-example
- key_count: 9
  name: Hubspot Crm Lists List Example
  slug: hubspot-crm-lists-list-example
- key_count: 2
  name: Hubspot Crm Lists Membership Change Request Example
  slug: hubspot-crm-lists-membership-change-request-example
- key_count: 4
  name: Hubspot Crm Lists Membership Change Response Example
  slug: hubspot-crm-lists-membership-change-response-example
- key_count: 2
  name: Hubspot Crm Lists Membership Example
  slug: hubspot-crm-lists-membership-example
- key_count: 1
  name: Hubspot Crm Lists Paging Example
  slug: hubspot-crm-lists-paging-example
- key_count: 5
  name: Hubspot Crm Search Crm Object Example
  slug: hubspot-crm-search-crm-object-example
- key_count: 5
  name: Hubspot Crm Search Error Example
  slug: hubspot-crm-search-error-example
- key_count: 5
  name: Hubspot Crm Search Filter Example
  slug: hubspot-crm-search-filter-example
- key_count: 1
  name: Hubspot Crm Search Filter Group Example
  slug: hubspot-crm-search-filter-group-example
- key_count: 1
  name: Hubspot Crm Search Paging Example
  slug: hubspot-crm-search-paging-example
- key_count: 6
  name: Hubspot Crm Search Search Request Example
  slug: hubspot-crm-search-search-request-example
- key_count: 3
  name: Hubspot Crm Search Search Response Example
  slug: hubspot-crm-search-search-response-example
- key_count: 2
  name: Hubspot Crm Search Sort Example
  slug: hubspot-crm-search-sort-example
- key_count: 2
  name: Hubspot Crm Tickets Association Example
  slug: hubspot-crm-tickets-association-example
- key_count: 1
  name: Hubspot Crm Tickets Batch Archive Input Example
  slug: hubspot-crm-tickets-batch-archive-input-example
- key_count: 1
  name: Hubspot Crm Tickets Batch Create Input Example
  slug: hubspot-crm-tickets-batch-create-input-example
- key_count: 2
  name: Hubspot Crm Tickets Batch Read Input Example
  slug: hubspot-crm-tickets-batch-read-input-example
- key_count: 3
  name: Hubspot Crm Tickets Batch Response Ticket Example
  slug: hubspot-crm-tickets-batch-response-ticket-example
- key_count: 1
  name: Hubspot Crm Tickets Batch Update Input Example
  slug: hubspot-crm-tickets-batch-update-input-example
- key_count: 2
  name: Hubspot Crm Tickets Collection Response Association Example
  slug: hubspot-crm-tickets-collection-response-association-example
- key_count: 2
  name: Hubspot Crm Tickets Collection Response Ticket Example
  slug: hubspot-crm-tickets-collection-response-ticket-example
- key_count: 4
  name: Hubspot Crm Tickets Error Example
  slug: hubspot-crm-tickets-error-example
- key_count: 3
  name: Hubspot Crm Tickets Filter Example
  slug: hubspot-crm-tickets-filter-example
- key_count: 1
  name: Hubspot Crm Tickets Filter Group Example
  slug: hubspot-crm-tickets-filter-group-example
- key_count: 1
  name: Hubspot Crm Tickets Paging Example
  slug: hubspot-crm-tickets-paging-example
- key_count: 6
  name: Hubspot Crm Tickets Search Request Example
  slug: hubspot-crm-tickets-search-request-example
- key_count: 1
  name: Hubspot Crm Tickets Simple Public Object Input Example
  slug: hubspot-crm-tickets-simple-public-object-input-example
- key_count: 6
  name: Hubspot Crm Tickets Ticket Example
  slug: hubspot-crm-tickets-ticket-example
- key_count: 2
  name: Hubspot Custom Workflow Actions Action Definition Collection Example
  slug: hubspot-custom-workflow-actions-action-definition-collection-example
- key_count: 10
  name: Hubspot Custom Workflow Actions Action Definition Example
  slug: hubspot-custom-workflow-actions-action-definition-example
- key_count: 7
  name: Hubspot Custom Workflow Actions Action Definition Input Example
  slug: hubspot-custom-workflow-actions-action-definition-input-example
- key_count: 7
  name: Hubspot Custom Workflow Actions Action Definition Patch Example
  slug: hubspot-custom-workflow-actions-action-definition-patch-example
- key_count: 2
  name: Hubspot Custom Workflow Actions Action Definition Revision Collection Example
  slug: hubspot-custom-workflow-actions-action-definition-revision-collection-example
- key_count: 3
  name: Hubspot Custom Workflow Actions Action Definition Revision Example
  slug: hubspot-custom-workflow-actions-action-definition-revision-example
- key_count: 1
  name: Hubspot Custom Workflow Actions Action Function Collection Example
  slug: hubspot-custom-workflow-actions-action-function-collection-example
- key_count: 3
  name: Hubspot Custom Workflow Actions Action Function Example
  slug: hubspot-custom-workflow-actions-action-function-example
- key_count: 1
  name: Hubspot Custom Workflow Actions Action Function Input Example
  slug: hubspot-custom-workflow-actions-action-function-input-example
- key_count: 2
  name: Hubspot Custom Workflow Actions Action Function Reference Example
  slug: hubspot-custom-workflow-actions-action-function-reference-example
- key_count: 4
  name: Hubspot Custom Workflow Actions Action Labels Example
  slug: hubspot-custom-workflow-actions-action-labels-example
- key_count: 1
  name: Hubspot Custom Workflow Actions Batch Callback Completion Request Example
  slug: hubspot-custom-workflow-actions-batch-callback-completion-request-example
- key_count: 3
  name: Hubspot Custom Workflow Actions Batch Callback Error Example
  slug: hubspot-custom-workflow-actions-batch-callback-error-example
- key_count: 2
  name: Hubspot Custom Workflow Actions Batch Callback Input Example
  slug: hubspot-custom-workflow-actions-batch-callback-input-example
- key_count: 2
  name: Hubspot Custom Workflow Actions Batch Callback Response Example
  slug: hubspot-custom-workflow-actions-batch-callback-response-example
- key_count: 1
  name: Hubspot Custom Workflow Actions Callback Completion Request Example
  slug: hubspot-custom-workflow-actions-callback-completion-request-example
- key_count: 5
  name: Hubspot Custom Workflow Actions Error Detail Example
  slug: hubspot-custom-workflow-actions-error-detail-example
- key_count: 7
  name: Hubspot Custom Workflow Actions Error Example
  slug: hubspot-custom-workflow-actions-error-example
- key_count: 3
  name: Hubspot Custom Workflow Actions Field Option Example
  slug: hubspot-custom-workflow-actions-field-option-example
- key_count: 6
  name: Hubspot Custom Workflow Actions Field Type Definition Example
  slug: hubspot-custom-workflow-actions-field-type-definition-example
- key_count: 3
  name: Hubspot Custom Workflow Actions Input Field Example
  slug: hubspot-custom-workflow-actions-input-field-example
- key_count: 1
  name: Hubspot Custom Workflow Actions Object Request Options Example
  slug: hubspot-custom-workflow-actions-object-request-options-example
- key_count: 1
  name: Hubspot Custom Workflow Actions Output Field Example
  slug: hubspot-custom-workflow-actions-output-field-example
- key_count: 1
  name: Hubspot Custom Workflow Actions Paging Example
  slug: hubspot-custom-workflow-actions-paging-example
- key_count: 3
  name: Hubspot Domains Domain Collection Response Example
  slug: hubspot-domains-domain-collection-response-example
- key_count: 21
  name: Hubspot Domains Domain Example
  slug: hubspot-domains-domain-example
- key_count: 5
  name: Hubspot Domains Error Detail Example
  slug: hubspot-domains-error-detail-example
- key_count: 7
  name: Hubspot Domains Error Example
  slug: hubspot-domains-error-example
- key_count: 1
  name: Hubspot Domains Forward Paging Example
  slug: hubspot-domains-forward-paging-example
- key_count: 2
  name: Hubspot Domains Next Page Example
  slug: hubspot-domains-next-page-example
- key_count: 2
  name: Hubspot Engagement Calls Association Input Example
  slug: hubspot-engagement-calls-association-input-example
- key_count: 2
  name: Hubspot Engagement Calls Association Type Example
  slug: hubspot-engagement-calls-association-type-example
- key_count: 1
  name: Hubspot Engagement Calls Batch Archive Calls Request Example
  slug: hubspot-engagement-calls-batch-archive-calls-request-example
- key_count: 7
  name: Hubspot Engagement Calls Batch Calls Response Example
  slug: hubspot-engagement-calls-batch-calls-response-example
- key_count: 1
  name: Hubspot Engagement Calls Batch Create Calls Request Example
  slug: hubspot-engagement-calls-batch-create-calls-request-example
- key_count: 5
  name: Hubspot Engagement Calls Batch Error Example
  slug: hubspot-engagement-calls-batch-error-example
- key_count: 4
  name: Hubspot Engagement Calls Batch Read Calls Request Example
  slug: hubspot-engagement-calls-batch-read-calls-request-example
- key_count: 1
  name: Hubspot Engagement Calls Batch Read Input Example
  slug: hubspot-engagement-calls-batch-read-input-example
- key_count: 1
  name: Hubspot Engagement Calls Batch Update Calls Request Example
  slug: hubspot-engagement-calls-batch-update-calls-request-example
- key_count: 2
  name: Hubspot Engagement Calls Batch Update Input Example
  slug: hubspot-engagement-calls-batch-update-input-example
- key_count: 2
  name: Hubspot Engagement Calls Call Collection Response Example
  slug: hubspot-engagement-calls-call-collection-response-example
- key_count: 2
  name: Hubspot Engagement Calls Call Create Request Example
  slug: hubspot-engagement-calls-call-create-request-example
- key_count: 7
  name: Hubspot Engagement Calls Call Example
  slug: hubspot-engagement-calls-call-example
- key_count: 6
  name: Hubspot Engagement Calls Call Search Request Example
  slug: hubspot-engagement-calls-call-search-request-example
- key_count: 3
  name: Hubspot Engagement Calls Call Search Response Example
  slug: hubspot-engagement-calls-call-search-response-example
- key_count: 1
  name: Hubspot Engagement Calls Call Update Request Example
  slug: hubspot-engagement-calls-call-update-request-example
- key_count: 5
  name: Hubspot Engagement Calls Error Detail Example
  slug: hubspot-engagement-calls-error-detail-example
- key_count: 7
  name: Hubspot Engagement Calls Error Example
  slug: hubspot-engagement-calls-error-example
- key_count: 5
  name: Hubspot Engagement Calls Filter Example
  slug: hubspot-engagement-calls-filter-example
- key_count: 1
  name: Hubspot Engagement Calls Filter Group Example
  slug: hubspot-engagement-calls-filter-group-example
- key_count: 2
  name: Hubspot Engagement Calls Gdpr Delete Request Example
  slug: hubspot-engagement-calls-gdpr-delete-request-example
- key_count: 2
  name: Hubspot Engagement Calls Next Page Example
  slug: hubspot-engagement-calls-next-page-example
- key_count: 1
  name: Hubspot Engagement Calls Paging Example
  slug: hubspot-engagement-calls-paging-example
- key_count: 6
  name: Hubspot Engagement Calls Property History Example
  slug: hubspot-engagement-calls-property-history-example
- key_count: 2
  name: Hubspot Engagement Calls Sort Option Example
  slug: hubspot-engagement-calls-sort-option-example
- key_count: 2
  name: Hubspot Engagement Emails Association Example
  slug: hubspot-engagement-emails-association-example
- key_count: 1
  name: Hubspot Engagement Emails Batch Create Input Example
  slug: hubspot-engagement-emails-batch-create-input-example
- key_count: 2
  name: Hubspot Engagement Emails Batch Read Input Example
  slug: hubspot-engagement-emails-batch-read-input-example
- key_count: 1
  name: Hubspot Engagement Emails Batch Update Input Example
  slug: hubspot-engagement-emails-batch-update-input-example
- key_count: 2
  name: Hubspot Engagement Emails Collection Response Association Example
  slug: hubspot-engagement-emails-collection-response-association-example
- key_count: 4
  name: Hubspot Engagement Emails Error Example
  slug: hubspot-engagement-emails-error-example
- key_count: 3
  name: Hubspot Engagement Emails Filter Example
  slug: hubspot-engagement-emails-filter-example
- key_count: 1
  name: Hubspot Engagement Emails Filter Group Example
  slug: hubspot-engagement-emails-filter-group-example
- key_count: 1
  name: Hubspot Engagement Emails Paging Example
  slug: hubspot-engagement-emails-paging-example
- key_count: 6
  name: Hubspot Engagement Emails Search Request Example
  slug: hubspot-engagement-emails-search-request-example
- key_count: 1
  name: Hubspot Engagement Emails Simple Public Object Input Example
  slug: hubspot-engagement-emails-simple-public-object-input-example
- key_count: 2
  name: Hubspot Engagement Meetings Association Example
  slug: hubspot-engagement-meetings-association-example
- key_count: 1
  name: Hubspot Engagement Meetings Batch Create Input Example
  slug: hubspot-engagement-meetings-batch-create-input-example
- key_count: 2
  name: Hubspot Engagement Meetings Batch Read Input Example
  slug: hubspot-engagement-meetings-batch-read-input-example
- key_count: 3
  name: Hubspot Engagement Meetings Batch Response Meeting Example
  slug: hubspot-engagement-meetings-batch-response-meeting-example
- key_count: 1
  name: Hubspot Engagement Meetings Batch Update Input Example
  slug: hubspot-engagement-meetings-batch-update-input-example
- key_count: 2
  name: Hubspot Engagement Meetings Collection Response Association Example
  slug: hubspot-engagement-meetings-collection-response-association-example
- key_count: 2
  name: Hubspot Engagement Meetings Collection Response Meeting Example
  slug: hubspot-engagement-meetings-collection-response-meeting-example
- key_count: 4
  name: Hubspot Engagement Meetings Error Example
  slug: hubspot-engagement-meetings-error-example
- key_count: 3
  name: Hubspot Engagement Meetings Filter Example
  slug: hubspot-engagement-meetings-filter-example
- key_count: 1
  name: Hubspot Engagement Meetings Filter Group Example
  slug: hubspot-engagement-meetings-filter-group-example
- key_count: 6
  name: Hubspot Engagement Meetings Meeting Example
  slug: hubspot-engagement-meetings-meeting-example
- key_count: 1
  name: Hubspot Engagement Meetings Paging Example
  slug: hubspot-engagement-meetings-paging-example
- key_count: 6
  name: Hubspot Engagement Meetings Search Request Example
  slug: hubspot-engagement-meetings-search-request-example
- key_count: 1
  name: Hubspot Engagement Meetings Simple Public Object Input Example
  slug: hubspot-engagement-meetings-simple-public-object-input-example
- key_count: 2
  name: Hubspot Engagement Notes Association Input Example
  slug: hubspot-engagement-notes-association-input-example
- key_count: 2
  name: Hubspot Engagement Notes Association Type Example
  slug: hubspot-engagement-notes-association-type-example
- key_count: 1
  name: Hubspot Engagement Notes Batch Archive Notes Request Example
  slug: hubspot-engagement-notes-batch-archive-notes-request-example
- key_count: 1
  name: Hubspot Engagement Notes Batch Create Notes Request Example
  slug: hubspot-engagement-notes-batch-create-notes-request-example
- key_count: 5
  name: Hubspot Engagement Notes Batch Error Example
  slug: hubspot-engagement-notes-batch-error-example
- key_count: 7
  name: Hubspot Engagement Notes Batch Notes Response Example
  slug: hubspot-engagement-notes-batch-notes-response-example
- key_count: 1
  name: Hubspot Engagement Notes Batch Read Input Example
  slug: hubspot-engagement-notes-batch-read-input-example
- key_count: 4
  name: Hubspot Engagement Notes Batch Read Notes Request Example
  slug: hubspot-engagement-notes-batch-read-notes-request-example
- key_count: 2
  name: Hubspot Engagement Notes Batch Update Input Example
  slug: hubspot-engagement-notes-batch-update-input-example
- key_count: 1
  name: Hubspot Engagement Notes Batch Update Notes Request Example
  slug: hubspot-engagement-notes-batch-update-notes-request-example
- key_count: 5
  name: Hubspot Engagement Notes Error Detail Example
  slug: hubspot-engagement-notes-error-detail-example
- key_count: 7
  name: Hubspot Engagement Notes Error Example
  slug: hubspot-engagement-notes-error-example
- key_count: 5
  name: Hubspot Engagement Notes Filter Example
  slug: hubspot-engagement-notes-filter-example
- key_count: 1
  name: Hubspot Engagement Notes Filter Group Example
  slug: hubspot-engagement-notes-filter-group-example
- key_count: 2
  name: Hubspot Engagement Notes Gdpr Delete Request Example
  slug: hubspot-engagement-notes-gdpr-delete-request-example
- key_count: 2
  name: Hubspot Engagement Notes Next Page Example
  slug: hubspot-engagement-notes-next-page-example
- key_count: 2
  name: Hubspot Engagement Notes Note Collection Response Example
  slug: hubspot-engagement-notes-note-collection-response-example
- key_count: 2
  name: Hubspot Engagement Notes Note Create Request Example
  slug: hubspot-engagement-notes-note-create-request-example
- key_count: 7
  name: Hubspot Engagement Notes Note Example
  slug: hubspot-engagement-notes-note-example
- key_count: 6
  name: Hubspot Engagement Notes Note Search Request Example
  slug: hubspot-engagement-notes-note-search-request-example
- key_count: 3
  name: Hubspot Engagement Notes Note Search Response Example
  slug: hubspot-engagement-notes-note-search-response-example
- key_count: 1
  name: Hubspot Engagement Notes Note Update Request Example
  slug: hubspot-engagement-notes-note-update-request-example
- key_count: 1
  name: Hubspot Engagement Notes Paging Example
  slug: hubspot-engagement-notes-paging-example
- key_count: 6
  name: Hubspot Engagement Notes Property History Example
  slug: hubspot-engagement-notes-property-history-example
- key_count: 2
  name: Hubspot Engagement Notes Sort Option Example
  slug: hubspot-engagement-notes-sort-option-example
- key_count: 2
  name: Hubspot Engagement Tasks Association Example
  slug: hubspot-engagement-tasks-association-example
- key_count: 1
  name: Hubspot Engagement Tasks Batch Create Input Example
  slug: hubspot-engagement-tasks-batch-create-input-example
- key_count: 2
  name: Hubspot Engagement Tasks Batch Read Input Example
  slug: hubspot-engagement-tasks-batch-read-input-example
- key_count: 3
  name: Hubspot Engagement Tasks Batch Response Task Example
  slug: hubspot-engagement-tasks-batch-response-task-example
- key_count: 1
  name: Hubspot Engagement Tasks Batch Update Input Example
  slug: hubspot-engagement-tasks-batch-update-input-example
- key_count: 2
  name: Hubspot Engagement Tasks Collection Response Association Example
  slug: hubspot-engagement-tasks-collection-response-association-example
- key_count: 2
  name: Hubspot Engagement Tasks Collection Response Task Example
  slug: hubspot-engagement-tasks-collection-response-task-example
- key_count: 4
  name: Hubspot Engagement Tasks Error Example
  slug: hubspot-engagement-tasks-error-example
- key_count: 3
  name: Hubspot Engagement Tasks Filter Example
  slug: hubspot-engagement-tasks-filter-example
- key_count: 1
  name: Hubspot Engagement Tasks Filter Group Example
  slug: hubspot-engagement-tasks-filter-group-example
- key_count: 1
  name: Hubspot Engagement Tasks Paging Example
  slug: hubspot-engagement-tasks-paging-example
- key_count: 6
  name: Hubspot Engagement Tasks Search Request Example
  slug: hubspot-engagement-tasks-search-request-example
- key_count: 1
  name: Hubspot Engagement Tasks Simple Public Object Input Example
  slug: hubspot-engagement-tasks-simple-public-object-input-example
- key_count: 6
  name: Hubspot Engagement Tasks Task Example
  slug: hubspot-engagement-tasks-task-example
- key_count: 5
  name: Hubspot Marketing Emal Error Detail Example
  slug: hubspot-marketing-emal-error-detail-example
- key_count: 7
  name: Hubspot Marketing Emal Error Example
  slug: hubspot-marketing-emal-error-example
- key_count: 2
  name: Hubspot Marketing Emal Next Page Example
  slug: hubspot-marketing-emal-next-page-example
- key_count: 1
  name: Hubspot Marketing Emal Paging Example
  slug: hubspot-marketing-emal-paging-example
- key_count: 2
  name: Hubspot Marketing Emal Smtp Token Collection Response Example
  slug: hubspot-marketing-emal-smtp-token-collection-response-example
- key_count: 2
  name: Hubspot Marketing Emal Smtp Token Create Request Example
  slug: hubspot-marketing-emal-smtp-token-create-request-example
- key_count: 6
  name: Hubspot Marketing Emal Smtp Token Example
  slug: hubspot-marketing-emal-smtp-token-example
- key_count: 7
  name: Hubspot Marketing Emal Smtp Token With Password Example
  slug: hubspot-marketing-emal-smtp-token-with-password-example
- key_count: 9
  name: Hubspot Oauth Access Token Metadata Example
  slug: hubspot-oauth-access-token-metadata-example
- key_count: 5
  name: Hubspot Oauth Error Detail Example
  slug: hubspot-oauth-error-detail-example
- key_count: 7
  name: Hubspot Oauth Error Example
  slug: hubspot-oauth-error-example
- key_count: 6
  name: Hubspot Oauth Refresh Token Metadata Example
  slug: hubspot-oauth-refresh-token-metadata-example
- key_count: 6
  name: Hubspot Oauth Token Request Example
  slug: hubspot-oauth-token-request-example
- key_count: 5
  name: Hubspot Oauth Token Response Example
  slug: hubspot-oauth-token-response-example
- key_count: 5
  name: Hubspot Source Code Action Response Example
  slug: hubspot-source-code-action-response-example
- key_count: 8
  name: Hubspot Source Code Asset File Metadata Example
  slug: hubspot-source-code-asset-file-metadata-example
- key_count: 5
  name: Hubspot Source Code Error Detail Example
  slug: hubspot-source-code-error-detail-example
- key_count: 7
  name: Hubspot Source Code Error Example
  slug: hubspot-source-code-error-example
- key_count: 1
  name: Hubspot Source Code File Extract Request Example
  slug: hubspot-source-code-file-extract-request-example
- key_count: 1
  name: Hubspot Source Code File Upload Request Example
  slug: hubspot-source-code-file-upload-request-example
- key_count: 2
  name: Hubspot Source Code Task Locator Example
  slug: hubspot-source-code-task-locator-example
- key_count: 6
  name: Marketing Emal Api Email Message Example
  slug: marketing-emal-api-email-message-example
- key_count: 2
  name: Marketing Emal Api Next Page Example
  slug: marketing-emal-api-next-page-example
- key_count: 1
  name: Marketing Emal Api Paging Example
  slug: marketing-emal-api-paging-example
- key_count: 2
  name: Marketing Emal Api Smtp Token Collection Response Example
  slug: marketing-emal-api-smtp-token-collection-response-example
- key_count: 2
  name: Marketing Emal Api Smtp Token Create Request Example
  slug: marketing-emal-api-smtp-token-create-request-example
- key_count: 6
  name: Marketing Emal Api Smtp Token Example
  slug: marketing-emal-api-smtp-token-example
- key_count: 7
  name: Marketing Emal Api Smtp Token With Password Example
  slug: marketing-emal-api-smtp-token-with-password-example
- key_count: 4
  name: Marketing Emal Api Transactional Email Request Example
  slug: marketing-emal-api-transactional-email-request-example
- key_count: 6
  name: Marketing Emal Api Transactional Email Response Example
  slug: marketing-emal-api-transactional-email-response-example
- key_count: 9
  name: Oauth Api Access Token Metadata Example
  slug: oauth-api-access-token-metadata-example
- key_count: 6
  name: Oauth Api Refresh Token Metadata Example
  slug: oauth-api-refresh-token-metadata-example
- key_count: 6
  name: Oauth Api Token Request Example
  slug: oauth-api-token-request-example
- key_count: 5
  name: Oauth Api Token Response Example
  slug: oauth-api-token-response-example
- key_count: 5
  name: Source Code Api Action Response Example
  slug: source-code-api-action-response-example
- key_count: 8
  name: Source Code Api Asset File Metadata Example
  slug: source-code-api-asset-file-metadata-example
- key_count: 1
  name: Source Code Api File Extract Request Example
  slug: source-code-api-file-extract-request-example
- key_count: 1
  name: Source Code Api File Upload Request Example
  slug: source-code-api-file-upload-request-example
- key_count: 2
  name: Source Code Api Task Locator Example
  slug: source-code-api-task-locator-example
- key_count: 4
  name: Source Code Api Validation Error Example
  slug: source-code-api-validation-error-example
- key_count: 3
  name: Source Code Api Validation Result Example
  slug: source-code-api-validation-result-example
- key_count: 3
  name: Source Code Api Validation Warning Example
  slug: source-code-api-validation-warning-example
features:
- Free CRM with unlimited free users
- Marketing Hub Starter at $9/seat/mo annual
- Marketing Hub Professional at $890/mo with mandatory $3,000 onboarding
- Marketing Hub Enterprise at $3,600/mo with $7,000 onboarding
- Sales, Service, Operations, CMS, and Content Hubs with parallel tiering
- Marketing Contact-based pricing (1k included Starter, 2k Pro, 10k Enterprise)
- Additional 5,000 contacts at $250/month on Professional
- Additional seats at $45/month (Pro) or $75/month (Enterprise)
- REST API at 250k req/day Free/Starter, 500k Pro/Enterprise
- 100 req/10s burst (Free/Starter), 150 req/10s (Pro/Enterprise)
- Search API limited to 4 req/sec
- Batch endpoints up to 100 objects per request
- Custom objects on Enterprise
- Workflows, sequences, and automation
- OAuth 2.0 and private app tokens
- Webhooks v3 for object change events
finops:
- has_sources: true
  method: derived
  name: Hubspot Finops
  primary_unit: seat
  service_category: ''
  slug: hubspot-finops
  template: false
image: https://www.hubspot.com/hubfs/HubSpot_Logos/HubSpot-Inversed-Favicon.png
integrations:
- description: Bi-directional CRM sync between HubSpot and Salesforce for unified sales and marketing data.
  name: Salesforce
- description: Send HubSpot notifications, create tasks, and share CRM data directly in Slack channels.
  name: Slack
- description: Sync contacts, calendar events, and emails between HubSpot and Google Workspace apps.
  name: Google Workspace
- description: Connect Outlook email, calendar, and contacts with HubSpot CRM for seamless productivity.
  name: Microsoft 365
- description: Automatically log Zoom meeting details and recordings on CRM contact timelines.
  name: Zoom
- description: Sync ecommerce order data, products, and customers between Shopify and HubSpot.
  name: Shopify
- description: Embed HubSpot forms, live chat, and analytics on WordPress sites with the official plugin.
  name: WordPress
- description: Process payments and sync transaction data between Stripe and HubSpot Commerce.
  name: Stripe
- description: Connect HubSpot with thousands of apps through automated Zapier workflows.
  name: Zapier
- description: Sync support tickets and development issues between HubSpot and Jira.
  name: Jira
- description: Sync invoices, payments, and customer data between HubSpot and QuickBooks.
  name: QuickBooks
- description: Share HubSpot CRM and marketing data with Snowflake for advanced analytics.
  name: Snowflake
- description: Track ad performance and sync audiences between HubSpot and Google Ads.
  name: Google Ads
- description: Create and manage Facebook ad campaigns with HubSpot audience targeting.
  name: Facebook Ads
- description: Sync LinkedIn lead gen forms and ads data with HubSpot for B2B marketing.
  name: LinkedIn
json_schemas:
- name: EventInstanceCollection
  property_count: 2
  slug: analytics-events-api-event-instance-collection
- name: EventInstance
  property_count: 6
  slug: analytics-events-api-event-instance
- name: EventTypeCollection
  property_count: 1
  slug: analytics-events-api-event-type-collection
- name: PagingNext
  property_count: 2
  slug: analytics-events-api-paging-next
- name: PagingPrevious
  property_count: 2
  slug: analytics-events-api-paging-previous
- name: Paging
  property_count: 2
  slug: analytics-events-api-paging
- name: AttachToLanguageGroupRequest
  property_count: 4
  slug: authors-api-attach-to-language-group-request
- name: BatchArchiveInput
  property_count: 1
  slug: authors-api-batch-archive-input
- name: BatchCreateInput
  property_count: 1
  slug: authors-api-batch-create-input
- name: BatchInputItem
  property_count: 2
  slug: authors-api-batch-input-item
- name: BatchInput
  property_count: 1
  slug: authors-api-batch-input
- name: BatchReadInput
  property_count: 1
  slug: authors-api-batch-read-input
- name: BatchResponse
  property_count: 6
  slug: authors-api-batch-response
- name: BatchResponseWithErrors
  property_count: 8
  slug: authors-api-batch-response-with-errors
- name: BlogAuthorCollection
  property_count: 3
  slug: authors-api-blog-author-collection
- name: BlogAuthorInput
  property_count: 9
  slug: authors-api-blog-author-input
- name: BlogAuthor
  property_count: 15
  slug: authors-api-blog-author
- name: CreateLanguageVariationRequest
  property_count: 2
  slug: authors-api-create-language-variation-request
- name: DetachFromLanguageGroupRequest
  property_count: 1
  slug: authors-api-detach-from-language-group-request
- name: PagingNext
  property_count: 2
  slug: authors-api-paging-next
- name: Paging
  property_count: 1
  slug: authors-api-paging
- name: SetLanguagePrimaryRequest
  property_count: 1
  slug: authors-api-set-language-primary-request
- name: AttachToLanguageGroupRequest
  property_count: 4
  slug: blog-posts-api-attach-to-language-group-request
- name: BatchInputItem
  property_count: 1
  slug: blog-posts-api-batch-input-item
- name: BatchInput
  property_count: 1
  slug: blog-posts-api-batch-input
- name: BatchResponse
  property_count: 6
  slug: blog-posts-api-batch-response
- name: BatchResponseWithErrors
  property_count: 8
  slug: blog-posts-api-batch-response-with-errors
- name: BlogPostCollection
  property_count: 3
  slug: blog-posts-api-blog-post-collection
- name: BlogPostInput
  property_count: 15
  slug: blog-posts-api-blog-post-input
- name: BlogPost
  property_count: 32
  slug: blog-posts-api-blog-post
- name: CloneRequest
  property_count: 1
  slug: blog-posts-api-clone-request
- name: CreateLanguageVariationRequest
  property_count: 2
  slug: blog-posts-api-create-language-variation-request
- name: DetachFromLanguageGroupRequest
  property_count: 1
  slug: blog-posts-api-detach-from-language-group-request
- name: PagingNext
  property_count: 2
  slug: blog-posts-api-paging-next
- name: PagingPrevious
  property_count: 2
  slug: blog-posts-api-paging-previous
- name: Paging
  property_count: 2
  slug: blog-posts-api-paging
- name: PushLiveRequest
  property_count: 1
  slug: blog-posts-api-push-live-request
- name: ResetDraftRequest
  property_count: 1
  slug: blog-posts-api-reset-draft-request
- name: RestorePreviousVersionRequest
  property_count: 2
  slug: blog-posts-api-restore-previous-version-request
- name: ScheduleRequest
  property_count: 2
  slug: blog-posts-api-schedule-request
- name: SetLanguagePrimaryRequest
  property_count: 1
  slug: blog-posts-api-set-language-primary-request
- name: VersionHistory
  property_count: 4
  slug: blog-posts-api-version-history
- name: CollectionResponseHubDBRow
  property_count: 2
  slug: cms-hubdb-api-collection-response-hub-dbrow
- name: CollectionResponseHubDBTable
  property_count: 2
  slug: cms-hubdb-api-collection-response-hub-dbtable
- name: HubDBColumn
  property_count: 5
  slug: cms-hubdb-api-hub-dbcolumn
- name: HubDBRowCreateRequest
  property_count: 1
  slug: cms-hubdb-api-hub-dbrow-create-request
- name: HubDBRow
  property_count: 4
  slug: cms-hubdb-api-hub-dbrow
- name: HubDBTableCreateRequest
  property_count: 3
  slug: cms-hubdb-api-hub-dbtable-create-request
- name: HubDBTable
  property_count: 9
  slug: cms-hubdb-api-hub-dbtable
- name: Paging
  property_count: 1
  slug: cms-hubdb-api-paging
- name: CollectionResponsePage
  property_count: 2
  slug: cms-pages-api-collection-response-page
- name: PageCreateRequest
  property_count: 8
  slug: cms-pages-api-page-create-request
- name: Page
  property_count: 16
  slug: cms-pages-api-page
- name: PageUpdateRequest
  property_count: 5
  slug: cms-pages-api-page-update-request
- name: Paging
  property_count: 1
  slug: cms-pages-api-paging
- name: AssociationInput
  property_count: 2
  slug: commerce-payments-api-association-input
- name: AssociationResult
  property_count: 2
  slug: commerce-payments-api-association-result
- name: AssociationType
  property_count: 2
  slug: commerce-payments-api-association-type
- name: BatchArchiveRequest
  property_count: 1
  slug: commerce-payments-api-batch-archive-request
- name: BatchCreateRequest
  property_count: 1
  slug: commerce-payments-api-batch-create-request
- name: BatchCreateResponse
  property_count: 8
  slug: commerce-payments-api-batch-create-response
- name: BatchError
  property_count: 8
  slug: commerce-payments-api-batch-error
- name: BatchReadInputItem
  property_count: 1
  slug: commerce-payments-api-batch-read-input-item
- name: BatchReadRequest
  property_count: 4
  slug: commerce-payments-api-batch-read-request
- name: BatchReadResponse
  property_count: 8
  slug: commerce-payments-api-batch-read-response
- name: BatchUpdateInputItem
  property_count: 3
  slug: commerce-payments-api-batch-update-input-item
- name: BatchUpdateRequest
  property_count: 1
  slug: commerce-payments-api-batch-update-request
- name: BatchUpdateResponse
  property_count: 8
  slug: commerce-payments-api-batch-update-response
- name: CommercePaymentCollection
  property_count: 2
  slug: commerce-payments-api-commerce-payment-collection
- name: CommercePaymentInput
  property_count: 2
  slug: commerce-payments-api-commerce-payment-input
- name: CommercePaymentPatch
  property_count: 1
  slug: commerce-payments-api-commerce-payment-patch
- name: CommercePayment
  property_count: 8
  slug: commerce-payments-api-commerce-payment
- name: FilterGroup
  property_count: 1
  slug: commerce-payments-api-filter-group
- name: Filter
  property_count: 5
  slug: commerce-payments-api-filter
- name: Paging
  property_count: 2
  slug: commerce-payments-api-paging
- name: PropertyHistory
  property_count: 6
  slug: commerce-payments-api-property-history
- name: SearchRequest
  property_count: 6
  slug: commerce-payments-api-search-request
- name: SearchResponse
  property_count: 3
  slug: commerce-payments-api-search-response
- name: SortOption
  property_count: 2
  slug: commerce-payments-api-sort-option
- name: Association
  property_count: 2
  slug: commerce-subscriptions-api-association
- name: BatchCreateInput
  property_count: 1
  slug: commerce-subscriptions-api-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: commerce-subscriptions-api-batch-read-input
- name: BatchResponseSubscription
  property_count: 3
  slug: commerce-subscriptions-api-batch-response-subscription
- name: BatchUpdateInput
  property_count: 1
  slug: commerce-subscriptions-api-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: commerce-subscriptions-api-collection-response-association
- name: CollectionResponseSubscription
  property_count: 2
  slug: commerce-subscriptions-api-collection-response-subscription
- name: FilterGroup
  property_count: 1
  slug: commerce-subscriptions-api-filter-group
- name: Filter
  property_count: 3
  slug: commerce-subscriptions-api-filter
- name: Paging
  property_count: 1
  slug: commerce-subscriptions-api-paging
- name: SearchRequest
  property_count: 6
  slug: commerce-subscriptions-api-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: commerce-subscriptions-api-simple-public-object-input
- name: Subscription
  property_count: 6
  slug: commerce-subscriptions-api-subscription
- name: ActorCollection
  property_count: 2
  slug: conversations-api-actor-collection
- name: Actor
  property_count: 5
  slug: conversations-api-actor
- name: Attachment
  property_count: 5
  slug: conversations-api-attachment
- name: ChannelCollection
  property_count: 2
  slug: conversations-api-channel-collection
- name: Channel
  property_count: 5
  slug: conversations-api-channel
- name: InboxCollection
  property_count: 3
  slug: conversations-api-inbox-collection
- name: Inbox
  property_count: 6
  slug: conversations-api-inbox
- name: MessageCollection
  property_count: 2
  slug: conversations-api-message-collection
- name: MessageRecipient
  property_count: 1
  slug: conversations-api-message-recipient
- name: Message
  property_count: 13
  slug: conversations-api-message
- name: MessageStatus
  property_count: 1
  slug: conversations-api-message-status
- name: PagingNext
  property_count: 2
  slug: conversations-api-paging-next
- name: Paging
  property_count: 1
  slug: conversations-api-paging
- name: SendMessageRequest
  property_count: 7
  slug: conversations-api-send-message-request
- name: ThreadCollection
  property_count: 2
  slug: conversations-api-thread-collection
- name: Thread
  property_count: 14
  slug: conversations-api-thread
- name: UpdateThreadRequest
  property_count: 2
  slug: conversations-api-update-thread-request
- name: AssociationDefinitionCollection
  property_count: 2
  slug: crm-associations-api-association-definition-collection
- name: AssociationDefinition
  property_count: 7
  slug: crm-associations-api-association-definition
- name: AssociationLabelCollection
  property_count: 2
  slug: crm-associations-api-association-label-collection
- name: AssociationLabel
  property_count: 3
  slug: crm-associations-api-association-label
- name: AssociationResult
  property_count: 3
  slug: crm-associations-api-association-result
- name: Association
  property_count: 2
  slug: crm-associations-api-association
- name: AssociationTypeInput
  property_count: 2
  slug: crm-associations-api-association-type-input
- name: AssociationType
  property_count: 3
  slug: crm-associations-api-association-type
- name: BatchAssociationArchiveInput
  property_count: 1
  slug: crm-associations-api-batch-association-archive-input
- name: BatchAssociationArchiveItem
  property_count: 3
  slug: crm-associations-api-batch-association-archive-item
- name: BatchAssociationCreateInput
  property_count: 1
  slug: crm-associations-api-batch-association-create-input
- name: BatchAssociationCreateItem
  property_count: 3
  slug: crm-associations-api-batch-association-create-item
- name: BatchAssociationReadInput
  property_count: 1
  slug: crm-associations-api-batch-association-read-input
- name: BatchAssociationResponse
  property_count: 8
  slug: crm-associations-api-batch-association-response
- name: CreateAssociationInput
  property_count: 2
  slug: crm-associations-api-create-association-input
- name: CreateLabelInput
  property_count: 3
  slug: crm-associations-api-create-label-input
- name: ObjectReference
  property_count: 1
  slug: crm-associations-api-object-reference
- name: PagingNext
  property_count: 2
  slug: crm-associations-api-paging-next
- name: Paging
  property_count: 1
  slug: crm-associations-api-paging
- name: Association
  property_count: 2
  slug: crm-companies-api-association
- name: BatchArchiveInput
  property_count: 1
  slug: crm-companies-api-batch-archive-input
- name: BatchCreateInput
  property_count: 1
  slug: crm-companies-api-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: crm-companies-api-batch-read-input
- name: BatchResponseCompany
  property_count: 3
  slug: crm-companies-api-batch-response-company
- name: BatchUpdateInput
  property_count: 1
  slug: crm-companies-api-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: crm-companies-api-collection-response-association
- name: CollectionResponseCompany
  property_count: 2
  slug: crm-companies-api-collection-response-company
- name: Company
  property_count: 6
  slug: crm-companies-api-company
- name: FilterGroup
  property_count: 1
  slug: crm-companies-api-filter-group
- name: Filter
  property_count: 3
  slug: crm-companies-api-filter
- name: Paging
  property_count: 1
  slug: crm-companies-api-paging
- name: SearchRequest
  property_count: 6
  slug: crm-companies-api-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: crm-companies-api-simple-public-object-input
- name: Association
  property_count: 2
  slug: crm-contacts-api-association
- name: BatchArchiveInput
  property_count: 1
  slug: crm-contacts-api-batch-archive-input
- name: BatchCreateInput
  property_count: 1
  slug: crm-contacts-api-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: crm-contacts-api-batch-read-input
- name: BatchResponseContact
  property_count: 3
  slug: crm-contacts-api-batch-response-contact
- name: BatchUpdateInput
  property_count: 1
  slug: crm-contacts-api-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: crm-contacts-api-collection-response-association
- name: CollectionResponseContact
  property_count: 2
  slug: crm-contacts-api-collection-response-contact
- name: Contact
  property_count: 6
  slug: crm-contacts-api-contact
- name: FilterGroup
  property_count: 1
  slug: crm-contacts-api-filter-group
- name: Filter
  property_count: 3
  slug: crm-contacts-api-filter
- name: Paging
  property_count: 1
  slug: crm-contacts-api-paging
- name: SearchRequest
  property_count: 6
  slug: crm-contacts-api-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: crm-contacts-api-simple-public-object-input
- name: Association
  property_count: 2
  slug: crm-deals-api-association
- name: BatchArchiveInput
  property_count: 1
  slug: crm-deals-api-batch-archive-input
- name: BatchCreateInput
  property_count: 1
  slug: crm-deals-api-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: crm-deals-api-batch-read-input
- name: BatchResponseDeal
  property_count: 3
  slug: crm-deals-api-batch-response-deal
- name: BatchUpdateInput
  property_count: 1
  slug: crm-deals-api-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: crm-deals-api-collection-response-association
- name: CollectionResponseDeal
  property_count: 2
  slug: crm-deals-api-collection-response-deal
- name: Deal
  property_count: 6
  slug: crm-deals-api-deal
- name: FilterGroup
  property_count: 1
  slug: crm-deals-api-filter-group
- name: Filter
  property_count: 3
  slug: crm-deals-api-filter
- name: Paging
  property_count: 1
  slug: crm-deals-api-paging
- name: SearchRequest
  property_count: 6
  slug: crm-deals-api-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: crm-deals-api-simple-public-object-input
- name: BatchDeleteInputItem
  property_count: 1
  slug: crm-feature-flags-api-batch-delete-input-item
- name: BatchDeleteInput
  property_count: 1
  slug: crm-feature-flags-api-batch-delete-input
- name: BatchError
  property_count: 4
  slug: crm-feature-flags-api-batch-error
- name: BatchPortalFlagStateInputItem
  property_count: 2
  slug: crm-feature-flags-api-batch-portal-flag-state-input-item
- name: BatchPortalFlagStateInput
  property_count: 1
  slug: crm-feature-flags-api-batch-portal-flag-state-input
- name: BatchPortalFlagStateResponse
  property_count: 4
  slug: crm-feature-flags-api-batch-portal-flag-state-response
- name: BatchPortalFlagStateResponseWithErrors
  property_count: 5
  slug: crm-feature-flags-api-batch-portal-flag-state-response-with-errors
- name: FeatureFlagInput
  property_count: 1
  slug: crm-feature-flags-api-feature-flag-input
- name: FeatureFlag
  property_count: 4
  slug: crm-feature-flags-api-feature-flag
- name: FlagState
  property_count: 0
  slug: crm-feature-flags-api-flag-state
- name: PagingNext
  property_count: 2
  slug: crm-feature-flags-api-paging-next
- name: Paging
  property_count: 1
  slug: crm-feature-flags-api-paging
- name: PortalFlagStateCollection
  property_count: 2
  slug: crm-feature-flags-api-portal-flag-state-collection
- name: PortalFlagStateInput
  property_count: 1
  slug: crm-feature-flags-api-portal-flag-state-input
- name: PortalFlagState
  property_count: 4
  slug: crm-feature-flags-api-portal-flag-state
- name: CollectionResponseList
  property_count: 2
  slug: crm-lists-api-collection-response-list
- name: CollectionResponseMembership
  property_count: 2
  slug: crm-lists-api-collection-response-membership
- name: ListCreateRequest
  property_count: 4
  slug: crm-lists-api-list-create-request
- name: List
  property_count: 9
  slug: crm-lists-api-list
- name: MembershipChangeRequest
  property_count: 2
  slug: crm-lists-api-membership-change-request
- name: MembershipChangeResponse
  property_count: 4
  slug: crm-lists-api-membership-change-response
- name: Membership
  property_count: 2
  slug: crm-lists-api-membership
- name: Paging
  property_count: 1
  slug: crm-lists-api-paging
- name: CRMObject
  property_count: 5
  slug: crm-search-api-crmobject
- name: FilterGroup
  property_count: 1
  slug: crm-search-api-filter-group
- name: Filter
  property_count: 5
  slug: crm-search-api-filter
- name: Paging
  property_count: 1
  slug: crm-search-api-paging
- name: SearchRequest
  property_count: 6
  slug: crm-search-api-search-request
- name: SearchResponse
  property_count: 3
  slug: crm-search-api-search-response
- name: Sort
  property_count: 2
  slug: crm-search-api-sort
- name: Association
  property_count: 2
  slug: crm-tickets-api-association
- name: BatchArchiveInput
  property_count: 1
  slug: crm-tickets-api-batch-archive-input
- name: BatchCreateInput
  property_count: 1
  slug: crm-tickets-api-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: crm-tickets-api-batch-read-input
- name: BatchResponseTicket
  property_count: 3
  slug: crm-tickets-api-batch-response-ticket
- name: BatchUpdateInput
  property_count: 1
  slug: crm-tickets-api-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: crm-tickets-api-collection-response-association
- name: CollectionResponseTicket
  property_count: 2
  slug: crm-tickets-api-collection-response-ticket
- name: FilterGroup
  property_count: 1
  slug: crm-tickets-api-filter-group
- name: Filter
  property_count: 3
  slug: crm-tickets-api-filter
- name: Paging
  property_count: 1
  slug: crm-tickets-api-paging
- name: SearchRequest
  property_count: 6
  slug: crm-tickets-api-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: crm-tickets-api-simple-public-object-input
- name: Ticket
  property_count: 6
  slug: crm-tickets-api-ticket
- name: ActionDefinitionCollection
  property_count: 2
  slug: custom-workflow-actions-api-action-definition-collection
- name: ActionDefinitionInput
  property_count: 7
  slug: custom-workflow-actions-api-action-definition-input
- name: ActionDefinitionPatch
  property_count: 7
  slug: custom-workflow-actions-api-action-definition-patch
- name: ActionDefinitionRevisionCollection
  property_count: 2
  slug: custom-workflow-actions-api-action-definition-revision-collection
- name: ActionDefinitionRevision
  property_count: 3
  slug: custom-workflow-actions-api-action-definition-revision
- name: ActionDefinition
  property_count: 10
  slug: custom-workflow-actions-api-action-definition
- name: ActionFunctionCollection
  property_count: 1
  slug: custom-workflow-actions-api-action-function-collection
- name: ActionFunctionInput
  property_count: 1
  slug: custom-workflow-actions-api-action-function-input
- name: ActionFunctionReference
  property_count: 2
  slug: custom-workflow-actions-api-action-function-reference
- name: ActionFunction
  property_count: 3
  slug: custom-workflow-actions-api-action-function
- name: ActionLabels
  property_count: 4
  slug: custom-workflow-actions-api-action-labels
- name: BatchCallbackCompletionRequest
  property_count: 1
  slug: custom-workflow-actions-api-batch-callback-completion-request
- name: BatchCallbackError
  property_count: 3
  slug: custom-workflow-actions-api-batch-callback-error
- name: BatchCallbackInput
  property_count: 2
  slug: custom-workflow-actions-api-batch-callback-input
- name: BatchCallbackResponse
  property_count: 2
  slug: custom-workflow-actions-api-batch-callback-response
- name: CallbackCompletionRequest
  property_count: 1
  slug: custom-workflow-actions-api-callback-completion-request
- name: FieldOption
  property_count: 3
  slug: custom-workflow-actions-api-field-option
- name: FieldTypeDefinition
  property_count: 6
  slug: custom-workflow-actions-api-field-type-definition
- name: InputField
  property_count: 3
  slug: custom-workflow-actions-api-input-field
- name: ObjectRequestOptions
  property_count: 1
  slug: custom-workflow-actions-api-object-request-options
- name: OutputField
  property_count: 1
  slug: custom-workflow-actions-api-output-field
- name: Paging
  property_count: 1
  slug: custom-workflow-actions-api-paging
- name: DomainCollectionResponse
  property_count: 3
  slug: domains-api-domain-collection-response
- name: Domain
  property_count: 21
  slug: domains-api-domain
- name: ForwardPaging
  property_count: 1
  slug: domains-api-forward-paging
- name: NextPage
  property_count: 2
  slug: domains-api-next-page
- name: AssociationInput
  property_count: 2
  slug: engagement-calls-api-association-input
- name: AssociationType
  property_count: 2
  slug: engagement-calls-api-association-type
- name: BatchArchiveCallsRequest
  property_count: 1
  slug: engagement-calls-api-batch-archive-calls-request
- name: BatchCallsResponse
  property_count: 7
  slug: engagement-calls-api-batch-calls-response
- name: BatchCreateCallsRequest
  property_count: 1
  slug: engagement-calls-api-batch-create-calls-request
- name: BatchError
  property_count: 5
  slug: engagement-calls-api-batch-error
- name: BatchReadCallsRequest
  property_count: 4
  slug: engagement-calls-api-batch-read-calls-request
- name: BatchReadInput
  property_count: 1
  slug: engagement-calls-api-batch-read-input
- name: BatchUpdateCallsRequest
  property_count: 1
  slug: engagement-calls-api-batch-update-calls-request
- name: BatchUpdateInput
  property_count: 2
  slug: engagement-calls-api-batch-update-input
- name: CallCollectionResponse
  property_count: 2
  slug: engagement-calls-api-call-collection-response
- name: CallCreateRequest
  property_count: 2
  slug: engagement-calls-api-call-create-request
- name: Call
  property_count: 7
  slug: engagement-calls-api-call
- name: CallSearchRequest
  property_count: 6
  slug: engagement-calls-api-call-search-request
- name: CallSearchResponse
  property_count: 3
  slug: engagement-calls-api-call-search-response
- name: CallUpdateRequest
  property_count: 1
  slug: engagement-calls-api-call-update-request
- name: FilterGroup
  property_count: 1
  slug: engagement-calls-api-filter-group
- name: Filter
  property_count: 5
  slug: engagement-calls-api-filter
- name: GdprDeleteRequest
  property_count: 2
  slug: engagement-calls-api-gdpr-delete-request
- name: NextPage
  property_count: 2
  slug: engagement-calls-api-next-page
- name: Paging
  property_count: 1
  slug: engagement-calls-api-paging
- name: PropertyHistory
  property_count: 6
  slug: engagement-calls-api-property-history
- name: SortOption
  property_count: 2
  slug: engagement-calls-api-sort-option
- name: Association
  property_count: 2
  slug: engagement-emails-api-association
- name: BatchCreateInput
  property_count: 1
  slug: engagement-emails-api-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: engagement-emails-api-batch-read-input
- name: BatchResponseEmailEngagement
  property_count: 3
  slug: engagement-emails-api-batch-response-email-engagement
- name: BatchUpdateInput
  property_count: 1
  slug: engagement-emails-api-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: engagement-emails-api-collection-response-association
- name: CollectionResponseEmailEngagement
  property_count: 2
  slug: engagement-emails-api-collection-response-email-engagement
- name: EmailEngagement
  property_count: 6
  slug: engagement-emails-api-email-engagement
- name: FilterGroup
  property_count: 1
  slug: engagement-emails-api-filter-group
- name: Filter
  property_count: 3
  slug: engagement-emails-api-filter
- name: Paging
  property_count: 1
  slug: engagement-emails-api-paging
- name: SearchRequest
  property_count: 6
  slug: engagement-emails-api-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: engagement-emails-api-simple-public-object-input
- name: Association
  property_count: 2
  slug: engagement-meetings-api-association
- name: BatchCreateInput
  property_count: 1
  slug: engagement-meetings-api-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: engagement-meetings-api-batch-read-input
- name: BatchResponseMeeting
  property_count: 3
  slug: engagement-meetings-api-batch-response-meeting
- name: BatchUpdateInput
  property_count: 1
  slug: engagement-meetings-api-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: engagement-meetings-api-collection-response-association
- name: CollectionResponseMeeting
  property_count: 2
  slug: engagement-meetings-api-collection-response-meeting
- name: FilterGroup
  property_count: 1
  slug: engagement-meetings-api-filter-group
- name: Filter
  property_count: 3
  slug: engagement-meetings-api-filter
- name: Meeting
  property_count: 6
  slug: engagement-meetings-api-meeting
- name: Paging
  property_count: 1
  slug: engagement-meetings-api-paging
- name: SearchRequest
  property_count: 6
  slug: engagement-meetings-api-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: engagement-meetings-api-simple-public-object-input
- name: AssociationInput
  property_count: 2
  slug: engagement-notes-association-input
- name: AssociationType
  property_count: 2
  slug: engagement-notes-association-type
- name: BatchArchiveNotesRequest
  property_count: 1
  slug: engagement-notes-batch-archive-notes-request
- name: BatchCreateNotesRequest
  property_count: 1
  slug: engagement-notes-batch-create-notes-request
- name: BatchError
  property_count: 5
  slug: engagement-notes-batch-error
- name: BatchNotesResponse
  property_count: 7
  slug: engagement-notes-batch-notes-response
- name: BatchReadInput
  property_count: 1
  slug: engagement-notes-batch-read-input
- name: BatchReadNotesRequest
  property_count: 4
  slug: engagement-notes-batch-read-notes-request
- name: BatchUpdateInput
  property_count: 2
  slug: engagement-notes-batch-update-input
- name: BatchUpdateNotesRequest
  property_count: 1
  slug: engagement-notes-batch-update-notes-request
- name: FilterGroup
  property_count: 1
  slug: engagement-notes-filter-group
- name: Filter
  property_count: 5
  slug: engagement-notes-filter
- name: GdprDeleteRequest
  property_count: 2
  slug: engagement-notes-gdpr-delete-request
- name: NextPage
  property_count: 2
  slug: engagement-notes-next-page
- name: NoteCollectionResponse
  property_count: 2
  slug: engagement-notes-note-collection-response
- name: NoteCreateRequest
  property_count: 2
  slug: engagement-notes-note-create-request
- name: Note
  property_count: 7
  slug: engagement-notes-note
- name: NoteSearchRequest
  property_count: 6
  slug: engagement-notes-note-search-request
- name: NoteSearchResponse
  property_count: 3
  slug: engagement-notes-note-search-response
- name: NoteUpdateRequest
  property_count: 1
  slug: engagement-notes-note-update-request
- name: Paging
  property_count: 1
  slug: engagement-notes-paging
- name: PropertyHistory
  property_count: 6
  slug: engagement-notes-property-history
- name: SortOption
  property_count: 2
  slug: engagement-notes-sort-option
- name: Association
  property_count: 2
  slug: engagement-tasks-api-association
- name: BatchCreateInput
  property_count: 1
  slug: engagement-tasks-api-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: engagement-tasks-api-batch-read-input
- name: BatchResponseTask
  property_count: 3
  slug: engagement-tasks-api-batch-response-task
- name: BatchUpdateInput
  property_count: 1
  slug: engagement-tasks-api-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: engagement-tasks-api-collection-response-association
- name: CollectionResponseTask
  property_count: 2
  slug: engagement-tasks-api-collection-response-task
- name: FilterGroup
  property_count: 1
  slug: engagement-tasks-api-filter-group
- name: Filter
  property_count: 3
  slug: engagement-tasks-api-filter
- name: Paging
  property_count: 1
  slug: engagement-tasks-api-paging
- name: SearchRequest
  property_count: 6
  slug: engagement-tasks-api-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: engagement-tasks-api-simple-public-object-input
- name: Task
  property_count: 6
  slug: engagement-tasks-api-task
- name: ErrorDetail
  property_count: 5
  slug: hubspot-analytics-events-error-detail
- name: Error
  property_count: 7
  slug: hubspot-analytics-events-error
- name: EventInstanceCollection
  property_count: 2
  slug: hubspot-analytics-events-event-instance-collection
- name: EventInstance
  property_count: 6
  slug: hubspot-analytics-events-event-instance
- name: EventTypeCollection
  property_count: 1
  slug: hubspot-analytics-events-event-type-collection
- name: PagingNext
  property_count: 2
  slug: hubspot-analytics-events-paging-next
- name: PagingPrevious
  property_count: 2
  slug: hubspot-analytics-events-paging-previous
- name: Paging
  property_count: 2
  slug: hubspot-analytics-events-paging
- name: AttachToLanguageGroupRequest
  property_count: 4
  slug: hubspot-authors-attach-to-language-group-request
- name: BatchArchiveInput
  property_count: 1
  slug: hubspot-authors-batch-archive-input
- name: BatchCreateInput
  property_count: 1
  slug: hubspot-authors-batch-create-input
- name: BatchInputItem
  property_count: 2
  slug: hubspot-authors-batch-input-item
- name: BatchInput
  property_count: 1
  slug: hubspot-authors-batch-input
- name: BatchReadInput
  property_count: 1
  slug: hubspot-authors-batch-read-input
- name: BatchResponse
  property_count: 6
  slug: hubspot-authors-batch-response
- name: BatchResponseWithErrors
  property_count: 0
  slug: hubspot-authors-batch-response-with-errors
- name: BlogAuthorCollection
  property_count: 3
  slug: hubspot-authors-blog-author-collection
- name: BlogAuthorInput
  property_count: 9
  slug: hubspot-authors-blog-author-input
- name: BlogAuthor
  property_count: 15
  slug: hubspot-authors-blog-author
- name: CreateLanguageVariationRequest
  property_count: 2
  slug: hubspot-authors-create-language-variation-request
- name: DetachFromLanguageGroupRequest
  property_count: 1
  slug: hubspot-authors-detach-from-language-group-request
- name: ErrorDetail
  property_count: 5
  slug: hubspot-authors-error-detail
- name: Error
  property_count: 7
  slug: hubspot-authors-error
- name: PagingNext
  property_count: 2
  slug: hubspot-authors-paging-next
- name: Paging
  property_count: 1
  slug: hubspot-authors-paging
- name: SetLanguagePrimaryRequest
  property_count: 1
  slug: hubspot-authors-set-language-primary-request
- name: StandardError
  property_count: 7
  slug: hubspot-authors-standard-error
- name: AttachToLanguageGroupRequest
  property_count: 4
  slug: hubspot-blog-posts-attach-to-language-group-request
- name: BatchInputItem
  property_count: 1
  slug: hubspot-blog-posts-batch-input-item
- name: BatchInput
  property_count: 1
  slug: hubspot-blog-posts-batch-input
- name: BatchResponse
  property_count: 6
  slug: hubspot-blog-posts-batch-response
- name: BatchResponseWithErrors
  property_count: 0
  slug: hubspot-blog-posts-batch-response-with-errors
- name: BlogPostCollection
  property_count: 3
  slug: hubspot-blog-posts-blog-post-collection
- name: BlogPostInput
  property_count: 15
  slug: hubspot-blog-posts-blog-post-input
- name: BlogPost
  property_count: 32
  slug: hubspot-blog-posts-blog-post
- name: CloneRequest
  property_count: 1
  slug: hubspot-blog-posts-clone-request
- name: CreateLanguageVariationRequest
  property_count: 2
  slug: hubspot-blog-posts-create-language-variation-request
- name: DetachFromLanguageGroupRequest
  property_count: 1
  slug: hubspot-blog-posts-detach-from-language-group-request
- name: ErrorDetail
  property_count: 5
  slug: hubspot-blog-posts-error-detail
- name: Error
  property_count: 7
  slug: hubspot-blog-posts-error
- name: PagingNext
  property_count: 2
  slug: hubspot-blog-posts-paging-next
- name: PagingPrevious
  property_count: 2
  slug: hubspot-blog-posts-paging-previous
- name: Paging
  property_count: 2
  slug: hubspot-blog-posts-paging
- name: PushLiveRequest
  property_count: 1
  slug: hubspot-blog-posts-push-live-request
- name: ResetDraftRequest
  property_count: 1
  slug: hubspot-blog-posts-reset-draft-request
- name: RestorePreviousVersionRequest
  property_count: 2
  slug: hubspot-blog-posts-restore-previous-version-request
- name: ScheduleRequest
  property_count: 2
  slug: hubspot-blog-posts-schedule-request
- name: SetLanguagePrimaryRequest
  property_count: 1
  slug: hubspot-blog-posts-set-language-primary-request
- name: StandardError
  property_count: 7
  slug: hubspot-blog-posts-standard-error
- name: VersionHistory
  property_count: 4
  slug: hubspot-blog-posts-version-history
- name: CollectionResponseHubDBRow
  property_count: 2
  slug: hubspot-cms-hubdb-collection-response-hub-db-row
- name: CollectionResponseHubDBTable
  property_count: 2
  slug: hubspot-cms-hubdb-collection-response-hub-db-table
- name: Error
  property_count: 4
  slug: hubspot-cms-hubdb-error
- name: HubDBColumn
  property_count: 5
  slug: hubspot-cms-hubdb-hub-db-column
- name: HubDBRowCreateRequest
  property_count: 1
  slug: hubspot-cms-hubdb-hub-db-row-create-request
- name: HubDBRow
  property_count: 4
  slug: hubspot-cms-hubdb-hub-db-row
- name: HubDBTableCreateRequest
  property_count: 3
  slug: hubspot-cms-hubdb-hub-db-table-create-request
- name: HubDBTable
  property_count: 9
  slug: hubspot-cms-hubdb-hub-db-table
- name: Paging
  property_count: 1
  slug: hubspot-cms-hubdb-paging
- name: CollectionResponsePage
  property_count: 2
  slug: hubspot-cms-pages-collection-response-page
- name: Error
  property_count: 4
  slug: hubspot-cms-pages-error
- name: PageCreateRequest
  property_count: 8
  slug: hubspot-cms-pages-page-create-request
- name: Page
  property_count: 16
  slug: hubspot-cms-pages-page
- name: PageUpdateRequest
  property_count: 5
  slug: hubspot-cms-pages-page-update-request
- name: Paging
  property_count: 1
  slug: hubspot-cms-pages-paging
- name: AssociationInput
  property_count: 2
  slug: hubspot-commerce-payments-association-input
- name: AssociationResult
  property_count: 2
  slug: hubspot-commerce-payments-association-result
- name: AssociationType
  property_count: 2
  slug: hubspot-commerce-payments-association-type
- name: BatchArchiveRequest
  property_count: 1
  slug: hubspot-commerce-payments-batch-archive-request
- name: BatchCreateRequest
  property_count: 1
  slug: hubspot-commerce-payments-batch-create-request
- name: BatchCreateResponse
  property_count: 8
  slug: hubspot-commerce-payments-batch-create-response
- name: BatchError
  property_count: 8
  slug: hubspot-commerce-payments-batch-error
- name: BatchReadInputItem
  property_count: 1
  slug: hubspot-commerce-payments-batch-read-input-item
- name: BatchReadRequest
  property_count: 4
  slug: hubspot-commerce-payments-batch-read-request
- name: BatchReadResponse
  property_count: 8
  slug: hubspot-commerce-payments-batch-read-response
- name: BatchUpdateInputItem
  property_count: 3
  slug: hubspot-commerce-payments-batch-update-input-item
- name: BatchUpdateRequest
  property_count: 1
  slug: hubspot-commerce-payments-batch-update-request
- name: BatchUpdateResponse
  property_count: 8
  slug: hubspot-commerce-payments-batch-update-response
- name: CommercePaymentCollection
  property_count: 2
  slug: hubspot-commerce-payments-commerce-payment-collection
- name: CommercePaymentInput
  property_count: 2
  slug: hubspot-commerce-payments-commerce-payment-input
- name: CommercePaymentPatch
  property_count: 1
  slug: hubspot-commerce-payments-commerce-payment-patch
- name: CommercePayment
  property_count: 8
  slug: hubspot-commerce-payments-commerce-payment
- name: ErrorDetail
  property_count: 5
  slug: hubspot-commerce-payments-error-detail
- name: Error
  property_count: 7
  slug: hubspot-commerce-payments-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-commerce-payments-filter-group
- name: Filter
  property_count: 5
  slug: hubspot-commerce-payments-filter
- name: Paging
  property_count: 2
  slug: hubspot-commerce-payments-paging
- name: PropertyHistory
  property_count: 6
  slug: hubspot-commerce-payments-property-history
- name: SearchRequest
  property_count: 6
  slug: hubspot-commerce-payments-search-request
- name: SearchResponse
  property_count: 3
  slug: hubspot-commerce-payments-search-response
- name: SortOption
  property_count: 2
  slug: hubspot-commerce-payments-sort-option
- name: Association
  property_count: 2
  slug: hubspot-commerce-subscriptions-association
- name: BatchCreateInput
  property_count: 1
  slug: hubspot-commerce-subscriptions-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: hubspot-commerce-subscriptions-batch-read-input
- name: BatchResponseSubscription
  property_count: 3
  slug: hubspot-commerce-subscriptions-batch-response-subscription
- name: BatchUpdateInput
  property_count: 1
  slug: hubspot-commerce-subscriptions-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: hubspot-commerce-subscriptions-collection-response-association
- name: CollectionResponseSubscription
  property_count: 2
  slug: hubspot-commerce-subscriptions-collection-response-subscription
- name: Error
  property_count: 4
  slug: hubspot-commerce-subscriptions-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-commerce-subscriptions-filter-group
- name: Filter
  property_count: 3
  slug: hubspot-commerce-subscriptions-filter
- name: Paging
  property_count: 1
  slug: hubspot-commerce-subscriptions-paging
- name: SearchRequest
  property_count: 6
  slug: hubspot-commerce-subscriptions-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: hubspot-commerce-subscriptions-simple-public-object-input
- name: Subscription
  property_count: 6
  slug: hubspot-commerce-subscriptions-subscription
- name: ActorCollection
  property_count: 2
  slug: hubspot-conversations-actor-collection
- name: Actor
  property_count: 5
  slug: hubspot-conversations-actor
- name: Attachment
  property_count: 5
  slug: hubspot-conversations-attachment
- name: ChannelCollection
  property_count: 2
  slug: hubspot-conversations-channel-collection
- name: Channel
  property_count: 5
  slug: hubspot-conversations-channel
- name: ErrorDetail
  property_count: 5
  slug: hubspot-conversations-error-detail
- name: Error
  property_count: 7
  slug: hubspot-conversations-error
- name: InboxCollection
  property_count: 3
  slug: hubspot-conversations-inbox-collection
- name: Inbox
  property_count: 6
  slug: hubspot-conversations-inbox
- name: MessageCollection
  property_count: 2
  slug: hubspot-conversations-message-collection
- name: MessageRecipient
  property_count: 1
  slug: hubspot-conversations-message-recipient
- name: Message
  property_count: 13
  slug: hubspot-conversations-message
- name: MessageStatus
  property_count: 1
  slug: hubspot-conversations-message-status
- name: PagingNext
  property_count: 2
  slug: hubspot-conversations-paging-next
- name: Paging
  property_count: 1
  slug: hubspot-conversations-paging
- name: SendMessageRequest
  property_count: 7
  slug: hubspot-conversations-send-message-request
- name: ThreadCollection
  property_count: 2
  slug: hubspot-conversations-thread-collection
- name: Thread
  property_count: 14
  slug: hubspot-conversations-thread
- name: UpdateThreadRequest
  property_count: 2
  slug: hubspot-conversations-update-thread-request
- name: AssociationDefinitionCollection
  property_count: 2
  slug: hubspot-crm-associations-association-definition-collection
- name: AssociationDefinition
  property_count: 7
  slug: hubspot-crm-associations-association-definition
- name: AssociationLabelCollection
  property_count: 2
  slug: hubspot-crm-associations-association-label-collection
- name: AssociationLabel
  property_count: 3
  slug: hubspot-crm-associations-association-label
- name: AssociationResult
  property_count: 3
  slug: hubspot-crm-associations-association-result
- name: Association
  property_count: 2
  slug: hubspot-crm-associations-association
- name: AssociationTypeInput
  property_count: 2
  slug: hubspot-crm-associations-association-type-input
- name: AssociationType
  property_count: 3
  slug: hubspot-crm-associations-association-type
- name: BatchAssociationArchiveInput
  property_count: 1
  slug: hubspot-crm-associations-batch-association-archive-input
- name: BatchAssociationArchiveItem
  property_count: 3
  slug: hubspot-crm-associations-batch-association-archive-item
- name: BatchAssociationCreateInput
  property_count: 1
  slug: hubspot-crm-associations-batch-association-create-input
- name: BatchAssociationCreateItem
  property_count: 3
  slug: hubspot-crm-associations-batch-association-create-item
- name: BatchAssociationReadInput
  property_count: 1
  slug: hubspot-crm-associations-batch-association-read-input
- name: BatchAssociationResponse
  property_count: 8
  slug: hubspot-crm-associations-batch-association-response
- name: CreateAssociationInput
  property_count: 2
  slug: hubspot-crm-associations-create-association-input
- name: CreateLabelInput
  property_count: 3
  slug: hubspot-crm-associations-create-label-input
- name: ErrorDetail
  property_count: 5
  slug: hubspot-crm-associations-error-detail
- name: Error
  property_count: 7
  slug: hubspot-crm-associations-error
- name: ObjectReference
  property_count: 1
  slug: hubspot-crm-associations-object-reference
- name: PagingNext
  property_count: 2
  slug: hubspot-crm-associations-paging-next
- name: Paging
  property_count: 1
  slug: hubspot-crm-associations-paging
- name: StandardError
  property_count: 7
  slug: hubspot-crm-associations-standard-error
- name: Association
  property_count: 2
  slug: hubspot-crm-companies-association
- name: BatchArchiveInput
  property_count: 1
  slug: hubspot-crm-companies-batch-archive-input
- name: BatchCreateInput
  property_count: 1
  slug: hubspot-crm-companies-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: hubspot-crm-companies-batch-read-input
- name: BatchResponseCompany
  property_count: 3
  slug: hubspot-crm-companies-batch-response-company
- name: BatchUpdateInput
  property_count: 1
  slug: hubspot-crm-companies-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: hubspot-crm-companies-collection-response-association
- name: CollectionResponseCompany
  property_count: 2
  slug: hubspot-crm-companies-collection-response-company
- name: Company
  property_count: 6
  slug: hubspot-crm-companies-company
- name: Error
  property_count: 4
  slug: hubspot-crm-companies-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-crm-companies-filter-group
- name: Filter
  property_count: 3
  slug: hubspot-crm-companies-filter
- name: Paging
  property_count: 1
  slug: hubspot-crm-companies-paging
- name: SearchRequest
  property_count: 6
  slug: hubspot-crm-companies-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: hubspot-crm-companies-simple-public-object-input
- name: Association
  property_count: 2
  slug: hubspot-crm-contacts-association
- name: BatchArchiveInput
  property_count: 1
  slug: hubspot-crm-contacts-batch-archive-input
- name: BatchCreateInput
  property_count: 1
  slug: hubspot-crm-contacts-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: hubspot-crm-contacts-batch-read-input
- name: BatchResponseContact
  property_count: 3
  slug: hubspot-crm-contacts-batch-response-contact
- name: BatchUpdateInput
  property_count: 1
  slug: hubspot-crm-contacts-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: hubspot-crm-contacts-collection-response-association
- name: CollectionResponseContact
  property_count: 2
  slug: hubspot-crm-contacts-collection-response-contact
- name: Contact
  property_count: 6
  slug: hubspot-crm-contacts-contact
- name: Error
  property_count: 4
  slug: hubspot-crm-contacts-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-crm-contacts-filter-group
- name: Filter
  property_count: 3
  slug: hubspot-crm-contacts-filter
- name: Paging
  property_count: 1
  slug: hubspot-crm-contacts-paging
- name: SearchRequest
  property_count: 6
  slug: hubspot-crm-contacts-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: hubspot-crm-contacts-simple-public-object-input
- name: Association
  property_count: 2
  slug: hubspot-crm-deals-association
- name: BatchArchiveInput
  property_count: 1
  slug: hubspot-crm-deals-batch-archive-input
- name: BatchCreateInput
  property_count: 1
  slug: hubspot-crm-deals-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: hubspot-crm-deals-batch-read-input
- name: BatchResponseDeal
  property_count: 3
  slug: hubspot-crm-deals-batch-response-deal
- name: BatchUpdateInput
  property_count: 1
  slug: hubspot-crm-deals-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: hubspot-crm-deals-collection-response-association
- name: CollectionResponseDeal
  property_count: 2
  slug: hubspot-crm-deals-collection-response-deal
- name: Deal
  property_count: 6
  slug: hubspot-crm-deals-deal
- name: Error
  property_count: 4
  slug: hubspot-crm-deals-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-crm-deals-filter-group
- name: Filter
  property_count: 3
  slug: hubspot-crm-deals-filter
- name: Paging
  property_count: 1
  slug: hubspot-crm-deals-paging
- name: SearchRequest
  property_count: 6
  slug: hubspot-crm-deals-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: hubspot-crm-deals-simple-public-object-input
- name: BatchDeleteInputItem
  property_count: 1
  slug: hubspot-crm-feature-flags-batch-delete-input-item
- name: BatchDeleteInput
  property_count: 1
  slug: hubspot-crm-feature-flags-batch-delete-input
- name: BatchError
  property_count: 4
  slug: hubspot-crm-feature-flags-batch-error
- name: BatchPortalFlagStateInputItem
  property_count: 2
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-input-item
- name: BatchPortalFlagStateInput
  property_count: 1
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-input
- name: BatchPortalFlagStateResponse
  property_count: 4
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-response
- name: BatchPortalFlagStateResponseWithErrors
  property_count: 5
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-response-with-errors
- name: ErrorDetail
  property_count: 5
  slug: hubspot-crm-feature-flags-error-detail
- name: Error
  property_count: 7
  slug: hubspot-crm-feature-flags-error
- name: FeatureFlagInput
  property_count: 1
  slug: hubspot-crm-feature-flags-feature-flag-input
- name: FeatureFlag
  property_count: 4
  slug: hubspot-crm-feature-flags-feature-flag
- name: FlagState
  property_count: 0
  slug: hubspot-crm-feature-flags-flag-state
- name: PagingNext
  property_count: 2
  slug: hubspot-crm-feature-flags-paging-next
- name: Paging
  property_count: 1
  slug: hubspot-crm-feature-flags-paging
- name: PortalFlagStateCollection
  property_count: 2
  slug: hubspot-crm-feature-flags-portal-flag-state-collection
- name: PortalFlagStateInput
  property_count: 1
  slug: hubspot-crm-feature-flags-portal-flag-state-input
- name: PortalFlagState
  property_count: 4
  slug: hubspot-crm-feature-flags-portal-flag-state
- name: CollectionResponseList
  property_count: 2
  slug: hubspot-crm-lists-collection-response-list
- name: CollectionResponseMembership
  property_count: 2
  slug: hubspot-crm-lists-collection-response-membership
- name: Error
  property_count: 4
  slug: hubspot-crm-lists-error
- name: ListCreateRequest
  property_count: 4
  slug: hubspot-crm-lists-list-create-request
- name: List
  property_count: 9
  slug: hubspot-crm-lists-list
- name: MembershipChangeRequest
  property_count: 2
  slug: hubspot-crm-lists-membership-change-request
- name: MembershipChangeResponse
  property_count: 4
  slug: hubspot-crm-lists-membership-change-response
- name: Membership
  property_count: 2
  slug: hubspot-crm-lists-membership
- name: Paging
  property_count: 1
  slug: hubspot-crm-lists-paging
- name: HubSpot CRM Object
  property_count: 8
  slug: hubspot-crm-object
- name: CRMObject
  property_count: 5
  slug: hubspot-crm-search-crm-object
- name: Error
  property_count: 5
  slug: hubspot-crm-search-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-crm-search-filter-group
- name: Filter
  property_count: 5
  slug: hubspot-crm-search-filter
- name: Paging
  property_count: 1
  slug: hubspot-crm-search-paging
- name: HubSpot CRM Search Request
  property_count: 6
  slug: hubspot-crm-search-request
- name: SearchRequest
  property_count: 6
  slug: hubspot-crm-search-search-request
- name: SearchResponse
  property_count: 3
  slug: hubspot-crm-search-search-response
- name: Sort
  property_count: 2
  slug: hubspot-crm-search-sort
- name: Association
  property_count: 2
  slug: hubspot-crm-tickets-association
- name: BatchArchiveInput
  property_count: 1
  slug: hubspot-crm-tickets-batch-archive-input
- name: BatchCreateInput
  property_count: 1
  slug: hubspot-crm-tickets-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: hubspot-crm-tickets-batch-read-input
- name: BatchResponseTicket
  property_count: 3
  slug: hubspot-crm-tickets-batch-response-ticket
- name: BatchUpdateInput
  property_count: 1
  slug: hubspot-crm-tickets-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: hubspot-crm-tickets-collection-response-association
- name: CollectionResponseTicket
  property_count: 2
  slug: hubspot-crm-tickets-collection-response-ticket
- name: Error
  property_count: 4
  slug: hubspot-crm-tickets-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-crm-tickets-filter-group
- name: Filter
  property_count: 3
  slug: hubspot-crm-tickets-filter
- name: Paging
  property_count: 1
  slug: hubspot-crm-tickets-paging
- name: SearchRequest
  property_count: 6
  slug: hubspot-crm-tickets-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: hubspot-crm-tickets-simple-public-object-input
- name: Ticket
  property_count: 6
  slug: hubspot-crm-tickets-ticket
- name: ActionDefinitionCollection
  property_count: 2
  slug: hubspot-custom-workflow-actions-action-definition-collection
- name: ActionDefinitionInput
  property_count: 7
  slug: hubspot-custom-workflow-actions-action-definition-input
- name: ActionDefinitionPatch
  property_count: 7
  slug: hubspot-custom-workflow-actions-action-definition-patch
- name: ActionDefinitionRevisionCollection
  property_count: 2
  slug: hubspot-custom-workflow-actions-action-definition-revision-collection
- name: ActionDefinitionRevision
  property_count: 3
  slug: hubspot-custom-workflow-actions-action-definition-revision
- name: ActionDefinition
  property_count: 10
  slug: hubspot-custom-workflow-actions-action-definition
- name: ActionFunctionCollection
  property_count: 1
  slug: hubspot-custom-workflow-actions-action-function-collection
- name: ActionFunctionInput
  property_count: 1
  slug: hubspot-custom-workflow-actions-action-function-input
- name: ActionFunctionReference
  property_count: 2
  slug: hubspot-custom-workflow-actions-action-function-reference
- name: ActionFunction
  property_count: 3
  slug: hubspot-custom-workflow-actions-action-function
- name: ActionLabels
  property_count: 4
  slug: hubspot-custom-workflow-actions-action-labels
- name: BatchCallbackCompletionRequest
  property_count: 1
  slug: hubspot-custom-workflow-actions-batch-callback-completion-request
- name: BatchCallbackError
  property_count: 3
  slug: hubspot-custom-workflow-actions-batch-callback-error
- name: BatchCallbackInput
  property_count: 2
  slug: hubspot-custom-workflow-actions-batch-callback-input
- name: BatchCallbackResponse
  property_count: 2
  slug: hubspot-custom-workflow-actions-batch-callback-response
- name: CallbackCompletionRequest
  property_count: 1
  slug: hubspot-custom-workflow-actions-callback-completion-request
- name: ErrorDetail
  property_count: 5
  slug: hubspot-custom-workflow-actions-error-detail
- name: Error
  property_count: 7
  slug: hubspot-custom-workflow-actions-error
- name: FieldOption
  property_count: 3
  slug: hubspot-custom-workflow-actions-field-option
- name: FieldTypeDefinition
  property_count: 6
  slug: hubspot-custom-workflow-actions-field-type-definition
- name: InputField
  property_count: 3
  slug: hubspot-custom-workflow-actions-input-field
- name: ObjectRequestOptions
  property_count: 1
  slug: hubspot-custom-workflow-actions-object-request-options
- name: OutputField
  property_count: 1
  slug: hubspot-custom-workflow-actions-output-field
- name: Paging
  property_count: 1
  slug: hubspot-custom-workflow-actions-paging
- name: DomainCollectionResponse
  property_count: 3
  slug: hubspot-domains-domain-collection-response
- name: Domain
  property_count: 21
  slug: hubspot-domains-domain
- name: ErrorDetail
  property_count: 5
  slug: hubspot-domains-error-detail
- name: Error
  property_count: 7
  slug: hubspot-domains-error
- name: ForwardPaging
  property_count: 1
  slug: hubspot-domains-forward-paging
- name: NextPage
  property_count: 2
  slug: hubspot-domains-next-page
- name: AssociationInput
  property_count: 2
  slug: hubspot-engagement-calls-association-input
- name: AssociationType
  property_count: 2
  slug: hubspot-engagement-calls-association-type
- name: BatchArchiveCallsRequest
  property_count: 1
  slug: hubspot-engagement-calls-batch-archive-calls-request
- name: BatchCallsResponse
  property_count: 7
  slug: hubspot-engagement-calls-batch-calls-response
- name: BatchCreateCallsRequest
  property_count: 1
  slug: hubspot-engagement-calls-batch-create-calls-request
- name: BatchError
  property_count: 5
  slug: hubspot-engagement-calls-batch-error
- name: BatchReadCallsRequest
  property_count: 4
  slug: hubspot-engagement-calls-batch-read-calls-request
- name: BatchReadInput
  property_count: 1
  slug: hubspot-engagement-calls-batch-read-input
- name: BatchUpdateCallsRequest
  property_count: 1
  slug: hubspot-engagement-calls-batch-update-calls-request
- name: BatchUpdateInput
  property_count: 2
  slug: hubspot-engagement-calls-batch-update-input
- name: CallCollectionResponse
  property_count: 2
  slug: hubspot-engagement-calls-call-collection-response
- name: CallCreateRequest
  property_count: 2
  slug: hubspot-engagement-calls-call-create-request
- name: Call
  property_count: 7
  slug: hubspot-engagement-calls-call
- name: CallSearchRequest
  property_count: 6
  slug: hubspot-engagement-calls-call-search-request
- name: CallSearchResponse
  property_count: 3
  slug: hubspot-engagement-calls-call-search-response
- name: CallUpdateRequest
  property_count: 1
  slug: hubspot-engagement-calls-call-update-request
- name: ErrorDetail
  property_count: 5
  slug: hubspot-engagement-calls-error-detail
- name: Error
  property_count: 7
  slug: hubspot-engagement-calls-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-engagement-calls-filter-group
- name: Filter
  property_count: 5
  slug: hubspot-engagement-calls-filter
- name: GdprDeleteRequest
  property_count: 2
  slug: hubspot-engagement-calls-gdpr-delete-request
- name: NextPage
  property_count: 2
  slug: hubspot-engagement-calls-next-page
- name: Paging
  property_count: 1
  slug: hubspot-engagement-calls-paging
- name: PropertyHistory
  property_count: 6
  slug: hubspot-engagement-calls-property-history
- name: SortOption
  property_count: 2
  slug: hubspot-engagement-calls-sort-option
- name: Association
  property_count: 2
  slug: hubspot-engagement-emails-association
- name: BatchCreateInput
  property_count: 1
  slug: hubspot-engagement-emails-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: hubspot-engagement-emails-batch-read-input
- name: BatchResponseEmailEngagement
  property_count: 3
  slug: hubspot-engagement-emails-batch-response-email-engagement
- name: BatchUpdateInput
  property_count: 1
  slug: hubspot-engagement-emails-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: hubspot-engagement-emails-collection-response-association
- name: CollectionResponseEmailEngagement
  property_count: 2
  slug: hubspot-engagement-emails-collection-response-email-engagement
- name: EmailEngagement
  property_count: 6
  slug: hubspot-engagement-emails-email-engagement
- name: Error
  property_count: 4
  slug: hubspot-engagement-emails-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-engagement-emails-filter-group
- name: Filter
  property_count: 3
  slug: hubspot-engagement-emails-filter
- name: Paging
  property_count: 1
  slug: hubspot-engagement-emails-paging
- name: SearchRequest
  property_count: 6
  slug: hubspot-engagement-emails-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: hubspot-engagement-emails-simple-public-object-input
- name: Association
  property_count: 2
  slug: hubspot-engagement-meetings-association
- name: BatchCreateInput
  property_count: 1
  slug: hubspot-engagement-meetings-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: hubspot-engagement-meetings-batch-read-input
- name: BatchResponseMeeting
  property_count: 3
  slug: hubspot-engagement-meetings-batch-response-meeting
- name: BatchUpdateInput
  property_count: 1
  slug: hubspot-engagement-meetings-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: hubspot-engagement-meetings-collection-response-association
- name: CollectionResponseMeeting
  property_count: 2
  slug: hubspot-engagement-meetings-collection-response-meeting
- name: Error
  property_count: 4
  slug: hubspot-engagement-meetings-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-engagement-meetings-filter-group
- name: Filter
  property_count: 3
  slug: hubspot-engagement-meetings-filter
- name: Meeting
  property_count: 6
  slug: hubspot-engagement-meetings-meeting
- name: Paging
  property_count: 1
  slug: hubspot-engagement-meetings-paging
- name: SearchRequest
  property_count: 6
  slug: hubspot-engagement-meetings-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: hubspot-engagement-meetings-simple-public-object-input
- name: AssociationInput
  property_count: 2
  slug: hubspot-engagement-notes-association-input
- name: AssociationType
  property_count: 2
  slug: hubspot-engagement-notes-association-type
- name: BatchArchiveNotesRequest
  property_count: 1
  slug: hubspot-engagement-notes-batch-archive-notes-request
- name: BatchCreateNotesRequest
  property_count: 1
  slug: hubspot-engagement-notes-batch-create-notes-request
- name: BatchError
  property_count: 5
  slug: hubspot-engagement-notes-batch-error
- name: BatchNotesResponse
  property_count: 7
  slug: hubspot-engagement-notes-batch-notes-response
- name: BatchReadInput
  property_count: 1
  slug: hubspot-engagement-notes-batch-read-input
- name: BatchReadNotesRequest
  property_count: 4
  slug: hubspot-engagement-notes-batch-read-notes-request
- name: BatchUpdateInput
  property_count: 2
  slug: hubspot-engagement-notes-batch-update-input
- name: BatchUpdateNotesRequest
  property_count: 1
  slug: hubspot-engagement-notes-batch-update-notes-request
- name: ErrorDetail
  property_count: 5
  slug: hubspot-engagement-notes-error-detail
- name: Error
  property_count: 7
  slug: hubspot-engagement-notes-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-engagement-notes-filter-group
- name: Filter
  property_count: 5
  slug: hubspot-engagement-notes-filter
- name: GdprDeleteRequest
  property_count: 2
  slug: hubspot-engagement-notes-gdpr-delete-request
- name: NextPage
  property_count: 2
  slug: hubspot-engagement-notes-next-page
- name: NoteCollectionResponse
  property_count: 2
  slug: hubspot-engagement-notes-note-collection-response
- name: NoteCreateRequest
  property_count: 2
  slug: hubspot-engagement-notes-note-create-request
- name: Note
  property_count: 7
  slug: hubspot-engagement-notes-note
- name: NoteSearchRequest
  property_count: 6
  slug: hubspot-engagement-notes-note-search-request
- name: NoteSearchResponse
  property_count: 3
  slug: hubspot-engagement-notes-note-search-response
- name: NoteUpdateRequest
  property_count: 1
  slug: hubspot-engagement-notes-note-update-request
- name: Paging
  property_count: 1
  slug: hubspot-engagement-notes-paging
- name: PropertyHistory
  property_count: 6
  slug: hubspot-engagement-notes-property-history
- name: SortOption
  property_count: 2
  slug: hubspot-engagement-notes-sort-option
- name: Association
  property_count: 2
  slug: hubspot-engagement-tasks-association
- name: BatchCreateInput
  property_count: 1
  slug: hubspot-engagement-tasks-batch-create-input
- name: BatchReadInput
  property_count: 2
  slug: hubspot-engagement-tasks-batch-read-input
- name: BatchResponseTask
  property_count: 3
  slug: hubspot-engagement-tasks-batch-response-task
- name: BatchUpdateInput
  property_count: 1
  slug: hubspot-engagement-tasks-batch-update-input
- name: CollectionResponseAssociation
  property_count: 2
  slug: hubspot-engagement-tasks-collection-response-association
- name: CollectionResponseTask
  property_count: 2
  slug: hubspot-engagement-tasks-collection-response-task
- name: Error
  property_count: 4
  slug: hubspot-engagement-tasks-error
- name: FilterGroup
  property_count: 1
  slug: hubspot-engagement-tasks-filter-group
- name: Filter
  property_count: 3
  slug: hubspot-engagement-tasks-filter
- name: Paging
  property_count: 1
  slug: hubspot-engagement-tasks-paging
- name: SearchRequest
  property_count: 6
  slug: hubspot-engagement-tasks-search-request
- name: SimplePublicObjectInput
  property_count: 1
  slug: hubspot-engagement-tasks-simple-public-object-input
- name: Task
  property_count: 6
  slug: hubspot-engagement-tasks-task
- name: EmailMessage
  property_count: 6
  slug: hubspot-marketing-emal-email-message
- name: ErrorDetail
  property_count: 5
  slug: hubspot-marketing-emal-error-detail
- name: Error
  property_count: 7
  slug: hubspot-marketing-emal-error
- name: NextPage
  property_count: 2
  slug: hubspot-marketing-emal-next-page
- name: Paging
  property_count: 1
  slug: hubspot-marketing-emal-paging
- name: SmtpTokenCollectionResponse
  property_count: 2
  slug: hubspot-marketing-emal-smtp-token-collection-response
- name: SmtpTokenCreateRequest
  property_count: 2
  slug: hubspot-marketing-emal-smtp-token-create-request
- name: SmtpToken
  property_count: 6
  slug: hubspot-marketing-emal-smtp-token
- name: SmtpTokenWithPassword
  property_count: 7
  slug: hubspot-marketing-emal-smtp-token-with-password
- name: TransactionalEmailRequest
  property_count: 4
  slug: hubspot-marketing-emal-transactional-email-request
- name: TransactionalEmailResponse
  property_count: 6
  slug: hubspot-marketing-emal-transactional-email-response
- name: AccessTokenMetadata
  property_count: 9
  slug: hubspot-oauth-access-token-metadata
- name: ErrorDetail
  property_count: 5
  slug: hubspot-oauth-error-detail
- name: Error
  property_count: 7
  slug: hubspot-oauth-error
- name: RefreshTokenMetadata
  property_count: 6
  slug: hubspot-oauth-refresh-token-metadata
- name: TokenRequest
  property_count: 6
  slug: hubspot-oauth-token-request
- name: TokenResponse
  property_count: 5
  slug: hubspot-oauth-token-response
- name: ActionResponse
  property_count: 5
  slug: hubspot-source-code-action-response
- name: AssetFileMetadata
  property_count: 8
  slug: hubspot-source-code-asset-file-metadata
- name: ErrorDetail
  property_count: 5
  slug: hubspot-source-code-error-detail
- name: Error
  property_count: 7
  slug: hubspot-source-code-error
- name: FileExtractRequest
  property_count: 1
  slug: hubspot-source-code-file-extract-request
- name: FileUploadRequest
  property_count: 1
  slug: hubspot-source-code-file-upload-request
- name: TaskLocator
  property_count: 2
  slug: hubspot-source-code-task-locator
- name: ValidationError
  property_count: 4
  slug: hubspot-source-code-validation-error
- name: ValidationResult
  property_count: 3
  slug: hubspot-source-code-validation-result
- name: ValidationWarning
  property_count: 3
  slug: hubspot-source-code-validation-warning
- name: EmailMessage
  property_count: 6
  slug: marketing-emal-api-email-message
- name: NextPage
  property_count: 2
  slug: marketing-emal-api-next-page
- name: Paging
  property_count: 1
  slug: marketing-emal-api-paging
- name: SmtpTokenCollectionResponse
  property_count: 2
  slug: marketing-emal-api-smtp-token-collection-response
- name: SmtpTokenCreateRequest
  property_count: 2
  slug: marketing-emal-api-smtp-token-create-request
- name: SmtpToken
  property_count: 6
  slug: marketing-emal-api-smtp-token
- name: SmtpTokenWithPassword
  property_count: 7
  slug: marketing-emal-api-smtp-token-with-password
- name: TransactionalEmailRequest
  property_count: 4
  slug: marketing-emal-api-transactional-email-request
- name: TransactionalEmailResponse
  property_count: 6
  slug: marketing-emal-api-transactional-email-response
- name: AccessTokenMetadata
  property_count: 9
  slug: oauth-api-access-token-metadata
- name: RefreshTokenMetadata
  property_count: 6
  slug: oauth-api-refresh-token-metadata
- name: TokenRequest
  property_count: 6
  slug: oauth-api-token-request
- name: TokenResponse
  property_count: 5
  slug: oauth-api-token-response
- name: ActionResponse
  property_count: 5
  slug: source-code-api-action-response
- name: AssetFileMetadata
  property_count: 8
  slug: source-code-api-asset-file-metadata
- name: FileExtractRequest
  property_count: 1
  slug: source-code-api-file-extract-request
- name: FileUploadRequest
  property_count: 1
  slug: source-code-api-file-upload-request
- name: TaskLocator
  property_count: 2
  slug: source-code-api-task-locator
- name: ValidationError
  property_count: 4
  slug: source-code-api-validation-error
- name: ValidationResult
  property_count: 3
  slug: source-code-api-validation-result
- name: ValidationWarning
  property_count: 3
  slug: source-code-api-validation-warning
json_structures:
- name: Analytics Events Api Event Instance Collection Structure
  property_count: 2
  slug: analytics-events-api-event-instance-collection-structure
- name: Analytics Events Api Event Instance Structure
  property_count: 6
  slug: analytics-events-api-event-instance-structure
- name: Analytics Events Api Event Type Collection Structure
  property_count: 1
  slug: analytics-events-api-event-type-collection-structure
- name: Analytics Events Api Paging Next Structure
  property_count: 2
  slug: analytics-events-api-paging-next-structure
- name: Analytics Events Api Paging Previous Structure
  property_count: 2
  slug: analytics-events-api-paging-previous-structure
- name: Analytics Events Api Paging Structure
  property_count: 2
  slug: analytics-events-api-paging-structure
- name: Authors Api Attach To Language Group Request Structure
  property_count: 4
  slug: authors-api-attach-to-language-group-request-structure
- name: Authors Api Batch Archive Input Structure
  property_count: 1
  slug: authors-api-batch-archive-input-structure
- name: Authors Api Batch Create Input Structure
  property_count: 1
  slug: authors-api-batch-create-input-structure
- name: Authors Api Batch Input Item Structure
  property_count: 2
  slug: authors-api-batch-input-item-structure
- name: Authors Api Batch Input Structure
  property_count: 1
  slug: authors-api-batch-input-structure
- name: Authors Api Batch Read Input Structure
  property_count: 1
  slug: authors-api-batch-read-input-structure
- name: Authors Api Batch Response Structure
  property_count: 6
  slug: authors-api-batch-response-structure
- name: Authors Api Batch Response With Errors Structure
  property_count: 0
  slug: authors-api-batch-response-with-errors-structure
- name: Authors Api Blog Author Collection Structure
  property_count: 3
  slug: authors-api-blog-author-collection-structure
- name: Authors Api Blog Author Input Structure
  property_count: 9
  slug: authors-api-blog-author-input-structure
- name: Authors Api Blog Author Structure
  property_count: 15
  slug: authors-api-blog-author-structure
- name: Authors Api Create Language Variation Request Structure
  property_count: 2
  slug: authors-api-create-language-variation-request-structure
- name: Authors Api Detach From Language Group Request Structure
  property_count: 1
  slug: authors-api-detach-from-language-group-request-structure
- name: Authors Api Paging Next Structure
  property_count: 2
  slug: authors-api-paging-next-structure
- name: Authors Api Paging Structure
  property_count: 1
  slug: authors-api-paging-structure
- name: Authors Api Set Language Primary Request Structure
  property_count: 1
  slug: authors-api-set-language-primary-request-structure
- name: Blog Posts Api Attach To Language Group Request Structure
  property_count: 4
  slug: blog-posts-api-attach-to-language-group-request-structure
- name: Blog Posts Api Batch Input Item Structure
  property_count: 1
  slug: blog-posts-api-batch-input-item-structure
- name: Blog Posts Api Batch Input Structure
  property_count: 1
  slug: blog-posts-api-batch-input-structure
- name: Blog Posts Api Batch Response Structure
  property_count: 6
  slug: blog-posts-api-batch-response-structure
- name: Blog Posts Api Batch Response With Errors Structure
  property_count: 0
  slug: blog-posts-api-batch-response-with-errors-structure
- name: Blog Posts Api Blog Post Collection Structure
  property_count: 3
  slug: blog-posts-api-blog-post-collection-structure
- name: Blog Posts Api Blog Post Input Structure
  property_count: 15
  slug: blog-posts-api-blog-post-input-structure
- name: Blog Posts Api Blog Post Structure
  property_count: 32
  slug: blog-posts-api-blog-post-structure
- name: Blog Posts Api Clone Request Structure
  property_count: 1
  slug: blog-posts-api-clone-request-structure
- name: Blog Posts Api Create Language Variation Request Structure
  property_count: 2
  slug: blog-posts-api-create-language-variation-request-structure
- name: Blog Posts Api Detach From Language Group Request Structure
  property_count: 1
  slug: blog-posts-api-detach-from-language-group-request-structure
- name: Blog Posts Api Paging Next Structure
  property_count: 2
  slug: blog-posts-api-paging-next-structure
- name: Blog Posts Api Paging Previous Structure
  property_count: 2
  slug: blog-posts-api-paging-previous-structure
- name: Blog Posts Api Paging Structure
  property_count: 2
  slug: blog-posts-api-paging-structure
- name: Blog Posts Api Push Live Request Structure
  property_count: 1
  slug: blog-posts-api-push-live-request-structure
- name: Blog Posts Api Reset Draft Request Structure
  property_count: 1
  slug: blog-posts-api-reset-draft-request-structure
- name: Blog Posts Api Restore Previous Version Request Structure
  property_count: 2
  slug: blog-posts-api-restore-previous-version-request-structure
- name: Blog Posts Api Schedule Request Structure
  property_count: 2
  slug: blog-posts-api-schedule-request-structure
- name: Blog Posts Api Set Language Primary Request Structure
  property_count: 1
  slug: blog-posts-api-set-language-primary-request-structure
- name: Blog Posts Api Version History Structure
  property_count: 4
  slug: blog-posts-api-version-history-structure
- name: Cms Hubdb Api Collection Response Hub Dbrow Structure
  property_count: 2
  slug: cms-hubdb-api-collection-response-hub-dbrow-structure
- name: Cms Hubdb Api Collection Response Hub Dbtable Structure
  property_count: 2
  slug: cms-hubdb-api-collection-response-hub-dbtable-structure
- name: Cms Hubdb Api Hub Dbcolumn Structure
  property_count: 5
  slug: cms-hubdb-api-hub-dbcolumn-structure
- name: Cms Hubdb Api Hub Dbrow Create Request Structure
  property_count: 1
  slug: cms-hubdb-api-hub-dbrow-create-request-structure
- name: Cms Hubdb Api Hub Dbrow Structure
  property_count: 4
  slug: cms-hubdb-api-hub-dbrow-structure
- name: Cms Hubdb Api Hub Dbtable Create Request Structure
  property_count: 3
  slug: cms-hubdb-api-hub-dbtable-create-request-structure
- name: Cms Hubdb Api Hub Dbtable Structure
  property_count: 9
  slug: cms-hubdb-api-hub-dbtable-structure
- name: Cms Hubdb Api Paging Structure
  property_count: 1
  slug: cms-hubdb-api-paging-structure
- name: Cms Pages Api Collection Response Page Structure
  property_count: 2
  slug: cms-pages-api-collection-response-page-structure
- name: Cms Pages Api Page Create Request Structure
  property_count: 8
  slug: cms-pages-api-page-create-request-structure
- name: Cms Pages Api Page Structure
  property_count: 16
  slug: cms-pages-api-page-structure
- name: Cms Pages Api Page Update Request Structure
  property_count: 5
  slug: cms-pages-api-page-update-request-structure
- name: Cms Pages Api Paging Structure
  property_count: 1
  slug: cms-pages-api-paging-structure
- name: Commerce Payments Api Association Input Structure
  property_count: 2
  slug: commerce-payments-api-association-input-structure
- name: Commerce Payments Api Association Result Structure
  property_count: 2
  slug: commerce-payments-api-association-result-structure
- name: Commerce Payments Api Association Type Structure
  property_count: 2
  slug: commerce-payments-api-association-type-structure
- name: Commerce Payments Api Batch Archive Request Structure
  property_count: 1
  slug: commerce-payments-api-batch-archive-request-structure
- name: Commerce Payments Api Batch Create Request Structure
  property_count: 1
  slug: commerce-payments-api-batch-create-request-structure
- name: Commerce Payments Api Batch Create Response Structure
  property_count: 8
  slug: commerce-payments-api-batch-create-response-structure
- name: Commerce Payments Api Batch Error Structure
  property_count: 8
  slug: commerce-payments-api-batch-error-structure
- name: Commerce Payments Api Batch Read Input Item Structure
  property_count: 1
  slug: commerce-payments-api-batch-read-input-item-structure
- name: Commerce Payments Api Batch Read Request Structure
  property_count: 4
  slug: commerce-payments-api-batch-read-request-structure
- name: Commerce Payments Api Batch Read Response Structure
  property_count: 8
  slug: commerce-payments-api-batch-read-response-structure
- name: Commerce Payments Api Batch Update Input Item Structure
  property_count: 3
  slug: commerce-payments-api-batch-update-input-item-structure
- name: Commerce Payments Api Batch Update Request Structure
  property_count: 1
  slug: commerce-payments-api-batch-update-request-structure
- name: Commerce Payments Api Batch Update Response Structure
  property_count: 8
  slug: commerce-payments-api-batch-update-response-structure
- name: Commerce Payments Api Commerce Payment Collection Structure
  property_count: 2
  slug: commerce-payments-api-commerce-payment-collection-structure
- name: Commerce Payments Api Commerce Payment Input Structure
  property_count: 2
  slug: commerce-payments-api-commerce-payment-input-structure
- name: Commerce Payments Api Commerce Payment Patch Structure
  property_count: 1
  slug: commerce-payments-api-commerce-payment-patch-structure
- name: Commerce Payments Api Commerce Payment Structure
  property_count: 8
  slug: commerce-payments-api-commerce-payment-structure
- name: Commerce Payments Api Filter Group Structure
  property_count: 1
  slug: commerce-payments-api-filter-group-structure
- name: Commerce Payments Api Filter Structure
  property_count: 5
  slug: commerce-payments-api-filter-structure
- name: Commerce Payments Api Paging Structure
  property_count: 2
  slug: commerce-payments-api-paging-structure
- name: Commerce Payments Api Property History Structure
  property_count: 6
  slug: commerce-payments-api-property-history-structure
- name: Commerce Payments Api Search Request Structure
  property_count: 6
  slug: commerce-payments-api-search-request-structure
- name: Commerce Payments Api Search Response Structure
  property_count: 3
  slug: commerce-payments-api-search-response-structure
- name: Commerce Payments Api Sort Option Structure
  property_count: 2
  slug: commerce-payments-api-sort-option-structure
- name: Commerce Subscriptions Api Association Structure
  property_count: 2
  slug: commerce-subscriptions-api-association-structure
- name: Commerce Subscriptions Api Batch Create Input Structure
  property_count: 1
  slug: commerce-subscriptions-api-batch-create-input-structure
- name: Commerce Subscriptions Api Batch Read Input Structure
  property_count: 2
  slug: commerce-subscriptions-api-batch-read-input-structure
- name: Commerce Subscriptions Api Batch Response Subscription Structure
  property_count: 3
  slug: commerce-subscriptions-api-batch-response-subscription-structure
- name: Commerce Subscriptions Api Batch Update Input Structure
  property_count: 1
  slug: commerce-subscriptions-api-batch-update-input-structure
- name: Commerce Subscriptions Api Collection Response Association Structure
  property_count: 2
  slug: commerce-subscriptions-api-collection-response-association-structure
- name: Commerce Subscriptions Api Collection Response Subscription Structure
  property_count: 2
  slug: commerce-subscriptions-api-collection-response-subscription-structure
- name: Commerce Subscriptions Api Filter Group Structure
  property_count: 1
  slug: commerce-subscriptions-api-filter-group-structure
- name: Commerce Subscriptions Api Filter Structure
  property_count: 3
  slug: commerce-subscriptions-api-filter-structure
- name: Commerce Subscriptions Api Paging Structure
  property_count: 1
  slug: commerce-subscriptions-api-paging-structure
- name: Commerce Subscriptions Api Search Request Structure
  property_count: 6
  slug: commerce-subscriptions-api-search-request-structure
- name: Commerce Subscriptions Api Simple Public Object Input Structure
  property_count: 1
  slug: commerce-subscriptions-api-simple-public-object-input-structure
- name: Commerce Subscriptions Api Subscription Structure
  property_count: 6
  slug: commerce-subscriptions-api-subscription-structure
- name: Conversations Api Actor Collection Structure
  property_count: 2
  slug: conversations-api-actor-collection-structure
- name: Conversations Api Actor Structure
  property_count: 5
  slug: conversations-api-actor-structure
- name: Conversations Api Attachment Structure
  property_count: 5
  slug: conversations-api-attachment-structure
- name: Conversations Api Channel Collection Structure
  property_count: 2
  slug: conversations-api-channel-collection-structure
- name: Conversations Api Channel Structure
  property_count: 5
  slug: conversations-api-channel-structure
- name: Conversations Api Inbox Collection Structure
  property_count: 3
  slug: conversations-api-inbox-collection-structure
- name: Conversations Api Inbox Structure
  property_count: 6
  slug: conversations-api-inbox-structure
- name: Conversations Api Message Collection Structure
  property_count: 2
  slug: conversations-api-message-collection-structure
- name: Conversations Api Message Recipient Structure
  property_count: 1
  slug: conversations-api-message-recipient-structure
- name: Conversations Api Message Status Structure
  property_count: 1
  slug: conversations-api-message-status-structure
- name: Conversations Api Message Structure
  property_count: 13
  slug: conversations-api-message-structure
- name: Conversations Api Paging Next Structure
  property_count: 2
  slug: conversations-api-paging-next-structure
- name: Conversations Api Paging Structure
  property_count: 1
  slug: conversations-api-paging-structure
- name: Conversations Api Send Message Request Structure
  property_count: 7
  slug: conversations-api-send-message-request-structure
- name: Conversations Api Thread Collection Structure
  property_count: 2
  slug: conversations-api-thread-collection-structure
- name: Conversations Api Thread Structure
  property_count: 14
  slug: conversations-api-thread-structure
- name: Conversations Api Update Thread Request Structure
  property_count: 2
  slug: conversations-api-update-thread-request-structure
- name: Crm Associations Api Association Definition Collection Structure
  property_count: 2
  slug: crm-associations-api-association-definition-collection-structure
- name: Crm Associations Api Association Definition Structure
  property_count: 7
  slug: crm-associations-api-association-definition-structure
- name: Crm Associations Api Association Label Collection Structure
  property_count: 2
  slug: crm-associations-api-association-label-collection-structure
- name: Crm Associations Api Association Label Structure
  property_count: 3
  slug: crm-associations-api-association-label-structure
- name: Crm Associations Api Association Result Structure
  property_count: 3
  slug: crm-associations-api-association-result-structure
- name: Crm Associations Api Association Structure
  property_count: 2
  slug: crm-associations-api-association-structure
- name: Crm Associations Api Association Type Input Structure
  property_count: 2
  slug: crm-associations-api-association-type-input-structure
- name: Crm Associations Api Association Type Structure
  property_count: 3
  slug: crm-associations-api-association-type-structure
- name: Crm Associations Api Batch Association Archive Input Structure
  property_count: 1
  slug: crm-associations-api-batch-association-archive-input-structure
- name: Crm Associations Api Batch Association Archive Item Structure
  property_count: 3
  slug: crm-associations-api-batch-association-archive-item-structure
- name: Crm Associations Api Batch Association Create Input Structure
  property_count: 1
  slug: crm-associations-api-batch-association-create-input-structure
- name: Crm Associations Api Batch Association Create Item Structure
  property_count: 3
  slug: crm-associations-api-batch-association-create-item-structure
- name: Crm Associations Api Batch Association Read Input Structure
  property_count: 1
  slug: crm-associations-api-batch-association-read-input-structure
- name: Crm Associations Api Batch Association Response Structure
  property_count: 8
  slug: crm-associations-api-batch-association-response-structure
- name: Crm Associations Api Create Association Input Structure
  property_count: 2
  slug: crm-associations-api-create-association-input-structure
- name: Crm Associations Api Create Label Input Structure
  property_count: 3
  slug: crm-associations-api-create-label-input-structure
- name: Crm Associations Api Object Reference Structure
  property_count: 1
  slug: crm-associations-api-object-reference-structure
- name: Crm Associations Api Paging Next Structure
  property_count: 2
  slug: crm-associations-api-paging-next-structure
- name: Crm Associations Api Paging Structure
  property_count: 1
  slug: crm-associations-api-paging-structure
- name: Crm Companies Api Association Structure
  property_count: 2
  slug: crm-companies-api-association-structure
- name: Crm Companies Api Batch Archive Input Structure
  property_count: 1
  slug: crm-companies-api-batch-archive-input-structure
- name: Crm Companies Api Batch Create Input Structure
  property_count: 1
  slug: crm-companies-api-batch-create-input-structure
- name: Crm Companies Api Batch Read Input Structure
  property_count: 2
  slug: crm-companies-api-batch-read-input-structure
- name: Crm Companies Api Batch Response Company Structure
  property_count: 3
  slug: crm-companies-api-batch-response-company-structure
- name: Crm Companies Api Batch Update Input Structure
  property_count: 1
  slug: crm-companies-api-batch-update-input-structure
- name: Crm Companies Api Collection Response Association Structure
  property_count: 2
  slug: crm-companies-api-collection-response-association-structure
- name: Crm Companies Api Collection Response Company Structure
  property_count: 2
  slug: crm-companies-api-collection-response-company-structure
- name: Crm Companies Api Company Structure
  property_count: 6
  slug: crm-companies-api-company-structure
- name: Crm Companies Api Filter Group Structure
  property_count: 1
  slug: crm-companies-api-filter-group-structure
- name: Crm Companies Api Filter Structure
  property_count: 3
  slug: crm-companies-api-filter-structure
- name: Crm Companies Api Paging Structure
  property_count: 1
  slug: crm-companies-api-paging-structure
- name: Crm Companies Api Search Request Structure
  property_count: 6
  slug: crm-companies-api-search-request-structure
- name: Crm Companies Api Simple Public Object Input Structure
  property_count: 1
  slug: crm-companies-api-simple-public-object-input-structure
- name: Crm Contacts Api Association Structure
  property_count: 2
  slug: crm-contacts-api-association-structure
- name: Crm Contacts Api Batch Archive Input Structure
  property_count: 1
  slug: crm-contacts-api-batch-archive-input-structure
- name: Crm Contacts Api Batch Create Input Structure
  property_count: 1
  slug: crm-contacts-api-batch-create-input-structure
- name: Crm Contacts Api Batch Read Input Structure
  property_count: 2
  slug: crm-contacts-api-batch-read-input-structure
- name: Crm Contacts Api Batch Response Contact Structure
  property_count: 3
  slug: crm-contacts-api-batch-response-contact-structure
- name: Crm Contacts Api Batch Update Input Structure
  property_count: 1
  slug: crm-contacts-api-batch-update-input-structure
- name: Crm Contacts Api Collection Response Association Structure
  property_count: 2
  slug: crm-contacts-api-collection-response-association-structure
- name: Crm Contacts Api Collection Response Contact Structure
  property_count: 2
  slug: crm-contacts-api-collection-response-contact-structure
- name: Crm Contacts Api Contact Structure
  property_count: 6
  slug: crm-contacts-api-contact-structure
- name: Crm Contacts Api Filter Group Structure
  property_count: 1
  slug: crm-contacts-api-filter-group-structure
- name: Crm Contacts Api Filter Structure
  property_count: 3
  slug: crm-contacts-api-filter-structure
- name: Crm Contacts Api Paging Structure
  property_count: 1
  slug: crm-contacts-api-paging-structure
- name: Crm Contacts Api Search Request Structure
  property_count: 6
  slug: crm-contacts-api-search-request-structure
- name: Crm Contacts Api Simple Public Object Input Structure
  property_count: 1
  slug: crm-contacts-api-simple-public-object-input-structure
- name: Crm Deals Api Association Structure
  property_count: 2
  slug: crm-deals-api-association-structure
- name: Crm Deals Api Batch Archive Input Structure
  property_count: 1
  slug: crm-deals-api-batch-archive-input-structure
- name: Crm Deals Api Batch Create Input Structure
  property_count: 1
  slug: crm-deals-api-batch-create-input-structure
- name: Crm Deals Api Batch Read Input Structure
  property_count: 2
  slug: crm-deals-api-batch-read-input-structure
- name: Crm Deals Api Batch Response Deal Structure
  property_count: 3
  slug: crm-deals-api-batch-response-deal-structure
- name: Crm Deals Api Batch Update Input Structure
  property_count: 1
  slug: crm-deals-api-batch-update-input-structure
- name: Crm Deals Api Collection Response Association Structure
  property_count: 2
  slug: crm-deals-api-collection-response-association-structure
- name: Crm Deals Api Collection Response Deal Structure
  property_count: 2
  slug: crm-deals-api-collection-response-deal-structure
- name: Crm Deals Api Deal Structure
  property_count: 6
  slug: crm-deals-api-deal-structure
- name: Crm Deals Api Filter Group Structure
  property_count: 1
  slug: crm-deals-api-filter-group-structure
- name: Crm Deals Api Filter Structure
  property_count: 3
  slug: crm-deals-api-filter-structure
- name: Crm Deals Api Paging Structure
  property_count: 1
  slug: crm-deals-api-paging-structure
- name: Crm Deals Api Search Request Structure
  property_count: 6
  slug: crm-deals-api-search-request-structure
- name: Crm Deals Api Simple Public Object Input Structure
  property_count: 1
  slug: crm-deals-api-simple-public-object-input-structure
- name: Crm Feature Flags Api Batch Delete Input Item Structure
  property_count: 1
  slug: crm-feature-flags-api-batch-delete-input-item-structure
- name: Crm Feature Flags Api Batch Delete Input Structure
  property_count: 1
  slug: crm-feature-flags-api-batch-delete-input-structure
- name: Crm Feature Flags Api Batch Error Structure
  property_count: 4
  slug: crm-feature-flags-api-batch-error-structure
- name: Crm Feature Flags Api Batch Portal Flag State Input Item Structure
  property_count: 2
  slug: crm-feature-flags-api-batch-portal-flag-state-input-item-structure
- name: Crm Feature Flags Api Batch Portal Flag State Input Structure
  property_count: 1
  slug: crm-feature-flags-api-batch-portal-flag-state-input-structure
- name: Crm Feature Flags Api Batch Portal Flag State Response Structure
  property_count: 4
  slug: crm-feature-flags-api-batch-portal-flag-state-response-structure
- name: Crm Feature Flags Api Batch Portal Flag State Response With Errors Structure
  property_count: 5
  slug: crm-feature-flags-api-batch-portal-flag-state-response-with-errors-structure
- name: Crm Feature Flags Api Feature Flag Input Structure
  property_count: 1
  slug: crm-feature-flags-api-feature-flag-input-structure
- name: Crm Feature Flags Api Feature Flag Structure
  property_count: 4
  slug: crm-feature-flags-api-feature-flag-structure
- name: Crm Feature Flags Api Flag State Structure
  property_count: 0
  slug: crm-feature-flags-api-flag-state-structure
- name: Crm Feature Flags Api Paging Next Structure
  property_count: 2
  slug: crm-feature-flags-api-paging-next-structure
- name: Crm Feature Flags Api Paging Structure
  property_count: 1
  slug: crm-feature-flags-api-paging-structure
- name: Crm Feature Flags Api Portal Flag State Collection Structure
  property_count: 2
  slug: crm-feature-flags-api-portal-flag-state-collection-structure
- name: Crm Feature Flags Api Portal Flag State Input Structure
  property_count: 1
  slug: crm-feature-flags-api-portal-flag-state-input-structure
- name: Crm Feature Flags Api Portal Flag State Structure
  property_count: 4
  slug: crm-feature-flags-api-portal-flag-state-structure
- name: Crm Lists Api Collection Response List Structure
  property_count: 2
  slug: crm-lists-api-collection-response-list-structure
- name: Crm Lists Api Collection Response Membership Structure
  property_count: 2
  slug: crm-lists-api-collection-response-membership-structure
- name: Crm Lists Api List Create Request Structure
  property_count: 4
  slug: crm-lists-api-list-create-request-structure
- name: Crm Lists Api List Structure
  property_count: 9
  slug: crm-lists-api-list-structure
- name: Crm Lists Api Membership Change Request Structure
  property_count: 2
  slug: crm-lists-api-membership-change-request-structure
- name: Crm Lists Api Membership Change Response Structure
  property_count: 4
  slug: crm-lists-api-membership-change-response-structure
- name: Crm Lists Api Membership Structure
  property_count: 2
  slug: crm-lists-api-membership-structure
- name: Crm Lists Api Paging Structure
  property_count: 1
  slug: crm-lists-api-paging-structure
- name: Crm Search Api Crmobject Structure
  property_count: 5
  slug: crm-search-api-crmobject-structure
- name: Crm Search Api Filter Group Structure
  property_count: 1
  slug: crm-search-api-filter-group-structure
- name: Crm Search Api Filter Structure
  property_count: 5
  slug: crm-search-api-filter-structure
- name: Crm Search Api Paging Structure
  property_count: 1
  slug: crm-search-api-paging-structure
- name: Crm Search Api Search Request Structure
  property_count: 6
  slug: crm-search-api-search-request-structure
- name: Crm Search Api Search Response Structure
  property_count: 3
  slug: crm-search-api-search-response-structure
- name: Crm Search Api Sort Structure
  property_count: 2
  slug: crm-search-api-sort-structure
- name: Crm Tickets Api Association Structure
  property_count: 2
  slug: crm-tickets-api-association-structure
- name: Crm Tickets Api Batch Archive Input Structure
  property_count: 1
  slug: crm-tickets-api-batch-archive-input-structure
- name: Crm Tickets Api Batch Create Input Structure
  property_count: 1
  slug: crm-tickets-api-batch-create-input-structure
- name: Crm Tickets Api Batch Read Input Structure
  property_count: 2
  slug: crm-tickets-api-batch-read-input-structure
- name: Crm Tickets Api Batch Response Ticket Structure
  property_count: 3
  slug: crm-tickets-api-batch-response-ticket-structure
- name: Crm Tickets Api Batch Update Input Structure
  property_count: 1
  slug: crm-tickets-api-batch-update-input-structure
- name: Crm Tickets Api Collection Response Association Structure
  property_count: 2
  slug: crm-tickets-api-collection-response-association-structure
- name: Crm Tickets Api Collection Response Ticket Structure
  property_count: 2
  slug: crm-tickets-api-collection-response-ticket-structure
- name: Crm Tickets Api Filter Group Structure
  property_count: 1
  slug: crm-tickets-api-filter-group-structure
- name: Crm Tickets Api Filter Structure
  property_count: 3
  slug: crm-tickets-api-filter-structure
- name: Crm Tickets Api Paging Structure
  property_count: 1
  slug: crm-tickets-api-paging-structure
- name: Crm Tickets Api Search Request Structure
  property_count: 6
  slug: crm-tickets-api-search-request-structure
- name: Crm Tickets Api Simple Public Object Input Structure
  property_count: 1
  slug: crm-tickets-api-simple-public-object-input-structure
- name: Crm Tickets Api Ticket Structure
  property_count: 6
  slug: crm-tickets-api-ticket-structure
- name: Custom Workflow Actions Api Action Definition Collection Structure
  property_count: 2
  slug: custom-workflow-actions-api-action-definition-collection-structure
- name: Custom Workflow Actions Api Action Definition Input Structure
  property_count: 7
  slug: custom-workflow-actions-api-action-definition-input-structure
- name: Custom Workflow Actions Api Action Definition Patch Structure
  property_count: 7
  slug: custom-workflow-actions-api-action-definition-patch-structure
- name: Custom Workflow Actions Api Action Definition Revision Collection Structure
  property_count: 2
  slug: custom-workflow-actions-api-action-definition-revision-collection-structure
- name: Custom Workflow Actions Api Action Definition Revision Structure
  property_count: 3
  slug: custom-workflow-actions-api-action-definition-revision-structure
- name: Custom Workflow Actions Api Action Definition Structure
  property_count: 10
  slug: custom-workflow-actions-api-action-definition-structure
- name: Custom Workflow Actions Api Action Function Collection Structure
  property_count: 1
  slug: custom-workflow-actions-api-action-function-collection-structure
- name: Custom Workflow Actions Api Action Function Input Structure
  property_count: 1
  slug: custom-workflow-actions-api-action-function-input-structure
- name: Custom Workflow Actions Api Action Function Reference Structure
  property_count: 2
  slug: custom-workflow-actions-api-action-function-reference-structure
- name: Custom Workflow Actions Api Action Function Structure
  property_count: 3
  slug: custom-workflow-actions-api-action-function-structure
- name: Custom Workflow Actions Api Action Labels Structure
  property_count: 4
  slug: custom-workflow-actions-api-action-labels-structure
- name: Custom Workflow Actions Api Batch Callback Completion Request Structure
  property_count: 1
  slug: custom-workflow-actions-api-batch-callback-completion-request-structure
- name: Custom Workflow Actions Api Batch Callback Error Structure
  property_count: 3
  slug: custom-workflow-actions-api-batch-callback-error-structure
- name: Custom Workflow Actions Api Batch Callback Input Structure
  property_count: 2
  slug: custom-workflow-actions-api-batch-callback-input-structure
- name: Custom Workflow Actions Api Batch Callback Response Structure
  property_count: 2
  slug: custom-workflow-actions-api-batch-callback-response-structure
- name: Custom Workflow Actions Api Callback Completion Request Structure
  property_count: 1
  slug: custom-workflow-actions-api-callback-completion-request-structure
- name: Custom Workflow Actions Api Field Option Structure
  property_count: 3
  slug: custom-workflow-actions-api-field-option-structure
- name: Custom Workflow Actions Api Field Type Definition Structure
  property_count: 6
  slug: custom-workflow-actions-api-field-type-definition-structure
- name: Custom Workflow Actions Api Input Field Structure
  property_count: 3
  slug: custom-workflow-actions-api-input-field-structure
- name: Custom Workflow Actions Api Object Request Options Structure
  property_count: 1
  slug: custom-workflow-actions-api-object-request-options-structure
- name: Custom Workflow Actions Api Output Field Structure
  property_count: 1
  slug: custom-workflow-actions-api-output-field-structure
- name: Custom Workflow Actions Api Paging Structure
  property_count: 1
  slug: custom-workflow-actions-api-paging-structure
- name: Domains Api Domain Collection Response Structure
  property_count: 3
  slug: domains-api-domain-collection-response-structure
- name: Domains Api Domain Structure
  property_count: 21
  slug: domains-api-domain-structure
- name: Domains Api Forward Paging Structure
  property_count: 1
  slug: domains-api-forward-paging-structure
- name: Domains Api Next Page Structure
  property_count: 2
  slug: domains-api-next-page-structure
- name: Engagement Calls Api Association Input Structure
  property_count: 2
  slug: engagement-calls-api-association-input-structure
- name: Engagement Calls Api Association Type Structure
  property_count: 2
  slug: engagement-calls-api-association-type-structure
- name: Engagement Calls Api Batch Archive Calls Request Structure
  property_count: 1
  slug: engagement-calls-api-batch-archive-calls-request-structure
- name: Engagement Calls Api Batch Calls Response Structure
  property_count: 7
  slug: engagement-calls-api-batch-calls-response-structure
- name: Engagement Calls Api Batch Create Calls Request Structure
  property_count: 1
  slug: engagement-calls-api-batch-create-calls-request-structure
- name: Engagement Calls Api Batch Error Structure
  property_count: 5
  slug: engagement-calls-api-batch-error-structure
- name: Engagement Calls Api Batch Read Calls Request Structure
  property_count: 4
  slug: engagement-calls-api-batch-read-calls-request-structure
- name: Engagement Calls Api Batch Read Input Structure
  property_count: 1
  slug: engagement-calls-api-batch-read-input-structure
- name: Engagement Calls Api Batch Update Calls Request Structure
  property_count: 1
  slug: engagement-calls-api-batch-update-calls-request-structure
- name: Engagement Calls Api Batch Update Input Structure
  property_count: 2
  slug: engagement-calls-api-batch-update-input-structure
- name: Engagement Calls Api Call Collection Response Structure
  property_count: 2
  slug: engagement-calls-api-call-collection-response-structure
- name: Engagement Calls Api Call Create Request Structure
  property_count: 2
  slug: engagement-calls-api-call-create-request-structure
- name: Engagement Calls Api Call Search Request Structure
  property_count: 6
  slug: engagement-calls-api-call-search-request-structure
- name: Engagement Calls Api Call Search Response Structure
  property_count: 3
  slug: engagement-calls-api-call-search-response-structure
- name: Engagement Calls Api Call Structure
  property_count: 7
  slug: engagement-calls-api-call-structure
- name: Engagement Calls Api Call Update Request Structure
  property_count: 1
  slug: engagement-calls-api-call-update-request-structure
- name: Engagement Calls Api Filter Group Structure
  property_count: 1
  slug: engagement-calls-api-filter-group-structure
- name: Engagement Calls Api Filter Structure
  property_count: 5
  slug: engagement-calls-api-filter-structure
- name: Engagement Calls Api Gdpr Delete Request Structure
  property_count: 2
  slug: engagement-calls-api-gdpr-delete-request-structure
- name: Engagement Calls Api Next Page Structure
  property_count: 2
  slug: engagement-calls-api-next-page-structure
- name: Engagement Calls Api Paging Structure
  property_count: 1
  slug: engagement-calls-api-paging-structure
- name: Engagement Calls Api Property History Structure
  property_count: 6
  slug: engagement-calls-api-property-history-structure
- name: Engagement Calls Api Sort Option Structure
  property_count: 2
  slug: engagement-calls-api-sort-option-structure
- name: Engagement Emails Api Association Structure
  property_count: 2
  slug: engagement-emails-api-association-structure
- name: Engagement Emails Api Batch Create Input Structure
  property_count: 1
  slug: engagement-emails-api-batch-create-input-structure
- name: Engagement Emails Api Batch Read Input Structure
  property_count: 2
  slug: engagement-emails-api-batch-read-input-structure
- name: Engagement Emails Api Batch Response Email Engagement Structure
  property_count: 3
  slug: engagement-emails-api-batch-response-email-engagement-structure
- name: Engagement Emails Api Batch Update Input Structure
  property_count: 1
  slug: engagement-emails-api-batch-update-input-structure
- name: Engagement Emails Api Collection Response Association Structure
  property_count: 2
  slug: engagement-emails-api-collection-response-association-structure
- name: Engagement Emails Api Collection Response Email Engagement Structure
  property_count: 2
  slug: engagement-emails-api-collection-response-email-engagement-structure
- name: Engagement Emails Api Email Engagement Structure
  property_count: 6
  slug: engagement-emails-api-email-engagement-structure
- name: Engagement Emails Api Filter Group Structure
  property_count: 1
  slug: engagement-emails-api-filter-group-structure
- name: Engagement Emails Api Filter Structure
  property_count: 3
  slug: engagement-emails-api-filter-structure
- name: Engagement Emails Api Paging Structure
  property_count: 1
  slug: engagement-emails-api-paging-structure
- name: Engagement Emails Api Search Request Structure
  property_count: 6
  slug: engagement-emails-api-search-request-structure
- name: Engagement Emails Api Simple Public Object Input Structure
  property_count: 1
  slug: engagement-emails-api-simple-public-object-input-structure
- name: Engagement Meetings Api Association Structure
  property_count: 2
  slug: engagement-meetings-api-association-structure
- name: Engagement Meetings Api Batch Create Input Structure
  property_count: 1
  slug: engagement-meetings-api-batch-create-input-structure
- name: Engagement Meetings Api Batch Read Input Structure
  property_count: 2
  slug: engagement-meetings-api-batch-read-input-structure
- name: Engagement Meetings Api Batch Response Meeting Structure
  property_count: 3
  slug: engagement-meetings-api-batch-response-meeting-structure
- name: Engagement Meetings Api Batch Update Input Structure
  property_count: 1
  slug: engagement-meetings-api-batch-update-input-structure
- name: Engagement Meetings Api Collection Response Association Structure
  property_count: 2
  slug: engagement-meetings-api-collection-response-association-structure
- name: Engagement Meetings Api Collection Response Meeting Structure
  property_count: 2
  slug: engagement-meetings-api-collection-response-meeting-structure
- name: Engagement Meetings Api Filter Group Structure
  property_count: 1
  slug: engagement-meetings-api-filter-group-structure
- name: Engagement Meetings Api Filter Structure
  property_count: 3
  slug: engagement-meetings-api-filter-structure
- name: Engagement Meetings Api Meeting Structure
  property_count: 6
  slug: engagement-meetings-api-meeting-structure
- name: Engagement Meetings Api Paging Structure
  property_count: 1
  slug: engagement-meetings-api-paging-structure
- name: Engagement Meetings Api Search Request Structure
  property_count: 6
  slug: engagement-meetings-api-search-request-structure
- name: Engagement Meetings Api Simple Public Object Input Structure
  property_count: 1
  slug: engagement-meetings-api-simple-public-object-input-structure
- name: Engagement Notes Association Input Structure
  property_count: 2
  slug: engagement-notes-association-input-structure
- name: Engagement Notes Association Type Structure
  property_count: 2
  slug: engagement-notes-association-type-structure
- name: Engagement Notes Batch Archive Notes Request Structure
  property_count: 1
  slug: engagement-notes-batch-archive-notes-request-structure
- name: Engagement Notes Batch Create Notes Request Structure
  property_count: 1
  slug: engagement-notes-batch-create-notes-request-structure
- name: Engagement Notes Batch Error Structure
  property_count: 5
  slug: engagement-notes-batch-error-structure
- name: Engagement Notes Batch Notes Response Structure
  property_count: 7
  slug: engagement-notes-batch-notes-response-structure
- name: Engagement Notes Batch Read Input Structure
  property_count: 1
  slug: engagement-notes-batch-read-input-structure
- name: Engagement Notes Batch Read Notes Request Structure
  property_count: 4
  slug: engagement-notes-batch-read-notes-request-structure
- name: Engagement Notes Batch Update Input Structure
  property_count: 2
  slug: engagement-notes-batch-update-input-structure
- name: Engagement Notes Batch Update Notes Request Structure
  property_count: 1
  slug: engagement-notes-batch-update-notes-request-structure
- name: Engagement Notes Filter Group Structure
  property_count: 1
  slug: engagement-notes-filter-group-structure
- name: Engagement Notes Filter Structure
  property_count: 5
  slug: engagement-notes-filter-structure
- name: Engagement Notes Gdpr Delete Request Structure
  property_count: 2
  slug: engagement-notes-gdpr-delete-request-structure
- name: Engagement Notes Next Page Structure
  property_count: 2
  slug: engagement-notes-next-page-structure
- name: Engagement Notes Note Collection Response Structure
  property_count: 2
  slug: engagement-notes-note-collection-response-structure
- name: Engagement Notes Note Create Request Structure
  property_count: 2
  slug: engagement-notes-note-create-request-structure
- name: Engagement Notes Note Search Request Structure
  property_count: 6
  slug: engagement-notes-note-search-request-structure
- name: Engagement Notes Note Search Response Structure
  property_count: 3
  slug: engagement-notes-note-search-response-structure
- name: Engagement Notes Note Structure
  property_count: 7
  slug: engagement-notes-note-structure
- name: Engagement Notes Note Update Request Structure
  property_count: 1
  slug: engagement-notes-note-update-request-structure
- name: Engagement Notes Paging Structure
  property_count: 1
  slug: engagement-notes-paging-structure
- name: Engagement Notes Property History Structure
  property_count: 6
  slug: engagement-notes-property-history-structure
- name: Engagement Notes Sort Option Structure
  property_count: 2
  slug: engagement-notes-sort-option-structure
- name: Engagement Tasks Api Association Structure
  property_count: 2
  slug: engagement-tasks-api-association-structure
- name: Engagement Tasks Api Batch Create Input Structure
  property_count: 1
  slug: engagement-tasks-api-batch-create-input-structure
- name: Engagement Tasks Api Batch Read Input Structure
  property_count: 2
  slug: engagement-tasks-api-batch-read-input-structure
- name: Engagement Tasks Api Batch Response Task Structure
  property_count: 3
  slug: engagement-tasks-api-batch-response-task-structure
- name: Engagement Tasks Api Batch Update Input Structure
  property_count: 1
  slug: engagement-tasks-api-batch-update-input-structure
- name: Engagement Tasks Api Collection Response Association Structure
  property_count: 2
  slug: engagement-tasks-api-collection-response-association-structure
- name: Engagement Tasks Api Collection Response Task Structure
  property_count: 2
  slug: engagement-tasks-api-collection-response-task-structure
- name: Engagement Tasks Api Filter Group Structure
  property_count: 1
  slug: engagement-tasks-api-filter-group-structure
- name: Engagement Tasks Api Filter Structure
  property_count: 3
  slug: engagement-tasks-api-filter-structure
- name: Engagement Tasks Api Paging Structure
  property_count: 1
  slug: engagement-tasks-api-paging-structure
- name: Engagement Tasks Api Search Request Structure
  property_count: 6
  slug: engagement-tasks-api-search-request-structure
- name: Engagement Tasks Api Simple Public Object Input Structure
  property_count: 1
  slug: engagement-tasks-api-simple-public-object-input-structure
- name: Engagement Tasks Api Task Structure
  property_count: 6
  slug: engagement-tasks-api-task-structure
- name: Hubspot Analytics Events Error Detail Structure
  property_count: 5
  slug: hubspot-analytics-events-error-detail-structure
- name: Hubspot Analytics Events Error Structure
  property_count: 7
  slug: hubspot-analytics-events-error-structure
- name: Hubspot Analytics Events Event Instance Collection Structure
  property_count: 2
  slug: hubspot-analytics-events-event-instance-collection-structure
- name: Hubspot Analytics Events Event Instance Structure
  property_count: 6
  slug: hubspot-analytics-events-event-instance-structure
- name: Hubspot Analytics Events Event Type Collection Structure
  property_count: 1
  slug: hubspot-analytics-events-event-type-collection-structure
- name: Hubspot Analytics Events Paging Next Structure
  property_count: 2
  slug: hubspot-analytics-events-paging-next-structure
- name: Hubspot Analytics Events Paging Previous Structure
  property_count: 2
  slug: hubspot-analytics-events-paging-previous-structure
- name: Hubspot Analytics Events Paging Structure
  property_count: 2
  slug: hubspot-analytics-events-paging-structure
- name: Hubspot Authors Attach To Language Group Request Structure
  property_count: 4
  slug: hubspot-authors-attach-to-language-group-request-structure
- name: Hubspot Authors Batch Archive Input Structure
  property_count: 1
  slug: hubspot-authors-batch-archive-input-structure
- name: Hubspot Authors Batch Create Input Structure
  property_count: 1
  slug: hubspot-authors-batch-create-input-structure
- name: Hubspot Authors Batch Input Item Structure
  property_count: 2
  slug: hubspot-authors-batch-input-item-structure
- name: Hubspot Authors Batch Input Structure
  property_count: 1
  slug: hubspot-authors-batch-input-structure
- name: Hubspot Authors Batch Read Input Structure
  property_count: 1
  slug: hubspot-authors-batch-read-input-structure
- name: Hubspot Authors Batch Response Structure
  property_count: 6
  slug: hubspot-authors-batch-response-structure
- name: Hubspot Authors Batch Response With Errors Structure
  property_count: 0
  slug: hubspot-authors-batch-response-with-errors-structure
- name: Hubspot Authors Blog Author Collection Structure
  property_count: 3
  slug: hubspot-authors-blog-author-collection-structure
- name: Hubspot Authors Blog Author Input Structure
  property_count: 9
  slug: hubspot-authors-blog-author-input-structure
- name: Hubspot Authors Blog Author Structure
  property_count: 15
  slug: hubspot-authors-blog-author-structure
- name: Hubspot Authors Create Language Variation Request Structure
  property_count: 2
  slug: hubspot-authors-create-language-variation-request-structure
- name: Hubspot Authors Detach From Language Group Request Structure
  property_count: 1
  slug: hubspot-authors-detach-from-language-group-request-structure
- name: Hubspot Authors Error Detail Structure
  property_count: 5
  slug: hubspot-authors-error-detail-structure
- name: Hubspot Authors Error Structure
  property_count: 7
  slug: hubspot-authors-error-structure
- name: Hubspot Authors Paging Next Structure
  property_count: 2
  slug: hubspot-authors-paging-next-structure
- name: Hubspot Authors Paging Structure
  property_count: 1
  slug: hubspot-authors-paging-structure
- name: Hubspot Authors Set Language Primary Request Structure
  property_count: 1
  slug: hubspot-authors-set-language-primary-request-structure
- name: Hubspot Authors Standard Error Structure
  property_count: 7
  slug: hubspot-authors-standard-error-structure
- name: Hubspot Blog Posts Attach To Language Group Request Structure
  property_count: 4
  slug: hubspot-blog-posts-attach-to-language-group-request-structure
- name: Hubspot Blog Posts Batch Input Item Structure
  property_count: 1
  slug: hubspot-blog-posts-batch-input-item-structure
- name: Hubspot Blog Posts Batch Input Structure
  property_count: 1
  slug: hubspot-blog-posts-batch-input-structure
- name: Hubspot Blog Posts Batch Response Structure
  property_count: 6
  slug: hubspot-blog-posts-batch-response-structure
- name: Hubspot Blog Posts Batch Response With Errors Structure
  property_count: 0
  slug: hubspot-blog-posts-batch-response-with-errors-structure
- name: Hubspot Blog Posts Blog Post Collection Structure
  property_count: 3
  slug: hubspot-blog-posts-blog-post-collection-structure
- name: Hubspot Blog Posts Blog Post Input Structure
  property_count: 15
  slug: hubspot-blog-posts-blog-post-input-structure
- name: Hubspot Blog Posts Blog Post Structure
  property_count: 32
  slug: hubspot-blog-posts-blog-post-structure
- name: Hubspot Blog Posts Clone Request Structure
  property_count: 1
  slug: hubspot-blog-posts-clone-request-structure
- name: Hubspot Blog Posts Create Language Variation Request Structure
  property_count: 2
  slug: hubspot-blog-posts-create-language-variation-request-structure
- name: Hubspot Blog Posts Detach From Language Group Request Structure
  property_count: 1
  slug: hubspot-blog-posts-detach-from-language-group-request-structure
- name: Hubspot Blog Posts Error Detail Structure
  property_count: 5
  slug: hubspot-blog-posts-error-detail-structure
- name: Hubspot Blog Posts Error Structure
  property_count: 7
  slug: hubspot-blog-posts-error-structure
- name: Hubspot Blog Posts Paging Next Structure
  property_count: 2
  slug: hubspot-blog-posts-paging-next-structure
- name: Hubspot Blog Posts Paging Previous Structure
  property_count: 2
  slug: hubspot-blog-posts-paging-previous-structure
- name: Hubspot Blog Posts Paging Structure
  property_count: 2
  slug: hubspot-blog-posts-paging-structure
- name: Hubspot Blog Posts Push Live Request Structure
  property_count: 1
  slug: hubspot-blog-posts-push-live-request-structure
- name: Hubspot Blog Posts Reset Draft Request Structure
  property_count: 1
  slug: hubspot-blog-posts-reset-draft-request-structure
- name: Hubspot Blog Posts Restore Previous Version Request Structure
  property_count: 2
  slug: hubspot-blog-posts-restore-previous-version-request-structure
- name: Hubspot Blog Posts Schedule Request Structure
  property_count: 2
  slug: hubspot-blog-posts-schedule-request-structure
- name: Hubspot Blog Posts Set Language Primary Request Structure
  property_count: 1
  slug: hubspot-blog-posts-set-language-primary-request-structure
- name: Hubspot Blog Posts Standard Error Structure
  property_count: 7
  slug: hubspot-blog-posts-standard-error-structure
- name: Hubspot Blog Posts Version History Structure
  property_count: 4
  slug: hubspot-blog-posts-version-history-structure
- name: Hubspot Cms Hubdb Collection Response Hub Db Row Structure
  property_count: 2
  slug: hubspot-cms-hubdb-collection-response-hub-db-row-structure
- name: Hubspot Cms Hubdb Collection Response Hub Db Table Structure
  property_count: 2
  slug: hubspot-cms-hubdb-collection-response-hub-db-table-structure
- name: Hubspot Cms Hubdb Error Structure
  property_count: 4
  slug: hubspot-cms-hubdb-error-structure
- name: Hubspot Cms Hubdb Hub Db Column Structure
  property_count: 5
  slug: hubspot-cms-hubdb-hub-db-column-structure
- name: Hubspot Cms Hubdb Hub Db Row Create Request Structure
  property_count: 1
  slug: hubspot-cms-hubdb-hub-db-row-create-request-structure
- name: Hubspot Cms Hubdb Hub Db Row Structure
  property_count: 4
  slug: hubspot-cms-hubdb-hub-db-row-structure
- name: Hubspot Cms Hubdb Hub Db Table Create Request Structure
  property_count: 3
  slug: hubspot-cms-hubdb-hub-db-table-create-request-structure
- name: Hubspot Cms Hubdb Hub Db Table Structure
  property_count: 9
  slug: hubspot-cms-hubdb-hub-db-table-structure
- name: Hubspot Cms Hubdb Paging Structure
  property_count: 1
  slug: hubspot-cms-hubdb-paging-structure
- name: Hubspot Cms Pages Collection Response Page Structure
  property_count: 2
  slug: hubspot-cms-pages-collection-response-page-structure
- name: Hubspot Cms Pages Error Structure
  property_count: 4
  slug: hubspot-cms-pages-error-structure
- name: Hubspot Cms Pages Page Create Request Structure
  property_count: 8
  slug: hubspot-cms-pages-page-create-request-structure
- name: Hubspot Cms Pages Page Structure
  property_count: 16
  slug: hubspot-cms-pages-page-structure
- name: Hubspot Cms Pages Page Update Request Structure
  property_count: 5
  slug: hubspot-cms-pages-page-update-request-structure
- name: Hubspot Cms Pages Paging Structure
  property_count: 1
  slug: hubspot-cms-pages-paging-structure
- name: Hubspot Commerce Payments Association Input Structure
  property_count: 2
  slug: hubspot-commerce-payments-association-input-structure
- name: Hubspot Commerce Payments Association Result Structure
  property_count: 2
  slug: hubspot-commerce-payments-association-result-structure
- name: Hubspot Commerce Payments Association Type Structure
  property_count: 2
  slug: hubspot-commerce-payments-association-type-structure
- name: Hubspot Commerce Payments Batch Archive Request Structure
  property_count: 1
  slug: hubspot-commerce-payments-batch-archive-request-structure
- name: Hubspot Commerce Payments Batch Create Request Structure
  property_count: 1
  slug: hubspot-commerce-payments-batch-create-request-structure
- name: Hubspot Commerce Payments Batch Create Response Structure
  property_count: 8
  slug: hubspot-commerce-payments-batch-create-response-structure
- name: Hubspot Commerce Payments Batch Error Structure
  property_count: 8
  slug: hubspot-commerce-payments-batch-error-structure
- name: Hubspot Commerce Payments Batch Read Input Item Structure
  property_count: 1
  slug: hubspot-commerce-payments-batch-read-input-item-structure
- name: Hubspot Commerce Payments Batch Read Request Structure
  property_count: 4
  slug: hubspot-commerce-payments-batch-read-request-structure
- name: Hubspot Commerce Payments Batch Read Response Structure
  property_count: 8
  slug: hubspot-commerce-payments-batch-read-response-structure
- name: Hubspot Commerce Payments Batch Update Input Item Structure
  property_count: 3
  slug: hubspot-commerce-payments-batch-update-input-item-structure
- name: Hubspot Commerce Payments Batch Update Request Structure
  property_count: 1
  slug: hubspot-commerce-payments-batch-update-request-structure
- name: Hubspot Commerce Payments Batch Update Response Structure
  property_count: 8
  slug: hubspot-commerce-payments-batch-update-response-structure
- name: Hubspot Commerce Payments Commerce Payment Collection Structure
  property_count: 2
  slug: hubspot-commerce-payments-commerce-payment-collection-structure
- name: Hubspot Commerce Payments Commerce Payment Input Structure
  property_count: 2
  slug: hubspot-commerce-payments-commerce-payment-input-structure
- name: Hubspot Commerce Payments Commerce Payment Patch Structure
  property_count: 1
  slug: hubspot-commerce-payments-commerce-payment-patch-structure
- name: Hubspot Commerce Payments Commerce Payment Structure
  property_count: 8
  slug: hubspot-commerce-payments-commerce-payment-structure
- name: Hubspot Commerce Payments Error Detail Structure
  property_count: 5
  slug: hubspot-commerce-payments-error-detail-structure
- name: Hubspot Commerce Payments Error Structure
  property_count: 7
  slug: hubspot-commerce-payments-error-structure
- name: Hubspot Commerce Payments Filter Group Structure
  property_count: 1
  slug: hubspot-commerce-payments-filter-group-structure
- name: Hubspot Commerce Payments Filter Structure
  property_count: 5
  slug: hubspot-commerce-payments-filter-structure
- name: Hubspot Commerce Payments Paging Structure
  property_count: 2
  slug: hubspot-commerce-payments-paging-structure
- name: Hubspot Commerce Payments Property History Structure
  property_count: 6
  slug: hubspot-commerce-payments-property-history-structure
- name: Hubspot Commerce Payments Search Request Structure
  property_count: 6
  slug: hubspot-commerce-payments-search-request-structure
- name: Hubspot Commerce Payments Search Response Structure
  property_count: 3
  slug: hubspot-commerce-payments-search-response-structure
- name: Hubspot Commerce Payments Sort Option Structure
  property_count: 2
  slug: hubspot-commerce-payments-sort-option-structure
- name: Hubspot Commerce Subscriptions Association Structure
  property_count: 2
  slug: hubspot-commerce-subscriptions-association-structure
- name: Hubspot Commerce Subscriptions Batch Create Input Structure
  property_count: 1
  slug: hubspot-commerce-subscriptions-batch-create-input-structure
- name: Hubspot Commerce Subscriptions Batch Read Input Structure
  property_count: 2
  slug: hubspot-commerce-subscriptions-batch-read-input-structure
- name: Hubspot Commerce Subscriptions Batch Response Subscription Structure
  property_count: 3
  slug: hubspot-commerce-subscriptions-batch-response-subscription-structure
- name: Hubspot Commerce Subscriptions Batch Update Input Structure
  property_count: 1
  slug: hubspot-commerce-subscriptions-batch-update-input-structure
- name: Hubspot Commerce Subscriptions Collection Response Association Structure
  property_count: 2
  slug: hubspot-commerce-subscriptions-collection-response-association-structure
- name: Hubspot Commerce Subscriptions Collection Response Subscription Structure
  property_count: 2
  slug: hubspot-commerce-subscriptions-collection-response-subscription-structure
- name: Hubspot Commerce Subscriptions Error Structure
  property_count: 4
  slug: hubspot-commerce-subscriptions-error-structure
- name: Hubspot Commerce Subscriptions Filter Group Structure
  property_count: 1
  slug: hubspot-commerce-subscriptions-filter-group-structure
- name: Hubspot Commerce Subscriptions Filter Structure
  property_count: 3
  slug: hubspot-commerce-subscriptions-filter-structure
- name: Hubspot Commerce Subscriptions Paging Structure
  property_count: 1
  slug: hubspot-commerce-subscriptions-paging-structure
- name: Hubspot Commerce Subscriptions Search Request Structure
  property_count: 6
  slug: hubspot-commerce-subscriptions-search-request-structure
- name: Hubspot Commerce Subscriptions Simple Public Object Input Structure
  property_count: 1
  slug: hubspot-commerce-subscriptions-simple-public-object-input-structure
- name: Hubspot Commerce Subscriptions Subscription Structure
  property_count: 6
  slug: hubspot-commerce-subscriptions-subscription-structure
- name: Hubspot Conversations Actor Collection Structure
  property_count: 2
  slug: hubspot-conversations-actor-collection-structure
- name: Hubspot Conversations Actor Structure
  property_count: 5
  slug: hubspot-conversations-actor-structure
- name: Hubspot Conversations Attachment Structure
  property_count: 5
  slug: hubspot-conversations-attachment-structure
- name: Hubspot Conversations Channel Collection Structure
  property_count: 2
  slug: hubspot-conversations-channel-collection-structure
- name: Hubspot Conversations Channel Structure
  property_count: 5
  slug: hubspot-conversations-channel-structure
- name: Hubspot Conversations Error Detail Structure
  property_count: 5
  slug: hubspot-conversations-error-detail-structure
- name: Hubspot Conversations Error Structure
  property_count: 7
  slug: hubspot-conversations-error-structure
- name: Hubspot Conversations Inbox Collection Structure
  property_count: 3
  slug: hubspot-conversations-inbox-collection-structure
- name: Hubspot Conversations Inbox Structure
  property_count: 6
  slug: hubspot-conversations-inbox-structure
- name: Hubspot Conversations Message Collection Structure
  property_count: 2
  slug: hubspot-conversations-message-collection-structure
- name: Hubspot Conversations Message Recipient Structure
  property_count: 1
  slug: hubspot-conversations-message-recipient-structure
- name: Hubspot Conversations Message Status Structure
  property_count: 1
  slug: hubspot-conversations-message-status-structure
- name: Hubspot Conversations Message Structure
  property_count: 13
  slug: hubspot-conversations-message-structure
- name: Hubspot Conversations Paging Next Structure
  property_count: 2
  slug: hubspot-conversations-paging-next-structure
- name: Hubspot Conversations Paging Structure
  property_count: 1
  slug: hubspot-conversations-paging-structure
- name: Hubspot Conversations Send Message Request Structure
  property_count: 7
  slug: hubspot-conversations-send-message-request-structure
- name: Hubspot Conversations Thread Collection Structure
  property_count: 2
  slug: hubspot-conversations-thread-collection-structure
- name: Hubspot Conversations Thread Structure
  property_count: 14
  slug: hubspot-conversations-thread-structure
- name: Hubspot Conversations Update Thread Request Structure
  property_count: 2
  slug: hubspot-conversations-update-thread-request-structure
- name: Hubspot Crm Associations Association Definition Collection Structure
  property_count: 2
  slug: hubspot-crm-associations-association-definition-collection-structure
- name: Hubspot Crm Associations Association Definition Structure
  property_count: 7
  slug: hubspot-crm-associations-association-definition-structure
- name: Hubspot Crm Associations Association Label Collection Structure
  property_count: 2
  slug: hubspot-crm-associations-association-label-collection-structure
- name: Hubspot Crm Associations Association Label Structure
  property_count: 3
  slug: hubspot-crm-associations-association-label-structure
- name: Hubspot Crm Associations Association Result Structure
  property_count: 3
  slug: hubspot-crm-associations-association-result-structure
- name: Hubspot Crm Associations Association Structure
  property_count: 2
  slug: hubspot-crm-associations-association-structure
- name: Hubspot Crm Associations Association Type Input Structure
  property_count: 2
  slug: hubspot-crm-associations-association-type-input-structure
- name: Hubspot Crm Associations Association Type Structure
  property_count: 3
  slug: hubspot-crm-associations-association-type-structure
- name: Hubspot Crm Associations Batch Association Archive Input Structure
  property_count: 1
  slug: hubspot-crm-associations-batch-association-archive-input-structure
- name: Hubspot Crm Associations Batch Association Archive Item Structure
  property_count: 3
  slug: hubspot-crm-associations-batch-association-archive-item-structure
- name: Hubspot Crm Associations Batch Association Create Input Structure
  property_count: 1
  slug: hubspot-crm-associations-batch-association-create-input-structure
- name: Hubspot Crm Associations Batch Association Create Item Structure
  property_count: 3
  slug: hubspot-crm-associations-batch-association-create-item-structure
- name: Hubspot Crm Associations Batch Association Read Input Structure
  property_count: 1
  slug: hubspot-crm-associations-batch-association-read-input-structure
- name: Hubspot Crm Associations Batch Association Response Structure
  property_count: 8
  slug: hubspot-crm-associations-batch-association-response-structure
- name: Hubspot Crm Associations Create Association Input Structure
  property_count: 2
  slug: hubspot-crm-associations-create-association-input-structure
- name: Hubspot Crm Associations Create Label Input Structure
  property_count: 3
  slug: hubspot-crm-associations-create-label-input-structure
- name: Hubspot Crm Associations Error Detail Structure
  property_count: 5
  slug: hubspot-crm-associations-error-detail-structure
- name: Hubspot Crm Associations Error Structure
  property_count: 7
  slug: hubspot-crm-associations-error-structure
- name: Hubspot Crm Associations Object Reference Structure
  property_count: 1
  slug: hubspot-crm-associations-object-reference-structure
- name: Hubspot Crm Associations Paging Next Structure
  property_count: 2
  slug: hubspot-crm-associations-paging-next-structure
- name: Hubspot Crm Associations Paging Structure
  property_count: 1
  slug: hubspot-crm-associations-paging-structure
- name: Hubspot Crm Associations Standard Error Structure
  property_count: 7
  slug: hubspot-crm-associations-standard-error-structure
- name: Hubspot Crm Companies Association Structure
  property_count: 2
  slug: hubspot-crm-companies-association-structure
- name: Hubspot Crm Companies Batch Archive Input Structure
  property_count: 1
  slug: hubspot-crm-companies-batch-archive-input-structure
- name: Hubspot Crm Companies Batch Create Input Structure
  property_count: 1
  slug: hubspot-crm-companies-batch-create-input-structure
- name: Hubspot Crm Companies Batch Read Input Structure
  property_count: 2
  slug: hubspot-crm-companies-batch-read-input-structure
- name: Hubspot Crm Companies Batch Response Company Structure
  property_count: 3
  slug: hubspot-crm-companies-batch-response-company-structure
- name: Hubspot Crm Companies Batch Update Input Structure
  property_count: 1
  slug: hubspot-crm-companies-batch-update-input-structure
- name: Hubspot Crm Companies Collection Response Association Structure
  property_count: 2
  slug: hubspot-crm-companies-collection-response-association-structure
- name: Hubspot Crm Companies Collection Response Company Structure
  property_count: 2
  slug: hubspot-crm-companies-collection-response-company-structure
- name: Hubspot Crm Companies Company Structure
  property_count: 6
  slug: hubspot-crm-companies-company-structure
- name: Hubspot Crm Companies Error Structure
  property_count: 4
  slug: hubspot-crm-companies-error-structure
- name: Hubspot Crm Companies Filter Group Structure
  property_count: 1
  slug: hubspot-crm-companies-filter-group-structure
- name: Hubspot Crm Companies Filter Structure
  property_count: 3
  slug: hubspot-crm-companies-filter-structure
- name: Hubspot Crm Companies Paging Structure
  property_count: 1
  slug: hubspot-crm-companies-paging-structure
- name: Hubspot Crm Companies Search Request Structure
  property_count: 6
  slug: hubspot-crm-companies-search-request-structure
- name: Hubspot Crm Companies Simple Public Object Input Structure
  property_count: 1
  slug: hubspot-crm-companies-simple-public-object-input-structure
- name: Hubspot Crm Contacts Association Structure
  property_count: 2
  slug: hubspot-crm-contacts-association-structure
- name: Hubspot Crm Contacts Batch Archive Input Structure
  property_count: 1
  slug: hubspot-crm-contacts-batch-archive-input-structure
- name: Hubspot Crm Contacts Batch Create Input Structure
  property_count: 1
  slug: hubspot-crm-contacts-batch-create-input-structure
- name: Hubspot Crm Contacts Batch Read Input Structure
  property_count: 2
  slug: hubspot-crm-contacts-batch-read-input-structure
- name: Hubspot Crm Contacts Batch Response Contact Structure
  property_count: 3
  slug: hubspot-crm-contacts-batch-response-contact-structure
- name: Hubspot Crm Contacts Batch Update Input Structure
  property_count: 1
  slug: hubspot-crm-contacts-batch-update-input-structure
- name: Hubspot Crm Contacts Collection Response Association Structure
  property_count: 2
  slug: hubspot-crm-contacts-collection-response-association-structure
- name: Hubspot Crm Contacts Collection Response Contact Structure
  property_count: 2
  slug: hubspot-crm-contacts-collection-response-contact-structure
- name: Hubspot Crm Contacts Contact Structure
  property_count: 6
  slug: hubspot-crm-contacts-contact-structure
- name: Hubspot Crm Contacts Error Structure
  property_count: 4
  slug: hubspot-crm-contacts-error-structure
- name: Hubspot Crm Contacts Filter Group Structure
  property_count: 1
  slug: hubspot-crm-contacts-filter-group-structure
- name: Hubspot Crm Contacts Filter Structure
  property_count: 3
  slug: hubspot-crm-contacts-filter-structure
- name: Hubspot Crm Contacts Paging Structure
  property_count: 1
  slug: hubspot-crm-contacts-paging-structure
- name: Hubspot Crm Contacts Search Request Structure
  property_count: 6
  slug: hubspot-crm-contacts-search-request-structure
- name: Hubspot Crm Contacts Simple Public Object Input Structure
  property_count: 1
  slug: hubspot-crm-contacts-simple-public-object-input-structure
- name: Hubspot Crm Deals Association Structure
  property_count: 2
  slug: hubspot-crm-deals-association-structure
- name: Hubspot Crm Deals Batch Archive Input Structure
  property_count: 1
  slug: hubspot-crm-deals-batch-archive-input-structure
- name: Hubspot Crm Deals Batch Create Input Structure
  property_count: 1
  slug: hubspot-crm-deals-batch-create-input-structure
- name: Hubspot Crm Deals Batch Read Input Structure
  property_count: 2
  slug: hubspot-crm-deals-batch-read-input-structure
- name: Hubspot Crm Deals Batch Response Deal Structure
  property_count: 3
  slug: hubspot-crm-deals-batch-response-deal-structure
- name: Hubspot Crm Deals Batch Update Input Structure
  property_count: 1
  slug: hubspot-crm-deals-batch-update-input-structure
- name: Hubspot Crm Deals Collection Response Association Structure
  property_count: 2
  slug: hubspot-crm-deals-collection-response-association-structure
- name: Hubspot Crm Deals Collection Response Deal Structure
  property_count: 2
  slug: hubspot-crm-deals-collection-response-deal-structure
- name: Hubspot Crm Deals Deal Structure
  property_count: 6
  slug: hubspot-crm-deals-deal-structure
- name: Hubspot Crm Deals Error Structure
  property_count: 4
  slug: hubspot-crm-deals-error-structure
- name: Hubspot Crm Deals Filter Group Structure
  property_count: 1
  slug: hubspot-crm-deals-filter-group-structure
- name: Hubspot Crm Deals Filter Structure
  property_count: 3
  slug: hubspot-crm-deals-filter-structure
- name: Hubspot Crm Deals Paging Structure
  property_count: 1
  slug: hubspot-crm-deals-paging-structure
- name: Hubspot Crm Deals Search Request Structure
  property_count: 6
  slug: hubspot-crm-deals-search-request-structure
- name: Hubspot Crm Deals Simple Public Object Input Structure
  property_count: 1
  slug: hubspot-crm-deals-simple-public-object-input-structure
- name: Hubspot Crm Feature Flags Batch Delete Input Item Structure
  property_count: 1
  slug: hubspot-crm-feature-flags-batch-delete-input-item-structure
- name: Hubspot Crm Feature Flags Batch Delete Input Structure
  property_count: 1
  slug: hubspot-crm-feature-flags-batch-delete-input-structure
- name: Hubspot Crm Feature Flags Batch Error Structure
  property_count: 4
  slug: hubspot-crm-feature-flags-batch-error-structure
- name: Hubspot Crm Feature Flags Batch Portal Flag State Input Item Structure
  property_count: 2
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-input-item-structure
- name: Hubspot Crm Feature Flags Batch Portal Flag State Input Structure
  property_count: 1
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-input-structure
- name: Hubspot Crm Feature Flags Batch Portal Flag State Response Structure
  property_count: 4
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-response-structure
- name: Hubspot Crm Feature Flags Batch Portal Flag State Response With Errors Structure
  property_count: 5
  slug: hubspot-crm-feature-flags-batch-portal-flag-state-response-with-errors-structure
- name: Hubspot Crm Feature Flags Error Detail Structure
  property_count: 5
  slug: hubspot-crm-feature-flags-error-detail-structure
- name: Hubspot Crm Feature Flags Error Structure
  property_count: 7
  slug: hubspot-crm-feature-flags-error-structure
- name: Hubspot Crm Feature Flags Feature Flag Input Structure
  property_count: 1
  slug: hubspot-crm-feature-flags-feature-flag-input-structure
- name: Hubspot Crm Feature Flags Feature Flag Structure
  property_count: 4
  slug: hubspot-crm-feature-flags-feature-flag-structure
- name: Hubspot Crm Feature Flags Flag State Structure
  property_count: 0
  slug: hubspot-crm-feature-flags-flag-state-structure
- name: Hubspot Crm Feature Flags Paging Next Structure
  property_count: 2
  slug: hubspot-crm-feature-flags-paging-next-structure
- name: Hubspot Crm Feature Flags Paging Structure
  property_count: 1
  slug: hubspot-crm-feature-flags-paging-structure
- name: Hubspot Crm Feature Flags Portal Flag State Collection Structure
  property_count: 2
  slug: hubspot-crm-feature-flags-portal-flag-state-collection-structure
- name: Hubspot Crm Feature Flags Portal Flag State Input Structure
  property_count: 1
  slug: hubspot-crm-feature-flags-portal-flag-state-input-structure
- name: Hubspot Crm Feature Flags Portal Flag State Structure
  property_count: 4
  slug: hubspot-crm-feature-flags-portal-flag-state-structure
- name: Hubspot Crm Lists Collection Response List Structure
  property_count: 2
  slug: hubspot-crm-lists-collection-response-list-structure
- name: Hubspot Crm Lists Collection Response Membership Structure
  property_count: 2
  slug: hubspot-crm-lists-collection-response-membership-structure
- name: Hubspot Crm Lists Error Structure
  property_count: 4
  slug: hubspot-crm-lists-error-structure
- name: Hubspot Crm Lists List Create Request Structure
  property_count: 4
  slug: hubspot-crm-lists-list-create-request-structure
- name: Hubspot Crm Lists List Structure
  property_count: 9
  slug: hubspot-crm-lists-list-structure
- name: Hubspot Crm Lists Membership Change Request Structure
  property_count: 2
  slug: hubspot-crm-lists-membership-change-request-structure
- name: Hubspot Crm Lists Membership Change Response Structure
  property_count: 4
  slug: hubspot-crm-lists-membership-change-response-structure
- name: Hubspot Crm Lists Membership Structure
  property_count: 2
  slug: hubspot-crm-lists-membership-structure
- name: Hubspot Crm Lists Paging Structure
  property_count: 1
  slug: hubspot-crm-lists-paging-structure
- name: Hubspot Crm Search Crm Object Structure
  property_count: 5
  slug: hubspot-crm-search-crm-object-structure
- name: Hubspot Crm Search Error Structure
  property_count: 5
  slug: hubspot-crm-search-error-structure
- name: Hubspot Crm Search Filter Group Structure
  property_count: 1
  slug: hubspot-crm-search-filter-group-structure
- name: Hubspot Crm Search Filter Structure
  property_count: 5
  slug: hubspot-crm-search-filter-structure
- name: Hubspot Crm Search Paging Structure
  property_count: 1
  slug: hubspot-crm-search-paging-structure
- name: Hubspot Crm Search Search Request Structure
  property_count: 6
  slug: hubspot-crm-search-search-request-structure
- name: Hubspot Crm Search Search Response Structure
  property_count: 3
  slug: hubspot-crm-search-search-response-structure
- name: Hubspot Crm Search Sort Structure
  property_count: 2
  slug: hubspot-crm-search-sort-structure
- name: Hubspot Crm Tickets Association Structure
  property_count: 2
  slug: hubspot-crm-tickets-association-structure
- name: Hubspot Crm Tickets Batch Archive Input Structure
  property_count: 1
  slug: hubspot-crm-tickets-batch-archive-input-structure
- name: Hubspot Crm Tickets Batch Create Input Structure
  property_count: 1
  slug: hubspot-crm-tickets-batch-create-input-structure
- name: Hubspot Crm Tickets Batch Read Input Structure
  property_count: 2
  slug: hubspot-crm-tickets-batch-read-input-structure
- name: Hubspot Crm Tickets Batch Response Ticket Structure
  property_count: 3
  slug: hubspot-crm-tickets-batch-response-ticket-structure
- name: Hubspot Crm Tickets Batch Update Input Structure
  property_count: 1
  slug: hubspot-crm-tickets-batch-update-input-structure
- name: Hubspot Crm Tickets Collection Response Association Structure
  property_count: 2
  slug: hubspot-crm-tickets-collection-response-association-structure
- name: Hubspot Crm Tickets Collection Response Ticket Structure
  property_count: 2
  slug: hubspot-crm-tickets-collection-response-ticket-structure
- name: Hubspot Crm Tickets Error Structure
  property_count: 4
  slug: hubspot-crm-tickets-error-structure
- name: Hubspot Crm Tickets Filter Group Structure
  property_count: 1
  slug: hubspot-crm-tickets-filter-group-structure
- name: Hubspot Crm Tickets Filter Structure
  property_count: 3
  slug: hubspot-crm-tickets-filter-structure
- name: Hubspot Crm Tickets Paging Structure
  property_count: 1
  slug: hubspot-crm-tickets-paging-structure
- name: Hubspot Crm Tickets Search Request Structure
  property_count: 6
  slug: hubspot-crm-tickets-search-request-structure
- name: Hubspot Crm Tickets Simple Public Object Input Structure
  property_count: 1
  slug: hubspot-crm-tickets-simple-public-object-input-structure
- name: Hubspot Crm Tickets Ticket Structure
  property_count: 6
  slug: hubspot-crm-tickets-ticket-structure
- name: Hubspot Custom Workflow Actions Action Definition Collection Structure
  property_count: 2
  slug: hubspot-custom-workflow-actions-action-definition-collection-structure
- name: Hubspot Custom Workflow Actions Action Definition Input Structure
  property_count: 7
  slug: hubspot-custom-workflow-actions-action-definition-input-structure
- name: Hubspot Custom Workflow Actions Action Definition Patch Structure
  property_count: 7
  slug: hubspot-custom-workflow-actions-action-definition-patch-structure
- name: Hubspot Custom Workflow Actions Action Definition Revision Collection Structure
  property_count: 2
  slug: hubspot-custom-workflow-actions-action-definition-revision-collection-structure
- name: Hubspot Custom Workflow Actions Action Definition Revision Structure
  property_count: 3
  slug: hubspot-custom-workflow-actions-action-definition-revision-structure
- name: Hubspot Custom Workflow Actions Action Definition Structure
  property_count: 10
  slug: hubspot-custom-workflow-actions-action-definition-structure
- name: Hubspot Custom Workflow Actions Action Function Collection Structure
  property_count: 1
  slug: hubspot-custom-workflow-actions-action-function-collection-structure
- name: Hubspot Custom Workflow Actions Action Function Input Structure
  property_count: 1
  slug: hubspot-custom-workflow-actions-action-function-input-structure
- name: Hubspot Custom Workflow Actions Action Function Reference Structure
  property_count: 2
  slug: hubspot-custom-workflow-actions-action-function-reference-structure
- name: Hubspot Custom Workflow Actions Action Function Structure
  property_count: 3
  slug: hubspot-custom-workflow-actions-action-function-structure
- name: Hubspot Custom Workflow Actions Action Labels Structure
  property_count: 4
  slug: hubspot-custom-workflow-actions-action-labels-structure
- name: Hubspot Custom Workflow Actions Batch Callback Completion Request Structure
  property_count: 1
  slug: hubspot-custom-workflow-actions-batch-callback-completion-request-structure
- name: Hubspot Custom Workflow Actions Batch Callback Error Structure
  property_count: 3
  slug: hubspot-custom-workflow-actions-batch-callback-error-structure
- name: Hubspot Custom Workflow Actions Batch Callback Input Structure
  property_count: 2
  slug: hubspot-custom-workflow-actions-batch-callback-input-structure
- name: Hubspot Custom Workflow Actions Batch Callback Response Structure
  property_count: 2
  slug: hubspot-custom-workflow-actions-batch-callback-response-structure
- name: Hubspot Custom Workflow Actions Callback Completion Request Structure
  property_count: 1
  slug: hubspot-custom-workflow-actions-callback-completion-request-structure
- name: Hubspot Custom Workflow Actions Error Detail Structure
  property_count: 5
  slug: hubspot-custom-workflow-actions-error-detail-structure
- name: Hubspot Custom Workflow Actions Error Structure
  property_count: 7
  slug: hubspot-custom-workflow-actions-error-structure
- name: Hubspot Custom Workflow Actions Field Option Structure
  property_count: 3
  slug: hubspot-custom-workflow-actions-field-option-structure
- name: Hubspot Custom Workflow Actions Field Type Definition Structure
  property_count: 6
  slug: hubspot-custom-workflow-actions-field-type-definition-structure
- name: Hubspot Custom Workflow Actions Input Field Structure
  property_count: 3
  slug: hubspot-custom-workflow-actions-input-field-structure
- name: Hubspot Custom Workflow Actions Object Request Options Structure
  property_count: 1
  slug: hubspot-custom-workflow-actions-object-request-options-structure
- name: Hubspot Custom Workflow Actions Output Field Structure
  property_count: 1
  slug: hubspot-custom-workflow-actions-output-field-structure
- name: Hubspot Custom Workflow Actions Paging Structure
  property_count: 1
  slug: hubspot-custom-workflow-actions-paging-structure
- name: Hubspot Domains Domain Collection Response Structure
  property_count: 3
  slug: hubspot-domains-domain-collection-response-structure
- name: Hubspot Domains Domain Structure
  property_count: 21
  slug: hubspot-domains-domain-structure
- name: Hubspot Domains Error Detail Structure
  property_count: 5
  slug: hubspot-domains-error-detail-structure
- name: Hubspot Domains Error Structure
  property_count: 7
  slug: hubspot-domains-error-structure
- name: Hubspot Domains Forward Paging Structure
  property_count: 1
  slug: hubspot-domains-forward-paging-structure
- name: Hubspot Domains Next Page Structure
  property_count: 2
  slug: hubspot-domains-next-page-structure
- name: Hubspot Engagement Calls Association Input Structure
  property_count: 2
  slug: hubspot-engagement-calls-association-input-structure
- name: Hubspot Engagement Calls Association Type Structure
  property_count: 2
  slug: hubspot-engagement-calls-association-type-structure
- name: Hubspot Engagement Calls Batch Archive Calls Request Structure
  property_count: 1
  slug: hubspot-engagement-calls-batch-archive-calls-request-structure
- name: Hubspot Engagement Calls Batch Calls Response Structure
  property_count: 7
  slug: hubspot-engagement-calls-batch-calls-response-structure
- name: Hubspot Engagement Calls Batch Create Calls Request Structure
  property_count: 1
  slug: hubspot-engagement-calls-batch-create-calls-request-structure
- name: Hubspot Engagement Calls Batch Error Structure
  property_count: 5
  slug: hubspot-engagement-calls-batch-error-structure
- name: Hubspot Engagement Calls Batch Read Calls Request Structure
  property_count: 4
  slug: hubspot-engagement-calls-batch-read-calls-request-structure
- name: Hubspot Engagement Calls Batch Read Input Structure
  property_count: 1
  slug: hubspot-engagement-calls-batch-read-input-structure
- name: Hubspot Engagement Calls Batch Update Calls Request Structure
  property_count: 1
  slug: hubspot-engagement-calls-batch-update-calls-request-structure
- name: Hubspot Engagement Calls Batch Update Input Structure
  property_count: 2
  slug: hubspot-engagement-calls-batch-update-input-structure
- name: Hubspot Engagement Calls Call Collection Response Structure
  property_count: 2
  slug: hubspot-engagement-calls-call-collection-response-structure
- name: Hubspot Engagement Calls Call Create Request Structure
  property_count: 2
  slug: hubspot-engagement-calls-call-create-request-structure
- name: Hubspot Engagement Calls Call Search Request Structure
  property_count: 6
  slug: hubspot-engagement-calls-call-search-request-structure
- name: Hubspot Engagement Calls Call Search Response Structure
  property_count: 3
  slug: hubspot-engagement-calls-call-search-response-structure
- name: Hubspot Engagement Calls Call Structure
  property_count: 7
  slug: hubspot-engagement-calls-call-structure
- name: Hubspot Engagement Calls Call Update Request Structure
  property_count: 1
  slug: hubspot-engagement-calls-call-update-request-structure
- name: Hubspot Engagement Calls Error Detail Structure
  property_count: 5
  slug: hubspot-engagement-calls-error-detail-structure
- name: Hubspot Engagement Calls Error Structure
  property_count: 7
  slug: hubspot-engagement-calls-error-structure
- name: Hubspot Engagement Calls Filter Group Structure
  property_count: 1
  slug: hubspot-engagement-calls-filter-group-structure
- name: Hubspot Engagement Calls Filter Structure
  property_count: 5
  slug: hubspot-engagement-calls-filter-structure
- name: Hubspot Engagement Calls Gdpr Delete Request Structure
  property_count: 2
  slug: hubspot-engagement-calls-gdpr-delete-request-structure
- name: Hubspot Engagement Calls Next Page Structure
  property_count: 2
  slug: hubspot-engagement-calls-next-page-structure
- name: Hubspot Engagement Calls Paging Structure
  property_count: 1
  slug: hubspot-engagement-calls-paging-structure
- name: Hubspot Engagement Calls Property History Structure
  property_count: 6
  slug: hubspot-engagement-calls-property-history-structure
- name: Hubspot Engagement Calls Sort Option Structure
  property_count: 2
  slug: hubspot-engagement-calls-sort-option-structure
- name: Hubspot Engagement Emails Association Structure
  property_count: 2
  slug: hubspot-engagement-emails-association-structure
- name: Hubspot Engagement Emails Batch Create Input Structure
  property_count: 1
  slug: hubspot-engagement-emails-batch-create-input-structure
- name: Hubspot Engagement Emails Batch Read Input Structure
  property_count: 2
  slug: hubspot-engagement-emails-batch-read-input-structure
- name: Hubspot Engagement Emails Batch Response Email Engagement Structure
  property_count: 3
  slug: hubspot-engagement-emails-batch-response-email-engagement-structure
- name: Hubspot Engagement Emails Batch Update Input Structure
  property_count: 1
  slug: hubspot-engagement-emails-batch-update-input-structure
- name: Hubspot Engagement Emails Collection Response Association Structure
  property_count: 2
  slug: hubspot-engagement-emails-collection-response-association-structure
- name: Hubspot Engagement Emails Collection Response Email Engagement Structure
  property_count: 2
  slug: hubspot-engagement-emails-collection-response-email-engagement-structure
- name: Hubspot Engagement Emails Email Engagement Structure
  property_count: 6
  slug: hubspot-engagement-emails-email-engagement-structure
- name: Hubspot Engagement Emails Error Structure
  property_count: 4
  slug: hubspot-engagement-emails-error-structure
- name: Hubspot Engagement Emails Filter Group Structure
  property_count: 1
  slug: hubspot-engagement-emails-filter-group-structure
- name: Hubspot Engagement Emails Filter Structure
  property_count: 3
  slug: hubspot-engagement-emails-filter-structure
- name: Hubspot Engagement Emails Paging Structure
  property_count: 1
  slug: hubspot-engagement-emails-paging-structure
- name: Hubspot Engagement Emails Search Request Structure
  property_count: 6
  slug: hubspot-engagement-emails-search-request-structure
- name: Hubspot Engagement Emails Simple Public Object Input Structure
  property_count: 1
  slug: hubspot-engagement-emails-simple-public-object-input-structure
- name: Hubspot Engagement Meetings Association Structure
  property_count: 2
  slug: hubspot-engagement-meetings-association-structure
- name: Hubspot Engagement Meetings Batch Create Input Structure
  property_count: 1
  slug: hubspot-engagement-meetings-batch-create-input-structure
- name: Hubspot Engagement Meetings Batch Read Input Structure
  property_count: 2
  slug: hubspot-engagement-meetings-batch-read-input-structure
- name: Hubspot Engagement Meetings Batch Response Meeting Structure
  property_count: 3
  slug: hubspot-engagement-meetings-batch-response-meeting-structure
- name: Hubspot Engagement Meetings Batch Update Input Structure
  property_count: 1
  slug: hubspot-engagement-meetings-batch-update-input-structure
- name: Hubspot Engagement Meetings Collection Response Association Structure
  property_count: 2
  slug: hubspot-engagement-meetings-collection-response-association-structure
- name: Hubspot Engagement Meetings Collection Response Meeting Structure
  property_count: 2
  slug: hubspot-engagement-meetings-collection-response-meeting-structure
- name: Hubspot Engagement Meetings Error Structure
  property_count: 4
  slug: hubspot-engagement-meetings-error-structure
- name: Hubspot Engagement Meetings Filter Group Structure
  property_count: 1
  slug: hubspot-engagement-meetings-filter-group-structure
- name: Hubspot Engagement Meetings Filter Structure
  property_count: 3
  slug: hubspot-engagement-meetings-filter-structure
- name: Hubspot Engagement Meetings Meeting Structure
  property_count: 6
  slug: hubspot-engagement-meetings-meeting-structure
- name: Hubspot Engagement Meetings Paging Structure
  property_count: 1
  slug: hubspot-engagement-meetings-paging-structure
- name: Hubspot Engagement Meetings Search Request Structure
  property_count: 6
  slug: hubspot-engagement-meetings-search-request-structure
- name: Hubspot Engagement Meetings Simple Public Object Input Structure
  property_count: 1
  slug: hubspot-engagement-meetings-simple-public-object-input-structure
- name: Hubspot Engagement Notes Association Input Structure
  property_count: 2
  slug: hubspot-engagement-notes-association-input-structure
- name: Hubspot Engagement Notes Association Type Structure
  property_count: 2
  slug: hubspot-engagement-notes-association-type-structure
- name: Hubspot Engagement Notes Batch Archive Notes Request Structure
  property_count: 1
  slug: hubspot-engagement-notes-batch-archive-notes-request-structure
- name: Hubspot Engagement Notes Batch Create Notes Request Structure
  property_count: 1
  slug: hubspot-engagement-notes-batch-create-notes-request-structure
- name: Hubspot Engagement Notes Batch Error Structure
  property_count: 5
  slug: hubspot-engagement-notes-batch-error-structure
- name: Hubspot Engagement Notes Batch Notes Response Structure
  property_count: 7
  slug: hubspot-engagement-notes-batch-notes-response-structure
- name: Hubspot Engagement Notes Batch Read Input Structure
  property_count: 1
  slug: hubspot-engagement-notes-batch-read-input-structure
- name: Hubspot Engagement Notes Batch Read Notes Request Structure
  property_count: 4
  slug: hubspot-engagement-notes-batch-read-notes-request-structure
- name: Hubspot Engagement Notes Batch Update Input Structure
  property_count: 2
  slug: hubspot-engagement-notes-batch-update-input-structure
- name: Hubspot Engagement Notes Batch Update Notes Request Structure
  property_count: 1
  slug: hubspot-engagement-notes-batch-update-notes-request-structure
- name: Hubspot Engagement Notes Error Detail Structure
  property_count: 5
  slug: hubspot-engagement-notes-error-detail-structure
- name: Hubspot Engagement Notes Error Structure
  property_count: 7
  slug: hubspot-engagement-notes-error-structure
- name: Hubspot Engagement Notes Filter Group Structure
  property_count: 1
  slug: hubspot-engagement-notes-filter-group-structure
- name: Hubspot Engagement Notes Filter Structure
  property_count: 5
  slug: hubspot-engagement-notes-filter-structure
- name: Hubspot Engagement Notes Gdpr Delete Request Structure
  property_count: 2
  slug: hubspot-engagement-notes-gdpr-delete-request-structure
- name: Hubspot Engagement Notes Next Page Structure
  property_count: 2
  slug: hubspot-engagement-notes-next-page-structure
- name: Hubspot Engagement Notes Note Collection Response Structure
  property_count: 2
  slug: hubspot-engagement-notes-note-collection-response-structure
- name: Hubspot Engagement Notes Note Create Request Structure
  property_count: 2
  slug: hubspot-engagement-notes-note-create-request-structure
- name: Hubspot Engagement Notes Note Search Request Structure
  property_count: 6
  slug: hubspot-engagement-notes-note-search-request-structure
- name: Hubspot Engagement Notes Note Search Response Structure
  property_count: 3
  slug: hubspot-engagement-notes-note-search-response-structure
- name: Hubspot Engagement Notes Note Structure
  property_count: 7
  slug: hubspot-engagement-notes-note-structure
- name: Hubspot Engagement Notes Note Update Request Structure
  property_count: 1
  slug: hubspot-engagement-notes-note-update-request-structure
- name: Hubspot Engagement Notes Paging Structure
  property_count: 1
  slug: hubspot-engagement-notes-paging-structure
- name: Hubspot Engagement Notes Property History Structure
  property_count: 6
  slug: hubspot-engagement-notes-property-history-structure
- name: Hubspot Engagement Notes Sort Option Structure
  property_count: 2
  slug: hubspot-engagement-notes-sort-option-structure
- name: Hubspot Engagement Tasks Association Structure
  property_count: 2
  slug: hubspot-engagement-tasks-association-structure
- name: Hubspot Engagement Tasks Batch Create Input Structure
  property_count: 1
  slug: hubspot-engagement-tasks-batch-create-input-structure
- name: Hubspot Engagement Tasks Batch Read Input Structure
  property_count: 2
  slug: hubspot-engagement-tasks-batch-read-input-structure
- name: Hubspot Engagement Tasks Batch Response Task Structure
  property_count: 3
  slug: hubspot-engagement-tasks-batch-response-task-structure
- name: Hubspot Engagement Tasks Batch Update Input Structure
  property_count: 1
  slug: hubspot-engagement-tasks-batch-update-input-structure
- name: Hubspot Engagement Tasks Collection Response Association Structure
  property_count: 2
  slug: hubspot-engagement-tasks-collection-response-association-structure
- name: Hubspot Engagement Tasks Collection Response Task Structure
  property_count: 2
  slug: hubspot-engagement-tasks-collection-response-task-structure
- name: Hubspot Engagement Tasks Error Structure
  property_count: 4
  slug: hubspot-engagement-tasks-error-structure
- name: Hubspot Engagement Tasks Filter Group Structure
  property_count: 1
  slug: hubspot-engagement-tasks-filter-group-structure
- name: Hubspot Engagement Tasks Filter Structure
  property_count: 3
  slug: hubspot-engagement-tasks-filter-structure
- name: Hubspot Engagement Tasks Paging Structure
  property_count: 1
  slug: hubspot-engagement-tasks-paging-structure
- name: Hubspot Engagement Tasks Search Request Structure
  property_count: 6
  slug: hubspot-engagement-tasks-search-request-structure
- name: Hubspot Engagement Tasks Simple Public Object Input Structure
  property_count: 1
  slug: hubspot-engagement-tasks-simple-public-object-input-structure
- name: Hubspot Engagement Tasks Task Structure
  property_count: 6
  slug: hubspot-engagement-tasks-task-structure
- name: Hubspot Marketing Emal Email Message Structure
  property_count: 6
  slug: hubspot-marketing-emal-email-message-structure
- name: Hubspot Marketing Emal Error Detail Structure
  property_count: 5
  slug: hubspot-marketing-emal-error-detail-structure
- name: Hubspot Marketing Emal Error Structure
  property_count: 7
  slug: hubspot-marketing-emal-error-structure
- name: Hubspot Marketing Emal Next Page Structure
  property_count: 2
  slug: hubspot-marketing-emal-next-page-structure
- name: Hubspot Marketing Emal Paging Structure
  property_count: 1
  slug: hubspot-marketing-emal-paging-structure
- name: Hubspot Marketing Emal Smtp Token Collection Response Structure
  property_count: 2
  slug: hubspot-marketing-emal-smtp-token-collection-response-structure
- name: Hubspot Marketing Emal Smtp Token Create Request Structure
  property_count: 2
  slug: hubspot-marketing-emal-smtp-token-create-request-structure
- name: Hubspot Marketing Emal Smtp Token Structure
  property_count: 6
  slug: hubspot-marketing-emal-smtp-token-structure
- name: Hubspot Marketing Emal Smtp Token With Password Structure
  property_count: 7
  slug: hubspot-marketing-emal-smtp-token-with-password-structure
- name: Hubspot Marketing Emal Transactional Email Request Structure
  property_count: 4
  slug: hubspot-marketing-emal-transactional-email-request-structure
- name: Hubspot Marketing Emal Transactional Email Response Structure
  property_count: 6
  slug: hubspot-marketing-emal-transactional-email-response-structure
- name: Hubspot Oauth Access Token Metadata Structure
  property_count: 9
  slug: hubspot-oauth-access-token-metadata-structure
- name: Hubspot Oauth Error Detail Structure
  property_count: 5
  slug: hubspot-oauth-error-detail-structure
- name: Hubspot Oauth Error Structure
  property_count: 7
  slug: hubspot-oauth-error-structure
- name: Hubspot Oauth Refresh Token Metadata Structure
  property_count: 6
  slug: hubspot-oauth-refresh-token-metadata-structure
- name: Hubspot Oauth Token Request Structure
  property_count: 6
  slug: hubspot-oauth-token-request-structure
- name: Hubspot Oauth Token Response Structure
  property_count: 5
  slug: hubspot-oauth-token-response-structure
- name: Hubspot Source Code Action Response Structure
  property_count: 5
  slug: hubspot-source-code-action-response-structure
- name: Hubspot Source Code Asset File Metadata Structure
  property_count: 8
  slug: hubspot-source-code-asset-file-metadata-structure
- name: Hubspot Source Code Error Detail Structure
  property_count: 5
  slug: hubspot-source-code-error-detail-structure
- name: Hubspot Source Code Error Structure
  property_count: 7
  slug: hubspot-source-code-error-structure
- name: Hubspot Source Code File Extract Request Structure
  property_count: 1
  slug: hubspot-source-code-file-extract-request-structure
- name: Hubspot Source Code File Upload Request Structure
  property_count: 1
  slug: hubspot-source-code-file-upload-request-structure
- name: Hubspot Source Code Task Locator Structure
  property_count: 2
  slug: hubspot-source-code-task-locator-structure
- name: Hubspot Source Code Validation Error Structure
  property_count: 4
  slug: hubspot-source-code-validation-error-structure
- name: Hubspot Source Code Validation Result Structure
  property_count: 3
  slug: hubspot-source-code-validation-result-structure
- name: Hubspot Source Code Validation Warning Structure
  property_count: 3
  slug: hubspot-source-code-validation-warning-structure
- name: Marketing Emal Api Email Message Structure
  property_count: 6
  slug: marketing-emal-api-email-message-structure
- name: Marketing Emal Api Next Page Structure
  property_count: 2
  slug: marketing-emal-api-next-page-structure
- name: Marketing Emal Api Paging Structure
  property_count: 1
  slug: marketing-emal-api-paging-structure
- name: Marketing Emal Api Smtp Token Collection Response Structure
  property_count: 2
  slug: marketing-emal-api-smtp-token-collection-response-structure
- name: Marketing Emal Api Smtp Token Create Request Structure
  property_count: 2
  slug: marketing-emal-api-smtp-token-create-request-structure
- name: Marketing Emal Api Smtp Token Structure
  property_count: 6
  slug: marketing-emal-api-smtp-token-structure
- name: Marketing Emal Api Smtp Token With Password Structure
  property_count: 7
  slug: marketing-emal-api-smtp-token-with-password-structure
- name: Marketing Emal Api Transactional Email Request Structure
  property_count: 4
  slug: marketing-emal-api-transactional-email-request-structure
- name: Marketing Emal Api Transactional Email Response Structure
  property_count: 6
  slug: marketing-emal-api-transactional-email-response-structure
- name: Oauth Api Access Token Metadata Structure
  property_count: 9
  slug: oauth-api-access-token-metadata-structure
- name: Oauth Api Refresh Token Metadata Structure
  property_count: 6
  slug: oauth-api-refresh-token-metadata-structure
- name: Oauth Api Token Request Structure
  property_count: 6
  slug: oauth-api-token-request-structure
- name: Oauth Api Token Response Structure
  property_count: 5
  slug: oauth-api-token-response-structure
- name: Source Code Api Action Response Structure
  property_count: 5
  slug: source-code-api-action-response-structure
- name: Source Code Api Asset File Metadata Structure
  property_count: 8
  slug: source-code-api-asset-file-metadata-structure
- name: Source Code Api File Extract Request Structure
  property_count: 1
  slug: source-code-api-file-extract-request-structure
- name: Source Code Api File Upload Request Structure
  property_count: 1
  slug: source-code-api-file-upload-request-structure
- name: Source Code Api Task Locator Structure
  property_count: 2
  slug: source-code-api-task-locator-structure
- name: Source Code Api Validation Error Structure
  property_count: 4
  slug: source-code-api-validation-error-structure
- name: Source Code Api Validation Result Structure
  property_count: 3
  slug: source-code-api-validation-result-structure
- name: Source Code Api Validation Warning Structure
  property_count: 3
  slug: source-code-api-validation-warning-structure
jsonld:
- class_count: 6
  name: Hubspot Analytics Events Api Context
  property_count: 14
  slug: hubspot-analytics-events-api-context
- class_count: 0
  name: Hubspot Analytics Events Context
  property_count: 8
  slug: hubspot-analytics-events-context
- class_count: 15
  name: Hubspot Authors Api Context
  property_count: 30
  slug: hubspot-authors-api-context
- class_count: 0
  name: Hubspot Authors Context
  property_count: 18
  slug: hubspot-authors-context
- class_count: 19
  name: Hubspot Blog Posts Api Context
  property_count: 52
  slug: hubspot-blog-posts-api-context
- class_count: 0
  name: Hubspot Blog Posts Context
  property_count: 22
  slug: hubspot-blog-posts-context
- class_count: 8
  name: Hubspot Cms Hubdb Api Context
  property_count: 15
  slug: hubspot-cms-hubdb-api-context
- class_count: 0
  name: Hubspot Cms Hubdb Context
  property_count: 9
  slug: hubspot-cms-hubdb-context
- class_count: 5
  name: Hubspot Cms Pages Api Context
  property_count: 20
  slug: hubspot-cms-pages-api-context
- class_count: 0
  name: Hubspot Cms Pages Context
  property_count: 6
  slug: hubspot-cms-pages-context
- class_count: 24
  name: Hubspot Commerce Payments Api Context
  property_count: 47
  slug: hubspot-commerce-payments-api-context
- class_count: 0
  name: Hubspot Commerce Payments Context
  property_count: 26
  slug: hubspot-commerce-payments-context
- class_count: 13
  name: Hubspot Commerce Subscriptions Api Context
  property_count: 22
  slug: hubspot-commerce-subscriptions-api-context
- class_count: 0
  name: Hubspot Commerce Subscriptions Context
  property_count: 14
  slug: hubspot-commerce-subscriptions-context
- class_count: 1
  name: Hubspot Context
  property_count: 49
  slug: hubspot-context
- class_count: 17
  name: Hubspot Conversations Api Context
  property_count: 40
  slug: hubspot-conversations-api-context
- class_count: 0
  name: Hubspot Conversations Context
  property_count: 19
  slug: hubspot-conversations-context
- class_count: 19
  name: Hubspot Crm Associations Api Context
  property_count: 28
  slug: hubspot-crm-associations-api-context
- class_count: 0
  name: Hubspot Crm Associations Context
  property_count: 22
  slug: hubspot-crm-associations-context
- class_count: 14
  name: Hubspot Crm Companies Api Context
  property_count: 22
  slug: hubspot-crm-companies-api-context
- class_count: 0
  name: Hubspot Crm Companies Context
  property_count: 15
  slug: hubspot-crm-companies-context
- class_count: 14
  name: Hubspot Crm Contacts Api Context
  property_count: 22
  slug: hubspot-crm-contacts-api-context
- class_count: 0
  name: Hubspot Crm Contacts Context
  property_count: 15
  slug: hubspot-crm-contacts-context
- class_count: 14
  name: Hubspot Crm Deals Api Context
  property_count: 22
  slug: hubspot-crm-deals-api-context
- class_count: 0
  name: Hubspot Crm Deals Context
  property_count: 15
  slug: hubspot-crm-deals-context
- class_count: 14
  name: Hubspot Crm Feature Flags Api Context
  property_count: 20
  slug: hubspot-crm-feature-flags-api-context
- class_count: 0
  name: Hubspot Crm Feature Flags Context
  property_count: 16
  slug: hubspot-crm-feature-flags-context
- class_count: 8
  name: Hubspot Crm Lists Api Context
  property_count: 21
  slug: hubspot-crm-lists-api-context
- class_count: 0
  name: Hubspot Crm Lists Context
  property_count: 9
  slug: hubspot-crm-lists-context
- class_count: 7
  name: Hubspot Crm Search Api Context
  property_count: 21
  slug: hubspot-crm-search-api-context
- class_count: 0
  name: Hubspot Crm Search Context
  property_count: 8
  slug: hubspot-crm-search-context
- class_count: 14
  name: Hubspot Crm Tickets Api Context
  property_count: 22
  slug: hubspot-crm-tickets-api-context
- class_count: 0
  name: Hubspot Crm Tickets Context
  property_count: 15
  slug: hubspot-crm-tickets-context
- class_count: 22
  name: Hubspot Custom Workflow Actions Api Context
  property_count: 39
  slug: hubspot-custom-workflow-actions-api-context
- class_count: 0
  name: Hubspot Custom Workflow Actions Context
  property_count: 24
  slug: hubspot-custom-workflow-actions-context
- class_count: 4
  name: Hubspot Domains Api Context
  property_count: 27
  slug: hubspot-domains-api-context
- class_count: 0
  name: Hubspot Domains Context
  property_count: 6
  slug: hubspot-domains-context
- class_count: 23
  name: Hubspot Engagement Calls Api Context
  property_count: 46
  slug: hubspot-engagement-calls-api-context
- class_count: 0
  name: Hubspot Engagement Calls Context
  property_count: 25
  slug: hubspot-engagement-calls-context
- class_count: 13
  name: Hubspot Engagement Emails Api Context
  property_count: 22
  slug: hubspot-engagement-emails-api-context
- class_count: 0
  name: Hubspot Engagement Emails Context
  property_count: 14
  slug: hubspot-engagement-emails-context
- class_count: 13
  name: Hubspot Engagement Meetings Api Context
  property_count: 22
  slug: hubspot-engagement-meetings-api-context
- class_count: 0
  name: Hubspot Engagement Meetings Context
  property_count: 14
  slug: hubspot-engagement-meetings-context
- class_count: 2
  name: Hubspot Engagement Notes Association Context
  property_count: 4
  slug: hubspot-engagement-notes-association-context
- class_count: 8
  name: Hubspot Engagement Notes Batch Context
  property_count: 15
  slug: hubspot-engagement-notes-batch-context
- class_count: 0
  name: Hubspot Engagement Notes Context
  property_count: 25
  slug: hubspot-engagement-notes-context
- class_count: 2
  name: Hubspot Engagement Notes Filter Context
  property_count: 6
  slug: hubspot-engagement-notes-filter-context
- class_count: 1
  name: Hubspot Engagement Notes Gdpr Context
  property_count: 2
  slug: hubspot-engagement-notes-gdpr-context
- class_count: 1
  name: Hubspot Engagement Notes Next Context
  property_count: 2
  slug: hubspot-engagement-notes-next-context
- class_count: 6
  name: Hubspot Engagement Notes Note Context
  property_count: 16
  slug: hubspot-engagement-notes-note-context
- class_count: 1
  name: Hubspot Engagement Notes Paging Context
  property_count: 1
  slug: hubspot-engagement-notes-paging-context
- class_count: 1
  name: Hubspot Engagement Notes Property Context
  property_count: 6
  slug: hubspot-engagement-notes-property-context
- class_count: 1
  name: Hubspot Engagement Notes Sort Context
  property_count: 2
  slug: hubspot-engagement-notes-sort-context
- class_count: 13
  name: Hubspot Engagement Tasks Api Context
  property_count: 22
  slug: hubspot-engagement-tasks-api-context
- class_count: 0
  name: Hubspot Engagement Tasks Context
  property_count: 14
  slug: hubspot-engagement-tasks-context
- class_count: 9
  name: Hubspot Marketing Emal Api Context
  property_count: 28
  slug: hubspot-marketing-emal-api-context
- class_count: 0
  name: Hubspot Marketing Emal Context
  property_count: 11
  slug: hubspot-marketing-emal-context
- class_count: 4
  name: Hubspot Oauth Api Context
  property_count: 17
  slug: hubspot-oauth-api-context
- class_count: 0
  name: Hubspot Oauth Context
  property_count: 6
  slug: hubspot-oauth-context
- class_count: 8
  name: Hubspot Source Code Api Context
  property_count: 23
  slug: hubspot-source-code-api-context
- class_count: 0
  name: Hubspot Source Code Context
  property_count: 10
  slug: hubspot-source-code-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.hubspot.com over HTTP requiring OAuth.
  name: MCP Server
  slug: hubspot
modified: '2026-09-16'
name: HubSpot
nav: Providers
network: true
overview: 'HubSpot publishes 81 API contracts indexed on the [APIs.io](https://apis.io/) network, including Webhooks API, A/B tests API, Actors API, and 78 more. Tagged areas include Analytics, Commerce, Content, CRM, and Customer Service.


  The HubSpot catalog on APIs.io includes 1 event-driven AsyncAPI specification, 61 JSON-LD contexts, and 4 Spectral governance rulesets.


  HubSpot''s developer surface includes authentication, API reference, developer portal, documentation, changelog, support, engineering blog, and 178 more developer resources.'
plans:
- name: Hubspot Plans Pricing
  plan_count: 4
  slug: hubspot-plans-pricing
- name: Hubspot Price Estimates
  plan_count: 0
  slug: hubspot-price-estimates
random_paper: 5
rate_limits:
- limit_count: 13
  name: Hubspot Rate Limits
  slug: hubspot-rate-limits
rules:
- authorship: generated
  effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: HubSpot — asyncapi rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: hubspot-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: HubSpot — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: hubspot-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: HubSpot API Rules
  rule_count: 12
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 4
  slug: hubspot-rules
- authorship: generated
  effective_rule_count: 69
  extends:
  - spectral:oas
  name: HubSpot API Rules
  rule_count: 28
  severity_counts:
    error: 19
    hint: 0
    info: 2
    warn: 7
  slug: hubspot-spectral-rules
scopes:
- name: Hubspot Scopes
  scope_count: 29
  slug: hubspot-scopes
  summary_line: 29 scopes · authorizationCode
score:
  band: exemplar
  composite: 94.6
  coverage:
    artifact_dirs: 46
    catalog_earned: 87.0
    catalog_earned_first_party: 24.0
    catalog_gap: 28.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 100.0
    contract_governance: 45.5
    contract_quality: 63.8
    developer_ergonomics: 94.6
    discoverability: 81.7
    operational_transparency: 94.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 94.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 45
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 100.0
screenshot: https://apis.io/screenshots/hubspot/hubspot-2026-06-20T182920.png
security:
- kind: authentication
  name: Hubspot Authentication
  slug: hubspot-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Hubspot Domain Security
  slug: hubspot-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Hubspot Vulnerability Disclosure
  slug: hubspot-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Hubspot Trust Center
  slug: hubspot-trust-center
  summary_line: SOC 2, HIPAA, GDPR
skill_count: 5
skills:
- name: hubspot-advance-a-deal
  slug: hubspot-advance-a-deal
- name: hubspot-create-contact-with-company
  slug: hubspot-create-contact-with-company
- name: hubspot-handle-webhook-events
  slug: hubspot-handle-webhook-events
- name: hubspot-oauth-token-lifecycle
  slug: hubspot-oauth-token-lifecycle
- name: hubspot-upsert-contacts-in-bulk
  slug: hubspot-upsert-contacts-in-bulk
slug: hubspot
tags:
- Analytics
- Commerce
- Content
- CRM
- Customer Service
- Email Marketing
- Marketing
- Marketing Automation
- Sales
- HubSpot
use_cases:
- description: Use AI to generate blog posts, social media content, and marketing copy at scale.
  name: AI-Powered Content Creation
- description: Leverage AI for lead scoring, deal forecasting, and automated sales email generation.
  name: AI-Powered Sales
- description: Track and analyze marketing, sales, and service performance with unified reporting dashboards.
  name: Analytics
- description: Create, manage, and publish website content, blog posts, and landing pages.
  name: Content Creation and Management
- description: Centralized content management for creating and distributing content across channels.
  name: Content Hub
- description: Manage customer support tickets, knowledge base, and feedback surveys.
  name: Customer Service
- description: Automate ticket routing, responses, and escalation with workflow-based support.
  name: Customer Support Automation
- description: Clean, deduplicate, and enrich CRM data with automated data quality tools.
  name: Data Management and Insights
- description: Track deals through customizable pipeline stages with forecasting and reporting.
  name: Deal Management
- description: Design, send, and analyze marketing email campaigns with segmentation and A/B testing.
  name: Email Marketing
- description: Connect with 1,500+ integrations in the HubSpot App Marketplace.
  name: HubSpot Ecosystem
- description: Attract visitors with SEO, blogs, and social media, then convert them with forms and CTAs.
  name: Inbound Marketing
- description: Connect apps and automate business processes with programmable workflows.
  name: Integration and Automation
- description: Build landing pages with embedded forms to capture and qualify leads.
  name: Landing Pages & Forms
- description: Capture leads through forms, chatbots, and CTAs, then nurture with automated sequences.
  name: Lead Generation and Conversion
- description: Engage website visitors in real-time with live chat and route conversations to the right team.
  name: Live Chat
- description: Sync, clean, and automate business data across systems with programmable automation.
  name: Operations Hub
- description: Manage sales teams with activity tracking, quotas, forecasting, and coaching tools.
  name: Sales Management
- description: Deliver customer service with ticketing, knowledge base, feedback, and customer portal.
  name: Service Hub
- description: Automate repetitive tasks across marketing, sales, and service with visual workflow builder.
  name: Workflows
website: https://www.hubspot.com/
---
