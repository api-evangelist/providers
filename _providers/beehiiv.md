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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 61.2
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Beehiiv Agentic Access
  operation_count: 77
  slug: beehiiv-agentic-access
  summary_line: 77 operations · 32 acting
api_count: 5
apis:
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Authorizations API from beehiiv — 1 operation(s) for authorizations.
  name: beehiiv Authorizations API
  phrasing_intents:
  - id: authorize
    intent: Start the OAuth authorization flow
    question: How do I send a beehiiv user to log in and grant my app access?
  phrasing_ops: 1
  slug: beehiiv-authorizations-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Tokens API from beehiiv — 4 operation(s) for tokens.
  name: beehiiv Tokens API
  phrasing_intents:
  - id: token
    intent: Exchange a code or refresh token for access
    question: How do I turn an OAuth authorization code into an access token?
  - id: revoke
    intent: Revoke an access or refresh token
    question: How do I revoke a token when a user disconnects my app?
  - id: introspect
    intent: Check whether a token is active
    question: Is a given OAuth token still valid?
  - id: token-info
    intent: Get info about the current access token
    question: What scopes and expiry does the access token I'm calling with have?
  phrasing_ops: 4
  slug: beehiiv-tokens-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Webhooks API from beehiiv — 0 operation(s) for webhooks.
  name: beehiiv Webhooks API
  phrasing_intents:
  - id: create
    intent: Create a webhook
    question: How do I get notified at my own URL when someone subscribes?
  - id: index
    intent: List a publication's webhooks
    question: Which webhooks are registered on my newsletter?
  - id: show
    intent: Get one webhook
    question: What events and URL is a specific webhook configured with?
  - id: update
    intent: Change a webhook's events or description
    question: How do I change which events an existing webhook listens for?
  - id: delete
    intent: Delete a webhook
    question: How do I stop a webhook from receiving events?
  phrasing_ops: 5
  slug: beehiiv-webhooks-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Ad Network Offers API from beehiiv — 2 operation(s) for ad network offers.
  name: beehiiv Ad Network Offers API
  phrasing_intents:
  - id: index
    intent: List ad network offers for a publication
    question: What ad offers are available for my newsletter to run right now?
  - id: create
    intent: Accept an ad offer and place it in a post
    question: How do I accept an ad network offer and drop the ad into one of my posts?
  - id: advertisements
    intent: List the ad creatives for an ad offer
    question: What ad copy comes with a particular ad network offer?
  phrasing_ops: 3
  slug: beehiiv-ad-network-offers-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Ad Network Reports API from beehiiv — 3 operation(s) for ad network reports.
  name: beehiiv Ad Network Reports API
  phrasing_intents:
  - id: index
    intent: List ad performance and payment reports
    question: Where can I see per-ad performance and payment reports for my newsletter?
  - id: summary
    intent: Summarize ad revenue for one publication
    question: What is the total ad revenue for one of my newsletters this quarter?
  - id: account-summary
    intent: Summarize ad revenue across all publications
    question: How much ad revenue did my whole account earn across every newsletter?
  phrasing_ops: 3
  slug: beehiiv-ad-network-reports-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Advertisement Opportunities API from beehiiv — 1 operation(s) for advertisement opportunities.
  name: beehiiv Advertisement Opportunities API
  phrasing_intents:
  - id: index
    intent: List accepted advertisement opportunities
    question: Which ad opportunities have I already accepted for my newsletter?
  phrasing_ops: 1
  slug: beehiiv-advertisement-opportunities-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Authors API from beehiiv — 2 operation(s) for authors.
  name: beehiiv Authors API
  phrasing_intents:
  - id: index
    intent: List a publication's authors
    question: Who are the authors that can write for my newsletter?
  - id: show
    intent: Get one author's details
    question: What profile details are stored for a specific author?
  phrasing_ops: 2
  slug: beehiiv-authors-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Automation Journeys API from beehiiv — 2 operation(s) for automation journeys.
  name: beehiiv Automation Journeys API
  phrasing_intents:
  - id: create
    intent: Enroll an existing subscriber in an automation
    question: How do I add a current subscriber to an automation flow from my own app?
  - id: index
    intent: List subscriber journeys through an automation
    question: Which subscribers have gone through a particular automation?
  - id: show
    intent: Get one automation journey
    question: What happened in one specific subscriber's run through an automation?
  phrasing_ops: 3
  slug: beehiiv-automation-journeys-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Automations API from beehiiv — 3 operation(s) for automations.
  name: beehiiv Automations API
  phrasing_intents:
  - id: index
    intent: List a publication's automations
    question: What automations are set up on my newsletter?
  - id: show
    intent: Get one automation
    question: How is a specific automation configured?
  - id: list-emails
    intent: List an automation's emails with stats
    question: How are the emails inside my welcome automation performing?
  phrasing_ops: 3
  slug: beehiiv-automations-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Bulk Subscription Updates API from beehiiv — 4 operation(s) for bulk subscription updates.
  name: beehiiv Bulk Subscription Updates API
  phrasing_intents:
  - id: index
    intent: List bulk subscription update jobs
    question: Where can I see the history of bulk subscriber updates I've run?
  - id: show
    intent: Check one bulk subscription update job
    question: Did my bulk subscriber update finish successfully?
  - id: put
    intent: Bulk update subscription fields (PUT)
    question: How do I change custom fields and tiers for many subscribers at once using PUT?
  - id: patch
    intent: Bulk update subscription fields (PATCH)
    question: Can I PATCH custom fields and tiers across a batch of subscribers?
  - id: put-status
    intent: Bulk set subscription status (PUT)
    question: How do I set the same status on a list of subscription IDs with a PUT request?
  - id: patch-status
    intent: Bulk set subscription status (PATCH)
    question: Can I PATCH a batch of subscription IDs to a new status?
  phrasing_ops: 6
  slug: beehiiv-bulk-subscription-updates-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Bulk Subscriptions API from beehiiv — 1 operation(s) for bulk subscriptions.
  name: beehiiv Bulk Subscriptions API
  phrasing_intents:
  - id: create
    intent: Create many subscriptions at once
    question: How do I import a batch of new subscribers into my newsletter in one call?
  phrasing_ops: 1
  slug: beehiiv-bulk-subscriptions-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Complimentary Access API from beehiiv — 2 operation(s) for complimentary access.
  name: beehiiv Complimentary Access API
  phrasing_intents:
  - id: index
    intent: List complimentary access grants
    question: Who has been given free complimentary access to my paid newsletter?
  - id: show
    intent: Get one complimentary access grant
    question: What are the details of a specific complimentary access grant?
  phrasing_ops: 2
  slug: beehiiv-complimentary-access-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Condition Sets API from beehiiv — 2 operation(s) for condition sets.
  name: beehiiv Condition Sets API
  phrasing_intents:
  - id: index
    intent: List audience condition sets
    question: What reusable audience conditions are defined for my dynamic content?
  - id: show
    intent: Get one condition set
    question: How many active subscribers match a particular condition set?
  phrasing_ops: 2
  slug: beehiiv-condition-sets-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Custom Fields API from beehiiv — 2 operation(s) for custom fields.
  name: beehiiv Custom Fields API
  phrasing_intents:
  - id: create
    intent: Create a custom subscriber field
    question: How do I add a new custom field like birthday or company to my subscribers?
  - id: index
    intent: List a publication's custom fields
    question: What custom subscriber fields exist on my newsletter?
  - id: show
    intent: Get one custom field
    question: What type and label does a specific custom field have?
  - id: put
    intent: Rename a custom field (PUT)
    question: How do I change a custom field's display name with a PUT request?
  - id: patch
    intent: Rename a custom field (PATCH)
    question: Can I PATCH just the display label of a custom field?
  - id: delete
    intent: Delete a custom field
    question: How do I remove a custom field I no longer use?
  phrasing_ops: 6
  slug: beehiiv-custom-fields-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Data Deletion API from beehiiv — 2 operation(s) for data deletion.
  name: beehiiv Data Deletion API
  phrasing_intents:
  - id: create
    intent: Request permanent deletion of a subscriber's data
    question: How do I erase a subscriber's personal data across all my publications?
  - id: index
    intent: List subscriber data deletion requests
    question: Which GDPR-style data deletion requests have we filed?
  - id: show
    intent: Check a data deletion request's status
    question: Has a specific subscriber data deletion request been completed yet?
  phrasing_ops: 3
  slug: beehiiv-data-deletion-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The engagements API from beehiiv — 1 operation(s) for engagements.
  name: beehiiv Engagements API
  phrasing_intents:
  - id: index
    intent: Get email engagement metrics over time
    question: What were my newsletter's opens and clicks per day last week?
  phrasing_ops: 1
  slug: beehiiv-engagements-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Newsletter List Subscriptions API from beehiiv — 3 operation(s) for newsletter list subscriptions.
  name: beehiiv Newsletter List Subscriptions API
  phrasing_intents:
  - id: create
    intent: Add an existing subscriber to a newsletter list
    question: How do I put a current subscriber onto one of my newsletter lists?
  - id: index
    intent: List subscribers on a newsletter list
    question: Who is subscribed to a particular newsletter list?
  - id: show
    intent: Get one newsletter list membership
    question: What are the details of a single list membership record?
  - id: update
    intent: Unsubscribe a list membership by its ID
    question: How do I remove someone from a newsletter list using the list subscription ID?
  - id: update-by-subscription-id
    intent: Unsubscribe from a list by subscription ID
    question: What if I only have the subscriber's subscription ID and want them off a newsletter list?
  phrasing_ops: 5
  slug: beehiiv-newsletter-list-subscriptions-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Newsletter Lists API from beehiiv — 2 operation(s) for newsletter lists.
  name: beehiiv Newsletter Lists API
  phrasing_intents:
  - id: index
    intent: List a publication's newsletter lists
    question: What newsletter lists does my publication have?
  - id: create
    intent: Create a newsletter list
    question: How do I start a new topic list that readers can subscribe to separately?
  - id: show
    intent: Get one newsletter list
    question: What are the settings of a specific newsletter list?
  - id: update
    intent: Update a newsletter list
    question: How do I rename a newsletter list or change its description?
  - id: delete
    intent: Delete a newsletter list
    question: How do I get rid of a newsletter list I no longer send?
  phrasing_ops: 5
  slug: beehiiv-newsletter-lists-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The oauth_users API from beehiiv — 1 operation(s) for oauth_users.
  name: beehiiv OAUTH Users API
  phrasing_intents:
  - id: identify
    intent: Identify the user behind an OAuth token
    question: Which beehiiv user authorized my app's access token?
  phrasing_ops: 1
  slug: beehiiv-oauth-users-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The podcasts API from beehiiv — 4 operation(s) for podcasts.
  name: beehiiv Podcasts API
  phrasing_intents:
  - id: list-podcasts
    intent: List a publication's podcasts
    question: What podcast shows does my publication host?
  - id: get-podcast
    intent: Get one podcast show
    question: What are the details of a specific podcast show?
  - id: list-episodes
    intent: List a podcast's episodes
    question: Which episodes have been published on my podcast?
  - id: get-episode
    intent: Get one podcast episode
    question: What are the details of one particular podcast episode?
  phrasing_ops: 4
  slug: beehiiv-podcasts-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Polls API from beehiiv — 3 operation(s) for polls.
  name: beehiiv Polls API
  phrasing_intents:
  - id: index
    intent: List a publication's polls
    question: What polls have I run in my newsletter?
  - id: show
    intent: Get one poll and its vote counts
    question: How many votes did each choice get on a specific poll?
  - id: list-responses
    intent: List individual responses to a poll
    question: Which subscribers answered a poll, and what did each one pick?
  phrasing_ops: 3
  slug: beehiiv-polls-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Post Templates API from beehiiv — 1 operation(s) for post templates.
  name: beehiiv Post Templates API
  phrasing_intents:
  - id: index
    intent: List post templates
    question: What post templates can I start a new issue from?
  phrasing_ops: 1
  slug: beehiiv-post-templates-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Posts API from beehiiv — 5 operation(s) for posts.
  name: beehiiv Posts API
  phrasing_intents:
  - id: create
    intent: Create a newsletter post
    question: How do I create and schedule a newsletter issue through the API?
  - id: index
    intent: List a publication's posts
    question: What posts have I published on my newsletter?
  - id: update
    intent: Update an existing post
    question: How do I change the title or subtitle of an existing post?
  - id: show
    intent: Get one post
    question: Can I fetch a single post and its content by ID?
  - id: delete
    intent: Delete or archive a post
    question: How do I delete a draft post I don't need?
  - id: aggregate-stats
    intent: Get combined stats across all posts
    question: What are the total opens and clicks across all my posts combined?
  - id: test-send
    intent: Send a test email of a post
    question: How do I email myself a test copy of a post before it goes out?
  - id: preview
    intent: Generate a preview link for a post
    question: How can I see what a post looks like to premium subscribers before sending?
  phrasing_ops: 8
  slug: beehiiv-posts-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Publications API from beehiiv — 2 operation(s) for publications.
  name: beehiiv Publications API
  phrasing_intents:
  - id: index
    intent: List my publications
    question: Which newsletters can my API key access?
  - id: show
    intent: Get one publication
    question: What are the details and subscriber stats for one of my newsletters?
  phrasing_ops: 2
  slug: beehiiv-publications-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Referral Program API from beehiiv — 1 operation(s) for referral program.
  name: beehiiv Referral Program API
  phrasing_intents:
  - id: show
    intent: Get the referral program and its rewards
    question: What milestones and rewards are set up in my newsletter's referral program?
  phrasing_ops: 1
  slug: beehiiv-referral-program-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Segments API from beehiiv — 5 operation(s) for segments.
  name: beehiiv Segments API
  phrasing_intents:
  - id: create
    intent: Create a subscriber segment
    question: How do I build a segment from a list of email addresses?
  - id: index
    intent: List a publication's segments
    question: What subscriber segments have I built?
  - id: show
    intent: Get one segment
    question: What is the status and size of a specific segment?
  - id: delete
    intent: Delete a segment
    question: How do I remove a segment I no longer need?
  - id: recalculate
    intent: Recalculate a segment
    question: How do I refresh a segment so it reflects current subscriber data?
  - id: list-members
    intent: List a segment's subscribers with full details
    question: Who is in a segment, with their full subscriber profiles?
  - id: expand-results
    intent: List only the subscriber IDs in a segment
    question: Is there a lightweight way to get just the subscription IDs in a segment?
  phrasing_ops: 7
  slug: beehiiv-segments-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Subscription Tags API from beehiiv — 1 operation(s) for subscription tags.
  name: beehiiv Subscription Tags API
  phrasing_intents:
  - id: create
    intent: Tag a subscriber
    question: How do I add tags to a subscriber?
  phrasing_ops: 1
  slug: beehiiv-subscription-tags-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Subscriptions API from beehiiv — 3 operation(s) for subscriptions.
  name: beehiiv Subscriptions API
  phrasing_intents:
  - id: create
    intent: Subscribe a new reader
    question: How do I add a new subscriber to my newsletter from my signup form?
  - id: index
    intent: List a publication's subscribers
    question: Who subscribes to my newsletter?
  - id: get-by-email
    intent: Look up a subscriber by email
    question: Is a given email address subscribed to my newsletter?
  - id: update-by-email
    intent: Update a subscriber found by email
    question: How do I change a subscriber's tier when I only know their email?
  - id: get-by-id
    intent: Get a subscriber by subscription ID
    question: Can I fetch one subscriber's details by their subscription ID?
  - id: put
    intent: Update a subscriber by ID (PUT)
    question: How do I PUT changes to a subscriber's tier or custom fields by subscription ID?
  - id: patch
    intent: Update a subscriber by ID (PATCH)
    question: Can I PATCH a subscriber's custom fields using their subscription ID?
  - id: delete
    intent: Permanently delete a subscriber
    question: How do I permanently delete a subscriber and all their data?
  phrasing_ops: 8
  slug: beehiiv-subscriptions-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The Tiers API from beehiiv — 2 operation(s) for tiers.
  name: beehiiv Tiers API
  phrasing_intents:
  - id: create
    intent: Create a subscription tier
    question: How do I add a new paid tier to my newsletter?
  - id: index
    intent: List a publication's subscription tiers
    question: What paid tiers does my newsletter offer?
  - id: show
    intent: Get one subscription tier
    question: What's included in a specific tier and what does it cost?
  - id: put
    intent: Update a subscription tier (PUT)
    question: How do I PUT a new name or description onto an existing tier?
  - id: patch
    intent: Update a subscription tier (PATCH)
    question: Can I PATCH just the description of an existing tier?
  phrasing_ops: 5
  slug: beehiiv-tiers-api
