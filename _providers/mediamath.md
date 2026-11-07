---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
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
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: partial
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
- acting_count: 143
  human_in_the_loop: 0
  name: Mediamath Agentic Access
  operation_count: 363
  slug: mediamath-agentic-access
  summary_line: 363 operations · 143 acting
api_count: 10
apis:
- description: API for ingesting audience event data into the MediaMath Platform via real-time server-side pixel events and batch event uploads. Supports UUID, mobile advertising IDs, and CTV device IDs for cross-de
  name: MediaMath Audience Onboarding API
  slug: mediamath-audience-onboarding-api
- description: API for syncing audience segment data through server-to-server data distribution, supporting UUID-to-segment mappings, SFTP file transfer, and processing log access with Basic Authentication.
  name: MediaMath Server-to-Server Data Distribution API
  slug: mediamath-server-to-server-data-distribution-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Ad Servers
  name: MediaMath Ad Servers API
  phrasing_intents:
  - id: list-ad-servers
    intent: List ad servers
    question: Which third-party ad servers does MediaMath recognize?
  phrasing_ops: 1
  slug: mediamath-ad-servers-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Advertisers
  name: MediaMath Advertisers API
  phrasing_intents:
  - id: list-advertisers
    intent: List advertisers
    question: Which advertisers do I have access to in MediaMath?
  - id: create-advertiser
    intent: Create an advertiser
    question: How do I set up a new advertiser under my agency?
  - id: get-advertiser
    intent: Get an advertiser
    question: How do I look up one advertiser's details by ID?
  - id: update-advertiser
    intent: Update an advertiser
    question: How do I change an existing advertiser's settings?
  - id: advertiser-audit-log
    intent: View an advertiser's change history
    question: Who changed this advertiser and when?
  - id: list-advertisers-pixel-x-advertisers
    intent: List sibling advertisers sharing pixels
    question: Which sibling advertisers can share pixels when cross-advertiser pixels are enabled?
  - id: list-user-permissions-advertiser
    intent: List user permissions for an advertiser
    question: Which users have permission to access this advertiser?
  - id: advertiser-audit-log-bulk
    intent: View change history for several advertisers
    question: Can I pull the audit log for many advertisers in one request?
  phrasing_ops: 8
  slug: mediamath-advertisers-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Agencies
  name: MediaMath Agencies API
  phrasing_intents:
  - id: list-agencies
    intent: List agencies
    question: Which agencies exist under my MediaMath organizations?
  - id: create-agency
    intent: Create an agency
    question: How do I add a new agency?
  - id: get-agency
    intent: Get an agency
    question: What details are stored for a specific agency?
  - id: update-agency
    intent: Update an agency
    question: How do I edit an existing agency's details?
  - id: agency-audit-log
    intent: View an agency's change history
    question: Who changed this agency and when?
  - id: list-user-permissions-agency
    intent: List users with access to an agency
    question: Which users have permissions on a given agency?
  - id: agency-audit-log-bulk
    intent: View change history for several agencies
    question: Can I pull audit logs for multiple agencies at once?
  phrasing_ops: 7
  slug: mediamath-agencies-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Atomic Creatives
  name: MediaMath Atomic Creatives API
  phrasing_intents:
  - id: preview-creative-assets
    intent: Preview creative assets before upload
    question: Can I check my creative files and metadata before committing the upload?
  - id: upload-creative-assets
    intent: Upload creative assets
    question: How do I upload creative files so they become atomic creatives?
  - id: list-atomic-creatives
    intent: List atomic creatives
    question: Which display creatives exist in my MediaMath account?
  - id: post-atomic_creatives
    intent: Create an atomic creative
    question: How do I create a creative from an ad tag with a set width and height?
  - id: get-atomic-creative
    intent: Get an atomic creative
    question: What are the settings of a specific atomic creative?
  - id: post-atomic_creatives-atomic_creative_id
    intent: Update an atomic creative
    question: How do I change the click-through URL on an existing atomic creative?
  - id: atomic-creative-audit-log
    intent: View an atomic creative's change history
    question: Who edited this atomic creative and when?
  - id: atomic-creatives-healthcheck
    intent: Check atomic creatives' health
    question: Are my atomic creatives healthy and ready to serve?
  phrasing_ops: 9
  slug: mediamath-atomic-creatives-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Audience Vendors
  name: MediaMath Audience Vendors API
  phrasing_intents:
  - id: list-audience-vendors
    intent: List audience vendors
    question: Which third-party audience data vendors are available?
  - id: create-audience-vendor
    intent: Create an audience vendor
    question: How do I register a new audience data vendor?
  - id: get-audience-vendor
    intent: Get an audience vendor
    question: How do I look up one audience vendor by ID?
  - id: update-audience-vendor
    intent: Update an audience vendor
    question: How do I change an existing audience vendor's settings?
  phrasing_ops: 4
  slug: mediamath-audience-vendors-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Campaign Plans
  name: MediaMath Campaign Plans API
  phrasing_intents:
  - id: list-campaign-plans
    intent: List campaign plans
    question: Which campaign plans have been drafted so far?
  - id: create-campaign-plan
    intent: Create a campaign plan
    question: How do I draft a campaign plan with a budget and duration?
  - id: get-campaign-plan
    intent: Get a campaign plan
    question: How do I look up one campaign plan by ID?
  - id: update-campaign-plan
    intent: Update a campaign plan
    question: How do I change the budget or duration of an existing campaign plan?
  phrasing_ops: 4
  slug: mediamath-campaign-plans-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Campaigns
  name: MediaMath Campaigns API
  phrasing_intents:
  - id: bulk-update-campaigns
    intent: Update many campaigns at once
    question: Can I change settings on several campaigns in a single request?
  - id: get-campaign
    intent: Get a campaign
    question: What are the budget, goals and status of a specific campaign?
  - id: update-campaign
    intent: Update a campaign
    question: How can I change an existing campaign's budget or pacing?
  - id: list-campaigns
    intent: List campaigns
    question: Which campaigns are currently live?
  - id: create-campaign
    intent: Create a campaign
    question: How do I launch a new campaign for an advertiser?
  - id: campaign-audit-log
    intent: View a campaign's change history
    question: Who changed this campaign and when?
  - id: update-dba-single-legacy
    intent: Update a campaign's dynamic budget allocation (legacy)
    question: Can I toggle dynamic budget allocation on one campaign with the legacy endpoint?
  - id: copy-campaign
    intent: Copy a campaign
    question: Can I duplicate an existing campaign with new dates?
  phrasing_ops: 11
  slug: mediamath-campaigns-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Campaigns Budget Flights
  name: MediaMath Campaigns Budget Flights API
  phrasing_intents:
  - id: bulk-update-budget-flights
    intent: Update many budget flights at once
    question: Can I change several campaign budget flights in one request?
  - id: list-budget-flights
    intent: List a campaign's budget flights
    question: What budget flights are scheduled for a campaign?
  - id: campaign-budget-flights-audit-log
    intent: View budget flight change history
    question: Who changed a campaign's budget flights and when?
  phrasing_ops: 3
  slug: mediamath-campaigns-budget-flights-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Concepts
  name: MediaMath Concepts API
  phrasing_intents:
  - id: list-concepts
    intent: List creative concepts
    question: Which creative concepts does my account have?
  - id: create-concept
    intent: Create a creative concept
    question: How do I create a concept to group creatives for an advertiser?
  - id: get-concept
    intent: Get a creative concept
    question: What are the details of one concept?
  - id: update-concept
    intent: Update a creative concept
    question: Can I rename or archive an existing concept?
  - id: concepts-audit-log
    intent: View a concept's change history
    question: Who changed this concept and when?
  - id: bulk-update-concepts
    intent: Update many concepts at once
    question: Can I update several concepts in one request?
  phrasing_ops: 6
  slug: mediamath-concepts-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Contracts
  name: MediaMath Contracts API
  phrasing_intents:
  - id: create-contract
    intent: Create a contract
    question: How do I set up a fee contract for an organization?
  - id: list-contracts
    intent: List contracts
    question: Which platform contracts are on file in MediaMath?
  - id: update-contract
    intent: Update a contract
    question: How do I change the end date on an existing contract?
  - id: get-contract
    intent: Get a contract
    question: What fees and dates are on a specific contract?
  - id: contract-audit-log
    intent: View a contract's change history
    question: Who changed this contract and when?
  phrasing_ops: 5
  slug: mediamath-contracts-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Creatives
  name: MediaMath Creatives API
  phrasing_intents:
  - id: get-creative
    intent: Get a creative
    question: What are the details of a specific creative?
  phrasing_ops: 1
  slug: mediamath-creatives-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Currency Rates
  name: MediaMath Currency Rates API
  phrasing_intents:
  - id: list-currency-rates
    intent: List currency exchange rates
    question: What exchange rates does MediaMath use for currency conversion?
  phrasing_ops: 1
  slug: mediamath-currency-rates-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: The Datasets API from MediaMath — 10 operation(s) for datasets.
  name: MediaMath Datasets API
  phrasing_intents:
  - id: postAllDimensionsAndMetrics
    intent: Report performance across the widest set of dimensions
    question: Which report lets me break campaign spend and results out by the widest range of dimensions?
  - id: postBrainFeatureSummary
    intent: Summarize which Brain features drive a model
    question: Which features does the bidding Brain rank as most important for my campaign's model goal?
  - id: postBrainFeatureValue
    intent: Report bid impact of individual Brain feature values
    question: How much bid impact does each individual feature value have in the Brain model?
  - id: postDayPart
    intent: Report performance by time of day and day of week
    question: What hours of the day and days of the week does my campaign perform best?
  - id: postDeals
    intent: Report private marketplace deal delivery
    question: How many biddable opportunities on my private marketplace deals turned into won impressions?
  - id: postPerformance
    intent: Report aggregated daily campaign performance
    question: How is my campaign performing to date in campaign currency?
  - id: postPerformanceHourly
    intent: Report campaign performance by hour
    question: How did my campaign perform hour by hour over the last few hours?
  - id: postPixelLoads
    intent: Report pixel loads and uniques by referrer
    question: How many times did my event and data pixels fire, and for how many unique users?
  phrasing_ops: 10
  slug: mediamath-datasets-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Enterprise Controls
  name: MediaMath Enterprise Controls API
  phrasing_intents:
  - id: list-entity-groups
    intent: List entity groups
    question: Which enterprise entity groups are set up?
  - id: get-entity-group
    intent: Get an entity group
    question: What does a particular entity group contain?
  - id: get-entity-group-controls-entity-type
    intent: Get an entity group's controls by type
    question: What enterprise controls apply to campaigns in an entity group?
  - id: entity-group-audit-log
    intent: View an entity group's change history
    question: Who changed this entity group's controls?
  phrasing_ops: 4
  slug: mediamath-enterprise-controls-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: General
  name: MediaMath General API
  phrasing_intents:
  - id: healthcheck
    intent: Check API availability
    question: Is the MediaMath API up right now?
  - id: list-roles
    intent: List user roles
    question: What user roles exist on the platform?
  - id: search-entities
    intent: Search organizations, agencies and advertisers by name
    question: How do I find an advertiser or agency when I only know part of its name?
  - id: list-target-values
    intent: List targeting values
    question: What targeting values are available to use on strategies?
  phrasing_ops: 4
  slug: mediamath-general-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Marketplaces
  name: MediaMath Marketplaces API
  phrasing_intents:
  - id: get-marketplace
    intent: Get a marketplace
    question: What are the settings of a specific marketplace?
  - id: update-marketplace
    intent: Update a marketplace
    question: How do I change the sell price on an existing marketplace?
  - id: list-marketplaces
    intent: List marketplaces
    question: Which marketplaces are available in MediaMath?
  - id: create-marketplace
    intent: Create a marketplace
    question: How do I set up a new marketplace?
  phrasing_ops: 4
  slug: mediamath-marketplaces-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: The New Strategy Groups API from MediaMath — 3 operation(s) for new strategy groups.
  name: MediaMath New Strategy Groups API
  phrasing_intents:
  - id: list-new-strategy-groups
    intent: List a campaign's strategy groups
    question: Which strategy groups exist in a campaign?
  - id: create-new-strategy-group
    intent: Create a strategy group
    question: How do I group strategies inside a campaign?
  - id: get-new-strategy-group
    intent: Get a strategy group
    question: What are the caps and settings on a specific strategy group?
  - id: update-new-strategy-group
    intent: Update a strategy group
    question: How do I change the spend cap on an existing strategy group?
  - id: delete-new-strategy-group
    intent: Delete a strategy group
    question: What happens to strategies when I delete their strategy group?
  - id: new-strategy-group-audit-log
    intent: View a strategy group's change history
    question: Who changed this strategy group and when?
  phrasing_ops: 6
  slug: mediamath-new-strategy-groups-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: New Strategy Plans
  name: MediaMath New Strategy Plans API
  phrasing_intents:
  - id: post-ephemeral-new-strategy-plan
    intent: Forecast a strategy plan without saving it
    question: Can I run a forecast on a strategy plan without saving the plan?
  - id: run-and-update-forecast
    intent: Rerun and save the forecast for a strategy plan
    question: How do I refresh the stored forecast for a saved strategy plan?
  - id: get-new-strategy-plan
    intent: Get a new strategy plan
    question: How do I look up a single new strategy plan by ID?
  - id: update-new-strategy-plan
    intent: Update a new strategy plan
    question: How do I change the channels on a saved strategy plan?
  - id: delete-new-strategy-plan
    intent: Delete a new strategy plan
    question: How do I delete a strategy plan I no longer need?
  - id: list-new-strategy-plans
    intent: List new strategy plans
    question: Which strategy plans exist for one of my advertisers?
  - id: create-new-strategy-plan
    intent: Create and save a new strategy plan
    question: How do I save a new strategy plan inside a campaign plan?
  - id: list-new-strategy-plan-target-values
    intent: List target values for strategy plans
    question: Which targeting values can I use when building a strategy plan?
  phrasing_ops: 8
  slug: mediamath-new-strategy-plans-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Organizations
  name: MediaMath Organizations API
  phrasing_intents:
  - id: list-organizations
    intent: List organizations
    question: Which organizations can I access in MediaMath?
  - id: create-organization
    intent: Create an organization
    question: How do I set up a new organization?
  - id: get-organization
    intent: Get an organization
    question: What details are stored for a specific organization?
  - id: update-organization
    intent: Update an organization
    question: How do I edit an organization's details?
  - id: organization-audit-log
    intent: View an organization's change history
    question: Who changed this organization and when?
  - id: organization-audit-log-bulk
    intent: View change history for several organizations
    question: Can I pull audit logs for multiple organizations at once?
  - id: list-user-permissions-organization
    intent: List users with access to an organization
    question: Which users have permissions on a given organization?
  - id: list-settings-organization
    intent: List an organization's settings
    question: What settings are configured for my organization?
  phrasing_ops: 9
  slug: mediamath-organizations-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Pixel Bundles
  name: MediaMath Pixel Bundles API
  phrasing_intents:
  - id: create-pixel-bundle
    intent: Create a pixel bundle
    question: How do I create a new event pixel for an advertiser?
  - id: list-pixel-bundles
    intent: List pixel bundles
    question: Which conversion and data pixels are set up in MediaMath?
  - id: update-pixel-bundle
    intent: Update a pixel bundle
    question: How do I rename or deactivate an existing pixel?
  - id: get-pixel-bundle
    intent: Get a pixel bundle
    question: What are the settings on a specific pixel?
  - id: pixel-bundle-audit-log
    intent: View a pixel bundle's change history
    question: Who changed this pixel and when?
  phrasing_ops: 5
  slug: mediamath-pixel-bundles-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Pixel Providers
  name: MediaMath Pixel Providers API
  phrasing_intents:
  - id: list-pixel-providers
    intent: List pixel providers
    question: Which pixel providers are available for tracking pixels?
  phrasing_ops: 1
  slug: mediamath-pixel-providers-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Segment Groups
  name: MediaMath Segment Groups API
  phrasing_intents:
  - id: create-segment-group
    intent: Create a segment group
    question: How do I bundle segments into a new segment group?
  - id: list-segment-groups
    intent: List segment groups
    question: Which segment groups exist in my organization?
  - id: update-segment-group
    intent: Update a segment group
    question: Can I rename a segment group or change its subgroups?
  - id: get-segment-group
    intent: Get a segment group
    question: What segments make up a particular segment group?
  - id: segment-groups-audit-log
    intent: View a segment group's change history
    question: Who modified this segment group?
  - id: get-segment-group-assignments
    intent: List where a segment group is assigned
    question: Which strategies or entities use a given segment group?
  phrasing_ops: 6
  slug: mediamath-segment-groups-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Site Lists
  name: MediaMath Site Lists API
  phrasing_intents:
  - id: list-site-lists
    intent: List site lists
    question: Which site lists exist in my organization?
  - id: get-site-list
    intent: Get a site list
    question: How do I look up one site list's details by ID?
  - id: upload-create-site-lists
    intent: Upload a file as a new site list
    question: How do I create a site list by uploading a file of domains?
  - id: upload-update-site-lists
    intent: Replace a site list's contents by upload
    question: How do I upload a new file to replace the sites in an existing list?
  - id: download-site-lists
    intent: Download a site list as CSV
    question: How do I export the sites in a site list to CSV?
  - id: get-site-list-assignments
    intent: List where a site list is assigned
    question: What entities is this site list currently assigned to?
  phrasing_ops: 6
  slug: mediamath-site-lists-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Strategies
  name: MediaMath Strategies API
  phrasing_intents:
  - id: create-strategy
    intent: Create a strategy in a campaign
    question: How do I add a new strategy to a campaign with goals and pacing?
  - id: list-strategies
    intent: List strategies
    question: Which strategies are running across my MediaMath campaigns?
  - id: update-strategy
    intent: Update a strategy's targeting
    question: How do I change the targeting on an existing strategy?
  - id: get-strategy
    intent: Get a strategy
    question: What are the settings of a specific strategy?
  - id: post-copy-strategy
    intent: Copy a strategy
    question: Can I duplicate a strategy under a new name?
  - id: get-strategy-healthcheck
    intent: Check a strategy's health
    question: Is my strategy healthy and able to bid?
  - id: get-strategy-friendly-names
    intent: Get readable names for a strategy's targeting
    question: What do the targeting IDs on my strategy actually mean in plain names?
  - id: get-strategy-forecast-query
    intent: Get a strategy's forecast query
    question: What forecast query is generated for a strategy?
  phrasing_ops: 13
  slug: mediamath-strategies-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Strategy Parameters
  name: MediaMath Strategy Parameters API
  phrasing_intents:
  - id: list-strategy-deals
    intent: List deals attached to strategies
    question: Which private deals are assigned to my strategies?
  - id: list-strategy-day-parts
    intent: List strategy day parts
    question: What days and hours are my strategies scheduled to bid?
  - id: list-strategy-groups
    intent: List strategy groups
    question: What strategy groups exist for a campaign?
  - id: list-strategy-ip-addresses
    intent: List strategy IP address targets
    question: Which IP addresses or CIDR ranges are my strategies targeting?
  - id: download-strategy-ip-addresses
    intent: Download a strategy's IP addresses as CSV
    question: Can I export the IP addresses targeted by one strategy to a CSV file?
  - id: list-strategy-concepts
    intent: List concepts assigned to strategies
    question: Which creative concepts are attached to my strategies?
  - id: list-strategy-target-values
    intent: List strategy target values
    question: What target values are applied to my strategies?
  - id: list-strategy-postal-codes
    intent: List strategy postal code targets
    question: Which postal codes are my strategies including or excluding?
  phrasing_ops: 9
  slug: mediamath-strategy-parameters-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Strategy Templates
  name: MediaMath Strategy Templates API
  phrasing_intents:
  - id: create-strategy-template
    intent: Create a strategy template
    question: How do I save a reusable strategy template?
  - id: list-strategy-template
    intent: List strategy templates
    question: Which strategy templates are available to my advertiser?
  - id: update-strategy-template
    intent: Update a strategy template
    question: Can I change the settings stored in an existing strategy template?
  - id: get-strategy-template
    intent: Get a strategy template
    question: What settings does a particular strategy template contain?
  - id: delete-strategy-template
    intent: Delete a strategy template
    question: How do I remove a strategy template I no longer use?
  phrasing_ops: 5
  slug: mediamath-strategy-templates-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Supply Sources
  name: MediaMath Supply Sources API
  phrasing_intents:
  - id: list-supply-sources
    intent: List supply sources
    question: Which exchanges and supply sources can I buy from?
  - id: get-supply-source
    intent: Get a supply source
    question: What are the details of a specific supply source?
  phrasing_ops: 2
  slug: mediamath-supply-sources-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Targeting
  name: MediaMath Targeting API
  phrasing_intents:
  - id: list-targets-legacy
    intent: List targets via the legacy endpoint
    question: Is there an older singular /target endpoint for listing targets in MediaMath?
  - id: create-target-legacy
    intent: Create a target via the legacy endpoint
    question: Can I create a new target through the old singular /target path?
  - id: get-target-legacy
    intent: Get a target via the legacy endpoint
    question: How can I fetch one target by ID from the legacy /target path?
  - id: update-target-legacy
    intent: Update a target via the legacy POST endpoint
    question: Is there a POST-based legacy call to update a target on the singular /target path?
  - id: delete-target-legacy
    intent: Delete a target via the legacy endpoint
    question: Can I remove a target through the old singular /target delete call?
  - id: put-update-target-legacy
    intent: Replace a target via the legacy PUT endpoint
    question: Can I update a target with an HTTP PUT on the legacy /target path?
  - id: list-targets
    intent: List targets
    question: Which targets are available in my MediaMath account?
  - id: create-target
    intent: Create a target
    question: How do I add a new target value to the current targets collection?
  phrasing_ops: 20
  slug: mediamath-targeting-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: TargetingAttachments
  name: MediaMath Targeting Attachments API
  phrasing_intents:
  - id: list-attachments
    intent: List targeting attachments
    question: Which targeting attachments are on a given strategy?
  - id: create-attachment
    intent: Attach a target to a strategy
    question: How do I attach a targeting value to a strategy?
  - id: list-attachments-legacy
    intent: List attachments via the legacy endpoint
    question: Is there an older endpoint that still lists targeting attachments?
  - id: create-attachment-legacy
    intent: Attach a target via the legacy endpoint
    question: Can I still create a targeting attachment through the legacy endpoint?
  - id: get-attachment
    intent: Get a targeting attachment
    question: How do I look up one targeting attachment by its ID?
  - id: update-attachment
    intent: Update a targeting attachment
    question: Can I change the restriction or operator on an existing attachment?
  - id: delete-attachment
    intent: Delete a targeting attachment
    question: How do I remove a targeting attachment from a strategy?
  - id: get-attachment-legacy
    intent: Get an attachment via the legacy endpoint
    question: Can I fetch a single attachment from the legacy singular path?
  phrasing_ops: 10
  slug: mediamath-targeting-attachments-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Targeting Segment Objectives
  name: MediaMath Targeting Segment Objectives API
  phrasing_intents:
  - id: list-targeting-segment-objectives
    intent: List targeting segment objectives
    question: What objectives can targeting segments be tied to?
  - id: get-targeting-segment-objective
    intent: Get a targeting segment objective
    question: What does a specific targeting segment objective mean?
  phrasing_ops: 2
  slug: mediamath-targeting-segment-objectives-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Targeting Segments
  name: MediaMath Targeting Segments API
  phrasing_intents:
  - id: list-targeting-segments
    intent: List targeting segments
    question: Which audience targeting segments can I use?
  phrasing_ops: 1
  slug: mediamath-targeting-segments-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Timezones
  name: MediaMath Timezones API
  phrasing_intents:
  - id: list-timezones
    intent: List supported timezones
    question: Which timezones can I choose for campaigns?
  phrasing_ops: 1
  slug: mediamath-timezones-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: User Permissions
  name: MediaMath User Permissions API
  phrasing_intents:
  - id: update-permissions-user
    intent: Update a user's permissions
    question: How do I grant a user access to more advertisers or campaigns?
  - id: list-user-permissions
    intent: List a user's permissions
    question: What can a given user access across organizations, agencies and campaigns?
  - id: list-user-permissions-filtered
    intent: Check a user's permissions on specific entities
    question: Does this user have access to a particular set of campaigns and strategies?
  - id: list-user-permissions-organizations
    intent: List a user's organization permissions
    question: Which organizations does a user have access to?
  - id: list-user-permissions-agencies
    intent: List a user's agency permissions
    question: Which agencies is a user permitted to work with?
  - id: list-user-permissions-advertisers
    intent: List a user's advertiser permissions
    question: Which advertisers can this user manage?
  - id: list-user-permissions-campaigns
    intent: List a user's campaign permissions
    question: Which campaigns does a particular user have access to?
  - id: list-user-permissions-strategies
    intent: List a user's strategy permissions
    question: Which strategies is a user allowed to edit or view?
  phrasing_ops: 10
  slug: mediamath-user-permissions-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Users
  name: MediaMath Users API
  phrasing_intents:
  - id: list-users
    intent: List users
    question: Who are the users in my MediaMath account?
  - id: create-user
    intent: Create a user
    question: How do I add a new user?
  - id: get-user
    intent: Get a user
    question: What details are stored for a specific user?
  - id: update-user
    intent: Update a user
    question: How do I edit an existing user's profile?
  - id: user-audit-log
    intent: View a user's change history
    question: Who changed this user's record and when?
  - id: get-user-settings
    intent: Get a user's settings
    question: What settings are configured for a given user?
  - id: update-user-settings
    intent: Update a user's settings
    question: How do I change a user's settings?
  phrasing_ops: 7
  slug: mediamath-users-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Vendor Contracts
  name: MediaMath Vendor Contracts API
  phrasing_intents:
  - id: list-vendor-contracts
    intent: List vendor contracts
    question: Which vendor contracts are in place on my account?
  phrasing_ops: 1
  slug: mediamath-vendor-contracts-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Vendors
  name: MediaMath Vendors API
  phrasing_intents:
  - id: list-vendors
    intent: List vendors
    question: Which ad tech vendors are registered on the platform?
  - id: get-vendor
    intent: Get a vendor
    question: How do I look up one vendor by its ID?
  phrasing_ops: 2
  slug: mediamath-vendors-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Verticals
  name: MediaMath Verticals API
  phrasing_intents:
  - id: list-verticals
    intent: List verticals
    question: What advertiser verticals are available?
  phrasing_ops: 1
  slug: mediamath-verticals-api
- baseURL: https://api.mediamath.com
  baseurl_source: declared
  description: Component Creatives API (v3.0) for building and managing modular, component-based creatives in the MediaMath Platform — assembling creative components into dynamic ad units, managing component metadat
  name: MediaMath Component Creatives API
  phrasing_intents:
  - id: List-creatives
    intent: List component creatives (deprecated v1.0)
    question: Can I still list creatives with the deprecated component creatives v1.0 API?
  - id: Create-a-new-creative
    intent: Create a component creative (deprecated v1.0)
    question: Is there a legacy v1.0 call to create a new component creative?
  - id: Get-group-version-info
    intent: Get component creatives version info
    question: Which version of the component creatives service am I talking to?
  - id: List-Creative-Approvals
    intent: List creative approvals (deprecated v1.0)
    question: Where can I see v1.0 approval records for specific atomic creatives?
  - id: Post-an-Image-or-Subtitle-Asset
    intent: Upload a base64 image or subtitle asset
    question: Can I upload a base64-encoded image or subtitle file as a creative asset?
  - id: Get-details-about-a-creatives-eligibility
    intent: Get a creative's eligibility (deprecated v1.0)
    question: Is a given creative eligible to serve, according to the v1.0 API?
  - id: Get-details-of-a-creative
    intent: Get a component creative (deprecated v1.0)
    question: Can I fetch one component creative's details with the v1.0 API?
  - id: Update-creatives-details
    intent: Update a component creative (deprecated v1.0)
    question: Will updating a creative's assets in v1.0 replace its existing assets?
  phrasing_ops: 17
  slug: mediamath-component-creatives-api