- baseURL: https://api.beehiiv.com/v2
  baseurl_source: declared
  description: The workspaces API from beehiiv — 3 operation(s) for workspaces.
  name: beehiiv Workspaces API
  phrasing_intents:
  - id: identify
    intent: Identify the workspace behind a token
    question: Which workspace is my API key or OAuth token tied to?
  - id: permissions
    intent: List the scopes granted to a token
    question: What permissions does my current token have in this workspace?
  - id: publications-by-subscription-email
    intent: Find publications an email subscribes to
    question: Which of my newsletters is a given email subscribed to?
  phrasing_ops: 3
  slug: beehiiv-workspaces-api
artifact_total: 97
asyncapis:
- description: 'AsyncAPI 2.6 description of the beehiiv outbound webhook surface. beehiiv posts JSON event payloads to a customer-configured endpoint URL when selected events occur on a publication. The set of event '
  name: beehiiv Webhooks
  slug: beehiiv-asyncapi
collections:
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities API
  slug: postman-beehiiv-subpackage-advertisement-opportunities-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_authors API
  slug: postman-beehiiv-subpackage-authors-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_automationJourneys API
  slug: postman-beehiiv-subpackage-automationjourneys-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_automations API
  slug: postman-beehiiv-subpackage-automations-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_bulk_subscriptions API
  slug: postman-beehiiv-subpackage-bulk-subscriptions-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_bulkSubscriptionUpdates API
  slug: postman-beehiiv-subpackage-bulksubscriptionupdates-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_conditionSets API
  slug: postman-beehiiv-subpackage-conditionsets-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_customFields API
  slug: postman-beehiiv-subpackage-customfields-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_dataDeletion API
  slug: postman-beehiiv-subpackage-datadeletion-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_engagements API
  slug: postman-beehiiv-subpackage-engagements-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_newsletterLists API
  slug: postman-beehiiv-subpackage-newsletterlists-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_newsletterListSubscriptions API
  slug: postman-beehiiv-subpackage-newsletterlistsubscriptions-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_oauth_users API
  slug: postman-beehiiv-subpackage-oauth-users-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_polls API
  slug: postman-beehiiv-subpackage-polls-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_posts API
  slug: postman-beehiiv-subpackage-posts-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_postTemplates API
  slug: postman-beehiiv-subpackage-posttemplates-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_publications API
  slug: postman-beehiiv-subpackage-publications-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_referralProgram API
  slug: postman-beehiiv-subpackage-referralprogram-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_segments API
  slug: postman-beehiiv-subpackage-segments-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_subscriptions API
  slug: postman-beehiiv-subpackage-subscriptions-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_subscriptionTags API
  slug: postman-beehiiv-subpackage-subscriptiontags-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_tiers API
  slug: postman-beehiiv-subpackage-tiers-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_webhooks API
  slug: postman-beehiiv-subpackage-webhooks-api