- baseURL: https://api.mediamath.com/deals/v1.0
  baseurl_source: declared
  description: v3.0 creative approval status endpoints.
  name: MediaMath Approvals API
  phrasing_intents:
  - id: v3-get-approvals-status
    intent: Get approval status for creatives
    question: Have my creatives been approved to run?
  phrasing_ops: 1
  slug: mediamath-approvals-api
- baseURL: https://api.mediamath.com/deals/v1.0
  baseurl_source: declared
  description: BYOA (Bring Your Own Algorithm) allows advertisers to apply their own bidding algorithms within MediaMath. The participating campaigns and strategies are configured with the BYOA Campaign Settings
  name: MediaMath Campaign Settings API
  phrasing_intents:
  - id: GET_campaign_settings-campaign_id-strategies-strategy_id
    intent: Get a strategy's BYOA campaign settings
    question: What BYOA settings apply to one strategy within a campaign?
  - id: DELETE_campaign_settings-campaign_id-strategies-strategy_id
    intent: Remove a strategy's BYOA settings
    question: Can I remove BYOA settings from just one strategy?
  - id: PUT_campaign_settings-campaign_id-strategies-strategy_id
    intent: Configure BYOA for a strategy
    question: How do I turn on bring-your-own-algorithm for a single strategy?
  - id: DELETE_campaign_settings-campaign_id
    intent: Remove a campaign's BYOA settings
    question: Can I delete the BYOA configuration for a whole campaign?
  - id: PUT_campaign_settings-campaign_id
    intent: Configure BYOA for a campaign
    question: How do I enable bring-your-own-algorithm across an entire campaign?
  - id: GET_campaign_settings-campaign_id
    intent: Get a campaign's BYOA settings
    question: What BYOA settings are configured for a whole campaign?
  phrasing_ops: 6
  slug: mediamath-campaign-settings-api
- baseURL: https://api.mediamath.com/deals/v1.0
  baseurl_source: declared
  description: '{% admonition type="danger" name="This API is deprecated and will be removed in July 2026" %} Please migrate to the **Classification API v3.0** documented below. {% /admonition %} {% admonition type="'
  name: MediaMath Classification (V1.0 - Deprecated) API
  phrasing_intents:
  - id: GET_classification-v1-0-creative_id-inflate
    intent: Get a creative's classification with full labels
    question: How do I see a creative's classification with names expanded instead of just IDs?
  - id: GET_classification-v1-0-bulk-creative_ids-inflate
    intent: Get inflated classifications for several creatives
    question: Can I fetch expanded classifications for a batch of creatives at once?
  - id: GET_classification-v1-0-bulk-creative_ids
    intent: Get classifications for several creatives
    question: How do I retrieve the classification records of a group of creatives together?
  - id: POST_classification-v1-0-bulk
    intent: Bulk update creative classifications
    question: How do I update the classification of many creatives in one request?
  - id: POST_classification-v1-0-creative_id
    intent: Update a creative's classification
    question: How do I change the classification of a single creative?
  - id: GET_classification-v1-0-creative_id
    intent: Get a creative's classification
    question: What IAB classification is set on one of my creatives?
  phrasing_ops: 6
  slug: mediamath-classification-v1-0-deprecated-api
- baseURL: https://api.mediamath.com/deals/v1.0
  baseurl_source: declared
  description: V3.0 creative classification endpoints. Uses Bearer (JWT) authentication.
  name: MediaMath Classification (V3) API
  phrasing_intents:
  - id: GET_v3-0-classification-cid
    intent: Get a creative's classification
    question: How is a creative classified by language and vertical?
  - id: POST_v3-0-classification-cid
    intent: Save a creative's classification
    question: Can I set the language and verticals for a creative?
  - id: POST_v3-0-classification-cid-force-publish
    intent: Force-publish a creative's classification
    question: Can I push a creative's classification live immediately?
  - id: GET_v3-0-classification-cid-inflate
    intent: Get a creative's inflated classification
    question: Can I get a creative's classification with names expanded instead of IDs?
  - id: POST_v3-0-classification-bulk
    intent: Save classifications for many creatives
    question: Can I classify a batch of creatives in one request?
  - id: GET_v3-0-classification-bulk-cids
    intent: Get classifications for several creatives
    question: Can I fetch classifications for a comma-separated list of creatives?
  - id: GET_v3-0-classification-bulk-cids-inflate
    intent: Get inflated classifications for several creatives
    question: Can I get expanded classifications for many creatives in one call?
  phrasing_ops: 7
  slug: mediamath-classification-v3-api
- baseURL: https://api.mediamath.com/deals/v1.0
  baseurl_source: declared
  description: v3.0 component definition endpoints.
  name: MediaMath Components API
  phrasing_intents:
  - id: v3-list-all-components
    intent: List native creative components
    question: Which components can native creatives be built from?
  - id: v3-create-component
    intent: Create a creative component
    question: How do I define a new native creative component with a character limit?
  - id: v3-get-component-by-id
    intent: Get a creative component
    question: What are the settings of a specific component?
  - id: v3-update-component
    intent: Update a creative component
    question: Can I change a component's character limit or disable it?
  phrasing_ops: 4
  slug: mediamath-components-api
- baseURL: https://api.mediamath.com/deals/v1.0
  baseurl_source: declared
  description: _
  name: MediaMath Consumer Management API
  phrasing_intents:
  - id: list-accessible-customers
    intent: List my opportunity firehose consumers
    question: Which opportunity firehose consumers do I have access to?
  - id: list-filters-channel-types
    intent: Get one filter type's values for a consumer
    question: What values are set for a single filter type, like channel type, on my consumer?
  - id: Update-filters-channel-types
    intent: Update one filter type's values for a consumer
    question: How do I change the values of one specific filter type on my firehose consumer?
  - id: get-filter-list-per-consumer
    intent: See which filters I can change myself
    question: Which firehose filters and parameters am I allowed to update without contacting MediaMath?
  - id: List-consumers-active-filters
    intent: List all active filters on a consumer
    question: What filters are currently applied to my firehose consumer?
  - id: Get-consumer-statuses
    intent: Get a consumer's sample rate and enabled status
    question: Is my firehose consumer enabled, and what sample rate is it using?
  - id: Set-consumer-statuses
    intent: Set a consumer's sample rate or disable it
    question: How do I lower the sample rate on my opportunity firehose consumer?
  - id: Get-consumer-details
    intent: Get a consumer's full configuration
    question: How do I see the complete configuration of a firehose consumer?
  phrasing_ops: 13
  slug: mediamath-consumer-management-api
- baseURL: https://api.mediamath.com/deals/v1.0
  baseurl_source: declared
  description: v3.0 component (native) creative endpoints.
  name: MediaMath Creatives - Native API
  phrasing_intents:
  - id: v3-list-component-creatives
    intent: List native component creatives
    question: Which native component creatives does an advertiser have?
  - id: v3-create-component-creative
    intent: Create a native component creative
    question: How do I build a native ad from a title, body, image and brand name?
  - id: v3-get-component-creative-by-id
    intent: Get a native component creative
    question: What assets make up a specific component creative?
  - id: v3-update-component-creative
    intent: Update a native component creative
    question: If I send new assets to a component creative, are the old ones replaced?
  - id: v3-get-creative-eligibility
    intent: Check where a native creative can run
    question: Which placements is my native creative eligible for?
  phrasing_ops: 5
  slug: mediamath-creatives-native-api
- baseURL: https://api.mediamath.com/deals/v1.0
  baseurl_source: declared
  description: Custom Bid Router further extends the BYOA architecture allowing advertisers to apply their own bidding algorithms in their own ecosystem. The MediaMath system will invoke an external call to the clie
  name: MediaMath Custom Bid Router API
  phrasing_intents:
  - id: summary-bidvaluator-organization
    intent: Get custom bid router configuration summary
    question: Have I configured custom bid router endpoints for every region?
  - id: GET-executor-details
    intent: Get a custom bid router executor
    question: What endpoints are attached to a specific bid router executor?
  - id: PATCH-executor-details
    intent: Change an executor's sample rate
    question: How do I control what share of bid opportunities reach my endpoints?
  phrasing_ops: 3
  slug: mediamath-custom-bid-router-api
- baseURL: https://api.mediamath.com/deals/v1.0
  baseurl_source: declared
  description: In Customized Brain, the client uses the BYOA API to upload a set of logistic coefficients corresponding to any of the variables currently in use by the MediaMath Brain. These coefficients will then b
  name: MediaMath Custom Brain API
  phrasing_intents:
  - id: DELETE_data-namespace-models-model_id
    intent: Delete a custom brain model
    question: Can I delete a custom brain model I uploaded?
  - id: GET_data-namespace-models-model_id
    intent: Get a custom brain model
    question: What data is stored for a custom brain model?
  - id: PUT_data-namespace-models-model_id
    intent: Upload custom brain model data
    question: How do I upload data for my own custom brain model?
  - id: GET_data-decode-namespace-models-model_id
    intent: Get a decoded custom brain model
    question: Can I see a custom brain model's data in decoded, readable form?
  - id: GET_data-namespace
    intent: List all models in a namespace
    question: Which custom brain models live in a namespace?
  phrasing_ops: 5
  slug: mediamath-custom-brain-api
- baseURL: https://api.mediamath.com/deals/v1.0
  baseurl_source: declared
  description: _
  name: MediaMath Data Retrieval API
  phrasing_intents:
  - id: GET_report
    intent: Retrieve data from any report
    question: How do I pull rows from a named report with chosen dimensions and metrics?
  - id: GET_report-validate
    intent: Validate a report data request
    question: Can I check that a report query is valid before actually fetching the data?
  phrasing_ops: 2
  slug: mediamath-data-retrieval-api
- baseURL: https://api.mediamath.com/deals/v1.0
  baseurl_source: declared
  description: V3.0 IAB data endpoints. A single pair of endpoints serves all categories (`iab_verticals`, `iab_attributes`, `language`). Uses Bearer (JWT) authentication.
  name: MediaMath IAB Data (V3) API
  phrasing_intents:
  - id: GET_v3-0-static_data-category
    intent: Get IAB reference data for a category
    question: What IAB verticals are available for targeting?
  - id: GET_v3-0-static_data-category-id
    intent: Get one IAB reference data item
    question: What does a specific IAB vertical ID refer to?
  phrasing_ops: 2
  slug: mediamath-iab-data-v3-api
- baseURL: https://api.mediamath.com/deals/v1.0
  baseurl_source: declared
  description: '{% admonition type="danger" name="This API is deprecated and will be removed in July 2026" %} Please migrate to the **IAB Data API v3.0** (`GET /v3.0/static_data/{category}`) documented below. {% /adm'
  name: MediaMath IAB (V1.0 - Deprecated) API
  phrasing_intents:
  - id: GET_static_data-v1-0-iab_attributes
    intent: List IAB creative attributes
    question: What IAB creative attributes can I tag a creative with?
  - id: GET_static_data-v1-0-language-language_id
    intent: Get an IAB language
    question: How do I look up one language by its IAB language ID?
  - id: GET_static_data-v1-0-iab_verticals
    intent: List IAB verticals
    question: What IAB content verticals are available for classification?
  - id: GET_static_data-v1-0-iab_verticals-vertical_id
    intent: Get an IAB vertical
    question: How do I look up a single IAB vertical by ID?
  - id: GET_static_data-v1-0-language
    intent: List IAB languages
    question: Which languages can I assign to a creative?
  - id: Get-IAB-Attribute
    intent: Get an IAB attribute
    question: How do I look up a single IAB attribute by its ID?
  phrasing_ops: 6
  slug: mediamath-iab-v1-0-deprecated-api
- baseURL: https://api.mediamath.com/deals/v1.0
  baseurl_source: declared
  description: _
  name: MediaMath Metadata API
  phrasing_intents:
  - id: GET_meta
    intent: List available reports
    question: Which reports does the reporting API currently support?
  - id: GET_report-meta
    intent: Describe a report's dimensions and metrics
    question: What dimensions and metrics does a specific report support?
  phrasing_ops: 2
  slug: mediamath-metadata-api
- baseURL: https://api.mediamath.com/deals/v1.0
  baseurl_source: declared
  description: _
  name: MediaMath Permission Taxonomies API
  phrasing_intents:
  - id: POST_audience_segments
    intent: Create a permission taxonomy
    question: How do I publish a new audience segment taxonomy with permissions as a data vendor?
  - id: GET_audience_segments
    intent: List my permission taxonomies
    question: Which permission taxonomies have I published as a data provider?
  - id: GET_audience_segments-grants-$vendor_org_id
    intent: List entities granted to my data vendor
    question: Which organizations, agencies or advertisers can I grant my data to?
  - id: GET_audience_segments-taxonomy_id
    intent: Get a permission taxonomy
    question: How do I review the permissions and segments in one of my taxonomies?
  - id: POST_audience_segments-taxonomy_id
    intent: Update a permission taxonomy
    question: How do I add or remove segments in an existing taxonomy?
  phrasing_ops: 5
  slug: mediamath-permission-taxonomies-api
- baseURL: https://api.mediamath.com/deals/v1.0
  baseurl_source: declared
  description: Private Marketplace Direct (PMP-E)
  name: MediaMath Private Marketplace Exchange (PMP-E) API
  phrasing_intents:
  - id: LIST-deals
    intent: List private marketplace deals
    question: Which PMP deals does my organization own in MediaMath?
  - id: POST-deal
    intent: Create a private marketplace deal
    question: How do I set up a new PMP deal with a supply source and floor price?
  - id: LIST-deals-and-reporting-data
    intent: List deals with their performance reporting
    question: How are my PMP deals performing over the last 7 days?
  - id: GET-deal
    intent: Get a single deal's details
    question: What are the settings and price on a specific deal?
  - id: PUT-deal
    intent: Update an existing deal
    question: How do I change the price on a deal I already created?
  - id: LIST-deal-groups
    intent: List deal groups
    question: Which deal groups has my organization packaged up?
  - id: POST-deal-group
    intent: Create a deal group
    question: How do I package several deals into one group for targeting?
  - id: GET-deal-group
    intent: Get a deal group's details
    question: What deals are inside a specific deal group?
  phrasing_ops: 21
  slug: mediamath-private-marketplace-exchange-pmp-e-api
- baseURL: https://api.mediamath.com/deals/v1.0
  baseurl_source: declared
  description: _
  name: MediaMath Reports API
  phrasing_intents:
  - id: GET_app_transparency
    intent: Query the app transparency report
    question: Which mobile apps did my MediaMath ads actually run in?
  - id: GET_app_transparency-meta
    intent: Describe the app transparency report fields
    question: What dimensions and metrics does the app transparency report support?
  - id: Generate-Brain-Feature-Summary-report
    intent: Get the Brain feature summary report
    question: How can I see which impression features the Brain weighs most when optimizing?
  - id: Generate-Brain-Feature-Value-report
    intent: Get the Brain feature value report
    question: Which specific sites, creatives or exchanges push the Brain's predictions up or down most?
  - id: GET_by_hour
    intent: Get hourly performance metrics
    question: Can I get campaign performance down to the hour instead of by day?
  - id: GET_by_hour-meta
    intent: Describe the by-hour report fields
    question: Which dimensions can I break the hourly performance report out by?
  - id: GET_day_part
    intent: Get performance by time of day and weekday
    question: Which times of day and days of the week perform best for my ads?
  - id: GET_day_part-meta
    intent: Describe the day part report fields
    question: What metrics are available in the day part report?
  phrasing_ops: 26
  slug: mediamath-reports-api