- collection_type: postman
  name: API Reference subpackage_advertisement_opportunities subpackage_workspaces API
  slug: postman-beehiiv-subpackage-workspaces-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities API
  slug: open-beehiiv-subpackage-advertisement-opportunities-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_authors API
  slug: open-beehiiv-subpackage-authors-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_automationJourneys API
  slug: open-beehiiv-subpackage-automationjourneys-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_automations API
  slug: open-beehiiv-subpackage-automations-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_bulk_subscriptions API
  slug: open-beehiiv-subpackage-bulk-subscriptions-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_bulkSubscriptionUpdates API
  slug: open-beehiiv-subpackage-bulksubscriptionupdates-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_conditionSets API
  slug: open-beehiiv-subpackage-conditionsets-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_customFields API
  slug: open-beehiiv-subpackage-customfields-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_dataDeletion API
  slug: open-beehiiv-subpackage-datadeletion-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_engagements API
  slug: open-beehiiv-subpackage-engagements-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_newsletterLists API
  slug: open-beehiiv-subpackage-newsletterlists-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_newsletterListSubscriptions API
  slug: open-beehiiv-subpackage-newsletterlistsubscriptions-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_oauth_users API
  slug: open-beehiiv-subpackage-oauth-users-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_polls API
  slug: open-beehiiv-subpackage-polls-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_posts API
  slug: open-beehiiv-subpackage-posts-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_postTemplates API
  slug: open-beehiiv-subpackage-posttemplates-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_publications API
  slug: open-beehiiv-subpackage-publications-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_referralProgram API
  slug: open-beehiiv-subpackage-referralprogram-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_segments API
  slug: open-beehiiv-subpackage-segments-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_subscriptions API
  slug: open-beehiiv-subpackage-subscriptions-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_subscriptionTags API
  slug: open-beehiiv-subpackage-subscriptiontags-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_tiers API
  slug: open-beehiiv-subpackage-tiers-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_webhooks API
  slug: open-beehiiv-subpackage-webhooks-api