- baseURL: https://api.mediamath.com/deals/v1.0
  baseurl_source: declared
  description: V2.0 video creative endpoints (legacy)
  name: MediaMath Video Creative Management (V2) API
  phrasing_intents:
  - id: GET_video-v2-0-creatives-video_id-companions
    intent: List companion ads for a video creative
    question: Which companion banners are attached to my video creative?
  - id: POST_video-v2-0-creatives-video_id-companions
    intent: Add a companion ad to a video creative
    question: How do I attach a companion banner to a video creative?
  - id: POST_video-v2-0-creatives-video_id-upload
    intent: Upload the media file for a video creative
    question: How do I upload the actual video file for a creative on v2?
  - id: GET_video-v2-0-creatives-video_id-variants
    intent: List encoded variants of a video creative
    question: What encoded versions were produced for my video creative?
  - id: GET_video-v2-0-creatives-video_id-variants-variant_id
    intent: Get one encoded variant of a video
    question: How do I look up a single encoded variant of a video creative?
  - id: GET_video-v2-0-creatives-video_id-status
    intent: Check a video creative's upload and encoding status
    question: Has my video creative finished encoding yet?
  - id: GET_video-v2-0-creatives-video_id-companions-companion_id-delete
    intent: Delete a companion ad from a video creative
    question: How do I remove a companion banner from a video creative?
  - id: POST_video-v2-0-creatives-validateVAST
    intent: Validate VAST XML
    question: How can I check my VAST XML for errors before trafficking it?
  phrasing_ops: 10
  slug: mediamath-video-creative-management-v2-api
- baseURL: https://api.mediamath.com/deals/v1.0
  baseurl_source: declared
  description: V3.0 video creative management endpoints
  name: MediaMath Video Creative Management (V3) API
  phrasing_intents:
  - id: PUT_v3-0-creatives-bulk
    intent: Bulk create video creatives
    question: Can I upload a whole set of new video creatives in one request?
  - id: PATCH_v3-0-creatives-bulk
    intent: Bulk update video creatives
    question: Is there a way to edit many existing video creatives at once?
  - id: POST_v3-0-creatives
    intent: Create a video creative
    question: How do I create a new video creative and upload its video file?
  - id: POST_v3-0-creatives-list
    intent: Get several video creatives by ID
    question: Can I fetch multiple video creatives at once if I have their IDs?
  - id: GET_v3-0-creatives-creativeId
    intent: Get a video creative's status and details
    question: What is the status of a single video creative?
  - id: POST_v3-0-creatives-creativeId
    intent: Replace a video creative (full update)
    question: If I resend a video creative without some fields, are they removed?
  - id: PATCH_v3-0-creatives-creativeId
    intent: Partially update a video creative
    question: Can I change just the clickthrough URL on a video creative without resending everything?
  - id: POST_v3-0-creatives-validateVAST
    intent: Validate VAST XML
    question: Is my VAST XML valid before I attach it to a creative?
  phrasing_ops: 15
  slug: mediamath-video-creative-management-v3-api
- baseURL: https://api.mediamath.com/api/v3.0
  baseurl_source: declared
  description: Place Lists
  name: MediaMath Place Lists API
  slug: mediamath-place-lists-api
artifact_total: 439
asyncapis:
- description: ''
  name: Mediamath Webhooks
  slug: mediamath-webhooks
collections:
- collection_type: open
  name: Campaigns Ad Servers API
  slug: open-mediamath-ad-servers-api
- collection_type: open
  name: Campaigns Ad Servers Advertisers API
  slug: open-mediamath-advertisers-api
- collection_type: open
  name: Campaigns Ad Servers Agencies API
  slug: open-mediamath-agencies-api
- collection_type: open
  name: Campaigns Ad Servers Atomic Creatives API
  slug: open-mediamath-atomic-creatives-api
- collection_type: open
  name: Campaigns Ad Servers Audience Vendors API
  slug: open-mediamath-audience-vendors-api
- collection_type: open
  name: Campaigns Ad Servers Campaign Plans API
  slug: open-mediamath-campaign-plans-api
- collection_type: open
  name: Ad Servers Campaigns API
  slug: open-mediamath-campaigns-api
- collection_type: open
  name: Campaigns Ad Servers Campaigns Budget Flights API
  slug: open-mediamath-campaigns-budget-flights-api
- collection_type: open
  name: Campaigns Ad Servers Concepts API
  slug: open-mediamath-concepts-api
- collection_type: open
  name: Campaigns Ad Servers Contracts API
  slug: open-mediamath-contracts-api
- collection_type: open
  name: Campaigns Ad Servers Creatives API
  slug: open-mediamath-creatives-api
- collection_type: open
  name: Campaigns Ad Servers Currency Rates API
  slug: open-mediamath-currency-rates-api
- collection_type: open
  name: Campaigns Ad Servers Datasets API
  slug: open-mediamath-datasets-api
- collection_type: open
  name: Campaigns Ad Servers Enterprise Controls API
  slug: open-mediamath-enterprise-controls-api
- collection_type: open
  name: Campaigns Ad Servers General API
  slug: open-mediamath-general-api
- collection_type: open
  name: Campaigns Ad Servers Marketplaces API
  slug: open-mediamath-marketplaces-api
- collection_type: open
  name: Campaigns Ad Servers New Strategy Groups API
  slug: open-mediamath-new-strategy-groups-api
- collection_type: open
  name: Campaigns Ad Servers New Strategy Plans API
  slug: open-mediamath-new-strategy-plans-api
- collection_type: open
  name: Campaigns Ad Servers Organizations API
  slug: open-mediamath-organizations-api
- collection_type: open
  name: Campaigns Ad Servers Pixel Bundles API
  slug: open-mediamath-pixel-bundles-api
- collection_type: open
  name: Campaigns Ad Servers Pixel Providers API
  slug: open-mediamath-pixel-providers-api
- collection_type: open
  name: Campaigns Ad Servers Segment Groups API
  slug: open-mediamath-segment-groups-api
- collection_type: open
  name: Campaigns Ad Servers Site Lists API
  slug: open-mediamath-site-lists-api
- collection_type: open
  name: Campaigns Ad Servers Strategies API
  slug: open-mediamath-strategies-api
- collection_type: open
  name: Campaigns Ad Servers Strategy Parameters API
  slug: open-mediamath-strategy-parameters-api
- collection_type: open
  name: Campaigns Ad Servers Strategy Templates API
  slug: open-mediamath-strategy-templates-api
- collection_type: open
  name: Campaigns Ad Servers Supply Sources API
  slug: open-mediamath-supply-sources-api
- collection_type: open
  name: Campaigns Ad Servers Targeting API
  slug: open-mediamath-targeting-api
- collection_type: open
  name: Campaigns Ad Servers Targeting Attachments API
  slug: open-mediamath-targeting-attachments-api
- collection_type: open
  name: Campaigns Ad Servers Targeting Segment Objectives API
  slug: open-mediamath-targeting-segment-objectives-api
- collection_type: open
  name: Campaigns Ad Servers Targeting Segments API
  slug: open-mediamath-targeting-segments-api
- collection_type: open
  name: Campaigns Ad Servers Timezones API
  slug: open-mediamath-timezones-api
- collection_type: open
  name: Campaigns Ad Servers User Permissions API
  slug: open-mediamath-user-permissions-api
- collection_type: open
  name: Campaigns Ad Servers Users API
  slug: open-mediamath-users-api
- collection_type: open
  name: Campaigns Ad Servers Vendor Contracts API
  slug: open-mediamath-vendor-contracts-api
- collection_type: open
  name: Campaigns Ad Servers Vendors API
  slug: open-mediamath-vendors-api
- collection_type: open
  name: Campaigns Ad Servers Verticals API
  slug: open-mediamath-verticals-api
common:
- group: company
  title: ''
  type: Website
  url: https://mediamath.com
- group: other
  href: https://artifacts.apis.io/mediamath/capabilities/mediamath-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mediamath-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/mediamath/agentic-access/mediamath-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mediamath-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/mediamath/security/mediamath-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mediamath-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/mediamath/authentication/mediamath-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mediamath-authentication.yml
- group: auth
  href: https://artifacts.apis.io/mediamath/scopes/mediamath-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/mediamath-scopes.yml
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/mediamath/refs/heads/main/plans/mediamath-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/mediamath/refs/heads/main/rate-limits/mediamath-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/mediamath/refs/heads/main/finops/mediamath-finops.yml
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.mediamath.com/
- group: auth
  title: ''
  type: Authentication
  url: https://apidocs.mediamath.com/guides
- group: company
  title: ''
  type: Blog
  url: https://infillion.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.infillion.com/s/submit-a-case
- group: start
  title: ''
  type: Login
  url: https://platform.mediamath.com/
- group: learn
  title: ''
  type: Academy
  url: https://academy.mediamath.com/
- group: build
  href: https://artifacts.apis.io/mediamath/packages/mediamath-packages.yml
  title: ''
  type: Packages
  url: packages/mediamath-packages.yml
- group: build
  href: https://artifacts.apis.io/mediamath/packages/mediamath-packages.yml
  title: ''
  type: SDKs
  url: packages/mediamath-packages.yml
- group: agent
  href: https://artifacts.apis.io/mediamath/well-known/mediamath-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mediamath-well-known.yml
- group: agent
  href: https://artifacts.apis.io/mediamath/mcp/mediamath-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mediamath-mcp.yml
- group: build
  href: https://artifacts.apis.io/mediamath/mcp/mediamath-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/mediamath-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/mediamath/llms/mediamath-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mediamath-llms.txt
- group: other
  href: https://artifacts.apis.io/mediamath/grpc/mediamath-winnotice.proto
  title: ''
  type: Protobuf
  url: grpc/mediamath-winnotice.proto
- group: design
  href: https://artifacts.apis.io/mediamath/conformance/mediamath-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mediamath-conformance.yml
- group: design
  href: https://artifacts.apis.io/mediamath/errors/mediamath-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mediamath-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mediamath/lifecycle/mediamath-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mediamath-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/mediamath/lifecycle/mediamath-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/mediamath-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/mediamath/conventions/mediamath-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mediamath-conventions.yml
- group: design
  href: https://artifacts.apis.io/mediamath/data-model/mediamath-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mediamath-data-model.yml
- group: design
  href: https://artifacts.apis.io/mediamath/asyncapi/mediamath-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/mediamath-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/mediamath/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/mediamath/security/mediamath-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mediamath-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mediamath/security/mediamath-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/mediamath-vulnerability-disclosure.yml
- group: build
  href: https://artifacts.apis.io/mediamath/examples/
  title: ''
  type: Examples
  url: examples/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.mediamath.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.mediamath.com/apis/campaigns-api/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.mediamath.com/guides
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MediaMath
- group: build
  title: ''
  type: Postman
  url: https://apidocs.mediamath.com/guides/postman-collections
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apidocs.mediamath.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://infillion.com/privacy-policy/
- group: other
  href: https://artifacts.apis.io/mediamath/overlays/mediamath-audience-segments-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mediamath-audience-segments-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/mediamath/overlays/mediamath-bof-config-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mediamath-bof-config-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/mediamath/overlays/mediamath-byoa-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mediamath-byoa-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/mediamath/overlays/mediamath-campaigns-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mediamath-campaigns-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/mediamath/overlays/mediamath-component-creatives-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mediamath-component-creatives-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/mediamath/overlays/mediamath-marketplaces-api-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mediamath-marketplaces-api-v2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/mediamath/overlays/mediamath-reporting-api-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mediamath-reporting-api-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/mediamath/overlays/mediamath-video-creatives-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mediamath-video-creatives-api-overlay.yaml