- collection_type: open
  name: API Reference subpackage_advertisement_opportunities subpackage_workspaces API
  slug: open-beehiiv-subpackage-workspaces-api
- collection_type: open
  name: API Reference
  slug: open-beehiiv
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/capabilities/beehiiv-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/beehiiv-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/beehiiv/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/agentic-access/beehiiv-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/beehiiv-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/security/beehiiv-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/beehiiv-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/security/beehiiv-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beehiiv-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/authentication/beehiiv-authentication.yml
  title: ''
  type: Authentication
  url: authentication/beehiiv-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/beehiiv
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/beehiiv
- group: company
  title: ''
  type: Website
  url: https://www.beehiiv.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.beehiiv.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://developers.beehiiv.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.beehiiv.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.beehiiv.com/welcome/getting-started
- group: operate
  title: ''
  type: RateLimiting
  url: https://developers.beehiiv.com/welcome/rate-limiting
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/plans/beehiiv-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/beehiiv-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/rate-limits/beehiiv-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/beehiiv-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/finops/beehiiv-finops.yml
  title: ''
  type: FinOps
  url: finops/beehiiv-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/json-ld/beehiiv-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/beehiiv-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.beehiiv.com/llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.beehiiv.com/llms-full.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/mcp/beehiiv-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/beehiiv-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.beehiiv.com/mcp