created: '2026-06-13'
description: MediaMath (by Infillion) is a programmatic advertising DSP with REST APIs for managing campaigns, targeting, bidding strategies, creative trafficking, audience segments, and performance analytics. The platform provides an API-first composable architecture supporting campaign management, reporting, audience onboarding, marketplaces access, and custom bidding algorithms.
examples:
- key_count: 6
  name: Reporting Post All Dimensions And Metrics Request
  slug: reporting-post-all-dimensions-and-metrics-request
- key_count: 2
  name: Reporting Post All Dimensions And Metrics Response 200
  slug: reporting-post-all-dimensions-and-metrics-response-200
- key_count: 6
  name: Reporting Post Brain Feature Summary Request
  slug: reporting-post-brain-feature-summary-request
- key_count: 2
  name: Reporting Post Brain Feature Summary Response 200
  slug: reporting-post-brain-feature-summary-response-200
- key_count: 6
  name: Reporting Post Brain Feature Value Request
  slug: reporting-post-brain-feature-value-request
- key_count: 2
  name: Reporting Post Brain Feature Value Response 200
  slug: reporting-post-brain-feature-value-response-200
- key_count: 6
  name: Reporting Post Day Part Request
  slug: reporting-post-day-part-request
- key_count: 2
  name: Reporting Post Day Part Response 200
  slug: reporting-post-day-part-response-200
- key_count: 6
  name: Reporting Post Deals Request
  slug: reporting-post-deals-request
- key_count: 2
  name: Reporting Post Deals Response 200
  slug: reporting-post-deals-response-200
- key_count: 6
  name: Reporting Post Performance Hourly Request
  slug: reporting-post-performance-hourly-request
- key_count: 2
  name: Reporting Post Performance Hourly Response 200
  slug: reporting-post-performance-hourly-response-200
- key_count: 6
  name: Reporting Post Performance Request
  slug: reporting-post-performance-request
- key_count: 2
  name: Reporting Post Performance Response 200
  slug: reporting-post-performance-response-200
- key_count: 6
  name: Reporting Post Pixel Loads Request
  slug: reporting-post-pixel-loads-request
- key_count: 2
  name: Reporting Post Pixel Loads Response 200
  slug: reporting-post-pixel-loads-response-200
- key_count: 6
  name: Reporting Post Reach Frequency Request
  slug: reporting-post-reach-frequency-request
- key_count: 2
  name: Reporting Post Reach Frequency Response 200
  slug: reporting-post-reach-frequency-response-200
- key_count: 6
  name: Reporting Post Win Loss Request
  slug: reporting-post-win-loss-request
- key_count: 2
  name: Reporting Post Win Loss Response 200
  slug: reporting-post-win-loss-response-200
finops:
- has_sources: true
  method: derived
  name: Mediamath Finops
  primary_unit: ''
  service_category: ''
  slug: mediamath-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mediamath.png
json_schemas:
- name: ad_server_collection
  property_count: 2
  slug: campaigns-ad_server_collection
- name: ad_server_collection_full
  property_count: 2
  slug: campaigns-ad_server_collection_full
- name: ad_server_full
  property_count: 3
  slug: campaigns-ad_server_full
- name: advertiser
  property_count: 20
  slug: campaigns-advertiser_base
- name: advertiser_collection
  property_count: 2
  slug: campaigns-advertiser_collection
- name: advertiser_collection_full
  property_count: 2
  slug: campaigns-advertiser_collection_full
- name: advertiser_create
  property_count: 1
  slug: campaigns-advertiser_create
- name: advertiser_response
  property_count: 2
  slug: campaigns-advertiser_response
- name: advertiser_response_base
  property_count: 12
  slug: campaigns-advertiser_response_base
- name: advertiser_response_extended
  property_count: 2
  slug: campaigns-advertiser_response_extended
- name: advertiser_update
  property_count: 1
  slug: campaigns-advertiser_update
- name: agency
  property_count: 9
  slug: campaigns-agency_base
- name: agency_collection
  property_count: 2
  slug: campaigns-agency_collection
- name: agency_collection_full
  property_count: 2
  slug: campaigns-agency_collection_full
- name: agency_create
  property_count: 1
  slug: campaigns-agency_create
- name: agency_response
  property_count: 2
  slug: campaigns-agency_response
- name: agency_response_base
  property_count: 9
  slug: campaigns-agency_response_base
- name: agency_response_extended
  property_count: 2
  slug: campaigns-agency_response_extended
- name: agency_update
  property_count: 1
  slug: campaigns-agency_update
- name: atomic_creative_create
  property_count: 40
  slug: campaigns-atomic_creative_create
- name: atomic_creative_healthcheck_response
  property_count: 14
  slug: campaigns-atomic_creative_healthcheck_response
- name: atomic_creative_response
  property_count: 50
  slug: campaigns-atomic_creative_response
- name: atomic_creative_response_extended
  property_count: 56
  slug: campaigns-atomic_creative_response_extended
- name: atomic_creative_update
  property_count: 28
  slug: campaigns-atomic_creative_update
- name: atomic_creative_vendor
  property_count: 1
  slug: campaigns-atomic_creative_vendor
- name: attachment_base
  property_count: 10
  slug: campaigns-attachment_base
- name: attachment_create
  property_count: 5
  slug: campaigns-attachment_create
- name: attachment_update
  property_count: 6
  slug: campaigns-attachment_update
- name: audience_segment_short
  property_count: 7
  slug: campaigns-audience_segment_short
- name: audience_segments_group
  property_count: 2
  slug: campaigns-audience_segments_group
- name: audience_target
  property_count: 2
  slug: campaigns-audience_target
- name: audience_vendor
  property_count: 12
  slug: campaigns-audience_vendor
- name: budget_flight_collection
  property_count: 2
  slug: campaigns-budget_flight_collection
- name: budget_flight_collection_full
  property_count: 2
  slug: campaigns-budget_flight_collection_full
- name: budget_flight_full
  property_count: 13
  slug: campaigns-budget_flight_full
- name: bulk errors
  property_count: 0
  slug: campaigns-bulk_errors
- name: campaign_ad_server
  property_count: 5
  slug: campaigns-campaign_ad_server
- name: campaign_attribution
  property_count: 8
  slug: campaigns-campaign_attribution
- name: campaign_base
  property_count: 18
  slug: campaigns-campaign_base
- name: campaign_budget
  property_count: 7
  slug: campaigns-campaign_budget
- name: campaign_budget_flights
  property_count: 6
  slug: campaigns-campaign_budget_flights
- name: campaign_budget_flights_create
  property_count: 4
  slug: campaigns-campaign_budget_flights_create
- name: campaign_bulk
  property_count: 7
  slug: campaigns-campaign_bulk
- name: campaign_collection
  property_count: 2
  slug: campaigns-campaign_collection
- name: campaign_collection_full
  property_count: 2
  slug: campaigns-campaign_collection_full
- name: campaign_create
  property_count: 7
  slug: campaigns-campaign_create
- name: campaign_custom_brain_selection
  property_count: 16
  slug: campaigns-campaign_custom_brain_selection
- name: campaign_dba_collection
  property_count: 2
  slug: campaigns-campaign_dba_collection
- name: campaign_dba_collection_full
  property_count: 2
  slug: campaigns-campaign_dba_collection_full
- name: campaign_duration
  property_count: 2
  slug: campaigns-campaign_duration
- name: campaign_frequency
  property_count: 5
  slug: campaigns-campaign_frequency
- name: campaign_response
  property_count: 2
  slug: campaigns-campaign_full-2
- name: campaign_full
  property_count: 16
  slug: campaigns-campaign_full
- name: campaign_response_extended
  property_count: 2
  slug: campaigns-campaign_full_extended-2
- name: campaign_full_extended
  property_count: 3
  slug: campaigns-campaign_full_extended
- name: campaign_full_with_inherited
  property_count: 3
  slug: campaigns-campaign_full_with_inherited
- name: campaign_goals
  property_count: 4
  slug: campaigns-campaign_goals
- name: campaign_goals_create
  property_count: 0
  slug: campaigns-campaign_goals_create
- name: campaign_identity
  property_count: 3
  slug: campaigns-campaign_identity
- name: campaign_inventory
  property_count: 7
  slug: campaigns-campaign_inventory
- name: campaign_pacing
  property_count: 10
  slug: campaigns-campaign_pacing
- name: campaign_plan
  property_count: 0
  slug: campaigns-campaign_plan
- name: campaign_plan_common
  property_count: 5
  slug: campaigns-campaign_plan_common
- name: campaign_plan_create
  property_count: 4
  slug: campaigns-campaign_plan_create
- name: campaign_plan_update
  property_count: 1
  slug: campaigns-campaign_plan_update
- name: campaign_site_list
  property_count: 15
  slug: campaigns-campaign_site_list
- name: campaign_update
  property_count: 7
  slug: campaigns-campaign_update
- name: campaign_viewability
  property_count: 3
  slug: campaigns-campaign_viewability
- name: campaign_with
  property_count: 2
  slug: campaigns-campaign_with
- name: concept_common
  property_count: 3
  slug: campaigns-concept_common
- name: concept_create
  property_count: 1
  slug: campaigns-concept_create
- name: concept_full
  property_count: 8
  slug: campaigns-concept_response
- name: concept_update
  property_count: 1
  slug: campaigns-concept_update
- name: concept
  property_count: 3
  slug: campaigns-concepts_collection_short
- name: contextual_segment_collection
  property_count: 2
  slug: campaigns-contextual_segment_collection
- name: contextual_segment_collection_full
  property_count: 2
  slug: campaigns-contextual_segment_collection_full
- name: contextual_segment_full
  property_count: 12
  slug: campaigns-contextual_segment_full
- name: contextual_segment_short
  property_count: 7
  slug: campaigns-contextual_segment_short
- name: contract_base
  property_count: 81
  slug: campaigns-contract_base
- name: contract_base_response
  property_count: 2
  slug: campaigns-contract_base_response
- name: contract_collection
  property_count: 2
  slug: campaigns-contract_collection
- name: contract_collection_full
  property_count: 2
  slug: campaigns-contract_collection_full
- name: control_boolean
  property_count: 2
  slug: campaigns-control_boolean
- name: control_decimal
  property_count: 2
  slug: campaigns-control_decimal
- name: control_decimal_array
  property_count: 2
  slug: campaigns-control_decimal_array
- name: control_integer
  property_count: 2
  slug: campaigns-control_integer
- name: control_integer_array
  property_count: 2
  slug: campaigns-control_integer_array
- name: control_string
  property_count: 2
  slug: campaigns-control_string
- name: control_string_array
  property_count: 2
  slug: campaigns-control_string_array
- name: cpm
  property_count: 2
  slug: campaigns-cpm
- name: creative
  property_count: 4
  slug: campaigns-creative_base
- name: creative_response
  property_count: 2
  slug: campaigns-creative_response
- name: currency_rate_collection
  property_count: 2
  slug: campaigns-currency_rate_collection
- name: currency_rate_collection_full
  property_count: 2
  slug: campaigns-currency_rate_collection_full