- group: agent
  title: ''
  type: MCPServer
  url: https://developers.beehiiv.com/_mcp/server
- group: build
  title: ''
  type: SDKs
  url: https://github.com/beehiiv/typescript-sdk
- group: operate
  title: ''
  type: Support
  url: https://support.beehiiv.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.beehiiv.com/blog
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/packages/beehiiv-packages.yml
  title: ''
  type: Packages
  url: packages/beehiiv-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/well-known/beehiiv-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beehiiv-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/well-known/beehiiv-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/beehiiv-api-catalog.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/mcp/beehiiv-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/beehiiv-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/llms/beehiiv-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beehiiv-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/overlays/beehiiv-api-reference-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/beehiiv-api-reference-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/conformance/beehiiv-conformance.yml
  title: ''
  type: Conformance
  url: conformance/beehiiv-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/conformance/beehiiv-conformance.yml
  title: ''
  type: Compliance
  url: conformance/beehiiv-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/errors/beehiiv-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/beehiiv-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/lifecycle/beehiiv-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/beehiiv-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.beehiiv.com
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/lifecycle/beehiiv-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/beehiiv-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/scopes/beehiiv-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/beehiiv-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/conventions/beehiiv-conventions.yml
  title: ''
  type: Conventions
  url: conventions/beehiiv-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/changelog/beehiiv-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/beehiiv-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/data-model/beehiiv-data-model.yml
  title: ''
  type: DataModel
  url: data-model/beehiiv-data-model.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/asyncapi/beehiiv-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/beehiiv-asyncapi.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/openapi/_original/beehiiv-webhook-events-openapi.yml
  title: ''
  type: Webhooks
  url: openapi/_original/beehiiv-webhook-events-openapi.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.beehiiv.com/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/kinlaneapi/beehiiv/overview
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beehiiv.com/tou
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beehiiv.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.beehiiv.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.beehiiv.com/login
created: '2026-05-08'
description: beehiiv is a newsletter publishing platform offering email publishing, subscriber management, paid subscriptions, an ad network, referrals, polls, automations, segments, webhooks, and analytics for creators and media companies. Founded in 2021 by former Morning Brew operators and headquartered in New York City.
finops:
- name: Beehiiv Finops
  service_category: Newsletter Publishing
  slug: beehiiv-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/beehiiv.png
json_schemas:
- name: beehiiv Post
  property_count: 19
  slug: beehiiv-post
- name: beehiiv Subscription
  property_count: 16
  slug: beehiiv-subscription
jsonld:
- class_count: 0
  name: Beehiiv Context
  property_count: 6
  slug: beehiiv-context
layout: provider
mcp_servers:
- description: ''
  name: beehiiv MCP Server
  slug: beehiiv-mcp-server
- description: ''
  name: beehiiv MCP Server
  slug: beehiiv-mcp-server-2
- description: ''
  name: beehiiv MCP Server
  slug: beehiiv-mcp-server-3
modified: '2026-08-13'
name: beehiiv
nav: Providers
network: true
overview: 'beehiiv publishes 30 APIs on the [APIs.io](https://apis.io/) network, including Authorizations API, Tokens API, Webhooks API, and 27 more. Tagged areas include Newsletters, Creators, Email, Subscription, and Publishing.


  The beehiiv catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  beehiiv''s developer surface includes authentication, pricing, documentation, API reference, getting-started guide, support, engineering blog, and 44 more developer resources.'
plans:
- name: Beehiiv Plans Pricing
  plan_count: 4
  slug: beehiiv-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Beehiiv Rate Limits
  slug: beehiiv-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: beehiiv API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: beehiiv-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: beehiiv API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: beehiiv-jsonschema-spectral-rules
scopes:
- name: Beehiiv Scopes
  scope_count: 0
  slug: beehiiv-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 73.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 81.5
    catalog_earned_first_party: 20.0
    catalog_gap: 33.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 65.4
    developer_ergonomics: 72.0
    discoverability: 80.0
    operational_transparency: 63.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 73.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 54
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/beehiiv/refs/heads/main/screenshots/beehiiv-2026-06-20T173135.png
security:
- kind: authentication
  name: Beehiiv Authentication
  slug: beehiiv-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Beehiiv Domain Security
  slug: beehiiv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Beehiiv Trust Center
  slug: beehiiv-trust-center
  summary_line: SOC 2 Type I
slug: beehiiv
tags:
- Newsletters
- Creators
- Email
- Subscription
- Publishing
- Media
- Advertising
- Creator Economy
website: https://www.beehiiv.com/
---