- name: currency_rate_full
  property_count: 7
  slug: campaigns-currency_rate_full
- name: day_part
  property_count: 4
  slug: campaigns-day_part
- name: dba
  property_count: 0
  slug: campaigns-dba
- name: ''
  property_count: 1
  slug: campaigns-deal
- name: ''
  property_count: 1
  slug: campaigns-deal_group
- name: domain_restriction
  property_count: 2
  slug: campaigns-domain_restriction
- name: duration_base
  property_count: 2
  slug: campaigns-duration_base
- name: enterprise_control
  property_count: 2
  slug: campaigns-enterprise_control
- name: entity_group
  property_count: 8
  slug: campaigns-entity_group
- name: entity_group_advertiser
  property_count: 2
  slug: campaigns-entity_group_advertiser
- name: entity_group_agency
  property_count: 1
  slug: campaigns-entity_group_agency
- name: entity_group_entity
  property_count: 2
  slug: campaigns-entity_group_entity
- name: entity_group_list_item
  property_count: 7
  slug: campaigns-entity_group_list_item
- name: error response
  property_count: 2
  slug: campaigns-error_response
- name: exchange_seat
  property_count: 7
  slug: campaigns-exchange_seat
- name: exchange_seat_extended
  property_count: 1
  slug: campaigns-exchange_seat_extended
- name: forecast
  property_count: 2
  slug: campaigns-forecast
- name: forecast_request
  property_count: 2
  slug: campaigns-forecast_request
- name: frequency_base
  property_count: 3
  slug: campaigns-frequency_base
- name: healthcheck_result
  property_count: 2
  slug: campaigns-healthcheck_result
- name: inventory_base
  property_count: 0
  slug: campaigns-inventory_base
- name: pagination metadata
  property_count: 6
  slug: campaigns-list_metadata
- name: ''
  property_count: 13
  slug: campaigns-location_response
- name: marketplace_create
  property_count: 0
  slug: campaigns-marketplace_create
- name: marketplace_full
  property_count: 23
  slug: campaigns-marketplace_full
- name: marketplace_full_response
  property_count: 2
  slug: campaigns-marketplace_full_response
- name: marketplace_update
  property_count: 1
  slug: campaigns-marketplace_update
- name: new_strategy_group_base
  property_count: 7
  slug: campaigns-new_strategy_group_base
- name: new_strategy_group_collection
  property_count: 2
  slug: campaigns-new_strategy_group_collection
- name: new_strategy_group_collection_full
  property_count: 2
  slug: campaigns-new_strategy_group_collection_full
- name: new_strategy_group_create
  property_count: 1
  slug: campaigns-new_strategy_group_create
- name: new_strategy_group_full
  property_count: 7
  slug: campaigns-new_strategy_group_full
- name: new_strategy_group_list_item
  property_count: 6
  slug: campaigns-new_strategy_group_list_item
- name: new_strategy_group_response
  property_count: 2
  slug: campaigns-new_strategy_group_response
- name: new_strategy_group_strategy_embed
  property_count: 3
  slug: campaigns-new_strategy_group_strategy_embed
- name: new_strategy_group_update
  property_count: 1
  slug: campaigns-new_strategy_group_update
- name: new_strategy_plan_collection_full
  property_count: 2
  slug: campaigns-new_strategy_plan_collection_full
- name: new_strategy_plan_collection_full_extended
  property_count: 2
  slug: campaigns-new_strategy_plan_collection_full_extended
- name: new_strategy_plan_full
  property_count: 10
  slug: campaigns-new_strategy_plan_full
- name: new_strategy_plan_full_extended
  property_count: 10
  slug: campaigns-new_strategy_plan_full_extended
- name: new_strategy_plan_full_response
  property_count: 3
  slug: campaigns-new_strategy_plan_full_response
- name: new_strategy_plan_full_response_extended
  property_count: 3
  slug: campaigns-new_strategy_plan_full_response_extended
- name: new_strategy_plan_response
  property_count: 2
  slug: campaigns-new_strategy_plan_response
- name: new_strategy_plan_response_extended
  property_count: 2
  slug: campaigns-new_strategy_plan_response_extended
- name: organization_base
  property_count: 40
  slug: campaigns-organization_base
- name: organization_collection
  property_count: 2
  slug: campaigns-organization_collection
- name: organization_create
  property_count: 0
  slug: campaigns-organization_create
- name: organization_response
  property_count: 2
  slug: campaigns-organization_response
- name: organization_update
  property_count: 2
  slug: campaigns-organization_update
- name: path_audience_segment
  property_count: 17
  slug: campaigns-path_audience_segment
- name: path_audience_segments_full
  property_count: 2
  slug: campaigns-path_audience_segments_collection_full
- name: permission
  property_count: 6
  slug: campaigns-permission
- name: permission_advertiser
  property_count: 1
  slug: campaigns-permission_advertiser
- name: permission_agency
  property_count: 1
  slug: campaigns-permission_agency
- name: permission_campaign
  property_count: 1
  slug: campaigns-permission_campaign
- name: permission_campaign_with_user
  property_count: 1
  slug: campaigns-permission_campaign_with_user
- name: permission_flags
  property_count: 5
  slug: campaigns-permission_flags
- name: permission_list
  property_count: 5
  slug: campaigns-permission_list
- name: permission_organization
  property_count: 1
  slug: campaigns-permission_organization
- name: permission_strategy
  property_count: 1
  slug: campaigns-permission_strategy
- name: permission_strategy_with_user
  property_count: 1
  slug: campaigns-permission_strategy_with_user
- name: permission_user_output
  property_count: 35
  slug: campaigns-permission_user_output
- name: permission_v2_advertiser
  property_count: 5
  slug: campaigns-permission_v2_advertiser
- name: permission_v2_agency
  property_count: 5
  slug: campaigns-permission_v2_agency
- name: permission_v2_flags
  property_count: 12
  slug: campaigns-permission_v2_flags
- name: permission_v2_object
  property_count: 2
  slug: campaigns-permission_v2_object
- name: permission_v2_organization
  property_count: 4
  slug: campaigns-permission_v2_organization
- name: pixel_bundle_base
  property_count: 24
  slug: campaigns-pixel_bundle_base
- name: pixel_bundle_collection
  property_count: 2
  slug: campaigns-pixel_bundle_collection
- name: pixel_bundle_collection_full
  property_count: 2
  slug: campaigns-pixel_bundle_collection_full
- name: pixel_bundle_create
  property_count: 3
  slug: campaigns-pixel_bundle_create
- name: pixel_bundle
  property_count: 1
  slug: campaigns-pixel_bundle_response
- name: pixel_providers_response
  property_count: 2
  slug: campaigns-pixel_providers_response
- name: pixel_providers_full_response
  property_count: 2
  slug: campaigns-pixel_providers_response_full
- name: roles
  property_count: 0
  slug: campaigns-roles
- name: search_result
  property_count: 3
  slug: campaigns-search_result
- name: segment_group_create
  property_count: 5
  slug: campaigns-segment_group_create
- name: segment_group_update
  property_count: 5
  slug: campaigns-segment_group_update
- name: settings_organization
  property_count: 2
  slug: campaigns-settings_organization
- name: settings_organization_update
  property_count: 1
  slug: campaigns-settings_organization_update
- name: sidekick_usage_log_base
  property_count: 26
  slug: campaigns-sidekick_usage_log_base
- name: sidekick_usage_log_create
  property_count: 22
  slug: campaigns-sidekick_usage_log_create
- name: single_metadata
  property_count: 1
  slug: campaigns-single_metadata
- name: site_list
  property_count: 2
  slug: campaigns-site_list
- name: site_list_assignment_collection
  property_count: 2
  slug: campaigns-site_list_assignment_collection
- name: site_list_assignment_collection_full
  property_count: 2
  slug: campaigns-site_list_assignment_collection_full
- name: site_list_assignment_full
  property_count: 6
  slug: campaigns-site_list_assignment_full
- name: site_list_collection
  property_count: 2
  slug: campaigns-site_list_collection
- name: site_list_collection_full
  property_count: 2
  slug: campaigns-site_list_collection_full
- name: site_list_extended
  property_count: 10
  slug: campaigns-site_list_extended
- name: site_list_full
  property_count: 14
  slug: campaigns-site_list_full
- name: strategy_response
  property_count: 2
  slug: campaigns-strategy
- name: strategy_audience_segment
  property_count: 2
  slug: campaigns-strategy_audience_segment
- name: ''
  property_count: 10
  slug: campaigns-strategy_audience_segment_extended
- name: strategy_base
  property_count: 6
  slug: campaigns-strategy_base
- name: strategy_budget
  property_count: 3
  slug: campaigns-strategy_budget
- name: strategy_campaign_info
  property_count: 9
  slug: campaigns-strategy_campaign_info
- name: strategy_collection
  property_count: 2
  slug: campaigns-strategy_collection
- name: strategy_collection_full
  property_count: 2
  slug: campaigns-strategy_collection_full
- name: strategy_collection_full_extended
  property_count: 2
  slug: campaigns-strategy_collection_full_extended
- name: strategy_concept_collection
  property_count: 2
  slug: campaigns-strategy_concept_collection
- name: strategy_concept_collection_full
  property_count: 2
  slug: campaigns-strategy_concept_collection_full
- name: strategy_concept_full
  property_count: 9
  slug: campaigns-strategy_concept_full
- name: strategy_concepts
  property_count: 2
  slug: campaigns-strategy_concepts
- name: strategy_concepts_extended
  property_count: 2
  slug: campaigns-strategy_concepts_extended
- name: strategy_contextual_segment
  property_count: 2
  slug: campaigns-strategy_contextual_segment
- name: ''
  property_count: 11
  slug: campaigns-strategy_contextual_segment_extended
- name: strategy_create_request
  property_count: 0
  slug: campaigns-strategy_create_request
- name: strategy_day_part_collection
  property_count: 2
  slug: campaigns-strategy_day_part_collection
- name: strategy_day_part_collection_full
  property_count: 2
  slug: campaigns-strategy_day_part_collection_full
- name: strategy_day_part_full
  property_count: 10
  slug: campaigns-strategy_day_part_full
- name: strategy_deal_collection
  property_count: 2
  slug: campaigns-strategy_deal_collection
- name: strategy_deal_collection_full
  property_count: 2
  slug: campaigns-strategy_deal_collection_full
- name: strategy_deal_full
  property_count: 4
  slug: campaigns-strategy_deal_full
- name: strategy_details
  property_count: 15
  slug: campaigns-strategy_details
- name: strategy_duration
  property_count: 4
  slug: campaigns-strategy_duration
- name: strategy_extended_response
  property_count: 2
  slug: campaigns-strategy_extended
- name: strategy_forecast_query
  property_count: 5
  slug: campaigns-strategy_forecast_query
- name: strategy_frequency
  property_count: 4
  slug: campaigns-strategy_frequency
- name: strategy_full
  property_count: 4
  slug: campaigns-strategy_full
- name: strategy_full_extended
  property_count: 12
  slug: campaigns-strategy_full_extended
- name: strategy_full_response
  property_count: 3
  slug: campaigns-strategy_full_response
- name: ''
  property_count: 2
  slug: campaigns-strategy_geofence
- name: ''
  property_count: 2
  slug: campaigns-strategy_geofence_extended
- name: strategy_goals
  property_count: 11
  slug: campaigns-strategy_goals
- name: strategy_group_collection
  property_count: 2
  slug: campaigns-strategy_group_collection
- name: strategy_group_collection_full
  property_count: 2
  slug: campaigns-strategy_group_collection_full
- name: strategy_group_collection_full_extended
  property_count: 2
  slug: campaigns-strategy_group_collection_full_extended
- name: strategy_group_full
  property_count: 1
  slug: campaigns-strategy_group_full
- name: strategy_group_full_extended
  property_count: 3
  slug: campaigns-strategy_group_full_extended
- name: strategy_healthcheck
  property_count: 8
  slug: campaigns-strategy_healthcheck
- name: strategy_inventory
  property_count: 10
  slug: campaigns-strategy_inventory
- name: strategy_inventory_extended
  property_count: 9
  slug: campaigns-strategy_inventory_extended
- name: strategy_ip_address_collection
  property_count: 2
  slug: campaigns-strategy_ip_address_collection
- name: strategy_ip_address_collection_full
  property_count: 2
  slug: campaigns-strategy_ip_address_collection_full
- name: strategy_ip_address_full
  property_count: 6
  slug: campaigns-strategy_ip_address_full
- name: ''
  property_count: 3
  slug: campaigns-strategy_location
- name: ''
  property_count: 6
  slug: campaigns-strategy_location_extended
- name: ''
  property_count: 2
  slug: campaigns-strategy_my_data
- name: ''
  property_count: 2
  slug: campaigns-strategy_my_data_extended
- name: strategy_pacing
  property_count: 10
  slug: campaigns-strategy_pacing
- name: strategy_plan_budget
  property_count: 2
  slug: campaigns-strategy_plan_budget
- name: strategy_plan_creatives
  property_count: 3
  slug: campaigns-strategy_plan_creatives
- name: strategy_plan_details
  property_count: 3
  slug: campaigns-strategy_plan_details
- name: strategy_plan_duration
  property_count: 4
  slug: campaigns-strategy_plan_duration
- name: strategy_plan_frequency
  property_count: 4
  slug: campaigns-strategy_plan_frequency
- name: strategy_plan_goals
  property_count: 10
  slug: campaigns-strategy_plan_goals
- name: strategy_plan_inventory
  property_count: 8
  slug: campaigns-strategy_plan_inventory
- name: strategy_plan_target_full
  property_count: 6
  slug: campaigns-strategy_plan_target_full
- name: strategy_plan_target_value_collection
  property_count: 2
  slug: campaigns-strategy_plan_target_value_collection
- name: strategy_plan_target_value_collection_full
  property_count: 2
  slug: campaigns-strategy_plan_target_value_collection_full
- name: strategy_plan_target_value_full
  property_count: 3
  slug: campaigns-strategy_plan_target_value_full
- name: strategy_plan_targeting
  property_count: 12
  slug: campaigns-strategy_plan_targeting
- name: strategy_plan_targeting_extended
  property_count: 12
  slug: campaigns-strategy_plan_targeting_extended
- name: strategy_postal_code_collection
  property_count: 2
  slug: campaigns-strategy_postal_code_collection
- name: strategy_postal_code_collection_full
  property_count: 2
  slug: campaigns-strategy_postal_code_collection_full
- name: strategy_postal_code_full
  property_count: 6
  slug: campaigns-strategy_postal_code_full
- name: strategy_segment_group
  property_count: 2
  slug: campaigns-strategy_segment_group
- name: strategy_segment_group_exclude
  property_count: 1
  slug: campaigns-strategy_segment_group_exclude
- name: strategy_segment_group_exclude_extended
  property_count: 1
  slug: campaigns-strategy_segment_group_exclude_extended
- name: strategy_segment_group_extended
  property_count: 2
  slug: campaigns-strategy_segment_group_extended
- name: strategy_target_full
  property_count: 6
  slug: campaigns-strategy_target_full
- name: strategy_target_value_collection
  property_count: 2
  slug: campaigns-strategy_target_value_collection
- name: strategy_target_value_collection_full
  property_count: 2
  slug: campaigns-strategy_target_value_collection_full
- name: strategy_target_value_full
  property_count: 3
  slug: campaigns-strategy_target_value_full
- name: strategy_targeting
  property_count: 10
  slug: campaigns-strategy_targeting
- name: strategy_targeting_expression
  property_count: 1
  slug: campaigns-strategy_targeting_expression
- name: strategy_targeting_extended
  property_count: 14
  slug: campaigns-strategy_targeting_extended
- name: strategy_targeting_request
  property_count: 1
  slug: campaigns-strategy_targeting_request
- name: strategy_targeting_request_for_bulk
  property_count: 1
  slug: campaigns-strategy_targeting_request_for_bulk
- name: ''
  property_count: 3
  slug: campaigns-strategy_technology
- name: ''
  property_count: 4
  slug: campaigns-strategy_technology_extended
- name: strategy template response
  property_count: 10
  slug: campaigns-strategy_template_response
- name: ''
  property_count: 1
  slug: campaigns-supply_source
- name: ''
  property_count: 3
  slug: campaigns-supply_source_extended
- name: supply_source_response
  property_count: 33
  slug: campaigns-supply_source_response
- name: target_base
  property_count: 9
  slug: campaigns-target_base
- name: target_create
  property_count: 0
  slug: campaigns-target_create
- name: target_dimension_exclude
  property_count: 3
  slug: campaigns-target_dimension_exclude
- name: target_dimension_include
  property_count: 3
  slug: campaigns-target_dimension_include
- name: target_update
  property_count: 10
  slug: campaigns-target_update
- name: target_value_full
  property_count: 7
  slug: campaigns-target_value_full
- name: targeting_base
  property_count: 6
  slug: campaigns-targeting_base
- name: targeting_friendly_name
  property_count: 7
  slug: campaigns-targeting_friendly_name
- name: targeting_ip_addresses
  property_count: 2
  slug: campaigns-targeting_ip_addresses
- name: targeting_ip_addresses_response
  property_count: 2
  slug: campaigns-targeting_ip_addresses_response
- name: targeting_postal_codes
  property_count: 2
  slug: campaigns-targeting_postal_codes
- name: targeting_postal_codes_response
  property_count: 2
  slug: campaigns-targeting_postal_codes_response
- name: targeting_recency_element_request
  property_count: 3
  slug: campaigns-targeting_recency_element_request
- name: targeting_recency_element_response
  property_count: 3
  slug: campaigns-targeting_recency_element_response
- name: targeting_segment_collection
  property_count: 2
  slug: campaigns-targeting_segment_collection
- name: targeting_segment_collection_full
  property_count: 2
  slug: campaigns-targeting_segment_collection_full
- name: targeting_segment_full
  property_count: 16
  slug: campaigns-targeting_segment_full
- name: targeting_segment_objective_response
  property_count: 5
  slug: campaigns-targeting_segment_objective_response
- name: timezone_collection
  property_count: 2
  slug: campaigns-timezone_collection
- name: timezone_collection_full
  property_count: 2
  slug: campaigns-timezone_collection_full
- name: timezone_full
  property_count: 8
  slug: campaigns-timezone_full
- name: user
  property_count: 4
  slug: campaigns-user_base
- name: user_create
  property_count: 5
  slug: campaigns-user_create
- name: user permission
  property_count: 5
  slug: campaigns-user_permission
- name: user_permission_update
  property_count: 1
  slug: campaigns-user_permission_update
- name: user permissions
  property_count: 3
  slug: campaigns-user_permissions
- name: user_permissions_response
  property_count: 2
  slug: campaigns-user_permissions_response
- name: user_response
  property_count: 2
  slug: campaigns-user_response
- name: user_settings_response
  property_count: 3
  slug: campaigns-user_settings_response
- name: user_settings_update_request
  property_count: 1
  slug: campaigns-user_settings_update_request
- name: user_update
  property_count: 6
  slug: campaigns-user_update
- name: vendor
  property_count: 22
  slug: campaigns-vendor_base
- name: vendor_collection
  property_count: 2
  slug: campaigns-vendor_collection
- name: vendor_collection_full
  property_count: 2
  slug: campaigns-vendor_collection_full
- name: vendor_contract
  property_count: 4
  slug: campaigns-vendor_contract
- name: vendor_contract_base
  property_count: 4
  slug: campaigns-vendor_contract_base
- name: Error
  property_count: 3
  slug: reporting-Error
- name: Streaming Response
  property_count: 0
  slug: reporting-StreamingResponse
layout: provider
mcp_servers:
- description: Remote MCP server at apidocs.mediamath.com; 6 tools listed.
  name: MediaMath MCP Server
  slug: mediamath-mcp-yml
modified: '2026-09-16'
name: MediaMath
nav: Providers
network: true
overview: 'MediaMath publishes 59 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ad Servers API, Advertisers API, Agencies API, and 56 more. Tagged areas include Programmatic Advertising, DSP, Campaign Management, AdTech, and Bidding.


  The MediaMath catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  MediaMath''s developer surface includes authentication, documentation, engineering blog, support, academy / training, code examples, API reference, and 41 more developer resources.'
plans:
- name: Mediamath Plans
  plan_count: 2
  slug: mediamath-plans
random_paper: 2
rate_limits:
- limit_count: 7
  name: Mediamath Rate Limits
  slug: mediamath-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: MediaMath — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: mediamath-jsonschema-spectral-rules
scopes:
- name: Mediamath Scopes
  scope_count: 2
  slug: mediamath-scopes
  summary_line: 2 scopes · authorizationCode/password/clientCredentials
score:
  band: strong
  composite: 65.7
  coverage:
    artifact_dirs: 34
    catalog_earned: 63.3
    catalog_earned_first_party: 20.0
    catalog_gap: 51.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 48.7
    contract_governance: 14.4
    contract_quality: 64.5
    developer_ergonomics: 70.8
    discoverability: 80.0
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 65.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 97.1
      derived: 0
      marker_coverage: 0.0
      total: 102
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
screenshot: https://apis.io/screenshots/mediamath/mediamath-2026-06-20T185115.png
security:
- kind: authentication
  name: Mediamath Authentication
  slug: mediamath-authentication
  summary_line: apiKey/oauth2 · 6 schemes
- kind: domain-security
  name: Mediamath Domain Security
  slug: mediamath-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Mediamath Vulnerability Disclosure
  slug: mediamath-vulnerability-disclosure
  summary_line: no policy recorded
skill_count: 4
skills:
- name: mediamath-launch-campaign
  slug: mediamath-launch-campaign
- name: mediamath-manage-pmp-deals
  slug: mediamath-manage-pmp-deals
- name: mediamath-pull-performance-report
  slug: mediamath-pull-performance-report
- name: mediamath-traffic-creatives
  slug: mediamath-traffic-creatives
slug: mediamath
tags:
- Programmatic Advertising
- DSP
- Campaign Management
- AdTech
- Bidding
- Audience Segments
- Creative Management
- Reporting
- Analytics
website: https://mediamath.com
---
